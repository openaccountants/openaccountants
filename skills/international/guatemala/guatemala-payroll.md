---
name: guatemala-payroll
description: Use this skill whenever asked about Guatemala payroll processing for employed persons. Trigger on phrases like "Guatemala payroll", "nómina Guatemala", "ISR Guatemala", "retención ISR", "rentas del trabajo en relación de dependencia", "cuota laboral IGSS", "cuota patronal", "IGSS contribution", "INTECAP", "IRTRA", "bonificación incentivo", "bono 14", "aguinaldo", "salario mínimo Guatemala", "net salary Guatemala", "salario neto", "PAYE Guatemala", "tax withholding Guatemala", "employer contributions Guatemala", "RetenISR", "constancia de retención", "SAT Guatemala", "gross to net Guatemala", "GTQ payroll", "quetzal salary", or any question about computing employee pay, withholding income tax (ISR), or mandatory social-security contributions for Guatemala-based employees. This skill covers ISR withholding on employment income (Decreto 10-2012), employee and employer IGSS/INTECAP/IRTRA contributions, the standard personal deduction and IVA credit, statutory bonuses (bonificación incentivo, aguinaldo, Bono 14), minimum wage by economic circumscription, non-resident withholding, and SAT/IGSS filing obligations. ALWAYS read this skill before processing any Guatemala payroll.
version: 0.1
jurisdiction: GT
tax_year: 2026
last_updated: 2026-07-13
review_status: pending_review
depends_on: - payroll-workflow-base
category: payroll
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Guatemala Payroll

## Guatemala Payroll Skill v0.1

**Tier 2 — research-verified. Figures below are sourced from the Guatemalan Tax Administration (Superintendencia de Administración Tributaria, SAT), the Guatemalan Social Security Institute (Instituto Guatemalteco de Seguridad Social, IGSS), the Ley de Actualización Tributaria (Decreto 10-2012), the Código Tributario (Decreto 6-91), labour decrees (78-89, 76-78, 42-92), PwC Worldwide Tax Summaries, EY, Deloitte, Baker Tilly Guatemala, and the official gazette (Diario de Centro América). NOT yet signed off by a licensed Guatemalan accountant (Contador Público y Auditor) or tax adviser. Treat every computation as an estimate pending professional review.**

## Section 1 -- Quick Reference

**Quick Reference table**

| Field | Value |
| --- | --- |
| Country | Guatemala (Republic of Guatemala / República de Guatemala) |
| Currency | Guatemalan Quetzal (GTQ / Q) only |
| Standard pay frequency | Monthly (quincenal — twice monthly — also common) |
| Tax year | Calendar year (1 January -- 31 December) (PwC) |
| Income tax (ISR) withholding system | Monthly withholding by the employer on projected annual income, divided by 12; annual final settlement (liquidación) in December (Decreto 10-2012; oficsa) |
| Income tax authority | Superintendencia de Administración Tributaria (SAT) |
| Social security authority | Instituto Guatemalteco de Seguridad Social (IGSS) |
| Training levy authority | Instituto Técnico de Capacitación y Productividad (INTECAP) |
| Recreation levy authority | Instituto de Recreación de los Trabajadores (IRTRA) |
| Key legislation | Ley de Actualización Tributaria (Decreto 10-2012); Código Tributario (Decreto 6-91); Bonificación Incentivo (Decreto 78-89); Aguinaldo (Decreto 76-78); Bono 14 (Decreto 42-92) |
| Filing portal | SAT — Agencia Virtual / RetenISR (Sistema de Retenciones Web -ISR-) (portal.sat.gob.gt) |
| Validated by | Pending -- requires sign-off by a licensed Guatemalan Contador Público y Auditor / tax adviser |
| Skill version | 0.1 |

**Read this whole section before computing anything. The shared payroll runbook lives in `payroll-workflow-base` — follow that runbook with this skill supplying the Guatemala-specific content.**

### The single most important Guatemala facts

- **ISR on employment income** — Guatemala DOES have a personal income tax (ISR) on employment income, withheld at source by the employer under Decreto 10-2012. It is mildly progressive: 5% on the first Q300,000 of annual taxable income and Q15,000 + 7% on the excess.  _(PwC; Decreto 10-2012)_
- **Q250 bonificación incentivo non-salary** — The Q250/month bonificación incentivo (Decreto 78-89) is non-salary by law. It is excluded from the IGSS contribution base and from benefit calculations. Its ISR treatment is flagged as Tier-2.  _(misalario; copades)_

## Section 2 -- Income Tax Withholding (ISR — Rentas del Trabajo)

The employer withholds ISR on "rentas del trabajo en relación de dependencia". The standard method: project the employee's annual income, compute annual ISR, divide by 12, and withhold monthly; the year-end final settlement (liquidación) in December applies the full deduction set. (Decreto 10-2012; oficsa)

### ISR Brackets — Resident Employment Income (2025 and 2026)

**ISR Brackets table**  _(PwC — taxes on personal income; Decreto 10-2012; Prensa Libre citing SAT)_

| Annual taxable income (renta imponible) | Marginal rate | Tax formula |
| --- | --- | --- |
| Q0.01 – Q300,000.00 | 5% | 5% × taxable income |
| Over Q300,000.00 | 7% on the excess | Q15,000 fixed + 7% × (taxable income − 300,000) |

(PwC — taxes on personal income; Decreto 10-2012; Prensa Libre citing SAT) The fixed Q15,000 = 5% × Q300,000 (verify: 0.05 × 300,000 = 15,000 ✓), so the schedule is continuous at the Q300,000 boundary. These rates are set in Decreto 10-2012 and have **not** changed for 2025/2026.

### Deductions in Computing Annual Taxable Income

**Deductions table**  _(PwC)_

| Deduction | Amount (annual) | Notes / source |
| --- | --- | --- |
| Personal expenses (sin comprobación) | Q48,000.00 | Standard, no receipts required (PwC — deductions; Prensa Libre) |
| IVA (VAT) credit on personal expenses | Up to Q12,000.00 | Must be backed by tax invoices (facturas) (PwC; Prensa Libre) |
| IGSS employee contributions (cuota laboral) | Actual paid (4.83% of salary base) | Deductible (PwC — deductions) |
| Donations | Restricted (commonly up to 5% of net income) | (PwC) **[T2 — confirm exact cap and base]** |
| Life insurance premiums | Deductible | (PwC) **[T2 — confirm conditions/limits]** |

> The Q48,000 + Q12,000 = the commonly cited **Q60,000 combined base deduction floor**. (Prensa Libre; PwC) Practical effect: an employee earning **≤ ~Q4,000/month (≈Q48,000/yr salary)** effectively pays no ISR after the standard personal deduction alone.

