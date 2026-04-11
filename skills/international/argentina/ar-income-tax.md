---
name: ar-income-tax
description: Use this skill whenever asked about Argentine income tax (Impuesto a las Ganancias) for self-employed individuals. Trigger on phrases like "Ganancias", "impuesto a las ganancias", "autónomo", "monotributo vs responsable inscripto", "cuarta categoría", "deducciones personales", "ganancia no imponible", "bienes personales", "DDJJ Ganancias", or any question about filing or computing income tax for a self-employed client in Argentina. This skill covers progressive rates (5-35%), personal deductions (ganancia no imponible, cargas de familia, deducción especial), Bienes Personales interaction, advance payments, and ARCA (ex-AFIP) filing. ALWAYS read this skill before touching any Argentine income tax work.
---

# Argentina Income Tax (Ganancias) -- Self-Employed Skill

---

## Skill Metadata

| Field | Value |
|-------|-------|
| Jurisdiction | Argentina |
| Jurisdiction Code | AR |
| Primary Legislation | Ley 20.628 de Impuesto a las Ganancias (texto ordenado) |
| Supporting Legislation | Ley 27.743 (Paquete Fiscal 2024); Decreto Reglamentario; RG ARCA (resoluciones generales); Ley 23.966 (Bienes Personales) |
| Tax Authority | ARCA (Agencia de Recaudación y Control Aduanero, formerly AFIP) |
| Filing Portal | ARCA Servicios con Clave Fiscal (www.arca.gob.ar) |
| Contributor | Open Accountants Community |
| Validated By | Pending -- requires sign-off by an Argentine Contador Público |
| Validation Date | Pending |
| Skill Version | 1.0 |
| Confidence Coverage | Tier 1: rate table application, personal deduction amounts, deducción especial multiplier, filing deadlines. Tier 2: expense classification, home office, mixed-use vehicle, Bienes Personales interaction. Tier 3: transfer pricing, foreign-source income, trust taxation, corporate reorganisations. |

---

## Confidence Tier Definitions

- **[T1] Tier 1 -- Deterministic.** Apply exactly as written. No reviewer judgement required.
- **[T2] Tier 2 -- Reviewer Judgement Required.** Claude flags and presents options. Contador Público must confirm.
- **[T3] Tier 3 -- Out of Scope / Escalate.** Do not guess. Escalate and document.

---

## Step 0: Client Onboarding Questions

Before computing any income tax figure, you MUST know:

1. **Tax category** [T1] -- 4ta categoría (rentas del trabajo personal) or autónomo under art. 53 (professional/self-employed)
2. **Marital / family status** [T1] -- for cargas de familia deductions (spouse, children, etc.)
3. **Gross annual income from self-employment** [T1] -- total honorarios / ingresos brutos
4. **Business expenses** [T1/T2] -- documented, deductible expenses
5. **Retirement contributions (jubilación autónomos)** [T1] -- mandatory contributions paid
6. **Obra social and prepaga contributions** [T1] -- health insurance paid
7. **Other income sources** [T1] -- employment (4ta cat. relación de dependencia), rental (1ra cat.), financial (2da cat.)
8. **Bienes Personales status** [T2] -- assets above threshold trigger wealth tax
9. **CUIT** [T1] -- tax identification number, determines filing schedule

**If tax category is unknown, STOP. The deducción especial multiplier differs between autónomos and empleados. Category is mandatory.**

---

## Step 1: Determine Applicable Rate Table [T1]

**Legislation:** Ley 20.628, art. 94 (progressive scale)

**CRITICAL NOTE:** Argentina adjusts these thresholds semi-annually (January and July) by the IPC (Consumer Price Index). The amounts below are for the **first semester 2025 (January-June 2025)**. You MUST verify the current semester's thresholds with ARCA before applying.

### Progressive Tax Scale -- First Semester 2025 (Illustrative) [T1]

