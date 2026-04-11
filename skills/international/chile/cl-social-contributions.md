---
name: cl-social-contributions
description: Use this skill whenever asked about Chilean self-employed social contributions (cotizaciones previsionales para independientes). Trigger on phrases like "cotizaciones independientes", "AFP independiente", "Fonasa boletas", "SIS seguro invalidez", "retención previsional", "boleta de honorarios cotización", or any question about Chilean social security obligations for independent workers. Covers AFP pension (mandatory since Ley 21.133 phase-in), Fonasa/Isapre health 7%, SIS, withholding from boletas, and Operación Renta annual settlement. ALWAYS read this skill before touching any Chilean social contribution work.
---

# Chile Social Contributions (Cotizaciones Previsionales) -- Self-Employed Skill

---

## Skill Metadata

| Field | Value |
|-------|-------|
| Jurisdiction | Chile |
| Jurisdiction Code | CL |
| Primary Legislation | DL 3.500 (Pension System), Ley 21.133 (Mandatory contributions for independientes, 2019 phase-in) |
| Supporting Legislation | DL 3.500 Art. 89-90 (AFP rates), Ley 18.469 (Fonasa), Ley 16.744 (SIS/Workplace safety) |
| Tax Authority | SII (Servicio de Impuestos Internos) for withholding; Superintendencia de Pensiones for AFP oversight |
| Rate Publisher | Superintendencia de Pensiones (annual tope imponible), AFP administrators (comisiones) |
| Skill Version | 1.0 |
| Confidence Coverage | Tier 1: rate calculation, withholding mechanics, annual settlement. Tier 2: Isapre vs. Fonasa election, partial year, voluntary additional contributions. Tier 3: disability pension claims, foreign worker exemptions. |

---

## Confidence Tier Definitions

- **[T1] Tier 1 -- Deterministic.** Apply exactly as written. No reviewer judgement required.
- **[T2] Tier 2 -- Reviewer Judgement Required.** Claude flags and presents options. Qualified contador must confirm.
- **[T3] Tier 3 -- Out of Scope / Escalate.** Do not guess. Escalate and document.

---

## Step 0: Client Onboarding Questions

Before computing any cotización figure, you MUST know:

1. **Does client issue boletas de honorarios?** [T1] -- mandatory withholding applies to boleta issuers
2. **Total gross boleta income for the year** [T1] -- determines renta imponible
3. **AFP affiliation** [T1] -- which AFP and its comisión rate
4. **Health system** [T1] -- Fonasa or Isapre
5. **Any employment income (dependiente)?** [T1] -- dual status rules apply
6. **Tax year** [T1] -- phase-in percentages changed 2019-2028

**If client does not issue boletas and has no dependent employment, confirm whether they are a voluntary contributor.**

---

## Step 1: Determine Obligation [T1]

**Legislation:** Ley 21.133 (effective 2019, phased implementation)

| Worker Type | Obligation | Mechanism |
|-------------|-----------|-----------|
| Boleta de honorarios issuer | Mandatory | Automatic withholding + annual settlement in Operación Renta |
| Independent without boletas | Voluntary (unless above threshold) | Self-declaration |
| Employed (dependiente) | Covered by employer | Payroll withholding |
| Dual status (employed + boletas) | Both apply | Employer covers employment; boleta withholding covers independent income |

**Phase-in schedule (percentage of renta imponible subject to cotización):**

| Year | Percentage |
|------|-----------|
| 2019 | 5% |
| 2020 | 17% |
| 2021 | 37% |
| 2022 | 57% |
| 2023 | 77% |
| 2024 | 90% |
| 2025+ | 100% |

From 2025 onward, 100% of the renta imponible is subject to cotización. The phase-in is complete.

---

## Step 2: Renta Imponible Calculation [T1]

**Legislation:** DL 3.500 Art. 90

### Formula
```
renta_imponible = gross_boleta_income × 80% / 12
```

- The 80% factor accounts for allowable expenses (20% presumed expenses)
- Divide by 12 to get monthly renta imponible
- Capped at tope imponible (maximum pensionable earnings)

### Tope Imponible (2025)

| Item | Amount | Source |
|------|--------|--------|
| Tope imponible mensual | 87.8 UF | Superintendencia de Pensiones |
| UF value | Variable daily (check SII/BCCh) | Banco Central de Chile |

**If monthly renta imponible exceeds 87.8 UF, cap at 87.8 UF for pension/SIS calculations.**

---

## Step 3: Contribution Rates [T1]

**Legislation:** DL 3.500, Ley 16.744

