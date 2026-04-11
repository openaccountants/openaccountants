---
name: br-income-tax
description: >
  Use this skill whenever asked about Brazilian individual income tax for self-employed individuals (autônomos / profissionais liberais). Trigger on phrases like "how much tax do I pay in Brazil", "DIRPF", "IRPF", "Carnê-Leão", "livro caixa", "imposto de renda", "CPF", "income tax return Brazil", "deductible expenses Brazil", "self-employed tax Brazil", or any question about filing or computing income tax for a self-employed or freelance client in Brazil. This skill covers the DIRPF annual return, Carnê-Leão monthly estimated payments, progressive tax brackets, livro caixa (cash book), allowable deductions, simplified deduction option, mandatory filing thresholds, INSS contributions, and penalties. ALWAYS read this skill before touching any Brazilian income tax work.
version: 1.0
jurisdiction: BR
tax_year: 2025
category: international
depends_on:
  - income-tax-workflow-base
---

# Brazil Income Tax (IRPF) -- Self-Employed Skill

---

## Skill Metadata

| Field | Value |
|-------|-------|
| Jurisdiction | Brazil |
| Jurisdiction Code | BR |
| Primary Legislation | Regulamento do Imposto de Renda (RIR/2018, Decreto 9.580/2018) |
| Supporting Legislation | Lei 7.713/1988 (progressive table); Lei 8.134/1990 (Carnê-Leão); IN RFB 1.500/2014 (withholding); Medida Provisória 1.294/2025 (updated brackets from May 2025); Lei 15.270/2025 (2026 bracket update) |
| Tax Authority | Receita Federal do Brasil (RFB) |
| Filing Portal | Programa IRPF (desktop) / e-CAC portal |
| Contributor | Open Accountants Community |
| Validated By | Pending -- requires sign-off by a Brazilian CRC-registered accountant (Contador) |
| Validation Date | Pending |
| Skill Version | 1.0 |
| Confidence Coverage | Tier 1: rate table application, filing thresholds, Carnê-Leão obligation, deduction caps, simplified deduction, deadline. Tier 2: livro caixa expense classification, home office apportionment, mixed-use vehicle, INSS contribution base for autônomos. Tier 3: foreign income, capital gains, exit tax, MEI transition. |

---

## Confidence Tier Definitions

- **[T1] Tier 1 -- Deterministic.** Apply exactly as written. No reviewer judgement required.
- **[T2] Tier 2 -- Reviewer Judgement Required.** Claude flags and presents options. Licensed Contador must confirm.
- **[T3] Tier 3 -- Out of Scope / Escalate.** Do not guess. Escalate and document.

---

## Step 0: Client Onboarding Questions

Before computing any income tax figure, you MUST know:

1. **CPF number** [T1] -- Cadastro de Pessoas Físicas. Required for all filings. If missing, STOP.
2. **Filing status** [T1] -- individual or joint declaration with spouse (declaração em conjunto)
3. **Employment status** [T1] -- fully self-employed (autônomo), liberal professional, or employed with side income
4. **Gross self-employment income** [T1] -- total received in the calendar year from all sources
5. **Source of payments** [T1] -- from legal entities (pessoa jurídica, PJ) or from individuals (pessoa física, PF) or from abroad. Determines Carnê-Leão obligation.
6. **Business expenses** [T1/T2] -- nature and amount of each expense recorded in livro caixa
7. **INSS contributions paid** [T1] -- amount of social security contributions paid during the year
8. **Number of dependants** [T1] -- for dependant deductions
9. **Education and medical expenses** [T1] -- amounts paid, with receipts
10. **Declaration model preference** [T1] -- complete (deduções legais) or simplified (desconto simplificado)

**If CPF is unknown, STOP. CPF is mandatory for any Brazilian tax computation.**

---

## Step 1: Determine If Filing Is Mandatory [T1]

**Legislation:** IN RFB (Instrução Normativa) -- updated annually

A pessoa física must file the DIRPF 2026 (tax year 2025) if ANY of the following apply:

