---
name: pk-payroll-eobi
description: ALWAYS read this skill before touching any Pakistan payroll work. Use whenever asked to compute, review, or advise on Pakistan monthly payroll — salary tax withholding under Section 149 of the Income Tax Ordinance 2001, Employees' Old-Age Benefits Institution (EOBI) federal pension contributions, provincial social security (SESSI Sindh, PESSI Punjab, KPESSI Khyber Pakhtunkhwa, BESSI Balochistan), Workers Welfare Fund (WWF), and Workers Profit Participation Fund (WPPF). Trigger on phrases like "Pakistan payroll", "salary tax Pakistan", "EOBI Pakistan", "PESSI Punjab", "SESSI Sindh", "PAYE Pakistan", "monthly statement Section 149", "WWF Pakistan", "WPPF Pakistan", "Section 165 statement", "Karachi payroll", "Lahore payroll", or any request involving running monthly payroll for one or more employees in Pakistan. This skill is the ORCHESTRATOR — it pulls salary bracket rates from `pk-income-tax` and sequences statutory deductions into the correct computation order.
jurisdiction: PK
tax_year: 2025
last_updated: 2026-07-13
reviewed_by: Ibrar Ali
review_status: current
tier: 1
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# PK Payroll Eobi

## Pakistan — Payroll (Salary Tax + EOBI + Provincial Social Security) — Skill v1.0

> **Scope note:** This skill is the **end-to-end monthly payroll orchestrator** for Pakistan. It does NOT redefine the salary tax brackets — those live in `pk-income-tax` and are applied here for monthly withholding under **Section 149** of the Income Tax Ordinance 2001 (ITO 2001). This skill defines the **sequence**, the **EOBI computation**, the **provincial social security routing**, the **WWF/WPPF treatment**, the **remittance calendar**, and the **year-end reconciliation workflow**.
>
> **Tax year 2025-26 note:** Pakistan's tax year runs **1 July – 30 June**. References to "2025-26" mean the year ending **30 June 2026**. Salary tax brackets are set annually by the Finance Act and are applied via `pk-income-tax`. EOBI rates have remained 5% employer / 1% employee on the federal minimum wage base for an extended period; provincial social security thresholds vary by province and are tracked here as ranges, not point estimates, because they are revised by provincial notification.

## Verified rates & thresholds (accountant-reviewed)

> Reviewed against the cited tax authorities by **Ibrar Ali** on 2026-06-12.
> Items flagged for further clarification are tracked separately and excluded here.
> This block is generated from verified `skill_facts` — edit the facts, not the prose.

### pk-payroll-eobi

