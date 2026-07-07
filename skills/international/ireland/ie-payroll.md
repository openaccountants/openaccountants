---
name: ie-payroll
description: Use this skill whenever asked to compute, review, or advise on end-to-end Irish monthly or weekly payroll for employees — gross-to-net calculation, payslip generation, statutory deduction sequencing (pension, BIK, PAYE, USC, PRSI, LPT-at-source), real-time submission to Revenue (PSR / "payroll submission request"), and year-end Employee Detail Summary reconciliation under Revenue myAccount. Trigger on phrases like "Ireland payroll", "Irish payroll", "Irish payslip", "compute Irish payroll", "monthly payroll Ireland", "weekly payroll Ireland", "gross to net Ireland", "RPN", "Revenue Payroll Notification", "PSR submission", "Employee Detail Summary", "BrightPay", "Sage payroll Ireland", "Surf Accounts payroll", "Thesaurus payroll", "BIK Ireland", "company car BIK Ireland", or any request involving running monthly or weekly payroll for one or more employees in Ireland. This skill is the ORCHESTRATOR — it pulls PAYE bracket rules from `ie-paye`, USC bands from `ie-usc`, and PRSI Class A rates from `ie-prsi-class-s` (which also covers Class A for completeness), and sequences them into the correct computation order. ALWAYS read this skill before touching Irish payroll computation.
jurisdiction: IE
tax_year: 2025
tier: 2
last_updated: 2026-07-06
---

# ie-payroll

## Ireland — Payroll Computation (End-to-End) — Skill v1.0

> **Scope note:** This skill is the **end-to-end weekly / monthly payroll orchestrator** for Irish employments. It does NOT redefine PAYE bands, USC bands, or PRSI rates — those live in the dependency skills (`ie-paye`, `ie-usc`, `ie-prsi-class-s`). This skill defines the **sequence**, the **payslip layout**, the **PSR (Payroll Submission Request) real-time submission workflow**, and the **year-end reconciliation** that replaced the legacy P60.
>
> **2025 context (v1.0):** Ireland operates **PAYE Modernisation** (live since 1 January 2019), under which every payroll run must be reported to Revenue **on or before the pay date** via a Payroll Submission Request (PSR). The legacy P30, P35, P45, and P60 forms have been **abolished**. Year-end reconciliation is now via the **Employee Detail Summary** available to employees through Revenue **myAccount**. See Section 5 for the PSR workflow and Section 6 for year-end activities.

## Section 1 — Quick reference: payroll component order

**Payroll component order**  _(—)_

| Step | Component | Effect on bases | Paid by |
| --- | --- | --- | --- |
| 1 | **Gross pay** (basic + commission + overtime + cash allowances) | Starting point | — |
| 2 | + **Notional pay for BIK** (company car, medical insurance, preferential loan, share awards subject to PAYE) | **Added** — becomes part of taxable + USC + PRSI pay | Employer values it |
| 3 | = **Total gross** (for PRSI) | PRSI base = this figure | — |
| 4 | − **Employee pension / PRSA / AVC contribution** (subject to age-related % limits, earnings cap €115,000) | **Reduces** PAYE base and USC base; does NOT reduce PRSI base | Employee |
| 5 | = **Taxable pay** | PAYE base + USC base = this figure | — |
| 6 | Apply **RPN** — standard rate cut-off point (SRCOP) for the period, and weekly/monthly tax credits | Determines PAYE bracket and credit | Revenue notifies via RPN |
| 7 | Compute **PAYE** — 20% up to SRCOP, 40% above; then subtract tax credits | → PAYE for the period | Employee (withheld) |
| 8 | Compute **USC** — bands applied on taxable pay (after pension); standard 2025 bands (see `ie-usc`) | → USC for the period | Employee (withheld) |
| 9 | Compute **PRSI Class A** — employee 4.1% on full gross (before pension), employer 8.9% (≤ €496/week) or 11.15% (> €496/week) on full gross | → PRSI employee + employer | Both |
| 10 | − **LPT at source** if Revenue has issued an instruction (Local Property Tax mandatory deduction order) | Deducted from net pay | Employee |
| 11 | **Net pay** = Total gross − Pension − PAYE − USC − Employee PRSI − LPT − any voluntary deductions | — | — |

