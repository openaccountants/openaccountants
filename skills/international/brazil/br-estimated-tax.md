---
name: br-estimated-tax
description: >
  Use this skill whenever asked about Brazilian estimated monthly tax payments (Carne-Leao) for self-employed individuals, freelancers, or professionals receiving income from individuals or foreign sources. Trigger on phrases like "Carne-Leao", "carnê-leão", "estimated tax Brazil", "Brazilian monthly tax", "DARF 0190", "recolhimento mensal obrigatorio", "livro caixa", "autonomous income tax", or any question about monthly advance income tax obligations under Brazilian tax law. This skill covers the monthly payment schedule, progressive rate table, deductible expenses (livro caixa), DARF 0190 payment procedure, penalties for late payment, and interaction with the annual DIRPF return. ALWAYS read this skill before touching any estimated tax work for Brazil.
version: 1.0
jurisdiction: BR
tax_year: 2025
category: international
depends_on:
  - income-tax-workflow-base
---

# Brazil Estimated Tax (Carne-Leao) -- Self-Employed Skill

---

## Skill Metadata

| Field | Value |
|-------|-------|
| Jurisdiction | Brazil |
| Jurisdiction Code | BR |
| Primary Legislation | Regulamento do Imposto de Renda (RIR/2018), Decreto 9.580/2018, Arts. 118-122 (Carne-Leao); Lei 7.713/1988, Art. 6 (monthly obligation) |
| Supporting Legislation | Instrucao Normativa RFB 1.500/2014 (operational rules); Lei 9.250/1995 Art. 8 (livro caixa); CTN Art. 161 (late payment interest) |
| Tax Authority | Receita Federal do Brasil (RFB) |
| Rate Publisher | Receita Federal (publishes progressive table updates) |
| Contributor | Open Accountants community |
| Validated By | Pending -- requires sign-off by Brazilian contador |
| Validation Date | Pending |
| Skill Version | 1.0 |
| Confidence Coverage | Tier 1: monthly obligation, progressive rates, DARF 0190 procedure, livro caixa deductions, late payment penalty. Tier 2: foreign-source income treatment, dependent deduction, multi-source income aggregation. Tier 3: non-resident interactions, tax treaty credits, cryptocurrency income. |

---

## Confidence Tier Definitions

- **[T1] Tier 1 -- Deterministic.** Apply exactly as written. No reviewer judgement required.
- **[T2] Tier 2 -- Reviewer Judgement Required.** Claude flags and presents options. Contador must confirm.
- **[T3] Tier 3 -- Out of Scope / Escalate.** Do not guess. Escalate and document.

---

## Step 0: Client Onboarding Questions

Before computing any Carne-Leao payment, you MUST know:

1. **Source of income** [T1] -- from individuals (pessoas fisicas), from abroad, rental income, or other non-withheld sources
2. **Monthly gross income** [T1] -- total received from sources not subject to withholding at source
3. **Deductible expenses (livro caixa)** [T1] -- expenses essential to the professional activity
4. **Number of dependents** [T1] -- each dependent generates a monthly deduction
5. **Social security (INSS) contributions** [T1] -- deductible from the tax base
6. **Alimony payments (pensao alimenticia) ordered by court** [T1] -- deductible
7. **Other income subject to withholding (IRRF)?** [T1] -- NOT included in Carne-Leao computation
8. **Is this income from abroad?** [T2] -- subject to Carne-Leao but with FOREX conversion rules

**Carne-Leao applies ONLY to income received from individuals (pessoas fisicas) or from abroad. Income from legal entities (pessoas juridicas) is subject to withholding at source (IRRF) and is NOT part of Carne-Leao.**

---

## Step 1: Determine Carne-Leao Obligation [T1]

**Legislation:** RIR/2018, Art. 118; Lei 7.713/1988, Art. 6

### Who Must Pay Carne-Leao

| Category | Carne-Leao Required? |
|----------|---------------------|
| Freelancer/professional receiving from individuals | YES |
| Landlord receiving rent from individual tenants | YES |
| Resident receiving income from abroad (salary, services, etc.) | YES |
| Professional receiving from legal entities (companies) | NO (subject to IRRF at source) |
| Employee with only salary income | NO (employer withholds IRRF) |

