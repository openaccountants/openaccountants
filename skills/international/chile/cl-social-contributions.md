---
name: cl-social-contributions
description: Use this skill whenever asked about Chilean self-employed social contributions (cotizaciones previsionales para independientes). Trigger on phrases like "cotizaciones independientes", "AFP independiente", "Fonasa boletas", "SIS seguro invalidez", "retención previsional", "boleta de honorarios cotización", or any question about Chilean social security obligations for independent workers. Covers AFP pension (mandatory since Ley 21.133 phase-in), Fonasa/Isapre health 7%, SIS, withholding from boletas, and Operación Renta annual settlement. ALWAYS read this skill before touching any Chilean social contribution work.
version: 2.0
---

# Chile Social Contributions (Cotizaciones Previsionales) -- Self-Employed Skill v2.0

## Section 1 -- Quick reference

| Field | Value |
|---|---|
| Country | Chile |
| Authority | SII (withholding); Superintendencia de Pensiones (AFP oversight) |
| Primary legislation | DL 3.500 (Pension System); Ley 21.133 (mandatory contributions, 2019) |
| Supporting legislation | Ley 18.469 (Fonasa); Ley 16.744 (SIS) |
| AFP rate | 10% of renta imponible |
| AFP comisión | 0.46%-1.44% (varies by AFP) |
| SIS rate | ~1.49% (2025) |
| Salud rate | 7% (Fonasa/Isapre) |
| Withholding rate | 13.75% of gross boleta (2025) |
| Renta imponible | Gross boleta x 80% / 12 |
| Tope imponible | 87.8 UF/month |
| Phase-in | 100% from 2025 (complete) |
| Settlement | Operación Renta (April) |
| Currency | CLP (UF-linked for tope) |
| Contributor | Open Accountants |
| Validated by | Pending -- requires validation by Chilean contador |
| Validation date | Pending |

---

## Section 2 -- Required inputs and refusal catalogue

### Required inputs

Before computing, you MUST obtain:

1. **Does client issue boletas de honorarios?** -- mandatory withholding applies
2. **Total gross boleta income for the year** -- determines renta imponible
3. **AFP affiliation** -- which AFP and its comisión
4. **Health system** -- Fonasa or Isapre
5. **Any employment income?** -- dual status rules
6. **Tax year** -- phase-in complete from 2025

**If client does not issue boletas, confirm whether voluntary contributor.**

### Refusal catalogue

**R-CL-SOC-1 -- Bilateral agreement.** Trigger: foreign national with bilateral social security agreement. Message: "Bilateral agreements may exempt from Chilean cotizaciones. Escalate for legal review."

### Prohibitions

- NEVER compute without knowing whether client issues boletas
- NEVER use prior year's tope imponible -- verify UF-based cap
- NEVER tell a boleta issuer they can opt out from 2025 -- phase-in complete
- NEVER ignore the 80% factor -- gross boleta is NOT the base
- NEVER assume Fonasa -- confirm Fonasa vs Isapre
- NEVER present AFP comisión without confirming specific AFP
- NEVER assume withholding covers full cotización -- shortfalls are common

---

## Section 3 -- Renta imponible and tope

**Legislation:** DL 3.500 Art. 90

```
renta_imponible = gross_boleta_income x 80% / 12
```

The 80% factor accounts for 20% presumed expenses. Capped at tope imponible (87.8 UF/month, variable in CLP).

---

## Section 4 -- Contribution rates

| Component | Rate | Notes |
|---|---|---|
| AFP (pension) | 10% | Mandatory capitalization |
| AFP comisión | 0.46%-1.44% | Varies by AFP |
| SIS | ~1.49% | Set annually |
| Salud (Fonasa) | 7% | Mandatory statutory |
| Salud (Isapre) | 7% minimum | Difference paid directly by client |

Total effective: ~18.95-19.93% of renta imponible.

---

## Section 5 -- Withholding and annual settlement

### Withholding from boletas

| Item | Detail |
|---|---|
| Rate | 13.75% of gross boleta |
| Withheld by | Pagador (paying entity) |
| Destination | SII holds, distributes at Operación Renta |

### Operación Renta (April)

