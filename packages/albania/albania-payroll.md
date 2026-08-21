---
name: albania-payroll
description: Use this skill whenever asked about Albania payroll processing for employed persons. Trigger on phrases like "Albania payroll", "Albanian payroll", "lista e pagave", "payroll list Albania", "PAYE Albania", "withholding tax Albania", "tatimi mbi te ardhurat Albania", "social insurance Albania", "sigurime shoqerore", "sigurime shendetesore", "health insurance contribution Albania", "ISSH contribution", "net salary Albania", "neto pagese", "gross to net Albania", "employer contribution Albania", "16.7%", "11.2%", "DIVA Albania", "minimum wage Albania", "paga minimale", "tatime.gov.al payroll", or any question about computing employee pay, withholding tax (PIT), or social/health insurance contributions for Albania-based employees. This skill covers cumulative monthly PIT withholding under Law 29/2023, social and health insurance contributions (employee and employer shares), the social-insurance floor and ceiling, the minimum wage, the monthly payroll-list declaration, and the annual DIVA reconciliation. ALWAYS read this skill before processing any Albania payroll.
version: 0.1
jurisdiction: AL
tax_year: 2025
last_updated: 2026-07-13
review_status: pending_review
depends_on: - payroll-workflow-base
category: payroll
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Albania Payroll Skill v0.1 (Tier 2 — research-verified, reviewer sign-off pending)

## Albania Payroll Skill v0.1 (Tier 2 — research-verified, reviewer sign-off pending)

> **Tier 2 status.** Every rate, threshold, and deadline below is sourced to a named authority or Big-4 summary (PwC Worldwide Tax Summaries, KPMG Albania) and cited inline. It has **not** yet been section-by-section verified by a licensed Albanian accountant. Items marked **[RESEARCH GAP — reviewer to confirm]** carry residual uncertainty and must be confirmed against primary sources before reliance.

## Section 1 -- Quick Reference

**Quick Reference table**

| Field | Value |
| --- | --- |
| Country | Albania (Republic of Albania) |
| Currency | ALL (Albanian Lek) only |
| Standard pay frequency | Monthly |
| Tax year | Calendar year (1 January -- 31 December) |
| Tax withholding system | Cumulative monthly PAYE-style withholding by the employer (payroll agent), reconciled annually (Law 29/2023) |
| PIT annual rates | 13% up to 2,040,000 ALL; 23% on the excess (PwC; KPMG) |
| Employer contribution rate | 16.7% (15% social + 1.7% health) (PwC) |
| Employee contribution rate | 11.2% (9.5% social + 1.7% health) (PwC) |
| Social-insurance base (2025) | Floor 40,000 ALL / ceiling 176,416 ALL per month (HLB Albania; rate guides) |
| Health-insurance base | Full gross salary — no floor, no ceiling (PwC) |
| Minimum wage (2025) | 40,000 ALL/month gross (HLB Albania; Karanovic & Partners) |
| Tax authority | General Directorate of Taxation — Drejtoria e Pergjithshme e Tatimeve (GDT/DPT), tatime.gov.al |
| Social-insurance authority | Social Insurance Institute — Instituti i Sigurimeve Shoqerore (ISSH), issh.gov.al |
| Collection | Contributions and PIT declared and paid **jointly** via the GDT e-filing portal |
| Key legislation | Law No. 29/2023 "On Income Tax" (effective 1 Jan 2024); Law No. 9136/2003 (contributions collection); Law No. 9920/2008 "On Tax Procedures"; VKM (Council of Ministers Decision) on the minimum wage |
| Monthly declaration deadline | 20th of the month following the payroll period (PwC; tatime.gov.al) |
| Annual reconciliation | DIVA (Deklarata Individuale Vjetore e te Ardhurave) — 31 March of the following year (PwC) |
| Validated by | Pending — requires sign-off by a licensed Albanian accountant |
| Skill version | 0.1 (Tier 2) |

## Section 2 -- Income Tax Withholding (PIT, Law 29/2023)

Albania **does** levy personal income tax on employment income. The regime was reformed by **Law No. 29/2023 "On Income Tax"**, effective from 1 January 2024 and **unchanged for tax year 2025** (PwC — Significant developments; KPMG Albania). The employer acts as withholding/payroll agent and withholds PIT monthly, with an annual reconciliation.

### 2.1 Annual rate brackets (statutory basis)

**Annual rate brackets (statutory basis)**  _(PwC Worldwide Tax Summaries; KPMG Albania)_

| Annual employment income (ALL) | Rate | Source |
| --- | --- | --- |
| 0 -- 2,040,000 | 13% | PwC Worldwide Tax Summaries; KPMG Albania |
| Over 2,040,000 | 23% on the excess above 2,040,000 | PwC; KPMG |

### 2.2 Operational monthly withholding table (PwC — the figures payroll software uses)

The annual 13%/23% structure is implemented through a banded **monthly** withholding table. Use the **PwC 2025 table** below (break-points 50,000 / 60,000 / 200,000 ALL). **Do NOT** use the table still shown on the tatime.gov.al English page — see the caveat in Section 11.

**Operational monthly withholding table**  _(PwC — Taxes on personal income)_

