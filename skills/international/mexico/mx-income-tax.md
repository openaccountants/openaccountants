---
name: mx-income-tax
description: >
  Use this skill whenever asked about Mexican individual income tax (ISR) for self-employed individuals (personas físicas con actividades empresariales y profesionales). Trigger on phrases like "how much tax do I pay in Mexico", "ISR", "Declaración Anual", "pagos provisionales", "actividades profesionales", "honorarios", "RESICO", "deducciones personales", "deducciones autorizadas", "RFC", "income tax return Mexico", "SAT", or any question about filing or computing income tax for a self-employed or freelance client in Mexico. This skill covers the Declaración Anual PF, pagos provisionales (monthly estimated payments), progressive ISR brackets, deducciones autorizadas and personales, retenciones on professional invoices, and the RESICO regime comparison. ALWAYS read this skill before touching any Mexican income tax work.
version: 1.0
jurisdiction: MX
tax_year: 2025
category: international
depends_on:
  - income-tax-workflow-base
---

# Mexico Income Tax (ISR) -- Self-Employed Skill

---

## Skill Metadata

| Field | Value |
|-------|-------|
| Jurisdiction | Mexico |
| Jurisdiction Code | MX |
| Primary Legislation | Ley del Impuesto Sobre la Renta (LISR), particularly Título IV, Capítulo II, Sección I (Actividades Empresariales y Profesionales) |
| Supporting Legislation | Código Fiscal de la Federación (CFF); Resolución Miscelánea Fiscal (RMF) 2025, Anexo 8 (tarifas); LISR Arts. 100-110 (business/professional activities), Art. 111-113 (RESICO), Art. 148 (non-deductible), Art. 151 (personal deductions), Art. 152 (annual tariff) |
| Tax Authority | Servicio de Administración Tributaria (SAT) |
| Filing Portal | Portal del SAT (sat.gob.mx) |
| Contributor | Open Accountants Community |
| Validated By | Pending -- requires sign-off by a Mexican Contador Público Certificado (CPC) |
| Validation Date | Pending |
| Skill Version | 1.0 |
| Confidence Coverage | Tier 1: rate table application, pago provisional calculation, personal deduction caps, filing deadline, retención rate, RESICO eligibility threshold. Tier 2: deducción autorizada classification, depreciation rates, mixed-use expense apportionment, home office. Tier 3: foreign income, tax treaties, corporate structures, transfer pricing, RESICO-to-general transition mid-year. |

---

## Confidence Tier Definitions

- **[T1] Tier 1 -- Deterministic.** Apply exactly as written. No reviewer judgement required.
- **[T2] Tier 2 -- Reviewer Judgement Required.** Claude flags and presents options. Licensed Contador Público must confirm.
- **[T3] Tier 3 -- Out of Scope / Escalate.** Do not guess. Escalate and document.

---

## Step 0: Client Onboarding Questions

Before computing any income tax figure, you MUST know:

1. **RFC (Registro Federal de Contribuyentes)** [T1] -- mandatory for all filings. If missing, STOP.
2. **Tax regime** [T1] -- Régimen de Actividades Empresariales y Profesionales (general) or RESICO. Determines computation method.
3. **Type of activity** [T1] -- actividades empresariales (business) or servicios profesionales (professional/freelance). Affects retención rules.
4. **Gross income** [T1] -- total invoiced (facturado) in the fiscal year via CFDI
5. **Source of income** [T1] -- from personas morales (companies), personas físicas (individuals), or foreign. Determines retención applicability.
6. **Business expenses (deducciones autorizadas)** [T1/T2] -- nature and amount, with CFDI backup
7. **Personal deductions (deducciones personales)** [T1] -- medical, education, funeral, mortgage, donations
8. **Pagos provisionales made** [T1] -- monthly estimated tax payments made during the year
9. **Retenciones received** [T1] -- ISR withheld by clients (personas morales)
10. **Other income** [T1] -- employment (salarios), rental (arrendamiento), interest, dividends

