---
name: croatia-social-contributions
description: Use this skill whenever asked about Croatian social security contributions (doprinosi) and the related personal income tax (porez na dohodak) on employment income for the 2025 tax year. Trigger on phrases like "how much pension contribution do I pay", "Croatia payroll contributions", "Pillar I and Pillar II pension", "mirovinsko osiguranje", "zdravstveno osiguranje", "16.5% health contribution", "20% pension contribution", "gross to net Croatia", "Croatian salary calculation", "doprinosi za mirovinsko", "HZZO contribution", "Croatia income tax rate", "porez na dohodak", "JOPPD", "Croatian minimum wage 2025", or any question about a Croatian employee's gross-to-net pay, employer on-costs, or contribution caps. Also trigger when classifying bank statement transactions that relate to HZMO, HZZO, Porezna uprava, doprinosi, or plaća payments from Croatian banks (Zagrebačka banka, PBZ, Erste, OTP, Raiffeisen). Also trigger when preparing or reviewing a JOPPD report where contribution bases, low-salary relief, or the pension base cap are relevant. This skill covers employee pension contributions (15% Pillar I + 5% Pillar II), the 16.5% employer health contribution, low-salary pension relief, monthly/annual base caps, the floor base, the two-band income tax, JOPPD filing, bank statement classification patterns, and edge cases. ALWAYS read this skill before touching any Croatian contributions or payroll work.
version: 0.1
jurisdiction: HR
tax_year: 2025
last_updated: 2026-07-13
review_status: pending_review
depends_on:
  - social-contributions-workflow-base
category: international
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Croatia Social Security Contributions (Doprinosi) -- Employment

## Croatia Social Security Contributions (Doprinosi) -- Employment Skill v0.1

## Section 1 -- Quick reference

**Read this whole section before computing or classifying anything.**

**Quick reference field table**

| Field | Value |
| --- | --- |
| Country | Croatia (Republic of Croatia / Republika Hrvatska) |
| Primary Legislation | Zakon o doprinosima (Contributions Act, OG 84/08 as amended) |
| Supporting Legislation | Zakon o porezu na dohodak (Personal Income Tax Act); Pravilnik o doprinosima (Ordinance on Contributions); Zakon o mirovinskom osiguranju (Pension Insurance Act); Zakon o obveznom zdravstvenom osiguranju (Compulsory Health Insurance Act); Zakon o minimalnoj plaći (Minimum Wage Act) |
| Tax Authority | Ministry of Finance -- Tax Administration (Porezna uprava), https://porezna-uprava.gov.hr |
| Pension administration | Hrvatski zavod za mirovinsko osiguranje (HZMO), https://www.mirovinsko.hr |
| Health administration | Hrvatski zavod za zdravstveno osiguranje (HZZO), https://www.hzzo.hr |
| Employee pension rate (total) | 20% of base: 15% Pillar I + 5% Pillar II (Porezna uprava 7319) |
| Employer health rate | 16.5% of gross salary, uncapped (PwC) |
| Monthly pension base cap (2025) | EUR 11,958.00 (= 6.0 x EUR 1,993 average gross) (PwC) |
| Annual Pillar I base cap (2025) | EUR 143,496.00 (PwC) |
| Lowest monthly base (full-time, 2025) | EUR 757.34 (= 0.38 x EUR 1,993) (FINaCRO/Pravilnik) |
| Income tax bands (2025) | Lower: up to EUR 60,000/yr (EUR 5,000/mo); Higher: above (Porezna uprava 7322) |
| Default income tax rates | 20% lower / 30% higher where local rate not set (Porezna uprava 7322) |
| Basic personal allowance (2025) | EUR 600.00/month (EUR 7,200/yr) (Deloitte) |
| Minimum gross wage (2025) | EUR 970.00/month (Deloitte) |
| Currency | EUR only (Croatia adopted EUR on 1 Jan 2023; HRK retired) |
| Reporting form | JOPPD (Obrazac JOPPD), monthly, electronic (Porezna uprava 7319) |
| Validated by | Pending -- requires sign-off by a Croatian licensed tax adviser / accountant |
| Validation date | Pending |

**Contribution overview (employment income, 2025):**

**Contribution overview table**

| Contribution | Who pays | Rate | Base | Source |
| --- | --- | --- | --- | --- |
| Pension -- Pillar I (mirovinsko, I. stup) | Employee (withheld) | 15% (in Pillar II) or 20% (not in Pillar II) | Capped salary base | Porezna uprava 7319 |
| Pension -- Pillar II (II. stup) | Employee (withheld) | 5% | Capped salary base | Porezna uprava 7319 |
| **Employee pension total** | **Employee** | **20%** | **Capped salary base** | Porezna uprava 7319 |
| Health insurance (zdravstveno, HZZO) | Employer (on top) | 16.5% | Gross salary, uncapped | PwC |
| **Employer total** | **Employer** | **16.5%** | **Gross salary, uncapped** | PwC |

Arithmetic check: employee pension 15% + 5% = 20%. Employer total = 16.5% (single consolidated contribution). Both verified against Porezna uprava 7319 and PwC.

**Conservative defaults:**

**Conservative defaults table**

| Ambiguity | Default |
| --- | --- |
| Local income tax rate unknown | Use default 20% (lower band) / 30% (higher band) -- statutory fallback (Porezna uprava 7322) |
| Employee Pillar II membership unknown | Assume in Pillar II: 15% Pillar I + 5% Pillar II = 20% (Porezna uprava 7319) |
| Employer on-costs | 16.5% health only -- do NOT add legacy unemployment/injury contributions (PwC) |
| Unknown gross salary | STOP -- do not compute contributions or net pay without gross |
| Low salary, base unclear | Apply low-salary pension relief formula; never go below EUR 757.34 floor (FINaCRO/Pravilnik) |
| Personal allowance/dependants unknown | Apply basic EUR 600/month only; do not assume dependants (Deloitte) |
| Pillar II split for older worker unknown | STOP -- confirm Pillar II status (older workers may be Pillar I only at 20%) [RESEARCH GAP -- reviewer to confirm] |
| High earner near cap | Apply EUR 11,958.00 monthly pension base cap + EUR 143,496.00 annual Pillar I cap (PwC) |

