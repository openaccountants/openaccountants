---
name: pt-income-tax
description: >
  Use this skill whenever asked about Portuguese individual income tax (IRS) for self-employed individuals (trabalhadores independentes). Trigger on phrases like "how much tax do I pay in Portugal", "IRS", "Modelo 3", "Anexo B", "Categoria B", "regime simplificado", "contabilidade organizada", "retenção na fonte", "trabalhador independente", "recibos verdes", "income tax return Portugal", "NIF", or any question about filing or computing income tax for a self-employed or freelance client in Portugal. This skill covers the Modelo 3 + Anexo B annual return, Categoria B income, regime simplificado vs contabilidade organizada, progressive IRS brackets, adicional de solidariedade, allowable deductions, withholding tax, IRS Jovem, and filing deadlines. ALWAYS read this skill before touching any Portuguese income tax work.
version: 1.0
jurisdiction: PT
tax_year: 2025
category: international
depends_on:
  - income-tax-workflow-base
---

# Portugal Income Tax (IRS) -- Self-Employed Skill

---

## Skill Metadata

| Field | Value |
|-------|-------|
| Jurisdiction | Portugal |
| Jurisdiction Code | PT |
| Primary Legislation | Código do Imposto sobre o Rendimento das Pessoas Singulares (CIRS), approved by Decreto-Lei 442-A/88 |
| Supporting Legislation | CIRS Art. 31 (regime simplificado); Art. 68 (progressive brackets); Art. 101 (retenção na fonte); Art. 151 (professions table); Lei 55-A/2025 (OE2025 amendments); Decreto Regulamentar 25/2009 (depreciation); CIRS Art. 12-B (IRS Jovem) |
| Tax Authority | Autoridade Tributária e Aduaneira (AT) |
| Filing Portal | Portal das Finanças (portaldasfinancas.gov.pt) |
| Contributor | Open Accountants Community |
| Validated By | Pending -- requires sign-off by a Portuguese Contabilista Certificado (CC) |
| Validation Date | Pending |
| Skill Version | 1.0 |
| Confidence Coverage | Tier 1: rate table application, regime simplificado coefficients, withholding rates, filing deadline, adicional de solidariedade. Tier 2: contabilidade organizada expense classification, mixed-use apportionment, home office, regime choice optimisation. Tier 3: NHR (Non-Habitual Resident) regime, foreign income, double taxation treaties, crypto assets, exit tax. |

---

## Confidence Tier Definitions

- **[T1] Tier 1 -- Deterministic.** Apply exactly as written. No reviewer judgement required.
- **[T2] Tier 2 -- Reviewer Judgement Required.** Claude flags and presents options. Licensed Contabilista Certificado must confirm.
- **[T3] Tier 3 -- Out of Scope / Escalate.** Do not guess. Escalate and document.

---

## Step 0: Client Onboarding Questions

Before computing any income tax figure, you MUST know:

1. **NIF (Número de Identificação Fiscal)** [T1] -- mandatory for all filings. If missing, STOP.
2. **Filing status** [T1] -- single (solteiro/a), married filing jointly (casado, tributação conjunta), or married filing separately (tributação separada). Determines whether income is split (quociente conjugal).
3. **Tax regime** [T1] -- regime simplificado or contabilidade organizada. Determines how net income is computed.
4. **Activity type** [T1] -- services (prestação de serviços) or sale of goods (venda de mercadorias). Determines simplificado coefficient.
5. **CIRS Art. 151 activity** [T1] -- whether the activity is listed in the Art. 151 professions table. Affects withholding rate.
6. **Gross income (Categoria B)** [T1] -- total invoiced in the calendar year via recibos verdes / e-fatura
7. **Business expenses** [T1/T2] -- relevant only under contabilidade organizada
8. **Social security contributions (Segurança Social) paid** [T1] -- amount paid during the year
9. **Other income** [T1] -- employment (Cat. A), rental (Cat. F), capital (Cat. E), pensions (Cat. H)
10. **Dependants** [T1] -- number and ages of dependants
11. **IRS Jovem eligibility** [T1] -- age, first year of employment/self-employment, degree completion date

**If NIF is unknown or filing status is unknown, STOP. Both are mandatory.**

---

## Step 1: Determine Tax Regime for Categoria B [T1]