**If RFC is unknown, STOP. RFC is mandatory for any Mexican tax computation.**

---

## Step 1: Determine Tax Regime [T1]

**Legislation:** LISR Título IV, Capítulo II

### Régimen de Actividades Empresariales y Profesionales (General) [T1]

This is the standard regime for self-employed professionals and business owners. This skill primarily covers this regime.

- No revenue cap
- Tax computed on net profit (income minus deducciones autorizadas)
- Progressive rates from 1.92% to 35%
- Monthly pagos provisionales required
- Annual Declaración Anual required

### RESICO (Régimen Simplificado de Confianza) -- Comparison Only [T1]

| Feature | RESICO | General Regime |
|---------|--------|----------------|
| Revenue cap | MXN $3,500,000/year | No cap |
| Tax base | Gross revenue (ingresos cobrados) | Net profit (ingresos - deducciones) |
| Rates | 1.00% to 2.50% on revenue | 1.92% to 35% on profit |
| Deductions | NOT allowed (except personal) | Fully allowed |
| Invoicing | CFDI required | CFDI required |
| Best for | Low-expense businesses | High-expense businesses |

**RESICO is OUT OF SCOPE for detailed computation in this skill.** If a client is on RESICO, note the regime and flag for a Contador to handle. This skill provides the general regime computation only.

---

## Step 2: Annual ISR Tariff (Art. 152 LISR) [T1]

**Legislation:** LISR Art. 152; RMF 2025, Anexo 8

### Annual Progressive Table (Fiscal Year 2025)

| Límite Inferior (MXN) | Límite Superior (MXN) | Cuota Fija (MXN) | % sobre Excedente |
|------------------------|------------------------|-------------------|--------------------|
| $0.01 | $8,952.48 | $0.00 | 1.92% |
| $8,952.49 | $75,984.60 | $171.84 | 6.40% |
| $75,984.61 | $133,536.12 | $4,461.96 | 10.88% |
| $133,536.13 | $155,229.84 | $10,723.56 | 16.00% |
| $155,229.85 | $185,852.52 | $14,194.56 | 17.92% |
| $185,852.53 | $374,837.88 | $19,671.84 | 21.36% |
| $374,837.89 | $590,796.00 | $59,965.52 | 23.52% |
| $590,796.01 | $1,127,926.80 | $110,842.56 | 30.00% |
| $1,127,926.81 | $1,503,902.40 | $271,981.80 | 32.00% |
| $1,503,902.41 | $4,511,707.32 | $392,294.04 | 34.00% |
| $4,511,707.33 | En adelante | $1,414,947.72 | 35.00% |

**Note:** The 2025 tariff is unchanged from 2024. Under Art. 152 LISR, brackets are updated only when accumulated inflation exceeds 10% since the last update (January 2021). This threshold was not met for 2025.

### How to Calculate Annual ISR [T1]

```
1. Determine base gravable (taxable income)
2. Locate the row where base gravable falls between Límite Inferior and Límite Superior
3. Excedente = base gravable - Límite Inferior of that row
4. ISR = Cuota Fija + (Excedente x % sobre Excedente)
```

---

## Step 3: UMA Values for 2025 [T1]

**Legislation:** Ley para Determinar el Valor de la UMA; INEGI annual update

| Period | Daily | Monthly | Annual |
|--------|-------|---------|--------|
| 2025 (from 1 Feb 2025) | $113.14 | $3,439.46 | $41,273.52 |

The UMA (Unidad de Medida y Actualización) is used to calculate caps on personal deductions, social security contributions, and other fiscal thresholds. It replaced the minimum wage (salario mínimo) for fiscal purposes.

---

## Step 4: Pagos Provisionales -- Monthly Estimated Tax [T1]

**Legislation:** LISR Arts. 106, 109

### How Pagos Provisionales Work [T1]

Self-employed individuals under the general regime must make monthly estimated tax payments by the 17th of the following month.

### Calculation Method [T1]

