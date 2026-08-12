---
name: mozambique-payroll
description: Use this skill whenever asked about Mozambique payroll processing for employed persons. Trigger on phrases like "Mozambique payroll", "IRPS withholding", "IRPS Moçambique", "INSS deduction", "segurança social Moçambique", "PAYE Mozambique", "Form 19", "Modelo 19", "M/19", "tax withholding Mozambique", "salário líquido Moçambique", "net salary Mozambique", "employer INSS Mozambique", "salário mínimo Moçambique", "minimum wage Mozambique", "MAIBOR penalty", "gross to net Mozambique", "non-resident 20% Mozambique", "Lista Nominal", or any question about computing employee pay, income-tax withholding, or social-security contributions for Mozambique-based employees. This skill covers IRPS (income tax) monthly withholding by the employer, INSS social security (employee 3% + employer 4%), the monthly PAYE table, non-resident flat withholding, minimum wage by sector, and filing obligations to the Autoridade Tributária (AT) and INSS. ALWAYS read this skill before processing any Mozambique payroll.
version: 0.1
jurisdiction: MZ
tax_year: 2025
last_updated: 2026-07-13
review_status: pending_review
depends_on: - payroll-workflow-base
category: payroll
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Mozambique Payroll

## Mozambique Payroll Skill v0.1

> **Tier 2 (research-verified) — NOT yet accountant-verified.** Several figures carry `[RESEARCH GAP — reviewer to confirm]` markers. A licensed Mozambican *contabilista* or *técnico de contas* must reconcile those before any output is presented as final. In particular the full **monthly PAYE per-cell deduction matrix** (income band × dependents) and the **exact statutory penalty schedule** are incomplete here.

## Section 1 -- Quick Reference

**Quick Reference table**

| Field | Value |
| --- | --- |
| Country | Mozambique (República de Moçambique) |
| Currency | Metical (MZN / MT) only |
| Standard pay frequency | Monthly (most common) |
| Tax year | Calendar year (1 January -- 31 December) (PwC) |
| Income tax | YES — IRPS (Imposto sobre o Rendimento das Pessoas Singulares), progressive 10%–32%, employer-withheld monthly |
| Tax authority | AT (Autoridade Tributária de Moçambique) |
| Social security authority | INSS (Instituto Nacional de Segurança Social) |
| Resident PAYE | Monthly PAYE table keyed to monthly remuneration × number of dependents (RSM 2025 p.14) |
| Non-resident tax | Flat **20%** final withholding on MZ-source employment income (PwC; RSM 2025 p.14) |
| IRPS PAYE form | **IRPS Form 19 (Modelo M/19)** (RSM 2025 pp.3–4) |
| IRPS PAYE deadline | By the **20th** of the following month (RSM 2025 pp.3–4) |
| INSS return deadline | By the **10th** of the following month (RSM 2025 pp.3–4) |
| Annual Nominal List (Lista Nominal) | By **30 April** each year (RSM 2025 pp.3–4) |
| Key legislation | Código do IRPS; Lei n.º 11/2025 (IRPS reform, eff. 29 Dec 2025); Código Geral Tributário; Lei do INSS; INSS Note n.º 246/INSS/GAB-DG/432/2024 |
| Validated by | Pending -- requires sign-off by a licensed Mozambican accountant |
| Skill version | 0.1 |

## Section 2 -- Income Tax Withholding (IRPS — Imposto sobre o Rendimento das Pessoas Singulares)

Mozambique **does** levy personal income tax on employees. The employer is the **withholding agent**: it deducts IRPS monthly from payroll and remits it monthly to the AT. IRPS is formally **assessed annually** on a progressive 10%–32% scale, but the operative payroll mechanism is the **monthly PAYE table** (RSM 2025 p.14), which approximates the annual scale and is keyed to **monthly remuneration AND the number of dependents (0–4+)**.

The IRPS employment-income brackets (10%–32%) and thresholds were **re-confirmed unchanged by Lei n.º 11/2025** (effective 29 December 2025) (DLA Piper Africa).

### IRPS Annual Progressive Table — residents (PwC, 2024 tax year; unchanged by Lei 11/2025)

