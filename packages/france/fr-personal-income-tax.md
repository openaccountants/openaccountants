---
name: fr-personal-income-tax
description: "Comprehensive French personal income tax (impôt sur le revenu / IR) guide for all individuals. Trigger on phrases like \"impôt sur le revenu\", \"IR France\", \"barème progressif\", \"quotient familial\", \"décote\", \"prélèvement à la source\", \"PAS\", \"CEHR\", \"contribution exceptionnelle hauts revenus\", \"CDHR\", \"déclaration 2042\", \"revenus exceptionnels\", \"quotient pour revenus exceptionnels\", \"TMI\", \"taux marginal d'imposition\", \"tranches d'imposition France\", \"parts fiscales\", \"parent isolé case T\", \"pension alimentaire déduction\", \"réductions d'impôt\", \"crédits d'impôt\", \"emploi à domicile\", \"dons associations\", \"plafonnement niches fiscales\", \"non-résident fiscal France\", \"exit tax\", \"impatriation\", \"PUMA cotisation subsidiaire\", \"calcul IR France\", \"simulation impôt sur le revenu\", \"avis d'imposition\". Covers the full IR computation sequence: progressive brackets, quotient familial with plafonnement, décote, CEHR, CDHR, prélèvement à la source, deductions/reductions/credits, non-residents, and special cases. For capital gains see fr-capital-gains, for rental income see fr-rental-income, for crypto see fr-crypto-tax."
version: 1.0
jurisdiction: FR
tax_year: 2025
last_updated: 2026-07-13
review_status: pending_review
category: international
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# FR Personal Income Tax

## France — Personal Income Tax (Impôt sur le Revenu) — Comprehensive Guide v1.0