| Ganancia Neta Imponible Acumulada (ARS) | Rate | Cumulative Fixed Amount |
|-----------------------------------------|------|------------------------|
| 0 -- 1,750,026 | 5% | -- |
| 1,750,027 -- 3,500,053 | 9% | 87,501 |
| 3,500,054 -- 5,250,079 | 12% | 245,004 |
| 5,250,080 -- 7,000,106 | 15% | 455,007 |
| 7,000,107 -- 10,500,159 | 19% | 717,511 |
| 10,500,160 -- 14,000,211 | 23% | 1,382,521 |
| 14,000,212 -- 21,000,317 | 27% | 2,187,033 |
| 21,000,318 -- 28,000,423 | 31% | 4,077,062 |
| 28,000,424+ | 35% | 6,247,095 |

**WARNING: These thresholds change every 6 months. Always verify with ARCA RG for the applicable period before computing. Argentina's semi-annual adjustment renders any hardcoded table stale within months.**

---

## Step 2: Personal Deductions (Deducciones Personales) [T1]

**Legislation:** Ley 20.628, art. 30

**CRITICAL NOTE:** Like the scale, these amounts are updated semi-annually. Values below are for **first semester 2025 (illustrative)**. Verify with ARCA.

### Deduction Categories [T1]

| Deduction | First Semester 2025 (ARS, illustrative) | Notes |
|-----------|----------------------------------------|-------|
| Ganancia no imponible (art. 30 inc. a) | ~3,916,268 (annual) | Minimum non-taxable income for all taxpayers |
| Deducción especial -- autónomos (art. 30 inc. c, subinc. i) | GNI x 2.5 = ~9,790,671 | For autonomous workers (art. 53 income) |
| Deducción especial -- empleados (art. 30 inc. c, subinc. ii) | GNI x 3.8 = ~14,881,819 | For employees (4ta cat. relación de dependencia) -- NOT for autónomos |
| Cónyuge (art. 30 inc. b, subinc. 1) | ~3,688,339 | Spouse with income below GNI |
| Hijo/a menor de 18 (art. 30 inc. b, subinc. 2) | ~1,860,043 | Per child under 18 |
| Hijo/a con discapacidad (art. 30 inc. b, subinc. 2) | ~3,720,086 | Per child with disability (no age limit) |

### Key Rules [T1]

- **Autónomos use the 2.5x multiplier**, not the 3.8x multiplier (3.8x is exclusively for employees)
- Cargas de familia: the dependent must have income below the ganancia no imponible to qualify
- Only one family member can claim each dependent
- Deductions are prorated if the taxpayer was a resident for part of the year

---

## Step 3: Computation Structure [T1]

**Legislation:** Ley 20.628, arts. 23, 29, 30, 83, 94

| Step | Description |
|------|-------------|
| A | Ganancia bruta (gross income from all categories) |
| B | Less: Gastos deducibles (allowable business expenses per art. 83-87) |
| C | Ganancia neta (A minus B) |
| D | Less: Deducciones generales (art. 85 -- retirement contributions, medical, life insurance, etc.) |
| E | Less: Deducciones personales (art. 30 -- GNI + deducción especial + cargas de familia) |
| F | Ganancia neta imponible (C minus D minus E) |
| G | Apply progressive scale to F |
| H | Less: Anticipos paid (advance payments) |
| I | Less: Retenciones sufridas (withholdings suffered) |
| J | Less: Percepciones (tax perceptions, e.g., on foreign currency purchases) |
| K | Tax due / (refund) |

---

## Step 4: Allowable Deductions [T1/T2]

**Legislation:** Ley 20.628, arts. 83-87

### Deductible Expenses (Gastos Deducibles)

