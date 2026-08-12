---
name: iceland-social-contributions
description: Use this skill whenever asked about Iceland (Ísland) social security contributions, payroll levies, and mandatory pension for employers, employees, and self-employed individuals. Trigger on phrases like "how much social security do I pay in Iceland", "tryggingagjald", "social security contribution Iceland", "payroll tax Iceland", "lífeyrissjóður", "mandatory pension fund", "occupational pension contribution", "4% employee pension", "11.5% employer pension", "séreignarsparnaður", "additional voluntary pension", "A1 certificate Iceland", "fishermen social security", "staðgreiðsla withholding", "self-employed pension reiknað endurgjald", or any question about Icelandic social/payroll contribution obligations. Also trigger when classifying bank statement transactions for tryggingagjald remittances, pension fund (lífeyrissjóður) debits, or Skatturinn withholding payments from Landsbankinn, Íslandsbanki, Arion banki, or other Icelandic banks. This skill covers the 6.35% general payroll levy (tryggingagjald), fishermen and A1 reduced rates, the 15.5% mandatory occupational pension split (4% employee / 11.5% employer), voluntary pension, self-employed contributions, employer pension tax-free caps, the monthly PAYE/staðgreiðsla remittance cycle, bank statement classification, and edge cases. ALWAYS read this skill before touching any Icelandic social contribution work.
version: 0.1
jurisdiction: IS
tax_year: 2025
last_updated: 2026-07-13
review_status: pending_review
depends_on: - social-contributions-workflow-base
category: international
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Iceland Social Security Contributions and Mandatory Pension

## Iceland Social Security Contributions and Mandatory Pension -- Skill v0.1

Tier 2 (research-verified) skill. Figures are drawn from Skatturinn (Iceland Revenue and Customs) official Key Rates 2025 and 2026 pages, KPMG Icelandic Tax Facts 2025, PwC Worldwide Tax Summaries, and the Central Bank of Iceland. This skill has NOT yet been signed off by an Icelandic licensed accountant/tax adviser. All outputs require professional review before filing. Items marked [RESEARCH GAP — reviewer to confirm] were not pinned to an authoritative English-language source in research and must be verified.

## Section 1 -- Quick reference

**Quick reference field table**

| Field | Value |
| --- | --- |
| Country | Iceland (Ísland / Republic of Iceland) |
| Primary legislation | Act No. 113/1990 on Social Security Contribution (Lög nr. 113/1990 um tryggingagjald) |
| Supporting legislation | Act No. 129/1997 on Mandatory Pension Insurance and Pension Funds; Act No. 45/1987 on Withholding of Public Levies (PAYE / staðgreiðsla); Act No. 90/2003 on Income Tax; Act No. 50/1988 on VAT |
| Tax / levy authority | Skatturinn — Iceland Revenue and Customs (Ríkisskattstjóri) |
| Pension supervision | Central Bank of Iceland (Fjármálaeftirlitið) — pension fund oversight |
| Benefits administration | Tryggingastofnun (Social Insurance Admin.) and Vinnumálastofnun (Directorate of Labour) |
| General payroll levy (tryggingagjald) | 6.35% of total gross remuneration, employer-paid, NO ceiling (2025 & 2026 unchanged) (Skatturinn Key Rates 2025/2026; KPMG sec 4.2) |
| Fishermen/seamen levy | 7.00% (6.35% + 0.65% surcharge) (KPMG sec 4.2) |
| A1-certificate (EU/EEA) reduced levy | 0.425% (KPMG sec 4.2 & fn 6) |
| Mandatory pension — employee | 4% of total wages (deductible from income-tax base) (PwC; KPMG sec 4.2/13.1) |
| Mandatory pension — employer | 11.5% of total wages (minimum) (PwC; KPMG fn 7) |
| Mandatory pension — total minimum | 15.5% (4% + 11.5%) (PwC; Central Bank of Iceland) |
| Pension age range | Ages 16–70 (mandatory obligation) (PwC; Central Bank of Iceland) |
| Self-employed | Pays tryggingagjald 6.35% AND full pension 15.5% on reckoned remuneration (KPMG sec 13.1 fn 31 & 4.2) |
| Remittance cycle | Monthly PAYE/staðgreiðsla; due by the 15th of the following month (PwC tax admin; Skatturinn) |
| Currency | ISK only (Icelandic króna) |
| Validated by | Pending — requires sign-off by an Icelandic licensed accountant/tax adviser |
| Validation date | Pending |
| Skill version | 0.1 |

**Contribution overview (per ISK 100 of gross wages, general case)**

