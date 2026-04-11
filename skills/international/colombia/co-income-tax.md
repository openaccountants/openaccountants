---
name: co-income-tax
description: Use this skill whenever asked about Colombian income tax for self-employed individuals. Trigger on phrases like "declaración de renta", "renta personas naturales", "Formulario 210", "cédula general", "UVT", "retención en la fuente", "renta presuntiva", "DIAN", or any question about filing or computing income tax for a self-employed or independent worker in Colombia. This skill covers cédula general progressive rates (0-39%), UVT-based thresholds, renta presuntiva, deductions (dependientes, interest, health), retención en la fuente, and DIAN filing. ALWAYS read this skill before touching any Colombian income tax work.
---

# Colombia Income Tax (Renta Personas Naturales) -- Self-Employed Skill

---

## Skill Metadata

| Field | Value |
|-------|-------|
| Jurisdiction | Colombia |
| Jurisdiction Code | CO |
| Primary Legislation | Estatuto Tributario (ET), Libro I, Título I (arts. 5-364) |
| Supporting Legislation | Ley 2277 de 2022 (Reforma Tributaria); Ley 2010 de 2019; Decreto 1625 de 2016 (DUR Tributario) |
| Tax Authority | Dirección de Impuestos y Aduanas Nacionales (DIAN) |
| Filing Portal | DIAN Portal (www.dian.gov.co) -- Servicios en Línea |
| Contributor | Open Accountants Community |
| Validated By | Pending -- requires sign-off by a Colombian Contador Público |
| Validation Date | Pending |
| Skill Version | 1.0 |
| Confidence Coverage | Tier 1: rate table (art. 241), UVT value, filing thresholds, renta presuntiva rate, retención en la fuente on services. Tier 2: cédula general vs cédula de pensiones classification, deduction limits, cost/expense allocation for independent workers. Tier 3: transfer pricing, foreign-source income, tax treaties, controlled foreign corporations. |

---

## Confidence Tier Definitions

- **[T1] Tier 1 -- Deterministic.** Apply exactly as written. No reviewer judgement required.
- **[T2] Tier 2 -- Reviewer Judgement Required.** Claude flags and presents options. Contador Público must confirm.
- **[T3] Tier 3 -- Out of Scope / Escalate.** Do not guess. Escalate and document.

---

## Step 0: Client Onboarding Questions

Before computing any income tax figure, you MUST know:

1. **Residency status** [T1] -- resident (183+ days) vs non-resident; this skill covers residents only
2. **Type of income** [T1] -- cédula general (work, capital, non-labour) vs pension vs dividends
3. **Gross annual income from independent work** [T1] -- total ingresos brutos
4. **Costs and expenses** [T1/T2] -- documented costs and deductions
5. **Retención en la fuente suffered** [T1] -- withholdings deducted at source during the year
6. **Dependants** [T1] -- number of qualifying dependants (children, spouse, parents)
7. **Social security contributions** [T1] -- pensión, salud, ARL paid
8. **NIT / cédula** [T1] -- determines filing schedule (by last 2 digits)
9. **Patrimonio bruto** [T2] -- for renta presuntiva and filing threshold analysis

**If residency status is unknown, STOP. Non-residents pay flat 35% on Colombia-source income. Residency is mandatory.**

---

## Step 1: UVT (Unidad de Valor Tributario) [T1]

**Legislation:** ET art. 868

| Year | UVT Value (COP) |
|------|-----------------|
| 2024 | COP 47,065 |
| 2025 | COP 49,799 |

**All thresholds, brackets, and limits in Colombian tax law are expressed in UVT. Convert UVT to COP using the applicable year's value.**

For income earned in 2024 (declared in 2025): use UVT 2024 = COP 47,065.
For income earned in 2025 (declared in 2026): use UVT 2025 = COP 49,799.

---

## Step 2: Determine Applicable Rate Table [T1]

**Legislation:** ET art. 241 (Cédula General)

### Progressive Tax Table -- Cédula General

