---
name: mx-imss
description: Use this skill whenever asked about Mexican IMSS social security for self-employed individuals. Trigger on phrases like "IMSS", "seguro social Mexico", "regimen voluntario", "incorporacion voluntaria", "IMSS freelancer", "aseguramiento voluntario", or any question about voluntary IMSS enrollment, contribution calculation, or benefits for self-employed persons in Mexico. Covers voluntary inscription (Modalidad 40, regimen voluntario), contribution bases, and health/maternity/retirement/disability benefits. ALWAYS read this skill before touching any Mexican IMSS work.
---

# Mexico IMSS Self-Employed -- Skill

---

## Skill Metadata

| Field | Value |
|-------|-------|
| Jurisdiction | Mexico |
| Jurisdiction Code | MX |
| Primary Legislation | Ley del Seguro Social (LSS) |
| Supporting Legislation | Reglamento de la LSS en materia de Afiliacion; Ley del INFONAVIT |
| Authority | Instituto Mexicano del Seguro Social (IMSS) |
| Portal | IMSS Digital (imss.gob.mx) |
| Contributor | Open Accountants Community |
| Validated By | Pending -- requires sign-off by a Mexican contador publico or social security specialist |
| Validation Date | Pending |
| Skill Version | 1.0 |
| Tax Year | 2025 |
| Confidence Coverage | Tier 1: voluntary enrollment options, contribution structure, UMA-based calculations. Tier 2: benefit eligibility periods, Modalidad 40 strategy. Tier 3: disability claims, employer-employee disputes, INFONAVIT interaction. |

---

## Confidence Tier Definitions

- **[T1] Tier 1 -- Deterministic.** Apply exactly as written. No reviewer judgement required.
- **[T2] Tier 2 -- Reviewer Judgement Required.** Claude flags and presents options. Qualified professional must confirm.
- **[T3] Tier 3 -- Out of Scope / Escalate.** Do not guess. Escalate and document.

---

## Step 0: Client Onboarding Questions

Before advising on IMSS matters, you MUST know:

1. **Current employment status** [T1] -- purely self-employed, or also employed part-time
2. **Whether currently enrolled in any IMSS regime** [T1] -- active or inactive
3. **CURP and RFC** [T1] -- identification and tax ID
4. **Prior IMSS contribution history** [T1] -- weeks contributed (semanas cotizadas)
5. **Family members to cover** [T1] -- spouse, children, parents (for health coverage)
6. **Desired salary base for contributions** [T2] -- affects both cost and future pension

**If the client is a salaried employee, the EMPLOYER handles IMSS. STOP. This skill covers self-employed/voluntary only.**

---

## Step 1: IMSS Coverage Overview [T1]

**Legislation:** LSS, Art. 6, 11

IMSS covers five branches of insurance:

| Branch | Coverage |
|--------|---------|
| Enfermedades y Maternidad (Illness and Maternity) | Medical care, prescriptions, maternity leave |
| Invalidez y Vida (Disability and Life) | Disability pension, death benefits |
| Retiro, Cesantia y Vejez (Retirement) | Old-age pension, unemployment in advanced age |
| Riesgos de Trabajo (Work Risks) | Work accidents and occupational diseases |
| Guarderias y Prestaciones Sociales (Childcare) | Daycare, social services |

---

## Step 2: Voluntary Enrollment Options [T1]

**Legislation:** LSS, Art. 13, 218, 240

### Option 1: Incorporacion Voluntaria al Regimen Obligatorio (IVRO) [T1]

| Detail | Value |
|--------|-------|
| Who | Self-employed workers, freelancers, independent professionals |
| Coverage | All 5 branches of insurance |
| Base salary | Chosen by the insured (minimum 1 UMA, commonly set at desired level) |
| Family coverage | Spouse and children included for health |
| Art. 13 categories | Domestic workers, ejidatarios, self-employed, employers with up to 5 employees |

### Option 2: Seguro de Salud para la Familia (Family Health Insurance) [T1]

| Detail | Value |
|--------|-------|
| Who | Any person not otherwise covered by IMSS |
| Coverage | Illness and Maternity ONLY (no pension, no disability) |
| Cost | Fixed annual amount per family member based on age brackets |
| Pension | Does NOT contribute to pension or retirement |

