---
name: br-inss
description: Use this skill whenever asked about Brazilian INSS social contributions for self-employed individuals (contribuinte individual). Trigger on phrases like "INSS autônomo", "contribuinte individual", "GPS pagamento", "INSS 20%", "INSS simplificado 11%", "teto INSS", "previdência autônomo", or any question about Brazilian social security obligations for self-employed persons. Covers the 20% normal plan, 11% simplified plan, 5% MEI plan, contribution ceiling (teto), GPS payment mechanics, and edge cases. ALWAYS read this skill before touching any Brazilian INSS work.
version: 2.0
---

# Brazil INSS Contributions (Contribuinte Individual) -- Self-Employed Skill v2.0

## Section 1 -- Quick reference

| Field | Value |
|---|---|
| Country | Brazil (Federative Republic of Brazil) |
| Authority | Receita Federal (collection); INSS (benefits) |
| Primary legislation | Lei 8.212/1991 (Custeio); Lei 8.213/1991 (Benefícios) |
| Supporting legislation | Decreto 3.048/1999; LC 123/2006 (MEI) |
| Plano Normal rate | 20% of income (between salário mínimo and teto) |
| Plano Simplificado rate | 11% of salário mínimo (fixed) |
| MEI rate | 5% of salário mínimo (fixed) |
| Salário mínimo (2025) | R$ 1,518.00 |
| Teto INSS (2025) | R$ 8,157.41 |
| Min contribution (20%) | R$ 303.60 |
| Max contribution (20%) | R$ 1,631.48 |
| Simplified (11%) | R$ 166.98 |
| MEI (5%) | R$ 75.90 |
| GPS due date | 15th of following month |
| Currency | BRL only |
| Contributor | Open Accountants |
| Validated by | Pending -- requires validation by Brazilian contador |
| Validation date | Pending |

---

## Section 2 -- Required inputs and refusal catalogue

### Required inputs

Before computing, you MUST obtain:

1. **Worker classification** -- contribuinte individual, MEI, or facultativo?
2. **Monthly gross income from self-employment**
3. **Concurrent employment (CLT)?** -- dual status rules
4. **Desired plan** -- Plano Normal (20%) or Simplificado (11%)
5. **Does client want aposentadoria por tempo de contribuição?** -- only with 20% plan
6. **Is client a MEI?** -- separate 5% regime

**If classification is unknown, STOP.**

### Refusal catalogue

**R-BR-INSS-1 -- Bilateral agreement.** Trigger: foreign worker with bilateral social security agreement. Message: "Bilateral agreements may exempt from INSS. Escalate for legal review."

**R-BR-INSS-2 -- Complementação interest calculation.** Trigger: computing retroactive complementação (code 1295) with interest. Message: "Interest calculation at SELIC requires current rate data. Escalate to contador."

### Prohibitions

- NEVER allow 11% plan client to believe they qualify for aposentadoria por tempo -- they do not
- NEVER compute below salário mínimo floor
- NEVER compute above teto ceiling (20% plan)
- NEVER ignore PJ withholdings when computing GPS difference
- NEVER tell zero-income client they must pay -- voluntary for zero-income months
- NEVER confuse contribuinte individual codes (1007/1163) with facultativo codes (1406/1473)
- NEVER present 5% MEI rate as available to non-MEI
- NEVER compute complementação interest without current SELIC

---

## Section 3 -- Contribution plans

**Legislation:** Lei 8.212/1991 Art. 21

| Plan | Rate | Base | GPS code | Benefits |
|---|---|---|---|---|
| Plano Normal | 20% | Income (min-teto) | 1007 | Full: idade, tempo, invalidez, pensão, auxílio |
| Plano Simplificado | 11% | Salário mínimo (fixed) | 1163 | Limited: idade only |
| MEI | 5% | Salário mínimo (fixed) | DAS-MEI | Limited: idade only |

---

## Section 4 -- Calculation rules

### Plano Normal (20%)

```
contribution = min(monthly_income, teto_INSS) x 20%
contribution = clamp(R$ 303.60, contribution, R$ 1,631.48)
```

### Plano Simplificado (11%)

```
contribution = R$ 1,518.00 x 11% = R$ 166.98 (fixed)
```

Always based on salário mínimo regardless of actual income.

### PJ withholding (services to companies)

Company withholds 11% of payment (up to teto). If client on 20% plan, pay 9% difference via GPS code 1007. If total withholdings from multiple PJs reach teto, no additional payment needed.

---

## Section 5 -- GPS payment and registration

### GPS (Guia da Previdência Social)

