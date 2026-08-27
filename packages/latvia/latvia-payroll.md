---
name: latvia-payroll
description: Use this skill whenever asked about Latvia payroll processing for employed persons. Trigger on phrases like "Latvia payroll", "VSAOI", "IIN Latvia", "PIT withholding Latvia", "social contributions Latvia", "Darba devēja ziņojums", "employer's report Latvia", "non-taxable minimum Latvia", "algas nodokļa grāmatiņa", "wage tax book", "solidarity tax Latvia", "business risk state fee", "uzņēmējdarbības riska valsts nodeva", "net salary Latvia", "gross to net Latvia", "minimum wage Latvia", "EDS report", "VID withholding", "salary calculation Latvia", or any question about computing employee pay, personal income tax withholding, or state social insurance contributions for Latvia-based employees. This skill covers IIN (personal income tax) — flat 25.5% monthly withholding, with the 33% band and +3% surtax settled at the annual income declaration — VSAOI state social insurance (employee and employer shares), the business risk state fee, the fixed non-taxable minimum, dependant and disability allowances, solidarity tax, minimum wage, and EDS filing obligations for tax year 2025. ALWAYS read this skill before processing any Latvia payroll.
version: 0.1
jurisdiction: LV
tax_year: 2025
last_updated: 2026-07-13
review_status: pending_review
depends_on:
  - payroll-workflow-base
category: payroll
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Latvia Payroll

## Latvia Payroll Skill v0.1

Tier 2 — research-verified. NOT yet signed off by a Latvian-licensed accountant. Treat every figure as provisional pending professional review.

## Section 1 -- Quick Reference

**Quick Reference table**

| Field | Value |
| --- | --- |
| Country | Latvia (Republic of Latvia / Latvijas Republika) |
| Currency | EUR only |
| Standard pay frequency | Monthly (most common) |
| Tax year | Calendar year (1 January -- 31 December) |
| Tax withholding system | Monthly PIT withholding by employer as tax agent (IIN), reconciled via annual income declaration |
| Personal income tax (PIT / IIN) | Progressive at annual reconciliation: 25.5% (annual income up to EUR 105,300) / 33% (above), +3% surtax over EUR 200,000. Monthly payroll is withheld at a **flat 25.5%** (VID; PwC). |
| Tax authority | State Revenue Service (Valsts ieņēmumu dienests, VID) -- via Electronic Declaration System (EDS, eds.vid.gov.lv) |
| Social insurance authority | State Social Insurance Agency (Valsts sociālās apdrošināšanas aģentūra, VSAA) |
| Mandatory social contributions | VSAOI -- employer 23.59% + employee 10.50% = 34.09% (standard, 2025) |
| Business risk state fee | EUR 0.36 per employee per month (employer only; unchanged 2025-2026) |
| Key legislation | Law "On Personal Income Tax" (Likums "Par iedzīvotāju ienākuma nodokli", IIN); Law "On State Social Insurance" (Likums "Par valsts sociālo apdrošināšanu"); Solidarity Tax Law (Solidaritātes nodokļa likums); Labour Law (Darba likums) |
| Filing portal | VID Electronic Declaration System (EDS) -- eds.vid.gov.lv |
| Validated by | Pending -- requires sign-off by a Latvian-licensed accountant |
| Skill version | 0.1 |

The 2025 PIT reform took effect 1 January 2025: the income-tested differentiated non-taxable minimum was abolished and replaced with a fixed EUR 510/month minimum, and the prior three-rate PIT was replaced with the two-rate 25.5%/33% system. (Source: Ministry of Finance, "Changes in taxation and finances from 2025"; Lex & Finance.)

## Section 2 -- Personal Income Tax Withholding (IIN)

The employer acts as the tax agent: it withholds personal income tax (IIN) and the employee's share of state social insurance (VSAOI) from gross monthly salary, and remits both to VID's single tax account. The employer adds its own VSAOI share on top of gross.

### PIT Rates (2025) — progressive at ANNUAL reconciliation, flat 25.5% withheld MONTHLY

VID applies the progressive PIT scale to **annual** income; the higher rates are settled on the annual income declaration. Employers withhold a **flat 25.5% monthly** regardless of the monthly amount. (Source: VID "Personal Income Tax rates" — "25.5% — monthly income"; "income under EUR 105,300 — 25.5%, income from EUR 105,300 — 33%"; PwC Worldwide Tax Summaries — Latvia.)

**PIT Rates 2025 table**  _(VID "Personal Income Tax rates"; PwC Worldwide Tax Summaries — Latvia)_

| Annual taxable income (EUR) | Rate | Withheld monthly by employer? |
| --- | --- | --- |
| Up to 105,300 | 25.5% | Yes — flat 25.5% on each month's taxable base. Same EUR 105,300 figure is the VSAOI annual cap. |
| Above 105,300 | 33% | **No.** Settled on the annual income declaration the following year; monthly payroll still withholds 25.5%. |
| Above 200,000 total annual income | +3% surtax (on the excess, on top of 33%) | **No.** Annual income declaration only. |

- **No monthly EUR 8,775 PIT bracket** — There is no monthly EUR 8,775 PIT bracket. EUR 8,775 ≈ 105,300/12 is only the monthly equivalent of the annual band boundary; it is NOT a statutory monthly withholding threshold. Monthly payroll always withholds at 25.5%; the 33% and +3% are annual-reconciliation items.  _(VID "Personal Income Tax rates"; PwC)_

### Monthly Withholding Method

- **Monthly PIT withholding formula** — Taxable income = Gross monthly salary - employee VSAOI (10.50% of gross) - non-taxable minimum (if wage tax book held — see Section 5) - applicable allowances (dependant / disability / repressed) Monthly PIT withheld = 25.5% × taxable income (flat, all months)  _(VID; PwC)_
- **33% and 3% surtax reconciliation timing** — The 33% rate (annual income above EUR 105,300) and the +3% surtax (annual income above EUR 200,000) are reconciled by the individual on the annual income declaration (gada ienākumu deklarācija); they are NOT applied in routine monthly payroll.  _(VID; PwC)_