### Option 3: Continuacion Voluntaria (Modalidad 40) [T1]

| Detail | Value |
|--------|-------|
| Who | Persons previously enrolled in IMSS who left employment |
| Requirement | Must have at least 52 weeks of prior contributions |
| Coverage | Invalidez y Vida + Retiro, Cesantia y Vejez (NO health coverage) |
| Purpose | Primarily to boost pension by continuing/increasing contributions |
| Base salary | Can choose up to 25 UMA (allowing higher pension) |

---

## Step 3: Contribution Rates (IVRO) [T1]

**Legislation:** LSS, Art. 106, 147, 168, 211

The UMA (Unidad de Medida y Actualizacion) replaces the salario minimo for IMSS calculations.

| Item | 2025 Value (approximate) |
|------|-------------------------|
| Daily UMA | ~MXN 113.14 (verify with INEGI) |
| Monthly UMA | ~MXN 3,439.46 |
| Annual UMA | ~MXN 41,273.52 |

### IVRO Contribution Breakdown (Self-Employed) [T1]

For IVRO, the self-employed person pays BOTH the employer and employee portions:

| Branch | Total Rate (% of base salary) |
|--------|------------------------------|
| Enfermedades y Maternidad (in kind, fixed) | ~20.40% |
| Enfermedades y Maternidad (in kind, excess) | Varies by salary level above 3 UMA |
| Enfermedades y Maternidad (cash) | ~1.00% |
| Invalidez y Vida | ~2.375% |
| Retiro | 2.00% |
| Cesantia en Edad Avanzada y Vejez | ~4.375% (increasing under 2020 reform) |
| Guarderias | 1.00% |
| Riesgos de Trabajo | Risk class-based (~0.54% average for office/low-risk) |
| **Approximate total** | **~31-33%** of chosen base salary |

**Note:** Rates are complex with multiple sub-components. The total varies by chosen salary base level. Use the IMSS contribution calculator at imss.gob.mx for exact amounts.

---

## Step 4: Modalidad 40 Contribution [T1]

**Legislation:** LSS, Art. 218

| Component | Rate |
|-----------|------|
| Invalidez y Vida | ~2.375% |
| Retiro | 2.00% |
| Cesantia y Vejez | ~4.375% |
| **Total Modalidad 40** | **~10.075%** of chosen base salary |

Maximum base salary for Modalidad 40: 25 UMA diario = ~MXN 2,828.50/day = ~MXN 86,001/month (verify).

---

## Step 5: Seguro de Salud para la Familia [T1]

**Legislation:** LSS, Art. 240-245

Annual cost per family member (2025 approximate):

| Age Group | Annual Cost (approx. % of annual UMA) |
|-----------|--------------------------------------|
| Under 19 | ~5.9% of annual UMA |
| 19-39 | ~7.5% of annual UMA |
| 40-59 | ~9.1% of annual UMA |
| 60+ | ~11.9% of annual UMA |

Payment is annual, upfront.

---

## Step 6: Tax Deductibility [T1]

**Legislation:** Ley del ISR, Art. 151

| Contribution Type | Deductible? |
|-------------------|-------------|
| IVRO contributions | Yes -- as social security contribution deduction |
| Modalidad 40 | Yes -- deductible for ISR purposes |
| Seguro de Salud para la Familia | Yes -- as medical expense deduction (limited) |

---

## Step 7: Edge Case Registry

### EC1 -- Freelancer choosing between IVRO and Seguro de Salud [T2]
**Situation:** Freelancer wants health coverage only, no pension.
**Resolution:** Seguro de Salud para la Familia covers health only at lower cost. But no pension credits accumulate. If the client wants pension, IVRO is required. [T2] Flag for reviewer to assess long-term retirement impact.

### EC2 -- Modalidad 40 with insufficient prior weeks [T1]
**Situation:** Client has 40 weeks of prior IMSS contributions.
**Resolution:** Modalidad 40 requires at least 52 weeks (1 year) of prior contributions. Client is ineligible. Must use IVRO instead or accumulate more weeks first.