**Legislation:** CIRS Arts. 28, 31

### Regime Simplificado [T1]

Applies automatically when:
- Annual gross Categoria B income does not exceed EUR 200,000
- Taxpayer has not opted for contabilidade organizada

Under the simplified regime, taxable income is determined by applying coefficients to gross income:

| Type of Income | Coefficient (taxable %) | Deemed Expense % |
|---------------|------------------------|-------------------|
| Services (prestação de serviços) -- Art. 151 activities | 75% | 25% automatic deduction |
| Sale of goods (venda de mercadorias) | 15% | 85% automatic deduction |
| Income from intellectual property | 95% | 5% automatic deduction |
| Accommodation/food services (alojamento local) | 35% | 65% automatic deduction |
| Subsidies for acquisition of assets | 30% | 70% automatic deduction |
| Other Categoria B income | 95% | 5% automatic deduction |

**The 25% deemed expense for services is NOT free.** To benefit from the full 25% automatic deduction, the taxpayer must prove expenses and charges equal to at least 15% of gross income. If actual documented expenses (in e-fatura) are less than 15%, the taxable income increases accordingly. The remaining 10% is unconditionally deemed as expense.

### Contabilidade Organizada [T2]

- Taxpayer opts for (or is required to use) organised accounting
- Net income = actual revenue minus actual documented expenses
- Requires a Contabilista Certificado (CC) to maintain the accounts
- More beneficial when actual expenses exceed the deemed expense percentage under simplificado

### Regime Choice [T2]

- The choice between simplificado and contabilidade organizada is made at the start of the activity or by 31 March of the fiscal year (via Portal das Finanças)
- Once chosen, it applies for at least 3 years
- [T2] Flag for reviewer: always compare both regimes before recommending

---

## Step 2: Progressive IRS Brackets (Art. 68 CIRS) [T1]

**Legislation:** CIRS Art. 68, as amended by Lei 55-A/2025 (OE2025)

### Tax Year 2025 Brackets

| Bracket | Taxable Income (EUR) | Normal Rate | Average Rate |
|---------|---------------------|-------------|--------------|
| 1st | Up to 8,059 | 13.00% | 13.000% |
| 2nd | 8,059 to 12,160 | 16.50% | 14.180% |
| 3rd | 12,160 to 17,233 | 22.00% | 16.482% |
| 4th | 17,233 to 22,306 | 25.00% | 18.419% |
| 5th | 22,306 to 28,400 | 32.00% | 21.334% |
| 6th | 28,400 to 41,629 | 35.50% | 25.835% |
| 7th | 41,629 to 44,987 | 43.50% | 27.154% |
| 8th | 44,987 to 83,696 | 45.00% | 35.408% |
| 9th | Above 83,696 | 48.00% | -- |

**Note:** The 2025 brackets were updated by 4.6% compared to 2024. Tax rates remained unchanged. Brackets are updated annually in line with the State Budget (Orçamento do Estado).

### How Portuguese IRS Brackets Work [T1]

Portuguese IRS uses a **split-rate system**, not a simple marginal system:

1. Determine the highest bracket that the taxable income fully covers
2. That portion is taxed at the **average rate** of that bracket
3. The excess above that bracket is taxed at the **normal rate** of the next bracket

**Example:** Taxable income of EUR 15,000.
- First EUR 12,160 taxed at the average rate of the 2nd bracket (14.180%) = EUR 1,724.29
- Remaining EUR 2,840 taxed at the normal rate of the 3rd bracket (22.00%) = EUR 624.80
- Total IRS = EUR 2,349.09

### Quociente Conjugal (Married Filing Jointly) [T1]

When married taxpayers file jointly (tributação conjunta):
1. Sum both spouses' total income
2. Divide by 2 (quociente familiar = 2)
3. Apply the bracket table to the halved amount
4. Multiply the resulting tax by 2

This is always more favourable when spouses have significantly different incomes.

---

## Step 3: Adicional de Solidariedade (Solidarity Surcharge) [T1]

**Legislation:** CIRS Art. 68-A

| Taxable Income (EUR) | Surcharge Rate |
|---------------------|----------------|
| Up to 80,000 | 0% |
| 80,001 to 250,000 | 2.5% on the portion above 80,000 |
| Above 250,000 | 5.0% on the portion above 250,000 (plus 2.5% on 80,001-250,000) |

