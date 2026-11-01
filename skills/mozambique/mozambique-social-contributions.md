---
name: mozambique-social-contributions
description: Use this skill whenever asked about Mozambique social security contributions (INSS), payroll, or personal income tax (IRPS) for employees, employers, or self-employed individuals. Trigger on phrases like "how much INSS do I pay", "Mozambique social security", "INSS employer rate", "INSS employee 3%", "Segurança Social", "Instituto Nacional de Segurança Social", "Mozambique payroll tax", "IRPS calculation", "Mozambique income tax brackets", "PAYE Mozambique", "salário mínimo", "Mozambican minimum wage", or any question about Mozambique payroll or social-contribution obligations. Also trigger when classifying bank statement transactions that relate to INSS debits, IRPS/PAYE remittances, or salary payments from Mozambican banks (BCI, Millennium BIM, Standard Bank Moçambique, Absa Moçambique). This skill covers the 4% employer / 3% employee INSS rates, contribution base, registration and payment deadlines, IRPS resident brackets and PAYE, non-resident flat withholding, minimum wages by sector, bank statement classification patterns, and edge cases. ALWAYS read this skill before touching any Mozambique payroll or social-contribution work.
version: 0.2
jurisdiction: MZ
tax_year: 2026
last_updated: 2026-11-01
review_status: pending_review
trust_label: Built by Michael Cutajar and the OpenAccountants team
depends_on:
  - social-contributions-workflow-base
category: international
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Mozambique Social Security (INSS) and Payroll Tax v0.2

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

Tax year 2026 (calendar year). The governing 2026 texts could not be read: Boletim da Republica I Serie n.o 248 of 29 Dec 2025 (Leis 9/2025 ISPC, 10/2025 IVA, 11/2025 IRPS, 12/2025 IRPC) is listed on the AT site, at.gov.mz and inss.gov.mz refused both direct fetch and a real browser on 2026-11-01, and the gazette files have no archive copy. Every row below that rests on an older text says so.

## Who this applies to

Employers and employees in the obligatory social security system (Lei 4/2007; Regulamento, Decreto 51/2017, amended by Decreto 56/2024), and self-employed members. Contributions run from the first day of the contract to the day paid work ends (RSSO art. 14).

## Rates, bands and thresholds

| Item | Amount | Tax year | Official source |
|---|---|---|---|
| INSS employee rate | unverified, old skill 3% | no official page with the rate opened | unverified |
| INSS employer rate | unverified, old skill 4% | same | unverified |
| Contribution payment window | 20th of the reference month to the 10th of the next (RSSO art. 14) | in force on read copy | https://web.archive.org/web/20260411210933/https://www.inss.gov.mz/wp-content/uploads/2024/04/Decreto-51-2017-de-9-de-Outubro-Regulamento-da-Seguranca-Social-Obrigatoria.pdf |
| Default interest | 2% per month or part month (RSSO, Juros de mora) | same | same |
| Late declaration or payment fine | 1 to 3 minimum wages, times workers on the declaration | same | https://web.archive.org/web/20260308011042/https://www.inss.gov.mz/duvidas/ |
| Late worker registration fine | 1 to 5 minimum wages | same | same |


## The base

Contribution = rate x remuneration in the base (RSSO art. 14). RSSO art. 15 sets no percentage; the rate sits in a separate diploma not opened. Whether the meal subsidy is outside the base, and whether a ceiling exists, is unconfirmed.

### Payment pattern library
> Kept from the old skill. Any rate, floor, base rule or reform point in this section is unverified until the texts under "Not yet confirmed:" are read. Do not apply it as a current figure.

Deterministic pre-classifier for Mozambican bank statement transactions. Match by case-insensitive substring on the counterparty/reference. INSS and IRPS payments always EXCLUDE from any VAT return or revenue/expense classification -- they are statutory payroll obligations, not business supplies. (Portuguese is the official language; references appear in Portuguese.)

#### 3.1 INSS social-security debits

