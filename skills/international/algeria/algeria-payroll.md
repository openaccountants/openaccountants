---
name: algeria-payroll
description: Use this skill whenever asked about Algeria payroll processing for employed persons. Trigger on phrases like "Algeria payroll", "IRG Traitements et Salaires", "IRG withholding Algeria", "retenue à la source Algérie", "CNAS deduction", "cotisation sociale Algérie", "G50 declaration", "DAS CNAS", "bordereau CNAS", "salaire net Algérie", "PAYE Algeria", "net salary Algeria", "SNMG", "salaire minimum Algérie", "abattement 40% salaire", "employer social security Algeria", "gross to net Algeria", "barème IRG", or any question about computing employee pay, income-tax withholding, or social-security contributions for Algeria-based employees. This skill covers IRG (income tax) withholding by the employer, CNAS social security (employee 9% + employer 26%), the branch-by-branch contribution breakdown, the 40% salary abattement, the SNMG minimum wage, and filing obligations to the DGI (G50) and CNAS (monthly + annual DAS). ALWAYS read this skill before processing any Algeria payroll.
version: 0.1
jurisdiction: DZ
tax_year: 2025
last_updated: 2026-07-13
review_status: pending_review
depends_on: - payroll-workflow-base
category: payroll
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Algeria Payroll

## Algeria Payroll Skill v0.1

> **Tier 2 (research-verified) — NOT yet accountant-verified.** Several figures carry `[RESEARCH GAP — reviewer to confirm]` markers. A licensed Algerian expert-comptable / commissaire aux comptes must reconcile those before any output is presented as final.

## Section 1 -- Quick Reference

**Quick Reference**

| Field | Value |
| --- | --- |
| Country | Algeria (République algérienne démocratique et populaire) |
| Currency | Algerian Dinar (DZD / DA) only — wages paid in Dinars |
| Standard pay frequency | Monthly (most common) |
| Tax year | Calendar year (1 January -- 31 December) |
| Income tax | YES — IRG (Impôt sur le Revenu Global, Traitements et Salaires), progressive 0% / 23% / 27% / 30% / 33% / 35%, employer-withheld monthly (retenue à la source) (PwC; DGI/Radio Algérienne) |
| Tax authority | DGI (Direction Générale des Impôts) |
| Social security authority | CNAS (Caisse Nationale des Assurances Sociales) |
| IRG declaration form | **G50** (bordereau-avis de versement, monthly) (Rivermate) |
| CNAS annual return | **DAS** (Déclaration Annuelle des Salaires), due **31 January** (Radio Algérienne; Fatoura; teledeclaration.cnas.dz) |
| Key legislation | Code des Impôts Directs (IRG, Traitements et Salaires); Loi de Finances 2022 (current IRG scale); Loi 83-11 (sécurité sociale); Code des Procédures Fiscales |
| Filing portals | DGI (G50); CNAS télédéclaration (`teledeclaration.cnas.dz`) |
| Validated by | Pending -- requires sign-off by a licensed Algerian expert-comptable |
| Skill version | 0.1 |

## Section 2 -- Income Tax Withholding (IRG — Traitements et Salaires)

Algeria **does** levy personal income tax on salaries. The employer is the **withholding agent**: it deducts IRG monthly from payroll (*retenue à la source*) and remits it on the **G50** declaration (PwC — Taxes on personal income; Rivermate). The progressive scale was introduced by the **Loi de Finances 2022 (FL 2022), effective 1 January 2022**, and remains the current scale for 2025 (no replacement scale published for 2025/2026 as of the research date).

### IRG Progressive Scale — annual taxable salary income (DZD)

**IRG Progressive Scale — annual taxable salary income (DZD)**  _(PwC Worldwide Tax Summaries (Algeria — Individual / Taxes on personal income, "effective FL 2022, marginal rate 35%"); DGI press release via Radio Algérienne (news.radioalgerie.dz/fr/node/3142))_

| Annual taxable income (DZD) | Marginal rate | Cumulative tax at top of band (DZD) |
| --- | --- | --- |
| 0 – 240,000 | **0% (exonéré)** | 0.00 |
| 240,001 – 480,000 | **23%** | 55,200.00 |
| 480,001 – 960,000 | **27%** | 184,800.00 |
| 960,001 – 1,920,000 | **30%** | 472,800.00 |
| 1,920,001 – 3,840,000 | **33%** | 1,106,400.00 |
| Above 3,840,000 | **35%** | — |