The adicional de solidariedade is computed on the same taxable income as the main IRS and is added to the total tax liability.

---

## Step 4: Retenção na Fonte -- Withholding Tax [T1]

**Legislation:** CIRS Art. 101

### Withholding Rates for Categoria B Income (2025)

| Activity Type | Withholding Rate |
|--------------|-----------------|
| Professional activities listed in Art. 151 CIRS | 23% |
| Other Categoria B services (not in Art. 151) | 11.5% |
| Isolated acts (actos isolados) | 11.5% |
| Intellectual property | 16.5% |

### When Withholding Applies [T1]

Withholding is required when:
- The payer is an entity with organised accounting (empresa ou entidade com contabilidade organizada)
- The payee issues a recibo verde (green receipt) via the Portal das Finanças

Withholding does NOT apply when:
- The client is an individual (pessoa singular) without organised accounting
- The taxpayer is exempt from withholding (annual income below EUR 14,500 in the prior year -- dispensed from retenção)

### Exemption from Withholding [T1]

Taxpayers who earned less than EUR 14,500 in Categoria B income in the previous year may request dispensation from retenção na fonte via the Portal das Finanças. This does not eliminate the tax obligation -- it only defers payment to the annual settlement.

---

## Step 5: Social Security Contributions (Segurança Social) [T1]

**Legislation:** Código dos Regimes Contributivos (CRC), Art. 163 et seq.

### Contribution Rates for Trabalhadores Independentes [T1]

| Contributor Type | Rate | Base |
|-----------------|------|------|
| Self-employed (standard) | 21.4% | On 70% of average quarterly income (rendimento relevante) |
| Self-employed (first year) | Exempt | First 12 months of activity |
| Self-employed (reduced, on request) | Various reduced rates | Available under specific conditions |

### Deductibility [T1]

Social security contributions paid during the year are deductible from Categoria B income under the regime simplificado (they count towards the 15% expense threshold) and are deductible as an expense under contabilidade organizada.

In the annual IRS computation, SSC is deducted from taxable income (specific deduction under Art. 26 CIRS).

---

## Step 6: Personal Deductions (Deduções à Coleta) [T1]

**Legislation:** CIRS Arts. 78-78-E

Portuguese personal deductions work as **tax credits** (deducted from the tax, not from income):

| Deduction | Amount / Rate | Cap |
|-----------|--------------|-----|
| General family deduction (dedução pessoal) | EUR 600 per taxpayer + EUR 300 per dependant (under 3: EUR 450) | Fixed amounts |
| Health expenses (saúde) | 15% of expenses | EUR 1,000 per household |
| Education expenses (educação) | 30% of expenses | EUR 800 per household |
| Housing expenses (habitação) | 15% of rent or mortgage interest | EUR 502 (rent) / EUR 296 (mortgage) |
| Retirement home expenses (lares) | 25% of expenses | EUR 403.75 |
| Alimony (pensão de alimentos) | 20% of amounts paid | No cap (court-ordered) |
| VAT invoices (exigência de fatura) | 15% of IVA on qualifying sectors | EUR 250 per household |
| General expenses (despesas gerais familiares) | 35% of general household expenses | EUR 250 per taxpayer |

### Important Rule for Self-Employed [T1]

Under the regime simplificado, the general expenses deduction (despesas gerais familiares) is reduced for Categoria B taxpayers. Only 25% of their general expenses qualify (vs 35% for employees), reflecting that some expenses are already deemed deducted through the simplified coefficient.

---

## Step 7: IRS Jovem -- Young Taxpayer Relief [T1]

**Legislation:** CIRS Art. 12-B (as amended by OE2025)

### Eligibility [T1]

| Condition | Requirement |
|-----------|-------------|
| Age | Up to 35 years old (inclusive) |
| Education | Completed at least ISCED Level 4 (secondary education or higher) |
| Not claimed as dependant | Must not be a dependant on another taxpayer's return |
| First years of activity | Applies to the first 10 years of earning income after completing studies |

### Exemption Levels (OE2025 onwards) [T1]