**INSS social-security debit patterns**

| Pattern | Treatment | Notes |
| --- | --- | --- |
| INSS, I.N.S.S. | EXCLUDE -- INSS contribution | Monthly 7% (4% employer + 3% employee) remittance |
| SEGURANCA SOCIAL, SEGURANÇA SOCIAL | EXCLUDE -- INSS contribution | Portuguese-language reference |
| INST NACIONAL SEGURANCA SOCIAL | EXCLUDE -- INSS contribution | Full authority name |
| CONTRIBUICAO INSS, CONTRIBUIÇÃO INSS | EXCLUDE -- INSS contribution | Explicit contribution reference |

#### 3.2 IRPS / PAYE tax remittances (NOT INSS -- do not confuse)

**IRPS/PAYE tax remittance patterns**

| Pattern | Treatment | Notes |
| --- | --- | --- |
| IRPS | EXCLUDE -- income tax (PAYE), not INSS | Withheld employee income tax remitted to AT |
| AUTORIDADE TRIBUTARIA, AT MOCAMBIQUE | EXCLUDE -- tax payment | AT remittance, not social security |
| EDECLARACAO, eDeclaração | EXCLUDE -- tax filing/payment | AT income-tax platform |
| IRPC | EXCLUDE -- corporate income tax | Company-level, not payroll INSS |
| IVA, VAT | EXCLUDE -- value added tax (16%) | Not INSS |

#### 3.3 Salary and payroll (exclude from INSS classification)

**Salary and payroll patterns**

| Pattern | Treatment | Notes |
| --- | --- | --- |
| SALARIO, SALÁRIO, ORDENADO (outgoing) | EXCLUDE -- payroll expense | Gross wage payment, not the INSS remittance |
| VENCIMENTO, PAGAMENTO SALARIAL (outgoing) | EXCLUDE -- payroll expense | Same |
| SALARIO, ORDENADO (incoming) | EXCLUDE -- employment income received | Not an INSS payment |

#### 3.4 Mozambican banks -- typical debit descriptions

**Mozambican banks typical debit descriptions**

| Bank | Typical description | Treatment |
| --- | --- | --- |
| BCI (Banco Comercial e de Investimentos) | "INSS" or "SEGURANCA SOCIAL" | EXCLUDE -- INSS |
| Millennium BIM | "INSS CONTRIB" or "SEGURANÇA SOCIAL" | EXCLUDE -- INSS |
| Standard Bank Moçambique | "INSS" or "INST NAC SEG SOCIAL" | EXCLUDE -- INSS |
| Absa Moçambique | "INSS" or "CONTRIBUICAO SOCIAL" | EXCLUDE -- INSS |

### Tier 2 catalogue
Flag these for reviewer confirmation when data is ambiguous.

#### T2-1 -- Pay-component classification ambiguity

- **T2-1** , Trigger: A pay item (e.g. a commission or allowance) may or may not be "regular/consistent" enough to enter the INSS base. Issue: Only regular, consistent allowances/commissions are in-base; irregular ones are out. The boundary is judgemental. Action: Flag for reviewer with the payment history.

#### T2-2 -- Foreign employee with home-country scheme

- **T2-2** , Trigger: Foreign employee asserts a comparable home-country contribution. Issue: Exemption is by application only and depends on the comparability of the foreign scheme. Action: Flag for reviewer; do not exclude INSS without confirmation.

#### T2-3 -- Law 11/2025 residency reclassification

- **T2-3** , Trigger: Worker's residency status is unclear post-29 Dec 2025. Issue: secondary commentary, unread law: Law 11/2025 removed the 180-day test and broadened residency to main residence, professional activity, centre of economic interests, Mozambican vessel/aircraft crew, and nationals on foreign assignment not fully taxed abroad. Action: Flag for reviewer to determine resident vs non-resident treatment.

#### T2-4 -- Digital-service / e-money agent income

