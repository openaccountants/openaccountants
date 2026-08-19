---
name: bulgaria-social-contributions
description: Use this skill whenever asked about Bulgaria social security and health insurance contributions for employees, employers, or self-insured persons (self-employed / freelancers / sole traders). Trigger on phrases like "Bulgaria social security", "osigurovki", "how much social contribution in Bulgaria", "Category III employee", "Universal Pension Fund", "2nd pillar Bulgaria", "Declaration 1", "Declaration 6", "Декларация Образец 1", "self-insured person Bulgaria", "freelancer social contributions Bulgaria", "EOOD payroll", "minimum insurable income", "maximum insurable income ceiling", "health insurance NHIF Bulgaria", "10% flat tax Bulgaria", or any question about Bulgarian payroll, social-security withholding, or contribution caps. Also trigger when classifying bank statement transactions that relate to NRA (НАП) contribution payments, NSSI (НОИ) debits, or social/health insurance remittances from Bulgarian banks (UniCredit Bulbank, DSK Bank, Postbank, etc.). Also trigger when computing the 10% flat personal income tax base, since the PIT base is gross remuneration MINUS the employee's mandatory social and health contributions. This skill covers per-fund contribution rates by birth cohort, the 2nd pillar carve-out, floors/ceilings, the 2025 two-sub-period BGN thresholds, the 2026 euro figures, self-insured-person rates, monthly NRA compliance (Declaration 1 / Declaration 6), the annual return, bank-statement classification patterns, and edge cases. ALWAYS read this skill before touching any Bulgarian social-contribution or payroll work.
version: 0.1
jurisdiction: BG
tax_year: 2025
last_updated: 2026-07-13
review_status: pending_review
depends_on:
  - social-contributions-workflow-base
category: international
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Bulgaria Social Security & Health Insurance Contributions

## Bulgaria Social Security & Health Insurance Contributions -- Skill v0.1

> **Tier 2 (research-verified).** Figures below are sourced inline. Several depend on the 2026 State Social Security Budget Act (Закон за бюджета на държавното обществено осигуряване), which was pending/just-adopted as of early 2026; provisional figures are marked **[RESEARCH GAP — reviewer to confirm]**. This skill has NOT been signed off by a Bulgarian-licensed accountant.

## Section 1 -- Quick reference

**Read this whole section before computing or classifying anything.**

- **Country** — Bulgaria (Republic of Bulgaria)
- **Primary Legislation** — Social Security Code (Кодекс за социално осигуряване)
- **Supporting Legislation** — Health Insurance Act (Закон за здравното осигуряване); annual State Social Security Budget Act (Закон за бюджета на държавното обществено осигуряване)
- **Tax / contribution authority** — National Revenue Agency (NRA / НАП) — nra.bg (collects contributions + PIT); National Social Security Institute (NSSI / НОИ) — nssi.bg (administers benefits)
- **Personal income tax** — Flat 10% on gross remuneration LESS the employee's mandatory social/health contributions  _(Ministry of Economy; PwC, reviewed 30 Jan 2026)_
- **Corporate income tax** — Flat 10%; no local CIT — relevant for EOOD-vs-freelancer entity choice  _(PwC corporate)_
- **Total employee+employer contribution (Category III, born after 1959)** — 32.7%–33.4% of insurable income: employee 13.78%, employer 18.92%–19.62%  _(Ministry of Economy; PwC)_
- **Self-insured persons (born after 1959)** — 27.8% (pension 14.8% + 2nd pillar 5% + health 8%); +3.5% if optionally insured for sickness/maternity  _(innovires; Ruskov & Kollegen; PwC)_
- **Currency** — EUR from 1 Jan 2026; BGN through 31 Dec 2025; irrevocable fixed rate BGN 1.95583 = EUR 1  _(Ruskov & Kollegen)_
- **Min monthly insurable income (employees)** — BGN 933 (1 Jan–31 Mar 2025); BGN 1,077 (1 Apr–31 Dec 2025); from 2026 follows the minimum wage EUR 620.20 (= BGN 1,213)  _(Ministry of Economy; PwC)_
- **Min monthly insurable income (self-insured)** — BGN 1,077 (2025, = the minimum wage); EUR 550.66/month (= BGN 1,077, carried over for 2026 pending Budget Act)  _(PwC *Other taxes*; Ruskov & Kollegen)_
- **Max monthly insurable income (ceiling, all)** — BGN 3,750 (1 Jan–31 Mar 2025); BGN 4,130 (1 Apr–31 Dec 2025); EUR 2,111.64 (= BGN 4,130, 2026 pending Budget Act)  _(Ministry of Economy; PwC *Other taxes*)_
- **Minimum monthly wage** — BGN 1,077 (1 Jan 2025, = EUR 550.66); BGN 1,213 = EUR 620.20 (1 Jan 2026, Council of Ministers Decree No. 243 of 13.11.2025)  _(Ministry of Economy; Ruskov & Kollegen)_
- **Monthly compliance** — Declaration 1 + Declaration 6 filed electronically with the NRA; contributions paid; all by the 25th of the following month  _(activpayroll; Lano)_
- **Annual return** — Годишна данъчна декларация (GDD) — by 30 April of the following year  _(innovires; PwC)_

Pending — requires sign-off by a Bulgarian-licensed accountant

Pending

**Quick reference field table**

