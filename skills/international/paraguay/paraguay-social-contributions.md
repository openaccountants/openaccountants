---
name: paraguay-social-contributions
description: Use this skill whenever asked about Paraguay IPS social security contributions (aportes IPS) for employed persons, domestic workers, or independent contributors. Trigger on phrases like "aportes IPS", "IPS Paraguay", "social security Paraguay", "aporte obrero", "aporte patronal", "9% IPS", "16.5% IPS", "25.5% IPS", "Instituto de Previsión Social", "trabajo doméstico IPS", "domestic worker social security Paraguay", "empleada doméstica aportes", "REI Paraguay", "planilla de aporte obrero-patronal", "número patronal", "IPS deadline", "recargos IPS", "salario mínimo Paraguay IPS base", "how much IPS do I pay", or any question about computing or classifying IPS social-security contributions for a Paraguay-based worker. Also trigger when classifying bank statement transactions that relate to IPS debits or aporte obrero-patronal payments from Paraguayan banks (Itaú, Continental, Visión, Regional, Ueno). This skill covers the general-regime employee/employer rates, the post-2019 domestic-worker rate, the contribution base, the minimum-wage floor, monthly REI filing, payment deadlines by número patronal, surcharges, and edge cases. ALWAYS read this skill before touching any Paraguay IPS work.
version: 0.1
jurisdiction: PY
tax_year: 2025
last_updated: 2026-07-13
review_status: pending_review
depends_on:
  - social-contributions-workflow-base
category: international
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Paraguay IPS Social Security Contributions (Aportes)

## Paraguay IPS Social Security Contributions (Aportes) -- Skill v0.1

Paraguay IPS Social Security Contributions (Aportes) -- Skill v0.1

## Tier 2 status disclaimer

> **Tier 2 status.** Every rate, threshold, and deadline below is sourced to a named authority (IPS, SET/DNIT, MTESS, BACN) or a Big-4 summary (PwC Worldwide Tax Summaries) and cited inline. It has **not** yet been section-by-section verified by a licensed Paraguayan accountant (contador público). Items marked **[RESEARCH GAP — reviewer to confirm]** carry residual uncertainty and must be confirmed against primary sources before reliance.

## READ THIS FIRST — the single most important rate fact

- **Domestic worker rate equals general rate since Law 6.338/2019** — Since Law N° 6.338/2019 (modifying Art. 10 of Law N° 5.407/2015 — Del Trabajo Doméstico), domestic workers contribute to IPS at the SAME full general rate as ordinary private-sector employees: 9% employee (obrero) + 16.5% employer (patronal) = 25.5%. The old pre-2019 reduced rate of 2.5% / 5.5% (8% total) is superseded — do NOT use it. There is no differentiated "28% bank/financial-entity IPS rate"; historically bank employees were affiliated to a separate pension fund (Caja Bancaria), not charged a higher IPS tariff. See Sections 1, 5, and the flags in Section 10.  _(Law N° 6.338/2019; Law N° 5.407/2015 Art.10)_

## Section 1 -- Quick reference

**Read this whole section before computing or classifying anything.**

**Quick reference table**

