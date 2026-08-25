---
name: honduras-social-contributions
description: Use this skill whenever asked about Honduras payroll contributions, social security, or personal income tax (ISR) for employees, employers, or self-employed individuals. Trigger on phrases like "how much IHSS do I pay", "Honduras social security", "IHSS contribution", "RAP deduction", "INFOP levy", "ISR withholding Honduras", "Honduras income tax table", "tabla progresiva", "techo de cotización", "aguinaldo tax", "13th month Honduras", "Código 111 withholding", "Honduras net salary", or any question about Honduran payroll deductions, employer contributions, or ISR. Also trigger when classifying bank-statement transactions that relate to IHSS, RAP, INFOP, or SAR (tax) debits from Honduran banks (Banco Atlántida, Banco Ficohsa, BAC Credomatic, Banco de Occidente). This skill covers the 2025/2026 ISR progressive table, IHSS (IVM + EM) rates and ceilings, RAP labor-reserve fund, INFOP training levy, 13th/14th month pay, filing forms and deadlines, penalties, bank-statement classification patterns, and edge cases. ALWAYS read this skill before touching any Honduran payroll or ISR work.
version: 0.1
jurisdiction: HN
tax_year: 2025
last_updated: 2026-07-13
review_status: pending_review
depends_on:
  - social-contributions-workflow-base
category: international
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Honduras Payroll Contributions & Income Tax (ISR)

## Honduras Payroll Contributions & Income Tax (ISR) Skill v0.1

> **Tier 2 (research-verified) — NOT yet professionally verified.** Figures are drawn from sourced research (Big-4 summaries, Honduran press citing the IHSS/SAR, and statute references) but have NOT been signed off by a Honduran Contador Público Colegiado. Treat all outputs as estimates pending review.

## Section 1 -- Quick reference

**Read this whole section before computing or classifying anything.**

**Quick reference field table**