| Monthly gross salary (ALL) | Monthly PIT | Source |
| --- | --- | --- |
| Up to 50,000 | **0%** (fully exempt) | PwC — Taxes on personal income |
| 50,001 -- 60,000 | 0% on the first 35,000; **13%** on the portion exceeding 35,000 | PwC — Taxes on personal income |
| Above 60,000 | 0% on the first 30,000; **13%** on the portion 30,001 -- 200,000; **22,100 ALL + 23%** on the portion exceeding 200,000 | PwC — Taxes on personal income |

- **Arithmetic check on the 22,100 ALL constant** — In the "above 60,000" band the 13% slice runs from 30,001 to 200,000 → 13% × (200,000 − 30,000) = 13% × 170,000 = 22,100 ALL. The constant reconciles to the cumulative tax at the 200,000 cutover. (Self-verified.)  _(Self-verified)_

### 2.3 Withholding method

- **Cumulative monthly withholding** — Cumulative monthly PAYE-style withholding by the employer, proportional to the annual 13%/23% thresholds, reconciled annually.  _(KPMG; PwC)_
- **Joint declaration** — PIT and contributions are declared and paid together monthly via the GDT portal.
- **Residence basis** — Residents are taxed on worldwide income; non-residents are taxed only on Albania-sourced (territorial) income.  _(PwC)_

> **[RESEARCH GAP — reviewer to confirm]** Whether the 11.2% employee social+health contributions are deducted from gross *before* PIT is computed. The research `conservative_defaults` instruct deducting contributions first, but the PwC monthly table is defined on **monthly gross salary**. This skill applies the PwC banded table to **gross salary** for the band determination (the literal PwC reading) in all worked examples, and flags the alternative (contributions-first) method here. The precise mechanics of the phased deductions in the 50,000–60,000 band reportedly depend on standard annual deduction tiers (600,000 / 420,000 / 360,000 ALL); a licensed Albanian accountant must confirm the exact formula against current GDT Albanian-language guidance and the payroll software.

## Section 3 -- Social and Health Insurance -- Employee Deductions

Employee contributions total **11.2%** of gross, split between social insurance and health insurance, withheld by the employer (PwC — Other taxes).

**Employee deductions table**  _(PwC)_

| Contribution | Employee rate | Base | Source |
| --- | --- | --- | --- |
| Social insurance (pension/social) | 9.5% | Monthly gross between floor 40,000 ALL and ceiling 176,416 ALL (2025) | PwC; HLB Albania |
| Health insurance | 1.7% | **Full** monthly gross — no floor, no ceiling | PwC |
| **Total employee** | **11.2%** | see component bases | PwC |

- **Column check** — 9.5% + 1.7% = 11.2% ✓ (Self-verified.)  _(Self-verified)_
- **Social component floor/ceiling** — The 9.5% social component is capped at the ceiling (176,416 ALL) and floored at 40,000 ALL (2025).  _(PwC; HLB Albania)_
- **Health component no cap/floor** — The 1.7% health component is assessed on full gross with no cap or floor.  _(PwC)_

## Section 4 -- Social and Health Insurance -- Employer Contributions

Employer contributions total **16.7%** of gross (PwC — Other taxes).

**Employer contributions table**  _(PwC)_

| Contribution | Employer rate | Base | Source |
| --- | --- | --- | --- |
| Social insurance (pension/social) | 15% | Monthly gross between floor 40,000 ALL and ceiling 176,416 ALL (2025) | PwC; HLB Albania |
| Health insurance | 1.7% | **Full** monthly gross — no floor, no ceiling | PwC |
| **Total employer** | **16.7%** | see component bases | PwC |

- **Column check** — 15% + 1.7% = 16.7% ✓ (Self-verified.)  _(Self-verified)_

### 4.1 Combined burden

**Combined burden table**

| Party | Social | Health | Total |
| --- | --- | --- | --- |
| Employee | 9.5% | 1.7% | 11.2% |
| Employer | 15% | 1.7% | 16.7% |
| **Combined** | **24.5%** | **3.4%** | **27.9%** |

- **Total-row check** — Total-row check: social column 9.5 + 15 = 24.5 ✓; health column 1.7 + 1.7 = 3.4 ✓; total column 11.2 + 16.7 = 27.9 ✓; and 24.5 + 3.4 = 27.9 ✓. (Self-verified — all three additions reconcile.)  _(Self-verified)_

### 4.2 Self-employed (reference only — not employer payroll)

**Self-employed contributions table**  _(PwC — Other taxes; PwC; HLB Albania)_

| Contribution | Rate | Base | Source |
| --- | --- | --- | --- |
| Self-employed (non-agriculture) social insurance | 23% (combined) | Not less than the minimum salary; minimum monthly base 40,000 ALL (2025) | PwC — Other taxes |
| Self-employed health insurance | 3.4% (combined) | Not less than twice the minimum salary (≈ 80,000 ALL in 2025) | PwC; HLB Albania |