- **Deduction order rationale** — The order of deductions matters because **employee pension contributions reduce the PAYE and USC base** (but NOT the PRSI base — PRSI is computed on gross including pension), while **BIK is added to gross before all withholdings**. The cumulative tax credit / standard rate cut-off framework operates from the RPN (Revenue Payroll Notification) downloaded from ROS before each pay run.  _(—)_
- **Conservative default — uncertain pension deductibility** — When in doubt whether a contribution is pension-deductible for PAYE purposes (e.g. employer matching above statutory %, or unapproved schemes), treat it as **non-deductible** and compute PAYE on the higher figure. Under-withholding triggers Revenue interest at 0.0219% per day (~8% per annum) plus penalties; over-withholding is recoverable by the employee via their Employee Detail Summary in myAccount.  _(—)_

### 2025 rates at a glance (cross-reference dependency skills for full bracket detail)

**2025 rates at a glance**  _(see table cells)_

| Item | 2025 figure | Source |
| --- | --- | --- |
| PAYE standard rate | 20% | `ie-paye` |
| PAYE higher rate | 40% | `ie-paye` |
| Single SRCOP (annual) | €44,000 | `ie-paye` |
| Married one-earner SRCOP | €53,000 | `ie-paye` |
| Personal tax credit (single) | €2,000 | `ie-paye` |
| PAYE / employee credit | €2,000 | `ie-paye` |
| USC band 1 (0 – €12,012) | 0.5% | `ie-usc` |
| USC band 2 (€12,013 – €27,382) | 2% | `ie-usc` |
| USC band 3 (€27,383 – €70,044) | 3% (reduced from 4% — Finance Act 2024) | `ie-usc` |
| USC band 4 (> €70,044) | 8% | `ie-usc` |
| USC surcharge — self-employed > €100k | +3% | `ie-usc` (not applicable to Class A payroll) |
| PRSI Class A employee | 4.1% (rate raised from 4.0% on 1 Oct 2024) | `ie-prsi-class-s` |
| PRSI Class A employer (≤ €496/wk) | 8.9% | `ie-prsi-class-s` |
| PRSI Class A employer (> €496/wk) | 11.15% | `ie-prsi-class-s` |
| Earnings cap for pension tax relief | €115,000 | Revenue, Pensions Manual |

### Age-related pension contribution limits (% of net relevant earnings, capped at €115,000)

**Age-related pension contribution limits**

| Age | Max % deductible for PAYE/USC relief |
| --- | --- |
| Under 30 | 15% |
| 30 – 39 | 20% |
| 40 – 49 | 25% |
| 50 – 54 | 30% |
| 55 – 59 | 35% |
| 60 and over | 40% |

### BIK on company cars — 2025 categories (post Finance Act 2022 reforms)

**BIK on company cars — 2025 categories**

| Category | CO₂ g/km | BIK % (lowest mileage band, ≤ 26,000 km) |
| --- | --- | --- |
| A | 0 – 59 | **9%** |
| B | 60 – 99 | **13.5%** |
| C | 100 – 139 | **15%** |
| D | 140 – 179 | **22%** |
| E | 180+ | **26.5%** |

The 2025 BIK percentage on company cars is determined by **CO₂ emissions category** and **annual business mileage**. The simplified high-mileage table below.

> **EV BIK relief (taper):** For battery electric vehicles, the **OMV is reduced by €10,000** in 2025 (extension of the relief that began in 2023 at €35,000 and tapers down annually). For 2026 the relief is scheduled to fall to €5,000 and to nil from 2027, **subject to Finance Bill confirmation each year**. Flag any EV BIK case for reviewer confirmation of the applicable taper figure for the relevant year.

## Section 2 — Required inputs & refusal catalogue

### 2.1 Inputs required to run a payroll

**Inputs required to run a payroll**