- **Employer contribution** — 5% of federal minimum wage  _(Employees' Old-Age Benefits Act 1976)_
- **Employee contribution** — 1% of federal minimum wage  _(Employees' Old-Age Benefits Act 1976)_
- **Contribution base** — Rs. 40,000 per month  _(Federal notification)_
- **Coverage threshold** — Mandatory at ≥ 5 employees  _(EOBI Act 1976)_
- **Monthly contribution (PR-03/PR-04)** — Due 15th of following month  _(EOBI)_
- **SESSI (Sindh)** — 6% of insured worker's wage  _(Sindh Employees' Social Security Ordinance 1965)_
- **PESSI (Punjab)** — 6% of insured worker's wage  _(Punjab adapted 1965 Ordinance)_
- **KPESSI (KP)** — 6% (verify)  _(KP adapted 1965 Ordinance)_
- **BESSI (Balochistan)** — 6% (verify)  _(Balochistan adapted 1965 Ordinance)_
- **Insured-worker threshold** — Provincial minimum wage (PKR 40,000 for Punjab, Sindh, KP; PKR 37,000 for Balochistan)  _(Provincial notification)_
- **Routing** — To the province where the establishment/worker is employed  _(Provincial Ordinances)_
- **Monthly withholding mechanic** — Estimated annual salary tax / 12 (salary brackets from pk-income-tax)  _(ITO 2001 §149)_
- **§165 monthly statement** — 165 is filed quarterly and last date is 20 of the month following the quarter  _(ITO 2001 §165)_
- **Annual reconciliation + employee certificate** — By 31 July (Rule 42 certificate to each employee)  _(ITO 2001 §149; Rule 42)_
- **Workers Welfare Fund (WWF)** — 2% of accounting profit or taxable income, whichever is higher.  _(Workers Welfare Fund Ordinance 1971)_
- **Workers Profit Participation Fund (WPPF)** — 5% of profit before tax. Applies if: 50+ employees, OR paid-up capital/fixed assets exceed statutory provincial thresholds.  _(Companies Profits (Workers' Participation) Act 1968)_

## Section 1 — Quick reference: contribution table

The order matters because **only employee EOBI is deductible from salary**, and **none of the provincial social security contributions reduce the employee's chargeable salary for Section 149 purposes** unless paid by the employee (provincial social security is typically employer-only).

**Contribution table**  _(—)_

| Component | Rate | Base | Paid by | Effect on salary tax base |
| --- | --- | --- | --- | --- |
| **Salary tax (Sec 149 ITO 2001)** | Slab rates — see `pk-income-tax` | Annualised taxable salary | Employee (withheld at source) | — |
| **EOBI — Employee** | 1% | Federal minimum wage (currently Rs. 40,000/month – verify current notification) | Employee | **No reduction** of Section 149 base (statutory deduction, not allowed against salary income) |
| **EOBI — Employer** | 5% | Federal minimum wage | Employer | Employer cost only |
| **SESSI (Sindh)** | 6% | Wage of insured worker (workers earning ≤ provincial threshold) | Employer-only | Employer cost only |
| **PESSI (Punjab)** | 6% | Wage of insured worker (subject to Punjab ESSI Ordinance threshold) | Employer-only | Employer cost only |
| **KPESSI (Khyber Pakhtunkhwa)** | 6% (verify current notification) | Wage of insured worker | Employer-only | Employer cost only |
| **BESSI (Balochistan)** | 6% (verify current notification) | Wage of insured worker | Employer-only | Employer cost only |
| **WWF (Workers Welfare Fund)** | 2% | Taxable profit of company | Employer-only | Corporate-tax-side; not a payroll deduction |
| **WPPF (Workers Profit Participation Fund)** | 5% | Profit before tax (companies with 50+ employees, or threshold under provincial law) | Employer-only | Distributed to workers; not a salary-tax-side deduction |

> **Conservative default:** When in doubt whether a provincial social security scheme applies (because the employee's wage hovers around the provincial threshold), **include the contribution** and flag for reviewer. Under-contribution triggers provincial inspector recovery + penalty; over-contribution is harmless and can be reclaimed on later reconciliation.

- **Provincial routing rule of thumb** — the provincial social security institution of the **province where the establishment is located / where the worker is employed** receives the contribution — not the province of the worker's domicile.

## Section 2 — Required inputs & refusal catalogue

### 2.1 Inputs required to run a Pakistan payroll

**Inputs required to run a Pakistan payroll**

| Input | Source | Notes |
| --- | --- | --- |
| NTN (National Tax Number) — employer | FBR | Required on every Section 149 statement |
| CNIC of each employee | Employee record | Used as the FBR identifier where no NTN is held |
| NTN of each employee (if held) | Employee record | Required for higher earners |
| Province where the establishment is registered | Employer record | Determines SESSI / PESSI / KPESSI / BESSI routing |
| EOBI registration number | EOBI portal | Required if establishment has ≥ 5 employees (lower in some sectors) |
| Provincial social security registration | Provincial portal | Separate registration per province |
| Gross monthly emolument breakdown | HR / contract | Basic + allowances + perquisites |
| Perquisites in cash and kind | Accounts payable | Must be valued under Section 13 ITO 2001 |
| Federal minimum wage in force (for EOBI) | Federal notification | Verify current value — track Finance Act and notifications |
| Provincial wage threshold for ESSI coverage | Provincial notification | Determines whether the worker is "insured" |
| Whether employer has ≥ 50 employees (for WPPF) | HR headcount | WPPF applies only above the threshold |
| Whether employer is a company subject to WWF | Corporate tax status | WWF is corporate-side, computed in the tax return |

### 2.2 Refusal catalogue — out of scope

**Refusal catalogue — out of scope**

| Scenario | Action |
| --- | --- |
| Non-resident employees / split-pay / treaty relief | Refer to a qualified Pakistan tax consultant — treaty analysis required |
| Expatriates on Pakistan assignment with home-country payroll continuation | Out of scope; bespoke |
| Employee stock options, RSUs, share-based payments | Out of scope — Section 14 ITO valuation required by specialist |
| Termination payments, golden handshake, gratuity above statutory exemption | Flag — Section 12(6) and Sixth Schedule exemptions need legal review |
| Backdated salary spanning two tax years (Pakistan tax year ends 30 June) | Refer to specialist — re-opening of prior-year Section 165 statement may be needed |
| Provident Fund (recognised vs unrecognised) treatment | Out of scope here — refer to specialist; the Sixth Schedule rules on PF contributions and accumulated balances are complex |
| Directors' fees not run through payroll | Out of scope — covered by separate withholding under ITO Part III |
| Casual / piece-rate workers under the Industrial Relations Acts | Flag for reviewer — provincial coverage differs |

## Section 3 — Salary tax (Section 149 ITO 2001) — monthly withholding

### 3.1 Statutory basis

- **Statutory basis** — **Section 149 of the Income Tax Ordinance 2001** requires every employer paying salary to deduct tax at the time of payment, on the basis of the **estimated annual salary** for the tax year (1 July – 30 June). The bracket rates are set in the **First Schedule, Part I, Division I** of the ITO 2001, updated each year by the Finance Act. **Do not embed the rates here** — pull them from `pk-income-tax`, which is the canonical source.  _(Section 149 of the Income Tax Ordinance 2001)_

### 3.2 Monthly withholding mechanic

- **Monthly withholding mechanic** — 1.  Estimate annual taxable salary: AnnualTaxable = (Gross monthly × number of months remaining) + perquisites for the year + bonuses expected in the year − exemptions (Sixth Schedule items, e.g. some allowances) − allowable deductions for salaried persons (see pk-income-tax) 2.  Apply the First Schedule salary brackets (from pk-income-tax) to AnnualTaxable → AnnualTax 3.  Subtract any tax credits the employee has notified to the employer (Section 60 to 65 credits — e.g. donations under Sec 61, investment in approved pension fund under Sec 63, etc.; only those notified in writing) → AnnualTaxNet 4.  MonthlyWithholding = AnnualTaxNet / 12 (or / remaining months for a mid-year joiner) 5.  Adjust for under/over-withholding from earlier months in the same tax year — Section 149(3) permits this.

> **Note on bonuses and arrears:** Lump-sum bonuses, arrears and one-off payments must be **annualised into the estimated annual salary** and reflected in the recalculated monthly withholding from the month of payment forward — not taxed at marginal rate in a single month. This avoids over-withholding spikes.

### 3.3 Section 165 monthly statement

- **Filing requirement** — Every employer must file a **quarterly statement of tax withheld under Section 165** (and the related Income Tax Rules) by the **20th of the month following the quarter**, via the **FBR IRIS portal**. The statement covers all withholding categories, including Section 149 salary tax.

**Section 165 monthly statement fields**

| Field | Content |
| --- | --- |
| Employer NTN | Withholding agent identifier |
| Employee details | Name, CNIC, NTN (if any), gross salary, tax withheld |
| Payment date | For each salary payment |
| Tax challan / CPR number | Proof of deposit with FBR |

### 3.4 Annual employer certificate

- **Annual employer certificate obligations** — By **31 July** following the close of the tax year (30 June), every employer must: 1. File the **annual Section 149 / 165 reconciliation** on IRIS. 2. Issue each employee a **Certificate of Tax Collected/Deducted (Form prescribed under Rule 42 of the Income Tax Rules 2002)** showing gross salary, tax deducted by month, and CPR references — the employee uses this to file their own annual return.  _(Rule 42 of the Income Tax Rules 2002)_

### 3.5 Late-payment / late-statement penalties (summary)

**Late-payment / late-statement penalties (summary)**

| Default | Consequence |
| --- | --- |
| Late deposit of withheld tax | Default surcharge under Sec 205 (KIBOR + 3%) + recovery |
| Late filing of Section 165 statement | Penalty under Sec 182 — PKR 5,000 per day of default, subject to maxima |
| Failure to deduct | Employer personally liable for the tax + default surcharge (Sec 161) |

Full detail in `pk-income-tax`.

## Section 4 — EOBI — federal pension scheme

### 4.1 Statutory basis

- **Statutory basis** — **Employees' Old-Age Benefits Act 1976** (federal). Administered by the **Employees' Old-Age Benefits Institution (EOBI)**, an autonomous federal body. After the 18th Constitutional Amendment, social security was devolved to the provinces, but **EOBI continues to operate federally** pending substitute provincial pension legislation; courts have repeatedly upheld this. Treat EOBI as **federal and mandatory** in all four provinces and Islamabad Capital Territory.  _(Employees' Old-Age Benefits Act 1976)_

### 4.2 Coverage threshold

**Coverage threshold table**

| Establishment size | EOBI applicability |
| --- | --- |
| ≥ 5 employees | **Mandatory** registration and contribution |
| < 5 employees in some specified industries (e.g. shops & establishments under provincial law) | May still be covered — verify under the EOBI Act and current notifications |
| Once covered, always covered | Even if headcount later falls below 5, registration is retained |

### 4.3 Contribution rates and base

**Contribution rates and base**

| Party | Rate | Base |
| --- | --- | --- |
| Employer | **5%** | Federal minimum wage (notified periodically — **verify current notification each cycle**) |
| Employee | **1%** | Federal minimum wage |

> **Important — the base is the minimum wage, not the actual salary.** EOBI contributions are computed on the **prevailing federal minimum wage** (as notified), capped at that figure regardless of how much the employee actually earns. Track the current notification: at recent notifications the minimum wage figure was PKR 32,000 → PKR 37,000 → PKR 40,000 (and may be revised again). **Confirm the figure in force in the month of the contribution.**

### 4.4 Computation

- **EOBI computation formula** — EOBI Employer monthly  = 5% × MinimumWage EOBI Employee monthly  = 1% × MinimumWage  (deducted from employee's salary) Total EOBI monthly     = 6% × MinimumWage  per insured employee

### 4.5 Filing and payment

**Monthly EOBI contribution (PR-03 challan + PR-04 schedule of insured persons)**

| Item | Recipient | Deadline | Channel |
| --- | --- | --- | --- |
| Monthly EOBI contribution (PR-03 challan + PR-04 schedule of insured persons) | EOBI via designated banks | **15th of the following month** | EOBI online portal `eobi.gov.pk` + bank challan |

### 4.6 Penalty

- **EOBI penalty** — Late payment attracts a **monthly default surcharge** under the EOBI Act + recovery as arrears of land revenue. Long-running default also exposes directors personally under Section 12 EOBI Act.  _(Section 12 EOBI Act)_

## Section 5 — Provincial social security schemes

Each province operates its own **Employees Social Security Institution** under provincial law (post-18th Amendment). The schemes provide **medical care, sickness benefits, maternity, injury, and death benefits** to "insured" workers — i.e. workers whose monthly wage is at or below a provincial threshold.

### 5.1 The four provincial institutions

**The four provincial institutions**

| Province | Institution | Statute | Threshold (verify current notification) | Rate (employer-only) |
| --- | --- | --- | --- | --- |
| **Sindh** | **SESSI** (Sindh Employees Social Security Institution) | Provincial Employees' Social Security Ordinance 1965 as adapted by Sindh | Wage threshold: PKR 40,000/month (Punjab, Sindh, KP); PKR 37,000/month (Balochistan) — track current provincial notifications | **6%** of wage of insured employee |
| **Punjab** | **PESSI** (Punjab Employees Social Security Institution) | Provincial Employees Social Security Ordinance 1965 (Punjab Adapted) | Punjab-notified threshold — track current PESSI notification | **6%** of wage of insured employee |
| **Khyber Pakhtunkhwa** | **KPESSI** | KP adaptation of the 1965 Ordinance | KP-notified threshold | **6%** (verify) |
| **Balochistan** | **BESSI** | Balochistan adaptation of the 1965 Ordinance | Balochistan-notified threshold | **6%** (verify) |

> **Threshold caveat:** the wage threshold for "insured person" status is **revised by provincial notification**. The rule is: if the employee's **gross wage ≤ threshold in force**, the worker is an "insured person" and the employer must contribute **6% of that worker's actual wage** to the provincial institution. Workers above the threshold are typically excluded (but check the latest notification — some provinces have extended coverage to all workers).

### 5.2 Computation

- **Provincial social security computation** — ProvincialSS_monthly = 6% × Wage(insured employee) (per worker, for each insured worker)
- **Employer-only, no reduction, routing** — - **Employer-only** — there is no employee share. - **Does NOT reduce the employee's salary tax base** because it is not deducted from the employee. - Routed to the **province where the establishment is located** — i.e. the place of employment, not the worker's domicile.

### 5.3 Filing and payment

**Filing and payment table**

| Item | Deadline | Channel |
| --- | --- | --- |
| Monthly contribution + return of insured persons | Typically **by the 15th** of the following month (verify per-province) | Provincial ESSI portal + designated banks |
| Annual reconciliation | Per provincial rules — typically by 31 July | Provincial ESSI portal |

### 5.4 Penalty

Each province has its own penalty regime, typically:

- Default surcharge at a notified monthly rate.
- Recovery by the provincial Social Security Department as arrears of land revenue.
- Criminal liability of directors / partners under the 1965 Ordinance for sustained default.

### 5.5 Inter-province workers

- **Inter-province workers** — If an establishment has branches in more than one province, contributions are made to **each provincial institution for the workers employed at the establishment in that province**. There is no cross-province credit — each province collects on its own workers.

## Section 6 — Other employer-side deductions: WWF and WPPF

These are **corporate-side** levies, not strictly payroll, but they are commonly run through the HR / finance interface because the WPPF distribution flows to the workers.

### 6.1 Workers Welfare Fund (WWF)

**Workers Welfare Fund (WWF) table**

| Element | Detail |
| --- | --- |
| Statute | **Workers Welfare Fund Ordinance 1971** (federal; provincial variants also enacted post-18th Amendment — see caveat) |
| Rate | **2% of accounting profit or taxable income, whichever is higher** (companies) |
| Base | Accounting profit or taxable income of the establishment, whichever is higher |
| Paid by | **Employer only** — not deducted from employee |
| Routed to | Federal WWF or provincial WWF, depending on the establishment's jurisdiction and current case law |
| Frequency | Annual — assessed via the corporate tax return |

> **Jurisdictional caveat:** Post-18th Amendment, Sindh, Punjab, KP and Balochistan enacted their own **Provincial Workers Welfare Fund** statutes. Supreme Court of Pakistan judgments (notably *Workers Welfare Funds v Various* line of cases) have produced complex routing rules between the federal and provincial WWFs depending on the period and the entity. **Defer the WWF jurisdiction question to the corporate tax skill / a qualified Pakistani tax consultant** — flag any direct WWF computation request to a reviewer.

### 6.2 Workers Profit Participation Fund (WPPF)

**Workers Profit Participation Fund (WPPF) table**

| Element | Detail |
| --- | --- |
| Statute | **Companies Profits (Workers' Participation) Act 1968** |
| Threshold | Companies with **50+ employees**, OR where paid-up capital/fixed assets exceed statutory provincial thresholds |
| Rate | **5% of profit before tax** |
| Distribution | Distributed to eligible workers in accordance with the Act + Scheme (subject to per-worker ceiling) |
| Residual | Any undistributed balance is transferred to the WWF |
| Paid by | **Employer only** |
| Frequency | Annual — within nine months of close of accounting year (per the Act and Scheme) |

> **Workers profit participation interacts with WWF** — undistributed WPPF flows to WWF. This linkage is corporate-tax-side and is handled in the corporate compliance skill, not here.

## Section 7 — Worked example

**Scenario:** Software developer, **Karachi (Sindh) resident**, employed at a Karachi-based fintech with 35 employees. Gross monthly emolument **PKR 250,000**. Pakistani citizen, CNIC and NTN held. Employer is EOBI-registered. Tax year 2025-26.

**Assumed inputs (verify each from current notifications and `pk-income-tax`):**

- Federal minimum wage in force for EOBI: **PKR 40,000/month** (placeholder — verify current notification)
- SESSI wage threshold for "insured person": **PKR 50,000/month** (placeholder — verify Sindh notification). At PKR 250,000/month the employee is **above the threshold → not an insured person → no SESSI contribution payable**.
- Salary tax brackets: pulled from `pk-income-tax` (do **not** rely on the numbers below for any other purpose).
- No bonus or perquisites in this month.

### A — Salary tax (Section 149) — illustration only

- **Salary tax illustration** — Annual taxable salary = 250,000 × 12         = 3,000,000 Apply 2025-26 First Schedule salary brackets (from pk-income-tax). For illustration only (DO NOT use as authoritative — pk-income-tax governs): Slice 1:   0 –   600,000        @  0%     =        0 Slice 2:   600,001 – 1,200,000  @  5%     =   30,000 Slice 3:   1,200,001 – 2,200,000 @ 15%    =  150,000 Slice 4:   2,200,001 – 3,000,000 @ 25%    =  200,000 Annual tax (illustrative)                  =  380,000 Monthly withholding (illustrative)         =   31,667

> The bracket numbers above are **illustrative placeholders** — the real computation MUST be done by `pk-income-tax`, which carries the Finance Act 2025 rates.

### B — EOBI

- **EOBI computation for example** — EOBI Employee (1% × 40,000)        =   400 EOBI Employer (5% × 40,000)        = 2,000

### C — SESSI (Sindh)

Employee's wage PKR 250,000 > assumed threshold PKR 50,000 → **not insured** → **no SESSI contribution**.

If the same employee earned PKR 40,000:
```
SESSI Employer (6% × 40,000)       = 2,400      (employer-only)
```

### D — WWF / WPPF

Not run through this payslip — computed annually on profit-before-tax in the corporate tax return.

### E — Payslip summary (illustrative)

**Payslip summary**

| Item | PKR |
| --- | --- |
| Gross monthly emolument | 250,000 |
| − Salary tax withheld (Sec 149) | (31,667) *illustrative — pk-income-tax governs* |
| − EOBI employee | (370) |
| **Net pay** | **217,963** |

### F — Remittances arising from this payslip

**Remittances table**

| Recipient | Amount PKR | Deadline |
| --- | --- | --- |
| FBR (Section 149 salary tax) | 31,667 | Deposit by **15th of following month** via challan; Section 165 statement by **20th of the month following the quarter** on IRIS |
| EOBI (employee 400 + employer 2,000) | 2,400 | **15th of following month** — PR-03 / PR-04 via EOBI portal and bank |
| SESSI | n/a | — |

## Section 8 — Filing and payment calendar

### 8.1 Monthly cycle

**Monthly cycle table**

| Item | Recipient | Deadline | Channel |
| --- | --- | --- | --- |
| **Salary tax deposit** | FBR | At time of payment (challan deposited promptly — typically **within 7 days of withholding**; verify current rule) | Bank challan (CPR) |
| **Section 165 quarterly statement** | FBR | **20th of the month following the quarter** | FBR **IRIS** portal |
| **EOBI contribution + PR-04 schedule** | EOBI | **15th of the following month** | EOBI portal + designated bank |
| **Provincial ESSI contribution** | SESSI / PESSI / KPESSI / BESSI | Typically **15th of the following month** (verify per-province) | Provincial ESSI portal + designated bank |

### 8.2 Annual cycle

**Annual cycle table**

| Item | Deadline | Notes |
| --- | --- | --- |
| **Annual Section 149 / 165 reconciliation** | **31 July** following tax-year-end 30 June | Filed on IRIS — must reconcile sum of monthly statements to annual withholding |
| **Employee tax deduction certificate** (Rule 42) | **By the time of the annual statement** | Issued to each employee for use in their own return |
| **EOBI annual reconciliation** | Per EOBI rules | Reconcile sum of monthly PR-04 schedules to insured headcount × 12 |
| **Provincial ESSI annual reconciliation** | Per provincial notification | Typically by 31 July |
| **WWF (corporate)** | With corporate tax return | Out of scope here |
| **WPPF distribution** | **Within 9 months of accounting-year-end** | Out of scope here; residual to WWF |

### 8.3 Penalty summary

**Penalty summary table**

| Default | Consequence |
| --- | --- |
| Late salary tax deposit | Default surcharge under Sec 205 ITO 2001 (KIBOR + 3%) |
| Late Section 165 statement | Sec 182 penalty — PKR 5,000/day, subject to caps |
| Failure to deduct salary tax | Employer personally liable (Sec 161) + surcharge |
| Late EOBI | Default surcharge per EOBI Act + recovery as arrears of land revenue |
| Late provincial ESSI | Per provincial regime — surcharge + recovery |

## Section 9 — Conservative defaults

**Conservative defaults table**

| Situation | Conservative position |
| --- | --- |
| EOBI coverage uncertain (establishment hovering around 5 employees) | Treat as covered; register on EOBI portal; under-contribution risk outweighs the small monthly cost |
| Provincial ESSI threshold ambiguous | Treat employee as insured if wage near threshold; contribute and reclaim later if unnecessary |
| Minimum wage notification updated mid-month | Apply the **higher** rate from the date of notification; do not back-spread |
| Bonus or arrears paid in one month | Annualise into the Sec 149 estimated annual salary and recompute monthly withholding from that month forward — do **not** apply marginal rate to the lump sum in a single month |
| Employee CNIC missing | Withhold normally but **flag immediately** — Section 165 statement will reject without CNIC |
| Employee NTN missing (high earner) | Compute tax normally; flag to HR to enrol the employee on IRIS — required for higher-earner statements |
| Mid-year joiner | Estimate the annual salary on a pro-rata basis (months remaining × monthly gross + expected perquisites) and divide the tax by the remaining months |
| Mid-year leaver | Issue interim Rule 42 certificate covering the period of employment, reconcile via Section 149(3) adjustment in the leaver's final month |
| Worker in Punjab establishment but resident in Sindh | Contribute to **PESSI** (province of employment), not SESSI |
| Multi-province establishment | Contribute to each provincial ESSI for the workers physically employed there |
| WWF / WPPF computation request | Refer to corporate tax skill / reviewer — jurisdictional routing is complex post-18th Amendment |
| Provident Fund deduction | Refer to specialist — Sixth Schedule treatment depends on recognition status |
| Salary paid in foreign currency | Convert to PKR at the SBP rate on payment date; document the rate |

## Section 10 — Sources

**Sources table**

| Source | Reference |
| --- | --- |
| Income Tax Ordinance 2001 — Section 149 (deduction of tax from salary) | FBR |
| Income Tax Ordinance 2001 — Section 165 (statement of tax collected or deducted) | FBR |
| Income Tax Ordinance 2001 — First Schedule Part I (salary brackets) | FBR — applied via `pk-income-tax` |
| Income Tax Rules 2002 — Rule 42 (employee tax deduction certificate) | FBR |
| Employees' Old-Age Benefits Act 1976 | EOBI |
| EOBI portal | https://eobi.gov.pk |
| Provincial Employees' Social Security Ordinance 1965 (as adapted by Sindh, Punjab, KP, Balochistan) | Provincial gazettes |
| Sindh Employees Social Security Institution (SESSI) | https://sessi.gos.pk |
| Punjab Employees Social Security Institution (PESSI) | https://pessi.punjab.gov.pk |
| Khyber Pakhtunkhwa Employees Social Security Institution (KPESSI) | KP provincial portal |
| Balochistan Employees Social Security Institution (BESSI) | Balochistan provincial portal |
| Workers Welfare Fund Ordinance 1971 + provincial WWF statutes | Federal / provincial gazettes |
| Companies Profits (Workers' Participation) Act 1968 (WPPF) | Federal gazette |
| FBR IRIS portal | https://iris.fbr.gov.pk |
| Companion skill — Pakistan income tax (salary brackets, slabs, tax credits) | `pk-income-tax` |
| Companion skill — Pakistan sales tax | `pakistan-sales-tax` |
| Foundation skill — global workflow base | `foundation` |

## Footer disclaimer

*OpenAccountants — open-source accounting skills for AI*
*This is not tax advice. All outputs must be reviewed by a qualified Pakistani payroll professional or tax consultant before any payslip is issued or any remittance is made.*

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
