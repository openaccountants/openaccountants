---
name: co-social-contributions
description: Use this skill whenever asked about Colombian self-employed social contributions (aportes a seguridad social para independientes). Trigger on phrases like "seguridad social independientes", "salud y pensión independiente", "IBC independiente", "PILA independiente", "ARL independiente", "40% IBC rule", or any question about Colombian social security obligations for self-employed individuals. Covers salud (12.5%), pensión (16%), ARL, Fondo de Solidaridad Pensional, the 40% IBC rule, PILA filing, and edge cases. ALWAYS read this skill before touching any Colombian social contribution work.
version: 2.0
---

# Colombia Social Contributions (Aportes Seguridad Social) -- Self-Employed Skill v2.0

## Section 1 -- Quick reference

| Field | Value |
|---|---|
| Country | Colombia |
| Authority | UGPP (enforcement); EPS/AFP/ARL (collection) |
| Primary legislation | Ley 100 de 1993; Decreto 1273 de 2018 |
| Supporting legislation | Ley 797/2003; Ley 1122/2007; Decreto 780/2016; Decreto 1072/2015 |
| IBC rule | 40% of monthly gross income |
| Minimum IBC | 1 SMMLV = COP 1,423,500 (2025) |
| Maximum IBC | 25 SMMLV = COP 35,587,500 |
| Salud rate | 12.5% |
| Pensión rate | 16% |
| ARL rate (Level I) | 0.522% |
| Fondo Solidaridad | 1% (when IBC > 4 SMMLV) |
| Total (Level I, no solidarity) | ~29.022% of IBC |
| Payment method | PILA (Planilla Integrada) |
| Due date | Last business day of contribution month |
| Currency | COP only |
| Contributor | Open Accountants |
| Validated by | Pending -- requires validation by Colombian contador |
| Validation date | Pending |

---

## Section 2 -- Required inputs and refusal catalogue

### Required inputs

Before computing, you MUST obtain:

1. **Type of independent** -- cuenta propia vs contrato de prestación de servicios
2. **Monthly gross income** -- determines IBC
3. **Number of contracts / income sources**
4. **ARL risk level** -- Level I through V
5. **Pension regime** -- RPM (Colpensiones) vs RAIS (private AFP)
6. **EPS affiliation**
7. **Contract duration** -- post-July 2025 rules for prestación de servicios

**If monthly gross income is unknown, STOP.**

### Refusal catalogue

**R-CO-SOC-1 -- Pension reform.** Trigger: question about Ley 2381 / sistema de pilares. Message: "Pension reform implementing regulations not finalized. Escalate to qualified counsel."

### Prohibitions

- NEVER compute IBC without applying the 40% rule
- NEVER allow IBC below 1 SMMLV
- NEVER skip ARL -- mandatory since Decreto 723/2013
- NEVER ignore Fondo de Solidaridad when IBC > 4 SMMLV
- NEVER assume pensionado exempt from all contributions -- salud and ARL still apply
- NEVER file separate PILA for multiple contracts -- combine into one IBC
- NEVER present IBC without confirming current SMMLV
- NEVER assume contratante handles contributions without confirming post-July 2025 rules

---

## Section 3 -- IBC calculation

**Legislation:** Ley 100/1993, Decreto 1273/2018

```
IBC = monthly_gross_income x 40%
IBC = clamp(1_SMMLV, IBC, 25_SMMLV)
```

| Monthly gross | 40% calc | IBC applied |
|---|---|---|
| COP 2,000,000 | COP 800,000 | COP 1,423,500 (minimum) |
| COP 5,000,000 | COP 2,000,000 | COP 2,000,000 |
| COP 100,000,000 | COP 40,000,000 | COP 35,587,500 (maximum) |

---

## Section 4 -- Contribution rates

| Component | Rate | Notes |
|---|---|---|
| Salud | 12.5% | Independent pays 100% |
| Pensión | 16% | Independent pays 100% |
| ARL Level I | 0.522% | Office/consulting/IT |
| ARL Level II | 1.044% | Light manufacturing |
| ARL Level III | 2.436% | Industrial |
| ARL Level IV | 4.350% | High-risk manufacturing |
| ARL Level V | 6.960% | Mining/construction |
| Fondo Solidaridad | 1% | Only if IBC > 4 SMMLV |
| Fondo Subsistencia | 0.5-1.5% additional | Only if IBC > 16 SMMLV |

---

## Section 5 -- Computation and PILA filing

### Computation (Level I)

```
salud = IBC x 12.5%
pensión = IBC x 16%
ARL = IBC x 0.522%
solidarity = IBC x 1% (if IBC > 4 SMMLV)
total = salud + pensión + ARL + solidarity
```

### PILA filing