> **[RESEARCH GAP — reviewer to confirm]** The self-employed health base of "twice the minimum salary" is stated as 100,000 ALL in 2026 sources (2× the 2026 minimum of 50,000). The 2025 equivalent (2× 40,000 = 80,000 ALL) was not directly confirmed from a primary source for 2025. Self-employed payroll is out of scope for this skill — see `albania-income-tax` / `albania-self-employed` for the self-employed regime.

## Section 5 -- Minimum Wage and Contribution Base

**Minimum wage and contribution base table**

| Item | 2025 value | Source |
| --- | --- | --- |
| National minimum wage | 40,000 ALL/month gross (in force since March 2023, based on 174 normal working hours/month) | HLB Albania; Karanovic & Partners |
| Social-insurance floor | 40,000 ALL/month (equal to minimum wage) | PwC; HLB Albania |
| Social-insurance ceiling | 176,416 ALL/month (indexed with the minimum wage) | HLB Albania; rate guides |
| Health-insurance base | Full gross — no floor, no ceiling | PwC |

### 5.1 2026 change (forward-looking, NOT applied to 2025 payroll)

- **2026 minimum wage increase** — From 1 January 2026, the minimum wage rises to 50,000 ALL/month under Council of Ministers Decision No. 776 dated 19 December 2025. The social-insurance floor moves to 50,000 ALL and the ceiling rises.  _(HLB Albania; Karanovic & Partners)_

> **[RESEARCH GAP — reviewer to confirm]** Sources disagree on the post-1-Jan-2026 **maximum social-insurance base**: HLB states **186,416 ALL** (a flat +10,000 increase matching the minimum-wage rise) while Karanovic/secondary summaries state **220,520 ALL** (a +25% indexation). The 2025 figure (176,416 ALL) is consistent across sources. Confirm the 2026 ceiling from the official ISSH/GDT publication before applying to any 2026 period.

## Section 6 -- Conservative Defaults

When inputs are ambiguous, apply these defaults and flag the assumption to the user:

- **1. Monthly withholding table** — Use the PwC 2025 monthly table (50,000 / 60,000 / 200,000 ALL break-points), NOT the outdated table on the tatime.gov.al English page (30,000 / 150,000 / 15,600 ALL), which reflects the pre-2024 Law 8438/1998 regime.  _(PwC; caveat Section 11)_
- **2. Contribution base (2025)** — Apply social-insurance floor 40,000 ALL and ceiling 176,416 ALL. For periods from 1 January 2026, the floor becomes 50,000 ALL and the ceiling rises (exact 2026 ceiling unresolved — see Section 5.1).
- **3. Health insurance base** — The 1.7% employer + 1.7% employee health components are computed on full gross with no cap or floor; apply the cap/floor only to the 15%/9.5% social-insurance components.
- **4. PIT band determination** — Determine the PIT band from monthly gross salary per the PwC table. (The alternative — deducting 11.2% contributions before PIT — is flagged as a research gap in Section 2.3; do not silently switch methods.)
- **5. Currency** — All amounts in ALL. Never assume EUR.
- **6. Residence** — Assume the employee is an Albanian tax resident unless told otherwise (worldwide-income basis). For non-residents, only Albania-sourced employment income is taxed.  _(PwC)_

## Section 7 -- Required Inputs and Refusal Catalogue

### 7.1 Required inputs (must have before computing)

**Required inputs table**

| Input | Why needed |
| --- | --- |
| Monthly **gross** salary in ALL | Drives PIT band, social base (subject to floor/ceiling), and health base |
| Pay period (month/year) | Determines which floor/ceiling and minimum wage apply (2025 vs 2026 differ) |
| Employee tax residence (resident / non-resident) | Resident = worldwide; non-resident = Albania-source only |
| Whether the employee has more than one employer | Triggers mandatory DIVA annual filing (Section 9) |
| Full-time / part-time and hours | Affects whether the 40,000 ALL social floor binds (part-time / partial month) |
| Employer registration status with GDT | Must be registered before running payroll; foreign employers too |

### 7.2 Refusal catalogue — STOP and ask rather than guess

**Refusal catalogue table**

| Situation | Action |
| --- | --- |
| Salary stated in EUR or another currency | **Refuse to compute.** Ask for the ALL gross amount (or the FX basis the employer uses). |
| Pay period in 2026 or later | Compute using 2025 figures **only if** the user confirms; otherwise flag that the floor (50,000 ALL) and ceiling changed and the 2026 ceiling is unresolved (Section 5.1). |
| Employee may be a non-resident | Confirm residence; do not apply worldwide basis to a non-resident. |
| User asks for the "official" monthly table and quotes the tatime.gov.al 30,000/150,000 figures | Do not use them — explain they are the pre-2024 regime; use the PwC 2025 table (Section 11). |
| Self-employed / sole trader, not an employee | Out of scope — direct to the self-employed/income-tax skill (Section 4.2). |
| Request to compute exact penalty amounts for late filing / unregistered workers | State the 10% late-payment penalty + interest (sourced) and flag that exact administrative-fine figures are unconfirmed (Section 10). |
| Net-to-gross "gross-up" with a target net | Possible but iterative; state that the result is an estimate and that the contributions-vs-PIT ordering gap (Section 2.3) affects the answer. |

## Section 8 -- Transaction / Payment Pattern Library

