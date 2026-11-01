---
name: rwanda-social-contributions
description: "Rwanda RSSB contributions for 2026: pension 6% plus 6% under Presidential Order 086/01, steps to 20% by 2030, maternity, medical, CBHI, Ishema declaration by the 15th, payment and sanctions."
version: 0.2
jurisdiction: RW
tax_year: 2026
last_updated: 2026-11-01
review_status: pending_review
trust_label: Built by Michael Cutajar and the OpenAccountants team
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Rwanda RSSB Social Contributions v0.2

Tax year 2026. PAYE computation sits in [rwanda-payroll](rwanda-payroll.md).

## Who this applies to

Employers and employees under the labour law and public service statutes; voluntary pension members.

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

Pension and maternity are on gross; medical on basic; CBHI on net. Employee contributions do not reduce PAYE (see payroll skill). Pension access: age 60, or 55 for early old age (https://imisanzu.rssb.rw/). Voluntary members pay on a chosen salary.

### Carried: Required inputs and refusal catalogue

#### Required inputs

**Minimum viable**: gross monthly salary and whether a transport allowance is included. Without the gross figure, STOP.

**Recommended**: the basic-salary component (needed if medical/RAMA applies), the transport-allowance amount (excluded from the maternity base), residency status, and whether the worker is a regular employee or casual labour.

**Ideal**: the employer's RSSB registration status and which schemes apply (medical/RAMA optional), the E-Tax/MyRRA monthly declaration, and bank statements showing RRA/RSSB remittances.

#### Refusal catalogue

- **R-RW-1: Medical (RAMA) contribution without basic salary** : Trigger: employer is RAMA-enrolled but only the gross figure is supplied. Message: "The medical scheme contribution (7.5% employee + 7.5% employer) is computed on basic salary, not gross. Cannot compute without the basic-salary component."
- **R-RW-2: KIFC foreign-income exemption** : Trigger: client claims the 5-year KIFC exemption on foreign-sourced income. Message: "The KIFC PIT exemption depends on holding a qualifying KIFC licence and on the source/timing of the income. This is case-specific and outside the scope of this skill. Escalate to a Rwandan licensed accountant / RRA-registered tax agent."
- **R-RW-3: Arrears, penalties and interest** : Trigger: client has unpaid PAYE/RSSB and asks for the total owed. Message: "Late-payment interest (0.5%--1.5%/month, capped at 100% of annual tax) and administrative fines (5%--30%, plus a possible 60% non-declaration penalty) under Tax Procedures Law No. 020/2023 depend on the exact delay and turnover band. Do not estimate. Request an RRA statement and escalate to a reviewer."
- **R-RW-4: Pension phased increases beyond 2026** : Trigger: client asks for pension contributions for 2027 onward. Message: "The scheduled pension step-ups (7% each from 2027 up to 10% each by 2030) are reported by PwC but I have not confirmed the underlying RSSB ministerial order text. Treat the 2025 6%+6% rate as firm; flag future years for reviewer confirmation. [RESEARCH GAP: reviewer to confirm 2027--2030 steps against the RSSB order.]"
- **R-RW-5: Minimum wage** : Trigger: client asks for the national minimum wage. Message: "Rwanda has no enforceable national minimum wage; the 1974 statutory rate is obsolete and effective wages are set by sector/collective agreement. The widely cited ~RWF 60,000/month figure is unconfirmed press/HR-guide speculation. [RESEARCH GAP: no gazetted statutory rate; reviewer to confirm.]"

### Carried: Payment pattern library

Deterministic pre-classifier for bank statement transactions related to Rwanda payroll taxes and RSSB. When a transaction matches a pattern below, apply the treatment directly. Match by case-insensitive substring on the counterparty/reference. RRA tax and RSSB contributions are statutory remittances: always EXCLUDE from any VAT return or revenue/expense P&L classification beyond their proper payroll-liability treatment.

#### 4.1 RRA tax remittances (PAYE and other)

**RRA tax remittances patterns**

| Pattern | Treatment | Notes |
| --- | --- | --- |
| RRA, RWANDA REVENUE AUTHORITY | EXCLUDE: statutory tax remittance | PAYE / income tax / VAT payment to RRA |
| PAYE, P.A.Y.E | EXCLUDE: employee income tax remitted | Monthly PAYE |
| E-TAX, MYRRA, ETAX | EXCLUDE: RRA portal payment | Unified declaration settlement |
| IMISORO, UMUSORO | EXCLUDE: tax (Kinyarwanda "umusoro" = tax) | Generic tax reference |

#### 4.2 RSSB social-contribution remittances

**RSSB contribution patterns**

| Pattern | Treatment | Notes |
| --- | --- | --- |
| RSSB, RWANDA SOCIAL SECURITY BOARD | EXCLUDE: social contribution remittance | Pension / occ. hazards / maternity / CBHIS |
| PENSION, RETIREMENT CONTRIB | EXCLUDE: pension contribution | RSSB pension scheme |
| RAMA, MEDICAL SCHEME, ASSURANCE MALADIE | EXCLUDE: medical scheme | RSSB medical (formerly RAMA) |
| CBHI, CBHIS, MUTUELLE, MUTUELLE DE SANTE | EXCLUDE: community health contribution | Community-Based Health Insurance |
| KUBAKA, IMITURIRE (transport allowance ref) | Component of gross: see base notes | Affects pension/maternity bases |

#### 4.3 Rwandan bank debit descriptions

**Bank debit descriptions**

| Bank | Typical debit description | Treatment |
| --- | --- | --- |
| Bank of Kigali (BK) | "RRA TAX", "RSSB CONTRIB", "PAYE" | EXCLUDE: statutory remittance |
| BPR Bank (Atlas Mara / BPR) | "RWANDA REVENUE", "RSSB" | EXCLUDE: statutory remittance |
| Equity Bank Rwanda | "RRA E-TAX", "RSSB PENSION" | EXCLUDE: statutory remittance |
| I&M Bank Rwanda | "RRA", "SOCIAL SECURITY" | EXCLUDE: statutory remittance |
| Mobile money (MoMo / Airtel Money) | "RRA PAYMENT", "RSSB" | EXCLUDE: statutory remittance |

#### 4.4 Payroll and benefits received (not contributions)

**Payroll/benefit patterns**

| Pattern | Treatment | Notes |
| --- | --- | --- |
| SALARY, UMUSHAHARA (outgoing) | EXCLUDE: payroll expense | Net wage paid to employee, not a contribution |
| RSSB PENSION (incoming credit) | EXCLUDE: pension benefit received | Inbound benefit, not a contribution paid |
| MATERNITY BENEFIT (incoming) | EXCLUDE: benefit received | Not a contribution |

### Carried: Tier 2 catalogue (reviewer judgement)

Flag these for reviewer confirmation.

#### T2-1: Transport allowance treatment

- **Transport allowance** : Trigger: the gross/transport split is unclear or transport is paid as a separate line. Issue: transport is included in the pension base (from 2025) but excluded from the maternity base. Mis-classifying it shifts both contributions and the PAYE base. Action: confirm the exact transport amount before computing.

#### T2-2: Medical (RAMA) enrolment

- **Medical enrolment** : Trigger: employer's RSSB medical enrolment status unknown, or fewer than 7 employees. Issue: medical is mandatory only for civil servants; private opt-in requires all-employee enrolment and ≥7 staff. The base is basic salary, not gross. Action: confirm enrolment and obtain the basic-salary figure.

#### T2-3: Casual labour vs regular employment

- **Casual vs regular** : Trigger: short-term or irregular engagement. Issue: casual labour is taxed at flat 15%; RSSB applicability is case-specific. Action: confirm engagement nature; flag RSSB registration question.

#### T2-4: Expatriate / KIFC foreign-income exemption

- **KIFC exemption** : Trigger: non-resident or KIFC-licensed taxpayer with foreign-sourced income. Issue: the 5-year KIFC PIT exemption on foreign income is licence- and source-dependent. Action: escalate; do not auto-apply the exemption.

#### T2-5: Arrears, interest and penalties

- **Arrears/penalties** : Trigger: unpaid PAYE/RSSB from prior periods. Issue: interest 0.5%--1.5%/month (capped at 100% of annual tax) plus 5%/10%/30% administrative fines and a possible 60% non-declaration penalty. Action: do not estimate; request an RRA statement; escalate.

#### T2-6: Future-year pension step-ups

- **Future step-ups** : Trigger: computation requested for 2027 onward. Issue: scheduled 7%--10% step-ups are unconfirmed at primary source. Action: flag; confirm against the RSSB ministerial order before applying.

### Carried: Excel working paper template

RWANDA PAYROLL / RSSB COMPUTATION: WORKING PAPER
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

EMPLOYEE SOCIAL SECURITY (does not reduce PAYE)
  Pension EE        6%  x gross:               [____]
  Occ. hazards EE   0%  x gross:               0
  Maternity EE      0.3% x (gross - transport): [____]
  Subtotal EE social security (pre-PAYE):      [____]

PAYE
  PAYE taxable base (gross, no deduction of the subtotal above):  [____]
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

### Carried: Bank statement reading guide

#### How Rwanda payroll remittances appear

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
4. Irregular lump sums referencing "ARREARS / INTEREST / FINE" may include penalties under Tax Procedures Law No. 020/2023: flag for reviewer.

#### Kinyarwanda / French terms glossary

**Terms glossary**

| Term | Meaning |
| --- | --- |
| Umusoro / Imisoro | Tax / taxes |
| Umushahara | Salary / wages |
| Mutuelle (de santé) | Community-Based Health Insurance (CBHIS) |
| Assurance maladie | Medical insurance (RAMA) |
| Pension / pansiyo | Pension |

### Carried: Onboarding fallback

If the client provides only a bank statement and no payroll detail:

1. **Scan for RRA and RSSB debits**: identify all outgoing payments matching Section 4 patterns.
2. **Separate tax from contributions**: "RRA / E-TAX / PAYE / UMUSORO" = PAYE; "RSSB / PENSION / RAMA / CBHI / MUTUELLE" = social contributions.
3. **Sum the monthly remittances** to estimate total payroll cost; note that a single unified debit may combine PAYE + RSSB.
4. **Do not reverse-engineer individual salaries** from a combined debit without the declaration: the differing bases (gross / gross-excl-transport / net / basic) make this unreliable.
5. **Flag for reviewer:** "Payroll figures derived from bank statement totals only. Gross/basic/transport split, residency, and RAMA enrolment have not been verified. Reviewer must confirm before relying on the monthly declaration."


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

RSSB surcharge and recovery: see the rates table and https://www.rra.gov.rw/en/domestic-tax-services/rssb-contributions/declaration-payment-of-rssb-contributions.

## Cross-border points

Foreign staff are covered on the same rates; no social security agreement was found in the pages read.

## Two worked examples that recompute

**Example 1. Gross and basic FRW 150,000, enrolled in medical.**

```oa-check
name: Employee deductions, FRW 150,000
inputs:
  gross: 150000
steps:
  - paye: (100000 - 60000) * 0.10 + (gross - 100000) * 0.20
  - pension: gross * 0.06
  - maternity: gross * 0.003
  - medical: gross * 0.075
  - cbhi: (gross - paye - pension - maternity) * 0.005
  - total: paye + pension + maternity + medical + cbhi
expected:
  total: 35332.75
```

**Example 2. Decision: enrol in the medical scheme?** Basic FRW 400,000. Enrolment costs each side FRW 30,000 a month, 60,000 in all. RSSB covers 85% of bills. Enrol if expected cover exceeds that.

```oa-check
name: Medical scheme cost
inputs:
  basic: 400000
steps:
  - each: basic * 0.075
  - total: each * 2
expected:
  total: 60000.00
```

## Ask the client first

1. Employer or voluntary member?
2. Gross, basic, allowances?
3. Medical enrolment?
4. Any arrears?

## Sources

| Source | URL | Read on |
|---|---|---|
| Presidential Order 086/01 of 12/12/2024, pension rate (whole) | https://www.minijust.gov.rw/fileadmin/user_upload/Minijust/Official_gazettes_2/______2024_Igazeti_ya_Leta/UKUBOZA-December-Decembre/OG_n___Special_of_13.12.2024__Ingano_y_umusanzu_mu_bwiteganyirize_bwa_pansiyo_butegetswe.pdf | 2026-11-01 |
| RSSB, Imisanzu portal home page (whole page) | https://imisanzu.rssb.rw/ | 2026-11-01 |
| RRA, pension contribution page (whole page) | https://www.rra.gov.rw/en/domestic-tax-services/rssb-contributions/pension-scheme-contribution | 2026-11-01 |
| RRA, medical scheme page (whole page) | https://www.rra.gov.rw/en/domestic-tax-services/rssb-contributions/medical-scheme-contribution | 2026-11-01 |
| RRA, maternity leave page (whole page) | https://www.rra.gov.rw/en/domestic-tax-services/rssb-contributions/maternity-leave-contribution | 2026-11-01 |
| RRA, CBHI page (whole page) | https://www.rra.gov.rw/en/domestic-tax-services/rssb-contributions/cbhi-contribution | 2026-11-01 |
| RRA, declaration and payment of RSSB contributions page (whole page) | https://www.rra.gov.rw/en/domestic-tax-services/rssb-contributions/declaration-payment-of-rssb-contributions | 2026-11-01 |
| RRA, Calculate PAYE page (whole page) | https://www.rra.gov.rw/en/domestic-tax-services/employment-tax-paye/calculate-paye | 2026-11-01 |
| Law 020/2023 on tax procedures (read: arts 15, 35, 78, 80-88) | https://www.rra.gov.rw/fileadmin/user_upload/OG_n___Special_ter_of_31.03.2023_Uburyo_bw_isoresha_Tax_procedures_01.pdf | 2026-11-01 |
| Commissioner General Instructions 001/2023, quarterly PAYE and VAT (whole) | https://www.rra.gov.rw/fileadmin/user_upload/13.1.23_OG_n___Special_of_11.01.2023_Kumenyekanisha_no_kwishyura_umusoro_ku_bihembo_n_umusoro_ku_nyongeragaciro_ku_gihembwe.pdf | 2026-11-01 |
| Law 027/2022 establishing taxes on income (read: arts 3-5, 8-10, 12-21, 24-33, 36-38, 44-50, 56-69) | https://www.rra.gov.rw/fileadmin/user_upload/Income_Tax_law_of_2022.pdf | 2026-11-01 |
| RRA Tax Handbook 2025 (read: E-Tax steps, real regime, PAYE, VAT declaration chapters) | https://www.rra.gov.rw/fileadmin/Folder_for_2025/RRA_Tax_Handbook_2025_Final.pdf | 2026-11-01 |

Not yet confirmed: occupational hazards rate; the pension and maternity treatment of transport; the definition of net for CBHI; the 7-employee minimum and 10th of the month date for medical; split of pension from 2027.

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
