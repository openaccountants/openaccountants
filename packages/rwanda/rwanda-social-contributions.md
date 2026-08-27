---
name: rwanda-social-contributions
description: Use this skill whenever asked about Rwanda payroll taxes, PAYE, or social security / RSSB contributions for employees and employers. Trigger on phrases like "how much PAYE in Rwanda", "RSSB pension contribution", "Rwanda social security rate", "what is the pension rate 2025", "occupational hazards contribution", "maternity scheme RSSB", "CBHIS deduction", "RAMA / medical insurance scheme", "net pay calculation Rwanda", "casual labour tax rate", "Rwanda monthly declaration deadline", or any question about an employee's or employer's RSSB / RRA obligations. Also trigger when classifying bank statement transactions that relate to RRA tax payments, RSSB contribution debits, or PAYE remittances from Bank of Kigali, BPR, Equity Bank Rwanda, I&M Bank or other Rwandan banks. Also trigger when preparing or reviewing a monthly unified PAYE + RSSB declaration on E-Tax / MyRRA. This skill covers the 2025 PAYE brackets, the five RSSB schemes (pension, occupational hazards, maternity, CBHIS, medical), their differing contribution bases, the unified monthly declaration, penalties and interest under the Tax Procedures Law, expat/KIFC treatment, bank statement classification patterns, and edge cases. ALWAYS read this skill before touching any Rwanda payroll or social-contribution work.
version: 0.1
jurisdiction: RW
tax_year: 2025
last_updated: 2026-07-13
review_status: pending_review
depends_on:
  - social-contributions-workflow-base
category: international
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Rwanda PAYE & RSSB Social Contributions

## Rwanda PAYE & RSSB Social Contributions Skill v0.1

> Rwanda **does** levy personal income tax. This is a standard PAYE + social-insurance jurisdiction. Payroll obligations are filed jointly to the **Rwanda Revenue Authority (RRA)** and the **Rwanda Social Security Board (RSSB)** via a single monthly declaration on **E-Tax / MyRRA**.

## Section 1 -- Quick reference

**Read this whole section before computing or classifying anything.**

**Quick reference table**

| Field | Value |
| --- | --- |
| Country | Republic of Rwanda |
| Tax year | Calendar year (1 Jan -- 31 Dec) |
| Currency | RWF (Rwandan Franc) -- RWF only |
| PAYE legislation | Law No. 027/2022 of 20/10/2022 establishing taxes on income, Art. 56 (PwC Rwanda -- Individual income tax) |
| Procedures / penalties | Tax Procedures Law No. 020/2023 (effective 1 April 2023) |
| Tax authority | Rwanda Revenue Authority (RRA) |
| Social security board | Rwanda Social Security Board (RSSB) |
| Filing portal | E-Tax / MyRRA (unified PAYE + RSSB declaration) |
| PAYE basis | Progressive monthly brackets; residents on worldwide income, non-residents on Rwanda-sourced income (PwC Rwanda -- Taxes on personal income) |
| Casual labour rate | Flat 15% (PwC Rwanda -- Taxes on personal income) |
| Pension (2025) | 6% employee + 6% employer = 12% of gross (PwC Rwanda -- Other taxes) |
| Occupational hazards | 0% employee + 2% employer of gross (PwC Rwanda -- Other taxes) |
| Maternity | 0.3% employee + 0.3% employer of gross excl. transport (PwC Rwanda -- Other taxes) |
| CBHIS | 0.5% employee + 0% employer of net salary (PwC Rwanda -- Other taxes) |
| Medical (RAMA, if enrolled) | 7.5% employee + 7.5% employer of basic salary (RRA -- Medical Insurance Scheme) |
| Monthly declaration deadline | 15th of the following month (PwC Rwanda -- Tax administration) |
| Medical scheme payment deadline | 10th of the following month (RRA -- Medical Insurance Scheme) |
| Annual individual return | 31 March following the tax period (PwC Rwanda -- Tax administration) |
| Validated by | Pending -- requires sign-off by a Rwandan licensed accountant / RRA-registered tax agent |
| Validation date | Pending |