## Section 2 -- Required inputs and refusal catalogue

### Required inputs

**Minimum viable** -- gross monthly salary (bruto plaća) in EUR, and confirmation this is Croatian employment income subject to doprinosi. Without a gross salary figure, STOP. Do not compute contributions or net pay.

**Recommended** -- whether the employee is a member of the mandatory second pillar (Pillar II), the municipality/town/city of the local self-government unit (determines the income tax rate within statutory bands), and the number/type of dependants (affects the personal allowance).

**Ideal** -- the employer's JOPPD report for the period, a payslip (obračun plaće) showing the contribution bases applied, the employment contract showing contractual gross, and confirmation of any relief (first-job health relief, etc.).

### Refusal catalogue

- **R-HR-SSC-1 -- Gross salary unknown** — Trigger: gross monthly salary not provided (or only net is known). Message: "Croatian payroll is computed gross-to-net. Gross monthly salary in EUR is mandatory: pension contributions, income tax, and employer health cost all derive from the gross. Reverse net-to-gross grossing-up is iterative and locality-dependent. Cannot proceed reliably without the contractual gross."
- **R-HR-SSC-2 -- Local income tax rate not confirmed** — Trigger: an exact net figure is requested but the residence municipality and its adopted rates are unknown. Message: "Croatian personal income tax rates are set by each local self-government unit within statutory bands (lower 15%-23%, higher 25%-33%). The 20%/30% default is an estimate only and is the statutory fallback where no local rate is set. Confirm the employee's residence municipality and its adopted rates before presenting a definitive net."  _(Porezna uprava 7322; Deloitte)_
- **R-HR-SSC-3 -- Pillar II status uncertain for older worker** — Trigger: employee may pre-date the 2002 pension reform or be over the age cut-off and Pillar II membership is unconfirmed. Message: "Mandatory Pillar II membership generally applies to those who entered insurance in/after 2002 or were under 40 at the 2002 reform; older workers may be Pillar I only (full 20% to Pillar I). [RESEARCH GAP -- reviewer to confirm.] Confirm Pillar II status with HZMO / the pension fund before splitting the 20% pension contribution."  _(Porezna uprava 7319; conservative_defaults)_
- **R-HR-SSC-4 -- Self-employed / sole proprietor (obrt) bases** — Trigger: client is an obrtnik (sole proprietor) taxed on income, or a flat-rate (paušalni) taxpayer, not an employee. Message: "Self-employed minimum bases differ: an obrtnik dohodaš faces a minimum monthly gross base of about EUR 1,295.45 for 2025 (= 0.65 x average gross salary EUR 1,993), with contributions at the same rates (FINaCRO/Pravilnik). This skill computes employment payroll; escalate self-employed base determination to a Croatian accountant."
- **R-HR-SSC-5 -- Penalties, arrears, and default interest** — Trigger: unpaid or late contributions / JOPPD from prior periods. Message: "Exact statutory fine amounts and the default-interest rate for late JOPPD/contributions were not found on the consulted authority pages [RESEARCH GAP -- reviewer to confirm against Zakon o doprinosima and Opci porezni zakon (General Tax Act)]. Do not quantify arrears or penalties without a Porezna uprava statement. Escalate to a Croatian accountant."  _(caveats; PwC)_
- **R-HR-SSC-6 -- Cross-border / posted / expat workers** — Trigger: worker is posted, a non-resident, or covered by an A1 certificate / social security coordination. Message: "EU coordination (Reg. 883/2004), A1 certificates, and totalisation are outside this skill's scope. Escalate to a Croatian accountant." [RESEARCH GAP -- outside research scope]

## Section 3 -- Payment pattern library

This is the deterministic pre-classifier for bank statement transactions related to Croatian social security and payroll. When a transaction matches a pattern below, apply the treatment directly. Do not second-guess.

**How to read this table.** Match by case-insensitive substring on the counterparty/reference as it appears in the bank statement. Contribution and income-tax remittances always EXCLUDE from any VAT (PDV) return or revenue/expense reclassification -- they are statutory payroll obligations remitted via JOPPD to the state, not business supplies. From the employer's books, employee pension (20%) and income tax are withheld from gross wages, and the 16.5% health contribution is a payroll on-cost.

### 3.1 Pension contribution remittances (employee-withheld)

**Pension contribution remittances table**

| Pattern | Treatment | Notes |
| --- | --- | --- |
| MIROVINSKO, MIROVINSKO OSIGURANJE | EXCLUDE -- pension contribution | Pillar I and/or Pillar II remittance |
| DOPRINOS MIROVINSKO, DOPR. MIO | EXCLUDE -- pension contribution | Abbreviated reference |
| I. STUP, II. STUP, MIO I, MIO II | EXCLUDE -- pension contribution | Pillar I / Pillar II explicit |
| HZMO | EXCLUDE -- pension contribution | Hrvatski zavod za mirovinsko osiguranje |
| OBVEZNI MIROVINSKI FOND, OMF | EXCLUDE -- Pillar II contribution | Mandatory second-pillar fund |

### 3.2 Health contribution remittances (employer)

**Health contribution remittances table**

| Pattern | Treatment | Notes |
| --- | --- | --- |
| ZDRAVSTVENO, ZDRAVSTVENO OSIGURANJE | EXCLUDE -- health contribution | Employer 16.5% HZZO |
| DOPRINOS ZDRAVSTVENO, DOPR. ZO | EXCLUDE -- health contribution | Abbreviated reference |
| HZZO | EXCLUDE -- health contribution | Hrvatski zavod za zdravstveno osiguranje |

### 3.3 Income tax remittances (NOT a contribution -- do not confuse)

**Income tax remittances table**

| Pattern | Treatment | Notes |
| --- | --- | --- |
| POREZ NA DOHODAK, POREZ DOHODAK | EXCLUDE -- income tax (PIT), not a contribution | Withheld PIT |
| JOPPD | EXCLUDE -- consolidated tax/contribution remittance | Reported at salary payment |
| POREZNA UPRAVA, DRŽAVNI PRORAČUN | EXCLUDE -- tax/contribution remittance | Tax Administration / State Budget account |
| PRIREZ | EXCLUDE -- (abolished) local surtax | Former surtax abolished from 2024 (Deloitte) |