**IRPS Annual Progressive Table — residents**  _(PwC — https://taxsummaries.pwc.com/mozambique/individual/taxes-on-personal-income (last reviewed 04 Mar 2026))_

| Annual taxable income (MZN) | Marginal rate | Deduction (MZN) |
| --- | --- | --- |
| 0 – 42,000 | **10%** | — |
| 42,000 – 168,000 | **15%** | 2,100 |
| 168,000 – 504,000 | **20%** | 10,500 |
| 504,000 – 1,512,000 | **25%** | 37,500 |
| Over 1,512,000 | **32%** | 141,540 |

- **Subtract method formula** — tax = annual taxable income × rate − deduction  _(PwC)_

*Continuity note:* the first three bands tie out exactly under the subtract method (at 42,000 → 10%×42,000 = 15%×42,000 − 2,100 = **4,200**; at 168,000 → 15%×168,000 − 2,100 = 20%×168,000 − 10,500 = **23,100**). The 25% and 32% bands as published do **not** tie perfectly at their edges (at 504,000 the 20% formula gives 90,300 but the 25% formula gives 90,300 only if the deduction were 35,700, not 37,500; the published 37,500 yields 88,500). This is a feature of the PwC-published presentation. **[RESEARCH GAP — reviewer to confirm exact 25%/32% deduction constants against the Código do IRPS / AT tables before relying on annual-table results in those bands.]**

### Monthly PAYE table — THE operative payroll mechanism (RSM 2025 p.14)

**Monthly PAYE table (0 dependents)**  _(RSM Mozambique Tax Pocket Guide 2025, p.14 — https://www.rsm.global/mozambique/sites/default/files/media/2025/Mozambique%20Tax%20Pocket%20Guide%202025%20ENG.pdf)_

| Monthly remuneration (MZN) | Marginal rate |
| --- | --- |
| Up to **20,249.99** | **0%** (effective monthly exemption floor) |
| 20,250 – 60,749.99 (band incl. 10%/15%/20% sub-steps) | **10% → 20%** |
| 60,750 – 144,749.99 | **25%** |
| Over **144,750** | **32%** |

- **Deduction at 144,750+ with 0 dependents** — 28,375 MZN (0 dependents)  _(RSM 2025 p.14)_

> **[RESEARCH GAP — reviewer to confirm]** The **full per-cell monthly PAYE deduction matrix** (every income band × every dependent count 0–4+, with its deduction constant) could not be fully transcribed — the published PDF rendered only partial cell values. Reproduce the complete official AT table / RSM p.14 matrix before computing precise monthly withholding in the 10%–20% band. The annual progressive table (above) is the sourced fallback for estimation.

### Non-residents

- **Non-resident flat withholding on MZ-source employment income** — 20%  _(PwC; RSM 2025 p.14)_

This also applies to a resident not present in the country (see residency note) and to income paid to a service provider.

### Other IRPS rates relevant to payroll-adjacent income (RSM 2025 p.15)

**Other IRPS rates relevant to payroll-adjacent income**  _(RSM 2025 p.15)_

| Income type | Rate | Source |
| --- | --- | --- |
| Self-employment / service provision (resident) | **20%** | RSM 2025 p.15 |
| Professional artists and athletes | **10%** | RSM 2025 p.15 |
| Electronic-money agents' commissions; non-resident digital services | **10% final WHT** (new, Lei 11/2025) | DLA Piper Africa |

### Lei n.º 11/2025 changes (effective 29 December 2025)

- **180-day test eliminated** — Eliminates the 180-day physical-presence test; residency now based on primary residence / centre of economic interests / professional activity.  _(DLA Piper Africa — https://www.dlapiperafrica.com/en/mozambique/insights/2026/Changes-to-the-Personal-Income-Tax-Code)_
- **New digital services WHT** — Adds 10% final WHT on digital services and e-money agent commissions.  _(DLA Piper Africa — https://www.dlapiperafrica.com/en/mozambique/insights/2026/Changes-to-the-Personal-Income-Tax-Code)_
- **Brackets unchanged** — Employment-income brackets (10%–32%) and thresholds unchanged.  _(DLA Piper Africa — https://www.dlapiperafrica.com/en/mozambique/insights/2026/Changes-to-the-Personal-Income-Tax-Code)_

### Deduction before taxable income

- **Employee 3% INSS deductible** — The employee's 3% INSS contribution is deductible from gross income for IRPS purposes. The skill therefore computes IRPS on `gross − employee INSS`.  _(PwC)_

## Section 3 -- Social Security (INSS) — Employee + Employer

**INSS rates**  _(INSS Note n.º 246/INSS/GAB-DG/432/2024; RSM 2025 p.16)_

| Party | Rate | Source |
| --- | --- | --- |
| **Employee** | **3%** | INSS Note 246/2024; RSM 2025 p.16 |
| **Employer** | **4%** | INSS Note 246/2024; RSM 2025 p.16 |
| **Total** | **7%** | INSS Note 246/2024; RSM 2025 p.16 |

*Column check:* employee 3% + employer 4% = **7%** total. Tie out.

- **INSS base** — Base: monthly regular remuneration (salary, wages, regular bonuses).  _(RSM 2025 p.16)_
- **Excluded from base** — Meal subsidies; profit-sharing, dividends, holiday pay and similar irregular payments are NOT in the contribution base.  _(RSM 2025 p.16)_
- **No salary floor or ceiling** — No salary floor or ceiling is specified in the authoritative sources — contributions are on full regular remuneration.  _(RSM 2025 pp.16–17)_
- **Employee 3% IRPS-deductible** — Employee's 3% is IRPS-deductible.  _(PwC)_
- **Registration requirement** — Employers must register ALL employees (Mozambican and expat). Expats are exempt only if they prove coverage in another country's scheme (request to INSS required).  _(RSM 2025 pp.16–17)_
- **Expat refund** — Foreign employees can reclaim their 3% if they leave permanently before retirement entitlement; the right expires 1 year after the last contribution.  _(RSM 2025 pp.16–17)_

## Section 4 -- Minimum Wage (sectoral)

Mozambique sets minimum wages by sector — there is no single national figure. The 2025 values were approved by the Council of Ministers on 2 Sept 2025, increases of 2.9%–9%, effective retroactively from 1 July 2025. Selected monthly figures (MZN):

**Sectoral minimum wages 2025**  _(https://clubofmozambique.com/news/mozambique-minimum-wages-increase-2-9-to-9-depending-on-sector-with-retroactive-effect-from-1-july/ and https://www.dlapiperafrica.com/pt/mozambique/insights/2025/Approval-of-New-Minimum-Wages-2025)_

| Sector | Min wage (MZN/month) | Increase | Source |
| --- | --- | --- | --- |
| Agriculture, livestock, hunting, forestry | **6,688** | +5.5% | Club of Mozambique; DLA Piper |
| Fishing (maritime/industrial/semi-industrial) | **6,726.88** | +2.9% | Club of Mozambique; DLA Piper |
| Hotels / tourism | **9,700** | +9% | Club of Mozambique; DLA Piper |
| Non-financial services (general) | **10,310** | +7.8% | Club of Mozambique; DLA Piper |
| Microfinance / micro-insurance | **16,764** | +6.5% | Club of Mozambique; DLA Piper |
| Financial services — banks / insurance | **19,043.61** | +6.5% | Club of Mozambique; DLA Piper |

> The lowest sector minimum (≈**6,688** MZN/month) sits **below** the monthly IRPS 0% PAYE floor (≈**20,250** MZN/month), so most minimum-wage earners owe **no IRPS** but **do pay the 3% INSS**.

## Section 5 -- Conservative Defaults

When an input is missing or ambiguous, apply the conservative assumption (the one that does NOT understate withholding/contributions) and FLAG it for the reviewer.

**Conservative Defaults table**

| Unknown | Conservative default | Why |
| --- | --- | --- |
| Residency status | Treat as **resident** (progressive PAYE table) ONLY if presence/economic-interest evidence supports it; otherwise FLAG. If clearly non-resident, apply flat **20%**. | Lei 11/2025 changed the residency test |
| Number of dependents | Use **0 dependents** if unproven | Fewer dependents → higher withholding → conservative |
| Whether monthly pay ≤ 20,249.99 floor | Apply **0% PAYE** only when clearly at/below the floor | Floor is the published exemption |
| INSS base composition | Include only **regular** remuneration; exclude meal subsidy, profit-share, dividends, holiday pay | RSM 2025 p.16 |
| INSS ceiling | **None** — contribute on full regular remuneration | No ceiling in sources |
| Employee INSS deductibility for IRPS | Always deduct employee **3%** before IRPS base | PwC |
| Expat INSS | Register and contribute **3%/4%** unless foreign-scheme coverage proven | RSM 2025 pp.16–17 |
| Tax year | Default to **2025** table unless date triggers Lei 11/2025 changes (≥ 29 Dec 2025) | Skill tax_year is 2025 |
| Currency | Metical (MZN) | Local currency |

## Section 6 -- Required Inputs + Refusal Catalogue

### Required inputs before computing payroll

- **1. Gross salary** — Gross monthly salary in Meticais (and which components are regular vs irregular).
- **2. Residency status** — Residency status (resident vs non-resident) and supporting evidence.
- **3. Number of dependents** — Number of dependents (0–4+) for the monthly PAYE cell.
- **4. Pay frequency** — Pay frequency (monthly assumed).
- **5. Tax/fiscal year** — Tax/fiscal year (2024/2025 table vs Lei 11/2025 changes from 29 Dec 2025).
- **6. Expat foreign coverage** — Whether the employee is an expat with proven foreign social-security coverage.
- **7. Non-regular pay components** — Confirmation of any non-regular pay components (meal subsidy, profit-share, holiday pay).

### Refusal catalogue — DO NOT compute, refuse and request input

**Refusal catalogue**

| Situation | Action |
| --- | --- |
| No gross salary provided | REFUSE — request salary in Meticais |
| Salary stated in USD/EUR with no MZN conversion and no rate | REFUSE — request MZN figure |
| Request to omit IRPS withholding or INSS to "save money" | REFUSE — both are statutory; escalate to accountant |
| Request to apply resident progressive rates to a clear non-resident (or vice versa) | REFUSE — confirm residency under Lei 11/2025 first |
| Request to include meal subsidy / profit-share in the INSS base | REFUSE — excluded by RSM 2025 p.16; flag |
| Self-employment / service-provider / digital-services income mixed in | REFUSE payroll path — route to the relevant IRPS/WHT treatment (20% / 10%) |
| Definitive "this is your exact tax" assertion requested | REFUSE — outputs are estimates pending accountant sign-off |
| Precise late-filing penalty amount requested | REFUSE the precise figure — penalty schedule is an unconfirmed research gap |

## Section 7 -- Transaction / Payment Pattern Library (deterministic)

Classify bank-statement lines deterministically. Match case-insensitively; longest / most-specific pattern wins.

### Salary credits (money arriving in an employee account)

**Salary credits table**

| Pattern (case-insensitive) | Classification |
| --- | --- |
| `SALARIO`, `ORDENADO`, `VENCIMENTO`, `PAGAMENTO SALARIO` | Net salary payment |
| `TRANSF.* [empresa]`, `CREDITO SALARIO` | Net salary payment |
| `SUBSIDIO REFEICAO`, `SUBS. ALIMENTACAO` | Meal subsidy (excluded from INSS base) |
| `13.* MES`, `SUBSIDIO NATAL` | Year-end / Christmas subsidy (irregular — outside INSS base) |
| `REEMBOLSO INSS`, `DEVOLUCAO INSS` | INSS refund/adjustment — not income |

### Employer debits (money leaving the employer account)

**Employer debits table**

| Pattern | Classification |
| --- | --- |
| `AT`, `IRPS`, `RETENCAO IRPS`, `MODELO 19`, `M/19` | IRPS PAYE remitted to the AT (liability settlement) |
| `INSS`, `SEGURANCA SOCIAL`, `CONTRIBUICAO INSS` | INSS contribution (employer 4% + employee 3%) |
| `PAGAMENTO SALARIOS`, `FOLHA SALARIAL`, `PROCESSAMENTO` | Net wages disbursed to employees |
| `IRPC`, `IMPOSTO RENDIMENTO PESSOAS COLECTIVAS` | Corporate income tax — route to a corporate skill, not payroll |

## Section 8 -- Worked Examples

> Resident examples compute IRPS via the **annual progressive table** (PwC, sourced) on `gross − employee 3% INSS`, then divide by 12 for a monthly estimate. This is an **estimation method**: the operative monthly PAYE per-cell matrix (with dependents) is a research gap, and below the **20,250/month** floor the monthly PAYE table withholds **0%** even where the annualised method would show tax. Where the two diverge, the example shows both and FLAGS it. INSS employee = 3%, employer = 4%, no ceiling. Amounts to the cent.

### Example 1 — Minimum-wage earner (agriculture), below the PAYE floor

**Inputs:** Salary **6,688 MZN/month** (agriculture sector minimum), resident, 0 dependents.

- Monthly pay 6,688 < **20,250** PAYE floor → **IRPS PAYE = 0.00** (operative table).
- INSS employee 3% × 6,688 = **200.64**.
- **Net pay** = 6,688.00 − 0.00 − 200.64 = **6,487.36 MZN**.
- Employer INSS 4% × 6,688 = **267.52**; total employer cost = 6,688.00 + 267.52 = **6,955.52**.

*Bank line example:* `PAGAMENTO SALARIO — JUNHO` credit **6,487.36 MZN**.

### Example 2 — Financial-sector minimum-wage earner, just below the PAYE floor

**Inputs:** Salary **19,043.61 MZN/month** (banks/insurance minimum), resident, 0 dependents.

- Monthly pay 19,043.61 < **20,250** floor → **IRPS PAYE = 0.00** (operative monthly table).
- INSS employee 3% × 19,043.61 = **571.31**.
- **Net pay** = 19,043.61 − 0.00 − 571.31 = **18,472.30 MZN**.

> *Annual-table cross-check (illustrative only):* taxable = (19,043.61 × 12) − (571.31 × 12) = 228,523.32 − 6,855.72 = 221,667.60; annual IRPS = 0.20 × 221,667.60 − 10,500 = 33,833.52; ÷12 ≈ 2,819.46/month. The operative monthly PAYE table withholds **0** at this level because the pay is below the 20,250 floor. **[RESEARCH GAP — reviewer to confirm how the 0% floor reconciles with annual assessment for sub-floor earners.]**

### Example 3 — Mid earner, into the 20% annual band

**Inputs:** Salary **30,000 MZN/month**, resident, 0 dependents.

- INSS employee 3% × 30,000 = **900.00/month** → annual **10,800.00**.
- Annual taxable = (30,000 × 12) − 10,800 = 360,000 − 10,800 = **349,200.00** (20% band: 168,000–504,000).
- Annual IRPS = 0.20 × 349,200 − 10,500 = 69,840.00 − 10,500 = **59,340.00/year**.
- Monthly IRPS estimate ≈ 59,340.00 ÷ 12 = **4,945.00**.
- **Employee deductions** = 4,945.00 + 900.00 = **5,845.00**.
- **Net pay** = 30,000.00 − 5,845.00 = **24,155.00 MZN**.

### Example 4 — Higher earner, 20% band

**Inputs:** Salary **60,000 MZN/month**, resident, 0 dependents.

- INSS employee 3% × 60,000 = **1,800.00/month** → annual **21,600.00**.
- Annual taxable = 720,000 − 21,600 = **698,400.00** (25% band: 504,000–1,512,000).
- Annual IRPS = 0.25 × 698,400 − 37,500 = 174,600.00 − 37,500 = **137,100.00/year**.
- Monthly IRPS estimate ≈ 137,100.00 ÷ 12 = **11,425.00**.
- **Employee deductions** = 11,425.00 + 1,800.00 = **13,225.00**.
- **Net pay** = 60,000.00 − 13,225.00 = **46,775.00 MZN**.

### Example 5 — Top-band earner (32% annual)

**Inputs:** Salary **150,000 MZN/month**, resident, 0 dependents.

- INSS employee 3% × 150,000 = **4,500.00/month** → annual **54,000.00**.
- Annual taxable = 1,800,000 − 54,000 = **1,746,000.00** (over 1,512,000 → 32% band).
- Annual IRPS = 0.32 × 1,746,000 − 141,540 = 558,720.00 − 141,540 = **417,180.00/year**.
- Monthly IRPS estimate ≈ 417,180.00 ÷ 12 = **34,765.00**.
- **Employee deductions** = 34,765.00 + 4,500.00 = **39,265.00**.
- **Net pay** = 150,000.00 − 39,265.00 = **110,735.00 MZN**.

### Example 6 — Non-resident, flat 20%

**Inputs:** MZ-source employment income **60,000 MZN/month**, **non-resident**.

- Non-resident final WHT = 20% × 60,000 = **12,000.00** (no progressive table; flat).
- **Net pay** = 60,000.00 − 12,000.00 = **48,000.00 MZN**.
- INSS still applies if the engagement is INSS-covered employment (3% employee / 4% employer), unless foreign-scheme coverage is proven. **[RESEARCH GAP — reviewer to confirm INSS applicability to a non-resident in this fact pattern.]**

### Example 7 — Employer total cost of a mid earner (30,000 MZN/month)

**Employer total cost table**  _(Example 3)_

| Employer cost item | Computation | Amount (MZN) |
| --- | --- | --- |
| Gross salary | — | 30,000.00 |
| INSS employer 4% | 4% × 30,000.00 | 1,200.00 |
| **Total employer cost** | sum | **31,200.00** |

*Check:* 30,000.00 + 1,200.00 = **31,200.00**. Tie out. (Employer-on-top burden = 1,200.00 = 4.00% of gross — INSS has no ceiling, so this 4% holds at every salary level.)

## Section 9 -- Tier 1 Rules (hard, non-negotiable)

- **1. IRPS withholding and filing** — IRPS is employer-withheld monthly and remitted to the AT via Form 19 (M/19) by the 20th of the following month.  _(RSM 2025 pp.3–4)_
- **2. INSS rate, base and filing** — INSS is employee 3% + employer 4% = 7%, on regular remuneration, no ceiling, filed and paid by the 10th of the following month.  _(INSS Note 246/2024; RSM 2025)_
- **3. Employee INSS deductible before IRPS base** — The employee's 3% INSS is deductible from gross before the IRPS base.  _(PwC)_
- **4. 0% IRPS floor** — Monthly remuneration at or below ≈20,250 MZN withholds 0% IRPS under the operative monthly PAYE table.  _(RSM 2025 p.14)_
- **5. Non-resident flat rate** — Non-residents pay a flat 20% final withholding on MZ-source employment income.  _(PwC; RSM 2025 p.14)_
- **6. Exclusions from INSS base** — Meal subsidies and irregular payments (profit-share, dividends, holiday pay) are excluded from the INSS base.  _(RSM 2025 p.16)_
- **7. Nominal List deadline** — The annual Nominal List (Lista Nominal) is due 30 April.  _(RSM 2025 pp.3–4)_
- **8. Lei 11/2025 residency change** — Lei 11/2025 (eff. 29 Dec 2025) left the 10%–32% employment brackets unchanged but redefined residency (no 180-day test) — confirm residency before choosing the table.  _(DLA Piper Africa)_
- **9. Estimate disclaimer** — Every output is an estimate pending licensed-accountant sign-off.

## Section 10 -- Tier 2 Catalogue (reviewer judgement required)

**Tier 2 Catalogue**

| Question | Why it needs a reviewer |
| --- | --- |
| Full monthly PAYE per-cell deduction matrix (income × dependents) | Published PDF rendered only partial cell values |
| Exact 25%/32% annual deduction constants | Published bracket edges do not tie under subtract method |
| Reconciliation of 0% monthly floor vs annual assessment for sub-floor earners | Monthly table and annual scale diverge |
| Residency determination under Lei 11/2025 | 180-day test removed; now facts-and-circumstances |
| INSS applicability to non-residents / expats | Depends on foreign-scheme coverage proof |
| Exact statutory penalty amounts (late M/19, late INSS) | Not cleanly extractable from primary law |
| Whether a given bonus is "regular" (INSS base) or "irregular" (excluded) | Fact-specific characterisation |
| 2026 INSS rate revision (if any) | Current authoritative figure is the 2024 INSS Note, still in force per RSM 2025 |

## Section 11 -- Excel Working Paper Template

Suggested layout (one row per employee per month):

**Excel Working Paper Template columns**

| Col | Header | Formula / source |
| --- | --- | --- |
| A | Employee name | input |
| B | Resident? (Y/N) | input (drives table choice) |
| C | Dependents (0–4+) | input (drives PAYE cell) |
| D | Gross monthly salary (MZN) | input (regular remuneration) |
| E | Employee INSS 3% | `=D*3%` |
| F | Employer INSS 4% | `=D*4%` |
| G | Below PAYE floor? | `=IF(D<=20249.99,TRUE,FALSE)` |
| H | Annual taxable (resident) | `=MAX(0,(D-E)*12)` |
| I | Annual IRPS (resident) | nested IF on H using PwC deductions (—/2,100/10,500/37,500/141,540) |
| J | Monthly IRPS (resident est.) | `=IF(B="N", D*20%, IF(G, 0, I/12))` |
| K | Employee deductions | `=E+J` |
| L | Net pay | `=D-K` |
| M | Total employer cost | `=D+F` |

- **Resident annual-IRPS formula (column I)** — =IF(H<=42000, H*0.10, IF(H<=168000, H*0.15-2100, IF(H<=504000, H*0.20-10500, IF(H<=1512000, H*0.25-37500, H*0.32-141540))))  _(PwC deductions)_

> The column-J `IF(G,0,...)` 0%-floor shortcut and the resident annual-÷12 estimate are stand-ins for the **operative monthly PAYE matrix**, which must replace them once the full per-cell table is transcribed. **[RESEARCH GAP — reviewer to confirm.]**

## Section 12 -- Bank Statement / Terminology Reading Guide

**Terminology reading guide**

| Portuguese term | English / meaning |
| --- | --- |
| Salário / Ordenado / Vencimento | Salary / wage |
| Folha salarial / Processamento de salários | Payroll / payroll run |
| Retenção na fonte | Withholding at source |
| IRPS | Personal income tax (Imposto sobre o Rendimento das Pessoas Singulares) |
| IRPC | Corporate income tax (Imposto sobre o Rendimento das Pessoas Colectivas) |
| INSS | National Social Security Institute |
| Segurança social | Social security |
| Modelo 19 / M/19 | IRPS PAYE form |
| Lista Nominal | Annual employee nominal roster |
| Subsídio de refeição / alimentação | Meal subsidy (excluded from INSS base) |
| Subsídio de férias | Holiday pay (irregular — excluded from INSS base) |
| Subsídio de Natal / 13.º mês | Christmas / 13th-month subsidy (irregular) |
| Dependentes | Dependents (drives PAYE cell) |
| Salário mínimo | Minimum wage |
| Autoridade Tributária (AT) | Tax authority |
| MAIBOR | Maputo Interbank Offered Rate (drives late-payment interest) |

## Section 13 -- Onboarding Fallback

If the engagement lacks key data:

1. **No prior payroll register available** → request the last 3 months of folhas salariais and INSS/AT (M/19) receipts to back-solve the rates and PAYE cells actually applied.
2. **Unknown dependents** → default **0 dependents**, FLAG; confirm before first remittance.
3. **Unknown residency** → gather presence / economic-interest evidence under Lei 11/2025; do not assume the resident table without it.
4. **Unknown sector / min-wage band** → use the relevant 2025 sectoral figure only as a sanity check, never as the contractual wage; obtain the employee's contract.
5. **Expat employee** → confirm whether foreign-scheme coverage is proven before deciding INSS applicability; request the INSS exemption confirmation if claimed.
6. **Full monthly PAYE matrix needed** → obtain the official AT table / RSM p.14 matrix before computing 10%–20% band withholding precisely.

## Section 14 -- Filing, Forms & Deadlines (RSM 2025 Tax Calendar, pp.3–4)

**Filing, Forms & Deadlines**  _(RSM 2025 pp.3–4)_

| Obligation | Form | Deadline | Source |
| --- | --- | --- | --- |
| **IRPS PAYE & withholding filing/payment** | **IRPS Form 19 (M/19)** | By the **20th** of the following month | RSM 2025 pp.3–4 |
| **INSS return filing & payment** | (INSS return) | By the **10th** of the following month | RSM 2025 pp.3–4 |
| **Employee Nominal List** (annual roster) | Lista Nominal | By **30 April** each year | RSM 2025 pp.3–4 |
| Annual PIT return (where required) | — | (annual; see AT) | RSM 2025 pp.3–4 |

> Two distinct monthly deadlines: **INSS by the 10th**, **IRPS withholding by the 20th** of the following month. Do not conflate them.

## Section 15 -- Penalties (late filing / late payment)

Governed by the Código Geral Tributário and the Fiscal Offences regime (Regime Geral das Infracções Tributárias / RGIT).

**Penalties table**

| Item | Detail | Source |
| --- | --- | --- |
| Late-payment interest | Charged at the **12-month MAIBOR interbank rate + 2% surcharge** | South African Tax Guide / KPMG fiscal-guide summary (secondary) |
| Late payment / non-payment / inadequate records | Additional fines (multas) under the Código Geral Tributário and the Fiscal Offences regime | Código Geral Tributário; RGIT |

> **[RESEARCH GAP — reviewer to confirm]** The exact statutory **fine percentages and monetary amounts** (e.g. specific multas for a late M/19 or a late INSS return) could NOT be confirmed from a clean authoritative source — the primary AT text and the Orbitax page were not retrievable. Read the precise penalty schedule directly from the **Código Geral Tributário / RGIT** before relying on any figure beyond the **MAIBOR + 2%** interest.

## Section 16 -- Summary Employer/Employee Burden (2025)

**Summary Employer/Employee Burden**

| Contribution | Employee | Employer | Base / cap |
| --- | --- | --- | --- |
| IRPS (resident) | 10%–32% progressive (0% below ≈20,250/mo) | (withholding agent) | annual taxable net (gross − 3% INSS) |
| IRPS (non-resident) | flat 20% final WHT | (withholding agent) | MZ-source employment income |
| INSS | 3% | 4% | regular remuneration, **no ceiling** |
| **INSS total** | **3%** | **4%** | **= 7%** combined |

*Column check:* INSS employee 3% + employer 4% = **7%** total. Tie out.

## Section 17 -- Reference Material

**Reference Material table**

| Topic | Figure | Source |
| --- | --- | --- |
| IRPS resident brackets | 10% / 15% / 20% / 25% / 32% (deductions —/2,100/10,500/37,500/141,540) | PwC |
| IRPS monthly PAYE 0% floor | ≈20,250 MZN/month | RSM 2025 p.14 |
| IRPS non-resident | flat 20% final WHT | PwC; RSM 2025 p.14 |
| Self-employment / service provider | 20% | RSM 2025 p.15 |
| Artists / athletes | 10% | RSM 2025 p.15 |
| Digital services / e-money agents | 10% final WHT (Lei 11/2025) | DLA Piper Africa |
| INSS rates | employee 3% / employer 4% / total 7% | INSS Note 246/2024; RSM 2025 p.16 |
| INSS employee 3% IRPS-deductible | yes | PwC |
| M/19 (IRPS PAYE) deadline | 20th of following month | RSM 2025 pp.3–4 |
| INSS return deadline | 10th of following month | RSM 2025 pp.3–4 |
| Nominal List deadline | 30 April | RSM 2025 pp.3–4 |
| Min wage 2025 (lowest sector) | 6,688 MZN/month (agriculture) | Club of Mozambique; DLA Piper |
| Min wage 2025 (financial sector) | 19,043.61 MZN/month | Club of Mozambique; DLA Piper |
| Late-payment interest | MAIBOR (12-mo) + 2% | South African Tax Guide / KPMG (secondary) |

Key authorities: AT (Autoridade Tributária de Moçambique), INSS, Banco de Moçambique (MAIBOR). Big-4 / secondary: PwC Tax Summaries, RSM Mozambique Tax Pocket Guide 2025, DLA Piper Africa, KPMG, Club of Mozambique.

Source URLs:
- PwC IRPS & social security — https://taxsummaries.pwc.com/mozambique/individual/taxes-on-personal-income ; https://taxsummaries.pwc.com/mozambique/individual/other-taxes
- RSM Mozambique Tax Pocket Guide 2025 — https://www.rsm.global/mozambique/sites/default/files/media/2025/Mozambique%20Tax%20Pocket%20Guide%202025%20ENG.pdf
- DLA Piper Africa (Lei 11/2025 IRPS changes) — https://www.dlapiperafrica.com/en/mozambique/insights/2026/Changes-to-the-Personal-Income-Tax-Code
- Minimum wage 2025 — https://clubofmozambique.com/news/mozambique-minimum-wages-increase-2-9-to-9-depending-on-sector-with-retroactive-effect-from-1-july/

## Section 18 -- Test Suite

Each test recomputes end-to-end. Resident IRPS via the annual table (÷12) per the estimation method; INSS employee 3% / employer 4%, no ceiling.

Agriculture min-wage earner. Salary 6,688/mo, resident, 0 deps. Expected: IRPS PAYE 0.00 (below floor); employee INSS 200.64; net 6,487.36; employer cost 6,955.52.

Financial-sector min-wage earner. Salary 19,043.61/mo, resident. Expected: IRPS PAYE 0.00 (below 20,250 floor); employee INSS 571.31; net 18,472.30.

Mid earner (20% band). Salary 30,000/mo, resident, 0 deps. Annual taxable 349,200.00; annual IRPS 59,340.00; monthly IRPS 4,945.00; net 24,155.00.

Higher earner (25% band). Salary 60,000/mo, resident. Annual taxable 698,400.00; annual IRPS 137,100.00; monthly IRPS 11,425.00; net 46,775.00.

Top-band earner (32%). Salary 150,000/mo, resident. Annual taxable 1,746,000.00; annual IRPS 417,180.00; monthly IRPS 34,765.00; net 110,735.00.

Non-resident flat 20%. MZ-source 60,000/mo, non-resident. WHT 12,000.00; net 48,000.00.

Employer cost. Salary 30,000/mo. Employer INSS 4% 1,200.00; total employer cost 31,200.00.

INSS total check. Employee 3% + employer 4% = 7% combined.

Bracket continuity (low bands). At 42,000 → IRPS 4,200.00; at 168,000 → IRPS 23,100.00 (subtract constants tie out).

Currency refusal. Salary stated in USD with no MZN conversion → REFUSE and request a Metical figure.

## PROHIBITIONS

- **IRPS withholding obligation** — NEVER skip IRPS withholding for taxable salaried employees — the employer is the legal withholding agent and must file Form 19 (M/19).  _(Form 19 (M/19))_
- **IRPS PAYE floor application** — NEVER apply IRPS above the 0% PAYE floor (≈20,250/mo) without the correct dependent cell — and never below it where the operative monthly table withholds 0%.  _(≈20,250/mo PAYE floor)_
- **INSS contribution base exclusions** — NEVER include meal subsidies or irregular payments (profit-share, dividends, holiday pay) in the INSS contribution base.
- **No INSS ceiling** — NEVER apply an INSS ceiling — the authoritative sources specify none.
- **Employee INSS deductible before IRPS base** — NEVER forget that the employee's 3% INSS is deductible before the IRPS base.
- **Non-resident flat rate application** — NEVER apply the resident progressive table to a non-resident — non-residents pay a flat 20% final withholding.
- **Residency test - old 180-day rule removed** — NEVER assume residency under the old 180-day test — Lei 11/2025 removed it.  _(Lei 11/2025)_
- **Late-filing penalty unconfirmed** — NEVER state an exact late-filing penalty amount — only the MAIBOR + 2% interest is sourced; the fine schedule is an unconfirmed research gap.  _(MAIBOR + 2% interest)_
- **Filing deadlines** — NEVER miss the INSS (10th) or IRPS M/19 (20th) monthly deadline, or the 30 April Nominal List.  _(INSS 10th, IRPS M/19 20th, Nominal List 30 April)_
- **Estimated computations disclaimer** — NEVER present payroll computations as definitive — always label as estimated and direct to a licensed Mozambican accountant.

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a licensed accountant in Mozambique) before implementation.

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