| Year of Activity | Exemption % of Categoria B Income |
|-----------------|------------------------------------|
| 1st year | 100% (up to 55 x IAS) |
| 2nd year | 75% (up to 55 x IAS) |
| 3rd and 4th years | 50% (up to 55 x IAS) |
| 5th to 10th years | 25% (up to 55 x IAS) |

**IAS (Indexante dos Apoios Sociais) 2025:** EUR 522.50/month = EUR 6,270/year. Cap = 55 x IAS = EUR 28,737.50/year of exempt income.

**[T2] Flag for reviewer:** Confirm exact year of first income and degree completion date to determine which year of the exemption applies.

---

## Step 8: Annual Return Computation [T1]

**Legislation:** CIRS Arts. 22, 28, 31, 65, 68, 78

### Computation Walkthrough (Regime Simplificado, Single Taxpayer)

```
1. Gross Categoria B income (services)                        = A
2. Apply simplificado coefficient (75% for services)          = B = A x 0.75
   (Verify 15% expense threshold is met -- see Step 1)
3. Less: Social security contributions (specific deduction)   = C
4. Add: Other category income (Cat. A, F, E, H if any)       = D
5. Total taxable income (rendimento coletável)                = E = B - C + D
6. Apply Art. 68 bracket table to E                           = F (coleta)
7. Add: Adicional de solidariedade (if E > EUR 80,000)        = G
8. Gross tax                                                   = H = F + G
9. Less: Personal deductions (deduções à coleta, Step 6)      = I
10. Less: IRS Jovem exemption (if eligible, Step 7)           = J
11. Net tax liability                                          = K = H - I - J
12. Less: Retenção na fonte (withholding paid during year)    = L
13. Less: Pagamentos por conta (advance payments, if any)     = M
14. IRS due or refund                                          = N = K - L - M
```

**If N > 0:** tax balance due, payable with the return.
**If N < 0:** refund (reembolso), paid by AT typically within months of filing.

### Pagamentos por Conta (Advance Payments) [T1]

Self-employed taxpayers with Categoria B income may be required to make three advance payments (pagamentos por conta) during the year:

| Instalment | Deadline |
|-----------|----------|
| 1st | 20 July |
| 2nd | 20 September |
| 3rd | 20 December |

Each payment = (prior year IRS attributable to Cat. B - withholdings) / 3 x 76.5% (for simplificado) or 80% (for contabilidade organizada). These are credited against the annual tax.

---

## Step 9: Filing Deadlines [T1]

**Legislation:** CIRS Art. 60

| Event | Deadline |
|-------|----------|
| IRS Modelo 3 (tax year 2025) submission period | 1 April to 30 June 2026 |
| IRS Automático (pre-filled return, if eligible) | Same period |
| Pagamentos por conta (1st / 2nd / 3rd) | 20 July / 20 September / 20 December |
| Retenção na fonte (monthly) | By the 20th of the following month |

### Late Filing Penalties [T1]

| Offence | Penalty |
|---------|---------|
| Late filing (up to 30 days) | EUR 25 to EUR 75 (if regularised voluntarily) |
| Late filing (over 30 days) | EUR 150 to EUR 3,750 |
| Omission of income | EUR 375 to EUR 22,500 |
| Tax fraud | Criminal penalties under RGIT (Regime Geral das Infrações Tributárias) |
| Late payment interest (juros de mora) | 4% per year (updated periodically) |

---

## Step 10: Edge Case Registry

### EC1 -- 15% expense threshold not met under simplificado [T1]
**Situation:** Freelance consultant earns EUR 40,000. Documented expenses in e-fatura total only EUR 3,000 (7.5% of income, below the 15% threshold of EUR 6,000).
**Resolution:** The shortfall is EUR 3,000 (EUR 6,000 required - EUR 3,000 actual). This EUR 3,000 is added back to the taxable income. Taxable = EUR 40,000 x 75% + EUR 3,000 = EUR 33,000 instead of the standard EUR 30,000. The taxpayer should increase documented expenses (e.g., SSC, professional insurance, training).

### EC2 -- Mixed activity: services and goods [T1]
**Situation:** Client provides IT consulting (services) and also sells computer hardware (goods). Services income EUR 50,000, goods income EUR 20,000.
**Resolution:** Apply each coefficient separately. Services: EUR 50,000 x 75% = EUR 37,500. Goods: EUR 20,000 x 15% = EUR 3,000. Total taxable Categoria B = EUR 40,500. Do NOT apply a blended rate.

