---
name: france-tax-optimization
description: Use this skill whenever asked about reducing tax in France, tax planning, saving tax, optimizing tax, allowances, deductions the client might be missing, or any question about legal strategies to minimize income tax liability for self-employed individuals in France. Trigger on phrases like "reduce tax", "tax planning", "save tax", "optimize", "allowances", "deductions I'm missing", "payer moins d'impôts", "optimisation fiscale", "réduire ses impôts", "défiscalisation". ALWAYS read this skill before advising on any French tax optimization strategy.
version: 1.0
jurisdiction: FR
tax_year: 2025
last_updated: 2026-07-13
review_status: pending_review
depends_on: []
category: tax-optimization
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# France Tax Optimization

## Section 1 -- Quick Reference

**Quick Reference**

| Field | Value |
| --- | --- |
| Country | France (République française) |
| Key optimization legislation | Code Général des Impôts (CGI) -- Art. 39 (charges déductibles), Art. 44 sexies (ZFU/JEI), Art. 83 (frais professionnels salariés), Art. 154 bis (Madelin), Art. 156 (charges du revenu global), Art. 163 quatervicies (PER), Art. 199 sexdecies (emploi à domicile), Art. 200 (dons), Art. 200-0 A (plafonnement des niches fiscales) |
| Tax authority attitude to planning | The Direction Générale des Finances Publiques (DGFiP) accepts legitimate optimization. France has a general anti-abuse provision (Art. L64 du Livre des Procédures Fiscales -- abus de droit) and a mini-abuse provision (Art. L64 A LPF) for arrangements with a "principally fiscal" motivation. The Comité de l'abus de droit fiscal advises on borderline cases. |
| Currency | EUR |
| Tax year | Calendar year (1 Jan -- 31 Dec) |
| Filing deadline | Typically May-June of the following year (varies by département and filing method) |

### Income Tax Rates 2026 (Barème progressif)

**Income Tax Rates 2026 (Barème progressif)**

| Tranche | Taxable income per part (EUR) | Rate |
| --- | --- | --- |
| 1 | 0 -- 11,497 | 0% |
| 2 | 11,498 -- 29,315 | 11% |
| 3 | 29,316 -- 83,823 | 30% |
| 4 | 83,824 -- 180,294 | 41% |
| 5 | 180,295+ | 45% |

Income is divided by the number of parts (quotient familial): 1 per adult, 0.5 per dependent child (1 for the 3rd child onwards). This mechanism itself is a powerful income-splitting tool.

## Section 2 -- Income Splitting & Structuring

### Micro-Entreprise vs Régime Réel

**Micro-Entreprise vs Régime Réel**

| Factor | Micro-Entreprise (micro-BIC / micro-BNC) | Régime Réel |
| --- | --- | --- |
| Turnover ceiling (2026) | EUR 77,700 (services/BNC) / EUR 188,700 (goods/BIC) | No limit |
| Taxation method | Flat abatement: 34% (BNC) or 50% (BIC services) or 71% (BIC goods) | Actual expenses deducted |
| When to choose réel | When actual deductible expenses exceed the flat abatement | Always compare before choosing |
| Social contributions | Based on turnover (micro) vs net profit (réel) | Réel may be lower if expenses are high |

- **Legislation** — CGI Art. 50-0 (micro-BIC), Art. 102 ter (micro-BNC)  _(CGI Art. 50-0, Art. 102 ter)_

### Quotient Familial (Family Splitting)

**Quotient Familial (Family Splitting)**

| Parts | Family situation |
| --- | --- |
| 1 | Single, no children |
| 2 | Married/PACS, no children |
| 2.5 | Married/PACS, 1 child |
| 3 | Married/PACS, 2 children |
| 4 | Married/PACS, 3 children (1 full part from 3rd child) |

- **Strategy** — The quotient familial significantly reduces the marginal rate. A married couple with 3 children earning EUR 120,000 pays substantially less than a single person with the same income. However, the benefit per half-part is capped at EUR 1,759 (2026).  _(CGI Art. 193-197)_
- **Legislation** — CGI Art. 193-197  _(CGI Art. 193-197)_

### EURL/SARL vs Entreprise Individuelle

**EURL/SARL vs Entreprise Individuelle**

