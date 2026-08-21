---
name: ivory-coast-payroll
description: Use this skill whenever asked about Côte d'Ivoire (Ivory Coast) payroll processing for employed persons. Trigger on phrases like "Ivory Coast payroll", "Côte d'Ivoire payroll", "ITS", "Impôt sur les Traitements et Salaires", "salary tax Côte d'Ivoire", "CNPS contributions", "CNPS retraite", "prestations familiales", "FDFP levy", "taxe d'apprentissage", "contribution employeur", "expatriate payroll tax Ivory Coast", "RICF family reduction", "SMIG", "CMU", "DISA", "net salary Côte d'Ivoire", "gross to net XOF", "FCFA payroll", "e-Impôts", or any question about computing employee pay, salary withholding tax, or social security contributions for Ivory Coast-based employees. This skill covers ITS progressive income-tax withholding, the RICF family-charge reduction, CNPS social contributions (employee and employer), the employer payroll tax (local vs expatriate), FDFP training levies, CMU, minimum wage, and filing obligations to the DGI and CNPS. ALWAYS read this skill before processing any Côte d'Ivoire payroll.
version: 0.1
jurisdiction: CI
tax_year: 2025
last_updated: 2026-07-13
review_status: pending_review
depends_on:
  - payroll-workflow-base
category: payroll
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Côte d'Ivoire (Ivory Coast) Payroll

## Côte d'Ivoire (Ivory Coast) Payroll Skill v0.1

