---
name: ivory-coast-social-contributions
description: Use this skill whenever asked about Côte d'Ivoire (Ivory Coast) social security contributions (CNPS) for employers and salaried employees. Trigger on phrases like "CNPS contributions", "cotisations sociales Côte d'Ivoire", "Ivory Coast social security", "retraite CNPS", "prestations familiales", "accident du travail rate", "CMU contribution", "how much CNPS do I pay", "employer social charges Ivory Coast", "assiette plafonnée", "plafond CNPS", or any question about Ivorian social-contribution obligations. Also trigger when classifying bank-statement or payroll transactions that relate to CNPS débits, cotisations sociales, or CMU payments from Ivorian banks (SGCI, BICICI, Ecobank, NSIA, Coris). Also trigger when preparing a DISA/DASC annual declaration or a monthly/quarterly appel de cotisations where contribution ceilings and rates are relevant. This skill covers pension (vieillesse) rates and the XOF 3,375,000 ceiling, family benefits, maternity, work-injury bands, CMU, the SMIG floor, declaration periodicity, penalties, registration, payment patterns, and edge cases. ALWAYS read this skill before touching any CNPS-related work.
version: 0.1
jurisdiction: CI
tax_year: 2025
last_updated: 2026-07-13
review_status: pending_review
depends_on: - social-contributions-workflow-base
category: international
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Côte d'Ivoire (Ivory Coast) Social Contributions (CNPS) -- Employer & Employee

## Côte d'Ivoire (Ivory Coast) Social Contributions (CNPS) -- Employer & Employee Skill v0.1

## Section 1 -- Quick reference

**Read this whole section before computing or classifying anything.**

- **Country** — Côte d'Ivoire (Republic of Côte d'Ivoire / Ivory Coast)
- **Primary Legislation** — Loi n° 99-477 du 2 août 1999 (Code de Prévoyance Sociale), arts. 5, 23, 26, 30
- **Ceiling Legislation** — Décret n° 2022-986 du 21 décembre 2022 (sets SMIG XOF 75,000; pension ceiling 45 × SMIG), in force 1 Jan 2023
- **Tax / Social Authority** — Caisse Nationale de Prévoyance Sociale (CNPS) — www.cnps.ci; portal e.cnps.ci
- **Currency** — West African CFA franc (XOF / FCFA) — **XOF only**
- **SMIG (minimum wage)** — XOF 75,000/month (since 1 Jan 2023, 40h/week) — used as the contribution floor (plancher)
- **Pension (vieillesse) rate** — 6.3% employee + 7.7% employer = 14%
- **Pension monthly ceiling (assiette max)** — **XOF 3,375,000** (= 45 × SMIG) — NOT 1,647,315, NOT 2,700,000
- **Family benefits (prestations familiales)** — 5% employer only
- **Maternity (assurance maternité)** — 0.75% employer only
- **Work injury (AT/MP)** — 2%–5% employer only, by sector risk category
- **PF / Maternity / AT-MP monthly ceiling** — XOF 75,000 (floor = ceiling at the SMIG)
- **CMU (Couverture Maladie Universelle, health)** — XOF 500/month employee + XOF 500/month employer, per person (flat, no % base)
- **Payment frequency** — Monthly if ≥20 employees; quarterly if <20 employees
- **Payment deadline** — Within the first 15 days following the month/quarter ended
- **Annual regularisation** — DISA + DASC by 31 March of the following year (art. 26)
- **Late penalty** — 10% of contributions due, plus majorations de retard

Pending — requires sign-off by a warranted Ivorian accountant / expert-comptable

Pending

**Quick reference table**