Deterministic classification of typical Albanian bank-statement lines (descriptions appear in Albanian and English). Match on the **uppercased** description.

### 8.1 Salary credits (to employees)

**Salary credits table**

| Pattern (ALL bank statement) | Classification |
| --- | --- |
| `PAGE`, `PAGESA`, `PAGA NETO`, `RROGA` | Net salary payment |
| `SALARY`, `NET SALARY`, `WAGES` | Net salary payment |
| `PAGESE PAGE [emri]` | Net salary to named employee |
| `PARADHENIE PAGE`, `ADVANCE SALARY` | Salary advance — reconcile against month-end net |
| `BONUS`, `SHPERBLIM` | Bonus — taxable employment income |

### 8.2 Employer debits to the State (GDT / ISSH)

**Employer debits table**

| Pattern | Classification |
| --- | --- |
| `DPT`, `TATIME`, `GDT`, `TAP` (tatimi mbi te ardhurat personale) | PIT withheld remitted to GDT |
| `SIGURIME SHOQERORE`, `KONTRIBUTE SHOQERORE`, `SOCIAL INSURANCE` | Social-insurance contribution (employer + employee share remitted together) |
| `SIGURIME SHENDETESORE`, `HEALTH INSURANCE` | Health-insurance contribution (employer + employee share) |
| `ISSH`, `INSTITUTI I SIGURIMEVE SHOQERORE` | Social-insurance institute remittance |
| `LISTA E PAGAVE`, `PAYROLL LIST` | Combined monthly payroll-list payment (PIT + social + health) |

### 8.3 Non-payroll / not income

**Non-payroll table**

| Pattern | Classification |
| --- | --- |
| `RIMBURSIM`, `REFUND` | Reimbursement / refund — not salary |
| `SHPENZIM UDHETIMI`, `TRAVEL EXPENSE` | Expense reimbursement — review for taxability |
| `KESTI KREDISE`, `LOAN REPAYMENT` | Loan deduction — not an employer cost |

## Section 9 -- Worked Examples

All figures in ALL, tax year 2025. Social base = gross clamped to [40,000 ; 176,416]; health base = full gross; PIT per the PwC monthly table (Section 2.2). Each line is recomputed end-to-end below.

### Example A — Gross 45,000 ALL/month (within social band, below PIT threshold)

**Example A table**

| Line | Computation | Amount |
| --- | --- | --- |
| Gross | — | 45,000.00 |
| Social base | 45,000 within [40,000;176,416] | 45,000.00 |
| Employee social | 9.5% × 45,000 | 4,275.00 |
| Employee health | 1.7% × 45,000 | 765.00 |
| **Employee contributions** | 4,275 + 765 | **5,040.00** |
| PIT | gross ≤ 50,000 → 0% | 0.00 |
| **Net pay** | 45,000 − 5,040 − 0 | **39,960.00** |
| Employer social | 15% × 45,000 | 6,750.00 |
| Employer health | 1.7% × 45,000 | 765.00 |
| **Employer contributions** | 6,750 + 765 | **7,515.00** |
| **Total employer cost** | 45,000 + 7,515 | **52,515.00** |

### Example B — Gross 55,000 ALL/month (50,001–60,000 PIT band)

**Example B table**

| Line | Computation | Amount |
| --- | --- | --- |
| Gross | — | 55,000.00 |
| Social base | 55,000 within band | 55,000.00 |
| Employee social | 9.5% × 55,000 | 5,225.00 |
| Employee health | 1.7% × 55,000 | 935.00 |
| **Employee contributions** | 5,225 + 935 | **6,160.00** |
| PIT | 0% on first 35,000; 13% × (55,000 − 35,000) = 13% × 20,000 | 2,600.00 |
| **Net pay** | 55,000 − 6,160 − 2,600 | **46,240.00** |
| Employer social | 15% × 55,000 | 8,250.00 |
| Employer health | 1.7% × 55,000 | 935.00 |
| **Employer contributions** | 8,250 + 935 | **9,185.00** |
| **Total employer cost** | 55,000 + 9,185 | **64,185.00** |

### Example C — Gross 120,000 ALL/month (above 60,000 band, below ceiling and below 200,000)

**Example C table**

| Line | Computation | Amount |
| --- | --- | --- |
| Gross | — | 120,000.00 |
| Social base | 120,000 < 176,416 | 120,000.00 |
| Employee social | 9.5% × 120,000 | 11,400.00 |
| Employee health | 1.7% × 120,000 | 2,040.00 |
| **Employee contributions** | 11,400 + 2,040 | **13,440.00** |
| PIT | 0% on first 30,000; 13% × (120,000 − 30,000) = 13% × 90,000 | 11,700.00 |
| **Net pay** | 120,000 − 13,440 − 11,700 | **94,860.00** |
| Employer social | 15% × 120,000 | 18,000.00 |
| Employer health | 1.7% × 120,000 | 2,040.00 |
| **Employer contributions** | 18,000 + 2,040 | **20,040.00** |
| **Total employer cost** | 120,000 + 20,040 | **140,040.00** |

