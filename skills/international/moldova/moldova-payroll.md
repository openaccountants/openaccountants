---
name: moldova-payroll
description: Use this skill whenever asked about Moldova (Republic of Moldova) payroll processing for employed persons. Trigger on phrases like "Moldova payroll", "Moldova PAYE", "impozit pe venit", "income tax withholding Moldova", "CNAS", "BASS", "social insurance Moldova", "CNAM", "FAOAM", "health insurance Moldova", "Form IPC21", "darea de seama IPC21", "scutire personala", "personal exemption Moldova", "net salary Moldova", "salariu net", "gross to net Moldova", "minimum wage Moldova", "salariul minim", "employer social contribution Moldova", "SFS Moldova", "Serviciul Fiscal de Stat", "MDL payroll", or any question about computing employee pay, withholding income tax, or social/health contributions for Moldova-based employees. This skill covers flat 12% income-tax withholding, employee social insurance (CNAS 6%), mandatory health insurance (CNAM 9%), the 24% employer social contribution, personal/dependent exemptions, minimum wage, the unified monthly IPC21 return, and filing obligations. ALWAYS read this skill before processing any Moldova payroll.
version: 0.1
jurisdiction: MD
tax_year: 2025
last_updated: 2026-07-13
review_status: pending_review
depends_on:
  - payroll-workflow-base
category: payroll
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Moldova Payroll

## Moldova Payroll Skill v0.1

Tier 2 (research-verified). Figures below are drawn primarily from PwC Worldwide Tax Summaries (reviewed Jan 2026), EY Moldova tax alerts, and Moldovan accounting portals (buhgalter.md, salarii.md) because the State Tax Service (sfs.md), CNAS (cnas.gov.md) and CNAM (cnam.md) authority rate pages were not directly retrievable at research time (homepages did not expose the schedule; some authority pages returned HTTP 403). A Moldova-licensed accountant must confirm against the current annual Social Insurance Budget Law, the Health Insurance Fund Law and the Tax Code before sign-off.

## Section 1 -- Quick Reference

**Quick Reference**

| Field | Value |
| --- | --- |
| Country | Moldova (Republic of Moldova) |
| Currency | MDL (Moldovan leu) only |
| Standard pay frequency | Monthly |
| Tax year | Calendar year (1 January -- 31 December) |
| Tax withholding system | PAYE-style monthly withholding at source by the employer (Tax Code, Law No. 1163/1997, Title II) |
| Income tax | FLAT 12% (Tax Code art. 15) |
| Tax authority | State Tax Service -- Serviciul Fiscal de Stat (SFS), sfs.md |
| Social insurance authority | National Social Insurance House -- Casa Națională de Asigurări Sociale (CNAS / BASS), cnas.gov.md |
| Health insurance authority | National Health Insurance Company -- Compania Națională de Asigurări în Medicină (CNAM / FAOAM), cnam.md |
| Key legislation | Tax Code (Codul Fiscal, Law No. 1163/1997) — flat 12% under art. 15; Law No. 489/1999 on the public social insurance system + annual Social Insurance Budget Law (CNAS rates); Law No. 1593/2002 on mandatory health insurance premiums + annual Health Insurance Fund Law (CNAM 9%); Law No. 1432/2000 + Government Decision (guaranteed minimum monthly wage) |
| Filing portal | SFS electronic services (Form IPC21 filed electronically) |
| Validated by | Pending -- requires sign-off by a Moldova-licensed accountant |
| Skill version | 0.1 |

## Section 2 -- Income Tax Withholding (flat 12%)

Moldova levies a flat 12% personal income tax (impozit pe venit) on employment and most other resident income under Tax Code art. 15. There are no progressive brackets and no marital-status scales — the same 12% applies to every individual. Non-residents are taxed at 12% on Moldovan-source income (PwC Worldwide Tax Summaries, reviewed Jan 2026).

The employer withholds income tax monthly at source (PAYE-style) together with the employee social-insurance and health-insurance contributions, and remits all three on the unified monthly Form IPC21.

### Income Tax Rate -- 2025 (unchanged into 2026)

**Income Tax Rate -- 2025 (unchanged into 2026)**  _(Tax Code art. 15; PwC, reviewed Jan 2026)_

| Income | Rate | Source |
| --- | --- | --- |
| Monthly/annual taxable employment income (after CNAM and exemptions) | 12% (flat) | Tax Code art. 15; PwC, reviewed Jan 2026 |

### Special non-payroll rates (documented for completeness — NOT applied in standard payroll)

**Special non-payroll rates**  _(PwC (taxes on personal income))_

| Income type | Rate | Source |
| --- | --- | --- |
| Dividends | 6% | PwC (taxes on personal income) |
| Certain farming/agricultural distributions | 7% | PwC (taxes on personal income) |
| Gambling / lottery winnings | 18% | PwC (taxes on personal income) |

These are not part of standard salary withholding and are listed only so the agent does not misclassify a dividend or winnings line as employment income.

### PIT Computation Method (the calculation ORDER matters)

- **PIT computation order** — 1. Gross salary = contractual gross (including meal tickets and other remunerations). 2. Employee CNAM = 9% × gross. CNAM is deductible before the income-tax base is computed. 3. Monthly exemptions = personal exemption + any dependent/spouse exemptions (see Section 6). 4. PIT base = gross − CNAM 9% − monthly exemptions. 5. PIT = 12% × PIT base. 6. Employee CNAS = 6% × gross (NOT deducted from the PIT base — it is computed on gross in parallel; PwC).  _(buhgalter.md worked example)_

Important: only CNAM (9%) and the exemptions reduce the PIT base. Employee CNAS (6%) does NOT reduce the PIT base in this model — it is withheld on gross in parallel. This follows the buhgalter.md worked example and the PwC deduction guidance. [RESEARCH GAP — reviewer to confirm] the precise statutory deduction set against the current Tax Code annex, since some calculators net both contributions before PIT.

