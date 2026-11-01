---
name: morocco-professional-income-tax
description: >
  Use this skill whenever asked about Morocco personal income tax (Impot sur le Revenu, IR) on
  professional or business income under the real net result (RNR) or simplified net result (RNS)
  systems, for tax year 2026. Covers the Art. 73 scale, the Art. 74 family reduction, business
  income, deductible and non-deductible charges, the cotisation minimale, the annual revenu global
  return, deadlines and penalties. Trigger on phrases like "impot sur le revenu Maroc", "Morocco
  income tax", "IR professionnel", "resultat net reel", "resultat net simplifie", "RNR", "RNS",
  "bareme IR Maroc", "cotisation minimale", "declaration revenu global", "الضريبة على الدخل المغرب",
  "صافي الربح". Replies in the user's language (English, French, Moroccan Arabic or Darija).
version: 2.0
jurisdiction: MA
tax_year: 2026
tier: 2
last_updated: 2026-11-01
category: international
review_status: pending_review
trust_label: Built by Michael Cutajar and the OpenAccountants team
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
depends_on:
  - income-tax-workflow-base
---

# Morocco: personal income tax on professional income (IR), 2026

Built by Michael Cutajar and the OpenAccountants team. All articles are from the Code General des Impots 2026 (CGI), published by the Direction Generale des Impots (DGI).

> **General reference only.** This does not constitute tax, legal or financial advice. Verify figures against the cited sources or with a licensed professional before relying on them.

## Who this applies to

Individuals with professional income under CGI Art. 30: commercial, industrial and artisanal professions; property developers, land subdividers and property dealers; liberal professions and any other profession; and repetitive income not in another category. The taxpayer is on RNR by default, or RNS by option where turnover allows (Art. 39).

Out of scope, route elsewhere:

- **R-MA-1 Company tax.** Companies under IS are not taxed here.
- **R-MA-2 Auto-entrepreneur and CPU.** See `ma-auto-entrepreneur` and `ma-cpu`.
- **R-MA-3 VAT.** See `morocco-vat`.
- **R-MA-4 Salary-only taxpayers.** Limit to the professional component; see `morocco-payroll`.
- **R-MA-5** Agricultural regimes, real-estate profits and financial-product withholdings: reviewer only.
- **R-MA-6** Non-residents and treaty relief: refer to a Moroccan expert-comptable.
- **R-MA-7** Never submit a return as filed; produce a draft for expert-comptable sign-off.

## Rates, bands and thresholds

