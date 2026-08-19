---
name: paraguay-payroll
description: "Use this skill whenever asked about Paraguay payroll processing for employed persons. Trigger on phrases like \"Paraguay payroll\", \"Paraguayan payroll\", \"planilla de sueldos\", \"planilla de aporte obrero-patronal\", \"IPS Paraguay\", \"aporte obrero\", \"aporte patronal\", \"Instituto de Previsión Social\", \"social security Paraguay\", \"9% IPS\", \"16.5% IPS\", \"IRP Paraguay\", \"Impuesto a la Renta Personal\", \"renta de servicios personales\", \"Formulario 515\", \"Marangatú\", \"salario mínimo Paraguay\", \"minimum wage Paraguay\", \"aguinaldo\", \"13th salary Paraguay\", \"net salary Paraguay\", \"salario neto\", \"gross to net Paraguay\", \"employer contribution Paraguay\", \"DNIT payroll\", \"REI Paraguay\", or any question about computing employee pay, social security contributions, or the income-tax position for Paraguay-based employees. CRITICAL STRUCTURAL FACT: in Paraguay the employer is generally NOT an income-tax (IRP) withholding agent on dependent salaries — IRP is self-assessed annually by the individual. The employer's mandatory payroll burden is IPS social security (employee 9% + employer 16.5% commercial). This skill covers IPS contributions, the minimum wage, the mandatory aguinaldo (13th salary), the IRP self-assessment position, monthly IPS filing, and payslip/income-certificate obligations. ALWAYS read this skill before processing any Paraguay payroll."
version: 0.1
jurisdiction: PY
tax_year: 2025
last_updated: 2026-07-13
review_status: pending_review
depends_on:
  - payroll-workflow-base
category: payroll
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Paraguay Payroll Skill v0.1 (Tier 2 — research-verified, reviewer sign-off pending)

## Paraguay Payroll Skill v0.1 (Tier 2 — research-verified, reviewer sign-off pending)

> **Tier 2 status.** Every rate, threshold, and deadline below is sourced to a named authority (DNIT, IPS, MTESS) or a Big-4 summary (PwC Worldwide Tax Summaries) and cited inline. It has **not** yet been section-by-section verified by a licensed Paraguayan accountant (contador público). Items marked **[RESEARCH GAP — reviewer to confirm]** carry residual uncertainty and must be confirmed against primary sources before reliance.

> **READ THIS FIRST — the single most important structural fact.** Paraguay levies a personal income tax (**IRP — Impuesto a la Renta Personal**), but for salaried (dependent) employees **IRP is NOT withheld at source by the employer.** It is a **self-assessed annual tax** filed by the individual taxpayer (Form 515 via Marangatú). The employer's mandatory monthly payroll burden is therefore primarily **IPS social security** (employee withholding + employer contribution). Do not "withhold IRP from a salary" — that is wrong for Paraguay. See Section 2.

## Section 1 -- Quick Reference

**Quick Reference table**

| Field | Value |
| --- | --- |
| Country | Paraguay (Republic of Paraguay) |
| Currency | PYG (Paraguayan Guaraní) only |
| Standard pay frequency | Monthly |
| Tax year | Calendar year (1 January -- 31 December) |
| Income-tax withholding on salaries | **None by the employer** — IRP is self-assessed annually by the individual (Ley N° 6380/2019; DNIT) |
| Employee IPS contribution (commercial) | **9.0%** of gross wage, withheld by employer (PwC; IPS) |
| Employer IPS contribution (commercial) | **16.5%** of gross wage (PwC; IPS) |
| Combined IPS (commercial) | **25.5%** (PwC) |
| Employee / employer IPS (financial sector) | **11% / 17%** (PwC) |
| IPS base | Every wage item in cash or in kind, EXCEPT aguinaldo and family allowance; floor = minimum wage (PwC) |
| IPS ceiling | No salary ceiling confirmed — **[RESEARCH GAP — reviewer to confirm]** (PwC reports none specified) |
| IRP registration/filing threshold | Gross personal-service income **> PYG 80,000,000/year** (DNIT; PwC) |
| IRP rates (net taxable income) | 8% up to 50,000,000; 9% on 50,000,001–150,000,000; 10% above 150,000,000 (PwC; DNIT) |
| Minimum wage (from 1 Jul 2025) | **PYG 2,899,048/month** (general) (MTESS Resolución N° 677/2025) |
| Aguinaldo (13th salary) | Mandatory; 1/12 of annual remuneration; payable before 31 Dec; **exempt from IPS and IRP** (Ley N° 417/73) |
| Tax authority | DNIT — Dirección Nacional de Ingresos Tributarios (absorbed the former SET in 2023) |
| Social-security authority | IPS — Instituto de Previsión Social |
| Labour authority (minimum wage) | MTESS — Ministerio de Trabajo, Empleo y Seguridad Social |
| Key legislation | Ley N° 6380/2019 (IRP) + Decreto N° 3184/2019; Ley N° 98/92 & Ley N° 213/93 (Código del Trabajo, IPS), reformed by Ley N° 7446/2024; Ley N° 417/73 (aguinaldo) |
| Filing portals | IPS: **REI** (Registro del Empleador por Internet); DNIT/IRP: **Marangatú** |
| Validated by | Pending — requires sign-off by a licensed Paraguayan accountant |
| Skill version | 0.1 (Tier 2) |