### Example D — Gross 250,000 ALL/month (above social ceiling AND above 200,000 PIT cutover)

**Example D table**

| Line | Computation | Amount |
| --- | --- | --- |
| Gross | — | 250,000.00 |
| Social base | capped at ceiling | 176,416.00 |
| Employee social | 9.5% × 176,416 | 16,759.52 |
| Employee health | 1.7% × 250,000 (uncapped) | 4,250.00 |
| **Employee contributions** | 16,759.52 + 4,250 | **21,009.52** |
| PIT | 22,100 + 23% × (250,000 − 200,000) = 22,100 + 23% × 50,000 = 22,100 + 11,500 | 33,600.00 |
| **Net pay** | 250,000 − 21,009.52 − 33,600 | **195,390.48** |
| Employer social | 15% × 176,416 | 26,462.40 |
| Employer health | 1.7% × 250,000 | 4,250.00 |
| **Employer contributions** | 26,462.40 + 4,250 | **30,712.40** |
| **Total employer cost** | 250,000 + 30,712.40 | **280,712.40** |

### Example E — Minimum wage, gross 40,000 ALL/month (floor edge)

**Example E table**

| Line | Computation | Amount |
| --- | --- | --- |
| Gross | — | 40,000.00 |
| Social base | = floor 40,000 | 40,000.00 |
| Employee social | 9.5% × 40,000 | 3,800.00 |
| Employee health | 1.7% × 40,000 | 680.00 |
| **Employee contributions** | 3,800 + 680 | **4,480.00** |
| PIT | gross ≤ 50,000 → 0% | 0.00 |
| **Net pay** | 40,000 − 4,480 − 0 | **35,520.00** |
| Employer social | 15% × 40,000 | 6,000.00 |
| Employer health | 1.7% × 40,000 | 680.00 |
| **Employer contributions** | 6,000 + 680 | **6,680.00** |
| **Total employer cost** | 40,000 + 6,680 | **46,680.00** |

### Example F — Part-time, gross 30,000 ALL/month (below social floor)

A part-time / partial-month wage can be below the 40,000 ALL social floor. The **social** components are computed on the **40,000 floor**, while the **health** components use the **actual gross** (no floor).

**Example F table**

| Line | Computation | Amount |
| --- | --- | --- |
| Gross | — | 30,000.00 |
| Social base | floored at 40,000 | 40,000.00 |
| Employee social | 9.5% × 40,000 | 3,800.00 |
| Employee health | 1.7% × 30,000 (no floor) | 510.00 |
| **Employee contributions** | 3,800 + 510 | **4,310.00** |
| PIT | gross ≤ 50,000 → 0% | 0.00 |
| **Net pay** | 30,000 − 4,310 − 0 | **25,690.00** |
| Employer social | 15% × 40,000 | 6,000.00 |
| Employer health | 1.7% × 30,000 | 510.00 |
| **Employer contributions** | 6,000 + 510 | **6,510.00** |
| **Total employer cost** | 30,000 + 6,510 | **36,510.00** |

> **[RESEARCH GAP — reviewer to confirm]** The exact treatment of a sub-floor part-time / partial-month wage (whether the 40,000 ALL floor is pro-rated for part-time, or applied in full) was not confirmed from a primary source. Example F applies the full floor conservatively; a licensed Albanian accountant should confirm the pro-ration rule.

## Section 10 -- Tier 1 Rules (deterministic — apply mechanically)

- **PIT rate bands (annual)** — PIT exists on employment income; 13% up to 2,040,000 ALL/year, 23% above  _(PwC; KPMG)_
- **Monthly withholding table to use** — Use the PwC 2025 monthly withholding table (break-points 50,000 / 60,000 / 200,000 ALL), not the pre-2024 tatime.gov.al English table (Section 11)  _(PwC)_
- **Salary ≤ 50,000 ALL/month** — 0% PIT  _(PwC)_
- **Salary 50,001–60,000 ALL/month** — 0% on first 35,000, 13% on the excess  _(PwC)_
- **Salary > 60,000 ALL/month** — 0% on first 30,000, 13% on 30,001–200,000, then 22,100 ALL + 23% on the excess over 200,000  _(PwC)_
- **Employer contributions rate** — 16.7% (15% social + 1.7% health)  _(PwC)_
- **Employee contributions rate** — 11.2% (9.5% social + 1.7% health)  _(PwC)_
- **Combined employer + employee burden** — 27.9%  _(PwC; arithmetic verified Section 4.1)_
- **2025 social base floor/ceiling** — floor 40,000 ALL, ceiling 176,416 ALL; cap/floor apply ONLY to the 15%/9.5% social components  _(HLB Albania; rate guides)_
- **Health components basis** — Health components (1.7% each) are on full gross — no floor, no ceiling  _(PwC)_
- **2025 minimum wage** — 40,000 ALL/month  _(HLB Albania; Karanovic & Partners)_
- **Monthly payroll declaration deadline** — Monthly payroll list (PIT + social + health) declared and paid electronically by the 20th of the following month  _(PwC; tatime.gov.al)_
- **DIVA annual return deadline** — DIVA annual return due 31 March of the following year; balance of tax also due 31 March  _(PwC)_
- **Employer/employee registration requirement** — Employers (including foreign companies without a local entity) must register with the GDT and register each employee at least one day before work starts  _(Rivermate; tatime.gov.al)_
- **Late payment penalty** — Late payment of tax/contributions → 10% penalty + default interest under the Law on Tax Procedures (No. 9920/2008)  _(Playroll; statute)_