### 2026 reform — Decreto 13-2026

> **[RESEARCH GAP — reviewer to confirm before relying on it]** Decreto 13-2026 (reported approved by Congress 28 April 2026) is stated to (a) exempt minimum-wage earners from ISR withholding and (b) add an **extra deduction of Q3,024** on top of the Q60,000 already established by Decreto 10-2012. (guatemala.com; Congreso de la República) The Q3,024 figure and its effective tax year must be re-verified against the final published decree text. The worked examples below do NOT apply the Q3,024 extra deduction pending that confirmation.

### Non-Resident Employment Income

**Non-resident withholding table**  _(Art. 104 num. 3, Decreto 10-2012 (Baker Tilly Guatemala))_

| Income type | Withholding | Basis | Mechanics |
| --- | --- | --- | --- |
| Salaries, wages, per diems, bonuses, other remuneration to non-residents | **15% flat (definitive)** | Applied to **gross**, no deductions | Art. 104 num. 3, Decreto 10-2012 (Baker Tilly Guatemala) |

- **Non-resident remittance timing** — The withholding agent remits via sworn declaration within the first 10 business days of the month following payment and must issue a withholding certificate (constancia).  _(Baker Tilly Guatemala)_

### Monthly Withholding Method (resident)

- **Deterministic withholding order** — 1. Start with annual projected gross salary (12 ordinary monthly salaries; add Bono 14 and aguinaldo if treated as taxable — see Tier-2 note). 2. Subtract the Q48,000 standard personal deduction. 3. Subtract the IVA credit of up to Q12,000 (only if backed by facturas; default to Q0 if unconfirmed). 4. Subtract the actual IGSS employee contributions (4.83% of the salary base). 5. Subtract any confirmed donations / life-insurance premiums (default Q0). 6. The result is the annual taxable income (renta imponible). 7. Apply the bracket schedule → annual ISR. 8. Divide annual ISR by 12 → monthly ISR withholding. 9. At the December final settlement (liquidación), reconcile against amounts already withheld.  _(Decreto 10-2012; oficsa; PwC)_

## Section 3 -- Contributions: Employee Deductions (IGSS cuota laboral)

The employee pays a single mandatory social-security deduction: the IGSS cuota laboral, withheld from the salary base. There is no separate employee INTECAP or IRTRA deduction (those are employer-only).

**Employee contribution table**  _(IGSS)_

| Contribution | Rate | Payer | Authority | Base | Source |
| --- | --- | --- | --- | --- | --- |
| IGSS (cuota laboral) | 4.83% | Employee (withheld) | IGSS | Ordinary + extraordinary salary, **excluding** the Q250 bonificación incentivo | PwC — other taxes |
| **Total employee contribution** | **4.83%** | Employee (withheld) | — | — | (single line — no other employee levy) |

- **Contribution base** — The contribution base is the base salary = ordinary + extraordinary wages, generally excluding the Q250 bonificación incentivo (non-salary by Decreto 78-89).  _(misalario; copades)_
- **No IGSS ceiling or floor** — No IGSS contribution ceiling or floor was found in any authoritative source — IGSS contributions apply to the full ordinary + extraordinary salary with no cap. **[T2 — confirm there is no salary cap against current IGSS regulations.]**  _(PwC; IGSS)_

## Section 4 -- Contributions: Employer Contributions (IGSS / INTECAP / IRTRA)

The employer pays a cuota patronal that bundles three levies on the same salary base (ordinary + extraordinary, excluding the Q250 bonificación incentivo).

**Employer contribution table**  _(PwC)_

| Contribution | Rate | Authority | Source |
| --- | --- | --- | --- |
| IGSS (cuota patronal) | 10.67% | IGSS | IGSS (official); PwC |
| INTECAP | 1.00% | INTECAP | copades; misalario |
| IRTRA | 1.00% | IRTRA | copades; misalario |
| **Total employer contribution** | **12.67%** | — | verify: 10.67 + 1.00 + 1.00 = 12.67 ✓ (PwC) |

**Combined employee + employer social-security wedge**  _(PwC; IGSS)_

| Component | Employee | Employer | Combined |
| --- | --- | --- | --- |
| IGSS | 4.83% | 10.67% | 15.50% |
| INTECAP | — | 1.00% | 1.00% |
| IRTRA | — | 1.00% | 1.00% |
| **Total** | **4.83%** | **12.67%** | **17.50%** |

> Verify the totals: employee column 4.83% ✓; employer column 10.67 + 1.00 + 1.00 = 12.67% ✓; combined 4.83 + 12.67 = 17.50% ✓; IGSS-only combined 4.83 + 10.67 = 15.50% ✓. (PwC; IGSS)

- **Tax treatment of employer IGSS contribution** — The employer IGSS contribution is "renta no imponible" (non-taxable income) for ISR purposes. The levies sit on top of salary as an employer cost — they are never deducted from the employee.  _(IGSS)_

### Employer Registration with IGSS

**Registration table**  _(Prensa Libre; IGSS; EY)_

| Aspect | Rule | Source |
| --- | --- | --- |
| Registration threshold | **1 worker** (lowered from 3), mandatory since **17 January 2023** (Reglamento de Inscripción, Acuerdo JD 1529) | Prensa Libre; IGSS; EY |
| Deadline | Within **30 business days** of the obligation arising; later filing is "extemporánea" (late) | IGSS; Prensa Libre |

## Section 5 -- Minimum Wage and Working Hours

Guatemala uses two economic circumscriptions: CE1 = Department of Guatemala; CE2 = all other departments. All figures are monthly base plus the mandatory Q250 bonificación incentivo on top.

### 2026 — Acuerdo Gubernativo 256-2025 (published 22 Dec 2025, effective 1 Jan 2026)

**CE1 (Department of Guatemala)**  _(EY tax alert — salario mínimo 2026; Diario de Centro América)_

| Sector | Monthly base (Q) | + Incentivo (Q) | Total (Q) |
| --- | --- | --- | --- |
| Agricultural | 3,791.20 | 250.00 | 4,041.20 |
| Non-agricultural | 4,002.28 | 250.00 | 4,252.28 |
| Export / Maquila | 3,409.73 | 250.00 | 3,659.73 |

**CE2 (other departments)**  _(EY tax alert — salario mínimo 2026; Diario de Centro América)_

| Sector | Monthly base (Q) | + Incentivo (Q) | Total (Q) |
| --- | --- | --- | --- |
| Agricultural | 3,625.89 | 250.00 | 3,875.89 |
| Non-agricultural | 3,816.90 | 250.00 | 4,066.90 |
| Export / Maquila | 3,221.10 | 250.00 | 3,471.10 |