| Taxable Income (UVT) | Rate | Computation |
|----------------------|------|-------------|
| 0 -- 1,090 | 0% | 0 |
| >1,090 -- 1,700 | 19% | (Base gravable in UVT - 1,090) x 19% |
| >1,700 -- 4,100 | 28% | (Base gravable in UVT - 1,700) x 28% + 115.9 UVT |
| >4,100 -- 8,670 | 33% | (Base gravable in UVT - 4,100) x 33% + 788 UVT |
| >8,670 -- 18,970 | 35% | (Base gravable in UVT - 8,670) x 35% + 2,296.1 UVT |
| >18,970 -- 31,000 | 37% | (Base gravable in UVT - 18,970) x 37% + 5,901.1 UVT |
| >31,000 | 39% | (Base gravable in UVT - 31,000) x 39% + 10,352.2 UVT |

### In COP (at UVT 2025 = COP 49,799) -- Illustrative

| UVT Range | COP Equivalent (approx) |
|-----------|------------------------|
| 1,090 UVT | COP 54,280,910 |
| 1,700 UVT | COP 84,658,300 |
| 4,100 UVT | COP 204,175,900 |
| 8,670 UVT | COP 431,757,330 |
| 18,970 UVT | COP 944,687,030 |
| 31,000 UVT | COP 1,543,769,000 |

### Non-Resident Rate [T1]

Non-residents: flat 35% on Colombia-source income. No deductions. This skill does not cover non-residents further.

---

## Step 3: Filing Thresholds -- Who Must File? [T1]

**Legislation:** ET art. 592-594; Decreto annual de plazos

A natural person must file a renta return if ANY of these apply (2025 thresholds for 2024 income, at UVT 2024 = COP 47,065):

| Condition | Threshold |
|-----------|-----------|
| Gross income | >= 1,400 UVT (COP 65,891,000) |
| Gross patrimonio (assets) | >= 4,500 UVT (COP 211,793,000) |
| Credit card purchases | >= 1,400 UVT |
| Total purchases and consumption | >= 1,400 UVT |
| Bank account deposits | >= 1,400 UVT |

**Most self-employed individuals will exceed at least one threshold and must file.**

---

## Step 4: Computation Structure -- Cédula General [T1]

**Legislation:** ET arts. 26, 103, 335-336, 241

| Step | Description |
|------|-------------|
| A | Ingresos brutos (gross income from independent work + capital + non-labour) |
| B | Less: Ingresos no constitutivos de renta (non-taxable income -- e.g., mandatory pension contributions by employer portion) |
| C | Ingresos netos (A minus B) |
| D | Less: Costos y gastos procedentes (allowable costs and expenses -- must have causal relation, necessity, proportionality) |
| E | Renta líquida (C minus D) |
| F | Less: Rentas exentas (exempt income -- 25% of renta líquida, capped; plus other specific exemptions) |
| G | Less: Deducciones (deductions -- dependants, interest, health, etc.) |
| H | **Important:** Total of F + G cannot exceed 40% of ingresos netos (C), subject to annual UVT cap of 5,040 UVT |
| I | Renta líquida gravable (base gravable) = E minus F minus G (with 40% / 5,040 UVT cap) |
| J | Compare with renta presuntiva (see Step 6) -- taxable income = higher of I or renta presuntiva |
| K | Apply art. 241 progressive table |
| L | Less: Retención en la fuente (withholdings suffered) |
| M | Less: Anticipos paid |
| N | Tax due / (refund) |

---

## Step 5: Deductions and Exempt Income [T1/T2]

**Legislation:** ET arts. 119, 126-1, 126-4, 336, 387

### Rentas Exentas (Exempt Income) [T1]

| Exemption | Limit |
|-----------|-------|
| 25% of renta líquida (general exemption for workers) | Capped at 240 UVT/month (2,880 UVT/year) |
| Voluntary pension contributions (AFC, FVP) | Up to 30% of gross income or 3,800 UVT/year |

### Deducciones (Deductions) [T1]

