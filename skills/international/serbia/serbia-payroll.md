---
name: serbia-payroll
description: Use this skill whenever asked about Serbia payroll processing for employed persons. Trigger on phrases like "Serbia payroll", "Serbian payroll", "obracun zarade", "zarada", "salary tax Serbia", "porez na zarade", "social contributions Serbia", "doprinosi", "PIO Serbia", "PPP-PD", "ePorezi payroll", "CROSO", "M obrazac", "net salary Serbia", "neto zarada", "bruto na neto", "gross to net Serbia", "employer cost Serbia", "minimum wage Serbia", "minimalna zarada", "non-taxable amount Serbia", "neoporezivi iznos", or any question about computing employee pay, salary withholding tax, or mandatory social insurance contributions for Serbia-based employees. This skill covers the 10% flat salary tax on the gross-minus-non-taxable base, the 35.05% combined social insurance contributions (employee 19.9% + employer 15.15%), contribution floors/ceilings, minimum wage, statutory non-taxable benefits, the supplementary annual personal income tax (PP-GPDG), and filing on the consolidated PPP-PD return via ePorezi. ALWAYS read this skill before processing any Serbia payroll.
version: 0.1
jurisdiction: RS
tax_year: 2025
last_updated: 2026-07-13
review_status: pending_review
depends_on: - payroll-workflow-base
category: payroll
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Serbia Payroll

## Serbia Payroll Skill v0.1

> **Tier 2 — Research-verified.** Rates and structure are cross-verified across PwC Worldwide Tax Summaries, Eurofast Tax Card 2025, Orbitax, KPMG Serbia and Forvis Mazars Serbia. Official PURS / Ministry of Finance rulebook PDFs were not directly text-extracted; figures rely on Big-4 and specialist summaries that cite the official Ministry of Finance publications. Every figure below carries an inline source or a `[RESEARCH GAP — reviewer to confirm]` marker. A qualified Serbian tax adviser (poreski savetnik) must validate this skill before production use.

## Section 1 -- Quick Reference

**Quick Reference**