(EY tax alert — salario mínimo 2026; Diario de Centro América) Verify a sample total: 4,002.28 + 250.00 = 4,252.28 ✓.

### 2025 — Acuerdo Gubernativo 264-2024 (published 27 Dec 2024, effective 1 Jan 2025)

**2025 minimum wage table**  _(guatemala.com; ONSEC table)_

| Sector | Reported figure | Source |
| --- | --- | --- |
| Agricultural & Non-agricultural (CE1) | ≈ Q122.40/day ≈ Q3,723/month | guatemala.com; ONSEC table |
| Export / Maquila (CE1) | ≈ Q107.79/day ≈ Q3,278/month | guatemala.com; ONSEC table |

> **[RESEARCH GAP — reviewer to confirm]** The 2025 source consolidated the agrícola / no-agrícola split for CE1 and did not give a clean per-sector / per-circumscription breakdown. For precise 2025 per-sector figures consult the official ONSEC table. The 2025 increase was +10% (agrícola & no agrícola) and +6% (exportadora / maquila).

### Working Hours and Overtime

> **[RESEARCH GAP — reviewer to confirm]** Statutory overtime multipliers, maximum daily/weekly hours, and night/Sunday/holiday premiums under the Código de Trabajo were not part of this research dataset. A reviewer should populate these from the Código de Trabajo before relying on overtime figures.

## Section 6 -- Mandatory Statutory Bonuses

**Statutory bonuses table**  _(misalario; copades; Mintrabajo)_

| Bonus | Law | Amount | Payment timing | Source |
| --- | --- | --- | --- | --- |
| **Bonificación Incentivo** | Decreto 78-89 | **Q250/month**, fixed, all private-sector workers | Monthly, with salary. Excluded from benefit calcs and the IGSS base. | misalario; copades |
| **Aguinaldo** | Decreto 76-78 | One month's salary (pro-rated) | Accrual period 1 Dec–30 Nov; **50% paid in the first 15 days of December**, remainder by **15 January** | Mintrabajo |
| **Bono 14 (Bonificación Anual)** | Decreto 42-92 | One month's salary (pro-rated) | Accrual period 1 Jul–30 Jun; paid no later than **15 July** | Mintrabajo (Bono 14) |

- **Aguinaldo and Bono 14 bases** — Aguinaldo and Bono 14 are computed on separate bases — neither counts toward the other. Both are typically treated as taxable income for ISR; the Q250 bonificación incentivo's ISR treatment is flagged as Tier-2 (T2-3).  _(Decreto 42-92)_

## Section 7 -- Conservative Defaults

**Conservative defaults table**  _(PwC; Prensa Libre)_

| Field | Default | Rationale |
| --- | --- | --- |
| IVA credit (Q12,000) | **Q0 unless facturas are confirmed** | The IVA credit requires invoice backing; absent proof, do not grant it. (PwC; Prensa Libre) |
| Donations / life-insurance deductions | **Q0** | Apply only when confirmed and documented. |
| Decreto 13-2026 Q3,024 extra deduction | **Do NOT apply** | Reform unconfirmed against the final decree text. **[RESEARCH GAP]** |
| Residency | **Resident** (progressive 5% / 7% with deductions) | Apply the 15% non-resident flat rate only when non-residence is confirmed. |
| IGSS base | **Ordinary + extraordinary salary, excluding the Q250 incentivo** | The incentivo is non-salary by Decreto 78-89. |
| IGSS ceiling | **No cap** | No authoritative ceiling found; apply contributions to the full base. **[T2]** |
| Bonificación incentivo (Q250) | **Always add Q250/month on top of base salary** | Mandatory for all private-sector workers (Decreto 78-89). |
| Pay frequency | **Monthly** | Most common; quincenal is a presentation split of the same monthly figures. |
| Employer cost estimate | **Base × 1.1267 (add 12.67% IGSS/INTECAP/IRTRA)** plus Q250 incentivo plus aguinaldo/Bono 14 accrual | Captures the full statutory employer burden. |

## Section 8 -- Required Inputs and Refusal Catalogue

1. **Monthly base salary** (salario base) in GTQ.
2. **Residency status** — resident (progressive ISR) vs non-resident (15% flat definitive).
3. **Economic circumscription and sector** — CE1 vs CE2; agricultural / non-agricultural / export-maquila — to validate against the minimum wage.
4. **IVA credit** — whether up to Q12,000 of personal expenses is backed by facturas (default Q0).
5. **Other deductions** — confirmed donations / life-insurance premiums (default Q0).
6. **Pay period (month and year)** — to pick the correct minimum wage and any reform that has taken effect (2025 vs 2026).
7. Whether **aguinaldo / Bono 14** fall in the period — to include them in taxable income.

### Refusal Catalogue — DO NOT attempt; route to a licensed accountant

**Refusal catalogue table**

| Scenario | Why it is out of scope |
| --- | --- |
| Cross-border / posted workers / totalization (social-security coordination) | Requires treaty / IGSS determination — see `cross-border-payroll-coordination`. |
| Double-tax-treaty relief, expat tax-equalisation, tie-breaker residency | Beyond a domestic payroll run; route to a reviewer. |
| Decreto 13-2026 application (minimum-wage ISR exemption, Q3,024 extra deduction) | Unconfirmed against the final decree. **[RESEARCH GAP]** |
| Benefits in kind / company cars / stock-option valuation | Guatemalan BIK valuation rules were not in this research dataset. **[RESEARCH GAP]** |
| Severance / indemnización por despido taxation | Not in scope; route to a reviewer. |
| Self-employed / professional services ISR regimes | Different regime (rentas de actividades lucrativas) — out of scope for employer payroll. |
| Exact penalty quantification beyond the Section 13 statutory rates | Form numbers and some wording are from secondary sources (SAT portal returned HTTP 403); reviewer to confirm on SAT directly. |

## Section 9 -- Transaction / Payment Pattern Library

Deterministic classification of Guatemalan bank-statement lines for payroll. Match on the uppercased description fragment.

### Salary credits (what lands in the employee's account)

**Salary credits table**

| Bank statement text (ES / EN) | Classification |
| --- | --- |
| `SALARIO`, `SUELDO`, `NOMINA`, `PAGO NOMINA` | Net salary payment |
| `PLANILLA`, `PAYROLL`, `SALARY` | Net salary payment (variant) |
| `ANTICIPO`, `ADELANTO DE SUELDO` | Salary advance (not final pay) |
| `BONIFICACION INCENTIVO`, `BONO INCENTIVO` | Q250 monthly bonificación incentivo (non-salary) |
| `AGUINALDO` | Aguinaldo (Decreto 76-78) — Dec/Jan |
| `BONO 14`, `BONIFICACION ANUAL` | Bono 14 (Decreto 42-92) — by 15 July |
| `DEVOLUCION ISR`, `REINTEGRO ISR` | ISR refund — NOT income |