## Section 3 -- Social & Health Contributions -- Employee Deductions

Each month the employer withholds three amounts from the employee's gross salary: social insurance (CNAS), mandatory health insurance (CNAM), and income tax (PIT).

### Employee Deductions (2025)

**Employee Deductions (2025)**  _(PwC (other taxes); buhgalter.md)_

| Deduction | Rate | Base | Ceiling | Source |
| --- | --- | --- | --- | --- |
| Social insurance contribution (CNAS / BASS) | 6% | Gross salary + other remunerations | No ceiling on the percentage rate | PwC (other taxes) |
| Mandatory health insurance (CNAM / FAOAM) | 9% | Gross salary + other remunerations | No ceiling | PwC (other taxes) |
| Personal income tax (PIT) | 12% | Gross − CNAM 9% − exemptions | n/a (flat) | Tax Code art. 15; PwC |
| **Total employee deductions (before exemptions, no PIT exemption)** | **27% of gross (6% + 9% + 12%)** | -- | -- | buhgalter.md |

Arithmetic check (employee column): 6% (CNAS) + 9% (CNAM) + 12% (PIT, before exemptions) = 27% of gross. With exemptions the effective PIT is lower, so the realised total deduction is below 27% — see worked examples. CNAM (9%) is fully borne by the employee; there is no separate employer health premium (PwC).

Source conflict: several EOR/secondary sites show CNAM as a 4.5% employer + 4.5% employee split. The authoritative PwC position and the Tax Code treatment used here is 9% employee-only, no employer health premium. salarii.md additionally mislabels the 9% as "CNAS" when it is CNAM. [RESEARCH GAP — reviewer to confirm] against the current annual Health Insurance Fund Law before relying on this for a specific employer's setup.

## Section 4 -- Social Contributions -- Employer Contributions

The employer pays a social insurance contribution (CNAS / BASS) on top of gross salary. For the standard private sector this is 24%. There is no separate employer-paid health-insurance percentage on payroll — the full 9% CNAM is the employee's withheld premium (PwC).

### Employer Contribution Rates (2025)

**Employer Contribution Rates (2025)**  _(PwC (other taxes))_

| Employment category | Employer CNAS rate | Base | Notes | Source |
| --- | --- | --- | --- | --- |
| Standard private sector | 24% | Gross salary + meal tickets + other remunerations | Default | PwC (other taxes) |
| Special / hazardous working conditions | 32% | Same base | Higher rate for jobs in special working conditions | PwC (other taxes) |
| Agriculture sector | 24% total = **18% employer + 6% state budget** | Same base | Employer pays only 18%; the state budget funds the remaining 6% | PwC (other taxes) |
| Higher education / certain medical institutions | 24% | Same base | Same as standard | PwC (other taxes) |
| Employer health-insurance premium | **0% (none)** | -- | No separate employer CNAM; the 9% is employee-only | PwC (other taxes) |

Arithmetic check (agriculture row): 18% (employer) + 6% (state budget) = 24% total — matches the standard total but the employer outlay is only 18% of gross.

### Combined Employer + Employee Snapshot (standard private sector, before exemptions)

**Combined Employer + Employee Snapshot (standard private sector, before exemptions)**

| Party | Components | Rate of gross |
| --- | --- | --- |
| Employee | CNAS 6% + CNAM 9% + PIT 12% (before exemptions) | 27% |
| Employer | CNAS 24% | 24% |
| Employer health premium | none | 0% |

There is no general wage ceiling on the percentage CNAS/CNAM rates for employees. Fixed-sum amounts (CNAM fixed annual MDL 12,636 for 2025/2026; CNAS fixed annual example MDL 22,878 for 2026) apply only to non-employee categories (self-employed) and are NOT processed through this employer-payroll skill (PwC). [RESEARCH GAP — reviewer to confirm] the exact fixed-sum figures for the relevant year if a self-employed person is in scope.

## Section 5 -- Minimum Wage and Reference Wages

### Guaranteed Minimum Monthly Wage (whole economy)

**Guaranteed Minimum Monthly Wage (whole economy)**  _(WageIndicator.org (Jan 2025); Government of Moldova (gov.md, Dec 2025))_

| Period | Minimum monthly wage (MDL) | Notes | Source |
| --- | --- | --- | --- |
| 2025 (from 1 Jan 2025) | 5,500 | Up from MDL 5,000; ~MDL 32.54/hour at 169 h/month | WageIndicator.org (Jan 2025) |
| 2026 (from 1 Jan 2026) | 6,300 | Increase confirmed | Government of Moldova (gov.md, Dec 2025) |

### Reference / Average Wage

**Reference / Average Wage**  _(salarii.md (2025 changes))_

| Item | Value (MDL) | Source |
| --- | --- | --- |
| Projected average monthly wage 2025 (reference base) | 16,100 | salarii.md (2025 changes) |

Minimum wage is full-time gross. [RESEARCH GAP — reviewer to confirm] sector-specific or real-economy minimum wages and any 2025/2026 hourly conversions if hourly pay is in scope.

## Section 6 -- Personal and Dependent Exemptions

Exemptions reduce the income-tax (PIT) base only. They do NOT reduce the CNAS or CNAM contribution base. Apply an exemption only when the employee has declared and documented eligibility. Annual figures are converted to monthly by dividing by 12.

**Personal and Dependent Exemptions table**  _(PwC (deductions); buhgalter.md; salarii.md)_

