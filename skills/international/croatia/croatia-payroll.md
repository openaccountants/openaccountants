---
name: croatia-payroll
description: Use this skill whenever asked about Croatia payroll processing for employed persons. Trigger on phrases like "Croatia payroll", "Hrvatska plaća", "JOPPD form", "income tax Croatia", "porez na dohodak", "mirovinsko osiguranje", "pension Pillar I Pillar II", "I. stup II. stup", "zdravstveno osiguranje", "health contribution Croatia", "net salary Croatia", "neto plaća", "PAYE Croatia", "tax withholding Croatia", "employer contributions Croatia", "doprinosi", "minimum wage Croatia", "minimalna plaća", "personal allowance Croatia", "osobni odbitak", "gross to net Croatia", "bruto neto", "ePorezna", "Porezna uprava", "predujam poreza na dohodak", or any question about computing employee pay, withholding income tax, or mandatory social contributions for Croatia-based employees. This skill covers PAYE income tax withholding (two-rate local system), employee pension contributions (Pillar I + Pillar II), the employer health insurance contribution, the personal allowance, dependent-child allowances, minimum wage, contribution floors and ceilings, and JOPPD filing obligations. ALWAYS read this skill before processing any Croatia payroll.
version: 0.1
jurisdiction: HR
tax_year: 2025
last_updated: 2026-07-13
review_status: pending_review
depends_on:
  - payroll-workflow-base
category: payroll
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Croatia Payroll

## Croatia Payroll Skill v0.1

Tier 2 — research-verified. Figures below are sourced from the Croatian Tax Administration (Ministarstvo financija — Porezna uprava), the Croatian Pension Insurance Institute (HZMO), the Croatian Health Insurance Fund (HZZO), PwC Worldwide Tax Summaries, KPMG, CMS, TPA, Lano and FINACRO. NOT yet signed off by a licensed Croatian accountant (ovlašteni računovođa) or tax adviser (porezni savjetnik). Treat every computation as an estimate pending professional review.

## Section 1 -- Quick Reference

**Quick Reference table**

| Field | Value |
| --- | --- |
| Country | Croatia (Republic of Croatia / Republika Hrvatska) |
| Currency | EUR only (euro adopted 1 January 2023 — any HRK figure is obsolete) |
| Standard pay frequency | Monthly |
| Tax year | Calendar year (1 January -- 31 December) |
| Tax withholding system | Monthly PAYE (predujam poreza na dohodak) — the employer (payer) withholds income tax and all contributions |
| Income tax authority | Ministry of Finance — Tax Administration (Ministarstvo financija — Porezna uprava) |
| Pension authority | Croatian Pension Insurance Institute (Hrvatski zavod za mirovinsko osiguranje, HZMO) |
| Health authority | Croatian Health Insurance Fund (Hrvatski zavod za zdravstveno osiguranje, HZZO) |
| Key legislation | Personal Income Tax Act (Zakon o porezu na dohodak); Contributions Act (Zakon o doprinosima); Minimum Wage Act (Zakon o minimalnoj plaći); annual minimum-wage decree (NN 132/2025 for 2026) |
| Filing portal | ePorezna (eporezna.porezna-uprava.hr) |
| Surtax (prirez) | ABOLISHED from 1 January 2024 — replaced by wider local income-tax rate ranges (TPA; Crowe) |
| Validated by | Pending -- requires sign-off by a licensed Croatian accountant / tax adviser |
| Skill version | 0.1 |

Read this whole section before computing anything. The shared payroll runbook lives in `payroll-workflow-base` — follow that runbook with this skill supplying the Croatia-specific content.

### The single most important Croatia fact

- **No single national income-tax rate** — Croatia has NO single national income-tax rate. Each local self-government unit (jedinica lokalne samouprave, "JLS" — municipality, town or city) sets its own lower and higher income-tax rates within statutory ranges. The applicable rate depends on the employee's municipality of residence, not the employer's location. If you do not know the employee's municipality, fall back to the national default of 20% lower / 30% higher (the statutory rate applied when a JLS fails to set rates by the deadline).  _(Porezna uprava; PwC)_

## Section 2 -- Income Tax Withholding (porez na dohodak)

The employer (payer) withholds income tax monthly under PAYE (predujam poreza na dohodak). There is a two-rate progressive system. The surtax (prirez) was abolished on 1 January 2024 and folded into wider local rate ranges instead — do not add a separate surtax line. (TPA; Crowe; Invest in Croatia)

### Two-Rate System (2025–2026)

**Two-Rate System (2025–2026)**  _(PwC; Porezna uprava)_

| Band | Monthly tax base | Annual tax base | National default rate | Local range (set by JLS) |
| --- | --- | --- | --- | --- |
| Lower rate | up to EUR 5,000.00 | up to EUR 60,000.00 | 20% | 15% – 23% |
| Higher rate | over EUR 5,000.00 | over EUR 60,000.00 | 30% | 25% – 33% |

- **Higher-rate threshold change** — The higher-rate threshold was raised from EUR 4,200/month (EUR 50,400/yr) in 2024 to EUR 5,000/month (EUR 60,000/yr) effective 2025, and is unchanged for 2026.  _(PwC; CMS; Vialto)_
- **Default rate when JLS unset** — If a JLS does not set its rates by the statutory deadline, the national default rates of 20% (lower) and 30% (higher) apply.  _(Porezna uprava; PwC)_

### Local rate ranges — selecting the JLS rate