| Contributor | Item | Rate | Notes |
| --- | --- | --- | --- |
| Employer | Tryggingagjald (payroll levy) | 6.35% | On total gross remuneration, no ceiling |
| Employer | Mandatory pension | 11.5% | Minimum statutory |
| **Employer total** |  | **17.85%** | 6.35% + 11.5% |
| Employee | Mandatory pension | 4.00% | Deductible from income-tax base |
| **Employee total** |  | **4.00%** | (income tax is separate, see Section 10) |
| **Combined total** |  | **21.85%** | 17.85% employer + 4.00% employee |

Arithmetic check: employer 6.35 + 11.50 = 17.85; combined 17.85 + 4.00 = 21.85. ✓

**Conservative defaults**

| Ambiguity | Default |
| --- | --- |
| Unknown employer levy category | Apply general tryggingagjald 6.35% (not fishermen 7.00% or A1 0.425%) |
| Unknown pension rate | Apply statutory minimum split: 4% employee / 11.5% employer |
| Unknown A1 certificate status | Assume employee is socially insured in Iceland (full levy) until A1 produced |
| Unknown employment status | Treat the individual as an employee; flag self-employed (reiknað endurgjald) question for reviewer |
| Unknown personal tax credit allocation (income tax only) | Assume primary employer applies full credit; secondary employer applies none |
| Minimum wage needed | Defer to applicable collective agreement; treat any single figure as indicative — Iceland has NO statutory minimum wage |
| Unknown whether DSS/Skatturinn debit is levy or penalty | Classify as levy/withholding; flag for reviewer |

## Section 2 -- Required inputs and refusal catalogue

### Required inputs

- **Required inputs levels** — Minimum viable — gross remuneration (monthly or annual) and the contributor's role (employer, employee, or self-employed). Without gross remuneration, STOP. Do not compute contributions. Recommended — employer levy category (general / fishermen / A1-certificate holder), age (to confirm the 16–70 pension obligation), and whether the worker pays into the standard or an alternative/private pension fund. Ideal — payslip (launaseðill), the monthly staðgreiðsla return, employment contract or collective agreement reference, and (for self-employed) the reckoned remuneration (reiknað endurgjald) figure.

### Refusal catalogue

- **R-IS-SSC-1 — Gross remuneration unknown** — Trigger: gross pay or reckoned remuneration not provided. Message: "Gross remuneration is mandatory for tryggingagjald and pension computation. Both the 6.35% levy and the 15.5% pension are percentages of total wages with no ceiling. Cannot proceed without this figure."
- **R-IS-SSC-2 — Penalty / arrears quantification** — Trigger: client has overdue tryggingagjald or withholding and wants the penalty quantified. Message: "Icelandic default-interest (dráttarvextir) and the statutory mark-up (álag) are set by law and re-set periodically by the Central Bank; the exact current percentage was not confirmed from an English-language authoritative source [RESEARCH GAP — reviewer to confirm]. Do not estimate penalties. Escalate to an Icelandic licensed accountant with the Skatturinn statement of account."
- **R-IS-SSC-3 — A1 certificate / posted worker** — Trigger: worker claims to remain insured abroad under an EU/EEA A1 certificate. Message: "Reduced tryggingagjald (0.425%) applies only on production of a valid A1 certificate confirming the worker is socially insured in another EU/EEA state. Pension and social-security coordination for posted workers is fact-specific. Escalate to a reviewer; do not apply the reduced levy without sighting the A1."
- **R-IS-SSC-4 — Employer pension tax-free cap / fringe benefit** — Trigger: employer contributes above the statutory minimum, or client asks whether the employer's pension contribution is taxable to the employee. Message: "Employer pension contributions are tax-free to the employee only up to 12% of remuneration AND ISK 2,000,000 per year; the excess is taxable employee income (PwC; KPMG fn 8). Confirm the contribution structure with a reviewer before treating any portion as tax-free."

## Section 3 -- Payment pattern library

This is the deterministic pre-classifier for bank statement transactions related to social/payroll contributions. When a transaction matches a pattern below, apply the treatment directly. Do not second-guess. How to read this table. Match by case-insensitive substring on the counterparty/reference as it appears in the bank statement. Tryggingagjald and pension remittances are statutory employer/employee obligations — they EXCLUDE from any VAT return. Tryggingagjald and the employer's pension portion ARE deductible business payroll costs for the employer; the employee's 4% pension is deductible from the employee's income-tax base.

### 3.1 Tryggingagjald and withholding remittances to Skatturinn

**Pattern table 3.1**

