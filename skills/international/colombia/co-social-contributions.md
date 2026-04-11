---
name: co-social-contributions
description: Use this skill whenever asked about Colombian self-employed social contributions (aportes a seguridad social para independientes). Trigger on phrases like "seguridad social independientes", "salud y pensión independiente", "IBC independiente", "PILA independiente", "ARL independiente", "40% IBC rule", or any question about Colombian social security obligations for self-employed individuals. Covers salud (12.5%), pensión (16%), ARL, Fondo de Solidaridad Pensional, the 40% IBC rule, PILA filing, and edge cases. ALWAYS read this skill before touching any Colombian social contribution work.
---

# Colombia Social Contributions (Aportes Seguridad Social) -- Self-Employed Skill

---

## Skill Metadata

| Field | Value |
|-------|-------|
| Jurisdiction | Colombia |
| Jurisdiction Code | CO |
| Primary Legislation | Ley 100 de 1993 (Sistema de Seguridad Social Integral), Decreto 1273 de 2018 |
| Supporting Legislation | Ley 797 de 2003 (pensiones), Ley 1122 de 2007 (salud), Decreto 780 de 2016 (sector salud), Decreto 1072 de 2015 (ARL) |
| Tax Authority | UGPP (Unidad de Gestión Pensional y Parafiscales) for enforcement; EPS/AFP/ARL for collection |
| Rate Publisher | MinSalud, MinTrabajo, UGPP |
| Skill Version | 1.0 |
| Confidence Coverage | Tier 1: IBC calculation, contribution rates, PILA filing, payment schedule. Tier 2: prestación de servicios changes (July 2025), multiple contracts, ARL risk classification. Tier 3: pension reform (Ley 2381), disability claims, bilateral agreements. |

---

## Confidence Tier Definitions

- **[T1] Tier 1 -- Deterministic.** Apply exactly as written. No reviewer judgement required.
- **[T2] Tier 2 -- Reviewer Judgement Required.** Claude flags and presents options. Qualified contador must confirm.
- **[T3] Tier 3 -- Out of Scope / Escalate.** Do not guess. Escalate and document.

---

## Step 0: Client Onboarding Questions

Before computing any aporte figure, you MUST know:

1. **Type of independent worker** [T1] -- cuenta propia vs. contrato de prestación de servicios
2. **Monthly gross income** [T1] -- determines IBC
3. **Number of contracts / income sources** [T1] -- affects IBC calculation
4. **ARL risk level** [T1] -- Level I (office work) through Level V (high risk)
5. **Pension regime** [T1] -- RPM (Colpensiones, public) vs. RAIS (private AFP)
6. **EPS affiliation** [T1] -- which EPS for health
7. **Does any contract exceed 1 month?** [T2] -- July 2025 Decreto 1273 change for prestación de servicios

**If monthly gross income is unknown, STOP. Cannot compute IBC.**

---

## Step 1: Ingreso Base de Cotización (IBC) [T1]

**Legislation:** Ley 100/1993, Decreto 1273/2018

### The 40% Rule

```
IBC = monthly_gross_income × 40%
```

- The 40% factor presumes 60% of gross income covers operating expenses
- IBC cannot be less than 1 SMMLV
- IBC cannot exceed 25 SMMLV

### SMMLV 2025

| Item | Amount (COP) |
|------|-------------|
| SMMLV (Salario Mínimo Mensual Legal Vigente) | $1,423,500 |
| Minimum IBC | $1,423,500 (1 SMMLV) |
| Maximum IBC | $35,587,500 (25 SMMLV) |

**If 40% of gross income is below 1 SMMLV, the client must still pay on 1 SMMLV as the floor.**

### Example

| Monthly Gross Income | 40% Calculation | IBC Applied |
|---------------------|----------------|-------------|
| $2,000,000 | $800,000 | $1,423,500 (minimum) |
| $5,000,000 | $2,000,000 | $2,000,000 |
| $100,000,000 | $40,000,000 | $35,587,500 (maximum) |

---

## Step 2: Contribution Rates [T1]

**Legislation:** Ley 100/1993, Ley 797/2003, Ley 1122/2007

| Component | Rate | Base | Who Pays |
|-----------|------|------|----------|
| Salud (health) | 12.5% | IBC | Independent pays 100% |
| Pensión (pension) | 16% | IBC | Independent pays 100% |
| ARL (workplace risk insurance) | 0.522% - 6.960% | IBC | Independent pays (risk-dependent) |
| Fondo de Solidaridad Pensional | 1% | IBC | Only if IBC > 4 SMMLV ($5,694,000) |
| Fondo de Subsistencia | 0.5%-1.5% additional | IBC | Only if IBC > 16 SMMLV |

### ARL Risk Levels

| Level | Rate | Typical Activities |
|-------|------|--------------------|
| I | 0.522% | Office work, consulting, IT |
| II | 1.044% | Light manufacturing |
| III | 2.436% | Industrial work |
| IV | 4.350% | High-risk manufacturing |
| V | 6.960% | Mining, construction, hazardous |

