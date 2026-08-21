---
name: honduras-payroll
description: Use this skill whenever asked about Honduras payroll processing for employed persons. Trigger on phrases like "Honduras payroll", "ISR Honduras", "Impuesto Sobre la Renta withholding", "IHSS deduction", "RAP contribution", "INFOP", "planilla Honduras", "aguinaldo", "decimo tercer mes", "decimo cuarto mes", "catorceavo", "tabla progresiva ISR", "net salary Honduras", "PAYE Honduras", "salario minimo Honduras", "techo de cotizacion IHSS", "employer payroll Honduras", "gross to net Honduras", "salario neto Honduras", or any question about computing employee pay, income-tax withholding, or social-security/private-fund contributions for Honduras-based employees. This skill covers ISR (income tax) withholding by the employer, IHSS social security (EM + IVM + occupational risk), RAP private contributions, the INFOP training levy, the 13th and 14th month statutory salaries, minimum wage, and filing obligations to SAR. ALWAYS read this skill before processing any Honduras payroll.
version: 0.1
jurisdiction: HN
tax_year: 2025
last_updated: 2026-07-13
review_status: pending_review
depends_on: - payroll-workflow-base
category: payroll
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Honduras Payroll

## Honduras Payroll Skill v0.1

> **Tier 2 (research-verified) — NOT yet accountant-verified.** Several figures carry `[RESEARCH GAP — reviewer to confirm]` markers. A licensed Honduran contador público must reconcile those before any output is presented as final.

## Section 1 -- Quick Reference

**Quick Reference**

| Field | Value |
| --- | --- |
| Country | Honduras (República de Honduras) |
| Currency | Lempira (HNL / L) only — wages must be paid in Lempiras (Labor Code) |
| Standard pay frequency | Manual workers: weekly max; office/intellectual + domestic: monthly max (Labor Code Art. 368) |
| Tax year | Calendar year (1 January -- 31 December) (PwC — Tax administration) |
| Income tax | YES — ISR (Impuesto Sobre la Renta), progressive 0% / 15% / 20% / 25%, employer-withheld monthly |
| Tax authority | SAR (Servicio de Administración de Rentas) |
| Social security authority | IHSS (Instituto Hondureño de Seguridad Social) |
| Private fund | RAP (Régimen de Aportaciones Privadas) |
| Training levy | INFOP (Instituto Nacional de Formación Profesional) |
| Annual ISR return form | Declaración Jurada del ISR – Persona Natural, código **102**, via SAR DET Live (SAR) |
| Annual ISR deadline | **30 April** (rolls to next business day) (SAR; PwC) |
| Key legislation | Ley del Impuesto Sobre la Renta; Código Tributario (Decreto 22-97); Ley del IHSS; Decreto 47-2024 (RAP reform); Código del Trabajo; Acuerdo 02-95 (Reglamento Décimo Cuarto Mes) |
| Filing portal | SAR DET Live (`detlive.sar.gob.hn`) |
| Validated by | Pending -- requires sign-off by a licensed Honduran contador público |
| Skill version | 0.1 |

## Section 2 -- Income Tax Withholding (ISR — Impuesto Sobre la Renta)

Honduras **does** levy personal income tax on employees. The employer is the **withholding agent (agente de retención)**: it deducts ISR monthly from payroll and remits it monthly to SAR (PwC — Tax administration). The progressive table (*tabla progresiva*) is updated annually by SAR for inflation and is expressed on **annual Renta Neta Gravable** (taxable net income). Rates: **0% / 15% / 20% / 25%**.

### ISR Progressive Table — Fiscal Year 2025 (CONFIRMED)

**ISR Progressive Table 2025**  _(Bloomberg Línea (full table); KPMG TaxNewsFlash Honduras Jan 2025; Galindo & Asociados; Auxadi)_

| Annual taxable income (L) | Approx. monthly (L) | Marginal rate | Tax on this bracket (cumulative at top) |
| --- | --- | --- | --- |
| 0.01 – 217,493.16 | 0.01 – 21,457.76 | **0% (exento)** | L0.00 |
| 217,493.17 – 331,638.50 | 21,457.77 – 30,969.88 | **15%** | L17,121.80 |
| 331,638.51 – 771,252.38 | 30,969.89 – 67,604.36 | **20%** | L105,044.57 |
| 771,252.39 and above | 67,604.37+ | **25%** | — |

2025 brackets adjusted using a 3.88% inflation figure (Banco Central de Honduras). Exempt threshold rose from L209,369.62 (2024) to L217,493.16 (2025).

**Subtract-method constants (2025)**

| Band | Rate | Subtract (L) |
| --- | --- | --- |
| 217,493.17 – 331,638.50 | 15% | 32,623.97 |
| 331,638.51 – 771,252.38 | 20% | 49,205.89 |
| 771,252.39+ | 25% | 87,768.51 |