| Pattern | Treatment | Notes |
| --- | --- | --- |
| SKATTURINN, RSK, RÍKISSKATTSTJÓRI | EXCLUDE from VAT — Skatturinn remittance | Could bundle withheld income tax + tryggingagjald; split per return |
| STAÐGREIÐSLA, STADGREIDSLA | EXCLUDE from VAT — PAYE remittance | Monthly withholding (income tax + levy) |
| TRYGGINGAGJALD | EXCLUDE from VAT — employer payroll levy | Deductible employer payroll cost |
| SKILAGREIN, SKILAGREIN STAÐGREIÐSLU | EXCLUDE from VAT — withholding return payment | Monthly skilagrein remittance |

### 3.2 Pension fund (lífeyrissjóður) debits

**Pattern table 3.2**

| Pattern | Treatment | Notes |
| --- | --- | --- |
| LÍFEYRISSJÓÐUR, LIFEYRISSJODUR | EXCLUDE from VAT — pension contribution | 4% employee + 11.5% employer remitted to fund |
| LÍFEYRIR, LIFEYRIR | EXCLUDE from VAT — pension contribution | Generic "pension" reference |
| SÉREIGN, SEREIGN, SÉREIGNARSPARNAÐUR | EXCLUDE from VAT — voluntary pension | Additional voluntary (séreignarsparnaður) |
| GILDI, LSR, FRJÁLSI, BIRTA, STAPI (named funds) | EXCLUDE from VAT — pension contribution | Named Icelandic pension funds |

### 3.3 Income tax and other levies (NOT social/pension contributions — do not confuse)

**Pattern table 3.3**

| Pattern | Treatment | Notes |
| --- | --- | --- |
| TEKJUSKATTUR | EXCLUDE from VAT — income tax | National income tax, not a contribution |
| ÚTSVAR, UTSVAR | EXCLUDE from VAT — municipal income tax | Municipal tax, not a contribution |
| ÚTVARPSGJALD, UTVARPSGJALD | EXCLUDE from VAT — broadcasting fee | ISK 21,400 (2025) / 22,200 (2026) per individual |
| FRAMKVÆMDASJÓÐUR ALDRAÐRA | EXCLUDE from VAT — Construction Fund for the Elderly | ISK 14,093 (2025) / 14,614 (2026) |

### 3.4 Salary and payroll (exclude from contribution classification)

**Pattern table 3.4**

| Pattern | Treatment | Notes |
| --- | --- | --- |
| LAUN, LAUNAGREIÐSLA (outgoing) | EXCLUDE — gross salary payroll expense | Not itself a contribution |
| LAUN (incoming) | EXCLUDE — employment income received | Not a contribution payment |
| STÉTTARFÉLAG, FÉLAGSGJALD (union dues) | EXCLUDE from VAT — union dues | Deducted with payroll; not tryggingagjald/pension |

### 3.5 Benefits received (NOT contributions paid)

**Pattern table 3.5**

| Pattern | Treatment | Notes |
| --- | --- | --- |
| TRYGGINGASTOFNUN, TR (incoming) | EXCLUDE from VAT — benefit/pension received | Inbound benefit, not a contribution paid |
| ELLILÍFEYRIR (incoming) | EXCLUDE from VAT — old-age pension received | Taxable income, not a contribution |
| FÆÐINGARORLOF (incoming) | EXCLUDE from VAT — parental leave benefit | Financed by the levy; benefit received |

## Section 4 -- Worked examples

Six bank-statement / payroll classifications for a hypothetical Reykjavík employer and its employees (figures use the 2025 income year; switch to 2026 thresholds where noted). All ISK.

### Example 1 — Monthly tryggingagjald remittance (general 6.35%)

Input line: `15.02.2025 ; SKATTURINN STAÐGREIÐSLA ; DEBIT ; TRYGGINGAGJALD JAN ; -127,000 ; ISK`

Reasoning: Matches "TRYGGINGAGJALD" (pattern 3.1). For January wages of ISK 2,000,000 the general levy is 2,000,000 × 6.35% = ISK 127,000, remitted by the 15th of February (the month after payment) (Skatturinn; KPMG sec 4.2). Employer payroll cost; exclude from VAT.

Classification: EXCLUDE from VAT. Deductible employer payroll levy. Arithmetic: 2,000,000 × 0.0635 = 127,000. ✓

### Example 2 — Pension fund remittance (4% + 11.5%)

Input line: `10.02.2025 ; GILDI LÍFEYRISSJÓÐUR ; DEBIT ; LÍFEYRIR JAN ; -310,000 ; ISK`

Reasoning: Matches "LÍFEYRISSJÓÐUR" (pattern 3.2). On ISK 2,000,000 of wages the mandatory pension is 15.5% = ISK 310,000, split 4% employee (ISK 80,000, withheld from pay) + 11.5% employer (ISK 230,000) (PwC; KPMG fn 7; Central Bank of Iceland). Exclude from VAT.