### Employer debits (what leaves the employer's account)

**Employer debits table**

| Bank statement text (ES / EN) | Classification |
| --- | --- |
| `SAT`, `RETENCION ISR`, `RETENISR`, `ISR PLANILLA` | ISR remittance to SAT |
| `IGSS`, `CUOTA PATRONAL`, `CUOTA LABORAL` | IGSS contribution remittance (employer + withheld employee cuota) |
| `INTECAP` | INTECAP 1% levy remittance |
| `IRTRA` | IRTRA 1% levy remittance |
| `PAGO PLANILLA`, `NOMINA`, `PAYROLL RUN` | Net wages disbursed to employees |

> ISR is remitted to SAT (via RetenISR); the IGSS cuota laboral (withheld) and cuota patronal, plus INTECAP and IRTRA, are remitted through the IGSS planilla system.

## Section 10 -- Worked Examples

All examples use 2026 figures unless stated. Resident ISR uses the 5% / 7% schedule with the Q48,000 standard personal deduction; the Q12,000 IVA credit defaults to Q0 unless invoices are confirmed (Examples 1–4 assume the IVA credit is unproven → Q0, the conservative default). IGSS employee deduction = 4.83% of base salary; the Q250 bonificación incentivo is added on top of net and is excluded from the IGSS base. Every line below was recomputed end-to-end.

### Example 1 — Standard mid earner, Q8,000/month base salary (CE1 non-agricultural)

Bank statement context: `NOMINA … Q7,482.92` plus `BONIFICACION INCENTIVO … Q250.00` credited to the employee; `IGSS CUOTA PATRONAL … Q853.60`, `INTECAP … Q80.00`, `IRTRA … Q80.00`, `RETENCION ISR … Q130.68` debited from the employer.

**Example 1 computation table**

| Step | Computation | Q |
| --- | --- | --- |
| Annual base salary | 8,000 × 12 | 96,000.00 |
| IGSS employee (4.83% × 96,000) | annual | 4,636.80 |
| Standard personal deduction | — | 48,000.00 |
| IVA credit (unproven → default Q0) | — | 0.00 |
| Annual taxable income | 96,000 − 48,000 − 4,636.80 | 43,363.20 |
| Annual ISR (5%, below Q300,000) | 43,363.20 × 5% | 2,168.16 |
| Monthly ISR | 2,168.16 ÷ 12 | 180.68 |
| Monthly IGSS employee | 4,636.80 ÷ 12 | 386.40 |
| **Net monthly (salary)** | 8,000 − 386.40 − 180.68 | **7,432.92** |
| + Bonificación incentivo | added on top, no deductions | 250.00 |
| **Net monthly received** | 7,432.92 + 250.00 | **7,682.92** |

> If Q12,000 of IVA-backed personal expenses were proven, taxable income would fall to Q31,363.20, annual ISR to Q1,568.16, and monthly ISR to Q130.68 — raising net salary to Q7,482.92 + Q250.00. The Q130.68 figure in the bank-statement context above reflects that fully-deducted scenario; the table reflects the conservative Q0 IVA default.

### Example 2 — Minimum-wage worker (2026 CE1 non-agricultural), Q4,002.28/month base

**Example 2 computation table**

| Step | Computation | Q |
| --- | --- | --- |
| Annual base salary | 4,002.28 × 12 | 48,027.36 |
| IGSS employee (4.83% × 48,027.36) | annual | 2,319.72 |
| Standard personal deduction | — | 48,000.00 |
| Annual taxable income | max(48,027.36 − 48,000 − 2,319.72, 0) | 0.00 |
| Annual ISR | taxable base is 0 | 0.00 |
| Monthly ISR | — | 0.00 |
| Monthly IGSS employee | 2,319.72 ÷ 12 | 193.31 |
| **Net monthly (salary)** | 4,002.28 − 193.31 − 0 | **3,808.97** |
| + Bonificación incentivo | on top | 250.00 |
| **Net monthly received** | 3,808.97 + 250.00 | **4,058.97** |

> The Q48,000 standard personal deduction alone wipes out the ISR base for a minimum-wage worker even before the IVA credit. Decreto 13-2026 would formalise this minimum-wage ISR exemption, but is unconfirmed **[RESEARCH GAP]**.

### Example 3 — High earner, Q40,000/month base salary

**Example 3 computation table**

| Step | Computation | Q |
| --- | --- | --- |
| Annual base salary | 40,000 × 12 | 480,000.00 |
| IGSS employee (4.83% × 480,000) | annual | 23,184.00 |
| Standard personal deduction | — | 48,000.00 |
| IVA credit (proven, max) | — | 12,000.00 |
| Annual taxable income | 480,000 − 48,000 − 12,000 − 23,184 | 396,816.00 |
| ISR — first Q300,000 | fixed | 15,000.00 |
| ISR — excess (7% × (396,816 − 300,000)) | 7% × 96,816 | 6,777.12 |
| Annual ISR | 15,000 + 6,777.12 | 21,777.12 |
| Monthly ISR | 21,777.12 ÷ 12 | 1,814.76 |
| Monthly IGSS employee | 23,184 ÷ 12 | 1,932.00 |
| **Net monthly (salary)** | 40,000 − 1,932.00 − 1,814.76 | **36,253.24** |
| + Bonificación incentivo | on top | 250.00 |
| **Net monthly received** | 36,253.24 + 250.00 | **36,503.24** |

> The 7% rate bites only on annual taxable income above Q300,000. Here Q96,816 sits in the higher band. This example assumes the full Q12,000 IVA credit is invoice-backed.

### Example 4 — Single-bracket upper earner, Q30,000/month base salary

**Example 4 computation table**

| Step | Computation | Q |
| --- | --- | --- |
| Annual base salary | 30,000 × 12 | 360,000.00 |
| IGSS employee (4.83% × 360,000) | annual | 17,388.00 |
| Standard personal deduction | — | 48,000.00 |
| IVA credit (proven, max) | — | 12,000.00 |
| Annual taxable income | 360,000 − 48,000 − 12,000 − 17,388 | 282,612.00 |
| Annual ISR (5%, below Q300,000) | 282,612 × 5% | 14,130.60 |
| Monthly ISR | 14,130.60 ÷ 12 | 1,177.55 |
| Monthly IGSS employee | 17,388 ÷ 12 | 1,449.00 |
| **Net monthly (salary)** | 30,000 − 1,449.00 − 1,177.55 | **27,373.45** |
| + Bonificación incentivo | on top | 250.00 |
| **Net monthly received** | 27,373.45 + 250.00 | **27,623.45** |