```
1. Cumulative income (ingresos acumulables) from January to current month     = A
2. Less: Cumulative deducciones autorizadas from January to current month     = B
3. Less: PTU paid to employees (if applicable)                                = C
4. Less: Prior year losses carried forward (pérdidas fiscales)                = D
5. Cumulative taxable base                                                    = E = A - B - C - D
6. Apply the MONTHLY cumulative tariff (Anexo 8 RMF) to E                    = F (gross tax)
7. Less: Subsidio para el empleo (if applicable)                              = G
8. Less: Retenciones received from personas morales (cumulative)              = H
9. Less: Pagos provisionales previously paid in the year                      = I
10. Pago provisional due for this month                                       = J = F - G - H - I
```

**If J is negative or zero, no payment is due for the month, but the declaration must still be filed.**

### Retención on Professional Services [T1]

**Legislation:** LISR Art. 106, penultimate paragraph

When a persona moral (company) pays a persona física for professional services (honorarios), the company must withhold:

| Item | Rate |
|------|------|
| ISR retención | 10% of the gross payment (before IVA) |

This 10% retención is credited against the professional's pago provisional and annual ISR liability. The professional must issue a CFDI showing the retención.

**The 10% retención only applies to payments from personas morales. Payments from personas físicas do not carry ISR retención.**

---

## Step 5: Deducciones Autorizadas -- Business Deductions [T1/T2]

**Legislation:** LISR Arts. 103-106; Art. 148 (non-deductible)

### Requirements for Deductibility [T1]

ALL business deductions must meet these conditions:
1. **Strictly indispensable** (estrictamente indispensable) for the business activity
2. **Supported by a valid CFDI** (Comprobante Fiscal Digital por Internet)
3. **Paid via bank transfer, cheque, or electronic means** if amount exceeds MXN $2,000 (cash payments above this amount are non-deductible)
4. **Properly registered** in accounting records

### Deductible Business Expenses

| Expense | Tier | Treatment |
|---------|------|-----------|
| Office rent | T1 | Fully deductible with CFDI |
| Employee wages and social security (IMSS, SAR, Infonavit) | T1 | Fully deductible |
| Professional services (subcontractors with CFDI) | T1 | Fully deductible |
| Office supplies and materials | T1 | Fully deductible |
| Software subscriptions | T1 | Fully deductible |
| Marketing and advertising | T1 | Fully deductible |
| Insurance premiums (business) | T1 | Fully deductible |
| Business travel (flights, hotels, meals on travel) | T1 | Fully deductible with CFDI and business purpose documented |
| Vehicle fuel (combustible) | T1 | Deductible with CFDI -- payment must be electronic |
| Depreciation (depreciación fiscal) | T1 | Per LISR Art. 31-38 rates |
| Bad debts (cuentas incobrables) | T2 | Deductible after meeting prescription or documented uncollectibility. Flag for reviewer |
| Home office | T2 | Proportional only. Flag for reviewer |
| Vehicle expenses (mixed use) | T2 | Business portion only. Flag for reviewer |

### Depreciation Rates (Art. 31-38 LISR) [T1]

| Asset Type | Maximum Annual Rate |
|-----------|-------------------|
| Computers and peripherals | 30% |
| Office furniture | 10% |
| Motor vehicles | 25% |
| Buildings | 5% |
| Machinery and equipment | 10% |
| Dies, moulds, tooling | 35% |

**Vehicle depreciation cap:** The deductible cost basis for automobiles is capped at MXN $175,000 (approximately). Verify the current year's cap.

### NOT Deductible (Art. 148 LISR) [T1]

| Expense | Reason |
|---------|--------|
| ISR payments | Tax on income cannot reduce income |
| Personal living expenses | Not business-related |
| Fines and penalties (multas, recargos) | Public policy -- Art. 148 fraction I |
| Provisions and reserves | Not yet incurred |
| Cash payments above MXN $2,000 without bank transfer | Art. 148 fraction VII |
| Expenses without valid CFDI | No fiscal proof |
| Entertainment and gifts (representación) | Blocked -- Art. 148 fraction III |
| Donations (as business expense) | Only deductible as personal deduction, not business |