Order of operations note: employee VSAOI is deducted from gross *before* PIT is computed; the non-taxable minimum and allowances are then subtracted from the post-VSAOI amount. Always confirm sequencing for edge cases with the reviewer. [RESEARCH GAP — reviewer to confirm exact statutory ordering of VSAOI vs. non-taxable-minimum deduction in the monthly base.]

## Section 3 -- State Social Insurance -- Employee Deductions (VSAOI)

The employee VSAOI share is withheld by the employer from gross salary before PIT and remitted with the employer share.

### Employee VSAOI Rates (2025)

**Employee VSAOI Rates table**  _(VSAA "On contributions"; MindLink national social insurance rates 2025; PwC)_

| Employee category | Employee rate | Base | Floor | Ceiling |
| --- | --- | --- | --- | --- |
| Standard (fully insured, below state pension age) | 10.50% | Gross salary before PIT | None for standard employees | EUR 105,300/year |
| Reached state pension age / granted old-age pension | 9.25% | Gross salary before PIT | None | EUR 105,300/year |

- **Above-cap treatment** — Income above the EUR 105,300 annual cap is no longer subject to ordinary VSAOI — it falls under the solidarity-tax mechanism (Section 4 / Section 9).

## Section 4 -- State Social Insurance -- Employer Contributions (VSAOI) + Solidarity Tax

The employer pays its VSAOI share on top of gross salary.

### Employer VSAOI Rates (2025)

**Employer VSAOI Rates table**  _(VSAA "On contributions"; MindLink 2025; PwC. 1 percentage point of the total funds health/healthcare services.)_

| Employee category | Employer rate | Combined (employer + employee) | Base | Ceiling |
| --- | --- | --- | --- | --- |
| Standard (fully insured, below state pension age) | 23.59% | 34.09% (23.59% + 10.50%) | Gross salary before PIT | EUR 105,300/year |
| Reached state pension age / granted old-age pension | 20.77% | 30.02% (20.77% + 9.25%) | Gross salary before PIT | EUR 105,300/year |

### Business Risk State Fee (uzņēmējdarbības riska valsts nodeva)

**Business Risk State Fee table**  _(VID; Cabinet Regulation 2025; mkd.gov.lv "Business risk state fee unchanged in 2026"; ifinanses 2026)_

| Item | Amount | Note |
| --- | --- | --- |
| Business risk state fee | **EUR 0.36 per employee per month** | Paid solely by the employer for each person in an employment relationship (excluding seasonal agricultural workers under that special regime). Funds the Employee Claims Guarantee Fund. **Unchanged at EUR 0.36 for both 2025 and 2026.** Paid by the 23rd of the following month with PIT + VSAOI. |

- **Fee nature** — This is a flat per-head amount, NOT a percentage of wages, and is part of total employer cost.  _(VID; Cabinet Regulation 2025; mkd.gov.lv; ifinanses 2026)_

[RESEARCH GAP — reviewer to confirm] The retirement-age split (employer 20.77% / employee 9.25% = 30.02%) is published by PwC Worldwide Tax Summaries (Latvia, "Other taxes") and MindLink's 2025 rate table. VSAA's own page states only the combined standard 34.09% and notes rates vary by insured-person status without publishing the per-category percentages; the per-category distribution should still be confirmed against the current Cabinet Regulation on VSAOI rate distribution.

### Solidarity Tax (solidaritātes nodoklis)

**Solidarity Tax table**  _(lexfinance.lv; PwC; VSAA)_

| Item | Detail |
| --- | --- |
| Applies to | Income exceeding the EUR 105,300/year VSAOI cap |
| Withheld during year | Full 34.09% VSAOI rate is withheld on income above the cap |
| Year-end reconciliation | VID reconciles down to an **effective 25%** solidarity tax rate (legislated since 2021); the difference is refunded/reconciled |
| Administered by | VID |

- **Routine payroll treatment above cap** — In routine monthly payroll, continue applying the full VSAOI rate above the cap; the reconciliation to the effective 25% rate is an annual / VID-driven process, not a payroll-run adjustment.  _(lexfinance.lv; PwC; VSAA)_

### Fixed Non-Taxable Minimum and Allowances (2025)

**Fixed Non-Taxable Minimum and Allowances table**  _(Ministry of Finance "Non-taxable minimum and tax allowances" and "Changes 2025"; VSAA pension minimum 2025; lexfinance.lv)_

| Item | Monthly | Annual | Condition |
| --- | --- | --- | --- |
| Fixed non-taxable minimum | EUR 510 | EUR 6,120 | Fixed for all employees regardless of income (differentiated minimum abolished from 1 Jan 2025). Applied only if the employee has filed their wage tax book with this employer. |
| Pensioner non-taxable minimum | EUR 1,000 | EUR 12,000 | Old-age pensioners; EUR 1,000/month for both 2025 and 2026. (Source: Ministry of Finance "Non-taxable minimum and tax allowances".) |
| Dependant allowance (per dependant) | EUR 250 | EUR 3,000 | Per dependant (typically children); unchanged since 2021. Applied only by the employer holding the wage tax book. |
| Additional allowance — disability Group I and II | EUR 154 | EUR 1,848 | — |
| Additional allowance — disability Group III | EUR 120 | EUR 1,440 | — |
| Additional allowance — politically repressed persons / national resistance participants | EUR 154 | EUR 1,848 | — |

- **Wage tax book gateway** — Critical: The non-taxable minimum and ALL allowances can be applied at payroll only by the employer holding the employee's wage tax book (algas nodokļa grāmatiņa). If the wage tax book is not filed with this employer, withhold WITHOUT them (see Conservative Defaults).

### National Minimum Wage (2025)