1. Access PILA operator (SOI, Mi Planilla, Aportes en Línea)
2. Enter IBC for period
3. System calculates per component
4. Confirm and pay electronically

---

## Section 6 -- Payment schedule, tax deductibility, and penalties

### Payment schedule

Monthly via PILA. Due by last business day of contribution month.

### Prestación de servicios -- July 2025 change

For contracts > 1 month: contratante (hiring entity) must manage and pay contributions through their PILA. Verify compliance. Flag for reviewer.

### Tax deductibility

| Question | Answer |
|---|---|
| Are aportes deductible? | YES -- for impuesto de renta |
| IBC as expense? | 60% presumed expenses already factored into IBC |

### Penalties

| Penalty | Detail |
|---|---|
| Late PILA | Interest at tasa de usura |
| Non-affiliation | UGPP fines up to 5 SMMLV/month |
| Underreporting | UGPP audit + back-payments + penalties |
| UGPP enforcement | Cross-references income tax with PILA |

---

## Section 7 -- Registration and special situations

### Registration

Must affiliate with EPS, AFP/Colpensiones, and ARL before first PILA payment.

### Pensionado working independently

Must still pay salud (12.5%) and ARL. Pensión NOT required.

### Multiple contracts

Sum all contract income. Apply 40% to total. Single PILA filing on combined IBC.

### Income fluctuates monthly

IBC calculated monthly on actual income. Each month's PILA reflects that month's IBC (subject to minimum).

---

## Section 8 -- Edge case registry

### EC1 -- Multiple contracts
**Situation:** 3 contracts totaling COP 15,000,000/month.
**Resolution:** IBC = COP 6,000,000. Single PILA.

### EC2 -- Below minimum
**Situation:** Income COP 2,000,000, 40% = COP 800,000.
**Resolution:** IBC = COP 1,423,500 (minimum).

### EC3 -- Dual status (employed + independent)
**Situation:** Employed COP 3,000,000 + independent COP 5,000,000.
**Resolution:** Independent IBC = COP 2,000,000. Separate PILA.

### EC4 -- Fondo Solidaridad triggered
**Situation:** IBC exceeds 4 SMMLV.
**Resolution:** Additional 1% applies. Above 16 SMMLV: graduated additional 0.5-1.5%.

### EC5 -- ARL risk dispute
**Situation:** Classified Level I but does field work.
**Resolution:** Classification should reflect actual risk. Flag for reviewer.

### EC6 -- Prestación de servicios post-July 2025
**Situation:** 6-month contract starting August 2025.
**Resolution:** Contratante responsible. Verify compliance. Flag.

### EC7 -- UGPP audit
**Situation:** IBC reported at 1 SMMLV but income tax shows COP 120M annual.
**Resolution:** Expected IBC COP 4,000,000/month. Back-payments + penalties. Flag.

---

## Section 9 -- Reviewer escalation protocol

When a situation requires reviewer judgement:

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

When a situation is outside skill scope:

```
ESCALATION REQUIRED
Tier: T3
Client: [name]
Situation: [description]
Issue: [outside skill scope]
Action Required: Do not advise. Refer to qualified contador. Document gap.
```

---

## Section 10 -- Test suite

### Test 1 -- Standard, Risk Level I
**Input:** Gross COP 5,000,000. Level I. RPM. 2025.
**Expected output:** IBC COP 2,000,000. Salud COP 250,000. Pensión COP 320,000. ARL COP 10,440. Total ~COP 580,440.

### Test 2 -- Below minimum
**Input:** Gross COP 2,000,000. Level I.
**Expected output:** IBC COP 1,423,500. Total ~COP 413,129.

### Test 3 -- High income, solidarity
**Input:** Gross COP 20,000,000. Level I.
**Expected output:** IBC COP 8,000,000. Solidarity 1% = COP 80,000. Total ~COP 2,401,760.

### Test 4 -- Maximum cap
**Input:** Gross COP 100,000,000. Level I.
**Expected output:** IBC COP 35,587,500. All rates on capped amount.

### Test 5 -- Dual status
**Input:** Employed COP 3,000,000 + independent COP 8,000,000.
**Expected output:** Independent IBC COP 3,200,000. Separate PILA.

### Test 6 -- Pensionado
**Input:** Retiree, independent COP 6,000,000.
**Expected output:** IBC COP 2,400,000. Salud + ARL only. No pensión.

### Test 7 -- Multiple contracts
**Input:** COP 3M + 5M + 2M = COP 10M.
**Expected output:** Combined IBC COP 4,000,000. Single PILA.

---

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a CPA, EA, tax attorney, or equivalent licensed practitioner in your jurisdiction) before filing or acting upon.

The most up-to-date, verified version of this skill is maintained at [openaccountants.com](https://openaccountants.com). Log in to access the latest version, request a professional review from a licensed accountant, and track updates as tax law changes.