| Condition | Threshold (2025) |
|-----------|-----------------|
| Taxable income (rendimentos tributáveis) | Above R$ 33,888.00 |
| Exempt or non-taxable income | Above R$ 200,000.00 |
| Capital gains on asset disposal | Any amount |
| Rural gross revenue | Above R$ 169,440.00 |
| Assets and rights on 31 Dec | Above R$ 800,000.00 |
| New resident of Brazil | In any month of 2025 |
| Self-employed with Carnê-Leão payments | Filing is mandatory to offset Carnê-Leão paid |

**Self-employed individuals who paid Carnê-Leão during the year should always file to credit those payments against the annual liability.**

---

## Step 2: Progressive Tax Table [T1]

**Legislation:** Medida Provisória 1.294/2025; RIR/2018 Art. 677

### Annual Table (Tax Year 2025 -- for DIRPF filed in 2026)

| Taxable Income (R$) | Rate | Deduction (Parcela a Deduzir) |
|---------------------|------|-------------------------------|
| Up to 28,467.20 | 0% | -- |
| 28,467.21 to 33,919.80 | 7.5% | R$ 2,135.04 |
| 33,919.81 to 45,012.60 | 15.0% | R$ 4,679.03 |
| 45,012.61 to 55,976.16 | 22.5% | R$ 8,054.97 |
| Above 55,976.16 | 27.5% | R$ 10,853.78 |

### Monthly Table (May -- December 2025)

| Taxable Income (R$) | Rate | Deduction (Parcela a Deduzir) |
|---------------------|------|-------------------------------|
| Up to 2,428.80 | 0% | -- |
| 2,428.81 to 2,826.65 | 7.5% | R$ 182.16 |
| 2,826.66 to 3,751.05 | 15.0% | R$ 394.16 |
| 3,751.06 to 4,664.68 | 22.5% | R$ 675.49 |
| Above 4,664.68 | 27.5% | R$ 908.73 |

### Monthly Table (January -- April 2025)

| Taxable Income (R$) | Rate | Deduction (Parcela a Deduzir) |
|---------------------|------|-------------------------------|
| Up to 2,259.20 | 0% | -- |
| 2,259.21 to 2,826.65 | 7.5% | R$ 169.44 |
| 2,826.66 to 3,751.05 | 15.0% | R$ 381.44 |
| 3,751.06 to 4,664.68 | 22.5% | R$ 662.77 |
| Above 4,664.68 | 27.5% | R$ 896.00 |

**Note:** The monthly table changed mid-year in 2025 (MP 1.294/2025 effective May 2025). When computing the annual tax, use the annual table above. The monthly tables are relevant for Carnê-Leão and withholding calculations.

**NEVER compute the annual tax by summing 12 monthly calculations -- always use the annual table for the DIRPF.**

---

## Step 3: Carnê-Leão -- Monthly Estimated Tax [T1]

**Legislation:** RIR/2018, Arts. 118-121; Lei 8.134/1990

### When Carnê-Leão Applies [T1]

Carnê-Leão is mandatory when a self-employed individual receives income from:
- **Individuals (pessoa física)** -- e.g., a freelance designer paid directly by a client who is a natural person
- **Foreign sources** -- income from abroad

Carnê-Leão does NOT apply when income is received from a legal entity (PJ), because PJ already withholds IRRF (Imposto de Renda Retido na Fonte) at source.

### How It Works [T1]

1. Each month, compute gross income received from PF/foreign sources
2. Subtract allowable livro caixa deductions (Step 4)
3. Subtract INSS contribution paid in the month
4. Subtract dependant deduction (R$ 189.59/month per dependant)
5. Apply the monthly progressive table to the net taxable income
6. Pay the resulting tax via DARF code 0190 by the last business day of the following month

### Carnê-Leão Web [T1]

Since 2021, Carnê-Leão is filed monthly via the e-CAC portal (Carnê-Leão Web). Data entered monthly is automatically imported into the DIRPF annual program.

---

## Step 4: Livro Caixa -- Cash Book Deductions [T1/T2]