*Continuity check:* at L331,638.50 → 0.15 × 331,638.50 − 32,623.97 = **L17,121.80**; at L771,252.38 → 0.20 × 771,252.38 − 49,205.89 = **L105,044.57**. Both bands tie out.

### ISR Progressive Table — Fiscal Year 2026 (CONFIRMED, SAR-published)

**ISR Progressive Table 2026**  _(SAR — Actualización de la Tabla Progresiva 2026; figures transcribed by Auxadi (Feb 2026))_

| Annual taxable income (L) | Approx. monthly (L) | Marginal rate |
| --- | --- | --- |
| 0.01 – 228,324.32 | 0.01 – 22,360.36 | **0% (exento)** |
| 228,324.33 – 348,154.10 | 22,360.37 – 32,346.18 | **15%** |
| 348,154.11 – 809,660.75 | 32,346.19 – 70,805.06 | **20%** |
| 809,660.76 and above | 70,805.07+ | **25%** |

**Subtract-method constants (2026)**

| Band | Rate | Subtract (L) |
| --- | --- | --- |
| 228,324.33 – 348,154.10 | 15% | 34,248.65 |
| 348,154.11 – 809,660.75 | 20% | 51,664.06 |
| 809,660.76+ | 25% | 92,130.10 |

*Continuity check:* at L348,154.10 → 0.15 × 348,154.10 − 34,248.65 = **L17,974.47**; 0.20 × 348,154.10 − 51,664.06 = **L17,966.76**. (~L7.71 rounding drift from the published bracket edges — acceptable for estimation; the precise SAR-published constants should be used in production. **[RESEARCH GAP — reviewer to confirm exact 2026 subtract constants]**.)

### Deductions before taxable net income

**Deductions table**  _(Bloomberg Línea; Galindo & Asociados)_

| Deduction | Amount | Notes | Source |
| --- | --- | --- | --- |
| Medical/educational expense deduction | **L40,000 flat per year** | Subtracted from gross before arriving at Renta Neta Gravable. The "approx. monthly" columns above EXCLUDE this L40,000. | Bloomberg Línea; Galindo & Asociados |
| IHSS + RAP employee contributions | Actual | Mandatory contributions reduce taxable base in practice. | **[RESEARCH GAP — reviewer to confirm deductibility/ordering against ISR law]** |

### Withholding mechanism

- ISR is **withheld monthly by the employer** from payroll and remitted monthly to SAR (PwC — Tax administration).
- Pure-salary employees whose tax is fully withheld generally **do not file** an annual return; those with fees, commissions, royalties, rental, or interest income **must file** Form 102 (PwC — Tax administration).

## Section 3 -- Social Security -- IHSS (Employee + Employer)

IHSS runs two contributory regimes plus occupational-risk cover. For 2025 both EM and IVM are capped at a monthly **contribution ceiling (techo de cotización) of L11,903.13** (Dinero HN — *IHSS oficializa techo 2025*). The ceiling rises gradually with minimum-wage adjustments; rate percentages did not change for 2025.

### IHSS Contribution Rates (2025)

**IHSS Contribution Rates**  _(ceiling + IVM split — Dinero HN; EM/IVM employer/employee splits — Mismo (Honduras Payroll Guide))_

| Regime | Employee | Employer | State | Monthly ceiling (2025) |
| --- | --- | --- | --- | --- |
| **EM** (Enfermedad y Maternidad — sickness/maternity) | **2.5%** | **5.0%** | 0.5% | L11,903.13 |
| **IVM** (Invalidez, Vejez y Muerte — disability/old-age/death) | **2.5%**\* | **3.5%** | 0.5% | L11,903.13 |
| **Riesgo Profesional** (occupational risk) | 0% | **0.2%** (range 0.2%–3.4% by risk class) | — | salary (no ceiling cited) |

**Column totals (employee side, EM + IVM, at/above ceiling):** 2.5% + 2.5% = **5.0%**. **Column totals (employer side, EM + IVM + min. occupational risk):** 5.0% + 3.5% + 0.2% = **8.7%** (8.5% without occupational risk; occupational risk varies by risk class).

> **[RESEARCH GAP — reviewer to confirm]** IHSS/Dinero HN report the IVM **employee** rate as **2.5%**; PwC (Other taxes) reports **1.0%** and shows older ceilings (L11,109.36 / L11,336.00). This skill uses the IHSS-published 2.5% and the L11,903.13 ceiling as the default. The IVM employee percentage and the EM/IVM employer percentages must be reconciled against the current IHSS resolution before any output is finalized.

**Monthly L-amounts at the 2025 ceiling (L11,903.13)**

