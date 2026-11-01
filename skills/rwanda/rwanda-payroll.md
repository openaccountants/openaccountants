---
name: rwanda-payroll
description: "Rwanda payroll for 2026: PAYE on gross, RSSB pension at 6% plus 6%, maternity, medical, CBHI, unified declaration in Ishema by the 15th, quarterly PAYE option, penalties, and the 2027 pension step to 14%."
version: 0.2
jurisdiction: RW
tax_year: 2026
last_updated: 2026-11-01
review_status: pending_review
trust_label: Built by Michael Cutajar and the OpenAccountants team
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Rwanda Payroll v0.2

Tax year 2026.

## Who this applies to

Employers paying staff in cash or in kind (art 57), including foreign employers with a Rwandan presence. Exempt from PAYE: aid workers under government agreements, non-resident employees of non-resident employers with no permanent establishment, diplomats (arts 16-17).

## Rates, bands and thresholds

| Item | Amount | Tax year | Official URL |
|---|---|---|---|
| PAYE monthly bands | 0% to 60,000; 10% to 100,000; 20% to 200,000; 30% above | 2026 | https://www.rra.gov.rw/en/domestic-tax-services/employment-tax-paye/calculate-paye |
| Casual labourer | 15%; first FRW 60,000 a month at 0% (art 56) | 2026 | https://www.rra.gov.rw/fileadmin/user_upload/Income_Tax_law_of_2022.pdf |
| Second employer | 30% (art 57) | 2026 | same |
| Board member allowance | 30% (art 59) | 2026 | same |
| Pension, total | 12% from 1 January 2025; 14% from 1 January 2027; 16% 2028; 18% 2029; 20% 2030 | 2026 | https://www.minijust.gov.rw/fileadmin/user_upload/Minijust/Official_gazettes_2/______2024_Igazeti_ya_Leta/UKUBOZA-December-Decembre/OG_n___Special_of_13.12.2024__Ingano_y_umusanzu_mu_bwiteganyirize_bwa_pansiyo_butegetswe.pdf |
| Pension, split | 6% employer, 6% employee of gross | 2026 | https://imisanzu.rssb.rw/ |
| Voluntary pension | 12% of chosen salary | 2026 | https://www.rra.gov.rw/en/domestic-tax-services/rssb-contributions/pension-scheme-contribution |
| Maternity | 0.3% employer, 0.3% employee of gross | 2026 | https://www.rra.gov.rw/en/domestic-tax-services/rssb-contributions/maternity-leave-contribution |
| Medical scheme | 7.5% employer, 7.5% employee of basic salary | 2026 | https://www.rra.gov.rw/en/domestic-tax-services/rssb-contributions/medical-scheme-contribution |
| CBHI | 0.5% of net salary, employee, deducted by employer | 2026 | https://www.rra.gov.rw/en/domestic-tax-services/rssb-contributions/cbhi-contribution |
| Occupational hazards | unverified: 2% employer (old file; no official page opened states it) | 2026 | unverified |
| RSSB late surcharge | 1.5% a month for the late list, 1.5% for late payment | 2026 | https://www.rra.gov.rw/en/domestic-tax-services/rssb-contributions/declaration-payment-of-rssb-contributions |

## The base

PAYE is on gross: salary, allowances, cash reimbursements of private expenses, bonuses and benefits in kind (art 15). The exclusions in art 16 cover the employer's RSSB contribution, not the employee's. RRA's own example taxes salary plus transport plus housing with no deduction (Handbook example 28). Our earlier social contributions skill deducted employee RSSB before PAYE; that was wrong and is corrected. Contributions to a qualified pension fund are excluded up to 10% of employment income or FRW 1,200,000 a year, whichever is lower (Handbook). Terminal payments are taxed.

Order of work: gross, PAYE, pension and maternity, then CBHI on net, then medical if enrolled. Foreigners working in Rwanda are in the RSSB schemes; the annexure has category flags. Exempt employees use category E.

### Carried: Minimum Wage

**Minimum Wage**

| Item | Detail | Source |
| --- | --- | --- |
| Statutory national minimum wage | **None effective / enforceable.** The only formally established rate dates to **1974 (Frw 100/day ≈ Frw 2,440/month)** and is obsolete and not enforced | unverified |
| Practice | Wages set by **sector agreements / collective bargaining** (e.g. mining sector living wage ~Frw 1,500/day old figure) | unverified |
| Status | A statutory minimum wage has been discussed but **not yet introduced** | unverified |