| Exemption | Annual (MDL) | Monthly (MDL) | Condition | Source |
| --- | --- | --- | --- | --- |
| Standard personal exemption (scutire personală) | 29,700 | 2,475 | Resident individuals with annual taxable income ≤ MDL 360,000 | PwC (deductions); buhgalter.md; salarii.md |
| Major / increased personal exemption (scutire personală majorată) | 34,620 | 2,885 | Privileged categories (certain disabilities, war-injury, rehabilitated repression victims) | PwC (deductions) |
| Per dependent (scutire pentru persoane întreținute) | 9,900 | 825 | Per qualifying dependent | PwC (deductions); buhgalter.md |
| Increased dependent (severe childhood disability) | 21,780 | 1,815 | Per qualifying dependent with severe childhood disability | PwC (deductions) |
| Spouse (major) exemption | 21,780 | 1,815 | Transferable spouse exemption where the spouse does not use their own; available only against the major exemption category | PwC (deductions) |
| Income cap for the STANDARD personal exemption | 360,000/yr | -- | Standard personal exemption lost where annual taxable income exceeds this | PwC (deductions) |

Arithmetic check (monthly conversions): 29,700/12 = 2,475.00; 34,620/12 = 2,885.00; 9,900/12 = 825.00; 21,780/12 = 1,815.00. All exact.

[RESEARCH GAP — reviewer to confirm] the exact-year (2025) figures against the Tax Policy annex: the dependent/spouse amounts (MDL 9,900 / 21,780) and major exemption (MDL 34,620) match across the PwC table (now labelled 2026) and the salarii.md 2025 table, but precise-year confirmation is advisable.

## Section 7 -- Conservative Defaults

- **Conservative defaults** — 1. Employer CNAS rate. Default to 24% (standard private sector). Use 32% only if the role is confirmed to be in special/hazardous working conditions; use 18% employer + 6% state only if the employer is confirmed agriculture-sector (PwC). 2. Health insurance split. Treat CNAM as 9% employee-only, with no employer health premium. Ignore secondary EOR sites showing a 4.5%/4.5% split (PwC). 3. Calculation order. Deduct 9% CNAM and the applicable exemptions from gross before applying 12% PIT; apply 6% CNAS to gross in parallel (not deducted from the PIT base). Confirmed by the buhgalter.md worked example. 4. No exemption unless declared. Apply only the standard personal exemption (MDL 2,475/month) by default, and only if the employee is a resident below the MDL 360,000 income cap. Do NOT apply major, dependent, or spouse exemptions without documentation. 5. Income cap. If annual taxable income exceeds MDL 360,000, drop the standard personal exemption (PwC). 6. Monthly IPC21 filing. Assume the employer files Form IPC21 and remits PIT + CNAS + CNAM by the 25th of the month following the payroll month (Rivermate; PwC). 7. Currency. All amounts in MDL; never convert to EUR/USD on the working paper.  _(PwC; buhgalter.md; Rivermate)_

## Section 8 -- Required Inputs + Refusal Catalogue

### Required Inputs (refuse to finalise a payroll run without these)

**Required Inputs table**

| Input | Why needed |
| --- | --- |
| Pay period and pay date (and calendar year) | Confirms which year's minimum wage / exemption figures apply |
| Gross salary for the period (incl. meal tickets and other remunerations) | Base for PIT, CNAS, CNAM |
| Residency status (resident / non-resident) | Determines exemption eligibility (exemptions are for residents) |
| Annual taxable income estimate | Determines whether the standard personal exemption is lost (> MDL 360,000) |
| Exemption declaration (personal / major / dependents / spouse) | Determines the correct PIT base |
| Employer category (standard / special-conditions / agriculture) | Determines employer CNAS rate (24% / 32% / 18%) |
| Employee personal tax code (IDNP) + CNAS/CNAM enrolment | Required to report on IPC21 |
| Year-to-date gross + PIT + CNAS + CNAM already withheld | For cumulative reconciliation |

### Refusal Catalogue (stop and ask, do not guess)

- **Refusal Catalogue** — No exemption declaration → default to the standard personal exemption ONLY if residency and the income cap are confirmed; otherwise refuse and ask. Residency unknown → refuse to apply any exemption; flag (non-residents are taxed at 12% on Moldovan-source income with exemption rules differing). Employer category unknown → default to 24% employer CNAS but flag explicitly; do not silently apply 32% or 18%. No employee personal tax code (IDNP) → refuse to file IPC21. Annual income near or above MDL 360,000 → flag; the standard personal exemption may be lost. Self-employed / fixed-sum category → out of scope for this employer-payroll skill; redirect to a Moldova self-employed contribution skill. CNAM split claimed at 4.5%/4.5% → refuse to use; default to 9% employee-only per PwC and flag the conflict.

## Section 9 -- Transaction / Payment Pattern Library

Deterministic classification of Moldova bank-statement lines. Romanian and English descriptors both appear.

### Salary Credits (employee side)

**Salary Credits (employee side)**

| Pattern (statement text) | Classification |
| --- | --- |
| SALARIU, SALARY, PLATA SALARIU | Net salary payment |
| AVANS, AVANS SALARIU | Salary advance (part of net salary) |
| PREMIU, BONUS, PREMIE | Bonus / premium (taxable employment income) |
| TICHETE DE MASA, MEAL TICKETS | Meal tickets (part of remuneration base for CNAS/CNAM) |
| RESTITUIRE CNAS / CNAM | Contribution refund/adjustment — not income |

### Employer Debits (employer side)

**Employer Debits (employer side)**

| Pattern (statement text) | Classification |
| --- | --- |
| IMPOZIT PE VENIT, PIT, SFS IPC21 | Income-tax (PIT) remittance to SFS |
| CNAS, BASS, ASIG SOCIALE | Social insurance remittance (employee 6% + employer 24%) |
| CNAM, FAOAM, ASIG MEDICALA | Mandatory health-insurance remittance (employee 9%) |
| IPC21, DARE DE SEAMA IPC21 | Unified monthly payroll return payment (PIT + CNAS + CNAM) |
| SALARII, STATE DE PLATA, PAYROLL | Salary disbursement batch to employees |

