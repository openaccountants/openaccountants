---
name: br-estimated-tax
description: >
  Use this skill whenever asked about Brazilian estimated monthly tax payments (Carne-Leao) for self-employed individuals, freelancers, or professionals receiving income from individuals or foreign sources. Trigger on phrases like "Carne-Leao", "carne-leao", "estimated tax Brazil", "Brazilian monthly tax", "DARF 0190", "recolhimento mensal obrigatorio", "livro caixa", "autonomous income tax", or any question about monthly advance income tax obligations under Brazilian tax law. Covers the monthly payment schedule, progressive rate table, deductible expenses (livro caixa), DARF 0190 payment procedure, penalties for late payment, and interaction with the annual DIRPF return. ALWAYS read this skill before touching any estimated tax work for Brazil.
version: 2.0
jurisdiction: BR
tax_year: 2025
category: international
depends_on:
  - income-tax-workflow-base
---

# Brazil Estimated Tax (Carne-Leao) -- Self-Employed Skill v2.0

## Section 1 -- Quick reference

| Field | Value |
|---|---|
| Country | Brazil |
| Tax | Monthly mandatory income tax prepayment (Carne-Leao / IRPF mensal) |
| Primary legislation | RIR/2018 (Decreto 9.580/2018), Arts. 118-122; Lei 7.713/1988, Art. 6 |
| Supporting legislation | IN RFB 1.500/2014; Lei 9.250/1995 Art. 8 (livro caixa); CTN Art. 161 |
| Authority | Receita Federal do Brasil (RFB) |
| Portal | carne-leao.receita.fazenda.gov.br / Meu Imposto de Renda |
| Currency | BRL only |
| Payment schedule | Monthly -- by last business day of the month following the income month |
| DARF code | 0190 |
| Computation | Progressive rate table applied to monthly taxable income after deductions |
| Scope | Income from individuals (pessoas fisicas) and foreign sources ONLY |
| Contributor | Open Accountants Community |
| Validated by | Pending -- requires sign-off by Brazilian contador |
| Validation date | Pending |

**Progressive rate table (2025 -- confirm when published):**

| Monthly taxable income (BRL) | Rate | Deduction (BRL) |
|---|---|---|
| Up to 2,259.20 | 0% | 0.00 |
| 2,259.21 -- 2,826.65 | 7.5% | 169.44 |
| 2,826.66 -- 3,751.05 | 15% | 381.44 |
| 3,751.06 -- 4,664.68 | 22.5% | 662.77 |
| Above 4,664.68 | 27.5% | 896.00 |

**Conservative defaults:**

| Ambiguity | Default |
|---|---|
| Income source unclear (individual vs company) | Confirm -- only income from individuals/abroad triggers Carne-Leao |
| Livro caixa expense legitimacy uncertain | Exclude uncertain expenses (cannot create negative taxable income) |
| Foreign exchange rate uncertain | Use PTAX rate per IN RFB 1.500/2014 |
| Simplified discount vs itemized | Choose whichever is higher for the client |
| No income in a month | No obligation for that month |

---

## Section 2 -- Required inputs and refusal catalogue

### Required inputs

**Minimum viable** -- monthly gross income from individuals and/or foreign sources, INSS contributions paid, number of dependents.

**Recommended** -- livro caixa expenses with documentation, alimony payments (court-ordered), prior month DARF payments.

**Ideal** -- complete monthly accounting, all client invoices/receipts, INSS contribution proofs, complete livro caixa.

**Refusal policy if minimum is missing -- SOFT WARN.** Without monthly income figures, the progressive table cannot be applied. Request at minimum the gross amount received.

### Refusal catalogue

**R-BR-ET-1 -- Income from legal entities.** Trigger: client asks about Carne-Leao on income from companies. Message: "Income from legal entities (pessoas juridicas) is subject to IRRF at source, not Carne-Leao. Carne-Leao applies only to income from individuals and foreign sources."

**R-BR-ET-2 -- Cryptocurrency income.** Trigger: client asks about crypto Carne-Leao. Message: "Cryptocurrency income taxation has specific rules outside this skill."

**R-BR-ET-3 -- Non-resident interactions.** Trigger: client is non-resident or transitioning residency. Message: "Non-resident tax obligations are outside this skill."

---

## Section 3 -- Payment pattern library

This is the deterministic pre-classifier for bank statement transactions. When a debit matches a pattern below, classify it as a Carne-Leao payment.

### 3.1 DARF 0190 debits