| Deduction | Limit |
|-----------|-------|
| Dependientes (dependants) | 10% of gross income, max 32 UVT/month (384 UVT/year) |
| Intereses de vivienda (mortgage interest) | Up to 100 UVT/month (1,200 UVT/year) |
| Medicina prepagada (private health insurance) | Up to 16 UVT/month (192 UVT/year) |
| GMF (4x1000 financial transaction tax, 50%) | 50% of GMF paid is deductible |

### The 40% / 5,040 UVT Cap [T1]

**CRITICAL RULE:** The total of rentas exentas + deducciones cannot exceed 40% of ingresos netos OR 5,040 UVT per year, whichever is lower.

At UVT 2025 = COP 49,799: 5,040 UVT = COP 250,986,960.

---

## Step 6: Renta Presuntiva [T1]

**Legislation:** ET arts. 188-189

| Year | Rate |
|------|------|
| 2021 | 1.5% |
| 2022 | 1% |
| 2023+ | 0% |

**For tax year 2023 onwards (declared from 2024), renta presuntiva is effectively 0%.** The calculation field still appears on Formulario 210 but the result is COP 0.

**Verify this remains at 0% -- future reform could reinstate a positive rate.**

---

## Step 7: Retención en la Fuente (Withholding at Source) [T1]

**Legislation:** ET arts. 383, 392

### Withholding on Independent Professional Services [T1]

| Type of Payment | Withholding Rate |
|-----------------|-----------------|
| Professional services (servicios) | 11% if declarante; 10% if not |
| Honorarios (professional fees) | 11% if declarante; 10% if not |
| Commissions | 11% if declarante; 10% if not |
| Services rendered by non-declarante | 10% or 6% (depending on base) |

### Key Rules [T1]

- Withholding applies when payment exceeds 4 UVT per transaction (for services)
- The entity paying the independent worker must withhold and remit to DIAN
- Retención en la fuente is a credit against the final tax in the annual return
- Self-employed workers should collect certificates (certificados de retención) from all payers

---

## Step 8: Social Security for Independent Workers [T1]

**Legislation:** Ley 100 de 1993; Decreto 1273 de 2018

### Mandatory Contributions [T1]

| Contribution | Rate (on 40% of gross income) | Notes |
|-------------|-------------------------------|-------|
| Pensión | 16% (worker pays full amount) | On ingreso base de cotización (IBC) = 40% of gross |
| Salud | 12.5% (worker pays full amount) | On IBC = 40% of gross |
| ARL | 0.522% (minimum) | Risk-based; worker pays |

### Key Rules [T1]

- IBC (ingreso base de cotización) = 40% of gross monthly income
- IBC cannot be below 1 SMLMV (salario mínimo legal mensual vigente)
- IBC cannot exceed 25 SMLMV
- Contributions must be paid monthly via PILA (Planilla Integrada de Liquidación de Aportes)
- Pension contributions by the worker are non-taxable income (ingreso no constitutivo de renta)

---

## Step 9: Filing and Deadlines [T1]

**Legislation:** ET; Decreto anual de plazos (DIAN)

| Filing / Payment | Deadline |
|-----------------|----------|
| Declaración de Renta (Formulario 210) | August -- October of following year, based on last 2 digits of NIT/cédula |
| Anticipo de renta | Calculated in the return; 75% first 2 years, then formula-based |
| Retención en la fuente (monthly, if agente de retención) | Monthly, per DIAN schedule |

### Filing Schedule Example [T1]

DIAN publishes annual deadlines. Typically:
- Last 2 digits 01-02: early August
- Last 2 digits 99-00: late October
- Check DIAN calendario tributario annually

### Filing Method [T1]

- Via DIAN portal (Servicios en Línea) using firma electrónica
- Formulario 210 (Declaración de Renta y Complementario Personas Naturales)
- Pre-populated data available via "información exógena"

---

## Step 10: Penalties [T1]

**Legislation:** ET arts. 634, 635, 641, 642, 643, 644