| Field | Value |
| --- | --- |
| Country | Côte d'Ivoire (Republic of Côte d'Ivoire / Ivory Coast) |
| Primary Legislation | Loi n° 99-477 du 2 août 1999 (Code de Prévoyance Sociale), arts. 5, 23, 26, 30 |
| Ceiling Legislation | Décret n° 2022-986 du 21 décembre 2022 (sets SMIG XOF 75,000; pension ceiling 45 × SMIG), in force 1 Jan 2023 |
| Tax / Social Authority | Caisse Nationale de Prévoyance Sociale (CNPS) — www.cnps.ci; portal e.cnps.ci |
| Currency | West African CFA franc (XOF / FCFA) — **XOF only** |
| SMIG (minimum wage) | XOF 75,000/month (since 1 Jan 2023, 40h/week) — used as the contribution floor (plancher) |
| Pension (vieillesse) rate | 6.3% employee + 7.7% employer = 14% |
| Pension monthly ceiling (assiette max) | **XOF 3,375,000** (= 45 × SMIG) — NOT 1,647,315, NOT 2,700,000 |
| Family benefits (prestations familiales) | 5% employer only |
| Maternity (assurance maternité) | 0.75% employer only |
| Work injury (AT/MP) | 2%–5% employer only, by sector risk category |
| PF / Maternity / AT-MP monthly ceiling | XOF 75,000 (floor = ceiling at the SMIG) |
| CMU (Couverture Maladie Universelle, health) | XOF 500/month employee + XOF 500/month employer, per person (flat, no % base) |
| Payment frequency | Monthly if ≥20 employees; quarterly if <20 employees |
| Payment deadline | Within the first 15 days following the month/quarter ended |
| Annual regularisation | DISA + DASC by 31 March of the following year (art. 26) |
| Late penalty | 10% of contributions due, plus majorations de retard |
| Validated by | Pending — requires sign-off by a warranted Ivorian accountant / expert-comptable |
| Validation date | Pending |

**Branch overview (private-sector salaried, régime général)**

| Branch | Employee | Employer | Total | Monthly ceiling (assiette max) |
| --- | --- | --- | --- | --- |
| Assurance Vieillesse (pension/retraite) | 6.3% | 7.7% | 14% | XOF 3,375,000 |
| Prestations Familiales (family benefits) | — | 5% | 5% | XOF 75,000 |
| Assurance Maternité (maternity) | — | 0.75% | 0.75% | XOF 75,000 |
| Accidents du Travail / Maladies Pro. (work injury) | — | 2%–5% | 2%–5% | XOF 75,000 |
| CMU (health, flat per capita) | XOF 500/mo | XOF 500/mo | XOF 1,000/mo | flat per person, no % base |

**Conservative defaults**

| Ambiguity | Default |
| --- | --- |
| Unknown AT/MP risk category | Use 2% (lowest band); flag for reviewer to confirm employer's assigned category |
| Unknown headcount (monthly vs quarterly) | Assume <20 → quarterly; flag to confirm |
| Salary below SMIG (XOF 75,000) | Apply the SMIG floor (plancher) to ALL branches; do not contribute on the lower figure |
| Pension ceiling in any source citing 1,647,315 or 2,700,000 | REJECT — use XOF 3,375,000 (current since 1 Jan 2023) |
| Unknown number of CMU dependants | Compute CMU on the employee only (500 + 500); flag to confirm covered persons |
| Benefits-in-kind / indemnities | Include in the assiette (art. 23) UNLESS they are genuine expense reimbursements |
| Self-employed (RSTI) query | STOP — this skill is the régime général (salaried); RSTI uses different rates/bases. Flag for reviewer |

## Section 2 -- Required inputs and refusal catalogue

### Required inputs

- **Minimum viable** — gross monthly salary (brut) per employee, and the period (month/quarter). Without gross salary, STOP. Do not compute contributions.
- **Recommended** — employer's AT/MP risk category (1–4), total headcount (determines monthly vs quarterly payment), and number of CMU-covered persons per employee.
- **Ideal** — the CNPS appel de cotisations, the employer's immatriculation number, benefits-in-kind breakdown, and the prior DISA/DASC for reconciliation.

### Refusal catalogue