## Section 2 -- Income Tax Position (IRP — self-assessed, NOT employer-withheld)

Paraguay **does** levy a personal income tax — **IRP (Impuesto a la Renta Personal), Rentas de Servicios Personales** — under **Ley N° 6380/2019 ("Modernización Tributaria")** and **Decreto N° 3184/2019** (DNIT). The crucial payroll consequence: for **dependent (salaried) employees the employer is generally NOT an IRP withholding agent.** IRP is **self-assessed and filed annually by the individual** taxpayer.

### 2.1 What the employer does (and does not) do

- **Employer role for IRP vs IPS** — The employer does NOT withhold IRP from monthly salaries. The employer's role for IRP is to issue payslips / income certificates that the employee uses to prepare their own annual Form 515 (DNIT — IRP portal). The employer DOES withhold and remit IPS (Sections 3–4) — that is the mandatory monthly payroll burden.  _(DNIT — IRP portal)_

### 2.2 IRP registration / filing threshold (the employee's own obligation)

- **Register & pay IRP only if gross personal-service income exceeds** — PYG 80,000,000 per year  _(DNIT — IRP portal; PwC — Taxes on personal income)_

> PwC: "If the taxpayer's gross income from the provision of personal services does not exceed PYG 80 million, they will not be required to pay the tax." Below the threshold, **no IRP is due** and no registration is required.

### 2.3 IRP progressive rate scale (on NET taxable income, FY2025)

**IRP progressive rate scale**  _(PwC; DNIT)_

| Net taxable income (PYG) | Rate | Source |
| --- | --- | --- |
| Up to 50,000,000 | 8% | PwC; DNIT |
| 50,000,001 – 150,000,000 | 9% (on the slice in this band) | PwC; DNIT |
| 150,000,001 and above | 10% (on the slice above 150,000,000) | PwC; DNIT |

Applied to **net taxable income** (gross less allowable deductions), not gross. (DNIT — IRP portal; PwC.)

**Cumulative-tax check (recomputed):**
- At exactly 50,000,000 net: 8% × 50,000,000 = **4,000,000**.
- At exactly 150,000,000 net: 4,000,000 + 9% × (150,000,000 − 50,000,000) = 4,000,000 + 9,000,000 = **13,000,000**.
- At 200,000,000 net: 13,000,000 + 10% × (200,000,000 − 150,000,000) = 13,000,000 + 5,000,000 = **18,000,000**. (Self-verified — see Section 9, IRP illustration.)

> A secondary search summary cited a "9% at PYG 100M" break-point; the authoritative PwC/DNIT brackets (50M / 150M thresholds) above are treated as correct. The flat **8%** rate also applies to capital gains and rental income.

### 2.4 IRP deductions

IRP-RSP allows deduction of documented personal/family expenses and investments (the DNIT "net income scale"), governed by **Decreto N° 3184/2019**.

> **[RESEARCH GAP — reviewer to confirm]** The exact deductible categories and any caps were not quoted from an authoritative figure-level source. A licensed Paraguayan accountant must confirm the deductible-expense rules and caps against Decreto N° 3184/2019 and current DNIT guidance before computing any employee's net taxable income.

### 2.5 IRP forms, system and deadline

**IRP forms, system and deadline**  _(DNIT)_

| Item | Detail | Source |
| --- | --- | --- |
| Form | **Formulario 515** — Declaración Jurada IRP Rentas de Servicios Personales | DNIT — Instructivo Formulario 515 |
| System | **Marangatú** (electronic) | DNIT |
| Obligation codes | Form 715-IRP RSP / Form 716-IRP RGC referenced on the DNIT institutional page | DNIT |
| Deadline | Annually in **March**, per the "calendario perpetuo" keyed to the taxpayer's RUC ending digit | DNIT — IRP portal |

### 2.6 Aguinaldo is IRP-exempt

- **Aguinaldo IRP exemption** — The mandatory aguinaldo (13th salary) is exempt from IRP — it does not enter the taxable base. See Section 6.  _(Ley N° 417/73)_

## Section 3 -- Social Security (IPS) -- Employee Deductions

Paraguay's mandatory social-security scheme is **IPS (Instituto de Previsión Social)** (Ley N° 98/92; Ley N° 213/93 Código del Trabajo; reformed by Ley N° 7446/2024). The employer **withholds** the employee share and remits it together with the employer share via the **REI** online system.

### 3.1 Employee contribution (Aporte Obrero)

**Employee IPS contribution rates**  _(PwC — Other taxes; IPS/MTESS)_

| Sector | Employee rate | Base | Source |
| --- | --- | --- | --- |
| Commercial / private-sector | **9.0%** of gross wage | Every wage item in cash or in kind, EXCEPT aguinaldo and family allowance; floor = minimum wage | PwC — Other taxes; IPS/MTESS |
| Financial sector (banks/finance) | **11%** of gross wage | Same | PwC — Other taxes |