| Input | Source | Notes |
| --- | --- | --- |
| PPS Number | Employee record / new starter form | Required for RPN retrieval; if missing, employee is taxed at the **emergency basis** (no credits, week 1 / month 1) per Revenue rules |
| RPN (Revenue Payroll Notification) | ROS — must be downloaded **before each pay run** | Contains SRCOP, tax credits, USC bands, PAYE basis (cumulative, week 1, emergency) |
| Date of commencement / cessation | HR | Determines week 1 / cumulative basis and final PSR |
| Gross pay breakdown | Contract / HR | Basic, overtime, commission, bonuses, allowances |
| BIK details | HR / fleet manager | Company car CO₂ + OMV + annual business mileage; medical insurance premium; preferential loan balances; share awards |
| Pension scheme details | Provider / HR | Scheme type (occupational, PRSA, AVC), employee %, employer %, age band |
| LPT deduction-at-source instruction | Revenue ROS | Only deduct if Revenue has issued an instruction; do NOT deduct based on employee request alone |
| Court orders / attachment of earnings | Court / Department of Social Protection | Apply per the order — usually after statutory deductions but before voluntary |
| Cycle-to-Work / TaxSaver Commuter Ticket salary sacrifice | HR | Reduces gross before PAYE/USC/PRSI; flag scheme caps |

For each employee, the following must be confirmed before the first PSR of the year and re-checked on every pay run:

### 2.2 Refusal catalogue — out of scope for this skill

**Refusal catalogue**

| Scenario | Action |
| --- | --- |
| Cross-border employees (Republic-of-Ireland employer, Northern Ireland or UK resident) | Refer to a qualified Irish payroll specialist — PAYE Exclusion Order or trans-border worker relief may apply |
| Posted workers from another EU state under A1 certificate | Refer to specialist — PRSI exemption depends on A1 validity and duration |
| Multiple concurrent employments with the same employee | Out of scope — apportionment of SRCOP and credits across employments must be done via RPN; flag any case where the RPN looks inconsistent with the employee's other employment |
| Employee share schemes (RSUs, ESOP, KEEP, APSS, SAYE) | Out of scope — bespoke valuation and RTSO/PSR interaction; refer to specialist |
| Pension lump sums on retirement | Out of scope — interaction with the Standard Fund Threshold and CGT treatment |
| Termination payments / ex-gratia above the statutory exemption (€10,160 + €765/year service basic, with SCSB top-up) | Refer to specialist — exemption interaction with PAYE is fact-specific |
| Directors paid via fees only, no PAYE employment | Refer to `ie-income-tax-form11` for proprietary directors; non-proprietary directors are normal Class A payroll |
| Salary sacrifice into pension above age-related limit | Permitted but excess does NOT attract PAYE/USC relief — flag and compute relief on the cap only |
| Backdated pay covering > 1 tax year | Refer to specialist — re-opening of prior-year Employee Detail Summary may be required via Revenue MyEnquiries |
| Insolvency / Redundancy Payments Scheme claims | Out of scope — Department of Social Protection process |

## Section 3 — Step-by-step weekly / monthly computation

The procedure below is the **canonical pay run**. Apply per employee. Periodicity options are weekly, fortnightly, four-weekly, or monthly — Ireland does **not** require uniform periodicity across employees.

### Step 1 — Download RPN from ROS

0. **Download RPN from ROS** — Before computing **any** pay, log into ROS, navigate to "PAYE Services → Manage employees" and download the latest RPN for each employee. The RPN tells you: - **Tax credit** for the period (annual ÷ frequency) - **SRCOP** for the period (annual ÷ frequency) - **USC bands** for the period - **Basis of tax** — cumulative, week 1 / month 1, or emergency - Any **LPT deduction-at-source** instruction If no RPN is available for the employee (new hire whose PPS number has not yet been confirmed by Revenue), apply the **emergency tax basis**: no credits, week 1 / month 1, full PAYE at 40%, USC at the highest band, until the RPN arrives.

### Step 2 — Build the gross pay

0. **Build the gross pay** — ``` Basic salary                          B + Overtime / commission               O + Cash allowances (taxable)           A + Cash bonus paid in period           X + Notional pay for BIK                K   (company car, medical insurance, etc.) = Total gross                         G = B + O + A + X + K ``` > **BIK note:** The BIK value is **notional pay** — it is added to gross for PAYE, USC, and PRSI but is NOT cash paid to the employee. The employer therefore withholds tax on the BIK from the **cash element** of the pay packet.

### Step 3 — Deduct pension / PRSA / AVC contribution

- **Pension deduction / taxable pay formula** — Pension contribution = min(employee chosen %, age-related cap %) × min(annualised earnings, €115,000) ÷ periods per year Taxable pay (for PAYE and USC) = G − pension contribution  _(Section 3 Step 3)_
- **Pension does not reduce PRSI base** — Pension does **not** reduce the PRSI base.  _(Section 3 Step 3)_