### 3.4 Salary and payroll (exclude from contribution classification)

**Salary and payroll table**

| Pattern | Treatment | Notes |
| --- | --- | --- |
| PLAĆA, NETO PLAĆA, ISPLATA PLAĆE (outgoing) | EXCLUDE -- net salary payment | Take-home pay, not a contribution |
| PLAĆA (incoming) | EXCLUDE -- employment income received | Not a contribution |
| NAKNADA, DNEVNICE, PUTNI TROŠAK, BONUS | EXCLUDE -- allowance/per-diem/bonus | Treat per payroll rules, not as a contribution |

### 3.5 Pension / benefit receipts (received -- not contributions)

**Pension / benefit receipts table**

| Pattern | Treatment | Notes |
| --- | --- | --- |
| MIROVINA, ISPLATA MIROVINE | EXCLUDE -- pension income received | A benefit paid out, not a contribution |
| HZMO MIROVINA | EXCLUDE -- pension income received | Inbound credit, not an outbound contribution |
| BOLOVANJE, NAKNADA HZZO | EXCLUDE -- sickness benefit received | Not a contribution paid |

## Section 4 -- Worked examples

Six bank statement / payroll classifications and computations for a hypothetical Croatian employer running monthly payroll for an IT consultancy. Where a net figure is shown, the DEFAULT income tax rates (20% / 30%) and the basic personal allowance (EUR 600.00) are applied; local rates must be confirmed for a definitive figure. Employees are assumed to be in Pillar II unless stated. All figures in EUR.

### Example 1 -- Standard mid-range salary (gross EUR 2,000/month)

**Input:** Employee, gross monthly salary EUR 2,000.00, tax year 2025, municipality unknown (use defaults).

**Bank line:**
`05.02.2025 ; ISPLATA PLAĆE ; DEBIT ; NETO PLAĆA SIJEČANJ ; -1,400.00 ; EUR`

**Reasoning:**
Matches "ISPLATA PLAĆE" (pattern 3.4). Verify the gross-to-net:
- Gross EUR 2,000 > EUR 1,300 -> no low-salary relief -> pension base = EUR 2,000 (Rule 2; PwC).
- Employee pension 20% = EUR 400.00 (Pillar I 15% = EUR 300.00; Pillar II 5% = EUR 100.00) (Porezna uprava 7319).
- PIT base = gross - pension - personal allowance = 2,000 - 400 - 600 = EUR 1,000.00 (allowance EUR 600/mo, Deloitte).
- Monthly PIT base EUR 1,000 <= EUR 5,000 -> lower band 20% (default) = EUR 200.00 (Porezna uprava 7322).
- Net pay = 2,000 - 400 - 200 = **EUR 1,400.00**. Reconciles to the bank line.
- Employer health 16.5% x 2,000 = EUR 330.00 (uncapped) -> total employer cost = EUR 2,330.00 (PwC).

**Classification:** EXCLUDE -- net salary. Employee pension EUR 400 + PIT EUR 200 + employer health EUR 330 remitted via JOPPD.

### Example 2 -- Minimum wage employee (gross EUR 970/month, low-salary relief)

**Input:** Employee, gross monthly salary EUR 970.00 (2025 minimum wage), tax year 2025, defaults.

**Bank line:**
`05.02.2025 ; PLAĆA ; DEBIT ; NETO ANA HORVAT ; -767.20 ; EUR`

**Reasoning:**
Matches "PLAĆA" (pattern 3.4). Gross EUR 970 = 2025 minimum wage (Deloitte). It falls in the EUR 700.01-1,300 relief band (Rule 2; PwC):
- Pension base = gross - 0.5 x (1,300 - gross) = 970 - 0.5 x (1,300 - 970) = 970 - 165 = EUR 805.00.
- Employee pension 20% = EUR 161.00 (Pillar I EUR 120.75; Pillar II EUR 40.25).
- PIT base = 970 - 161 - 600 = EUR 209.00. PIT 20% = EUR 41.80.
- Net = 970 - 161 - 41.80 = **EUR 767.20**. Reconciles.
- Employer health 16.5% x 970 = EUR 160.05 (uses gross, not the reduced base).

**Classification:** EXCLUDE -- net salary. Low-salary pension relief reduced the pension base from EUR 970 to EUR 805.

### Example 3 -- High earner above the pension cap (gross EUR 15,000/month)

**Input:** Employee, gross monthly salary EUR 15,000.00, tax year 2025, defaults.

**Bank line:**
`05.02.2025 ; ISPLATA PLAĆE ; DEBIT ; NETO IVAN KOVAČ ; -9,505.88 ; EUR`

**Reasoning:**
Matches "ISPLATA PLAĆE" (pattern 3.4). Gross EUR 15,000 exceeds the monthly pension base cap of EUR 11,958.00 (Rule 4; PwC):
- Pension base capped at EUR 11,958.00. Employee pension 20% = EUR 2,391.60 (Pillar I EUR 1,793.70; Pillar II EUR 597.90).
- PIT base = 15,000 - 2,391.60 - 600 = EUR 12,008.40.
- PIT: lower band first EUR 5,000 x 20% = EUR 1,000.00; higher band (12,008.40 - 5,000) = 7,008.40 x 30% = EUR 2,102.52; total PIT = EUR 3,102.52 (Porezna uprava 7322; threshold EUR 5,000/mo, Deloitte).
- Net = 15,000 - 2,391.60 - 3,102.52 = **EUR 9,505.88**. Reconciles.
- Employer health 16.5% x 15,000 = EUR 2,475.00 (health base is NOT capped, PwC).
- Also monitor the annual Pillar I base cap EUR 143,496.00 across the year (Rule 4; PwC).

**Classification:** EXCLUDE -- net salary. Pension capped at EUR 11,958 base; health uncapped.

### Example 4 -- Contribution / tax remittance to the state (NOT salary)