| Expense | Tier | Treatment |
|---------|------|-----------|
| Office rent | T1 | Fully deductible |
| Professional insurance | T1 | Fully deductible |
| Accounting / legal fees | T1 | Fully deductible |
| Office supplies | T1 | Fully deductible |
| Software subscriptions | T1 | Fully deductible |
| Marketing / advertising | T1 | Fully deductible |
| Bank charges (business) | T1 | Fully deductible |
| Professional body fees (Colegio) | T1 | Fully deductible |
| Staff salaries + cargas sociales | T1 | Fully deductible |
| Amortisation of intangibles | T1 | Straight-line over useful life |
| Motor vehicle (business portion) | T2 | Limited -- see automobile rules |
| Home office | T2 | Proportional -- dedicated space required |

### General Deductions (Deducciones Generales, art. 85) [T1]

| Deduction | Limit |
|-----------|-------|
| Aportes jubilatorios (retirement contributions) | Actual amount paid (mandatory + voluntary to cap) |
| Obra social / prepaga (health insurance) | 5% of ganancia neta |
| Seguros de vida / retiro (life insurance / retirement insurance) | Annual cap (adjusted semi-annually) |
| Servicio doméstico (domestic staff) | Up to GNI amount |
| Alquiler vivienda habitual (housing rent) | 40% of rent, up to GNI amount |
| Donaciones (donations to exempt entities) | 5% of ganancia neta |

### NOT Deductible [T1]

| Expense | Reason |
|---------|--------|
| Personal / family expenses | Not related to income production |
| Income tax (Ganancias) itself | Circular |
| Fines and penalties | Public policy |
| Gastos no documentados | s38 -- no receipt = not deductible + additional tax |
| Automobile expenses above limits | Art. 88 -- vehicle acquisition and running costs are capped |

### Automobile Rules [T2]

- Amortisation limited to the value of ARS-equivalent of specific cap (updated periodically)
- Running costs (fuel, insurance, maintenance) proportional to business use
- [T2] Flag for reviewer: vehicle business use percentage must be documented

---

## Step 5: Advance Payments (Anticipos) [T1]

**Legislation:** RG (ARCA) applicable

### Schedule

| Instalment | Deadline |
|-----------|----------|
| 1st through 5th | Monthly, starting in June (for prior year DDJJ filed in June) |

### Rules [T1]

- 5 bimonthly anticipos (every 2 months)
- Each = 20% of prior year's determined tax (less retenciones and percepciones)
- First anticipo due in June; last in February of following year
- Reduction requests possible via ARCA system if current year income will be materially lower

---

## Step 6: Bienes Personales Interaction [T2]

**Legislation:** Ley 23.966 (Impuesto sobre los Bienes Personales)

| Rule | Detail |
|------|--------|
| Threshold | Assets exceeding ARS threshold (adjusted annually -- verify with ARCA) |
| Rate | Progressive 0.5% to 1.75% (Ley 27.743 modified rates -- verify) |
| Includes | All worldwide assets for residents -- real estate, vehicles, bank accounts, investments |
| Filing | Same period as Ganancias (DDJJ annual) |
| Interaction | Bienes Personales is a separate tax but filed alongside Ganancias |

**[T2] Always flag Bienes Personales when a self-employed client's asset base may exceed the threshold. The filing is separate but simultaneous.**

---

## Step 7: Filing and Deadlines [T1]

**Legislation:** RG (ARCA) calendario fiscal

| Filing / Payment | Deadline |
|-----------------|----------|
| DDJJ Ganancias (annual return) | June -- exact date depends on last digit of CUIT (0-1: mid-June, 2-3: late June, etc.) |
| DDJJ Bienes Personales | Same schedule as Ganancias |
| Anticipos (advance payments) | Bimonthly from June |
| Retenciones (monthly) | If the taxpayer is an agente de retención |

### Filing Method [T1]

- Via ARCA web portal (Servicios con Clave Fiscal)
- Application: "Ganancias Personas Humanas" (SIRADIG for employees; Régimen simplificado for certain categories)
- DDJJ must include all income categories, deductions, and foreign assets

---

## Step 8: Penalties [T1]

**Legislation:** Ley 11.683 (Procedimiento Tributario)