> A Q30,000/month base earner with full deductions still lands a taxable income below Q300,000 — entirely in the 5% band. The 7% band only engages once deductions no longer hold taxable income under Q300,000 (roughly above a Q31,500/month base with full deductions).

### Example 5 — Non-resident, Q50,000 gross remuneration

**Example 5 computation table**

| Step | Computation | Q |
| --- | --- | --- |
| Gross remuneration | — | 50,000.00 |
| ISR withholding (15% flat, definitive, no deductions) | 50,000 × 15% | 7,500.00 |
| **Net to non-resident** | 50,000 − 7,500 | **42,500.00** |

> Non-resident employment income is taxed at a 15% definitive flat rate on gross (Art. 104 num. 3, Decreto 10-2012) — no Q48,000/Q12,000 deductions, no progressive schedule. The withholding agent remits within the first 10 business days of the following month and issues a constancia. (Baker Tilly Guatemala) IGSS may still apply if the work is performed in Guatemala **[T2 — confirm IGSS treatment for the specific assignment]**.

### Example 6 — Employer cost for a Q8,000/month employee (CE1 non-agricultural)

**Example 6 computation table**

| Step | Computation | Q |
| --- | --- | --- |
| Monthly base salary | — | 8,000.00 |
| IGSS cuota patronal (10.67% × 8,000) | — | 853.60 |
| INTECAP (1% × 8,000) | — | 80.00 |
| IRTRA (1% × 8,000) | — | 80.00 |
| Total cuota patronal (12.67%) | 853.60 + 80.00 + 80.00 | 1,013.60 |
| Bonificación incentivo (employer-paid, on top) | — | 250.00 |
| Aguinaldo accrual (one month / 12) | 8,000 ÷ 12 | 666.67 |
| Bono 14 accrual (one month / 12) | 8,000 ÷ 12 | 666.67 |
| **Total monthly employer cost** | 8,000 + 1,013.60 + 250.00 + 666.67 + 666.67 | **10,596.94** |

> Verify the cuota patronal: 10.67% + 1% + 1% = 12.67%; 12.67% × 8,000 = 1,013.60 ✓. The IGSS/INTECAP/IRTRA levies are charged on the base salary (excluding the Q250 incentivo). Aguinaldo and Bono 14 each accrue one month's salary per year (≈Q666.67/month each on a Q8,000 base) and should be provisioned monthly even though paid in lump sums.

## Section 11 -- Tier 1 Rules (deterministic — the skill applies these directly)

- **T1-1 Resident ISR schedule** — Resident ISR on employment income (2025–2026): 5% on annual taxable income up to Q300,000; Q15,000 + 7% on the excess. The schedule is continuous (Q15,000 = 5% × 300,000).  _(PwC; Decreto 10-2012)_
- **T1-2 Standard personal deduction and IVA credit** — Standard personal deduction = Q48,000/year (sin comprobación); plus an IVA credit of up to Q12,000/year but only if backed by facturas (default Q0).  _(PwC; Prensa Libre)_
- **T1-3 IGSS employee contributions deductible** — Employee IGSS contributions (4.83% of the salary base) are deductible in computing taxable income.  _(PwC)_
- **T1-4 Employee social security** — Employee social security = 4.83% IGSS cuota laboral on the salary base (ordinary + extraordinary, excluding the Q250 incentivo). No employee INTECAP/IRTRA. No salary cap found.  _(PwC; IGSS)_
- **T1-5 Employer social security** — Employer social security = 12.67% cuota patronal = IGSS 10.67% + INTECAP 1% + IRTRA 1%, on the same base, paid on top of salary.  _(IGSS; PwC; copades)_
- **T1-6 Combined social-security wedge** — Combined social-security wedge = 17.50% (employee 4.83% + employer 12.67%).  _(PwC)_
- **T1-7 Bonificación incentivo exclusion** — The Q250/month bonificación incentivo (Decreto 78-89) is non-salary: excluded from the IGSS base and from benefit calculations, and paid on top of base salary.  _(misalario; copades)_
- **T1-8 Aguinaldo and Bono 14 timing** — Aguinaldo (Decreto 76-78) and Bono 14 (Decreto 42-92) are each one month's salary (pro-rated): aguinaldo 50% in the first 15 days of December and the rest by 15 January; Bono 14 by 15 July.  _(Mintrabajo)_
- **T1-9 Non-resident employment income** — Non-resident employment income: 15% flat definitive on gross, no deductions; remit within the first 10 business days of the following month with a constancia.  _(Decreto 10-2012; Baker Tilly)_
- **T1-10 Withholding order** — Withholding order: project annual income → subtract Q48,000 personal deduction, IVA credit (if proven), actual IGSS, confirmed donations/insurance → annual taxable income → apply 5% / 7% schedule → divide by 12 → monthly ISR; reconcile at the December liquidación.  _(Decreto 10-2012; oficsa)_
- **T1-11 Employer IGSS registration threshold** — Employer IGSS registration threshold = 1 worker since 17 Jan 2023 (Acuerdo JD 1529); register within 30 business days of the obligation arising.  _(IGSS; EY; Prensa Libre)_
- **T1-12 Currency and tax year** — Currency is GTQ (Quetzal) only; the tax year is the calendar year.  _(PwC)_

## Section 12 -- Tier 2 Catalogue (reviewer judgement required)

These items depend on facts or sources not fully resolved in this research. The skill must surface them and recommend professional review rather than asserting a single answer.

**Tier 2 catalogue table**

| Ref | Issue | What the reviewer must resolve |
| --- | --- | --- |
| **[T2-1]** | Decreto 13-2026 (minimum-wage ISR exemption + Q3,024 extra deduction) | Confirm the final published decree text, the exact Q3,024 figure, and the effective tax year before applying it. **[RESEARCH GAP]** |
| **[T2-2]** | Exact SAT form numbers and filing wording | SAT portal returned HTTP 403; form references SAT-1411 / SAT-1431 and the RetenISR mechanics come from secondary advisory sources — verify directly on the SAT portal. |
| **[T2-3]** | ISR treatment of the Q250 bonificación incentivo | Research confirmed the IGSS exclusion only; confirm whether the Q250 is also exempt from ISR or forms part of taxable income. |
| **[T2-4]** | Donations and life-insurance deduction limits | Confirm exact caps (commonly cited up to 5% of net income for donations) and conditions. |
| **[T2-5]** | IGSS contribution ceiling | No salary cap was found in any authoritative source — confirm "none" against current IGSS regulations. |
| **[T2-6]** | 2025 per-sector / per-circumscription minimum wage | The 2025 source consolidated agrícola / no-agrícola for CE1 — confirm the per-sector split against the official ONSEC table. |
| **[T2-7]** | Overtime / night / Sunday / holiday premiums and maximum hours | Not researched here — confirm from the Código de Trabajo and any pacto colectivo. |
| **[T2-8]** | Benefits in kind, severance / indemnización, per-diem tax limits | Not in this research dataset — reviewer to populate. |
| **[T2-9]** | Penalty figures and the daily/late-filing wording | The Código Tributario rates in Section 13 come from a secondary summary; confirm the exact article wording and current amounts against the in-force Decreto 6-91. |
| **[T2-10]** | IGSS treatment of non-residents performing work in Guatemala | Confirm whether IGSS contributions apply alongside the 15% ISR for a given assignment. |