- **R-CI-CNPS-1 — Self-employed / RSTI** — Trigger: query concerns a self-employed person, independent worker, or RSTI registrant. Message: "This skill covers the salaried régime général only. The Régime Social des Travailleurs Indépendants (RSTI) uses category-based floors (XOF 30,000–150,000), a 12% rate (9% retirement + 3% other risks), and a different supplementary retirement rule. Do not apply régime général rates. Escalate to a warranted Ivorian accountant."
- **R-CI-CNPS-2 — Outdated ceiling** — Trigger: a source, prior workpaper, or the user states the pension ceiling is XOF 1,647,315 or XOF 2,700,000. Message: "Those are defunct ceilings. 1,647,315 is a legacy pre-2014 figure; 2,700,000 was 45 × 60,000 (2018 leaflet). The current pension ceiling since 1 January 2023 (décret 2022-986) is XOF 3,375,000 = 45 × SMIG (75,000). Use 3,375,000."
- **R-CI-CNPS-3 — Contribution arrears / penalties** — Trigger: client has unpaid CNPS contributions from prior periods. Message: "Arrears attract a 10% penalty plus majorations de retard, computed from the CNPS appel and statement. Do not estimate arrears without the official CNPS statement. Escalate to a warranted accountant."
- **R-CI-CNPS-4 — AT/MP risk category determination** — Trigger: user asks you to assign the work-injury risk category (and thus the 2%–5% rate). Message: "The AT/MP category is set per employer by CNPS based on sector/activity (4 categories). It cannot be self-assigned from the skill. Use 2% as a conservative placeholder and flag for reviewer to confirm the employer's official category."
- **R-CI-CNPS-5 — Public-sector / IPS-CGRAE** — Trigger: employee is a civil servant or state employee. Message: "State employees fall under IPS-CGRAE, not CNPS régime général. This skill does not cover that scheme. Escalate to a warranted accountant."

## Section 3 -- Payment pattern library

This is the deterministic pre-classifier for bank-statement and payroll transactions related to CNPS social contributions. When a transaction matches a pattern below, apply the treatment directly. Do not second-guess.

**How to read this table.** Match by case-insensitive substring on the counterparty/reference as it appears in the statement. CNPS contribution payments always EXCLUDE from any VAT/TVA return — they are statutory social charges, not taxable supplies. Employer contributions are a deductible payroll cost; the employee share is withheld from gross pay.

### 3.1 CNPS contribution débits

**3.1 CNPS contribution débits**

| Pattern | Treatment | Notes |
| --- | --- | --- |
| CNPS, PREVOYANCE SOCIALE | EXCLUDE — CNPS contribution | Monthly/quarterly appel de cotisations |
| COTISATION SOCIALE, COTISATIONS CNPS | EXCLUDE — CNPS contribution | Same |
| RETRAITE CNPS, ASSURANCE VIEILLESSE | EXCLUDE — pension branch | Pension portion |
| PRESTATIONS FAMILIALES, ALLOC FAMILIALES | EXCLUDE — family-benefits branch | Employer-only |
| ACCIDENT TRAVAIL, AT/MP | EXCLUDE — work-injury branch | Employer-only |
| APPEL DE COTISATIONS | EXCLUDE — CNPS contribution | The CNPS billing reference |

### 3.2 CMU (health) débits

**3.2 CMU (health) débits**

| Pattern | Treatment | Notes |
| --- | --- | --- |
| CMU, COUVERTURE MALADIE UNIVERSELLE | EXCLUDE — CMU health contribution | Flat XOF 500 + 500 per person/month |
| CNAM | EXCLUDE — CMU health | Caisse Nationale d'Assurance Maladie (CMU manager) |

### 3.3 CNPS débits appearing on specific Ivorian banks

**3.3 CNPS débits appearing on specific Ivorian banks**

| Bank | Typical débit description | Treatment |
| --- | --- | --- |
| SGCI (Société Générale CI) | "CNPS COTISATIONS" or "PREVOYANCE SOCIALE" | EXCLUDE — CNPS |
| BICICI | "CNPS" or "COTIS SOCIALES" | EXCLUDE — CNPS |
| Ecobank CI | "CNPS COTISATION" or "PREVOYANCE" | EXCLUDE — CNPS |
| NSIA Banque | "CNPS" or "COTISATION SOCIALE" | EXCLUDE — CNPS |
| Coris Bank | "CNPS" or "APPEL COTISATIONS" | EXCLUDE — CNPS |

### 3.4 Tax payments (NOT social contributions — do not confuse)

**3.4 Tax payments (NOT social contributions — do not confuse)**

| Pattern | Treatment | Notes |
| --- | --- | --- |
| DGI, DIRECTION GENERALE DES IMPOTS | EXCLUDE — tax, not CNPS | Income/payroll tax (ITS, etc.), not social security |
| ITS, IMPOT SUR SALAIRES | EXCLUDE — payroll tax | Not a CNPS contribution |
| TVA | EXCLUDE — VAT | Not a CNPS contribution |

### 3.5 Salary and benefit payments (exclude from CNPS classification)

**3.5 Salary and benefit payments (exclude from CNPS classification)**