| Factor | Entreprise Individuelle | EURL/SARL (IS option) |
| --- | --- | --- |
| Top marginal rate | 45% + social charges (~45%) | IS: 15% (up to EUR 42,500) / 25% above |
| When to consider | For simplicity and lower income | When profits exceed ~EUR 60,000 and can be retained |
| Rémunération du gérant | N/A | Salary deductible from company profit, taxed as income for gérant |

## Section 3 -- Deductions Most People Miss

**Deductions Most People Miss**

| Deduction | Legislation | Notes |
| --- | --- | --- |
| Cotisations sociales (self-employed SSC) | CGI Art. 154 bis | CSG déductible (6.8% of total 9.2% CSG) is deductible from taxable income. CRDS (0.5%) is not deductible. |
| CSG déductible | CGI Art. 154 quinquies | 6.8% of 9.2% total CSG on earned income. Often missed -- automatically deductible but verify it is correctly reported. |
| Frais de véhicule (barème kilométrique) | CGI Art. 83-3° | Use the official barème kilométrique for business travel. For a 6 CV car doing 15,000 km/year: ~EUR 5,500 deduction. Includes fuel, insurance, depreciation, maintenance. |
| Home office (local professionnel) | CGI Art. 39, Art. 93 | Proportion of rent, utilities, insurance for dedicated professional space. Calculate by floor area ratio. |
| Formation professionnelle | CGI Art. 39, Art. 93 | Training, certifications, conferences related to current activity. Fully deductible. Crédit d'impôt formation (up to EUR 878 for 2026 for dirigeants of TPE). |
| Cotisations professionnelles | CGI Art. 93 | Ordres professionnels, syndicats, associations professionnelles. |
| Frais de repas (solo meals) | CGI Art. 93; BOI-BNC-BASE-40-60-60 | Meals taken alone during work: difference between actual cost and the forfait repas pris au domicile (EUR 5.35 in 2025). Max deductible: ~EUR 14.65/meal (EUR 20.00 ceiling - EUR 5.35). |
| Intérêts d'emprunt | CGI Art. 39-1-1° | Interest on loans taken for professional purposes is deductible. |
| Assurances professionnelles | CGI Art. 39, Art. 93 | RC Pro, prévoyance complémentaire Madelin (within limits), multirisque professionnelle. |
| Dons aux œuvres | CGI Art. 200 | 66% tax reduction on donations to eligible charities (up to 20% of taxable income). 75% for "Coluche" organizations (meals for the needy), capped at EUR 1,000. |

## Section 4 -- Capital Allowances Optimization

- **Legislation** — CGI Art. 39 (amortissements), Art. 39 A (dégressif)  _(CGI Art. 39, Art. 39 A)_

### Amortissement Linéaire (Straight-Line) vs Dégressif (Declining Balance)

**Amortissement Linéaire (Straight-Line) vs Dégressif (Declining Balance)**

| Method | When to use | Coefficient (for assets with useful life ≥ 3 years) |
| --- | --- | --- |
| Linéaire | Default method, equal annual deductions | N/A |
| Dégressif | Accelerated deductions in early years. Available for industrial equipment, certain IT assets. | 3-4 yrs: ×1.25; 5-6 yrs: ×1.75; 7+ yrs: ×2.25 |

### Timing of Purchases

- **Timing of Purchases** — Under both methods, depreciation starts from the date the asset is put into service. For dégressif, depreciation starts from the first day of the month of acquisition (pro-rata to 1/12ths). Purchase in January rather than December to maximize the first-year deduction under dégressif.  _(CGI Art. 39 A)_

### Low-Value Assets

- **Low-Value Assets** — Assets under EUR 500 HT can be immediately expensed without depreciation (tolérance administrative). Above EUR 500 HT, depreciation is required.  _(tolérance administrative)_

### Suramortissement (Super-Depreciation)

- **Suramortissement** — Certain categories of investment benefit from additional depreciation (40% extra over the useful life): industrial robotics, digital transformation equipment, energy transition assets. Check annually for eligible categories.  _(CGI Art. 39 decies and following)_

## Section 5 -- Loss Utilization

- **Legislation** — CGI Art. 156 I, Art. 156 I bis  _(CGI Art. 156 I, Art. 156 I bis)_

**Loss Utilization table**