- **Floor, ceiling, and illegal over-deduction** — Floor: the contribution base cannot be below the legal minimum wage (Section 5). Ceiling: [RESEARCH GAP — reviewer to confirm] — no salary ceiling confirmed; PwC reports none specified. Treat IPS as uncapped on the full wage absent contrary authority. It is illegal to deduct more than the 9% employee share from the worker's pay (misappropriation offence) — the 16.5% employer share must be paid from the employer's own funds.  _(MTESS)_

## Section 4 -- Social Security (IPS) -- Employer Contributions

### 4.1 Employer contribution (Aporte Patronal)

**Employer IPS contribution rates**  _(PwC — Other taxes; IPS/MTESS)_

| Sector | Employer rate | Base | Source |
| --- | --- | --- | --- |
| Commercial / private-sector | **16.5%** of gross wage | Same base as employee | PwC — Other taxes; IPS/MTESS |
| Financial sector (banks/finance) | **17%** of gross wage | Same | PwC — Other taxes |

### 4.2 Combined IPS burden

**Combined IPS burden table**  _(PwC)_

| Sector | Employee | Employer | Combined |
| --- | --- | --- | --- |
| Commercial | 9.0% | 16.5% | **25.5%** |
| Financial | 11% | 17% | **28%** |

**Total-row check (recomputed):** commercial 9.0 + 16.5 = **25.5** ✓; financial 11 + 17 = **28** ✓. (Self-verified — both additions reconcile.)

### 4.3 Aguinaldo is IPS-exempt

- **Aguinaldo IPS exemption** — The aguinaldo is NOT subject to IPS contributions and is unembargable (no deductions permitted). See Section 6.  _(PwC; IPS)_

### 4.4 Payment deadline and penalties

**Payment deadline and penalties table**  _(IPS portal; Vouga; Ley N° 7446/2024; worki360/Deel (secondary))_

| Item | Detail | Source |
| --- | --- | --- |
| Monthly filing | "Planilla de aporte obrero-patronal" via the **REI** system | IPS portal |
| Payment deadline | Per the IPS **"Calendario de Pago"** (Resolución C.A. N° 066/2022); **"Mora Patronal"** (employer default) arises the day after the due date | Vouga / IPS |
| Administrative component | Reduced to **1%** by Ley N° 7446/2024 | Ley N° 7446/2024 |
| Late-payment surcharges (recargos moratorios) | Reported range **1% up to 50%** depending on months of delay, plus interest — **[RESEARCH GAP — reviewer to confirm]** (from secondary aggregators; confirm against the IPS resolution) | worki360/Deel (secondary) |

## Section 5 -- Minimum Wage (Salario Mínimo)

**Minimum wage table**  _(MTESS Resolución N° 677/2025)_

| Item | 2025 value | Source |
| --- | --- | --- |
| Monthly minimum (general/unspecified activities) | **PYG 2,899,048** | MTESS Resolución N° 677/2025 |
| Daily wage (jornaleros) | PYG 111,502 | MTESS Res. 677/2025 |
| Daily rate (mensualizados) | PYG 96,635 | MTESS Res. 677/2025 |
| Hourly rate (mensualizados) | PYG 12,080 | MTESS Res. 677/2025 |
| Night-shift monthly (with +30%) | PYG 3,768,763 | MTESS Res. 677/2025 |

**Authority:** MTESS. Current: **Resolución MTESS N° 677/2025**, effective **1 July 2025** (+3.6% adjustment).

- The minimum wage also functions as the **IPS contribution floor** (Section 3).

> **[RESEARCH GAP — reviewer to confirm]** The next adjustment is expected July 2026 (under tripartite negotiation as of April 2026; not yet officially confirmed). Use the **PYG 2,899,048** figure as the current authoritative minimum; do not apply an unconfirmed 2026 figure.

## Section 6 -- Aguinaldo (13th-month salary) — mandatory

**Aguinaldo table**  _(Ley N° 417/73)_

| Item | Detail | Source |
| --- | --- | --- |
| Legal basis | Código del Trabajo + **Ley N° 417/73** | Ley N° 417/73 |
| Amount | **1/12 of total remuneration earned during the calendar year** | Ley N° 417/73 |
| Payment deadline | **Before 31 December** | Ley N° 417/73 |
| IPS treatment | **Exempt** — not in the IPS base | PwC; IPS |
| IRP treatment | **Exempt** — not in the IRP taxable base | Ley N° 417/73 |
| Other | Unembargable; no deductions permitted | finiquitojusto (secondary) |

## Section 7 -- Conservative Defaults