| Pattern | Treatment | Notes |
| --- | --- | --- |
| SALAIRE, PAIE, VIREMENT SALAIRE (outgoing) | EXCLUDE — payroll expense | Not a contribution payment |
| PENSION CNPS, RENTE (incoming/received) | EXCLUDE — benefit received | Not a contribution paid |

## Section 4 -- Worked examples

Six classifications and computations for a hypothetical Ivorian SME employer in Abidjan. All amounts in XOF. AT/MP category assumed at 3% (a mid-band manufacturing risk) unless stated. Every figure reconciles to the unit.

### Example 1 — Employee paid exactly at the SMIG floor (XOF 75,000/month)

**Input:** Gross monthly salary = XOF 75,000. AT/MP = 3%.

**Reasoning:** Salary equals the SMIG, so floor = base for all branches; pension base is also 75,000 (well below the 3,375,000 ceiling).

**Example 1 breakdown table**

| Branch | Base | Rate | Employee | Employer |
| --- | --- | --- | --- | --- |
| Vieillesse | 75,000 | 6.3% / 7.7% | 4,725.00 | 5,775.00 |
| Prestations familiales | 75,000 | 5% | — | 3,750.00 |
| Maternité | 75,000 | 0.75% | — | 562.50 |
| AT/MP | 75,000 | 3% | — | 2,250.00 |
| CMU | flat | 500/500 | 500.00 | 500.00 |
| **Total** |  |  | **5,225.00** | **12,837.50** |

Employer % load on the 75,000 base (excl. flat CMU) = 7.7 + 5 + 0.75 + 3 = 16.45% → 12,337.50, plus CMU 500 = 12,837.50. Reconciles.

**Classification:** EXCLUDE from TVA. Employer total 12,837.50 is a deductible payroll cost; employee 5,225.00 withheld from gross.

### Example 2 — Mid-range salary, below pension ceiling (XOF 500,000/month)

**Input:** Gross monthly salary = XOF 500,000. AT/MP = 3%.

**Reasoning:** 500,000 is above the SMIG floor and below the 3,375,000 pension ceiling, so pension applies to the full 500,000. PF/Maternité/AT-MP are capped at 75,000.

**Example 2 breakdown table**

| Branch | Base | Rate | Employee | Employer |
| --- | --- | --- | --- | --- |
| Vieillesse | 500,000 | 6.3% / 7.7% | 31,500.00 | 38,500.00 |
| Prestations familiales | 75,000 (cap) | 5% | — | 3,750.00 |
| Maternité | 75,000 (cap) | 0.75% | — | 562.50 |
| AT/MP | 75,000 (cap) | 3% | — | 2,250.00 |
| CMU | flat | 500/500 | 500.00 | 500.00 |
| **Total** |  |  | **32,000.00** | **45,562.50** |

**Classification:** EXCLUDE from TVA. Employer 45,562.50 deductible; employee 32,000.00 withheld.

### Example 3 — High earner above the pension ceiling (XOF 5,000,000/month)

**Input:** Gross monthly salary = XOF 5,000,000. AT/MP = 3%.

**Reasoning:** Salary exceeds the pension ceiling, so the pension base is capped at XOF 3,375,000. PF/Maternité/AT-MP remain capped at 75,000.

**Example 3 breakdown table**

| Branch | Base | Rate | Employee | Employer |
| --- | --- | --- | --- | --- |
| Vieillesse | 3,375,000 (cap) | 6.3% / 7.7% | 212,625.00 | 259,875.00 |
| Prestations familiales | 75,000 (cap) | 5% | — | 3,750.00 |
| Maternité | 75,000 (cap) | 0.75% | — | 562.50 |
| AT/MP | 75,000 (cap) | 3% | — | 2,250.00 |
| CMU | flat | 500/500 | 500.00 | 500.00 |
| **Total** |  |  | **213,125.00** | **266,937.50** |

Pension cap check: 3,375,000 × 6.3% = 212,625.00; × 7.7% = 259,875.00. Reconciles. Note: had a source used the wrong 1,647,315 ceiling, employee pension would be only 103,780.85 — materially understated. Use 3,375,000.

**Classification:** EXCLUDE from TVA. Employer 266,937.50 deductible; employee 213,125.00 withheld.

### Example 4 — DGI/ITS débit (NOT a CNPS contribution)

**Input line:**
`15.04.2025 ; DIRECTION GENERALE DES IMPOTS ; DEBIT ; ITS MARS 2025 ; -185,000 ; XOF`