| Item | Amount | Conditions | Tax year | Source |
|---|---|---|---|---|
| Band to MAD 40,000 | 0% | Annual revenu global | 2026 | CGI Art. 73-I https://www.tax.gov.ma/wps/wcm/connect/08712531-1e81-4e28-a38b-2bd9edf8e09e/CGI+2026+FR.pdf?MOD=AJPERES&CACHEID=ROOTWORKSPACE-08712531-1e81-4e28-a38b-2bd9edf8e09e-pM5DEs1 |
| MAD 40,001 to 60,000 | 10% | Quick deduction MAD 4,000 (computed from the bands) | 2026 | same |
| MAD 60,001 to 80,000 | 20% | Quick deduction MAD 10,000 | 2026 | same |
| MAD 80,001 to 100,000 | 30% | Quick deduction MAD 18,000 | 2026 | same |
| MAD 100,001 to 180,000 | 34% | Quick deduction MAD 22,000 | 2026 | same |
| Above MAD 180,000 | 37% | Quick deduction MAD 27,400 | 2026 | same |
| Family reduction | MAD 600 per dependant, total cap MAD 3,600 | Off the tax. Dependants: wife; own and legally taken-in children, each with annual revenu global not above the exempt band and aged 27 or under (no age limit for a child whose disability prevents self-support). A woman taxpayer claims for her husband and children when they are legally her dependants. A family change counts from the month after it happens | 2026 | CGI Art. 74 https://www.tax.gov.ma/wps/wcm/connect/08712531-1e81-4e28-a38b-2bd9edf8e09e/CGI+2026+FR.pdf?MOD=AJPERES&CACHEID=ROOTWORKSPACE-08712531-1e81-4e28-a38b-2bd9edf8e09e-pM5DEs1 |
| Cotisation minimale, standard | 0.25% | Base in Art. 144-I-B | 2026 | CGI Art. 144-I-D https://www.tax.gov.ma/wps/wcm/connect/08712531-1e81-4e28-a38b-2bd9edf8e09e/CGI+2026+FR.pdf?MOD=AJPERES&CACHEID=ROOTWORKSPACE-08712531-1e81-4e28-a38b-2bd9edf8e09e-pM5DEs1 |
| Cotisation minimale, reduced | 0.15% | Commercial sales of petroleum products, gas, butter, oil, sugar, flour, water, electricity, medicines | 2026 | same |
| Cotisation minimale, professions | 4% | Under IR. Art. 89-I-12: lawyer, interpreter, notary, adel, bailiff, architect, quantity surveyor, land surveyor, topographer, engineer, consultant, expert in any field, approved accountant, veterinarian. Art. 91-VI-1: doctor, dentist, physiotherapist, orthoptist, speech therapist, nurse, herbalist, midwife, clinic or care-home operator, medical laboratory operator | 2026 | same |
| Cotisation minimale floor | MAD 1,500 | IR on RNR or RNS, even with no turnover | 2026 | same |
| RNS ceiling, trade, industry, craft, fishing shipowner | MAD 2,000,000 turnover excl. VAT | Annual or annualised turnover. Option ends after two consecutive years over | 2026 | CGI Art. 39 https://www.tax.gov.ma/wps/wcm/connect/08712531-1e81-4e28-a38b-2bd9edf8e09e/CGI+2026+FR.pdf?MOD=AJPERES&CACHEID=ROOTWORKSPACE-08712531-1e81-4e28-a38b-2bd9edf8e09e-pM5DEs1 |
| RNS ceiling, services and professions | MAD 500,000 turnover excl. VAT | Same | 2026 | same |
| RNS abatement | 15% of base | Member of an approved accounting management centre | 2026 | CGI Art. 38-III https://www.tax.gov.ma/wps/wcm/connect/08712531-1e81-4e28-a38b-2bd9edf8e09e/CGI+2026+FR.pdf?MOD=AJPERES&CACHEID=ROOTWORKSPACE-08712531-1e81-4e28-a38b-2bd9edf8e09e-pM5DEs1 |
| Cash payment limit | MAD 5,000 per day and MAD 50,000 per month, per supplier | Applies to Art. 10 (I-A, B and E) charges. Above this the charge is not deductible unless paid by crossed non-endorsable cheque, bill of exchange, magnetic means, bank transfer, electronic process, or set-off on dated and signed documents | 2026 | CGI Art. 11-II https://www.tax.gov.ma/wps/wcm/connect/08712531-1e81-4e28-a38b-2bd9edf8e09e/CGI+2026+FR.pdf?MOD=AJPERES&CACHEID=ROOTWORKSPACE-08712531-1e81-4e28-a38b-2bd9edf8e09e-pM5DEs1 |
| Promotional gifts | Deductible up to MAD 100 per item | Item must carry the business name, initials or brand | 2026 | CGI Art. 10-I-B-1 https://www.tax.gov.ma/wps/wcm/connect/08712531-1e81-4e28-a38b-2bd9edf8e09e/CGI+2026+FR.pdf?MOD=AJPERES&CACHEID=ROOTWORKSPACE-08712531-1e81-4e28-a38b-2bd9edf8e09e-pM5DEs1 |
| Withholding on fees and rents received | 10% on fees, 5% on rents, excl. VAT | Paid to an RNR or RNS individual by a legal person or by an RNR or RNS individual. Credits against IR, with refund. An RNR or RNS client paying fees or rent to an individual must withhold too | 2026 | CGI Art. 4-IV, 4-V, 73-II-A, 73-II-B-8, 157 https://www.tax.gov.ma/wps/wcm/connect/08712531-1e81-4e28-a38b-2bd9edf8e09e/CGI+2026+FR.pdf?MOD=AJPERES&CACHEID=ROOTWORKSPACE-08712531-1e81-4e28-a38b-2bd9edf8e09e-pM5DEs1 |