- **Conservative defaults list** — When inputs are ambiguous, apply these defaults and flag the assumption to the user: 1. No employer IRP withholding. Never withhold IRP from a monthly salary. Compute IPS only; treat IRP as the employee's own annual self-assessment (Section 2). If asked to "withhold income tax from the salary", explain that Paraguay does not do this for dependent employees. 2. Sector = commercial. Apply the commercial IPS rates (employee 9.0% / employer 16.5%) unless the employer is a bank/finance entity, in which case use 11% / 17% (Section 4). 3. IPS base = full gross (every cash/in-kind wage item) excluding aguinaldo and family allowance, with the minimum-wage floor applied. Apply no ceiling (uncapped) absent confirmed authority — and flag this as a research gap (Section 3). 4. Currency: all amounts in PYG. Never assume USD or any other currency. 5. Pay period: assume FY2025 figures (minimum wage PYG 2,899,048 from 1 Jul 2025). Do not apply an unconfirmed 2026 minimum wage. 6. Aguinaldo: compute as 1/12 of annual remuneration, exempt from both IPS and IRP (Section 6). 7. IRP deductions: do not assume any deduction figures — they are a research gap (Section 2.4). Compute IRP illustrations on stated net taxable income only, and label them estimates.

### 8.1 Required inputs (must have before computing IPS payroll)

**Required inputs table**

| Input | Why needed |
| --- | --- |
| Monthly **gross** wage in PYG (cash + in kind) | Drives the IPS base and both contribution shares |
| Employer sector (commercial vs financial) | Selects 9%/16.5% vs 11%/17% IPS rates |
| Pay period (month/year) | Confirms which minimum-wage floor applies (FY2025 = PYG 2,899,048) |
| Whether the wage includes aguinaldo or family allowance | Those are excluded from the IPS base |
| Employer registration with IPS (REI) | Must be registered before running payroll |

### 8.2 Refusal catalogue — STOP and ask rather than guess

**Refusal catalogue table**

| Situation | Action |
| --- | --- |
| Wage stated in USD or another currency | **Refuse to compute.** Ask for the PYG gross amount (or the FX basis the employer uses). |
| User asks the employer to "withhold income tax (IRP) from the salary" | Do **not** do it. Explain Paraguay does not withhold IRP on dependent salaries — IRP is the employee's annual self-assessment (Section 2). Offer to compute IPS instead. |
| User asks for the employee's exact IRP liability | Compute only on a stated **net taxable income**, label it an estimate, and flag that deductible categories/caps are a research gap (Section 2.4) and that the PYG 80M registration threshold applies. |
| Pay period in 2026 or later | Flag that the FY2025 minimum wage applies until the (unconfirmed) July-2026 adjustment; do not invent a 2026 figure. |
| Financial-sector employer not confirmed | Confirm the sector; do not silently apply 11%/17% to a commercial employer or vice versa. |
| Request for exact IPS late-payment surcharge amount | State the reported 1%–50% range and flag it as a research gap (Section 4.4) — do not present a precise figure as confirmed. |
| Self-employed / sole trader, not an employee | Out of scope for employer payroll — direct to the IRP self-assessment / income-tax skill. |

## Section 9 -- Worked Examples

All figures in PYG, tax year 2025, **commercial sector** unless stated. IPS base = full gross (no aguinaldo/family allowance), floored at the minimum wage (PYG 2,899,048), **no ceiling** applied. **No IRP is withheld by the employer** in any example. Each line is recomputed end-to-end.

### Example A — Minimum wage, gross PYG 2,899,048/month (floor edge)

**Example A table**

| Line | Computation | Amount (PYG) |
| --- | --- | --- |
| Gross | — | 2,899,048.00 |
| IPS base | = minimum-wage floor | 2,899,048.00 |
| Employee IPS | 9.0% × 2,899,048 | 260,914.32 |
| IRP withheld | none — self-assessed | 0.00 |
| **Net pay** | 2,899,048 − 260,914.32 | **2,638,133.68** |
| Employer IPS | 16.5% × 2,899,048 | 478,342.92 |
| **Total employer cost** | 2,899,048 + 478,342.92 | **3,377,390.92** |

### Example B — Gross PYG 5,000,000/month (typical mid salary)

**Example B table**

| Line | Computation | Amount (PYG) |
| --- | --- | --- |
| Gross | — | 5,000,000.00 |
| IPS base | 5,000,000 ≥ floor | 5,000,000.00 |
| Employee IPS | 9.0% × 5,000,000 | 450,000.00 |
| IRP withheld | none — self-assessed | 0.00 |
| **Net pay** | 5,000,000 − 450,000 | **4,550,000.00** |
| Employer IPS | 16.5% × 5,000,000 | 825,000.00 |
| **Total employer cost** | 5,000,000 + 825,000 | **5,825,000.00** |

### Example C — Gross PYG 8,000,000/month (higher salary; annualised crosses IRP threshold)

Annualised gross = 8,000,000 × 12 = 96,000,000 > PYG 80,000,000 → the **employee** must register and self-assess IRP (Section 2.2). The **employer still withholds no IRP** — only IPS.

**Example C table**

| Line | Computation | Amount (PYG) |
| --- | --- | --- |
| Gross | — | 8,000,000.00 |
| IPS base | 8,000,000 ≥ floor | 8,000,000.00 |
| Employee IPS | 9.0% × 8,000,000 | 720,000.00 |
| IRP withheld | none — employee self-assesses annually | 0.00 |
| **Net pay** | 8,000,000 − 720,000 | **7,280,000.00** |
| Employer IPS | 16.5% × 8,000,000 | 1,320,000.00 |
| **Total employer cost** | 8,000,000 + 1,320,000 | **9,320,000.00** |