**Reasoning:** Matches "DIRECTION GENERALE DES IMPOTS" / "ITS" (pattern 3.4). This is payroll tax (impôt sur salaires) paid to the DGI, NOT a CNPS social contribution. Do not classify under CNPS branches.

**Classification:** EXCLUDE from TVA. Payroll tax (DGI), NOT a CNPS contribution.

### Example 5 — Salary above floor with low AT/MP category (XOF 200,000, AT/MP = 2%)

**Input:** Gross monthly salary = XOF 200,000. AT/MP = 2% (Category 1, low risk).

**Reasoning:** Above SMIG floor, below pension ceiling. Pension on full 200,000; other branches capped at 75,000 at the 2% AT/MP rate.

**Example 5 breakdown table**

| Branch | Base | Rate | Employee | Employer |
| --- | --- | --- | --- | --- |
| Vieillesse | 200,000 | 6.3% / 7.7% | 12,600.00 | 15,400.00 |
| Prestations familiales | 75,000 (cap) | 5% | — | 3,750.00 |
| Maternité | 75,000 (cap) | 0.75% | — | 562.50 |
| AT/MP | 75,000 (cap) | 2% | — | 1,500.00 |
| CMU | flat | 500/500 | 500.00 | 500.00 |
| **Total** |  |  | **13,100.00** | **21,712.50** |

**Classification:** EXCLUDE from TVA. Employer 21,712.50 deductible; employee 13,100.00 withheld.

### Example 6 — Ambiguous CNPS lump-sum (arrears or penalty)

**Input line:**
`20.07.2025 ; CNPS PREVOYANCE SOCIALE ; DEBIT ; REGULARISATION ; -1,450,000 ; XOF`

**Reasoning:** Matches "CNPS PREVOYANCE SOCIALE" (pattern 3.1) but the amount is irregular and the reference says "REGULARISATION." This may bundle contribution principal with a 10% penalty plus majorations de retard. Cannot separate principal from penalty without the CNPS appel/statement.

**Classification:** EXCLUDE from TVA. Flag for reviewer — request the CNPS breakdown to split contribution principal (deductible payroll cost) from penalties/majorations (treat per reviewer guidance).

## Section 5 -- Tier 1 rules

These rules apply when payroll/bank data is clear and all required inputs are available. Apply exactly as written.

### Rule 1 — Branch formulas (per employee, per month)

- **Branch formulas** — floor          = XOF 75,000                       (SMIG plancher, all branches) pension_base   = clamp(gross_salary, 75,000, 3,375,000) other_base     = clamp(gross_salary, 75,000, 75,000) = 75,000   (PF / Maternité / AT-MP capped at SMIG) Pension EE     = pension_base × 6.3% Pension ER     = pension_base × 7.7% Family (PF)    = 75,000 × 5%          (employer only) Maternity      = 75,000 × 0.75%       (employer only) AT/MP          = 75,000 × rate        (employer only; rate 2%–5% by risk category) CMU EE         = XOF 500 per covered person   (flat) CMU ER         = XOF 500 per covered person   (flat)

### Rule 2 — Pension ceiling is XOF 3,375,000

- **Pension ceiling** — The vieillesse ceiling is 45 × SMIG = 45 × 75,000 = XOF 3,375,000/month (décret 2022-986, since 1 Jan 2023). REJECT 1,647,315 (legacy) and 2,700,000 (2018 leaflet, 45 × 60,000). Only pension uses this ceiling; all other branches are capped at the SMIG (75,000).  _(décret 2022-986)_

### Rule 3 — SMIG is the floor for every branch

- **SMIG floor** — XOF 75,000/month is the contribution floor (plancher). If gross salary < 75,000, contribute on 75,000, never on the lower figure. (Apprentices under contract: ½ SMIG; otherwise full SMIG — confirm with reviewer.)

### Rule 4 — Employee bears pension + CMU only

- **Employee deductions** — The only employee deductions are pension 6.3% and CMU XOF 500/person. Family benefits, maternity, and AT/MP are 100% employer-borne. Never deduct PF/Maternité/AT-MP from the employee.

### Rule 5 — Assiette (contribution base)

- **Assiette definition** — The base is total salary including benefits-in-kind and indemnities (art. 23), EXCEPT genuine expense reimbursements (frais professionnels réels). Include before applying the floor/ceiling clamp.  _(art. 23)_