> Do **not** rely on the 1974 figure as a contractual floor. Use the employee's contract and any applicable sector agreement; flag for the reviewer where no sector benchmark exists.

### Carried: Conservative Defaults

When an input is missing or ambiguous, apply the **conservative** assumption (the one that does NOT understate withholding/contributions) and FLAG it for the reviewer.

**Conservative Defaults table**

| Unknown | Conservative default | Why |
| --- | --- | --- |
| Whether employer is enrolled in medical scheme | If headcount ≥ 7 → assume **enrolled** (7.5%/7.5%); FLAG | Mandatory once registration criteria met |
| Headcount unknown | Compute **without** medical scheme but FLAG; never silently apply 15% | Avoids fabricating a 15% deduction |
| Transport allowance split | If basic vs gross not given, treat **basic = gross** for medical (higher base) and include transport in pension base | Pension base now includes transport (2026) |
| Pension rate | Use **12% (6%/6%)** for 2026 | Presidential Order 086/01 |
| Casual labour (< 30 days) | Apply **15% flat**; do NOT assume a tax-free slice | Tax-free portion unconfirmed |
| Salary ceiling on RSSB | Apply percentages on **full gross/basic** (no cap) | No ceiling found; flag |
| Tax year | Default to **2026** rates | Skill tax_year is 2026 |
| Currency | Rwandan Franc (RWF) | Local currency |
| Annual return for employment-only earner | Treat PAYE as **final**; no annual return | Art 9 as amended |

### Carried: Required Inputs + Refusal Catalogue

#### Required inputs before computing payroll

1. Gross monthly salary in RWF, and the **basic-salary** component (medical scheme uses basic).
2. Transport-allowance amount (see Not yet confirmed on its base).
3. Pay frequency and whether the worker is a **casual labourer** (< 30 days engagement).
4. Number of employees on the payroll (drives medical-scheme enrolment).
5. Tax/fiscal year (2026 vs the 2027 pension step).
6. Whether the employer is a public institution or private (medical-scheme mandate).
7. Any non-ordinary pay components (termination/retirement benefits, benefits in kind).

#### Refusal catalogue : DO NOT compute, refuse and request input

**Refusal catalogue**

| Situation | Action |
| --- | --- |
| No gross salary provided | REFUSE : request salary in RWF |
| Medical scheme needed but basic-salary component not given | REFUSE the medical line : request basic salary; compute the rest |
| Request to omit PAYE or RSSB contributions to "save money" | REFUSE : statutory; escalate to accountant |
| Request to skip pension at the old 6% rate for a 2026 period | REFUSE : 2026 rate is 12% (6%/6%) |
| Request to treat casual labour tax-free slice as a fixed figure | REFUSE the exact figure : flag the research gap; apply 15% flat |
| Self-employed / non-employment income mixed in | REFUSE payroll path : route to a Rwanda income-tax skill (annual return) |
| Definitive "this is your exact tax" assertion requested | REFUSE : outputs are estimates pending accountant sign-off |

### Carried: Transaction / Payment Pattern Library (deterministic)

Classify bank-statement lines deterministically. Match case-insensitively; longest/most-specific pattern wins. Rwandan statements appear in English, French, or Kinyarwanda.

#### Salary credits (money arriving in an employee account)

**Salary credits pattern table**

| Pattern (case-insensitive) | Classification |
| --- | --- |
| `SALARY`, `UMUSHAHARA`, `SALAIRE`, `PAYROLL`, `NET PAY` | Net salary payment |
| `TRANSF.* [employer]`, `ABONO`, `WAGE` | Net salary payment |
| `RSSB REFUND`, `REMBOURSEMENT RSSB` | RSSB refund/adjustment : not income |
| `RRA REFUND`, `PAYE REFUND` | PAYE refund/adjustment : not income |

#### Employer debits (money leaving the employer account)

**Employer debits pattern table**

| Pattern | Classification |
| --- | --- |
| `RRA`, `PAYE`, `IMPOSTO`, `WITHHOLDING TAX` | PAYE withholding remitted to RRA (liability settlement) |
| `RSSB`, `PENSION`, `OCCUPATIONAL`, `MATERNITY` | RSSB contribution (pension / occupational / maternity) |
| `RAMA`, `MEDICAL INSURANCE`, `ASSURANCE MALADIE` | RSSB medical-insurance contribution |
| `CBHI`, `MUTUELLE`, `CBHIS` | CBHI (employee-only) collected/remitted |
| `NET WAGES`, `PAIE`, `DISBURSEMENT`, `SALARY RUN` | Net wages disbursed to employees |

