---
name: iceland-payroll
description: Use this skill whenever asked about Iceland payroll processing for employed persons. Trigger on phrases like "Iceland payroll", "Icelandic payroll", "staðgreiðsla", "PAYE Iceland", "withholding Iceland", "tryggingagjald", "social security contribution Iceland", "persónuafsláttur", "personal tax credit Iceland", "lífeyrissjóður", "mandatory pension Iceland", "séreignarsparnaður", "supplementary pension", "launagreiðendaskrá", "employer registry Iceland", "RSK 5.02", "launamiði", "skilagreining", "net salary Iceland", "tax withholding Iceland", "employer social cost Iceland", "kjarasamningur", "minimum wage Iceland", "municipal income tax Iceland", "gross to net Iceland", "salary calculation Iceland", or any question about computing employee pay, withholding income tax (state + municipal), or social contributions for Iceland-based employees. This skill covers PAYE (staðgreiðsla) income tax withholding, the personal tax credit, employer social security contribution (tryggingagjald), mandatory occupational pension (employee 4% + employer 11.5%), supplementary private pension, no statutory minimum wage (collective-agreement minimums), and filing obligations to Skatturinn. ALWAYS read this skill before processing any Iceland payroll.
version: 0.1
jurisdiction: IS
tax_year: 2025
last_updated: 2026-07-13
review_status: pending_review
depends_on: - payroll-workflow-base
category: payroll
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Iceland Payroll

## Iceland Payroll Skill v0.1

Tier 2 (research-verified). Core 2025 figures (tax brackets, personal tax credit, tryggingagjald) are drawn directly from Skatturinn (Iceland Revenue and Customs) key-rates and tax-bracket pages and corroborated by PwC Worldwide Tax Summaries. The state-vs-municipal split of each bracket is approximate (Skatturinn publishes only the COMBINED withholding rate); the exact late-payment surcharge on staðgreiðsla/tryggingagjald and the minimum-wage figures (which are NOT statutory) are flagged as research gaps below. An Iceland-registered accountant must confirm against the official Skatturinn rate tables and the applicable collective agreement (kjarasamningur) before sign-off.

## Section 1 -- Quick Reference

**Quick Reference**

| Field | Value |
| --- | --- |
| Country | Iceland (Ísland) |
| Currency | ISK only |
| Standard pay frequency | Monthly (most common) |
| Tax year | Calendar year (1 January -- 31 December) |
| Tax withholding system | PAYE -- "staðgreiðsla": employer withholds combined state + municipal income tax monthly on the period's pay, then deducts the personal tax credit (Lög nr. 45/1987 um staðgreiðslu opinberra gjalda) |
| Income tax structure | Progressive, COMBINING a state income tax and a municipal income tax into three combined withholding brackets |
| Tax authority | Skatturinn (Iceland Revenue and Customs / Directorate of Internal Revenue) -- https://www.skatturinn.is/english/ |
| Social-insurance financing | tryggingagjald (employer social security contribution), collected by Skatturinn |
| Pension authority | Mandatory occupational pension funds (lífeyrissjóðir) under Lög nr. 129/1997 |
| Key legislation | Lög nr. 90/2003 um tekjuskatt (Income Tax Act); Lög nr. 45/1987 um staðgreiðslu opinberra gjalda (PAYE/withholding); Lög nr. 113/1990 um tryggingagjald (Social Security Contribution Act); Lög nr. 129/1997 um skyldutryggingu lífeyrisréttinda (Mandatory Pension Insurance Act) |
| Filing portal | Skatturinn service portal (thjonusta.skatturinn.is) / island.is |
| Validated by | Pending -- requires sign-off by an Iceland-registered accountant |
| Skill version | 0.1 |

This skill's PRIMARY tax year is 2025. Officially-confirmed 2026 figures (Skatturinn) are noted alongside where they differ, but DO NOT use the 2026 figures for a 2025 pay period.

## Section 2 -- Income Tax Withholding (PAYE / staðgreiðsla)

Iceland levies personal income tax that COMBINES a **state income tax** and a **municipal income tax**. The employer withholds the combined tax monthly under "staðgreiðsla": it applies the three-bracket schedule to the period's taxable base, then subtracts the employee's monthly **personal tax credit (persónuafsláttur)** (Lög nr. 45/1987; Skatturinn tax brackets 2025).

There are **no marital-status / married-vs-single scales** in Iceland — the same progressive scale and the same per-person credit apply to every individual. Unused personal credit is carried forward within the year and up to 100% transferable to a spouse (Skatturinn).

### Combined Withholding Bracket Table -- 2025 (per MONTH of taxable income)

**Combined Withholding Bracket Table -- 2025**  _(Skatturinn, "Tax brackets 2025" and "Key rates and amounts 2025")_

| Bracket | Monthly taxable income (ISK) | Combined rate | Tax on band (ISK) | Cumulative tax at top of band (ISK) |
| --- | --- | --- | --- | --- |
| 1 | 0 -- 472,005 | 31.49% | 148,634.37 | 148,634.37 |
| 2 | 472,006 -- 1,325,127 | 37.99% | 324,101.05 | 472,735.42 |
| 3 | over 1,325,127 | 46.29% | -- | (472,735.42 + 46.29% of excess over 1,325,127) |

Cumulative recomputed: 472,005 × 31.49% = 148,634.37; bracket-2 band width 1,325,127 − 472,005 = 853,122 × 37.99% = 324,101.05 (→ 472,735.42 cumulative at top of bracket 2). The combined rate = state component + municipal component (see split below). The personal tax credit is applied AFTER computing this gross tax.

### State / municipal split of each bracket (approximate)

**State / municipal split of each bracket (approximate)**  _(PwC Worldwide Tax Summaries (state/municipal split))_

| Bracket | Combined | State component (approx) | Municipal component (withholding average) |
| --- | --- | --- | --- |
| 1 | 31.49% | ~16.55% | 14.94% |
| 2 | 37.99% | ~23.05% | 14.94% |
| 3 | 46.29% | ~31.35% | 14.94% |

Skatturinn publishes only the COMBINED rate, so the state-component figures are APPROXIMATE. Withholding always uses the 14.94% average municipal rate; the **final assessed municipal rate ranges 12.44%–14.94% by municipality** and is trued up at the annual assessment (Skatturinn; PwC). Using the maximum municipal rate at withholding avoids under-withholding.

### Personal tax credit (persónuafsláttur)

**Personal tax credit (persónuafsláttur)**  _(Skatturinn)_