| Field | Value |
| --- | --- |
| Country | Bulgaria (Republic of Bulgaria) |
| Primary Legislation | Social Security Code (Кодекс за социално осигуряване) |
| Supporting Legislation | Health Insurance Act (Закон за здравното осигуряване); annual State Social Security Budget Act (Закон за бюджета на държавното обществено осигуряване) |
| Tax / contribution authority | National Revenue Agency (NRA / НАП) — nra.bg (collects contributions + PIT); National Social Security Institute (NSSI / НОИ) — nssi.bg (administers benefits) |
| Personal income tax | Flat 10% on gross remuneration LESS the employee's mandatory social/health contributions (Ministry of Economy; PwC, reviewed 30 Jan 2026) |
| Corporate income tax | Flat 10%; no local CIT (PwC corporate) — relevant for EOOD-vs-freelancer entity choice |
| Total employee+employer contribution (Category III, born after 1959) | 32.7%–33.4% of insurable income: employee 13.78%, employer 18.92%–19.62% (Ministry of Economy; PwC) |
| Self-insured persons (born after 1959) | 27.8% (pension 14.8% + 2nd pillar 5% + health 8%); +3.5% if optionally insured for sickness/maternity (innovires; Ruskov & Kollegen; PwC) |
| Currency | EUR from 1 Jan 2026; BGN through 31 Dec 2025; irrevocable fixed rate BGN 1.95583 = EUR 1 (Ruskov & Kollegen) |
| Min monthly insurable income (employees) | BGN 933 (1 Jan–31 Mar 2025); BGN 1,077 (1 Apr–31 Dec 2025); from 2026 follows the minimum wage EUR 620.20 (= BGN 1,213) (Ministry of Economy; PwC) |
| Min monthly insurable income (self-insured) | BGN 1,077 (2025, = the minimum wage); EUR 550.66/month (= BGN 1,077, carried over for 2026 pending Budget Act) (PwC *Other taxes*; Ruskov & Kollegen) |
| Max monthly insurable income (ceiling, all) | BGN 3,750 (1 Jan–31 Mar 2025); BGN 4,130 (1 Apr–31 Dec 2025); EUR 2,111.64 (= BGN 4,130, 2026 pending Budget Act) (Ministry of Economy; PwC *Other taxes*) |
| Minimum monthly wage | BGN 1,077 (1 Jan 2025, = EUR 550.66); BGN 1,213 = EUR 620.20 (1 Jan 2026, Council of Ministers Decree No. 243 of 13.11.2025) (Ministry of Economy; Ruskov & Kollegen) |
| Monthly compliance | Declaration 1 + Declaration 6 filed electronically with the NRA; contributions paid; all by the 25th of the following month (activpayroll; Lano) |
| Annual return | Годишна данъчна декларация (GDD) — by 30 April of the following year (innovires; PwC) |
| Validated by | Pending — requires sign-off by a Bulgarian-licensed accountant |
| Validation date | Pending |

**Contribution overview (Category III employee, born after 31 Dec 1959)**  _(Ministry of Economy; PwC; innovires; ISSA)_

| Fund | Total | Employee | Employer |
| --- | --- | --- | --- |
| Pension Fund (1st pillar) | 14.8% | 6.58% | 8.22% |
| Supplementary mandatory pension (2nd pillar, Universal Pension Fund) | 5% | 2.2% | 2.8% |
| General Disease & Maternity Fund | 3.5% | 1.4% | 2.1% |
| Unemployment Fund | 1% | 0.4% | 0.6% |
| Accident at Work & Occupational Diseases Fund | 0.4%–1.1% | 0% | 0.4%–1.1% |
| Health Insurance (NHIF) | 8% | 3.2% | 4.8% |
| **TOTAL** | **32.7%–33.4%** | **13.78%** | **18.92%–19.62%** |

*Source: Ministry of Economy; PwC; innovires; ISSA. Per-fund splits cross-checked: employee column 6.58+2.2+1.4+0.4+0+3.2 = 13.78%; employer column (low) 8.22+2.8+2.1+0.6+0.4+4.8 = 18.92%, (high) substitutes 1.1% work-accident = 19.62%.*

**Conservative defaults**

| Ambiguity | Default |
| --- | --- |
| Unknown birth year | Assume born **after** 31 Dec 1959 (Category III, in 2nd pillar) — the standard active-workforce case (research conservative_defaults) |
| Unknown employment status | Determine before computing — employee vs self-insured changes the rate from 13.78%/18.92% to 27.8% |
| Work-accident rate (economic activity unknown) | Apply low end 0.4% (or services ~0.5%) and flag that the exact rate is in the Budget Act NACE annex (research conservative_defaults) |
| Income below floor | Clamp UP to the applicable minimum insurable income |
| Income above ceiling | Clamp DOWN to the maximum insurable income; excess not contributory |
| Date in 2026+ | Use EUR figures; date in 2025 use BGN figures for the correct sub-period (Jan–Mar vs Apr–Dec) |
| Self-insured, no optional sickness cover | Use 27.8% (do NOT add the 3.5% Disease & Maternity unless voluntarily elected) |

## Section 2 -- Required inputs and refusal catalogue

### Required inputs

- **Minimum viable inputs** — (1) period/date (to pick 2025 BGN sub-period vs 2026 EUR), (2) employment status (employee vs self-insured person), and (3) gross monthly remuneration / declared insurable income. Without employment status and period, STOP.
- **Recommended inputs** — birth cohort (born before 1 Jan 1960 vs after 31 Dec 1959, which changes the pension rate and 2nd-pillar eligibility), the employer's economic-activity / NACE code (to fix the 0.4%–1.1% work-accident rate), and whether a self-insured person has elected optional sickness/maternity cover.
- **Ideal inputs** — payroll register, NRA Declaration 1 / Declaration 6 filings, NSSI insurance record, prior-year GDD for self-insured reconciliation, and bank statements showing NRA contribution remittances.

### Refusal catalogue

- **R-BG-SSC-1 -- Period/currency undetermined** — Trigger: the relevant date is not known, so the system cannot tell whether to apply 2025 BGN sub-period thresholds or 2026 EUR figures. Message: "Bulgaria adopted the euro on 1 Jan 2026 (fixed rate BGN 1.95583 = EUR 1) and raised the wage/insurable-income thresholds effective 1 Apr 2025. The applicable floors, ceilings and currency depend on the exact period. Provide the contribution month before computing."
- **R-BG-SSC-2 -- 2026 floors/ceilings treated as final** — Trigger: a self-employed minimum (EUR 550.66) or ceiling (EUR 2,111.64) figure is needed for a 2026 date. Message: "The 2026 EUR floors/ceilings are 2025 amounts carried over at the fixed rate (self-employed min EUR 550.66 = BGN 1,077; ceiling EUR 2,111.64 = BGN 4,130). They remain in force only while the 2025 State Social Security Budget Act continues to apply (reported through 31 Mar 2026, per Ruskov & Kollegen). The draft 2026 State Social Security Budget Act proposes raising the self-employed minimum insurable income to EUR 620.20 and the ceiling to EUR 2,352, but this was NOT yet adopted as of early 2026. Treat the post-Budget figures as provisional and verify against the adopted Act. **[RESEARCH GAP — reviewer to confirm]**."
- **R-BG-SSC-3 -- Work-accident rate by activity** — Trigger: the precise Accident-at-Work rate is needed and the economic-activity / NACE code is unknown. Message: "The work-accident contribution (employer-only) is 0.4%–1.1% and is keyed to the company's economic activity in the annual Budget Act annex, which was not retrieved in full. Look up the activity-specific rate in the Budget Act annex before relying on a figure. **[RESEARCH GAP — reviewer to confirm]**."
- **R-BG-SSC-4 -- Arrears, penalties, statutory interest** — Trigger: client has unpaid contributions and wants the penalty/interest quantified. Message: "Penalty amounts (reported EUR 250–500 late filing; BGN 500–10,000 general) come from secondary payroll guides, and the statutory interest formula (BNB base rate + 10 pts, per the Interest Act) was not re-confirmed from the authority. Do not quantify arrears without checking the Social Security Code administrative-penalty schedule and the Interest Act. Escalate to a Bulgarian-licensed accountant. **[RESEARCH GAP — reviewer to confirm]**."
- **R-BG-SSC-5 -- Pre-1960 birth cohort** — Trigger: person born before 1 Jan 1960. Message: "Persons born before 1 Jan 1960 are NOT in the 2nd pillar; their state pension rate is 19.8% (employee 8.78% / employer 11.02%) instead of 14.8%. Confirm exact birth date and that the person is genuinely outside the Universal Pension Fund before applying the higher rate."