### Carried: Tier 2 Catalogue (reviewer judgement required)

**Tier 2 Catalogue**

| Question | Why it needs a reviewer |
| --- | --- |
| Casual-labour tax-free portion (30,000 vs 60,000) | Secondary sources conflict; only the 15% flat rate is confirmed |
| Penalty percentages (20% / 40% / 60%) | Sourced from an advisory firm summarising Law 020/2023, not RRA primary text |
| Medical-scheme remittance date (10th vs 15th) | One RRA medical page references the 10th; general RSSB deadline is the 15th |
| Absence of an RSSB salary ceiling/cap | No cap found in sources; confirm explicitly with RSSB |
| Exact maternity-base treatment of benefits in kind | "Excl. transport/termination" confirmed; in-kind edge cases not |
| Whether a specific private employer must enrol in medical scheme | Depends on ≥ 7 employees + registration criteria |

### Carried: Excel Working Paper Template

Suggested layout (one row per employee per month):

**Excel Working Paper Template table**

| Col | Header | Formula / source |
| --- | --- | --- |
| A | Employee name | input |
| B | Gross monthly salary (Frw) | input |
| C | Basic salary (Frw) | input (drives medical) |
| D | Medical-enrolled? (Y/N) | input (headcount ≥ 7 or public) |
| E | PAYE (monthly) | nested IF on B using subtract constants (6,000 / 16,000 / 36,000) |
| F | Pension employee | `=B*6%` |
| G | Maternity employee | `=B*0.3%` |
| H | Medical employee | `=IF(D="Y", C*7.5%, 0)` |
| I | CBHI base (net) | `=B - E - F - 0 - G` |
| J | CBHI employee | `=I*0.5%` |
| K | Employee deductions | `=E+F+G+H+J` |
| L | Net pay | `=B-K` |
| M | Pension employer | `=B*6%` |
| N | Occupational hazards | `=B*2%` |
| O | Maternity employer | `=B*0.3%` |
| P | Medical employer | `=IF(D="Y", C*7.5%, 0)` |
| Q | Total employer cost | `=B+M+N+O+P` |

- **PAYE formula for column E (2026, monthly)** : `=IF(B<=60000,0, IF(B<=100000, B*0.10-6000, IF(B<=200000, B*0.20-16000, B*0.30-36000)))`

### Carried: Bank Statement / Terminology Reading Guide

**Terminology Reading Guide**

| Term (English / French / Kinyarwanda) | Meaning |
| --- | --- |
| Salary / Salaire / Umushahara | Salary / wage |
| PAYE | Pay-As-You-Earn income-tax withholding |
| RRA (Rwanda Revenue Authority) | Tax authority |
| RSSB (Rwanda Social Security Board) | Social-security authority |
| Pension / Retraite | Pension scheme contribution |
| Occupational hazards / Risques professionnels | Occupational-risk scheme (employer-only) |
| Maternity / Maternité | Maternity-leave benefits scheme |
| RAMA / Medical insurance / Assurance maladie | RSSB medical-insurance scheme (basic salary) |
| CBHI / CBHIS / Mutuelle de Santé | Community-Based Health Insurance (employee-only, on net) |
| Casual labourer | Worker engaged < 30 days/year (flat 15% PAYE) |
| Net pay / Net à payer | Take-home pay after deductions |
| Transport allowance / Indemnité de transport | Allowance now in pension base (2026) |

### Carried: Onboarding Fallback

If the engagement lacks key data:

1. **No prior payroll register available** → request the last 3 months of payroll and RRA/RSSB receipts to back-solve the rates actually applied.
2. **Unknown headcount** → default medical scheme OFF, FLAG; confirm before first remittance.
3. **Unknown basic-vs-gross split** → request the contract; medical needs basic salary specifically.
4. **Unknown transport allowance** → confirm; it enters the pension base (2026) and is excluded from the maternity base.
5. **Year ambiguity** → default 2026 table/rates; switch only for periods ≥ 1 Jan of a later year (pension steps up again in 2027).


## Deadlines and filing

