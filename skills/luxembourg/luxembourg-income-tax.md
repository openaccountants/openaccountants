---
name: luxembourg-income-tax
description: "Luxembourg personal income tax for resident individuals and self-employed people (indépendants) for tax year 2026: the 23-band scale (0% to 42%), tax classes 1, 1a and 2, the employment fund surcharge (7%, or 9% above EUR 150,000 / 300,000), the CIS, CII, CI-CO2, CISSM and single-parent credits, expenses, depreciation (arts. 32 and 34), special expenses and CCSS contributions, Form 100 and Form 163 annual adjustment, quarterly advances, penalties and interest. Trigger on: impôt sur le revenu Luxembourg, modèle 100, décompte annuel 163, classe d'impôt, barème 2026, indépendant Luxembourg, avances trimestrielles. Out of scope: lu-cross-border, luxembourg-payroll, luxembourg-social-contributions, lu-corporate-tax."
version: 0.4
jurisdiction: LU
tax_year: 2026
last_updated: 2026-10-27
review_status: pending_review
trust_label: Built by Michael Cutajar and the OpenAccountants team
depends_on:
  - income-tax-workflow-base
category: international
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Luxembourg personal income tax: residents and the self-employed (2026) v0.4

> **Source-cited draft: not reviewed by an accountant.** This skill is general tax reference material for AI-assisted work. It has not been reviewed for any person's facts. Do not rely on it to file, pay or take a tax position without review by a qualified professional in Luxembourg.

What matters for 2026:

- **The scale did not change.** The LIR text in force on 1 January 2026 still carries the art. 118 scale set by the law of 20 December 2024 and first applied for 2025: 0% up to EUR 13,230, then 8% rising to 42% above EUR 234,870.
- **CI-CO2 is EUR 216 a year** for employees and the self-employed (arts. 152ter and 154quater, as amended by the law of 19 December 2025).
- **Pension contributions rose to 17% in total** (8.5% + 8.5% for employees; 17% for the self-employed), and the social parameters changed again on 1 June 2026 (CCSS).
- **Deadline:** the 2026 return (Form 100) and the 2026 annual adjustment (Form 163 R / 163 NR) are due by 31 December 2027.

This skill computes the annual tax of a resident individual. For non-residents, frontier workers, the 90% option and the impatriate regime use `lu-cross-border`. For monthly wage withholding use `luxembourg-payroll`. For the full contribution rules (self-employed base, voluntary insurance, minima) use `luxembourg-social-contributions`.

## Who this applies to

- **Residents.** An individual with a fiscal domicile or habitual stay in Luxembourg is taxed on worldwide income (art. 2(1) and (2) LIR). Non-residents are taxed only on Luxembourg-source income (art. 2(3), art. 156): see `lu-cross-border`.
- **The self-employed (indépendants):** trade (art. 14), farming and forestry (art. 61) and liberal professions (art. 91), as sole operators. Profit is computed from accounts; this skill covers the income-tax side.
- **Employees and pensioners.** Tax is withheld at source on the electronic tax card (`luxembourg-payroll`). Those not taxed by assessment may claim an annual adjustment (art. 145). Those taxed by assessment (for example with more than EUR 600 of other net income, or spouses who opted for joint taxation; art. 153(1)) file Form 100.
- **Tax classes (art. 119):**
  - Class 1: anyone not in class 1a or 2.
  - Class 1a: unless in class 2, widowed persons; persons who get the child tax reduction (art. 122); persons who had completed their 64th year at the start of the tax year.
  - Class 2: spouses taxed jointly (art. 3), partners taxed jointly (art. 3bis), persons widowed in the three preceding years, and persons divorced or separated in the three preceding years (if they did not use this rule in the five years before).
- **Out of this skill:** companies, partnerships and holding structures (`lu-corporate-tax`); capital gains on real estate and substantial shareholdings; the participative premium and stock-option schemes; arrears under enforcement. Escalate these to a Luxembourg tax adviser.

## Rates, bands and thresholds