**Subtract-method constants**  _(IRG = (annual taxable income × rate) − subtract)_

| Band | Rate | Subtract (DZD) |
| --- | --- | --- |
| 240,001 – 480,000 | 23% | 55,200.00 |
| 480,001 – 960,000 | 27% | 74,400.00 |
| 960,001 – 1,920,000 | 30% | 103,200.00 |
| 1,920,001 – 3,840,000 | 33% | 160,800.00 |
| 3,840,001+ | 35% | 237,600.00 |

*Continuity check:* at 480,000 → 0.23 × 480,000 − 55,200 = **55,200.00**; at 960,000 → 0.27 × 960,000 − 74,400 = **184,800.00**; at 1,920,000 → 0.30 × 1,920,000 − 103,200 = **472,800.00**; at 3,840,000 → 0.33 × 3,840,000 − 160,800 = **1,106,400.00**. All bands tie out.

### Monthly full exemption

- **IRG monthly full exemption** — Salaries up to 30,000 DA/month are fully exempt from IRG, regardless of the annual-scale outcome. Apply this exemption as a hard gate: if monthly gross ≤ 30,000 DA, IRG = 0.  _(DGI / Radio Algérienne — news.radioalgerie.dz/fr/node/3142)_

### Salary abattement (professional-expense deduction)

- **Salary abattement** — A 40% deduction is applied to salary income before the scale, floored at 12,000 DA/year (1,000 DA/month) and capped at 18,000 DA/year (1,500 DA/month).  _(Radio Algérienne — node/3142)_

### IRG base — order of operations

- **IRG base calculation order** — IRG is computed on salary net of employee social contributions (the 9% CNAS employee share is deducted first) and after the 40% abattement, then the annual scale is applied: 1. Start from monthly gross salary. 2. Subtract employee CNAS (9%) → salary after social contributions. 3. Subtract the 40% abattement (min 1,000 / max 1,500 DA per month) → monthly IRG base. 4. Annualise (× 12), apply the progressive scale (subtract-method), divide by 12 → monthly IRG. 5. If monthly gross ≤ 30,000 DA, override IRG to 0 (full exemption).  _(IRG order of operations, section 2)_

> **[RESEARCH GAP — reviewer to confirm]** The exact ordering (abattement vs. social-contribution deduction) and whether the 30,000 DA exemption is a clean gate or interacts with the abattement floor should be confirmed against the DGI's IRG-Traitements-et-Salaires text before finalizing.

## Section 3 -- Social Security -- CNAS (Employee + Employer)

CNAS social security runs across five branches. The total statutory rate is 35% of gross salary = employer 26% + employee 9% (PwC — Other taxes; Rivermate). Contributions are levied on gross salary with no upper ceiling (uncapped) for the general salaried regime; the effective floor is the SNMG minimum wage — contributions cannot be based on less than the SNMG (PwC; Rivermate; CLEISS).

### Operative payroll figures

**Operative payroll figures**  _(PwC (taxsummaries.pwc.com/algeria/individual/other-taxes); Rivermate (rivermate.com/guides/algeria/taxes))_

| Side | Rate | Base |
| --- | --- | --- |
| Employee CNAS | **9%** | Gross salary (uncapped; floor = SNMG) |
| Employer CNAS | **26%** | Gross salary (uncapped; floor = SNMG) |
| **Total** | **35%** | — |

### Branch-by-branch breakdown (CLEISS, effective 1 January 2024, unchanged into 2025)

**Branch-by-branch breakdown**  _(CLEISS — official French inter-scheme liaison body (cleiss.fr/docs/cotisations/algerie.html))_

| Branch | Employer | Employee | Other funds | Total |
| --- | --- | --- | --- | --- |
| Assurances sociales (sickness, maternity, disability, death) | 11.5% | 1.5% | — | 13.0% |
| Accidents du travail / maladies professionnelles | 1.25% | — | — | 1.25% |
| Retraite (pension) | 11.0% | 6.75% | 0.5% (FNPOS social-housing) | 18.25% |
| Retraite anticipée (early retirement) | 0.25% | 0.25% | — | 0.5% |
| Assurance chômage (unemployment) | 1.0% | 0.5% | — | 1.5% |
| **TOTALS** | **25.0%** | **9.0%** | **0.5%** | **34.5%** |