1. SII calculates total renta imponible
2. Total cotizaciones owed = renta imponible x rates
3. Compare owed vs withheld
4. Difference = additional payment or refund

### Distribution priority

1. SIS (first)
2. AFP (second)
3. Salud (last -- most likely underfunded)

---

## Section 6 -- Payment, registration, and tax interaction

### Registration

Must be affiliated with an AFP. If not, assigned to lowest-comisión AFP. Must declare Fonasa/Isapre affiliation.

### Tax deductibility

| Question | Answer |
|---|---|
| Are cotizaciones deductible? | YES -- reduce income tax base |
| Where? | Annual return (Formulario 22) |
| 13.75% withholding | Covers BOTH income tax and previsional |

### Penalties

| Penalty | Detail |
|---|---|
| Non-affiliation | Assigned to lowest-cost AFP |
| Opt-out from 2025 | No longer available |

---

## Section 7 -- Phase-in completion and Isapre

### Phase-in (Ley 21.133)

From 2025 onward, 100% of renta imponible subject to cotización. No partial exemption.

### Isapre plans above 7%

If Isapre plan costs more than 7%, the difference must be paid directly by the client. Only statutory 7% allocated from withholding.

### Boleta to foreign client

Withholding still applies. If no Chilean pagador, client must self-declare.

---

## Section 8 -- Edge case registry

### EC1 -- Opted out in prior years
**Situation:** Client opted out 2019-2024.
**Resolution:** From 2025, opt-out unavailable. Full cotización deducted at Operación Renta 2026.

### EC2 -- Dual status (employed + boletas)
**Situation:** Employed and issues boletas.
**Resolution:** Employment cotizaciones cover employment income. Boleta withholding covers independent income separately.

### EC3 -- Income exceeds tope
**Situation:** Monthly renta imponible exceeds 87.8 UF.
**Resolution:** Cap at 87.8 UF. Excess has no additional obligation.

### EC4 -- Isapre above 7%
**Situation:** Isapre plan at 9%.
**Resolution:** 2% difference paid directly to Isapre. Flag for reviewer.

### EC5 -- Insufficient withholding
**Situation:** 13.75% withholding totals CLP 500,000 but owed CLP 800,000.
**Resolution:** CLP 300,000 shortfall at Operación Renta. Priority: SIS > AFP > salud.

### EC6 -- No boletas (informal)
**Situation:** Self-employed, no boletas.
**Resolution:** No mandatory cotización. Recommend voluntary. Flag tax compliance issue.

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

### Test 1 -- Standard, Fonasa, AFP Modelo
**Input:** Gross boletas CLP 24,000,000/year. AFP Modelo (0.58%). Fonasa. 2025.
**Expected output:** Renta imponible CLP 1,600,000/month. AFP 10% = CLP 160,000. Comisión = CLP 9,280. SIS = CLP 23,840. Salud = CLP 112,000. Monthly ~CLP 305,120.

### Test 2 -- Exceeds tope
**Input:** Gross CLP 120,000,000/year. AFP Uno (0.46%). Fonasa.
**Expected output:** Monthly capped at 87.8 UF. Rates on capped amount.

### Test 3 -- Dual status
**Input:** Employed CLP 2,000,000/month + boletas CLP 12,000,000/year.
**Expected output:** Boleta renta imponible CLP 800,000/month. Separate cotización.

### Test 4 -- Phase-in complete
**Input:** Client who opted out in 2023. Tax year 2025.
**Expected output:** 100% subject. No exemption.

### Test 5 -- Insufficient withholding
**Input:** Withholding CLP 500,000, owed CLP 800,000.
**Expected output:** CLP 300,000 shortfall at Operación Renta.

### Test 6 -- Isapre above 7%
**Input:** Isapre 9%.
**Expected output:** 7% from withholding. 2% paid directly. Flag.

---

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a CPA, EA, tax attorney, or equivalent licensed practitioner in your jurisdiction) before filing or acting upon.

The most up-to-date, verified version of this skill is maintained at [openaccountants.com](https://openaccountants.com). Log in to access the latest version, request a professional review from a licensed accountant, and track updates as tax law changes.