**RSSB scheme overview (2025)**  _(PwC Rwanda -- Corporate "Other taxes" (https://taxsummaries.pwc.com/rwanda/corporate/other-taxes); PwC sample personal income tax calculation (https://taxsummaries.pwc.com/rwanda/individual/sample-personal-income-tax-calculation); RRA -- Medical Insurance Scheme)_

| Scheme | Employee | Employer | Total | Contribution base |
| --- | --- | --- | --- | --- |
| Pension | 6% | 6% | 12% | Gross salary (incl. transport allowance from 1 Jan 2025) |
| Occupational hazards | 0% | 2% | 2% | Gross salary |
| Maternity leave benefits | 0.3% | 0.3% | 0.6% | Gross pay excl. transport & termination/retirement benefits |
| CBHIS (community health) | 0.5% | 0% | 0.5% | Net salary (gross + benefits less PAYE, pension, occ. hazards, maternity) |
| Medical (RAMA, if enrolled) | 7.5% | 7.5% | 15% | Basic salary |

*Arithmetic check: Pension 6+6=12; Occ. hazards 0+2=2; Maternity 0.3+0.3=0.6; CBHIS 0.5+0=0.5; Medical 7.5+7.5=15. Each total row equals the sum of its components.*
Source for the full breakdown: PwC Rwanda -- Corporate "Other taxes" (https://taxsummaries.pwc.com/rwanda/corporate/other-taxes) and the PwC sample personal income tax calculation (https://taxsummaries.pwc.com/rwanda/individual/sample-personal-income-tax-calculation). Medical scheme: RRA -- Medical Insurance Scheme (https://www.rra.gov.rw/en/details?tx_news_pi1%5Baction%5D=detail&tx_news_pi1%5Bcontroller%5D=News&tx_news_pi1%5Bnews%5D=469&cHash=dc8044c4d18d710cf5ab2cc68f2283b4).

- **Note on differing bases** — This is the single most error-prone feature of Rwanda payroll: the four mandatory schemes use different contribution bases. Pension and occupational hazards are on gross; maternity is on gross excluding transport; CBHIS is on net (after PAYE and the other deductions); medical (RAMA) is on basic salary. Do not apply one base across all schemes.

**Conservative defaults**

| Ambiguity | Default |
| --- | --- |
| Unknown whether transport allowance is paid | Assume transport is part of gross (pension base now includes it from 2025); flag for reviewer |
| Unknown whether employer is RAMA/medical-enrolled | Assume NOT enrolled (medical is mandatory only for civil servants; private opt-in needs ≥7 employees); flag for reviewer |
| Unknown residency status | Assume resident (taxed on worldwide income); flag for reviewer to confirm |
| Unknown whether worker is casual labour | Assume regular employee on progressive brackets, not the 15% flat rate; flag |
| Unknown basic vs gross split | Cannot compute medical contribution; STOP and request the basic-salary figure |
| Ambiguous RRA/RSSB bank debit (tax vs penalty) | Classify as statutory remittance; flag for reviewer |
| KIFC foreign-income exemption claimed | Do not apply; escalate to reviewer (case-specific licensing required) |

## Section 2 -- PAYE brackets and rates (2025)

Progressive **monthly** brackets, in force since November 2023 (Law No. 027/2022 of 20/10/2022, Art. 56 second-year rates, still current for 2025). Source: RRA "new rates" guide (https://www.rra.gov.rw/en/details?tx_news_pi1%5Baction%5D=detail&tx_news_pi1%5Bcontroller%5D=News&tx_news_pi1%5Bnews%5D=1669&cHash=8a281f98a1e1d9501765985f3a91fe8d) and PwC Rwanda -- Taxes on personal income (https://taxsummaries.pwc.com/rwanda/individual/taxes-on-personal-income).

**PAYE brackets 2025**  _(RRA new rates guide; PwC Rwanda -- Taxes on personal income)_

| Monthly taxable income (RWF) | Rate | Tax on this band | Cumulative tax at top of band |
| --- | --- | --- | --- |
| 0 -- 60,000 | 0% | 0 | 0 |
| 60,001 -- 100,000 | 10% | 4,000 | 4,000 |
| 100,001 -- 200,000 | 20% | 20,000 | 24,000 |
| 200,001 and above | 30% | — | — |

*Cumulative check: band 2 = 10% × 40,000 = 4,000 → cumulative 4,000. Band 3 = 20% × 100,000 = 20,000 → cumulative 24,000. Consistent.*

- **PAYE shortcut formula** — If B <= 60,000        PAYE = 0 If 60,001..100,000    PAYE = (B - 60,000) * 0.10 If 100,001..200,000   PAYE = 4,000 + (B - 100,000) * 0.20 If B >= 200,001       PAYE = 24,000 + (B - 200,000) * 0.30  _(RRA new rates guide; PwC Rwanda -- Taxes on personal income)_
- **Casual labour rate** — 15% (flat, special rate; not the progressive brackets)  _(PwC Rwanda -- Taxes on personal income)_
- **PAYE taxable base** — PAYE taxable base = gross employment income less the employee's deductible social-security contributions (pension, occupational hazards, maternity).  _(PwC Rwanda -- Taxes on personal income (social security deductible before PAYE) and the PwC sample calculation)_
- **Residency** — Residents taxed on worldwide income; non-residents on Rwanda-sourced income. No local/municipal income taxes.  _(PwC Rwanda -- Taxes on personal income)_
- **KIFC exemption** — New residents in Kigali International Financial Centre--licensed activities may be exempt from PIT on foreign-sourced income for their first 5 years. Do not auto-apply -- case-specific; escalate.  _(PwC Rwanda -- Taxes on personal income)_

## Section 3 -- Required inputs and refusal catalogue

### Required inputs

**Minimum viable** -- gross monthly salary and whether a transport allowance is included. Without the gross figure, STOP.

**Recommended** -- the basic-salary component (needed if medical/RAMA applies), the transport-allowance amount (excluded from the maternity base), residency status, and whether the worker is a regular employee or casual labour.

**Ideal** -- the employer's RSSB registration status and which schemes apply (medical/RAMA optional), the E-Tax/MyRRA monthly declaration, and bank statements showing RRA/RSSB remittances.

### Refusal catalogue

- **R-RW-1 -- Medical (RAMA) contribution without basic salary** — Trigger: employer is RAMA-enrolled but only the gross figure is supplied. Message: "The medical scheme contribution (7.5% employee + 7.5% employer) is computed on basic salary, not gross. Cannot compute without the basic-salary component."
- **R-RW-2 -- KIFC foreign-income exemption** — Trigger: client claims the 5-year KIFC exemption on foreign-sourced income. Message: "The KIFC PIT exemption depends on holding a qualifying KIFC licence and on the source/timing of the income. This is case-specific and outside the scope of this skill. Escalate to a Rwandan licensed accountant / RRA-registered tax agent."
- **R-RW-3 -- Arrears, penalties and interest** — Trigger: client has unpaid PAYE/RSSB and asks for the total owed. Message: "Late-payment interest (0.5%--1.5%/month, capped at 100% of annual tax) and administrative fines (5%--30%, plus a possible 60% non-declaration penalty) under Tax Procedures Law No. 020/2023 depend on the exact delay and turnover band. Do not estimate. Request an RRA statement and escalate to a reviewer."  _(Tax Procedures Law No. 020/2023)_
- **R-RW-4 -- Pension phased increases beyond 2025** — Trigger: client asks for pension contributions for 2027 onward. Message: "The scheduled pension step-ups (7% each from 2027 up to 10% each by 2030) are reported by PwC but I have not confirmed the underlying RSSB ministerial order text. Treat the 2025 6%+6% rate as firm; flag future years for reviewer confirmation. [RESEARCH GAP -- reviewer to confirm 2027--2030 steps against the RSSB order.]"
- **R-RW-5 -- Minimum wage** — Trigger: client asks for the national minimum wage. Message: "Rwanda has no enforceable national minimum wage; the 1974 statutory rate is obsolete and effective wages are set by sector/collective agreement. The widely cited ~RWF 60,000/month figure is unconfirmed press/HR-guide speculation. [RESEARCH GAP -- no gazetted statutory rate; reviewer to confirm.]"

## Section 4 -- Payment pattern library

Deterministic pre-classifier for bank statement transactions related to Rwanda payroll taxes and RSSB. When a transaction matches a pattern below, apply the treatment directly. Match by case-insensitive substring on the counterparty/reference. RRA tax and RSSB contributions are statutory remittances -- always EXCLUDE from any VAT return or revenue/expense P&L classification beyond their proper payroll-liability treatment.

### 4.1 RRA tax remittances (PAYE and other)

**RRA tax remittances patterns**

| Pattern | Treatment | Notes |
| --- | --- | --- |
| RRA, RWANDA REVENUE AUTHORITY | EXCLUDE -- statutory tax remittance | PAYE / income tax / VAT payment to RRA |
| PAYE, P.A.Y.E | EXCLUDE -- employee income tax remitted | Monthly PAYE |
| E-TAX, MYRRA, ETAX | EXCLUDE -- RRA portal payment | Unified declaration settlement |
| IMISORO, UMUSORO | EXCLUDE -- tax (Kinyarwanda "umusoro" = tax) | Generic tax reference |

### 4.2 RSSB social-contribution remittances

**RSSB contribution patterns**

| Pattern | Treatment | Notes |
| --- | --- | --- |
| RSSB, RWANDA SOCIAL SECURITY BOARD | EXCLUDE -- social contribution remittance | Pension / occ. hazards / maternity / CBHIS |
| PENSION, RETIREMENT CONTRIB | EXCLUDE -- pension contribution | RSSB pension scheme |
| RAMA, MEDICAL SCHEME, ASSURANCE MALADIE | EXCLUDE -- medical scheme | RSSB medical (formerly RAMA) |
| CBHI, CBHIS, MUTUELLE, MUTUELLE DE SANTE | EXCLUDE -- community health contribution | Community-Based Health Insurance |
| KUBAKA, IMITURIRE (transport allowance ref) | Component of gross -- see base notes | Affects pension/maternity bases |

### 4.3 Rwandan bank debit descriptions

**Bank debit descriptions**

| Bank | Typical debit description | Treatment |
| --- | --- | --- |
| Bank of Kigali (BK) | "RRA TAX", "RSSB CONTRIB", "PAYE" | EXCLUDE -- statutory remittance |
| BPR Bank (Atlas Mara / BPR) | "RWANDA REVENUE", "RSSB" | EXCLUDE -- statutory remittance |
| Equity Bank Rwanda | "RRA E-TAX", "RSSB PENSION" | EXCLUDE -- statutory remittance |
| I&M Bank Rwanda | "RRA", "SOCIAL SECURITY" | EXCLUDE -- statutory remittance |
| Mobile money (MoMo / Airtel Money) | "RRA PAYMENT", "RSSB" | EXCLUDE -- statutory remittance |

### 4.4 Payroll and benefits received (not contributions)

**Payroll/benefit patterns**

| Pattern | Treatment | Notes |
| --- | --- | --- |
| SALARY, UMUSHAHARA (outgoing) | EXCLUDE -- payroll expense | Net wage paid to employee, not a contribution |
| RSSB PENSION (incoming credit) | EXCLUDE -- pension benefit received | Inbound benefit, not a contribution paid |
| MATERNITY BENEFIT (incoming) | EXCLUDE -- benefit received | Not a contribution |

## Section 5 -- Worked examples

Five payroll computations and bank-statement classifications for a hypothetical Kigali employer and its staff. All figures in RWF. The employer is not RAMA-enrolled unless stated (so no 7.5% medical) — the four mandatory schemes apply.

### Example 1 -- Standard salaried employee, full computation

**Input:** Gross monthly salary RWF 500,000, of which transport allowance RWF 30,000. Resident, regular employee, employer not RAMA-enrolled.

**Step 1 -- Employee social security (deductible before PAYE):**
- Pension EE = 6% × 500,000 = **30,000** (base: gross incl. transport)
- Occupational hazards EE = 0% × 500,000 = **0**
- Maternity EE = 0.3% × (500,000 − 30,000) = 0.3% × 470,000 = **1,410** (base: gross excl. transport)

**Step 2 -- PAYE taxable base:** 500,000 − 30,000 − 0 − 1,410 = **468,590**

**Step 3 -- PAYE** (B = 468,590, top band): 24,000 + 0.30 × (468,590 − 200,000) = 24,000 + 0.30 × 268,590 = 24,000 + 80,577 = **104,577**

**Step 4 -- CBHIS** (base = net = gross − PAYE − pension − occ. hazards − maternity): 500,000 − 104,577 − 30,000 − 0 − 1,410 = 364,013; CBHIS EE = 0.5% × 364,013 = **1,820.07**

**Step 5 -- Net pay:** 500,000 − 30,000 − 1,410 − 104,577 − 1,820.07 = **362,192.93**

**Employer-side cost on top of gross:** pension ER 6% × 500,000 = 30,000; occ. hazards 2% × 500,000 = 10,000; maternity ER 0.3% × 470,000 = 1,410. Employer total = **41,410**.

**Classification:** the RRA PAYE remittance of 104,577 and the RSSB contributions are EXCLUDE -- statutory remittances on the unified monthly declaration (due 15th of next month).

### Example 2 -- Low earner below the PAYE threshold

**Input:** Gross monthly salary RWF 55,000, no transport allowance. Regular employee, not RAMA-enrolled.

**Reasoning:**
- Pension EE = 6% × 55,000 = 3,300; occ. hazards EE = 0; maternity EE = 0.3% × 55,000 = 165.
- PAYE base = 55,000 − 3,300 − 165 = 51,535 → **below 60,000 → PAYE = 0**.
- CBHIS net base = 55,000 − 0 − 3,300 − 0 − 165 = 51,535; CBHIS EE = 0.5% × 51,535 = 257.675 ≈ **257.68**.
- Net pay = 55,000 − 3,300 − 165 − 0 − 257.68 = **51,277.32**.

**Classification:** No PAYE due this month, but RSSB contributions still apply and must be declared.

### Example 3 -- Casual labourer (flat 15%)

**Input:** Casual worker paid RWF 80,000 for a short engagement.

**Reasoning:** Casual labour uses the flat 15% special rate, not the progressive brackets. PAYE = 15% × 80,000 = **12,000**. (RSSB treatment of casual labour is case-specific; flag for reviewer whether the engagement triggers RSSB registration.)

**Classification:** RRA remittance of 12,000 -- EXCLUDE, statutory tax remittance. Flag RSSB applicability.

### Example 4 -- RRA/RSSB bank debit on the unified declaration

**Input line:**
`13.02.2025 ; RWANDA REVENUE AUTHORITY ; DEBIT ; E-TAX PAYE+RSSB JAN 2025 ; -145,987 ; RWF`

**Reasoning:** Matches "RWANDA REVENUE AUTHORITY" / "E-TAX" (patterns 4.1). This is the January 2025 unified PAYE + RSSB declaration settled before the 15 Feb deadline. EXCLUDE from VAT/P&L; it clears the payroll statutory liabilities.

**Classification:** EXCLUDE -- statutory remittance (PAYE + RSSB). Paid on time (before 15th).

### Example 5 -- Ambiguous RSSB debit (possible penalty/arrears)

**Input line:**
`28.03.2025 ; RSSB CONTRIB ; DEBIT ; ARREARS + INTEREST ; -512,300 ; RWF`

**Reasoning:** Matches "RSSB" (pattern 4.2) but the reference says "ARREARS + INTEREST" and the amount is irregular. Under Tax Procedures Law No. 020/2023, late payment carries interest (0.5%--1.5%/month, capped at 100% of annual tax) plus administrative fines (5%/10%/30%). Cannot separate principal from interest/penalty without an RRA/RSSB statement.

**Classification:** EXCLUDE from VAT. Flag for reviewer -- request the RRA/RSSB breakdown to split contribution principal from interest and penalty.

## Section 6 -- Tier 1 rules

Apply exactly as written when inputs are clear.

### Rule 1 -- Compute employee social security first, then PAYE

- **Order of computation** — Deduct pension, occupational hazards and maternity (employee shares) from gross to get the PAYE taxable base. CBHIS is computed after PAYE (it sits on net).  _(PwC Rwanda -- sample personal income tax calculation)_

### Rule 2 -- Use the correct base per scheme

- **Contribution bases** — Pension & occupational hazards → gross. Maternity → gross excl. transport & termination/retirement benefits. CBHIS → net (gross + benefits − PAYE − pension − occ. hazards − maternity). Medical/RAMA → basic salary.  _(PwC Rwanda -- Other taxes; RRA -- Medical Insurance Scheme)_

### Rule 3 -- Pension is 6% + 6% in 2025 and includes transport

- **Pension rate and base 2025** — From 1 Jan 2025 the pension rate is 6% employee + 6% employer (doubled from 3%+3%), and the base now includes the transport allowance (harmonised with the PAYE base). Future step-ups (2027--2030) are scheduled but unconfirmed at source — see Rule 11.  _(PwC Rwanda -- Other taxes)_

### Rule 4 -- Occupational hazards is employer-only

- **Occupational hazards** — 2% employer, 0% employee, on gross. Never deduct it from the employee.  _(PwC Rwanda -- Other taxes)_

### Rule 5 -- Maternity is 0.3% each, excluding transport

- **Maternity** — 0.3% employee + 0.3% employer on gross excluding transport and termination/retirement benefits.  _(PwC Rwanda -- Other taxes)_

### Rule 6 -- CBHIS is employee-only on net

- **CBHIS** — 0.5% employee, 0% employer, on net salary as defined in Rule 2.  _(PwC Rwanda -- Other taxes)_

### Rule 7 -- Medical (RAMA) only if enrolled

- **Medical/RAMA** — 7.5% employee + 7.5% employer on basic salary, due by the 10th of the following month. Mandatory for civil servants (automatic). Private institutions may opt in but must enrol all employees and need at least 7 employees. If enrolment is unknown, assume not enrolled and flag.  _(RRA -- Medical Insurance Scheme)_

### Rule 8 -- PAYE brackets are monthly and progressive

- **PAYE brackets** — 0% to 60,000; 10% on 60,001--100,000; 20% on 100,001--200,000; 30% above 200,000. Casual labour is a flat 15%.  _(RRA new-rates guide; PwC Rwanda -- Taxes on personal income)_

### Rule 9 -- Residency drives scope

- **Residency scope** — Residents: worldwide income. Non-residents: Rwanda-sourced only. No local income taxes.  _(PwC Rwanda -- Taxes on personal income)_

### Rule 10 -- Unified monthly declaration deadline

- **Filing deadlines** — PAYE + RSSB (except voluntary pension) are declared and paid via E-Tax/MyRRA by the 15th of the following month. RSSB medical itself is due the 10th. Annual individual return due 31 March of the following year.  _(PwC Rwanda -- Tax administration; RRA PAYE declaration page (https://www.rra.gov.rw/en/domestic-tax-services/employment-tax-paye/declare-paye))_

### Rule 11 -- Treat 2025 rates as firm; flag future years

- **Pension future rates** — The 2025 6%+6% pension rate is firm. The scheduled increases (7% each in 2027, 8% in 2028, 9% in 2029, 10% in 2030) come from PwC only and lack confirmed primary-order text. Do not apply them silently. [RESEARCH GAP -- reviewer to confirm 2027--2030 steps.]

## Section 7 -- Tier 2 catalogue (reviewer judgement)

Flag these for reviewer confirmation.

### T2-1 -- Transport allowance treatment

- **Transport allowance** — Trigger: the gross/transport split is unclear or transport is paid as a separate line. Issue: transport is included in the pension base (from 2025) but excluded from the maternity base. Mis-classifying it shifts both contributions and the PAYE base. Action: confirm the exact transport amount before computing.

### T2-2 -- Medical (RAMA) enrolment

- **Medical enrolment** — Trigger: employer's RSSB medical enrolment status unknown, or fewer than 7 employees. Issue: medical is mandatory only for civil servants; private opt-in requires all-employee enrolment and ≥7 staff. The base is basic salary, not gross. Action: confirm enrolment and obtain the basic-salary figure.

### T2-3 -- Casual labour vs regular employment

- **Casual vs regular** — Trigger: short-term or irregular engagement. Issue: casual labour is taxed at flat 15%; RSSB applicability is case-specific. Action: confirm engagement nature; flag RSSB registration question.

### T2-4 -- Expatriate / KIFC foreign-income exemption

- **KIFC exemption** — Trigger: non-resident or KIFC-licensed taxpayer with foreign-sourced income. Issue: the 5-year KIFC PIT exemption on foreign income is licence- and source-dependent. Action: escalate; do not auto-apply the exemption.

### T2-5 -- Arrears, interest and penalties

- **Arrears/penalties** — Trigger: unpaid PAYE/RSSB from prior periods. Issue: interest 0.5%--1.5%/month (capped at 100% of annual tax) plus 5%/10%/30% administrative fines and a possible 60% non-declaration penalty. Action: do not estimate; request an RRA statement; escalate.

### T2-6 -- Future-year pension step-ups

- **Future step-ups** — Trigger: computation requested for 2027 onward. Issue: scheduled 7%--10% step-ups are unconfirmed at primary source. Action: flag; confirm against the RSSB ministerial order before applying.

## Section 8 -- Excel working paper template

RWANDA PAYROLL / RSSB COMPUTATION -- WORKING PAPER
Client: [name]            Employee: [name]
Tax Period (month/year):  [____]
Prepared: [date]

INPUT DATA
  Gross monthly salary (RWF):        [____]
  Transport allowance (RWF):         [____]
  Basic salary (RWF, for medical):   [____]
  Residency:                         [Resident / Non-resident]
  Worker type:                       [Regular employee / Casual labour]
  RAMA / medical enrolled:           [YES / NO]

EMPLOYEE SOCIAL SECURITY (deductible before PAYE)
  Pension EE        6%  x gross:               [____]
  Occ. hazards EE   0%  x gross:               0
  Maternity EE      0.3% x (gross - transport): [____]
  Subtotal EE social security (pre-PAYE):      [____]

PAYE
  PAYE taxable base (gross - subtotal above):  [____]
  PAYE (progressive brackets / 15% casual):    [____]

CBHIS (on net)
  Net base = gross - PAYE - pension - occ.haz - maternity: [____]
  CBHIS EE 0.5% x net base:                    [____]

MEDICAL (if enrolled)
  Medical EE 7.5% x basic:                     [____]
  Medical ER 7.5% x basic:                     [____]

NET PAY = gross - pension EE - maternity EE - PAYE - CBHIS [- medical EE]: [____]

EMPLOYER COST ON TOP OF GROSS
  Pension ER 6% x gross:                       [____]
  Occ. hazards ER 2% x gross:                  [____]
  Maternity ER 0.3% x (gross - transport):     [____]
  Medical ER 7.5% x basic (if enrolled):       [____]
  Employer total:                              [____]

FILING
  Unified PAYE+RSSB declaration due (15th):     [____]
  Medical scheme payment due (10th):            [____]

REVIEWER FLAGS
  [List any Tier 2 flags here]

CONSERVATIVE DEFAULTS APPLIED
  [List any defaults applied and their impact]

## Section 9 -- Bank statement reading guide

### How Rwanda payroll remittances appear

**Bank of Kigali (BK):**
- Description: "RRA TAX", "RRA E-TAX", "PAYE", "RSSB CONTRIB", "RSSB PENSION"
- Timing: around the 10th (medical) and by the 15th (unified declaration) of the following month
- Amount: the monthly PAYE + RSSB total per the declaration

**BPR / Equity Bank Rwanda / I&M Bank Rwanda:**
- Description: "RWANDA REVENUE", "RRA", "RSSB", "SOCIAL SECURITY", "MUTUELLE / CBHI"
- Timing: same monthly cycle

**Mobile money (MoMo / Airtel Money):**
- Description: "RRA PAYMENT", "RSSB"
- Used by small employers to settle via the portal

**Key identification tips:**
1. RRA and RSSB remittances are outgoing (DEBIT), recurring monthly.
2. "RRA / E-TAX / MyRRA / UMUSORO" = tax (PAYE). "RSSB / PENSION / RAMA / CBHI / MUTUELLE" = social contributions.
3. Inbound "RSSB PENSION" or "MATERNITY BENEFIT" credits are benefits received, not contributions paid.
4. Irregular lump sums referencing "ARREARS / INTEREST / FINE" may include penalties under Tax Procedures Law No. 020/2023 -- flag for reviewer.

### Kinyarwanda / French terms glossary

**Terms glossary**

| Term | Meaning |
| --- | --- |
| Umusoro / Imisoro | Tax / taxes |
| Umushahara | Salary / wages |
| Mutuelle (de santé) | Community-Based Health Insurance (CBHIS) |
| Assurance maladie | Medical insurance (RAMA) |
| Pension / pansiyo | Pension |

## Section 10 -- Onboarding fallback

If the client provides only a bank statement and no payroll detail:

1. **Scan for RRA and RSSB debits** -- identify all outgoing payments matching Section 4 patterns.
2. **Separate tax from contributions** -- "RRA / E-TAX / PAYE / UMUSORO" = PAYE; "RSSB / PENSION / RAMA / CBHI / MUTUELLE" = social contributions.
3. **Sum the monthly remittances** to estimate total payroll cost; note that a single unified debit may combine PAYE + RSSB.
4. **Do not reverse-engineer individual salaries** from a combined debit without the declaration -- the differing bases (gross / gross-excl-transport / net / basic) make this unreliable.
5. **Flag for reviewer:** "Payroll figures derived from bank statement totals only. Gross/basic/transport split, residency, and RAMA enrolment have not been verified. Reviewer must confirm before relying on the monthly declaration."

## Section 11 -- Reference material

### Corporate income tax (context only -- not payroll)

**CIT rates**  _(PwC Rwanda -- Taxes on corporate income (https://taxsummaries.pwc.com/rwanda/corporate/taxes-on-corporate-income))_

| Item | Rate | Source |
| --- | --- | --- |
| Standard CIT | 28% (reduced from 30%, effective tax year 2025) | PwC Rwanda -- Taxes on corporate income |
| Newly listed (5 yr), ≥30% public float | 25% | PwC Rwanda -- Taxes on corporate income |
| Newly listed (5 yr), ≥40% public float | 20% | PwC Rwanda -- Taxes on corporate income |
| Small business (turnover RWF 12m--20m) | 3% of turnover | PwC Rwanda -- Taxes on corporate income |
| Micro-enterprise (turnover < RWF 12m) | Flat RWF 60,000--300,000 by bracket | PwC Rwanda -- Taxes on corporate income |

### Penalties & interest -- Tax Procedures Law No. 020/2023 (effective 1 April 2023)

**Late-payment interest**  _(Tax Procedures Law No. 020/2023)_

| Delay | Interest |
| --- | --- |
| ≤ 6 months | 0.5% / month |
| 6 -- 12 months | 1.0% / month |
| > 12 months | 1.5% / month |

**Administrative fine for late payment**  _(Tax Procedures Law No. 020/2023)_

| Lateness | Fine |
| --- | --- |
| Up to 30 days | 5% |
| 31 -- 60 days | 10% |
| More than 60 days | 30% |

- **Non-declaration penalty** — 60% of tax payable if not declared by the due date.  _(Tax Procedures Law No. 020/2023)_

**Fixed administrative fines by taxpayer size**  _(Tax Procedures Law No. 020/2023; RRA changes notice (https://www.rra.gov.rw/en/details?tx_news_pi1%5Baction%5D=detail&tx_news_pi1%5Bcontroller%5D=News&tx_news_pi1%5Bnews%5D=1575&cHash=70805f202a7443789fa71390cac28042); EY alert (https://www.ey.com/en_gl/technical/tax-alerts/rwanda-gazettes-new-tax-procedures-law); official gazette PDF (https://www.rra.gov.rw/fileadmin/user_upload/NEW_TAX_PROCEDURES_LAW_2023.pdf))_

| Taxpayer size (annual turnover) | Fixed fine |
| --- | --- |
| RWF 2m -- 20m | RWF 50,000 |
| Above RWF 20m | RWF 300,000 |
| Large taxpayer | RWF 500,000 |

### Filing exemptions (no annual individual return required)

- **Filing exemptions** — - Annual turnover below RWF 2 million; or - Only employment income (PAYE is final); or - Only investment income subject to final WHT; or - Non-residents with Rwandan WHT income. Record retention: 10 years; returns auditable for 5 years.  _(PwC Rwanda -- Tax administration (https://taxsummaries.pwc.com/rwanda/individual/tax-administration))_

### Minimum wage

No enforceable national minimum wage. The 1974 statutory rate is obsolete; effective floors are set by sector/collective agreement. A new statutory minimum (reportedly ~RWF 60,000/month) has been discussed but not implemented as of 2025. [RESEARCH GAP -- no gazetted statutory rate; secondary HR/payroll guides only; reviewer to confirm.]

### Pension phased increases (scheduled, indicative)

**Pension phased increase schedule**  _(PwC Rwanda -- Other taxes (https://taxsummaries.pwc.com/rwanda/corporate/other-taxes). [RESEARCH GAP -- 2027--2030 steps not confirmed against the underlying RSSB ministerial order; reviewer to confirm.])_

| Effective | Employee | Employer | Total |
| --- | --- | --- | --- |
| 1 Jan 2025 (firm) | 6% | 6% | 12% |
| 1 Jan 2027 | 7% | 7% | 14% |
| 1 Jan 2028 | 8% | 8% | 16% |
| 1 Jan 2029 | 9% | 9% | 18% |
| 1 Jan 2030 | 10% | 10% | 20% |

### Test suite

**Test 1 -- PAYE at top band.** Taxable base RWF 468,590. PAYE = 24,000 + 0.30 × (468,590 − 200,000) = 24,000 + 80,577 = **104,577**.

**Test 2 -- PAYE in the 20% band.** Taxable base RWF 150,000. PAYE = 4,000 + 0.20 × (150,000 − 100,000) = 4,000 + 10,000 = **14,000**.

**Test 3 -- PAYE in the 10% band.** Taxable base RWF 90,000. PAYE = 0.10 × (90,000 − 60,000) = **3,000**.

**Test 4 -- Below threshold.** Taxable base RWF 55,000 → **PAYE = 0**.

**Test 5 -- Casual labour.** Payment RWF 80,000 at flat 15% → PAYE = **12,000**.

**Test 6 -- Pension contribution.** Gross RWF 500,000 → pension EE 6% = **30,000**; pension ER 6% = **30,000**; total = **60,000**.

**Test 7 -- Maternity base excludes transport.** Gross RWF 500,000 incl. transport RWF 30,000 → maternity EE 0.3% × 470,000 = **1,410**.

**Test 8 -- CBHIS on net.** From Example 1: net base 364,013 → CBHIS EE 0.5% = **1,820.07**.

**Test 9 -- Medical on basic (if enrolled).** Basic salary RWF 400,000 → medical EE 7.5% = **30,000**; medical ER 7.5% = **30,000**; total = **60,000**.

**Test 10 -- Full net pay reconciliation (Example 1, not RAMA-enrolled).** 500,000 − 30,000 (pension) − 1,410 (maternity) − 104,577 (PAYE) − 1,820.07 (CBHIS) = **362,192.93**.

### Prohibitions

- NEVER apply a single contribution base across all schemes -- pension/occ.hazards use gross, maternity uses gross-excl-transport, CBHIS uses net, medical uses basic.
- NEVER deduct occupational hazards (2%) from the employee -- it is employer-only.
- NEVER compute the medical (RAMA) contribution on gross -- it is on basic salary.
- NEVER apply the medical scheme without confirming enrolment (mandatory only for civil servants; private opt-in needs ≥7 employees).
- NEVER use the progressive brackets for casual labour -- it is a flat 15%.
- NEVER apply the 2027--2030 pension step-ups without reviewer confirmation -- they are unconfirmed at primary source.
- NEVER quote a Rwandan national minimum wage as a hard figure -- there is no enforceable gazetted rate.
- NEVER auto-apply the KIFC foreign-income exemption -- it is licence- and source-specific; escalate.
- NEVER estimate arrears, interest or penalties without an RRA/RSSB statement -- escalate to a reviewer.
- NEVER present these figures as definitive -- label them estimated and direct the client to their RRA/RSSB declaration.

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a CPA, EA, tax attorney, RRA-registered tax agent, or equivalent licensed practitioner in your jurisdiction) before filing or acting upon.

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