**Input line:**
`15.02.2025 ; POREZNA UPRAVA - DRŽAVNI PRORAČUN ; DEBIT ; JOPPD DOPRINOSI I POREZ SIJEČANJ ; -930.00 ; EUR`

**Reasoning:**
Matches "POREZNA UPRAVA" + "JOPPD" (patterns 3.1/3.2/3.3). This is the employer remitting, for the Example 1 employee, withheld pension (EUR 400), income tax (EUR 200), and employer health (EUR 330): 400 + 200 + 330 = EUR 930.00. It is a state remittance, not a wage. Contributions and tax are due at the time of salary payment, reported on JOPPD (Porezna uprava 7319).

**Classification:** EXCLUDE from PDV/revenue. Statutory payroll remittance via JOPPD.

### Example 5 -- Pension income received (not a contribution)

**Input line:**
`12.02.2025 ; HZMO ; CREDIT ; MIROVINA VELJAČA ; +680.00 ; EUR`

**Reasoning:**
Matches "HZMO MIROVINA" (pattern 3.5). This is a pension benefit RECEIVED, not a contribution paid. Do not confuse inbound HZMO credits with outbound contribution debits. Pension benefits are not an employer payroll cost.

**Classification:** EXCLUDE from contribution classification. Pension income received (taxed under pension rules, outside this skill).

### Example 6 -- Worker not in Pillar II (full 20% to Pillar I)

**Input:** Employee, gross monthly salary EUR 2,000.00, tax year 2025, confirmed NOT in the mandatory second pillar.

**Bank line:**
`05.02.2025 ; PLAĆA ; DEBIT ; NETO MARIJA NOVAK ; -1,400.00 ; EUR`

**Reasoning:**
Matches "PLAĆA" (pattern 3.4). Same gross EUR 2,000 as Example 1, but the worker is confirmed NOT in Pillar II (e.g. older worker, Pillar I only). The total employee pension is still **20%**, but the entire 20% goes to Pillar I; there is no 5% Pillar II split (Rule 1; Porezna uprava 7319):
- Employee pension 20% (all Pillar I) = EUR 400.00. PIT base, PIT, net, and employer health are IDENTICAL to Example 1 (net EUR 1,400.00, employer health EUR 330.00) because the total rate (20%) and base are unchanged.
- The ONLY difference is the JOPPD allocation: EUR 400 to Pillar I, EUR 0 to Pillar II. **Confirm Pillar II status before allocating** [RESEARCH GAP -- reviewer to confirm age/entry-year edge cases].

**Classification:** EXCLUDE -- net salary. Same totals as Example 1; differs only in pension pillar allocation.

## Section 5 -- Tier 1 rules

These rules apply when payroll data is clear and all required inputs are available. Apply exactly as written.

### Rule 1 -- Employee pension formula

- **Employee pension formula** — pension_base    = clamp(relief_adjusted_gross, EUR 757.34 floor, EUR 11,958.00 monthly cap) employee_pension = pension_base x 20% -> if in Pillar II: 15% Pillar I + 5% Pillar II -> if NOT in Pillar II: full 20% to Pillar I  _(Porezna uprava 7319)_
- **Total employee pension and caps** — Total employee pension is always 20% of base. Monthly cap EUR 11,958.00; full-time floor EUR 757.34.  _(Porezna uprava 7319; PwC; FINaCRO/Pravilnik)_

### Rule 2 -- Low-salary pension relief

**Low-salary pension relief table**  _(PwC)_

| Gross monthly salary | Pension base | Source |
| --- | --- | --- |
| Up to EUR 700.00 | gross - EUR 300 | PwC |
| EUR 700.01 -- EUR 1,300.00 | gross - 0.5 x (1,300 - gross) | PwC |
| Above EUR 1,300.00 | gross (no relief) | PwC |

- **Relief scope** — Relief reduces only the pension base, not the health or income-tax computation directly. Above EUR 1,300 there is no reduction.  _(key_rules; PwC)_

### Rule 3 -- Employer health contribution

- **Employer health contribution** — Employer pays 16.5% health insurance on the FULL gross salary, on top of the gross wage. The health base is NOT capped. This is the ONLY mandatory employer "according to base" contribution: since the 2019 reform it absorbed the former 1.7% unemployment and 0.5% occupational-injury contributions, which are no longer levied separately. There is NO employer pension contribution -- all pension (20%) is employee-side. Do NOT add separate unemployment/injury lines.  _(PwC; Porezna uprava 7319)_

### Rule 4 -- Contribution base caps

- **Contribution base caps** — Monthly pension base cap = EUR 11,958.00 (= 6.0 x average gross salary EUR 1,993), applies to both Pillar I and Pillar II on salary. Annual Pillar I base cap = EUR 143,496.00 across all remuneration types. Health base uncapped.  _(PwC)_

### Rule 5 -- Income tax bands and rates (2025)

**Income tax bands and rates table**

| Band | Monthly tax base | Annual | Rate range (local) | Default |
| --- | --- | --- | --- | --- |
| Lower | up to EUR 5,000.00 | up to EUR 60,000.00 | 15%-23% | 20% |
| Higher | above EUR 5,000.00 | above EUR 60,000.00 | 25%-33% | 30% |

- **Local rate and threshold change note** — The exact rate is set by the local self-government unit; where no local rate is set, the statutory default (20% / 30%) applies. The former surtax (prirez) was abolished from 2024. The threshold was raised from EUR 50,400 to EUR 60,000 annual (EUR 4,200 to EUR 5,000 monthly) effective 1 Jan 2025.  _(Porezna uprava 7322; Deloitte)_

### Rule 6 -- Income tax base and order of operations

- **Income tax base and order of operations** — PIT_base = gross_salary - employee_pension - personal_allowance PIT      = (min(PIT_base, 5,000) x lower_rate) + (max(PIT_base - 5,000, 0) x higher_rate)   [monthly] net_pay  = gross_salary - employee_pension - PIT
- **Personal allowance and dependants note** — Basic personal allowance is EUR 600.00/month (EUR 7,200/yr) for 2025, raised from EUR 560. Dependant allowances scale proportionally [RESEARCH GAP -- specific dependant multipliers not in research data; reviewer to confirm]. Pension contributions are deducted from gross before tax; the 16.5% health contribution is an employer cost and does NOT reduce the employee's PIT base.  _(Deloitte)_