Quick method: IR before reductions = income x band rate - quick deduction. Then subtract the family reduction and credits.

## The base

The scale applies to revenu global: all IR categories combined. Professional income is one part.

- **RNR:** income over charges of the year, as for Art. 8-I; the year closes on 31 December (Art. 33). Charges follow Art. 34 to 36 and Art. 10 and 11. The owner's drawings are not a staff cost; the owner's own AMO (law 98-15) and pension (law 99-15) contributions are deductible (Art. 35).
- **RNS:** income over charges for the activity, excluding provisions and carried-forward losses, and subject to Art. 11 and 35; closes on 31 December (Art. 38).
- **Losses, RNR only:** deduct from the following years up to the fourth year after the loss (Art. 37, 12). No time limit applies to the part of a loss that comes from depreciation properly booked and deducted under Art. 10-I-F-1-b (Art. 12).
- **Nil or loss year:** attach to the return a signed explanatory statement (état explicatif) of the origin of the loss or nil result (Art. 82-IV). If it is missing, the DGI gives 15 days by letter, then fines MAD 2,000 (Art. 198 bis).
- **Non-deductible:** fines, penalties and surcharges (Art. 11-I), except late-payment indemnities under law 32-10; IR itself (Art. 35); purchases, works and services without a regular invoice or other proof in the taxpayer's name carrying the Art. 145 details (Art. 11-III; a reassessment becomes final only if the invoice is not completed during the Art. 220 or 221 procedure); purchases and services of a gratuitous nature (Art. 11-IV); the social solidarity contribution (Art. 11-IV); and cash-paid charges above the limit. Depreciation of assets bought that way is also not deductible (Art. 11-II). Exception: live animals and unprocessed farm products, except between traders.
- **Cotisation minimale base (Art. 144-I-B):** turnover and other operating income, financial income, and state, local and third-party subsidies and gifts, all excluding VAT.
- **Year covered:** the cotisation relates to the previous year's professional income (Art. 144-I-A).
- **Exemption:** first three financial years after activity starts. No new period when the same activity resumes after a sale or stoppage (Art. 144-I-C-2). A temporary-stoppage declaration under Art. 150 bis lifts the floor only (C-3).
- **Interaction with tax (Art. 144-I-E):** the cotisation is credited against IR. Where the IR share for professional income is below the cotisation, the difference stays with the Treasury. It is tested on the professional share, so "the higher of" holds only when professional income is the sole income.

### Transaction patterns


Classify bank-statement lines and ledger entries. Keywords appear in **French**,
**Moroccan Arabic / Darija (transliterated + script)**, and **English**.

### Income (revenu professionnel: taxable)

| Pattern (FR / AR / EN) | Treatment |
|---|---|
| `VIREMENT RECU`, `VRMT`, `ENCAISSEMENT`, `REGLEMENT CLIENT`, `FACTURE` | Business receipt → turnover |
| `CHEQUE REMIS`, `REMISE CHEQUE`, `versement espèces` | Receipt → turnover (confirm source) |
| `تحويل وارد` (tahwil warid), `أداء زبون` (client payment), `فاتورة` (fatura) | Client payment → turnover |
| `produits financiers`, `intérêts créditeurs`, `فوائد` | Financial income → in CM base |
| `subvention`, `don reçu`, `إعانة` | Subsidy/grant → in CM base (Art. 144-I-B) |

### Deductible expenses (charges déductibles)