| Field | Value |
| --- | --- |
| Country | Serbia (Republic of Serbia / Republika Srbija) |
| Jurisdiction code | RS |
| Currency | RSD (Serbian dinar) only |
| Standard pay frequency | Monthly |
| Tax year | Calendar year (1 January -- 31 December) |
| Has personal income tax? | Yes -- flat 10% salary tax + supplementary annual PIT for high earners |
| Salary tax | 10% flat on (gross salary − monthly non-taxable amount). Source: Eurofast Tax Card 2025; PwC. |
| Combined social contributions | 35.05% of gross (employee 19.9% + employer 15.15%). Source: PwC Worldwide Tax Summaries; Eurofast Tax Card 2025. |
| Monthly non-taxable amount (2025) | RSD 28,423 (effective 1 Feb 2025 -- 31 Jan 2026). Source: Eurofast; KPMG RS. |
| Monthly non-taxable amount (2026) | RSD 34,221 (adopted Dec 2025). Source: KPMG RS tax alert (Dec 2025); Eurofast. |
| Min monthly contribution base (2025) | RSD 45,950. Source: Orbitax; Eurofast; Mondaq. |
| Max monthly contribution base (2025) | RSD 656,425 (annual max RSD 7,877,100). Source: Orbitax; Eurofast. |
| Tax authority | Tax Administration of the Republic of Serbia (Poreska uprava / PURS) |
| Social insurance registry | Central Registry of Compulsory Social Insurance (CROSO) |
| Filing portal | ePorezi (https://eporezi.purs.gov.rs) -- requires qualified electronic certificate |
| Primary forms | PPP-PD (salary tax + contributions), PP-GPDG (annual PIT), M Form (CROSO registration) |
| Validated by | Pending -- requires sign-off by a qualified Serbian tax adviser |
| Skill version | 0.1 |

## Confidence Tier Definitions

Every rule in this skill is tagged with a confidence tier:

- **[T1] Tier 1 -- Deterministic.** Apply exactly as written. No reviewer judgement required.
- **[T2] Tier 2 -- Reviewer Judgement Required.** Flag the issue and present options. A qualified Serbian tax adviser must confirm before filing.
- **[T3] Tier 3 -- Out of Scope / Escalate.** Skill does not cover this. Do not guess. Escalate and document the gap.

## Section 2 -- Salary Tax (Porez na Zarade)

- **Salary tax overview** — Employment income is taxed at a flat 10% salary tax on the gross salary less a monthly non-taxable amount. The tax is a final withholding tax: the employer computes it, withholds it from the employee, and remits it.  _(Eurofast Tax Card 2025; KPMG RS; Forvis Mazars; PwC.)_

### Salary tax formula [T1]

- **Salary tax formula** — Salary tax = (Gross salary − Monthly non-taxable amount) × 10% - If gross salary is at or below the monthly non-taxable amount, salary tax = 0 (the base cannot go negative). - The non-taxable amount applies to actual gross salary, NOT to the contribution base floor/ceiling (those affect contributions only -- see Section 3).

### Monthly non-taxable amount [T1]

**Monthly non-taxable amount**  _(Eurofast; KPMG RS)_

| Period | Monthly non-taxable amount | Source |
| --- | --- | --- |
| Prior to 1 Feb 2025 | RSD 25,000 | KPMG RS |
| 1 Feb 2025 -- 31 Jan 2026 | **RSD 28,423** | Eurofast; KPMG RS |
| From 1 Jan 2026 (index period Feb 2026) | **RSD 34,221** | KPMG RS tax alert (Dec 2025); Eurofast |

> **Note on the index period.** The non-taxable amount is re-indexed annually with effect from 1 February. RSD 28,423 is the figure for the Feb 2025 -- Jan 2026 cycle. For payrolls dated Feb 2025 through Jan 2026 use RSD 28,423; switch to RSD 34,221 for the 2026 cycle. Source: Eurofast caveat.

## Section 3 -- Social Insurance Contributions (Doprinosi)

- **Social insurance overview** — Total mandatory social insurance contributions are 35.05% of gross salary, split between employee (withheld from gross) and employer (paid on top of gross).  _(PwC Worldwide Tax Summaries; Eurofast Tax Card 2025.)_

### Contribution rate table (2025 and 2026) [T1]

**Contribution rate table**  _(PwC; Eurofast)_

| Contribution class | Employee | Employer | Combined | Base | Source |
| --- | --- | --- | --- | --- | --- |
| Pension & Disability Insurance (PIO) | 14.00% | 10.00% | 24.00% | Gross (floor/ceiling apply) | PwC; Eurofast |
| Health Insurance (zdravstveno) | 5.15% | 5.15% | 10.30% | Gross (floor/ceiling apply) | PwC; Eurofast |
| Unemployment Insurance (osiguranje za slucaj nezaposlenosti) | 0.75% | 0.00% | 0.75% | Gross (employee-only; employer abolished 2019) | PwC; Eurofast |
| **TOTAL** | **19.90%** | **15.15%** | **35.05%** | Gross | PwC; Eurofast |

- **Arithmetic check** — Employee column 14.00 + 5.15 + 0.75 = 19.90%. Employer column 10.00 + 5.15 + 0.00 = 15.15%. Combined column 24.00 + 10.30 + 0.75 = 35.05%. Each component row sums across to its combined value (e.g. 14.00 + 10.00 = 24.00). [T1]
- **No employer unemployment contribution** — There is no employer unemployment contribution -- it was abolished in 2019.  _(PwC; Eurofast)_

### Contribution base floor and ceiling [T1]

**Contribution base floor and ceiling**  _(Orbitax; Eurofast; Mondaq / Zunic Law; DMK)_

| Item | 2025 value | 2026 value | Source |
| --- | --- | --- | --- |
| Minimum monthly contribution base (floor) | RSD 45,950 (35% of avg monthly salary) | RSD 51,297 | Orbitax; Eurofast; Mondaq / Zunic Law; DMK |
| Maximum monthly contribution base (ceiling) | RSD 656,425 (5× avg monthly salary) | RSD 732,820 | Orbitax; Eurofast / Eurofast; TaxRavens |
| Maximum annual contribution base | RSD 7,877,100 (= 656,425 × 12) | [RESEARCH GAP — reviewer to confirm 2026 annual max] | Orbitax (2025) |

- **Arithmetic check** — ceiling RSD 656,425 ≥ floor RSD 45,950 (2025) and 732,820 ≥ 51,297 (2026). Annual max 656,425 × 12 = 7,877,100. [T1]

### How floor/ceiling apply [T1]

- **Floor/ceiling application formula** — Contribution base = MIN( MAX( gross salary, floor ), ceiling ) Employee contributions = Contribution base × 19.90% Employer contributions = Contribution base × 15.15% - If gross < floor (e.g. part-time), contributions are still computed on the floor. - If gross > ceiling, contributions are capped at the ceiling. - Pro-rate the floor for partial months of employment (conservative default). Source: conservative default — exact pro-ration method [RESEARCH GAP — reviewer to confirm].

## Section 4 -- Gross-to-Net Computation Order

- **Gross-to-net computation order** — 1.  Determine gross salary (bruto). 2.  Contribution base = MIN( MAX(gross, floor), ceiling ). 3.  Employee contributions = Contribution base × 19.90%   (withheld from gross). 4.  Salary tax base = MAX(gross − monthly non-taxable amount, 0). 5.  Salary tax = Salary tax base × 10%                     (withheld from gross). 6.  Net pay (neto) = gross − employee contributions − salary tax. 7.  Employer contributions = Contribution base × 15.15%    (paid on top of gross). 8.  Total employer cost = gross + employer contributions   (= gross × 1.1515 when gross is within floor/ceiling).  _(Eurofast Tax Card 2025 (withholding mechanics); employer cost multiplier 1.1515 per Eurofast.)_

> **Conservative default:** treat total employer cash cost as `gross × 1.1515` only when gross sits between the floor and ceiling. When gross is below the floor or above the ceiling, compute employer contributions on the bounded base instead.

## Section 5 -- Conservative Defaults

**Conservative defaults**  _(research conservative_defaults)_

| # | Default assumption |
| --- | --- |
| CD1 | Use the 2025 monthly non-taxable salary amount RSD 28,423 for any payroll dated Feb 2025 -- Jan 2026; switch to RSD 34,221 for the 2026 cycle. |
| CD2 | Apply minimum contribution base RSD 45,950 and maximum RSD 656,425 for all 2025 monthly payrolls; pro-rate the floor for partial months. |
| CD3 | Treat total employer cost as gross × 1.1515 (employer contributions on top of gross) when gross is within the floor/ceiling band. |
| CD4 | Assume the unemployment contribution is employee-only (0.75%); the employer pays no unemployment contribution. |
| CD5 | Assume the employee is a standard resident employee with no special incentive/relief unless told otherwise (new-employee reliefs extended to 31 Dec 2026 — see Section 12). Source: KPMG RS tax alert (Dec 2025). |

## Section 6 -- Required Inputs and Refusal Catalogue

- **Required inputs before computing any payroll** — Ask for any unknown item. Do not compute until items 1--5 are confirmed. 1. Employer PIB (Poreski identifikacioni broj — 9-digit tax ID) and APR company registration. Source: Playroll. 2. Pay period and payment date (the PPP-PD is filed at/before each salary payment — Section 8). 3. Gross salary (bruto) for the period, in RSD. If only a net figure is known, flag CD-net (gross-up required). 4. Employee CROSO registration status (registered via the M Form before commencement of work). Source: Playroll. 5. Whether any contribution/tax relief or incentive applies (e.g. new-employee relief; young/disabled/returnee incentives) [T2]. 6. Employee age and number of dependents (only relevant to the supplementary annual PIT — Section 9) [T2].  _(Playroll)_

### Refusal Catalogue [T1]

**Refusal Catalogue**

| Trigger | Action |
| --- | --- |
| Gross salary not provided (only "net" or "budget") | Flag CD-net; gross-up requires iterative computation — present as estimate only and flag for reviewer [T2]. |
| Employee not registered in CROSO (no M Form) | STOP. Registration must precede employment. Do not compute payroll. Source: Playroll. |
| Payment date / pay period unknown | STOP. PPP-PD timing and the applicable non-taxable amount depend on the date. |
| A relief/incentive is claimed but not documented | Flag [T2]. Do not apply relief without confirming eligibility and the governing rulebook. |
| Income is not employment income (dividends, royalties, rent, capital gains, self-employment) | OUT OF SCOPE for this skill. Escalate to the relevant Serbia skill / adviser [T3]. |
| Supplementary annual PIT base or ordering is ambiguous | Flag [T2] — see Section 9 research-gap note. |

## Section 7 -- Transaction / Payment Pattern Library (Deterministic)

Map bank-statement narrations (typically in Serbian) to payroll classifications. All patterns [T1] unless flagged.

### 7a. Salary credits to the employee's account

**Salary credits**

| Narration pattern (Serbian / common) | Classification |
| --- | --- |
| ZARADA, ISPLATA ZARADE, PLATA, NETO ZARADA | Net salary payment (neto) |
| AKONTACIJA ZARADE | Salary advance (akontacija) — partial net payment |
| ZARADA [month/year], MESECNA ZARADA | Net monthly salary |
| NAKNADA ZARADE (bolovanje) | Salary compensation during sick leave [T2] — confirm payer (employer vs RFZO) |
| REGRES, REGRES ZA GODISNJI ODMOR | Holiday allowance (taxable as part of salary) [T2] |

### 7b. Statutory non-taxable employee benefits (reimbursements)

**Statutory non-taxable employee benefits**  _(research payroll_items)_

| Narration pattern | Classification | Non-taxable cap (2025) | Source |
| --- | --- | --- | --- |
| DNEVNICA, DNEVNICE (domace) | Domestic per diem | up to RSD 3,380/day | research payroll_items |
| PREVOZ, NAKNADA ZA PREVOZ | Commuting / public transport reimbursement | up to RSD 5,630/month | research payroll_items |
| DOBROVOLJNO PENZIJSKO/ZDRAVSTVENO | Supplementary pension & health plan premiums | up to RSD 8,449/month | research payroll_items |
| JUBILARNA NAGRADA | Anniversary (jubilee) award | RSD 28,152 | research payroll_items |

> Amounts paid above these caps are taxable as salary and bear contributions [T2]. The caps above are for the 2025 cycle; re-index for 2026 [RESEARCH GAP — reviewer to confirm 2026 benefit caps].

### 7c. Employer remittances (debits from the company account)

**Employer remittances**

| Narration pattern | Classification |
| --- | --- |
| POREZ NA ZARADE, PURS POREZ | Salary tax remittance to PURS |
| DOPRINOSI PIO / DOPRINOS ZA PENZIJSKO | Pension (PIO) contributions remittance |
| DOPRINOSI ZDRAVSTVO / RFZO | Health contributions remittance |
| DOPRINOS NEZAPOSLENOST | Unemployment contribution remittance (employee 0.75% only) |
| PPP-PD, OBJEDINJENA NAPLATA | Consolidated PPP-PD payment (tax + all contributions) |

- **VAT exclusion note** — Salaries, contributions and salary tax are never items on a VAT (PDV) return — keep them out of serbia-vat.  _(serbia-vat.md Step 1a)_

### Forms [T1]

**Forms**  _(PURS; TaxAdvisorSerbia; Playroll)_

| Form | Purpose | Deadline | Portal | Source |
| --- | --- | --- | --- | --- |
| **PPP-PD** | Consolidated individual electronic tax return for withheld salary tax + all social contributions; lists every employee per income payment | Filed on or before the day salary is paid; tax and contributions due no later than the salary payment date | ePorezi (qualified e-certificate required) | PURS; TaxAdvisorSerbia; Playroll |
| **PP-GPDG** | Supplementary annual personal income tax return for high earners (annual income above 3× average annual salary) | 15 May of the year following the income year (e.g. 15 May 2025 for 2025 income); pre-filled by PURS | ePorezi | PwC; Eurofast; Forvis Mazars; KPMG |
| **M Form (CROSO)** | Registration of an employee into compulsory social insurance via the Central Registry | Before the employee starts work | CROSO (croso.gov.rs) | Playroll |

> **PPP-PD timing caveat:** the PPP-PD is filed at/before each salary payment with tax due on payment. The commonly-cited "15th of the following month" relates more to certain other obligations. `[RESEARCH GAP — reviewer to confirm exact PPP-PD timing against current PURS guidance.]` Source: research caveat (5).

### Employer setup sequence [T1]

- **Employer setup sequence** — 1. Register the business with APR (Serbian Business Registers Agency). 2. Obtain a tax ID (PIB) from PURS. 3. Register each employee into compulsory social insurance via CROSO using the M Form before commencement of work.  _(Playroll)_

## Section 9 -- Supplementary Annual Personal Income Tax (Godisnji porez)

- **Supplementary annual PIT overview** — A supplementary annual personal income tax applies only to individuals whose total annual income exceeds 3× the average annual salary. It is separate from the monthly 10% salary tax and is reconciled via the pre-filled PP-GPDG.  _(PwC; Eurofast; Forvis Mazars; KPMG)_

### Average annual salary (income year 2025) [T1]

**Average annual salary**  _(Forvis Mazars)_

| Item | Value | Source |
| --- | --- | --- |
| Average **annual** salary (2024) | RSD 1,813,032 (published by the Republic Statistical Office, 26 Feb 2025) | Forvis Mazars |
| 3× average annual salary (filing threshold) | RSD 5,439,096 | PwC; Eurofast |
| 6× average annual salary (top-band threshold) | RSD 10,878,192 | PwC; Eurofast |

> 2026 annual PIT thresholds (based on the 2025 average salary) will be published in early 2027. `[RESEARCH GAP — reviewer to confirm 2025-income-year thresholds when published.]` Source: research caveat (4).

### Annual PIT bands (2025 income) [T1]

**Annual PIT bands**  _(PwC; Eurofast)_

| Band | Annual income range (2024) | Rate | Source |
| --- | --- | --- | --- |
| 1 | Up to 3× avg = RSD 5,439,096 | 0% (exempt) | PwC; Eurofast |
| 2 | 3×--6× avg = RSD 5,439,096 -- 10,878,192 | 10% | PwC; Eurofast |
| 3 | Above 6× avg = above RSD 10,878,192 | 15% | PwC; Eurofast |

### Annual PIT allowances (2025 income) [T1]

**Annual PIT allowances**  _(Eurofast Tax Card 2025; Forvis Mazars)_

| Allowance | Amount | Source |
| --- | --- | --- |
| Personal allowance | 40% of avg annual salary = RSD 725,213 (= 1,813,032 × 40%) | Eurofast Tax Card 2025; Forvis Mazars |
| Per dependent | 15% of avg annual salary = RSD 271,955 each (= 1,813,032 × 15%) | Eurofast; Forvis Mazars |
| Total allowances cap | 50% of taxable income | Eurofast; Forvis Mazars |
| Young taxpayer relief (under 40 on 31 Dec of tax year) | Additional deduction of 3× avg annual salary (RSD 5,439,096) on employment / self-employment / author income | PwC; Eurofast |

- **Arithmetic check** — 1,813,032 × 40% = 725,213.40 → RSD 725,213. 1,813,032 × 15% = 271,955.40 → RSD 271,955. [T1]

> [RESEARCH GAP — reviewer to confirm] the precise ordering of the annual PIT computation — specifically whether the 0/10/15% bands apply to total annual income before or after deducting the personal/dependent allowances and the young-taxpayer relief. The worked example below applies the bands to income after allowances (the conventional Serbian mechanic) and flags this as [T2].

## Section 10 -- Worked Examples

All figures in RSD. Each example is recomputed end-to-end.

### Example 1 -- Standard salary, RSD 100,000 gross, 2025 cycle [T1]

- Gross = 100,000. Within floor (45,950) and ceiling (656,425) → contribution base = 100,000.
- Employee contributions = 100,000 × 19.90% = **19,900.00**
- Salary tax base = 100,000 − 28,423 = 71,577; salary tax = 71,577 × 10% = **7,157.70**
- **Net pay = 100,000 − 19,900.00 − 7,157.70 = 72,942.30**
- Employer contributions = 100,000 × 15.15% = **15,150.00**
- **Total employer cost = 100,000 + 15,150.00 = 115,150.00** (= 100,000 × 1.1515) ✓

Bank statement: a credit of RSD 72,942.30 narrated `ZARADA 03/2025`.

### Example 2 -- Mid salary, RSD 200,000 gross, 2025 cycle [T1]

- Contribution base = 200,000 (within bounds).
- Employee contributions = 200,000 × 19.90% = **39,800.00**
- Salary tax base = 200,000 − 28,423 = 171,577; salary tax = 171,577 × 10% = **17,157.70**
- **Net pay = 200,000 − 39,800.00 − 17,157.70 = 143,042.30**
- Employer contributions = 200,000 × 15.15% = **30,300.00**
- **Total employer cost = 230,300.00**

### Example 3 -- Below the contribution floor, RSD 40,000 gross (part-time), 2025 [T1]

- Gross 40,000 < floor 45,950 → **contribution base = 45,950** (the floor).
- Employee contributions = 45,950 × 19.90% = **9,144.05**
- Salary tax base uses actual gross: 40,000 − 28,423 = 11,577; salary tax = 11,577 × 10% = **1,157.70**
- **Net pay = 40,000 − 9,144.05 − 1,157.70 = 29,698.25**
- Employer contributions = 45,950 × 15.15% = **6,961.43** (6,961.4250 rounded)
- **Total employer cost = 40,000 + 6,961.43 = 46,961.43**

> Note: contributions are on the floor (45,950) while salary tax is on actual gross (40,000). The two bases differ by design [T1]. Net pay can therefore fall faster than gross for sub-floor wages.

### Example 4 -- Above the contribution ceiling, RSD 800,000 gross, 2025 [T1]

- Gross 800,000 > ceiling 656,425 → **contribution base = 656,425** (the ceiling).
- Employee contributions = 656,425 × 19.90% = **130,628.58** (130,628.5750 rounded)
- Salary tax base = 800,000 − 28,423 = 771,577; salary tax = 771,577 × 10% = **77,157.70**
- **Net pay = 800,000 − 130,628.58 − 77,157.70 = 592,213.72**
- Employer contributions = 656,425 × 15.15% = **99,448.39** (99,448.3875 rounded)
- **Total employer cost = 800,000 + 99,448.39 = 899,448.39**

> Salary tax has no ceiling — it is 10% of (full gross − non-taxable amount). Only contributions are capped. [T1]

### Example 5 -- 2026 cycle, RSD 120,000 gross [T1]

Uses 2026 parameters: non-taxable RSD 34,221; floor RSD 51,297; ceiling RSD 732,820.

- Contribution base = 120,000 (within bounds).
- Employee contributions = 120,000 × 19.90% = **23,880.00**
- Salary tax base = 120,000 − 34,221 = 85,779; salary tax = 85,779 × 10% = **8,577.90**
- **Net pay = 120,000 − 23,880.00 − 8,577.90 = 87,542.10**
- Employer contributions = 120,000 × 15.15% = **18,180.00**
- **Total employer cost = 138,180.00**

### Example 6 -- Supplementary annual PIT, 2025 income RSD 11,000,000, over 40, 1 dependent [T2]

- Income 11,000,000 > 3× threshold (5,439,096) → annual PIT applies. Source: PwC.
- Personal allowance = 725,213; dependent allowance = 271,955; total allowances = 893,659.
- Allowance cap = 50% × 11,000,000 = 5,500,000; 893,659 < cap → full allowances used. [T1]
- Taxable base (income after allowances) = 11,000,000 − 893,659 = 10,106,341.
- Apply bands to the taxable base:
  - Band 1 (0–5,439,096): 0% → 0
  - Band 2 (5,439,096–10,878,192): (10,878,192 − 5,439,096) × 10% = 5,439,096 × 10% = **487,450.80**
  - Band 3 (above 10,878,192): (10,106,341 − 10,878,192) × 15% = 357,325 × 15% = **53,598.75**
- **Annual PIT ≈ 487,450.80 + 53,598.75 = 541,049.55**

> **[T2] / [RESEARCH GAP — reviewer to confirm]** the base ordering (bands on income before vs after allowances) per the Section 9 note. This example applies bands after allowances. The monthly 10% salary tax already paid is separate and is not netted here — confirm interaction with the adviser. Source: research caveat (3)/(4).

## Section 11 -- Minimum Wage

**Minimum wage table**  _(TSG.rs; NNRoad; RS Partners)_

| Period | Net minimum wage per working hour | Indicative monthly (at 174 h) | Source |
| --- | --- | --- | --- |
| 1 Jan -- 30 Sep 2025 | RSD 308/hour (net) | ≈ RSD 53,592 (illustrative, not statutory) | TSG.rs |
| From 1 Oct 2025 | RSD 337/hour (net) — extraordinary 9.4% increase | varies with hours | TSG.rs |
| January 2026 increase | Announced | `[RESEARCH GAP — reviewer to confirm exact 2026 rate]` | research caveat (2) |

> The ~RSD 53,592 monthly figure is illustrative only (308 × 174 = 53,592); the statutory rate is the per-hour net amount, and monthly pay depends on actual working hours. Source: research caveat (2).

## Section 12 -- Tier 1 Rules (Deterministic)

**Tier 1 rules**

| # | Rule | Source |
| --- | --- | --- |
| T1-1 | Salary tax = (gross − monthly non-taxable amount) × 10%, floored at 0. Non-taxable amount RSD 28,423 (Feb 2025–Jan 2026), RSD 34,221 (2026). | Eurofast; KPMG; PwC |
| T1-2 | Combined social contributions = 35.05% of base: employee 19.9% (14% PIO + 5.15% health + 0.75% unemployment), employer 15.15% (10% PIO + 5.15% health). No employer unemployment contribution. | PwC; Eurofast |
| T1-3 | Employee contributions and salary tax are withheld from gross; employer contributions are paid on top. Employer total cash cost = gross × 1.1515 within the floor/ceiling band. | Eurofast |
| T1-4 | Contributions are computed on a base = MIN(MAX(gross, floor), ceiling). 2025: floor RSD 45,950, ceiling RSD 656,425 (annual max RSD 7,877,100). 2026: floor RSD 51,297, ceiling RSD 732,820. | Orbitax; Eurofast; TaxRavens |
| T1-5 | Salary tax has no ceiling; only contributions are capped. The non-taxable amount applies to actual gross, not the contribution base. | derived from Eurofast mechanics |
| T1-6 | Salary tax and all contributions are reported on the consolidated PPP-PD via ePorezi at/before each salary payment; payment due no later than the salary payment date. | PURS; TaxAdvisorSerbia; Playroll |
| T1-7 | Employees must be registered into compulsory social insurance via CROSO (M Form) before commencement of work; the business must hold a PIB and APR registration. | Playroll |
| T1-8 | Self-employed entrepreneurs pay both employee and employer portions (combined 35.05%: PIO 24% + health 10.3% + unemployment 0.75%) on their own base. | PwC; TaxRavens |
| T1-9 | New-employee payroll tax/contribution relief (incentives for newly hired workers) is extended through 31 December 2026. | KPMG RS tax alert (Dec 2025) |

### Context rates (for cross-skill reference; not payroll) [T1]

**Context rates**

| Item | Rate | Source |
| --- | --- | --- |
| Corporate income tax | 15% (flat) | Eurofast Tax Card 2025 |
| Standard VAT (PDV) | 20% (reduced 10%, farmer compensation 8%) | Eurofast; see serbia-vat.md |
| Withholding tax to non-residents | generally 20% (25% to preferential-tax jurisdictions), subject to treaty relief | Eurofast |
| VAT registration threshold | RSD 8,000,000 turnover in prior 12 months (≈ EUR 68k) | Eurofast; see serbia-vat.md |

## Section 13 -- Tier 2 Catalogue (Reviewer Judgement Required)

**Tier 2 catalogue**

| # | Situation | Why it needs judgement | Action |
| --- | --- | --- | --- |
| T2-1 | A payroll relief / incentive is claimed (new-employee, young/disabled/returnee) | Eligibility and the governing rulebook vary; reliefs extended to 31 Dec 2026 but conditions must be met | Confirm eligibility and the specific decree before applying. Source: KPMG RS. |
| T2-2 | Benefit paid above a non-taxable cap (per diem, transport, jubilee, supplementary pension/health) | Excess is taxable salary bearing tax + contributions | Recompute the excess into the salary base; flag. |
| T2-3 | Sub-floor or partial-month employment | Floor pro-ration method not pinned to primary source | Apply CD2 default; flag for adviser. `[RESEARCH GAP]` |
| T2-4 | Supplementary annual PIT base/ordering | Whether bands apply before/after allowances is unconfirmed | Apply Section 9 default; flag. `[RESEARCH GAP]` |
| T2-5 | Holiday allowance (regres) / bolovanje compensation | Payer (employer vs RFZO) and taxability vary | Confirm payer and treatment before classifying. |
| T2-6 | Non-resident / posted / cross-border employee | Treaty, social-security coordination and residency rules apply | Escalate [T3] — outside payroll scope. |
| T2-7 | Net-to-gross gross-up requested | Requires iterative computation; rounding sensitive | Present as estimate; flag for adviser. |

## Section 14 -- Excel Working Paper Template

**Excel working paper template**

| Cell ref | Label | Formula / source |
| --- | --- | --- |
| B1 | Pay period (month/year) | input |
| B2 | Payment date | input — drives non-taxable amount & cycle |
| B3 | Gross salary (bruto) | input |
| B4 | Contribution floor | 45,950 (2025) / 51,297 (2026) |
| B5 | Contribution ceiling | 656,425 (2025) / 732,820 (2026) |
| B6 | Contribution base | `=MIN(MAX(B3,B4),B5)` |
| B7 | Monthly non-taxable amount | 28,423 (Feb25–Jan26) / 34,221 (2026) |
| B8 | Employee contributions (19.9%) | `=ROUND(B6*0.199,2)` |
| B9 | Salary tax base | `=MAX(B3-B7,0)` |
| B10 | Salary tax (10%) | `=ROUND(B9*0.10,2)` |
| B11 | **Net pay (neto)** | `=B3-B8-B10` |
| B12 | Employer contributions (15.15%) | `=ROUND(B6*0.1515,2)` |
| B13 | **Total employer cost** | `=B3+B12` |
| B14 | Total to remit to PURS (tax + all contributions) | `=B8+B10+B12` |

Validation rows: confirm B6 ≥ B4 and B6 ≤ B5; confirm B11 + B8 + B10 = B3.

## Section 15 -- Bank Statement / Terminology Reading Guide

**Terminology guide**

| Serbian term | English | Notes |
| --- | --- | --- |
| zarada | salary / wage | gross unless prefixed "neto" |
| bruto | gross | gross salary |
| neto | net | take-home pay |
| porez na zarade | salary (wage) tax | the 10% withholding |
| doprinosi | contributions | social insurance |
| PIO | pension & disability insurance | penzijsko i invalidsko osiguranje |
| zdravstveno osiguranje | health insurance | 5.15% each side |
| osiguranje za slucaj nezaposlenosti | unemployment insurance | 0.75% employee-only |
| neoporezivi iznos | non-taxable amount | the monthly salary-tax allowance |
| akontacija | advance / instalment | partial salary payment |
| regres | holiday allowance | taxability [T2] |
| dnevnica | per diem | non-taxable up to cap |
| naknada za prevoz | transport reimbursement | non-taxable up to cap |
| jubilarna nagrada | jubilee/anniversary award | non-taxable up to cap |
| obracun zarade | payroll calculation / payslip | the computation sheet |
| PIB | tax identification number | employer ID |

## Section 16 -- Onboarding Fallback

- **Onboarding fallback steps** — If the engagement is mid-year or records are incomplete: 1. No prior PPP-PD filings on hand → request the ePorezi PPP-PD history; reconcile each month's tax + contributions against bank remittances. Do not assume prior months were correct. 2. Net-only history → reconstruct gross via the gross-to-net order (Section 4), iterating; mark all reconstructed grosses as estimates [T2]. 3. Unknown which non-taxable amount applied → key off the payment date of each run (RSD 28,423 for Feb 2025–Jan 2026; RSD 34,221 for 2026). 4. Employee CROSO status unknown → STOP and confirm registration (M Form) before processing; an unregistered employee cannot be lawfully run on payroll. Source: Playroll. 5. Relief/incentive history unclear → default to no relief (CD5), flag [T2], and ask the adviser to confirm eligibility.  _(Playroll)_

## Section 17 -- Reference Material

**Reference Material**  _(Eurofast; PwC; KPMG RS; Orbitax; TaxRavens; Forvis Mazars; TSG.rs; research payroll_items)_

| Item | Value | Source |
| --- | --- | --- |
| Salary tax rate | 10% flat on (gross − non-taxable) | Eurofast; PwC |
| Non-taxable amount 2025 / 2026 | RSD 28,423 / RSD 34,221 | KPMG RS; Eurofast |
| Employee contributions | 19.90% (PIO 14% + health 5.15% + unemployment 0.75%) | PwC; Eurofast |
| Employer contributions | 15.15% (PIO 10% + health 5.15%) | PwC; Eurofast |
| Combined contributions | 35.05% | PwC; Eurofast |
| Contribution floor 2025 / 2026 | RSD 45,950 / RSD 51,297 | Orbitax; Eurofast; TaxRavens |
| Contribution ceiling 2025 / 2026 | RSD 656,425 / RSD 732,820 | Orbitax; Eurofast; TaxRavens |
| Annual max contribution base 2025 | RSD 7,877,100 | Orbitax |
| Average annual salary (2024) | RSD 1,813,032 | Forvis Mazars |
| Annual PIT thresholds (2025 income) | 3× = 5,439,096; 6× = 10,878,192 | PwC; Eurofast |
| Annual PIT rates | 0% / 10% / 15% | PwC; Eurofast |
| Annual PIT personal allowance | RSD 725,213 (40% of avg) | Eurofast; Forvis Mazars |
| Annual PIT per-dependent allowance | RSD 271,955 (15% of avg) | Eurofast; Forvis Mazars |
| Minimum wage 2025 (Jan–Sep / from 1 Oct) | RSD 308 / RSD 337 net per hour | TSG.rs |
| Statutory non-taxable per diem (domestic) | up to RSD 3,380/day | research payroll_items |
| Statutory non-taxable transport | up to RSD 5,630/month | research payroll_items |
| Statutory non-taxable supplementary pension/health | up to RSD 8,449/month | research payroll_items |
| Statutory non-taxable jubilee award | RSD 28,152 | research payroll_items |
| New-employee relief | extended to 31 Dec 2026 | KPMG RS |

### Penalties [T2]

**Penalties [T2]**  _(Playroll guide; ZPPPA mechanism)_

| Violation | Amount / rate | Source |
| --- | --- | --- |
| Legal entity — failure to file/pay payroll (income) tax correctly | Fines up to RSD 150,000 | Playroll guide — `[RESEARCH GAP — confirm exact bands against ZPPPA]` |
| Health insurance contribution failures | RSD 50,000 -- 100,000 | Playroll guide — `[RESEARCH GAP — confirm against contribution law]` |
| Pension (PIO) contribution violations | up to RSD 100,000 | Playroll guide — `[RESEARCH GAP — confirm against contribution law]` |
| Late payment interest | Statutory default interest = NBS reference rate + 10 percentage points on overdue tax/contributions | ZPPPA mechanism — `[RESEARCH GAP — exact current rate not pinned to primary source]` |

### Authorities and legislation

- **Tax Administration (Poreska uprava / PURS)** — purs.gov.rs; filing via ePorezi (https://eporezi.purs.gov.rs).
- **Central Registry of Compulsory Social Insurance (CROSO)** — croso.gov.rs.
- **Ministry of Finance (mfin.gov.rs)**.
- **Law on Personal Income Tax** (Zakon o porezu na dohodak gradjana) — salary tax & annual PIT.
- **Law on Mandatory Social Insurance Contributions** (Zakon o doprinosima za obavezno socijalno osiguranje) — contributions.
- **Labour Law** (Zakon o radu) — minimum wage.
- **Law on Tax Procedure and Tax Administration (ZPPPA)** — penalties and default interest.

### Sources

1. PwC Worldwide Tax Summaries — Serbia, Individual: Other taxes (social security rates), last reviewed 25 Feb 2026. https://taxsummaries.pwc.com/serbia/individual/other-taxes
2. PwC Worldwide Tax Summaries — Serbia, Individual: Taxes on personal income. https://taxsummaries.pwc.com/serbia/individual/taxes-on-personal-income
3. Eurofast — Serbia Tax Card 2025. https://eurofast.eu/wp-content/uploads/2025/02/SerbiaTaxCard_2025-1.pdf
4. Eurofast — Changes in Non-Taxable Amount, Minimum and Maximum Contribution Base in Serbia. https://eurofast.eu/changes-in-non-taxable-amount-minimum-and-maximum-contribution-base-in-serbia/
5. Orbitax — Serbia Social Security Contribution Basis Amounts for 2025. https://orbitax.com/news/country/article/Serbia-Social-Security-Contrib-57687
6. Forvis Mazars Serbia — March 2025 Tax Newsletter (avg annual salary RSD 1,813,032). https://www.forvismazars.com/rs/en/insights/tax-newsletter/march-2025
7. KPMG Serbia — Amendments to Personal Income Tax and Social Security Contributions Adopted (2026 non-taxable RSD 34,221), Dec 2025. https://kpmg.com/rs/en/insights/tax-alerts/2025/12/amendments-to-personal-income-tax-and-social-security-contributions-adopted.html
8. TSG Serbia — Minimum Wage in Serbia, changes from October 2025 (RSD 308 → RSD 337 net/hour). https://tsg.rs/en/newsletter/minimum-wage-in-serbia-changes-from-october-2025-and-employers-obligations/
9. Playroll — How to Run Payroll in Serbia: Employment Taxes & Setup (PPP-PD, CROSO, registration, penalties). https://www.playroll.com/payroll/serbia
10. Tax Administration of the Republic of Serbia (PURS) — E-taxes Information (ePorezi portal). https://purs.gov.rs/en/E-taxes/Information1.html
11. TaxRavens — Social Security Contributions (Doprinosi), Serbia 2026 (bases RSD 51,297 / RSD 732,820). https://taxravens.com/en/serbia/social-contributions

## Section 18 -- Test Suite

Each test states inputs and the recomputed expected output. Reviewers should rerun every figure.

### Test 1 -- Standard salary, 2025 cycle

**Input:** Gross RSD 100,000, paid March 2025.
**Expected:** Contribution base 100,000. Employee contributions 19,900.00. Salary tax base 71,577; salary tax 7,157.70. **Net 72,942.30.** Employer contributions 15,150.00. **Total employer cost 115,150.00.**

### Test 2 -- Mid salary, 2025 cycle

**Input:** Gross RSD 200,000, paid June 2025.
**Expected:** Employee contributions 39,800.00. Salary tax 17,157.70. **Net 143,042.30.** Employer contributions 30,300.00. **Total employer cost 230,300.00.**

### Test 3 -- Below floor (part-time), 2025

**Input:** Gross RSD 40,000, paid May 2025.
**Expected:** Contribution base = floor 45,950. Employee contributions 9,144.05. Salary tax base 11,577; salary tax 1,157.70. **Net 29,698.25.** Employer contributions 6,961.43. **Total employer cost 46,961.43.**

### Test 4 -- Above ceiling, 2025

**Input:** Gross RSD 800,000, paid April 2025.
**Expected:** Contribution base = ceiling 656,425. Employee contributions 130,628.58. Salary tax base 771,577; salary tax 77,157.70. **Net 592,213.72.** Employer contributions 99,448.39. **Total employer cost 899,448.39.**

### Test 5 -- 2026 cycle

**Input:** Gross RSD 120,000, paid March 2026 (non-taxable 34,221; floor 51,297; ceiling 732,820).
**Expected:** Employee contributions 23,880.00. Salary tax base 85,779; salary tax 8,577.90. **Net 87,542.10.** Employer contributions 18,180.00. **Total employer cost 138,180.00.**

### Test 6 -- Salary at the non-taxable amount, 2025

**Input:** Gross RSD 28,423, paid July 2025.
**Expected:** Salary tax base = 0 → **salary tax 0.00.** Gross below floor 45,950 → contribution base = 45,950. Employee contributions 9,144.05. **Net = 28,423 − 9,144.05 − 0 = 19,278.95.** Employer contributions 6,961.43.

### Test 7 -- Supplementary annual PIT [T2]

**Input:** 2024 total income RSD 11,000,000, taxpayer over 40, 1 dependent.
**Expected:** Allowances 725,213 + 271,955 = 893,659 (< 50% cap). Taxable base 10,106,341. Band 2 = 487,450.80; Band 3 = 53,598.75. **Annual PIT ≈ 541,049.55** (flag base-ordering [T2]/[RESEARCH GAP]).

### Test 8 -- Below filing threshold, no annual PIT

**Input:** 2024 total income RSD 4,000,000 (< 3× avg = 5,439,096).
**Expected:** No supplementary annual PIT due. PP-GPDG not required. Source: PwC.

### Test 9 -- Total remittance reconciliation, 2025

**Input:** Gross RSD 100,000 (Test 1).
**Expected:** Total to remit to PURS = employee contributions 19,900.00 + salary tax 7,157.70 + employer contributions 15,150.00 = **42,207.70.** Reported on PPP-PD.

## PROHIBITIONS

- NEVER compute payroll for an employee not registered in CROSO (M Form) — registration must precede employment.
- NEVER apply the contribution floor/ceiling to the salary tax — the non-taxable amount applies to actual gross; only contributions are bounded.
- NEVER charge an employer unemployment contribution — it was abolished in 2019; employer total is 15.15%, not 15.90%.
- NEVER cap the salary tax — only contributions are capped at the ceiling.
- NEVER use the wrong cycle's non-taxable amount — RSD 28,423 for Feb 2025–Jan 2026, RSD 34,221 for 2026; key off the payment date.
- NEVER put salaries, salary tax, or contributions on a VAT (PDV) return — they are out of scope for serbia-vat.
- NEVER apply a relief/incentive without confirming eligibility and the governing rulebook (flag [T2]).
- NEVER treat the illustrative monthly minimum wage (~RSD 53,592) as statutory — the statutory rate is per net working hour.
- NEVER miss the PPP-PD timing — it is filed at/before each salary payment with tax due on the payment date.
- NEVER present payroll computations as definitive — always label as estimated and direct to a qualified Serbian tax adviser.
- NEVER guess any figure marked `[RESEARCH GAP — reviewer to confirm]`.

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a qualified Serbian tax adviser or licensed accountant) before implementation.

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