**Legislation:** RIR/2018, Art. 104; Lei 8.134/1990, Art. 6

### The Rule [T1]
Self-employed individuals (autônomos) who receive income from individuals or from abroad may deduct business expenses recorded in the livro caixa. The livro caixa is the only mechanism for deducting business expenses against self-employment income in Brazil.

### Deductible Expenses (Livro Caixa)

| Expense | Tier | Treatment |
|---------|------|-----------|
| Office rent (dedicated business premises) | T1 | Fully deductible |
| Employee wages and social charges (INSS, FGTS) | T1 | Fully deductible |
| Utility bills (business premises) | T1 | Fully deductible |
| Office supplies and materials | T1 | Fully deductible |
| Professional dues (CRM, OAB, CRC, CREA, etc.) | T1 | Fully deductible |
| ISS (Imposto Sobre Serviços) paid | T1 | Fully deductible |
| Accounting and legal fees | T1 | Fully deductible |
| Software subscriptions (business use) | T1 | Fully deductible |
| Marketing and advertising | T1 | Fully deductible |
| Business travel (documented) | T1 | Fully deductible |
| Home office expenses | T2 | Proportional -- dedicated room only. Flag for reviewer |
| Vehicle expenses (fuel, maintenance) | T2 | Business portion only -- mileage log required. Flag for reviewer |
| Phone / internet | T2 | Business portion only -- apportionment required |

### NOT Deductible in Livro Caixa [T1]

| Expense | Reason |
|---------|--------|
| Personal living expenses | Not business-related |
| Clothing (unless uniforms) | Personal |
| Entertainment and meals | Not allowed under livro caixa rules |
| Fines and penalties | Public policy |
| IRPF itself | Tax on income cannot reduce income |
| Depreciation of assets | Not permitted in livro caixa for autônomos |
| Capital expenditure | Not deductible as expense |

### Critical Rule [T1]

**Livro caixa deductions CANNOT create a loss.** The maximum deduction in any month is limited to the gross income of that month. Any excess cannot be carried forward.

---

## Step 5: Deductions on the Annual Return [T1]

**Legislation:** RIR/2018, Arts. 71-82

### Option A: Complete Declaration (Deduções Legais) [T1]

| Deduction | Limit | Notes |
|-----------|-------|-------|
| INSS (social security contributions) | Actual amount paid | No cap |
| Dependants | R$ 2,275.08 per dependant/year | Fixed amount |
| Education expenses | R$ 3,561.50 per person/year | Capped -- includes taxpayer, dependants, and alimentandos |
| Medical expenses | No cap | Must have receipts (recibos/notas fiscais) |
| Private pension (PGBL) | Up to 12% of taxable income | Only PGBL, not VGBL |
| Alimony (pensão alimentícia) | Actual amount paid | Must be court-ordered or by formal agreement |
| Livro caixa deductions | As per Step 4 | Already deducted from self-employment income |

### Option B: Simplified Declaration (Desconto Simplificado) [T1]

- Automatic deduction of 20% of taxable income
- Capped at R$ 16,754.34
- Replaces ALL itemised deductions (dependants, education, medical, etc.)
- Livro caixa deductions still apply to self-employment income before the simplified deduction is computed
- Choose simplified only if 20% (up to cap) exceeds total itemised deductions

**The DIRPF program automatically calculates both options and shows which is more favourable. Always verify which model produces lower tax.**

---

## Step 6: INSS for Self-Employed [T1/T2]

**Legislation:** Lei 8.212/1991; IN RFB 971/2009

### Contribution Rates for Autônomos [T1]

| Contributor Type | Rate | Base |
|-----------------|------|------|
| Individual contributor (contribuinte individual) | 20% | On income received, between minimum wage and INSS ceiling |
| Simplified plan (plano simplificado) | 11% | On minimum wage only -- reduced benefits |
| MEI (Microempreendedor Individual) | 5% | On minimum wage -- out of scope for this skill |

### INSS Ceiling (Teto) 2025 [T1]