### Total Monthly Contribution (Level I Risk)

```
salud = IBC × 12.5%
pensión = IBC × 16%
ARL = IBC × 0.522%
total = salud + pensión + ARL (+ solidarity fund if applicable)
total ≈ IBC × 29.022%
```

---

## Step 3: Payment Method and Schedule [T1]

**Legislation:** Decreto 1273/2018

| Item | Detail |
|------|--------|
| Payment instrument | PILA (Planilla Integrada de Liquidación de Aportes) |
| PILA operators | SOI, Mi Planilla, Aportes en Línea, Simple |
| Due date | By the last business day of the month of the contribution period |
| Frequency | Monthly |
| Payment channels | Online via PILA operator; bank transfer |

### PILA Filing Steps

1. Access PILA operator platform
2. Enter IBC for the period
3. System auto-calculates contributions per component
4. Confirm and pay electronically
5. Retain planilla receipt as proof

---

## Step 4: Registration [T1]

| Requirement | Detail |
|-------------|--------|
| EPS (health) | Must affiliate with an EPS before first PILA payment |
| AFP/Colpensiones (pension) | Must choose RPM (Colpensiones) or RAIS (private AFP) |
| ARL | Must affiliate with an ARL; risk level determined by activity |
| CCF (Caja de Compensación) | Optional for independents (mandatory for employers) |

---

## Step 5: Prestación de Servicios -- July 2025 Change [T2]

**Legislation:** Decreto 1273/2018

Starting July 2025, for contracts of prestación de servicios exceeding 1 month:

| Before July 2025 | After July 2025 |
|-------------------|-----------------|
| Independent pays 100% of contributions | Contratante (hiring entity) must manage and pay contributions through their PILA |
| Independent responsible for PILA filing | Contratante deducts from contract payments |

**This is a significant change.** [T2] flag for all prestación de servicios contracts to confirm whether the new rules apply.

---

## Step 6: Interaction with Income Tax [T1]

| Question | Answer |
|----------|--------|
| Are aportes deductible? | YES -- mandatory social contributions are deductible for income tax |
| Which tax? | Impuesto de Renta (annual income tax return) |
| IBC as expense? | The 60% presumed expenses (complement of 40% IBC) is NOT a separate deduction -- it is already factored into the IBC |

---

## Step 7: Penalties [T1]

**Legislation:** Ley 100/1993, UGPP enforcement

| Penalty | Detail |
|---------|--------|
| Late PILA payment | Interest (mora) at tasa de usura rate |
| Non-affiliation | UGPP can impose fines up to 5 SMMLV per month of non-compliance |
| Underreporting IBC | UGPP audits and recomputes; back-payments + interest + penalties |
| No ARL affiliation | No workers' compensation coverage; personal liability for injuries |
| UGPP enforcement | UGPP cross-references income tax returns with PILA payments |

---

## Step 8: Edge Case Registry

### EC1 -- Multiple contracts with different entities [T1]
**Situation:** Client has 3 prestación de servicios contracts totaling COP 15,000,000/month.
**Resolution:** Sum all contract income. IBC = COP 15,000,000 x 40% = COP 6,000,000. Pay on combined IBC through a single PILA. Health contribution goes to one EPS only.

### EC2 -- IBC below minimum (low income) [T1]
**Situation:** Client earns COP 2,000,000/month. 40% = COP 800,000, below SMMLV.
**Resolution:** Must pay on 1 SMMLV (COP 1,423,500) as the floor. No exception.

### EC3 -- Dual status: employed + independent [T1]
**Situation:** Client is employed (salary COP 3,000,000) and also has independent income (COP 5,000,000/month).
**Resolution:** Employer handles employee contributions on salary. Client must additionally pay independent contributions on IBC = COP 5,000,000 x 40% = COP 2,000,000. Two separate PILA filings.

### EC4 -- Fondo de Solidaridad Pensional triggered [T1]
**Situation:** Client's IBC exceeds 4 SMMLV (COP 5,694,000).
**Resolution:** Additional 1% solidarity contribution applies on IBC. If IBC > 16 SMMLV, additional 0.5%-1.5% for Fondo de Subsistencia (graduated scale).

### EC5 -- ARL risk level dispute [T2]
**Situation:** Client classified as Risk Level I but performs field work.
**Resolution:** ARL classification should reflect actual risk, not just contract description. [T2] flag for reviewer to verify with ARL provider.

### EC6 -- Prestación de servicios post-July 2025 [T2]
**Situation:** Client has a 6-month prestación de servicios contract starting August 2025.
**Resolution:** Contratante (hiring entity) is responsible for managing and paying social contributions. Verify with contratante that they are complying. [T2] flag -- transition rules may create gaps.

### EC7 -- Pensionado (retiree) working as independent [T1]
**Situation:** Client receives pension but continues working independently.
**Resolution:** Must still pay salud (12.5%) on IBC. Pensión contribution is NOT required. ARL still required.