Classification: EXCLUDE from VAT. Employer portion is a payroll cost; employee 4% is deductible from the employee's income-tax base. Arithmetic: 2,000,000 × 0.155 = 310,000; 80,000 + 230,000 = 310,000. ✓

### Example 3 — Fishermen surcharge (7.00%)

Input line: `15.03.2025 ; SKATTURINN ; DEBIT ; TRYGGINGAGJALD SJÓMENN FEB ; -70,000 ; ISK`

Reasoning: Reference flags "SJÓMENN" (seamen/fishermen). For fishermen the levy is 7.00% (6.35% general + 0.65% surcharge) (KPMG sec 4.2). On ISK 1,000,000 of fishermen wages: 1,000,000 × 7.00% = ISK 70,000. Do NOT apply the general 6.35% here.

Classification: EXCLUDE from VAT. Deductible employer payroll levy at the fishermen rate. Arithmetic: 1,000,000 × 0.07 = 70,000. ✓

### Example 4 — A1-certificate posted worker (0.425%)

Input line: `15.04.2025 ; SKATTURINN ; DEBIT ; TRYGGINGAGJALD A1 MAR ; -2,125 ; ISK`

Reasoning: Reference flags "A1". Where the employee holds a valid EU/EEA A1 certificate and remains socially insured abroad, the reduced levy of 0.425% applies (KPMG sec 4.2 & fn 6). On ISK 500,000 of remuneration: 500,000 × 0.425% = ISK 2,125. Do NOT apply this without sighting the A1 (see R-IS-SSC-3).

Classification: EXCLUDE from VAT. Reduced-rate levy — reviewer must confirm A1 certificate on file. Arithmetic: 500,000 × 0.00425 = 2,125. ✓

### Example 5 — Income tax remittance (NOT a contribution)

Input line: `15.02.2025 ; SKATTURINN ; DEBIT ; STAÐGREIÐSLA TEKJUSKATTUR + ÚTSVAR ; -119,461 ; ISK`

Reasoning: Reference flags "TEKJUSKATTUR + ÚTSVAR" (pattern 3.3) — withheld personal income tax (national + municipal), NOT a social/pension contribution. For an employee on ISK 600,000 monthly gross (2025): pension 4% = 24,000; income-tax base = 600,000 − 24,000 = 576,000; tax = 472,005 × 31.49% + (576,000 − 472,005) × 37.99% − 68,691 personal credit = 148,644 + 39,508 − 68,691 = ISK 119,461 (Skatturinn Tax-brackets 2025; Key Rates 2025).

Classification: EXCLUDE from VAT. Withheld income tax — do NOT count as tryggingagjald or pension. Arithmetic: 472,005 × 0.3149 = 148,644.37; 103,995 × 0.3799 = 39,507.70; sum 188,152.07; less 68,691 = 119,461.07 → ISK 119,461. ✓

### Example 6 — Self-employed contributions (reiknað endurgjald)

Input line: `15.05.2025 ; SKATTURINN ; DEBIT ; SJÁLFSTÆTT TRYGGINGAGJ + LÍFEYRIR ; -217,500 ; ISK`

Reasoning: A self-employed person pays tryggingagjald 6.35% on reckoned remuneration AND the full pension 15.5% (both employee 4% and employer 11.5% parts) (KPMG sec 13.1 fn 31 & 4.2). On reckoned monthly remuneration of ISK 1,000,000: tryggingagjald 1,000,000 × 6.35% = 63,500; pension 1,000,000 × 15.5% = 155,000; total monthly = 218,500. The statement line shows ISK 217,500 — flag the ISK 1,000 difference for reviewer (rounding or partial period).

Classification: EXCLUDE from VAT. Self-employed levy + pension. Flag the discrepancy. Arithmetic check: 63,500 + 155,000 = 218,500 (not 217,500) → reviewer flag. ✓

## Section 5 -- Tier 1 rules

These rules apply when payroll/bank-statement data is clear and all required inputs are available. Apply exactly as written.

### Rule 1 — Tryggingagjald formula (general)

- **Tryggingagjald formula** — Tryggingagjald = total_gross_remuneration × 6.35%. No floor, no ceiling. Employer-paid; self-employed pay it on reckoned remuneration.  _(Skatturinn Key Rates 2025/2026; KPMG sec 4.2)_

### Rule 2 — Levy category overrides the general rate

- **Levy category overrides** — Fishermen/seamen: 7.00% (6.35% + 0.65% surcharge). Employee with valid EU/EEA A1 certificate: 0.425%. All other employment: 6.35% (default).  _(KPMG sec 4.2 & fn 6)_

### Rule 3 — Mandatory pension split

- **Mandatory pension formula** — Mandatory pension = total_wages × 15.5% = employee 4% + employer 11.5% (minimum). The employee's 4% is deductible from the employee's income-tax base; the employer's 11.5% is a payroll cost.  _(PwC; KPMG sec 4.2/13.1; Central Bank of Iceland)_