---

## Step 2: Payment Schedule [T1]

### Monthly Due Dates

Carne-Leao is computed and paid MONTHLY. Payment is due by the **last business day of the month following the month in which income was received**.

| Income Month | Payment Deadline |
|-------------|-----------------|
| January 2025 | Last business day of February 2025 |
| February 2025 | Last business day of March 2025 |
| March 2025 | Last business day of April 2025 |
| ... | ... |
| December 2025 | Last business day of January 2026 |

---

## Step 3: Computation Method [T1]

### Monthly Progressive Table (2025)

**Note:** The table below reflects the 2024 table (Lei 14.848/2024). Confirm the 2025 table when published by Receita Federal.

| Monthly Taxable Income (BRL) | Rate | Deduction (BRL) |
|------------------------------|------|-----------------|
| Up to 2,259.20 | 0% | 0.00 |
| 2,259.21 -- 2,826.65 | 7.5% | 169.44 |
| 2,826.66 -- 3,751.05 | 15% | 381.44 |
| 3,751.06 -- 4,664.68 | 22.5% | 662.77 |
| Above 4,664.68 | 27.5% | 896.00 |

### Deductions Allowed Before Applying the Table

| Deduction | Amount (2025) |
|-----------|---------------|
| Per dependent | BRL 189.59 per month |
| INSS contributions (as contribuinte individual) | Actual amount paid |
| Livro caixa expenses | Actual documented expenses (see Step 4) |
| Alimony (court-ordered pensao alimenticia) | Actual amount paid |
| Simplified monthly discount | BRL 564.80 (optional alternative to itemized deductions) |

### Computation Formula

```
gross_income = total income from individuals + foreign income for the month
deductions = dependents + INSS + livro_caixa + alimony
taxable_income = gross_income - deductions
tax_due = (taxable_income x applicable_rate) - table_deduction
carne_leao_payment = tax_due
```

### Example: Monthly Income BRL 8,000

| Item | Amount |
|------|--------|
| Gross income | BRL 8,000.00 |
| INSS contribution | BRL 877.24 |
| 1 dependent | BRL 189.59 |
| Livro caixa expenses | BRL 1,200.00 |
| Taxable income | BRL 5,733.17 |
| Tax (27.5% x 5,733.17) | BRL 1,576.62 |
| Less table deduction | BRL 896.00 |
| Carne-Leao due | BRL 680.62 |

---

## Step 4: Livro Caixa (Cash Book) Deductions [T1]

**Legislation:** Lei 9.250/1995, Art. 8

### Allowed Expenses

| Category | Examples |
|----------|----------|
| Office rent | Rent for professional office/studio |
| Utilities | Electricity, water, internet for the professional space |
| Professional materials | Supplies, equipment depreciation |
| Employee costs | Salary, FGTS, INSS of employees |
| Professional development | Courses, books, conferences directly related to activity |
| Travel | Travel expenses directly related to professional services |

### NOT Allowed

| Category | Why |
|----------|-----|
| Personal expenses | Not related to the professional activity |
| Vehicle depreciation (personal use) | Mixed use requires apportionment -- [T2] |
| Home office (full) | Only proportional area may be deducted -- [T2] |

**Livro caixa deductions cannot create a negative taxable income. The minimum taxable income from the activity is BRL 0.**

---

## Step 5: DARF Payment Procedure [T1]

### DARF Code

| Code | Description |
|------|-------------|
| **0190** | Carne-Leao -- IRPF recolhimento mensal |

### How to Generate and Pay the DARF

| Step | Action |
|------|--------|
| 1 | Access the Carne-Leao module at carne-leao.receita.fazenda.gov.br or via the Meu Imposto de Renda program |
| 2 | Enter monthly income, deductions, and dependents |
| 3 | System calculates the tax and generates the DARF with code 0190 |
| 4 | Pay via internet banking, ATM, or bank branch by the due date |
| 5 | Retain the DARF receipt for annual return filing |