### Rule 7 -- Local self-government rate ranges

**Local self-government rate ranges table**  _(Deloitte; Porezna uprava 7322)_

| Unit type | Lower band range | Higher band range |
| --- | --- | --- |
| Municipalities (općine) | 15%-20% | 25%-30% |
| Towns (gradovi) | 15%-21% | 25%-31% |
| Cities / county seats | 15%-22% | 25%-32% |
| City of Zagreb | 15%-23% | 25%-33% |

- **Default when local rate unknown** — Use the actual local rate where known; otherwise apply the conservative default 20%/30%.  _(Porezna uprava 7322)_

### Rule 8 -- JOPPD filing and payment timing

- **JOPPD filing and payment timing** — Employers calculate, withhold, and remit employee pension (20%), withheld income tax, and pay the employer health contribution (16.5%) via the monthly electronic JOPPD report. Contributions and tax are due at the same time as the salary payment. JOPPD is filed by the day of salary payment at the latest; for salary not paid on time, the statutory due date is commonly cited as the 15th of the following month [RESEARCH GAP -- late-salary JOPPD due date to confirm against Pravilnik]. There is NO separate contributions return.  _(forms; Porezna uprava 7319)_

### Rule 9 -- Minimum wage and floor base

- **Minimum wage and floor base** — Minimum gross wage for 1 Jan-31 Dec 2025 is EUR 970.00/month. The lowest full-time monthly contribution base is EUR 757.34 (= 0.38 x EUR 1,993); full-time contributions cannot be computed on a base below this. Minimum wage rises to EUR 1,050 from 1 Jan 2026 -- do NOT use for 2025.  _(Deloitte; FINaCRO/Pravilnik)_

### Rule 10 -- First-job health-contribution relief

- **First-job health-contribution relief** — Employers get up to one year of relief from the 16.5% health contribution for a first-time permanent (indefinite) employment contract. The prior employer health-contribution exemption for hiring under-30s was abolished from 2025. Apply only on confirmation that the contract qualifies.  _(Deloitte)_

### Rule 11 -- Annual income tax return and auto-assessment

- **Annual income tax return and auto-assessment** — Most employees are auto-assessed by the Tax Administration's special procedure (poseban postupak). The annual personal income tax return is required only for those obliged to file, due by the end of February of the year following the tax year.  _(Porezna uprava 7322)_

## Section 6 -- Tier 2 catalogue

When payroll data is ambiguous or client circumstances are unclear, flag these situations for reviewer confirmation.

### T2-1 -- Pillar II membership for older or pre-2002 workers

- **T2-1** — **Trigger:** Employee may pre-date the 2002 pension reform or be over the relevant age cut-off; Pillar II status unconfirmed. **Issue:** Total pension is always 20%, but the 15%/5% split applies only to mandatory Pillar II members; non-members put the full 20% in Pillar I. Net pay is unaffected, but JOPPD allocation differs. [RESEARCH GAP -- entry-year/age rule inferred from the reform framework; reviewer to confirm.] **Action:** Flag for reviewer. Confirm Pillar II status with HZMO / the pension fund before allocating.

### T2-2 -- Local self-government income tax rate

- **T2-2** — **Trigger:** The employee's municipality/town/city is unknown, or the local rate has not been confirmed. **Issue:** Local rates range from 15% to 23% (lower) and 25% to 33% (higher). Using the wrong rate misstates net pay and withholding. **Action:** Apply the conservative default 20%/30% and flag for reviewer to confirm the actual local rate.  _(Porezna uprava 7322)_

### T2-3 -- Dependant and special personal allowances

- **T2-3** — **Trigger:** Employee claims dependant children/spouse, disability, or other personal-allowance increases. **Issue:** Dependant multipliers scale the basic EUR 600/month allowance, materially changing the PIT base. The specific multipliers are not in the research data. **Action:** Flag for reviewer. Apply basic EUR 600 only until dependant entitlements are confirmed. [RESEARCH GAP -- dependant multipliers to confirm.]

### T2-4 -- First-job / hiring reliefs

- **T2-4** — **Trigger:** Employer claims relief from the 16.5% health contribution (first-time permanent contract) or any other hiring incentive. **Issue:** First-job health relief lasts up to one year and requires a qualifying first-ever permanent contract; the under-30 employer exemption was abolished from 2025 (Deloitte). **Action:** Flag for reviewer to confirm eligibility and the relief period before excluding the 16.5% cost.  _(Deloitte)_

### T2-5 -- Self-employed / sole proprietor (obrt) bases

- **T2-5** — **Trigger:** Client is an obrtnik (sole proprietor), paušalist (flat-rate taxpayer), or otherwise self-employed. **Issue:** Minimum monthly bases differ (e.g. obrtnik dohodaš approx EUR 1,295.45 = 0.65 x EUR 1,993 for 2025), with contributions at the same rates but a different base regime (FINaCRO/Pravilnik). **Action:** Flag for reviewer. This skill computes employment payroll only.  _(FINaCRO/Pravilnik)_

### T2-6 -- Low-salary relief near a threshold edge

- **T2-6** — **Trigger:** Gross salary sits near EUR 700 or EUR 1,300, or the period is not 2025. **Issue:** The relief formula has discontinuities at the band edges, and the thresholds may be re-indexed in other years. **Action:** Flag for reviewer. Confirm the applicable-year thresholds and that the gross does not fall below the EUR 757.34 floor base (FINaCRO/Pravilnik).  _(FINaCRO/Pravilnik)_

### T2-7 -- Cross-border, posted, and non-resident workers

- **T2-7** — **Trigger:** Worker is posted, holds an A1 certificate, is a non-resident, or is covered by a social security treaty. **Issue:** EU coordination (Reg. 883/2004) and treaties can shift the contribution liability to another state. **Action:** Flag for reviewer. [RESEARCH GAP -- cross-border rules outside research scope.]