*Column check:* employer 11.5 + 1.25 + 11.0 + 0.25 + 1.0 = **25.0%**; employee 1.5 + 0 + 6.75 + 0.25 + 0.5 = **9.0%**; other = **0.5%**; grand total = **34.5%**.

- **Reconciliation note** — CLEISS itemises the employer side as 25% + 0.5% FNPOS social-housing levy = 25.5%; adding 0.5% for œuvres sociales (social works) brings the headline employer figure to the commonly cited 26%. The Big-4 / payroll summaries (PwC, Rivermate) state the headline as a flat employer 26% / employee 9% / total 35%. Both describe the same regime; the 35% headline includes the social-works and housing-fund components that CLEISS lists separately. Use 26% employer / 9% employee / 35% total as the operative payroll figures, with the CLEISS table as the branch detail.  _(CLEISS; PwC; Rivermate)_

### Sector add-on (construction)

- **CACOBATPH construction add-on** — Construction / public works / hydraulics pay an extra 0.375% each (employer and employee) via CACOBATPH (sector leave / bad-weather fund). Apply only for those sectors.  _(CLEISS)_

## Section 4 -- Minimum Wage — SNMG (Salaire National Minimum Garanti)

**SNMG by year**  _(Algeria Invest (algeriainvest.com); Radio Algérienne (news.radioalgerie.dz/en/node/75102); WageIndicator (wageindicator.org))_

| Year | SNMG (DZD/month) | Status | Source |
| --- | --- | --- | --- |
| 2025 | **20,000** | In effect | Algeria Invest; Radio Algérienne |
| 2026 | **24,000** (≈+20%) | Approved by Council of Ministers, effective **1 January 2026** | Algeria Invest; Radio Algérienne; WageIndicator |

The SNMG is a single national figure applying to public and private sectors. It is the floor for CNAS contributions (contributions cannot be based on less than the SNMG).

> Context only (not a payroll deduction): the unemployment allowance (*allocation chômage*) was raised to **18,000 DA** alongside the 2026 SNMG hike (Algeria Invest).

## Section 5 -- Conservative Defaults

**Conservative Defaults**

| Unknown | Conservative default | Why |
| --- | --- | --- |
| Tax year | Default to **2025** scale (FL 2022, still current) | Skill tax_year is 2025; no 2026 scale published |
| Sector (construction add-on) | Assume **no** CACOBATPH 0.375% add-on unless told construction | Avoids over-stating; flag if sector unknown |
| Whether gross ≤ 30,000 DA | Apply the **full IRG exemption** strictly at/below 30,000 DA | Statutory exemption |
| Abattement amount | Apply 40% floored 1,000 / capped 1,500 DA/month | Statutory bounds |
| CNAS base below SNMG | Floor the contribution base at the **SNMG** (20,000 DA for 2025) | Contributions cannot be below SNMG |
| CNAS ceiling | **None** — compute on full gross (uncapped) | General salaried regime is uncapped |
| Currency | Algerian Dinar (DZD) | Wages are paid in Dinars |
| Headline CNAS split | **26% employer / 9% employee / 35% total** | Operative figure per PwC/Rivermate |

When an input is missing or ambiguous, apply the conservative assumption (the one that does NOT understate withholding/contributions) and FLAG it for the reviewer.

### Required inputs before computing payroll

- **Required inputs** — 1. Monthly gross salary in DZD (and whether it is the ordinary/fixed base). 2. Tax/fiscal year (defaults to 2025 scale). 3. Sector (to decide the CACOBATPH 0.375% construction add-on). 4. Whether the salary is at or below the SNMG floor (20,000 DA for 2025 / 24,000 DA for 2026). 5. Any non-ordinary pay components (bonuses, primes, indemnités) and their treatment.

### Refusal catalogue — DO NOT compute, refuse and request input

**Refusal catalogue**