| Relief | Detail | Limit |
| --- | --- | --- |
| Déficit BIC/BNC against global income | Professional losses (BIC/BNC professionnel) can offset other income (salaries, pensions, rental) in the same year | Unlimited for professional deficits |
| Carry-forward | Unused deficit is carried forward for 6 years against profits of the same category | 6-year limit |
| Non-professional losses (BIC/BNC non-professionnel) | Cannot offset other categories -- only offset against future profits from the same non-professional activity | 6-year carry-forward, same category only |
| Déficit foncier (rental losses) | Rental losses from deductible expenses (not interest) offset global income up to EUR 10,700/year | EUR 10,700/year against global income; excess carries forward 6 years for foncier, 10 years for interest |

### Strategy

If starting a business with heavy initial costs, structure as a profession libérale or commercial activity (BIC/BNC professionnel) so that first-year losses can be offset against any other income (salary, pension). This is unavailable for non-professional activities.

## Section 6 -- Timing Strategies

**Timing Strategies**

| Strategy | Detail |
| --- | --- |
| Defer revenue | Under micro-BNC/BIC, revenue is recognized when received (encaissements). Delay invoicing to January. Under régime réel BNC (déclaration contrôlée), the same cash-basis principle applies. |
| Accelerate expenses | Prepay deductible expenses (insurance, subscriptions, training) before 31 December. Under BNC déclaration contrôlée, expenses are deductible when paid. |
| PER contribution timing | Maximize PER contributions before 31 December. Contributions are deductible from the current year's income. Unused deduction capacity can now be carried forward for 5 years (previously 3), with spouse pooling. |
| Quotient familial optimization | Declare PACS or marry before 31 December to benefit from joint taxation for the entire year. |
| Versement libératoire timing | Under micro, the versement libératoire (flat tax on turnover) is monthly or quarterly. Manage cash flow around payment dates. |
| Income smoothing (système du quotient) | For exceptional income (Art. 163-0 A CGI), apply the quotient system: add 1/4 of exceptional income to normal income, calculate marginal tax, multiply by 4. Reduces effective rate on lumpy income. |

## Section 7 -- VAT Optimization (TVA)

- **Legislation** — CGI Art. 293 B (franchise en base), Art. 302 septies A (régime simplifié)  _(CGI Art. 293 B, Art. 302 septies A)_

**VAT Optimization (TVA) table**

| Strategy | Detail |
| --- | --- |
| Franchise en base de TVA | Below EUR 36,800 (services) or EUR 91,900 (goods): no TVA charged. No input TVA recovery. Competitive advantage for B2C. |
| Opt for TVA | If significant input TVA (investment phase), opt to charge TVA to recover inputs. Lock-in: 2 calendar years. |
| Régime simplifié | Annual TVA return with 2 quarterly acomptes. Available if turnover < EUR 840,000 (goods) / EUR 254,000 (services). |
| TVA sur les débits vs encaissements | For service providers: TVA on encaissements (payment received) defers TVA liability vs. débits (invoice date). |
| Autoliquidation (reverse charge) | For intra-EU B2B services: no French TVA charged. Report via DES/DEB. |

## Section 8 -- Social Security Optimization

- **Legislation** — Code de la Sécurité Sociale; Loi de financement de la Sécurité sociale 2026  _(Code de la Sécurité Sociale; Loi de financement de la Sécurité sociale 2026)_

### Cotisations Sociales Structure (Travailleurs Non-Salariés / TNS)

**Cotisations Sociales Structure (Travailleurs Non-Salariés / TNS)**

| Contribution | Rate (approximate) | Base |
| --- | --- | --- |
| Assurance maladie-maternité | 0-6.5% (progressive) | Net profit |
| Allocations familiales | 0-3.1% (progressive) | Net profit |
| Retraite de base (CNAV) | 17.75% up to PASS; 0.6% above | Net profit |
| Retraite complémentaire (RCI) | 7-8% up to 4× PASS | Net profit |
| Invalidité-décès | 1.3% | Net profit |
| CSG/CRDS | 9.7% | Revenue + cotisations |
| CFP (formation) | 0.25% of PASS | Flat contribution |
| **Total effective rate** | **~40-45%** of net profit |  |

### Optimization Strategies

**Optimization Strategies**