| Year | Per month (ISK) | Per year (ISK) | Source |
| --- | --- | --- | --- |
| 2025 | 68,691 | 824,288 | Skatturinn "Key rates and amounts 2025" |
| 2026 | 72,492 | 869,898 | Skatturinn "Key rates and amounts 2026" |

Available to residents aged 16+. The monthly figure × 12 (824,292 for 2025; 869,904 for 2026) differs by a few ISK from Skatturinn's published annual figure (824,288 / 869,898) — Skatturinn publishes both independently; use the monthly figure for monthly withholding and the annual figure at year-end assessment. Unused credit carries forward within the year and up to 100% transfers to a spouse (Skatturinn).

### PAYE Computation Method (staðgreiðsla)

- **PAYE computation steps** — 1. Start from gross remuneration for the period. 2. Deduct the employee's mandatory pension contribution (4%) — it is deductible from the income-tax base (PwC). This gives the taxable base. 3. Apply the combined bracket table to the taxable base to get gross monthly income tax. 4. Subtract the monthly personal tax credit (persónuafsláttur). If gross tax < credit, income tax withheld = 0 and the unused credit carries forward within the year (or transfers to a spouse). 5. The result is the income tax withheld for the period; net pay = gross − pension − income tax.  _(PwC)_

Iceland's staðgreiðsla applies the schedule to each period's pay (not a full-year cumulative projection like UK PAYE); the annual assessment (álagning) trues up state/municipal differences and any unused/over-used credit.

## Section 3 -- Social Contributions -- Employee Deductions

The only mandatory employee deduction besides income tax is the **mandatory occupational pension (lífeyrissjóður)** at **4%** minimum. There is **no employee tryggingagjald** — the social security contribution is employer-only.

### Employee Contribution Rates (2025)

**Employee Contribution Rates (2025)**  _(PwC Worldwide Tax Summaries — Iceland Individual: Other taxes)_

| Contribution | Rate | Base | Floor | Ceiling | Notes |
| --- | --- | --- | --- | --- | --- |
| Mandatory pension (employee) | 4% (minimum) | Total wages | none | none | Withheld by employer; **deductible** from the income-tax base (PwC) |
| Supplementary private pension (séreignarsparnaður) -- OPTIONAL | up to 4% | Wages | none | none | Voluntary; **deductible**; employer commonly matches up to 2% under collective agreements (PwC) |
| **Total mandatory employee deduction (pension)** | **4%** | -- | -- | -- | Plus PAYE income tax on top |

Sources: PwC Worldwide Tax Summaries — Iceland Individual: Other taxes. The 4% mandatory employee pension is the statutory minimum under Lög nr. 129/1997; collective agreements (kjarasamningar) may set a higher rate — confirm per the applicable agreement.

> Iceland has NO employee-side social security tax. tryggingagjald (Section 4) is paid solely by the employer.

## Section 4 -- Social Contributions -- Employer Contributions

Employers pay (a) the social security contribution **tryggingagjald** and (b) the **employer mandatory pension** (11.5% minimum). tryggingagjald is employer-only with **no floor and no ceiling**.

### Employer Contribution Rates (2025)

**Employer Contribution Rates (2025)**  _(Skatturinn "Key rates and amounts" 2025 & 2026; PwC Corporate: Other taxes; PwC Individual: Other taxes; Lög nr. 129/1997)_

| Contribution | Rate | Base | Floor | Ceiling | Who |
| --- | --- | --- | --- | --- | --- |
| tryggingagjald (general rate) | 6.35% | Total gross remuneration (wages, salaries, benefits, calculated remuneration of self-employed) | none | none | Employer only |
| Mandatory pension (employer) | 11.5% (minimum) | Total wages | none | none | Employer |
| **Total standard employer load** | **17.85%** | -- | -- | -- | -- |

Arithmetic check (employer column): 6.35% + 11.5% = 17.85%.

### tryggingagjald rate variants

**tryggingagjald rate variants**  _(Skatturinn 2025/2026; PwC Corporate: Other taxes)_

| Variant | Rate | Applies to | Source |
| --- | --- | --- | --- |
| General rate | 6.35% | All standard employment | Skatturinn 2025/2026; PwC |
| Fishermen / seamen surcharge | +0.65% (≈7.00% total) | Gross wages of seamen | PwC Corporate: Other taxes |
| A1 (posted EEA worker) reduced rate | 0.425% | Gross wages where worker covered under an A1 certificate in the home country | PwC Corporate: Other taxes |

Several EOR/payroll-vendor blogs cite 6.85% or 6.90% for tryggingagjald — these appear stale or to aggregate sub-components. The authoritative **6.35%** general rate (Skatturinn 2025 & 2026; PwC) is used throughout this skill.

### Combined Employer + Employee Snapshot (standard case)

**Combined Employer + Employee Snapshot (standard case)**  _(Lög nr. 129/1997)_

| Party | Components | Rate of gross |
| --- | --- | --- |
| Employee | Mandatory pension 4% | 4% (+ PAYE income tax) |
| Employer | tryggingagjald 6.35% + mandatory pension 11.5% | 17.85% |
| **Total pension (employee + employer)** | 4% + 11.5% | **15.5% minimum** (Lög nr. 129/1997) |

### Employer pension contributions taxable to the employee

- **Employer pension taxable threshold** — Employer pension contributions become taxable income to the employee only where they exceed BOTH 12% of remuneration AND ISK 2,000,000 per year (PwC). Below either threshold they are tax-free to the employee.  _(PwC)_

## Section 5 -- Minimum Wage and Hiring Mechanics

### Minimum Wage -- there is NO statutory minimum wage

Iceland has **no statutory minimum wage**. Minimum pay is set by **collective bargaining agreements (kjarasamningar)** covering approximately 88–90% of the workforce.

**Minimum wage table**  _(Secondary (Playroll / VR union))_

| Item | Value | Source |
| --- | --- | --- |
| Statutory minimum wage | None — set by collective agreement | (no statute) |
| Lowest negotiated full-time monthly minimum (2025, approx) | ISK 425,985 – 454,977 depending on agreement/sector (e.g. SGS / Efling / VR) | Secondary (Playroll / VR union) — **[RESEARCH GAP — reviewer to confirm]** against the specific kjarasamningur |

Always confirm the applicable collective agreement (kjarasamningur) — it varies by union/sector and updates mid-contract via wage-drift clauses. Do NOT treat the figure above as a fixed statutory floor.

### Hiring and Registration