| Regime | Employee | Employer |
| --- | --- | --- |
| EM | 2.5% × 11,903.13 = **L297.58** | 5.0% × 11,903.13 = **L595.16** |
| IVM | 2.5% × 11,903.13 = **L297.58** | 3.5% × 11,903.13 = **L416.61** |
| Occupational risk (0.2%) | — | 0.2% × 11,903.13 = **L23.81** |
| **Total IHSS at ceiling** | **L595.16** | **L1,035.58** |

*Check:* employee 297.58 + 297.58 = 595.16. Employer 595.16 + 416.61 + 23.81 = 1,035.58. Tie out.

## Section 4 -- Private Contributions -- RAP (Régimen de Aportaciones Privadas)

**RAP components**  _(Mismo — Honduras Payroll Guide)_

| Component | Employee | Employer | Base |
| --- | --- | --- | --- |
| **Fondo de Reserva Laboral** (reserve labor fund — severance/seniority) | 0% | **4.0%** | Ordinary monthly salary, capped at **3× the highest minimum wage** |
| **Ahorro sobre el techo IHSS** (savings above the IHSS ceiling) | **1.5%** | **1.5%** | Only the portion of salary **exceeding** the L11,903.13 IHSS ceiling |

- The Fondo de Reserva Laboral is **employer-only** and replaces the legacy severance reserve.
- The above-ceiling savings (1.5% + 1.5%) apply ONLY to the salary slice above L11,903.13/month.
- **[RESEARCH GAP — reviewer to confirm]** PwC describes the legacy "RAP 1.5%" as **optional** post-reform. Confirm mandatory vs optional treatment under Decreto 47-2024 before finalizing.

## Section 5 -- INFOP Training Levy

**INFOP details**  _(PwC — Other taxes; Mismo)_

| Item | Detail | Source |
| --- | --- | --- |
| Rate | **1% of total accrued monthly payroll** | PwC — Other taxes; Mismo |
| Who pays | **Employer-only** | PwC; Mismo |
| Applicability threshold | Commonly cited as **5+ employees** | Mismo — **[RESEARCH GAP — reviewer to confirm threshold against INFOP law]** |
| Payment deadline | Within **10 business days after month-end** | Mismo |

## Section 6 -- 13th & 14th Month Salary (Aguinaldo / Catorceavo)

Both are statutory and, under Honduran labor law, **fully exempt from ISR and from IHSS/RAP deductions** (legal basis: Reglamento del Décimo Cuarto Mes, Acuerdo 02-95).

**13th & 14th month table**  _(Finiquito Justo — Aguinaldo; Finiquito Justo — Décimo Cuarto; Acuerdo 02-95)_

| Item | Amount | Paid | Calculation | Source |
| --- | --- | --- | --- | --- |
| **13th month** (Aguinaldo / Décimo Tercer Mes) | One month's salary | **December** | Sum of fixed monthly salary Jan–Dec ÷ 12 | Finiquito Justo — Aguinaldo |
| **14th month** (Décimo Cuarto Mes / Catorceavo) | One month's salary | **June (deadline 30 June)** | Ordinary salarios 1 Jul (prior yr) – 30 Jun ÷ 12 | Finiquito Justo — Décimo Cuarto; Acuerdo 02-95 |

> **[RESEARCH GAP — reviewer to confirm]** Some secondary guides claim the 13th/14th are exempt only "up to 10× minimum wage." The labor regulation and Honduran labor-rights guidance treat them as **fully exempt**; this skill uses full exemption as the authoritative default. Flag the 10× cap as unverified against primary law (Reglamento + ISR law).

## Section 7 -- Minimum Wage

Honduras sets minimum wage by **sector and company size** (12 economic activities), not a single national figure. The maquila/textile free-zone sector has a single uniform wage.

### 2025 (CONFIRMED in effect)

**2025 minimum wage table**  _(EY; Secretaría de Trabajo)_

| Item | Amount | Source |
| --- | --- | --- |
| Legal basis | Acuerdo Ejecutivo STSS/SETRASS-109-2024, La Gaceta 21 Mar 2024 | EY; Secretaría de Trabajo |
| Average minimum wage 2025 | **~L13,985.16/month** | EY; Secretaría de Trabajo |
| Maquila (textile/free zones) 2025 | **L11,972.29/month** | EY; SETRASS Acuerdo 109-2024 |

Lowest-sector wages (agriculture, small business) are materially below the average.

### 2026 (PARTIAL / provisional)

**2026 minimum wage table**  _(SETRASS Acuerdo 109-2024; El Heraldo / La Prensa)_