| Pattern (FR / AR / EN) | Treatment |
|---|---|
| `LOYER`, `bail`, `كراء` (kira) | Rent of business premises → deductible |
| `SALAIRES`, `paie`, `أجور` | Staff wages → deductible (with CNSS) |
| `CNSS`, `AMO`, `cotisations sociales` | Social charges → deductible |
| `prélèvement exploitant`, owner's pay | Owner's drawings → **not** deductible (Art. 35) |
| `ACHAT`, `fournisseur`, `marchandises`, `مشتريات` | Purchases / stock → deductible (COGS) |
| `ELECTRICITE`, `EAU`, `LYDEC`, `REDAL`, `ONEE`, `كهرباء` | Utilities (business share) → deductible |
| `TELEPHONE`, `INTERNET`, `IAM`, `INWI`, `ORANGE` | Telecom (business share) → deductible |
| `ASSURANCE`, `تأمين` | Business insurance → deductible |
| `HONORAIRES`, `comptable`, `avocat`, `أتعاب` | Professional fees → deductible |
| `CARBURANT`, `GASOIL`, `AFRIQUIA`, `SHELL`, `وقود` | Fuel (business use) → deductible (substantiate) |
| `AMORTISSEMENT`, `dotation` | Depreciation of fixed assets → deductible under Art. 10-I-F |
| `INTERETS EMPRUNT`, `crédit`, `قرض` | Loan interest (business) → deductible |

### Non-deductible (charges non déductibles: reintegrate)

| Pattern (FR / AR / EN) | Treatment |
|---|---|
| `AMENDE`, `PENALITE`, `majoration`, `غرامة` | Fines & penalties → **non-deductible** |
| `IR`, `acompte IR`, `cotisation minimale` | The IR itself / CM → **non-deductible** |
| `cadeaux` over MAD 100 per item, `dons` not listed in Art. 10-I-B-2 | Excess gifts / non-qualifying donations → non-deductible |
| Cash expense > regulatory threshold (paiement espèces) | Portion over the cash-payment limit → **non-deductible** (Art. 11-II, above) |
| `frais sans justificatif`, no invoice | Unsupported expense → non-deductible (Art. 11-III) |

### Likely personal (exclusions: not business)

| Pattern (FR / AR / EN) | Treatment |
|---|---|
| `RETRAIT GAB`, `retrait DAB`, `سحب` (cash withdrawal) | Personal unless proven business |
| `MARJANE`, `CARREFOUR`, `ACIMA`, groceries, `سوق` | Personal household → exclude |
| `transfert famille`, `virement personnel`, `تحويل عائلي` | Personal transfer → exclude |
| `restaurant`, `café`, clothing, `ملابس` | Personal unless a substantiated business meal/representation |
| `scolarité`, `école`, school fees | Personal → exclude |

> Apply a **likely-personal default**: mixed-use and undocumented private-looking
> spend is **excluded from business expenses** until the user substantiates a
> business purpose.

### Bank statements


Morocco's main retail banks; statement layouts and label conventions:

### Attijariwafa Bank

- Labels often abbreviated: `VIR`, `VRST`, `RET GAB`, `PRLV`, `COM` (commissions).
- Client receipts: `VIREMENT RECU` / `VRT EN VOTRE FAVEUR`. Card acquiring (TPE):
  `REMISE TPE` / `VERSEMENT MONETIQUE` → turnover.
- Bank charges `COMMISSION` / `FRAIS TENUE DE COMPTE` → deductible business cost if
  the account is professional.

### BMCE / Bank of Africa

- `VIREMENT EN VOTRE FAVEUR`, `MISE A DISPOSITION`, `VRST ESPECES` → receipts.
- `PRELEVEMENT` (PRLV) for recurring suppliers/utilities → expense (classify by
  counterparty: ONEE/Lydec = utilities; IAM/Inwi/Orange = telecom).
- Loan lines `ECHEANCE CREDIT` → split principal (non-deductible) vs interest
  (deductible).

### Banque Populaire (BCP / BP régionales)

- `VERSEMENT`, `REMISE CHEQUE`, `VIREMENT RECU` → receipts.
- `CHABI` / mobile-wallet credits → confirm whether business receipts.
- `AGIOS`, `COMMISSIONS`, `INTERETS DEBITEURS` → finance cost (deductible if
  business); `INTERETS CREDITEURS` → financial income (in CM base).

> Across all banks: a **mixed personal/professional account** is the biggest risk.
> Default private-looking lines (`RET GAB`, supermarkets, family transfers, school
> fees) to **excluded** and ask the user to confirm any business reclassification.