### Rule 4 — Alternative/private pension fund adds 2% employer

- **Alternative fund 2% addition** — If the employee pays into an alternative/private pension fund instead of the standard fund, the employer must pay an extra 2% to that fund.  _(KPMG fn 7)_

### Rule 5 — Voluntary pension (séreignarsparnaður)

- **Voluntary pension rule** — Employee may contribute up to an additional 4% (deductible), with the employer typically matching 2%. Optional — do not assume it applies unless stated.  _(KPMG sec 4.2)_

### Rule 6 — Self-employed pay both pension parts plus the levy

- **Self-employed rule** — Self-employed pay tryggingagjald (6.35%) themselves AND the full 15.5% pension (4% + 11.5%) on reckoned remuneration (reiknað endurgjald).  _(KPMG sec 13.1 fn 31 & 4.2)_

### Rule 7 — Pension obligation age range

- **Pension obligation age range rule** — Mandatory pension applies to wage earners and self-employed aged 16–70.  _(PwC; Central Bank of Iceland)_

### Rule 8 — Employer pension tax-free cap

- **Employer pension tax-free cap rule** — Employer pension contributions are tax-free to the employee unless they exceed 12% of remuneration AND ISK 2,000,000 per year — the excess is taxable employee income.  _(PwC; KPMG fn 8)_

### Rule 9 — Remittance schedule (PAYE / staðgreiðsla)

- **Remittance schedule rule** — Employer withholds income tax and tryggingagjald monthly; the remittance (skilagrein staðgreiðslu) is due by the 15th of the month following the wage-payment month (14 days after wages paid).  _(PwC tax admin; Skatturinn)_

### Rule 10 — Contributions are not VAT supplies

- **VAT exclusion rule** — Tryggingagjald, pension contributions, withheld income tax, and union dues are statutory/payroll obligations — never VAT-able supplies. Exclude from any VAT (VSK) return.

## Section 6 -- Tier 2 catalogue

When data is ambiguous or client circumstances are unclear, flag these situations for reviewer confirmation.

### T2-1 — Levy category uncertainty (fishermen vs general)

- **T2-1** — Trigger: Worker is in fishing/maritime sector but the role on the bank line is ambiguous. Issue: Fishermen attract 7.00% vs general 6.35% — a 0.65 pp difference. Action: Flag for reviewer; confirm whether the worker falls within the statutory fishermen/seamen category.

### T2-2 — A1 certificate validity and coverage period

- **T2-2** — Trigger: Worker claims A1 coverage from another EU/EEA state. Issue: Reduced 0.425% applies only for the period the A1 is valid and only if produced. Action: Flag for reviewer; do not apply 0.425% without sighting the certificate and its validity dates.

### T2-3 — Employer contribution above tax-free cap

- **T2-3** — Trigger: Employer contributes more than 11.5%, or total employer pension nears 12% / ISK 2,000,000/year. Issue: Excess over 12% of remuneration AND ISK 2,000,000/year becomes taxable employee income (PwC; KPMG fn 8). Action: Flag for reviewer to quantify the taxable fringe benefit.  _(PwC; KPMG fn 8)_

### T2-4 — Self-employed reckoned remuneration (reiknað endurgjald)

- **T2-4** — Trigger: Self-employed person's reckoned remuneration is below Skatturinn's minimum tables or disputed. Issue: The base for both the levy and pension is the reckoned remuneration, which Skatturinn can challenge. Action: Flag for reviewer to confirm the reiknað endurgjald category before computing.

### T2-5 — Overdue levy/withholding (penalty exposure)

- **T2-5** — Trigger: Monthly remittance not paid by the 15th. Issue: Default interest (dráttarvextir) and a statutory mark-up (álag) apply; the exact percentages were not confirmed from an English authoritative source [RESEARCH GAP — reviewer to confirm]. Action: Do not estimate. Escalate to a reviewer with the Skatturinn statement of account.

### T2-6 — Minimum-wage / collective-agreement floor

- **T2-6** — Trigger: Need to test whether wages meet a legal floor. Issue: Iceland has NO statutory minimum wage; floors are set by collective agreements (ASÍ/SA) and vary by sector. Action: Flag for reviewer; identify the applicable collective agreement. Treat any single figure (e.g. ~ISK 425,985/month under some 2025 SGS agreements — union/secondary source) as indicative only [RESEARCH GAP — reviewer to confirm against the live agreement].

## Section 7 -- Excel working paper template

When producing an Iceland contribution computation, structure the working paper as follows:

```
ICELAND SOCIAL CONTRIBUTIONS -- WORKING PAPER
Client / Employer: [name]
Worker:            [name]
Income year:       [2025 / 2026]
Prepared:          [date]

INPUT DATA
  Role:                          [Employer / Employee / Self-employed]
  Levy category:                 [General / Fishermen / A1-certificate]
  A1 certificate sighted:        [YES / NO]
  Age (16-70 pension?):          [____]
  Monthly gross remuneration:    ISK [____]
  Alternative pension fund?:     [YES / NO]
  Voluntary pension elected?:    [YES / NO]

CONTRIBUTION COMPUTATION
  Tryggingagjald rate:           [6.35% / 7.00% / 0.425%]
  Tryggingagjald (employer):     ISK [____]   = gross x rate
  Pension employee (4%):         ISK [____]
  Pension employer (11.5%):      ISK [____]
  Extra 2% to alt. fund:         ISK [____]   (if applicable)
  Voluntary employee (<=4%):     ISK [____]   (if elected)
  Voluntary employer (2%):       ISK [____]   (if elected)
  ----------------------------------------------------
  Employer total cost:           ISK [____]
  Employee deductions:           ISK [____]

INCOME-TAX BASE INTERACTION (see iceland-income-tax skill)
  Gross less 4% pension:         ISK [____]   = income-tax base
  (income tax computed in the income-tax skill)

REMITTANCE
  Wage payment month:            [____]
  Skilagrein staðgreiðslu due:   [15th of following month]

REVIEWER FLAGS
  [List any Tier 2 flags here]

CONSERVATIVE DEFAULTS APPLIED
  [List any defaults applied and their impact]
```

## Section 8 -- Bank statement reading guide

### How contribution payments appear on Icelandic bank statements

Landsbankinn / Íslandsbanki / Arion banki (main retail banks):
- Tryggingagjald + withholding: "SKATTURINN", "RSK", "STAÐGREIÐSLA", "SKILAGREIN"
- Pension: "LÍFEYRISSJÓÐUR" or the named fund (Gildi, LSR, Frjálsi, Birta, Stapi, etc.)
- Voluntary pension: "SÉREIGN" / "SÉREIGNARSPARNAÐUR"
- Union dues: "STÉTTARFÉLAG" / "FÉLAGSGJALD"

Key identification tips:
1. Contribution remittances are outgoing (DEBIT). Inbound credits from TRYGGINGASTOFNUN or TR are benefits received, not contributions.
2. Tryggingagjald and withheld income tax may be bundled into one Skatturinn remittance — split using the staðgreiðsla return (skilagrein), not the bank line alone.
3. Tryggingagjald should equal gross wages × 6.35% (or 7.00% fishermen / 0.425% A1). If it does not divide cleanly, check the levy category.
4. Pension remittances should equal gross × 15.5% (4% + 11.5%) for the standard fund.
5. Remittances cluster around the 15th of each month (the staðgreiðsla due date).
6. Do NOT confuse ÚTSVAR (municipal income tax), ÚTVARPSGJALD (broadcasting fee), or FRAMKVÆMDASJÓÐUR ALDRAÐRA (Construction Fund for the Elderly) with social/pension contributions.

### Icelandic terminology quick-reference

**Terminology table**

| Icelandic | English |
| --- | --- |
| Tryggingagjald | Social security contribution / general payroll levy |
| Lífeyrissjóður | Pension fund |
| Lífeyrir | Pension |
| Séreignarsparnaður | Additional voluntary (private) pension savings |
| Staðgreiðsla | PAYE withholding at source |
| Skilagrein staðgreiðslu | Monthly withholding return |
| Reiknað endurgjald | Calculated/reckoned remuneration (self-employed) |
| Launaseðill | Payslip |
| Sjómenn | Fishermen / seamen |
| Stéttarfélag / Félagsgjald | Union / union dues |
| Tryggingastofnun | Social Insurance Administration (benefits) |

## Section 9 -- Onboarding fallback

If the client provides only a bank statement and no other information:

1. Scan for Skatturinn / pension debits — identify all outgoing payments matching Section 3 patterns.
2. Separate the streams — Skatturinn remittances (levy + income tax) vs lífeyrissjóður (pension) vs ÚTSVAR/broadcasting/Construction-Fund (not contributions).
3. Reverse-engineer the base:
   - If a pension debit is present, implied gross ≈ pension debit ÷ 0.155 (standard 15.5%).
   - If a tryggingagjald line is present, implied gross ≈ levy ÷ 0.0635 (general) — but check for fishermen 7.00% or A1 0.425% first.
4. Flag for reviewer: "Contribution classification derived from bank statement amounts only. Levy category (general/fishermen/A1), pension fund type, and the split between withheld income tax and tryggingagjald have not been independently verified. Reviewer must confirm against the staðgreiðsla returns before filing."