## Section 3 -- Payment pattern library

This is the deterministic pre-classifier for bank statement transactions related to Bulgarian social/health contributions and PIT. When a transaction matches a pattern below, apply the treatment directly. Do not second-guess.

**How to read this table.** Match by case-insensitive substring on the counterparty/reference as it appears in the bank statement. Contribution and PIT remittances always EXCLUDE from any VAT return or revenue/expense classification of the business -- the employee-side portion and PIT are withholdings from staff pay, and the employer-side contributions are a payroll cost, not a taxable supply.

### 3.1 NRA contribution / tax remittances (outgoing)

**NRA contribution/tax remittance patterns**

| Pattern | Treatment | Notes |
| --- | --- | --- |
| НАП, NAP, NRA, NATIONAL REVENUE AGENCY | EXCLUDE -- contribution/PIT remittance | NRA collects both social/health contributions and PIT |
| ОСИГУРОВКИ, OSIGUROVKI, SOCIAL INSURANCE | EXCLUDE -- social contribution payment | Generic social-insurance reference |
| ЗДРАВНИ ОСИГУРОВКИ, HEALTH INSURANCE, NHIF, НЗОК | EXCLUDE -- health-insurance contribution | 8% NHIF fund |
| ДДФЛ, PIT, DOHODEN DANAK, INCOME TAX | EXCLUDE -- withheld 10% PIT | Flat-tax remittance, not a social contribution |
| ДОО, DOO, STATE SOCIAL SECURITY | EXCLUDE -- state social security (1st pillar etc.) | Държавно обществено осигуряване |
| УПФ, UPF, UNIVERSAL PENSION FUND | EXCLUDE -- 2nd-pillar supplementary pension | 5% Universal Pension Fund |

### 3.2 Contribution debits appearing on specific Bulgarian banks

**Bank-specific contribution debits**

| Bank | Typical debit description | Treatment |
| --- | --- | --- |
| UniCredit Bulbank | "НАП ОСИГУРОВКИ" or "NAP CONTRIBUTIONS" | EXCLUDE -- contribution remittance |
| DSK Bank | "НАП" or "ОСИГУРИТЕЛНИ ВНОСКИ" | EXCLUDE -- contribution remittance |
| Postbank (Eurobank Bulgaria) | "NRA" or "SOC INSURANCE" | EXCLUDE -- contribution remittance |
| Fibank (First Investment Bank) | "НАП ДДФЛ" or "TAX/SSC" | EXCLUDE -- PIT or contribution |
| Wise / Revolut | Rare -- NRA debits typically come from local BGN/EUR accounts | If present, EXCLUDE |

*Bank-specific reference strings are illustrative of common Bulgarian payroll-remittance descriptions; exact text varies by bank. **[RESEARCH GAP — reviewer to confirm]** the literal description used by each institution.*

### 3.3 Self-insured persons (own contributions)

**Self-insured contribution patterns**

| Pattern | Treatment | Notes |
| --- | --- | --- |
| НАП САМООСИГУРЯВАЩ, SELF-INSURED, SOL | EXCLUDE -- self-insured person's own 27.8% contribution | Self-declared insurable income |
| ДЕКЛАРАЦИЯ 6, DECLARATION 6 | EXCLUDE -- contribution remittance per Decl. 6 | Monthly/annual settlement |

### 3.4 Salary and payroll (exclude from contribution classification)

**Salary/payroll exclusion patterns**

| Pattern | Treatment | Notes |
| --- | --- | --- |
| ЗАПЛАТА, ZAPLATA, SALARY, WAGES (outgoing) | EXCLUDE -- payroll expense | Net pay to employee, not a contribution |
| АВАНС, ADVANCE (outgoing) | EXCLUDE -- salary advance | Not a contribution |

### 3.5 Benefits received (not contributions)

**Benefit received patterns**

| Pattern | Treatment | Notes |
| --- | --- | --- |
| НОИ, NOI, NSSI, ПЕНСИЯ, PENSION (incoming) | EXCLUDE -- benefit received | Pension/benefit paid out by NSSI, not a contribution |
| ОБЕЗЩЕТЕНИЕ, БОЛНИЧНИ, SICK PAY (incoming) | EXCLUDE -- benefit received | Sickness/maternity benefit, not a contribution |

## Section 4 -- Worked examples

Six bank statement / payroll classifications for a hypothetical Bulgarian software company and a freelance consultant. All employees assumed born after 31 Dec 1959 (Category III). Where 2026 EUR figures are used, the ceiling is EUR 2,111.64 and the work-accident rate is taken at the low end (0.4%) unless stated.

### Example 1 -- Standard employee, gross within the band (2026, EUR)

**Input line:**
`25.02.2026 ; НАП ОСИГУРОВКИ ; DEBIT ; FEB 2026 SOC+HEALTH+PIT ; -826.44 ; EUR`