## Section 7 -- Excel working paper template

When producing a Croatian payroll/contribution computation, structure the working paper as follows:

```
CROATIA PAYROLL / CONTRIBUTIONS -- WORKING PAPER
Client / Employer: [name]
Employee: [name]
Tax Year: 2025
Period (month): [____]
Prepared: [date]

INPUT DATA
  Gross monthly salary (bruto):        EUR [____]
  Member of Pillar II:                 [YES/NO]
  Residence municipality / local unit: [____]
  Local PIT rates (lower / higher):    [____% / ____%]  (default 20% / 30%)
  Dependants / special allowance:       [____]
  First-job health relief:              [YES/NO]

PENSION (EMPLOYEE)
  Low-salary relief band:               [<=700 / 700.01-1300 / >1300]
  Relief-adjusted gross:                EUR [____]
  Pension base (floor 757.34,
    cap 11,958.00):                     EUR [____]
  Pillar I  (15% or full 20%):          EUR [____]
  Pillar II (5% or 0):                  EUR [____]
  Employee pension total (20%):         EUR [____]

INCOME TAX (PIT)
  Personal allowance:                   EUR 600.00  (+ dependants [____])
  PIT base (gross - pension
    - allowance):                       EUR [____]
  Lower band (<= 5,000) @ [20%]:        EUR [____]
  Higher band (> 5,000) @ [30%]:        EUR [____]
  Total PIT:                            EUR [____]

NET PAY
  Net = gross - pension - PIT:          EUR [____]

EMPLOYER COST
  Health 16.5% (uncapped,
    less any first-job relief):         EUR [____]
  Total employer cost (gross + health): EUR [____]

JOPPD ALLOCATION / REMITTANCE
  Pension Pillar I:                     EUR [____]
  Pension Pillar II:                    EUR [____]
  Income tax:                           EUR [____]
  Health (employer):                    EUR [____]
  Annual Pillar I cap watch (143,496):  [running total]

REVIEWER FLAGS
  [List any Tier 2 flags / RESEARCH GAP markers here]

CONSERVATIVE DEFAULTS APPLIED
  [List any defaults applied -- e.g. 20%/30% default rates, Pillar II assumed]
```

## Section 8 -- Bank statement reading guide

### How payroll remittances appear on Croatian bank statements

Croatian payroll involves several distinct outgoing legs settled around the salary-payment date: net salary to the employee, withheld income tax, employee pension contributions (Pillar I/II), and the employer health contribution -- all reported on a single JOPPD form. Banks include Zagrebačka banka (ZABA), Privredna banka Zagreb (PBZ), Erste, OTP, and Raiffeisen (RBA).

**Pension contributions:**
- Description: "MIROVINSKO", "DOPRINOS MIO", "I. STUP"/"II. STUP", "HZMO", or a named mandatory pension fund (OMF) for Pillar II
- Timing: at salary payment; tax/contributions remitted simultaneously
- Treatment: EXCLUDE -- employee-withheld pension contribution (20% of base)

**Health contribution:**
- Description: "ZDRAVSTVENO", "DOPRINOS ZO", "HZZO"
- Timing: same cycle
- Treatment: EXCLUDE -- employer health contribution (16.5% of gross, uncapped)

**Income tax:**
- Description: "POREZ NA DOHODAK", "POREZNA UPRAVA", "DRŽAVNI PRORAČUN", "JOPPD"
- Treatment: EXCLUDE -- withheld PIT (NOT a contribution)

**Net salary:**
- Description: "PLAĆA", "NETO PLAĆA", "ISPLATA PLAĆE" with employee name
- Treatment: EXCLUDE -- salary leg (the take-home pay)

**Key identification tips:**
1. Contribution and tax remittances are outgoing (DEBIT) to the Porezna uprava / HZMO / HZZO / State Budget, never credits.
2. They recur monthly with amounts that move with gross salary changes.
3. Pension legs are employee-side (20% of base); health is employer-side (16.5% of gross, uncapped).
4. Do not confuse "POREZ NA DOHODAK" (PIT) with contributions, or with "POREZ NA DOBIT" (corporate profit tax, company-level).
5. Inbound "MIROVINA" / "BOLOVANJE" credits are benefits RECEIVED, not contributions paid.
6. Common terms: doprinosi = contributions; mirovinsko = pension; zdravstveno = health; plaća = salary; bruto = gross; neto = net; porez na dohodak = income tax; prirez = (abolished) surtax.

## Section 9 -- Onboarding fallback

If the client provides only a bank statement and no other information:

1. **Scan for payroll legs** -- identify outgoing payments matching Section 3 patterns (pension, health, PIT, net salary).
2. **Group by month** -- each payroll month should show a pension leg, a health leg, a PIT leg, and a net-salary leg.
3. **Reverse-engineer gross from the contributions (approximate only):**
   - Employee pension (20% of base): base = pension / 0.20 (then check against gross).
   - Employer health (16.5% of gross): gross approximately = health / 0.165.
   - Cross-check: if pension implies a base of exactly EUR 11,958.00, the employee is at/above the monthly cap.
   - A net around EUR 767 is consistent with the EUR 970 minimum wage after relief (Example 2); a net around EUR 1,400 with a EUR 2,000 gross at default rates (Example 1).
4. **Estimate net** using DEFAULT 20%/30% PIT and the EUR 600 allowance -- label as estimate only.
5. **Flag for reviewer:** "Payroll figures derived from bank statement amounts only. Gross salary, Pillar II status, residence municipality (and therefore local PIT rate), and any dependant allowances or reliefs have not been independently verified. Reviewer must confirm against the JOPPD filing before relying on these figures."

### Thresholds and figures (2025)

**Thresholds and figures (2025)**  _(Porezna uprava 7319; PwC; FINaCRO/Pravilnik; Deloitte; Porezna uprava 7322)_