> **Based on work by [Romain Simon (@romainsimon)](https://github.com/romainsimon/paperasse)**, licensed under MIT. Adapted for the OpenAccountants format.

> **Disclaimer:** This skill is for informational purposes only and does not constitute tax advice. All positions must be reviewed and signed off by a qualified expert-comptable or avocat fiscaliste before filing. Get this reviewed at **openaccountants.com**.

## Section 1 — Quick Reference

**Quick Reference table**

| Field | Value |
| --- | --- |
| Country | France (République française) |
| Tax | Impôt sur le Revenu (IR) + Prélèvements sociaux + CEHR + CDHR |
| Currency | EUR only |
| Tax year | Calendar year (1 January – 31 December) |
| Primary legislation | Code Général des Impôts (CGI), art. 197 |
| Tax authority | Direction Générale des Finances Publiques (DGFiP) |
| Filing portal | impots.gouv.fr (espace particulier) |
| Filing deadline | Late May / early June (varies by département, online) |
| Key forms | 2042, 2042-C, 2042-C-PRO, 2042-IFI, 2047, 2074, 2086 |

## Section 2 — Full IR Computation Sequence

**Never skip a step. Each intermediate must be computed.**

```
1. Revenus bruts par catégorie
   ↓ abattements spécifiques (10% salaires, 10% pensions, 40% dividendes if barème…)
2. Revenus nets catégoriels
   ↓ somme
3. Revenu brut global (RBG)
   ↓ déductions (PER, pension alimentaire, CSG déductible N-1)
4. Revenu Net Imposable (RNI)
   ↓ ÷ nombre de parts
5. Quotient
   ↓ application du barème progressif
6. Impôt par part
   ↓ × nombre de parts
7. Impôt brut
   ↓ plafonnement du gain QF
8. Impôt après QF
   ↓ décote (if impôt < threshold)
9. Impôt après décote
   ↓ − réductions d'impôt (floor at 0)
10. Impôt après réductions
    ↓ − crédits d'impôt (refundable — can be negative)
11. Impôt net
    + Prélèvements sociaux (separate, on capital income)
    + CEHR (if RFR > thresholds)
    + CDHR (if effective rate < 20% floor)
    = Total tax liability
```

## Section 3 — Progressive Rate Table (Barème IR)

### 2025 Brackets (revenus 2025, déclaration 2026) — per part

**2025 Brackets table**  _(art. 197 CGI)_

| Revenu net imposable (EUR/part) | Rate | Cumulative tax at top of bracket |
| --- | --- | --- |
| 0 – 11,600 | 0% | 0 |
| 11,601 – 29,579 | 11% | 1,977.69 |
| 29,580 – 84,577 | 30% | 18,477.09 |
| 84,578 – 181,917 | 41% | 58,386.49 |
| Above 181,917 | 45% | — |

*Tranches LFI 2026 (revenus 2025, indexation +0.9%). Source: art. 197 CGI.*

### Worked Example — Single, RNI = EUR 40,000, 1 part

**Worked example table**

| Bracket | Calculation | Tax |
| --- | --- | --- |
| 0 – 11,600 | 11,600 × 0% | 0 |
| 11,601 – 29,579 | 17,979 × 11% | 1,977.69 |
| 29,580 – 40,000 | 10,421 × 30% | 3,126.30 |
| **Total** |  | **5,103.99** |

## Section 4 — Abattements (Standard Deductions) by Income Category

**Abattements table**

| Income type | 2042 box | Abattement | Min / Max | Notes |
| --- | --- | --- | --- | --- |
| Salaries (salaires) | 1AJ/1BJ | 10% | min EUR 509, max EUR 14,555 | Or opt for frais réels |
| Pensions / retirement | 1AS/1BS | 10% | min EUR 450, max EUR 4,446 per household |  |
| **Unemployment (ARE)** | **1AP/1BP** | **None** | — | Common trap: never put in 1AJ |
| Dividends (option barème) | 2DC | 40% | — | Only under barème option |
| Dividends (PFU) | 2DC | None | — |  |
| Micro-BNC | 5TE | 34% | min EUR 305, ceiling EUR 77,700 |  |
| Micro-foncier (bare rental) | 4BE | 30% | ceiling EUR 15,000 |  |
| Micro-BIC LMNP long-term | 5ND | 50% | ceiling EUR 77,700 |  |
| Micro-BIC furnished tourism unclassified | 5ND | 30% | ceiling EUR 15,000 | Loi Le Meur |
| Micro-BIC furnished tourism classified | 5NG | 50% | ceiling EUR 77,700 |  |

**Salary terminology trap table**

| Term | Where found | Value |
| --- | --- | --- |
| Salaire brut | Pay slip — top | Before contributions |
| Salaire net | Pay slip — deposited amount | After contributions, before non-deductible CSG |
| **Salaire net imposable (1AJ)** | **Pay slip — dedicated line** | **Amount declared in box 1AJ** |
| RNI (after abattement) | Avis d'imposition | 1AJ × 0.9 (standard range) |

## Section 5 — Quotient Familial (Family Quotient)

### Parts de base (base shares)

**Parts de base table**

| Situation | Base parts |
| --- | --- |
| Single, divorced, separated | 1 |
| Married / PACSed (joint filing) | 2 |
| Widowed without children | 1 |
| Widowed with child(ren) | 2 (+ child parts) |

### Majoration for children

**Majoration table**

| Child rank | Additional parts |
| --- | --- |
| 1st child | +0.5 |
| 2nd child | +0.5 |
| 3rd child and each subsequent | +1.0 each |

**Special cases:**
- Shared custody (résidence alternée): half the above values (0.25 / 0.25 / 0.5)
- Disabled child (carte CMI-invalidité): +0.5 additional part
- Single parent (parent isolé, case T): +0.5 on first child

### Examples

**Examples table**

| Household | Total parts |
| --- | --- |
| Single, no children | 1 |
| Single, 1 child | 1.5 (or 2 if parent isolé) |
| Married, 0 children | 2 |
| Married, 2 children | 3 |
| Married, 3 children | 4 |

### Plafonnement du gain QF (QF capping)

- **Cap per half part (revenus 2025)** — EUR 1,807 EUR (revenus 2025)  _(art. 197-2 CGI)_
- **QF capping algorithm** — tax_with_all_parts     = normal calculation with all parts tax_without_children   = calculation with base parts only (1 or 2) actual_gain            = tax_without_children − tax_with_all_parts cap_per_half_part      = EUR 1,807 (revenus 2025) nb_supplementary_halves = (total_parts − base_parts) × 2 max_gain               = cap_per_half_part × nb_supplementary_halves final_tax = tax_without_children − min(actual_gain, max_gain)  _(art. 197-2 CGI)_

**Critical mechanism often forgotten.** The tax benefit from supplementary half-parts (children) is capped.

**Practical consequence:** above approximately EUR 90,000–100,000 RNI for a couple with 2 children, the QF benefit plateaus at EUR 3,614 (2 × EUR 1,807).

**Parent isolé (case T):** the half-part for single parents has its own higher cap (EUR 4,273 for the first child-related part). Widowed with children: cap EUR 4,273.

## Section 6 — Décote (Low-Income Smoothing)

- **Décote application order** — Applied after QF plafonnement, before reductions/credits.  _(art. 197-4° CGI)_

### Formulas (revenus 2025)

**Décote formulas table**  _(art. 197-4° CGI)_

| Situation | Condition | Décote formula |
| --- | --- | --- |
| Single | Impôt brut < EUR 1,982 | 897 − 0.4525 × impôt brut |
| Couple | Impôt brut < EUR 3,277 | 1,483 − 0.4525 × impôt brut |

- **Décote floor** — The décote cannot make the tax negative (floor at 0).  _(art. 197-4° CGI)_

### Effective marginal rate in the décote zone

In the décote zone, each additional euro of income:
- Increases tax at the bracket rate
- Reduces the décote by 0.4525 × that amount

Effective marginal rate ≈ bracket_rate × 1.4525. A household in the 11% bracket can face ~16% effective marginal rate in the décote zone.

## Section 7 — CEHR (Contribution Exceptionnelle sur les Hauts Revenus)

- **CEHR base and applicability** — Base: RFR (revenu fiscal de référence), not RNI. Added on top of IR net.  _(art. 223 sexies CGI)_

**CEHR thresholds table**  _(art. 223 sexies CGI)_

| Situation | 3% bracket | 4% bracket |
| --- | --- | --- |
| Single | EUR 250,001 – 500,000 | > EUR 500,000 |
| Couple | EUR 500,001 – 1,000,000 | > EUR 1,000,000 |

- **CEHR smoothing** — Smoothing possible over the average of the 2 preceding years.  _(art. 223 sexies CGI)_

## Section 8 — CDHR (Contribution Différentielle sur les Hauts Revenus)

- **CDHR mechanism overview** — Distinct from CEHR. Imposes a 20% floor on effective tax rate for high-RFR households, created by LFI 2025 (loi n° 2025-127), extended by LFI 2026 until deficit < 3% GDP.  _(art. 224 CGI)_

**CDHR thresholds table**  _(art. 224 CGI)_

| Situation | RFR threshold |
| --- | --- |
| Single, widowed, separated, divorced | > EUR 250,000 |
| Couple (married or PACSed, joint filing) | > EUR 500,000 |

- **CDHR mechanism formula** — if (IR + CEHR) / adjusted RFR < 20%, the CDHR tops up the difference.  _(art. 224 CGI)_

**Automatic calculation** by the administration after filing. Advance of 95% due between 1–15 December via impots.gouv.fr PAS service.

**Typical profiles affected:** executives with large PFU dividends (effective IR ~12.8% while RFR > 250k), business angels with large capital gains, RSU/BSPCE vesting years.

## Section 9 — Prélèvement à la Source (PAS — Withholding at Source)

### Two mechanisms

**Two mechanisms table**

| Mechanism | Income types | Collector |
| --- | --- | --- |
| Retenue à la source (withholding) | Salaries, pensions, unemployment | Employer / pension fund / Pôle Emploi |
| Acompte contemporain (advance payment) | BIC, BNC, BA, rental income, received alimony | DGFiP via bank debit (monthly or quarterly) |

### Rate types

**Rate types table**

| Rate type | Description |
| --- | --- |
| Personalised (default) | Calculated by DGFiP from last filing |
| Individualised (couples) | Separate rates per spouse — same total, different split |
| Neutral (non-personalised) | Grid for single with no children — confidentiality option |

### Modulation

- **Downward modulation** — Allowed if estimated gap > 5%. Penalty 10% if gap > 10% and unjustified.  _(art. 1729 G CGI)_
- **Upward modulation** — Allowed without minimum threshold.
- **Life change signal deadline** — Marriage, PACS, birth, divorce, death — signal within 60 days. days  _(art. 204 I CGI)_

### Annual settlement

PAS is an **advance**, not final. Declaration in Apr-Jun N+1 leads to:
1. Definitive IR calculated on year N income
2. Compared with total withheld in N
3. **Balance due** (September N+1, spread if > EUR 300) or **refund** (July-August N+1)

### January advance for tax credits

- **January advance mechanism** — DGFiP pays a 60% advance mid-January based on N-2 expenses (emploi à domicile, garde d'enfant, dons, Pinel). Adjusted in summer N+1. Option to renounce in December if expense won't recur. %

## Section 10 — Deductions, Reductions, and Credits

### Fundamental distinction

**Fundamental distinction table**

| Mechanism | Acts on | Refundable if excess? | Calculation step |
| --- | --- | --- | --- |
| **Déduction** | Taxable income (RNI) | N/A | Step 3 |
| **Réduction** | Tax due | No — floor at 0 | Step 9 |
| **Crédit** | Tax due | Yes — refunded | Step 10 |

A EUR 1,000 deduction at TMI 30% saves EUR 300. A EUR 1,000 credit saves EUR 1,000.

### Key deductions (act on RNI)

**Key deductions table**

| Deduction | Limit | Notes |
| --- | --- | --- |
| PER (épargne retraite) | 10% of professional income, min EUR 4,710, max EUR 37,680 | Report unused caps 3 years; couple mutualisation |
| Pension alimentaire (child support) | Capped annually | Proof of need and actual payment required |
| CSG déductible | 6.8% of capital income CSG | Only if barème option on capital in N-1; zero under PFU |
| Frais réels (actual expenses) | Replaces 10% salary abattement | Must document every expense |

### Key reductions (floor at 0)

**Subject to the EUR 10,000 global cap (plafonnement des niches fiscales):**

**Reductions inside cap table**

| Device | Rate | Notes |
| --- | --- | --- |
| Pinel | Spread over 6/9/12 years | Last vintage 2024 — in extinction |
| FCPI / FIP | 18% – 25% of investment | Separate investment ceiling |
| Denormandie | Similar to Pinel, older housing | Targeted to degraded town centres |

**Outside the EUR 10,000 cap:**

**Reductions outside cap table**

| Device | Rate | Notes |
| --- | --- | --- |
| Dons associations (charitable gifts) | 66% standard; 75% for poverty relief (up to EUR 1,000/year) | Excess above 20% of taxable income reportable 5 years |
| Cotisations syndicales (union dues) | 66% | Cap: 1% of gross salary |
| Girardin industriel (overseas) | Variable | Specific conditions |

### Key credits (refundable)

**Key credits table**

| Credit | Rate | Ceiling | Notes |
| --- | --- | --- | --- |
| Emploi à domicile (home help) | 50% | EUR 12,000/year (max credit EUR 6,000); +EUR 1,500 per child or person 65+ (max EUR 15,000) | CESU+ instant advance available since 2022 |
| Garde d'enfant hors domicile (childcare) | 50% | EUR 3,500/child (max credit EUR 1,750/child) | Child under 6 at 1 January |

### Global cap on tax incentives (plafonnement des niches fiscales)

- **Global cap on tax incentives** — EUR 10,000 per year (EUR 18,000 for specific overseas investments) EUR  _(art. 200-0 A CGI)_
- **Excess treatment for devices inside cap** — Devices "inside the cap" (Pinel, FCPI, etc.) are summed. If total exceeds EUR 10,000, the excess is lost (not reportable). Devices "outside the cap" (charitable gifts, home help credit) are unlimited by this mechanism.  _(art. 200-0 A CGI)_

## Section 11 — Special Cases

### Revenus exceptionnels — Quotient mechanism

- **Exceptional income quotient formula** — supplementary_tax = [IR(ordinary_income + exceptional/4) − IR(ordinary_income)] × 4  _(art. 163-0 A CGI)_

Smoothing for one-off income (RSU vesting, departure indemnity, exceptional bonus) that would artificially push through multiple brackets.

**Conditions:**
- Income exceeds the average of taxable income over the 3 preceding years
- Exceptional, non-recurring character
- Explicit request on the declaration

**Useless if** the household is already at TMI 45% — the marginal rate doesn't change with division.

### Non-residents

- **Non-residents taxation scope** — Taxed only on French-source income.  _(art. 164 A CGI)_
- **Minimum rate for non-residents** — 20% on fraction ≤ EUR 27,519 and 30% above (revenus 2025) %
- **No QF or décote for non-residents** — No quotient familial beyond 2 parts; no décote. Tax treaty analysis required — out of scope for complex cases.

### PUMA — Cotisation subsidiaire maladie

**PUMA thresholds table**  _(art. L. 380-2 CSS)_

| Condition | Threshold (2025) |
| --- | --- |
| Professional income below | ~20% PASS ≈ EUR 9,420 |
| Capital income above | ~50% PASS ≈ EUR 23,550 |

- **PUMA rate** — 6.5% on (capital income − 50% PASS) %  _(art. L. 380-2 CSS)_

Affects individuals with low professional income but significant capital income. Collected by URSSAF, not DGFiP. Non-deductible from IR.

**Trap:** commonly forgotten in FIRE / early-retirement simulations — adds ~6.5% on top of PS.

### Year of marriage / PACS

- **Marriage/PACS filing rule** — Joint filing for the entire year (since 2011), or separate filing on option. Compute both to find more favourable.

### Year of divorce / separation

- **Divorce/separation filing rule** — Separate filing for the full year. Case T (parent isolé) available for the parent with sole custody.

### Year of spouse's death

- **Death of spouse filing rule** — Joint filing from 1 January to date of death. Separate filing for the surviving spouse for the remainder.

### Statute of limitations (droit de reprise)

**Statute of limitations table**

| Tax | Standard period |
| --- | --- |
| IR | 3 years |
| IFI | 6 years |
| All taxes (undisclosed activity / fraud) | 10 years |

- **Document retention period** — minimum 6 years (recommended: 10 years) years

## Section 12 — Conservative Defaults

**Conservative defaults table**

| Ambiguity | Default |
| --- | --- |
| Filing status unknown | Single, 1 part |
| Number of children unknown | 0 |
| Regime unknown | Barème progressif (no PFU option) |
| Credit eligibility unclear | No credit applied |
| PAS rate unknown | Standard personalised rate |
| ARE vs salary unclear | Classify as ARE (no 10% abattement — conservative) |

## Section 13 — Key Legal References

**Key legal references table**

| Rule | Article |
| --- | --- |
| Progressive brackets | art. 197 CGI |
| Quotient familial | art. 194–195 CGI |
| QF capping | art. 197-2 CGI |
| Décote | art. 197-4° CGI |
| 10% salary abattement | art. 83-3° CGI |
| CEHR | art. 223 sexies CGI |
| CDHR | art. 224 CGI |
| PAS | art. 204 A to 204 N CGI |
| Exceptional income quotient | art. 163-0 A CGI |
| PER deduction | art. 163 quatervicies CGI |
| Non-residents | art. 164 A to 165 CGI |
| Tax residence definition | art. 4 B CGI |
| Charitable gifts | art. 200 CGI |
| Home help credit | art. 199 sexdecies CGI |
| Childcare credit | art. 200 quater B CGI |
| Global cap (niches) | art. 200-0 A CGI |
| PUMA | art. L. 380-2 CSS |

## Footer

*OpenAccountants — open-source accounting skills for AI*
*This output must be reviewed by a qualified professional before filing or acting upon.*
*Latest verified skills: **openaccountants.com** | Report errors: **github.com/openaccountants/openaccountants***

## Talk to a verified accountant

This skill is a tool, not an engagement. Every taxpayer's situation is
different, and the rules in the skill may not match your specific facts.

To speak with one of the licensed accountants who verifies skills for your
jurisdiction — **no liability on either side until you and the accountant sign
a formal engagement letter** — book a free 30-minute call:

**→ [Book a call](https://calendly.com/openaccountants-info/30min)**

We'll route you to the named verifier covering your country or state. You can
also see the full list of verified accountants at
[openaccountants.com/network](https://openaccountants.com/network).

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