**Reasoning:**
Employee gross EUR 2,000/month, within the floor (>= EUR 620.20) and below the ceiling (EUR 2,111.64), so the full EUR 2,000 is the insurable base.
- Employee contributions = 13.78% x 2,000 = EUR 275.60
- PIT base = 2,000 - 275.60 = EUR 1,724.40; PIT = 10% x 1,724.40 = EUR 172.44
- Employer contributions (18.92%) = 2,000 x 18.92% = EUR 378.40
- Total remitted to NRA = employee SSC 275.60 + PIT 172.44 + employer SSC 378.40 = **EUR 826.44** (matches the debit)
- Employee net pay = 2,000 - 275.60 - 172.44 = EUR 1,551.96; total employer cost = 2,000 + 378.40 = EUR 2,378.40

**Classification:** EXCLUDE -- combined NRA contribution + PIT remittance (Decl. 1 / Decl. 6). Not a VAT or revenue/expense item.

### Example 2 -- High earner, capped at the ceiling (2026, EUR)

**Input line:**
`25.03.2026 ; НАП ОСИГУРОВКИ ; DEBIT ; MAR 2026 ; -561.88 ; EUR`

**Reasoning:**
Employee gross EUR 3,000/month, above the EUR 2,111.64 ceiling, so the insurable base is clamped to EUR 2,111.64. PIT, however, is on the full gross less the (capped) actual contributions.
- Employee contributions = 13.78% x 2,111.64 = EUR 290.98
- PIT base = 3,000 - 290.98 = EUR 2,709.02; PIT = 10% x 2,709.02 = EUR 270.90
- Employee-side remittance shown = employee SSC 290.98 + PIT 270.90 = **EUR 561.88** (matches; employer share remitted separately)
- Employee net = 3,000 - 290.98 - 270.90 = EUR 2,438.12

**Classification:** EXCLUDE -- contribution + PIT remittance. Note the contribution cap but full-income PIT base.

### Example 3 -- PIT-only withholding line (2026, EUR)

**Input line:**
`25.02.2026 ; НАП ДДФЛ ; DEBIT ; FEB 2026 INCOME TAX ; -172.44 ; EUR`

**Reasoning:**
Matches "ДДФЛ" (pattern 3.1) -- this is the withheld 10% flat PIT only, separated from the social/health contributions. For the EUR 2,000 employee in Example 1, PIT = EUR 172.44. This is income tax, NOT a social contribution.

**Classification:** EXCLUDE -- withheld 10% PIT. Not a social-security contribution; do not double-count against the contribution funds.

### Example 4 -- Self-insured freelancer, own contributions (2026, EUR)

**Input line:**
`14.04.2026 ; НАП САМООСИГУРЯВАЩ ; DEBIT ; MAR 2026 SOL ; -417.00 ; EUR`

**Reasoning:**
Self-insured person (born after 1959) declaring insurable income of EUR 1,500/month (>= self-employed minimum EUR 550.66, <= ceiling EUR 2,111.64), NO optional sickness/maternity cover.
- Contributions = 27.8% x 1,500 = EUR 417.00 (pension 14.8% + 2nd pillar 5% + health 8%)
- If the person had elected optional Disease & Maternity (+3.5%): 31.3% x 1,500 = EUR 469.50

**Classification:** EXCLUDE -- self-insured person's own social/health contribution. Reconciled to actual annual income via the GDD (Decl. 6).

### Example 5 -- Salary net pay outgoing (not a contribution)

**Input line:**
`28.02.2026 ; IVAN PETROV ЗАПЛАТА ; DEBIT ; SALARY FEB ; -1,551.96 ; EUR`

**Reasoning:**
Matches "ЗАПЛАТА" / salary pattern (3.4). EUR 1,551.96 is the net pay for the EUR 2,000 gross employee in Example 1 (2,000 - 275.60 SSC - 172.44 PIT). This is wages paid, not a contribution.

**Classification:** EXCLUDE -- payroll expense (net wages). NOT a contribution remittance.

### Example 6 -- NSSI benefit received (not a contribution)

**Input line:**
`10.05.2026 ; НОИ ПЕНСИЯ ; CREDIT ; OLD-AGE PENSION MAY ; +540.00 ; EUR`

**Reasoning:**
Matches "НОИ" / "ПЕНСИЯ" (pattern 3.5). This is a benefit RECEIVED from NSSI, not a contribution paid. Do not confuse inbound NSSI credits with outbound NRA contribution debits.

**Classification:** EXCLUDE from VAT and from contribution classification -- benefit received, not a contribution.

## Section 5 -- Tier 1 rules

These rules apply when the period, status and figures are clear and all required inputs are available. Apply exactly as written. (Sources: Ministry of Economy; PwC reviewed 30 Jan 2026; ISSA; innovires; Ruskov & Kollegen.)

### Rule 1 -- Insurable base is clamped

- **Insurable base clamp formula** — insurable_base = clamp(gross_insurable_income, floor, ceiling)  _(Ministry of Economy; PwC)_
- **floor (employees)** — BGN 933 (Jan–Mar 2025) / BGN 1,077 (Apr–Dec 2025) / minimum wage EUR 620.20 = BGN 1,213 (2026)  _(Ministry of Economy; PwC)_
- **floor (self-insured)** — BGN 1,077 (2025) / EUR 550.66 = BGN 1,077 (2026, carried over pending Budget Act) **[RESEARCH GAP — reviewer to confirm 2026 final value; draft Budget proposes EUR 620.20]**  _(Ministry of Economy; PwC)_
- **ceiling (all)** — BGN 3,750 (Jan–Mar 2025) / BGN 4,130 (Apr–Dec 2025) / EUR 2,111.64 = BGN 4,130 (2026, carried over pending Budget Act; draft proposes EUR 2,352)  _(Ministry of Economy; PwC)_
- **Income above ceiling not contributory** — Income above the ceiling is NOT subject to social or health contributions.  _(Ministry of Economy; PwC)_

### Rule 2 -- Category III employee total (born after 31 Dec 1959)

- **Employee/employer contribution formula** — employee_contributions = 13.78% x insurable_base employer_contributions = (18.92% to 19.62%) x insurable_base   # range = work-accident 0.4%-1.1%
- **Per-fund employee/employer split** — pension 6.58/8.22; 2nd pillar 2.2/2.8; disease & maternity 1.4/2.1; unemployment 0.4/0.6; work accident 0/0.4–1.1; health 3.2/4.8  _(Ministry of Economy; innovires; PwC)_

### Rule 3 -- Birth cohort changes ONLY the pension fund and 2nd-pillar eligibility