### EC8 -- Income fluctuates month to month [T1]
**Situation:** Client earns COP 10,000,000 one month and COP 1,000,000 the next.
**Resolution:** IBC is calculated monthly based on actual income that month. COP 10M month: IBC = COP 4,000,000. COP 1M month: IBC = COP 1,423,500 (minimum). Each month's PILA reflects that month's IBC.

### EC9 -- UGPP audit for underreporting [T2]
**Situation:** Client reported IBC of 1 SMMLV but income tax return shows COP 120,000,000 annual income.
**Resolution:** UGPP cross-references. Expected IBC = COP 120M / 12 x 40% = COP 4,000,000/month. Difference triggers back-payments + interest + fines. [T2] flag for reviewer to quantify exposure.

### EC10 -- Pension reform (Ley 2381 / sistema de pilares) [T3]
**Situation:** Client asks about the new pension reform and how it affects independent contributions.
**Resolution:** [T3] Escalate. The pension reform introduces a multi-pillar system with significant changes to contribution routing. Do not advise until implementing regulations are finalized and reviewed by qualified counsel.

---

## Step 9: Reviewer Escalation Protocol

When Claude identifies a [T2] situation:

```
REVIEWER FLAG
Tier: T2
Client: [name]
Situation: [description]
Issue: [what is ambiguous]
Options: [possible treatments]
Recommended: [most likely correct treatment and why]
Action Required: Qualified contador must confirm before advising client.
```

When Claude identifies a [T3] situation:

```
ESCALATION REQUIRED
Tier: T3
Client: [name]
Situation: [description]
Issue: [outside skill scope]
Action Required: Do not advise. Refer to qualified contador. Document gap.
```

---

## Step 10: Test Suite

### Test 1 -- Standard independent, Risk Level I
**Input:** Monthly gross income COP 5,000,000. Risk Level I. RPM (Colpensiones). 2025.
**Expected output:** IBC = COP 2,000,000. Salud = COP 250,000. Pensión = COP 320,000. ARL = COP 10,440. Total ≈ COP 580,440.

### Test 2 -- Income below minimum IBC
**Input:** Monthly gross income COP 2,000,000. Risk Level I.
**Expected output:** 40% = COP 800,000 but below SMMLV. IBC = COP 1,423,500 (minimum). Salud = COP 177,938. Pensión = COP 227,760. ARL = COP 7,431. Total ≈ COP 413,129.

### Test 3 -- High income, solidarity fund triggered
**Input:** Monthly gross income COP 20,000,000. Risk Level I.
**Expected output:** IBC = COP 8,000,000 (40%). Exceeds 4 SMMLV threshold. Solidarity fund 1% = COP 80,000. Salud = COP 1,000,000. Pensión = COP 1,280,000. ARL = COP 41,760. Total ≈ COP 2,401,760.

### Test 4 -- Maximum IBC cap
**Input:** Monthly gross income COP 100,000,000. Risk Level I.
**Expected output:** 40% = COP 40,000,000 but capped at 25 SMMLV = COP 35,587,500. All rates apply to COP 35,587,500.

### Test 5 -- Dual status (employed + independent)
**Input:** Employed (salary COP 3,000,000, employer handles). Independent income COP 8,000,000/month.
**Expected output:** Independent IBC = COP 3,200,000. Separate PILA payment. Employer contribution is separate.

### Test 6 -- Pensionado working
**Input:** Retiree with pension, independent income COP 6,000,000/month.
**Expected output:** IBC = COP 2,400,000. Salud (12.5%) = COP 300,000. ARL = applicable rate. NO pensión contribution required.

### Test 7 -- Multiple contracts
**Input:** Three contracts: COP 3M + COP 5M + COP 2M = COP 10M total.
**Expected output:** Combined IBC = COP 10M x 40% = COP 4,000,000. Single PILA filing on combined IBC.

---

## PROHIBITIONS

- NEVER compute IBC without applying the 40% rule to gross income
- NEVER allow IBC below 1 SMMLV -- the minimum always applies
- NEVER skip ARL for independent workers -- it is mandatory since Decreto 723/2013
- NEVER ignore the Fondo de Solidaridad Pensional when IBC exceeds 4 SMMLV
- NEVER assume a pensionado is exempt from all contributions -- salud and ARL still apply
- NEVER file separate PILA planillas for multiple contracts -- combine income into one IBC
- NEVER present IBC calculations without confirming the current year's SMMLV
- NEVER advise on pension reform (sistema de pilares) without escalating
- NEVER assume the contratante handles contributions without confirming whether post-July 2025 rules apply to the specific contract

---

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a CPA, EA, tax attorney, or equivalent licensed practitioner in your jurisdiction) before filing or acting upon.

The most up-to-date, verified version of this skill is maintained at [openaccountants.com](https://openaccountants.com). Log in to access the latest version, request a professional review from a licensed accountant, and track updates as tax law changes.