| Item | Amount | Source / status |
| --- | --- | --- |
| Maquila 2026 | **L12,930.07/month** (+8%) | SETRASS Acuerdo 109-2024 (firm) |
| Average minimum wage 2026 | **L14,917.20/month** (≈L62.16/hr, +L932.04) | El Heraldo / La Prensa, **press only — [RESEARCH GAP — reviewer to confirm Acuerdo 233-2026 on official trabajo.gob.hn table]** |
| 2026 sector range | ~L9,596.64 (agriculture, small co.) up to L13,654.55–L19,298.72 (financial/insurance/real-estate) | La Prensa, **[RESEARCH GAP]** |

> For production, use the **2025 official table (Acuerdo 109-2024)** as the firm baseline and treat 2026 general-sector figures as provisional until confirmed on the official table.

## Section 8 -- Conservative Defaults

**Conservative defaults table**

| Unknown | Conservative default | Why |
| --- | --- | --- |
| Employee birth year / IVM rate split | Use **IVM employee 2.5%** (IHSS-published) | Higher than PwC's 1.0%; avoids under-withholding. Flag for reconciliation. |
| Occupational-risk class | Use **0.2%** (lowest band) for employer cost ONLY if class unknown, but FLAG | Avoids over-stating cost; but note range to 3.4% |
| Whether salary exceeds IHSS ceiling | Compute IHSS on **min(salary, L11,903.13)** | Ceiling is statutory |
| RAP above-ceiling savings | Apply 1.5% + 1.5% on the **excess over L11,903.13** | Mandatory per Decreto 47-2024 (pending optional-status flag) |
| INFOP applicability | Apply **1%** if employer has 5+ employees; FLAG if headcount unknown | Threshold unconfirmed |
| Medical deduction | Apply **L40,000** only if substantiated; otherwise omit | Deduction requires support |
| 13th/14th month taxability | Treat as **fully ISR/IHSS/RAP-exempt** | Labor-law default |
| Tax year | Default to **2025** table unless date ≥ 1 Jan 2026 | Skill tax_year is 2025 |
| Currency | Lempira (HNL) | Foreign-currency wage payment is prohibited |

## Section 9 -- Required Inputs + Refusal Catalogue

### Required inputs before computing payroll

1. Gross monthly salary in Lempiras (and whether it is fixed/ordinary).
2. Pay frequency (weekly/monthly) and worker class (manual vs office/intellectual).
3. Number of employees on the planilla (for INFOP applicability).
4. Tax/fiscal year (2025 vs 2026 ISR table).
5. Whether the L40,000 medical deduction is substantiated.
6. Occupational-risk class (for employer cost) where available.
7. Confirmation of any non-ordinary pay components (overtime, commissions, bonuses).

### Refusal catalogue — DO NOT compute, refuse and request input

- **No gross salary provided** — REFUSE — request salary in Lempiras
- **Salary stated in USD/EUR with no HNL conversion and no rate** — REFUSE — wages are legally paid in Lempiras; request HNL figure
- **Request to pay wages in foreign currency** — REFUSE — prohibited under the Labor Code
- **Request to omit ISR withholding or IHSS/RAP/INFOP to "save money"** — REFUSE — these are statutory; escalate to accountant
- **Request to treat 13th/14th month as taxable to inflate withholding** — REFUSE — statutorily exempt; flag
- **Self-employed / fee / rental / royalty income mixed in** — REFUSE payroll path — route to a Honduras income-tax skill (Form 102)
- **Definitive "this is your exact tax" assertion requested** — REFUSE — outputs are estimates pending accountant sign-off

## Section 10 -- Transaction / Payment Pattern Library (deterministic)

Classify bank-statement lines deterministically. Match case-insensitively; longest/most-specific pattern wins.

### Salary credits (money arriving in an employee account)

**Salary credits table**

| Pattern (regex-ish, case-insensitive) | Classification |
| --- | --- |
| `SALARIO`, `PAGO PLANILLA`, `NOMINA`, `SUELDO` | Net salary payment |
| `TRANSF.* [empresa]`, `ABONO SALARIO` | Net salary payment |
| `AGUINALDO`, `DECIMO TERCER`, `13.* MES` | 13th month (ISR-exempt) |
| `CATORCEAVO`, `DECIMO CUARTO`, `14.* MES` | 14th month (ISR-exempt) |
| `REINTEGRO IHSS`, `DEVOLUCION IHSS` | IHSS refund/adjustment — not income |

### Employer debits (money leaving the employer account)

**Employer debits table**

| Pattern | Classification |
| --- | --- |
| `SAR`, `RETENCION ISR`, `ISR PLANILLA`, `DET LIVE` | ISR withholding remitted to SAR (liability settlement) |
| `IHSS`, `PLANILLA IHSS`, `SEGURO SOCIAL` | IHSS contribution (employer + employee portions) |
| `RAP`, `APORTACIONES PRIVADAS`, `FONDO RESERVA` | RAP contribution |
| `INFOP` | INFOP 1% training levy |
| `PAGO NOMINA`, `PLANILLA SALARIOS`, `DISPERSION` | Net wages disbursed to employees |