| Item | Value | Source |
| --- | --- | --- |
| Employee pension rate (total) | 20% (15% Pillar I + 5% Pillar II) | Porezna uprava 7319 |
| Employer health rate | 16.5% (uncapped) | PwC |
| Monthly pension base cap | EUR 11,958.00 (= 6.0 x EUR 1,993) | PwC |
| Annual Pillar I base cap | EUR 143,496.00 | PwC |
| Lowest full-time monthly base | EUR 757.34 (= 0.38 x EUR 1,993) | FINaCRO/Pravilnik |
| Low-salary relief lower threshold | EUR 700.00 (base = gross - 300) | PwC |
| Low-salary relief upper threshold | EUR 1,300.00 (base = gross - 0.5 x (1,300 - gross)) | PwC |
| Income tax bracket threshold | EUR 60,000/yr (EUR 5,000/mo) | Deloitte |
| Default income tax rates | 20% lower / 30% higher | Porezna uprava 7322 |
| Basic personal allowance | EUR 600.00/mo (EUR 7,200/yr) | Deloitte |
| Minimum gross wage (2025) | EUR 970.00/mo | Deloitte |
| Average gross monthly salary reference | EUR 1,993.00 | FINaCRO/Pravilnik |
| Obrtnik dohodaš min monthly gross base | approx EUR 1,295.45 (= 0.65 x EUR 1,993) | FINaCRO/Pravilnik |
| Minimum wage 2026 (reference only) | EUR 1,050.00/mo | Deloitte |
| Income tax bracket threshold 2024 (superseded) | EUR 50,400/yr (EUR 4,200/mo) | Deloitte |

- **Employee pension rate (total)** — 20% (15% Pillar I + 5% Pillar II)  _(Porezna uprava 7319)_
- **Employer health rate** — 16.5% (uncapped)  _(PwC)_
- **Monthly pension base cap** — EUR 11,958.00 (= 6.0 x EUR 1,993)  _(PwC)_
- **Annual Pillar I base cap** — EUR 143,496.00  _(PwC)_
- **Lowest full-time monthly base** — EUR 757.34 (= 0.38 x EUR 1,993)  _(FINaCRO/Pravilnik)_
- **Low-salary relief lower threshold** — EUR 700.00 (base = gross - 300)  _(PwC)_
- **Low-salary relief upper threshold** — EUR 1,300.00 (base = gross - 0.5 x (1,300 - gross))  _(PwC)_
- **Income tax bracket threshold** — EUR 60,000/yr (EUR 5,000/mo)  _(Deloitte)_
- **Default income tax rates** — 20% lower / 30% higher  _(Porezna uprava 7322)_
- **Basic personal allowance** — EUR 600.00/mo (EUR 7,200/yr)  _(Deloitte)_
- **Minimum gross wage (2025)** — EUR 970.00/mo  _(Deloitte)_
- **Average gross monthly salary reference** — EUR 1,993.00  _(FINaCRO/Pravilnik)_
- **Obrtnik dohodaš min monthly gross base** — approx EUR 1,295.45 (= 0.65 x EUR 1,993)  _(FINaCRO/Pravilnik)_
- **Minimum wage 2026 (reference only)** — EUR 1,050.00/mo  _(Deloitte)_
- **Income tax bracket threshold 2024 (superseded)** — EUR 50,400/yr (EUR 4,200/mo)  _(Deloitte)_

### Gross-to-net illustrations (2025, default 20%/30% rates, in Pillar II)

**Gross-to-net illustrations (2025, default 20%/30% rates, in Pillar II)**  _(Porezna uprava 7322 (rates); PwC (caps/relief); Deloitte (allowance))_

| Gross/mo | Pension base | Pension 20% | PIT base | PIT | Net | Employer health 16.5% |
| --- | --- | --- | --- | --- | --- | --- |
| EUR 970 | EUR 805.00 | EUR 161.00 | EUR 209.00 | EUR 41.80 | EUR 767.20 | EUR 160.05 |
| EUR 1,300 | EUR 1,300.00 | EUR 260.00 | EUR 440.00 | EUR 88.00 | EUR 952.00 | EUR 214.50 |
| EUR 2,000 | EUR 2,000.00 | EUR 400.00 | EUR 1,000.00 | EUR 200.00 | EUR 1,400.00 | EUR 330.00 |
| EUR 8,000 | EUR 8,000.00 | EUR 1,600.00 | EUR 5,800.00 | EUR 1,240.00 | EUR 5,160.00 | EUR 1,320.00 |
| EUR 15,000 | EUR 11,958.00 | EUR 2,391.60 | EUR 12,008.40 | EUR 3,102.52 | EUR 9,505.88 | EUR 2,475.00 |

Arithmetic notes (recomputed; rates Porezna uprava 7322, caps/relief PwC, allowance Deloitte):
- EUR 970: relief base = 970 - 0.5x(1300-970)=805; pension 161; PIT base 970-161-600=209; PIT 209x20%=41.80; net 970-161-41.80=767.20.
- EUR 1,300: no relief (=1,300); pension 260; PIT base 1300-260-600=440; PIT 440x20%=88; net 1300-260-88=952.
- EUR 2,000: pension 400; PIT base 2000-400-600=1,000; PIT 1000x20%=200; net 2000-400-200=1,400.
- EUR 8,000: pension 1,600; PIT base 8000-1600-600=5,800; PIT = 5,000x20% + 800x30% = 1,000+240=1,240; net 8000-1600-1240=5,160.
- EUR 15,000: pension capped base 11,958 -> 2,391.60; PIT base 15000-2391.60-600=12,008.40; PIT = 5,000x20% + 7,008.40x30% = 1,000+2,102.52=3,102.52; net 15000-2391.60-3102.52=9,505.88.

### Forms

**Forms**  _(Porezna uprava 7319; Porezna uprava 7322)_

| Form | Purpose | Deadline | Source |
| --- | --- | --- | --- |
| JOPPD (Obrazac JOPPD) | Monthly electronic report of salaries/payments, income tax withheld and all social contributions per recipient, filed with the Tax Administration. No separate contributions return. | By the day of salary payment at the latest; contributions and tax due simultaneously with salary. Late-salary scenarios commonly cited as the 15th of the following month [RESEARCH GAP -- confirm]. | Porezna uprava 7319 |
| Annual personal income tax return / final assessment | Annual reconciliation of income tax; Tax Administration issues a special assessment (poseban postupak) automatically for most employees. | By end of February of the following year (for those obliged to file). | Porezna uprava 7322 |