> **Tier 2 — research-verified, pending accountant sign-off.** Every figure below carries an inline source or an explicit `[RESEARCH GAP — reviewer to confirm]` marker. Do not treat any output as final until a licensed Ivorian accountant (expert-comptable inscrit à l'Ordre) has reviewed it.

## Section 1 — Quick Reference

**Quick Reference table**

| Field | Value |
| --- | --- |
| Country | Côte d'Ivoire (Republic of Côte d'Ivoire / Ivory Coast) |
| Currency | West African CFA franc (XOF / FCFA) only |
| Standard pay frequency | Monthly |
| Tax year | Calendar year (1 January — 31 December) |
| Income tax on salary | **YES** — single progressive ITS (Impôt sur les Traitements et Salaires) |
| Tax withholding system | ITS withheld at source by employer, declared/paid via e-Impôts |
| Tax authority | Direction Générale des Impôts (DGI) — [e-impots.gouv.ci](https://e-impots.gouv.ci/) |
| Social security authority | Caisse Nationale de Prévoyance Sociale (CNPS) — [cnps.ci](https://www.cnps.ci/) |
| Training-levy authority | Fonds de Développement de la Formation Professionnelle (FDFP) |
| Key legislation | Code Général des Impôts (CGI) Art. 119 bis (ITS scale), Art. 120 (RICF), Art. 138 (payment); Ordonnance n° 2023-719 of 13 Sept 2023 (ITS reform, effective 1 Jan 2024) |
| Minimum wage (SMIG) | 75,000 XOF/month (Decree n° 2022-986, in force since 1 Jan 2023) |
| Validated by | Pending — requires sign-off by an Ivorian expert-comptable |
| Skill version | 0.1 |

> **Reform alert.** Ordonnance n° 2023-719 (13 Sept 2023) merged the three former salary taxes — the proportional IS, the Contribution Nationale (CN), and the IGR — into a **single progressive ITS**, effective **1 January 2024**. The old "IGR + CN + IS" stack that many legacy calculators still show is **OBSOLETE**. Do NOT use it. (Source: PwC Ivory Coast — Taxes on personal income, last reviewed Mar 2026, https://taxsummaries.pwc.com/ivory-coast/individual/taxes-on-personal-income)

## Section 2 — Income Tax Withholding (ITS)

The employer withholds the **ITS** monthly at source on each employee's gross taxable salary (cash pay plus benefits in kind), applies the progressive scale, then deducts the fixed RICF family-charge reduction, and remits the net to the DGI.

### 2.1 Progressive Monthly Scale — CGI Article 119 bis (current, 2024–)

**Progressive Monthly Scale**  _(CGI Art. 119 bis, reproduced at loidici.biz (https://loidici.biz/2025/02/21/67781/), and PwC Ivory Coast (https://taxsummaries.pwc.com/ivory-coast/individual/taxes-on-personal-income))_

| Monthly taxable income (XOF) | Marginal rate | Cumulative ITS at top of band (XOF) |
| --- | --- | --- |
| 0 — 75,000 | 0% | 0 |
| 75,001 — 240,000 | 16% | 26,400 |
| 240,001 — 800,000 | 21% | 144,000 |
| 800,001 — 2,400,000 | 24% | 528,000 |
| 2,400,001 — 8,000,000 | 28% | 2,096,000 |
| Above 8,000,000 | 32% | — (no ceiling) |

The 0% floor of 75,000 XOF coincides exactly with the SMIG.

- 75,000 → 0
- 240,000 → 0 + 16% × 165,000 = 26,400
- 800,000 → 26,400 + 21% × 560,000 = 144,000
- 2,400,000 → 144,000 + 24% × 1,600,000 = 528,000
- 8,000,000 → 528,000 + 28% × 5,600,000 = 2,096,000

> `[RESEARCH GAP — reviewer to confirm]` **Professional abatement.** The pre-reform regime applied a 20% professional abatement before the old scale. Under the unified ITS, PwC presents the scale as applied to **gross** taxable salary, and this skill follows that (no standalone abatement). A separate abatement percentage under the new law could **not** be confirmed from a primary source (the DGI/Deloitte rate images did not render to text). Reviewer must confirm whether any abatement still applies before signing off.

### 2.2 Family-Charge Reduction — RICF, CGI Article 120

- **RICF definition** — The Réduction d'Impôt pour Charges de Famille (RICF) replaces the old family-quotient system. It is a fixed XOF amount subtracted from the gross monthly ITS — NOT a percentage. Parts run from 1 to 5: the employee receives 1 part, +0.5 part per dependent child (and the configuration of the household), up to a maximum of 5 parts.  _(CGI Art. 120)_

**RICF table**  _(CGI Art. 120 via loidici.biz (https://loidici.biz/2025/02/21/67781/))_

| Parts | Monthly reduction (XOF) | Annual reduction (XOF) |
| --- | --- | --- |
| 1 | 0 | 0 |
| 1.5 | 5,500 | 66,000 |
| 2 | 11,000 | 132,000 |
| 2.5 | 16,500 | 198,000 |
| 3 | 22,000 | 264,000 |
| 3.5 | 27,500 | 330,000 |
| 4 | 33,000 | 396,000 |
| 4.5 | 38,500 | 462,000 |
| 5 | 44,000 | 528,000 |

- **RICF increment rule** — 11,000 XOF/month per additional full part, 5,500 XOF per half-part.  _(CGI Art. 120 via loidici.biz (https://loidici.biz/2025/02/21/67781/))_

> `[RESEARCH GAP — reviewer to confirm]` The annual figure for 5 parts rendered inconsistently in one extraction (showed "328,000"). **528,000** is the arithmetically consistent value (44,000 × 12 = 528,000) and is used here, but the reviewer must confirm against the official CGI text.

- **Net ITS formula** — Net ITS = gross ITS (from §2.1 scale) − RICF reduction (from §2.2 table), floored at 0.  _(CGI Art. 120)_

### 2.3 ITS Filing & Payment

**ITS Filing & Payment table**

| Item | Detail | Source |
| --- | --- | --- |
| Withholding | Monthly at source by employer | CGI Art. 119 bis / DGI |
| Declaration & payment | By the **15th of the following month** via e-Impôts ([e-impots.gouv.ci](https://e-impots.gouv.ci/)) | DGI fiscal calendar (CALENDRIER.pdf); corroborated by multiple guides |
| Small-withholding option (CGI Art. 138) | If monthly ITS ≤ 1,000 XOF, may pay semi-annually (by 15 Jul / 15 Jan). But if in any month the amount exceeds 5,000 XOF, all sums due for the current semester fall due within the first 15 days of the following month. | CGI Art. 138 |
| Late penalty | 25% surcharge on the amount due, **plus** 2% interest per month of delay | DGI / PwC |

> `[RESEARCH GAP — reviewer to confirm]` The DGI calendar PDF did not render to text, so whether the ITS deadline shifts by taxpayer regime (DGE large enterprises vs CME/SME) is unconfirmed. The commonly cited date is the **15th of the following month**.

## Section 3 — CNPS Social Contributions (effective 1 January 2025)

CNPS contributions are split across five branches. Two distinct monthly base ceilings apply: **3,375,000 XOF** for retirement; **70,000 XOF** for family allowances, maternity, and work-injury. CMU is a flat per-person amount.

### 3.1 Contribution Table (effective 1 Jan 2025)

**Contribution Table**  _(CLEISS — Les cotisations en Côte d'Ivoire, effective 1 Jan 2025 (https://www.cleiss.fr/docs/cotisations/cotedivoire.html); PwC Ivory Coast — Other taxes (https://taxsummaries.pwc.com/ivory-coast/individual/other-taxes); CNPS (https://www.cnps.ci/))_

| Branch | Employee | Employer | Total | Monthly base ceiling (XOF) |
| --- | --- | --- | --- | --- |
| Retirement / old-age (assurance vieillesse) | 6.30% | 7.70% | 14.00% | 3,375,000 |
| Family allowances (prestations familiales) | 0% | 5.00% | 5.00% | 70,000 |
| Maternity (assurance maternité) | 0% | 0.75% | 0.75% | 70,000 |
| Work injury / occupational disease (AT/MP) | 0% | 2%–5% (by sector risk) | 2%–5% | 70,000 |
| CMU (universal health coverage) | 500 XOF/person/mo (flat) | 500 XOF/person/mo (flat) | 1,000 XOF/person/mo | flat (no %) |

**Percentage totals (self-checked, excluding flat CMU and excluding the variable AT/MP range):**
- **Employee %:** 6.30% (retirement only).
- **Employer %:** 7.70% (retirement) + 5.00% (family) + 0.75% (maternity) + AT/MP (2%–5%) = **15.45% to 18.45%**.
- Family + maternity are frequently quoted together as **5.75%** (5.00% + 0.75%), entirely employer-borne.
- Plus 500 XOF/person CMU on each side (flat).

> `[RESEARCH GAP — reviewer to confirm]` The **AT/MP work-injury rate is sector-specific (2%–5%)**, set by the employer's CNPS risk classification. The exact rate for a given employer must be confirmed from its CNPS notification before payroll is finalised. Worked examples below assume a placeholder; reviewer to substitute the real rate.

### 3.2 CNPS Filing & Payment

**CNPS Filing & Payment table**

| Item | Detail | Source |
| --- | --- | --- |
| Periodicity | **Monthly** if ≥ 20 employees; **quarterly** if < 20 employees | CLEISS |
| Deadline | Within the first **15 days** following the month/quarter end | CLEISS |
| Filing channel | Online via e-CNPS (https://e.cnps.ci/) | CNPS |
| DISA (Déclaration Individuelle des Salaires Annuels) | Annual salary declaration due **by 31 March** of the following year | CNPS DISA form |
| Late penalty (contributions) | **5%** surcharge for the first month, then **1%** per additional month | CLEISS |
| DISA non-filing penalty | **10%** of total monthly contributions due | CNPS / CLEISS |

## Section 4 — Employer Payroll Tax (Contribution Employeur / Taxe sur Salaires)

**Employer payroll tax table**  _(PwC Ivory Coast — Corporate — Other taxes (https://taxsummaries.pwc.com/ivory-coast/corporate/other-taxes); confirmed on PwC individual/other-taxes)_

| Category | Rate |
| --- | --- |
| Local employees | 2.8% |
| Expatriate employees | 12% |

- **Expatriate definition** — "Expatriate" status follows from an expatriate employment contract approved by the Agence Emploi Jeune (AEJ) — it is determined by contract type, not strictly nationality. Confirm the contract classification before applying the 12% rate.  _(PwC Ivory Coast — Corporate — Other taxes)_

## Section 5 — FDFP Training Levies (employer-borne, on total payroll / masse salariale)

**FDFP Training Levies table**  _(FDFP via eRegulations CI (https://cotedivoire.eregulations.org/media/taxe%20fdfp.pdf); FDFP (https://fdfp.ci/presentation-du-fdfp/))_

| Levy | Rate |
| --- | --- |
| Taxe d'apprentissage (apprenticeship tax) | 0.4% of payroll |
| Taxe additionnelle à la formation professionnelle continue (continuing vocational training) | 1.2% of payroll |

- **Combined FDFP employer cost** — 1.6% of payroll (0.4% + 1.2%)  _(FDFP via eRegulations CI)_

## Section 6 — Minimum Wage (SMIG / SMAG)

**Minimum wage table**

| Category | Monthly amount | Source |
| --- | --- | --- |
| SMIG (general minimum wage) | 75,000 XOF | Decree n° 2022-986 of 21 Dec 2022, in force since 1 Jan 2023 |
| SMAG (agricultural minimum wage) | 39,960 XOF | Decree n° 2022-986 |

Source: secondary (guidedufonctionnaire.com, citing Decree n° 2022-986). The 75,000 XOF SMIG aligns exactly with the ITS 0% threshold and is widely corroborated; unchanged through 2025/2026 as of latest reporting.

> `[RESEARCH GAP — reviewer to confirm]` Only secondary sources were fetched for the SMIG/SMAG amounts. Confirm against the official decree text.

## Section 7 — Conservative Defaults

When a required input is ambiguous or missing, apply the most cautious assumption and flag it. Never silently pick a favourable value.

**Conservative Defaults table**

| Unknown | Conservative default | Rationale |
| --- | --- | --- |
| Number of RICF parts | **1 part (zero reduction)** | Never assume dependants; under-claiming RICF over-withholds ITS (employee can reclaim), over-claiming under-withholds (employer liable). |
| Employee/expatriate status | **Expatriate (12% employer payroll tax)** only if a contract clearly shows AEJ-approved expatriate terms; otherwise default to **local (2.8%)** and flag for confirmation | 12% should not be applied without contract evidence; but flag because misclassification cuts both ways. |
| AT/MP work-injury rate | **5% (top of band)** for accrual until the CNPS risk-class notification is sighted | Avoids under-accruing the employer liability. |
| Benefits in kind | **Include in ITS taxable base and employer-payroll-tax base** unless proven exempt | The scale applies to gross including benefits in kind. |
| Professional abatement | **Apply none** (scale on gross) per PwC | See §2.1 research gap; conservative = no abatement = higher withholding. |
| Filing periodicity | If headcount unknown, assume **monthly** CNPS filing | Monthly is stricter than quarterly. |
| Pay currency | **XOF/FCFA** — refuse any other currency | No foreign-currency payroll. |

## Section 8 — Required Inputs & Refusal Catalogue

### 8.1 Required Inputs

Before computing, you MUST have:

1. **Gross monthly remuneration in XOF** (cash + allowances + benefits in kind).
2. **RICF parts** (or the data to derive them: marital configuration + number of dependent children).
3. **Local vs expatriate status** (contract classification per AEJ).
4. **Employer headcount** (to set CNPS periodicity: ≥20 monthly, <20 quarterly).
5. **CNPS AT/MP risk-class rate** for the employer (2%–5%).
6. **Number of CMU-covered persons** per employee (for the flat 500 XOF/person each side).

### 8.2 Refusal Catalogue — STOP and refuse if:

**Refusal Catalogue table**

| Trigger | Action |
| --- | --- |
| Remuneration given in EUR, USD, or any non-XOF currency | Refuse; request XOF figures. No FX conversion in payroll. |
| Pre-2024 "IGR + CN + IS" stack requested | Refuse the obsolete method; explain the 2024 ITS reform (Ord. 2023-719) and offer the unified ITS. |
| Asked to apply the 12% expatriate rate without contract evidence | Refuse; require AEJ contract classification. |
| Asked to skip CNPS or FDFP "to save cost" | Refuse; these are statutory employer obligations. |
| Asked to treat ITS/CNPS as final without accountant sign-off | Refuse to label as final; output is Tier 2 estimate only. |
| Net-pay calc requested with no RICF / dependant data | Proceed only on the **1-part** conservative default, clearly flagged. |
| Sub-SMIG salary (< 75,000 XOF, non-agricultural) | Flag as below statutory minimum; do not normalise it. |

## Section 9 — Transaction / Payment Pattern Library (deterministic)

Map gross pay through statutory deductions and employer charges in this fixed order. Bookkeeping classification follows.

### 9.1 Computation order (deterministic)

- **Computation order** — 1. Determine **gross taxable salary** (cash + benefits in kind), in XOF. 2. **Gross ITS** = apply §2.1 progressive scale to gross taxable salary. 3. **Net ITS** = gross ITS − §2.2 RICF reduction (floor 0). 4. **Employee CNPS** = 6.30% × min(gross, 3,375,000) + 500 XOF/person CMU. 5. **Net pay** = gross − net ITS − employee CNPS share. 6. **Employer CNPS** = 7.70% × min(gross, 3,375,000) + 5.75% × min(gross, 70,000) + AT/MP% × min(gross, 70,000) + 500 XOF/person CMU. 7. **Employer payroll tax** = 2.8% (local) or 12% (expatriate) × gross taxable remuneration. 8. **FDFP** = 1.6% × payroll (0.4% apprenticeship + 1.2% continuing training).

### 9.2 Bookkeeping classification

**Bookkeeping classification table**

| Item | Account treatment |
| --- | --- |
| Gross salary | Expense (charges de personnel) |
| Employer CNPS, employer payroll tax, FDFP | Expense (charges sociales / charges fiscales) |
| Net ITS withheld | Liability to DGI until remitted (by the 15th) |
| Employee CNPS + CMU withheld | Liability to CNPS until remitted |
| Net pay | Liability to employee until paid; then cash out |

## Section 10 — Worked Examples

> All examples assume **gross = monthly taxable salary in XOF**, no benefits in kind unless stated, and an **AT/MP placeholder of 3%** (mid-band) — reviewer to substitute the employer's actual risk rate. CMU assumes **1 covered person** (500 XOF each side). All arithmetic self-checked to the franc.

### Example 1 — Single employee at the SMIG, 75,000 XOF, 1 part

- Gross ITS: income is at the 0% floor → **0**.
- RICF (1 part): 0.
- **Net ITS = 0.**
- Employee CNPS retirement: 6.30% × 75,000 = 4,725. CMU: 500. Employee deductions = **5,225**.
- **Net pay = 75,000 − 0 − 5,225 = 69,775 XOF.**
- Employer CNPS: 7.70% × 75,000 = 5,775 (retirement); family+maternity 5.75% × 70,000 (capped) = 4,025; AT/MP 3% × 70,000 = 2,100; CMU 500 → employer CNPS = **12,400**.
- Employer payroll tax (local 2.8%): 2,100. FDFP 1.6%: 1,200.
- **Total employer cost = 75,000 + 12,400 + 2,100 + 1,200 = 90,700 XOF.**

### Example 2 — Single employee, 500,000 XOF, 1 part

- Gross ITS (scale): 0 (first 75,000) + 16% × 165,000 = 26,400 + 21% × (500,000 − 240,000 = 260,000) = 54,600 → **81,000**.
- RICF (1 part): 0. **Net ITS = 81,000.**
- Employee CNPS: 6.30% × 500,000 = 31,500 + CMU 500 = **32,000**.
- **Net pay = 500,000 − 81,000 − 32,000 = 387,000 XOF.**
- Employer CNPS: 7.70% × 500,000 = 38,500 + 5.75% × 70,000 = 4,025 + 3% × 70,000 = 2,100 + CMU 500 = **45,125**.
- Employer payroll tax (2.8%): 14,000. FDFP (1.6%): 8,000.
- **Total employer cost = 500,000 + 45,125 + 14,000 + 8,000 = 567,125 XOF.**

### Example 3 — Married employee, 2 children (3 parts), 500,000 XOF

- Gross ITS (scale): **81,000** (as Example 2).
- RICF (3 parts): 22,000. **Net ITS = 81,000 − 22,000 = 59,000.**
- Employee CNPS: 31,500 + CMU (assume 1 person) 500 = **32,000**.
- **Net pay = 500,000 − 59,000 − 32,000 = 409,000 XOF.**
- Employer side identical to Example 2: employer CNPS 45,125, payroll tax 14,000, FDFP 8,000.
- **Total employer cost = 567,125 XOF** (unchanged; RICF affects only employee ITS).

### Example 4 — Senior local employee, 1,000,000 XOF, 1 part

- Gross ITS (scale): 26,400 (to 240,000) + 21% × 560,000 = 117,600 (to 800,000) → 144,000 + 24% × (1,000,000 − 800,000 = 200,000) = 48,000 → **192,000**.
- RICF (1 part): 0. **Net ITS = 192,000.**
- Employee CNPS: 6.30% × 1,000,000 = 63,000 + CMU 500 = **63,500**.
- **Net pay = 1,000,000 − 192,000 − 63,500 = 744,500 XOF.**
- Employer CNPS: 7.70% × 1,000,000 = 77,000 + 5.75% × 70,000 = 4,025 + 3% × 70,000 = 2,100 + CMU 500 = **83,625**.
- Employer payroll tax (2.8%): 28,000. FDFP (1.6%): 16,000.
- **Total employer cost = 1,000,000 + 83,625 + 28,000 + 16,000 = 1,127,625 XOF.**

### Example 5 — Expatriate executive, 4,000,000 XOF, 1 part

- Gross ITS (scale): 528,000 (to 2,400,000) + 28% × (4,000,000 − 2,400,000 = 1,600,000) = 448,000 → **976,000**.
- RICF (1 part): 0. **Net ITS = 976,000.**
- Employee CNPS retirement is capped at base 3,375,000: 6.30% × 3,375,000 = 212,625 + CMU 500 = **213,125**.
- **Net pay = 4,000,000 − 976,000 − 213,125 = 2,810,875 XOF.**
- Employer CNPS: retirement 7.70% × 3,375,000 (capped) = 259,875 + family/maternity 5.75% × 70,000 = 4,025 + AT/MP 3% × 70,000 = 2,100 + CMU 500 = **266,500**.
- Employer payroll tax (**expatriate 12%**): 12% × 4,000,000 = 480,000. FDFP (1.6%): 64,000.
- **Total employer cost = 4,000,000 + 266,500 + 480,000 + 64,000 = 4,810,500 XOF.**

### Example 6 — High earner above the top band, 10,000,000 XOF, 1 part

- Gross ITS (scale): 2,096,000 (to 8,000,000) + 32% × (10,000,000 − 8,000,000 = 2,000,000) = 640,000 → **2,736,000**.
- RICF (1 part): 0. **Net ITS = 2,736,000.**
- Employee CNPS: capped — 6.30% × 3,375,000 = 212,625 + CMU 500 = **213,125**.
- **Net pay = 10,000,000 − 2,736,000 − 213,125 = 7,050,875 XOF.**
- Employer CNPS: 7.70% × 3,375,000 = 259,875 + 5.75% × 70,000 = 4,025 + 3% × 70,000 = 2,100 + CMU 500 = **266,500**.
- Employer payroll tax (local 2.8%): 280,000. FDFP (1.6%): 160,000.
- **Total employer cost = 10,000,000 + 266,500 + 280,000 + 160,000 = 10,706,500 XOF.**

## Section 11 — Tier 1 Rules (always apply — no judgement)

- **Tier 1 Rules** — 1. **Currency is XOF/FCFA.** Refuse any other currency. 2. **Use the unified ITS scale (CGI Art. 119 bis), not the pre-2024 IGR/CN/IS stack.** 3. **Apply the progressive scale to gross taxable salary** (cash + benefits in kind), per §2.1. 4. **Subtract RICF (CGI Art. 120) after computing gross ITS**, never before; floor net ITS at 0. 5. **Employee CNPS = 6.30% retirement only** (plus flat CMU). The employee does NOT pay family allowances, maternity, AT/MP, or the employer payroll tax. 6. **Cap retirement contributions** on a monthly base of 3,375,000 XOF; **cap family/maternity/AT-MP** on 70,000 XOF. 7. **Employer payroll tax: 2.8% local / 12% expatriate** — apply 12% only with AEJ contract evidence. 8. **FDFP = 1.6%** of payroll (0.4% + 1.2%), employer-borne. 9. **ITS remitted to DGI by the 15th** of the following month; CNPS by the 15th (monthly if ≥20 staff, quarterly if <20). 10. **Never present output as final** — Tier 2 estimate pending accountant sign-off.

## Section 12 — Tier 2 Catalogue (reviewer judgement required)

These items require an Ivorian expert-comptable to confirm before sign-off:

1. **Professional abatement** under the unified ITS — confirm none applies (or supply the rate). [§2.1 gap]
2. **RICF derivation of parts** — confirm how marital configuration + children map to 1–5 parts and the half-part increments for the specific household.
3. **RICF 5-part annual value** (528,000 vs the "328,000" extraction glitch). [§2.2 gap]
4. **AT/MP risk-class rate** for the employer (2%–5%). [§3.1 gap]
5. **Benefits-in-kind valuation** rules for the ITS and employer-payroll-tax bases.
6. **Expatriate classification** under the AEJ contract regime.
7. **ITS deadline by taxpayer regime** (DGE vs CME). [§2.3 gap]
8. **SMIG/SMAG** confirmation against the official Decree n° 2022-986. [§6 gap]
9. **CMU counting** — number of covered persons per employee.
10. **Small-withholding semi-annual option** eligibility (CGI Art. 138).

## Section 13 — Excel Working Paper Template

**Excel Working Paper Template**

| Col | Header | Formula / source |
| --- | --- | --- |
| A | Employee name | input |
| B | Gross taxable salary | input (cash + benefits in kind) |
| C | RICF parts | input (1–5) |
| D | Gross ITS | progressive scale on B (§2.1) |
| E | RICF reduction | lookup on C (§2.2) |
| F | Net ITS | =MAX(D − E, 0) |
| G | Employee CNPS retirement | =6.30% × MIN(B, 3,375,000) |
| H | CMU (employee) | =500 × persons |
| I | Net pay | =B − F − G − H |
| J | Employer CNPS retirement | =7.70% × MIN(B, 3,375,000) |
| K | Employer family+maternity | =5.75% × MIN(B, 70,000) |
| L | Employer AT/MP | =rate% × MIN(B, 70,000) |
| M | CMU (employer) | =500 × persons |
| N | Employer payroll tax | =IF(expat, 12%, 2.8%) × B |
| O | FDFP | =1.6% × B |
| P | Total employer cost | =B + J + K + L + M + N + O |

Control totals: sum of F → DGI liability; sum of (G+H+J+K+L+M) → CNPS liability; sum of N → employer payroll-tax liability; sum of O → FDFP liability.

## Section 14 — Bank Statement / Terminology Reading Guide

Statements and payroll documents are typically in **French**. Common terms and patterns:

### 14.1 Salary credits (employee view)

**Salary credits table**

| Pattern (French) | Meaning |
| --- | --- |
| SALAIRE, PAIE, VIREMENT SALAIRE | Net salary payment |
| NET À PAYER | Net pay line on payslip |
| AVANTAGES EN NATURE | Benefits in kind (taxable) |
| PRIME, INDEMNITÉ | Bonus / allowance (check taxability) |

### 14.2 Employer debit patterns

**Employer debit patterns table**

| Pattern (French) | Meaning |
| --- | --- |
| DGI ITS, IMPÔT SUR SALAIRES, e-IMPÔTS | ITS remittance to the DGI |
| CNPS, COTISATION CNPS, e-CNPS | CNPS contribution remittance |
| CMU | Universal health coverage flat contribution |
| FDFP, TAXE APPRENTISSAGE, FPC | FDFP training levies |
| CONTRIBUTION EMPLOYEUR, TAXE SUR SALAIRES | Employer payroll tax (2.8% / 12%) |

### 14.3 Glossary

**Glossary table**

| French | English |
| --- | --- |
| Impôt sur les Traitements et Salaires (ITS) | Salary income tax |
| Réduction pour Charges de Famille (RICF) | Family-charge reduction |
| Masse salariale | Total payroll |
| Caisse Nationale de Prévoyance Sociale (CNPS) | National social-security fund |
| Prestations familiales | Family allowances |
| Assurance vieillesse | Old-age / retirement insurance |
| Accident du travail / maladie professionnelle (AT/MP) | Work injury / occupational disease |
| DISA | Annual individual salary declaration |
| SMIG / SMAG | Minimum wage (general / agricultural) |

## Section 15 — Onboarding Fallback

- **Onboarding fallback order** — If the engagement lacks key data, proceed in this order: 1. **No RICF/dependant data** → compute on **1 part** (zero reduction), flag the employee can reclaim over-withheld ITS. 2. **No headcount** → assume **monthly** CNPS filing (stricter). 3. **No AT/MP notification** → accrue at **5%** (top of band), flag for correction. 4. **No contract classification** → treat as **local (2.8%)**, flag to confirm against AEJ status before any 12% application. 5. **No CMU person count** → assume **1 person** (500 XOF each side), flag. 6. **No benefit-in-kind values** → request them; do not omit from the taxable base. 7. **Any obsolete-method request** → redirect to the unified ITS (Ord. 2023-719). Always hand off to an Ivorian expert-comptable for final sign-off.

## Section 16 — Reference Material

**Reference Material summary table**  _(see per-row sources)_

| Item | Value | Source |
| --- | --- | --- |
| ITS scale | 0/16/21/24/28/32% (§2.1) | CGI Art. 119 bis; PwC |
| RICF | fixed 11,000 XOF/part-month (§2.2) | CGI Art. 120 |
| ITS deadline | 15th of following month | DGI calendar (commonly cited) `[RESEARCH GAP]` |
| ITS late penalty | 25% + 2%/month | DGI / PwC |
| CNPS retirement | 6.30% EE / 7.70% ER; cap 3,375,000/mo | CLEISS (eff. 1 Jan 2025) |
| Family + maternity | 5.75% ER; cap 70,000/mo | CLEISS |
| AT/MP | 2%–5% ER; cap 70,000/mo | CLEISS / CNPS `[RESEARCH GAP — sector rate]` |
| CMU | 500 XOF/person each side | CLEISS / PwC |
| CNPS periodicity | monthly ≥20 / quarterly <20; due day 15 | CLEISS |
| CNPS late penalty | 5% first month, then 1%/month | CLEISS |
| DISA | due 31 March; 10% non-filing penalty | CNPS |
| Employer payroll tax | 2.8% local / 12% expat | PwC |
| FDFP | 0.4% + 1.2% = 1.6% | FDFP / eRegulations CI |
| SMIG / SMAG | 75,000 / 39,960 XOF | Decree n° 2022-986 `[RESEARCH GAP — secondary]` |
| VAT (context only) | 18% standard | PwC |

- **ITS scale** — 0/16/21/24/28/32% (§2.1)  _(CGI Art. 119 bis; PwC)_
- **RICF** — fixed 11,000 XOF/part-month (§2.2)  _(CGI Art. 120)_
- **ITS deadline** — 15th of following month  _(DGI calendar (commonly cited) `[RESEARCH GAP]`)_
- **ITS late penalty** — 25% + 2%/month  _(DGI / PwC)_
- **CNPS retirement** — 6.30% EE / 7.70% ER; cap 3,375,000/mo  _(CLEISS (eff. 1 Jan 2025))_
- **Family + maternity** — 5.75% ER; cap 70,000/mo  _(CLEISS)_
- **AT/MP** — 2%–5% ER; cap 70,000/mo  _(CLEISS / CNPS `[RESEARCH GAP — sector rate]`)_
- **CMU** — 500 XOF/person each side  _(CLEISS / PwC)_
- **CNPS periodicity** — monthly ≥20 / quarterly <20; due day 15  _(CLEISS)_
- **CNPS late penalty** — 5% first month, then 1%/month  _(CLEISS)_
- **DISA** — due 31 March; 10% non-filing penalty  _(CNPS)_
- **Employer payroll tax** — 2.8% local / 12% expat  _(PwC)_
- **FDFP** — 0.4% + 1.2% = 1.6%  _(FDFP / eRegulations CI)_
- **SMIG / SMAG** — 75,000 / 39,960 XOF  _(Decree n° 2022-986 `[RESEARCH GAP — secondary]`)_
- **VAT (context only)** — 18% standard  _(PwC)_

### Authorities & portals

- DGI e-Impôts — https://e-impots.gouv.ci/
- DGI fiscal calendar — https://www.dgi.gouv.ci/assets/documents/CALENDRIER.pdf
- CNPS — https://www.cnps.ci/ ; e-CNPS — https://e.cnps.ci/
- CLEISS (cotisations CI) — https://www.cleiss.fr/docs/cotisations/cotedivoire.html
- PwC Ivory Coast — https://taxsummaries.pwc.com/ivory-coast/
- FDFP — https://fdfp.ci/presentation-du-fdfp/
- CGI Art. 119 bis / 120 (legal text) — https://loidici.biz/2025/02/21/67781/

## Section 17 — Test Suite

Each test recomputed end-to-end; AT/MP placeholder 3%, CMU 1 person.

1. **SMIG, 1 part:** gross 75,000 → net ITS 0, EE CNPS 5,225, **net pay 69,775**. (Example 1)
2. **500,000, 1 part:** gross ITS 81,000, EE CNPS 32,000, **net pay 387,000**. (Example 2)
3. **500,000, 3 parts:** RICF 22,000 → net ITS 59,000, **net pay 409,000**. (Example 3)
4. **1,000,000, 1 part:** gross ITS 192,000, EE CNPS 63,500, **net pay 744,500**. (Example 4)
5. **Expat 4,000,000, 1 part:** net ITS 976,000, EE CNPS capped 213,125, **net pay 2,810,875**; employer payroll tax 12% = 480,000. (Example 5)
6. **10,000,000, 1 part:** net ITS 2,736,000, EE CNPS capped 213,125, **net pay 7,050,875**. (Example 6)
7. **Cumulative-scale check:** ITS at exactly 800,000 = 144,000; at 2,400,000 = 528,000; at 8,000,000 = 2,096,000.
8. **RICF check:** 2 parts → 11,000/mo (132,000/yr); 4 parts → 33,000/mo (396,000/yr).
9. **Cap check:** at gross 5,000,000, EE retirement = 6.30% × 3,375,000 = 212,625 (NOT 315,000).
10. **Currency refusal:** input "EUR 3,000" → refuse, request XOF.

## PROHIBITIONS

- NEVER process payroll in any currency other than XOF/FCFA.
- NEVER use the pre-2024 IGR + CN + IS method — it was abolished by Ordonnance n° 2023-719 (effective 1 Jan 2024).
- NEVER apply the RICF reduction before computing gross ITS, and never let net ITS go below 0.
- NEVER charge the employee for family allowances, maternity, AT/MP, FDFP, or the employer payroll tax — those are employer-borne.
- NEVER apply the 12% expatriate payroll-tax rate without AEJ contract evidence.
- NEVER ignore the CNPS contribution ceilings (3,375,000 retirement; 70,000 family/maternity/AT-MP).
- NEVER omit the FDFP 1.6% levy or the flat CMU contribution.
- NEVER assume the AT/MP rate — confirm the employer's CNPS risk class (2%–5%).
- NEVER miss the 15th-of-following-month DGI/CNPS deadline.
- NEVER present any `[RESEARCH GAP]` figure as confirmed, and NEVER present payroll computations as definitive — always label as estimated (Tier 2) and direct to a licensed Ivorian accountant.

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as an expert-comptable inscrit à l'Ordre in Côte d'Ivoire) before implementation. This is a Tier 2 research-verified skill pending accountant sign-off; figures marked `[RESEARCH GAP — reviewer to confirm]` are unverified.

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