## Section 13 -- Filing Obligations

### Monthly — ISR withholding (RetenISR)

**RetenISR filing table**  _(SAT portal; Baker Tilly)_

| Form / system | Purpose | Deadline | Source |
| --- | --- | --- | --- |
| **RetenISR (Sistema de Retenciones Web -ISR-)** | Employer reports and remits monthly ISR withheld on employment income to SAT | Remitted monthly; non-resident withholding remitted within the **first 10 business days of the month following** payment | SAT portal; Baker Tilly **[T2-2 — confirm exact resident-withholding monthly deadline on SAT]** |
| **Constancia de retención** | Final withholding statement issued to the employee via RetenISR | Within **10 business days** of the last payment of the settlement period | oficsa; Deloitte **[T2-2]** |

### Social security — IGSS planilla

**IGSS planilla table**  _(IGSS)_

| Filing | Purpose | Source |
| --- | --- | --- |
| IGSS planilla (cuota patronal + cuota laboral) | Monthly remittance of employer 12.67% and withheld employee 4.83% (plus INTECAP/IRTRA where bundled) | IGSS **[T2 — confirm exact monthly planilla deadline]** |

### Annual

**Annual filing table**  _(oficsa; Deloitte)_

| Form | Purpose | Deadline | Source |
| --- | --- | --- | --- |
| Final settlement (liquidación) | Employer year-end reconciliation applying the Q48,000 / Q12,000 / donations / insurance / IGSS deductions | Performed in **December** | oficsa; Deloitte |
| Employee annual sworn declaration (where applicable) | Employee's own ISR reconciliation when required | Within the **first 3 months** of the year following the tax period | oficsa **[T2-2 — confirm SAT form number (SAT-1431 / SAT-1411 cited by secondary sources)]** |

### Employer registration

**Employer registration filing table**  _(IGSS; EY; Prensa Libre)_

| Filing | Purpose | Deadline | Source |
| --- | --- | --- | --- |
| IGSS employer registration (inscripción patronal) | Register a new employer with IGSS (threshold: 1 worker) | Within **30 business days** of the obligation arising | IGSS; EY; Prensa Libre |

## Section 14 -- Penalties (Código Tributario, Decreto 6-91)

> Figures below come from a secondary summary of the Código Tributario; confirm exact article wording and current amounts against the in-force Decreto 6-91. **[T2-9]**

**Penalties table**  _(Código Tributario, Decreto 6-91)_

| Infraction | Penalty | Reference |
| --- | --- | --- |
| **Mora** (late payment of self-assessed tax) | Tax × **0.005 per day** of delay | Art. 92 (Prensa Libre summarising Código Tributario) |
| **Omisión de pago** (omitted / incorrect tax) | **100%** of the omitted tax | Art. 89 |
| **Failure to withhold / remit** (retención no efectuada) | Fine = the tax that should have been withheld (withholding-agent liability) | Código Tributario |
| **Late filing of a declaration** | **Q50 per day**, capped at **Q1,000** | Código Tributario (secondary) **[T2-9 — confirm article]** |
| Voluntary reduction (before SAT notice) | Mora fine reduced **85%**; omisión fine reduced **50%** | Arts. 91, 106 |

> Default interest and additional sanctions may apply. Record-retention requirements were not part of this research dataset. **[RESEARCH GAP — confirm record-retention period.]**

## Section 15 -- Excel Working Paper Template

**Excel working paper column table**

| Col | Heading | Type | Formula / source |
| --- | --- | --- | --- |
| A | Employee name | Input | — |
| B | NIT (tax ID) | Input | SAT identifier |
| C | Residency | Input | resident / non-resident |
| D | Monthly base salary (Q) | Input | salario base |
| E | Annual base salary (Q) | Computed | `D * 12` |
| F | IGSS employee (4.83%) | Computed | `E * 4.83%` |
| G | Standard personal deduction | Input | `48000` |
| H | IVA credit (max 12,000) | Input | `0` unless facturas proven, capped at 12000 |
| I | Donations / insurance | Input | confirmed only, else 0 |
| J | Annual taxable income | Computed | `MAX(E - F - G - H - I, 0)` |
| K | ISR — first band | Computed | `MIN(J,300000) * 5%` |
| L | ISR — higher band | Computed | `MAX(J-300000,0) * 7%` |
| M | Annual ISR | Computed | `K + L` |
| N | Monthly ISR | Computed | `M / 12` |
| O | Monthly IGSS employee | Computed | `F / 12` |
| P | Net monthly (salary) | Computed | `D - O - N` |
| Q | Bonificación incentivo | Input | `250` |
| R | Net monthly received | Computed | `P + Q` |
| S | Employer cuota patronal (12.67%) | Computed | `D * 12.67%` |
| T | Total monthly employer cost | Computed | `D + S + Q + (D/12)*2` (adds aguinaldo + Bono 14 accrual) |

> For a non-resident (col C = non-resident), ISR = `D * 15%` on gross with no deductions; columns F–O do not apply. Footer checks: sum of column N ties to the RetenISR remittance; sum of O + S ties to the IGSS planilla; sum of R ties to total net wages disbursed.

## Section 16 -- Guatemalan Bank Statement & Terminology Reading Guide

**Terminology table**