**National Minimum Wage table**  _(Ministry of Welfare; Cabinet of Ministers; Eurofound)_

| Item | Amount |
| --- | --- |
| Statutory minimum monthly wage (gross) | EUR 740/month, effective 1 January 2025 |

- **2026 minimum wage warning** — Rises to EUR 780/month from 1 January 2026 — do NOT use the 2026 figure for a 2025 computation.  _(Ministry of Welfare; Cabinet of Ministers; Eurofound)_

### Minimum VSAOI Contribution Base

- **Minimum VSAOI object / top-up rule** — A minimum monthly VSAOI object equal to the minimum wage (EUR 740/month) applies. If an employee's reported monthly VSAOI income is below EUR 740, the employer must pay top-up minimum contributions on the shortfall, assessed quarterly by VSAA. Statutory exceptions apply (e.g. first 3 months of employment, multiple employers, disability, students).  _(VSAA; payroll guides)_

[RESEARCH GAP — reviewer to detail] The full list of minimum-contribution exemptions (first months of employment, multiple-employer aggregation, disability, students) should be confirmed against the current statute by the reviewer.

- **Self-employed voluntary minimum annual base** — The self-employed / voluntary minimum annual VSAOI base for 2025 is 12 × EUR 740 = EUR 8,880/year (not applicable to standard employed payroll; included for cross-reference).

## Section 6 -- Conservative Defaults

**Conservative Defaults table**

| Assumption | Conservative default |
| --- | --- |
| Non-taxable minimum applied | **EUR 0** unless the employee has filed their wage tax book (algas nodokļa grāmatiņa) with this employer. The EUR 510/month minimum and EUR 250/dependant allowance can only be applied at the employer holding the wage tax book. |
| Standard VSAOI rate | Use **23.59% employer + 10.50% employee (34.09% total)** for a standard fully-insured employee below state pension age. Switch to 20.77% + 9.25% only when retirement-age status is confirmed. |
| Income vs. VSAOI cap | Apply full VSAOI on the whole salary up to **EUR 105,300/year**; only above the cap does the solidarity-tax treatment apply. |
| PIT rate (monthly) | Withhold a **flat 25.5%** on the monthly taxable base for all employees. Do NOT apply 33% in monthly payroll (it is an annual-reconciliation item keyed to annual income above EUR 105,300), and do not pre-apply the 3% surtax. |
| Dependant / disability allowance | EUR 0 unless documented and the wage tax book is held by this employer. |
| Business risk state fee | Always **EUR 0.36 per employee per month** (employer only); add to every employee's total employer cost. |

## Section 7 -- Required Inputs and Refusal Catalogue

### Required Inputs

- **Required inputs list** — Before computing Latvia payroll, you MUST have: 1. Gross monthly salary (EUR). 2. Wage tax book status — is the algas nodokļa grāmatiņa filed with THIS employer? (Determines whether the non-taxable minimum and allowances apply.) 3. Employee age / pension status — has the employee reached state pension age or been granted an old-age pension? (Determines 34.09% vs. 30.02% VSAOI.) 4. Number of dependants (for the EUR 250/dependant allowance) — only if the wage tax book is held here. 5. Disability / repressed-person status (for additional allowances) — only if documented and wage tax book held here. 6. Year-to-date gross — needed to track the EUR 105,300 annual VSAOI cap (which also marks where annual PIT moves from 25.5% to 33% at the annual declaration). Monthly withholding stays at 25.5% regardless.

### Refusal Catalogue — STOP and ask before computing if:

**Refusal Catalogue table**

| Missing / ambiguous | Why it blocks computation |
| --- | --- |
| Wage tax book status unknown | Cannot decide whether to apply the EUR 510 minimum and allowances; defaulting wrong over-/under-withholds materially. |
| Pension-age status unknown for an older worker | Wrong VSAOI rate (34.09% vs. 30.02%). |
| Salary near or above EUR 105,300/year | VSAOI cap, the 25.5%→33% annual band change, and solidarity-tax interaction all trigger — confirm YTD figures. (Monthly withholding still 25.5%; the 33% is annual.) |
| Sub-minimum-wage salary | Minimum-contribution top-up may be due; confirm exemptions. |
| Claimed allowances without documentation | Allowances require the wage tax book and supporting status. |
| Request to apply the 3% surcharge or solidarity reconciliation in monthly payroll | These are annual / VID-driven, not payroll-run items — clarify scope. |

- **Never guess directive** — Never guess any of the above. State the assumption, label outputs as estimates, and direct to a licensed accountant.

## Section 8 -- Transaction / Payment Pattern Library

Deterministic classification of bank-statement lines for Latvian payroll. Latvian banks (Swedbank, SEB, Citadele, Luminor) post descriptions in Latvian and sometimes English.

### Salary Credits (employee side)

**Salary Credits table**

| Pattern (LV / EN) | Classification |
| --- | --- |
| ALGA, DARBA ALGA, NETO ALGA | Net salary payment |
| ATALGOJUMS, SAMAKSA PAR DARBU | Net salary / remuneration |
| PIEMAKSA, PRĒMIJA, BONUSS | Bonus / supplement (taxable) |
| ATVAĻINĀJUMA NAUDA | Holiday pay (taxable) |
| PĀRSKAITĪJUMS NO [employer name] | Net salary inbound transfer |

### Employer Debit Patterns

**Employer Debit Patterns table**

| Pattern (LV / EN) | Classification |
| --- | --- |
| VID, VALSTS IEŅĒMUMU DIENESTS, VIENOTAIS NODOKĻU KONTS | Tax remittance to VID single tax account (PIT + VSAOI) |
| IIN, IEDZĪVOTĀJU IENĀKUMA NODOKLIS | Personal income tax remittance |
| VSAOI, SOCIĀLĀS APDROŠINĀŠANAS IEMAKSAS | State social insurance contributions (employer + withheld employee share) |
| SOLIDARITĀTES NODOKLIS | Solidarity tax (above-cap income) |
| UZŅĒMĒJDARBĪBAS RISKA VALSTS NODEVA, RISKA NODEVA | Business risk state fee (EUR 0.36 × headcount) |
| ALGU IZMAKSA, ALGAS, DARBA ALGAS | Net wages disbursement to employees |
| NOKAVĒJUMA NAUDA | Late-payment interest (0.05%/day) — penalty, not payroll cost |