### EC3 -- First-year SSC exemption [T1]
**Situation:** Client opened activity as trabalhador independente in March 2025. No SSC paid in 2025.
**Resolution:** Correct. First 12 months of activity are exempt from SSC. No SSC deduction for 2025. The exemption ends in March 2026, after which quarterly SSC obligations begin.

### EC4 -- Dispensation from withholding misunderstood as tax exemption [T1]
**Situation:** Client earns EUR 12,000 in Categoria B and was dispensed from retenção na fonte (prior year income < EUR 14,500). Client believes no tax is due.
**Resolution:** Dispensation from withholding is NOT a tax exemption. The full income is taxable on the annual return. The client will owe the full IRS amount at filing time, with no withholding credits to offset. Advise the client to set aside funds for the annual tax payment.

### EC5 -- Married couple, one self-employed, filing jointly vs separately [T2]
**Situation:** Spouse A earns EUR 60,000 (Cat. A employment). Spouse B earns EUR 15,000 (Cat. B self-employment). Should they file jointly?
**Resolution:** [T2] Compare both options. Joint: combined EUR 75,000 / 2 = EUR 37,500 per quotient, taxed at 6th bracket rates. Separate: A at EUR 60,000 (8th bracket), B at EUR 11,250 (75% of EUR 15,000, 2nd bracket). The optimal choice depends on the full deduction profile. Flag for reviewer to compute both scenarios.

### EC6 -- Contabilidade organizada: personal expense mixed in [T1]
**Situation:** Under contabilidade organizada, client includes personal car insurance (EUR 800) as a business expense.
**Resolution:** NOT deductible unless apportioned for business use. Under contabilidade organizada, only expenses wholly and exclusively incurred for the business are deductible. Personal expenses must be excluded or apportioned. [T2] Flag if mixed-use apportionment is needed.

### EC7 -- Adicional de solidariedade triggered [T1]
**Situation:** Single freelancer with taxable income of EUR 120,000.
**Resolution:** Standard IRS on EUR 120,000 per bracket table. Adicional de solidariedade: 2.5% x (EUR 120,000 - EUR 80,000) = 2.5% x EUR 40,000 = EUR 1,000. This EUR 1,000 is added to the IRS liability.

### EC8 -- IRS Jovem eligibility edge case [T2]
**Situation:** Client is 34 years old, completed a master's degree in 2020, started freelancing in 2021. Filing for 2025 (5th year of activity).
**Resolution:** 5th year of activity qualifies for 25% exemption under IRS Jovem (OE2025 rules). Exempt income capped at 55 x IAS = EUR 28,737.50. Client is under 35, so age criterion is met. [T2] Flag for reviewer to confirm year count from first income after degree completion.

### EC9 -- NHR (Non-Habitual Resident) [T3]
**Situation:** Client moved to Portugal in 2023 and has NHR status. Asks about flat 20% rate on Categoria B income.
**Resolution:** [T3] ESCALATE. The NHR regime was significantly changed by OE2024 and OE2025. Transitional rules apply for existing NHR holders. New applications under the original NHR were closed (replaced by tax incentive for scientific research and innovation). Refer to a Contabilista Certificado or tax lawyer with NHR expertise.