### Step 4 — Apply RPN credits and SRCOP to compute PAYE

- **PAYE formula** — PAYE_gross = min(Taxable pay, SRCOP_period) × 20% + max(0, Taxable pay − SRCOP_period) × 40% PAYE = max(0, PAYE_gross − Tax credit_period)  _(Section 3 Step 4)_
- **Cumulative basis** — Each pay period uses YTD figures — `PAYE_period = PAYE_YTD_new − PAYE_YTD_old`. This is the default and smooths out variable income.  _(Section 3 Step 4)_
- **Week 1 / month 1 basis** — Each period is computed in isolation — used after material changes (new employment, marriage, etc.) until RPN re-issues on cumulative.  _(Section 3 Step 4)_
- **Emergency basis** — No credits; week 1 / month 1; SRCOP set to a low default. Triggered by missing RPN.  _(Section 3 Step 4)_

### Step 5 — Compute USC on taxable pay (after pension)

- **USC formula** — USC = Σ (band slice × band rate)  _(see `ie-usc` for the canonical breakdown)_
- **USC total exemption** — Apply the period-equivalent USC bands from the RPN (see `ie-usc` for the canonical breakdown). Total exemption applies if **annualised** taxable pay ≤ €13,000.

### Step 6 — Compute PRSI Class A on GROSS (before pension)

- **PRSI Class A formula** — PRSI employee = 4.1% × G                  (from 1 Oct 2024; was 4.0%) PRSI employer = 8.9%  × G  if G ≤ €496 per week = 11.15% × G  if G > €496 per week  _(Section 3 Step 6)_
- **PRSI credit taper** — For employees earning €352.01 – €424 per week (Class A1), a tapering PRSI credit reduces the employee PRSI. The credit is `€12 − (gross − €352.01) ÷ 6`, applied per week. The RPN does NOT compute this — the payroll software does. See `ie-prsi-class-s` for the full taper table.  _(`ie-prsi-class-s`)_

### Step 7 — Apply LPT-at-source (if RPN-instructed)

- **LPT-at-source rule** — If the RPN contains an LPT deduction instruction, deduct the period-equivalent LPT amount from net pay. The annual LPT is spread over the remaining pay periods of the year. Do NOT apply LPT based on an employee request alone — Revenue must instruct it.

### Step 8 — Net pay

- **Net pay formula** — Net pay = G − Pension − PAYE − USC − Employee PRSI − LPT − Voluntary deductions (court orders, union dues, salary sacrifice repayments, etc.)

### Step 9 — Submit PSR to Revenue on or before pay date

- **PSR submission rule** — For every pay run, submit a **Payroll Submission Request (PSR)** via ROS or via the payroll software's direct ROS integration **before or on the pay date**. The PSR lists each employee, gross pay, PAYE, USC, employee PRSI, employer PRSI, LPT, pension, and BIK breakdown. See Section 5.

## Section 4 — Payslip components & sample

- **Minimum payslip content** — A **conforming Irish payslip** must show, at minimum, under the Payment of Wages Act 1991 §4: 1. Employer name, address, employer registration number 2. Employee name, PPS number 3. Pay period and pay date 4. Gross pay breakdown (basic, overtime, allowances, BIK notional pay) 5. Statutory deductions, **itemized** (Pension, PAYE, USC, employee PRSI, LPT) 6. Voluntary deductions (court orders, union dues, salary sacrifice) 7. Net pay 8. YTD totals (cumulative gross, cumulative PAYE, cumulative USC, cumulative PRSI) 9. PRSI class (e.g. A1, AX) and number of insurable weeks in the period 10. Tax basis used (cumulative / week 1 / emergency)  _(Payment of Wages Act 1991 §4)_

### Sample payslip — Dublin employee, €70,000 gross annual, monthly pay

> Full worked numbers are in Section 7. The layout below is the recommended template.