| Offence | Penalty |
|---------|---------|
| Late filing (extemporaneidad) | 5% of tax per month of delay (max 100% of tax or 5% of retenciones per month) |
| Late payment interest (intereses moratorios) | Tasa de usura certificada by Superintendencia Financiera (~30-35% annual -- verify) |
| Failure to file (emplazamiento) | 10% of total tax after DIAN emplazamiento |
| Inexactitud (inaccuracy) | 100% of the tax difference (reduced to 50% if corrected before sanción) |
| No filing after emplazamiento | 20% of patrimonio líquido or 160% of tax payable |

---

## Step 11: Record Keeping [T1]

**Legislation:** ET art. 632; Código de Comercio art. 60

| Requirement | Detail |
|-------------|--------|
| Minimum retention | 5 years from the filing deadline (tax); 10 years (commercial books) |
| What to keep | Facturas electrónicas, soportes de costos y gastos, certificados de retención, extractos bancarios, PILA payments |
| Format | Electronic (factura electrónica mandatory since 2020) |
| Electronic invoicing | Via DIAN authorized technological providers |

---

## Step 12: Edge Case Registry

### EC1 -- 40% cap on exemptions + deductions exceeded [T1]
**Situation:** Client's rentas exentas (25% general + AFC) plus deducciones total 55% of ingresos netos.
**Resolution:** Cap at 40% of ingresos netos or 5,040 UVT, whichever is lower. Reduce exemptions/deductions proportionally to 40%.

### EC2 -- Dependant deduction claimed but dependant earns income [T1]
**Situation:** Client claims dependant deduction for spouse who earns COP 40,000,000/year.
**Resolution:** Verify dependant definition under ET art. 387. A dependant is a person who depends economically on the taxpayer. If the dependant has significant independent income, the deduction may not apply. [T2] Flag for reviewer.

### EC3 -- Retención certificates missing [T1]
**Situation:** Client cannot provide certificados de retención from some clients.
**Resolution:** Without certificates, retención cannot be credited. Contact payers to obtain certificates. If unavailable, the withholding credit is lost. Client pays the full tax.

### EC4 -- IBC below minimum [T1]
**Situation:** Independent worker earns COP 2,000,000/month. 40% = COP 800,000 (below SMLMV).
**Resolution:** IBC must be at least 1 SMLMV (COP 1,300,000 for 2024 -- verify 2025). Social security contributions calculated on SMLMV, not on 40% of actual income.

### EC5 -- Renta presuntiva vs renta líquida comparison [T1]
**Situation:** Client asks whether to compare renta presuntiva with renta líquida.
**Resolution:** For 2023+ (declared from 2024), renta presuntiva = 0%. No comparison needed. Taxable income = renta líquida gravable. If future reform reinstates a positive rate, the higher of the two applies.

### EC6 -- Non-resident earning Colombia-source income [T1]
**Situation:** Non-resident freelancer invoices Colombian client.
**Resolution:** Flat 35% withholding at source. No deductions, no progressive table. This is a final tax. Refer to payer for withholding obligations.

### EC7 -- GMF deduction not claimed [T1]
**Situation:** Client pays significant 4x1000 financial transaction tax but does not claim the 50% deduction.
**Resolution:** 50% of GMF paid is deductible under ET art. 115. Include in deducciones. Often overlooked.

### EC8 -- AFC voluntary pension contributions exceed cap [T1]
**Situation:** Client contributes COP 200,000,000 to AFC in one year.
**Resolution:** Exempt portion capped at 30% of gross income or 3,800 UVT (COP 189,236,200 at UVT 49,799), whichever is lower. Excess is not exempt. Still subject to the overall 40%/5,040 UVT cap on total exemptions + deductions.

### EC9 -- First-year filer anticipo calculation [T1]
**Situation:** Client files renta for the first time.
**Resolution:** Anticipo (advance for next year) = 25% of tax determined in first year. Second year = 50%. Third year onwards = 75%. Anticipo is credited against next year's tax.

---

## Step 13: Reviewer Escalation Protocol

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

## Step 14: Test Suite