The INSS contribution ceiling for 2025 is R$ 8,157.41/month (subject to annual update). Contributions above this ceiling are not required and not deductible.

### Deductibility [T1]

INSS contributions actually paid during the calendar year are deductible from taxable income on the DIRPF. They are deducted before applying the progressive table.

---

## Step 7: Filing Deadline and Penalties [T1]

**Legislation:** IN RFB (annual instruction)

### Deadline [T1]

| Event | Deadline |
|-------|----------|
| DIRPF 2026 (tax year 2025) submission period | 17 March to 30 May 2026 |
| Carnê-Leão monthly payment | Last business day of the month following receipt |
| IRPF balance due (imposto a pagar) | First instalment or full payment by 30 May 2026 |

### Instalments [T1]

- Balance due may be split into up to 8 monthly instalments
- Minimum instalment: R$ 50.00
- If total tax due is under R$ 100.00, pay in full (no instalments)
- Instalments after the first are adjusted by SELIC rate

### Late Filing Penalty [T1]

| Offence | Penalty |
|---------|---------|
| Late filing of DIRPF | 1% per month on tax due, minimum R$ 165.74, maximum 20% of tax due |
| Late payment (Carnê-Leão or DIRPF balance) | 0.33% per day up to 20%, plus SELIC interest |
| Incorrect declaration (omission of income) | 75% of the difference in tax (multa de ofício), reducible to 37.5% if corrected voluntarily |
| Fraud | 150% of the difference in tax |

---

## Step 8: Computation Walkthrough [T1]

### Annual DIRPF Computation (Complete Declaration)

```
1. Gross self-employment income (from PJ + PF + foreign)      = A
2. Less: Livro caixa deductions (cannot exceed A)              = B
3. Net self-employment income                                  = C = A - B
4. Add: Other taxable income (employment, rental, etc.)        = D
5. Total taxable income before deductions                      = E = C + D
6. Less: INSS contributions paid                               = F
7. Less: Dependant deductions (R$ 2,275.08 x number)           = G
8. Less: Education expenses (up to R$ 3,561.50 per person)     = H
9. Less: Medical expenses (actual, no cap)                     = I
10. Less: Private pension PGBL (up to 12% of E)                = J
11. Less: Alimony paid (court-ordered)                         = K
12. Taxable income (base de cálculo)                           = L = E - F - G - H - I - J - K
13. Apply annual progressive table to L                        = M (gross tax)
14. Less: IRRF withheld at source by PJ payers                 = N
15. Less: Carnê-Leão paid during the year                      = O
16. Tax due or refund                                          = P = M - N - O
```

**If P > 0:** tax balance due, payable from first instalment by 30 May.
**If P < 0:** refund (restituição), paid in batches by Receita Federal.

---

## Step 9: Interaction with Other Taxes [T1]

| Tax | Interaction with IRPF |
|-----|----------------------|
| INSS (social security) | Deductible from taxable income |
| ISS (municipal services tax) | Deductible in livro caixa as business expense |
| IRRF (withholding by PJ) | Credited against annual IRPF liability |
| Carnê-Leão (monthly IRPF) | Credited against annual IRPF liability |
| CSLL, PIS, COFINS | Applicable to PJ only -- not relevant for autônomo PF |

---

## Step 10: Edge Case Registry

### EC1 -- Livro caixa deduction exceeds monthly income [T1]
**Situation:** Autônomo earns R$ 3,000 in March but has R$ 4,500 in livro caixa expenses.
**Resolution:** Maximum deduction for March is R$ 3,000. Net income = R$ 0. The excess R$ 1,500 is lost -- livro caixa losses CANNOT be carried forward to the next month or to the annual return. This is a hard rule.

### EC2 -- Income from PJ and PF in same month [T1]
**Situation:** Freelancer receives R$ 5,000 from a company (PJ) with IRRF withheld, and R$ 3,000 from an individual client (PF) with no withholding.
**Resolution:** Carnê-Leão applies only to the R$ 3,000 from PF. The R$ 5,000 from PJ already had IRRF withheld at source. Both amounts appear on the DIRPF. The IRRF and Carnê-Leão paid are both credited in the annual computation.