**Income tax scale, all classes (art. 118 LIR; taxable income first rounded down to a multiple of EUR 50, art. 126(2)).** Source: [LIR, consolidated text in force on 1 January 2026](https://impotsdirects.public.lu/dam-assets/fr/legislation/LIR/texte-coordonn-en-vigueur-au-1er-janvier-2026-ver-08052026.pdf). Tax years 2025 and 2026.

| Taxable income (EUR) | Rate | Cumulative tax at top of band (EUR) |
|---|---|---|
| 0 to 13,230 | 0% | 0.00 |
| 13,230 to 15,435 | 8% | 176.40 |
| 15,435 to 17,640 | 9% | 374.85 |
| 17,640 to 19,845 | 10% | 595.35 |
| 19,845 to 22,050 | 11% | 837.90 |
| 22,050 to 24,255 | 12% | 1,102.50 |
| 24,255 to 26,550 | 14% | 1,423.80 |
| 26,550 to 28,845 | 16% | 1,791.00 |
| 28,845 to 31,140 | 18% | 2,204.10 |
| 31,140 to 33,435 | 20% | 2,663.10 |
| 33,435 to 35,730 | 22% | 3,168.00 |
| 35,730 to 38,025 | 24% | 3,718.80 |
| 38,025 to 40,320 | 26% | 4,315.50 |
| 40,320 to 42,615 | 28% | 4,958.10 |
| 42,615 to 44,910 | 30% | 5,646.60 |
| 44,910 to 47,205 | 32% | 6,381.00 |
| 47,205 to 49,500 | 34% | 7,161.30 |
| 49,500 to 51,795 | 36% | 7,987.50 |
| 51,795 to 54,090 | 38% | 8,859.60 |
| 54,090 to 117,450 | 39% | 33,570.00 |
| 117,450 to 176,160 | 40% | 57,054.00 |
| 176,160 to 234,870 | 41% | 81,125.10 |
| above 234,870 | 42% | |

**How each class uses the scale.**

| Class | Computation | Source |
|---|---|---|
| 1 | Scale applied to adjusted taxable income | [LIR art. 120](https://impotsdirects.public.lu/dam-assets/fr/legislation/LIR/texte-coordonn-en-vigueur-au-1er-janvier-2026-ver-08052026.pdf) |
| 1a | Scale applied to income reduced by a quarter of its shortfall below EUR 79,380, with the marginal rate capped at 39% from EUR 51,804 to 117,450, then 40%, 41% and 42% as in the scale | LIR art. 120bis (same URL) |
| 2 | Twice the tax on half the income (splitting) | LIR art. 121 (same URL) |

**Other figures (tax year 2026).**

| Item | Amount | Source |
|---|---|---|
| Employment fund surcharge | 7% of the income tax; 9% where adjusted taxable income exceeds EUR 150,000 (classes 1 and 1a) or EUR 300,000 (class 2) | [ACD, fonds pour l'emploi](https://impotsdirects.public.lu/fr/az/f/fond_empl.html) |
| Employee credit (CIS) | EUR 300 + (gross - 936) x 0.029 for gross EUR 936 to 11,265; EUR 600 for 11,266 to 40,000; 600 - (gross - 40,000) x 0.015 for 40,001 to 79,999; nil from 80,000 | [LIR art. 154quater](https://impotsdirects.public.lu/dam-assets/fr/legislation/LIR/texte-coordonn-en-vigueur-au-1er-janvier-2026-ver-08052026.pdf) |
| CO2 credit (CI-CO2), employees and self-employed | EUR 216 for income EUR 936 to 40,000; 216 - (income - 40,000) x 0.0054 for 40,001 to 79,999; nil from 80,000 | LIR arts. 152ter and 154quater (same URL) |
| Self-employed credit (CII) | Same bands as the CIS, on net profit; EUR 300 where net profit is under EUR 936; needs compulsory social-security affiliation for that profit; not combined with the CIS or the pensioner credit; granted once a year for all self-employed profit; CII and CI-CO2 are deducted from the tax on assessment, and the ACD pays out any part the tax does not absorb | LIR art. 152ter(1), (3) and (4) (same URL) |
| Minimum-wage credit (CISSM), employees | EUR 81 a month for monthly gross EUR 1,800 to 3,000; 81 / 600 x (3,600 - gross) from 3,000 to 3,600; nil from 3,600 | LIR art. 139quater (same URL) |
| Single-parent credit (CIM) | EUR 3,504 below adjusted taxable income EUR 60,000; 3,504 - (income - 60,000) x 0.0612 from 60,000 to 105,000; EUR 750 above 105,000; reduced by 50% of child maintenance above EUR 2,712 a year | LIR art. 154ter (same URL) |
| Child tax reduction as a rebate (no family allowance paid) | EUR 922.50 per child | LIR art. 122(3) (same URL) |
| Flat deduction, employment expenses | EUR 540 (pensions EUR 300; investment income EUR 25) | LIR art. 107 (same URL) |
| Flat home-to-work deduction (employees) | EUR 99 per distance unit above 4 units, maximum EUR 2,574 | LIR art. 105bis (same URL) |
| Flat deduction, special expenses | EUR 480 (art. 113(1)); does not cover compulsory social contributions, which are deducted in full | LIR arts. 110 and 113 (same URL) |
| Extra-professional abatement, couples both working | EUR 4,500 | LIR art. 129b (same URL) |
| Immediate write-off of low-value assets | EUR 870 per item (owner-user) | LIR art. 34 (same URL) |
| Declining-balance cap | Lower of 3 x the linear rate and 30% (4 x and 40% for research equipment) | LIR art. 32(3) (same URL) |
| Building components (lifts, heating, sanitary, lighting, air-conditioning, IT cabling) | Up to 10% linear, no declining balance | [ACD circular L.I.R. n° 32/2](https://impotsdirects.public.lu/dam-assets/fr/legislation/legi22/lir-32-2-du-3052022.pdf) |
| Late-payment interest | 0.6% a month; 0.1% or 0.2% a month under an agreed payment plan | [ACD, prélèvements supplémentaires](https://impotsdirects.public.lu/fr/az/p/prelev.html) |
| Late-filing surcharge | Up to 10% of the tax | same URL |

**Social contributions (2026), for the tax computation only.** Full rules in `luxembourg-social-contributions`.

| Item | Amount | Source |
|---|---|---|
| Employee share | Pension 8.50%, sickness 2.80%, cash-benefit surcharge 0.25%, dependency 1.40% (total 12.95%) | [CCSS notice of 16 January 2026](https://ccss.public.lu/dam-assets/publications/2026/ccss-20260116-avis-80-99-fr-de.pdf) |
| Self-employed | Pension 17.00%, sickness 5.60%, cash benefits 0.50% where covered, dependency 1.40% (24.50% before accident insurance); accident 0.65% x factor | [CCSS, paramètres sociaux](https://ccss.public.lu/fr/parametres-sociaux.html) |
| Monthly ceiling (5 x SSM) | EUR 13,518.68 from 1 January 2026; EUR 13,856.63 from 1 June 2026 | CCSS notices of [16 January](https://ccss.public.lu/dam-assets/publications/2026/ccss-20260116-avis-80-99-fr-de.pdf) and [14 August 2026](https://ccss.public.lu/dam-assets/publications/2026/ccss-20260814-avis-80-99.pdf) |
| Social minimum wage, unskilled, 18+ | EUR 2,703.74 a month from 1 January 2026; EUR 2,771.33 from 1 June 2026 | same notices |
| Dependency abatement | EUR 675.93 a month from 1 January 2026; EUR 692.83 from 1 June 2026; the dependency contribution has no ceiling | same notices |

**VAT figures a self-employed client needs.** Franchise up to EUR 50,000 of annual turnover from 1 January 2025; a business that crosses it keeps the franchise to the end of that year if turnover stays within EUR 55,000, and loses it the next year ([AED, régime de franchise](https://pfi.public.lu/fr/professionnel/tva/sme.html)). Rates: 17% standard, 14% intermediate, 8% reduced, 3% super-reduced ([AED, taux nationaux](https://pfi.public.lu/fr/professionnel/tva/taxe-valeur-ajoutee/taux-nationaux-applicables.html)). For returns use `luxembourg-vat-return`.

## The taxable base

Work in this order.

1. **Net income per category.** Business profit, employment income less expenses (at least the art. 107 flat EUR 540 and the art. 105bis travel deduction), pensions, investment income, rental income. Residents include foreign income; income exempt under a treaty with a progression clause sets the rate (art. 134).
2. **Less special expenses.** Compulsory health, accident and pension contributions are deducted in full (art. 110 nos. 1 and 2). The dependency contribution is not on that list and is not deducted. Other special expenses (interest, insurance premiums, pension savings) are deducted as claimed, at least the EUR 480 flat amount (art. 113). Business losses of the 17 preceding years carry forward, oldest first, if regular accounts were kept; losses from years closed 1991 to 2016 have no time limit (art. 114).
3. **Less abatements** (arts. 127 to 130), such as the EUR 4,500 extra-professional abatement for couples who both work (art. 129b).
4. **Round down** to a multiple of EUR 50 (art. 126(2)), apply the scale for the class, add the employment fund surcharge, then deduct credits (CII, CIS, CI-CO2, CIM) and withholding and advances already paid.

**Business expenses.** An expense is deductible only if the business alone caused it (art. 45(1)); expenses linked to exempt income are not (art. 45(2)). Never deductible: household and lifestyle costs, including spending driven by the client's social or economic position even when it helps the business (art. 12 no. 1); gifts (art. 12 no. 2); income tax and net wealth tax (art. 12 no. 3a); fines and penalties (art. 12 no. 4). Pay to the operator or to a spouse taxed jointly is not an expense (art. 48 no. 3). Home-to-work travel of the self-employed is deductible only within the limits of the grand-ducal regulation under art. 46 no. 9.

**Representation costs.** The LIR sets no fixed percentage. A client meal is deductible only with a named guest and a business purpose (art. 45(1)); without them it is private (art. 12 no. 1). The client's own share of a meal is private.

**Mixed-use costs** (car, phone, home office): deduct only the business share on a documented basis (mileage log, floor area of a room used only for work). Default 0% until the client documents it.

**Depreciation.**

- **Linear.** Cost (less any salvage value) spread equally over the useful life remaining from the start of the year (art. 32(1)). The useful life is set in years from the kind and conditions of use of the asset (art. 32(2)). The LIR and the ACD publish no table of rates by asset type; the rate is 100% divided by the useful life.
- **Deferred linear.** On request with the return, the client may deduct less than the linear charge and carry the unused part forward; the balance is deducted in the last year of the useful life (art. 32(1a); [ACD circular L.I.R. n° 32/1](https://impotsdirects.public.lu/dam-assets/fr/legislation/legi18/circulairelir32-1du15052018-amortissement-differe.pdf)).
- **Declining balance.** Tangible assets other than buildings, where the owner is the user, at a fixed rate on book value capped at the lower of 3 x the linear rate and 30%; it needs the bookkeeping entries set by regulation. Switching to linear is allowed; switching from linear to declining balance is not (art. 32(3) to (5)).
- **Immediate write-off.** An asset with a useful life of one year or less, or costing EUR 870 or less per item where the owner is the user, may be written off in the year of acquisition; not for assets taken over with a business (art. 34).
- **Year of acquisition.** Depreciation runs in principle from purchase or entry into service. As a simplification, a full year may be taken for an asset bought in the first half of the year and half a year for one bought in the second half ([Guichet.lu, résultat d'exploitation](https://guichet.public.lu/fr/entreprises/fiscalite/impots-benefices/benefices-patrimoine/entreprise-individuelle-societe-personne/calcul-resultat-exploitation.html)).
- **Acquisition price** includes transport, assembly and customs; it excludes input VAT the client can deduct and includes VAT it cannot; a public subsidy tied directly to the purchase reduces it ([ACD circular L.I.R. n° 34/1](https://impotsdirects.public.lu/dam-assets/fr/legislation/circulaires/circulaire-lir-n-34-1-du-19-juin-1998.pdf)).
- **Extraordinary write-down** for extraordinary technical or economic loss (art. 31).

**VAT and profit.** For a VAT-registered client, VAT collected is not income and recoverable input VAT is not an expense; blocked input VAT and foreign VAT that cannot be reclaimed are part of the cost. A client under the franchise records income and purchases gross.

**Classifying a bank statement.** Merchant names never decide business use on their own.

| Bank text | Treatment |
|---|---|
| Client transfers (VIREMENT, VIR, ÜBERWEISUNG), HONORAIRES, Stripe, PayPal, Wise, Upwork, Malt payouts | Business income, net of VAT if registered; match payouts to invoices |
| SALAIRE, GEHALT, PAYROLL | Employment income, tax already withheld |
| LOYER REÇU, MIETE; INTÉRÊTS, DIVIDENDE | Rental or investment income (separate categories) |
| AIDE, SUBVENTION | Subsidy tied to an asset reduces its cost (circular 34/1); an operating subsidy is income |
| Office rent, RC Pro insurance, fiduciaire and legal fees, software subscriptions, ads, training, bank and payment fees | Operating expense (art. 45(1)) |
| ENOVOS, POST, TANGO, ORANGE, fuel, parking | Business share only |
| RESTAURANT, DÉJEUNER CLIENT | Blocked until guest and purpose are documented |
| Groceries, personal spending, drawings | Not deductible (art. 12 no. 1) |
| AMENDE, PÉNALITÉ | Not deductible (art. 12 no. 4) |
| ACD, IMPÔT, AVANCE | Not an expense; advances are credited against the tax |
| CCSS COTISATIONS | Special expense, not an operating expense; take out the dependency part |
| TVA payments, own-account transfers, loan principal | Exclude |
| Laptop, furniture, car | EUR 870 test (art. 34), else capitalise and depreciate (art. 32) |

## Deadlines and filing

| Item | Rule | Source |
|---|---|---|
| Tax year | Calendar year | [LIR art. 1(2)](https://impotsdirects.public.lu/dam-assets/fr/legislation/LIR/texte-coordonn-en-vigueur-au-1er-janvier-2026-ver-08052026.pdf) |
| Annual return | Form 100 (modèle 100), online through MyGuichet.lu with LuxTrust, as a PDF through MyGuichet, or on paper | [ACD, formulaires personnes physiques](https://impotsdirects.public.lu/fr/formulaires/pers_physiques.html) |
| Return deadline | 31 December of the following year (from tax year 2022); tax year 2026 is due 31 December 2027 | [ACD, délais de dépôt](https://impotsdirects.public.lu/fr/az/d/delais/depot.html) |
| Annual adjustment (employees and pensioners not taxed by assessment) | Form 163 R (residents) or 163 NR (non-residents), by 31 December of the following year; the ACD page gives 31 December 2026 for tax year 2025 | [ACD, décompte annuel](https://impotsdirects.public.lu/fr/formulaires/decompte_annuel.html); LIR art. 145 |
| Quarterly advances | 10 March, 10 June, 10 September, 10 December of the tax year; each in principle a quarter of the last assessed tax after withholding; the ACD may change them on request or of its own motion | [LIR art. 135](https://impotsdirects.public.lu/dam-assets/fr/legislation/LIR/texte-coordonn-en-vigueur-au-1er-janvier-2026-ver-08052026.pdf) |
| Balance on assessment | Due by the end of the month after the month the assessment notice (bulletin d'impôt) is received | [ACD, prélèvements supplémentaires](https://impotsdirects.public.lu/fr/az/p/prelev.html) |

## Penalties and interest

- **Late filing:** the tax office can add a supplement of up to 10% of the tax. If the return is still missing, it sets a final deadline and then a penalty payment (astreinte) whose amount it announces in advance ([ACD, prélèvements supplémentaires](https://impotsdirects.public.lu/fr/az/p/prelev.html)).
- **Late payment:** interest at 0.6% a month from the end of the month after the assessment notice is received; also on a late advance. Under an agreed payment plan the rate is 0.1% or 0.2% a month (same source).
- **No return at all:** the tax office assesses by estimate.
- A client with arrears under enforcement goes to a Luxembourg tax adviser.

## Cross-border points

- **Non-residents** are taxed only on Luxembourg-source income (arts. 2(3) and 156); their classes, the 90% option (art. 157ter) and frontier-worker rules are in `lu-cross-border`.
- **Residents with foreign income:** income exempt under a treaty is still counted to set the rate (exemption with progression, art. 134).
- **Impatriates** (art. 115 no. 13b): `lu-cross-border`.
- **Social security** of people working in more than one state (Reg. 883/2004, telework agreement): `lu-cross-border`.
- **Foreign VAT** the client cannot reclaim is part of the cost.

## Worked examples

Both examples are 2026 estimates for residents. The client paid no advances and has no other income. Pass the taxable income to the deterministic engine for the filed figure.

### Example 1: single self-employed consultant, class 1

A single consultant, no children, aged 40, class 1. Net profit for 2026 is EUR 60,000. She paid EUR 13,000 of compulsory health, accident and pension contributions to the CCSS and EUR 750 of dependency contribution. She has no other special expenses.

**Taxable income.** Profit 60,000 less contributions 13,000 (art. 110 no. 2; the 750 dependency contribution is not deductible) less the EUR 480 flat special-expense deduction (art. 113) = 46,520, rounded down to EUR 46,500 (art. 126(2)).

**Tax.** Cumulative tax at EUR 44,910 is 5,646.60. The remaining 1,590 is taxed at 32% = 508.80. Income tax = **6,155.40**. Surcharge at 7% (income under EUR 150,000) = 430.88. Total = 6,586.28.

**Credits.** Net profit is between EUR 40,001 and 79,999. CII = 600 - (60,000 - 40,000) x 0.015 = 300.00. CI-CO2 = 216 - 20,000 x 0.0054 = 108.00. Tax payable = 6,586.28 - 408.00 = **EUR 6,178.28**.

```oa-check
name: LU class 1, self-employed, net profit EUR 60,000 (2026)
inputs:
  profit: 60000
  contributions: 13000
  forfait: 480
steps:
  - taxable: floor((profit - contributions - forfait) / 50) * 50
  - tax: 5646.60 + (taxable - 44910) * 0.32
  - surcharge: round(tax * 0.07, 2)
  - total: tax + surcharge
  - cii: 600 - (profit - 40000) * 0.015
  - co2: 216 - (profit - 40000) * 0.0054
  - payable: total - cii - co2
expected:
  taxable: 46500
  tax: 6155.40
  surcharge: 430.88
  total: 6586.28
  cii: 300.00
  co2: 108.00
  payable: 6178.28
```

### Example 2: married sole earner, class 2, with capital assets

Spouses taxed jointly, class 2. Only one spouse works, as a self-employed engineer, so there is no extra-professional abatement. Profit before depreciation is EUR 92,000. On 1 January 2026 the engineer put into service equipment costing EUR 12,000 net of deductible VAT, useful life 5 years, booked on declining balance. The same day he bought a monitor for EUR 450 net. He paid EUR 19,000 of compulsory health, accident and pension contributions.

**Depreciation.** Linear rate 20%; declining-balance rate capped at the lower of 3 x 20% and 30%, so 30% (art. 32(3)): 12,000 x 30% = 3,600. The asset entered service on 1 January, so a full year applies. The monitor costs under EUR 870 and is written off in full: 450 (art. 34). Profit = 92,000 - 3,600 - 450 = 87,950.

**Taxable income.** 87,950 - 19,000 - 480 = 68,470, rounded down to EUR 68,450.

**Tax.** Class 2 takes twice the tax on half the income (art. 121). Half = 34,225. Tax on the half = 2,663.10 + (34,225 - 33,435) x 22% = 2,836.90. Doubled = **5,673.80**. Surcharge at 7% (income under EUR 300,000) = 397.17. Total = 6,070.97.

**Credits.** Net profit is EUR 80,000 or more, so there is no CII and no CI-CO2 (art. 152ter(2)). Tax payable = **EUR 6,070.97**.

The edge cases: the declining-balance cap, the EUR 870 write-off, the splitting, and the credit cut-off at EUR 80,000 of profit. Had the equipment been bought in the second half of the year, only half a year's charge (1,800) would apply under the Guichet.lu simplification.

```oa-check
name: LU class 2, sole earner, depreciation and splitting (2026)
inputs:
  profit_before_dep: 92000
  equipment: 12000
  life: 5
  monitor: 450
  contributions: 19000
  forfait: 480
steps:
  - db_rate: min(3 / life, 0.30)
  - depreciation: equipment * db_rate
  - writeoff: monitor
  - profit: profit_before_dep - depreciation - writeoff
  - taxable: floor((profit - contributions - forfait) / 50) * 50
  - half: taxable / 2
  - tax_half: 2663.10 + (half - 33435) * 0.22
  - tax: tax_half * 2
  - surcharge: round(tax * 0.07, 2)
  - payable: tax + surcharge
expected:
  depreciation: 3600.00
  profit: 87950
  taxable: 68450
  tax: 5673.80
  surcharge: 397.17
  payable: 6070.97
```

## Ask the client first

1. Family situation on 1 January 2026: single, married or partnered (and do you file jointly), widowed, divorced or separated in the last three years; children in the household and their ages; your age. This sets the class (1, 1a or 2) and the credits.
2. What income did you have in 2026: self-employed profit, salary, pension, rent, interest or dividends, and any income from abroad?
3. For self-employed profit: are you VAT-registered or under the franchise, which assets did you buy (price, date, useful life), and which costs are partly private (car, phone, home office)?
4. What did you pay to the CCSS in 2026, split between health, accident, pension and dependency?
5. Which advances did you pay on 10 March, June, September and December, and did an employer withhold tax?
6. Do you live or work partly outside Luxembourg? If yes, use `lu-cross-border` first.

## Sources

| Source | URL | Read on |
|---|---|---|
| LIR, consolidated text in force on 1 January 2026 (ACD, updated 8 May 2026): arts. 1, 2, 12, 31, 32, 34, 45, 46, 48, 105bis, 107, 110, 113, 114, 118 to 123, 126, 129b, 134, 135, 139quater, 145, 152ter, 153, 154ter, 154quater | https://impotsdirects.public.lu/dam-assets/fr/legislation/LIR/texte-coordonn-en-vigueur-au-1er-janvier-2026-ver-08052026.pdf | 2026-10-23 |
| ACD circular L.I.R. n° 32/1 of 15 May 2018 (deferred depreciation) | https://impotsdirects.public.lu/dam-assets/fr/legislation/legi18/circulairelir32-1du15052018-amortissement-differe.pdf | 2026-10-23 |
| ACD circular L.I.R. n° 32/2 of 30 May 2022 (building components, 10%) | https://impotsdirects.public.lu/dam-assets/fr/legislation/legi22/lir-32-2-du-3052022.pdf | 2026-10-23 |
| ACD circular L.I.R. n° 34/1 of 19 June 1998 (low-value assets, acquisition price) | https://impotsdirects.public.lu/dam-assets/fr/legislation/circulaires/circulaire-lir-n-34-1-du-19-juin-1998.pdf | 2026-10-23 |
| Guichet.lu, résultat d'exploitation d'une entreprise individuelle (year-of-acquisition simplification; page last changed 11 June 2018) | https://guichet.public.lu/fr/entreprises/fiscalite/impots-benefices/benefices-patrimoine/entreprise-individuelle-societe-personne/calcul-resultat-exploitation.html | 2026-10-23 |
| ACD, fonds pour l'emploi (7% / 9%) | https://impotsdirects.public.lu/fr/az/f/fond_empl.html | 2026-10-23 |
| ACD, délais de dépôt (31 December of the following year) | https://impotsdirects.public.lu/fr/az/d/delais/depot.html | 2026-10-23 |
| ACD, formulaires personnes physiques (Form 100, MyGuichet) | https://impotsdirects.public.lu/fr/formulaires/pers_physiques.html | 2026-10-23 |
| ACD, décompte annuel (Forms 163 R and 163 NR, deadline) | https://impotsdirects.public.lu/fr/formulaires/decompte_annuel.html | 2026-10-23 |
| ACD, prélèvements supplémentaires (10% supplement, astreinte, 0.6% interest) | https://impotsdirects.public.lu/fr/az/p/prelev.html | 2026-10-23 |
| CCSS, avis aux employeurs, taux de cotisation au 1 January 2026 (abatement EUR 675.93) | https://ccss.public.lu/dam-assets/publications/2026/ccss-20260116-avis-80-99-fr-de.pdf | 2026-10-23 |
| CCSS, avis aux employeurs, minima et maximum au 1 June 2026 (abatement EUR 692.83) | https://ccss.public.lu/dam-assets/publications/2026/ccss-20260814-avis-80-99.pdf | 2026-10-23 |
| CCSS, paramètres sociaux (rates, SSM, ceiling) | https://ccss.public.lu/fr/parametres-sociaux.html | 2026-10-23 |
| AED, régime de franchise (EUR 50,000 / 55,000 from 2025) | https://pfi.public.lu/fr/professionnel/tva/sme.html | 2026-10-23 |
| AED, taux nationaux (17 / 14 / 8 / 3%) | https://pfi.public.lu/fr/professionnel/tva/taxe-valeur-ajoutee/taux-nationaux-applicables.html | 2026-10-23 |

Not yet confirmed: the year-of-acquisition rule rests only on the Guichet.lu page (last changed 2018, and it still says depreciation cannot be deferred, which art. 32(1a) has allowed since 2017); neither the LIR nor an ACD circular states it, so a reviewer must confirm current ACD practice before a part-year charge is filed. Whether the ACD smooths the step from 7% to 9% surcharge just above EUR 150,000 / 300,000 on assessment (the ACD page shows a plain step). The AED rates page was last updated 28 December 2023, and the consolidated VAT law (LTVA) was not read for 2026.

> Contributed by Ryan Duguid.

> Contributed by Michael Cutajar.

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