**Hiring and Registration**  _(Skatturinn)_

| Step | Detail | Authority |
| --- | --- | --- |
| Employer registration | Register on the employer registry (launagreiðendaskrá) via **form RSK 5.02** at least **8 days before** the first wage payment / start of operations | Skatturinn |
| VAT registration (if relevant) | Register if turnover exceeds ISK 2,000,000 per 12 months (standard VAT 24% / reduced 11%) — **[RESEARCH GAP — reviewer to confirm]** the ISK 2,000,000 figure against Skatturinn VAT pages (secondary source) | Skatturinn |

There is no minimum employee count or wage threshold for payroll registration — withholding and tryggingagjald apply from the first wage payment.

## Section 6 -- Other Taxable / Special Categories

**Other Taxable / Special Categories**  _(Skatturinn 2025 / PwC / island.is)_

| Category | Treatment | Source |
| --- | --- | --- |
| Capital income (interest, dividends, capital gains, rent) | Flat **22%**. ISK 300,000 per person of interest/dividend income from regulated securities is tax-free; 50% of residential rental income is tax-free (max two properties) | Skatturinn 2025 |
| Children born 2010 or later | Annual income exceeding **ISK 180,000** taxed at a flat **6%** (no personal credit) | Skatturinn 2025 |
| Non-resident directors'/committee members' fees | **20% state + 14.94% municipal = 34.94%** | PwC |
| RÚV broadcasting fee | ISK 21,400 (2025) levied annually on individuals with income above ISK 2,474,942 — collected via the tax ASSESSMENT, **not** payroll withholding | Skatturinn / island.is |

Capital income, the broadcasting fee and self-employed calculated remuneration are NOT processed through this employer-payroll skill except where they affect an employee's overall position.

## Section 7 -- Conservative Defaults

- **Conservative defaults when inputs missing/ambiguous** — 1. Combined withholding rates. Use 31.49% / 37.99% / 46.29% (state + 14.94% average municipal) on monthly taxable income bands 0–472,005 / 472,006–1,325,127 / over 1,325,127 ISK. The final municipal rate varies 12.44%–14.94% by municipality; withholding ALWAYS uses 14.94% and the true-up happens at the annual assessment, so under-withholding is avoided. 2. tryggingagjald = 6.35% general rate. Confirmed by Skatturinn 2025 & 2026 and PwC. Ignore the higher 6.85%/6.90% figures from EOR blogs (likely stale/aggregated). Apply the 0.65% seamen surcharge or 0.425% A1 rate only when the engagement confirms those facts. 3. Mandatory pension = 4% employee + 11.5% employer (minimum 15.5%). Actual rate may be higher under the applicable collective agreement — confirm per kjarasamningur. 4. Pension is deductible before income tax. Deduct the 4% employee pension from gross before applying the bracket table. 5. Personal tax credit. Apply the full monthly persónuafsláttur (ISK 68,691 for 2025) to the PRIMARY employer only; carry forward of unused credit within the year is allowed. Do not over-credit across multiple employers. 6. Year-correct figures. Use 2025 brackets and credit (68,691/mo) for 2025 pay periods; use the 2026 figures (brackets at 498,122 / 1,398,450; credit 72,492/mo) only for 2026 pay periods. 7. No statutory minimum wage. Do not assume a floor; flag that minimum pay depends on the collective agreement.  _(Skatturinn 2025 & 2026; PwC)_

### Required Inputs (refuse to finalise a payroll run without these)

**Required Inputs**

| Input | Why needed |
| --- | --- |
| Pay period and pay date (and calendar year) | Determines whether 2025 or 2026 brackets/credit apply |
| Gross remuneration for the period (and annualised) | Base for the bracket calc and all contributions |
| Employee residency/age status (resident 16+?) | Determines entitlement to the personal tax credit |
| Whether this is the employee's PRIMARY employer | Personal credit applies to the primary employer only; avoids over-crediting |
| Mandatory pension rate per collective agreement | 4% is the statutory minimum; the agreement may set higher |
| Unused personal-credit carry-forward (and any spouse transfer) | Adjusts the credit actually applied |
| Sector facts (seaman? A1-certificated posted worker?) | Selects the tryggingagjald variant (7.00% / 0.425%) |
| kennitala (national ID) / employer registration on launagreiðendaskrá | Required to withhold and file |

### Refusal Catalogue (stop and ask, do not guess)

- **Refusal Catalogue** — - Pay date year unknown → refuse; cannot choose 2025 vs 2026 brackets/credit. - Personal-credit status unknown / multiple employers → flag; apply the full monthly credit only to the confirmed primary employer. - Mandatory pension rate not confirmed → default to the 4%/11.5% statutory minimum and flag that the collective agreement may be higher. - Seaman / A1 status claimed without evidence → default to the 6.35% general tryggingagjald rate; do not silently apply 7.00% or 0.425%. - Employer not registered on launagreiðendaskrá → refuse to run payroll; registration (RSK 5.02) is required at least 8 days before the first wage payment. - Capital income / self-employed calculated remuneration → out of scope for this employer-payroll skill; redirect.

## Section 9 -- Transaction / Payment Pattern Library

Deterministic classification of Iceland bank-statement lines. Icelandic and English descriptors both appear.

### Salary Credits (employee side)

**Salary Credits (employee side)**

| Pattern (statement text) | Classification |
| --- | --- |
| LAUN, ÚTBORGUÐ LAUN, MÁNAÐARLAUN, SALARY, PAYROLL | Net salary payment |
| EMPLOYER [name] / VINNUVEITANDI, WAGES | Net salary payment |
| BÓNUS, BONUS, DESEMBERUPPBÓT, ORLOFSUPPBÓT | Bonus / holiday & December supplement (taxable) |
| ENDURGREIÐSLA SKATTS, TAX REFUND | Income-tax true-up refund — not current income |

### Employer Debits (employer side)

**Employer Debits (employer side)**

| Pattern (statement text) | Classification |
| --- | --- |
| SKATTURINN STAÐGREIÐSLA, STAÐGREIÐSLA, PAYE | Income tax (staðgreiðsla) remittance to Skatturinn |
| TRYGGINGAGJALD, SKATTURINN TRYGGINGAGJALD | Employer social security contribution remittance |
| LÍFEYRISSJÓÐUR, PENSION FUND, [fund name] | Mandatory + supplementary pension remittance to the pension fund |
| SÉREIGN, SÉREIGNARSPARNAÐUR | Supplementary private pension remittance |
| STÉTTARFÉLAG, FÉLAGSGJALD, UNION | Union dues withheld and remitted |
| LAUNAGREIÐSLA, SALARY RUN, PAYROLL BATCH | Salary disbursement to employees |