| Strategy | Detail |
| --- | --- |
| ACRE (first year) | 50% reduction in social contributions for the first year of business creation. Automatic for micro-entrepreneurs since 2020. |
| Micro vs réel social base | Under micro, social contributions are calculated on turnover (after flat abatement). Under réel, on net profit. Compare both. |
| Cotisation minimale | Below a minimum profit level, minimum contributions apply. In a loss year, you still pay minimum health/retirement contributions. |
| Conjoint collaborateur | A spouse working in the business without salary can be registered as conjoint collaborateur for social coverage at reduced cost. |
| PER contributions as social deduction | PER Madelin/154 bis contributions reduce the social contribution base for TNS if deducted from BIC/BNC profit. |

## Section 9 -- Investment & Retirement

### Plan d'Épargne Retraite (PER) -- CGI Art. 163 quatervicies / Art. 154 bis

**Plan d'Épargne Retraite (PER)**  _(CGI Art. 163 quatervicies / Art. 154 bis)_

| Feature | Detail |
| --- | --- |
| PER individuel (salarié/particulier) | Deductible contributions up to 10% of net taxable income, max EUR 38,448 (2026) or EUR 4,806 minimum |
| PER Madelin / TNS (Art. 154 bis) | Additional deduction: 15% of profit between 1× and 8× PASS. Total TNS envelope up to ~EUR 88,911 (2026). |
| Combined TNS deduction | Up to EUR 88,911/year for a high-earning TNS. At TMI 45%, this yields ~EUR 40,000 in tax savings. |
| Carry-forward of unused allowance | Now 5 years (extended from 3 years by Loi de Finances 2026). Spouse pooling maintained. |
| Exit taxation | Capital: IR + social charges (18.6% in 2026). Annuity: IR + social charges. |
| Age limit (from 2026) | Contributions after age 70 are no longer deductible for PER (not applicable to old PERP/Madelin). |
| Non-deduction option | At TMI 0% or 11%, opt for non-deduction: no tax benefit at entry, but tax-free capital at exit. |

For TNS at TMI 41% or 45%, maximize PER contributions. At EUR 88,911 with TMI 45%, the annual tax saving is EUR 40,010. For lower TMI (11%), consider the non-deduction option.

### Assurance-Vie

**Assurance-Vie**

| Feature | Detail |
| --- | --- |
| Tax treatment after 8 years | EUR 4,600 (single) / EUR 9,200 (couple) annual tax-free withdrawal on gains. Above: 7.5% + social charges (if older contracts). |
| No deduction at entry | Not deductible from income tax. But tax-efficient for long-term savings and estate planning. |
| Succession | Up to EUR 152,500 per beneficiary tax-free if funded before age 70. |

### Réductions d'Impôt (Tax Credits/Reductions)

**Réductions d'Impôt (Tax Credits/Reductions)**

| Reduction | Rate | Cap | Legislation |
| --- | --- | --- | --- |
| Emploi à domicile | 50% | EUR 12,000/year (+EUR 1,500/dependent, max EUR 15,000) | CGI Art. 199 sexdecies |
| Dons aux œuvres | 66% (general) / 75% (Coluche) | 20% of taxable income / EUR 1,000 | CGI Art. 200 |
| IR-PME (Madelin investment) | 18-25% | EUR 50,000 (single) / EUR 100,000 (couple) | CGI Art. 199 terdecies-0 A |
| Crédit d'impôt formation dirigeant | ~EUR 878 (2026) for TPE | Forfait annuel | CGI Art. 244 quater M |
| Plafonnement global des niches | EUR 10,000/year | All reductions combined | CGI Art. 200-0 A |

## Section 10 -- Red Lines

**Red Lines**

| Risk | Detail |
| --- | --- |
| Abus de droit (Art. L64 LPF) | Arrangements that are fictitious or have a tax purpose as their sole motivation can be recharacterized by the DGFiP. Penalty: 80% surcharge. |
| Mini abus de droit (Art. L64 A LPF) | Arrangements with a "principally fiscal" (not solely) motivation can also be challenged. Lower threshold than L64. Penalty: 40% surcharge. |
| Plafonnement des niches fiscales | Total tax reductions/credits capped at EUR 10,000/year (EUR 18,000 for overseas/Sofica). Exceeding the cap: lost forever. |
| Non-professional activities | Losses from non-professional BIC/BNC cannot offset other income. If activity is non-professional, loss utilization is severely limited. |
| PER after 70 (from 2026) | Contributions to PER after age 70 are no longer deductible. Old PERP/Madelin may still allow deduction (Art. 163 quinvicies CGI interpretation). |
| Micro-entreprise with high expenses | Choosing micro when actual expenses > flat abatement = paying more tax. Always compare. |
| TVA franchise in B2B context | Not charging TVA to B2B clients offers no competitive advantage (they recover it). May lose input VAT recovery on your own costs. |