### EC3 -- Simplified vs complete declaration choice [T1]
**Situation:** Client has R$ 80,000 taxable income, R$ 8,000 INSS, R$ 2,275 dependant, R$ 3,561 education, and R$ 15,000 medical expenses.
**Resolution:** Complete deductions = R$ 28,836. Simplified = 20% x R$ 80,000 = R$ 16,000 (under cap of R$ 16,754.34). Complete is more favourable. Always compute both and choose the lower tax.

### EC4 -- Medical expense without receipt [T1]
**Situation:** Client claims R$ 2,000 in dental expenses with no nota fiscal or recibo.
**Resolution:** NOT deductible. Medical expenses require documentary proof (nota fiscal, recibo with CPF of provider, or health insurance statement). Undocumented medical expenses must be excluded.

### EC5 -- Dependant claimed by both spouses [T1]
**Situation:** Married couple files separate returns. Both claim the same child as dependant.
**Resolution:** NOT allowed. A dependant may be claimed by only one taxpayer. If both claim the same child, the Receita Federal will reject one of the declarations. Confirm which spouse claims each dependant before filing.

### EC6 -- INSS paid above ceiling [T2]
**Situation:** Autônomo earns R$ 15,000/month and contributes 20% = R$ 3,000/month INSS.
**Resolution:** Maximum INSS contribution base is R$ 8,157.41/month. Maximum monthly contribution = R$ 1,631.48. Any INSS paid above the ceiling is not required and may be recoverable but is not additionally deductible. [T2] Flag for reviewer to verify whether excess was paid and advise on recovery.

### EC7 -- Education expense above cap [T1]
**Situation:** Client paid R$ 8,000 in university tuition for one child.
**Resolution:** Deductible amount is capped at R$ 3,561.50 per person. Only R$ 3,561.50 may be deducted. The remaining R$ 4,438.50 is not deductible.

### EC8 -- Mid-year change in monthly table [T1]
**Situation:** Client's Carnê-Leão for January-April 2025 uses the old table (exempt up to R$ 2,259.20). From May 2025, the new table applies (exempt up to R$ 2,428.80).
**Resolution:** Apply the correct monthly table for each month. January-April uses the old table. May-December uses the new table. The annual DIRPF uses the single annual table for the final computation, and Carnê-Leão payments are credited regardless of which monthly table was used.

### EC9 -- Foreign income [T3]
**Situation:** Brazilian tax resident receives freelance income from a US company paid in USD.
**Resolution:** [T3] ESCALATE. Foreign income is subject to Carnê-Leão (converted to BRL at the PTAX rate on the date of receipt) and must be declared on the DIRPF. However, tax treaty provisions, reciprocal credit for foreign tax paid, and currency conversion rules require specialist advice. Do not compute -- refer to a Contador with international tax expertise.