Income tax (staðgreiðsla) and tryggingagjald are remitted together to Skatturinn on the same monthly cycle; pension contributions are remitted separately to the relevant pension fund(s). Confirm the actual split with the employer's payment records.

## Section 10 -- Worked Examples

All examples use 2025 brackets, the 2025 personal credit (ISK 68,691/month), the statutory minimum pension (4% employee / 11.5% employer) and the general tryggingagjald rate (6.35%). The 4% employee pension is deducted before the income-tax base. Figures recomputed end-to-end; rounding to the cent (ISK shown to 2 dp for transparency — in practice rounded to whole ISK).

### Example 1 -- Standard monthly employee, ISK 600,000/month

**Example 1 table**

| Step | Amount (ISK) |
| --- | --- |
| Gross monthly remuneration | 600,000.00 |
| Employee mandatory pension 4% | 24,000.00 |
| Taxable base = 600,000 − 24,000 | 576,000.00 |
| Gross tax: 472,005 × 31.49% (148,634.37) + (576,000 − 472,005) × 37.99% (103,995 × 37.99% = 39,507.71) | 188,142.08 |
| Less personal tax credit | 68,691.00 |
| **Income tax withheld** | **119,451.08** |
| **Net pay** = 600,000 − 24,000 − 119,451.08 | **456,548.93** |

Employer cost: tryggingagjald 6.35% (38,100.00) + employer pension 11.5% (69,000.00) = 107,100.00; total employer outlay = 600,000 + 107,100 = **707,100.00/month**.

### Example 2 -- Lower earner, ISK 400,000/month (bracket 1 only)

**Example 2 table**

| Step | Amount (ISK) |
| --- | --- |
| Gross monthly remuneration | 400,000.00 |
| Employee mandatory pension 4% | 16,000.00 |
| Taxable base = 400,000 − 16,000 | 384,000.00 |
| Gross tax: 384,000 × 31.49% (all in bracket 1) | 120,921.60 |
| Less personal tax credit | 68,691.00 |
| **Income tax withheld** | **52,230.60** |
| **Net pay** = 400,000 − 16,000 − 52,230.60 | **331,769.40** |

Employer cost: tryggingagjald 25,400.00 + employer pension 46,000.00 = 71,400.00; total employer outlay = **471,400.00/month**.

### Example 3 -- Top-bracket earner, ISK 1,800,000/month

**Example 3 table**

| Step | Amount (ISK) |
| --- | --- |
| Gross monthly remuneration | 1,800,000.00 |
| Employee mandatory pension 4% | 72,000.00 |
| Taxable base = 1,800,000 − 72,000 | 1,728,000.00 |
| Gross tax — bracket 1: 472,005 × 31.49% | 148,634.37 |
| Gross tax — bracket 2: 853,122 × 37.99% | 324,101.05 |
| Gross tax — bracket 3: (1,728,000 − 1,325,127) = 402,873 × 46.29% | 186,489.91 |
| Total gross tax | 659,225.33 |
| Less personal tax credit | 68,691.00 |
| **Income tax withheld** | **590,534.33** |
| **Net pay** = 1,800,000 − 72,000 − 590,534.33 | **1,137,465.67** |

Employer cost: tryggingagjald 114,300.00 + employer pension 207,000.00 = 321,300.00; total employer outlay = **2,121,300.00/month**.

### Example 4 -- Near collective-agreement minimum, ISK 450,000/month

**Example 4 table**

| Step | Amount (ISK) |
| --- | --- |
| Gross monthly remuneration | 450,000.00 |
| Employee mandatory pension 4% | 18,000.00 |
| Taxable base = 450,000 − 18,000 | 432,000.00 |
| Gross tax: 432,000 × 31.49% (bracket 1) | 136,036.80 |
| Less personal tax credit | 68,691.00 |
| **Income tax withheld** | **67,345.80** |
| **Net pay** = 450,000 − 18,000 − 67,345.80 | **364,654.20** |

ISK 450,000 sits within the approximate 2025 collective-minimum band (ISK 425,985–454,977) — **[RESEARCH GAP — reviewer to confirm]** against the applicable kjarasamningur. Employer cost: tryggingagjald 28,575.00 + employer pension 51,750.00 = 80,325.00; total employer outlay = **530,325.00/month**.

### Example 5 -- Low earner where the credit fully absorbs the tax, ISK 220,000/month

**Example 5 table**

| Step | Amount (ISK) |
| --- | --- |
| Gross monthly remuneration | 220,000.00 |
| Employee mandatory pension 4% | 8,800.00 |
| Taxable base = 220,000 − 8,800 | 211,200.00 |
| Gross tax: 211,200 × 31.49% | 66,506.88 |
| Less personal tax credit (66,506.88 < 68,691) | 68,691.00 |
| **Income tax withheld** (cannot go below 0) | **0.00** |
| Unused credit carried forward within the year | 2,184.12 |
| **Net pay** = 220,000 − 8,800 − 0 | **211,200.00** |

When gross tax is below the personal credit, no income tax is withheld and the unused credit (here 2,184.12) carries forward within the year or transfers to a spouse.

### Example 6 -- Child (born 2010 or later) flat-6% case

Annual income of ISK 500,000 earned by a child born in 2012 → taxed at a flat **6% with no personal credit** = 500,000 × 6% = **ISK 30,000** (Skatturinn 2025). The 6% applies to income above the ISK 180,000 annual threshold; **[RESEARCH GAP — reviewer to confirm]** whether the 6% applies to the whole amount or only the excess over 180,000 in the year in question.

## Section 11 -- Tier 1 Rules (deterministic — apply directly)