### DARF Fields

| Field | Value |
|-------|-------|
| Codigo da Receita | 0190 |
| Periodo de Apuracao | Last day of the income month (e.g., 31/01/2025) |
| CPF | Client's CPF number |
| Valor Principal | Tax amount due |

---

## Step 6: Penalties for Late Payment [T1]

**Legislation:** CTN Art. 161; Lei 9.430/1996, Art. 61

### Late Payment Charges

| Element | Rule |
|---------|------|
| Multa de mora (penalty) | 0.33% per day, capped at 20% of the tax due |
| Juros de mora (interest) | SELIC rate accumulated from the month after due date to the month of payment, plus 1% in the month of payment |

### Computation

```
days_late = payment_date - due_date
penalty = min(unpaid_tax x 0.33% x days_late, unpaid_tax x 20%)
interest = unpaid_tax x (accumulated_SELIC_rate + 1%)
total_due = unpaid_tax + penalty + interest
```

---

## Step 7: Interaction with Annual Return (DIRPF) [T1]

**Legislation:** RIR/2018, Art. 122

### Year-End Treatment

All Carne-Leao payments made during the year are reported in the annual DIRPF (Declaracao do Imposto de Renda Pessoa Fisica) and credited against the annual tax liability.

```
annual_tax = tax_on_total_annual_income
total_carne_leao_paid = sum of all monthly DARF 0190 payments
total_IRRF = sum of all withholdings at source
balance = annual_tax - total_carne_leao_paid - total_IRRF
if balance > 0:
    pay_balance  # or split into up to 8 monthly instalments
else:
    refund = abs(balance)
```

**Failure to pay Carne-Leao during the year does NOT eliminate the obligation. The annual return will show the tax due plus accumulated penalties and interest.**

---

## Step 8: Edge Cases

### EC1 -- Mixed income from individuals and companies [T1]
**Situation:** Client receives BRL 5,000/month from individual clients and BRL 10,000/month from a company.
**Resolution:** Carne-Leao applies only to the BRL 5,000 from individuals. The BRL 10,000 from the company is subject to IRRF at source.

### EC2 -- Foreign-source income [T2]
**Situation:** Brazilian resident receives USD 3,000/month from a US client.
**Resolution:** Subject to Carne-Leao. Convert to BRL using the PTAX exchange rate on the last business day of the first half of the month prior to receipt (per IN RFB 1.500/2014). [T2] flag -- confirm exchange rate methodology with contador.

### EC3 -- No income in a particular month [T1]
**Situation:** Client had no qualifying income in March.
**Resolution:** No Carne-Leao obligation for that month. No DARF needs to be generated.

### EC4 -- Income below the exempt threshold [T1]
**Situation:** Client's monthly taxable income after deductions is below BRL 2,259.20.
**Resolution:** No tax due for that month. The 0% bracket applies.

---

## Self-Checks

Before delivering output, verify:

- [ ] Income source confirmed (individuals/abroad vs legal entities)
- [ ] Progressive table rates current for 2025
- [ ] Livro caixa deductions documented and legitimate
- [ ] DARF code 0190 used
- [ ] Payment deadline is last business day of following month
- [ ] SELIC-based interest rate current for penalty calculations

---

## PROHIBITIONS

- NEVER apply Carne-Leao to income received from legal entities (pessoas juridicas) -- that income is subject to IRRF at source
- NEVER allow livro caixa deductions to create a negative taxable income
- NEVER forget to include the SELIC-based interest when computing late payment charges
- NEVER use the wrong DARF code -- Carne-Leao is ALWAYS code 0190
- NEVER ignore the monthly nature of the obligation -- it is NOT quarterly
- NEVER present tax amounts as definitive -- advise client to confirm with their contador

---

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a contador or equivalent licensed practitioner in your jurisdiction) before filing or acting upon.

The most up-to-date, verified version of this skill is maintained at [openaccountants.com](https://openaccountants.com). Log in to access the latest version, request a professional review from a licensed accountant, and track updates as tax law changes.
