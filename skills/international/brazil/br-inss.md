---
name: br-inss
description: Use this skill whenever asked about Brazilian INSS social contributions for self-employed individuals (contribuinte individual). Trigger on phrases like "INSS autônomo", "contribuinte individual", "GPS pagamento", "INSS 20%", "INSS simplificado 11%", "teto INSS", "previdência autônomo", or any question about Brazilian social security obligations for self-employed persons. Covers the 20% normal plan, 11% simplified plan, 5% MEI plan, contribution ceiling (teto), GPS payment mechanics, and edge cases. ALWAYS read this skill before touching any Brazilian INSS work.
---

# Brazil INSS Contributions (Contribuinte Individual) -- Self-Employed Skill

---

## Skill Metadata

| Field | Value |
|-------|-------|
| Jurisdiction | Brazil |
| Jurisdiction Code | BR |
| Primary Legislation | Lei 8.212/1991 (Custeio da Previdência Social), Lei 8.213/1991 (Benefícios) |
| Supporting Legislation | Decreto 3.048/1999 (Regulamento da Previdência Social), LC 123/2006 (Simples Nacional / MEI) |
| Tax Authority | Receita Federal do Brasil (RFB) for collection; INSS for benefits |
| Rate Publisher | Governo Federal (annual ceiling adjustments, portarias) |
| Skill Version | 1.0 |
| Confidence Coverage | Tier 1: rate calculation, ceiling, GPS payment, plan selection. Tier 2: complementação, transition between plans, MEI vs. individual. Tier 3: aposentadoria por tempo/invalidez, bilateral agreements, judicial decisions. |

---

## Confidence Tier Definitions

- **[T1] Tier 1 -- Deterministic.** Apply exactly as written. No reviewer judgement required.
- **[T2] Tier 2 -- Reviewer Judgement Required.** Claude flags and presents options. Qualified contador must confirm.
- **[T3] Tier 3 -- Out of Scope / Escalate.** Do not guess. Escalate and document.

---

## Step 0: Client Onboarding Questions

Before computing any INSS figure, you MUST know:

1. **Worker classification** [T1] -- contribuinte individual (autônomo), MEI, or facultativo
2. **Monthly gross income from self-employment** [T1] -- determines contribution base
3. **Does client also have employment income (CLT)?** [T1] -- dual status rules
4. **Desired plan** [T1] -- Plano Normal (20%) or Plano Simplificado (11%)
5. **Does client want aposentadoria por tempo de contribuição?** [T1] -- only available under 20% plan
6. **Is client a MEI (Microempreendedor Individual)?** [T1] -- separate 5% regime

**If worker classification is unknown, STOP. Do not compute contributions.**

---

## Step 1: Contribution Plans [T1]

**Legislation:** Lei 8.212/1991 Art. 21

### Plan Options for Contribuinte Individual

| Plan | Rate | Base | GPS Code | Benefits |
|------|------|------|----------|----------|
| Plano Normal | 20% | Income between 1 salário mínimo and teto INSS | 1007 | Full: aposentadoria por idade, tempo de contribuição, invalidez, pensão por morte, auxílio-doença |
| Plano Simplificado | 11% | 1 salário mínimo (fixed base) | 1163 | Limited: aposentadoria por idade only (no tempo de contribuição) |
| MEI | 5% | 1 salário mínimo (fixed base) | DAS-MEI | Limited: aposentadoria por idade only |

### Key Values (2025)

| Item | Amount (BRL) | Source |
|------|-------------|--------|
| Salário mínimo | R$ 1,518.00 | Decreto federal 2025 |
| Teto INSS (contribution ceiling) | R$ 8,157.41 | Portaria MPS 2025 |
| Minimum contribution (20% plan) | R$ 303.60 (20% x R$ 1,518) | Calculated |
| Maximum contribution (20% plan) | R$ 1,631.48 (20% x R$ 8,157.41) | Calculated |
| Simplified plan contribution (11%) | R$ 166.98 (11% x R$ 1,518) | Calculated |
| MEI contribution (5%) | R$ 75.90 (5% x R$ 1,518) | Calculated |

---

## Step 2: Contribution Calculation [T1]

**Legislation:** Lei 8.212/1991

### Plano Normal (20%)

```
contribution = min(monthly_income, teto_INSS) × 20%
contribution = clamp(contribution, R$ 303.60, R$ 1,631.48)
```

### Plano Simplificado (11%)

```
contribution = salário_mínimo × 11% = R$ 166.98 (fixed)
```

**The simplified plan is ALWAYS based on 1 salário mínimo, regardless of actual income.**

### Calculation Examples (2025)