### EC3 -- Self-employed choosing base salary for IVRO [T2]
**Situation:** Freelancer earns MXN 60,000/month. What base to choose?
**Resolution:** Can choose any base from 1 UMA upward. Higher base = higher cost but higher pension and maternity/disability benefits. Common strategy: choose a base reflecting actual income for adequate coverage. [T2] Flag for reviewer to balance cost vs. coverage.

### EC4 -- Gap in contributions [T1]
**Situation:** Client had IMSS through an employer, left 3 years ago, no contributions since.
**Resolution:** Modalidad 40 requires enrollment within 5 years of last employer contribution. Client is still eligible. After 5 years, the right to Modalidad 40 lapses and IVRO is the only voluntary option.

### EC5 -- Client has both employment and freelance work [T1]
**Situation:** Part-time employee (employer pays IMSS) plus freelance income.
**Resolution:** If already enrolled through employer, the client is covered. No need for additional voluntary enrollment for health. May optionally use Modalidad 40 or voluntary savings (ahorro voluntario) to boost pension.

### EC6 -- 2020 Reform -- increasing Cesantia rates [T1]
**Situation:** Client asks why contribution rates increased.
**Resolution:** The 2020 pension reform gradually increases the employer share of Cesantia en Edad Avanzada y Vejez from 3.15% (2023) to 11.875% (2030). For IVRO, the self-employed pays both shares, so total contribution will increase annually through 2030.

---

## Step 8: Test Suite

### Test 1 -- IVRO at minimum base (1 UMA)
**Input:** Self-employed, IVRO at 1 UMA daily (~MXN 113.14/day).
**Expected output:**
- Monthly base: ~MXN 3,439.46
- Approximate monthly contribution: ~31% x 3,439.46 = ~MXN 1,066
- Covers all 5 branches including health for family

### Test 2 -- Modalidad 40 at moderate base
**Input:** Former employee, 200 weeks prior contributions. Chose base of 10 UMA daily.
**Expected output:**
- Daily base: ~MXN 1,131.40
- Monthly base: ~MXN 34,394.60
- Monthly contribution: ~10.075% x 34,394.60 = ~MXN 3,465
- No health coverage (Modalidad 40 is pension only)

### Test 3 -- Seguro de Salud para la Familia
**Input:** Family of 4: 2 adults (age 35, 33), 2 children (age 8, 5).
**Expected output:**
- Adults (19-39): 2 x 7.5% x ~41,274 = ~MXN 6,191
- Children (under 19): 2 x 5.9% x ~41,274 = ~MXN 4,870
- Total annual: ~MXN 11,061
- Health coverage only; no pension

### Test 4 -- Modalidad 40 at maximum base (25 UMA)
**Input:** High earner wanting maximum pension. 500 weeks prior.
**Expected output:**
- Daily base: 25 x 113.14 = ~MXN 2,828.50
- Monthly base: ~MXN 85,987
- Monthly contribution: ~10.075% x 85,987 = ~MXN 8,663
- Maximum pension accumulation strategy

---

## PROHIBITIONS

- NEVER enroll in Modalidad 40 without verifying at least 52 weeks of prior contributions
- NEVER assume Seguro de Salud para la Familia provides pension or disability coverage -- it is health only
- NEVER use salario minimo for IMSS calculations -- use UMA since 2017
- NEVER ignore the 5-year window for Modalidad 40 enrollment after leaving employment
- NEVER assume IVRO rates are fixed -- the 2020 reform increases Cesantia rates annually through 2030
- NEVER present IMSS calculations as exact -- use the IMSS calculator at imss.gob.mx for precise amounts
- NEVER advise on Modalidad 40 as a pension strategy without flagging for a qualified advisor [T2]
- NEVER present calculations as definitive -- always label as estimated and direct client to IMSS or a qualified Mexican contador publico

---

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a contador publico, social security specialist, or equivalent licensed practitioner in Mexico) before filing or acting upon.

The most up-to-date, verified version of this skill is maintained at [openaccountants.com](https://openaccountants.com). Log in to access the latest version, request a professional review from a licensed accountant, and track updates as tax law changes.
