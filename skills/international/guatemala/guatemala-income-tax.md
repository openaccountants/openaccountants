---
name: guatemala-income-tax
description: Use this skill whenever asked about Guatemala income tax (ISR — Impuesto Sobre la Renta) for employees and self-employed individuals. Trigger on phrases like "how much ISR do I pay", "renta del trabajo", "rentas de actividades lucrativas", "régimen opcional simplificado", "régimen sobre utilidades", "pequeño contribuyente", "SAT-1431", "planilla del IVA", "IGSS contributions", "deducción personal", "self-employed tax Guatemala", "ISR empleados", or any question about filing or computing ISR for an employee, sole proprietor, or professional in Guatemala. Also trigger when preparing or reviewing a SAT-1431 annual return, the monthly simplified-regime declaration, computing the Q48,000 personal deduction or the Q12,000 IVA credit, or advising on IGSS payroll contributions. This skill covers the employment-income brackets (5%/7%), the two self-employment regimes (5%/7% on gross vs 25% on profit), the Pequeño Contribuyente 5% regime, allowable deductions, IGSS social security, minimum wage, forms, deadlines, and penalties. ALWAYS read this skill before touching any Guatemala income tax work.
version: 0.1
jurisdiction: GT
tax_year: 2025
last_updated: 2026-07-13
review_status: pending_review
depends_on:
  - income-tax-workflow-base
category: international
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Guatemala Income Tax (ISR) — Employee & Self-Employed

## Section 1 — Quick Reference

**Quick Reference table**

| Field | Value |
| --- | --- |
| Country | Guatemala (República de Guatemala) |
| Tax | ISR — Impuesto Sobre la Renta (personal income tax) |
| Currency | Guatemalan Quetzal (GTQ / Q) only |
| Tax system | Territorial — only Guatemala-source income is taxed (Decreto 10-2012) |
| Tax year | Calendar year (1 January — 31 December) |
| Primary legislation | Ley de Actualización Tributaria, Decreto 10-2012 ("ISR Law") |
| Supporting legislation | Código Tributario (penalties); Decreto 78-89 (bonificación incentivo); Decreto 31-2024 (Pequeño Contribuyente limit) |
| Tax authority | SAT — Superintendencia de Administración Tributaria (portal.sat.gob.gt) |
| Social security authority | IGSS — Instituto Guatemalteco de Seguridad Social (igssgt.org) |
| Filing portal | SAT Agencia Virtual / Declaraguate |
| Employment annual return | SAT-1431, due 31 March (within 3 months of year-end) |
| Validated by | Pending — requires sign-off by a Guatemalan Contador Público y Auditor (CPA) |
| Validation date | Pending |
| Skill version | 0.1 |

> **Confidence note (Tier 2 / research-verified).** Core ISR rates, the Q48,000 / Q12,000 deductions, VAT 12%/5%, IGSS 4.83%/10.67%, the Pequeño Contribuyente Q465,381.25 limit, and the 2025/2026 minimum wages are confirmed from cited authoritative / Big-4 sources. Items marked **[RESEARCH GAP — reviewer to confirm]** were not confirmed from a primary/Big-4 source and MUST be verified against the SAT ISR Law or IGSS/Código Tributario text before any filing.

### 1.1 ISR — Employment Income (Renta del Trabajo en Relación de Dependencia)

**Employment income brackets**  _(Article 73, Decreto 10-2012 (PwC Guatemala — Taxes on personal income, reviewed 9 Jan 2026; Vesco Consultores — ISR empleados))_

| Annual taxable income (GTQ) | Marginal rate | Cumulative tax at top of band |
| --- | --- | --- |
| 0 — 300,000 | 5% | Q15,000 |
| Over 300,000 | Q15,000 fixed + 7% on excess | — |

- **Employment income ISR formula** — tax = 5% on the first Q300,000; income above Q300,000 pays Q15,000 + 7% of the excess.  _(Article 73, Decreto 10-2012)_

### 1.2 ISR — Self-Employment / Business / Professional Income (Rentas de Actividades Lucrativas)

Self-employed individuals and professionals choose ONE of two regimes (Decreto 10-2012):

**(a) Régimen Opcional Simplificado Sobre Ingresos** — tax on **gross income**, no expense deductions. Paid **monthly**. (Source: PwC; Grupo Macsol; inbers.com)

**Optional Simplified regime brackets**  _(PwC; Grupo Macsol; inbers.com)_

| Monthly gross income (GTQ) | Marginal rate | Cumulative tax at top of band |
| --- | --- | --- |
| 0 — 30,000 | 5% | Q1,500 |
| Over 30,000 | Q1,500 fixed + 7% on excess | — |

> **[RESEARCH GAP — reviewer to confirm]** The **Q30,000 monthly threshold** is reported consistently by Guatemalan advisory sources (Grupo Macsol, inbers) but was NOT confirmed directly from PwC/SAT. The 5%/7% rates and Q1,500 fixed amount mirror the statutory Article-44 structure of Decreto 10-2012. Verify the threshold against the SAT ISR Law text before publishing.

**(b) Régimen Sobre Utilidades de Actividades Lucrativas** — **25%** on net profit (income minus deductible costs/expenses). Quarterly payments; annual return due **31 March**. (Source: PwC; Concilia)

**Profit regime table**  _(Decreto 10-2012; Concilia)_

| Net profit | Rate |
| --- | --- |
| All net profit | 25% |

### 1.3 Pequeño Contribuyente (Small Taxpayer — IVA/ISR combined)

**Pequeño Contribuyente table**  _(Prensa Libre; inbers.com)_