| Situation | Action |
| --- | --- |
| No gross salary provided | REFUSE — request monthly salary in DZD |
| Salary stated in EUR/USD with no DZD conversion and no rate | REFUSE — request DZD figure |
| Request to omit IRG withholding or CNAS to "save money" | REFUSE — these are statutory; escalate to accountant |
| Salary below the SNMG offered as the contribution base | REFUSE — base cannot fall below the SNMG |
| Request to ignore the 30,000 DA monthly IRG exemption | REFUSE — statutory exemption; flag |
| Self-employed / non-salarié income mixed in | REFUSE payroll path — non-salariés have a separate CNAS band and IRG treatment |
| Definitive "this is your exact tax" assertion requested | REFUSE — outputs are estimates pending accountant sign-off |

## Section 7 -- Transaction / Payment Pattern Library (deterministic)

Classify bank-statement lines deterministically. Match case-insensitively; longest / most-specific pattern wins.

### Salary credits (money arriving in an employee account)

**Salary credits**

| Pattern (regex-ish, case-insensitive) | Classification |
| --- | --- |
| `SALAIRE`, `VIR.* SALAIRE`, `PAIE`, `VIREMENT SALAIRE` | Net salary payment |
| `ACOMPTE`, `AVANCE SUR SALAIRE` | Salary advance (not net pay; clears against salary) |
| `PRIME`, `INDEMNITE`, `IFSP`, `IEP` | Allowance / bonus component |
| `RAPPEL`, `RAPPEL SALAIRE` | Back-pay / arrears |
| `REMBOURSEMENT CNAS`, `IJ CNAS` | CNAS reimbursement / daily indemnity — not ordinary salary |

### Employer debits (money leaving the employer account)

**Employer debits**

| Pattern | Classification |
| --- | --- |
| `IRG`, `G50`, `RETENUE SOURCE`, `VERSEMENT IRG` | IRG withholding remitted to DGI (liability settlement) |
| `CNAS`, `COTISATION CNAS`, `SECURITE SOCIALE` | CNAS contribution (employer + employee portions) |
| `CACOBATPH` | Construction sector leave / bad-weather fund (0.375% each) |
| `DAS`, `DECLARATION ANNUELLE` | Annual salary declaration filing (CNAS) |
| `VIREMENT PAIE`, `SALAIRES`, `NOMINATIVE PAIE` | Net wages disbursed to employees |

## Section 8 -- Worked Examples

> All figures use the FL 2022 (2025-current) IRG scale, CNAS employee 9% and the 40% abattement (capped 1,500 DA/month). IRG base = (gross − 9% CNAS − abattement), annualised, scaled, ÷ 12. The 30,000 DA/month full exemption overrides to IRG = 0. Amounts rounded to the cent. Construction add-on excluded (general sector).

### Example 1 — At the 2026 SNMG, fully IRG-exempt

**Inputs:** Gross 24,000 DA/month (the 2026 SNMG).

- Employee CNAS 9% = 0.09 × 24,000 = **2,160.00**.
- Salary after CNAS = 24,000 − 2,160 = 21,840.00.
- Gross ≤ 30,000 DA → **IRG = 0.00** (full monthly exemption).
- **Net pay** = 24,000 − 2,160 − 0 = **21,840.00 DA**.

*Bank line example:* `VIR SALAIRE — MARS` credit **21,840.00 DA**.

### Example 2 — Just at the 30,000 DA exemption ceiling

**Inputs:** Gross 30,000 DA/month.

- Employee CNAS 9% = 0.09 × 30,000 = **2,700.00**.
- Salary after CNAS = 30,000 − 2,700 = 27,300.00.
- Gross = 30,000 DA ≤ 30,000 → **IRG = 0.00** (exemption applies at and below 30,000).
  *(Note: without the exemption, the annualised base would be (27,300 − 1,500) × 12 = 309,600, which falls in the 23% band and would otherwise yield IRG — the exemption is what zeroes it.)*
- **Net pay** = 30,000 − 2,700 − 0 = **27,300.00 DA**.

### Example 3 — Mid earner, into the 23%/27% bands

**Inputs:** Gross 45,000 DA/month.

- Employee CNAS 9% = 0.09 × 45,000 = **4,050.00**.
- Salary after CNAS = 45,000 − 4,050 = 40,950.00.
- Abattement = min(0.40 × 40,950, 1,500) = **1,500.00** (capped).
- Monthly IRG base = 40,950 − 1,500 = 39,450.00 → annualised = 39,450 × 12 = **473,400.00** (in the 23% band: 240,001–480,000).
- IRG annual = 0.23 × 473,400 − 55,200 = 108,882.00 − 55,200 = **53,682.00**.
- IRG monthly = 53,682.00 ÷ 12 = **4,473.50**.
- **Net pay** = 45,000 − 4,050 − 4,473.50 = **36,476.50 DA**.