- **T2-4** , Trigger: Worker earns digital-service income or electronic-money agent commissions. Issue: secondary commentary, unread law: these are subject to a final 10% withholding -- different from standard PAYE. Action: Flag for reviewer.

#### T2-5 -- Capital gains (autonomous regime)

- **T2-5** , Trigger: Individual realises capital gains. Issue: secondary commentary, unread law: Law 11/2025 added an autonomous capital-gains regime (Art. 54-A) using the same 10%--32% schedule; such income is no longer aggregated. Action: Flag for reviewer; do not aggregate into employment IRPS.

#### T2-6 -- INSS arrears / penalties

- **T2-6** , Trigger: Unpaid INSS from prior periods. Issue: Monthly late-payment interest and administrative fines apply; exact rates not stated in authoritative sources [RESEARCH GAP]. Action: Do not quantify without an INSS statement. Escalate.

#### T2-7 -- Minimum-wage breach

- **T2-7** , Trigger: Basic wage appears below the sector minimum (figures unverified). Issue: Minimum wages are sector-specific (Decrees 87/2025--94/2025). 2026 figures not sourced. Action: Flag for reviewer; payroll must comply before INSS computation.

### Excel working paper template
> Kept from the old skill. Any rate, floor, base rule or reform point in this section is unverified until the texts under "Not yet confirmed:" are read. Do not apply it as a current figure.

MOZAMBIQUE PAYROLL / INSS COMPUTATION -- WORKING PAPER
Client: [name]               NUIT: [____]
Tax Year: [year]             Prepared: [date]

INPUT DATA
  Worker status:                 [Employee / Self-employed]
  Residency (IRPS):              [Resident / Non-resident]
  Sector (minimum-wage check):   [____]
  Gross monthly remuneration:    MZN [____]
  Meal subsidy (EXCLUDED):       MZN [____]
  One-off bonuses (EXCLUDED):    MZN [____]
  Reimbursements (EXCLUDED):     MZN [____]
  INSS contribution base:        MZN [____]

INSS COMPUTATION (monthly)
  Employee 3%:                   MZN [____]
  Employer 4%:                   MZN [____]
  Total 7% remitted:             MZN [____]
  Payment due (10th of next mo): [____]

IRPS COMPUTATION (annual, residents)
  Annual taxable income:         MZN [____]
  Less employee INSS deduction:  MZN [____]
  Adjusted taxable income:       MZN [____]
  Marginal rate:                 [10/15/20/25/32]%
  Parcela a abater:              MZN [____]
  IRPS = income x rate - parcela:MZN [____]
  (Non-resident: 20% flat)       MZN [____]

REVIEWER FLAGS
  [List any Tier 2 flags here]

RESEARCH GAPS APPLIED
  [List any [RESEARCH GAP] items relied upon]

### Bank statement reading guide
> Kept from the old skill. Any rate, floor, base rule or reform point in this section is unverified until the texts under "Not yet confirmed:" are read. Do not apply it as a current figure.

#### How INSS and tax debits appear on Mozambican statements

**BCI (Banco Comercial e de Investimentos):**
- Description: "INSS" or "SEGURANCA SOCIAL"
- Timing: monthly, in the 20th-to-10th window (deadline 10th of following month)
- Amount: 7% of the monthly contribution base

**Millennium BIM:**
- Description: "INSS CONTRIB" or "SEGURANÇA SOCIAL"
- Timing: same monthly cycle

**Standard Bank Moçambique / Absa Moçambique:**
- Description: "INSS" / "INST NAC SEG SOCIAL" / "CONTRIBUICAO SOCIAL"
- Timing: same monthly cycle

**Key identification tips:**
1. INSS debits are outgoing (DEBITO), monthly, and equal 7% of the contribution base.
2. Do NOT confuse with AT/IRPS debits (income tax, due 20th of following month) or IRPC (corporate) or IVA (16% VAT).
3. Salary debits ("SALARIO", "VENCIMENTO", "ORDENADO") are net wages, not the INSS remittance.
4. References are typically in Portuguese.
5. The INSS figure should reconcile to 0.07 x base; the employee share alone is 0.03 x base.