## Section 11 -- Tier 2 Catalogue (reviewer judgement required)

These items require a licensed Albanian accountant's judgement and/or confirmation against primary sources before reliance.
1. **Monthly bracket discrepancy.** The tatime.gov.al English page still displays an **outdated** monthly table (0% to 30,000; 13% on 30,001–150,000; 15,600 ALL + 23% over 150,000) reflecting the pre-2024 **Law 8438/1998** regime. The current 2025 structure (Law 29/2023) is the **PwC** table used in this skill (50,000 / 60,000 / 200,000 break-points). A reviewer should confirm the exact monthly withholding formula against current GDT Albanian-language guidance and the payroll software, including the phased-deduction mechanics of the 50,000–60,000 band (reportedly linked to standard annual deduction tiers of 600,000 / 420,000 / 360,000 ALL).
2. **Contributions-vs-PIT ordering** (Section 2.3) — confirm whether the 11.2% employee contributions are deducted before PIT.
3. **2026 social ceiling** (Section 5.1) — HLB (186,416 ALL) vs Karanovic/secondary (220,520 ALL); confirm from ISSH/GDT before applying any 2026 period.
4. **Penalty amounts** (Section 10, rule 15 and below) — the 10% late-payment penalty + interest is from secondary summaries; exact administrative fines for late payroll declaration and for unregistered workers must be confirmed against the primary text of Law No. 9920/2008.
5. **Part-time social floor** pro-ration (Section 9, Example F).
6. **DIVA scope** for a given employee (single vs multiple employers, other non-final-withholding income) — confirm filing obligation (Section 12.2).

### 12.1 Monthly — Payroll list ("Lista e pagave")

**Monthly payroll list filing table**  _(PwC; tatime.gov.al; Rivermate)_

| Form | Purpose | Deadline | Source |
| --- | --- | --- | --- |
| Monthly payroll / withholding & contributions declaration ("Lista e pagave") | Declare and pay employees' PIT withheld plus employer + employee social and health contributions, filed electronically via the GDT portal | By the **20th** of the month following the payroll period | PwC; tatime.gov.al; Rivermate |

### 12.2 Annual — DIVA

**Annual DIVA filing table**  _(PwC — Tax administration; tatime.gov.al)_

| Form | Purpose | Deadline | Source |
| --- | --- | --- | --- |
| Annual Individual Income Declaration — DIVA (Deklarata Individuale Vjetore e te Ardhurave) | Year-end reconciliation of total income; balance of tax due | **31 March** of the year following the tax year | PwC — Tax administration; tatime.gov.al |

- **DIVA filing triggers** — Resident with annual taxable income over 1,200,000 ALL; or individuals with more than one employer (any amount); or other non-final-withholding income over 50,000 ALL. Self-employed / traders always file.  _(PwC — Tax administration)_

## Section 13 -- Thresholds Reference Table

**Thresholds Reference Table**  _(PwC; KPMG; HLB Albania; Karanovic & Partners; tatime.gov.al; Council of Ministers Decision No. 776/2025)_

| Threshold | Value | Source |
| --- | --- | --- |
| Annual PIT rate threshold (13% → 23%) | 2,040,000 ALL annual taxable employment income | PwC; KPMG |
| Monthly fully-exempt salary ceiling | 50,000 ALL/month (≤ this is 0% PIT) | PwC |
| Monthly 23% cutover | 200,000 ALL/month taxable salary | PwC |
| Social-insurance floor (2025) | 40,000 ALL/month | PwC; HLB Albania; rate guides |
| Social-insurance ceiling (2025) | 176,416 ALL/month | HLB Albania; rate guides |
| Health-insurance base | Full gross — no floor, no ceiling | PwC |
| Minimum wage (2025) | 40,000 ALL/month | HLB Albania; Karanovic & Partners |
| Minimum wage (from 1 Jan 2026) | 50,000 ALL/month | Council of Ministers Decision No. 776/2025 |
| DIVA annual filing trigger | Annual income > 1,200,000 ALL, OR any income from > 1 employer, OR other non-final income > 50,000 ALL | PwC — Tax administration |
| Monthly declaration deadline | 20th of following month | PwC; tatime.gov.al |
| DIVA deadline | 31 March following year | PwC |

Sanity check: ceiling (176,416) ≥ floor (40,000) ✓; all rates 1.7%–23% are plausible payroll percentages ✓. (Self-verified.)

## Section 14 -- Penalties

**Penalties table**  _(Playroll; Law No. 9920/2008)_