| Item | Detail |
|---|---|
| Generated via | Gov.br, Meu INSS, or manual Carnê |
| Due date | 15th of following month |
| Payment channels | Bank, internet banking, lotéricas |

### GPS codes

| Code | Description |
|---|---|
| 1007 | Contribuinte individual -- Normal (20%) |
| 1163 | Contribuinte individual -- Simplificado (11%) |
| 1104 | Contribuinte individual -- PJ service (empresa retains 11%) |
| 1295 | Complementação (11% to 20% retroactive) |

### Registration

CPF required. Must have NIT/PIS/PASEP.

---

## Section 6 -- Tax deductibility and penalties

### Tax deductibility

| Question | Answer |
|---|---|
| Deductible? | YES -- from gross income for IRPF |
| Where? | Annual IRPF declaration |
| Carnê-leão | INSS deducted before computing monthly estimate |

### Penalties

| Penalty | Detail |
|---|---|
| Late payment | SELIC daily + 0.33%/day (capped 20%) |
| Non-payment | Periods do not count for retirement |
| Retroactive collection | Up to 5 years |

---

## Section 7 -- Dual status and plan changes

### CLT employee + autônomo

Total INSS capped at teto. If employment contributions reach teto, no additional autonomous INSS needed.

### Zero income month

No mandatory contribution. Month does not count. May pay as facultativo optionally.

### Switching from simplified to normal

Client on 11% can switch to 20% going forward. For prior periods, pay complementação (9% difference) via GPS code 1295 with SELIC interest.

### MEI exceeding revenue limit

Must be desenquadrado. Transitions to contribuinte individual. Prior MEI periods (5%) valid for idade only. Flag for reviewer.

---

## Section 8 -- Edge case registry

### EC1 -- Simplified plan wants tempo
**Situation:** 11% plan client needs aposentadoria por tempo.
**Resolution:** Switch to 20% or pay complementação (code 1295) for prior periods.

### EC2 -- Dual status, employment at teto
**Situation:** CLT salary R$ 8,157.41, additional autônomo income.
**Resolution:** Employment already at teto. Zero additional GPS.

### EC3 -- PJ withholding + 20% plan
**Situation:** R$ 6,000 from PJ, 11% withheld = R$ 660. Client on 20%.
**Resolution:** Owed R$ 1,200. Withheld R$ 660. GPS R$ 540.

### EC4 -- Income below mínimo
**Situation:** Income R$ 800.
**Resolution:** Minimum base R$ 1,518. Contribution R$ 303.60 (20%) or R$ 166.98 (11%).

### EC5 -- Multiple PJs, over-withholding
**Situation:** R$ 5,000 from PJ-A + R$ 5,000 from PJ-B. Both withhold 11%.
**Resolution:** Total R$ 10,000 but teto R$ 8,157.41. Max withholding = R$ 897.32. May have overpaid. Request refund.

### EC6 -- Zero income month
**Situation:** No income March 2025.
**Resolution:** No mandatory contribution. May pay facultativo.

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

### Test 1 -- Standard 20%, mid-range
**Input:** Income R$ 4,000. Normal (20%). No PJ withholding.
**Expected output:** R$ 800.00. GPS 1007.

### Test 2 -- Exceeds teto
**Input:** Income R$ 12,000. Normal (20%).
**Expected output:** Base capped R$ 8,157.41. Contribution R$ 1,631.48.

### Test 3 -- Simplified
**Input:** Income R$ 5,000. Simplificado (11%).
**Expected output:** R$ 166.98 (fixed on mínimo). GPS 1163.

### Test 4 -- PJ withholding + 20% difference
**Input:** R$ 6,000 from PJ. Withheld R$ 660. 20% plan.
**Expected output:** Owed R$ 1,200. GPS R$ 540.

### Test 5 -- Dual status, at teto
**Input:** CLT R$ 8,157.41 + autônomo R$ 3,000.
**Expected output:** Zero additional GPS.

### Test 6 -- Zero income
**Input:** No income March 2025.
**Expected output:** No mandatory contribution.

### Test 7 -- Minimum income
**Input:** Income R$ 800. Normal (20%).
**Expected output:** Base R$ 1,518. Contribution R$ 303.60.

---

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a CPA, EA, tax attorney, or equivalent licensed practitioner in your jurisdiction) before filing or acting upon.

The most up-to-date, verified version of this skill is maintained at [openaccountants.com](https://openaccountants.com). Log in to access the latest version, request a professional review from a licensed accountant, and track updates as tax law changes.