| Field | Value |
| --- | --- |
| Country | Republic of Honduras |
| Currency | Honduran Lempira (HNL / "L") — **HNL only** |
| Basis of taxation | **Territorial** — Honduran-source income only ([PwC Honduras](https://taxsummaries.pwc.com/honduras/individual)) |
| Personal income tax | **YES** — progressive ISR (this is not a no-PIT jurisdiction) |
| Income tax authority | SAR (Servicio de Administración de Rentas) |
| Income tax law | Ley del Impuesto Sobre la Renta; annual table per Art. 22 (Decreto 20-2016) |
| 2025 ISR table | Acuerdo SAR-007-2025 (adjusted +3.88%, 2024 CPI) |
| 2025 exempt threshold | Monthly salary ≤ **L 21,457.76** pays no ISR ([Bloomberg Línea](https://www.bloomberglinea.com/latinoamerica/honduras/tabla-progresiva-2025-en-honduras-que-salarios-estan-exentos-del-isr/)) |
| Social security authority | IHSS (Instituto Hondureño de Seguridad Social) |
| IHSS 2025 ceiling (techo) | **L 11,903.13/month** ([El Heraldo](https://www.elheraldo.hn/honduras/techo-ihss-aumento-1361-lempiras-trabajadores-aportaran-mas-dinero-AM23495401)) |
| IHSS employee total | **5.0%** (IVM 2.5% + EM 2.5%) on salary up to ceiling |
| IHSS employer total | **8.5%** (IVM 3.5% + EM 5.0%) on salary up to ceiling, + ~0.2% occupational risk |
| RAP (private pension) | 4% employer labor-reserve fund + 1.5%/1.5% on salary above IHSS ceiling |
| INFOP (training levy) | **1% of payroll, employer-only**, firms with 5+ employees |
| Tax year | Calendar year ending 31 December |
| Annual ISR return due | **30 April** following the tax year ([SAR](https://www.sar.gob.hn/impuesto-sobre-renta-isr/)) |
| Validated by | Pending — requires sign-off by a Honduran Contador Público Colegiado |
| Validation date | Pending |

**ISR 2025 progressive table (Acuerdo SAR-007-2025, effective FY2025)**  _([Auxadi](https://www.auxadi.com/blog/2025/01/30/honduras-updates-income-tax/) · [KPMG TNF Jan 2025](https://kpmg.com/kpmg-us/content/dam/kpmg/taxnewsflash/pdf/2025/01/tnf-honduras1-jan14-2025.pdf))_

| Bracket | Annual net taxable income (L) | Approx. monthly salary (L) | Marginal rate |
| --- | --- | --- | --- |
| 1 | 0.01 – 217,493.16 | 0.01 – 21,457.76 | **0% (exempt)** |
| 2 | 217,493.17 – 331,638.50 | 21,457.77 – 30,969.88 | **15%** |
| 3 | 331,638.51 – 771,252.38 | 30,969.89 – 67,604.36 | **20%** |
| 4 | 771,252.39 and above | 67,604.37+ | **25%** |

**Cumulative ISR at each bracket boundary (recomputed)**

| At annual income (L) | Cumulative ISR (L) | Working |
| --- | --- | --- |
| 217,493.16 | 0.00 | bottom of bracket 2 |
| 331,638.50 | 17,121.80 | (331,638.50 − 217,493.16) × 15% = 114,145.34 × 15% |
| 771,252.38 | 105,044.58 | 17,121.80 + (771,252.38 − 331,638.50) × 20% = 17,121.80 + 439,613.88 × 20% (= 87,922.78) |
| above | 105,044.58 + 25% of excess over 771,252.38 | — |

**2026 ISR table (CONFIRMED — SAR Comunicado 02-2026)**  _([Deloitte Honduras](https://www.deloitte.com/latam/es/services/tax/perspectives/hn-12ene26-sar-actualiza-tabla-progresiva-para-2026-honduras.html) (+4.98% 2025 CPI, effective 12 Jan 2026, use only for FY2026 work))_

| Annual net taxable income (L) | Approx. monthly salary (L) | Rate |
| --- | --- | --- |
| 0.01 – 228,324.32 | 0.01 – 22,360.36 | 0% (exempt) |
| 228,324.33 – 348,154.10 | 22,360.37 – 32,346.18 | 15% |
| 348,154.11 – 809,660.75 | 32,346.19 – 70,805.06 | 20% |
| 809,660.76 and above | 70,805.07+ | 25% |

**Contribution overview (2025)**  _([Mismo Honduras payroll guide](https://mismo.team/honduras-payroll-guide-ihss-rap-infop-13th-14th/) · [El Heraldo nuevas tasas IHSS 2025](https://www.elheraldo.hn/honduras/nuevas-tasas-cotizacion-ihss-entran-vigor-2025-tras-aprobacion-congreso-nacional-IA23459188))_

| Scheme | Employee | Employer | State | Base |
| --- | --- | --- | --- | --- |
| IHSS — IVM (disability/old-age/death) | 2.5% | 3.5% | 0.5% | salary up to L 11,903.13 |
| IHSS — EM (sickness/maternity) | 2.5% | 5.0% | — | salary up to L 11,903.13 |
| **IHSS total** | **5.0%** | **8.5%** | **0.5%** | up to ceiling |
| IHSS — occupational risk (Riesgos Profesionales) | — | ~0.2% | — | varies by industry risk class |
| RAP — labor-reserve fund (Fondo de Reserva Laboral) | — | 4.0% | — | capped at 3× highest minimum wage |
| RAP — above-ceiling savings | 1.5% | 1.5% | — | salary portion **above** L 11,903.13 |
| INFOP — training levy | — | 1.0% | — | total payroll (firms with 5+ employees) |

Employee column 2.5 + 2.5 = **5.0** ✓ Employer column 3.5 + 5.0 = **8.5** ✓ (Riesgos/RAP/INFOP additional, shown separately).

> **Source conflict flag.** [PwC Honduras — Other taxes](https://taxsummaries.pwc.com/honduras/individual/other-taxes) still shows pre-reform figures (EM employee 2.5% on ceiling L 11,109.36; IVM employee 1% on ceiling L 11,336.00). Those **predate the 2025 reform** (Ley para la Regulación de las Aportaciones y Cotizaciones del IHSS) and must NOT be used for 2025. Use the unified ceiling L 11,903.13 and employee total 5.0%. **[RESEARCH GAP — reviewer to confirm the full per-line IVM/EM split against the IHSS law text/official PDF before Q1/Q2 verification.]**

**Conservative defaults**

| Ambiguity | Default |
| --- | --- |
| Unknown gross monthly salary | STOP — do not compute ISR or contributions without gross salary |
| Salary at or below exempt threshold | ISR = 0; IHSS/RAP/INFOP still apply |
| Unknown whether salary exceeds IHSS ceiling | Apply contributions only up to L 11,903.13; flag above-ceiling RAP for review |
| Unknown firm size for INFOP | Assume 5+ employees (1% applies); flag for confirmation |
| Unknown medical-expense documentation | Apply the flat L 40,000/year deduction (statutory, not itemized) |
| Aguinaldo / 14th month taxability | Treat as exempt only up to 10× average minimum wage; **[RESEARCH GAP — confirm exact 10× figure]** |
| Unknown DSS/SAR debit purpose | Classify per Section 3; flag ambiguous lines for reviewer |

## Section 2 -- Required inputs and refusal catalogue

### Required inputs

**Minimum viable** — gross monthly salary (HNL) and employment status (employee / employer / self-employed). Without gross salary, STOP. Do not compute ISR or contributions.

**Recommended** — number of employees in the firm (for INFOP), whether salary exceeds the IHSS ceiling (for above-ceiling RAP), and tax year (2025 vs 2026 table).

**Ideal** — full payslip, IHSS planilla, RAP statement, prior-year ISR return (Form 102), and bank statements showing IHSS/RAP/INFOP/SAR debits.

### Refusal catalogue

- **R-HN-1 — Gross salary unknown** — Trigger: gross monthly salary not provided. Message: "Gross monthly salary in HNL is mandatory for any ISR or contribution computation. Cannot proceed without it."
- **R-HN-2 — Arrears / mora computation** — Trigger: client has unpaid IHSS, RAP, INFOP, or ISR from prior periods. Message: "Honduran late-filing surcharges (5%–20% by delay), omission fines (40% of tax, floored at one minimum monthly salary), and late-payment interest (reported ~14% p.a. but set periodically) cannot be reliably quantified without official SAR/IHSS statements. Escalate to a Honduran Contador Público Colegiado."  _([Código Tributario, Decreto 22-97](https://www.tsc.gob.hn/web/leyes/C%C3%B3digo%20Tributario.pdf))_
- **R-HN-3 — Expatriate / non-resident / double-taxation** — Trigger: client is a foreign worker, non-resident, or asks about treaty relief. Message: "Honduras taxes on a territorial basis; expatriate residency, foreign-source exclusion, and treaty treatment are case-specific. Escalate to a Honduran tax professional."
- **R-HN-4 — Self-employed / professional ISR (non-salaried)** — Trigger: client earns business or professional income filed on Form 102 outside PAYE withholding. Message: "This skill's withholding logic (Código 111, Art. 22) is built for salaried workers. Self-employed annual ISR on Form 102 involves deductible expenses and quarterly payments on account — escalate for a full return computation."
- **R-HN-5 — Exemption / special regime claims** — Trigger: client claims maquila/ZIP exemption, disability relief, or a special-regime carve-out. Message: "Special regimes (maquila, ZOLI/ZIP free zones) and statutory exemptions require case-specific confirmation. Escalate to a Honduran tax professional."

## Section 3 -- Payment pattern library

Deterministic pre-classifier for Honduran bank-statement transactions related to payroll, contributions, and tax. Match by case-insensitive substring on the counterparty/reference. IHSS, RAP, INFOP, and SAR/ISR payments **EXCLUDE** from any sales-tax (ISV) return — they are statutory obligations, not business supplies.

### 3.1 IHSS social security contributions

**IHSS pattern table**

| Pattern | Treatment | Notes |
| --- | --- | --- |
| IHSS, INSTITUTO HONDUREÑO DE SEGURIDAD SOCIAL | EXCLUDE — IHSS contribution | Monthly IVM + EM |
| SEGURIDAD SOCIAL, SEGURO SOCIAL | EXCLUDE — IHSS contribution | Same |
| IVM, ENFERMEDAD Y MATERNIDAD, EM IHSS | EXCLUDE — IHSS contribution | Regime-specific reference |
| PLANILLA IHSS | EXCLUDE — IHSS payroll remittance | Employer planilla |

### 3.2 RAP — Régimen de Aportaciones Privadas

**RAP pattern table**

| Pattern | Treatment | Notes |
| --- | --- | --- |
| RAP, REGIMEN DE APORTACIONES PRIVADAS | EXCLUDE — RAP contribution | Labor-reserve / above-ceiling savings |
| FONDO DE RESERVA LABORAL | EXCLUDE — RAP labor-reserve fund | 4% employer-only |
| APORTACIONES PRIVADAS | EXCLUDE — RAP contribution | Same |

### 3.3 INFOP — training levy

**INFOP pattern table**

| Pattern | Treatment | Notes |
| --- | --- | --- |
| INFOP, INSTITUTO NACIONAL DE FORMACION PROFESIONAL | EXCLUDE — INFOP levy | 1% of payroll, employer-only |
| FORMACION PROFESIONAL | EXCLUDE — INFOP levy | Same |

### 3.4 ISR / tax payments (SAR — NOT a contribution)

**SAR/ISR pattern table**

| Pattern | Treatment | Notes |
| --- | --- | --- |
| SAR, SERVICIO DE ADMINISTRACION DE RENTAS | EXCLUDE — tax payment, not a contribution | ISR / ISV remittance |
| ISR, IMPUESTO SOBRE LA RENTA | EXCLUDE — income tax | Not IHSS/RAP/INFOP |
| ISV, IMPUESTO SOBRE VENTAS | EXCLUDE — sales tax | Not a payroll contribution |
| CODIGO 111, RETENCION ART 22 | EXCLUDE — employee ISR withholding | PAYE withholding, not a contribution |
| DET LIVE, OFICINA VIRTUAL SAR | EXCLUDE — SAR e-payment | Channel reference |

### 3.5 Salary / payroll (exclude from contribution classification)

**Salary/payroll pattern table**

| Pattern | Treatment | Notes |
| --- | --- | --- |
| SALARIO, SUELDO, NOMINA, PLANILLA (outgoing) | EXCLUDE — payroll expense | Wage payment, not a contribution |
| SALARIO, SUELDO (incoming) | EXCLUDE — employment income received | Not a contribution |
| AGUINALDO, CATORCEAVO, 13ER MES, 14TO MES | EXCLUDE — statutory bonus | 13th/14th month pay |

## Section 4 -- Worked examples

Six bank-statement / payslip classifications for a hypothetical Honduran SME and its employees. All amounts in HNL.

### Example 1 — Low-wage employee, below ISR exempt threshold

**Input line:**
`31.01.2025 ; IHSS PLANILLA ENE ; DEBITO ; SEGURIDAD SOCIAL ; -595.16 ; HNL`

**Reasoning:**
Employee gross salary L 12,000/month. ISR: monthly salary L 12,000 ≤ exempt threshold L 21,457.76 → **ISR = 0**. IHSS employee 5.0% applies to salary capped at ceiling L 11,903.13 → 11,903.13 × 5.0% = **L 595.156 ≈ L 595.16**. The debit matches "IHSS PLANILLA" (pattern 3.1). EXCLUDE from ISV. (Employer separately pays 8.5% = 11,903.13 × 8.5% = L 1,011.77, plus ~0.2% risk and 4% RAP labor-reserve.)

**Classification:** EXCLUDE — IHSS contribution. Employee ISR = 0 for this salary.

### Example 2 — Mid-range salaried employee, ISR withholding (Código 111)

**Input line:**
`05.02.2025 ; SAR CODIGO 111 ; DEBITO ; RETENCION ART 22 ENE ; -393.92 ; HNL`

**Reasoning:**
Employee gross salary L 30,000/month → annual L 360,000. Annual net taxable income = 360,000 − 40,000 medical deduction = **L 320,000**. This falls in bracket 2 (217,493.17–331,638.50, 15%). Annual ISR = (320,000 − 217,493.16) × 15% = 102,506.84 × 15% = **L 15,376.026 ≈ L 15,376.03/year**. Monthly withholding = 15,376.03 ÷ 12 = **L 1,281.34**. (The L 393.92 sample debit illustrates the *channel*, not this figure — see classification.) Matches "SAR CODIGO 111" (pattern 3.4): EXCLUDE — ISR withholding, not a contribution.

**Classification:** EXCLUDE — income tax withholding (Código 111). Computed annual ISR L 15,376.03; monthly L 1,281.34.

### Example 3 — High earner above the IHSS ceiling (RAP above-ceiling kicks in)

**Input line:**
`31.03.2025 ; RAP APORTACIONES PRIVADAS ; DEBITO ; SALARIO MARZO ; -881.55 ; HNL`

**Reasoning:**
Employee gross salary L 70,000/month, which exceeds the IHSS ceiling L 11,903.13. IHSS employee is capped at the ceiling (5.0% × 11,903.13 = L 595.16). The portion **above** the ceiling = 70,000 − 11,903.13 = **L 58,096.87** attracts RAP above-ceiling savings at 1.5% employee = 58,096.87 × 1.5% = **L 871.453 ≈ L 871.45** (employer matches 1.5%). The L 881.55 line is a RAP debit (pattern 3.2): EXCLUDE from ISV.

**Classification:** EXCLUDE — RAP above-ceiling contribution. Employee RAP ≈ L 871.45/month on the L 58,096.87 above-ceiling portion.

### Example 4 — INFOP employer levy (firm with 5+ employees)

**Input line:**
`10.02.2025 ; INFOP FORMACION PROFESIONAL ; DEBITO ; PLANILLA ENERO ; -1,500.00 ; HNL`

**Reasoning:**
Total monthly payroll L 150,000. INFOP = 1% of total payroll, employer-only, firms with 5+ employees → 150,000 × 1% = **L 1,500.00**. Due within 10 business days after month-end (this debit dated 10 Feb for January payroll is on-time). Matches "INFOP" (pattern 3.3): EXCLUDE from ISV. Employer expense, not deductible from any employee.

**Classification:** EXCLUDE — INFOP training levy (employer-only).

### Example 5 — Aguinaldo (13th month) paid in December

**Input line:**
`20.12.2025 ; AGUINALDO DICIEMBRE ; DEBITO ; PLANILLA 13ER MES ; -30,000.00 ; HNL`

**Reasoning:**
13th-month pay (aguinaldo) is a statutory bonus paid in December. Matches "AGUINALDO" (pattern 3.5): EXCLUDE from ISV — it is payroll, not a supply. ISR treatment: aguinaldo is exempt only up to **ten times the average minimum wage**; any excess is taxable at the employee's marginal rate. **[RESEARCH GAP — reviewer to confirm the exact "10× average minimum wage" exempt amount for 2025 before quantifying any taxable excess.]**

**Classification:** EXCLUDE from ISV — payroll/statutory bonus. ISR exempt up to 10× avg minimum wage; flag excess for reviewer.

### Example 6 — SAR ISR payment vs IHSS (do not confuse)

**Input line:**
`30.04.2025 ; SAR OFICINA VIRTUAL ; DEBITO ; ISR FORM 102 FY2024 ; -8,420.00 ; HNL`

**Reasoning:**
Matches "SAR" / "OFICINA VIRTUAL" (pattern 3.4). This is the **annual ISR return payment** (Form 102) for FY2024, due 30 April 2025 — an income-tax payment, NOT a social-security contribution. Do not classify as IHSS/RAP/INFOP. EXCLUDE from ISV.

**Classification:** EXCLUDE — income tax (ISR Form 102 settlement). NOT a contribution.

## Section 5 -- Tier 1 rules

Apply exactly as written when payslip/bank data is clear and inputs are available.

### Rule 1 — ISR base and medical deduction

- **ISR base and medical deduction** — annual_net_taxable_income = annual_gross_salary - 40,000   (flat medical deduction) ISR = progressive table applied to annual_net_taxable_income  _([Auxadi](https://www.auxadi.com/blog/2025/01/30/honduras-updates-income-tax/))_

The flat **L 40,000/year** medical-expense deduction is statutory, applied before the table.

### Rule 2 — ISR 2025 progressive computation (cumulative method)

- **ISR 2025 progressive computation** — income <= 217,493.16            -> ISR = 0 217,493.17 - 331,638.50         -> ISR = (income - 217,493.16) x 15% 331,638.51 - 771,252.38         -> ISR = 17,121.80 + (income - 331,638.50) x 20% income >= 771,252.39            -> ISR = 105,044.58 + (income - 771,252.38) x 25%  _(Acuerdo SAR-007-2025 ([SAR](https://www.sar.gob.hn/impuesto-sobre-renta-isr/)))_

Constants 17,121.80 and 105,044.58 are the recomputed cumulative tax at each boundary (see Section 1).

### Rule 3 — Monthly ISR withholding (Código 111 / Art. 22)

- **Monthly ISR withholding** — monthly_withholding = annual_ISR / 12

Employers withhold monthly under Art. 22 (Código 111). Salaried employees with only employment income need not file an annual return.

### Rule 4 — Use the correct year's table

- **Use the correct year's table** — FY2025 → Acuerdo SAR-007-2025. FY2026 → SAR Comunicado 02-2026 (effective 12 Jan 2026). Tables auto-adjust annually for CPI under Art. 22 (Decreto 20-2016).  _([Deloitte](https://www.deloitte.com/latam/es/services/tax/perspectives/hn-12ene26-sar-actualiza-tabla-progresiva-para-2026-honduras.html))_

### Rule 5 — IHSS contributions are capped at the ceiling

- **IHSS contributions capped at ceiling** — ihss_base = min(gross_monthly_salary, 11,903.13) employee_ihss = ihss_base x 5.0%       (IVM 2.5% + EM 2.5%) employer_ihss = ihss_base x 8.5%       (IVM 3.5% + EM 5.0%)  + ~0.2% occupational risk state_ihss    = ihss_base x 0.5%       (IVM state tranche)  _(Ceiling L 11,903.13/month for 2025 ([El Heraldo](https://www.elheraldo.hn/honduras/techo-ihss-aumento-1361-lempiras-trabajadores-aportaran-mas-dinero-AM23495401)))_

### Rule 6 — RAP has two distinct flows (Decreto 47-2024, in force 1 Jun 2024)

- **RAP two distinct flows** — rap_labor_reserve   = gross_salary x 4.0%   (EMPLOYER ONLY; capped at 3x highest minimum wage) above_ceiling_base  = max(gross_salary - 11,903.13, 0) rap_employee_above  = above_ceiling_base x 1.5% rap_employer_above  = above_ceiling_base x 1.5%  _([Mismo](https://mismo.team/honduras-payroll-guide-ihss-rap-infop-13th-14th/) · [Godoy Córdoba](https://godoycordoba.com/en/entra-en-vigencia-nueva-ley-del-fondo-de-reserva-laboral-de-capitalizacion-individual-y-ley-para-la-regulacion-de-las-aportaciones-y-cotizaciones-del-ihss/))_

The legacy 1.5% social-housing employee contribution is now **voluntary/optional** with no ceiling ([PwC](https://taxsummaries.pwc.com/honduras/individual/other-taxes)).

### Rule 7 — INFOP is employer-only, 1% of payroll, 5+ employees

- **INFOP formula** — infop = total_monthly_payroll x 1.0%   (only if firm has 5+ employees)  _(Due within 10 business days after month-end ([Mismo](https://mismo.team/honduras-payroll-guide-ihss-rap-infop-13th-14th/)))_

### Rule 8 — 13th and 14th month pay

- **13th and 14th month pay** — 13th month (aguinaldo) paid in December; 14th month paid by 30 June. ISR-exempt up to **10× average minimum wage**; excess taxable at marginal rate. **[RESEARCH GAP — confirm the exact 10× figure for the relevant year.]**  _([Mismo](https://mismo.team/honduras-payroll-guide-ihss-rap-infop-13th-14th/))_

### Rule 9 — Filing forms and deadlines

**Filing forms table**

| Form (SAR code) | Purpose |
| --- | --- |
| 102 | ISR Persona Natural (individuals) |
| 103 | ISR Persona Jurídica + Activo Neto + Aportación Solidaria (legal entities) |
| 106 | Cedular tax on rental income |
| 111 | Employee withholding (Art. 22) |

Annual ISR return due **30 April** following the tax year (FY2025 due 30 Apr 2026). Filed via SAR Oficina Virtual / DET Live ([SAR](https://www.sar.gob.hn/impuesto-sobre-renta-isr/)).

### Rule 10 — Contributions and ISR are separate obligations

- **Contributions and ISR separate obligations** — IHSS, RAP, and INFOP are social/labor contributions remitted to their respective institutes; ISR is income tax remitted to SAR. Never conflate them. Never net one against another.

## Section 6 -- Tier 2 catalogue

Flag these for reviewer confirmation when data is ambiguous.

### T2-1 — Salary straddling the IHSS ceiling

**Trigger:** Gross salary near or above L 11,903.13.
**Issue:** IHSS applies only up to the ceiling; the above-ceiling portion shifts to RAP at 1.5%/1.5%. Easy to over- or under-apply.
**Action:** Confirm exact gross and split base before computing. Flag.

### T2-2 — Occupational-risk (Riesgos Profesionales) rate

**Trigger:** Computing total employer cost.
**Issue:** The ~0.2% risk rate **varies by industry risk classification**; the exact rate is sector-specific.
**Action:** Flag for reviewer to confirm the firm's risk class. **[RESEARCH GAP — exact rate by class not in research.]**

### T2-3 — INFOP firm-size threshold

**Trigger:** Firm with around 5 employees.
**Issue:** INFOP applies to firms with 5+ employees; borderline headcount (part-timers, seasonal) affects liability.
**Action:** Confirm headcount basis. Flag.

### T2-4 — Aguinaldo / 14th-month taxable excess

**Trigger:** 13th/14th-month pay exceeds the exempt threshold.
**Issue:** Exempt only up to 10× average minimum wage; excess taxable at marginal rate. Exact 10× figure not confirmed in research.
**Action:** **[RESEARCH GAP]** — confirm the year's 10× average minimum wage before quantifying. Flag.

### T2-5 — Medical deduction beyond the flat L 40,000

**Trigger:** Client claims itemized medical or education expenses.
**Issue:** The skill applies the statutory flat L 40,000; other deductions (e.g., professional fees, education) may exist under the ISR law.
**Action:** Flag for reviewer to confirm available deductions for the year.

### T2-6 — Arrears, surcharges, and interest

**Trigger:** Unpaid IHSS/RAP/INFOP/ISR.
**Issue:** Late-filing surcharges (5%–20%), omission fine (40% of tax, floored at one minimum monthly salary), late-payment interest (~14% p.a., set periodically).
**Action:** Do not estimate. Escalate to a Honduran Contador Público Colegiado. **[RESEARCH GAP — confirm current interest rate.]**

## Section 7 -- Excel working paper template

```
HONDURAS PAYROLL / ISR COMPUTATION -- WORKING PAPER
Client / Employee: [name]
Tax Year:          [2025 / 2026]
Prepared:          [date]

INPUT DATA
  Gross monthly salary:          L [____]
  Annual gross salary:           L [____]
  Firm employee count (INFOP):   [____]
  Industry risk class (IHSS RP): [____]

ISR COMPUTATION (annual)
  Annual gross salary:           L [____]
  Less flat medical deduction:   L (40,000.00)
  Annual net taxable income:     L [____]
  Bracket applied:               [1 / 2 / 3 / 4]
  Annual ISR (cumulative method):L [____]
  Monthly withholding (/12):     L [____]   (Codigo 111)

IHSS (monthly, base = min(salary, 11,903.13))
  IHSS base:                     L [____]
  Employee 5.0% (IVM 2.5 + EM 2.5): L [____]
  Employer 8.5% (IVM 3.5 + EM 5.0): L [____]
  Occupational risk ~0.2%:       L [____]   [confirm class]
  State 0.5%:                    L [____]

RAP (monthly)
  Labor-reserve 4% (employer):   L [____]
  Above-ceiling base (sal - 11,903.13): L [____]
  RAP employee 1.5%:             L [____]
  RAP employer 1.5%:             L [____]

INFOP (monthly, if 5+ employees)
  1% of total payroll:           L [____]

NET PAY (monthly, employee side)
  Gross salary:                  L [____]
  Less employee IHSS:            L [____]
  Less employee RAP (above-ceiling): L [____]
  Less monthly ISR withholding:  L [____]
  Net pay:                       L [____]

REVIEWER FLAGS / RESEARCH GAPS
  [List Tier 2 flags and [RESEARCH GAP] markers here]
```

## Section 8 -- Bank statement reading guide

### How payroll debits appear on Honduran bank statements

**Banco Atlántida / Banco Ficohsa / BAC Credomatic / Banco de Occidente:**
- **IHSS:** "IHSS", "SEGURIDAD SOCIAL", "PLANILLA IHSS" — monthly, employer remits IVM + EM
- **RAP:** "RAP", "FONDO DE RESERVA LABORAL", "APORTACIONES PRIVADAS" — monthly
- **INFOP:** "INFOP", "FORMACION PROFESIONAL" — monthly, employer-only (5+ staff)
- **SAR / ISR:** "SAR", "ISR", "CODIGO 111", "OFICINA VIRTUAL", "DET LIVE" — withholding monthly; annual settlement around 30 April

**Key identification tips:**
1. Contribution debits (IHSS/RAP/INFOP) are outgoing, recur monthly, and go to the named institute — not to SAR.
2. SAR debits are **tax** (ISR/ISV), never social security. Código 111 = employee ISR withholding.
3. Amounts are in Lempira (L / HNL); watch for thousands separators ("." or "," vary by bank).
4. Aguinaldo/14th-month appear as large December and June payroll debits — statutory bonus, not contributions.
5. IHSS amounts cap out near L 595.16 employee / L 1,011.77 employer per worker (5.0% / 8.5% × L 11,903.13) — values much higher per worker suggest above-ceiling RAP or aggregated planillas.

## Section 9 -- Onboarding fallback

If the client provides only a bank statement and no payslip detail:

1. **Scan for institute debits** — identify IHSS, RAP, INFOP, and SAR lines per Section 3.
2. **Separate tax from contributions** — SAR/ISR/Código 111 lines are income tax; IHSS/RAP/INFOP are contributions.
3. **Reverse-engineer salary band (rough):**
   - IHSS employee ≈ L 595.16/worker → salary at or above the ceiling (L 11,903.13).
   - IHSS employee < L 595.16 → salary below the ceiling; salary ≈ (employee IHSS ÷ 5.0%).
   - Presence of RAP above-ceiling debits → salary exceeds L 11,903.13.
   - Monthly Código 111 withholding > 0 → annual income above the ISR exempt threshold (monthly salary > L 21,457.76 in 2025).
4. **Flag for reviewer:** "Salary band and ISR derived from bank-statement amounts only. Gross salary, firm size, and risk class have not been independently verified. Reviewer must confirm before filing."

### ISR 2025 calculation examples (recomputed end-to-end)

**ISR 2025 calculation examples (recomputed end-to-end)**  _(Acuerdo SAR-007-2025)_

| Annual gross (L) | Less L 40k → net taxable (L) | Bracket | Annual ISR (L) | Monthly withholding (L) |
| --- | --- | --- | --- | --- |
| 240,000 | 200,000 | 1 (0%) | 0.00 | 0.00 |
| 300,000 | 260,000 | 2 (15%) | (260,000 − 217,493.16) × 15% = 42,506.84 × 15% = **6,376.03** | 531.34 |
| 360,000 | 320,000 | 2 (15%) | (320,000 − 217,493.16) × 15% = 102,506.84 × 15% = **15,376.03** | 1,281.34 |
| 500,000 | 460,000 | 3 (20%) | 17,121.80 + (460,000 − 331,638.50) × 20% = 17,121.80 + 25,672.30 = **42,794.10** | 3,566.18 |
| 1,000,000 | 960,000 | 4 (25%) | 105,044.58 + (960,000 − 771,252.38) × 25% = 105,044.58 + 47,186.91 = **152,231.49** | 12,685.96 |

Bracket constants per Section 1 (Acuerdo SAR-007-2025). Each row's arithmetic is self-contained above.

### IHSS / RAP / INFOP quick figures (2025)

**IHSS / RAP / INFOP quick figures (2025)**  _([El Heraldo](https://www.elheraldo.hn/honduras/techo-ihss-aumento-1361-lempiras-trabajadores-aportaran-mas-dinero-AM23495401); [Mismo](https://mismo.team/honduras-payroll-guide-ihss-rap-infop-13th-14th/))_

| Item | Value | Source |
| --- | --- | --- |
| IHSS monthly ceiling | L 11,903.13 | [El Heraldo](https://www.elheraldo.hn/honduras/techo-ihss-aumento-1361-lempiras-trabajadores-aportaran-mas-dinero-AM23495401) |
| Employee IHSS at ceiling (5.0%) | L 595.16 (= 11,903.13 × 0.05 = 595.1565) | derived |
| Employer IHSS at ceiling (8.5%) | L 1,011.77 (= 11,903.13 × 0.085 = 1,011.766) | derived |
| State IHSS at ceiling (0.5%) | L 59.52 (= 11,903.13 × 0.005) | derived |
| RAP labor-reserve | 4% employer; cap 3× highest min wage | [Mismo](https://mismo.team/honduras-payroll-guide-ihss-rap-infop-13th-14th/) |
| RAP above-ceiling | 1.5% employee + 1.5% employer | [Mismo](https://mismo.team/honduras-payroll-guide-ihss-rap-infop-13th-14th/) |
| INFOP | 1% payroll, employer-only, 5+ staff | [Mismo](https://mismo.team/honduras-payroll-guide-ihss-rap-infop-13th-14th/) |

### Minimum wage (2025, selected — Acuerdo SETRASS-109-2024)

**Minimum wage (2025, selected — Acuerdo SETRASS-109-2024)**  _([Secretaría de Trabajo — Tabla salario mínimo 2025](https://www.trabajo.gob.hn/tabla-de-salario-minimo/) · [La Prensa](https://www.laprensa.hn/economia/honduras-salario-minimo-comercio-construccion-2025-CN23485373))_

| Sector / size | Monthly (L) |
| --- | --- |
| Commerce & Construction, 1–10 workers | 12,539.68 |
| Commerce & Construction, 11–50 | 12,937.94 |
| Commerce & Construction, 51–150 | 15,395.21 |
| Commerce & Construction, 151+ | 17,557.35 |
| Textile / Maquila | 11,972.29 |
| Financial system (large firms) | 18,036.19 |

Sector- and size-banded; no single national figure. 2025 figures remained in effect into early 2026. Source: [Secretaría de Trabajo — Tabla salario mínimo 2025](https://www.trabajo.gob.hn/tabla-de-salario-minimo/) · [La Prensa](https://www.laprensa.hn/economia/honduras-salario-minimo-comercio-construccion-2025-CN23485373).

### Penalties (Código Tributario, Decreto 22-97 consolidated)

**Penalties (Código Tributario, Decreto 22-97 consolidated)**  _([Código Tributario (Decreto 22-97), TSC](https://www.tsc.gob.hn/web/leyes/C%C3%B3digo%20Tributario.pdf) · [Texto Consolidado, SEFIN](http://www.sefin.gob.hn/wp-content/uploads/2018/06/Texto_Consolidado_Codigo_Tributario_25JUNIO2018_Y_ANEXOS.pdf) · [PwC — Tax administration](https://taxsummaries.pwc.com/honduras/individual/tax-administration))_

| Penalty | Rate |
| --- | --- |
| Late filing ≤ 1 month | 5% of tax due |
| Late filing > 1 to 2 months | 10% |
| Late filing > 2 to 3 months | 15% |
| Late filing > 3 months | 20% |
| Omission of a return | 40% of tax determined (floor: 1 minimum monthly salary; certain late-filing fines floor at 2 minimum salaries) |
| Late-payment interest | ~14% p.a. — **[RESEARCH GAP — set periodically; confirm current rate]** |
| ISV late filing | 1% if within 5 days, then 2%/month, capped 24% |

### Other context

- **Sales Tax (ISV) general rate** — 15% percent (general rate)  _([PwC — Other taxes](https://taxsummaries.pwc.com/honduras/corporate/other-taxes))_
- **Sales Tax (ISV) premium services rate** — 18% percent (certain premium services (alcohol, tobacco, premium telecom))  _([PwC — Other taxes](https://taxsummaries.pwc.com/honduras/corporate/other-taxes))_
- **Territorial taxation basis** — Honduras taxes on a territorial basis — Honduran-source income only.  _(Other context)_

### Test suite

**Test 1:** Annual gross L 240,000 → net taxable L 200,000 → bracket 1. **ISR = L 0.00.** (200,000 ≤ 217,493.16.)

**Test 2:** Annual gross L 300,000 → net L 260,000 → bracket 2. ISR = (260,000 − 217,493.16) × 15% = 42,506.84 × 15% = **L 6,376.03**. Monthly = **L 531.34**.

**Test 3:** Annual gross L 360,000 → net L 320,000 → bracket 2. ISR = 102,506.84 × 15% = **L 15,376.03**. Monthly = **L 1,281.34**.

**Test 4:** Annual gross L 500,000 → net L 460,000 → bracket 3. ISR = 17,121.80 + (460,000 − 331,638.50) × 20% = 17,121.80 + 25,672.30 = **L 42,794.10**. Monthly = **L 3,566.18**.

**Test 5:** Annual gross L 1,000,000 → net L 960,000 → bracket 4. ISR = 105,044.58 + (960,000 − 771,252.38) × 25% = 105,044.58 + 47,186.91 = **L 152,231.49**. Monthly = **L 12,685.96**.

**Test 6:** Salary L 12,000/month. IHSS base = min(12,000, 11,903.13) = 11,903.13. Employee IHSS = 11,903.13 × 5.0% = **L 595.16**. Employer = × 8.5% = **L 1,011.77**.

**Test 7:** Salary L 70,000/month. IHSS employee capped = **L 595.16**. Above-ceiling base = 70,000 − 11,903.13 = 58,096.87. RAP employee 1.5% = **L 871.45**; RAP employer 1.5% = **L 871.45**.

**Test 8:** Firm with total payroll L 150,000/month, 8 employees. INFOP = 150,000 × 1% = **L 1,500.00** (employer-only).

**Test 9:** Net pay for an employee on L 30,000/month (2025). Monthly ISR withholding = L 1,281.34 (Test 3). Employee IHSS = 595.16 (salary > ceiling, capped). Above-ceiling base = 30,000 − 11,903.13 = 18,096.87; RAP employee 1.5% = **L 271.45**. Net pay = 30,000 − 1,281.34 − 595.16 − 271.45 = **L 27,852.05**.

### Prohibitions

- **Never compute without gross salary** — NEVER compute ISR or contributions without the client's gross salary in HNL.  _(Prohibitions)_
- **Never use pre-reform IHSS ceilings** — NEVER use the pre-reform PwC IHSS ceilings (L 11,109.36 / L 11,336.00) for 2025 — use L 11,903.13.  _(Prohibitions)_
- **IHSS caps at ceiling; RAP above-ceiling applies to excess only** — NEVER apply IHSS or RAP-above-ceiling to salary beyond the L 11,903.13 ceiling incorrectly — IHSS caps AT the ceiling, RAP above-ceiling applies to the EXCESS only.  _(Prohibitions)_
- **Never conflate institutes** — NEVER conflate IHSS, RAP, INFOP, and SAR/ISR — they are separate institutes and obligations.  _(Prohibitions)_
- **Never omit medical deduction** — NEVER omit the flat L 40,000 medical deduction before applying the ISR table.  _(Prohibitions)_
- **Never apply wrong year table** — NEVER apply the 2026 table to FY2025 work, or vice versa.  _(Prohibitions)_
- **Never quantify aguinaldo/14th-month taxable excess without confirmation** — NEVER quantify aguinaldo/14th-month taxable excess without confirming the 10× average-minimum-wage exempt figure — it is a marked research gap.  _(Prohibitions)_
- **Never estimate arrears/interest without official statements** — NEVER estimate arrears, surcharges, or late-payment interest without official SAR/IHSS statements — escalate.  _(Prohibitions)_
- **Never present as definitive; Tier 2 disclosure** — NEVER present figures as definitive — this is a Tier 2 (research-verified, not professionally verified) skill; direct clients to official SAR/IHSS statements and a Honduran Contador Público Colegiado.  _(Prohibitions)_

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a CPA, EA, tax attorney, Contador Público Colegiado, or equivalent licensed practitioner in your jurisdiction) before filing or acting upon.

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