In Moldova the income tax, CNAS and CNAM are all reported on the single monthly IPC21 return and paid by the 25th of the following month. A statement may show one bundled payment or separate lines to SFS/CNAS/CNAM — confirm the split against the employer's payment records.

## Section 10 -- Worked Examples

All examples use 2025 rates (flat 12% PIT, employee CNAS 6%, employee CNAM 9%, employer CNAS 24% standard) and 2025 exemptions. Figures recomputed end-to-end; rounding to the cent (MDL).

### Example 1 -- Standard employee at the reference average wage, MDL 16,100/month (single, personal exemption only)

**Example 1 table**

| Step | Amount (MDL) |
| --- | --- |
| Gross monthly salary | 16,100.00 |
| Employee CNAS 6% (on gross) | 966.00 |
| Employee CNAM 9% (on gross, deductible before PIT) | 1,449.00 |
| Personal exemption (monthly) | 2,475.00 |
| PIT base = 16,100 − 1,449 − 2,475 | 12,176.00 |
| PIT 12% = 12,176 × 12% | 1,461.12 |
| **Net pay** = 16,100 − 966 − 1,449 − 1,461.12 | **12,223.88** |

Employer cost: CNAS 24% = 16,100 × 24% = 3,864.00; total employer outlay = 16,100 + 3,864 = 19,964.00/month. No employer health premium.

### Example 2 -- Minimum-wage employee, MDL 5,500/month (2025, single, personal exemption)

**Example 2 table**

| Step | Amount (MDL) |
| --- | --- |
| Gross monthly salary | 5,500.00 |
| Employee CNAS 6% | 330.00 |
| Employee CNAM 9% | 495.00 |
| Personal exemption (monthly) | 2,475.00 |
| PIT base = 5,500 − 495 − 2,475 | 2,530.00 |
| PIT 12% = 2,530 × 12% | 303.60 |
| **Net pay** = 5,500 − 330 − 495 − 303.60 | **4,371.40** |

Employer cost: CNAS 24% = 5,500 × 24% = 1,320.00; total employer outlay = 6,820.00/month.

### Example 3 -- Employee with two dependents, MDL 20,000/month (single, personal + 2 dependents)

**Example 3 table**

| Step | Amount (MDL) |
| --- | --- |
| Gross monthly salary | 20,000.00 |
| Employee CNAS 6% | 1,200.00 |
| Employee CNAM 9% | 1,800.00 |
| Personal exemption (monthly) | 2,475.00 |
| Dependent exemption: 2 × 825.00 (MDL 9,900/yr each ÷ 12) | 1,650.00 |
| PIT base = 20,000 − 1,800 − 2,475 − 1,650 | 14,075.00 |
| PIT 12% = 14,075 × 12% | 1,689.00 |
| **Net pay** = 20,000 − 1,200 − 1,800 − 1,689 | **15,311.00** |

Employer cost: CNAS 24% = 4,800.00; total employer outlay = 24,800.00/month.

### Example 4 -- Special-conditions employee (employer CNAS 32%), MDL 18,000/month (single, personal exemption)

**Example 4 table**

| Step | Amount (MDL) |
| --- | --- |
| Gross monthly salary | 18,000.00 |
| Employee CNAS 6% (employee rate unchanged) | 1,080.00 |
| Employee CNAM 9% | 1,620.00 |
| Personal exemption (monthly) | 2,475.00 |
| PIT base = 18,000 − 1,620 − 2,475 | 13,905.00 |
| PIT 12% = 13,905 × 12% | 1,668.60 |
| **Net pay** = 18,000 − 1,080 − 1,620 − 1,668.60 | **13,631.40** |

Employer cost: CNAS 32% = 18,000 × 32% = 5,760.00; total employer outlay = 23,760.00/month. The 32% rate affects ONLY the employer side — employee deductions are identical to the standard case.

### Example 5 -- Agriculture-sector employee (employer 18% + state 6%), MDL 10,000/month (single, personal exemption)

**Example 5 table**

| Step | Amount (MDL) |
| --- | --- |
| Gross monthly salary | 10,000.00 |
| Employee CNAS 6% | 600.00 |
| Employee CNAM 9% | 900.00 |
| Personal exemption (monthly) | 2,475.00 |
| PIT base = 10,000 − 900 − 2,475 | 6,625.00 |
| PIT 12% = 6,625 × 12% | 795.00 |
| **Net pay** = 10,000 − 600 − 900 − 795 | **7,705.00** |

Employer cost: CNAS 18% (employer portion) = 10,000 × 18% = 1,800.00; the remaining 6% (= 600.00) is funded by the state budget, not the employer. Employer outlay = 10,000 + 1,800 = 11,800.00/month; total social contribution into the system = 1,800 + 600 = 2,400.00 (= 24% of gross).

### Example 6 -- High earner above the personal-exemption income cap, MDL 35,000/month (annual MDL 420,000 > MDL 360,000)

**Example 6 table**

| Step | Amount (MDL) |
| --- | --- |
| Gross monthly salary | 35,000.00 |
| Employee CNAS 6% | 2,100.00 |
| Employee CNAM 9% | 3,150.00 |
| Personal exemption (annual income > MDL 360,000 → exemption LOST) | 0.00 |
| PIT base = 35,000 − 3,150 − 0 | 31,850.00 |
| PIT 12% = 31,850 × 12% | 3,822.00 |
| **Net pay** = 35,000 − 2,100 − 3,150 − 3,822 | **25,928.00** |

Employer cost: CNAS 24% = 8,400.00; total employer outlay = 43,400.00/month. Annual gross = 35,000 × 12 = 420,000 > 360,000, so the standard personal exemption is unavailable (PwC).

## Section 11 -- Tier 1 Rules (deterministic — apply directly)