### Example D — Financial sector, gross PYG 12,000,000/month (11% / 17%)

**Example D table**

| Line | Computation | Amount (PYG) |
| --- | --- | --- |
| Gross | — | 12,000,000.00 |
| IPS base | 12,000,000 ≥ floor | 12,000,000.00 |
| Employee IPS | 11% × 12,000,000 | 1,320,000.00 |
| IRP withheld | none — self-assessed | 0.00 |
| **Net pay** | 12,000,000 − 1,320,000 | **10,680,000.00** |
| Employer IPS | 17% × 12,000,000 | 2,040,000.00 |
| **Total employer cost** | 12,000,000 + 2,040,000 | **14,040,000.00** |

### Example E — Aguinaldo (13th salary), employee on PYG 5,000,000/month all year

Total remuneration in the calendar year = 5,000,000 × 12 = 60,000,000. Aguinaldo = 1/12 × 60,000,000.

> The aguinaldo is paid in full (no IPS, no IRP, unembargable) before 31 December (Section 6).

**Example E table**

| Line | Computation | Amount (PYG) |
| --- | --- | --- |
| Annual remuneration | 5,000,000 × 12 | 60,000,000.00 |
| Aguinaldo | 1/12 × 60,000,000 | 5,000,000.00 |
| IPS on aguinaldo | exempt | 0.00 |
| IRP on aguinaldo | exempt | 0.00 |
| **Aguinaldo paid (net)** | no deductions | **5,000,000.00** |

### Example F — IRP illustration (employee self-assessment, NOT payroll)

Reference only — the employer does not compute this. Employee with **net taxable income** of PYG 200,000,000 (after confirmed deductions — see the Section 2.4 research gap).

**Cumulative check:** matches Section 2.3 (18,000,000 at 200,000,000 net). (Self-verified.) Filed by the individual on Form 515 via Marangatú in March.

**Example F table**

| Band | Computation | Tax (PYG) |
| --- | --- | --- |
| Up to 50,000,000 @ 8% | 0.08 × 50,000,000 | 4,000,000.00 |
| 50,000,001–150,000,000 @ 9% | 0.09 × 100,000,000 | 9,000,000.00 |
| 150,000,001–200,000,000 @ 10% | 0.10 × 50,000,000 | 5,000,000.00 |
| **Total IRP** | 4,000,000 + 9,000,000 + 5,000,000 | **18,000,000.00** |

## Section 10 -- Tier 1 Rules (deterministic — apply mechanically)

- **Tier 1 rules list** — 1. The employer does NOT withhold IRP from dependent salaries — IRP is the employee's annual self-assessment (Ley N° 6380/2019; DNIT). 2. Commercial-sector IPS: employee 9.0%, employer 16.5%, combined 25.5% (PwC; IPS). 3. Financial-sector IPS: employee 11%, employer 17%, combined 28% (PwC). 4. IPS base = every cash/in-kind wage item EXCEPT aguinaldo and family allowance (PwC). 5. IPS contribution base cannot fall below the minimum wage (PYG 2,899,048 in FY2025) (PwC; MTESS). 6. No confirmed IPS salary ceiling — treat as uncapped, flag as a research gap (Section 3). 7. It is illegal to deduct more than the 9% employee share from the worker's pay; the 16.5% employer share is paid from employer funds (MTESS). 8. IRP applies only where the individual's gross personal-service income exceeds PYG 80,000,000/year (DNIT; PwC). 9. IRP rates on net taxable income: 8% up to 50,000,000; 9% on 50,000,001–150,000,000; 10% above 150,000,000 (PwC; DNIT). 10. Aguinaldo = 1/12 of annual remuneration, payable before 31 December, exempt from both IPS and IRP (Ley N° 417/73). 11. Minimum wage = PYG 2,899,048/month from 1 July 2025 (MTESS Res. 677/2025). 12. Monthly IPS planilla filed and paid via REI per the IPS "Calendario de Pago"; Mora Patronal arises the day after the due date (IPS; Vouga). 13. IRP Form 515 filed by the individual via Marangatú annually in March, keyed to the RUC ending digit (DNIT). 14. All payroll amounts in PYG (Guaraní) — never another currency.

## Section 11 -- Tier 2 Catalogue (reviewer judgement required)

These items require a licensed Paraguayan accountant's judgement and/or confirmation against primary sources before reliance.

1. IRP itemized deductions / caps (Section 2.4) — governed by Decreto N° 3184/2019; exact deductible categories and caps not quoted from a figure-level source. Confirm before computing any employee's net taxable income.
2. IPS contribution ceiling (Section 3) — no salary cap confirmed; PwC reports none specified. Confirm whether IPS is truly uncapped.
3. Exact IPS late-payment surcharge schedule (Section 4.4) — the 1%–50% range comes from secondary aggregators, not the IPS resolution. Confirm the exact recargos moratorios schedule.
4. 2026 figures (Section 5) — the July-2026 minimum-wage adjustment and any IRP changes are under negotiation and NOT officially confirmed. Do not apply 2026 figures until published.
5. IRP rate break-point (Section 2.3) — one secondary summary cited a "9% at PYG 100M" break-point; this skill uses the authoritative PwC/DNIT 50M/150M thresholds. Confirm against current DNIT guidance.
6. In-kind wage valuation for the IPS base — confirm how in-kind remuneration is valued for contribution purposes.