## Section 11 -- Worked Examples

> All figures use the **2025** ISR table and the L11,903.13 IHSS ceiling. IHSS IVM employee rate = 2.5% (IHSS-published default; pending PwC reconciliation). Amounts rounded to the cent.

### Example 1 — Low earner, below exempt threshold

**Inputs:** Fixed salary L18,000/month → annual gross L216,000. No medical deduction claimed.

- Annual gross L216,000 < L217,493.16 exempt threshold → **ISR = L0.00**.
- IHSS base = min(18,000, 11,903.13) = 11,903.13.
  - Employee EM 2.5% = L297.58; IVM 2.5% = L297.58 → **employee IHSS L595.16**.
- RAP: salary 18,000 > ceiling 11,903.13 → above-ceiling slice = 18,000 − 11,903.13 = L6,096.87.
  - Employee RAP 1.5% × 6,096.87 = **L91.45**.
- **Employee deductions total** = 595.16 + 91.45 = **L686.61**.
- **Net pay** = 18,000.00 − 0.00 − 686.61 = **L17,313.39**.

*Bank line example:* `PAGO PLANILLA — JUNIO` credit **L17,313.39**.

### Example 2 — Mid earner, into the 15% ISR band

**Inputs:** Fixed salary L28,000/month → annual gross L336,000. L40,000 medical deduction substantiated.

- Annual taxable net = 336,000 − 40,000 = **L296,000** (falls in the 15% band: 217,493.17–331,638.50).
- ISR (annual) = 0.15 × 296,000 − 32,623.97 = 44,400.00 − 32,623.97 = **L11,776.03/year**.
- Monthly ISR withholding ≈ 11,776.03 ÷ 12 = **L981.34**.
- IHSS base = ceiling 11,903.13 → employee EM 297.58 + IVM 297.58 = **L595.16**.
- RAP above-ceiling: (28,000 − 11,903.13) × 1.5% = 16,096.87 × 1.5% = **L241.45**.
- **Employee deductions total** = 981.34 + 595.16 + 241.45 = **L1,817.95**.
- **Net pay** = 28,000.00 − 1,817.95 = **L26,182.05**.

### Example 3 — Higher earner, into the 20% ISR band

**Inputs:** Fixed salary L50,000/month → annual gross L600,000. L40,000 medical deduction substantiated.

- Annual taxable net = 600,000 − 40,000 = **L560,000** (20% band: 331,638.51–771,252.38).
- ISR (annual) = 0.20 × 560,000 − 49,205.89 = 112,000.00 − 49,205.89 = **L62,794.11/year**.
- Monthly ISR ≈ 62,794.11 ÷ 12 = **L5,232.84**.
- IHSS employee at ceiling = **L595.16**.
- RAP above-ceiling: (50,000 − 11,903.13) × 1.5% = 38,096.87 × 1.5% = **L571.45**.
- **Employee deductions total** = 5,232.84 + 595.16 + 571.45 = **L6,399.45**.
- **Net pay** = 50,000.00 − 6,399.45 = **L43,600.55**.

### Example 4 — Top-band earner (25% ISR)

**Inputs:** Fixed salary L90,000/month → annual gross L1,080,000. L40,000 medical deduction.

- Annual taxable net = 1,080,000 − 40,000 = **L1,040,000** (25% band: ≥771,252.39).
- ISR (annual) = 0.25 × 1,040,000 − 87,768.51 = 260,000.00 − 87,768.51 = **L172,231.49/year**.
- Monthly ISR ≈ 172,231.49 ÷ 12 = **L14,352.62**.
- IHSS employee at ceiling = **L595.16**.
- RAP above-ceiling: (90,000 − 11,903.13) × 1.5% = 78,096.87 × 1.5% = **L1,171.45**.
- **Employee deductions total** = 14,352.62 + 595.16 + 1,171.45 = **L16,119.23**.
- **Net pay** = 90,000.00 − 16,119.23 = **L73,880.77**.

### Example 5 — Employer total cost of a mid earner (L28,000/month)

**Employer cost table**

| Employer cost item | Computation | Amount (L) |
| --- | --- | --- |
| Gross salary | — | 28,000.00 |
| IHSS EM 5.0% (on ceiling) | 5.0% × 11,903.13 | 595.16 |
| IHSS IVM 3.5% (on ceiling) | 3.5% × 11,903.13 | 416.61 |
| IHSS occupational risk 0.2% | 0.2% × 11,903.13 | 23.81 |
| RAP reserve fund 4.0% | 4.0% × 28,000.00 (within 3× max-min-wage cap) | 1,120.00 |
| RAP above-ceiling 1.5% (employer) | 1.5% × (28,000 − 11,903.13) | 241.45 |
| INFOP 1.0% (if 5+ employees) | 1.0% × 28,000.00 | 280.00 |
| **Total employer cost** | sum | **30,677.03** |