### EC10 -- Crypto income [T3]
**Situation:** Freelancer also earned EUR 5,000 from cryptocurrency trading.
**Resolution:** [T3] ESCALATE. Crypto taxation in Portugal changed significantly from 2023 onwards (Lei 24-D/2022). Short-term crypto gains (held < 365 days) are taxable at 28% autonomous rate. Long-term may be exempt. Classification as Categoria B income (if trading is the habitual activity) vs Categoria G (capital gains) requires specialist analysis. Refer to a tax specialist.

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
Action Required: Licensed Contabilista Certificado must confirm before filing.
```

When Claude identifies a [T3] situation:

```
ESCALATION REQUIRED
Tier: T3
Client: [name]
Situation: [description]
Issue: [outside skill scope]
Action Required: Do not advise. Refer to licensed Contabilista Certificado. Document gap.
```

---

## Step 12: Test Suite

### Test 1 -- Standard freelancer, regime simplificado, services
**Input:** Single, Art. 151 activity, gross Categoria B income EUR 40,000, SSC paid EUR 4,500, documented expenses EUR 7,000 (above 15% threshold of EUR 6,000), retenção na fonte paid EUR 9,200 (23% of EUR 40,000). No other income, no dependants.
**Expected output:** Taxable Cat. B = EUR 40,000 x 75% = EUR 30,000. Less SSC EUR 4,500. Rendimento coletável = EUR 25,500. IRS: first EUR 22,306 at average rate 21.334% = EUR 4,759.45, excess EUR 3,194 at 32.00% = EUR 1,022.08. Total coleta = EUR 5,781.53. Less personal deductions (general EUR 600, general expenses EUR 250, health/education as applicable). Net tax approx EUR 4,931. Less retenção EUR 9,200. Refund approx EUR 4,269.

### Test 2 -- 15% expense threshold shortfall
**Input:** Freelancer, services income EUR 30,000, documented expenses only EUR 2,000 (6.67%, below 15% = EUR 4,500).
**Expected output:** Shortfall = EUR 4,500 - EUR 2,000 = EUR 2,500. Taxable = EUR 30,000 x 75% + EUR 2,500 = EUR 25,000. NOT the standard EUR 22,500.

### Test 3 -- Mixed services and goods income
**Input:** IT consultant earns EUR 45,000 in consulting fees and EUR 10,000 from hardware sales.
**Expected output:** Services: EUR 45,000 x 75% = EUR 33,750. Goods: EUR 10,000 x 15% = EUR 1,500. Total Cat. B taxable = EUR 35,250.

### Test 4 -- Adicional de solidariedade
**Input:** Single, taxable income EUR 300,000.
**Expected output:** Standard IRS on EUR 300,000 per brackets. Adicional: 2.5% x (EUR 250,000 - EUR 80,000) = EUR 4,250, plus 5% x (EUR 300,000 - EUR 250,000) = EUR 2,500. Total adicional = EUR 6,750.

### Test 5 -- IRS Jovem, 2nd year
**Input:** Age 28, master's degree completed 2023, first professional income 2024. Filing for 2025 (2nd year). Cat. B income EUR 35,000.
**Expected output:** IRS Jovem 2nd year: 75% exemption. Exempt income = 75% x EUR 35,000 = EUR 26,250 (under cap of EUR 28,737.50). Taxable Cat. B = EUR 35,000 - EUR 26,250 = EUR 8,750 (before simplificado coefficient is applied -- note: the exemption applies to the rendimento bruto or líquido depending on AT guidance). [T2] Flag for reviewer to confirm how IRS Jovem interacts with the simplificado coefficient.

### Test 6 -- Withholding exemption misunderstood
**Input:** Freelancer earned EUR 13,000 in 2024 (prior year < EUR 14,500). Dispensed from retenção in 2025. Earns EUR 20,000 in 2025.
**Expected output:** No retenção was withheld during 2025. Taxable Cat. B = EUR 20,000 x 75% = EUR 15,000 (assuming expenses threshold met). Full IRS liability is due at filing. No withholding credits to offset. Client owes the full computed tax amount.

---

## PROHIBITIONS

- NEVER apply a single blended coefficient when a client has both services and goods income -- each type gets its own coefficient
- NEVER treat dispensation from retenção na fonte as a tax exemption
- NEVER ignore the 15% expense threshold under regime simplificado
- NEVER advise on NHR regime without escalating to a specialist
- NEVER advise on crypto taxation without escalating to a specialist
- NEVER allow personal expenses under contabilidade organizada without proper business apportionment
- NEVER compute IRS without knowing the filing status (single/married/joint/separate)
- NEVER ignore the adicional de solidariedade for incomes above EUR 80,000
- NEVER apply IRS Jovem without verifying age, degree, and year of first income
- NEVER present tax calculations as definitive -- always label as estimated and direct client to a licensed Contabilista Certificado for confirmation

---

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a Contabilista Certificado or equivalent licensed practitioner in Portugal) before filing or acting upon.

If you would like a licensed accountant to review your return, visit [openaccountants.com](https://openaccountants.com) and log in to request a professional review.