| Field | Value |
| --- | --- |
| Country | Paraguay (República del Paraguay) |
| Primary Legislation | Law N° 98/1992 (IPS contributions, surcharges); IPS Carta Orgánica |
| Supporting Legislation | Law N° 213/1993 (Código del Trabajo); Law N° 1286 (amends IPS laws); Law N° 5.407/2015 (Trabajo Doméstico); Law N° 6.338/2019 (domestic-worker rate → general rate) |
| Social-security authority | IPS — Instituto de Previsión Social (collects/administers contributions) |
| Tax authority (income-tax interaction) | SET / DNIT — Dirección Nacional de Ingresos Tributarios |
| Labour / minimum-wage authority | MTESS — Ministerio de Trabajo, Empleo y Seguridad Social |
| Currency | PYG (guaraní, ₲) only |
| Employee rate (aporte obrero, withheld) | **9.0%** of gross remuneration |
| Employer rate (aporte patronal) | **16.5%** of gross remuneration |
| Combined general rate | **25.5%** |
| Employer 16.5% breakdown | 14% to IPS proper + 2.5% earmarked for public-health/training funds (e.g. SENEPA, SNPP, SINAFOCAL) |
| Domestic-worker rate (post 1 Jul 2019) | **Same as general: 9% / 16.5% = 25.5%** (Law 6.338/2019) |
| Contribution base | Total remuneration in cash or in kind (salary, overtime, commissions, regalías, bonuses); EXCLUDES aguinaldo and family allowance |
| Base floor | Legal minimum wage |
| Base ceiling | No general-regime salary ceiling confirmed — **[RESEARCH GAP — reviewer to confirm]**; treat as uncapped |
| Monthly minimum wage (from 1 Jul 2025) | ₲ 2.899.048 (MTESS Resolución N° 677/2025) |
| Filing system | REI — Registro Electrónico de Información (monthly planilla) |
| Payment frequency | Monthly |
| Deadline | Monthly, staggered by last digit of the employer's número patronal (first business days of the following month) |
| Late payment | Recargos (surcharges) + daily interest (Law N° 98/1992) |
| Validated by | Pending — requires sign-off by a Paraguayan contador público |
| Validation date | Pending |

**Regime overview (rates)**

| Regime | Employee | Employer | Total |
| --- | --- | --- | --- |
| General (private salaried) | 9.0% | 16.5% | **25.5%** |
| Domestic workers (since 1 Jul 2019, Law 6.338/19) | 9.0% | 16.5% | **25.5%** |
| Independent / self-employed (voluntary) | 13% (self-paid) | — | **13%** *(secondary — see §10; [RESEARCH GAP])* |

**Total-row check (recomputed):** general 9.0 + 16.5 = **25.5** ✓; domestic 9.0 + 16.5 = **25.5** ✓. Both additions reconcile.

**Conservative defaults**

| Ambiguity | Default |
| --- | --- |
| Unknown worker category | Assume general regime (9% / 16.5%) |
| Domestic worker, unsure which rate | Use general 9% / 16.5% (post-2019); NEVER the old 2.5% / 5.5% |
| Bank/financial-sector worker | Flag — confirm whether affiliated to a separate caja, not a higher IPS rate (see §10) |
| Unknown gross wage | Apply the minimum-wage floor (₲ 2.899.048/month) |
| Wage below minimum wage | Contribution base = at least the proportional minimum wage |
| Unknown whether aguinaldo/family allowance included | Exclude both from the IPS base |
| Unknown ceiling | Treat IPS as uncapped on the full wage |

## Section 2 -- Required inputs and refusal catalogue

### Required inputs

**Minimum viable** -- worker category (general employee / domestic worker / independent) and gross monthly remuneration. Without the gross wage, apply the minimum-wage floor and flag.

**Recommended** -- breakdown of remuneration (base salary, overtime, commissions, in-kind), whether the worker is registered with IPS, and the employer's número patronal (for deadline determination).

**Ideal** -- the monthly REI planilla, payslips, bank statements showing IPS obrero-patronal debits, and the IPS *certificado de no adeudar*.

### Refusal catalogue

- **R-PY-IPS-1 -- Domestic-worker old rate requested** — Trigger: user asks to apply the pre-2019 2.5% / 5.5% reduced domestic-worker rate. Message: "That rate is superseded. Since Law N° 6.338/2019 (effective 1 July 2019), domestic workers contribute at the full general IPS rate: 9% employee + 16.5% employer = 25.5%. The 8% reduced rate is no longer valid."  _(Law N° 6.338/2019)_
- **R-PY-IPS-2 -- Bank/financial 28% IPS rate requested** — Trigger: user asks to apply an 11% / 17% (28%) special IPS rate for banks or financial entities. Message: "There is no differentiated 28% IPS tariff. Bank employees were historically affiliated to a separate pension fund (Caja Bancaria), not charged a higher IPS rate. Some third-party summaries publish 11% / 17%, but the IPS general regime is 9% / 16.5%. Escalate to a Paraguayan contador público to confirm fund affiliation before computing."
- **R-PY-IPS-3 -- Surcharge / mora quantification** — Trigger: client has unpaid IPS and wants the exact recargo and interest computed. Message: "IPS late-payment surcharges (recargos moratorios) and daily interest under Law N° 98/1992 require the IPS account statement and the official IPS surcharge schedule. Do not estimate. Escalate to a Paraguayan contador público."  _(Law N° 98/1992)_
- **R-PY-IPS-4 -- Non-standard regimes (ANDE, Magisterio, pensioners)** — Trigger: worker is an ANDE employee, public teacher (Magisterio), or pensioner with a non-general rate. Message: "Special-regime IPS rates (ANDE, public teachers, pensioners) are outside this skill's verified scope and carry lower-confidence figures. Escalate to a Paraguayan contador público."