### Example 4 — Higher earner, into the 27% band

**Inputs:** Gross 80,000 DA/month.

- Employee CNAS 9% = 0.09 × 80,000 = **7,200.00**.
- Salary after CNAS = 80,000 − 7,200 = 72,800.00.
- Abattement = **1,500.00** (capped).
- Monthly IRG base = 72,800 − 1,500 = 71,300.00 → annualised = 855,600.00 (in the 27% band: 480,001–960,000).
- IRG annual = 0.27 × 855,600 − 74,400 = 231,012.00 − 74,400 = **156,612.00**.
- IRG monthly = 156,612.00 ÷ 12 = **13,051.00**.
- **Net pay** = 80,000 − 7,200 − 13,051.00 = **59,749.00 DA**.

### Example 5 — Top-band earner (35% marginal)

**Inputs:** Gross 400,000 DA/month.

- Employee CNAS 9% = 0.09 × 400,000 = **36,000.00**.
- Salary after CNAS = 400,000 − 36,000 = 364,000.00.
- Abattement = **1,500.00** (capped).
- Monthly IRG base = 364,000 − 1,500 = 362,500.00 → annualised = 4,350,000.00 (above 3,840,000 → 35% band).
- IRG annual = 0.35 × 4,350,000 − 237,600 = 1,522,500.00 − 237,600 = **1,284,900.00**.
- IRG monthly = 1,284,900.00 ÷ 12 = **107,075.00**.
- **Net pay** = 400,000 − 36,000 − 107,075.00 = **256,925.00 DA**.

### Example 6 — Employer total cost of an 80,000 DA/month earner

**Employer total cost table**

| Employer cost item | Computation | Amount (DZD) |
| --- | --- | --- |
| Gross salary | — | 80,000.00 |
| Employer CNAS 26% | 0.26 × 80,000 | 20,800.00 |
| **Total employer cost** | sum | **100,800.00** |

Building on Example 4 (gross 80,000 DA/month, general sector):

*Check:* 80,000 + 20,800 = **100,800.00**. Employer-on-top burden = 20,800 = 26% of gross. (Construction add-on would add 0.375% × 80,000 = 300.00 DA on top — excluded here.)

## Section 9 -- Tier 1 Rules (hard, non-negotiable)

- **Tier 1 Rules** — 1. IRG is employer-withheld monthly (retenue à la source) and remitted to the DGI on the G50; never skip it for salaried staff (PwC; Rivermate). 2. Apply the IRG base order: gross → minus 9% CNAS → minus 40% abattement (1,000–1,500 DA/month) → annualise → progressive scale (subtract-method) → ÷ 12. 3. Salaries ≤ 30,000 DA/month are fully IRG-exempt — override IRG to 0 (DGI/Radio Algérienne). 4. CNAS is employee 9% + employer 26% = 35% total, on uncapped gross, floored at the SNMG (PwC; Rivermate; CLEISS). 5. The CNAS contribution base can never fall below the SNMG (20,000 DA for 2025; 24,000 DA for 2026). 6. Construction / public-works employers add CACOBATPH 0.375% each (employer and employee) (CLEISS). 7. Wages are paid in Algerian Dinars. 8. CNAS contributions are remitted monthly; the DAS annual return is due 31 January; the G50 is due by the 20th of the following month (Rivermate; Radio Algérienne; Fatoura). 9. Every output is an estimate pending licensed-accountant sign-off.  _(PwC; Rivermate; DGI/Radio Algérienne; CLEISS; Fatoura)_

## Section 10 -- Tier 2 Catalogue (reviewer judgement required)

**Tier 2 Catalogue**