| Pattern | Treatment | Notes |
|---|---|---|
| DARF, DOCUMENTO DE ARRECADACAO | Carne-Leao payment | Match with code 0190 |
| RECEITA FEDERAL, RFB | Carne-Leao payment | Match with monthly timing |
| CODIGO 0190 | Carne-Leao payment | Explicit DARF code |
| CARNE LEAO, CARNE-LEAO | Carne-Leao payment | Explicit description |
| IMPOSTO DE RENDA MENSAL | Carne-Leao payment | Monthly income tax |

### 3.2 Timing-based identification

Monthly payments are due by the last business day of the following month. A DARF 0190 debit in February likely covers January income.

| Debit month | Income month covered |
|---|---|
| February | January |
| March | February |
| ... | ... |
| January (next year) | December |

### 3.3 Related but NOT Carne-Leao

| Pattern | Treatment | Notes |
|---|---|---|
| DARF with code other than 0190 | EXCLUDE | Different tax obligation |
| INSS, CONTRIBUICAO PREVIDENCIARIA | EXCLUDE | Social security |
| ISS, IMPOSTO SOBRE SERVICOS | EXCLUDE | Municipal service tax |
| IRRF, RETENCAO NA FONTE | EXCLUDE | Withholding at source (from companies) |
| IRPF QUOTA, DECLARACAO ANUAL | EXCLUDE | Annual return balance payment |
| MULTA, JUROS DE MORA | EXCLUDE | Late payment penalty/interest |
| GPS, GUIA DA PREVIDENCIA | EXCLUDE | Social security contribution |

---

## Section 4 -- Worked examples

### Example 1 -- Standard monthly computation

**Input:** Monthly income BRL 8,000 from individual clients. INSS = BRL 877.24. 1 dependent. Livro caixa expenses = BRL 1,200.

| Item | Amount |
|---|---|
| Gross income | BRL 8,000.00 |
| Less INSS | BRL 877.24 |
| Less 1 dependent | BRL 189.59 |
| Less livro caixa | BRL 1,200.00 |
| Taxable income | BRL 5,733.17 |
| Tax (27.5%) | BRL 1,576.62 |
| Less table deduction | BRL 896.00 |
| **Carne-Leao due** | **BRL 680.62** |

### Example 2 -- Below exempt threshold

**Input:** Monthly income BRL 2,000 after deductions.

**Output:** Taxable income BRL 2,000 < BRL 2,259.20. 0% rate. No tax due.

### Example 3 -- Mixed income sources

**Input:** BRL 5,000 from individuals + BRL 10,000 from a company.

**Output:** Carne-Leao on BRL 5,000 only. The BRL 10,000 from the company is subject to IRRF at source.

### Example 4 -- Foreign-source income

**Input:** Brazilian resident receives USD 3,000 from US client. PTAX rate = BRL 5.20.

**Computation:** BRL equivalent = 3,000 x 5.20 = BRL 15,600. Subject to Carne-Leao at progressive rates. Flag for contador to confirm exchange rate methodology.

### Example 5 -- Bank statement classification

**Input line:** `28.02.2025 ; DARF COD 0190 PERIODO 01/2025 ; DEBITO ; -680.62 ; BRL`

**Classification:** Carne-Leao payment for January 2025 income. Tax payment -- not a deductible business expense.

---

## Section 5 -- Computation rules

### 5.1 Monthly computation formula

```
gross_income = income from individuals + foreign income for the month
deductions = dependents + INSS + livro_caixa + alimony
taxable_income = gross_income - deductions
tax_due = (taxable_income x applicable_rate) - table_deduction
carne_leao = max(0, tax_due)
```

### 5.2 Deductions allowed

| Deduction | Amount (2025) |
|---|---|
| Per dependent | BRL 189.59/month |
| INSS (contribuinte individual) | Actual amount paid |
| Livro caixa expenses | Actual documented expenses |
| Court-ordered alimony | Actual amount paid |
| Simplified monthly discount | BRL 564.80 (alternative to itemized) |

### 5.3 Livro caixa rules

Allowed: office rent, utilities for professional space, professional materials, employee costs, professional development, travel directly related to services.

Not allowed: personal expenses, vehicle depreciation (personal use), full home office (only proportional area).

Livro caixa deductions CANNOT create a negative taxable income from the activity. Floor is BRL 0.

### 5.4 Interaction with annual DIRPF

All Carne-Leao payments are credited against the annual DIRPF liability.

```
annual_tax = tax on total annual income
credits = total_carne_leao + total_IRRF
balance = annual_tax - credits
if balance > 0: pay (or split into up to 8 instalments)
if balance < 0: refund
```

---

## Section 6 -- Penalties and interest