- **Tier 1 Rules 1-18** — 1. Income tax is withheld monthly under staðgreiðsla, combining a state and a municipal income tax (Lög nr. 45/1987; Skatturinn). 2. 2025 combined withholding brackets (monthly taxable income): 31.49% on 0–472,005; 37.99% on 472,006–1,325,127; 46.29% above 1,325,127 ISK (Skatturinn "Tax brackets 2025"). 3. Withholding uses the average municipal rate 14.94%; the final assessed municipal rate ranges 12.44%–14.94% by municipality and is trued up at the annual assessment (Skatturinn; PwC). 4. 2025 personal tax credit (persónuafsláttur) = ISK 68,691/month (ISK 824,288/year), deducted from monthly gross tax for residents 16+; unused credit carries forward within the year and up to 100% transfers to a spouse (Skatturinn). 5. The 4% employee mandatory pension is deducted from gross BEFORE computing the income-tax base (PwC; conservative default). 6. Employer social security contribution (tryggingagjald) general rate = 6.35% of total gross remuneration, employer-only, no floor and no ceiling (Skatturinn 2025 & 2026; PwC). 7. tryggingagjald adds 0.65% for fishermen/seamen (≈7.00% total) and has a reduced 0.425% component for A1-certificated posted EEA workers (PwC). 8. Mandatory occupational pension: minimum 15.5% of wages = 4% employee (withheld, deductible) + 11.5% employer; collective agreements may set higher employer rates (Lög nr. 129/1997; PwC). 9. Optional supplementary private pension (séreignarsparnaður): employee may contribute up to 4% (deductible); employers commonly match up to 2% under collective agreements (PwC). 10. Employer pension contributions become taxable to the employee only where they exceed BOTH 12% of remuneration AND ISK 2,000,000/year (PwC). 11. Capital income (interest, dividends, gains, rent) is taxed at a flat 22%; ISK 300,000/person of interest/dividend income from regulated securities is tax-free; 50% of residential rental income is tax-free (max two properties) (Skatturinn 2025). 12. Iceland has NO statutory minimum wage; minimum pay is set by collective agreements covering ~88–90% of workers (verify the applicable kjarasamningur). 13. Employers must register on launagreiðendaskrá via form RSK 5.02 at least 8 days before the first wage payment / start of operations (Skatturinn). 14. Monthly PAYE return (skilagreining) and tryggingagjald are reported and paid by the 15th of the month following the wage month (Skatturinn; Lög nr. 45/1987). 15. Under-withholding identified at the annual assessment is collected increased by 2.5% of the difference; over-withholding is refunded (PwC Individual: Tax administration). 16. Children born 2010 or later are taxed at a flat 6% on annual income exceeding ISK 180,000, with no personal credit (Skatturinn 2025). 17. Non-resident directors'/committee members' fees are taxed at 20% state + 14.94% municipal = 34.94% (PwC). 18. The individual annual return (framtal) is due 14 March of the year following the tax year; the final assessment (álagning) is generally completed by 31 May (PwC; Skatturinn).  _(Lög nr. 45/1987; Skatturinn; PwC; Lög nr. 129/1997)_

## Section 12 -- Tier 2 Catalogue (reviewer judgement required)

**Tier 2 Catalogue**

| Topic | Judgement call |
| --- | --- |
| Applicable collective agreement (kjarasamningur) | Which agreement/sector applies, the actual minimum wage, and any higher mandatory pension rate. **[RESEARCH GAP — reviewer to confirm]** the specific agreement. |
| State/municipal split & municipality rate | The employee's municipality of residence sets the final municipal rate (12.44%–14.94%); the state-component split is approximate (PwC). True-up at assessment. |
| Personal-credit allocation | Allocation of the personal credit across multiple employers / spouse transfer / carry-forward within the year. |
| Supplementary pension match | Whether the employer matches séreignarsparnaður (commonly up to 2%) and the deductibility position. |
| Employer pension >12% / >ISK 2m test | Whether employer pension contributions cross BOTH thresholds and become taxable to the employee. |
| Benefits in kind | Valuation of non-cash benefits in the tryggingagjald and income-tax base. **[RESEARCH GAP — reviewer to confirm]** current BIK valuation rules. |
| Late-payment surcharge | The exact álag and dráttarvextir on overdue staðgreiðsla / tryggingagjald. **[RESEARCH GAP — reviewer to confirm]** the current percentage under Lög nr. 45/1987 / Skatturinn. |
| Seaman / A1 status | Whether the 7.00% seamen surcharge or the 0.425% A1 reduced rate applies. |

## Section 13 -- Excel Working Paper Template

**Excel Working Paper Template columns**

| Column | Formula / source |
| --- | --- |
| A. Employee name | input |
| B. kennitala (national ID) | input |
| C. Pay date / period | input (drives 2025 vs 2026 rules) |
| D. Primary employer? (Y/N) | input (controls personal credit) |
| E. Monthly gross remuneration | input |
| F. Employee mandatory pension 4% | = E × 4% (or agreement rate) |
| G. Taxable base | = E − F |
| H. Gross income tax | = bracket function on G (2025 or 2026 table) |
| I. Personal tax credit applied | = if D = Y then MIN(H, 68,691) else 0 (2025) / 72,492 (2026), adjusted for carry-forward |
| J. Income tax withheld | = MAX(H − I, 0) |
| K. Unused credit carry-forward | = MAX(I_entitlement − H, 0) |
| L. Monthly net pay | = E − F − J |
| M. Employer tryggingagjald | = E × 6.35% (or 7.00% seamen / 0.425% A1) |
| N. Employer mandatory pension 11.5% | = E × 11.5% (or agreement rate) |
| O. Supplementary pension (employee/employer) | = optional per agreement |
| P. Total employer cost | = E + M + N + (employer O) |

Build the bracket function (column H) as a nested IF or a lookup against the correct year's table from Section 2. Always recompute the cumulative band tax from the table — do not hard-code per-employee tax. The 14.94% withholding municipal rate is baked into the combined bracket rates; the assessment true-up is handled by Skatturinn, not the working paper.

## Section 14 -- Iceland Payslip / Statement Reading Guide

Iceland payslips (launaseðill) and bank statements mix Icelandic and English. Common terms:

**Term glossary**

| Term (Icelandic / English) | Meaning |
| --- | --- |
| Laun / Mánaðarlaun / Salary | Gross or monthly salary |
| Staðgreiðsla / Withholding tax | Income tax withheld (combined state + municipal) |
| Persónuafsláttur / Personal tax credit | Monthly credit deducted from gross tax (ISK 68,691 in 2025) |
| Tryggingagjald / Social security contribution | Employer-only 6.35% (does not appear as an employee deduction) |
| Lífeyrissjóður / Pension fund | Mandatory pension (4% employee / 11.5% employer) |
| Séreign / Séreignarsparnaður / Supplementary pension | Voluntary private pension (up to 4% employee, employer often matches 2%) |
| Stéttarfélag / Félagsgjald / Union dues | Union membership fee withheld |
| Orlof / Orlofsuppbót / Holiday allowance | Vacation pay / holiday supplement |
| Desemberuppbót / December bonus | Annual December supplement (taxable) |
| Kennitala / National ID | 10-digit identifier for the employee/employer |
| Útborguð laun / Net pay | Take-home pay after pension and tax |