### 12.1 Monthly — IPS planilla de aporte obrero-patronal

**Monthly filing table**  _(IPS portal; Vouga)_

| Form | Purpose | Deadline | Source |
| --- | --- | --- | --- |
| Monthly contribution payroll ("planilla de aporte obrero-patronal") | Declare and pay the employee (9%) + employer (16.5%) IPS contributions, filed via the **REI** system | Per the IPS **"Calendario de Pago"** (Resolución C.A. N° 066/2022); Mora Patronal arises the day after the due date | IPS portal; Vouga |

### 12.2 Annual — IRP (the employee's own filing, NOT the employer's)

**Annual filing table**  _(DNIT — IRP portal; Instructivo Form 515)_

| Form | Purpose | Deadline | Source |
| --- | --- | --- | --- |
| **Formulario 515** — Declaración Jurada IRP Rentas de Servicios Personales | The individual's annual self-assessment of IRP (only if gross personal-service income > PYG 80M/year) | Annually in **March**, per the "calendario perpetuo" keyed to the RUC ending digit | DNIT — IRP portal; Instructivo Form 515 |

**IRP filing triggers** (the employee's obligation, not the employer's): gross personal-service income exceeding **PYG 80,000,000/year** (DNIT; PwC). The employer's only IRP role is to issue the payslip/income certificate the employee uses for Form 515.

## Section 13 -- Thresholds Reference Table

**Thresholds Reference Table**

| Threshold | Value | Source |
| --- | --- | --- |
| IPS employee rate (commercial) | 9.0% of gross | PwC; IPS |
| IPS employer rate (commercial) | 16.5% of gross | PwC; IPS |
| IPS combined (commercial) | 25.5% | PwC |
| IPS employee / employer (financial) | 11% / 17% | PwC |
| IPS base floor | Minimum wage (PYG 2,899,048 in FY2025) | PwC; MTESS |
| IPS ceiling | None confirmed — **[RESEARCH GAP — reviewer to confirm]** | PwC (reports none) |
| IRP registration/filing threshold | Gross personal-service income > PYG 80,000,000/year | DNIT; PwC |
| IRP rate band 1 | 8% on net taxable income up to 50,000,000 | PwC; DNIT |
| IRP rate band 2 | 9% on net taxable income 50,000,001–150,000,000 | PwC; DNIT |
| IRP rate band 3 | 10% on net taxable income above 150,000,000 | PwC; DNIT |
| Minimum wage (from 1 Jul 2025) | PYG 2,899,048/month | MTESS Resolución N° 677/2025 |
| Aguinaldo | 1/12 of annual remuneration; before 31 Dec; IPS & IRP exempt | Ley N° 417/73 |
| IPS administrative component | 1% (post Ley N° 7446/2024) | Ley N° 7446/2024 |
| IRP filing deadline | March (per RUC ending digit) | DNIT |

**Sanity check:** IRP bands 50M < 150M (ordered) ✓; IPS combined 25.5% (commercial) and 28% (financial) are plausible payroll percentages ✓; minimum-wage floor is a positive amount ✓. No confirmed ceiling, so the floor-≤-ceiling check is N/A and flagged as a research gap. (Self-verified.)

## Section 14 -- Penalties

**Penalties table**

| Penalty | Detail | Source |
| --- | --- | --- |
| IPS Mora Patronal (employer default) | Arises the day after the contribution due date | IPS; Vouga |
| IPS late-payment surcharges (recargos moratorios) | Reported **1% up to 50%** depending on months of delay, plus interest — **[RESEARCH GAP — reviewer to confirm]** (secondary aggregators; confirm against the IPS resolution) | worki360/Deel (secondary) |
| Over-deduction from worker's pay | Deducting more than the 9% employee share is a misappropriation offence | MTESS |
| IRP late filing/payment | Administrative penalties apply to the individual taxpayer — **[RESEARCH GAP — reviewer to confirm]** exact figures not quoted from a primary source | DNIT |

## Section 15 -- Excel Working Paper Template

**Excel working paper template**

| Row | Label | Formula / source |
| --- | --- | --- |
| 1 | Employee name | input |
| 2 | Pay period (month/year) | input |
| 3 | Sector (C = commercial / F = financial) | input |
| 4 | **Gross wage (cash + in kind, excl. aguinaldo/family allowance)** | input |
| 5 | Minimum-wage floor | `2899048` (FY2025) |
| 6 | IPS base | `=MAX(B4,B5)` (floor; no ceiling) |
| 7 | Employee IPS rate | `=IF(B3="F",0.11,0.09)` |
| 8 | **Employee IPS** | `=B6*B7` |
| 9 | IRP withheld | `=0` (employer never withholds IRP) |
| 10 | **Net pay** | `=B4-B8-B9` |
| 11 | Employer IPS rate | `=IF(B3="F",0.17,0.165)` |
| 12 | **Employer IPS** | `=B6*B11` |
| 13 | **Total employer cost** | `=B4+B12` |
| 14 | Monthly IPS remittance to IPS | `=B8+B12` (employee + employer shares) |
| 15 | Aguinaldo accrual (memo) | `=B4` per month → 1/12 of annual; IPS & IRP exempt |