### 6.1 Late payment charges

| Element | Rule |
|---|---|
| Multa de mora (penalty) | 0.33% per day, capped at 20% |
| Juros de mora (interest) | SELIC accumulated from month after due date + 1% in payment month |

### 6.2 Computation

```
penalty = min(tax x 0.33% x days_late, tax x 20%)
interest = tax x (accumulated_SELIC + 1%)
total = tax + penalty + interest
```

### 6.3 Failure to pay does not eliminate obligation

Not paying Carne-Leao during the year does NOT eliminate the obligation. The annual DIRPF will show the tax due plus accumulated penalties and interest.

---

## Section 7 -- DARF payment procedure

### 7.1 DARF generation

1. Access Carne-Leao module at carne-leao.receita.fazenda.gov.br or Meu Imposto de Renda
2. Enter monthly income, deductions, dependents
3. System calculates tax and generates DARF with code 0190
4. Pay via internet banking, ATM, or bank branch
5. Retain DARF receipt for annual return filing

### 7.2 DARF fields

| Field | Value |
|---|---|
| Codigo da Receita | 0190 |
| Periodo de Apuracao | Last day of income month |
| CPF | Client's CPF |
| Valor Principal | Tax amount due |

---

## Section 8 -- Edge cases

**EC1 -- Mixed income from individuals and companies.** Carne-Leao applies only to the portion from individuals. Company income is subject to IRRF at source.

**EC2 -- Foreign-source income.** Subject to Carne-Leao. Convert using PTAX rate per IN RFB 1.500/2014. Flag for contador.

**EC3 -- No income in a month.** No Carne-Leao obligation. No DARF needed.

**EC4 -- Income below exempt threshold.** Taxable income below BRL 2,259.20 after deductions: 0% rate, no tax due.

**EC5 -- Livro caixa exceeds income.** Deductions cannot create negative taxable income. Floor is BRL 0.

**EC6 -- Simplified discount vs itemized.** Client may choose whichever produces lower taxable income: simplified BRL 564.80 or itemized deductions.

---

## Section 9 -- Self-checks

Before delivering output, verify:

- [ ] Income source confirmed (individuals/abroad vs legal entities)
- [ ] Progressive table rates current for 2025
- [ ] Livro caixa deductions documented and legitimate
- [ ] Livro caixa does not create negative taxable income
- [ ] DARF code 0190 used
- [ ] Payment deadline is last business day of following month
- [ ] SELIC-based interest rate current for penalty calculations
- [ ] Dependent deduction amount current
- [ ] INSS contribution correctly deducted
- [ ] Output labelled as estimated until contador confirms

---

## Section 10 -- Test suite

### Test 1 -- Standard monthly computation
**Input:** Income BRL 8,000. INSS BRL 877.24. 1 dependent. Livro caixa BRL 1,200.
**Expected:** Taxable = BRL 5,733.17. Tax = BRL 680.62.

### Test 2 -- Below exempt threshold
**Input:** Taxable income BRL 2,000.
**Expected:** 0% rate. No tax due.

### Test 3 -- Mixed sources
**Input:** BRL 5,000 from individuals. BRL 10,000 from company.
**Expected:** Carne-Leao on BRL 5,000 only.

### Test 4 -- No income
**Input:** No qualifying income in March.
**Expected:** No obligation.

### Test 5 -- Late payment
**Input:** BRL 680.62 due 28 Feb. Paid 45 days late. SELIC accumulated = 0.92%.
**Expected:** Penalty = BRL 680.62 x 0.33% x 45 = BRL 101.07 (capped at 20% = BRL 136.12, so BRL 101.07 applies). Interest = BRL 680.62 x (0.92% + 1%) = BRL 13.07.

### Test 6 -- Foreign income
**Input:** USD 3,000. PTAX = 5.20.
**Expected:** BRL 15,600 subject to Carne-Leao at progressive rates.

---

## Prohibitions

- NEVER apply Carne-Leao to income from legal entities (subject to IRRF at source)
- NEVER allow livro caixa deductions to create negative taxable income
- NEVER forget SELIC-based interest when computing late payment charges
- NEVER use the wrong DARF code -- always 0190 for Carne-Leao
- NEVER ignore the monthly nature of the obligation -- it is NOT quarterly
- NEVER present amounts as definitive -- advise confirmation with contador

---

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a contador or equivalent licensed practitioner in your jurisdiction) before filing or acting upon.

The most up-to-date, verified version of this skill is maintained at [openaccountants.com](https://openaccountants.com). Log in to access the latest version, request a professional review from a licensed accountant, and track updates as tax law changes.