### Accounting Classification Map

**Accounting Classification Map table**

| Payroll element | Books treatment |
| --- | --- |
| Gross wages | Expense |
| Employer VSAOI (23.59% / 20.77%) | Expense |
| Business risk state fee (EUR 0.36/employee/month) | Expense |
| Employee VSAOI (10.50% / 9.25%) | Liability (withheld) until remitted |
| Withheld PIT (IIN) | Liability (withheld) until remitted |
| Net pay to employee | Reduction of cash; clears wages payable |

## Section 9 -- Worked Examples

All examples use 2025 figures. Estimates only — not professional advice. "Wage tax book held" means the algas nodokļa grāmatiņa is filed with this employer (so the non-taxable minimum and allowances apply).

### Example 1 — Standard single employee, wage tax book held, no dependants

- Gross monthly salary: EUR 2,000
- Wage tax book held here: yes → apply EUR 510 non-taxable minimum
- Below pension age → VSAOI 34.09% (employer 23.59% / employee 10.50%)

**Example 1 computation table**

| Step | Computation | Amount (EUR) |
| --- | --- | --- |
| Employee VSAOI | 2,000 × 10.50% | 210.00 |
| PIT base | 2,000 − 210.00 − 510 (minimum) | 1,280.00 |
| PIT | 1,280.00 × 25.5% (flat monthly rate) | 326.40 |
| Net pay | 2,000 − 210.00 − 326.40 | **1,463.60** |
| Employer VSAOI | 2,000 × 23.59% | 471.80 |
| Business risk state fee | flat, per employee | 0.36 |
| Total employer cost | 2,000 + 471.80 + 0.36 | **2,472.16** |

Bank statement: `ALGA PĀRSKAITĪJUMS EUR 1,463.60` to employee; later `VID VIENOTAIS NODOKĻU KONTS` debit covering PIT EUR 326.40 + total VSAOI EUR 681.80; separate `UZŅĒMĒJDARBĪBAS RISKA VALSTS NODEVA EUR 0.36`.

### Example 2 — Same salary, NO wage tax book filed here

- Gross monthly salary: EUR 2,000
- Wage tax book held here: no → non-taxable minimum = EUR 0 (Conservative Default)

**Example 2 computation table**

| Step | Computation | Amount (EUR) |
| --- | --- | --- |
| Employee VSAOI | 2,000 × 10.50% | 210.00 |
| PIT base | 2,000 − 210.00 − 0 | 1,790.00 |
| PIT | 1,790.00 × 25.5% | 456.45 |
| Net pay | 2,000 − 210.00 − 456.45 | **1,333.55** |
| Employer VSAOI | 2,000 × 23.59% | 471.80 |
| Business risk state fee | flat, per employee | 0.36 |
| Total employer cost | 2,000 + 471.80 + 0.36 | **2,472.16** |

Note the EUR 130.05 difference in net pay vs. Example 1 — driven solely by whether the wage tax book is filed here. This is why wage tax book status is a required input.

### Example 3 — Employee with one dependant, wage tax book held

- Gross monthly salary: EUR 1,500
- Wage tax book held here: yes → EUR 510 minimum + EUR 250 dependant allowance
- Below pension age → 34.09% VSAOI

**Example 3 computation table**

| Step | Computation | Amount (EUR) |
| --- | --- | --- |
| Employee VSAOI | 1,500 × 10.50% | 157.50 |
| PIT base | 1,500 − 157.50 − 510 − 250 | 582.50 |
| PIT | 582.50 × 25.5% | 148.54 |
| Net pay | 1,500 − 157.50 − 148.54 | **1,193.96** |
| Employer VSAOI | 1,500 × 23.59% | 353.85 |
| Business risk state fee | flat, per employee | 0.36 |
| Total employer cost | 1,500 + 353.85 + 0.36 | **1,854.21** |

### Example 4 — Minimum-wage employee, wage tax book held

- Gross monthly salary: EUR 740 (2025 statutory minimum)
- Wage tax book held here: yes → EUR 510 minimum

**Example 4 computation table**

| Step | Computation | Amount (EUR) |
| --- | --- | --- |
| Employee VSAOI | 740 × 10.50% | 77.70 |
| PIT base | 740 − 77.70 − 510 | 152.30 |
| PIT | 152.30 × 25.5% | 38.84 |
| Net pay | 740 − 77.70 − 38.84 | **623.46** |
| Employer VSAOI | 740 × 23.59% | 174.57 |
| Business risk state fee | flat, per employee | 0.36 |
| Total employer cost | 740 + 174.57 + 0.36 | **914.93** |

At exactly the minimum wage the minimum VSAOI contribution base is met, so no employer top-up is due. If the salary were below EUR 740 (e.g. part-month), check the quarterly minimum-contribution rule (Section 5).

### Example 5 — Retirement-age employee

- Gross monthly salary: EUR 1,800
- Pension age reached → VSAOI 30.02% (employer 20.77% / employee 9.25%)
- Wage tax book held here: yes → EUR 1,000 pensioner non-taxable minimum (2025)

**Example 5 computation table**

| Step | Computation | Amount (EUR) |
| --- | --- | --- |
| Employee VSAOI | 1,800 × 9.25% | 166.50 |
| PIT base | 1,800 − 166.50 − 1,000 | 633.50 |
| PIT | 633.50 × 25.5% | 161.54 |
| Net pay | 1,800 − 166.50 − 161.54 | **1,471.96** |
| Employer VSAOI | 1,800 × 20.77% | 373.86 |
| Business risk state fee | flat, per employee | 0.36 |
| Total employer cost | 1,800 + 373.86 + 0.36 | **2,174.22** |