## Section 11 -- Annual Tax Planning Calendar

**Annual Tax Planning Calendar**

| Month | Action |
| --- | --- |
| January | Review prior year's profit. Plan PER contributions for the current year. Apply ACRE if new business. |
| February | Gather documents: bank statements, invoices, cotisations sociales attestations, PER certificates. |
| March | Review micro vs réel option (option must be exercised before the filing deadline for the prior year). |
| April | File déclaration de revenus (online, typically opens mid-April). Declare PER contributions, dons, emploi à domicile. |
| May-June | **Filing deadline** (varies by département). Finalize and submit. |
| July | URSSAF quarterly adjustment. Review estimated cotisations vs actual. |
| August | Mid-year profit review. Consider accelerating or deferring income/expenses. |
| September | Review investment plans: IR-PME, FCPI/FIP before December. |
| October | Assess PER contribution capacity. Calculate remaining deduction headroom. |
| November | Maximize PER contributions. Make donations for the current year's réduction. Hire emploi à domicile services. |
| December | **31 December** -- all PER contributions, dons, and investments must be made by this date. Prepay deductible expenses. Finalize invoicing strategy (defer to January if beneficial). |

## Section 12 -- Cash Impact Examples

### Example 1 -- PER Contribution (TNS, Net BNC EUR 100,000, TMI 41%)

**Example 1 -- PER Contribution (TNS, Net BNC EUR 100,000, TMI 41%)**

| PER contribution | EUR 15,750 (10% of profit + 15% of tranche 1-8 PASS) |
| --- | --- |
| Tax saving (41% × EUR 15,750) | **EUR 6,458/year** |
| Social contribution saving (~10% of deduction from BNC) | **~EUR 1,575/year** |

### Example 2 -- Micro-BNC vs Régime Réel (BNC Revenue EUR 60,000, Actual Expenses EUR 25,000)

**Example 2 -- Micro-BNC vs Régime Réel (BNC Revenue EUR 60,000, Actual Expenses EUR 25,000)**

| Scenario | Taxable income | Tax (single, TMI 30%) |
| --- | --- | --- |
| Micro-BNC (34% abatement) | EUR 39,600 | ~EUR 5,510 |
| Régime réel (actual expenses) | EUR 35,000 | ~EUR 4,130 |
| **Saving with régime réel** |  | **~EUR 1,380/year** |

### Example 3 -- Quotient Familial (Married, 2 Children, Income EUR 80,000)

**Example 3 -- Quotient Familial (Married, 2 Children, Income EUR 80,000)**

| Scenario | Parts | Tax |
| --- | --- | --- |
| Single, no children | 1 | ~EUR 15,673 |
| Married, 2 children | 3 | ~EUR 7,236 |
| **Annual saving** |  | **~EUR 8,437** |

### Example 4 -- Emploi à Domicile (Gardening/Cleaning EUR 6,000/year)

**Example 4 -- Emploi à Domicile (Gardening/Cleaning EUR 6,000/year)**

| Expense | EUR 6,000 |
| --- | --- |
| Tax credit (50%) | **EUR 3,000** |

### Example 5 -- CSG Déductible (Revenue EUR 80,000)

**Example 5 -- CSG Déductible (Revenue EUR 80,000)**

| CSG déductible (6.8%) | EUR 5,440 |
| --- | --- |
| Tax saving at TMI 30% | **EUR 1,632** |

### Example 6 -- Barème Kilométrique (6 CV, 15,000 km Business)

**Example 6 -- Barème Kilométrique (6 CV, 15,000 km Business)**

| Deduction (barème 2025) | ~EUR 5,500 |
| --- | --- |
| Tax saving at TMI 30% | **~EUR 1,650** |

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a CPA, EA, tax attorney, or equivalent licensed practitioner in your jurisdiction) before filing or acting upon.

The most up-to-date, verified version of this skill is maintained at [openaccountants.com](https://openaccountants.com).

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