---

## Step 6: Deducciones Personales -- Personal Deductions [T1]

**Legislation:** LISR Art. 151

### Personal Deduction Items [T1]

| Deduction | Limit | Notes |
|-----------|-------|-------|
| Medical, dental, hospital, and nutrition expenses | No cap per item | Must be paid via bank transfer. Only taxpayer, spouse, direct family. |
| Funeral expenses | 1 UMA annual = MXN $41,273.52 | Only for taxpayer and direct family |
| Charitable donations | Up to 7% of prior year's net taxable income | To authorised donatarias only |
| Mortgage interest (crédito hipotecario) | Interest on loans up to 750,000 UDIs | Primary residence only |
| Voluntary retirement contributions (aportaciones complementarias) | Up to 10% of income or 5 UMA annual, whichever is lower | To SAR, personal retirement plans |
| School tuition (colegiaturas) | Varies by level: preschool $14,200, primary $12,900, secondary $19,900, profesional técnico $17,100, bachillerato $24,500 | Per student. NOT university. |
| Health insurance premiums | Actual amount | Complementary health insurance only |
| Local transportation (transporte escolar) | Actual amount | Only if mandatory by school |

### Overall Cap on Personal Deductions [T1]

Total personal deductions are capped at the **lesser of**:
- 15% of the taxpayer's total gross income, OR
- 5 UMA anuales = MXN $206,367.60 (for 2025)

**Medical expenses are included in this cap.** This is a critical difference from Brazil where medical has no cap.

---

## Step 7: Annual Declaration Computation [T1]

**Legislation:** LISR Arts. 109, 150-152

### Computation Walkthrough

```
1. Total invoiced income (ingresos acumulables)                    = A
2. Less: Deducciones autorizadas (business deductions)             = B
3. Less: PTU paid                                                  = C
4. Less: Prior year tax losses (pérdidas fiscales pendientes)      = D
5. Net business profit (utilidad fiscal)                           = E = A - B - C - D
6. Add: Other taxable income (salarios, arrendamiento, etc.)      = F
7. Total accumulated income                                        = G = E + F
8. Less: Deducciones personales (capped per Step 6)               = H
9. Base gravable (taxable income)                                  = I = G - H
10. Apply Art. 152 annual tariff to I                              = J (ISR del ejercicio)
11. Less: Retenciones received (ISR withheld by payers)            = K
12. Less: Pagos provisionales paid during the year                 = L
13. ISR due or in favour                                           = M = J - K - L
```

**If M > 0:** tax balance due, payable with the annual declaration by 30 April.
**If M < 0:** saldo a favor -- request refund via the SAT portal.

---

## Step 8: Filing Deadlines [T1]

**Legislation:** LISR Art. 150; CFF

| Event | Deadline |
|-------|----------|
| Declaración Anual PF (tax year 2025) | 30 April 2026 |
| Pagos provisionales (monthly) | 17th of the following month |
| Informativa de retenciones (if applicable) | February of following year |

### Late Filing Penalties [T1]

| Offence | Penalty |
|---------|---------|
| Late filing of Declaración Anual | MXN $1,810 to $22,400 per obligation (CFF Art. 82) |
| Late pago provisional | Recargos (surcharges): approximately 1.47% per month on unpaid tax (updated monthly by SAT) |
| Actualización | Inflation adjustment on unpaid tax from due date to payment date |
| Omission of income | 55% to 75% of omitted tax (CFF Art. 76) |
| Tax fraud (defraudación fiscal) | Criminal penalties -- CFF Art. 108 |

---

## Step 9: Edge Case Registry

### EC1 -- Cash payment over MXN $2,000 [T1]
**Situation:** Freelancer pays MXN $5,000 cash to a supplier for materials with a valid CFDI.
**Resolution:** NOT deductible. Art. 148 LISR requires payments over MXN $2,000 to be made via bank transfer, cheque nominativo, or electronic means. The CFDI exists but the payment method disqualifies the deduction.