- **Birth cohort effect on pension fund** — Born **after** 31 Dec 1959 (Category III): pension 14.8% (6.58/8.22) PLUS 2nd-pillar 5% (2.2/2.8). Born **before** 1 Jan 1960: NOT in the 2nd pillar; full state pension rate is 19.8% (employee 8.78% / employer 11.02%), and no 5% Universal Pension Fund. All other funds (disease/maternity, unemployment, work accident, health) are unchanged. Note the employee/employer totals coincidentally net to the same 13.78%/18.92%–19.62% (the higher 1st-pillar pension exactly replaces the absent 2nd pillar — see Test 4).  _(Ministry of Economy; ISSA)_

### Rule 4 -- 10% flat PIT base

- **PIT base and PIT formula** — PIT_base = gross_remuneration - employee_mandatory_social_and_health_contributions PIT      = 10% x PIT_base  _(Ministry of Economy; PwC)_
- **No local income tax; contribution cap note** — Flat 10% on employment income; no local/municipal income tax. Note the contribution cap can apply to the contributions even though PIT is on the full gross less those (capped) contributions.  _(Ministry of Economy; PwC)_

### Rule 5 -- Self-insured persons (born after 1959)

- **Self-insured contribution formula** — contributions = 27.8% x declared_insurable_base            # pension 14.8% + 2nd pillar 5% + health 8% contributions = 31.3% x declared_insurable_base            # if optional Disease & Maternity (+3.5%) elected
- **No unemployment/work-accident for self-insured** — Unemployment and work-accident funds do NOT apply to self-insured persons. The declared base is clamped between the self-employed minimum and the general ceiling, and reconciled to actual annual income via the GDD.  _(innovires; Ruskov & Kollegen; PwC)_

### Rule 6 -- Work-accident fund is employer-only and activity-keyed

- **Work-accident fund rule** — 0.4%–1.1%, borne entirely by the employer, with the exact rate set by the company's economic activity (NACE) in the annual Budget Act annex; administration/services is reported around 0.5%. When the activity is unknown, use the low end and flag.  _(Ministry of Economy; PwC)_

### Rule 7 -- Monthly compliance and payment

**Monthly compliance table**

| Item | Form | Due |
| --- | --- | --- |
| Per-person insured data + contributions | Declaration 1 (Декларация Образец 1) | 25th of the following month |
| Employer totals (contributions + withheld PIT) | Declaration 6 (Декларация Образец 6) | 25th of the following month |
| Contribution + PIT payment | Remittance to NRA | 25th of the following month |

- **Electronic filing** — Both declarations are filed electronically with the NRA.  _(activpayroll; Lano)_

### Rule 8 -- Annual reconciliation (self-insured)

- **Annual reconciliation rule** — Self-insured persons declare insurable income monthly but reconcile to actual annual income via the annual personal income tax return (Годишна данъчна декларация / GDD), due 30 April of the following year.  _(innovires; PwC)_

### Rule 9 -- Euro adoption and currency selection

- **Euro adoption and currency selection rule** — Bulgaria joined the euro area on 1 Jan 2026 at the irrevocable fixed rate BGN 1.95583 = EUR 1. For dates in 2026+ use EUR figures; for 2025 use BGN figures and the correct sub-period (Jan–Mar vs Apr–Dec, because thresholds rose on 1 Apr 2025). Convert legacy BGN at the fixed rate.  _(Ruskov & Kollegen; sb-bg.com)_

### Rule 10 -- Employer registration

- **Employer registration rule** — Employers, including foreign employers with staff in Bulgaria, must register with the NRA and report insured persons; foreign employers can register directly with the NRA for social-security/payroll purposes.  _(innovires foreign-employer-registration)_

## Section 6 -- Tier 2 catalogue

When the period, status or figures are ambiguous, or the client circumstances are unusual, flag these situations for reviewer confirmation.

### T2-1 -- Birth cohort straddling 1 Jan 1960

- **T2-1 full entry** — Trigger: birth year near 1959/1960, or unconfirmed. Issue: Born after 31 Dec 1959 → 14.8% pension + 5% 2nd pillar; born before 1 Jan 1960 → 19.8% pension and no 2nd pillar. While the employee/employer totals coincide, the fund allocation (and 2nd-pillar membership) differs. Action: Flag for reviewer. Confirm exact birth date and 2nd-pillar membership before applying rates.

### T2-2 -- 2026 thresholds pending the Budget Act

- **T2-2 full entry** — Trigger: a 2026 computation relying on the self-employed minimum (EUR 550.66) or ceiling (EUR 2,111.64). Issue: These are the 2025 amounts carried over at the fixed rate (EUR 550.66 = BGN 1,077; EUR 2,111.64 = BGN 4,130) while the 2025 State Social Security Budget Act still applies (reported through 31 Mar 2026). The draft 2026 State Social Security Budget Act proposes raising the self-employed minimum to EUR 620.20 and the ceiling to EUR 2,352, but this was NOT adopted as of early 2026. Action: Flag for reviewer. Verify the in-force figures against the adopted 2026 State Social Security Budget Act. **[RESEARCH GAP — reviewer to confirm]**

### T2-3 -- Work-accident rate by economic activity

- **T2-3 full entry** — Trigger: the precise employer work-accident rate matters and the NACE code is unknown or the activity is high-risk. Issue: The rate ranges 0.4%–1.1% across activities; using the low end under-states the cost for higher-risk activities. Action: Flag for reviewer; look up the rate in the Budget Act NACE annex. **[RESEARCH GAP — reviewer to confirm]**

### T2-4 -- Self-insured: optional sickness/maternity cover

- **T2-4 full entry** — Trigger: a self-insured person's expected benefit entitlements (e.g. maternity, sickness) are relevant. Issue: General Disease & Maternity (+3.5%) is optional for self-insured persons; whether the person elected it changes the rate from 27.8% to 31.3% and changes benefit entitlement. Action: Flag for reviewer. Confirm the election on the NSSI/NRA record before computing.

### T2-5 -- Contribution arrears, penalties and interest

- **T2-5 full entry** — Trigger: unpaid contributions or late declarations. Issue: Penalty figures (EUR 250–500 late filing; BGN 500–10,000 general) come from secondary guides, and the statutory interest formula (BNB base + 10 pts) was not re-confirmed from the authority. Action: Do not quantify without checking the Social Security Code penalty schedule and the Interest Act. Escalate to a Bulgarian-licensed accountant. **[RESEARCH GAP — reviewer to confirm]**