| Monthly Income | Plan | Base | Contribution |
|---------------|------|------|-------------|
| R$ 3,000 | Normal (20%) | R$ 3,000 | R$ 600.00 |
| R$ 10,000 | Normal (20%) | R$ 8,157.41 (teto) | R$ 1,631.48 |
| R$ 1,518 | Normal (20%) | R$ 1,518 (mínimo) | R$ 303.60 |
| R$ 5,000 | Simplified (11%) | R$ 1,518 (fixed) | R$ 166.98 |
| R$ 50,000 | Normal (20%) | R$ 8,157.41 (teto) | R$ 1,631.48 |

---

## Step 3: GPS Payment [T1]

**Legislation:** Lei 8.212/1991, IN RFB

### GPS (Guia da Previdência Social)

| Item | Detail |
|------|--------|
| What | Payment voucher for INSS contributions |
| Where to generate | Portal Gov.br, Meu INSS, or manually (Carnê GPS) |
| Due date | 15th of the month following the competência (contribution period) |
| If 15th is weekend/holiday | Due on the next business day |
| Payment channels | Bank branch, internet banking, lottery houses (lotéricas) |

### GPS Codes for Contribuinte Individual

| Code | Description |
|------|-------------|
| 1007 | Contribuinte individual -- Plano Normal (20%) |
| 1163 | Contribuinte individual -- Plano Simplificado (11%) |
| 1104 | Contribuinte individual -- prestador de serviço a empresa (empresa retém 11%) |
| 1406 | Facultativo -- Plano Normal (20%) |
| 1473 | Facultativo -- Plano Simplificado (11%) |

---

## Step 4: Withholding When Providing Services to Companies [T1]

**Legislation:** Lei 8.212/1991 Art. 4

| Situation | Treatment |
|-----------|-----------|
| Individual provides service to a company (PJ) | Company must withhold 11% of payment (up to teto) and remit to INSS |
| Individual provides service to another individual (PF) | No withholding; individual pays own GPS |
| Multiple PJ clients in one month | Each company withholds 11%; total withholdings capped at teto |

**If company withholds 11% and client is on the 20% plan, the client must pay the 9% difference via GPS (code 1007).**

**If total withholdings from PJ clients reach the teto, no additional GPS payment is needed for that month.**

---

## Step 5: Registration [T1]

| Requirement | Detail |
|-------------|--------|
| Where | INSS office, Meu INSS portal, or CNIS (Cadastro Nacional de Informações Sociais) |
| Document | CPF (Cadastro de Pessoa Física) |
| NIT/PIS/PASEP | Must have a NIT (Número de Inscrição do Trabalhador) or PIS/PASEP |
| When | Before first contribution payment |

---

## Step 6: Interaction with Income Tax [T1]

| Question | Answer |
|----------|--------|
| Are INSS contributions deductible? | YES -- deductible from gross income for IRPF (Imposto de Renda Pessoa Física) |
| Where reported? | Annual IRPF declaration (Declaração de Ajuste Anual) |
| Carnê-leão | Monthly estimated income tax; INSS paid is deducted before computing carnê-leão |

---

## Step 7: Penalties [T1]

**Legislation:** Lei 8.212/1991

| Penalty | Detail |
|---------|--------|
| Late payment | SELIC rate applied daily on outstanding GPS |
| Minimum fine | 0.33% per day of delay, capped at 20% |
| No contribution = no benefit | Periods without payment do not count for retirement eligibility |
| INSS can collect retroactively | Up to 5 years of unpaid contributions (prescrição) |

---

## Step 8: Edge Case Registry

### EC1 -- Client on simplified plan wants aposentadoria por tempo [T1]
**Situation:** Client on Plano Simplificado (11%) discovers they need aposentadoria por tempo de contribuição.
**Resolution:** Plano Simplificado does not grant tempo de contribuição. Client must either: (a) switch to 20% plan going forward, or (b) pay the complementação (9% difference) for prior simplified periods via GPS code 1295.

### EC2 -- Dual status: CLT employee + autônomo [T1]
**Situation:** Client is employed (CLT, employer withholds INSS) and also works as autônomo.
**Resolution:** Total INSS (employment + autonomous) capped at teto. If employment contributions already reach teto, no additional autonomous contribution is needed. If below teto, pay GPS on autonomous income up to the remaining ceiling.

### EC3 -- Services to company (PJ) -- 11% withheld vs. 20% plan [T1]
**Situation:** Client on 20% plan provides services to a company. Company withholds 11%.
**Resolution:** Client owes the 9% difference. Calculate: (income x 20%) - (11% withheld by PJ). Pay difference via GPS code 1007. If multiple PJs and total withholdings reach teto x 11% = teto x 20%, no difference owed.

### EC4 -- Income below salário mínimo [T1]
**Situation:** Client earned R$ 800 in a given month.
**Resolution:** Minimum contribution base is 1 salário mínimo. Client must pay at least R$ 303.60 (20% plan) or R$ 166.98 (11% plan) regardless of actual income.