### EC10 -- MEI transitioning to autônomo [T3]
**Situation:** Client exceeded the MEI annual revenue limit (R$ 81,000) mid-year and must transition to individual taxpayer.
**Resolution:** [T3] ESCALATE. The MEI-to-autônomo transition involves retroactive reclassification, potential INSS changes, ISS recalculation, and a partial-year DIRPF with different rules. Refer to a Contador.

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
Action Required: Licensed Contador (CRC-registered) must confirm before filing.
```

When Claude identifies a [T3] situation:

```
ESCALATION REQUIRED
Tier: T3
Client: [name]
Situation: [description]
Issue: [outside skill scope]
Action Required: Do not advise. Refer to licensed Contador. Document gap.
```

---

## Step 12: Test Suite

### Test 1 -- Standard autônomo, complete declaration
**Input:** Single, gross self-employment income R$ 90,000 (all from PF), livro caixa deductions R$ 15,000, INSS paid R$ 12,000, 1 dependant, education R$ 3,561.50, medical R$ 8,000, no Carnê-Leão paid (error -- should have paid).
**Expected output:** Net self-employment = R$ 75,000. Deductions: INSS R$ 12,000 + dependant R$ 2,275.08 + education R$ 3,561.50 + medical R$ 8,000 = R$ 25,836.58. Taxable income = R$ 49,163.42. Tax = R$ 49,163.42 x 22.5% - R$ 8,054.97 = R$ 3,006.80. No credits (no Carnê-Leão paid, no IRRF). Tax due = R$ 3,006.80. Flag: client should have been paying Carnê-Leão monthly -- late payment penalties apply.

### Test 2 -- Simplified declaration is better
**Input:** Single, gross income R$ 50,000, livro caixa R$ 5,000, INSS R$ 6,000, no dependants, no medical, no education.
**Expected output:** Net income = R$ 45,000. Complete: INSS R$ 6,000, taxable = R$ 39,000. Tax = R$ 39,000 x 15% - R$ 4,679.03 = R$ 1,170.97. Simplified: 20% x R$ 45,000 = R$ 9,000, taxable = R$ 36,000. Tax = R$ 36,000 x 15% - R$ 4,679.03 = R$ 720.97. Simplified is better by R$ 450.

### Test 3 -- Livro caixa cannot create a loss
**Input:** Autônomo monthly income R$ 2,000, monthly expenses R$ 3,500.
**Expected output:** Livro caixa deduction capped at R$ 2,000. Net income for the month = R$ 0. Loss of R$ 1,500 is NOT carried forward. Carnê-Leão for the month = R$ 0.

### Test 4 -- Carnê-Leão not required for PJ income
**Input:** Freelancer receives R$ 10,000/month exclusively from companies (PJ). IRRF withheld at source.
**Expected output:** Carnê-Leão NOT required (income from PJ only). IRRF withheld is credited on the annual DIRPF. Client must still file the annual DIRPF if total income exceeds the filing threshold.

### Test 5 -- Education cap per person
**Input:** Client has 2 children. Tuition paid: Child 1 = R$ 5,000, Child 2 = R$ 2,000.
**Expected output:** Child 1 capped at R$ 3,561.50. Child 2 = R$ 2,000 (under cap). Total education deduction = R$ 5,561.50.

### Test 6 -- Both PF and PJ income in annual return
**Input:** Income from PJ = R$ 60,000 (IRRF withheld R$ 4,500). Income from PF = R$ 30,000 (Carnê-Leão paid R$ 2,800). Livro caixa on PF income = R$ 8,000. INSS = R$ 10,000. No other deductions.
**Expected output:** Net self-employment = R$ 60,000 + (R$ 30,000 - R$ 8,000) = R$ 82,000. Deductions: INSS R$ 10,000. Taxable = R$ 72,000. Tax = R$ 72,000 x 27.5% - R$ 10,853.78 = R$ 8,946.22. Credits: IRRF R$ 4,500 + Carnê-Leão R$ 2,800 = R$ 7,300. Tax due = R$ 1,646.22.

---

## PROHIBITIONS

- NEVER compute annual tax using the monthly table multiplied by 12 -- always use the annual table
- NEVER allow livro caixa deductions to exceed gross income in a given month
- NEVER carry forward livro caixa losses to the following month
- NEVER allow medical deductions without documented proof (nota fiscal or recibo)
- NEVER allow the same dependant to be claimed on two separate declarations
- NEVER present Carnê-Leão as optional when income is from individuals or foreign sources -- it is mandatory
- NEVER allow education deductions above R$ 3,561.50 per person
- NEVER allow depreciation in the livro caixa for autônomos
- NEVER advise on MEI, foreign income treaty credits, or capital gains without escalating to a Contador
- NEVER present tax calculations as definitive -- always label as estimated and direct client to a licensed Contador for confirmation

---

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a CRC-registered Contador or equivalent licensed practitioner in Brazil) before filing or acting upon.

The most up-to-date, verified version of this skill is maintained at [openaccountants.com](https://openaccountants.com). Log in to access the latest version, request a professional review from a licensed accountant, and track updates as tax law changes.