*Check:* 28,000 + 595.16 + 416.61 + 23.81 + 1,120.00 + 241.45 + 280.00 = **30,677.03**. Tie out. (Employer-on-top burden = L2,677.03 = ~9.56% of gross at this salary.)

### Example 6 — 13th month (aguinaldo), December

**Inputs:** Fixed salary L28,000/month, full year worked.

- Aguinaldo = sum(Jan–Dec salary) ÷ 12 = (28,000 × 12) ÷ 12 = **L28,000.00**.
- ISR on aguinaldo = **L0.00** (statutorily exempt).
- IHSS/RAP on aguinaldo = **L0.00** (exempt).
- **Net aguinaldo = L28,000.00** paid in December.

## Section 12 -- Tier 1 Rules (hard, non-negotiable)

- **Rule 1** — ISR is employer-withheld monthly and remitted to SAR; never skip it for salaried staff.  _(PwC)_
- **Rule 2** — Use the annual Renta Neta Gravable with the correct year's table; apply the subtract-method constants exactly.
- **Rule 3** — IHSS EM and IVM are each capped at the L11,903.13/month ceiling (2025).  _(Dinero HN)_
- **Rule 4** — The 13th and 14th month salaries are ISR/IHSS/RAP exempt by default.  _(Acuerdo 02-95)_
- **Rule 5** — RAP reserve fund (4% employer) and INFOP (1% employer) are employer-only.
- **Rule 6** — Wages must be paid in Lempiras; foreign-currency payment is prohibited.  _(Labor Code)_
- **Rule 7** — Annual ISR return (Form 102) is due 30 April.  _(SAR)_
- **Rule 8** — IHSS, RAP, and ISR withholding are remitted monthly; INFOP within 10 business days after month-end.
- **Rule 9** — Every output is an estimate pending licensed-accountant sign-off.

## Section 13 -- Tier 2 Catalogue (reviewer judgement required)

**Tier 2 catalogue table**

| Question | Why it needs a reviewer |
| --- | --- |
| IVM employee rate (2.5% vs PwC 1.0%) | Conflicting authoritative sources |
| Exact EM/IVM employer percentages vs current IHSS acuerdo | Ceiling changed; percentages need verification |
| RAP mandatory vs optional post-Decreto 47-2024 | PwC suggests optional treatment |
| Exact ISR late-filing multa % and interest rate | Código Tributario not cleanly extracted |
| 13th/14th month full exemption vs 10× min-wage cap | Secondary-source conflict |
| 2026 general-sector minimum wage (Acuerdo 233-2026) | Press-only, not on official table |
| INFOP 5+ employee threshold | Cited but not primary-confirmed |
| Deductibility/ordering of IHSS+RAP against ISR base | Not confirmed against ISR law |
| Occupational-risk class for a given employer | Varies 0.2%–3.4% by risk class |

## Section 14 -- Excel Working Paper Template

**Excel working paper template**

| Col | Header | Formula / source |
| --- | --- | --- |
| A | Employee name | input |
| B | Birth year | input (drives IVM split reconciliation) |
| C | Gross monthly salary (L) | input |
| D | Annual gross | `=C*12` |
| E | Medical deduction | `=IF(substantiated,40000,0)` |
| F | Annual taxable net | `=MAX(0, D-E)` |
| G | ISR annual | nested IF on F using 2025 subtract constants (32,623.97 / 49,205.89 / 87,768.51) |
| H | ISR monthly | `=G/12` |
| I | IHSS base | `=MIN(C, 11903.13)` |
| J | Employee IHSS | `=I*(2.5%+2.5%)` |
| K | Above-ceiling slice | `=MAX(0, C-11903.13)` |
| L | Employee RAP | `=K*1.5%` |
| M | Employee deductions | `=H+J+L` |
| N | Net pay | `=C-M` |
| O | Employer IHSS | `=I*(5.0%+3.5%+0.2%)` |
| P | Employer RAP | `=C*4.0% + K*1.5%` |
| Q | INFOP | `=IF(headcount>=5, C*1.0%, 0)` |
| R | Total employer cost | `=C+O+P+Q` |

- **ISR formula for column G (2025)** — =IF(F<=217493.16,0, IF(F<=331638.50, F*0.15-32623.97, IF(F<=771252.38, F*0.20-49205.89, F*0.25-87768.51)))