The 30.02% split is reviewer-pending (see Section 4 RESEARCH GAP).

### Example 6 — High earner (monthly withholding stays flat 25.5%)

- Gross monthly salary: EUR 10,000
- Wage tax book held here: yes (EUR 510 minimum)
- Below pension age → 34.09% VSAOI; on a single month this is well within the EUR 105,300 annual cap, so full VSAOI applies

**Example 6 computation table**

| Step | Computation | Amount (EUR) |
| --- | --- | --- |
| Employee VSAOI | 10,000 × 10.50% | 1,050.00 |
| PIT base | 10,000 − 1,050.00 − 510 | 8,440.00 |
| PIT withheld @ 25.5% | 8,440.00 × 25.5% (flat monthly rate) | 2,152.20 |
| Net pay | 10,000 − 1,050.00 − 2,152.20 | **6,797.80** |
| Employer VSAOI | 10,000 × 23.59% | 2,359.00 |
| Business risk state fee | flat, per employee | 0.36 |
| Total employer cost | 10,000 + 2,359.00 + 0.36 | **12,359.36** |

- **Flat monthly withholding regardless of salary level** — Monthly payroll withholds a flat 25.5% on the taxable base regardless of how high the monthly salary is — there is no monthly 33% bracket. The 33% rate is only applied at the annual income declaration on annual income above EUR 105,300, and the +3% surtax on annual income above EUR 200,000 is likewise an annual-declaration item. Track YTD gross against the EUR 105,300 VSAOI cap; once annual income exceeds it, VSAOI is reconciled to the solidarity-tax treatment (see Section 4) and annual PIT moves into the 33% band — but neither changes the in-year 25.5% monthly withholding.  _(VID "Personal Income Tax rates"; PwC)_

## Section 10 -- Tier 1 Rules (Deterministic — apply directly)