| Item | Deadline | Source |
|---|---|---|
| PAYE, monthly | 15th of the next month (art 57) | https://www.rra.gov.rw/en/domestic-tax-services/employment-tax-paye/pay-paye |
| PAYE, quarterly option | Turnover below FRW 200,000,000; 15 days after the quarter. RSSB stays monthly | https://www.rra.gov.rw/fileadmin/user_upload/13.1.23_OG_n___Special_of_11.01.2023_Kumenyekanisha_no_kwishyura_umusoro_ku_bihembo_n_umusoro_ku_nyongeragaciro_ku_gihembwe.pdf |
| RSSB | 15th of the next month | https://www.rra.gov.rw/en/domestic-tax-services/rssb-contributions/declaration-payment-of-rssb-contributions |

### How to declare

1. Go to www.ishema.rssb.rw, enter your phone number, log in.
2. Enter the company TIN and confirm the details, then your personal details.
3. Upload the unified annexure: one tab, Excel. For each employee: names, RSSB number, NID or passport, category (P permanent, C casual, E exempt, S second employer), Rama member Y/N, pays pension Y/N, pays maternity Y/N, pays CBHI Y/N, basic salary, benefits in kind (transport 10%, house 20%, others at market value), lump sum transport, other medical deductions, terminal benefit, retirement benefits, Ejo-Heza, other pension funds.
4. The system computes tax and contributions. Submit; you get a receipt for each item, and filing data passes to E-Tax.
5. Pay using the RRA Reference Number and amount on the receipt: mobile money, internet banking, MobiCash or a bank.

Steps from https://www.rra.gov.rw/fileadmin/Folder_for_2025/RRA_Tax_Handbook_2025_Final.pdf. RRA's page (https://www.rra.gov.rw/en/domestic-tax-services/employment-tax-paye/declare-paye) says to call 3004 or visit an office to register for the unified declaration. Separate declaration still exists.

## Penalties and interest

| Fault | Consequence | Source |
|---|---|---|
| Late declaration, fixed fine (Law 020/2023 art 81) | FRW 50,000 for a non-commercial person or turnover over FRW 2,000,000 up to FRW 20,000,000; FRW 300,000 for a public institution or non-profit with turnover over FRW 20,000,000; FRW 500,000 for a notified large taxpayer | https://www.rra.gov.rw/fileadmin/user_upload/OG_n___Special_ter_of_31.03.2023_Uburyo_bw_isoresha_Tax_procedures_01.pdf |
| Repeat fault within 2 years | Fine doubled; third time, four times | same |
| Certified statements not filed when required | FRW 500,000 every month until filed | same |
| Late declaration and payment (art 82) | 20% of tax up to 30 days, 40% from day 31 to 60, 60% after 60 days | same |
| Declared on time, paid late (art 82) | 5% up to 30 days, 10% from day 31 to 60, 30% after 60 days | same |
| Understatement of 10% to 20% (art 83) | 10% of the understatement; doubles above 20%; none if corrected and paid before notice of audit, but art 82 fines apply | same |
| Late-payment interest (art 80) | 0.5% a month up to 6 months, 1% from 6 to 12 months, 1.5% after 12 months; not compounded; every started month counts; capped at 100% of the tax | same |
| Tax evasion (art 81) | Fine equal to the evaded tax, plus criminal penalties | same |

Payments offset principal tax first, then the fine, then interest (art 80). The Law's art 82 text reads "twenty percent (10%)" for the middle band; we follow the figure 10%, as the numeric text and the 5/10/30 scale show.