### Onboarding fallback
> Kept from the old skill. Any rate, floor, base rule or reform point in this section is unverified until the texts under "Not yet confirmed:" are read. Do not apply it as a current figure.

If the client provides only a bank statement and no other information:

1. **Scan for INSS debits** -- identify outgoing payments matching the patterns above.
2. **Reverse-engineer the base** -- INSS / 0.07 = contribution base (e.g. 2,100.00 / 0.07 = 30,000.00).
3. **Separate tax from social security** -- AT/IRPS debits are income tax, not INSS; IRPC/IVA are company-level.
4. **Flag for reviewer:** "INSS and IRPS figures derived from bank statement amounts only. Contribution base composition, residency, and sector minimum wage have not been independently verified. Reviewer must confirm before filing."

## Deadlines and filing

Worker registration: within 30 days of the contract start. Declaration and payment: 20th of the reference month to the 10th of the next, on SISSMO or M-Contribuicao, using the payment guide the platform generates. Advance payment is not possible. The 13th month goes in the declaration of the month it is received. In SISSMO: open Elaborar Declaracao, use Referencia para Copia, pick the last month, Criar declaracao, amend, add new workers with +. A filed declaration cannot be topped up; cancel it if its guide is unpaid (INSS Duvidas).

## Penalties and interest

Withholding contributions and not paying them over is criminal abuse of trust; refusing to show documents is disobedience (INSS Duvidas, https://web.archive.org/web/20260308011042/https://www.inss.gov.mz/duvidas/). Fines and 2% default interest as in the table.

## Cross-border points

Foreign-employee exemption on request: old skill, unverified. Totalisation agreements are out of scope.

## Two worked examples that recompute

**Late interest.** MZN 3,500 of contributions two months late bears MZN 140.

```oa-check
name: Late interest two months
inputs:
  due: 3500
  months: 2
steps:
  - interest: due * 0.02 * months
expected:
  interest: 140.00
```

**Decision: pay now or wait a third month.** One more month costs a further MZN 70 of interest, plus exposure to the fine.

```oa-check
name: Extra month of interest
inputs:
  due: 3500
steps:
  - two: due * 0.02 * 2
  - three: due * 0.02 * 3
  - extra: three - two
expected:
  extra: 70.00
```


## Ask the client first

- Employee or self-employed.
- Pay items in the month.
- Foreign worker with a home scheme.
- Sector, for the minimum wage used in fines.
- Registration date and any arrears.

## Sources

| Source | URL | Read on |
|---|---|---|
| Decreto 51/2017, RSSO, on inss.gov.mz (archive copy of 11 Apr 2026; arts. 14, 15, penalties and default interest read) | https://web.archive.org/web/20260411210933/https://www.inss.gov.mz/wp-content/uploads/2024/04/Decreto-51-2017-de-9-de-Outubro-Regulamento-da-Seguranca-Social-Obrigatoria.pdf | 2026-11-01 |
| INSS, Duvidas (archive copy of 8 Mar 2026; whole page read) | https://web.archive.org/web/20260308011042/https://www.inss.gov.mz/duvidas/ | 2026-11-01 |
| AT, Legislacao Fiscal list naming BR 248 supplements (archive copy of 20 Feb 2026; list read, the gazette files were not archived) | https://web.archive.org/web/20260220064207/https://www.at.gov.mz/por/Legislacao/Legislacao-Fiscal/Leis | 2026-11-01 |

Not yet confirmed: INSS rates 3% and 4% and 7% total; meal subsidy exclusion; absence of floor or ceiling; foreign-employee exemption; IRPS deductibility of the employee share; sector minimum wages from July 2025; 2026 changes to any of these; IRPS figures here, which belong to mozambique-income-tax.

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. All outputs must be reviewed and signed off by a qualified professional before filing or acting upon.

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