- **1. PIT annual progressive / monthly flat withholding** — PIT (2025) is progressive at annual reconciliation: 25.5% on annual income up to EUR 105,300, 33% above. Monthly payroll withholds a flat 25.5% on the monthly taxable base — there is no monthly 33% bracket. The 33% is settled on the annual income declaration.  _(VID "Personal Income Tax rates"; PwC)_
- **2. +3% surtax annual only** — The +3% surtax on total annual income over EUR 200,000 is assessed only on the annual income declaration — never in monthly payroll.  _(VID; PwC)_
- **3. Fixed non-taxable minimum** — EUR 510/month (EUR 6,120/year) for 2025, replacing the abolished differentiated minimum.  _(Ministry of Finance; lexfinance.lv)_
- **4. Pensioner non-taxable minimum** — EUR 1,000/month (EUR 12,000/year) for both 2025 and 2026.  _(Ministry of Finance)_
- **5. Dependant allowance** — EUR 250/month (EUR 3,000/year) per dependant.  _(Ministry of Finance)_
- **6. Disability / repressed persons allowances** — Disability Group I/II allowance EUR 154/month; Group III EUR 120/month; politically repressed persons EUR 154/month.  _(Ministry of Finance)_
- **7. Wage tax book gateway** — The non-taxable minimum and all allowances apply at payroll only at the employer holding the wage tax book (algas nodokļa grāmatiņa).  _(VID)_
- **8. Standard VSAOI rate** — 34.09% (employer 23.59% + employee 10.50%); the employer withholds the employee share and remits the total.  _(VSAA; PwC)_
- **9. Retirement-age VSAOI rate** — 30.02% (employer 20.77% + employee 9.25%).  _(MindLink 2025 — reviewer-pending)_
- **10. VSAOI base and cap** — VSAOI is computed on gross salary before PIT; the annual cap is EUR 105,300 for 2025.  _(VSAA; PwC)_
- **11. Solidarity tax on above-cap income** — Income above the EUR 105,300 cap is subject to solidarity tax at an effective 25%; full 34.09% is withheld during the year and VID reconciles to 25%.  _(lexfinance.lv; PwC; VSAA)_
- **12. National minimum wage 2025** — National minimum monthly wage for 2025 is EUR 740 gross.  _(Ministry of Welfare)_
- **13. Minimum VSAOI contribution base** — A minimum VSAOI contribution base equal to the minimum wage applies; the employer must top up below-minimum cases, assessed quarterly by VSAA (subject to exemptions).  _(VSAA)_
- **14. Business risk state fee** — The employer pays a business risk state fee of EUR 0.36 per employee per month (flat, employer only; unchanged for 2025 and 2026).  _(VID; Cabinet Regulation; mkd.gov.lv)_
- **15. Filing and payment deadlines** — Employers file the monthly Darba devēja ziņojums (Employer's Report) via VID EDS by the 17th of the following month, and pay PIT + VSAOI + the business risk fee by the 23rd.  _(VID due dates)_
- **16. New employee registration timing** — New employees must be registered with VID at least 1 hour before work starts (electronic, EDS) or 1 day before (paper); status changes / terminations reported within 3 days.  _(VID; EURES; VDI)_
- **17. Late payment interest** — Late payment incurs late-payment interest (nokavējuma nauda) on the overdue amount; commonly cited as 0.05% per day but the current statutory daily rate must be confirmed with VID at filing time. [RESEARCH GAP — confirm current daily rate under the Law On Taxes and Fees with VID.]

## Section 11 -- Tier 2 Catalogue (Reviewer Judgement Required)

**Tier 2 Catalogue table**

| Item | Why it needs reviewer judgement |
| --- | --- |
| Retirement-age VSAOI split (20.77% / 9.25%) | Sourced from MindLink 2025; VSAA emphasises the combined rate. Confirm per-category distribution against the Cabinet Regulation. [RESEARCH GAP] |
| Minimum-contribution exemptions | First-3-months, multiple-employer, disability and student exemptions must be detailed against current statute. [RESEARCH GAP] |
| Ordering of VSAOI vs. non-taxable minimum in the PIT base | Confirm exact statutory sequencing. [RESEARCH GAP] |
| Annual reconciliation of the 33% band | Monthly payroll withholds flat 25.5% (VID); the 33% band on annual income above EUR 105,300 is settled by the individual on the annual income declaration. Confirm any employer reporting touchpoints for high earners. |
| Penalty amounts | EUR 70–1,100 / EUR 140–700 figures are from secondary payroll-guide summaries of the Administrative Liability Law and Labour Law; verify against current statute. [RESEARCH GAP] |
| Solidarity-tax reconciliation mechanics | Confirm timing and mechanism of VID's reconciliation from 34.09% to effective 25%. |
| Benefits-in-kind, business-trip allowances, and special PIT regimes (e.g. micro-enterprise, seasonal workers) | Out of scope of this base skill; reviewer to confirm interaction. [RESEARCH GAP] |
| Solidarity tax and 3% surcharge at the annual stage | These are individual annual-declaration items; confirm employer reporting touchpoints. |

## Section 12 -- Excel Working Paper Template

**Excel Working Paper Template table**

| Column | Content / formula |
| --- | --- |
| A — Employee | Name / personal code (last 4 masked) |
| B — Wage tax book here? | Yes/No |
| C — Pension age? | Yes/No |
| D — Dependants | Count |
| E — Gross | Gross monthly salary (EUR) |
| F — Employee VSAOI rate | 10.50% or 9.25% (from C) |
| G — Employee VSAOI | `=E*F` |
| H — Non-taxable minimum | 510 if B=Yes & not pensioner; 1,000 if pensioner & B=Yes; else 0 |
| I — Allowances | `=D*250` (+ disability/repressed) if B=Yes; else 0 |
| J — PIT base | `=E-G-H-I` |
| K — Monthly PIT withheld @ 25.5% | `=J*0.255` (flat monthly rate — no monthly 33% bracket; the 33% band is annual only) |
| L — Net pay | `=E-G-K` |
| M — Employer VSAOI rate | 23.59% or 20.77% (from C) |
| N — Employer VSAOI | `=E*M` |
| O — Business risk state fee | 0.36 (flat per employee) |
| P — Total employer cost | `=E+N+O` |
| Q — YTD gross | running sum of E (vs. EUR 105,300 annual VSAOI cap / 33% annual band boundary) |
| R — Cap flag | `=IF(Q>105300,"CAP/SOLIDARITY","OK")` |

Add a reconciliation tab summing K (monthly PIT) and G+N (total VSAOI) to tie out to the monthly Darba devēja ziņojums and the EDS payment.

## Section 13 -- Latvian Bank Statement / Terminology Reading Guide

**Terminology Reading Guide table**

| Latvian term | English | Relevance |
| --- | --- | --- |
| Alga / darba alga | Wage / salary | Gross or net salary line |
| Neto alga | Net salary | After deductions |
| Atalgojums | Remuneration | Gross pay |
| IIN (iedzīvotāju ienākuma nodoklis) | Personal income tax | Withheld PIT |
| VSAOI (valsts sociālās apdrošināšanas obligātās iemaksas) | Mandatory state social insurance contributions | Social contributions |
| Solidaritātes nodoklis | Solidarity tax | Above-cap income |
| Neapliekamais minimums | Non-taxable minimum | EUR 510/month (2025) |
| Atvieglojums | Allowance / relief | Dependant / disability allowance |
| Algas nodokļa grāmatiņa | Wage tax book / payroll tax booklet | Gateway for applying minimum + allowances |
| Darba devēja ziņojums | Employer's report | Monthly EDS filing |
| Vienotais nodokļu konts | Single tax account | Where PIT + VSAOI are paid |
| Nokavējuma nauda | Late-payment interest | Penalty (0.05%/day) |
| Apgādājamais | Dependant | For the EUR 250 allowance |
| Minimālā alga | Minimum wage | EUR 740/month (2025) |
| VID | State Revenue Service | Tax authority |
| VSAA | State Social Insurance Agency | Social insurance authority |
| EDS | Electronic Declaration System | Filing portal |

## Section 14 -- Onboarding Fallback

If the engagement is mid-year or records are incomplete: 1. Confirm wage tax book status for each employee with this employer (drives minimum + allowances). If unknown, default to EUR 0 minimum/allowances and flag for correction. 2. Rebuild YTD gross per employee from prior payslips or prior employer's reports to track the EUR 105,300 annual VSAOI cap (also the 25.5%→33% annual PIT band boundary). Monthly withholding stays at a flat 25.5%. 3. Confirm pension-age status for any worker plausibly at or above state pension age (drives 34.09% vs. 30.02%). 4. Check minimum-contribution top-ups for any sub-minimum-wage months; review quarterly VSAA assessments. 5. Reconcile to EDS — pull prior Darba devēja ziņojums filings and single-tax-account payments; tie out PIT and VSAOI. 6. Flag all assumptions and route the reconstructed payroll to a Latvian-licensed accountant before finalising.

If you cannot establish wage tax book status, pension status, or YTD gross, STOP and request them — do not guess.

## Section 15 -- Reference Material

### Filing Obligations (Forms and Deadlines)

**Filing Obligations (Forms and Deadlines)**

**Filing Obligations (Forms and Deadlines)**  _(VID; PwC tax-administration)_

| Form / item | Purpose | Deadline |
| --- | --- | --- |
| Employer's report (Darba devēja ziņojums) | Monthly report to VID/VSAA via EDS declaring each employee's gross income, withheld PIT, and VSAOI (employer + employee shares) | By the **17th** of the month following the reporting month (next working day if a weekend/holiday) |
| PIT + VSAOI payment | Remittance of withheld PIT and total VSAOI to the single tax account | By the **23rd** of the month following the reporting month |
| Employee registration ("Information regarding employees") | Notify VID of a new employee before work starts; report status change/termination | **≥ 1 hour before** work starts (electronic EDS) or **1 day before** (paper); status change/loss within **3 days** |
| Annual income statement / certificate to employee | Employer issues annual income and withheld-tax certificate for the employee's personal declaration | By **1 February** of the following year (on request) |
| Annual income declaration (gada ienākumu deklarācija) | Individual reconciles annual PIT, applies the 33% band and the +3% surtax over EUR 200,000, claims allowances | Filed by the **individual** (not the employer); standard window **1 March – 1 June** of the following year; **1 April – 1 July** if annual income exceeds **EUR 105,300** (VID; PwC tax-administration). |

### Key Thresholds (2025)

**Key Thresholds (2025)**

| Threshold | Value |
| --- | --- |
| PIT band boundary (25.5% → 33%) | EUR 105,300/year — applied at the ANNUAL declaration. Monthly payroll withholds a flat 25.5%; there is no monthly 33% bracket. |
| +3% surtax threshold | EUR 200,000/year total income (annual return only) |
| VSAOI maximum contribution base (cap) | EUR 105,300/year |
| Solidarity tax threshold | Income above EUR 105,300/year |
| Minimum mandatory VSAOI base (employees) | EUR 740/month (= minimum wage); employer tops up shortfall, assessed quarterly |
| Self-employed / voluntary minimum annual VSAOI base | EUR 8,880/year (12 × EUR 740) |
| Business risk state fee | EUR 0.36 per employee per month (employer only; unchanged 2025-2026) |

### Penalties

**Penalties**

| Type | Amount |
| --- | --- |
| Late payment of taxes/contributions | Late interest (nokavējuma nauda) of **0.05% per day** on the overdue amount |
| Administrative fines (payroll/employment violations) | Commonly **EUR 70–1,100** depending on severity. [RESEARCH GAP — verify against current statute] |
| Undeclared employment / unregistered employee | Reported **EUR 140–700** per violation tier, plus assessment of unpaid PIT and VSAOI with interest; repeat/serious cases escalate to higher fines and possible criminal liability. [RESEARCH GAP — verify against current statute] |

### Sources

- VID — Personal Income Tax rates: https://www.vid.gov.lv/en/personal-income-tax-rates
- VSAA — On contributions (VSAOI rates): https://www.vsaa.gov.lv/en/contributions-0
- Ministry of Finance — Non-taxable minimum and tax allowances: https://www.fm.gov.lv/en/non-taxable-minimum-and-tax-allowances
- Ministry of Finance — Changes in taxation and finances from 2025: https://www.fm.gov.lv/en/changes-taxation-and-finances-2025
- PwC Worldwide Tax Summaries — Latvia (Other taxes / social security): https://taxsummaries.pwc.com/latvia/individual/other-taxes
- PwC Worldwide Tax Summaries — Latvia (Taxes on personal income): https://taxsummaries.pwc.com/latvia/individual/taxes-on-personal-income
- MindLink — National social insurance rates: https://mindlink.lv/useful/national-social-insurance-rates
- Lex & Finance — Latvia's New PIT System in 2025: https://www.lexfinance.lv/en/blogs/latvias-new-personal-income-tax-pit-system-in-2025
- Ministry of Welfare — Minimum wage 2025/2026: https://www.lm.gov.lv/en/article/minimum-wage-latvia-will-be-780-euros
- VID — Solidarity Tax: https://www.vid.gov.lv/en/solidarity-tax
- VID — Due dates for filing returns and paying taxes: https://www.vid.gov.lv/en/due-dates-filing-returns-and-paying-taxes
- VID — Electronic Declaration System (EDS): https://www.vid.gov.lv/en/electronic-declaration-system-eds
- VID — Uzņēmējdarbības riska valsts nodeva (business risk state fee): https://www.vid.gov.lv/lv/uznemejdarbibas-riska-valsts-nodeva
- mkd.gov.lv — Business risk state fee unchanged at 36 cents in 2025: https://www.mkd.gov.lv/lv/jaunums/uznemejdarbibas-riska-valsts-nodeva-2025gada
- PwC Worldwide Tax Summaries — Latvia (Tax administration; annual declaration deadlines): https://taxsummaries.pwc.com/latvia/individual/tax-administration
- VSAA — Tax-exempt minimum for pensions in 2025: https://www.vsaa.gov.lv/en/article/application-tax-exempt-minimum-amount-pensions-2025
- KPMG Latvia — Amendments to the Law "On Taxes and Fees" (late-payment interest, Sept 2025): https://kpmg.com/lv/en/home/insights/2025/09/amendments-to-the-law-on-taxes-and-fees.html
- KPMG Baltics — Tax Card Latvia 2025: https://assets.kpmg.com/content/dam/kpmg/lv/pdf/Taxcard/Tax_card_Latvia_2025_.pdf [RESEARCH GAP — PDF itself not machine-parsed; the figures it would corroborate (25.5%/33%, VSAOI 23.59%/10.50%, EUR 105,300 cap, EUR 510 minimum, EUR 740 minimum wage, EUR 0.36 fee) have been independently confirmed against VID, PwC, VSAA, FM and Cabinet/Ministry sources above.]

### Tax-Year Boundary Warning

Several official pages (VSAA contributions, FM allowances) were re-published in late Dec 2025 / Jan 2026 and now display **2026** figures. The following 2026 values must NOT be used for a 2025 computation:
- Minimum wage EUR 780/month (2025 = **EUR 740**)
- Standard non-taxable minimum EUR 550/month (2025 = **EUR 510**)

The pensioner non-taxable minimum is **EUR 1,000/month (EUR 12,000/year) in both 2025 and 2026** (Ministry of Finance), so it is NOT a 2025-vs-2026 difference. (Note: some older guides quoted EUR 500/month for 2025; the authoritative Ministry of Finance figure used here is EUR 1,000/month.)

### Test Suite

Use these to self-check any implementation of this skill (2025 figures):

1. **Standard, wage tax book, EUR 2,000, no dependants** → employee VSAOI 210.00; PIT base 1,280.00; PIT 326.40; net 1,463.60; employer VSAOI 471.80; + business risk fee 0.36 → total employer cost 2,472.16. (Example 1.)
2. **Same EUR 2,000, NO wage tax book** → minimum = 0; PIT base 1,790.00; PIT 456.45; net 1,333.55. (Example 2.)
3. **EUR 1,500, wage tax book, one dependant** → VSAOI 157.50; PIT base 582.50; PIT 148.54; net 1,193.96. (Example 3.)
4. **Minimum wage EUR 740, wage tax book** → VSAOI 77.70; PIT base 152.30; PIT 38.84; net 623.46; no top-up due at exactly EUR 740. (Example 4.)
5. **Retirement age EUR 1,800, wage tax book** → employee VSAOI @ 9.25% = 166.50; pensioner minimum 1,000; PIT base 633.50; PIT 161.54; net 1,471.96; employer VSAOI @ 20.77% = 373.86; + business risk fee 0.36. (Example 5.)
6. **High earner EUR 10,000, wage tax book** → employee VSAOI 1,050.00; PIT base 8,440.00; monthly PIT withheld @ flat 25.5% = 2,152.20; net 6,797.80. (Example 6.)
7. **Flat-monthly-rate check** — confirm monthly payroll withholds 25.5% on the taxable base regardless of monthly amount; the 33% band and +3% surtax are NOT applied in monthly payroll (annual income declaration only). Reject any implementation that applies a 33% rate at a "EUR 8,775/month" threshold — no such monthly bracket exists.
8. **Cap check** — confirm VSAOI stops accruing once YTD gross exceeds EUR 105,300, with above-cap income flagged for solidarity-tax treatment.
9. **Business risk fee check** — EUR 0.36 per employee per month is added to total employer cost only (not withheld from the employee, not a percentage of pay), for both 2025 and 2026.
10. **VSAOI sum check** — confirm 23.59% + 10.50% = 34.09% (standard) and 20.77% + 9.25% = 30.02% (pension-age).
11. **Filing check** — Darba devēja ziņojums due by the 17th; payment (PIT + VSAOI + business risk fee) by the 23rd of the following month.
12. **Registration check** — new employee registered ≥ 1 hour before work starts (electronic).
13. **Late-interest check** — late-payment interest accrues per day on overdue amounts (commonly cited as 0.05%/day; confirm the current rate with VID — see RESEARCH GAP).
14. **2025-vs-2026 guard** — reject EUR 780 minimum wage and EUR 550 standard non-taxable minimum as out-of-year for 2025; the pensioner non-taxable minimum is EUR 1,000/month in BOTH years.

## Section 16 -- Interaction with Other Skills

**Interaction with Other Skills**

| Scenario | Skill to Use |
| --- | --- |
| Employee payroll (PIT withholding + VSAOI) | **This skill (latvia-payroll.md)** |
| Self-employed / business-activity income tax | latvia-income-tax.md (when available) |
| Latvia VAT (PVN) returns | latvia-vat-return.md (when available) |
| Latvia bookkeeping | latvia-bookkeeping.md (when available) |
| Employer corporate income tax | latvia-corporate-tax.md (when available) |

### Key Handoff Points

- **Payroll → Bookkeeping:** Gross wages and employer VSAOI are expenses; withheld PIT and employee VSAOI are liabilities until remitted to the single tax account.
- **Payroll → Income Tax:** The annual income statement issued to the employee feeds their personal annual income declaration, where the 33% bracket and 3% surcharge are reconciled.
- **Payroll → Social Insurance:** VSAOI paid through payroll counts toward the employee's pension and social entitlements; the EUR 105,300 cap and solidarity-tax mechanism govern high earners.

## PROHIBITIONS

- **Non-taxable minimum without wage tax book** — NEVER apply the non-taxable minimum (EUR 510) or any allowance unless the employee's wage tax book (algas nodokļa grāmatiņa) is filed with THIS employer.
- **No 2026 figures for 2025 computation** — NEVER use 2026 figures (EUR 780 minimum wage, EUR 550 minimum, EUR 1,000 pensioner minimum) for a 2025 computation.
- **VSAOI computed on gross** — NEVER compute VSAOI on net or post-PIT salary — VSAOI is on gross before PIT.
- **No 33% rate in monthly payroll** — NEVER apply the 33% rate in monthly payroll — monthly withholding is a flat 25.5%; the 33% band (annual income above EUR 105,300) is settled only on the annual income declaration. There is no monthly EUR 8,775 PIT bracket.
- **No surtax/solidarity in monthly payroll** — NEVER apply the +3% surtax or the solidarity-tax reconciliation in monthly payroll — these are annual / VID-driven.
- **Retirement-age VSAOI split confirmation** — NEVER use the retirement-age VSAOI split (20.77% / 9.25%) without confirming pension-age status.
- **Minimum VSAOI base for sub-minimum-wage employees** — NEVER ignore the minimum VSAOI contribution base for sub-minimum-wage employees.
- **Business risk state fee inclusion** — NEVER omit the business risk state fee (EUR 0.36 per employee per month) from total employer cost.
- **Filing/payment deadlines** — NEVER miss the Darba devēja ziņojums deadline (17th) or the payment deadline (23rd) — late interest of 0.05%/day applies.
- **VID registration before employment starts** — NEVER start an employee without VID registration (≥ 1 hour before work, electronic).
- **Estimated computations disclaimer** — NEVER present payroll computations as definitive — always label as estimated and direct to a Latvian-licensed accountant.

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a Latvian-licensed accountant) before implementation. This is a Tier 2 research-verified skill and has NOT yet been signed off by a licensed accountant.

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