### Rule 6 — AT/MP rate by risk category

- **AT/MP category rule** — The work-injury rate is 2%–5%, set per employer by CNPS across 4 sector/risk categories (Cat. 1 ≈ 2% … Cat. 4 e.g. construction ≈ 5%). Do not invent the category — use the employer's CNPS-assigned rate; default to 2% and flag if unknown.

### Rule 7 — CMU is flat, per covered person

- **CMU flat rule** — CMU is XOF 500 employee + XOF 500 employer per person per month (XOF 1,000 total/person). It is NOT a percentage of salary. Count each covered person (employee + declared dependants).

### Rule 8 — Payment periodicity

**Payment periodicity table**

| Headcount | Periodicity | Deadline |
| --- | --- | --- |
| ≥ 20 employees | Monthly | First 15 days after month-end |
| < 20 employees | Quarterly | First 15 days after quarter-end |

### Rule 9 — Annual regularisation (DISA / DASC)

- **DISA/DASC filing** — File the DISA (Déclaration Individuelle des Salaires Annuels) and DASC (Déclaration Annuelle des Salaires et Cotisations) no later than 31 March of the following year (art. 26). CNPS provides free e-DISA software. Declarations are filed exclusively online via e.cnps.ci.  _(art. 26)_

### Rule 10 — Late penalty

- **Late penalty rule** — Late payment attracts a 10% penalty of the contributions due (art. 30 / default), plus majorations de retard (late-payment surcharges). Do not estimate penalties without the CNPS statement.  _(art. 30)_

## Section 6 -- Tier 2 catalogue

When payroll data is ambiguous or circumstances are unclear, flag these situations for reviewer confirmation.

### T2-1 — AT/MP category uncertainty

- **T2-1** — Trigger: The employer's work-injury risk category is unknown or disputed. Issue: The rate swings from 2% to 5% — a 3-point spread on the 75,000 base (XOF 1,500 vs 3,750/employee/month). Action: Use 2% as a conservative placeholder, label it, and flag for reviewer to confirm the CNPS-assigned category.

### T2-2 — Headcount near the 20-employee threshold

- **T2-2** — Trigger: Employer hovers around 20 employees during the year (seasonal/temp staff). Issue: Crossing 20 switches the obligation from quarterly to monthly payment; misclassification risks late-payment penalties. Action: Flag for reviewer to confirm the headcount basis and effective periodicity.

### T2-3 — Benefits-in-kind and indemnities in the assiette

- **T2-3** — Trigger: Employee receives housing, vehicle, or allowances alongside cash salary. Issue: Benefits-in-kind and indemnities are contributory (art. 23) unless they are genuine expense reimbursements. Misclassifying a reimbursement as salary (or vice versa) shifts the base. Action: Flag for reviewer to confirm which amounts are genuine frais professionnels.

### T2-4 — Contribution arrears / régularisation

- **T2-4** — Trigger: Unpaid CNPS contributions from prior periods. Issue: Arrears carry a 10% penalty plus majorations de retard. Principal and penalty must be separated for accounting. Action: Do not estimate. Request the CNPS appel/statement and escalate to a warranted accountant.

### T2-5 — Salary above the pension ceiling

- **T2-5** — Trigger: Employee earns more than XOF 3,375,000/month. Issue: Pension is capped at 3,375,000; the excess is NOT contributory for pension. A source citing 1,647,315 or 2,700,000 would understate the base. Action: Apply the 3,375,000 cap. Flag if any input source quoted a different ceiling.

### T2-6 — Self-employed / RSTI or public-sector employee

- **T2-6** — Trigger: Worker is self-employed (RSTI) or a civil servant (IPS-CGRAE). Issue: Different scheme, rates, and bases entirely. The régime général rates do not apply. Action: STOP. Escalate to a warranted accountant. Do not compute with this skill's rates.

## Section 7 -- Working paper template

When producing a CNPS computation, structure the working paper as follows:

```
CÔTE D'IVOIRE CNPS COMPUTATION -- WORKING PAPER
Employer: [name]                 Immatriculation CNPS: [____]
Employee: [name]                 Period: [month / quarter, year]
Prepared: [date]                 Currency: XOF

INPUT DATA
  Gross monthly salary (brut):        XOF [____]
  Benefits-in-kind / indemnities:     XOF [____]  (contributory? Y/N)
  Genuine expense reimbursements:     XOF [____]  (excluded)
  Assiette (contribution base):       XOF [____]
  AT/MP risk category / rate:         [Cat __ / __%]
  Headcount (≥20 monthly / <20 qtly): [____]
  CMU covered persons:                [____]

CLAMPS
  SMIG floor (plancher):              XOF 75,000
  Pension ceiling (45 × SMIG):        XOF 3,375,000
  Pension base = clamp(assiette,75k,3,375k): XOF [____]
  Other-branch base (= 75,000):       XOF 75,000

COMPUTATION                         Employee      Employer
  Vieillesse 6.3% / 7.7%            XOF [____]    XOF [____]
  Prestations familiales 5%              —        XOF [____]
  Maternité 0.75%                        —        XOF [____]
  AT/MP __%                               —        XOF [____]
  CMU 500 / 500 per person          XOF [____]    XOF [____]
  TOTAL                             XOF [____]    XOF [____]

PAYMENT
  Periodicity:                       [Monthly / Quarterly]
  Deadline:                          [first 15 days after period-end]
  Total due (EE + ER):               XOF [____]

ANNUAL
  DISA / DASC due:                   31 March [year+1]

REVIEWER FLAGS
  [List any Tier 2 flags here]

CONSERVATIVE DEFAULTS APPLIED
  [List any defaults applied and their impact]
```

## Section 8 -- Bank statement reading guide

### How CNPS débits appear on Ivorian bank statements