## Section 10 -- Reference material

### Tryggingagjald rates (employer payroll levy)

**Tryggingagjald rates table**

| Category | Rate | Source |
| --- | --- | --- |
| General | 6.35% (2025 & 2026 unchanged) | Skatturinn Key Rates 2025/2026; KPMG sec 4.2 |
| Fishermen / seamen | 7.00% (6.35% + 0.65%) | KPMG sec 4.2 |
| A1-certificate (EU/EEA) | 0.425% | KPMG sec 4.2 & fn 6 |

Internal-composition note: KPMG (sec 1.3) describes the 6.35% total as bundling the social-security component, the Bankruptcy Wage Guarantee Fund contribution, and the market charge. A Bloomberg Tax report of the Ministry of Finance's 2026 announcement separately cites a "4.9% general social security tax rate", which appears to be the social-security sub-component within the 6.35% total. This skill uses 6.35% as the employer's total payroll levy; reviewers reconciling to a "4.9%" figure should treat it as the sub-component, not the headline levy [RESEARCH GAP — reviewer to confirm the exact internal breakdown].

### Mandatory pension contributions

**Mandatory pension contributions table**

| Contributor | Rate | Notes | Source |
| --- | --- | --- | --- |
| Employee | 4% of total wages | Deductible from income-tax base | PwC; KPMG sec 4.2/13.1 |
| Employer | 11.5% of total wages (min) | + 2% extra to alt./private fund | PwC; KPMG fn 7 |
| **Total minimum** | **15.5%** | 4% + 11.5% | PwC; Central Bank of Iceland |
| Voluntary employee | up to +4% (deductible) | optional (séreignarsparnaður) | KPMG sec 4.2 |
| Voluntary employer match | typically +2% | optional | KPMG sec 4.2 |
| Self-employed | 15.5% (both parts) | on reckoned remuneration | KPMG sec 13.1 fn 31 |

Arithmetic check: employee 4% + employer 11.5% = 15.5% total. ✓

### Income tax brackets (context — computed in the iceland-income-tax skill)

The 4% employee pension is deductible from the income-tax base; the figures below are provided so contribution work reconciles with payslip net pay. Rates are combined national + average municipal (útsvar 14.94% avg; municipal range 12.44%–14.94%).

**Income year 2025 bracket table**  _(Skatturinn Tax-brackets 2025)_

| Band | Monthly ISK | Combined rate |
| --- | --- | --- |
| 1 | 0 – 472,005 | 31.49% |
| 2 | 472,006 – 1,325,127 | 37.99% |
| 3 | over 1,325,127 | 46.29% |

**Income year 2026 bracket table**  _(Skatturinn Key Rates 2026; PwC; Bloomberg Tax MOF 23 Dec 2025)_

| Band | Monthly ISK | Combined rate |
| --- | --- | --- |
| 1 | 0 – 498,122 | 31.49% |
| 2 | 498,123 – 1,398,450 | 37.99% |
| 3 | over 1,398,450 | 46.29% |

- **Personal tax credit** — 2025 ISK 68,691/month (824,288/year); 2026 ISK 72,492/month (869,898/year)  _(Skatturinn Key Rates)_
- **Capital income tax** — flat 22% for individuals  _(Skatturinn; PwC)_

### Thresholds

**Thresholds table**

| Item | Value | Source |
| --- | --- | --- |
| VAT (VSK) registration | ISK 2,000,000 taxable turnover in any rolling 12 months; register (RSK 5.02) within 8 days | Skatturinn VAT; Avalara |
| Pension obligation age range | 16–70 | PwC; Central Bank of Iceland |
| Employer pension tax-free cap | excess over BOTH 12% of remuneration AND ISK 2,000,000/year is taxable | PwC; KPMG fn 8 |
| Construction Fund for the Elderly | ISK 14,093 (assessment 2025) / 14,614 (assessment 2026), individuals 16–69 | Skatturinn Key Rates 2025/2026 |
| National Broadcasting fee (Útvarpsgjald) | ISK 21,400 (assessment 2025) / 22,200 (assessment 2026); 2026 income threshold ISK 2,617,618 | Skatturinn Key Rates 2025/2026; PwC |
| Children's income flat rate | 6% on a child's (born 2010+) income over ISK 300,000/year (2026, up from 180,000) | Skatturinn Key Rates 2026; Bloomberg Tax |
| Minimum wage | NONE statutory — collective-agreement floors only (~ISK 425,985/month under some 2025 SGS agreements, indicative) | Union/secondary **[RESEARCH GAP — reviewer to confirm]** |

### Forms

**Forms table**