### Workbook


Suggested workbook (one sheet, formulas shown for the reviewer):

| Cell / Row | Label | Formula / Input |
|---|---|---|
| B1 | Turnover HT (CA) | input |
| B2 | Other operating + financial income + subsidies | input |
| B3 | **CM base** | `=B1+B2` |
| B4 | Deductible expenses (total) | input (from pattern library) |
| B5 | Reintegrations (non-deductible add-backs) | input |
| B6 | **Net professional result** | `=B1+B2-B4+B5` |
| B7 | Other revenu global (salary, rental, …) | input |
| B8 | **Net taxable income (revenu global)** | `=MAX(B6,0)+B7` |
| B9 | Bracket rate | lookup on B8 vs the rates table |
| B10 | Somme à déduire | lookup on B8 vs the rates table |
| B11 | **IR brut (scale)** | `=B8*B9-B10` |
| B12 | Dependents | input |
| B13 | Family deduction | `=MIN(B12*600,3600)` |
| B14 | **IR net (scale)** | `=MAX(B11-B13,0)` |
| B15 | CM rate | 0.25% / 0.15% / 4% (select) |
| B16 | CM raw | `=B3*B15` |
| B17 | **Cotisation minimale** | `=IF(new_business_exempt,0,MAX(B16,1500))` |
| B18 | **IR due (before credits)** | `=MAX(B14,B17)` (single-income case; with other income apply Art. 144-I-E, see The base) |
| B19 | Acomptes / CM paid / withholdings | input |
| B20 | **Net IR payable on filing** | `=MAX(B18-B19,0)` |

> The lookup in B9/B10 must use the rates table above. Keep the somme-à-déduire
> column in step with CGI Art. 73.

## Deadlines and filing

| Step | Deadline | Source |
|---|---|---|
| Choose RNS on starting | Written request by registered letter or by hand against receipt to the tax inspector before 1 May of the year after the start; valid for the start year | Art. 44-I |
| Choose RNS while active | Within the revenu global filing period for the prior year | Art. 44-I |
| Pay the cotisation minimale | Before 1 February each year, for the previous year | Art. 173-I |
| Return with professional income on RNR or RNS | Before 1 May of the following year | Art. 82-I |
| Return with no professional income | Before 1 March | Art. 82-I |
| Pay the IR | Same deadline as the return | Art. 173-I |
| Lawyers: provisional acomptes | MAD 100 per case. By option per file: at the court registry on filing, or electronically before the end of the month after the year. None for the first 60 months from the tax ID number | Art. 173-III |

Steps: 1. Close the year on 31 December. 2. Reconcile accounting result to tax result. 3. Build revenu global. 4. Apply scale and family reduction. 5. Compare the cotisation under Art. 144-I-E. 6. Deduct withholdings and the cotisation paid. 7. File through the DGI online service and pay by the deadline. Art. 173 sets no acomptes for RNR or RNS income other than the lawyers' acomptes. Those credit first against the cotisation, then against the IR on professional income; any balance stays with the Treasury (Art. 173-III), and the return must show them (Art. 82-I). Filing must be electronic for businesses and for the liberal professions listed by regulation (Art. 155-I). The return also carries an état des ventes by client ICE (Art. 82-I).

## Penalties and interest

- **Late or missing return (Art. 184):** 5% if within 30 days, or on a late corrective return producing more tax; 15% after 30 days; 20% on assessment for no, incomplete or insufficient return. Where the cotisation exceeds the tax, or the result is nil or a loss, the surcharge is on the cotisation. Minimum surcharge MAD 500. An incomplete return with no effect on the base or collection costs a MAD 500 fine instead.
- **Late payment (Art. 208-I):** 10% penalty, cut to 5% if paid within 30 days, plus 5% for the first month and 0.50% for each further month or part. The increases stop running past 12 months of a pending appeal before the local, regional or national commission.

## Cross-border points

Art. 30-3 taxes gross income under Art. 15 of non-residents for work or services for persons in Morocco not tied to a Moroccan establishment. Residence and treaty relief are not covered here (R-MA-6). See `Not yet confirmed` below.