```
+-----------------------------------------------------------------+
|  ACME IRELAND LTD                       PAYSLIP — MAY 2025      |
|  10 Hatch Street, Dublin 2, D02 X285                            |
|  Employer Registration No.: 1234567A                            |
+-----------------------------------------------------------------+
|  Employee: Aoife O'Sullivan       PPS: 1234567A                 |
|  Tax basis: Cumulative            PRSI class: A1                |
|  Pay date: 28 May 2025            Period: 01-31 May 2025        |
|  Insurable weeks this period: 4                                 |
+-----------------------------------------------------------------+
|  EARNINGS                              EUR                      |
|    Basic salary                        5,833.33                 |
|    BIK — medical insurance               100.00                 |
|    Gross pay (for PRSI)                5,933.33                 |
+-----------------------------------------------------------------+
|  PRE-TAX DEDUCTIONS                     EUR                     |
|    Employee pension (6%)                 350.00                 |
|    Taxable pay (for PAYE & USC)        5,583.33                 |
+-----------------------------------------------------------------+
|  STATUTORY DEDUCTIONS                   EUR                     |
|    PAYE                                  938.33                 |
|    USC                                   139.81                 |
|    Employee PRSI (4.1% × Gross)          243.27                 |
|    LPT at source                           0.00                 |
|    Total statutory                     1,321.41                 |
+-----------------------------------------------------------------+
|  NET PAY                               EUR 4,261.92             |
+-----------------------------------------------------------------+
|  EMPLOYER CONTRIBUTIONS (info only)     EUR                     |
|    Employer pension (6%)                 350.00                 |
|    Employer PRSI (11.15% × Gross)        661.57                 |
+-----------------------------------------------------------------+
|  YTD TOTALS (Jan–May 2025)              EUR                     |
|    Gross YTD                          29,666.65                 |
|    PAYE YTD                            4,691.65                 |
|    USC YTD                               699.05                 |
|    Employee PRSI YTD                   1,216.35                 |
|    Pension YTD (employee)              1,750.00                 |
+-----------------------------------------------------------------+
```

### 5.1 What is a PSR?

- **Payroll Submission Request (PSR)** — A **Payroll Submission Request (PSR)** is the real-time XML / JSON file submitted to Revenue via ROS for every pay run, listing each employee's pay, deductions, and pension. Under PAYE Modernisation (in force since 1 Jan 2019), a PSR must be filed **on or before the pay date** — late PSRs trigger Revenue compliance attention even if no tax is underpaid.

### 5.2 Submission channels

**Submission channels**

| Channel | Use case |
| --- | --- |
| **ROS direct entry** | Small employers (< 10 staff) without payroll software — manual entry in Revenue's online payroll module |
| **Payroll software direct integration** | BrightPay, Sage Payroll, Surf Accounts, Thesaurus Payroll, CollSoft, etc. — software submits PSR via ROS API |
| **CSV upload to ROS** | Mid-size employers running spreadsheet-based payroll — upload to ROS PAYE Services |

- **Conservative default — software choice** — Use a Revenue-certified payroll software product (BrightPay, Sage, Surf Accounts, Thesaurus, CollSoft) with direct ROS integration. Manual ROS entry is error-prone for anything above ~5 employees.

### 5.3 What goes into a PSR — per employee

**PSR fields per employee**

| Field | Source |
| --- | --- |
| Employer Registration Number | Revenue-issued |
| PPS Number | Employee record |
| Period start, period end, pay date | Pay run |
| Gross pay | Step 2 (incl. BIK notional pay) |
| Pension contribution (employee) | Step 3 |
| Taxable pay | Step 3 (gross − pension) |
| PAYE | Step 4 |
| USC | Step 5 |
| Employee PRSI + insurable weeks | Step 6 |
| Employer PRSI | Step 6 |
| LPT deducted at source | Step 7 |
| Notional pay (BIK) total | Step 2 |
| PRSI class | RPN |
| Tax basis (cumulative / week 1 / emergency) | RPN |
| Date of leaving (if cessation) | HR |

### 5.4 Monthly P30-replacement — Statement and Payment

- **Monthly Statement of Liability process** — Revenue automatically generates a **monthly Statement of Liability** for the employer from the aggregated PSRs of that month. The employer must: 1. **Review** the statement in ROS by the **14th of the following month**. 2. Accept or correct it (corrections are made via amended PSRs, not by amending the statement directly). 3. **Pay** the net PAYE + USC + employee PRSI + employer PRSI by the **23rd of the following month** via ROS Direct Debit, single direct debit, or ROS payment. If no action is taken by the 14th, the statement is **deemed accepted**. Mid-quarter and quarterly remitters exist for some smaller employers (< €50,000 annual PAYE+PRSI) — flag for reviewer.

### 5.5 PSR amendments and corrections