| Form | Purpose | Deadline | Source |
| --- | --- | --- | --- |
| Skilagrein staðgreiðslu | Monthly withholding return (income tax + tryggingagjald) | 15th of month following wage payment | PwC tax admin; Skatturinn |
| Individual income tax return (framtal) | Annual personal return | by 14 March of following year; final assessment by 31 May | PwC tax admin; KPMG |
| RSK 5.02 | VAT registration application | within 8 days of crossing ISK 2,000,000 / 12 months | Skatturinn; Avalara |
| Corporate income tax return | Annual company return | 31 May (set annually; was 31 May 2025) | KPMG Tax Facts 2025 |

### Penalties

**Penalties table**

| Penalty | Detail | Source |
| --- | --- | --- |
| Default interest (dráttarvextir) | Statutory rate (Central Bank base + premium) on overdue claims; cannot be negotiated. Exact % not in an English authoritative source **[RESEARCH GAP — reviewer to confirm]** | Skatturinn Collection of Liabilities |
| Surcharge / mark-up (álag) | Statutory mark-up added to principal in defined circumstances (income-tax álag commonly up to 25% of understated tax); exact % unconfirmed **[RESEARCH GAP — reviewer to confirm]** | Skatturinn Collection of Liabilities |
| Late withholding remittance | Triggers penalty interest + possible surcharge; persistent default → collection action | Skatturinn; PwC |

### Test suite

Employee, gross ISK 1,000,000/month, general category. → Tryggingagjald (employer) = 1,000,000 × 6.35% = ISK 63,500. Pension employee 4% = ISK 40,000; employer 11.5% = ISK 115,000; total pension ISK 155,000. (40,000 + 115,000 = 155,000 ✓)

Fisherman, gross ISK 1,000,000/month. → Tryggingagjald = 1,000,000 × 7.00% = ISK 70,000 (not 63,500). Pension unchanged: ISK 155,000.

A1-certificate employee, gross ISK 500,000/month, A1 sighted. → Tryggingagjald = 500,000 × 0.425% = ISK 2,125. (Pension treatment depends on coordination — flag if insured abroad.)

Self-employed, reckoned remuneration ISK 800,000/month. → Tryggingagjald 800,000 × 6.35% = ISK 50,800; pension 800,000 × 15.5% = ISK 124,000; total monthly = ISK 174,800. (50,800 + 124,000 = 174,800 ✓)

Employee, gross ISK 600,000/month, 2025. Income-tax base = 600,000 − 24,000 (4% pension) = 576,000. Tax = 472,005 × 31.49% + (576,000 − 472,005) × 37.99% − 68,691 = 148,644.37 + 39,507.70 − 68,691 = ISK 119,461. Net pay = 600,000 − 24,000 − 119,461 = ISK 456,539. (600,000 − 143,461 = 456,539 ✓)

Employer contributes 14% pension on ISK 2,500,000/year remuneration. → 14% of 2,500,000 = 350,000; tax-free cap is the LOWER bound of (12% of remuneration AND ISK 2,000,000). Here 350,000 < 2,000,000, but 14% > 12%, so the excess over 12% (i.e. 2% × 2,500,000 = ISK 50,000) is taxable employee income only if BOTH conditions are breached — since the ISK 2,000,000/year ceiling is NOT exceeded, no taxable benefit arises. Flag for reviewer (T2-3) to confirm the conjunctive test.

Bank line "STAÐGREIÐSLA" bundling income tax + tryggingagjald. → Split using the skilagrein return; do not treat the whole debit as either one. Flag if the return is unavailable.

Worker aged 72. → Mandatory pension obligation runs 16–70; flag for reviewer whether contributions are still due (PwC; Central Bank of Iceland).

### Prohibitions

- NEVER apply the general 6.35% to fishermen (7.00%) or A1-certificate workers (0.425%) without confirming the category.
- NEVER apply the reduced 0.425% A1 levy without sighting a valid A1 certificate.
- NEVER treat the 4% employee pension as anything other than deductible from the EMPLOYEE'S income-tax base.
- NEVER apply a ceiling to tryggingagjald or to the mandatory pension — there is none.
- NEVER estimate dráttarvextir (default interest) or álag (surcharge) — exact percentages are unconfirmed; escalate.
- NEVER quote a "statutory minimum wage" for Iceland — there is none; defer to the collective agreement.
- NEVER treat an employer pension contribution above 11.5% as automatically tax-free — test the 12% / ISK 2,000,000 conjunctive cap.
- NEVER confuse ÚTSVAR (municipal income tax), ÚTVARPSGJALD, or the Construction Fund for the Elderly with social/pension contributions.
- NEVER present contribution figures as definitive — label as estimated and direct the client to their staðgreiðsla returns and pension fund statement.
- NEVER include contributions in a VAT (VSK) return.

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