- **Tier 1 rules 1-14** — 1. Personal income tax is a flat 12% (Tax Code art. 15) on employment and most other resident income; non-residents 12% on Moldovan-source income (PwC). 2. Employee withholdings from gross each month: CNAS 6% + CNAM 9% + PIT 12% (PIT after CNAM and exemptions) (PwC; buhgalter.md). 3. PIT base = gross − 9% CNAM − applicable monthly exemptions; apply 12% to that base (buhgalter.md worked example). 4. Employee CNAS 6% is computed on gross and does NOT reduce the PIT base in this model (buhgalter.md). 5. Employer pays 24% CNAS on top of gross for the standard private sector; base = gross salary + meal tickets + other remunerations (PwC). 6. Special-conditions employment employer CNAS = 32%; agriculture sector total 24% but only 18% paid by the employer and 6% by the state budget (PwC). 7. Mandatory health insurance (CNAM 9%) is fully borne by the employee — there is no separate employer health premium on payroll (PwC). 8. Standard annual personal exemption MDL 29,700 (MDL 2,475/month), available only where annual taxable income ≤ MDL 360,000 (PwC; EY; salarii.md). 9. Major personal exemption MDL 34,620/yr; per-dependent MDL 9,900/yr; severe-childhood-disability dependent and spouse (major) exemptions MDL 21,780/yr (PwC). 10. Guaranteed minimum monthly wage = MDL 5,500 from 1 Jan 2025 (up from MDL 5,000); rises to MDL 6,300 from 1 Jan 2026 (WageIndicator; gov.md). 11. Monthly unified payroll return Form IPC21 (PIT + CNAS + CNAM) is filed with SFS and all amounts paid by the 25th of the following month (Rivermate; PwC). 12. Annual individual income declaration due by 30 April of the following year where filing is required (news-pravda Moldova). 13. Percentage rates (24% employer CNAS, 6% employee CNAS, 9% CNAM, 12% PIT) were unchanged for 2026, confirming continuity from 2025 (PwC / search confirmation). 14. No general wage ceiling applies to the percentage CNAS/CNAM rates for employees; fixed-sum ceilings apply only to non-employee categories (PwC).  _(PwC; buhgalter.md; EY; salarii.md; WageIndicator; gov.md; Rivermate; news-pravda Moldova)_

## Section 12 -- Tier 2 Catalogue (reviewer judgement required)

**Tier 2 Catalogue (reviewer judgement required)**

| Topic | Judgement call |
| --- | --- |
| CNAM split (9% employee-only vs 4.5%/4.5%) | Source conflict. PwC/Tax Code position is 9% employee-only. **[RESEARCH GAP — reviewer to confirm]** against the current Health Insurance Fund Law for a specific employer setup. |
| Employer CNAS category | Whether the role is standard (24%), special/hazardous (32%), or agriculture (18% + 6% state); materially changes employer cost. |
| Calculation order / deductibility | Whether only CNAM (and not CNAS) reduces the PIT base. **[RESEARCH GAP — reviewer to confirm]** the precise statutory deduction set. |
| Exemption eligibility | Major exemption category (disability/war-injury/rehabilitated), spouse-transfer mechanics, and the MDL 360,000 income-cap effect on the standard exemption. |
| Exact-year exemption figures | The 2025 dependent/spouse/major amounts vs the PwC page now labelled 2026. **[RESEARCH GAP — reviewer to confirm]** against the 2025 Tax Policy annex. |
| Late-payment interest rate | The daily late-payment interest (majorare de întârziere) is set annually by the Ministry of Finance. **[RESEARCH GAP — reviewer to confirm]** the current 2025/2026 rate on sfs.md. |
| Fixed-sum (self-employed) amounts | CNAM/CNAS fixed annual amounts for non-employees. **[RESEARCH GAP — reviewer to confirm]** exact figures for the relevant year. |
| Benefits in kind | Treatment and valuation of non-cash benefits and meal tickets in the PIT/contribution base. **[RESEARCH GAP — reviewer to confirm]** current rules. |

## Section 13 -- Excel Working Paper Template

**Excel Working Paper Template**