## Section 15 -- Onboarding Fallback

If you cannot establish enough to compute payroll, gather in this order and stop where blocked: 1. Calendar year + pay date — selects 2025 vs 2026 brackets and credit. 2. Monthly gross remuneration + whether any December/holiday supplement or bonus applies. 3. Residency/age status (resident 16+?) — credit entitlement. 4. Primary employer? + any unused credit carry-forward / spouse transfer — credit allocation. 5. Applicable collective agreement — minimum wage and mandatory pension rate (4% may be higher). 6. Sector facts — seaman (7.00% tryggingagjald) or A1-certificated posted worker (0.425%). 7. Employer registration on launagreiðendaskrá (RSK 5.02) — confirm registered before running payroll.

If the engagement turns out to be a self-employed person (reiknað endurgjald / calculated remuneration) or pure capital income, stop: this employer-payroll skill does not cover those.

## Section 16 -- Filing Obligations (Forms)

**Filing Obligations (Forms)**  _(Skatturinn; Lög nr. 45/1987; PwC)_

| Form | Purpose | Deadline |
| --- | --- | --- |
| **RSK 5.02 — Employer registration** | Register on the employer registry (launagreiðendaskrá) and, where relevant, the VAT registry; required before paying first wages | At least 8 days before start of operations / first wage payment (Skatturinn) |
| **Skilagreining staðgreiðslu — monthly withholding/PAYE return** | Report gross wages, withheld income tax and personal credit used per employee; filed via the Skatturinn service portal or payroll system | By the 15th of the month following the wage month (reportable from the 1st) (Skatturinn; Lög nr. 45/1987) |
| **Tryggingagjald — monthly return/payment** | Report and pay the employer social security contribution | Same monthly cycle — by the 15th of the following month, paid together with the withholding (Skatturinn) |
| **Launamiði / staðgreiðsluskýrsla — annual wage statement** | Year-end employee earnings and tax-withheld reconciliation submitted to Skatturinn; feeds the pre-filled individual return | Early in the year following the income year (Skatturinn) |
| **Framtal — individual income tax return** | Annual self-assessment by the employee | By 14 March of the year following the tax year (short extensions up to ~5 days) (PwC; Skatturinn) |

### Key Thresholds

**Key Thresholds**  _(Skatturinn / PwC / island.is)_

| Threshold | Value | Source |
| --- | --- | --- |
| Employer registration | Register on launagreiðendaskrá at least 8 days before the first wage payment / start of operations | Skatturinn launagreiðendaskrá |
| Bracket 1 ceiling (2025) | ISK 472,005/month | Skatturinn "Tax brackets 2025" |
| Bracket 2 ceiling (2025) | ISK 1,325,127/month | Skatturinn "Tax brackets 2025" |
| Personal tax credit (2025) | ISK 68,691/month (ISK 824,288/year) | Skatturinn "Key rates and amounts 2025" |
| Capital income tax-free allowance | ISK 300,000/person on interest & dividends from regulated securities (2025) | Skatturinn 2025 |
| Child flat-6% threshold | Annual income over ISK 180,000 (children born 2010 or later) | Skatturinn 2025 |
| Excess employer-pension taxable threshold | Taxable to employee only if > 12% of remuneration AND > ISK 2,000,000/year | PwC |
| RÚV broadcasting-fee income threshold | Income above ISK 2,474,942 (fee ISK 21,400 for 2025) | Skatturinn / island.is |
| VAT registration | ISK 2,000,000 turnover per 12 months (standard VAT 24% / reduced 11%) — **[RESEARCH GAP — reviewer to confirm]** (secondary source) | Skatturinn / PwC |

### Penalties

**Penalties**  _(Lög nr. 45/1987; Skatturinn; PwC Individual: Tax administration; Grant Thornton)_

| Penalty | Detail | Source |
| --- | --- | --- |
| Late payment of withholding / tryggingagjald | Late-payment surcharge (álag) plus penalty interest (dráttarvextir) accrue from the due date. **[RESEARCH GAP — reviewer to confirm]** the exact current percentage for staðgreiðsla — not confirmed from an authoritative English source in this research. | Lög nr. 45/1987; Skatturinn |
| Year-end assessment shortfall (under-withholding) | The difference between amount withheld and final assessed tax is collected increased by **2.5%** of the difference; over-withholding is refunded. | PwC Individual: Tax administration |
| Late / incorrect individual return | Surcharge (álag) up to 15% may be imposed on an under-reported tax base; reassessment possible for 6 prior years (2 years if returns properly filed). | PwC Individual: Tax administration |
| VAT late payment (comparator) | 1% per day surcharge up to a maximum of 10%, then penalty interest from one month after the due date. | Skatturinn / Grant Thornton (secondary) |

## Section 17 -- Interaction with Other Skills

**Interaction with Other Skills**

| Scenario | Skill to Use |
| --- | --- |
| Employee payroll (staðgreiðsla + tryggingagjald + pension) | **This skill (iceland-payroll.md)** |
| Self-employed income tax / calculated remuneration (reiknað endurgjald) | iceland self-employed / income-tax skill |
| Iceland VAT returns | iceland-vat skill |
| Iceland bookkeeping | iceland-bookkeeping skill |
| Employer corporate tax | iceland-corporate-tax skill |

### Key Handoff Points

- **Payroll → Bookkeeping:** Gross wages, employer tryggingagjald and employer pension are expenses; withheld income tax (staðgreiðsla) and employee pension are liabilities until remitted to Skatturinn / the pension fund.
- **Payroll → Income Tax:** The launamiði / annual wage statement feeds the employee's pre-filled framtal (due 14 March following year); the assessment trues up the state/municipal split and any unused personal credit.
- **Payroll → Pension:** Mandatory contributions count toward the employee's pension entitlement under Lög nr. 129/1997; supplementary séreignarsparnaður is a separate private account.

## Section 18 -- Reference Material

**Reference Material table**  _(Skatturinn; PwC)_