| Penalty | Detail | Source |
| --- | --- | --- |
| Late payment of tax / contributions | **10%** of the unpaid liability + default interest (interest per the Law on Tax Procedures / Ministry of Finance rate) | Playroll; Law No. 9920/2008 |
| Failure to register an employee / undeclared work | Administrative fines under Law No. 9920/2008; significant per-employee penalties — **[RESEARCH GAP — reviewer to confirm]** exact amount not confirmed from a primary source | tatime.gov.al; Law No. 9920/2008 |
| Late filing of a mandatory declaration | Fixed administrative fine (e.g. 10,000 ALL per month of delay cited for certain annual filings) — **[RESEARCH GAP — reviewer to confirm]** the specific payroll-declaration figure is from secondary summaries (Wise/Playroll), not confirmed from a primary source | Law No. 9920/2008 (secondary) |

## Section 15 -- Excel Working Paper Template

**Excel working paper template**  _(input)_

| Row | Label | Formula / source |
| --- | --- | --- |
| 1 | Employee name | input |
| 2 | Pay period (month/year) | input |
| 3 | Tax residence (R/NR) | input |
| 4 | **Gross salary** | input |
| 5 | Social base | `=MIN(MAX(B4,40000),176416)` (2025 floor/ceiling) |
| 6 | Health base | `=B4` (full gross, no cap) |
| 7 | Employee social (9.5%) | `=B5*0.095` |
| 8 | Employee health (1.7%) | `=B6*0.017` |
| 9 | **Employee contributions** | `=B7+B8` |
| 10 | PIT band | `=IF(B4<=50000,"0%",IF(B4<=60000,"50-60k",">60k"))` |
| 11 | **PIT withheld** | `=IF(B4<=50000,0,IF(B4<=60000,(B4-35000)*0.13,IF(B4<=200000,(B4-30000)*0.13,22100+(B4-200000)*0.23)))` |
| 12 | **Net pay** | `=B4-B9-B11` |
| 13 | Employer social (15%) | `=B5*0.15` |
| 14 | Employer health (1.7%) | `=B6*0.017` |
| 15 | **Employer contributions** | `=B13+B14` |
| 16 | **Total employer cost** | `=B4+B15` |
| 17 | Monthly remittance to GDT | `=B11+B9+B15` (PIT + employee + employer contributions) |

Reproduce this layout in a single worksheet (one column per employee, or one row per employee for a register). All cells in ALL.

**Cross-check against Example C (gross 120,000):** row 5 = 120,000; row 7 = 11,400; row 8 = 2,040; row 9 = 13,440; row 11 = (120,000−30,000)×0.13 = 11,700; row 12 = 94,860; row 15 = 20,040; row 16 = 140,040. ✓ Matches Example C exactly.

## Section 16 -- Bank Statement / Terminology Reading Guide

**Albanian to English payroll terminology**

| Albanian | English |
| --- | --- |
| Paga / Rroga | Salary / wage |
| Paga bruto | Gross salary |
| Paga neto | Net salary |
| Lista e pagave | Payroll list (monthly declaration) |
| Tatimi mbi te ardhurat personale (TAP) | Personal income tax (PIT) |
| Sigurime shoqerore | Social insurance |
| Sigurime shendetesore | Health insurance |
| Kontribute | Contributions |
| Paga minimale | Minimum wage |
| Drejtoria e Pergjithshme e Tatimeve (DPT) | General Directorate of Taxation (GDT) |
| Instituti i Sigurimeve Shoqerore (ISSH) | Social Insurance Institute |
| Deklarata Individuale Vjetore e te Ardhurave (DIVA) | Annual Individual Income Declaration |
| Shperblim / Bonus | Bonus |
| Paradhenie page | Salary advance |
| Gjobe | Penalty / fine |
| Interes | Interest |

## Section 17 -- Onboarding Fallback

If the user has not provided enough to run payroll, collect in this order:
1. Monthly **gross** salary in ALL (refuse if given in EUR — Section 7.2).
2. Pay period (month + year) — confirm 2025 vs 2026 figures.
3. Tax residence (resident / non-resident).
4. Whether the employee has more than one employer (DIVA trigger).
5. Full-time / part-time and contracted hours (floor edge — Section 9 Example F).
6. Confirm the employer is registered with the GDT and the employee was registered ≥ 1 day before starting (Section 10, rule 14).

If any required input is missing, state what is missing and **do not** fabricate a figure.

## Section 18 -- Interaction with Other Skills

**Interaction with other skills table**

| Scenario | Skill to Use |
| --- | --- |
| Employee payroll (PIT + social + health) | **This skill (albania-payroll.md)** |
| Self-employed / sole-trader income & contributions | albania-income-tax.md / albania-self-employed.md |
| Albania VAT (TVSH) returns | albania-vat-return.md |
| Albania corporate income tax | albania-corporate-tax.md |
| Albania bookkeeping | albania-bookkeeping.md |

### Key handoff points

- **Payroll → Bookkeeping:** gross wages and the 16.7% employer contributions are expenses; PIT withheld and the 11.2% employee contributions are liabilities until remitted on the 20th.
- **Payroll → Income Tax:** the year's withholding feeds the employee's DIVA reconciliation where a DIVA filing is required (Section 12.2).

### 19.1 Sources

**Sources table**