## Section 3 -- Payment pattern library

This is the deterministic pre-classifier for bank-statement transactions related to IPS social security. When a transaction matches a pattern below, apply the treatment directly. Do not second-guess.

**How to read this table.** Match by case-insensitive substring on the counterparty/reference as it appears in the bank statement. IPS payments always EXCLUDE from any IVA return or revenue/expense classification as a taxable supply — they are statutory social-security obligations (the employer share is a deductible payroll cost; the employee share is withheld from the worker's wage).

### 3.1 IPS obrero-patronal debits

**IPS obrero-patronal debits table**

| Pattern | Treatment | Notes |
| --- | --- | --- |
| IPS, I.P.S. | EXCLUDE -- IPS contribution | Monthly aporte obrero-patronal |
| INSTITUTO DE PREVISION SOCIAL | EXCLUDE -- IPS contribution | Full authority name |
| APORTE OBRERO, APORTE PATRONAL | EXCLUDE -- IPS contribution | Explicit aporte reference |
| OBRERO PATRONAL, OBRERO-PATRONAL | EXCLUDE -- IPS contribution | Combined reference |
| PLANILLA IPS, REI IPS | EXCLUDE -- IPS contribution | Planilla / REI reference |
| SEGURIDAD SOCIAL | EXCLUDE -- IPS contribution | Spanish-language reference |

### 3.2 IPS debits appearing on specific Paraguayan banks

**IPS debits by bank table**

| Bank | Typical debit description | Treatment |
| --- | --- | --- |
| Banco Itaú Paraguay | "IPS" or "APORTE IPS" or "INSTITUTO PREVISION SOCIAL" | EXCLUDE -- IPS |
| Banco Continental | "IPS OBRERO PATRONAL" or "IPS" | EXCLUDE -- IPS |
| Visión Banco | "IPS" or "SEGURIDAD SOCIAL" | EXCLUDE -- IPS |
| Banco Regional / Sudameris | "APORTE IPS" or "IPS" | EXCLUDE -- IPS |
| Ueno Bank | "IPS" or "PLANILLA IPS" | EXCLUDE -- IPS |

### 3.3 Tax payments (NOT IPS -- do not confuse)

**Tax payments table**

| Pattern | Treatment | Notes |
| --- | --- | --- |
| SET, DNIT | EXCLUDE -- tax payment, not IPS | SET/DNIT income tax / IVA |
| MARANGATU, MARANGATÚ | EXCLUDE -- tax portal payment | IRP/IVA, not social security |
| IRP, IVA | EXCLUDE -- tax, not IPS | Income tax / VAT |
| FORMULARIO 515 | EXCLUDE -- IRP self-assessment | Not an IPS contribution |

### 3.4 Salary and payroll (exclude from IPS classification)

**Salary and payroll exclusion table**

| Pattern | Treatment | Notes |
| --- | --- | --- |
| SUELDO, SALARIO, PAGO HABERES (outgoing) | EXCLUDE -- payroll expense | Not an IPS payment |
| SUELDO, SALARIO (incoming) | EXCLUDE -- employment income received | Not an IPS payment |
| AGUINALDO | EXCLUDE -- 13th-salary payroll | NOT in the IPS base |

### 3.5 IPS benefits received (not contributions)

**IPS benefits received table**

| Pattern | Treatment | Notes |
| --- | --- | --- |
| JUBILACION IPS, PENSION IPS | EXCLUDE -- pension income received | Not a contribution paid |
| SUBSIDIO IPS, REPOSO IPS | EXCLUDE -- sickness/maternity subsidy received | Not a contribution |

## Section 4 -- Worked examples

Six worked examples in guaraní (₲) for a hypothetical Paraguayan employer. **Every figure reconciles to the cent (well, to the guaraní — the guaraní has no subunit in practice).**

### Example 1 -- General employee at the minimum wage

**Input:** General-regime employee, gross monthly wage = the minimum wage ₲ 2.899.048.

**Reasoning:**
- Aporte obrero (9%) = 2.899.048 × 0,09 = **₲ 260.914,32** → withheld from wage.
- Aporte patronal (16.5%) = 2.899.048 × 0,165 = **₲ 478.342,92** → employer's own funds.
- Total IPS (25.5%) = 2.899.048 × 0,255 = **₲ 739.257,24**.
- Check: 260.914,32 + 478.342,92 = **739.257,24** ✓.

**Classification:** Obrero ₲ 260.914 withheld; patronal ₲ 478.343 employer cost; total ₲ 739.257 remitted via REI.

### Example 2 -- General employee above minimum wage

**Input:** General-regime employee, gross monthly wage = ₲ 5.000.000.

**Reasoning:**
- Aporte obrero (9%) = 5.000.000 × 0,09 = **₲ 450.000**.
- Aporte patronal (16.5%) = 5.000.000 × 0,165 = **₲ 825.000**.
- Total IPS (25.5%) = 5.000.000 × 0,255 = **₲ 1.275.000**.
- Check: 450.000 + 825.000 = **1.275.000** ✓.

**Classification:** Obrero ₲ 450.000 withheld; patronal ₲ 825.000 employer cost; total ₲ 1.275.000.

### Example 3 -- Domestic worker (post-2019 general rate)

**Input:** Domestic worker (empleada doméstica), gross monthly wage = ₲ 2.899.048 (minimum wage).

**Reasoning:**
- Since Law 6.338/2019, the domestic-worker rate equals the general rate. Do **not** apply the old 2.5% / 5.5%.
- Aporte obrero (9%) = 2.899.048 × 0,09 = **₲ 260.914,32**.
- Aporte patronal (16.5%) = 2.899.048 × 0,165 = **₲ 478.342,92**.
- Total (25.5%) = **₲ 739.257,24**.
- Check: 260.914,32 + 478.342,92 = **739.257,24** ✓.

**Classification:** Identical to a general employee at the same wage. EXCLUDE from IVA; remit via REI.

### Example 4 -- Domestic worker — WRONG old rate flagged

**Input:** A prior worksheet computed a domestic worker's IPS at 2.5% obrero / 5.5% patronal on ₲ 2.899.048.

**Reasoning:**
- Old (wrong) figures: obrero 2.899.048 × 0,025 = ₲ 72.476,20; patronal × 0,055 = ₲ 159.447,64; total 8% = ₲ 231.923,84.
- These are **superseded** by Law 6.338/2019. Correct figures are those in Example 3 (9% / 16.5% = 25.5% = ₲ 739.257,24).
- Understatement = 739.257,24 − 231.923,84 = **₲ 507.333,40** per month.

**Classification:** REJECT the worksheet. Re-compute at 9% / 16.5%. Flag the prior understatement and potential IPS arrears/recargos for reviewer.

### Example 5 -- SET/DNIT tax debit (NOT IPS)

**Input line:**
`10.05.2026 ; DNIT MARANGATU ; DEBIT ; IVA ABRIL ; -1.800.000 ; PYG`

**Reasoning:**
Matches "DNIT" / "MARANGATU" (pattern 3.3). This is an IVA tax payment, not an IPS contribution. Do not classify as social security.

**Classification:** EXCLUDE -- tax payment. NOT IPS.

### Example 6 -- Bank-sector worker (no special 28% rate)

**Input:** Employer asks the IPS rate for a bank employee, expecting "11% / 17% = 28%".

**Reasoning:**
- There is **no** differentiated 28% IPS tariff. Bank employees were historically affiliated to a separate pension fund (Caja Bancaria), not charged a higher IPS rate.
- If the worker is in fact within the IPS general regime, the rate is 9% / 16.5% = 25.5% (as Example 1/2).
- The 11% / 17% figure appears in some third-party summaries (e.g. PwC) but reflects the separate bank-fund framing, not an IPS sub-rate.

**Classification:** Do NOT author a 28% IPS computation. Flag for reviewer to confirm fund affiliation (IPS general regime vs Caja Bancaria) before computing.

## Section 5 -- Tier 1 rules

These rules apply when worker category and remuneration are clear. Apply exactly as written.

### Rule 1 -- General-regime IPS formula

- **General-regime IPS formula** — Aporte obrero   = base × 9.0%      (withheld from the worker's wage) Aporte patronal = base × 16.5%     (paid from the employer's own funds) Total IPS       = base × 25.5% Where `base` = total remuneration in cash or in kind, with a floor of the legal minimum wage.  _(Law N° 98/1992; IPS Carta Orgánica)_

### Rule 2 -- Domestic workers use the SAME general rate

- **Domestic workers use same general rate** — Since Law N° 6.338/2019 (effective 1 July 2019), domestic workers contribute at 9% obrero / 16.5% patronal = 25.5%, identical to general employees. The pre-2019 reduced rate (2.5% / 5.5% = 8%) is superseded and must never be used.  _(Law N° 6.338/2019)_

### Rule 3 -- No special bank/financial 28% IPS rate

- **No special bank/financial 28% IPS rate** — Do not author a differentiated 11% / 17% (28%) IPS rate. Bank-sector pension was historically a separate fund (Caja Bancaria), not a higher IPS tariff. Within the IPS general regime the rate is 9% / 16.5%.

### Rule 4 -- Contribution base

- **Contribution base** — The base is total remuneration in cash or in kind: ordinary salary, overtime, commissions, regalías, bonuses/premios. Excluded: aguinaldo (13th-month bonus) and family allowance (asignación familiar).

### Rule 5 -- Minimum-wage floor

- **Minimum-wage floor** — The base may not fall below the legal minimum wage (₲ 2.899.048/month from 1 Jul 2025). A worker earning below the minimum wage still contributes on at least the proportional minimum-wage base.

### Rule 6 -- No confirmed ceiling

- **No confirmed ceiling** — No general-regime salary ceiling is confirmed — [RESEARCH GAP — reviewer to confirm]. Treat IPS as uncapped on the full wage absent contrary authority.

### Rule 7 -- Employee share is withheld; employer share is not deducted from pay

- **Employee share withheld, employer share not deducted** — The employer withholds only the 9% obrero share from the wage. It is unlawful to deduct the 16.5% patronal share from the worker's pay — that must come from the employer's own funds. The employer remits both shares together.

### Rule 8 -- Monthly filing via REI

- **Monthly filing via REI** — The employer generates the monthly planilla (planilla de aporte obrero-patronal) in the REI (Registro Electrónico de Información) system, which auto-calculates 16.5% patronal + 9% obrero, registers personnel movements, and produces the certificado de no adeudar.

### Rule 9 -- Payment deadline by número patronal

- **Payment deadline by número patronal** — Contributions are paid monthly through authorized banks (Itaú, Continental, Visión Banco, Regional, etc.). The due date is staggered by the last digit of the employer's número patronal (first business days of the following month). If the due date falls on a non-business day, it rolls to the next business day.

### Rule 10 -- Aguinaldo and family allowance are IPS-exempt

- **Aguinaldo and family allowance IPS-exempt** — Neither the aguinaldo (mandatory 13th-month bonus) nor the family allowance (asignación familiar) is part of the IPS base. Do not include them in the contribution computation.

## Section 6 -- Tier 2 catalogue

When worker circumstances are unclear, flag these situations for reviewer confirmation.

### T2-1 -- Bank / financial-sector affiliation

- **Bank/financial-sector affiliation** — Trigger: Worker is employed by a bank or financial entity. Issue: Bank employees may be affiliated to a separate pension fund (Caja Bancaria) rather than the IPS general regime. Some summaries publish an 11% / 17% (28%) figure that reflects the separate fund, not an IPS sub-rate. Action: Flag for reviewer. Confirm fund affiliation before computing. Do not author a 28% IPS rate.

### T2-2 -- Domestic worker registered before July 2019

- **Domestic worker registered before July 2019** — Trigger: A domestic worker was registered under the old reduced rate. Issue: From 1 July 2019 the general rate (9% / 16.5%) applies. Worksheets carried over from before the change may still use 2.5% / 5.5% and understate contributions. Action: Re-compute at 9% / 16.5%. Flag any historical understatement and possible arrears/recargos for reviewer.

### T2-3 -- In-kind remuneration valuation

- **In-kind remuneration valuation** — Trigger: Part of remuneration is paid in kind (housing, meals, goods). Issue: In-kind remuneration is part of the IPS base, but its valuation can be contested. Action: Flag for reviewer to confirm the valuation method before computing.

### T2-4 -- Independent / self-employed voluntary affiliation

- **Independent / self-employed voluntary affiliation** — Trigger: Worker is self-employed and wishes to contribute voluntarily. Issue: The independent regime (commonly cited at 13% on a base not below the minimum wage) is secondary and lower-confidence — [RESEARCH GAP — reviewer to confirm]. Action: Flag for reviewer. Do not rely on the 13% figure without confirmation.

### T2-5 -- Wage below the minimum wage / part-time

- **Wage below minimum wage / part-time** — Trigger: Worker earns below the minimum wage, or is part-time. Issue: The minimum-wage floor still applies; part-time domestic-worker registration has its own IPS treatment. Action: Apply at least the proportional minimum-wage base; flag part-time cases for reviewer.

### T2-6 -- IPS arrears / mora patronal

- **IPS arrears / mora patronal** — Trigger: Employer has unpaid IPS from prior months. Issue: Recargos moratorios and daily interest under Law N° 98/1992 accrue. The exact amount needs the IPS statement and surcharge schedule. Action: Do not estimate. Escalate to a Paraguayan contador público.  _(Law N° 98/1992)_

## Section 7 -- Working paper template

When producing an IPS computation, structure the working paper as follows:

```
PARAGUAY IPS CONTRIBUTION -- WORKING PAPER
Client / Employer: [name]
Período (month/year): [____]
Número patronal: [____]
Prepared: [date]

INPUT DATA
  Worker category:               [General / Domestic / Independent]
  Gross monthly remuneration:    ₲ [____]
  In-kind component:             ₲ [____]
  Aguinaldo / family allowance:  EXCLUDED from base
  Minimum-wage floor applied:    [YES/NO]  (₲ 2.899.048 from 1 Jul 2025)

COMPUTATION (general / domestic regime)
  Contribution base:             ₲ [____]
  Aporte obrero (9.0%):          ₲ [____]   (withheld from wage)
  Aporte patronal (16.5%):       ₲ [____]   (employer funds)
  Total IPS (25.5%):             ₲ [____]
  Reconciliation check:          obrero + patronal = total?  [✓]

FILING & PAYMENT
  REI planilla generated:        [YES/NO]
  Deadline (by último dígito of número patronal): [____]
  Bank channel:                  [Itaú / Continental / Visión / Regional / ...]

REVIEWER FLAGS
  [List any Tier 2 flags here]

CONSERVATIVE DEFAULTS APPLIED
  [List any defaults applied and their impact]
```

## Section 8 -- Bank statement reading guide

### How IPS debits appear on Paraguayan bank statements

**Banco Itaú Paraguay:** "IPS", "APORTE IPS", "INSTITUTO PREVISION SOCIAL". Monthly, around the first business days of the following month.

**Banco Continental:** "IPS OBRERO PATRONAL" or "IPS". Same monthly cycle.

**Visión Banco:** "IPS" or "SEGURIDAD SOCIAL". Same cycle.

**Banco Regional / Sudameris / Ueno:** "APORTE IPS", "IPS", "PLANILLA IPS".

**Key identification tips:**
1. IPS debits are always outgoing (DEBIT), never credits (credits like "JUBILACION IPS" or "SUBSIDIO IPS" are benefits received).
2. They recur monthly. The amount should equal 25.5% of the total planilla base for that month.
3. The amount may differ month to month as headcount or wages change.
4. Do not confuse with SET/DNIT/Marangatú debits (income tax / IVA) or salary outflows.
5. Aguinaldo payments (December) are payroll, NOT in the IPS base — do not treat an aguinaldo outflow as an IPS contribution.

## Section 9 -- Onboarding fallback

If the client provides only a bank statement and no other information:

1. **Scan for IPS debits** -- identify all outgoing payments matching Section 3 patterns.
2. **Sum monthly IPS paid** -- total all IPS debits per month.
3. **Reverse-engineer the planilla base:**
   - Base ≈ monthly IPS total ÷ 0,255 (since total = 25.5% of base).
   - Implied employee share = base × 9%; employer share = base × 16.5%.
4. **Flag for reviewer:** "IPS figures derived from bank-statement amounts only. Worker category (general vs domestic vs bank-fund), remuneration breakdown, and número patronal have not been independently verified. Reviewer must confirm before filing the REI planilla."

## Section 10 -- Reference material

### Rate summary (2025)

**Rate summary table**

| Regime | Employee | Employer | Total | Legal basis |
| --- | --- | --- | --- | --- |
| General private-sector | 9.0% | 16.5% | **25.5%** | Law 98/1992; IPS Carta Orgánica |
| Domestic workers (from 1 Jul 2019) | 9.0% | 16.5% | **25.5%** | Law 6.338/2019 (amends Art.10 Law 5.407/2015) |
| Independent / self-employed (voluntary) | 13% (self) | — | **13%** | Secondary — **[RESEARCH GAP]** |

Employer 16.5% breakdown: **14% to IPS proper + 2.5%** earmarked for public-health/training funds (commonly cited as SENEPA, SNPP, SINAFOCAL / Ministerio de Salud Pública). Net economic IPS burden remains 25.5% total.

### Contribution base

- **Contribution base definition** — Included: ordinary salary, overtime, commissions, regalías, bonuses/premios; cash or in kind. Excluded: aguinaldo (13th-month) and family allowance (asignación familiar). Floor: the legal minimum wage. No confirmed general-regime ceiling — [RESEARCH GAP — reviewer to confirm].

### Minimum wage (contribution floor)

**Minimum wage table**

| Field | Value |
| --- | --- |
| Monthly minimum wage (diurnal, general activities) | ₲ 2.899.048 (from 1 Jul 2025, +3,6%, MTESS Resolución N° 677/2025) |
| Daily jornal | ₲ 111.502 |
| Part-time diurnal hour | ₲ 13.937 |

**[RESEARCH GAP — reviewer to confirm]** A new tripartite minimum-wage adjustment was reportedly under discussion for ~mid-2026; verify the current figure before reliance.

### Filing & payment

- **Filing and payment rules** — System: REI (Registro Electrónico de Información) — monthly planilla; auto-calculates 16.5% patronal + 9% obrero; produces the certificado de no adeudar. Payment: via authorized banks (Itaú, Continental, Visión Banco, Regional, etc.). Deadline: monthly, staggered by the last digit of the employer's número patronal (first business days of the following month); rolls to the next business day if non-business. Late payment: recargos (surcharges) + daily interest under Law N° 98/1992 and the IPS Carta Orgánica. [RESEARCH GAP — reviewer to confirm] exact surcharge schedule.  _(Law N° 98/1992; IPS Carta Orgánica)_

### Legal framework

- **Legal framework list** — Law N° 98/1992 — main IPS obligations/contributions law (rates, surcharges). Law N° 213/1993 — Código del Trabajo / social-security regulation. Law N° 1286 — amends/expands IPS-governing laws. Law N° 5.407/2015 — Del Trabajo Doméstico (incorporated domestic workers into IPS). Law N° 6.338/2019 — modifies Art. 10 of Law 5.407/2015; domestic-worker contribution → full general 9% / 16.5% rate. (Note: an instruction draft cited "Law 6.368/2019"; the authoritative BACN reference is Law N° 6.338/2019 — use 6.338.) IPS Carta Orgánica (consolidated).

### Key sources

- PwC Worldwide Tax Summaries (Paraguay — Other taxes): https://taxsummaries.pwc.com/paraguay/individual/other-taxes — confirms 9% / 16.5% / 25.5%.
- IPS portal (aportes): https://portal.ips.gov.py/sistemas/ipsportal/contenido.php?c=275
- BACN Law 6.338 (domestic work): https://www.bacn.gov.py/conoce-tu-ley/9146/trabajo-domestico-ley-n-6338-que-modifica-el-articulo-10-de-la-ley-n-540715
- BACN Law 1286 (IPS): https://www.bacn.gov.py/leyes-paraguayas/8309/ley-n-1286-modifica-y-amplia-disposiciones-de-las-leyes-que-rigen-el-instituto-de-prevision-social-ips
- IPS Carta Orgánica: https://informacionpublica.paraguay.gov.py/public/241273-CartaOrgnicadelIPSpdf-CartaOrgnicadelIPS.pdf
- Deel 2026 guide: https://www.deel.com/es/blog/aportes-ips-en-paraguay/ — confirms 14% IPS + 2.5%.
- TopTrabajos: https://www.toptrabajos.com/py/blog/ips-seguridad-social-paraguay/
- MTESS minimum wage 2025: https://www.mtess.gov.py/?p=30682

### Author flags (read before relying)

1. **Bank/financial 28% rate:** PwC publishes an 11% / 17% (28%) figure, and the sibling `paraguay-payroll` skill repeats it. Per the IPS "separate caja" framing and this skill's design, do not author a differentiated 28% IPS rate. If addressing banks, note the historical separate fund (Caja Bancaria), not a higher IPS tariff. This is a known discrepancy to reconcile across the Paraguay skill set.
2. **Domestic-worker law number:** use Law N° 6.338/2019 (not "6.368").
3. **Minimum wage is time-sensitive** — ₲ 2.899.048 valid from Jul 2025; re-check for any 2026 adjustment.
4. **Independent-regime and special-regime rates** (13% independent; ANDE 6%/12%; Magisterio 5.5%/2.5%; pensioners 6%) are secondary/lower-confidence — [RESEARCH GAP]; confirm before use.

### Test suite

**Test 1:** General employee, gross ₲ 2.899.048 (min wage). → obrero ₲ 260.914,32; patronal ₲ 478.342,92; total ₲ 739.257,24. (Sum check ✓.)

**Test 2:** General employee, gross ₲ 5.000.000. → obrero ₲ 450.000; patronal ₲ 825.000; total ₲ 1.275.000. (Sum check ✓.)

**Test 3:** Domestic worker, gross ₲ 2.899.048. → 9% / 16.5% = ₲ 260.914,32 / ₲ 478.342,92; total ₲ 739.257,24. SAME as Test 1. NOT the old 8% rate.

**Test 4:** Domestic worker, gross ₲ 4.000.000. → obrero ₲ 360.000; patronal ₲ 660.000; total ₲ 1.020.000. (Sum check ✓.)

**Test 5:** Worker earning ₲ 2.000.000 (below min wage). → base floored to ₲ 2.899.048; compute as Test 1. Flag.

**Test 6:** Bank employee, user expects 28%. → REFUSE the 28% IPS rate; flag fund affiliation (R-PY-IPS-2 / T2-1).

**Test 7:** Aguinaldo of ₲ 2.899.048 paid in December. → ₲ 0 IPS (aguinaldo excluded from base).

**Test 8:** Monthly IPS bank debit ₲ 739.257 with no other data. → implied base = 739.257 ÷ 0,255 ≈ ₲ 2.899.047; one employee at the minimum wage. Flag for reviewer.

### Prohibitions

- **Prohibitions list** — - NEVER apply the pre-2019 reduced domestic-worker rate (2.5% / 5.5% = 8%) — superseded by Law 6.338/2019. - NEVER author a differentiated 28% (11% / 17%) bank/financial IPS rate — no such IPS tariff exists. - NEVER deduct the 16.5% employer share from the worker's wage — only the 9% obrero share is withheld. - NEVER include aguinaldo or family allowance in the IPS base. - NEVER drop the minimum-wage floor for low-wage or part-time workers. - NEVER quantify IPS arrears, recargos, or interest without the IPS statement and official schedule — escalate. - NEVER confuse SET/DNIT/Marangatú tax debits with IPS contributions. - NEVER present IPS figures as definitive — always label as estimated and direct the client to their IPS account / REI planilla.  _(Law N° 6.338/2019)_

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a contador público, CPA, EA, tax attorney, or equivalent licensed practitioner in your jurisdiction) before filing or acting upon.

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