| Item | Value | Source |
| --- | --- | --- |
| 2025 combined brackets | 31.49% / 37.99% / 46.29% at monthly 472,005 / 1,325,127 | Skatturinn "Tax brackets 2025" |
| State/municipal split (approx) | ~16.55 / 23.05 / 31.35% state + 14.94% municipal (withholding average) | PwC |
| Final municipal rate range | 12.44%–14.94% by municipality (trued up at assessment) | Skatturinn; PwC |
| Personal tax credit 2025 | ISK 68,691/month (ISK 824,288/year) | Skatturinn "Key rates and amounts 2025" |
| Personal tax credit 2026 | ISK 72,492/month (ISK 869,898/year) | Skatturinn "Key rates and amounts 2026" |
| tryggingagjald general | 6.35% employer-only, no ceiling | Skatturinn 2025 & 2026; PwC |
| tryggingagjald seamen | +0.65% (≈7.00% total) | PwC Corporate: Other taxes |
| tryggingagjald A1 reduced | 0.425% | PwC Corporate: Other taxes |
| Mandatory pension | 4% employee + 11.5% employer (min 15.5%) | PwC; Lög nr. 129/1997 |
| Supplementary pension | up to 4% employee (deductible); employer match commonly up to 2% | PwC |
| Capital income tax | flat 22%; ISK 300,000 interest/dividend allowance; 50% rental exemption (max 2 properties) | Skatturinn 2025 |
| Child flat rate | 6% on annual income over ISK 180,000 (born 2010+) | Skatturinn 2025 |
| Non-resident director fee | 34.94% (20% state + 14.94% municipal) | PwC |
| 2026 brackets | same 31.49% / 37.99% / 46.29% at monthly 498,122 / 1,398,450 | Skatturinn "Key rates and amounts 2026" |
| Minimum wage | None statutory; ~ISK 425,985–454,977/month (2025) by collective agreement | Secondary (Playroll / VR) — **[RESEARCH GAP]** |
| VAT | standard 24% / reduced 11%; registration at ISK 2,000,000 turnover | Skatturinn / PwC (secondary for threshold) |

- **2025 combined brackets** — 31.49% / 37.99% / 46.29% at monthly 472,005 / 1,325,127  _(Skatturinn "Tax brackets 2025")_
- **State/municipal split (approx)** — ~16.55 / 23.05 / 31.35% state + 14.94% municipal (withholding average)  _(PwC)_
- **Final municipal rate range** — 12.44%–14.94% by municipality (trued up at assessment)  _(Skatturinn; PwC)_
- **Personal tax credit 2025** — ISK 68,691/month (ISK 824,288/year)  _(Skatturinn "Key rates and amounts 2025")_
- **Personal tax credit 2026** — ISK 72,492/month (ISK 869,898/year)  _(Skatturinn "Key rates and amounts 2026")_
- **tryggingagjald general** — 6.35% employer-only, no ceiling  _(Skatturinn 2025 & 2026; PwC)_
- **tryggingagjald seamen** — +0.65% (≈7.00% total)  _(PwC Corporate: Other taxes)_
- **tryggingagjald A1 reduced** — 0.425%  _(PwC Corporate: Other taxes)_
- **Mandatory pension** — 4% employee + 11.5% employer (min 15.5%)  _(PwC; Lög nr. 129/1997)_
- **Supplementary pension** — up to 4% employee (deductible); employer match commonly up to 2%  _(PwC)_
- **Capital income tax** — flat 22%; ISK 300,000 interest/dividend allowance; 50% rental exemption (max 2 properties)  _(Skatturinn 2025)_
- **Child flat rate** — 6% on annual income over ISK 180,000 (born 2010+)  _(Skatturinn 2025)_
- **Non-resident director fee** — 34.94% (20% state + 14.94% municipal)  _(PwC)_
- **2026 brackets** — same 31.49% / 37.99% / 46.29% at monthly 498,122 / 1,398,450  _(Skatturinn "Key rates and amounts 2026")_
- **Minimum wage** — None statutory; ~ISK 425,985–454,977/month (2025) by collective agreement  _(Secondary (Playroll / VR) — **[RESEARCH GAP]**)_
- **VAT** — standard 24% / reduced 11%; registration at ISK 2,000,000 turnover  _(Skatturinn / PwC (secondary for threshold))_

### Sources

1. Skatturinn (Iceland Revenue and Customs) — Tax brackets 2025 — https://www.skatturinn.is/english/individuals/tax-brackets/2025/
2. Skatturinn — Key rates and amounts 2025 — https://www.skatturinn.is/english/individuals/key-rates-and-amounts/2025/
3. Skatturinn — Key rates and amounts 2026 — https://www.skatturinn.is/english/individuals/key-rates-and-amounts/2026/
4. Skatturinn — Launagreiðendaskrá (employer registry / registration) — https://www.skatturinn.is/atvinnurekstur/ad-hefja-rekstur/launagreidendaskra/
5. Skatturinn — Staðgreiðsla og reiknað endurgjald í atvinnurekstri — https://www.skatturinn.is/atvinnurekstur/stadgreidsla-og-reiknad-endurgjald/
6. PwC Worldwide Tax Summaries — Iceland Individual: Other taxes (pension & social contributions) — https://taxsummaries.pwc.com/iceland/individual/other-taxes
7. PwC Worldwide Tax Summaries — Iceland Corporate: Other taxes (tryggingagjald rates) — https://taxsummaries.pwc.com/iceland/corporate/other-taxes
8. PwC Worldwide Tax Summaries — Iceland Individual: Taxes on personal income (state/municipal split) — https://taxsummaries.pwc.com/iceland/individual/taxes-on-personal-income
9. PwC Worldwide Tax Summaries — Iceland Individual: Tax administration (deadlines, penalties) — https://taxsummaries.pwc.com/iceland/individual/tax-administration
10. Ísland.is (Government of Iceland portal) — Tax on wages and pensions — https://island.is/en/taxes-individuals

### Research Caveats (read before relying on figures)