### EC2 -- CFDI missing for an expense [T1]
**Situation:** Client paid MXN $8,000 for equipment and has a receipt but no CFDI.
**Resolution:** NOT deductible. Without a valid CFDI, the expense cannot be included in deducciones autorizadas. The client should request the CFDI from the supplier retroactively if still within the fiscal year.

### EC3 -- Personal deduction cap exceeded [T1]
**Situation:** Client has MXN $500,000 gross income and claims MXN $120,000 in personal deductions (medical, tuition, etc.).
**Resolution:** Cap = lesser of 15% x $500,000 = $75,000 or 5 UMA anuales = $206,367.60. Cap is $75,000. Deductions capped at $75,000. The client must prioritise which deductions to claim up to the cap.

### EC4 -- Retención on payment from persona física [T1]
**Situation:** Freelance accountant invoices MXN $20,000 to an individual client (persona física). Client asks about withholding 10% ISR.
**Resolution:** NO retención applies. The 10% ISR retención under Art. 106 only applies when the payer is a persona moral (company). Payments from personas físicas carry no ISR retención. The freelancer must include this income in their pago provisional.

### EC5 -- RESICO client exceeds revenue cap [T1]
**Situation:** Client on RESICO earns MXN $4,000,000 in the year (exceeds MXN $3,500,000 cap).
**Resolution:** [T3] ESCALATE. The client must transition to the Régimen General. The SAT may reclassify retroactively. This requires specialist handling for the transition computation, historical pago recomputation, and potential penalties. Refer to a Contador.

### EC6 -- Entertainment deducted as business expense [T1]
**Situation:** Client includes MXN $15,000 in client entertainment (restaurant meals, gifts) in deducciones autorizadas.
**Resolution:** NOT deductible. Gastos de representación (entertainment/representation) are blocked under Art. 148, fraction III of LISR. Remove entirely from deductions.

### EC7 -- Vehicle depreciation above cap [T2]
**Situation:** Client purchases a car for MXN $600,000 and claims 25% annual depreciation on full cost = MXN $150,000.
**Resolution:** Depreciation base is capped at approximately MXN $175,000. Annual deduction = 25% x $175,000 = $43,750. The excess is non-deductible. [T2] Flag for reviewer to confirm current year's automobile depreciation cap.

### EC8 -- School tuition for university [T1]
**Situation:** Client claims MXN $80,000 in university tuition as personal deduction.
**Resolution:** NOT deductible. The school tuition deduction (Art. 151 LISR, Decreto de colegiaturas) covers only preschool through bachillerato (pre-university). University tuition is NOT included in the allowable deduction.

### EC9 -- Pago provisional negative [T1]
**Situation:** Cumulative retenciones exceed cumulative ISR liability in month 6. Computed pago provisional is -MXN $3,000.
**Resolution:** No pago provisional is due. The negative amount cannot be requested as a refund mid-year. It carries forward as a credit against future monthly pagos. The full reconciliation occurs in the Declaración Anual.

### EC10 -- Loss carryforward [T2]
**Situation:** Client had a net fiscal loss (pérdida fiscal) of MXN $200,000 in 2024. In 2025, net profit before loss deduction is MXN $150,000.
**Resolution:** The 2024 loss may be carried forward for up to 10 years and applied against profits of subsequent years. Apply MXN $150,000 of the loss, reducing 2025 taxable base to $0. Remaining MXN $50,000 carries to 2026. The loss must be updated for inflation (actualización). [T2] Flag for reviewer to verify the inflation-adjusted loss amount.

---

## Step 10: Reviewer Escalation Protocol

When Claude identifies a [T2] situation:

```
REVIEWER FLAG
Tier: T2
Client: [name]
Situation: [description]
Issue: [what is ambiguous]
Options: [possible treatments]
Recommended: [most likely correct treatment and why]
Action Required: Licensed Contador Público must confirm before filing.
```

