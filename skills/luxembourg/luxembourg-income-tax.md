---
name: luxembourg-income-tax
description: "Luxembourg resident personal income tax for 2026: full progressive scale, classes 1/1a/2, statutory rounding, employment-fund surcharge, self-employed credits, business costs, depreciation, compulsory contributions, Form 100, annual adjustment and advances. Trigger on impôt sur le revenu, indépendant, modèle 100, barème, classe d'impôt. Explicit holds cover employee/family credits, social-rate estimates, VAT and specialist cases."
version: 0.7
jurisdiction: LU
tax_year: 2026
last_updated: 2026-11-27
depends_on:
  - income-tax-workflow-base
category: international
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
tier: 2
domain: income-tax
type: computation
---

# Luxembourg personal income tax: residents and the self-employed (2026)

Compute the resident's annual income tax using the full scale below, the confirmed class, statutory rounding and applicable credits. Collect residence, family situation, all income, expense evidence, CCSS component statements and payments first. Unknown inputs stay unresolved; do not invent a tax class, VAT status or business-use percentage.

## Who this applies to

Residents have their fiscal domicile or habitual stay in Luxembourg and are taxed on domestic and foreign income (LIR art. 2). The income year is the calendar year (art. 1). This Guide covers individuals, including sole operators in trade, farming/forestry and liberal professions; salary, pensions, investment, rent and miscellaneous income remain separate categories (art. 10). [LIR](https://impotsdirects.public.lu/dam-assets/fr/legislation/LIR/texte-coordonn-en-vigueur-au-1er-janvier-2026-ver-08052026.pdf).

| Class | Eligibility and computation | Source |
|---|---|---|
| 1 | Anyone outside 1a and 2; apply the scale to adjusted taxable income | LIR arts. 119–120; https://impotsdirects.public.lu/dam-assets/fr/legislation/LIR/texte-coordonn-en-vigueur-au-1er-janvier-2026-ver-08052026.pdf |
| 1a | Unless in class 2: widowed; entitled to the child tax reduction under arts. 122–123; or completed the 64th year at the start of the year. Apply the scale to income reduced by one quarter of its complement to EUR 79,380, subject to maximum incremental rates of 39% for EUR 51,804–117,450, then 40%, 41%, 42% for the remaining upper bands | LIR arts. 119, 120bis; https://impotsdirects.public.lu/dam-assets/fr/legislation/LIR/texte-coordonn-en-vigueur-au-1er-janvier-2026-ver-08052026.pdf |
| 2 | Jointly taxed under arts. 3/3bis; or widowed within the preceding three years; or divorced/judicially or legally separated within those years, without using that concession during the preceding five years. Twice the unrounded scale tax on half the adjusted taxable income; apply art. 124 to the resulting class-2 tax | LIR arts. 119, 121, 124; https://impotsdirects.public.lu/dam-assets/fr/legislation/LIR/texte-coordonn-en-vigueur-au-1er-janvier-2026-ver-08052026.pdf |

Joint-tax eligibility/elections and changes during the year require their own conditions; a marriage certificate alone does not settle the class. Check this point with one of our partner accountants.

## Rates, bands and thresholds

LIR art. 118 in force for 2026 retains the scale applicable from 2025. The cumulative column is **computed, unrounded tariff arithmetic**, not the assessed basic tax. Round adjusted taxable income down to a multiple of EUR 50 before applying the tariff; then round the class tax down to a whole euro and treat a basic tax below EUR 12 as zero (arts. 124, 126). [LIR](https://impotsdirects.public.lu/dam-assets/fr/legislation/LIR/texte-coordonn-en-vigueur-au-1er-janvier-2026-ver-08052026.pdf).

| Taxable income (EUR) | Rate | Cumulative tax at top of band (EUR) | Source |
|---|---|---|---|
| 0 to 13,230 | 0% | 0.00 | https://impotsdirects.public.lu/dam-assets/fr/legislation/LIR/texte-coordonn-en-vigueur-au-1er-janvier-2026-ver-08052026.pdf |
| 13,230 to 15,435 | 8% | 176.40 (computed) | https://impotsdirects.public.lu/dam-assets/fr/legislation/LIR/texte-coordonn-en-vigueur-au-1er-janvier-2026-ver-08052026.pdf |
| 15,435 to 17,640 | 9% | 374.85 (computed) | https://impotsdirects.public.lu/dam-assets/fr/legislation/LIR/texte-coordonn-en-vigueur-au-1er-janvier-2026-ver-08052026.pdf |
| 17,640 to 19,845 | 10% | 595.35 (computed) | https://impotsdirects.public.lu/dam-assets/fr/legislation/LIR/texte-coordonn-en-vigueur-au-1er-janvier-2026-ver-08052026.pdf |
| 19,845 to 22,050 | 11% | 837.90 (computed) | https://impotsdirects.public.lu/dam-assets/fr/legislation/LIR/texte-coordonn-en-vigueur-au-1er-janvier-2026-ver-08052026.pdf |
| 22,050 to 24,255 | 12% | 1,102.50 (computed) | https://impotsdirects.public.lu/dam-assets/fr/legislation/LIR/texte-coordonn-en-vigueur-au-1er-janvier-2026-ver-08052026.pdf |
| 24,255 to 26,550 | 14% | 1,423.80 (computed) | https://impotsdirects.public.lu/dam-assets/fr/legislation/LIR/texte-coordonn-en-vigueur-au-1er-janvier-2026-ver-08052026.pdf |
| 26,550 to 28,845 | 16% | 1,791.00 (computed) | https://impotsdirects.public.lu/dam-assets/fr/legislation/LIR/texte-coordonn-en-vigueur-au-1er-janvier-2026-ver-08052026.pdf |
| 28,845 to 31,140 | 18% | 2,204.10 (computed) | https://impotsdirects.public.lu/dam-assets/fr/legislation/LIR/texte-coordonn-en-vigueur-au-1er-janvier-2026-ver-08052026.pdf |
| 31,140 to 33,435 | 20% | 2,663.10 (computed) | https://impotsdirects.public.lu/dam-assets/fr/legislation/LIR/texte-coordonn-en-vigueur-au-1er-janvier-2026-ver-08052026.pdf |
| 33,435 to 35,730 | 22% | 3,168.00 (computed) | https://impotsdirects.public.lu/dam-assets/fr/legislation/LIR/texte-coordonn-en-vigueur-au-1er-janvier-2026-ver-08052026.pdf |
| 35,730 to 38,025 | 24% | 3,718.80 (computed) | https://impotsdirects.public.lu/dam-assets/fr/legislation/LIR/texte-coordonn-en-vigueur-au-1er-janvier-2026-ver-08052026.pdf |
| 38,025 to 40,320 | 26% | 4,315.50 (computed) | https://impotsdirects.public.lu/dam-assets/fr/legislation/LIR/texte-coordonn-en-vigueur-au-1er-janvier-2026-ver-08052026.pdf |
| 40,320 to 42,615 | 28% | 4,958.10 (computed) | https://impotsdirects.public.lu/dam-assets/fr/legislation/LIR/texte-coordonn-en-vigueur-au-1er-janvier-2026-ver-08052026.pdf |
| 42,615 to 44,910 | 30% | 5,646.60 (computed) | https://impotsdirects.public.lu/dam-assets/fr/legislation/LIR/texte-coordonn-en-vigueur-au-1er-janvier-2026-ver-08052026.pdf |
| 44,910 to 47,205 | 32% | 6,381.00 (computed) | https://impotsdirects.public.lu/dam-assets/fr/legislation/LIR/texte-coordonn-en-vigueur-au-1er-janvier-2026-ver-08052026.pdf |
| 47,205 to 49,500 | 34% | 7,161.30 (computed) | https://impotsdirects.public.lu/dam-assets/fr/legislation/LIR/texte-coordonn-en-vigueur-au-1er-janvier-2026-ver-08052026.pdf |
| 49,500 to 51,795 | 36% | 7,987.50 (computed) | https://impotsdirects.public.lu/dam-assets/fr/legislation/LIR/texte-coordonn-en-vigueur-au-1er-janvier-2026-ver-08052026.pdf |
| 51,795 to 54,090 | 38% | 8,859.60 (computed) | https://impotsdirects.public.lu/dam-assets/fr/legislation/LIR/texte-coordonn-en-vigueur-au-1er-janvier-2026-ver-08052026.pdf |
| 54,090 to 117,450 | 39% | 33,570.00 (computed) | https://impotsdirects.public.lu/dam-assets/fr/legislation/LIR/texte-coordonn-en-vigueur-au-1er-janvier-2026-ver-08052026.pdf |
| 117,450 to 176,160 | 40% | 57,054.00 (computed) | https://impotsdirects.public.lu/dam-assets/fr/legislation/LIR/texte-coordonn-en-vigueur-au-1er-janvier-2026-ver-08052026.pdf |
| 176,160 to 234,870 | 41% | 81,125.10 (computed) | https://impotsdirects.public.lu/dam-assets/fr/legislation/LIR/texte-coordonn-en-vigueur-au-1er-janvier-2026-ver-08052026.pdf |
| above 234,870 | 42% | | https://impotsdirects.public.lu/dam-assets/fr/legislation/LIR/texte-coordonn-en-vigueur-au-1er-janvier-2026-ver-08052026.pdf |


**Employment fund:** 7% on basic income tax; the 9% rate applies to the tax attributable to the slice of adjusted taxable income above EUR 150,000 (classes 1/1a) or EUR 300,000 (class 2). It does not reprice all tax at 9% on crossing the boundary. Law of 30 June 1976 art. 6(1), as amended by law of 21 December 2012 art. 5: [2026 statutory collection, p. 419](https://igss.gouvernement.lu/dam-assets/publications/code-de-la-s%C3%A9curit%C3%A9-sociale/css2026.pdf), [enacted amendment](https://impotsdirects.public.lu/content/dam/acd/fr/legislation/legi12/M__morial_A_-_N___270_du_28_d__cembre_2012.pdf). The ACD's short [summary](https://impotsdirects.public.lu/fr/az/f/fond_empl.html) omits the slice condition; the statute controls.

**Self-employed credits (LIR art. 152ter).** Luxembourg must have the taxing right over the professional profit, with personal compulsory affiliation to a Luxembourg or qualifying treaty social-security scheme. Each credit is granted once for all self-employed income. A second spousal credit requires qualifying spouse-helper affiliation. Do not cumulate with employee or pensioner credits; simultaneous entitlements are regularised on assessment. [LIR](https://impotsdirects.public.lu/dam-assets/fr/legislation/LIR/texte-coordonn-en-vigueur-au-1er-janvier-2026-ver-08052026.pdf).

| Annual net profit, including art. 134 exempt profit | CII | Self-employed CI-CO2 | Source |
|---|---|---|---|
| Below EUR 936 | EUR 300 | None | LIR art. 152ter; https://impotsdirects.public.lu/dam-assets/fr/legislation/LIR/texte-coordonn-en-vigueur-au-1er-janvier-2026-ver-08052026.pdf |
| EUR 936–11,265 | EUR 300 + (profit − 936) × 0.029 | EUR 216 | LIR art. 152ter; https://impotsdirects.public.lu/dam-assets/fr/legislation/LIR/texte-coordonn-en-vigueur-au-1er-janvier-2026-ver-08052026.pdf |
| EUR 11,266–40,000 | EUR 600 | EUR 216 | LIR art. 152ter; https://impotsdirects.public.lu/dam-assets/fr/legislation/LIR/texte-coordonn-en-vigueur-au-1er-janvier-2026-ver-08052026.pdf |
| EUR 40,001–79,999 | EUR 600 − (profit − 40,000) × 0.015 | EUR 216 − (profit − 40,000) × 0.0054 | LIR art. 152ter; https://impotsdirects.public.lu/dam-assets/fr/legislation/LIR/texte-coordonn-en-vigueur-au-1er-janvier-2026-ver-08052026.pdf |
| From EUR 80,000 | None | None | LIR art. 152ter; https://impotsdirects.public.lu/dam-assets/fr/legislation/LIR/texte-coordonn-en-vigueur-au-1er-janvier-2026-ver-08052026.pdf |

These are annual amounts limited to the qualifying activity period, with monthly amounts equal to annual amounts divided by 12 and rounding upward to the next cent. They are credited and refundable only through assessment; insufficient tax does not extinguish the balance (art. 152ter(2)–(4)). [LIR](https://impotsdirects.public.lu/dam-assets/fr/legislation/LIR/texte-coordonn-en-vigueur-au-1er-janvier-2026-ver-08052026.pdf).

## The base

Use a working paper showing receipts and allowable costs by category, net business profit, other net income, special expenses, abatements, adjusted taxable income, class tax, surcharge, credits and payments. Bank receipts alone do not establish the correct taxable year or complete profit.

1. Separate the eight income categories in art. 10. For business costs, art. 45 permits expenses caused exclusively by the business and excludes costs connected with exempt income. Private household/lifestyle costs, gifts outside special-expense rules, personal income/wealth tax and statutory fines/penalties are excluded under art. 12. Pay to the operator or jointly taxed spouse is excluded under art. 48(3). [LIR](https://impotsdirects.public.lu/dam-assets/fr/legislation/LIR/texte-coordonn-en-vigueur-au-1er-janvier-2026-ver-08052026.pdf).
2. Use invoices, contracts and a documented allocation to establish business expenditure. Merchant names do not prove deductibility. Hold mixed car/phone/internet/home-office costs and meals until the business component and private element have been established. No flat entertainment percentage, dedicated-room test or automatic deduction follows from a bank label. Check this point with one of our partner accountants.
3. Deduct qualifying compulsory contributions as special expenses: employee health/pension; self-employed health/accident/pension (art. 110(1)–(2)). Contributions related to exempt income are excluded, subject to the employee salary-supplement exception in art. 110(1). Dependency insurance is not in these deductible components. Split the CCSS statement; do not deduct the whole payment automatically. [LIR](https://impotsdirects.public.lu/dam-assets/fr/legislation/LIR/texte-coordonn-en-vigueur-au-1er-janvier-2026-ver-08052026.pdf).
4. The EUR 480 minimum for the special expenses enumerated in art. 113(1) is separate from compulsory contributions. It is a minimum for that basket, not an additional deduction on top of larger actual expenses. Prorate for whole months of tax liability when less than a full year. For jointly taxed spouses each earning salary, art. 113(2) provides the separate-forfait rule and limits the lower earner's amount; sole-earner example 2 uses EUR 480. [LIR](https://impotsdirects.public.lu/dam-assets/fr/legislation/LIR/texte-coordonn-en-vigueur-au-1er-janvier-2026-ver-08052026.pdf).
5. Employee/pension/investment expense forfaits, travel allowances, other special-expense caps, loss carryforwards and family/extra-professional abatements are held below. Resolve them before finalising a case that needs them.
6. Round the adjusted taxable base down to EUR 50; calculate the class tax; round it down to EUR 1 (zero below EUR 12); apply the statutory surcharge; then the applicable credits and established withholding/advances. [LIR arts. 124, 126, 152ter](https://impotsdirects.public.lu/dam-assets/fr/legislation/LIR/texte-coordonn-en-vigueur-au-1er-janvier-2026-ver-08052026.pdf).

**Depreciation.** Under art. 32(1)–(2), divide the remaining net acquisition/production value less salvage value evenly over the remaining usual life, established from the asset's type and use; do not invent a statutory laptop/car rate. For tangible owner-used assets other than buildings, art. 32(3) caps declining balance at the lower of three times straight-line and 30%; exclusively scientific/technical research equipment has the four-times/40% limits. Required bookkeeping under art. 32(4) must be established. Switching from declining balance to linear is permitted (mandatory on extraordinary depreciation); switching from linear/deferred to declining balance is prohibited (art. 32(5)). [LIR](https://impotsdirects.public.lu/dam-assets/fr/legislation/LIR/texte-coordonn-en-vigueur-au-1er-janvier-2026-ver-08052026.pdf).

Art. 34 allows immediate depreciation for a useful life no longer than one year, or an owner-used independently functional asset costing no more than EUR 870; it excludes assets acquired with a business or autonomous business part. Test the functional asset, not an artificial invoice split. Acquisition cost includes transport, assembly and customs, less discounts/direct acquisition grants; include irrecoverable VAT and exclude deductible input VAT. Depreciation begins when the acquired asset is economically available, or a self-built asset is ready; actual payment/immediate use does not determine that date. [LIR art. 34](https://impotsdirects.public.lu/dam-assets/fr/legislation/LIR/texte-coordonn-en-vigueur-au-1er-janvier-2026-ver-08052026.pdf), [circular 34/1 pp. 3–4, historic franc threshold superseded by current art. 34](https://impotsdirects.public.lu/dam-assets/fr/legislation/circulaires/circulaire-lir-n-34-1-du-19-juin-1998.pdf).

**Bank descriptions and destinations.** These are intake cues only; confirm direction, counterparty, invoice, ownership and economic nature before populating the working paper.

| Original pattern group | Working-paper destination / required evidence |
|---|---|
| Client VIREMENT/VIR/ÜBERWEISUNG/TRANSFER/PAIEMENT FACTURE; HONORAIRES/FEES/PRESTATIONS; Stripe, PayPal, Wise; Upwork/Fiverr/Malt/Toptal | Reconcile invoices, gross customer receipts, platform fees and VAT separately; never treat the net payout as complete turnover automatically |
| SALAIRE/TRAITEMENT/GEHALT/PAYROLL; LOYER REÇU/MIETE; INTÉRÊTS/ZINSEN/DIVIDENDE | Separate employment, rental and investment categories; obtain annual certificates |
| REMBOURSEMENT IMPÔT/ACD REFUND; AIDE/SUBVENTION/GRANT | Establish what is refunded or subsidised; capital-acquisition grant reduces asset cost where directly linked; other grant treatment needs confirmation |
| Office rent, RC Pro, fiduciaire/accountant/audit, legal/notary, supplies, marketing, training/CPD/conference, professional/chamber dues, bank/payment fees, postage | Business-causation and exclusions test above, not automatic deductibility |
| Google/Microsoft, Adobe/Canva/Figma/Notion/Slack/Zoom, Anthropic/OpenAI/GitHub/Atlassian/Dropbox; domain/hosting/AWS/OVH; perpetual software licence | Establish subscription versus acquired asset and business purpose |
| Enovos/Creos/Leo/electricity/water; Post/Tango/Orange/mobile; fuel/parking/vignette; flights/hotels/rail/bus/taxi | Document purpose and mixed-use component; commuting and home-office outcomes held |
| Restaurant/client meal; Cactus/Auchan/Delhaize/groceries; drawings; amende/pénalité; ACD/impôt/avance | Establish nature; apply exclusions/holds above; income-tax advances belong in payments, not expenses |
| CCSS; TVA; own-account/internal transfer; loan repayment; cash withdrawal | Reconcile statements and split components/principal/interest; cash movement alone cannot establish a deduction |
| Laptop/printer/scanner/furniture/chair/car | Asset register; cost, ownership, functional unit, availability, useful life, private share and method |

BCEE/Spuerkeess, BIL, BGL, ING and Revolut/Wise formats and French/German labels are parsing cues only. Keep original statement, currency and reconciliation; the former deterministic classifier, default assumptions, duplicate glossary and spreadsheet layout are not legal evidence.

## Deadlines and filing

| Item | Rule | Source |
|---|---|---|
| Form 100 | Assessment taxpayers use modèle 100; eligible filers use MyGuichet with LuxTrust, alternatively PDF through MyGuichet or printed forms by post/office letterbox; ordinary email is not accepted | https://impotsdirects.public.lu/fr/formulaires/pers_physiques.html |
| Annual return | 31 December of the following year: for 2026, 31 December 2027 (derived date). Also respect specific ACD correspondence deadlines | https://impotsdirects.public.lu/fr/az/d/delais/depot.html |
| Annual adjustment | Form 163 R for resident employees/pensioners; 163 NR is the non-resident form. Taxpayers subject to assessment use Form 100. The currently published forms cover 2025 and give 31 December 2026; do not file a 2025 form as a 2026 return | https://impotsdirects.public.lu/fr/formulaires/decompte_annuel.html |
| Quarterly advances | 10 March, 10 June, 10 September, 10 December; normally one quarter of the last assessed tax after withholding. Probable current-year tax can replace it; a substantiated request requires adjustment and ACD can adjust of its own motion | LIR art. 135; https://impotsdirects.public.lu/dam-assets/fr/legislation/LIR/texte-coordonn-en-vigueur-au-1er-janvier-2026-ver-08052026.pdf |
| Assessment balance | End of the month following receipt of the assessment notice | https://impotsdirects.public.lu/fr/az/p/prelev.html |

For employee/pensioner assessment eligibility, the art. 153 tests and implementing regulations must be checked, including any small-additional-income adjustment. Do not use the old bare EUR 600 trigger or the mere fact that spouses are jointly taxed as a complete filing decision. Check this point with one of our partner accountants.

## Penalties and interest

ACD may impose a late-filing supplement up to 10% of the tax. For an astreinte, it first gives a final deadline and the announced amount, then fixes that amount if no response; refusal can lead to estimated assessment. The former unqualified EUR 25,000 fine is held. [ACD](https://impotsdirects.public.lu/fr/az/p/prelev.html).

Late-payment interest is 0.6% monthly at the due date, including late advances and late-filing supplements. Requested payment extensions can carry 0.1%/0.2% monthly interest. Missing a plan instalment makes full-rate interest due on the outstanding balance from that missed date; full rate also applies if the request was late or the granted extension exceeds three years. Enforcement cases: Check this point with one of our partner accountants. [ACD](https://impotsdirects.public.lu/fr/az/p/prelev.html).

## Cross-border points

Residency is not established by a bank address. Non-residents are taxable only on domestic income under art. 2(3), with special rules outside this computation. Residents' treaty-exempt income with a progression clause enters a fictitious base to set the global rate, but extraordinary foreign exempt income is excluded from that rate under art. 134(2). [LIR](https://impotsdirects.public.lu/dam-assets/fr/legislation/LIR/texte-coordonn-en-vigueur-au-1er-janvier-2026-ver-08052026.pdf).

For non-resident classes/assimilation and the 90% option, historical 34-day treaty thresholds, frontier workers, impatriates and multi-state social security/telework: use `lu-cross-border`; no outcome is authorised here. Check this point with one of our partner accountants.

## Two worked examples that recompute

Original 2026 inputs are unchanged. No advances or other income. These estimates show the retained rules and statutory basic-tax rounding, subject to confirmation of all stated eligibility facts and deductions; reconcile withholding/payments and the assessment before filing.

### Example 1: single self-employed consultant, class 1

Age 40, single, no children. Full-year qualifying activity/compulsory affiliation; profit EUR 60,000, paid compulsory deductible CCSS components EUR 13,000, separate dependency EUR 750, no other special expenses. Dependency is not deducted. Base = 60,000 − 13,000 − 480 = 46,520 → EUR 46,500. Raw tariff = 5,646.60 + 1,590 × 32% = 6,155.40; art. 124 basic tax = 6,155. Surcharge = 430.85; CII = 300 and CI-CO2 = 108. Result = **EUR 6,177.85** (computed).

```oa-check
name: LU class 1 original 2026 consultant with statutory rounding
inputs:
  profit: 60000
  contributions: 13000
  dependency: 750
  forfait: 480
steps:
  - taxable: floor((profit - contributions - forfait) / 50) * 50
  - raw_tax: 5646.60 + (taxable - 44910) * 0.32
  - tax: floor(raw_tax)
  - surcharge: round(tax * 0.07, 2)
  - cii: 600 - (profit - 40000) * 0.015
  - co2: 216 - (profit - 40000) * 0.0054
  - payable: tax + surcharge - cii - co2
expected:
  taxable: 46500
  raw_tax: 6155.40
  tax: 6155
  surcharge: 430.85
  cii: 300
  co2: 108
  payable: 6177.85
```

### Example 2: married sole earner, class 2, equipment

Original facts: jointly taxed spouses, sole self-employed engineer, profit before depreciation EUR 92,000, equipment EUR 12,000 net of deductible VAT put into service and available on 1 January 2026, useful life five years, booked on declining balance; monitor EUR 450 net of deductible VAT that day; paid deductible compulsory CCSS EUR 19,000. No spouse-helper activity or other abatement facts are supplied.

The statutory cap calculation is min(3 × 20%, 30%) = 30%; the proposed charge is EUR 3,600 and monitor write-off EUR 450. **Non-usable hold:** art. 32(4) regulation-compliant bookkeeping and the monitor's independent functionality have not been proven for these original facts. The following is conditional arithmetic only, not a deductible charge or filing result. Check this point with one of our partner accountants.

If those charges and the absence of another abatement are established: profit 87,950; base 87,950 − 19,000 − 480 = 68,470 → 68,450; half 34,225; raw half-tax 2,836.90; double 5,673.80 → whole-euro class tax 5,673; surcharge 397.11; profit exceeds the credit cut-off; conditional result **EUR 6,070.11**. Do not round each half separately. The former second-half acquisition variant (EUR 1,800) is held; its timing convention is not proven.

```oa-check
name: LU class 2 original 2026 inputs - conditional arithmetic only
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
  - profit: profit_before_dep - depreciation - monitor
  - taxable: floor((profit - contributions - forfait) / 50) * 50
  - half: taxable / 2
  - tax_half: 2663.10 + (half - 33435) * 0.22
  - raw_tax: tax_half * 2
  - tax: floor(raw_tax)
  - surcharge: round(tax * 0.07, 2)
  - payable: tax + surcharge
expected:
  depreciation: 3600
  profit: 87950
  taxable: 68450
  raw_tax: 5673.80
  tax: 5673
  surcharge: 397.11
  payable: 6070.11
```

**Historical cases retained with their original years and inputs:**

| Original case | Disposition |
|---|---|
| 15/03/2025 BCEE, STUDIO KREBS SARL, FACT 2025-003, +EUR 1,170; historical test 7 assumes 17% VAT | Arithmetic 1,170 / 1.17 = 1,000, difference 170. VAT eligibility/year/rate is not proven here; non-usable hold. Check this point with one of our partner accountants. |
| 01/04/2025 BIL, Adobe Creative Cloud AVR, −EUR 29.99 | No automatic deduction: business causation, invoice and VAT recovery must be established. Non-usable hold. Check this point with one of our partner accountants. |
| 22/04/2025 BGL, Restaurant Clairelune, déjeuner client, −EUR 85 | No invented entertainment percentage or automatic private-own-meal rule. Non-usable hold. Check this point with one of our partner accountants. |
| 10/01/2025 BCEE, CCSS indépendant T4 2024, −EUR 2,909.34; historical test 8 | Obtain the period-specific component statement, exempt-income position and timing; do not move the entire amount into deductions. Non-usable hold. Check this point with one of our partner accountants. |
| 03/06/2025 BGL, Apple Store Luxembourg, MacBook Pro, −EUR 1,899 | Cost/VAT, business/private use, useful life and method are missing; do not invent a depreciation rate. Non-usable hold. Check this point with one of our partner accountants. |
| 15/05/2025 BIL, internal savings transfer, −EUR 2,000 | Reconcile both accounts; identify as internal movement only once matched, without creating profit or a deduction. |
| Historical example 7/test 1: 2025 class 1 adjusted taxable income EUR 45,000 | Raw tariff 5,675.40 → basic 5,675; 7% surcharge 397.25; pre-credit total EUR 6,072.25 (computed). |
| Historical test 2: class 1 EUR 13,230 | Rounded base EUR 13,200; basic tax and surcharge zero (computed). |
| Historical test 3: class 1 EUR 60,000 | Raw tariff 11,164.50 → basic 11,164; surcharge 781.48; pre-credit total EUR 11,945.48 (computed). |
| Historical test 4: class 1 EUR 150,000 | Basic tax 46,590; surcharge 3,261.30; pre-credit total EUR 49,851.30 (computed). No whole-tax jump to 9% above the boundary. |
| Historical test 5: monthly employee gross EUR 4,000 (2025 and Jan–May 2026 variants) | Both original contribution estimates are non-usable holds, not interchangeable tax years. Check this point with one of our partner accountants. |
| Historical test 6: annual 2025 professional income EUR 60,000; later March 2026 monthly variant EUR 5,000 | Original income/year inputs retained. Dependency bases/abatements and amounts require year/month-specific proof; non-usable hold. Check this point with one of our partner accountants. |

## Ask the client first

Obtain residence and work locations for the whole year; age, children and family changes/elections; income in every category and country; invoices, asset register and mixed-use evidence; VAT status; CCSS components and dates; prior assessment, withholding, advance notices and payment dates. Read existing records first and ask only for missing facts. Preserve an unresolved-item list and do not finalise a case affected by a hold.

| Held current/historical topic | Destination and reason |
|---|---|
| Employee CIS, employee CI-CO2, CISSM (including part-time), pension credits, CIM/maintenance and child rebate; employment/pension/investment forfaits and employee travel | `luxembourg-payroll` plus individual assessment review; full eligibility, proration, interactions and limits not proven here. Check this point with one of our partner accountants. |
| Employee/employer/self-employed CCSS rates, totals, accident factor, MDE classes/thresholds, STM, cash-benefit cover, SSM unskilled/skilled, ceiling/minimum, uncapped dependency, Jan–Apr/May 2025 and Jan–May/June 2026 changes, voluntary cover | `luxembourg-social-contributions`; no single-rate/default-factor estimate authorised. Check this point with one of our partner accountants. |
| VAT franchise, tolerance, registration and national rates, sales/input/foreign VAT and return payments | `luxembourg-vat-return`; former turnover-only registration/default-VAT assumptions are not proven. Check this point with one of our partner accountants. |
| Deferred depreciation, extraordinary write-down, research-equipment application, sale/leaseback, building components (lifts/heating/sanitary/lighting/air-conditioning/IT cabling), acquisition half-year convention, commuting of the self-employed | Full conditions/implementing rules and timing require review; no half-year convention or component rate may be filed from this Guide. Check this point with one of our partner accountants. |
| Loss carryforwards (including pre-2017 losses), interest/insurance/pension-saving deductions, extraordinary/extra-professional/family abatements and spouse-helper/new-pension cases | Full conditions, remaining balances and income limits require case-specific review. Check this point with one of our partner accountants. |
| Companies/partnerships/holdings, property or substantial-share gains, participative premium, options/profit-sharing, arrears/enforcement | Specialist outcome outside this resident sole-operator computation; use `lu-corporate-tax` where relevant. Check this point with one of our partner accountants. |

## Sources

| Source and passage actually read | URL | Read on |
|---|---|---|
| ACD 2026 coordinated LIR (updated 8 May): arts. 1–2, 10, 12, 31–34, 45, 48, 107, 110, 113–114, 118–124, 126, 129b, 134–135, 152ter–153. Read operative conditions, including those moved to explicit holds; this coordinated text is the authority's reference compilation | https://impotsdirects.public.lu/dam-assets/fr/legislation/LIR/texte-coordonn-en-vigueur-au-1er-janvier-2026-ver-08052026.pdf | 2026-11-27 |
| 2026 statutory collection, p. 419, law of 30 June 1976 art. 6(1), Read for the surcharge slice and thresholds | https://igss.gouvernement.lu/dam-assets/publications/code-de-la-s%C3%A9curit%C3%A9-sociale/css2026.pdf | 2026-11-27 |
| Enacted law of 21 December 2012 art. 5: Read for the surcharge amendment and commencement | https://impotsdirects.public.lu/content/dam/acd/fr/legislation/legi12/M__morial_A_-_N___270_du_28_d__cembre_2012.pdf | 2026-11-27 |
| ACD employment-fund summary, Read for the rate wording; statutory slice condition prevails | https://impotsdirects.public.lu/fr/az/f/fond_empl.html | 2026-11-27 |
| ACD Form 100 page, Read for the filing channels and currently available form years | https://impotsdirects.public.lu/fr/formulaires/pers_physiques.html | 2026-11-27 |
| ACD filing deadlines, Read for the annual rule and correspondence deadlines | https://impotsdirects.public.lu/fr/az/d/delais/depot.html | 2026-11-27 |
| ACD annual adjustment page, Read for the 2025 forms/deadline and assessment restriction | https://impotsdirects.public.lu/fr/formulaires/decompte_annuel.html | 2026-11-27 |
| ACD late-filing, astreinte and payment-interest sections, Read for the full conditions | https://impotsdirects.public.lu/fr/az/p/prelev.html | 2026-11-27 |
| ACD circular 34/1, pp. 1–4: Read for the functional unit, acquisition cost and commencement; current LIR controls euro threshold | https://impotsdirects.public.lu/dam-assets/fr/legislation/circulaires/circulaire-lir-n-34-1-du-19-juin-1998.pdf | 2026-11-27 |
| ACD circular 32/1, pp. 1–3: Read for deferred-method applicability; its full application remains held | https://impotsdirects.public.lu/dam-assets/fr/legislation/legi18/circulairelir32-1du15052018-amortissement-differe.pdf | 2026-11-27 |
| ACD circular 32/2, pp. 1–2: Read for building-component conditions; specialist outcome held | https://impotsdirects.public.lu/dam-assets/fr/legislation/legi22/lir-32-2-du-3052022.pdf | 2026-11-27 |
| Guichet operating-result page, Read for the depreciation passage on the old half-year convention; 2018 text is not sufficient proof of current practice | https://guichet.public.lu/fr/entreprises/fiscalite/impots-benefices/benefices-patrimoine/entreprise-individuelle-societe-personne/calcul-resultat-exploitation.html | 2026-11-27 |

Not yet confirmed: all holds above are non-usable for a filing, payment or tax position until resolved. This includes 2026 annual-adjustment form/instructions and the original equipment example's bookkeeping conditions. Check this point with one of our partner accountants.

> Contributed by OpenAccountants.