- Confidence is **high** for the core 2025 payroll mechanics; brackets, personal credit and tryggingagjald are corroborated by Skatturinn AND PwC.
- **tryggingagjald rate:** Skatturinn (2025 & 2026 key rates) and PwC both state the general employer rate is **6.35%**. Several EOR/payroll vendor blogs cite 6.85% or 6.90% — these appear stale or to aggregate sub-components; the authoritative 6.35% is used here.
- **State-vs-municipal split** (16.55 / 23.05 / 31.35% state) is from PwC, Skatturinn publishes only the COMBINED rate, so the state-component figures are approximate and the municipal 14.94% is the withholding average (final municipal rate 12.44%–14.94% by municipality).
- **Minimum wage is NOT statutory.** Figures (≈ISK 425,985–454,977/month for 2025) come from secondary sources (Playroll, VR union) and must be confirmed against the specific applicable collective agreement (kjarasamningur), which varies by union/sector and updates mid-contract.
- The exact current **late-payment surcharge** on withholding tax / tryggingagjald (álag and dráttarvextir under Lög nr. 45/1987) was not confirmed from an authoritative English source — **[RESEARCH GAP — reviewer to confirm]**. The 2.5% under-withholding add-on and the VAT 1%/day-to-10% figures are documented but the staðgreiðsla-specific surcharge needs verification.
- The **VAT registration threshold (ISK 2,000,000)** is from secondary sources and should be confirmed against Skatturinn VAT pages if relevant.
- **Bracket annual figures** are derived by ×12 of the published monthly thresholds (Skatturinn publishes withholding thresholds monthly). The personal credit monthly × 12 (824,292) differs by a few ISK from the published annual (824,288); use the figure appropriate to the calculation.
- **2026 figures** are officially confirmed by Skatturinn and noted, but the skill's primary tax year is 2025.

## Section 19 -- Test Suite

Each test recomputed end-to-end; expected values reconcile to the cent (2025 brackets, credit ISK 68,691/month, 4% employee / 11.5% employer pension, 6.35% tryggingagjald).

- **Bracket-1 band tax** — 472,005 × 31.49% = 148,634.37 (full bracket-1 band tax).  _(Section 19 -- Test Suite)_
- **Bracket-2 cumulative** — Top of bracket 2 = 148,634.37 + (1,325,127 − 472,005) × 37.99% = 148,634.37 + 853,122 × 37.99% (324,101.05) = 472,735.42.  _(Section 19 -- Test Suite)_
- **Standard employee net** — Gross 600,000 → pension 24,000; base 576,000; gross tax 188,142.08; less credit 68,691 → income tax 119,451.08; net 456,548.93.  _(Section 19 -- Test Suite)_
- **Lower earner** — Gross 400,000 → pension 16,000; base 384,000; gross tax 120,921.60; less credit → income tax 52,230.60; net 331,769.40.  _(Section 19 -- Test Suite)_
- **Top bracket** — Gross 1,800,000 → pension 72,000; base 1,728,000; gross tax 148,634.37 + 324,101.05 + (1,728,000 − 1,325,127) × 46.29% (186,489.91) = 659,225.33; less credit → income tax 590,534.33; net 1,137,465.67.  _(Section 19 -- Test Suite)_
- **Credit fully absorbs tax** — Gross 220,000 → pension 8,800; base 211,200; gross tax 66,506.88 < credit 68,691 → income tax 0.00; unused credit carried forward 2,184.12; net 211,200.00.  _(Section 19 -- Test Suite)_
- **Employer load** — Gross 600,000 → tryggingagjald 6.35% = 38,100.00; employer pension 11.5% = 69,000.00; total employer cost 707,100.00.  _(Section 19 -- Test Suite)_
- **tryggingagjald is employer-only** — A 600,000 gross employee has NO tryggingagjald deduction on the employee side — the only employee deduction besides income tax is the 4% pension (24,000.00).  _(Section 19 -- Test Suite)_
- **Pension is deductible before tax** — Gross 400,000 → taxable base is 384,000 (after 4% pension), NOT 400,000 — gross tax computed on 384,000.  _(Section 19 -- Test Suite)_
- **Total pension minimum** — Employee 4% + employer 11.5% = 15.5% of wages (statutory minimum, Lög nr. 129/1997).  _(Lög nr. 129/1997)_
- **Non-resident director** — Fee ISK 1,000,000 → 1,000,000 × 34.94% = 349,400.00 (20% state + 14.94% municipal).  _(Section 19 -- Test Suite)_
- **Child flat rate example** — Child born 2012, annual income 500,000 → 500,000 × 6% = 30,000.00 (no personal credit). [RESEARCH GAP] whether 6% applies to the whole amount or only the excess over ISK 180,000.  _(Section 19 -- Test Suite)_
- **2026 bracket switch** — A pay period dated 15 Jan 2026 uses the 2026 brackets (bracket-1 ceiling 498,122) and the 2026 credit (72,492/month), NOT the 2025 figures.  _(Section 19 -- Test Suite)_
- **Registration refusal** — Employer not on launagreiðendaskrá → refuse to run payroll; RSK 5.02 registration is required at least 8 days before the first wage payment.  _(Section 19 -- Test Suite)_

## PROHIBITIONS

- **No tryggingagjald as employee deduction** — NEVER add tryggingagjald as an EMPLOYEE deduction — it is employer-only (6.35%); the only mandatory employee deduction besides income tax is the 4% pension.  _(PROHIBITIONS)_
- **Pension deductible before tax** — NEVER compute income tax on gross before deducting the 4% mandatory pension — pension is deductible from the income-tax base.  _(PROHIBITIONS)_
- **No stale tryggingagjald rate** — NEVER use a tryggingagjald rate other than 6.35% (general) without confirmed seaman (7.00%) or A1 (0.425%) status — ignore the stale 6.85%/6.90% EOR figures.  _(PROHIBITIONS)_
- **Personal credit single employer** — NEVER apply the full personal tax credit to more than one employer — it goes to the primary employer only; carry forward unused credit within the year.  _(PROHIBITIONS)_
- **No statutory minimum wage assumption** — NEVER assume a statutory minimum wage — Iceland has none; minimum pay depends on the applicable collective agreement (kjarasamningur).  _(PROHIBITIONS)_
- **Withholding municipal rate not final** — NEVER use the average 14.94% municipal rate as the FINAL rate — it is the withholding rate; the assessed rate (12.44%–14.94%) is trued up at assessment.  _(PROHIBITIONS)_
- **No cross-year bracket mixing** — NEVER use the 2025 brackets/credit for a 2026 pay period (or vice versa).  _(PROHIBITIONS)_
- **Filing deadline** — NEVER miss the 15th-of-following-month deadline for the staðgreiðsla return and tryggingagjald — surcharge and interest apply.  _(PROHIBITIONS)_
- **No unverified surcharge percentage** — NEVER state an unverified late-payment surcharge percentage — it is a documented research gap; direct the user to confirm with Skatturinn / the statute.  _(PROHIBITIONS)_
- **Estimated computations disclaimer** — NEVER present payroll computations as definitive — always label as estimated and direct to an Iceland-registered accountant.  _(PROHIBITIONS)_

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a registered accountant in Iceland) before implementation.

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