## Section 15 -- Bank Statement / Terminology Reading Guide

**Terminology reading guide**

| Spanish term | English / meaning |
| --- | --- |
| Planilla | Payroll / payroll run |
| Salario / Sueldo | Salary / wage |
| Retención ISR | Income-tax withholding |
| Renta Neta Gravable | Taxable net income |
| Aguinaldo / Décimo Tercer Mes | 13th month salary (December) |
| Catorceavo / Décimo Cuarto Mes | 14th month salary (June) |
| Techo de cotización | Contribution ceiling |
| IHSS | Honduran Social Security Institute |
| EM / IVM | Sickness-maternity / disability-old-age-death regimes |
| RAP | Private contributions regime |
| Fondo de Reserva Laboral | Reserve labor (severance) fund |
| INFOP | Vocational-training levy |
| Reintegro / Devolución | Refund / reimbursement |
| Maquila | Textile / free-zone manufacturing sector |
| Salario mínimo | Minimum wage |

## Section 16 -- Onboarding Fallback

If the engagement lacks key data:

1. **No prior planilla available** → request the last 3 months of payroll registers and IHSS/RAP/SAR receipts to back-solve rates actually applied.
2. **Unknown headcount** → default INFOP off, FLAG; confirm before first remittance.
3. **Unknown employee birth years** → default IVM employee 2.5%, FLAG for reconciliation.
4. **Unknown sector/min-wage band** → use the 2025 average (L13,985.16) only as a sanity check, never as the contractual wage; obtain the employee's contract.
5. **Year ambiguity** → default 2025 table; switch to 2026 only for periods ≥ 1 Jan 2026.

## Section 17 -- Filing, Forms & Deadlines

**Filing forms deadlines table**

| Item | Detail | Source |
| --- | --- | --- |
| Tax year | Calendar year ending 31 Dec | PwC — Tax administration |
| Annual ISR return (natural persons) | Due **30 April** (rolls to next business day). Form **102**, via SAR DET Live | SAR; SAR DET Live ISR_PN |
| Employer ISR withholding | Withheld monthly; remitted **monthly** to SAR | PwC |
| IHSS planilla | Filed and paid **monthly** (late filing can block employee healthcare access) | Mismo |
| RAP deposits | **Monthly** (reserve fund + above-ceiling savings) | Mismo |
| INFOP | Within **10 business days** after month-end | Mismo |

## Section 18 -- Penalties (late filing / late payment)

Governed by the **Código Tributario (Decreto 22-97 and reforms)** and the ISR/ISV laws.

**Penalties table**

| Item | Detail | Source |
| --- | --- | --- |
| Late-filed return | Fine (multa) + surcharge (recargo) + interest (interés) per the Tax Code. For ISV the cited rate is **5% of tax per month or fraction** of delay (Art. 11 ISV law); a comparable monthly surcharge applies to ISR. | SAR; Código Tributario |
| Late payment (mora) | Assessed tax payable within **10 days** of assessment; interest + surcharges accrue from the original due date. | Código Tributario; PwC |
| Escalation | Repeated/total or partial non-payment can become criminal **defraudación fiscal**. | Código Tributario |
| Statute of limitations | Generally **4–7 years**. | Código Tributario |

> **[RESEARCH GAP — reviewer to confirm]** The exact **ISR-specific** late-filing multa percentage, monetary caps, and interest rate could NOT be cleanly extracted from the Código Tributario PDF. The 5%/month figure is documented for ISV; read the ISR figures directly from Decreto 22-97 (consolidated) before relying on them.

## Section 19 -- Summary Employer/Employee Burden (2025, salary at/above ceiling)

**Summary burden table**

| Contribution | Employee | Employer | Base/cap |
| --- | --- | --- | --- |
| ISR | 0–25% progressive | (withholding agent) | annual taxable net |
| IHSS EM | 2.5% | 5.0% | up to L11,903.13/mo |
| IHSS IVM | 2.5%\* | 3.5% | up to L11,903.13/mo |
| IHSS occupational risk | — | 0.2% (0.2–3.4%) | salary |
| RAP reserve fund | — | 4.0% | salary, cap 3× max min wage |
| RAP above-ceiling savings | 1.5% | 1.5% | salary above L11,903.13 |
| INFOP | — | 1.0% | total payroll (5+ employees) |

*IVM employee rate: IHSS/Dinero HN = 2.5% (used here); PwC = 1.0% — **needs primary-source reconciliation.**

## Section 20 -- Reference Material

**Reference material table**