| Column | Formula / source |
| --- | --- |
| A. Employee name | input |
| B. Personal tax code (IDNP) | input (mandatory for IPC21) |
| C. CNAS/CNAM enrolment | input |
| D. Pay date / period | input (drives the correct year's minimum wage/exemptions) |
| E. Employer category | input (standard / special / agriculture) |
| F. Gross monthly salary (incl. meal tickets, other remunerations) | input |
| G. Annualised gross | = F × 12 |
| H. Personal exemption (monthly) | = 2,475 if resident AND G ≤ 360,000; else 0 (or 2,885 if major exemption documented) |
| I. Dependent / spouse exemptions (monthly) | = 825 × dependents (+ 1,815 each for severe-disability dependent / spouse) if documented; else 0 |
| J. Employee CNAM 9% | = F × 9% |
| K. Employee CNAS 6% | = F × 6% |
| L. PIT base | = F − J − H − I |
| M. PIT 12% | = MAX(L, 0) × 12% |
| N. Monthly net pay | = F − K − J − M |
| O. Employer CNAS rate | = 24% standard / 32% special / 18% agriculture (from E) |
| P. Employer CNAS amount | = F × O |
| Q. Total employer outlay | = F + P (no employer health premium) |

Notes: (1) CNAM (J) and exemptions (H, I) reduce the PIT base; employee CNAS (K) does NOT — it is computed on gross. (2) For the agriculture category, P uses 18% (employer portion); the 6% state-budget share is not an employer outlay. (3) Never let the PIT base go negative — floor at 0.

## Section 14 -- Moldova Payslip / Statement Reading Guide

**Moldova Payslip / Statement Reading Guide**

| Term (Romanian / English) | Meaning |
| --- | --- |
| Salariu / Salary | Gross or net salary |
| Salariu brut / Gross salary | Gross salary (base for CNAS/CNAM) |
| Salariu net / Net salary | Take-home pay after CNAS, CNAM, PIT |
| Impozit pe venit / Income tax (PIT) | 12% income tax withheld |
| CNAS / BASS / Asigurări sociale | Social insurance contribution (6% employee / 24% employer) |
| CNAM / FAOAM / Asigurare medicală | Mandatory health insurance (9% employee; no employer premium) |
| Scutire personală / Personal exemption | MDL 2,475/month standard personal exemption |
| Scutire pentru persoane întreținute / Dependent exemption | MDL 825/month per dependent |
| Tichete de masă / Meal tickets | Remuneration included in the CNAS/CNAM base |
| IPC21 / Darea de seamă | Unified monthly payroll return (PIT + CNAS + CNAM) |
| IDNP | Personal numeric identification code |

## Section 15 -- Onboarding Fallback

- **Onboarding fallback steps** — If you cannot establish enough to compute payroll, gather in this order and stop where blocked: 1. Calendar year + pay date — selects the correct minimum wage and exemption figures. 2. Gross monthly salary (incl. meal tickets and other remunerations). 3. Residency status — determines exemption eligibility. 4. Exemption declaration — personal / major / dependents / spouse, with documentation. 5. Annual income estimate — to test the MDL 360,000 standard-exemption cap. 6. Employer category — standard (24%), special (32%), or agriculture (18% + 6% state). 7. Personal tax code (IDNP) + CNAS/CNAM enrolment — required to file IPC21. 8. Year-to-date gross, PIT, CNAS, CNAM — for reconciliation. If the engagement turns out to be a self-employed person (fixed-sum CNAS/CNAM category), stop: this employer-payroll skill does not cover self-employed fixed annual contributions.

## Section 16 -- Filing Obligations (Forms)

**Filing Obligations (Forms)**  _(Rivermate; PwC; news-pravda Moldova)_

| Form | Purpose | Deadline | Source |
| --- | --- | --- | --- |
| **IPC21 — Darea de seamă privind reținerea impozitului pe venit, a primelor de asigurare obligatorie de asistență medicală și a contribuțiilor de asigurări sociale de stat obligatorii** | Unified monthly payroll return: income tax withheld + employee/employer social insurance (CNAS) + mandatory health insurance (CNAM); filed electronically with SFS | By the **25th of the month following** the reporting month; same deadline for payment of withheld tax and contributions | Rivermate; PwC |
| **Annual individual income declaration (CET18 / unified return)** | Individual annual income tax return where required (e.g. multiple income sources, over threshold) | By **30 April** following the tax year (2025 income due 30 Apr 2026) | news-pravda Moldova |

### Key Thresholds

**Key Thresholds**  _(PwC (deductions); WageIndicator.org; gov.md)_

| Threshold | Value | Source |
| --- | --- | --- |
| Standard personal exemption | MDL 29,700/yr (MDL 2,475/month) | PwC (deductions); buhgalter.md |
| Income cap for the standard personal exemption | MDL 360,000/yr | PwC (deductions) |
| Major personal exemption | MDL 34,620/yr | PwC (deductions) |
| Per-dependent exemption | MDL 9,900/yr (MDL 825/month) | PwC (deductions) |
| Severe-childhood-disability dependent / spouse (major) exemption | MDL 21,780/yr | PwC (deductions) |
| Minimum monthly wage (2025) | MDL 5,500 | WageIndicator.org |
| Minimum monthly wage (2026) | MDL 6,300 | gov.md |

### Penalties

**Penalties**  _(PwC (tax administration); intelcont.md)_

| Breach | Penalty | Source |
| --- | --- | --- |
| Under-declaring tax / SSC / health contributions via returns with incorrect data | Fine of **20%–30% of the reduced amount** | PwC (tax administration) |
| Failure to correctly complete / submit a tax return | **MDL 500–1,000 per return, capped at MDL 10,000** | PwC (tax administration) |
| Diminishing declared taxable income (general) | Fine of **12%–15%** of the undeclared/diminished taxable income | intelcont.md (Tax Code summary) |
| Late payment of tax/contributions | Daily late-payment interest (majorare de întârziere) accrues per day; rate set annually by the Tax Code/MoF; capped so interest does not exceed the liability under an adjusted return. **[RESEARCH GAP — reviewer to confirm]** the current daily rate on sfs.md | PwC (tax administration) |

## Section 17 -- Interaction with Other Skills

**Interaction with Other Skills**

| Scenario | Skill to Use |
| --- | --- |
| Employee payroll (PIT + CNAS + CNAM + employer CNAS) | **This skill (moldova-payroll.md)** |
| Self-employed fixed-sum CNAS/CNAM | Moldova self-employed contribution skill |
| Moldova VAT returns | moldova-vat skill |
| Moldova bookkeeping | Moldova bookkeeping skill |
| Employer corporate tax | Moldova corporate-tax skill |

### Key Handoff Points

Payroll → Bookkeeping: Gross wages and employer CNAS (24% / 32% / 18%) are expenses; PIT, employee CNAS and CNAM are liabilities until remitted on IPC21.
Payroll → Income Tax: Employment income and tax withheld feed the employee's annual income declaration (due 30 April) where a return is required.
Payroll → Social Insurance: CNAS contributions paid through payroll count toward the employee's pension/social entitlement.

## Section 18 -- Reference Material

**Section 18 Reference Material Table**  _(PwC; Tax Code art. 15; Rivermate; WageIndicator.org; gov.md; salarii.md; buhgalter.md; news-pravda Moldova)_

| Item | Value | Source |
| --- | --- | --- |
| Personal income tax | Flat 12% | Tax Code art. 15; PwC |
| Special non-payroll rates | 6% dividends; 7% certain farming distributions; 18% gambling/lottery | PwC (taxes on personal income) |
| Employee social insurance (CNAS / BASS) | 6% | PwC (other taxes) |
| Employee health insurance (CNAM / FAOAM) | 9% (employee-only) | PwC (other taxes) |
| Employer social insurance (CNAS) — standard | 24% | PwC (other taxes) |
| Employer CNAS — special/hazardous | 32% | PwC (other taxes) |
| Employer CNAS — agriculture | 18% employer + 6% state budget (24% total) | PwC (other taxes) |
| Employer health premium | none (0%) | PwC (other taxes) |
| Standard personal exemption | MDL 29,700/yr (MDL 2,475/mo), income cap MDL 360,000 | PwC (deductions); buhgalter.md; salarii.md |
| Major personal exemption | MDL 34,620/yr | PwC (deductions) |
| Per-dependent exemption | MDL 9,900/yr (MDL 825/mo) | PwC (deductions) |
| Severe-disability dependent / spouse (major) exemption | MDL 21,780/yr | PwC (deductions) |
| Minimum monthly wage 2025 | MDL 5,500 | WageIndicator.org |
| Minimum monthly wage 2026 | MDL 6,300 | gov.md |
| Reference average monthly wage 2025 | MDL 16,100 | salarii.md |
| Monthly return | Form IPC21, due 25th of following month | Rivermate; PwC |
| Annual individual declaration | Due 30 April following year | news-pravda Moldova |

- **Personal income tax** — Flat 12%  _(Tax Code art. 15; PwC)_
- **Special non-payroll rates** — 6% dividends; 7% certain farming distributions; 18% gambling/lottery  _(PwC (taxes on personal income))_
- **Employee social insurance (CNAS / BASS)** — 6%  _(PwC (other taxes))_
- **Employee health insurance (CNAM / FAOAM)** — 9% (employee-only)  _(PwC (other taxes))_
- **Employer social insurance (CNAS) — standard** — 24%  _(PwC (other taxes))_
- **Employer CNAS — special/hazardous** — 32%  _(PwC (other taxes))_
- **Employer CNAS — agriculture** — 18% employer + 6% state budget (24% total)  _(PwC (other taxes))_
- **Employer health premium** — none (0%)  _(PwC (other taxes))_
- **Standard personal exemption** — MDL 29,700/yr (MDL 2,475/mo), income cap MDL 360,000  _(PwC (deductions); buhgalter.md; salarii.md)_
- **Major personal exemption** — MDL 34,620/yr  _(PwC (deductions))_
- **Per-dependent exemption** — MDL 9,900/yr (MDL 825/mo)  _(PwC (deductions))_
- **Severe-disability dependent / spouse (major) exemption** — MDL 21,780/yr  _(PwC (deductions))_
- **Minimum monthly wage 2025** — MDL 5,500  _(WageIndicator.org)_
- **Minimum monthly wage 2026** — MDL 6,300  _(gov.md)_
- **Reference average monthly wage 2025** — MDL 16,100  _(salarii.md)_
- **Monthly return** — Form IPC21, due 25th of following month  _(Rivermate; PwC)_
- **Annual individual declaration** — Due 30 April following year  _(news-pravda Moldova)_

### Sources

1. PwC Worldwide Tax Summaries — Moldova Individual: Other taxes (social & health contributions) (reviewed Jan 2026) — https://taxsummaries.pwc.com/moldova/individual/other-taxes
2. PwC Worldwide Tax Summaries — Moldova Individual: Taxes on personal income (flat 12%) — https://taxsummaries.pwc.com/moldova/individual/taxes-on-personal-income
3. PwC Worldwide Tax Summaries — Moldova Individual: Deductions (personal/dependent exemptions) — https://taxsummaries.pwc.com/moldova/individual/deductions
4. PwC Worldwide Tax Summaries — Moldova Corporate: Tax administration (penalties, deadlines) — https://taxsummaries.pwc.com/moldova/corporate/tax-administration
5. EY Moldova Tax Alert 3 — September 2024 (2025 exemption increases) — https://www.ey.com/en_ro/technical/tax-alerts/ey-moldova-tax-alert-3---september-2024
6. Buhgalter.md — How to calculate salary and taxes in Moldova in 2025 (worked example) — https://www.buhgalter.md/en/cum-se-calculeaza-salariul-in-moldova/
7. WageIndicator.org — Minimum Wage Updated in Moldova from 01 January 2025 (MDL 5,500) — https://wageindicator.org/salary/minimum-wage/minimum-wages-news/2025/minimum-wage-updated-in-moldova-from-01-january-2025-january-01-2025
8. Government of the Republic of Moldova — Government approved minimum & average wage for 2026 (MDL 6,300) — https://gov.md/ro/comunicate-de-presa/guvernul-aprobat-cuantumul-salariului-minim-si-mediu-pentru-anul-2026
9. Rivermate — Employment Taxes in Moldova (Form IPC21, 25th deadline) — https://rivermate.com/guides/moldova/taxes
10. Salarii.md — Modificări taxe și scutiri salarii 2025 (2025 exemptions & rates) — https://salarii.md/modificari-taxe-si-scutiri-salarii-2025/
11. State Tax Service of Moldova (official) — https://www.sfs.md/en
12. National Social Insurance House (official) — https://cnas.gov.md/en/

### Research Caveats (read before relying on figures)

- Confidence is **high** for the core 2025 payroll mechanics; most figures are corroborated by two or more Big-4 / official-portal sources.
- The live SFS / CNAS / CNAM rate pages were not directly retrievable at research time (homepages did not expose the schedule; intelcont/cnam pages returned HTTP 403), so primary-authority figures were corroborated via PwC and Moldovan accounting portals rather than read off the authority's own rate schedule. **Confirm against the current annual Social Insurance Budget Law, Health Insurance Fund Law and the Tax Code.**
- **CNAM split conflict:** several EOR/secondary sites present CNAM as a 4.5% employer + 4.5% employee split, while PwC and the Tax Code position state 9% employee-only with no employer health premium. The 9% employee-only position is adopted here; verify before relying on it.
- salarii.md mislabels the 9% as "CNAS" — it is CNAM.
- 2025-specific dependent/spouse exemption amounts (MDL 9,900 / 21,780) and the major exemption (MDL 34,620) are taken from PwC (now labelled 2026) and salarii.md's 2025 table; they match across both years — verify the 2025 Tax Policy annex for exact-year precision.
- No general wage ceiling applies to the percentage CNAS/CNAM rates for employees; fixed-sum ceilings apply only to non-employee (self-employed) categories.
- The daily late-payment interest rate (majorare de întârziere) is set annually by the Ministry of Finance and was not captured as a precise 2025 figure — confirm the current rate on sfs.md.

## Section 19 -- Test Suite

Each test recomputed end-to-end; expected values reconcile to the cent (2025 rates/exemptions, MDL).

1. **Flat-rate base.** Gross MDL 16,100, single, personal exemption. CNAM 9% = 1,449.00; PIT base = 16,100 − 1,449 − 2,475 = 12,176.00; PIT 12% = **1,461.12**; CNAS 6% = 966.00; net = **12,223.88**.
2. **Minimum wage net.** Gross MDL 5,500 (2025). CNAM = 495.00; PIT base = 5,500 − 495 − 2,475 = 2,530.00; PIT = **303.60**; CNAS = 330.00; net = **4,371.40**.
3. **Two dependents.** Gross MDL 20,000. Dependent exemption = 2 × 825 = 1,650.00; PIT base = 20,000 − 1,800 − 2,475 − 1,650 = 14,075.00; PIT = **1,689.00**; net = **15,311.00**.
4. **Special-conditions employer rate.** Gross MDL 18,000, single. Employee side identical to standard: CNAS = 1,080.00, CNAM = 1,620.00, PIT base = 13,905.00, PIT = **1,668.60**, net = **13,631.40**. Employer CNAS 32% = **5,760.00** (vs 4,320.00 at 24%).
5. **Agriculture split.** Gross MDL 10,000. PIT base = 10,000 − 900 − 2,475 = 6,625.00; PIT = **795.00**; net = **7,705.00**. Employer outlay = 10,000 × 18% = **1,800.00**; state-budget 6% = 600.00; total system contribution = 2,400.00 (24%).
6. **Personal-exemption income cap.** Gross MDL 35,000 (annual 420,000 > 360,000) → personal exemption = 0. PIT base = 35,000 − 3,150 = 31,850.00; PIT = **3,822.00**; CNAS = 2,100.00; CNAM = 3,150.00; net = **25,928.00**.
7. **Employee combined rate (before exemptions).** CNAS 6% + CNAM 9% + PIT 12% = **27%** of gross before exemptions; with a positive exemption the realised total is below 27%.
8. **Employer standard load.** Gross MDL 16,100 → employer CNAS 24% = **3,864.00**; no employer health premium; total outlay = **19,964.00**.
9. **CNAM employee-only.** Gross MDL 16,100 → CNAM = 16,100 × 9% = **1,449.00** borne entirely by the employee; employer CNAM = 0.00 (NOT 724.50 on a 4.5% split).
10. **Monthly exemption conversion.** Standard personal exemption MDL 29,700/yr ÷ 12 = **2,475.00/mo**; dependent MDL 9,900/yr ÷ 12 = **825.00/mo**; both exact.
11. **IPC21 deadline.** A March 2025 payroll → IPC21 filed and PIT/CNAS/CNAM paid by **25 April 2025**.
12. **IDNP refusal.** Employee with no personal tax code (IDNP) → refuse to file IPC21.

- **IDNP refusal** — Employee with no personal tax code (IDNP) → refuse to file IPC21.  _(Section 19 Test Suite, item 12)_

## PROHIBITIONS

- **No progressive brackets** — NEVER apply progressive brackets — Moldova PIT is a FLAT 12% (Tax Code art. 15).  _(Tax Code art. 15)_
- **CNAS not deductible from PIT base** — NEVER deduct employee CNAS (6%) from the PIT base — only CNAM (9%) and exemptions reduce the PIT base; CNAS is computed on gross.  _(PROHIBITIONS section)_
- **No separate employer health-insurance percentage** — NEVER add a separate employer health-insurance percentage — CNAM is 9% employee-only, no employer premium.  _(PROHIBITIONS section)_
- **No 4.5%/4.5% CNAM split** — NEVER use a 4.5%/4.5% CNAM split — default to 9% employee-only and flag the conflict.  _(PROHIBITIONS section)_
- **Standard personal exemption income cap** — NEVER apply the standard personal exemption where annual taxable income exceeds MDL 360,000.  _(PROHIBITIONS section)_
- **Exemption eligibility documentation** — NEVER apply major, dependent, or spouse exemptions without documented eligibility.  _(PROHIBITIONS section)_
- **Employer CNAS rate default** — NEVER use the 32% or 18% employer CNAS rate unless the employer category (special-conditions / agriculture) is confirmed — default to 24%.  _(PROHIBITIONS section)_
- **Agriculture state-budget share not employer outlay** — NEVER treat the agriculture 6% state-budget share as an employer outlay — the employer pays only 18%.  _(PROHIBITIONS section)_
- **IPC21 deadline compliance** — NEVER miss the 25th-of-following-month IPC21 deadline — penalties and daily interest apply.  _(PROHIBITIONS section)_
- **Estimated computations disclosure** — NEVER present payroll computations as definitive — always label as estimated and direct to a Moldova-licensed accountant.  _(PROHIBITIONS section)_

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a licensed accountant in Moldova) before implementation.

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