| Offence | Penalty |
|---------|---------|
| Late filing (omisión) | 1% per month of unpaid tax (up to 100% of the tax) |
| Material omission (art. 45) | 100% of the omitted tax |
| Tax fraud (defraudación, art. 46) | 200-1000% of evaded tax + criminal prosecution |
| Failure to file | Fixed fine (adjusted annually) + interest |
| Undocumented expenses (art. 38 Ley 20.628) | 35% tax on the gross undocumented amount (effectively non-deductible + punitive tax) |
| Late payment interest | Resolutiva rate published by ARCA (currently ~4-6% monthly -- verify) |

---

## Step 9: Record Keeping [T1]

**Legislation:** Ley 11.683; Código de Comercio

| Requirement | Detail |
|-------------|--------|
| Minimum retention | 10 years (general prescription period under Ley 11.683 is 5 years, but books must be kept 10) |
| What to keep | All facturas, recibos, extractos bancarios, contratos, registros de bienes |
| Format | Paper or digital (factura electrónica is mandatory for most taxpayers) |
| Electronic invoicing | Mandatory via ARCA (factura electrónica) |

---

## Step 10: Edge Case Registry

### EC1 -- Autónomo applies 3.8x multiplier instead of 2.5x [T1]
**Situation:** Self-employed professional (autónomo) uses the 3.8x deducción especial multiplier.
**Resolution:** INCORRECT. The 3.8x multiplier is exclusively for employees in relación de dependencia. Autónomos use 2.5x the ganancia no imponible. Correct the calculation.

### EC2 -- Spouse claimed as carga de familia but earns above GNI [T1]
**Situation:** Client claims spouse deduction. Spouse earns ARS 5,000,000 (above ganancia no imponible).
**Resolution:** NOT deductible. Spouse income exceeds the GNI threshold. Remove the carga de familia deduction for spouse.

### EC3 -- Undocumented expenses (gastos sin factura) [T1]
**Situation:** Client claims ARS 500,000 in expenses without facturas.
**Resolution:** NOT deductible AND subject to 35% punitive tax under art. 38. Undocumented expenses = ARS 500,000 x 35% = ARS 175,000 additional tax. Remove from deductions and flag the 35% charge.

### EC4 -- Semi-annual threshold confusion [T2]
**Situation:** Client's fiscal year spans both semesters (Jan-Jun and Jul-Dec) with different scale thresholds.
**Resolution:** Each semester's income is computed using that semester's applicable thresholds. The annual DDJJ aggregates both. [T2] Flag for reviewer to confirm the correct semester thresholds are applied.

### EC5 -- Foreign income for Argentine resident [T3]
**Situation:** Argentine resident earns consulting income from a US client.
**Resolution:** ESCALATE. Argentine residents are taxed on worldwide income. Foreign-source income is subject to Ganancias, but foreign tax credits may apply under applicable tax treaties. Refer to Contador Público for treaty analysis.

### EC6 -- Monotributo vs Responsable Inscripto decision [T2]
**Situation:** Client asks whether to stay in Monotributo or switch to Responsable Inscripto.
**Resolution:** This skill covers Responsable Inscripto (Ganancias). Monotributo is a separate simplified regime (see ar-monotributo.md). [T2] Flag for reviewer: the decision depends on turnover, expense levels, and the client's broader tax position.

### EC7 -- Percepciones on foreign currency purchases [T1]
**Situation:** Client purchased USD and was charged 30% percepción (RG 4815) + 45% adelanto Ganancias.
**Resolution:** The percepciones are credits against the Ganancias DDJJ. Include in Step J of the computation. If the client has no tax liability, the excess becomes a saldo a favor (credit balance).

### EC8 -- Housing rent deduction exceeds cap [T1]
**Situation:** Client pays ARS 8,000,000 annual rent. Claims 40% = ARS 3,200,000 deduction.
**Resolution:** Check against GNI cap. If 40% of rent exceeds the ganancia no imponible, cap at GNI. Deduction = min(40% x rent, GNI).