| Item | Value |
| --- | --- |
| Rate | 5% of monthly gross income |
| Annual billing limit | Q465,381.25 (= 125 monthly non-agricultural minimum wages of Q3,723.05), Decreto 31-2024, effective 9 Apr 2025 |
| Invoicing | Must issue invoices for sales/services over Q50; keep only a Purchases & Sales book |
| Exceeding the limit | Must register in the General IVA Regime the following month (or SAT does so de oficio) |

### 1.4 VAT (IVA) — context for self-employed registration

**IVA rate table**

| Item | Value |
| --- | --- |
| Standard IVA rate | 12% ([PwC](https://taxsummaries.pwc.com/guatemala/individual/taxes-on-personal-income)) |
| Pequeño Contribuyente rate | 5% (see 1.3) |

### Conservative Defaults

**Conservative Defaults table**

| Ambiguity | Default |
| --- | --- |
| Unknown income type (employment vs self-employment) | STOP — do not apply a regime without knowing |
| Unknown self-employment regime | Optional Simplified (gross income, 5%/7%) — the SAT default if not elected otherwise |
| Unknown whether IVA credit (Planilla) was filed | Q0 IVA credit |
| Unknown business-use % (vehicle, phone, home) | 0% deduction |
| Unknown expense category | Not deductible |
| Personal deduction documentation | Q48,000 standard requires no docs; apply it. Anything above it must be supported |
| Unknown IGSS applicability | Assume employee in formal dependency = IGSS applies |

## Section 2 — Required Inputs and Refusal Catalogue

### Required Inputs

**Minimum viable** — bank statement for the full tax year in CSV, PDF, or pasted text, plus confirmation of income type (employee / self-employed) and, for self-employed, which regime applies (Optional Simplified, Profit, or Pequeño Contribuyente).

**Recommended** — payslips (recibo de salario) showing IGSS withholding and bonificación incentivo; sales invoices (facturas) and purchase receipts; Planilla del IVA confirmation; prior-year SAT-1431 or regime declarations; IGSS contribution records.

**Ideal** — complete income/expenditure account; asset register (Profit Regime); RetenISR projection from the employer; provisional/quarterly payment confirmations; any other Guatemala-source income.

**Refusal if minimum is missing — SOFT WARN.** No bank statement at all = hard stop. Bank statement without invoices = proceed with reviewer warning: "This computation was produced from bank statement alone. The reviewer must verify that income is correctly classified by regime, that the Q48,000 personal deduction and any IVA credit are properly supported, and that only Guatemala-source income is included."

### Refusal Catalogue

- **R-GT-1 — Income type unknown** — "ISR is split into separate categories. This skill cannot compute tax without knowing whether the client earns employment income (renta del trabajo) or self-employment/business income (rentas de actividades lucrativas). Please confirm before proceeding."  _(Section 2 — Refusal Catalogue)_
- **R-GT-2 — Companies / sociedades** — "This skill covers individual taxpayers (employees, sole proprietors, professionals) only. Sociedades anónimas and other entities file corporate ISR. Escalate to a Guatemalan CPA."  _(Section 2 — Refusal Catalogue)_
- **R-GT-3 — Foreign-source income** — "Guatemala uses a territorial system — only Guatemala-source income is taxed. Foreign-source income, expatriate, and double-taxation questions are out of scope. Escalate to a Guatemalan CPA."  _(Section 2 — Refusal Catalogue)_
- **R-GT-4 — Capital income / property disposals** — "Rentas de capital and capital-gains computations are a separate ISR category with different rates. Out of scope. Escalate to a Guatemalan CPA."  _(Section 2 — Refusal Catalogue)_
- **R-GT-5 — Arrears / SAT enforcement** — "Client has outstanding tax arrears or is subject to SAT enforcement. Mora accrues at 0.005 per day of the unpaid tax plus resarcitorio interest. Do not advise. Escalate to a Guatemalan CPA immediately."  _(Section 2 — Refusal Catalogue)_
- **R-GT-6 — IVA return requested** — "This skill covers income tax (ISR) only — except for the combined Pequeño Contribuyente 5%. For a standalone General Regime IVA return, escalate to a Guatemalan CPA or a dedicated IVA skill."  _(Section 2 — Refusal Catalogue)_

## Section 3 — Transaction Pattern Library

This is the deterministic pre-classifier. When a bank statement transaction matches a pattern below, apply the treatment directly. Do not second-guess. If none match, fall through to Tier 1 rules in Section 5.

**How to read this table.** Match by case-insensitive substring on the counterparty name or description as it appears in the bank statement (Spanish terms expected). If multiple patterns match, use the most specific. If none match, fall through to Tier 1 rules.

### 3.1 Income Patterns (Credits / Abonos)

**Income Patterns table**

| Pattern | Treatment | Notes |
| --- | --- | --- |
| SALARIO, SUELDO, NÓMINA, PLANILLA, [employer name] | Employment income (renta del trabajo) | Goes to the employment ISR computation, NOT self-employment |
| AGUINALDO | Employment income — exempt up to one month's salary | Excess over one month's salary is taxable |
| BONO 14, BONO CATORCE | Employment income — exempt up to one month's salary | Excess over one month's salary is taxable |
| BONIFICACIÓN INCENTIVO, BONIF INCENTIVO | Q250/month — NOT subject to ISR or IGSS | Decreto 78-89; exclude from ISR base and IGSS base |
| HONORARIOS, SERVICIOS PROFESIONALES, FACTURA | Self-employment gross income | Rentas de actividades lucrativas — apply elected regime |
| TRANSFERENCIA [client], PAGO [client], DEPÓSITO [client] | Self-employment gross income | Business income — match to facturas |
| STRIPE, PAYPAL, WISE, PAYONEER PAYOUT | Self-employment gross income | Platform payout — match to underlying invoices |
| UPWORK, FIVERR | Self-employment gross income | Freelance platform — net of platform commission |
| ALQUILER RECIBIDO, RENTA RECIBIDA | Rental / capital income | Separate ISR category — flag, out of standard scope (R-GT-4) |
| INTERESES, INTERÉS | Capital income | Separate ISR category — flag |
| DEVOLUCIÓN SAT, REINTEGRO ISR | EXCLUDE | Tax refund from a prior year |

### 3.2 Expense Patterns (Debits / Cargos) — Deductible only in the PROFIT regime (25%)

**Expense Patterns — Profit regime table**

| Pattern | Category | Treatment | Notes |
| --- | --- | --- | --- |
| ALQUILER OFICINA, RENTA LOCAL | Office rent | Deductible (Profit regime) | Dedicated business premises |
| CONTADOR, AUDITOR, HONORARIOS CONTABLES | Accountancy fees | Deductible (Profit regime) |  |
| ABOGADO, NOTARIO, LEGAL | Legal fees | Deductible (Profit regime) | Must be business-related |
| PAPELERÍA, ÚTILES, OFICINA | Office supplies | Deductible (Profit regime) |  |
| PUBLICIDAD, MARKETING, GOOGLE ADS, META ADS | Marketing/advertising | Deductible (Profit regime) |  |
| COMISIÓN BANCARIA, CARGO BANCARIO | Bank charges | Deductible (Profit regime) | Business account only |
| ENERGUATE, EEGSA, AGUA, INTERNET (business) | Utilities | Deductible (Profit regime), apportion if mixed | Business-use portion only |
| CLARO, TIGO, TELÉFONO | Telecoms | Deductible (Profit regime), business % only |  |

> Expenses are deductible ONLY under the Régimen Sobre Utilidades. Under the Optional Simplified or Pequeño Contribuyente regimes, tax is on **gross income** and these expenses give NO deduction.

### 3.3 Expense Patterns (Debits) — Deductions allowed in the EMPLOYMENT computation

**Employment deductions table**

| Pattern | Category | Treatment | Notes |
| --- | --- | --- | --- |
| IGSS, CUOTA LABORAL, SEGURO SOCIAL | IGSS employee contribution | Deductible from employment income | 4.83% of salary; fully deductible |
| SEGURO DE VIDA, PRIMA SEGURO VIDA | Life insurance premium | Deductible (non-dotal policies) | Employee's proportional portion |
| DONACIÓN [State/university/cultural] | Donation | Deductible — unlimited | To State / universities / cultural entities |
| DONACIÓN [nonprofit/foundation] | Donation | Deductible — capped at 5% of gross income | Nonprofits/foundations |
| IVA personal purchases (via Planilla) | IVA credit | Credit capped at Q12,000/year | Requires Planilla del IVA filed by 10 January |

### 3.4 Expense Patterns (Debits) — NOT Deductible

**Non-deductible expense patterns table**

| Pattern | Category | Treatment | Notes |
| --- | --- | --- | --- |
| RESTAURANTE, COMIDA, ENTRETENIMIENTO | Entertainment / personal meals | NOT deductible | Personal living costs |
| SUPERMERCADO, PAIZ, LA TORRE, DESPENSA, GROCERIES | Personal expenses | NOT deductible | Private living costs |
| MULTA, SANCIÓN | Fines/penalties | NOT deductible | Public policy |
| PAGO ISR, PAGO SAT, IMPUESTO | Tax payments | NOT deductible | Income tax cannot reduce income |
| RETIRO, CAJERO, ATM (personal) | Drawings | NOT deductible | Not an expense |

### 3.5 Exclusions (Neither Income nor Expense)

**Exclusions table**

| Pattern | Treatment | Notes |
| --- | --- | --- |
| TRANSFERENCIA PROPIA, ENTRE CUENTAS, CUENTA PROPIA | EXCLUDE | Own-account transfer |
| PRÉSTAMO, ABONO PRÉSTAMO, CRÉDITO | EXCLUDE | Loan principal movement |
| PAGO IVA, IVA SAT | EXCLUDE | IVA liability payment, not an ISR expense |
| ISR TRIMESTRAL, PAGO TRIMESTRAL | Credit against annual liability (Profit regime) | Quarterly ISR payment — not an expense |

### 3.6 Guatemalan Banks — Statement Format Reference

**Guatemalan Banks table**

| Bank | Common Patterns | Notes |
| --- | --- | --- |
| Banco Industrial (BI) | TRANSFERENCIA, ABONO, CARGO, COMISIÓN | PDF/CSV; date format DD/MM/YYYY |
| Banrural (Banco de Desarrollo Rural) | DEPÓSITO, RETIRO, TRANSF | PDF; widely used for payroll |
| BAC Credomatic | PAGO, TRANSFERENCIA, COMPRA | PDF/CSV; card transactions show merchant |
| G&T Continental | ABONO, CARGO, TRANSFERENCIA | PDF |
| Banco Promerica | TRANSFERENCIA, COMISIÓN | PDF/CSV |

## Section 4 — Worked Examples

### Example 1 — Employee, salary below the Q300,000 band

**Input lines (monthly, Banco Industrial):**
`28/02/2025 ; BI ABONO ; SALARIO FEBRERO ; EMPRESA XYZ S.A. ; +8,000.00 ; GTQ`
`28/02/2025 ; BI ABONO ; BONIFICACIÓN INCENTIVO ; ; +250.00 ; GTQ`

**Reasoning:**
Salary Q8,000/month = Q96,000/year of taxable employment income. The Q250/month bonificación incentivo (Q3,000/year) is exempt from ISR (Decreto 78-89) — exclude it. Apply the Q48,000 standard personal deduction. IGSS employee deduction = 4.83% of Q96,000 = Q4,636.80 (deductible). Assume no Planilla del IVA filed → Q0 IVA credit.

- Taxable employment income = Q96,000
- Less Q48,000 personal deduction − Q4,636.80 IGSS = base of Q96,000 − Q52,636.80 = **Q43,363.20**
- Base is within the 0–300,000 band → ISR = 5% × Q43,363.20 = **Q2,168.16**

**Classification:** Annual ISR ≈ Q2,168.16 (Article 73, 5% band). Bonificación incentivo excluded.

### Example 2 — Employee, salary above the Q300,000 band, with IVA credit

**Input:** Annual taxable salary Q420,000. IGSS withheld = 4.83% × Q420,000 = Q20,286. Planilla del IVA filed claiming the full Q12,000 IVA credit. Q48,000 personal deduction.

**Reasoning:**
- Net taxable base = Q420,000 − Q48,000 − Q20,286 = **Q351,714**
- This exceeds Q300,000. ISR = Q15,000 (fixed on first 300,000) + 7% × (Q351,714 − Q300,000)
- = Q15,000 + 7% × Q51,714 = Q15,000 + Q3,619.98 = **Q18,619.98**
- Less Q12,000 IVA credit → **net ISR = Q6,619.98**

**Classification:** ISR before credit Q18,619.98; after Q12,000 IVA credit, Q6,619.98 due.

### Example 3 — Self-employed, Optional Simplified Regime (5%/7% on gross), low month

**Input line:**
`15/03/2025 ; BAC PAGO ; HONORARIOS MARZO ; CLIENTE ABC ; +18,000.00 ; GTQ`

**Reasoning:**
Optional Simplified Regime taxes **gross income monthly**, no deductions. Monthly gross Q18,000 is within the 0–30,000 band → ISR = 5% × Q18,000 = **Q900**. Filed within the first 10 business days of April.

**Classification:** Monthly ISR = Q900 (5% band, gross income). No expenses deducted.

### Example 4 — Self-employed, Optional Simplified Regime, high month (above Q30,000)

**Input line:**
`30/04/2025 ; BI ABONO ; HONORARIOS ABRIL ; CLIENTE DEF ; +50,000.00 ; GTQ`

**Reasoning:**
Monthly gross Q50,000 exceeds the Q30,000 threshold. ISR = Q1,500 (fixed on first 30,000) + 7% × (Q50,000 − Q30,000) = Q1,500 + 7% × Q20,000 = Q1,500 + Q1,400 = **Q2,900**.

**Classification:** Monthly ISR = Q2,900. (Threshold flagged [RESEARCH GAP] — see Section 1.2.)

### Example 5 — Self-employed, Profit Regime (25% on net)

**Input:** Annual business income Q600,000; documented deductible costs/expenses Q360,000.

**Reasoning:**
Profit Regime: net profit = Q600,000 − Q360,000 = **Q240,000**. ISR = 25% × Q240,000 = **Q60,000**. Paid quarterly; annual SAT return due 31 March.

**Classification:** Annual ISR = Q60,000 (25% of net profit).

### Example 6 — Pequeño Contribuyente (5% flat)

**Input line:**
`20/05/2025 ; BANRURAL ABONO ; VENTA MAYO ; ; +25,000.00 ; GTQ`

**Reasoning:**
Pequeño Contribuyente pays a flat 5% of monthly gross, combining IVA and ISR. ISR/IVA = 5% × Q25,000 = **Q1,250**. Check the annual billing limit: if cumulative annual billing reaches Q465,381.25 the client must move to the General IVA Regime the following month (Decreto 31-2024).

**Classification:** Monthly combined tax = Q1,250.

### Example 7 — Bonificación incentivo (exclude from both ISR and IGSS)

**Input line:**
`30/06/2025 ; BI ABONO ; BONIFICACIÓN INCENTIVO JUNIO ; ; +250.00 ; GTQ`

**Reasoning:**
The Q250/month incentive bonus (Decreto 78-89) is not subject to ISR or IGSS. Exclude it from the ISR taxable base AND from the IGSS contribution base.

**Classification:** EXCLUDE from ISR base and IGSS base.

### 5.1 Territorial Principle

- **Territorial Principle** — Only Guatemala-source income is taxable. Foreign-source income is excluded. If any income is foreign-source or its source is unclear, flag for reviewer (R-GT-3).  _(Decreto 10-2012)_

### 5.2 Income Classification by Category

- **Income Classification by Category** — ISR is split into separate categories. Classify FIRST: - Renta del trabajo (employment in dependency) → brackets 5%/7%, Q15,000 pivot at Q300,000 (Article 73). - Rentas de actividades lucrativas (self-employment/business/professional) → elected regime (Optional Simplified or Profit). - Rentas de capital (rent, interest, dividends) → separate category, out of standard scope (R-GT-4).  _(Article 73)_

### 5.3 Employment Income — Deductions (Article 73 / Decreto 10-2012)

**Employment income deductions table**  _(Article 73 / Decreto 10-2012)_

| Deduction | Amount / cap | Source |
| --- | --- | --- |
| Standard personal deduction | Q48,000/year, no documentation | [Vesco Consultores](https://vescco.tax/blog/todo-sobre-el-isr-empleados-guatemala/) |
| IVA credit | VAT paid on personal purchases, capped Q12,000/year; requires Planilla del IVA filed by 10 January | [Vesco Consultores](https://vescco.tax/blog/todo-sobre-el-isr-empleados-guatemala/) |
| IGSS employee contributions | Fully deductible | [Vesco Consultores](https://vescco.tax/blog/todo-sobre-el-isr-empleados-guatemala/) |
| Life insurance premiums | Non-dotal policies, employee's proportional portion | [Vesco Consultores](https://vescco.tax/blog/todo-sobre-el-isr-empleados-guatemala/) |
| Donations | Unlimited to State/universities/cultural entities; capped at 5% of gross income for nonprofits/foundations | [Vesco Consultores](https://vescco.tax/blog/todo-sobre-el-isr-empleados-guatemala/) |

- **Exempt income** — Aguinaldo and Bono 14 are exempt up to one month's salary each. Bonificación incentivo (Q250/month, Decreto 78-89) is exempt from ISR entirely.  _(Decreto 78-89)_

### 5.4 Employment Income — Computation

- **Employment income computation steps** — 1. Sum gross taxable employment income for the year (exclude bonificación incentivo and the exempt portions of aguinaldo / Bono 14). 2. Subtract the Q48,000 personal deduction, IGSS contributions, life insurance, and donations within caps. 3. Apply the Article 73 brackets: 5% up to Q300,000; Q15,000 + 7% on the excess above Q300,000. 4. Subtract the IVA credit (max Q12,000) to get tax due.  _(Article 73)_

### 5.5 Self-Employment Regimes

**Self-Employment Regimes table**

| Regime | Base | Rate | Filing |
| --- | --- | --- | --- |
| Optional Simplified (Sobre Ingresos) | Gross income, monthly, no deductions | 5% up to Q30,000/month; Q1,500 + 7% on excess **[RESEARCH GAP — confirm threshold]** | Within first 10 business days of following month, electronically |
| Profit (Sobre Utilidades) | Net profit (income − deductible costs) | 25% | Quarterly + annual return due 31 March |

- **Election permanence** — Once elected, the regime applies for the year. Default to Optional Simplified if unknown.

### 5.6 Pequeño Contribuyente

- **Pequeño Contribuyente rule** — Flat 5% of monthly gross income, combines IVA + ISR. Annual billing limit Q465,381.25 (Decreto 31-2024, effective 9 Apr 2025). Must issue invoices for sales over Q50. If the limit is exceeded, register in the General IVA Regime the following month.  _(Decreto 31-2024)_

### 5.7 Non-Deductible Expenses

**Non-Deductible Expenses table**

| Expense | Reason |
| --- | --- |
| Personal living expenses (groceries, restaurants) | Not business-related |
| Fines and penalties | Public policy |
| ISR itself | Tax on income |
| Drawings / personal withdrawals | Not an expense |
| Any expense (Simplified / Pequeño Contribuyente regimes) | Those regimes tax gross income — no expense deductions at all |

### 5.8 VAT (IVA) Interaction

**VAT interaction table**

| Scenario | ISR treatment |
| --- | --- |
| Standard IVA 12% collected on sales (General Regime) | Not income — exclude from gross income |
| Pequeño Contribuyente 5% | Combined IVA+ISR — single 5% on gross |
| IVA paid on personal purchases (employee) | May be claimed as the Q12,000 IVA credit via Planilla del IVA |

## Section 6 — Tier 2 Catalogue (Reviewer Judgement Required)

### 6.1 Regime Election (Self-Employed)

- Choosing Optional Simplified (5%/7% gross) vs Profit (25% net) materially changes tax. Profit regime is usually better only when deductible expenses are high relative to revenue.
- **Flag for reviewer:** confirm which regime the client has actually elected with SAT, and whether a switch is advisable.

### 6.2 Home Office / Mixed-Use Expenses (Profit regime only)

- Only the business-use portion of rent, utilities, phone, internet is deductible.
- Must be a genuinely business-used space; mixed personal use must be apportioned reasonably and documented.

**Conservative default:** 0% deduction until reviewer confirms apportionment basis.

### 6.3 Motor Vehicle Business Use (Profit regime only)

- Only the business-use percentage of fuel, insurance, and maintenance is deductible.
- Requires a usage log distinguishing business vs personal.

**Conservative default:** 0% business use until a log is provided.

### 6.4 IVA Credit (Planilla del IVA)

- The Q12,000 IVA credit requires the Planilla del IVA to be filed by **10 January**. If not filed, the credit is lost for the year.
- **Flag for reviewer:** confirm the Planilla was filed and the VAT receipts support the claimed credit.

### 6.5 Aguinaldo / Bono 14 Exempt Portion

- Each is exempt up to one month's salary; any excess is taxable employment income.
- **Flag for reviewer:** confirm the one-month reference salary and compute the taxable excess if any.

### 6.6 Donations Cap

- Donations to nonprofits/foundations are capped at 5% of gross income; donations to State/universities/cultural entities are unlimited.
- **Flag for reviewer:** confirm donee category and recompute the cap.

## Section 7 — Excel Working Paper Template

```
GUATEMALA ISR — WORKING PAPER
Tax Year: 2025
Client: ___________________________
Income type: Employment / Self-employed
Self-employment regime: Optional Simplified / Profit / Pequeño Contribuyente
Currency: GTQ

=== A. EMPLOYMENT INCOME (Renta del Trabajo) ===
  A1. Gross taxable salary (exclude bonif. incentivo)   ___________
  A2. Less: exempt aguinaldo (up to 1 month)            ___________
  A3. Less: exempt Bono 14 (up to 1 month)              ___________
  A4. Taxable employment income (A1 - A2 - A3)          ___________
  A5. Less: Q48,000 personal deduction                 ___________
  A6. Less: IGSS employee contributions (4.83%)        ___________
  A7. Less: life insurance premiums                    ___________
  A8. Less: donations (within caps)                    ___________
  A9. Net taxable base (A4 - A5 - A6 - A7 - A8)        ___________
  A10. ISR per Article 73 (5% / Q15,000+7%)            ___________
  A11. Less: IVA credit (max Q12,000, Planilla filed)  ___________
  A12. ISR DUE (A10 - A11)                             ___________

=== B. SELF-EMPLOYMENT — OPTIONAL SIMPLIFIED (per month) ===
  B1. Monthly gross income                             ___________
  B2. Monthly ISR (5% to Q30,000; Q1,500+7% above)     ___________
       [RESEARCH GAP: confirm Q30,000 threshold]

=== C. SELF-EMPLOYMENT — PROFIT REGIME (annual) ===
  C1. Gross business income                            ___________
  C2. Less: deductible costs/expenses                  ___________
  C3. Net profit (C1 - C2)                             ___________
  C4. ISR (25% × C3)                                   ___________

=== D. PEQUEÑO CONTRIBUYENTE (per month) ===
  D1. Monthly gross income                             ___________
  D2. Combined IVA+ISR (5% × D1)                        ___________
  D3. Cumulative annual billing (limit Q465,381.25)    ___________

REVIEWER FLAGS:
  [ ] Income type and regime confirmed?
  [ ] Only Guatemala-source income included?
  [ ] Bonificación incentivo excluded from ISR & IGSS?
  [ ] Aguinaldo / Bono 14 exempt portion correct?
  [ ] Q48,000 deduction and IGSS applied (employment)?
  [ ] IVA credit supported by Planilla (filed by 10 Jan)?
  [ ] Optional-Simplified Q30,000 threshold verified?
  [ ] Pequeño Contribuyente limit not exceeded?
  [ ] No expenses deducted under gross-income regimes?
```

## Section 8 — Bank Statement Reading Guide

### Guatemalan Bank Statement Formats

**Bank Statement Formats table**

| Bank | Format | Key Fields | Notes |
| --- | --- | --- | --- |
| Banco Industrial (BI) | PDF, CSV | Fecha, Descripción, Débito (Cargo), Crédito (Abono), Saldo | Most common; description contains counterparty + reference |
| Banrural | PDF | Fecha, Concepto, Retiro, Depósito, Saldo | Widely used for payroll |
| BAC Credomatic | PDF, CSV | Fecha, Descripción, Monto, Saldo | Card transactions show merchant |
| G&T Continental | PDF | Fecha, Detalle, Cargo, Abono |  |
| Banco Promerica | PDF, CSV | Fecha, Descripción, Monto |  |

### Key Guatemalan Banking & Tax Terms

**Banking & Tax Terms table**

| Term | English | Classification Hint |
| --- | --- | --- |
| ABONO / DEPÓSITO | Credit / deposit | Potential income |
| CARGO / RETIRO | Debit / withdrawal | Potential expense |
| TRANSFERENCIA / TRANSF | Transfer | Check direction & whether own-account |
| SALARIO / SUELDO / NÓMINA | Salary / payroll | Employment income |
| HONORARIOS | Professional fees | Self-employment income |
| FACTURA | Invoice | Self-employment income source doc |
| BONIFICACIÓN INCENTIVO | Incentive bonus | Q250/month — exclude from ISR & IGSS |
| AGUINALDO / BONO 14 | Christmas / July bonus | Exempt up to one month's salary |
| IGSS / CUOTA LABORAL | Social security (employee) | Deductible (employment) |
| COMISIÓN | Bank charge | Deductible only in Profit regime |
| IVA | VAT | Not ISR income/expense (except Pequeño Contribuyente) |

## Section 9 — Onboarding Fallback

If the client provides a bank statement but cannot answer onboarding questions immediately:

1. Classify all transactions using the pattern library (Section 3).
2. Mark all Tier 2 items as "PENDING — reviewer must confirm".
3. Apply conservative defaults (Section 1).
4. Generate the working paper (Section 7) with clear flags.
5. Present the following questions to the client:

```
ONBOARDING QUESTIONS — GUATEMALA ISR
1. Income type: employee (renta del trabajo) or self-employed (actividades lucrativas)?
2. If self-employed, which regime: Optional Simplified (5%/7% on gross),
   Profit (25% on net), or Pequeño Contribuyente (5% flat)?
3. Is all income Guatemala-source? Any foreign income?
4. (Employee) Did you file the Planilla del IVA by 10 January to claim the IVA credit?
5. (Employee) Total IGSS withheld during the year?
6. (Employee) Any aguinaldo / Bono 14 above one month's salary?
7. Do you receive bonificación incentivo (Q250/month)?
8. (Profit regime) Do you have documented deductible costs/expenses?
9. (Pequeño Contribuyente) What was your total annual billing?
10. Any other Guatemala-source income (rent, interest, dividends)?
```

## Section 10 — Reference Material

### Key Legislation & Authority References

**Key Legislation & Authority References table**

| Topic | Reference | Source |
| --- | --- | --- |
| ISR law | Ley de Actualización Tributaria, Decreto 10-2012 | [PwC](https://taxsummaries.pwc.com/guatemala/individual/taxes-on-personal-income) |
| Employment brackets (5%/7%) | Decreto 10-2012, Article 73 | [PwC](https://taxsummaries.pwc.com/guatemala/individual/taxes-on-personal-income); [Vesco](https://vescco.tax/blog/todo-sobre-el-isr-empleados-guatemala/) |
| Optional Simplified regime | Decreto 10-2012, Art. 44 structure | [Grupo Macsol](https://grupomacsol.com/regimen-opcional-simplificado-sobre-ingresos-de-actividades-lucrativas/) |
| Profit regime (25%) | Decreto 10-2012 | [Concilia](https://concilia.com.gt/regimen-ingresos-vs-utilidades/) |
| Pequeño Contribuyente limit | Decreto 31-2024 (eff. 9 Apr 2025) | [Prensa Libre](https://www.prensalibre.com/economia/regimen-de-pequeno-contribuyente-en-guatemala-que-es-que-significa-ventajas-y-nuevo-limite-de-facturacion-en-2025/) |
| Bonificación incentivo | Decreto 78-89 | [Guatemala.com](https://www.guatemala.com/noticias/sociedad/salario-minimo-2025-en-guatemala.html) |
| Penalties | Código Tributario, Art. 92 et al. | [inbers.com](https://inbers.com/multas-sat/) |

### IGSS Social Security Contributions

**IGSS contributions table**  _(PwC — Other taxes; Banco Industrial — IGSS 2026)_

| Party | Rate |
| --- | --- |
| Employee (cuota laboral) | 4.83% |
| Employer (cuota patronal) | 10.67% |
| **TOTAL IGSS** | **15.50%** |

Total = **15.5%** of monthly salary (excluding bonificación incentivo). Rates in effect since September 2022 (IGSS acuerdo reforms); unchanged for 2025/2026. (Source: PwC — Other taxes; Banco Industrial — IGSS 2026)

**Arithmetic check:** 4.83% + 10.67% = 15.50%. ✓

**Additional mandatory employer payroll charges table**

| Charge | Rate | Source |
| --- | --- | --- |
| IRTRA | 1% of payroll | [Remote People](https://remotepeople.com/countries/guatemala/hire-employees/payroll-tax/) |
| INTECAP | 1% of payroll | [Rivermate](https://www.rivermate.com/guides/guatemala/taxes) |
| IGSS employer | 10.67% | (above) |
| **Total employer payroll burden** | **12.67%** |  |

**Arithmetic check:** 10.67% + 1% + 1% = 12.67%. ✓

> **[RESEARCH GAP — reviewer to confirm]** The IGSS **program-level breakdown** (Enfermedad y Maternidad / Accidentes / IVS split within the 4.83% and 10.67% totals) is reported inconsistently across secondary sources; the totals are confirmed but the per-program allocation is not. Verify against IGSS Acuerdo 1118/1123 before publishing. No IGSS earnings **ceiling** was found from an authoritative source — treat as "no ceiling" unless SAT/IGSS confirms otherwise.

### Minimum Wage (Salario Mínimo)

**2025** — Governmental Agreement **264-2024**, effective 1 Jan 2025 ([Guatemala.com](https://www.guatemala.com/noticias/sociedad/salario-minimo-2025-en-guatemala.html); [ONSEC PDF](https://www.onsec.gob.gt/w1/wp-content/uploads/2025/01/SALARIOS-MINIMOS-PARA-LAS-ACTIVIDADES-ECONOMICAS-POR-CIRCUNSCRIPCION-ECONOMICA.pdf)):

**2025 Minimum Wage table**  _(Governmental Agreement 264-2024, effective 1 Jan 2025; Guatemala.com; ONSEC PDF)_

| Circunscripción | Activity | Daily (Q) | Monthly (Q) |
| --- | --- | --- | --- |
| CE1 (Dept. of Guatemala) | Non-agricultural | 122.40 | 3,723.05 |
| CE1 | Export/Maquila | 107.79 | 3,278.59 |
| CE2 (rest of country) | Non-agricultural | 116.73 | 3,550.60 |
| CE2 | Export/Maquila | 101.83 | 3,097.21 |

**2026** — Governmental Agreement **256-2025**, effective 1 Jan 2026 ([AGN](https://agn.gt/asi-quedan-los-montos-del-salario-minimo-para-el-2026/)):

**2026 Minimum Wage table**  _(Governmental Agreement 256-2025, effective 1 Jan 2026; AGN)_

| Circunscripción | Activity | Daily (Q) | Monthly (Q) |
| --- | --- | --- | --- |
| C1 (Guatemala Dept.) | Agricultural | 124.64 | 3,791.20 |
| C1 | Non-agricultural | 131.58 | 4,002.28 |
| C1 | Export/Maquila | 112.10 | 3,409.73 |
| C2 (other depts.) | Agricultural | 119.21 | 3,625.89 |
| C2 | Non-agricultural | 125.49 | 3,816.90 |
| C2 | Export/Maquila | 105.90 | 3,321.10 |

**Bonificación incentivo: Q250.00/month** (Decreto 78-89), paid on top of the minimum wage; not subject to IGSS or ISR.

### Filing, Forms & Deadlines

**Filing, Forms & Deadlines table**

| Item | Form | Deadline | Source |
| --- | --- | --- | --- |
| Employment income annual return | SAT-1431 | 31 March (within 3 months of year-end) | [Vesco](https://vescco.tax/blog/todo-sobre-el-isr-empleados-guatemala/) |
| Planilla del IVA (to claim Q12,000 IVA credit) | Planilla IVA | 10 January | [Vesco](https://vescco.tax/blog/todo-sobre-el-isr-empleados-guatemala/) |
| Optional Simplified regime declaration | Monthly (electronic) | First 10 business days of following month | [PwC](https://taxsummaries.pwc.com/guatemala/individual/taxes-on-personal-income) |
| Pequeño Contribuyente | Monthly | First 10 business days of following month | [PwC](https://taxsummaries.pwc.com/guatemala/individual/taxes-on-personal-income) |
| Profit Regime | Annual + quarterly | 31 March (annual) | [PwC](https://taxsummaries.pwc.com/guatemala/individual/taxes-on-personal-income) |

Filing platform: SAT **Agencia Virtual** / **Declaraguate**.

### Penalties (Código Tributario)

**Penalties table**

| Penalty | Detail | Source |
| --- | --- | --- |
| Mora (late payment) | Tax × 0.005 per day of delay (Art. 92) | [inbers.com](https://inbers.com/multas-sat/) |
| Late monthly declaration | Q150 fine per overdue month (even zero-value returns) | [inbers.com](https://inbers.com/multas-sat/) |
| Resarcitorio interest | Accrues on unpaid tax; rate set periodically by SAT (~Art. 58–59) **[RESEARCH GAP — confirm rate]** | [Prensa Libre](https://www.prensalibre.com/economia/que-pasa-si-no-se-paga-impuestos-en-guatemala-y-cuales-son-las-sanciones-multas-y-consecuencias/) |
| Voluntary disclosure reduction | Up to 85% reduction if self-reported before SAT audit | [SAT PDF](https://portal.sat.gob.gt/portal/descarga/1817/orientacion-legal-y-derechos-de-contribuyentes/11586/reduccion-de-sanciones-tributarias-en-el-codigo-tributario-guatemalteco.pdf) |
| Omisión de pago | Commonly cited at 100% of omitted tax **[RESEARCH GAP — confirm % against Código Tributario]** | unconfirmed |

### Test Suite

**Test 1 — Employee below the Q300,000 band.**
Input: Annual taxable salary Q96,000; IGSS 4.83% = Q4,636.80; Q48,000 personal deduction; no IVA credit; bonificación incentivo excluded.
Expected: base = Q96,000 − Q48,000 − Q4,636.80 = Q43,363.20. ISR = 5% × Q43,363.20 = **Q2,168.16**.

**Test 2 — Employee above the Q300,000 band with IVA credit.**
Input: Annual taxable salary Q420,000; IGSS Q20,286; Q48,000 deduction; Q12,000 IVA credit.
Expected: base = Q351,714. ISR = Q15,000 + 7% × Q51,714 = Q18,619.98. Less Q12,000 = **Q6,619.98 due**.

**Test 3 — Optional Simplified, low month.**
Input: Monthly gross Q18,000.
Expected: ISR = 5% × Q18,000 = **Q900**.

**Test 4 — Optional Simplified, high month.**
Input: Monthly gross Q50,000.
Expected: ISR = Q1,500 + 7% × Q20,000 = **Q2,900**. (Threshold Q30,000 [RESEARCH GAP].)

**Test 5 — Profit Regime.**
Input: Gross Q600,000; deductible expenses Q360,000.
Expected: net Q240,000. ISR = 25% × Q240,000 = **Q60,000**.

**Test 6 — Pequeño Contribuyente.**
Input: Monthly gross Q25,000.
Expected: combined IVA+ISR = 5% × Q25,000 = **Q1,250**. Check annual billing vs Q465,381.25 limit.

**Test 7 — Bonificación incentivo.**
Input: Q250/month incentive bonus included in the bank feed.
Expected: EXCLUDE from both ISR base and IGSS base (Decreto 78-89).

**Test 8 — Wrong regime, expenses claimed.**
Input: Optional Simplified client tries to deduct Q40,000 of office expenses.
Expected: Reject — gross-income regimes allow NO expense deductions. Tax stays on gross.

## PROHIBITIONS

- NEVER apply a regime without first confirming income type (employment vs self-employment)
- NEVER deduct business expenses under the Optional Simplified or Pequeño Contribuyente regimes — those tax gross income
- NEVER include bonificación incentivo in the ISR base or the IGSS base
- NEVER tax foreign-source income — Guatemala is territorial
- NEVER claim the Q12,000 IVA credit without confirming the Planilla del IVA was filed by 10 January
- NEVER exceed the Q48,000 personal deduction without supporting documentation
- NEVER allow ISR itself, fines, or personal drawings as deductions
- NEVER treat the Q30,000 Optional-Simplified threshold as confirmed — it is a [RESEARCH GAP]
- NEVER apply an IGSS ceiling — none was confirmed; treat contributions as uncapped pending review
- NEVER present tax calculations as definitive — always label as estimated and flag [RESEARCH GAP] items

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a CPA, EA, tax attorney, or equivalent licensed practitioner in your jurisdiction) before filing or acting upon.

The most up-to-date, verified version of this skill is maintained at [openaccountants.com](https://openaccountants.com). Log in to access the latest version, request a professional review from a licensed accountant, and track updates as tax law changes.

<!-- openaccountants-cta-block -->

---

## Talk to a verified accountant

This guide is maintained by the OpenAccountants network — accountants who put
their name behind the tax answers AI gives people. The live, always-current
version (and the professional behind it) is at
[openaccountants.com](https://www.openaccountants.com).

- Use it in your AI: https://www.openaccountants.com/connect
- Meet the accountants: https://www.openaccountants.com/network

> **General reference only.** This document does not constitute tax, legal, or
> financial advice. Verify figures against the cited primary sources or with a
> licensed professional before relying on them.