### T2-6 -- EOOD vs freelancer entity choice

- **T2-6 full entry** — Trigger: client weighing operating as a sole trader/freelancer (self-insured at 27.8%) vs an EOOD (single-member company). Issue: Corporate income tax is a flat 10% (PwC corporate); the interaction of CIT, dividend taxation, manager-contract contributions and self-insured contributions affects total burden. Pillar Two QDMTT can raise the effective rate to 15% for groups with revenue > EUR 750m. Action: Flag for reviewer. Entity choice is a planning decision outside this skill's compute scope.

## Section 7 -- Excel working paper template

When producing a Bulgarian contribution computation, structure the working paper as follows:

```
BULGARIA SOCIAL/HEALTH CONTRIBUTION + PIT COMPUTATION -- WORKING PAPER
Client: [name]
Period: [month/year]    Currency: [BGN 2025 sub-period / EUR 2026]
Prepared: [date]

INPUT DATA
  Status:                         [Employee / Self-insured person]
  Born after 31 Dec 1959:         [YES/NO]   (NO => 19.8% pension, no 2nd pillar)
  Gross / declared income:        [____]
  Economic activity / NACE:       [____]     (sets work-accident 0.4%-1.1%)
  Optional sickness cover (SOL):  [YES/NO]   (self-insured only, +3.5%)

BASE CLAMP
  Floor (period-specific):        [933 / 1,077 BGN 2025 | 2026: employee 620.20 EUR (=BGN 1,213) / self-insured 550.66 EUR (=BGN 1,077)]
  Ceiling (period-specific):      [3,750 / 4,130 BGN | 2,111.64 EUR]
  Insurable base (clamped):       [____]

EMPLOYEE CONTRIBUTIONS (Category III, post-1959)
  Pension 1st pillar  6.58%:      [____]
  2nd pillar          2.20%:      [____]
  Disease & maternity 1.40%:      [____]
  Unemployment        0.40%:      [____]
  Health (NHIF)       3.20%:      [____]
  Employee total     13.78%:      [____]

EMPLOYER CONTRIBUTIONS (Category III, post-1959)
  Pension 1st pillar  8.22%:      [____]
  2nd pillar          2.80%:      [____]
  Disease & maternity 2.10%:      [____]
  Unemployment        0.60%:      [____]
  Work accident  0.4%-1.1%:       [____]
  Health (NHIF)       4.80%:      [____]
  Employer total 18.92%-19.62%:   [____]

SELF-INSURED (if applicable)
  Pension 14.8% + 2nd 5% + health 8% = 27.8%:  [____]
  + optional disease/maternity 3.5% => 31.3%:  [____]

PERSONAL INCOME TAX
  Gross remuneration:             [____]
  Less employee contributions:    [____]
  PIT base:                       [____]
  PIT @ 10%:                      [____]

NET / EMPLOYER COST
  Employee net pay:               [gross - employee SSC - PIT]
  Total employer cost:            [gross + employer SSC]

COMPLIANCE
  Declaration 1 due:              25th of following month
  Declaration 6 due:              25th of following month
  Payment due:                    25th of following month
  Annual GDD (self-insured):      30 April following year

REVIEWER FLAGS
  [List any Tier 2 flags / RESEARCH GAP markers here]

CONSERVATIVE DEFAULTS APPLIED
  [List any defaults applied and their impact]
```

## Section 8 -- Bank statement reading guide

### How contribution and PIT remittances appear on Bulgarian bank statements

**UniCredit Bulbank:**
- Description: "НАП ОСИГУРОВКИ", "NAP CONTRIBUTIONS", or split into "ОСИГУРОВКИ" and "ДДФЛ"
- Timing: around the 25th of each month (for the prior month)
- Amount: depends on headcount and gross pay

**DSK Bank:**
- Description: "НАП", "ОСИГУРИТЕЛНИ ВНОСКИ", or "ЗДРАВНИ ОСИГУРОВКИ"
- Timing: same monthly cycle

**Postbank (Eurobank Bulgaria) / Fibank:**
- Description: "NRA", "SOC INSURANCE", "НАП ДДФЛ"
- Timing: same monthly cycle

*Bank-specific reference strings above are illustrative. **[RESEARCH GAP — reviewer to confirm]** the literal description each institution prints.*

**Key identification tips:**
1. Contribution and PIT remittances are always outgoing (DEBIT) to the NRA; benefits (НОИ pension, sick pay) are incoming CREDITs.
2. They recur monthly, near the 25th.
3. A combined line bundles employee SSC + employer SSC + withheld PIT; a "ДДФЛ" line is PIT only.
4. Do not confuse NRA contribution debits with net-salary ("ЗАПЛАТА") payments to employees.
5. From 1 Jan 2026 amounts are in EUR; 2025 statements are in BGN (convert at 1.95583 if needed).

### Quick Bulgarian/Cyrillic glossary

**Glossary table**

| Term | Meaning |
| --- | --- |
| Осигуровки (osigurovki) | Social contributions |
| Здравно осигуряване | Health insurance (NHIF / НЗОК) |
| ДДФЛ | Personal income tax (10% flat) |
| ДОО | State social security (Държавно обществено осигуряване) |
| УПФ | Universal Pension Fund (2nd pillar) |
| Самоосигуряващо се лице (SOL) | Self-insured person (self-employed) |
| Заплата | Salary / wages |
| Декларация Образец 1 / 6 | Declaration 1 / 6 |
| Годишна данъчна декларация (GDD) | Annual personal income tax return |

## Section 9 -- Onboarding fallback

If the client provides only a bank statement and no other information:

1. **Scan for NRA debits** -- identify all outgoing payments matching Section 3.1/3.2 patterns (НАП / NAP / ОСИГУРОВКИ / ДДФЛ).
2. **Separate PIT from contributions** -- "ДДФЛ" lines are 10% PIT only; combined "ОСИГУРОВКИ" lines bundle social + health + (often) PIT.
3. **Determine the period/currency** -- 2025 statements are in BGN (use the Jan–Mar vs Apr–Dec sub-period); 2026 statements are in EUR.
4. **Reverse-engineer roughly:** for a single Category III employee, the combined monthly NRA outflow ≈ (13.78% + 18.92%) x insurable base + 10% x (gross − 13.78% x base). Use this only to sanity-check, not to assert exact pay.
5. **Flag for reviewer:** "Classification derived from bank statement amounts only. Employment status, birth cohort, economic-activity rate, and the in-force 2026 thresholds have not been independently verified. Reviewer must confirm before filing Declaration 1/6 or the GDD."