| Component | Rate | Base | Notes |
|-----------|------|------|-------|
| AFP (pension) | 10% | Renta imponible (capped at tope) | Mandatory capitalization account |
| AFP comisión | Variable by AFP (~0.46%-1.44%) | Renta imponible | AFP Uno lowest at 0.46% (Oct 2025) |
| SIS (Seguro de Invalidez y Sobrevivencia) | ~1.49%-1.54% | Renta imponible | Rate set annually; 1.49% for tax year 2025 settlement |
| Salud (Fonasa) | 7% | Renta imponible | Mandatory for Fonasa affiliates |
| Salud (Isapre) | 7% minimum | Renta imponible | May be higher per plan; difference is out-of-pocket |

### Total Effective Rate (approximate)

```
total ≈ 10% (AFP) + comisión (~0.46-1.44%) + 1.49% (SIS) + 7% (salud) ≈ 18.95-19.93%
```

---

## Step 4: Withholding and Settlement Mechanics [T1]

**Legislation:** Ley 21.133, DL 3.500

### Withholding from Boletas

| Item | Detail |
|------|--------|
| Withholding rate | 13.75% of gross boleta (2025) |
| Withheld by | Pagador (entity paying the boleta) |
| Destination | SII holds in trust, distributes during Operación Renta |

### Annual Settlement (Operación Renta, April)

1. SII calculates total renta imponible from all boletas
2. Total cotizaciones owed = renta imponible x applicable rates
3. Compare total owed vs. total withheld during the year
4. Difference = additional payment due OR refund (applied to tax return)

### Distribution Priority

Withheld amounts are allocated in this order:

1. SIS (Seguro de Invalidez y Sobrevivencia)
2. AFP (pension fund)
3. Salud (Fonasa or Isapre)

**If withholding is insufficient to cover all components, health is the last funded.**

---

## Step 5: Registration [T1]

| Requirement | Detail |
|-------------|--------|
| AFP affiliation | Must be affiliated with an AFP. If not, assigned to AFP with lowest comisión. |
| Fonasa/Isapre | Must declare health system affiliation |
| SII | Must have RUT and be registered as contribuyente |
| Boleta issuance | Electronic boletas via SII portal |

---

## Step 6: Interaction with Income Tax [T1]

| Question | Answer |
|----------|--------|
| Are cotizaciones deductible? | YES -- they reduce the base for income tax (impuesto a la renta) |
| Where? | Deducted in the annual tax return (Formulario 22) |
| 13.75% withholding | Covers BOTH income tax withholding AND previsional contributions |

---

## Step 7: Penalties [T1]

| Penalty | Detail |
|---------|--------|
| Non-affiliation to AFP | Assignment to lowest-cost AFP by Superintendencia |
| Failure to declare in Operación Renta | SII adjusts automatically; potential penalties under Código Tributario |
| Opt-out (renouncing cotización) | Was permitted 2019-2024 during phase-in. From 2025, opt-out is no longer available. |

---

## Step 8: Edge Case Registry

### EC1 -- Client opted out in prior years, now 2025 [T1]
**Situation:** Client opted out of previsional deductions during 2019-2024 phase-in period.
**Resolution:** From 2025, opt-out is no longer available. 100% of renta imponible is subject to cotización. Inform client that the full amount will be deducted during Operación Renta 2026 (for tax year 2025).

### EC2 -- Dual status: employed + boletas [T1]
**Situation:** Client is both employed (contrato de trabajo) and issues boletas de honorarios.
**Resolution:** Employment cotizaciones cover employment income. Boleta withholding covers independent income separately. Both apply. Tope imponible applies to each source independently but total pension contribution may be capped.

### EC3 -- Income exceeds tope imponible [T1]
**Situation:** Client's monthly renta imponible exceeds 87.8 UF.
**Resolution:** Cap renta imponible at 87.8 UF for AFP/SIS calculations. Health (7%) also capped. Excess income has no additional previsional obligation.

### EC4 -- Client on Isapre with plan above 7% [T2]
**Situation:** Client's Isapre plan costs 9% of renta imponible, but only 7% is covered by withholding.
**Resolution:** The 2% difference must be paid directly to the Isapre by the client. Only the statutory 7% is allocated from withholding. [T2] flag for reviewer to confirm Isapre plan terms.

### EC5 -- No boletas issued (informal independent) [T2]
**Situation:** Client is self-employed but does not issue boletas de honorarios.
**Resolution:** Mandatory cotización only applies to boleta issuers. Client may contribute voluntarily. If client should be issuing boletas but is not, this is a tax compliance issue. [T2] flag for reviewer.