| Question | Why it needs a reviewer |
| --- | --- |
| Exact ordering of abattement vs. CNAS deduction in the IRG base | Not cleanly confirmed against DGI text |
| Interaction of the 30,000 DA exemption with the abattement floor | Mechanic not fully documented |
| Whether the FL 2022 scale still applies for the period in question | No 2025/2026 replacement published; verify currency |
| Exact IRG (G50) late-payment penalty percentages | Not confirmed from a primary DGI source |
| Precise date of the annual DGI salary recap (~30 April) | Secondary source only |
| CACOBATPH applicability for a given employer | Sector-specific |
| Treatment of specific primes / indemnités (taxable vs exempt) | Component-specific, needs ruling |
| Headline 26% vs CLEISS 25.5% employer reconciliation | Two presentations of the same regime |

## Section 11 -- Excel Working Paper Template

**Excel Working Paper Template**

| Col | Header | Formula / source |
| --- | --- | --- |
| A | Employee name | input |
| B | Gross monthly salary (DZD) | input |
| C | Employee CNAS 9% | `=B*0.09` |
| D | Salary after CNAS | `=B-C` |
| E | Abattement | `=MIN(MAX(D*0.40,1000),1500)` |
| F | Monthly IRG base | `=MAX(0, D-E)` |
| G | Annual IRG base | `=F*12` |
| H | IRG annual | nested IF on G using subtract constants (55,200 / 74,400 / 103,200 / 160,800 / 237,600) |
| I | IRG monthly (pre-exemption) | `=H/12` |
| J | IRG monthly (final) | `=IF(B<=30000, 0, I)` |
| K | Net pay | `=B-C-J` |
| L | Employer CNAS 26% | `=B*0.26` |
| M | CACOBATPH (construction only) | `=IF(construction, B*0.375%*2, 0)` |
| N | Total employer cost | `=B+L+IF(construction, B*0.375%, 0)` |

- **IRG formula for column H** — =IF(G<=240000,0, IF(G<=480000, G*0.23-55200, IF(G<=960000, G*0.27-74400, IF(G<=1920000, G*0.30-103200, IF(G<=3840000, G*0.33-160800, G*0.35-237600)))))  _(Section 11 formulas)_

Suggested layout (one row per employee per month):

## Section 12 -- Bank Statement / Terminology Reading Guide

**Terminology Reading Guide**

| French / Arabic-transliterated term | English / meaning |
| --- | --- |
| Salaire / Paie | Salary / payroll run |
| IRG (Impôt sur le Revenu Global) | Personal income tax |
| Traitements et Salaires | Wages and salaries (the salary category of IRG) |
| Retenue à la source | Withholding at source |
| Abattement | Deduction / allowance (here, the 40% professional-expense deduction) |
| CNAS | National Social Insurance Fund |
| Cotisation | Contribution (social security) |
| G50 (bordereau) | Monthly tax/contribution declaration slip |
| DAS (Déclaration Annuelle des Salaires) | Annual salary declaration (CNAS) |
| SNMG | Guaranteed national minimum wage |
| Prime / Indemnité | Bonus / allowance |
| Acompte / Avance | Advance on salary |
| CACOBATPH | Construction-sector leave / bad-weather fund |
| FNPOS | Social-housing fund (0.5% pension-branch component) |
| Allocation chômage | Unemployment allowance |
| DGI | Directorate-General of Taxes |

## Section 13 -- Onboarding Fallback

- **Onboarding fallback steps** — If the engagement lacks key data: 1. No prior payroll register (livre de paie) available → request the last 3 months of payslips, G50 declarations, and CNAS bordereaux to back-solve the rates actually applied. 2. Unknown sector → default CACOBATPH off, FLAG; confirm before the first remittance. 3. Salary near the SNMG → confirm the contribution base is floored at the SNMG (20,000 DA for 2025 / 24,000 DA for 2026), never below. 4. Year ambiguity → default to the 2025 (FL 2022) scale; verify whether any new finance law has replaced it for periods after the research date. 5. Mixed self-employed income → route non-salarié income to a separate treatment; the non-salariés CNAS band (216,000–4,320,000 DZD/year, CLEISS) and IRG treatment differ.  _(CLEISS)_

## Section 14 -- Filing, Forms & Deadlines

**Filing, Forms & Deadlines**