- **JOPPD (Obrazac JOPPD)** — Monthly electronic report of salaries/payments, income tax withheld and all social contributions per recipient, filed with the Tax Administration. No separate contributions return.  _(Porezna uprava 7319)_
- **Annual personal income tax return / final assessment** — Annual reconciliation of income tax; Tax Administration issues a special assessment (poseban postupak) automatically for most employees.  _(Porezna uprava 7322)_

### Penalties

**Penalties**  _(PwC; Rivermate)_

| Type | Treatment | Source |
| --- | --- | --- |
| Late/missing JOPPD or late payment of contributions and tax | Administrative fines per Zakon o doprinosima and Opci porezni zakon (General Tax Act), plus statutory default interest. Specific fine amounts and the default-interest rate were NOT published on the consulted authority pages [RESEARCH GAP -- reviewer to confirm against the statutes]. | PwC |
| Undeclared work | Increased employer penalties; an unregistered employment relationship is presumed to have lasted six months, obliging the employer to pay full wages plus social contributions for that period. | Rivermate |

- **Late/missing JOPPD or late payment of contributions and tax** — Administrative fines per Zakon o doprinosima and Opci porezni zakon (General Tax Act), plus statutory default interest. Specific fine amounts and the default-interest rate were NOT published on the consulted authority pages [RESEARCH GAP -- reviewer to confirm against the statutes].  _(PwC)_
- **Undeclared work** — Increased employer penalties; an unregistered employment relationship is presumed to have lasted six months, obliging the employer to pay full wages plus social contributions for that period.  _(Rivermate)_

### Test suite

Gross EUR 2,000/mo, in Pillar II, default rates, no dependants. -> Pension EUR 400.00 (Pillar I 300 + Pillar II 100); PIT base EUR 1,000.00; PIT EUR 200.00; net EUR 1,400.00; employer health EUR 330.00.

Gross EUR 970/mo (minimum wage), in Pillar II, default rates. -> Pension base EUR 805.00 (relief); pension EUR 161.00; PIT base EUR 209.00; PIT EUR 41.80; net EUR 767.20; employer health EUR 160.05.

Gross EUR 1,300/mo, in Pillar II, default rates. -> Pension base EUR 1,300.00 (no relief at exactly 1,300); pension EUR 260.00; PIT base EUR 440.00; PIT EUR 88.00; net EUR 952.00; employer health EUR 214.50.

Gross EUR 8,000/mo, in Pillar II, default rates. -> Pension EUR 1,600.00; PIT base EUR 5,800.00; PIT = 5,000x20% + 800x30% = EUR 1,240.00; net EUR 5,160.00; employer health EUR 1,320.00.

Gross EUR 15,000/mo, in Pillar II, default rates (cap test). -> Pension base capped EUR 11,958.00; pension EUR 2,391.60; PIT base EUR 12,008.40; PIT EUR 3,102.52; net EUR 9,505.88; employer health EUR 2,475.00 (uncapped).

Gross EUR 2,000/mo, NOT in Pillar II. -> Total pension still EUR 400.00 but all to Pillar I (Pillar II EUR 0); net EUR 1,400.00 and employer health EUR 330.00 unchanged vs Test 1; only JOPPD allocation differs.

Gross EUR 600/mo (part-time, <=700 band, illustrative). -> Pension base = 600 - 300 = EUR 300.00; pension EUR 60.00; PIT base = 600 - 60 - 600 = EUR -60 -> EUR 0 (no positive PIT base); PIT EUR 0.00; net = 600 - 60 - 0 = EUR 540.00. Note: a EUR 600 full-time gross is below both the EUR 970 minimum wage and the EUR 757.34 floor base -- flag for reviewer as a part-time/edge scenario (FINaCRO/Pravilnik).

First-job permanent contract, gross EUR 2,000/mo. -> Employee pension EUR 400.00 and PIT EUR 200.00 unchanged; employer health relief may reduce the EUR 330.00 employer cost to EUR 0 for up to one year -- confirm eligibility before applying (Deloitte).

- **R-HR-SSC-1** — Net pay only known, no gross. -> STOP (R-HR-SSC-1). Do not gross up without the contractual gross.  _(Test 9)_
- **R-HR-SSC-2** — Definitive net requested, residence municipality unknown. -> R-HR-SSC-2: present default-rate (20%/30%) estimate only; flag for reviewer to confirm local rates.  _(Test 10)_

### Prohibitions

- NEVER compute Croatian net pay or employer cost without the gross monthly salary -- never reverse from net without escalation.
- NEVER add legacy unemployment (1.7%) or occupational-injury (0.5%) contributions on the employer side -- consolidated into the 16.5% health contribution since 2019 (PwC).
- NEVER apply an employer pension contribution -- all pension (20%) is employee-side; only health (16.5%) is employer-side.
- NEVER cap the employer health contribution -- its base is uncapped.
- NEVER forget the EUR 11,958.00 monthly pension base cap or the EUR 143,496.00 annual Pillar I cap for high earners.
- NEVER apply the 5% Pillar II split to a worker not confirmed in the mandatory second pillar -- allocate the full 20% to Pillar I instead (total rate unchanged).
- NEVER use the local income tax rate unless confirmed -- default to 20%/30% and flag.
- NEVER use the EUR 1,050 minimum wage or the EUR 50,400 threshold for 2025 -- those are 2026 / pre-2025 figures.
- NEVER compute a full-time contribution base below EUR 757.34.
- NEVER quantify penalties or default interest -- exact amounts are a RESEARCH GAP; escalate.
- NEVER treat inbound HZMO/HZZO credits (pensions, sickness benefit) as contributions paid.
- NEVER conflate "POREZ NA DOHODAK" (PIT) with contributions, or with "POREZ NA DOBIT" (corporate profit tax).
- NEVER present figures as definitive -- always label as estimated, pending reviewer confirmation and the actual local rate, and direct the client to the JOPPD filing and a Croatian accountant.

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