| Spanish term | English | Relevance |
| --- | --- | --- |
| Salario base / sueldo | Base salary | Starting figure for all computations |
| Salario neto | Net salary | What the employee receives |
| Renta imponible | Taxable income | After deductions, before ISR |
| ISR (Impuesto Sobre la Renta) | Income tax | Withheld monthly |
| Rentas del trabajo en relación de dependencia | Employment income | The category this skill covers |
| Retención ISR | ISR withholding | The monthly withholding mechanism |
| Cuota laboral | Employee IGSS contribution | 4.83%, withheld |
| Cuota patronal | Employer contribution | 12.67% (IGSS + INTECAP + IRTRA) |
| Bonificación incentivo | Incentive bonus | Q250/month, non-salary, on top |
| Aguinaldo | Christmas bonus | One month's salary, Dec/Jan |
| Bono 14 / Bonificación anual | 14th-month bonus | One month's salary, by 15 July |
| Salario mínimo | Minimum wage | By circumscription and sector |
| Liquidación | Final settlement | Year-end ISR reconciliation (December) |
| Constancia de retención | Withholding certificate | Issued to employee via RetenISR |
| SAT | Tax Administration | Receives ISR; runs RetenISR |
| IGSS | Social Security Institute | Receives IGSS contributions |
| INTECAP | Training institute | 1% employer levy |
| IRTRA | Workers' recreation institute | 1% employer levy |
| NIT | Tax identification number | Required for ISR |
| Planilla | Payroll / contribution schedule | IGSS monthly filing |
| RetenISR | SAT withholding web system | Electronic ISR filing |
| Quetzal (Q / GTQ) | Currency | All figures in Quetzales |

## Section 17 -- Onboarding Fallback

When key facts are missing, ask the user these questions before computing. If a question is unanswered, apply the Section 7 conservative default and clearly flag the assumption.

1. What is the employee's monthly base salary in GTQ?
2. Is the employee a resident or non-resident of Guatemala? (Non-resident → 15% flat on gross.)
3. Which economic circumscription (CE1 / CE2) and sector (agricultural / non-agricultural / export-maquila)? (To validate the minimum wage.)
4. Is up to Q12,000 of personal expenses backed by facturas for the IVA credit? (If unproven → Q0.)
5. Are there confirmed donations or life-insurance premiums to deduct? (If none → Q0.)
6. Which month and year is this pay run for? (Determines minimum wage and any reform in effect — 2025 vs 2026.)
7. Do aguinaldo or Bono 14 fall in this period? (To include them in taxable income.)

## Section 18 -- Interaction with Other Skills

**Interaction table**

| Scenario | Skill to use |
| --- | --- |
| Employee payroll (ISR + IGSS + INTECAP + IRTRA) | **This skill (guatemala-payroll.md)** |
| Guatemala personal income tax (annual / self-employment) | guatemala-income-tax.md |
| Guatemala social-security mechanics (detailed IGSS) | guatemala-social-security.md |
| Cross-border / posted workers / totalization | cross-border-payroll-coordination.md |
| Guatemala VAT (IVA) returns | guatemala-vat-return.md |
| Shared workflow runbook | payroll-workflow-base.md |

### Key handoff points

- **Payroll → Bookkeeping:** Gross wages, the Q250 incentivo, and the 12.67% employer cuota patronal (plus aguinaldo/Bono 14 accruals) are expenses; withheld ISR and the 4.83% employee IGSS are liabilities until remitted.
- **Payroll → Income tax:** Most employees are settled through the employer's December liquidación; some file an annual sworn declaration in the first 3 months of the following year.
- **Payroll → Social security:** IGSS contributions paid through payroll build the employee's social-security entitlement; INTECAP and IRTRA fund training and recreation, not individual benefits.

## Section 19 -- Reference Material

**Reference material table**

| # | Source | Publisher | URL |
| --- | --- | --- | --- |
| 1 | Guatemala — Individual — Taxes on personal income (ISR brackets 5% / 7%) | PwC Worldwide Tax Summaries | https://taxsummaries.pwc.com/guatemala/individual/taxes-on-personal-income |
| 2 | Guatemala — Individual — Deductions (Q48,000 / Q12,000, IGSS deductible) | PwC Worldwide Tax Summaries | https://taxsummaries.pwc.com/guatemala/individual/deductions |
| 3 | Guatemala — Individual — Other taxes (IGSS 4.83% / 12.67%, 17.50% combined) | PwC Worldwide Tax Summaries | https://taxsummaries.pwc.com/guatemala/individual/other-taxes |
| 4 | Guatemala — Individual — Tax administration (calendar tax year) | PwC Worldwide Tax Summaries | https://taxsummaries.pwc.com/guatemala/individual/tax-administration |
| 5 | A partir de qué salario se paga ISR (Q48,000 / Q12,000, 5% / 7%) | Prensa Libre (citing SAT) | https://www.prensalibre.com/economia/a-partir-de-que-salario-se-paga-isr-en-guatemala-y-como-se-calcula/ |
| 6 | RetenISR — Sistema de Retenciones Web -ISR- | SAT | https://portal.sat.gob.gt/portal/sistemas-web/retencioneswebisr/ |
| 7 | Régimen de retenciones de ISR a no residentes (15% flat, Art. 104) | Baker Tilly Guatemala | https://www.bakertilly.gt/en/insights/el-r%C3%A9gimen-de-retenciones-de-impuesto-sobre-la-renta-a-no-residentes-en-guatemala |
| 8 | Impuesto sobre la renta a empleados (monthly withholding, liquidación, constancia) | oficsa | https://oficsa.com/2025/09/17/impuesto-sobre-la-renta-a-empleados/ |
| 9 | La contribución del patrono al IGSS (employer 10.67%) | IGSS | https://www.igssgt.org/noticias/2023/04/17/la-contribucion-del-patrono-al-igss-trae-beneficios-para-su-empresa/ |
| 10 | Cuota patronal IGSS (INTECAP 1% + IRTRA 1% breakdown) | misalario.com.gt | https://misalario.com.gt/cuota-patronal-igss-guatemala/ |
| 11 | Cuota patronal breakdown (12.67% composition) | copades | https://copades.com/monec/?p=41737 |
| 12 | Inscripción patronal (1-worker threshold, 30-business-day deadline) | IGSS | https://www.igssgt.org/patronos/inscripcion-patronal/ |
| 13 | Nuevo reglamento de inscripción a la seguridad social (Acuerdo JD 1529) | EY | https://www.ey.com/es_ce/technical/tax/tax-alerts/guatemala-nuevo-reglamento-de-inscripcion-a-la-seguridad-socia |
| 14 | Todos los patronos deben registrarse (1-worker threshold) | Prensa Libre | https://www.prensalibre.com/economia/todos-los-patronos-deben-registrarse-y-pagar-igss-aunque-tengan-solo-un-trabajador/ |
| 15 | Salario mínimo 2026 (Acuerdo Gubernativo 256-2025) | EY tax alert | https://www.ey.com/es_ce/technical/tax/tax-alerts/guatemala-salario-minimo-2026 |
| 16 | Gobierno fija nuevos salarios mínimos para 2026 | Diario de Centro América | https://dca.gob.gt/noticias-guatemala-diario-centro-america/gobierno-fija-nuevos-salarios-minimos-para-2026/ |
| 17 | Salario mínimo 2025 (Acuerdo Gubernativo 264-2024) | guatemala.com | https://www.guatemala.com/noticias/sociedad/salario-minimo-2025-en-guatemala.html |
| 18 | Salarios mínimos por circunscripción económica (table) | ONSEC | https://www.onsec.gob.gt/w1/wp-content/uploads/2025/01/SALARIOS-MINIMOS-PARA-LAS-ACTIVIDADES-ECONOMICAS-POR-CIRCUNSCRIPCION-ECONOMICA.pdf |
| 19 | Bono 14 (Bonificación Anual, Decreto 42-92) | Mintrabajo | https://www.mintrabajo.gob.gt/bono-14 |
| 20 | Ley de Bonificación Anual (Decreto 42-92, official text) | Mintrabajo | https://www.mintrabajo.gob.gt/images/Documentacion/Leyes_Ordinarias/Decretos/Ley_de_Bonificacin_Anual_Para_Trabajadores_del_Sector_Privado_y_Pblico_Decreto_42-92.pdf |
| 21 | Cierre anual de retención (annual withholding close) | Deloitte | https://www2.deloitte.com/content/dam/Deloitte/gt/Documents/tax/GUATEMALA/Taxnewsletter/161219%20-%20Tax%20Newsletter%20-%20cierre%20anual%20de%20retenci%C3%B3n.pdf |
| 22 | Sanciones del Código Tributario (mora, omisión, multas) | Prensa Libre | https://www.prensalibre.com/economia/que-pasa-si-no-se-paga-impuestos-en-guatemala-y-cuales-son-las-sanciones-multas-y-consecuencias/ |
| 23 | Código Tributario (Decreto 6-91, text) | leyestributariasguatemala | https://www.leyestributariasguatemala.com/leyes/codigo-tributario-decreto-6-91 |
| 24 | Decreto 13-2026 (minimum-wage ISR exemption + Q3,024) | guatemala.com / Congreso | https://www.guatemala.com/noticias/comunidad/salario-minimo-estara-exento-retencion-isr-guatemala-decreto-13-2026.html |