### EC6 -- Foreign worker with bilateral agreement [T3]
**Situation:** Client is a foreign national working independently in Chile, from a country with a social security agreement.
**Resolution:** [T3] Escalate. Bilateral agreements may exempt from Chilean cotizaciones. Do not advise without legal review.

### EC7 -- Insufficient withholding to cover all components [T1]
**Situation:** Total 13.75% withholding does not fully cover AFP + SIS + salud.
**Resolution:** Distribution follows priority order (SIS first, then AFP, then salud). Shortfall on health means client may have gaps in Fonasa coverage. Additional voluntary payment can be made.

### EC8 -- Client turns 65 (men) or 60 (women) during the year [T2]
**Situation:** Client reaches pension age mid-year.
**Resolution:** Cotización obligation may change upon retirement. If client begins receiving pension but continues working, contributions may still apply. [T2] flag for reviewer.

### EC9 -- Boleta issued to foreign client [T1]
**Situation:** Client issues a boleta de honorarios for services rendered to a foreign entity.
**Resolution:** Withholding still applies to boletas regardless of who the client is. The 13.75% is withheld by the pagador if in Chile; if no Chilean pagador, client must self-declare.

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

### Test 1 -- Standard independent, Fonasa, AFP Modelo
**Input:** Gross boleta income CLP 24,000,000/year. AFP Modelo (comisión 0.58%). Fonasa. Tax year 2025.
**Expected output:** Renta imponible = CLP 24M x 80% / 12 = CLP 1,600,000/month. AFP 10% = CLP 160,000. Comisión 0.58% = CLP 9,280. SIS 1.49% = CLP 23,840. Salud 7% = CLP 112,000. Monthly total ≈ CLP 305,120.

### Test 2 -- Income exceeds tope imponible
**Input:** Gross boleta income CLP 120,000,000/year. AFP Uno (comisión 0.46%). Fonasa.
**Expected output:** Monthly renta imponible = CLP 8,000,000 but CAPPED at 87.8 UF (~CLP 3,300,000 approx. depending on UF value). All rates apply to capped amount only.

### Test 3 -- Dual status employed + boletas
**Input:** Client earns CLP 2,000,000/month employed + CLP 12,000,000/year from boletas.
**Expected output:** Employment cotizaciones handled by employer. Boleta renta imponible = CLP 12M x 80% / 12 = CLP 800,000. Separate cotización applies to this amount.

### Test 4 -- Phase-in complete (2025)
**Input:** Client who opted out in 2023. Tax year 2025.
**Expected output:** Opt-out no longer available from 2025. 100% of renta imponible subject to cotización. No partial exemption.

### Test 5 -- Insufficient withholding
**Input:** Client with low boleta volume; 13.75% withholding totals CLP 500,000 but cotizaciones owed total CLP 800,000.
**Expected output:** CLP 300,000 shortfall settled during Operación Renta. Priority: SIS funded first, then AFP, then salud.

### Test 6 -- Isapre plan above 7%
**Input:** Client on Isapre plan costing 9% of renta imponible.
**Expected output:** 7% allocated from withholding to Isapre. 2% difference paid directly by client to Isapre. Flag for reviewer.

### Test 7 -- No boletas issued
**Input:** Client is a freelance tutor paid in cash, no boletas.
**Expected output:** No mandatory cotización (only boleta issuers are covered). Recommend voluntary affiliation. Flag potential tax compliance issue.

---

## PROHIBITIONS

- NEVER compute cotizaciones without knowing whether the client issues boletas de honorarios
- NEVER use a prior year's tope imponible -- verify UF-based cap for current year
- NEVER tell a boleta-issuing client they can opt out of cotizaciones from 2025 onward -- the phase-in is complete
- NEVER ignore the 80% factor when computing renta imponible -- gross boleta income is NOT the base
- NEVER assume Fonasa is the health system -- confirm whether client is on Fonasa or Isapre
- NEVER present AFP comisión rates without confirming the client's specific AFP
- NEVER advise on bilateral social security agreements without escalating
- NEVER assume withholding covers the full cotización -- shortfalls are common and settled in Operación Renta
- NEVER conflate the 13.75% withholding rate with the actual cotización rate -- 13.75% includes income tax withholding

---

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a CPA, EA, tax attorney, or equivalent licensed practitioner in your jurisdiction) before filing or acting upon.

The most up-to-date, verified version of this skill is maintained at [openaccountants.com](https://openaccountants.com). Log in to access the latest version, request a professional review from a licensed accountant, and track updates as tax law changes.