Reproduce this layout in a single worksheet (one column per employee, or one row per employee for a register). All cells in PYG. **No IRP row** — the employer does not withhold IRP.

**Cross-check against Example B (commercial, gross 5,000,000):** row 6 = 5,000,000; row 8 = 5,000,000 × 0.09 = 450,000; row 10 = 5,000,000 − 450,000 = 4,550,000; row 12 = 5,000,000 × 0.165 = 825,000; row 13 = 5,825,000; row 14 = 450,000 + 825,000 = 1,275,000. ✓ Matches Example B exactly.

## Section 16 -- Bank Statement / Terminology Reading Guide

Common Paraguayan payroll terms (Spanish → English) and typical bank-statement patterns. Match on the **uppercased** description.

### 16.1 Salary credits (to employees)

**Salary credits table**

| Pattern (PYG bank statement) | Classification |
| --- | --- |
| `SUELDO`, `SALARIO`, `PAGO DE SUELDO`, `HABERES` | Net salary payment |
| `PAGO NOMINA`, `PLANILLA DE SUELDOS`, `TRANSFERENCIA SUELDO` | Net salary payment |
| `AGUINALDO`, `13ER SUELDO`, `DECIMO TERCER` | Aguinaldo (13th salary, IPS & IRP exempt) |
| `ANTICIPO`, `ADELANTO DE SUELDO` | Salary advance — reconcile against month-end net |
| `BONIFICACION`, `GRATIFICACION` | Bonus — wage item (review IPS-base inclusion) |

### 16.2 Employer debits to the State (IPS / DNIT)

**Employer debits table**