### Test 1 -- Standard independent worker, mid-range income
**Input:** Resident, gross independent income COP 150,000,000. Costs/expenses COP 30,000,000. Pension contributions (non-taxable) COP 9,600,000. 25% general exemption. No dependants. Retención suffered COP 12,000,000. UVT = 49,799.
**Expected output:** Ingresos netos = 150,000,000 - 9,600,000 = 140,400,000. Renta líquida = 140,400,000 - 30,000,000 = 110,400,000. 25% exemption = 27,600,000 (check cap 2,880 UVT = 143,421,120 -- under cap). Check 40% cap: 27,600,000 / 140,400,000 = 19.7% -- under 40%. Base gravable = 110,400,000 - 27,600,000 = 82,800,000 = ~1,662 UVT. Tax = (1,662 - 1,090) x 19% x 49,799 = 572 x 19% x 49,799 = ~COP 5,412,443. Less retención 12,000,000. Refund ~COP 6,587,557.

### Test 2 -- 40% cap binding
**Input:** Gross income COP 200,000,000. Worker claims 25% exemption (50,000,000) + dependants (20,000,000) + mortgage interest (10,000,000) + AFC (30,000,000) = 110,000,000. Ingresos netos = 190,000,000.
**Expected output:** Total exemptions + deductions = 110,000,000. 40% of ingresos netos = 76,000,000. 5,040 UVT = 250,986,960. Cap at 76,000,000 (the lower amount). Must reduce total claims from 110,000,000 to 76,000,000.

### Test 3 -- Below filing threshold
**Input:** Gross income COP 50,000,000. Patrimonio COP 100,000,000. No credit card purchases above threshold.
**Expected output:** 1,400 UVT (at 47,065 for 2024) = COP 65,891,000. Income below threshold. Patrimonio below 4,500 UVT = 211,793,000. Below threshold. Not required to file (but may file voluntarily for retención refund).

### Test 4 -- High earner in top bracket
**Input:** Gross income COP 2,000,000,000. After deductions/exemptions (at 40% cap): base gravable = COP 1,200,000,000 = ~24,096 UVT. Retención COP 180,000,000.
**Expected output:** Tax in top brackets. (24,096 - 18,970) x 37% x 49,799 + prior brackets cumulative. Significant tax liability minus retención credit.

### Test 5 -- IBC minimum applies
**Input:** Independent worker earns COP 3,000,000/month. IBC at 40% = 1,200,000.
**Expected output:** IBC below SMLMV (verify 2025 SMLMV). Must pay social security on SMLMV, not on 1,200,000.

### Test 6 -- Retención as refund trigger
**Input:** Low-income worker with COP 60,000,000 income. Retención suffered COP 5,000,000. Tax per table = COP 0 (below 1,090 UVT after deductions).
**Expected output:** Full retención refunded. Tax = COP 0. Refund = COP 5,000,000 (less anticipo for next year = 25% of 0 = 0).

---

## PROHIBITIONS

- NEVER use the wrong year's UVT value -- 2024 UVT for 2024 income, 2025 UVT for 2025 income
- NEVER allow total rentas exentas + deducciones to exceed 40% of ingresos netos or 5,040 UVT
- NEVER apply progressive rates to non-residents -- non-residents pay flat 35%
- NEVER ignore the IBC minimum (1 SMLMV) for social security contributions
- NEVER credit retención en la fuente without certificados de retención
- NEVER assume renta presuntiva is zero without verifying -- future reform could reinstate it
- NEVER file without checking all filing thresholds (income, patrimonio, credit cards, purchases, deposits)
- NEVER ignore the anticipo calculation -- it is calculated in the return and paid in advance
- NEVER treat pension contributions as a deduction -- they are ingresos no constitutivos de renta (excluded before arriving at ingresos netos)
- NEVER present tax calculations as definitive -- always label as estimated and direct client to a Contador Público for confirmation

---

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a Contador Público or equivalent licensed practitioner in Colombia) before filing or acting upon.

If you would like a licensed accountant to review your return, visit [openaccountants.com](https://openaccountants.com) and log in to request a professional review.