RSSB: forced recovery and penal sanctions for failure to register or declare (https://www.rra.gov.rw/en/domestic-tax-services/rssb-contributions/declaration-payment-of-rssb-contributions). The employer who fails to withhold is personally liable (art 66).

## Cross-border points

An employee with a foreign employer not bound to withhold under a treaty files within 15 days of the month end (art 58). KIFC experts: see [rwanda-income-tax](rwanda-income-tax.md).

## Two worked examples that recompute

**Example 1. Gross FRW 500,000, not enrolled in medical.**

```oa-check
name: Net pay, gross FRW 500,000
inputs:
  gross: 500000
steps:
  - paye: (100000 - 60000) * 0.10 + (200000 - 100000) * 0.20 + (gross - 200000) * 0.30
  - pension: gross * 0.06
  - maternity: gross * 0.003
  - net_base: gross - paye - pension - maternity
  - cbhi: net_base * 0.005
  - net_pay: net_base - cbhi
expected:
  paye: 114000.00
  cbhi: 1772.50
  net_pay: 352727.50
```

**Example 2. Decision: budget for the 2027 pension step.** Staff bill FRW 10,000,000 gross a month. Employer pension rises from 6% to 7% if split equally, adding FRW 100,000 a month. The order sets the total at 14%; the equal split is an assumption until RSSB confirms it.

```oa-check
name: Employer pension, 2026 and 2027
inputs:
  bill: 10000000
steps:
  - y2026: bill * 0.06
  - y2027: bill * 0.07
  - rise: y2027 - y2026
expected:
  rise: 100000.00
```

## Ask the client first

1. Permanent, casual, second employer, or exempt?
2. Gross split: basic, allowances, benefits?
3. Enrolled in the medical scheme?
4. Qualified private pension or Ejo-Heza?
5. Monthly or quarterly PAYE?
6. Resident? Paid from abroad?

## Sources

| Source | URL | Read on |
|---|---|---|
| Law 027/2022 establishing taxes on income (read: arts 3-5, 8-10, 12-21, 24-33, 36-38, 44-50, 56-69) | https://www.rra.gov.rw/fileadmin/user_upload/Income_Tax_law_of_2022.pdf | 2026-11-01 |
| Law 020/2023 on tax procedures (read: arts 15, 35, 78, 80-88) | https://www.rra.gov.rw/fileadmin/user_upload/OG_n___Special_ter_of_31.03.2023_Uburyo_bw_isoresha_Tax_procedures_01.pdf | 2026-11-01 |
| Commissioner General Instructions 001/2023, quarterly PAYE and VAT (whole) | https://www.rra.gov.rw/fileadmin/user_upload/13.1.23_OG_n___Special_of_11.01.2023_Kumenyekanisha_no_kwishyura_umusoro_ku_bihembo_n_umusoro_ku_nyongeragaciro_ku_gihembwe.pdf | 2026-11-01 |
| Presidential Order 086/01 of 12/12/2024, pension rate (whole) | https://www.minijust.gov.rw/fileadmin/user_upload/Minijust/Official_gazettes_2/______2024_Igazeti_ya_Leta/UKUBOZA-December-Decembre/OG_n___Special_of_13.12.2024__Ingano_y_umusanzu_mu_bwiteganyirize_bwa_pansiyo_butegetswe.pdf | 2026-11-01 |
| RSSB, Imisanzu portal home page (whole page) | https://imisanzu.rssb.rw/ | 2026-11-01 |
| RRA, Calculate PAYE page (whole page) | https://www.rra.gov.rw/en/domestic-tax-services/employment-tax-paye/calculate-paye | 2026-11-01 |
| RRA, Pay PAYE page (whole page) | https://www.rra.gov.rw/en/domestic-tax-services/employment-tax-paye/pay-paye | 2026-11-01 |
| RRA, Declare PAYE page (whole page) | https://www.rra.gov.rw/en/domestic-tax-services/employment-tax-paye/declare-paye | 2026-11-01 |
| RRA, pension contribution page (whole page) | https://www.rra.gov.rw/en/domestic-tax-services/rssb-contributions/pension-scheme-contribution | 2026-11-01 |
| RRA, medical scheme page (whole page) | https://www.rra.gov.rw/en/domestic-tax-services/rssb-contributions/medical-scheme-contribution | 2026-11-01 |
| RRA, maternity leave page (whole page) | https://www.rra.gov.rw/en/domestic-tax-services/rssb-contributions/maternity-leave-contribution | 2026-11-01 |
| RRA, CBHI page (whole page) | https://www.rra.gov.rw/en/domestic-tax-services/rssb-contributions/cbhi-contribution | 2026-11-01 |
| RRA, declaration and payment of RSSB contributions page (whole page) | https://www.rra.gov.rw/en/domestic-tax-services/rssb-contributions/declaration-payment-of-rssb-contributions | 2026-11-01 |
| RRA Tax Handbook 2025 (read: E-Tax steps, real regime, PAYE, VAT declaration chapters) | https://www.rra.gov.rw/fileadmin/Folder_for_2025/RRA_Tax_Handbook_2025_Final.pdf | 2026-11-01 |

Not yet confirmed: occupational hazards rate 2%; the split of 14% and later pension rates; whether transport is excluded from the maternity base and included in the pension base, which the old file said on secondary sources, while RRA says gross; the medical enrolment minimum of 7 employees and 10th of the month deadline, from the old file; the exact definition of net for CBHI; the 30-day limit for casual labour; minimum wage, carried from a secondary source and not checked against the labour law; RRA Pay PAYE page lists quarters from March while CG Instructions list calendar quarters; the Instructions predate Law 020/2023.

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