Primary authorities: SAT (https://portal.sat.gob.gt); IGSS (https://www.igssgt.org); Ministerio de Trabajo (https://www.mintrabajo.gob.gt); ONSEC (https://www.onsec.gob.gt).

### Test Suite

Run these to validate any implementation of this skill. Expected results use 2026 figures, resident status, and the Q12,000 IVA credit at Q0 (conservative default) unless stated otherwise.

1. **Standard mid earner.** Q8,000/month base, IVA credit Q0. Expect: annual IGSS Q4,636.80, annual taxable Q43,363.20, annual ISR Q2,168.16, monthly ISR Q180.68, monthly IGSS Q386.40, net salary Q7,432.92, net received (with Q250 incentivo) Q7,682.92.
2. **IVA credit applied.** Q8,000/month base, IVA credit Q12,000. Expect: annual taxable Q31,363.20, annual ISR Q1,568.16, monthly ISR Q130.68, net salary Q7,482.92.
3. **Minimum-wage worker (2026 CE1 non-ag).** Q4,002.28/month base. Expect: annual IGSS Q2,319.72, annual taxable Q0.00, ISR Q0.00, monthly IGSS Q193.31, net salary Q3,808.97, net received Q4,058.97.
4. **High earner, higher band.** Q40,000/month base, IVA credit Q12,000. Expect: annual taxable Q396,816.00, annual ISR Q21,777.12 (Q15,000 + 7% × Q96,816), monthly ISR Q1,814.76, monthly IGSS Q1,932.00, net salary Q36,253.24.
5. **Single-bracket upper earner.** Q30,000/month base, IVA credit Q12,000. Expect: annual taxable Q282,612.00 (below Q300,000), annual ISR Q14,130.60 (all at 5%), monthly ISR Q1,177.55, net salary Q27,373.45.
6. **Non-resident flat rate.** Q50,000 gross to a non-resident. Expect: ISR Q7,500.00 (15% on gross, no deductions), net Q42,500.00.
7. **Employer cost.** Q8,000/month base. Expect: cuota patronal Q1,013.60 (IGSS Q853.60 + INTECAP Q80 + IRTRA Q80), plus Q250 incentivo, plus aguinaldo Q666.67 and Bono 14 Q666.67 accrual → total employer cost Q10,596.94/month.
8. **Bracket-continuity check.** Confirm the schedule is continuous: tax at exactly Q300,000 = Q15,000 under both the 5% formula (300,000 × 5%) and the higher-band fixed amount.
9. **Incentivo exclusion.** Confirm the Q250 bonificación incentivo is excluded from the IGSS base and from ISR's IGSS-deduction figure, and is added on top of net pay.
10. **Contribution totals.** Confirm employee 4.83% + employer 12.67% = 17.50% combined, and IGSS-only combined = 15.50%.
11. **Deduction default.** IVA credit unconfirmed — confirm the skill applies Q0 (not Q12,000) and flags the assumption.
12. **Decreto 13-2026 guard.** Confirm the skill does NOT apply the Q3,024 extra deduction or the minimum-wage ISR exemption pending reviewer confirmation of the final decree.

## PROHIBITIONS

- NEVER claim Guatemala has no income tax — ISR applies to employment income at 5% / 7% under Decreto 10-2012.
- NEVER apply the Q12,000 IVA credit without confirmed facturas — default to Q0 and flag it.
- NEVER apply the Decreto 13-2026 Q3,024 extra deduction or minimum-wage ISR exemption until the final decree is confirmed — it is a flagged RESEARCH GAP.
- NEVER include the Q250 bonificación incentivo in the IGSS contribution base — it is non-salary by Decreto 78-89.
- NEVER deduct the 12.67% employer cuota patronal (IGSS + INTECAP + IRTRA) from the employee's net pay — it is an employer cost on top of salary.
- NEVER charge an employee INTECAP or IRTRA deduction — those levies are employer-only.
- NEVER apply the 7% rate to raw salary — it applies only to annual taxable income above Q300,000, after deductions.
- NEVER apply the resident progressive schedule to a non-resident — non-residents pay a 15% definitive flat rate on gross.
- NEVER omit the mandatory statutory bonuses (Q250 incentivo monthly, aguinaldo, Bono 14) from payroll cost.
- NEVER run a full-time employee below the applicable minimum wage for their circumscription and sector.
- NEVER quote a penalty figure as definitive — the Código Tributario amounts here are from a secondary summary pending reviewer confirmation.
- NEVER present payroll computations as definitive — always label them as estimated and direct the user to a licensed Guatemalan Contador Público y Auditor.

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a licensed Contador Público y Auditor or tax adviser in Guatemala) before implementation.

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