---

## Step 11: Reviewer Escalation Protocol

When Claude identifies a [T2] situation:

```
REVIEWER FLAG
Tier: T2
Client: [name]
Situation: [description]
Issue: [what is ambiguous]
Options: [possible treatments]
Recommended: [most likely correct treatment and why]
Action Required: Contador Público must confirm before filing.
```

When Claude identifies a [T3] situation:

```
ESCALATION REQUIRED
Tier: T3
Client: [name]
Situation: [description]
Issue: [outside skill scope]
Action Required: Do not advise. Refer to Contador Público. Document gap.
```

---

## Step 12: Test Suite

### Test 1 -- Standard autónomo, mid-range income
**Input:** Autónomo (art. 53), single, no dependants. Gross income ARS 20,000,000 (annual). Expenses ARS 5,000,000. Retirement contributions ARS 1,500,000. GNI = ARS 3,916,268. Deducción especial 2.5x = ARS 9,790,671. No anticipos paid.
**Expected output:** Ganancia neta = 15,000,000. Less general deductions 1,500,000 = 13,500,000. Less GNI 3,916,268 less deducción especial 9,790,671 = negative (fully sheltered). Ganancia neta imponible = max(0, 13,500,000 - 3,916,268 - 9,790,671) = max(0, -206,939) = 0. No tax.

### Test 2 -- Higher income autónomo with tax payable
**Input:** Autónomo, single, no dependants. Gross income ARS 50,000,000. Expenses ARS 12,000,000. Retirement ARS 2,000,000. GNI = 3,916,268. DE = 9,790,671. Anticipos ARS 1,000,000.
**Expected output:** Ganancia neta = 38,000,000. Less 2,000,000 = 36,000,000. Less GNI + DE = 13,706,939. GNI = 36,000,000 - 13,706,939 = 22,293,061. Apply scale (verify thresholds). Tax minus anticipos = amount due.

### Test 3 -- Cargas de familia deduction
**Input:** Married with 2 children under 18. Spouse has no income. GNI applies + cónyuge + 2 hijos.
**Expected output:** Personal deductions = GNI + deducción especial + cónyuge (3,688,339) + 2 x hijo (1,860,043 x 2) = total shelter before applying scale.

### Test 4 -- Undocumented expenses trigger 35% tax
**Input:** Client has ARS 1,000,000 in gastos sin factura.
**Expected output:** Expenses not deductible. Additional 35% tax = ARS 350,000 on top of normal Ganancias.

### Test 5 -- Percepciones as credit
**Input:** Client has ARS 800,000 in percepciones from foreign currency purchases. Tax liability from scale = ARS 500,000.
**Expected output:** Tax due = 500,000 - 800,000 = -300,000. Saldo a favor of ARS 300,000 (credit balance).

---

## PROHIBITIONS

- NEVER apply the 3.8x deducción especial multiplier to autónomos -- that is exclusively for empleados
- NEVER use hardcoded scale thresholds without verifying the current semester's ARCA-published amounts
- NEVER allow undocumented expenses (gastos sin factura) as deductions
- NEVER ignore the 35% punitive tax on undocumented expenses
- NEVER claim cargas de familia for dependants earning above the ganancia no imponible
- NEVER file Ganancias without considering Bienes Personales obligations
- NEVER compute a full year using only one semester's thresholds -- each semester may have different amounts
- NEVER ignore percepciones -- they are credits against the final DDJJ
- NEVER present tax calculations as definitive -- always label as estimated and direct client to a Contador Público for confirmation
- NEVER advise on Monotributo within this skill -- use ar-monotributo.md

---

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a Contador Público Nacional or equivalent licensed practitioner in Argentina) before filing or acting upon.

The most up-to-date, verified version of this skill is maintained at [openaccountants.com](https://openaccountants.com). Log in to access the latest version, request a professional review from a licensed accountant, and track updates as tax law changes.