Each JLS sets two rates within the 15%–23% (lower) and 25%–33% (higher) statutory bands. The City of Zagreb sits at the top of both bands (commonly cited around 23% lower / 33% higher). The exact figure for a given employer/employee location is set per municipality and changes annually (13 units changed their rates for 2026), so a reviewer must look up the specific location. (PwC) [T2-1 — reviewer to confirm the exact JLS rate for the employee's municipality.]

### Monthly Withholding Method

- **Deterministic withholding order** — 1. Start with gross salary (bruto plaća). 2. Subtract the 20% employee pension contribution (computed on the relieved base — see Section 3). The PwC sample states: gross salary minus 20% employee pension = income. 3. Subtract the monthly personal allowance (osobni odbitak) — basic EUR 600 plus any declared dependent/child allowances. 4. The result is the monthly tax base (porezna osnovica). 5. Apply the JLS lower rate to the portion of the base up to EUR 5,000, and the higher rate to any portion above EUR 5,000. 6. The sum is the withheld income tax for the month. The employer then adds the 16.5% health insurance contribution on top of gross (an employer cost, not a deduction — see Section 4).  _(PwC sample personal income tax calculation)_

### Personal Allowance (osobni odbitak) — 2025–2026

**Personal Allowance table**  _(PwC; CMS; expatincroatia)_

| Allowance | Monthly (EUR) | Annual (EUR) | Note |
| --- | --- | --- | --- |
| Basic personal allowance | 600.00 | 7,200.00 | Raised from EUR 560 (2024) to EUR 600 effective 2025; unchanged for 2026 (PwC; CMS; expatincroatia) |

Source conflict flagged: The official Porezna uprava English page still displays the stale EUR 560 (2024) basic allowance. The EUR 600 (2025–2026) figure comes from PwC and 2025 reform summaries and is treated as current. A reviewer should re-confirm against the live Ordinance. (PwC; CMS)

**Dependent / child allowances table**

| Dependant | Coefficient × EUR 600 | Monthly amount (EUR) | Annual (EUR) |
| --- | --- | --- | --- |
| First child | 0.5 × 600 | 300.00 | 3,600.00 |
| Second child | 0.7 × 600 | 420.00 | 5,040.00 |
| Third child | 1.0 × 600 | 600.00 | 7,200.00 |
| Each further child | coefficient rises progressively by +1.1 over the prior child (4th = 1.4 → 840.00; 5th = 1.9 → 1,140.00; …) | per coefficient | per coefficient |

- **Child allowance calculation basis** — Each child allowance equals its statutory coefficient × the EUR 600 basic personal allowance. The coefficients are 0.5 (first child), 0.7 (second child) and 1.0 (third child); for each further dependent child the coefficient is increased progressively by 1.1 over the coefficient for the previous child. Dependent/child allowances apply only where the employee has filed a tax card (Porezna kartica / PK) declaring them.  _(Porezna uprava — Personal allowance; PwC — Deductions)_

### Returning-emigrant relief

Returning Croatian emigrants who have been abroad for 2+ years may qualify for a 5-year exemption on employment income tax. (TaxRavens; reform summaries) [T2 — eligibility conditions and mechanics not fully resolved in this research; route any claim to a reviewer.]

## Section 3 -- Contributions: Employee Deductions (Pension)

- **Employee pension total** — Employees pay a total of 20% pension contribution, withheld from gross. It splits into two pillars.  _(PwC)_

**Employee pension contributions table**  _(PwC)_

| Contribution | Rate | Payer | Authority | Note |
| --- | --- | --- | --- | --- |
| Pension — Pillar I (Mirovinsko osiguranje, I. stup) | 15% | Employee (withheld) | HZMO | Pay-as-you-go state pension |
| Pension — Pillar II (mandatory funded, II. stup) | 5% | Employee (withheld) | Funded pension fund | Mandatory for those born after 1 January 1962 |
| **Total employee pension** | **20%** | Employee (withheld) | — | 15% + 5% — verify: 15 + 5 = 20 ✓ |

- **Non-Pillar II employees** — For employees not in Pillar II (born on or before 1 Jan 1962), the full 20% goes to Pillar I. [T2-5 — confirm Pillar II status for borderline DOB.]  _(PwC)_

### Low-Income Relief on the Pension Base

The base for the 20% pension contribution is reduced for lower earners. (PwC Other taxes)

**Pension base relief table**  _(PwC Worldwide Tax Summaries — Other taxes)_

| Monthly gross salary | Pension base |
| --- | --- |
| Up to EUR 700.00 | gross − EUR 300.00 |
| EUR 700.01 – 1,300.00 | gross − [0.5 × (1,300.00 − gross)] |
| Above EUR 1,300.00 | full gross (no reduction), subject to the monthly cap |

- **Relief applies to combined base** — The relief applies to the combined Pillar I + Pillar II base.  _(PwC Worldwide Tax Summaries — Other taxes)_

### Pension Contribution Ceilings

**Pension Contribution Ceilings table**  _(PwC; FINACRO)_

| Cap | Amount (EUR) | Basis | Year |
| --- | --- | --- | --- |
| Monthly cap (combined Pillar I + II base) | 11,958.00 | = 6.0 × average gross salary | 2025 and 2026 |
| Annual Pillar I ceiling | 143,496.00 | = EUR 11,958.00 × 12 (verify: 11,958 × 12 = 143,496 ✓) | 2025 and 2026 |

The monthly cap implies an average gross salary of EUR 1,993 (11,958 ÷ 6 = 1,993).

## Section 4 -- Contributions: Employer Contributions (Health)

Croatia is unusual: there is a single employer-borne mandatory contribution — health insurance — paid on top of gross salary. The employer does NOT match the employee pension, pays no maternity-fund levy, and applies no surtax. (PwC; Deloitte)

**Employer contribution table**  _(PwC; Deloitte)_

| Contribution | Rate | Payer | Authority | Ceiling | Note |
| --- | --- | --- | --- | --- | --- |
| Health insurance (Zdravstveno osiguranje) | 16.5% of gross salary | Employer (on top of gross) | HZZO | **NOT capped** | Sole employer-borne contribution; no floor relief |
| **Total employer contribution** | **16.5%** | Employer | — | Not capped | Single line — no other employer contribution |

- **Total employer cost formula** — Total employer cost = gross salary + (16.5% × gross salary) = gross × 1.165.  _(PwC)_

Worked example: for a EUR 2,000 gross monthly salary, the employer pays EUR 2,000 + EUR 330.00 (16.5% × 2,000) = EUR 2,330.00 total employer cost (verify: 2,000 × 1.165 = 2,330 ✓). The EUR 330 is never deducted from the employee — it sits on top.

Source conflict flagged: TaxRavens' social-contributions page gave inconsistent approximations (e.g. ~10% pension / ~3.5% health, ~36.5% combined) that contradict the PwC authoritative split. PwC was relied upon (employee pension 20%, employer health 16.5%, combined wedge 36.5%).

## Section 5 -- Minimum Wage and Contribution Floors

### National Minimum Gross Wage (minimalna plaća)

**National Minimum Gross Wage table**  _(employsome; gpa.net; usemultiplier)_

| Year | Monthly gross (EUR) | Note |
| --- | --- | --- |
| 2025 | 970.00 | Set by Government decree (employsome; gpa.net) |
| 2026 | 1,050.00 | NN 132/2025, effective 1 Jan 2026; ≈ EUR 6.05/hour at a 40-hour week (employsome; usemultiplier) |

### Minimum Monthly Contribution Base

**Minimum Monthly Contribution Base table**  _(FINACRO; TaxRavens)_

| Population | Minimum monthly base (EUR) | Basis | Year |
| --- | --- | --- | --- |
| General | 757.34 | 0.38 × average gross salary (0.38 × 1,993 = 757.34 ✓) | 2026 (FINACRO; TaxRavens) |
| Directors / board members NOT in an employment relationship | 1,295.45 (Gross I) | 0.65 × average gross salary (0.65 × 1,993 = 1,295.45 ✓) | 2026 (FINACRO; TaxRavens) |

Directors/board members not in an employment relationship are subject to the minimum contribution base even if their declared salary is lower; the total employer cost with 16.5% health is approximately EUR 1,509.20 (1,295.45 × 1.165 = 1,509.20 ✓). (FINACRO) [RESEARCH GAP — the general 2025 minimum base and the 2025 directors base were not in this research dataset; reviewer to confirm 2025 figures.]

### Maximum Monthly Contribution Base (pension)

- **Maximum monthly contribution base** — EUR 11,958.00 per month (6.0 × average gross salary), for 2025 and 2026 — see Section 3.  _(PwC; FINACRO)_

### Working Hours and Overtime

[RESEARCH GAP — reviewer to confirm] Statutory overtime multipliers, maximum weekly hours, and night/Sunday/holiday premiums under the Croatian Labour Act (Zakon o radu) were not part of this research dataset. A reviewer should populate this from the Labour Act and any applicable collective agreement (kolektivni ugovor) before relying on overtime figures.

## Section 6 -- Conservative Defaults

**Conservative Defaults table**  _(Porezna uprava; PwC; Lano)_

| Field | Default | Rationale |
| --- | --- | --- |
| Local income-tax rates | **20% lower / 30% higher** (national default) | Statutory fallback when a JLS does not set rates by the deadline; use when the employee's municipality is unknown. (Porezna uprava) |
| Pillar II membership | **Assume a member** (5% Pillar II + 15% Pillar I) | Mandatory for everyone born after 1 January 1962 — essentially the entire active 2025–2026 workforce. (PwC) |
| Personal allowance | **Basic allowance only (EUR 600/month)** | Dependent/child allowances require a tax card (Porezna kartica / PK) on file. Absent that card, withhold using only the basic allowance. |
| Pension base for gross > EUR 1,300 | **Full gross (no relief), capped at EUR 11,958/month** | No low-income relief above EUR 1,300; apply the monthly cap. (PwC) |
| Low-income pension relief | **Apply per the gross-salary tier** | The relief is automatic for low earners — compute it; do not omit it. (PwC) |
| Employer cost estimate | **Gross × 1.165** (add 16.5% health) | Single employer-borne contribution; no other employer levy. (PwC) |
| Remittance timing | **Treat the 15th of the following month** as both the JOPPD filing and payment deadline unless a later date is confirmed | Sources disagree on the exact date (see Section 12). (Lano; Porezna uprava) |

- **Conservative default enforcement rule** — When an input is unknown, the skill MUST apply the conservative default below and flag the assumption in its output rather than guessing a more favourable figure.

## Section 7 -- Required Inputs and Refusal Catalogue

### Required inputs before any computation

- **Required inputs list** — 1. Gross monthly salary (bruto plaća) in EUR. 2. Employee's municipality of residence (JLS) — to select the correct local lower/higher rate. If unknown, default to 20% / 30% and flag it. 3. Date of birth — to determine Pillar II membership (born after 1 Jan 1962) and any age-based relief eligibility. 4. Personal allowance status — whether a tax card (PK) is on file and what dependants/children are declared. 5. Pay period (month and year) — to pick the correct minimum wage, contribution base and threshold figures (2025 vs 2026). 6. Whether the worker is a director/board member not in an employment relationship — triggers the minimum contribution base.

### Refusal Catalogue — DO NOT attempt; route to a licensed accountant

**Refusal catalogue table**

| Scenario | Why it is out of scope |
| --- | --- |
| Posted workers / A1 certificates / cross-border social-security coordination | Requires EU Reg. 883/2004 analysis and HZMO/HZZO determinations — see `cross-border-payroll-coordination`. |
| Non-resident employees, double-tax-treaty relief, expat tax-equalisation | Treaty residency and tie-breaker analysis is beyond a domestic payroll run (KPMG TIES). |
| Returning-emigrant 5-year income-tax exemption | Eligibility conditions unresolved in this research — route to a reviewer. **[T2]** |
| Benefits in kind / company cars / stock options valuation | Croatian BIK valuation rules were not in this research dataset. **[RESEARCH GAP]** |
| Disability, sickness and maternity benefit reimbursement mechanics | Interaction with HZZO benefit refunds not covered here. |
| Severance / termination payment taxation | Not in scope; route to a reviewer. |
| Self-employed / sole-trader (obrt) contributions | Different contribution regime — out of scope for employer payroll. |
| Penalty quantification (exact fine amounts) | Available only in obsolete HRK; not confirmed in EUR from a primary source — see Section 13. |

## Section 8 -- Transaction / Payment Pattern Library

Deterministic classification of Croatian bank-statement lines for payroll. Match on the uppercased description fragment.

### Salary credits (what lands in the employee's account)

**Salary credits table**

| Bank statement text (HR / EN) | Classification |
| --- | --- |
| `PLAĆA`, `NETO PLAĆA`, `ISPLATA PLAĆE` | Net salary payment |
| `PLACA`, `SALARY`, `WAGES` | Net salary payment (ASCII / English variant) |
| `AKONTACIJA PLAĆE`, `PREDUJAM` | Salary advance (not final pay) |
| `NAKNADA`, `REGRES`, `BOŽIĆNICA` | Allowance / holiday or Christmas bonus (check taxability) |
| `DNEVNICA` | Per-diem / travel allowance (may be tax-exempt up to limits) |
| `POVRAT POREZA` | Income tax refund — NOT income |

### Employer debits (what leaves the employer's account)

**Employer debits table**

| Bank statement text (HR / EN) | Classification |
| --- | --- |
| `POREZ NA DOHODAK`, `POREZNA UPRAVA` | Income tax remittance to the Tax Administration |
| `DOPRINOS MIROVINSKO`, `MIO I. STUP`, `MIO II. STUP`, `HZMO` | Employee pension contribution remittance (Pillar I / II) |
| `DOPRINOS ZDRAVSTVENO`, `ZDRAVSTVENO`, `HZZO` | Employer health insurance contribution remittance |
| `ISPLATA PLAĆA`, `PAYROLL`, `OBRAČUN PLAĆE` | Net wages disbursed to employees |
| `JOPPD` | Reference tag for a JOPPD-linked payment batch |

Income tax and contributions are remitted to state accounts (administered by the Tax Administration); health goes to HZZO, pension to HZMO. All are reported together on the JOPPD form (Section 12).

## Section 9 -- Worked Examples

All examples use 2025 figures unless stated. Pension uses the 20% combined rate (Pillar I 15% + Pillar II 5%) and assumes Pillar II membership. Local rates default to 20% / 30% unless a municipality is named. Every line below was recomputed end-to-end.

### Example 1 — Standard Zagreb employee, EUR 2,000 gross/month

Bank statement context: `ISPLATA PLAĆE … 1.400,00 EUR` credited to the employee; `POREZNA UPRAVA … 200,00 EUR` and `HZMO … 400,00 EUR` debited from the employer.

**Example 1 computation table**

| Step | Computation | EUR |
| --- | --- | --- |
| Gross salary | — | 2,000.00 |
| Pension base relief | Gross > 1,300 → no reduction | 0.00 |
| Pension contribution (20% of 2,000) | 15% Pillar I (300) + 5% Pillar II (100) | 400.00 |
| Income after pension | 2,000 − 400 | 1,600.00 |
| Personal allowance (basic) | — | 600.00 |
| Tax base | 1,600 − 600 | 1,000.00 |
| Income tax (20% default lower rate) | 1,000 × 20% | 200.00 |
| **Net pay** | 1,600 − 200 | **1,400.00** |
| Employer health (16.5% of 2,000) | on top of gross | 330.00 |
| **Total employer cost** | 2,000 + 330 | **2,330.00** |

Zagreb may set its lower rate anywhere in 15–23%. At the Zagreb top of band (23%), income tax = 1,000 × 23% = EUR 230.00 and net pay = EUR 1,370.00. If the rate is unknown, apply the national default 20% as shown above.

### Example 2 — Minimum-wage worker (2025), EUR 970 gross/month, national default rates

**Example 2 computation table**

| Step | Computation | EUR |
| --- | --- | --- |
| Gross salary | — | 970.00 |
| Pension base relief | Gross in 700.01–1,300 → 0.5 × (1,300 − 970) = 165 | −165.00 |
| Pension base | 970 − 165 | 805.00 |
| Pension contribution (20% of 805) | — | 161.00 |
| Income after pension | 970 − 161 | 809.00 |
| Personal allowance (basic) | — | 600.00 |
| Tax base | 809 − 600 | 209.00 |
| Income tax (20% default lower rate) | 209 × 20% | 41.80 |
| **Net pay** | 809 − 41.80 | **767.20** |
| Employer health (16.5% of 970) | on top | 160.05 |
| **Total employer cost** | 970 + 160.05 | **1,130.05** |

### Example 3 — Low earner with full relief, EUR 650 gross/month

**Example 3 computation table**

| Step | Computation | EUR |
| --- | --- | --- |
| Gross salary | — | 650.00 |
| Pension base relief | Gross ≤ 700 → reduce by 300 | −300.00 |
| Pension base | 650 − 300 | 350.00 |
| Pension contribution (20% of 350) | — | 70.00 |
| Income after pension | 650 − 70 | 580.00 |
| Personal allowance (basic) | — | 600.00 |
| Tax base | max(580 − 600, 0) | 0.00 |
| Income tax | base is 0 | 0.00 |
| **Net pay** | 580 − 0 | **580.00** |
| Employer health (16.5% of 650) | on top | 107.25 |
| **Total employer cost** | 650 + 107.25 | **757.25** |

Note this gross is below the 2025 statutory minimum wage of EUR 970 for a full-time worker — used here only to illustrate the maximum pension relief and a zero tax base. Do not run a full-time worker below the minimum wage.

### Example 4 — High earner at the higher-rate threshold edge, EUR 7,000 gross/month, national default rates

**Example 4 computation table**

| Step | Computation | EUR |
| --- | --- | --- |
| Gross salary | — | 7,000.00 |
| Pension base relief | Gross > 1,300 → none | 0.00 |
| Pension contribution (20% of 7,000) | base below the EUR 11,958 monthly cap | 1,400.00 |
| Income after pension | 7,000 − 1,400 | 5,600.00 |
| Personal allowance (basic) | — | 600.00 |
| Tax base | 5,600 − 600 | 5,000.00 |
| Income tax — lower band (20% on first 5,000) | 5,000 × 20% | 1,000.00 |
| Income tax — higher band (30% on amount > 5,000) | base = 5,000 exactly → 0 above | 0.00 |
| **Net pay** | 5,600 − 1,000 | **4,600.00** |
| Employer health (16.5% of 7,000) | on top | 1,155.00 |
| **Total employer cost** | 7,000 + 1,155 | **8,155.00** |

The higher (30%) rate bites only once the tax base exceeds EUR 5,000/month — i.e. after pension and allowance are subtracted, not on raw gross. Here the base equals exactly 5,000, so nothing is taxed at the higher rate.

### Example 5 — Above the pension cap, EUR 13,000 gross/month, national default rates

**Example 5 computation table**

| Step | Computation | EUR |
| --- | --- | --- |
| Gross salary | — | 13,000.00 |
| Pension base relief | Gross > 1,300 → none | 0.00 |
| Pension base before cap | 13,000 | 13,000.00 |
| Pension base after cap | min(13,000, 11,958) | 11,958.00 |
| Pension contribution (20% of 11,958) | capped base | 2,391.60 |
| Income after pension | 13,000 − 2,391.60 | 10,608.40 |
| Personal allowance (basic) | — | 600.00 |
| Tax base | 10,608.40 − 600 | 10,008.40 |
| Income tax — lower band (20% on first 5,000) | 5,000 × 20% | 1,000.00 |
| Income tax — higher band (30% on 5,008.40) | (10,008.40 − 5,000) × 30% | 1,502.52 |
| Total income tax | 1,000.00 + 1,502.52 | 2,502.52 |
| **Net pay** | 10,608.40 − 2,502.52 | **8,105.88** |
| Employer health (16.5% of 13,000) | on top — health is NOT capped | 2,145.00 |
| **Total employer cost** | 13,000 + 2,145 | **15,145.00** |

The pension contribution is capped at the EUR 11,958 monthly base (so pension = EUR 2,391.60, not 20% of full gross), but the 16.5% health contribution is uncapped and applies to the full EUR 13,000 gross.

### Example 6 — Employee with two children, EUR 2,500 gross/month, national default rates

**Example 6 computation table**

| Step | Computation | EUR |
| --- | --- | --- |
| Gross salary | — | 2,500.00 |
| Pension base relief | Gross > 1,300 → none | 0.00 |
| Pension contribution (20% of 2,500) | — | 500.00 |
| Income after pension | 2,500 − 500 | 2,000.00 |
| Personal allowance — basic | — | 600.00 |
| Allowance — 1st child (0.5 × 600) | — | 300.00 |
| Allowance — 2nd child (0.7 × 600) | — | 420.00 |
| Total personal allowance | 600 + 300 + 420 | 1,320.00 |
| Tax base | 2,000 − 1,320 | 680.00 |
| Income tax (20% default lower rate) | 680 × 20% | 136.00 |
| **Net pay** | 2,000 − 136 | **1,864.00** |
| Employer health (16.5% of 2,500) | on top | 412.50 |
| **Total employer cost** | 2,500 + 412.50 | **2,912.50** |

Child allowances apply only if declared on a tax card (PK). The schedule uses statutory coefficients (1st child 0.5, 2nd 0.7, 3rd 1.0) × the EUR 600 basic allowance → EUR 300 / 420 / 600. (Porezna uprava; PwC)

## Section 10 -- Tier 1 Rules (deterministic — the skill applies these directly)

- **T1 rules list** — 1. [T1] Income tax 2025–2026 uses a two-rate progressive system: lower rate to a monthly tax base of EUR 5,000 (EUR 60,000/yr), higher rate above. Threshold raised from EUR 4,200/month (EUR 50,400/yr) in 2024. (PwC; CMS) 2. [T1] There is NO single national rate and NO surtax (prirez abolished 1 Jan 2024). Each JLS sets two rates within 15–23% (lower) / 25–33% (higher); the employee's residence municipality decides which rates apply. Default if unset = 20% / 30%. (Porezna uprava; PwC; TPA) 3. [T1] Basic monthly personal allowance = EUR 600 (EUR 7,200/yr), effective 2025, unchanged for 2026. (PwC; CMS) The official Porezna uprava EN page still shows the stale EUR 560 figure. 4. [T1] Child allowances (monthly, on top of basic, only if declared on a tax card) = statutory coefficient × the EUR 600 basic allowance: 1st child 0.5 → EUR 300, 2nd child 0.7 → EUR 420, 3rd child 1.0 → EUR 600; for each further child the coefficient rises by +1.1 over the prior child (4th = 1.4 → EUR 840, etc.). (Porezna uprava — Personal allowance; PwC — Deductions) 5. [T1] Employee pension = 20% of gross on the relieved base: 15% Pillar I (HZMO) + 5% Pillar II for those born after 1 Jan 1962; otherwise the full 20% to Pillar I. (PwC) 6. [T1] Pension base low-income relief: gross ≤ EUR 700 → base = gross − EUR 300; gross EUR 700.01–1,300 → base = gross − [0.5 × (1,300 − gross)]; gross > EUR 1,300 → full gross. (PwC) 7. [T1] Pension monthly cap = EUR 11,958.00 (6.0 × average gross salary), for 2025 and 2026. Annual Pillar I ceiling = EUR 143,496.00. (PwC; FINACRO) 8. [T1] Employer health insurance = 16.5% of gross, paid on top of gross, NOT capped. It is the only employer-borne mandatory contribution. (PwC; Deloitte) 9. [T1] Withholding order: gross → subtract 20% pension (relieved/capped base) → subtract personal allowance → apply local lower rate to base ≤ 5,000 and higher rate above → withheld income tax. Employer adds 16.5% health on top. (PwC sample calc) 10. [T1] Monthly JOPPD filed via ePorezna reports income tax AND all contributions together; there is no separate contributions filing. (Lano; Porezna uprava) 11. [T1] Minimum gross wage: EUR 970/month (2025) → EUR 1,050/month (2026, NN 132/2025). Minimum monthly contribution base 2026: general EUR 757.34; directors/board members not in employment EUR 1,295.45. (employsome; FINACRO) 12. [T1] Croatia uses EUR since 1 January 2023; any HRK figure is obsolete and must be reconverted/re-verified. (Tax reform record)

## Section 11 -- Tier 2 Catalogue (reviewer judgement required)

These items depend on facts or sources not fully resolved in this research. The skill must surface them and recommend professional review rather than asserting a single answer.

**Tier 2 Catalogue table**

| Ref | Issue | What the reviewer must resolve |
| --- | --- | --- |
| **[T2-1]** | Exact JLS rate for the employee's specific municipality | The 15–23% / 25–33% ranges are statutory; the actual figure is set per municipality and changes yearly (13 units changed for 2026). Confirm from the JLS decision or Porezna uprava list. |
| **[T2-2]** | Child-allowance schedule (1st/2nd/3rd+) | Confirmed against the Porezna uprava "Personal allowance" page and PwC: coefficients 0.5 / 0.7 / 1.0 × the EUR 600 basic allowance → EUR 300 / 420 / 600, rising by +1.1 per further child. Reviewer should re-confirm the live Ordinance and whether the announced 2026 child-relief reform alters the schedule. |
| **[T2-3]** | JOPPD filing and remittance timing | Sources disagree — authority guidance points to on/before the payment date; practitioner sources cite the 15th of the following month; some cite end of the following month. Confirm the precise deadline per income type with Porezna uprava. |
| **[T2-4]** | New-employee registration windows and exact form names | HZMO (M-11P / Tiskanica M-1P): earliest 8 days before start, no later than before work begins. HZZO (Form T1): within 8 days of start. Verify against current HZMO/HZZO rules. |
| **[T2-5]** | Pillar II status for borderline DOB (on/before 1 Jan 1962) | Confirm whether the worker is in the funded pillar; if not, 20% goes entirely to Pillar I. |
| **[T2-6]** | Returning-emigrant 5-year exemption | Eligibility conditions and mechanics not resolved here. |
| **[T2-7]** | Benefits in kind, severance, per-diem/travel-allowance tax limits | Not in this research dataset — reviewer to populate. |
| **[T2-8]** | Overtime / night / holiday premiums under the Labour Act | Not researched here — confirm from Zakon o radu and any collective agreement. |
| **[T2-9]** | 2025 minimum contribution bases (general and directors) | Only the 2026 bases (757.34 / 1,295.45) were in this research; confirm 2025 figures. |

## Section 12 -- Filing Obligations

### Monthly — JOPPD

**Monthly JOPPD table**

| Form | Purpose | Deadline |
| --- | --- | --- |
| **JOPPD** (Izvješće o primicima, porezu na dohodak i prirezu te doprinosima za obvezna osiguranja) | Consolidated monthly report of gross pay, withheld income tax, personal allowances, taxable income and all mandatory contributions per employee; filed electronically via ePorezna. There is **no separate contributions report** — JOPPD covers tax and all contributions. | By the 15th day of the month following the month the payment was made or due (filed on/before the payment date). **[T2-3 — sources disagree (payment date vs 15th vs end of following month); confirm with Porezna uprava.]** |
| Payment of income tax + contributions | Remittance of withheld income tax and social contributions to state accounts | Same as JOPPD (treat as the 15th of the following month unless a later date is confirmed). **[T2-3]** |

### Annual

**Annual filings table**

| Form | Purpose | Deadline |
| --- | --- | --- |
| ZPP-DOH | Request for special-procedure refund / recognition of additional allowances (filed by the individual) | End of February for the prior year (Porezna uprava) |
| Annual income tax return (godišnja prijava poreza na dohodak) | Required mainly for self-employment income, seafarers, and where required by the Tax Administration; most employees are settled via the special procedure / automatic assessment | End of February following the tax year (Porezna uprava) |

### Employee registration

**Employee registration table**

| Form | Purpose | Deadline |
| --- | --- | --- |
| M-11P / Tiskanica M-1P (HZMO — pension) | Register/de-register a new employee with HZMO | Earliest 8 days before start, no later than before the actual start of work (HZMO) |
| T1 (HZZO — health) | Register a new employee with HZZO | Within 8 days of start of work (HZZO) |

An OIB (personal identification number) is required for every employee. [T2-4 — verify exact windows and form names.]

## Section 13 -- Penalties

[RESEARCH GAP — reviewer to confirm exact figures] The Contributions Act and General Tax Act (Opći porezni zakon) prescribe specific fine bands plus default interest, but the only amounts available in this research were obsolete pre-euro HRK figures from secondary EOR sources (cited in the range of old HRK 5,000–100,000). Croatia adopted the euro on 1 January 2023, so those HRK figures are obsolete and must be re-verified in current EUR against the in-force legislation before publishing.

**Penalties table**

| Trigger | Consequence (qualitative) |
| --- | --- |
| Late or incorrect JOPPD filing; late payment of tax and contributions | Statutory fines plus default interest on unpaid amounts. **[Exact EUR fine amounts unconfirmed — reviewer to supply.]** |
| Failure to register an employee with HZMO / HZZO | Administrative fines and liability for unpaid contributions plus interest. **[Specific EUR penalties unconfirmed — reviewer to supply.]** |
| Late payment interest | Statutory default interest on overdue tax/contributions (rate set periodically by the Ministry of Finance / Croatian National Bank reference rate). **[Exact 2025 rate not confirmed in this research.]** |
| Record-keeping | Payroll records must be retained at least 5 years. **[RESEARCH GAP — confirm against the General Tax Act.]** |

## Section 14 -- Excel Working Paper Template

A reviewer-ready monthly payroll working paper should contain the following columns (one row per employee per month). Inputs are entered; computed cells follow the Section 2 / Section 3 order exactly.

**Excel Working Paper Template table**

| Col | Heading | Type | Formula / source |
| --- | --- | --- | --- |
| A | Employee name | Input | — |
| B | OIB | Input | 11-digit personal ID |
| C | Date of birth | Input | drives Pillar II eligibility |
| D | Municipality (JLS) | Input | drives local rates |
| E | Gross salary (EUR) | Input | bruto plaća |
| F | Pension base reduction | Computed | `IF(E<=700,300,IF(E<=1300,0.5*(1300-E),0))` |
| G | Pension base (capped) | Computed | `MIN(E - F, 11958)` |
| H | Pension contribution (20%) | Computed | `G * 20%` |
| I | Income after pension | Computed | `E - H` |
| J | Personal allowance | Input | 600 + declared children (0.5/0.7/1.0 × 600 = 300 / 420 / 600…) |
| K | Tax base | Computed | `MAX(I - J, 0)` |
| L | Tax — lower band | Computed | `MIN(K,5000) * lower_rate` (default 20%) |
| M | Tax — higher band | Computed | `MAX(K-5000,0) * higher_rate` (default 30%) |
| N | Income tax withheld | Computed | `L + M` |
| O | Net pay | Computed | `I - N` |
| P | Employer health (16.5%) | Computed | `E * 16.5%` (uncapped) |
| Q | Total employer cost | Computed | `E + P` |

Footer checks: sum of column N ties to the JOPPD income-tax line; sum of H ties to the pension remittance; sum of P ties to the HZZO remittance; sum of O ties to the total net wages disbursed.

## Section 15 -- Croatian Bank Statement & Terminology Reading Guide

**Terminology Reading Guide table**

| Croatian term | English | Relevance |
| --- | --- | --- |
| Bruto plaća | Gross salary | Starting figure for all computations |
| Neto plaća | Net salary | What the employee receives |
| Osobni odbitak | Personal allowance | Subtracted before tax |
| Porezna osnovica | Tax base | Income after pension and allowance |
| Porez na dohodak | Income tax | Withheld monthly |
| Predujam poreza na dohodak | PAYE / advance income tax | The monthly withholding mechanism |
| Prirez | Surtax | ABOLISHED 1 Jan 2024 — do not apply |
| Doprinosi | Contributions | Pension (employee) + health (employer) |
| Mirovinsko osiguranje (I. / II. stup) | Pension insurance (Pillar I / II) | 15% + 5%, employee-borne |
| Zdravstveno osiguranje | Health insurance | 16.5%, employer-borne, on top of gross |
| HZMO | Croatian Pension Insurance Institute | Receives pension contributions |
| HZZO | Croatian Health Insurance Fund | Receives health contribution |
| Porezna uprava | Tax Administration | Receives income tax; runs ePorezna |
| OIB | Personal identification number | Required for every employee |
| JLS (jedinica lokalne samouprave) | Local self-government unit | Sets local income-tax rates |
| Minimalna plaća | Minimum wage | EUR 970 (2025) / EUR 1,050 (2026) |
| Porezna kartica (PK) | Tax card | Declares allowances/dependants |
| JOPPD | Consolidated monthly payroll report | Tax + all contributions in one filing |
| ePorezna | e-Tax portal | Electronic filing of JOPPD |

## Section 16 -- Onboarding Fallback

When key facts are missing, ask the user these questions before computing. If a question is unanswered, apply the Section 6 conservative default and clearly flag the assumption.

1. What is the employee's **gross monthly salary** in EUR?
2. In which **municipality (JLS)** does the employee reside? (If unknown → default 20% / 30%.)
3. What is the employee's **date of birth**? (Determines Pillar II membership.)
4. Is a **tax card (Porezna kartica)** on file, and what **dependants/children** are declared? (If none → basic EUR 600 allowance only.)
5. Which **month and year** is this pay run for? (Determines minimum wage, contribution base and threshold figures — 2025 vs 2026.)
6. Is the worker a **director or board member not in an employment relationship**? (Triggers the minimum contribution base.)

## Section 17 -- Interaction with Other Skills

**Interaction with Other Skills**

| Scenario | Skill to use |
| --- | --- |
| Employee payroll (income tax + pension + health) | **This skill (croatia-payroll.md)** |
| Croatia personal income tax (annual / self-employment) | croatia-income-tax.md |
| Croatia social contributions (detailed contribution mechanics) | croatia-social-contributions.md |
| Cross-border / posted workers / A1 coordination | cross-border-payroll-coordination.md |
| Croatia VAT (PDV) returns | croatia-vat-return.md |
| Shared workflow runbook | payroll-workflow-base.md |

### Key handoff points

- **Payroll → Bookkeeping:** Gross wages and the 16.5% employer health contribution are expenses; withheld income tax and the 20% employee pension are liabilities until remitted via JOPPD.
- **Payroll → Income tax:** Most employees are reconciled automatically by the Tax Administration's special-procedure assessment; only some file an annual return (mainly self-employment income and seafarers).
- **Payroll → Pension:** Pillar I + II contributions paid through payroll build the employee's pension entitlement (state + funded).

## Section 18 -- Reference Material

**Reference Material**

| # | Source | Publisher | URL |
| --- | --- | --- | --- |
| 1 | Croatia — Individual — Other taxes (social security contributions, caps, base relief) | PwC Worldwide Tax Summaries | https://taxsummaries.pwc.com/croatia/individual/other-taxes |
| 2 | Croatia — Individual — Taxes on personal income (brackets, rates) | PwC Worldwide Tax Summaries | https://taxsummaries.pwc.com/croatia/individual/taxes-on-personal-income |
| 3 | Croatia — Individual — Sample personal income tax calculation | PwC Worldwide Tax Summaries | https://taxsummaries.pwc.com/croatia/individual/sample-personal-income-tax-calculation |
| 4 | Income tax — general rules, rates, taxpayer and annual return | Porezna uprava (Croatian Tax Administration) | https://porezna-uprava.gov.hr/en/income-t-ax-information-on-the-general-rules-rates-taxpayer-and-submitting-annual-income-tax-return/7322 |
| 5 | Application for Insurance and End of Insurance (HZMO registration deadlines) | HZMO | https://www.mirovinsko.hr/en/application-for-insurance-and-end-of-insurance/234 |
| 6 | Key Changes in Salaries and Income Tax as of January 1, 2026 | FINACRO | https://finacro.hr/en/dobro-je-znati/key-changes-in-salaries-and-income-tax-as-of-january-1-2026/ |
| 7 | Tax Law Changes in 2025 (higher-rate threshold, allowance) | CMS Law-Now | https://cms-lawnow.com/en/ealerts/2025/01/tax-law-changes-in-2025 |
| 8 | New round of tax reform – Year 2024 (abolition of prirez/surtax) | TPA Croatia | https://www.tpa-group.hr/news/new-round-of-tax-reform-year-2024 |
| 9 | Croatia minimum wage 2026 EUR 1,050 (NN 132/2025) | Employsome | https://employsome.com/hire/croatia/minimum-wage-croatia/ |
| 10 | Running Payroll in Croatia (JOPPD deadline, monthly remittance) | Lano | https://www.lano.io/global-payroll-guide/croatia |
| 11 | Taxation of international executives: Croatia (KPMG TIES) | KPMG | https://assets.kpmg.com/content/dam/kpmgsites/xx/pdf/2023/01/TIES-Croatia.pdf.coredownload.inline.pdf |
| 12 | Personal allowance — basic allowance and dependent-child coefficients (0.5 / 0.7 / 1.0, +1.1 per further child) | Porezna uprava (Croatian Tax Administration) | https://porezna-uprava.gov.hr/en/personal-allowance/7358 |
| 13 | Croatia — Individual — Deductions (personal allowance and dependent-child amounts: EUR 300 / 420 / 600) | PwC Worldwide Tax Summaries | https://taxsummaries.pwc.com/croatia/individual/deductions |

Primary authorities: Porezna uprava (https://porezna-uprava.gov.hr); HZMO (https://www.mirovinsko.hr); HZZO (https://www.hzzo.hr); filing portal ePorezna (https://eporezna.porezna-uprava.hr).

### Test Suite

Run these to validate any implementation of this skill. Expected results use 2025 figures, Pillar II membership, and the national default rates (20% / 30%) unless a municipality is named.

1. **Standard mid earner.** EUR 2,000 gross, no dependants, default 20% rate. Expect: pension EUR 400.00, tax base EUR 1,000.00, income tax EUR 200.00, net EUR 1,400.00, employer health EUR 330.00, total employer cost EUR 2,330.00.
2. **Zagreb top-of-band check.** EUR 2,000 gross, Zagreb lower rate 23%. Expect: income tax EUR 230.00, net EUR 1,370.00 (contributions and employer cost unchanged).
3. **Minimum-wage worker (2025).** EUR 970 gross, default rates. Expect: pension relief EUR 165.00, pension EUR 161.00, tax base EUR 209.00, income tax EUR 41.80, net EUR 767.20, employer cost EUR 1,130.05.
4. **Maximum pension relief / zero tax.** EUR 650 gross. Expect: relief EUR 300.00, pension EUR 70.00, tax base EUR 0.00, income tax EUR 0.00, net EUR 580.00, employer cost EUR 757.25.
5. **Higher-rate threshold edge.** EUR 7,000 gross, default rates. Expect: pension EUR 1,400.00, tax base exactly EUR 5,000.00, all taxed at the lower rate (EUR 1,000.00), nothing at the higher rate, net EUR 4,600.00, employer cost EUR 8,155.00.
6. **Pension cap + uncapped health.** EUR 13,000 gross, default rates. Expect: pension base capped at EUR 11,958.00, pension EUR 2,391.60, tax base EUR 10,008.40, income tax EUR 2,502.52, net EUR 8,105.88, employer health EUR 2,145.00 (on full gross), employer cost EUR 15,145.00.
7. **Two-child allowance.** EUR 2,500 gross, 2 children declared on a tax card, default rates. Expect: total allowance EUR 1,320.00 (600 + 0.5×600 + 0.7×600 = 600 + 300 + 420), tax base EUR 680.00, income tax EUR 136.00, net EUR 1,864.00, employer cost EUR 2,912.50.
8. **Surtax check.** Any salary — confirm the implementation applies NO surtax (prirez) line; prirez was abolished 1 Jan 2024.
9. **Pillar split.** Employee born on or before 1 Jan 1962 — confirm the full 20% is reported to Pillar I (HZMO) with EUR 0 to Pillar II.
10. **Employer-cost-only check.** Confirm the 16.5% health contribution is added on top of gross, is NEVER deducted from the employee's net pay, and is NOT capped.
11. **Filing check.** Confirm income tax AND all contributions are reported together on a single JOPPD via ePorezna with no separate contributions return.
12. **Default-rate fallback.** Municipality unknown — confirm the skill applies 20% / 30% and flags the assumption rather than guessing a specific JLS rate.

## PROHIBITIONS

- **No surtax (prirez)** — NEVER apply a surtax (prirez) — it was abolished on 1 January 2024.  _(abolition of prirez/surtax — TPA Croatia)_
- **No single national income tax rate** — NEVER use a single "national income tax rate" — the rate is set by the employee's municipality of residence; fall back to 20% / 30% only as a flagged default.
- **Health contribution not deducted from net pay** — NEVER deduct the 16.5% health contribution from the employee's net pay — it is an employer cost paid on top of gross.
- **Higher rate applies only above EUR 5,000 tax base** — NEVER apply the higher (25–33%) rate to raw gross — it applies only to the portion of the tax base (after pension and allowance) above EUR 5,000/month.
- **Low-income pension relief mandatory** — NEVER omit the low-income pension relief for employees earning EUR 1,300/month or less.
- **No assumed dependent allowances without tax card** — NEVER assume dependent/child allowances without a tax card (Porezna kartica) on file — default to the basic EUR 600 allowance.
- **Pension base cap and health uncapped** — NEVER exceed the EUR 11,958/month pension base cap or the EUR 143,496/yr Pillar I annual ceiling; but NEVER cap the 16.5% health contribution.
- **Single JOPPD filing** — NEVER file contributions separately from income tax — both go on the single monthly JOPPD via ePorezna.
- **Minimum wage floor** — NEVER run a full-time employee below the statutory minimum wage (EUR 970 in 2025, EUR 1,050 in 2026).  _(Croatia minimum wage 2026 EUR 1,050 (NN 132/2025) — Employsome)_
- **No specific penalty amounts** — NEVER quote a specific penalty amount — those figures are an unconfirmed RESEARCH GAP (obsolete HRK only) pending reviewer confirmation in EUR.
- **No HRK figures** — NEVER quote a figure in HRK — Croatia uses EUR since 1 January 2023.
- **Computations are estimates only** — NEVER present payroll computations as definitive — always label them as estimated and direct the user to a licensed Croatian accountant.

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a licensed accountant or tax adviser in Croatia) before implementation.

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