| Topic | Figure | Source |
| --- | --- | --- |
| ISR 2025 exempt threshold | L217,493.16 | Bloomberg Línea; KPMG; Auxadi |
| ISR 2025 bands | 15% / 20% / 25% at L331,638.50 / L771,252.38 edges | Bloomberg Línea; KPMG |
| ISR 2026 exempt threshold | L228,324.32 | SAR; Auxadi |
| Medical deduction | L40,000 | Bloomberg Línea; Galindo & Asociados |
| IHSS 2025 ceiling | L11,903.13 | Dinero HN |
| IHSS EM | 2.5% ee / 5.0% er | Mismo; Dinero HN |
| IHSS IVM | 2.5%\* ee / 3.5% er | Dinero HN (\*PwC 1.0%) |
| RAP reserve fund | 4.0% employer | Mismo (Decreto 47-2024) |
| RAP above-ceiling | 1.5% + 1.5% | Mismo |
| INFOP | 1.0% employer, 10 biz-day deadline | PwC; Mismo |
| Min wage 2025 average | L13,985.16/mo | EY; Secretaría de Trabajo |
| Maquila 2025 / 2026 | L11,972.29 / L12,930.07 | EY; SETRASS Acuerdo 109-2024 |
| Annual ISR deadline | 30 April, Form 102 | SAR |

Key authorities: SAR (`sar.gob.hn`, DET Live), IHSS, RAP, INFOP, Secretaría de Trabajo (`trabajo.gob.hn`), Banco Central de Honduras. Big-4/secondary: PwC Tax Summaries, KPMG TaxNewsFlash, EY, Auxadi, Galindo & Asociados, Mismo, Bloomberg Línea, Finiquito Justo.

## Section 21 -- Test Suite

Each test recomputes end-to-end. Expected values use the 2025 table and IVM employee 2.5%.

1. **Exempt earner.** Salary L18,000/mo (annual L216,000), no medical deduction.
   Expected: ISR = **L0.00**; employee IHSS = **L595.16**; employee RAP = **L91.45**;
   net = **L17,313.39**.

2. **15% band.** Salary L28,000/mo, L40,000 deduction. Taxable net **L296,000**;
   ISR annual **L11,776.03**; ISR monthly **L981.34**; net **L26,182.05**.

3. **20% band.** Salary L50,000/mo, L40,000 deduction. Taxable net **L560,000**;
   ISR annual **L62,794.11**; ISR monthly **L5,232.84**; net **L43,600.55**.

4. **25% band.** Salary L90,000/mo, L40,000 deduction. Taxable net **L1,040,000**;
   ISR annual **L172,231.49**; ISR monthly **L14,352.62**; net **L73,880.77**.

5. **Employer cost.** Salary L28,000/mo, 5+ employees. Total employer cost **L30,677.03**.

6. **Aguinaldo.** Salary L28,000/mo full year. 13th month = **L28,000.00**, ISR **L0.00**, net **L28,000.00**.

7. **Bracket continuity.** At L331,638.50 ISR = **L17,121.80**; at L771,252.38 ISR = **L105,044.57** (subtract constants tie out).

8. **IHSS ceiling.** Salary L11,903.13 or above → employee IHSS always **L595.16/mo** (EM 297.58 + IVM 297.58).

9. **Below threshold edge.** Annual taxable net L217,493.16 → ISR **L0.00**; L217,493.17 → ISR ≈ **L0.00002** (effectively zero at the cent).

10. **Currency refusal.** Salary stated in USD with no HNL conversion → REFUSE and request Lempira figure.

## PROHIBITIONS

- **ISR withholding obligation** — NEVER skip ISR withholding for salaried employees — the employer is the legal withholding agent.
- **13th/14th month ISR exemption** — NEVER apply ISR to the 13th or 14th month salary — they are statutorily exempt.
- **IHSS ceiling application** — NEVER apply IHSS EM/IVM contributions above the L11,903.13/month ceiling.
- **Employer-only obligations** — NEVER omit the employer-only obligations: RAP reserve fund (4%) and INFOP (1%, 5+ employees).
- **Currency requirement** — NEVER pay or compute wages in a foreign currency — Lempiras only.
- **PwC IVM rate conflict flag** — NEVER use PwC's 1.0% IVM employee rate without flagging the conflict with the IHSS-published 2.5%.
- **2026 minimum wage press-only status** — NEVER present the 2026 general-sector minimum wage (Acuerdo 233-2026) as confirmed — it is press-only.
- **ISR late-filing penalty unconfirmed** — NEVER state an exact ISR late-filing penalty — the precise figure is an unconfirmed research gap.
- **Remittance deadlines** — NEVER miss the monthly IHSS/RAP/ISR remittance or the 10-business-day INFOP deadline.
- **Estimated computations disclaimer requirement** — NEVER present payroll computations as definitive — always label as estimated and direct to a licensed Honduran accountant.

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a licensed contador público in Honduras) before implementation.

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