## Section 10 -- Reference material

### Rate summary (Category III employee, born after 31 Dec 1959)

**Rate summary (Category III employee, born after 31 Dec 1959)**  _(Ministry of Economy; ISSA; innovires; PwC)_

| Fund | Total | Employee | Employer | Source |
| --- | --- | --- | --- | --- |
| Pension (1st pillar) | 14.8% | 6.58% | 8.22% | Ministry of Economy; ISSA; innovires |
| 2nd pillar (Universal Pension Fund) | 5% | 2.2% | 2.8% | Ministry of Economy; PwC |
| Disease & Maternity | 3.5% | 1.4% | 2.1% | innovires; Ministry of Economy |
| Unemployment | 1% | 0.4% | 0.6% | innovires; Ministry of Economy |
| Work accident (employer only) | 0.4%–1.1% | 0% | 0.4%–1.1% | Ministry of Economy; PwC |
| Health (NHIF) | 8% | 3.2% | 4.8% | Ministry of Economy; PwC |
| **Total** | **32.7%–33.4%** | **13.78%** | **18.92%–19.62%** | Ministry of Economy; PwC |

Self-check: employee 6.58+2.2+1.4+0.4+0+3.2 = 13.78. Employer low 8.22+2.8+2.1+0.6+0.4+4.8 = 18.92; high (1.1% accident) = 19.62. Total 13.78+18.92 = 32.70; 13.78+19.62 = 33.40.

### Pre-1960 cohort (no 2nd pillar)

**Pre-1960 cohort (no 2nd pillar)**  _(Ministry of Economy; ISSA)_

| Fund | Total | Employee | Employer | Source |
| --- | --- | --- | --- | --- |
| Pension (1st pillar, higher) | 19.8% | 8.78% | 11.02% | Ministry of Economy; ISSA |
| 2nd pillar | n/a | n/a | n/a | Ministry of Economy; ISSA |

Self-check: 8.78 + 11.02 = 19.80. Other funds (disease/maternity, unemployment, work accident, health) are unchanged from the table above. Combined employee total again = 8.78+1.4+0.4+3.2 = 13.78; combined employer total (low) = 11.02+2.1+0.6+0.4+4.8 = 18.92.

### Self-insured persons (born after 1959)

**Self-insured persons (born after 1959)**  _(innovires; Ruskov & Kollegen; PwC)_

| Component | Rate | Source |
| --- | --- | --- |
| Pension (1st pillar) | 14.8% | innovires; Ruskov & Kollegen |
| 2nd pillar | 5% | innovires; PwC |
| Health (NHIF) | 8% | innovires; PwC |
| **Mandatory total** | **27.8%** | innovires; Ruskov & Kollegen; PwC |
| Optional Disease & Maternity | +3.5% | innovires |
| **With optional cover** | **31.3%** | innovires |

Self-check: 14.8 + 5 + 8 = 27.8; 27.8 + 3.5 = 31.3. Unemployment and work-accident funds do NOT apply.

### Floors and ceilings

**Floors and ceilings**  _(Ministry of Economy; PwC; Ruskov & Kollegen)_

| Item | 2025 (BGN) | 2026 (EUR) | Source |
| --- | --- | --- | --- |
| Min insurable income (employees, general) | 933 (Jan–Mar); 1,077 (Apr–Dec) | follows min wage 620.20 (= BGN 1,213) | Ministry of Economy; PwC |
| Min insurable income (self-insured) | 1,077 (= the minimum wage) | 550.66 (= BGN 1,077, carried over pending Budget Act; draft proposes 620.20) **[RESEARCH GAP — reviewer to confirm]** | PwC *Other taxes*; Ruskov & Kollegen |
| Max insurable income (ceiling, all) | 3,750 (Jan–Mar); 4,130 (Apr–Dec) | 2,111.64 (= BGN 4,130, carried over pending Budget Act; draft proposes 2,352) | Ministry of Economy; PwC *Other taxes* |
| Minimum monthly wage | 1,077 (from 1 Jan 2025, = EUR 550.66) | 620.20 (= BGN 1,213, from 1 Jan 2026; Council of Ministers Decree No. 243 of 13.11.2025) | Ministry of Economy; Ruskov & Kollegen |

Euro conversions at the irrevocable fixed rate BGN 1.95583 = EUR 1. Note the two distinct 2026 floors: the **employee** floor is the 2026 minimum wage EUR 620.20 (= BGN 1,213 / 1.95583 = 620.20); the **self-insured** floor is EUR 550.66 (= the 2025 BGN 1,077 carried over: 1,077 / 1.95583 = 550.66). These are NOT the same BGN amount — BGN 1,077 ≠ BGN 1,213. Ceiling: BGN 4,130 / 1.95583 = 2,111.65 (PwC rounds to EUR 2,111.64).

### Taxes (context)

**Taxes (context)**  _(Ministry of Economy; PwC; PwC corporate)_

| Tax | Rate | Source |
| --- | --- | --- |
| Personal income tax | 10% flat (no local/municipal PIT) | Ministry of Economy; PwC |
| Corporate income tax | 10% flat (no local CIT; Pillar Two QDMTT can lift effective rate to 15% for large groups) | PwC corporate |

### Forms and deadlines

**Forms and deadlines**  _(activpayroll; asanify; Lano; innovires; Ruskov & Kollegen; PwC; playroll)_

| Form | Purpose | Deadline | Source |
| --- | --- | --- | --- |
| Declaration 1 (Образец 1) | Per-employee insured data + contributions | 25th of following month | activpayroll; asanify; Lano |
| Declaration 6 (Образец 6) | Employer totals: contributions + withheld PIT; self-insured annual reconciliation | 25th of following month (employers) | activpayroll; innovires; Ruskov & Kollegen |
| Annual PIT return (GDD) | Self-insured annual reconciliation; freelancer/sole-trader income | 30 April following year | innovires; PwC |
| Monthly payment | Remittance of contributions + PIT to NRA | 25th of following month | Lano; playroll |

### Thresholds

**Thresholds**  _(innovires foreign-employer-registration; Ministry of Economy; ISSA; PwC)_