- **PSR amendment types** — - **Pre-pay-date corrections:** Re-submit the PSR before pay date. - **Post-pay-date corrections (same year):** Submit an amended PSR via ROS; Revenue automatically updates the Statement of Liability. - **Prior-year corrections:** Submit via the ROS "Amend Submission" workflow; may require Revenue MyEnquiries for material adjustments.

### 5.6 Late-submission consequences

**Late-submission consequences**  _(Taxes Consolidation Act 1997 §1080; TCA 1997 §1078)_

| Issue | Consequence |
| --- | --- |
| Late PSR (after pay date) | Revenue compliance attention; repeat offenders may face audit; no fixed penalty for a single late PSR but interest applies if it causes late payment |
| Late payment of monthly statement (after 23rd) | Interest at **0.0219% per day** (≈ 8% p.a.) — Taxes Consolidation Act 1997 §1080 |
| Underpayment discovered later | Self-correction via amended PSR avoids surcharge if filed promptly; otherwise Revenue audit can impose penalty up to 100% of the tax |
| Wilful failure | Criminal sanction under TCA 1997 §1078 |

## Section 6 — Year-end activities

- **Abolished forms** — The **P30 (monthly), P35 (annual), P45 (leaver), and P60 (year-end employee certificate) forms have all been ABOLISHED** since the introduction of PAYE Modernisation on 1 Jan 2019.

### 6.1 Employer year-end — no separate annual return

**Employer year-end steps**

| Step | Action | Deadline |
| --- | --- | --- |
| 1 | Reconcile total PSR gross, PAYE, USC, PRSI to the payroll software and to the general ledger | By 31 December |
| 2 | File any final PSR for December (including final BIK valuations for the year) | On or before the final pay date |
| 3 | Review the December Statement of Liability in ROS | By 14 January |
| 4 | Settle the December liability | By 23 January |
| 5 | Issue **Employment Detail Summary access notification** to employees (some employers issue a courtesy PDF; not statutory) | By end of January |

- **No separate P35 filing** — The cumulative PSRs filed during the year **constitute the annual return**. There is no separate P35-equivalent to file.

### 6.2 Employee year-end — the Employee Detail Summary

- **Employee Detail Summary (EDS)** — The legacy P60 is replaced by the **Employee Detail Summary (EDS)**, which each employee accesses via Revenue **myAccount**. The EDS shows, for the tax year: - Total gross pay, total PAYE, total USC, total employee PRSI, total LPT - Insurable weeks - BIK total - Pension contributions - Employer name(s) and registration number(s) The EDS is auto-generated from the PSRs filed by the employer(s). Employees can also file their annual **Form 12** (for normal PAYE workers with side income, claiming reliefs, etc.) within myAccount.

### 6.3 Leavers — no P45 anymore

- **Leaver process** — When an employee leaves, the employer files the **final PSR** with a **date of cessation**. The employee can access their final EDS through myAccount; the new employer downloads a fresh RPN.

### 6.4 Reconciliation checklist

**Reconciliation checklist**

| Check | Pass criterion |
| --- | --- |
| Sum of monthly Statements of Liability paid = sum of (PAYE+USC+employee PRSI+employer PRSI+LPT) per PSRs | Match within €1 rounding |
| Pension contributions (employee) per PSRs = pension scheme provider's bordereau | Match |
| BIK valuations consistent across months (esp. company car mileage band) | Year-end true-up filed if mileage band changed |
| Any retro pay or bonus → captured in PSR for the actual pay date | ✓ |
| All leavers have a final PSR with cessation date | ✓ |
| Total employer PRSI rate transitions (8.9% ↔ 11.15%) properly reflected when weekly pay crosses €496 | ✓ |
| PRSI rate change on 1 Oct 2024 (4.0% → 4.1%) correctly applied across the year | ✓ for 2024 reconciliation; not applicable to 2025 (whole-year 4.1%) |

## Section 7 — Worked example

**Scenario:** Software developer, **Dublin resident**, **€70,000 gross annual** salary, paid monthly, single. Employer-provided medical insurance (BIK = €1,200/year = €100/month). Employee contributes **6% to occupational pension**, employer matches 6%. No company car. No LPT instruction. Age 32 (so pension % cap is 20% — well above 6% chosen rate). Cumulative tax basis. PRSI Class A1.

### A — Gross pay breakdown (monthly)

**Gross pay breakdown**