**SGCI (Société Générale Côte d'Ivoire):**
- Description: "CNPS COTISATIONS" or "PREVOYANCE SOCIALE"
- Timing: Within 15 days after month-end (≥20 staff) or quarter-end (<20 staff)
- Amount: Sum of all branches across declared employees

**BICICI / Ecobank CI / NSIA / Coris:**
- Description: "CNPS", "COTISATION SOCIALE", "APPEL COTISATIONS", or "PREVOYANCE"
- Timing: Same monthly/quarterly cycle
- Amount: Matches the CNPS appel de cotisations

**CMU débits:**
- Description: "CMU", "COUVERTURE MALADIE UNIVERSELLE", or "CNAM"
- Amount: XOF 1,000 × number of covered persons (500 EE + 500 ER)

**Key identification tips:**
1. CNPS contribution débits are always outgoing, never credits (an incoming "PENSION CNPS" is a benefit received, not a contribution).
2. They recur monthly or quarterly with amounts tied to the appel de cotisations.
3. Do not confuse with DGI/ITS débits (payroll tax) or TVA (VAT) — those are tax, not social security.
4. Régularisation lump sums may bundle principal with the 10% penalty + majorations — flag for breakdown.

## Section 9 -- Onboarding fallback

If the employer provides only a bank statement and no payroll detail:

1. **Scan for CNPS débits** — identify all outgoing payments matching Section 3 patterns.
2. **Sum contributions paid** — total all CNPS and CMU débits in the period.
3. **Reverse-engineer roughly:**
   - Employer load on the first XOF 75,000 per employee ≈ 16.45%–18.45% (7.7% pension + 5% PF + 0.75% maternity + 2%–5% AT/MP) plus flat CMU.
   - Above 75,000 (up to 3,375,000), only the 7.7% employer / 6.3% employee pension continues.
4. **Flag for reviewer:** "CNPS classification derived from bank-statement amounts only. AT/MP category, headcount basis, and per-employee assiette have not been independently verified. Reviewer must confirm against the CNPS appel before filing the DISA/DASC."

## Section 10 -- Reference material

### Calculation examples (2025, AT/MP at 3% unless noted)

**Calculation examples table**

| Gross monthly salary | Pension base | Pension EE (6.3%) | Pension ER (7.7%) | Employer other branches (5% + 0.75% + AT%) on 75,000 | CMU (EE/ER) |
| --- | --- | --- | --- | --- | --- |
| XOF 75,000 | 75,000 | 4,725.00 | 5,775.00 | 6,562.50 (@3%) | 500 / 500 |
| XOF 200,000 | 200,000 | 12,600.00 | 15,400.00 | 5,812.50 (@2%) | 500 / 500 |
| XOF 500,000 | 500,000 | 31,500.00 | 38,500.00 | 6,562.50 (@3%) | 500 / 500 |
| XOF 3,375,000 | 3,375,000 | 212,625.00 | 259,875.00 | 6,562.50 (@3%) | 500 / 500 |
| XOF 5,000,000 | 3,375,000 (cap) | 212,625.00 | 259,875.00 | 6,562.50 (@3%) | 500 / 500 |

"Other branches" at 3% = 75,000 × (5% + 0.75% + 3%) = 75,000 × 8.75% = 6,562.50. At 2% = 75,000 × 7.75% = 5,812.50. Reconciles.

### Self-employed (RSTI) — out of scope, for awareness only

12% (9% retirement + 3% other risks) on a category-based floor (XOF 30,000–150,000); +9% supplementary retirement on income above XOF 180,000; CMU XOF 1,000/month; no pension ceiling like the régime général. Do NOT apply these to salaried employees. [Use the RSTI workflow / escalate.]

### Registration and forms

- **Employer immatriculation:** "Déclaration aux fins d'immatriculation" via GUFE/CEPICI at company creation or at a CNPS agency; effective from first hire (art. 5).
- **Employee declaration:** "fiche de déclaration du travailleur" via CEPICI, e-CNPS, or agency; effective first day of work.
- **Cessation:** "fiche de déclaration de cessation d'emploi" on departure.

### Penalties

**Penalties table**

| Item | Treatment |
| --- | --- |
| Late payment | 10% of contributions due |
| Late-payment surcharge | Majorations de retard (per CNPS statement) |
| Non-declaration | All unpaid contributions + penalties recoverable by CNPS |

### Test suite

**Test 1:** Gross XOF 75,000, AT/MP 3%. → Pension EE 4,725.00 / ER 5,775.00; PF 3,750.00; Maternité 562.50; AT/MP 2,250.00; CMU 500/500. Employee total 5,225.00; Employer total 12,837.50.

**Test 2:** Gross XOF 500,000, AT/MP 3%. → Pension EE 31,500.00 / ER 38,500.00; PF 3,750.00; Maternité 562.50; AT/MP 2,250.00; CMU 500/500. Employee total 32,000.00; Employer total 45,562.50.

**Test 3:** Gross XOF 5,000,000, AT/MP 3%. → Pension base capped at 3,375,000 → EE 212,625.00 / ER 259,875.00; PF 3,750.00; Maternité 562.50; AT/MP 2,250.00; CMU 500/500. Employee total 213,125.00; Employer total 266,937.50.

**Test 4:** Gross XOF 200,000, AT/MP 2%. → Pension EE 12,600.00 / ER 15,400.00; PF 3,750.00; Maternité 562.50; AT/MP 1,500.00; CMU 500/500. Employee total 13,100.00; Employer total 21,712.50.

**Test 5:** Gross XOF 50,000 (below SMIG). → Apply floor 75,000. Same as Test 1. Never contribute on 50,000.

**Test 6:** Source quotes pension ceiling 1,647,315. → REJECT. Use 3,375,000.

**Test 7:** Employer with 30 employees. → Monthly payment, due within 15 days of month-end.

**Test 8:** Employer with 8 employees. → Quarterly payment, due within 15 days of quarter-end. DISA/DASC by 31 March following.

**Test 9:** Pension exactly at ceiling, gross XOF 3,375,000. → EE 212,625.00 / ER 259,875.00 (no excess contributory).

### Prohibitions

- NEVER use the XOF 1,647,315 or 2,700,000 pension ceiling — the current ceiling is XOF 3,375,000.
- NEVER contribute on a salary below the XOF 75,000 SMIG floor — always apply the floor.
- NEVER apply the pension ceiling (3,375,000) to PF/Maternité/AT-MP — those are capped at 75,000.
- NEVER deduct family benefits, maternity, or AT/MP from the employee — they are employer-only.
- NEVER compute CMU as a percentage — it is flat XOF 500 + 500 per covered person.
- NEVER invent the AT/MP risk category — use the employer's CNPS-assigned rate; default 2% and flag.
- NEVER apply régime général rates to a self-employed (RSTI) or public-sector (IPS-CGRAE) worker.
- NEVER estimate arrears or penalties without the CNPS appel/statement.
- NEVER present figures as definitive — label as estimated and direct the client to their CNPS appel de cotisations.

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as an expert-comptable, CPA, EA, tax attorney, or equivalent licensed practitioner in your jurisdiction) before filing or acting upon.

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