When Claude identifies a [T3] situation:

```
ESCALATION REQUIRED
Tier: T3
Client: [name]
Situation: [description]
Issue: [outside skill scope]
Action Required: Do not advise. Refer to licensed Contador Público. Document gap.
```

---

## Step 11: Test Suite

### Test 1 -- Standard freelance professional, general regime
**Input:** Single, RFC active, gross professional income MXN $600,000 (all from personas morales, retención 10% = MXN $60,000 withheld), deducciones autorizadas MXN $150,000, personal deductions MXN $40,000, pagos provisionales paid MXN $25,000.
**Expected output:** Utilidad fiscal = $600,000 - $150,000 = $450,000. Base gravable = $450,000 - $40,000 = $410,000. ISR = $59,965.52 + ($410,000 - $374,837.89) x 23.52% = $59,965.52 + $8,272.51 = $68,238.03. Credits: retenciones $60,000 + pagos provisionales $25,000 = $85,000. Saldo a favor = -$16,761.97 (refund).

### Test 2 -- Cash payment disqualified
**Input:** Client claims MXN $10,000 expense paid in cash. Valid CFDI exists.
**Expected output:** Deduction rejected. Payment exceeds MXN $2,000 cash limit. Remove from deducciones autorizadas.

### Test 3 -- Personal deduction cap binding
**Input:** Gross income MXN $300,000. Personal deductions claimed: medical $30,000, funeral $10,000, school tuition $14,200. Total = $54,200.
**Expected output:** Cap = 15% x $300,000 = $45,000 (less than 5 UMA = $206,367.60). Personal deductions capped at $45,000. Client must choose which $45,000 of the $54,200 to claim.

### Test 4 -- Retención only from personas morales
**Input:** Freelancer earns MXN $100,000 from a company (retención $10,000 withheld) and MXN $50,000 from an individual client (no retención).
**Expected output:** Total income = $150,000. Retención credit = $10,000 only. The $50,000 from the persona física has no withholding and must be fully covered by pagos provisionales.

### Test 5 -- Entertainment expense blocked
**Input:** Client deducts MXN $20,000 in client meals and entertainment with valid CFDIs.
**Expected output:** Remove $20,000 from deducciones autorizadas. Gastos de representación blocked under Art. 148 LISR. Not deductible regardless of CFDI.

### Test 6 -- Pago provisional computation
**Input:** January income MXN $80,000, January deductions MXN $20,000. No retenciones, no prior pagos.
**Expected output:** Taxable base = $60,000. Apply monthly tariff: falls in bracket $8,952.49 - $75,984.60 (monthly). Excedente = $60,000 - $8,952.49 = $51,047.51. ISR = $171.84 + ($51,047.51 x 6.40%) = $171.84 + $3,267.04 = $3,438.88. Less retenciones $0, less prior pagos $0. Pago provisional = $3,438.88.

---

## PROHIBITIONS

- NEVER allow deductions without a valid CFDI
- NEVER allow cash payments over MXN $2,000 as deductible expenses
- NEVER allow entertainment or representation expenses as deductions
- NEVER allow university tuition as a personal deduction
- NEVER apply the 10% ISR retención to payments from personas físicas -- retención only applies to payments from personas morales
- NEVER allow personal deductions above the 15% of income / 5 UMA cap
- NEVER compute RESICO tax in this skill -- flag for Contador and note the regime
- NEVER allow ISR itself as a deduction
- NEVER request mid-year refund for negative pago provisional -- credit carries forward
- NEVER advise on RESICO-to-general transitions, foreign income, or tax treaties without escalating to a Contador
- NEVER present tax calculations as definitive -- always label as estimated and direct client to a licensed Contador Público for confirmation

---

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a Contador Público Certificado or equivalent licensed practitioner in Mexico) before filing or acting upon.

The most up-to-date, verified version of this skill is maintained at [openaccountants.com](https://openaccountants.com). Log in to access the latest version, request a professional review from a licensed accountant, and track updates as tax law changes.