### EC5 -- MEI exceeding revenue limit [T2]
**Situation:** MEI's annual revenue exceeds R$ 81,000 (or the current MEI ceiling).
**Resolution:** Must be desenquadrado (removed from MEI). Transitions to contribuinte individual. Prior MEI contributions (5%) remain valid but only for aposentadoria por idade. [T2] flag for reviewer -- transition timing and complementação options.

### EC6 -- Complementação of prior simplified periods [T2]
**Situation:** Client paid 11% for 5 years and now wants to complement to 20% for all those years.
**Resolution:** Can pay the 9% difference for each month via GPS code 1295 (complementação). Interest (SELIC) applies from original due date. [T2] flag for reviewer -- calculate total including interest.

### EC7 -- Foreign worker in Brazil [T2]
**Situation:** Foreign national working as autônomo in Brazil.
**Resolution:** Must contribute to INSS if performing remunerated activity in Brazil, unless covered by a bilateral social security agreement (e.g., with Portugal, Spain, Japan). [T2] flag for reviewer to confirm bilateral agreement status.

### EC8 -- Month with no income [T1]
**Situation:** Autônomo had no income in July.
**Resolution:** Contribution is NOT mandatory for months with zero income (unlike Monotributo in Argentina). However, the month will not count toward retirement. Client may pay as facultativo if they want the month to count.

### EC9 -- Income exceeds teto multiple times in one month [T1]
**Situation:** Client receives R$ 5,000 from PJ-A and R$ 5,000 from PJ-B in the same month.
**Resolution:** Total income = R$ 10,000 but teto = R$ 8,157.41. Total withholdings should not exceed 11% x teto = R$ 897.32. If both PJs withhold independently, client may have overpaid. Request devolução (refund) or use as credit.

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

### Test 1 -- Standard 20% plan, mid-range income
**Input:** Monthly income R$ 4,000. Plano Normal (20%). No PJ withholding.
**Expected output:** Contribution = R$ 4,000 x 20% = R$ 800.00. GPS code 1007. Due by 15th of following month.

### Test 2 -- Income exceeds teto
**Input:** Monthly income R$ 12,000. Plano Normal (20%).
**Expected output:** Base capped at R$ 8,157.41. Contribution = R$ 1,631.48. Income above teto has no additional INSS obligation.

### Test 3 -- Simplified plan
**Input:** Monthly income R$ 5,000. Plano Simplificado (11%).
**Expected output:** Contribution = R$ 1,518 x 11% = R$ 166.98 (fixed on salário mínimo). GPS code 1163. No aposentadoria por tempo de contribuição.

### Test 4 -- PJ withholding + 20% plan difference
**Input:** Income R$ 6,000 from one PJ. PJ withholds 11% = R$ 660. Client on 20% plan.
**Expected output:** Total owed = R$ 6,000 x 20% = R$ 1,200. Already withheld = R$ 660. GPS payment = R$ 540 (9% difference).

### Test 5 -- Dual status, employment at teto
**Input:** CLT salary R$ 8,157.41 (employer withholds full INSS). Additional autônomo income R$ 3,000.
**Expected output:** Employment INSS already at teto. No additional autonomous INSS due. Zero GPS payment.

### Test 6 -- Zero income month
**Input:** No income in March 2025. Contribuinte individual.
**Expected output:** No mandatory contribution. Month does not count for retirement. Client may optionally pay as facultativo (code 1406/1473).

### Test 7 -- Minimum income
**Input:** Income R$ 800. Plano Normal (20%).
**Expected output:** Minimum base = R$ 1,518. Contribution = R$ 303.60. Must pay on salário mínimo regardless of actual income.

---

## PROHIBITIONS

- NEVER allow a client on the 11% simplified plan to believe they qualify for aposentadoria por tempo de contribuição -- they do not
- NEVER compute contributions below the salário mínimo floor
- NEVER compute contributions above the teto INSS ceiling (for the 20% plan)
- NEVER ignore PJ withholdings when computing the GPS difference owed
- NEVER tell a client with zero income that they must pay -- it is voluntary (facultativo) for months without income
- NEVER confuse contribuinte individual codes (1007/1163) with facultativo codes (1406/1473) or empresa codes
- NEVER advise on bilateral social security agreements without escalating
- NEVER present the 5% MEI rate as available to non-MEI contributors
- NEVER compute complementação (code 1295) interest without consulting current SELIC rates

---

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a CPA, EA, tax attorney, or equivalent licensed practitioner in your jurisdiction) before filing or acting upon.

The most up-to-date, verified version of this skill is maintained at [openaccountants.com](https://openaccountants.com). Log in to access the latest version, request a professional review from a licensed accountant, and track updates as tax law changes.