## Two worked examples that recompute

**1. Trader on RNR, profit MAD 150,000, turnover MAD 900,000, two dependants, past the exemption.** Scale 150,000 x 34% - 22,000 = 29,000. Family 1,200. IR 27,800. Cotisation 2,250 is below the IR, so it is absorbed and credited. Net to pay on filing: 25,550.

```oa-check
name: Trader RNR 2026
inputs:
  profit: 150000
  turnover: 900000
  dependants: 2
steps:
  - scale: profit * 0.34 - 22000
  - family: min(dependants * 600, 3600)
  - ir: scale - family
  - cm: max(turnover * 0.0025, 1500)
  - balance: ir - cm
expected:
  ir: 27800.00
  cm: 2250.00
  balance: 25550.00
```

**2. Decision: is the 4% cotisation the real cost? Architect, profit MAD 90,000, fees MAD 600,000, no other income, no dependants.** Scale 90,000 x 30% - 18,000 = 9,000. Cotisation 600,000 x 4% = 24,000. The IR is below the cotisation, so the difference of 15,000 stays with the Treasury and the cost is 24,000. Had she been in her first three years, the cost would be 9,000.

```oa-check
name: Architect 4 percent cotisation
inputs:
  profit: 90000
  fees: 600000
steps:
  - scale: profit * 0.30 - 18000
  - cm: max(fees * 0.04, 1500)
  - cost_after_exemption: max(scale, cm)
  - lost_to_treasury: cm - scale
  - cost_in_exemption: scale
expected:
  cost_after_exemption: 24000.00
  lost_to_treasury: 15000.00
  cost_in_exemption: 9000.00
```

Other cases carried over:

- **RNS services, profit 35,000, turnover 120,000:** scale 0. Cotisation 300 rises to the floor of 1,500, or 0 in the exemption period.
- **RNR loss, turnover 1,200,000:** scale 0; cotisation 3,000, or 0 in the exemption period. The loss carries forward under RNR, never under RNS.
- **Profit 70,000 plus net salary 50,000:** revenu global 120,000; scale 120,000 x 34% - 22,000 = 18,800. Credit salary withholding. Apply Art. 144-I-E to the professional share only.

## Ask the client first

1. Individual or company? Company: R-MA-1.
2. RNR or RNS? Was an RNS option filed and is it still valid? If unknown, treat as RNR and flag.
3. Activity type: is it a profession under Art. 89-I-12 or 91-VI-1 (4% rate), or a reduced-rate sale?
4. Turnover excl. VAT, other operating and financial income, subsidies; net accounting result; bank or ledger export.
5. Other income: salary, rental, capital.
6. Dependants and their income.
7. Activity start date.
8. Cotisation paid, withholdings, and lawyers' acomptes.

Defaults when facts are missing: uncertain expense stays non-deductible until supported; private-looking spend is excluded; turnover near a ceiling is treated as breached, with a warning of the move to RNR (Art. 39). Compute both tax and cotisation every time.

Escalate to the expert-comptable: RNR or RNS eligibility and a forced switch; depreciation policy, mixed business and private assets, related-party charges; revenu global assembly and withholding credits; 4% or 0.15% cotisation edge cases and the exemption window. Present the computation, assumptions and open items, never a file-ready result.

## Sources

| Source | URL | Read on |
|---|---|---|
| DGI, Code General des Impots 2026 (French); Art. 4, 10, 11, 12, 30, 33 to 39, 44, 73, 74, 82, 89, 91, 144, 155, 157, 173, 184, 198 bis, 208 extracts read from the PDF | https://www.tax.gov.ma/wps/wcm/connect/08712531-1e81-4e28-a38b-2bd9edf8e09e/CGI+2026+FR.pdf?MOD=AJPERES&CACHEID=ROOTWORKSPACE-08712531-1e81-4e28-a38b-2bd9edf8e09e-pM5DEs1 | 2026-11-01 |

Not yet confirmed: the SIMPL-IR portal address and screens, and the current form number (DGI portal guide not read); depreciation rates; residence and treaty rules.