| # | Title | Publisher | URL |
| --- | --- | --- | --- |
| 1 | Albania — Individual — Taxes on personal income | PwC Worldwide Tax Summaries | https://taxsummaries.pwc.com/albania/individual/taxes-on-personal-income |
| 2 | Albania — Individual — Other taxes (social and health insurance) | PwC Worldwide Tax Summaries | https://taxsummaries.pwc.com/albania/individual/other-taxes |
| 3 | Albania — Individual — Tax administration | PwC Worldwide Tax Summaries | https://taxsummaries.pwc.com/albania/individual/tax-administration |
| 4 | Albania — Individual — Significant developments | PwC Worldwide Tax Summaries | https://taxsummaries.pwc.com/albania/individual/significant-developments |
| 5 | Taxation of Employment Income in 2024 | KPMG Albania | https://kpmg.com/al/en/insights/2023/09/taxation-of-employment-income-in-2024.html |
| 6 | Increase of the Minimum Wage in Albania from 1 January 2026 | HLB Albania | https://www.hlb.al/increase-of-the-minimum-wage-in-albania-from-1-january-2026-what-changes-for-employers-and-employees/ |
| 7 | Albania Adopts New Decision on National Minimum Wage (No. 776/2025) | Karanovic & Partners | https://www.karanovicpartners.com/news/albania-adopts-new-decision-on-national-minimum-wage/ |
| 8 | Tax on personal income | General Directorate of Taxation (tatime.gov.al) | https://www.tatime.gov.al/eng/c/4/96/108/tax-on-personal-income |
| 9 | Employment Taxes in Albania | Rivermate | https://www.rivermate.com/guides/albania/taxes |
| 10 | How to Run Payroll in Albania | Playroll | https://www.playroll.com/payroll/albania |

### 19.2 Test Suite (numbered — recompute to confirm any change)

**Test suite table**

| # | Input | Expected output | Recomputation |
| --- | --- | --- | --- |
| 1 | Gross 45,000 | Net 39,960; employer cost 52,515 | Ex. A — emp. contrib 5,040; PIT 0 |
| 2 | Gross 55,000 | Net 46,240; PIT 2,600; employer cost 64,185 | Ex. B — 13% × 20,000 = 2,600 |
| 3 | Gross 120,000 | Net 94,860; PIT 11,700; employer cost 140,040 | Ex. C — 13% × 90,000 = 11,700 |
| 4 | Gross 250,000 | Net 195,390.48; PIT 33,600; employer cost 280,712.40 | Ex. D — social capped at 176,416; PIT 22,100 + 23% × 50,000 |
| 5 | Gross 40,000 (min wage) | Net 35,520; PIT 0; employer cost 46,680 | Ex. E — floor binds at 40,000 |
| 6 | Gross 30,000 part-time | Net 25,690; PIT 0; employer cost 36,510 | Ex. F — social on 40,000 floor; health on 30,000 |
| 7 | Annual income 2,040,000 | Marginal rate steps 13% → 23% above this | Section 2.1 statutory threshold |
| 8 | Contribution totals | Employee 11.2%; employer 16.7%; combined 27.9% | Section 4.1 — all three additions reconcile |
| 9 | Monthly remittance, gross 120,000 | 11,700 + 13,440 + 20,040 = 45,180 to GDT | Template row 17 |
| 10 | Deadlines | Monthly list by 20th; DIVA by 31 March | Section 12 |

## PROHIBITIONS

- **Non-ALL currency refusal** — NEVER compute Albanian payroll in EUR or any non-ALL currency — refuse and ask for the ALL gross.
- **Outdated monthly table prohibition** — NEVER use the outdated tatime.gov.al English monthly table (30,000 / 150,000 / 15,600) — it reflects the pre-2024 Law 8438/1998 regime; use the PwC 2025 table.
- **Floor/ceiling not applicable to health** — NEVER apply the social-insurance floor/ceiling to the health-insurance components — health (1.7% each) is on full gross with no cap or floor.
- **No health cap** — NEVER apply the 1.7% health cap — there is none.
- **2025 figures not for 2026 without flag** — NEVER apply 2025 figures (floor 40,000 / ceiling 176,416 / min wage 40,000) to a 2026 or later period without flagging the 1 Jan 2026 changes and the unresolved 2026 ceiling.
- **Employer on-cost must be included** — NEVER omit the employer 16.7% on-cost when quoting total employment cost.
- **Penalty amounts uncertain** — NEVER state exact penalty/fine amounts for late declaration or unregistered workers as confirmed — they are research gaps pending primary-source confirmation.
- **Monthly deadline must not be missed** — NEVER miss the monthly payroll-list deadline (20th of the following month) — 10% penalty + interest applies.
- **Computations not definitive** — NEVER present payroll computations as definitive — label them estimated and direct the user to a licensed Albanian accountant.
- **Disclose assumption on method switching** — NEVER silently switch between the gross-basis PIT table and the contributions-first method (Section 2.3) — disclose the assumption.

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a licensed accountant in Albania) before implementation. This is a Tier 2 (research-verified) skill: figures are sourced to named authorities and Big-4 summaries but have not yet been verified section-by-section by a licensed Albanian accountant, and items marked "[RESEARCH GAP — reviewer to confirm]" carry residual uncertainty.

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