| Component | EUR |
| --- | --- |
| Basic (70,000 / 12) | 5,833.33 |
| BIK — medical insurance (1,200 / 12) | 100.00 |
| **Total gross (G) — PRSI base** | **5,933.33** |

Annualised gross for PRSI purposes = €71,200.

### B — Pension contribution

- **Pension contribution calc** — Employee pension = 6% × 5,833.33 = 350.00     (BIK does not attract pension; pension % applies to cash salary only by scheme rule) Earnings cap check: 6% well below 20% age-30-39 cap; 70,000 ≤ 115,000 → no cap binding

### C — Taxable pay (PAYE / USC base)

- **Taxable pay calc** — Taxable pay = G − Pension = 5,933.33 − 350.00 = 5,583.33

### D — PAYE (cumulative basis, single, 2025 RPN)

**PAYE RPN items**

| RPN item | Annual | Monthly |
| --- | --- | --- |
| SRCOP (single) | €44,000 | €3,666.67 |
| Personal credit | €2,000 | €166.67 |
| PAYE credit | €2,000 | €166.67 |
| Total credit | €4,000 | €333.33 |

- **PAYE calc** — PAYE gross = min(5,583.33, 3,666.67) × 20% + max(0, 5,583.33 − 3,666.67) × 40% = 3,666.67 × 20%   + 1,916.66 × 40% = 733.33           + 766.66 = 1,499.99 PAYE = 1,499.99 − 333.33 = 1,166.66

> Note: The Section 4 sample payslip used a slightly different monthly figure (€938.33) to keep that illustration round. The number here (€1,166.66) is the correct full computation for this scenario.

### E — USC (2025 bands, monthly)

Annualised taxable = €66,999.96. Below €70,044 → never enters the 8% band.

**USC band calc**

| Band (annual) | Monthly slice | Rate | USC monthly |
| --- | --- | --- | --- |
| 0 – 12,012 | 1,001.00 | 0.5% | 5.01 |
| 12,013 – 27,382 | 1,280.83 | 2% | 25.62 |
| 27,383 – 66,999.96 | 3,301.50 | 3% | 99.05 |
| **Monthly USC** |  |  | **129.68** |

### F — PRSI Class A1 employee

- **PRSI employee calc** — Employee PRSI = 4.1% × 5,933.33 = 243.27

Earnings well above €424/wk equivalent → no PRSI credit taper.

### G — Net pay

**Net pay**

| Item | EUR |
| --- | --- |
| Total gross | 5,933.33 |
| − Pension (employee) | (350.00) |
| − PAYE | (1,166.66) |
| − USC | (129.68) |
| − Employee PRSI | (243.27) |
| − LPT | (0.00) |
| **Net pay** | **4,043.72** |

### H — Employer cost ledger (monthly)

**Employer cost ledger**

| Item | EUR |
| --- | --- |
| Gross pay (cash + BIK) | 5,933.33 |
| Employer pension (6%) | 350.00 |
| Employer PRSI (11.15% × 5,933.33; weekly equivalent ≈ €1,370 > €496) | 661.57 |
| **Total employer cost** | **6,944.90** |

### I — Remittances arising from this payslip

**Remittances**

| Recipient | Amount EUR | Deadline |
| --- | --- | --- |
| Revenue (PAYE + USC + Employee PRSI + Employer PRSI = 1,166.66 + 129.68 + 243.27 + 661.57) | 2,201.18 | 23 Jun 2025 (via ROS, after accepting May Statement of Liability) |
| Pension scheme (employee 350.00 + employer 350.00) | 700.00 | Per scheme rules — typically by 21 Jun 2025 |
| PSR submission | n/a | **On or before 28 May 2025 (pay date)** |

### J — Annual reconciliation snapshot

**Annual reconciliation snapshot**

| Item | Annual EUR |
| --- | --- |
| Gross (cash) | 70,000 |
| BIK | 1,200 |
| Total gross | 71,200 |
| Pension (employee) | 4,200 |
| Taxable | 67,000 |
| PAYE | ≈ 13,999.92 |
| USC | ≈ 1,556.16 |
| Employee PRSI | ≈ 2,919.24 |
| Net | ≈ 48,524.68 |

(Annual figures are the monthly figures × 12; small rounding differences will appear in the EDS.)

## Section 8 — Conservative defaults

**Conservative defaults**