| Item | Detail | Source |
| --- | --- | --- |
| Tax year | Calendar year ending 31 Dec | DGI |
| IRG withholding | Withheld monthly; declared/paid on the **G50** by the **20th of the following month** (quarterly possible under the régime simplifié — verify the taxpayer's regime) | Rivermate |
| CNAS contributions | Employer withholds the employee 9% and remits the full 35% **monthly**, due in the following month | CLEISS; Radio Algérienne |
| CNAS annual return | **DAS** (Déclaration Annuelle des Salaires), due **31 January**, filed electronically at `teledeclaration.cnas.dz` (employer file + per-employee detail file) | Radio Algérienne; Fatoura; CNAS portal |
| Annual IRG salary recap (DGI) | États des salaires, typically by **~30 April** | Rivermate — **[RESEARCH GAP — reviewer to confirm exact DGI date]** |

## Section 15 -- Registration

- **Registration requirements** — Employers must register with CNAS as an affilié employeur and obtain an employer number before the first payroll; each employee is registered and assigned a social security number. Registration is triggered by hiring the first employee — there is no monetary threshold; any employer of salaried staff must register (CNAS employer portal, cnas.dz/en/employer/). Tax registration (NIF — numéro d'identification fiscale) with the DGI is required for the G50.  _(CNAS employer portal, cnas.dz/en/employer/)_

## Section 16 -- Penalties (late filing / late payment)

**Penalties**

| Item | Detail | Source |
| --- | --- | --- |
| CNAS — late / non-declaration of contributions | **15% of contributions due** (base penalty) **plus a 2%-per-month surcharge (majoration de retard)** for the period of delay | Fatoura / CNAS rules (fatoura.app), corroborated by multiple payroll guides |
| IRG (G50) — late payment | Standard DGI late-payment penalties apply (typically **10% if paid within the month after the deadline, rising thereafter, plus monthly interest / indemnité de retard**) | Rivermate / general — **[RESEARCH GAP — reviewer to confirm exact percentages against the Code des Procédures Fiscales]** |

> **[RESEARCH GAP — reviewer to confirm]** The exact IRG late-payment penalty percentages were not confirmed from a primary DGI source in this research. Read them directly from the *Code des Procédures Fiscales* before relying on specific figures.

## Section 17 -- Summary Employer/Employee Burden (general sector)

**Summary Employer/Employee Burden**

| Contribution | Employee | Employer | Base/cap |
| --- | --- | --- | --- |
| IRG | 0% / 23% / 27% / 30% / 33% / 35% progressive | (withholding agent) | annual taxable base; ≤30,000 DA/mo exempt |
| CNAS (all branches) | 9% | 26% | uncapped gross; floor = SNMG |
| CACOBATPH (construction only) | 0.375% | 0.375% | gross (construction sector) |

*Check:* CNAS employee 9% + employer 26% = **35% total** (operative figures, PwC/Rivermate); CLEISS branch detail sums to 25% employer + 9% employee + 0.5% other = 34.5% (same regime, social-works component shown separately).

## Section 18 -- Reference Material

**Reference Material**

| Topic | Figure | Source |
| --- | --- | --- |
| IRG scale (current) | 0% / 23% / 27% / 30% / 33% / 35%, FL 2022 | PwC; DGI/Radio Algérienne |
| IRG exempt threshold (annual) | 240,000 DZD | PwC; Radio Algérienne |
| IRG monthly full exemption | ≤ 30,000 DA/month | DGI / Radio Algérienne (node/3142) |
| Salary abattement | 40%, floor 12,000 / cap 18,000 DZD per year | Radio Algérienne (node/3142) |
| CNAS split | 9% employee / 26% employer / 35% total | PwC; Rivermate |
| CNAS branch detail | 25% er + 9% ee + 0.5% other = 34.5% | CLEISS (effective 1 Jan 2024) |
| CACOBATPH (construction) | 0.375% each | CLEISS |
| SNMG 2025 / 2026 | 20,000 / 24,000 DZD/month | Algeria Invest; Radio Algérienne; WageIndicator |
| G50 deadline | 20th of following month | Rivermate |
| DAS deadline | 31 January | Radio Algérienne; Fatoura; CNAS portal |
| CNAS penalty | 15% + 2%/month surcharge | Fatoura / CNAS |

Key authorities: DGI (`mfdgi.gov.dz`), CNAS (`cnas.dz`, `teledeclaration.cnas.dz`), CLEISS (`cleiss.fr`). Big-4 / secondary: PwC Worldwide Tax Summaries, Rivermate, Algeria Invest, Radio Algérienne, WageIndicator, Fatoura.

## Section 19 -- Test Suite

Each test recomputes end-to-end. Expected values use the FL 2022 (2025-current) scale, CNAS
employee 9%, and the 40% abattement (capped 1,500 DA/month).

- **Test 1: 2026 SNMG, exempt** — Gross 24,000 DA/mo. Employee CNAS = 2,160.00; IRG = 0.00 (≤ 30,000 exemption); net = 21,840.00.  _(Section 19 -- Test Suite)_
- **Test 2: Exemption ceiling** — Gross 30,000 DA/mo. Employee CNAS = 2,700.00; IRG = 0.00 (exemption applies at 30,000); net = 27,300.00.  _(Section 19 -- Test Suite)_
- **Test 3: 23% band** — Gross 45,000 DA/mo. After CNAS 40,950; abattement 1,500; annual base 473,400; IRG annual 53,682.00; IRG monthly 4,473.50; net 36,476.50.  _(Section 19 -- Test Suite)_
- **Test 4: 27% band** — Gross 80,000 DA/mo. After CNAS 72,800; annual base 855,600; IRG annual 156,612.00; IRG monthly 13,051.00; net 59,749.00.  _(Section 19 -- Test Suite)_
- **Test 5: 35% band** — Gross 400,000 DA/mo. After CNAS 364,000; annual base 4,350,000; IRG annual 1,284,900.00; IRG monthly 107,075.00; net 256,925.00.  _(Section 19 -- Test Suite)_
- **Test 6: Employer cost** — Gross 80,000 DA/mo, general sector. Employer CNAS 26% = 20,800.00; total employer cost = 100,800.00.  _(Section 19 -- Test Suite)_
- **Test 7: Bracket continuity** — Annual base 480,000 → IRG 55,200.00; 960,000 → 184,800.00; 1,920,000 → 472,800.00; 3,840,000 → 1,106,400.00 (subtract constants tie out).  _(Section 19 -- Test Suite)_
- **Test 8: Branch totals** — CLEISS employer column = 25.0%, employee column = 9.0%, grand total = 34.5%.  _(Section 19 -- Test Suite)_
- **Test 9: SNMG floor** — Contribution base for a 15,000 DA/mo nominal wage is floored at the SNMG (20,000 DA for 2025) → REFUSE a base below SNMG and flag.  _(Section 19 -- Test Suite)_
- **Test 10: Currency refusal** — Salary stated in EUR with no DZD conversion → REFUSE and request the Dinar figure.  _(Section 19 -- Test Suite)_

## PROHIBITIONS

- **Withholding obligation** — NEVER skip IRG withholding for salaried employees — the employer is the legal withholding agent.  _(PROHIBITIONS)_
- **Exemption threshold** — NEVER apply IRG to a salary of 30,000 DA/month or less — it is fully exempt.  _(PROHIBITIONS)_
- **Abattement requirement** — NEVER omit the 40% abattement (capped 1,500 DA/month) before applying the IRG scale.  _(PROHIBITIONS)_
- **CNAS floor** — NEVER apply a CNAS contribution base below the SNMG (20,000 DA for 2025 / 24,000 DA for 2026).  _(PROHIBITIONS)_
- **CNAS uncapped** — NEVER cap CNAS contributions — the general salaried regime is uncapped.  _(PROHIBITIONS)_
- **Employer CNAS share** — NEVER forget the employer's 26% CNAS share on top of the employee's 9%.  _(PROHIBITIONS)_
- **CACOBATPH restriction** — NEVER add CACOBATPH 0.375% outside the construction / public-works sectors.  _(PROHIBITIONS)_
- **G50 penalty uncertainty** — NEVER state an exact IRG (G50) late-payment penalty — the precise figure is an unconfirmed research gap.  _(PROHIBITIONS)_
- **Currency restriction** — NEVER pay or compute wages in a foreign currency — Algerian Dinars only.  _(PROHIBITIONS)_
- **Deadline compliance** — NEVER miss the monthly G50 (20th) / CNAS remittance or the 31 January DAS deadline.  _(PROHIBITIONS)_
- **Professional review requirement** — NEVER present payroll computations as definitive — always label as estimated and direct to a licensed Algerian expert-comptable.  _(PROHIBITIONS)_

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a licensed expert-comptable in Algeria) before implementation.

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