| Pattern | Classification |
| --- | --- |
| `IPS`, `INSTITUTO DE PREVISION SOCIAL`, `APORTE OBRERO PATRONAL` | IPS contribution (employee + employer shares remitted together) |
| `APORTE PATRONAL`, `APORTE OBRERO` | IPS contribution share |
| `PLANILLA IPS`, `REI` | Monthly IPS payroll-list payment |
| `DNIT`, `IRP`, `MARANGATU` | DNIT / IRP payment (normally the individual's own IRP, not employer payroll) |

### 16.3 Non-payroll / not income

**Non-payroll table**

| Pattern | Classification |
| --- | --- |
| `REEMBOLSO`, `REINTEGRO` | Reimbursement / refund — not salary |
| `VIATICOS`, `GASTOS DE VIAJE` | Travel allowance/expense — review for treatment |
| `CUOTA PRESTAMO`, `DESCUENTO PRESTAMO` | Loan deduction — not an employer cost |

## Section 17 -- Onboarding Fallback

If the user has not provided enough to run payroll, collect in this order:
1. Monthly gross wage in PYG (cash + in kind) — refuse if given in USD or another currency (Section 8.2).
2. Employer sector — commercial (9%/16.5%) or financial (11%/17%).
3. Pay period (month + year) — confirm FY2025 minimum wage (PYG 2,899,048).
4. Whether the wage includes aguinaldo or family allowance (excluded from the IPS base).
5. Confirm the employer is registered with IPS (REI).
6. Clarify if the user is asking about the employee's IRP self-assessment (annual, individual) rather than employer payroll — the employer does not withhold IRP.

If any required input is missing, state what is missing and do not fabricate a figure.

## Section 18 -- Interaction with Other Skills

**Interaction with other skills table**

| Scenario | Skill to Use |
| --- | --- |
| Employee payroll (IPS contributions) | **This skill (paraguay-payroll.md)** |
| Individual IRP self-assessment (Form 515) | paraguay-income-tax.md (employee's own annual filing) |
| Paraguay VAT (IVA) returns | paraguay-vat-return.md |
| Paraguay corporate income tax (IRE) | paraguay-corporate-tax.md |
| Paraguay bookkeeping | paraguay-bookkeeping.md |

### Key handoff points

- **Payroll → Bookkeeping:** gross wages and the 16.5% employer IPS are expenses; the 9% employee IPS withheld is a liability until remitted via REI. There is **no IRP withholding liability** on salaries.
- **Payroll → IRP:** the employer issues the payslip/income certificate; the employee uses it for their own Form 515 (only if gross personal-service income > PYG 80M/year). The two are separate filings.

### 19.1 Sources

**Sources table**

| # | Title | Publisher | URL |
| --- | --- | --- | --- |
| 1 | Paraguay — Individual — Taxes on personal income (IRP) | PwC Worldwide Tax Summaries | https://taxsummaries.pwc.com/paraguay/individual/taxes-on-personal-income |
| 2 | Paraguay — Individual — Other taxes (IPS social security) | PwC Worldwide Tax Summaries | https://taxsummaries.pwc.com/paraguay/individual/other-taxes |
| 3 | IRP — Impuesto a la Renta Personal (institutional portal) | DNIT | https://www.dnit.gov.py/en/web/portal-institucional/irp |
| 4 | IRP Cartilla (al 30.07.24) | DNIT | https://www.dnit.gov.py/documents/20123/233435/IRP+Cartilla+al+30.07.24.pdf |
| 5 | Instructivo del Formulario N° 515 (IRP RSP) | DNIT | https://www.dnit.gov.py/documents/47797/47809/ |
| 6 | IPS — contribución obrero-patronal | Instituto de Previsión Social (IPS) | https://portal.ips.gov.py/sistemas/ipsportal/contenido.php?c=315 |
| 7 | REI — Registro del Empleador por Internet | IPS | https://portal.ips.gov.py/sistemas/ipsportal/contenido.php?e=12 |
| 8 | Resolución MTESS N° 677/2025 — salario mínimo (1 Jul 2025) | MTESS | https://www.mtess.gov.py/?p=30682 |
| 9 | El MTESS reglamenta los nuevos salarios mínimos | Vouga Abogados | https://www.vouga.com.py/en/el-mtess-reglamenta-los-nuevos-salarios-minimos/ |
| 10 | El IPS estableció nuevos criterios (Calendario de Pago / Mora Patronal) | Vouga Abogados | https://www.vouga.com.py/en/el-instituto-de-prevision-social-ips-establecio-nuevos-criterios/ |
| 11 | Ley N° 417/73 (aguinaldo) | BACN | https://www.bacn.gov.py/leyes-paraguayas/2518/ |

### 19.2 Test Suite (numbered — recompute to confirm any change)

**Test suite table**

| # | Input | Expected output | Recomputation |
| --- | --- | --- | --- |
| 1 | Commercial, gross 2,899,048 (min wage) | Net 2,638,133.68; employer cost 3,377,390.92 | Ex. A — employee IPS 9% × 2,899,048 = 260,914.32; employer 16.5% = 478,342.92 |
| 2 | Commercial, gross 5,000,000 | Net 4,550,000; employer cost 5,825,000 | Ex. B — employee IPS 450,000; employer 825,000 |
| 3 | Commercial, gross 8,000,000 | Net 7,280,000; employer cost 9,320,000; employee must self-assess IRP (annual 96M > 80M) | Ex. C — employee IPS 720,000; employer 1,320,000; no IRP withheld |
| 4 | Financial, gross 12,000,000 | Net 10,680,000; employer cost 14,040,000 | Ex. D — 11% = 1,320,000; 17% = 2,040,000 |
| 5 | Aguinaldo, 5,000,000/month all year | Aguinaldo 5,000,000 paid in full; IPS 0; IRP 0 | Ex. E — 1/12 × 60,000,000; both exempt |
| 6 | IRP on net taxable 200,000,000 (employee filing) | IRP 18,000,000 | Ex. F — 8%×50M + 9%×100M + 10%×50M = 4M + 9M + 5M |
| 7 | Any salary, employer IRP withholding | 0 — employer never withholds IRP on dependent salaries | Section 2.1 |
| 8 | IPS rate totals | Commercial 25.5%; financial 28% | Section 4.2 — both additions reconcile |
| 9 | Monthly IPS remittance, commercial gross 5,000,000 | 450,000 + 825,000 = 1,275,000 to IPS | Template row 14 |
| 10 | Deadlines | IPS monthly per Calendario de Pago; IRP Form 515 in March | Section 12 |

## PROHIBITIONS

- NEVER withhold IRP from a dependent salary — Paraguay does not withhold income tax on employee wages; IRP is the employee's annual self-assessment (Form 515).
- NEVER compute Paraguayan payroll in USD or any non-PYG currency — refuse and ask for the PYG gross.
- NEVER apply commercial IPS rates (9%/16.5%) to a financial-sector employer, or financial rates (11%/17%) to a commercial employer, without confirming the sector.
- NEVER include the aguinaldo or family allowance in the IPS contribution base.
- NEVER apply IPS contributions to the aguinaldo, and never deduct IPS or IRP from it — it is exempt and unembargable.
- NEVER deduct more than the 9% employee IPS share from the worker's pay — the 16.5% employer share is paid from employer funds (misappropriation offence otherwise).
- NEVER compute the IPS base below the minimum-wage floor (PYG 2,899,048 in FY2025).
- NEVER assert an IPS salary ceiling as confirmed — none is confirmed (research gap); treat IPS as uncapped.
- NEVER state exact IPS late-payment surcharges or IRP penalty amounts as confirmed — they are research gaps pending primary-source confirmation.
- NEVER quote IRP deduction figures/caps as confirmed — the deductible categories are a research gap pending Decreto N° 3184/2019 confirmation.
- NEVER apply an unconfirmed 2026 minimum wage — use the FY2025 figure until the July-2026 adjustment is published.
- NEVER present payroll computations as definitive — label them estimated and direct the user to a licensed Paraguayan accountant.

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a licensed accountant in Paraguay) before implementation. This is a Tier 2 (research-verified) skill: figures are sourced to named authorities (DNIT, IPS, MTESS) and Big-4 summaries but have not yet been verified section-by-section by a licensed Paraguayan accountant, and items marked "[RESEARCH GAP — reviewer to confirm]" carry residual uncertainty.

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