| Threshold | Detail | Source |
| --- | --- | --- |
| Employer registration | Employers (incl. foreign employers with staff in BG) must register with the NRA and report insured persons | innovires foreign-employer-registration |
| 2nd pillar eligibility | Applies only to persons born after 31 Dec 1959; pre-1960 pay the higher 19.8% state pension instead | Ministry of Economy; ISSA |
| Contribution cap | Income above the ceiling (BGN 4,130 H2-2025 / EUR 2,111.64 2026) is not subject to social or health contributions | Ministry of Economy; PwC |

### Penalties

**Penalties**  _(asanify; activpayroll; secondary guides; Interest on Taxes, Fees and Other State Receivables Act)_

| Penalty | Amount | Source |
| --- | --- | --- |
| Late/missed Declaration 1 or 6 | Reported ~EUR 250–500 per late filing, plus statutory interest | asanify; activpayroll **[RESEARCH GAP — reviewer to confirm]** |
| General non-compliance / contribution violations | BGN 500–10,000 depending on severity/recurrence (Social Security Code admin-penalty provisions) | asanify; secondary guides **[RESEARCH GAP — reviewer to confirm]** |
| Interest on overdue contributions | Statutory interest (BNB base rate + 10 pts, per the Interest Act) from the due date | general; verify against the Interest on Taxes, Fees and Other State Receivables Act **[RESEARCH GAP — reviewer to confirm]** |

### Test suite

All employees born after 31 Dec 1959 (Category III) unless stated; 2026 figures use ceiling EUR 2,111.64 and work-accident at the low end (0.4%).

Test 1: Employee, gross EUR 1,000/month, 2026. Within band. Employee SSC = 13.78% x 1,000 = EUR 137.80. PIT base = 1,000 - 137.80 = EUR 862.20. PIT = EUR 86.22. Net = 1,000 - 137.80 - 86.22 = EUR 775.98. Employer SSC (18.92%) = EUR 189.20.

Test 2: Employee, gross EUR 2,000/month, 2026. Within band. Employee SSC = EUR 275.60. PIT base = EUR 1,724.40. PIT = EUR 172.44. Net = EUR 1,551.96. Employer SSC (18.92%) = EUR 378.40. Total NRA outflow = 275.60 + 172.44 + 378.40 = EUR 826.44.

Test 3: Employee, gross EUR 3,000/month, 2026. Above ceiling → base EUR 2,111.64. Employee SSC = 13.78% x 2,111.64 = EUR 290.98. PIT base = 3,000 - 290.98 = EUR 2,709.02. PIT = EUR 270.90. Net = EUR 2,438.12.

Test 4: Employee born 1955 (pre-1960), gross EUR 2,000/month, 2026. Pension 19.8% (8.78/11.02), no 2nd pillar. Employee total = 8.78 + 1.4 + 0.4 + 3.2 = 13.78% x 2,000 = EUR 275.60 (the higher 1st-pillar employee pension 8.78 replaces 6.58+2.2=8.78, so the total is unchanged). Employer total = 11.02 + 2.1 + 0.6 + 0.4 + 4.8 = 18.92% x 2,000 = EUR 378.40 (11.02 replaces 8.22+2.8=11.02). PIT base = EUR 1,724.40; PIT = EUR 172.44.

Test 5: Self-insured person, declared income EUR 1,500/month, 2026, no optional cover. Contributions = 27.8% x 1,500 = EUR 417.00.

Test 6: Self-insured person, declared income EUR 1,500/month, 2026, WITH optional Disease & Maternity. Contributions = 31.3% x 1,500 = EUR 469.50.

Test 7: Self-insured person, declared income below the EUR 550.66 floor → clamp UP to EUR 550.66. Contributions = 27.8% x 550.66 = EUR 153.08. **[RESEARCH GAP — reviewer to confirm 2026 final floor]**

Test 8: Employee, 2025 H2 (Apr–Dec), gross BGN 5,000/month → above ceiling BGN 4,130 → base BGN 4,130. Employee SSC = 13.78% x 4,130 = BGN 569.11. PIT base = 5,000 - 569.11 = BGN 4,430.89. PIT = BGN 443.09. Net = 5,000 - 569.11 - 443.09 = BGN 3,987.80.

Arithmetic self-check (Test 8): 4,130 x 0.1378 = 569.114 → BGN 569.11; 5,000 - 569.11 = 4,430.89; x10% = 443.089 → 443.09; 5,000 - 569.11 - 443.09 = 3,987.80.

### Prohibitions

- **Fix period and employment status first** — NEVER compute Bulgarian contributions without first fixing the period (2025 BGN sub-period vs 2026 EUR) and the employment status (employee vs self-insured person).  _(Prohibitions section)_
- **2nd pillar only for post-1959 births** — NEVER apply the 2nd pillar (5%) to a person born before 1 Jan 1960 — they pay the higher 19.8% state pension and are outside the Universal Pension Fund.  _(Prohibitions section)_
- **Disease & Maternity optional for self-insured** — NEVER add the 3.5% Disease & Maternity to a self-insured person's rate unless they have voluntarily elected that cover.  _(Prohibitions section)_
- **No unemployment/work-accident for self-insured** — NEVER apply unemployment or work-accident contributions to a self-insured person — those funds do not apply.  _(Prohibitions section)_
- **2026 EUR floors/ceilings pending confirmation** — NEVER treat the 2026 EUR floors/ceilings (EUR 550.66 / EUR 2,111.64) as final after ~Aug 2026 — they are pending the Budget Act; flag and verify.  _(Prohibitions section)_
- **Work-accident rate needs NACE code** — NEVER pick a single work-accident rate inside 0.4%–1.1% without the NACE/economic-activity code — flag the gap.  _(Prohibitions section)_
- **PIT base calculation** — NEVER compute the PIT base on gross alone — it is gross MINUS the employee's mandatory social/health contributions, then x 10%.  _(Prohibitions section)_
- **Ceiling clamp for contributions** — NEVER omit the ceiling clamp — contributions stop at the maximum insurable income even though PIT continues on the full base.  _(Prohibitions section)_
- **No definitive penalty quantification** — NEVER quantify penalties or statutory interest from this skill's figures — they are secondary-source and unconfirmed; escalate.  _(Prohibitions section)_
- **Label figures as estimates** — NEVER present figures as definitive — label as estimated and direct the client to the NRA/NSSI and a Bulgarian-licensed accountant.  _(Prohibitions section)_

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