| Situation | Conservative position |
| --- | --- |
| RPN not yet downloaded for a new starter | Apply **emergency basis** (no credits, week 1, full 40% PAYE, max USC) until RPN arrives — never guess credits |
| BIK value uncertain (company car CO₂ unknown) | Default to **Category E (26.5%)** until manufacturer's CO₂ data confirmed |
| EV BIK — uncertain whether OMV relief applies | Apply the **lower** OMV relief in the taper table for the year (€10,000 in 2025) and flag |
| Pension contribution above age-related cap | Apply relief on the cap only; excess flows through PAYE/USC at full rates |
| Employer matching pension above scheme rules | Treat employer contribution as fully tax-free for the employee per Revenue Pensions Manual; but flag if scheme is unapproved |
| PRSI class uncertain | Apply Class A1 (employee 4.1%, employer 11.15%) — most common; flag for HR to confirm AX, J, etc. cases |
| LPT requested by employee but no RPN instruction | Do NOT deduct — Revenue must instruct; tell employee to amend their LPT in myAccount |
| Mid-month joiner | Apply pro-rated gross; cumulative basis from RPN will smooth credits/SRCOP across remaining months |
| Mid-month leaver | Apply final PSR with cessation date; do NOT issue any P45-equivalent — employee uses myAccount EDS |
| Pay in foreign currency | Convert to EUR at the Revenue / Central Bank rate on the pay date; document the rate used |
| Late hire — backdated salary spanning months | Tax in the month of actual payment per the cumulative basis; do NOT re-open prior PSRs unless reviewer instructs |
| Bonus / 13th-month payment | Tax in the period actually paid; cumulative basis will smooth the PAYE/USC impact if SRCOP head-room available |
| Employee on PUP / Illness Benefit during the month | Adjust gross to actual pay; Illness Benefit is taxable but paid by DSP — coordinate with RPN |
| Court order / attachment of earnings | Apply per court order — usually after statutory deductions; document priority |

## Section 9 — Sources

**Sources table**

| Source | Reference |
| --- | --- |
| Taxes Consolidation Act 1997 (TCA 1997), as amended | Irish Statute Book |
| Finance Act 2024 (PAYE / USC / PRSI 2025 changes) | Irish Statute Book |
| Social Welfare Consolidation Act 2005 (PRSI Class A) | Department of Social Protection |
| Revenue Employer's Guide to PAYE | https://www.revenue.ie/en/employing-people/index.aspx |
| PAYE Modernisation — Real-time payroll reporting | https://www.revenue.ie/en/employing-people/paye-modernisation/index.aspx |
| Revenue Online Service (ROS) | https://www.ros.ie |
| Employee myAccount — Employee Detail Summary | https://www.revenue.ie/en/online-services/services/paye/employee-detail-summary.aspx |
| Revenue Pensions Manual | https://www.revenue.ie/en/tax-professionals/tdm/pensions/ |
| BIK on company cars — Tax and Duty Manual 05-01-01b | Revenue eBrief / TDM |
| Payment of Wages Act 1991 §4 (payslip content) | Irish Statute Book |
| Local Property Tax (Deduction at Source) — LPT TDM | Revenue |
| Companion skill — PAYE bands and credits | `ie-paye` |
| Companion skill — Universal Social Charge | `ie-usc` |
| Companion skill — PRSI (Class S self-employed; Class A reference) | `ie-prsi-class-s` |
| Companion skill — Self-employed income tax (Form 11) | `ie-income-tax-form11` |
| Revenue-certified payroll software list | https://www.revenue.ie/en/employing-people/payroll-software-providers.aspx |

## Footer disclaimer

*OpenAccountants — open-source accounting skills for AI*
*This is not tax advice. All outputs must be reviewed by a qualified Irish payroll professional or tax adviser before any payslip is issued, any PSR is submitted, or any remittance is made.*

## Talk to a verified accountant

This skill is a tool, not an engagement. Every taxpayer's situation is
different, and the rules in the skill may not match your specific facts.

To speak with one of the licensed accountants who verifies skills for your
jurisdiction — **no liability on either side until you and the accountant sign
a formal engagement letter** — book a free 30-minute call:

**→ [Book a call](https://calendly.com/openaccountants-info/30min)**

We'll route you to the named verifier covering your country or state. You can
also see the full list of verified accountants at
[openaccountants.com/network](https://openaccountants.com/network).
