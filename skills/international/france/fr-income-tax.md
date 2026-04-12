---
name: fr-income-tax
description: >
  Use this skill whenever asked about French income tax for self-employed individuals (professions libérales, BNC). Trigger on phrases like "déclaration de revenus", "2042", "2042-C-PRO", "BNC", "bénéfices non commerciaux", "quotient familial", "prélèvement à la source", "impôt sur le revenu France", "micro-BNC", "régime réel", "charges déductibles", "CSG déductible", "décote", "CEHR", or any question about filing or computing income tax for a French freelancer or profession libérale. Covers progressive brackets (0–45%), quotient familial, BNC micro vs réel, prélèvement à la source, charges déductibles, réductions/crédits d'impôt, CEHR surtax, décote, and penalties.
version: 2.0
---

# France Income Tax — Self-Employed Profession Libérale (BNC / Impôt sur le Revenu)

## Section 1 — Quick Reference

### Income Tax Brackets (2025 barème, applied to income per part)
| Income per part (EUR) | Rate |
|---|---|
| 0 – 11,294 | 0% |
| 11,295 – 28,797 | 11% |
| 28,798 – 82,341 | 30% |
| 82,342 – 177,106 | 41% |
| Over 177,106 | 45% |

**Quotient familial system:**
- Single (célibataire/veuf sans charge): 1 part
- Married/PACS (couple): 2 parts
- Each dependent child: +0.5 part (first 2); +1 part from 3rd child
- Single parent with child: 1 + 0.5 = 1.5 parts
- Disability: +0.5 part

**Formula:** Total household income ÷ number of parts = income per part → apply brackets → × parts = base tax → apply décote, réductions, crédits → tax due

### CEHR — Contribution Exceptionnelle sur les Hauts Revenus
| Household income (EUR) | Rate (single) | Rate (couple) |
|---|---|---|
| Up to 250,000 / 500,000 | 0% | 0% |
| 250,001 – 500,000 (single) / 500,001 – 1,000,000 (couple) | 3% | 3% |
| Above 500,000 (single) / above 1,000,000 (couple) | 4% | 4% |

### BNC Regimes: Micro vs Réel
| Feature | Micro-BNC | Régime réel (déclaration contrôlée) |
|---|---|---|
| Revenue threshold (2025) | ≤ €77,700 | Any revenue (mandatory above €77,700) |
| Tax base | Revenue × 66% (34% abattement forfaitaire) | Actual revenue − actual charges |
| Accounting required | Simple revenue register | Full double-entry bookkeeping |
| Declaration | 2042-C-PRO (case 5HQ) | 2035 + 2042-C-PRO |
| Social charges | URSSAF on gross revenue (micro-social or régime réel) | URSSAF on BNC |
| CSG deductible | No (micro) | Yes (6.8% of social contributions deductible) |
| Best choice | Low expenses (<34% of revenue) | High expenses (>34% of revenue) |

### Key Charges Déductibles (Régime Réel — Form 2035)
| Charge | Deductible? |
|---|---|
| Professional rent (cabinet office) | 100% |
| Home office (bureau à domicile) | Proportional — floor area |
| Phone — professional line | 100% |
| Phone — mixed use | Professional % only |
| Internet | Professional % |
| Software / SaaS (professional) | 100% |
| Professional insurance (RCP) | 100% |
| Accountant / CGA fees | 100% |
| Training (DPC — continuous professional development) | 100% |
| Professional books, subscriptions | 100% |
| Professional travel | 100% — business purpose required |
| Vehicle (BNC use) | Barème kilométrique OR actual costs × business % |
| Business meals (repas d'affaires) | With client: actual; working alone: forfait repas up to €19.40/day (2025) |
| Equipment (<€500 HT) | Expense immediately |
| Equipment (>€500 HT) | Amortise (durée d'usage) |
| Social charges URSSAF | Deductible on 2035 |
| CSG (6.8% of social charges) | Deductible on 2042 (not 2035) |
| Income tax | NOT deductible |
| Personal life insurance | NOT deductible (may qualify as credit) |

### Conservative Defaults
| Item | Default |
|---|---|
| Home office % | Do not assume — ask for floor area ratio |
| Vehicle business % | Do not assume — ask for km records |
| Phone/internet | 50% if mixed; 100% if dedicated professional line |
| Régime | Use micro-BNC if revenue ≤ €77,700 and no expense documentation |
| CSG deductible | 6.8% of URSSAF social charges paid previous year |

### Red Flag Thresholds
| Situation | Flag |
|---|---|
| Revenue > €77,700 | Micro-BNC no longer available — must use régime réel |
| Revenue > €250,000 (single) | CEHR applies |
| Charges > 70% of revenue | High — verify documentation |
| Home office > 30% | Aggressive — document |
| No RCP insurance | Flag — profession libérale normally required |

---

## Section 2 — Required Inputs & Refusal Catalogue

### Minimum Required Inputs
1. Total gross receipts (recettes professionnelles) for the year
2. Chosen regime (micro-BNC or régime réel)
3. If réel: itemised professional charges with receipts
4. Household composition (marital status, number of children/dependants)
5. URSSAF social charges paid in the year (for régime réel)
6. Previous year tax (for prélèvement à la source comparison)
7. Other household income (spouse earnings, rental, etc.)

### Refusal Catalogue
**R-FR-1 — No expense documentation (régime réel)**
Refuse undocumented charges. State: "Without receipts and records, we cannot claim actual charges under the régime réel. Consider micro-BNC (34% abattement) if this is your first year or if documentation is incomplete."

**R-FR-2 — Micro-BNC threshold exceeded**
If revenue > €77,700: cannot use micro-BNC. State: "Your revenue exceeds the micro-BNC threshold of €77,700. You must use the régime de la déclaration contrôlée (Form 2035) and maintain proper accounts."

**R-FR-3 — Personal expenses as professional charges**
Refuse personal costs (personal vacations, personal food, personal clothing) as professional charges. State: "These are personal expenses and cannot be deducted as charges professionnelles under French tax law."

**R-FR-4 — TVA amounts included in recettes**
If client is TVA-registered: gross receipts must exclude TVA collected. State: "TVA collected from clients is not your income. Recettes on Form 2035 are always HT (hors taxes)."

**R-FR-5 — Non-resident claiming personal reliefs**
Non-residents (non-domicilié fiscal) have different rules — no quotient familial, flat rates apply. State: "As a non-resident, different rules apply. I cannot apply the standard quotient familial calculation."

---

## Section 3 — Transaction Pattern Library

### 3.1 Income Patterns
| Bank Description Pattern | Income Type | Tax Treatment | Notes |
|---|---|---|---|
| Virement client + name | Professional receipts (recettes) | Include gross (HT if TVA registered) | |
| Virement SEPA from EU client | Professional receipts | Include (HT) | |
| Virement international / SWIFT | Foreign client receipts | Include — convert to EUR at date of receipt | |
| Stripe / Stripe paiement | Platform receipts | Include net + add Stripe fees as charges | |
| PayPal virement | Platform receipts | EUR equivalent | |
| Malt / Comet / Crème de la Crème | Freelance platform payout | Gross earnings (platform fee = charge) | |
| Intérêts créditeurs | Bank interest | Revenus de capitaux mobiliers — not BNC | Separate category |
| Loyer reçu | Rental income | Revenus fonciers — separate schedule | Not BNC |
| Remboursement frais | Expense reimbursement | EXCLUDE if pass-through (refacturation) — check | Gross up if debours |

### 3.2 Expense Patterns (Charges — Form 2035 Régime Réel)
| Bank Description Pattern | Charge Category | Deductible? | Notes |
|---|---|---|---|
| Orange Pro / SFR Pro / Bouygues | Téléphone professionnel | 100% if pro line | Partial if mixed |
| Free / Orange / SFR internet | Internet | Professional % | T2 |
| EDF / Engie / électricité | Electricity | Home office % | T2 |
| Loyer bureau / local professionnel | Loyer professionnel | 100% | Must be professional premises |
| Adobe / Figma / Notion | Logiciels/SaaS | 100% | |
| SNCF / Eurostar / train | Déplacements | 100% — professional purpose | Document destination + purpose |
| Air France / easyJet | Voyages professionnels | 100% — professional purpose | Document |
| Hôtel / Airbnb (déplacement pro) | Hébergement | 100% — professional purpose | |
| Restaurant (repas affaires — with client) | Repas d'affaires | Yes — with client name on receipt | Forfait solo max €19.40/day |
| URSSAF cotisations | Charges sociales | 100% deductible on 2035 | |
| Mutuelle santé Madelin | Assurance Madelin | 100% (within Madelin ceiling) | |
| Retraite Madelin / PER pro | Épargne retraite Madelin | 100% (within ceiling) | |
| RCP / assurance professionnelle | Assurance RCP | 100% | |
| Expert-comptable / CGA | Honoraires comptable | 100% | CGA membership = additional réduction |
| Formation professionnelle | Formation | 100% — professional DPC | |
| Livres / abonnements pro | Documentation | 100% — professional | |
| Matériel bureau (<€500 HT) | Petit matériel | 100% immediate | |
| MacBook / PC / tablette | Matériel amortissable | Amortissement (3 years typical) | T1: applies if ≥€500 |
| Impôt sur le revenu | Impôts | EXCLUDE — not deductible | |
| TVA payée | TVA | EXCLUDE — not income tax deductible | |
| Cotisation foncière des entreprises (CFE) | Taxes | Yes — deductible on 2035 | |
| Virement épargne / livret | Épargne | EXCLUDE — personal savings | |

### 3.3 CSG Déductible (Special Treatment)
- 6.8% of social charges paid to URSSAF (previous year) is deductible from overall income on Form 2042 (not Form 2035)
- Not a professional charge — a personal deduction applied after BNC is computed
- Must use actual URSSAF annual statement to determine amount
- **Pattern:** URSSAF payment on bank → record on 2035 as charge professionnelle. Then compute 6.8% of that for 2042 CSG deduction.

### 3.4 Foreign Currency & Platform Receipts
| Source | Currency | Treatment |
|---|---|---|
| USD client payment | USD | Convert to EUR at ECB/Banque de France rate on receipt date |
| GBP client | GBP | Convert at receipt date rate |
| Stripe USD | USD | Use Stripe statement EUR equivalent |
| PayPal multi-currency | Various | Use PayPal statement EUR equivalent |
| Malt.com payout | EUR | Net of Malt commission; add commission back as charge |
| Google AdSense | USD/EUR | Monthly — convert if USD |

### 3.5 Internal Transfers
| Pattern | Treatment |
|---|---|
| Virement vers compte épargne | EXCLUDE — personal savings movement |
| Remboursement carte bancaire | EXCLUDE — expense captured per transaction |
| Virement entre comptes propres | EXCLUDE |
| Prélèvement prêt immobilier | EXCLUDE — personal mortgage (not professional charge unless mixed-use property) |

---

## Section 4 — Worked Examples

### Example 1 — Société Générale: Consultant, Régime Réel, Single
**Scenario:** IT consultant, €95,000 recettes HT, €28,000 charges, URSSAF €22,000, single (1 part)

**Bank statement extract (Société Générale Pro):**
```
Date         | Libellé                                   | Débit (€)    | Crédit (€)   | Solde (€)
15/04/2025   | VIR SEPA TECHCORP FRANCE SAS             |              | 12,000.00    | 48,500.00
20/04/2025   | VIR SEPA STARTUP PARIS                   |              |  8,500.00    | 57,000.00
25/04/2025   | PRLV URSSAF COTISATIONS                  | 1,833.33     |              | 55,166.67
28/04/2025   | CB ADOBE SYSTEMS INC                     |    79.00     |              | 55,087.67
30/04/2025   | AGIOS / FRAIS BANCAIRES                  |    15.00     |              | 55,072.67
```

**BNC Computation (Form 2035):**
| Line | Amount |
|---|---|
| Recettes professionnelles | €95,000 |
| Charges professionnelles | (€28,000) |
| URSSAF cotisations | (€22,000) |
| **Bénéfice BNC (Form 2035)** | **€45,000** |

**Income tax (Form 2042):**
| Line | Amount |
|---|---|
| BNC (revenu professionnel) | €45,000 |
| CSG déductible (6.8% × €22,000 prior year URSSAF) | (€1,496) |
| Revenu brut global | €43,504 |
| Quotient: 1 part → tax base | €43,504 |
| Tax: 11% on (28,797−11,294) = €1,925 + 30% on (43,504−28,797) = €4,412 | €6,337 |
| Décote check: tax < €1,929 → not applicable (above threshold) | — |
| **Impôt sur le revenu** | **€6,337** |

### Example 2 — BNP Paribas: Designer, Micro-BNC, Married 2 Children
**Scenario:** Graphic designer, €55,000 recettes, micro-BNC, married (2 parts + 1 part = 3 parts for 2 children)

**Bank statement extract (BNP Paribas Pro):**
```
Date         | Référence                                 | Montant débit | Montant crédit | Solde
10/03/2025   | VIR SARL DESIGN STUDIO                   |               | 8,500.00       | 34,200.00
15/03/2025   | VIR MALT PLATFORM                        |               | 3,900.00       | 38,100.00
20/03/2025   | PRELEVEMENT ORANGE PRO                   | 45.99         |                | 38,054.01
22/03/2025   | CB SNCF BILLET PARIS LYON                | 89.00         |                | 37,965.01
28/03/2025   | FRAIS VIREMENT                           | 2.50          |                | 37,962.51
```

**BNC — Micro-BNC:**
- Recettes: €55,000
- Abattement forfaitaire: 34% = €18,700
- BNC imposable: €55,000 − €18,700 = **€36,300**

**Income tax (3 parts):**
| Line | Amount |
|---|---|
| BNC imposable | €36,300 |
| Revenu foyer (assuming spouse €0) | €36,300 |
| Per part: €36,300 ÷ 3 = | €12,100 |
| Tax per part: 11% × (12,100 − 11,294) = | €89 |
| × 3 parts | €267 |
| Décote check (seuil €1,929): tax €267 < threshold → décote applies | — |
| Décote: €833 − (€267 × 45.25%) = €833 − €121 = | €712 |
| But tax is only €267 — décote cannot exceed tax | — |
| **Impôt dû** | **€0** (décote > tax) |

### Example 3 — Crédit Agricole: Lawyer, Régime Réel, Home Office
**Scenario:** Avocate inscrite au barreau, €120,000 recettes, €35,000 charges (incl. home office), URSSAF €30,000

**Bank statement extract (Crédit Agricole Pro):**
```
Date opération | Libellé opération                       | Débit         | Crédit        | Solde
08/05/2025     | VIREMENT DE CABINET XYZ                |               | 15,000.00     | 78,000.00
12/05/2025     | VIREMENT CLIENT PARTICULIER             |               |  4,500.00     | 82,500.00
15/05/2025     | PRELEVEMENT URSSAF AVOCATS             | 2,500.00      |               | 80,000.00
20/05/2025     | CB DEBEAUSSE FOURNITURES BUREAU        |   145.00      |               | 79,855.00
25/05/2025     | CB RESTAURANT D'AFFAIRES (CLIENT)      |   120.00      |               | 79,735.00
```

**Home office calculation:**
- Apartment 75 sqm total; office room 15 sqm dedicated
- Home office %: 15/75 = 20%
- Annual rent €18,000 × 20% = €3,600
- Annual utilities €2,400 × 20% = €480

**BNC Computation:**
| Line | Amount |
|---|---|
| Recettes | €120,000 |
| Charges (direct) | (€30,920) |
| Home office: rent (€3,600) + utilities (€480) | (€4,080) |
| URSSAF | (€30,000) |
| **BNC** | **€55,000** |

**Income tax (single, 1 part):**
- Tax: 11% × (28,797−11,294) + 30% × (55,000−28,797) = €1,925 + €7,861 = **€9,786**

### Example 4 — LCL: Freelance Writer, Micro-BNC Comparison vs Réel
**Scenario:** Écrivain/journaliste, €40,000 recettes, actual charges only €5,000 (low expense business)

**Bank statement extract (LCL — Le Crédit Lyonnais):**
```
Date valeur | Libellé                                    | Débit (€)    | Crédit (€)   | Solde (€)
05/06/2025  | VIR EDITIONS GALLIMARD                    |              | 6,000.00     | 22,400.00
10/06/2025  | VIR MAGAZINE LE MONDE                     |              | 2,500.00     | 24,900.00
15/06/2025  | CB FNAC LIVRES PROFESSIONNELS             | 85.00        |              | 24,815.00
20/06/2025  | PRELEVEMENT SFR MOBILE                   | 29.99        |              | 24,785.01
25/06/2025  | CB TRAIN SNCF PARIS-BORDEAUX              | 72.00        |              | 24,713.01
```

**Comparison:**
| | Micro-BNC | Régime Réel |
|---|---|---|
| Recettes | €40,000 | €40,000 |
| Abattement / charges | −34% = €13,600 | −€5,000 actual |
| BNC imposable | **€26,400** | **€35,000** |
| Tax (single, 1 part approx.) | ~€2,800 | ~€5,000 |
| **Winner** | **Micro-BNC** | — |

**Rule:** If actual charges < 34% of revenue → micro-BNC wins.

### Example 5 — CIC: Developer with Madelin Retirement Plan
**Scenario:** Développeur, €80,000 recettes, €18,000 charges, URSSAF €20,000, Madelin PER €8,000

**Bank statement extract (CIC):**
```
Date         | Libellé                                   | Débit (€)    | Crédit (€)   | Solde (€)
12/07/2025   | VIREMENT STARTUP TECH                    |              | 18,000.00    | 65,000.00
18/07/2025   | VIR SEPA FINTECH PARIS                   |              |  9,500.00    | 74,500.00
22/07/2025   | PRLV URSSAF DSI                          | 1,666.67     |              | 72,833.33
26/07/2025   | PRLV MADELIN RETRAITE AXA                | 666.67       |              | 72,166.66
30/07/2025   | CB GITHUB ENTERPRISE                     | 320.00       |              | 71,846.66
```

**Madelin deduction ceiling:** 10% × BNC, plus 15% × (BNC − €43,992). Calculate after BNC is known.

**BNC Computation:**
| Line | Amount |
|---|---|
| Recettes | €80,000 |
| Charges | (€18,000) |
| URSSAF | (€20,000) |
| **BNC** | **€42,000** |

**Madelin ceiling:** 10% × €42,000 = €4,200 (if BNC < PASS). Actual Madelin paid: €8,000 → cap applies: deductible = **€4,200**

**Income tax (1 part):**
- Revenu: €42,000 − €4,200 (Madelin) − €1,360 (CSG) = €36,440
- Tax: 11% × (28,797−11,294) + 30% × (36,440−28,797) = €1,925 + €2,293 = **€4,218**

### Example 6 — Banque Populaire: Architect with TVA
**Scenario:** Architecte (TVA registered), €150,000 recettes TTC (incl. 20% TVA), charges €40,000 HT, URSSAF €35,000

**Bank statement extract (Banque Populaire Pro):**
```
Date         | Libellé                                    | Débit (€)     | Crédit (€)    | Solde (€)
03/08/2025   | VIR CABINET XYZ ARCHITECTES               |               | 24,000.00     | 110,000.00
10/08/2025   | VIR CLIENT PROMOTION IMMO                 |               | 18,000.00     | 128,000.00
15/08/2025   | PRLV TVA DGFiP                           | 4,500.00      |               | 123,500.00
20/08/2025   | CB MATÉRIAUX BUREAU                       |   890.00      |               | 122,610.00
25/08/2025   | PRLV URSSAF ARCHITECT                    | 2,916.67      |               | 119,693.33
```

**TVA separation:** Total TTC receipts €150,000 → HT recettes = €150,000 ÷ 1.20 = **€125,000 HT** (use this on Form 2035)

**BNC Computation:**
| Line | Amount |
|---|---|
| Recettes HT | €125,000 |
| Charges HT | (€40,000) |
| URSSAF | (€35,000) |
| **BNC** | **€50,000** |

---

## Section 5 — Tier 1 Rules (Compressed Reference)

### Domicile Fiscal (Tax Residency)
- **France resident:** Has principal home in France OR principal professional activity in France OR centre of economic interests in France → worldwide income taxable in France
- **Non-resident:** Taxable only on France-source income; flat rates apply (no quotient familial)

### BNC vs BA vs BIC
| Category | When |
|---|---|
| BNC (bénéfices non commerciaux) | Professions libérales: doctors, lawyers, architects, consultants, writers, artists |
| BIC (bénéfices industriels et commerciaux) | Commercial/artisanal activities: retail, manufacturing, some tech |
| BA (bénéfices agricoles) | Agricultural activities |

**Note:** Auto-entrepreneurs (micro-entrepreneurs) declare on 2042-C-PRO but use simplified micro calculation.

### Prélèvement à la Source (Withholding at Source)
- Since 2019: income tax paid monthly via PAS rate applied to income
- Self-employed: monthly/quarterly acomptes (advance payments) to DGFiP
- May optionally adjust acompte rate online via impots.gouv.fr (Mon Espace)
- Final settlement in September following year after 2042 declaration

### Assurance Madelin / PER
- Contributions to Madelin contracts (complementary health, retirement, disability, loss of employment) deductible from BNC
- Retirement ceiling: 10% × BNC + 15% × (BNC − PASS), or 10% × 8 × PASS if higher
- PASS 2025: €46,368

### Décote
- Applied when tax < €1,929 (single) or €3,191 (couple, 2025)
- Décote = €833 − (tax × 45.25%) for single; €1,330 − (tax × 45.25%) for couple
- Reduces tax by this amount (cannot reduce below €0)

### Filing Deadlines
| Event | Deadline |
|---|---|
| Declaration 2042 (online, zone 1: IDF + major cities) | Mid-May (exact date varies) |
| Declaration 2042 (online, zones 2/3) | Late May / early June |
| Paper declaration | End April |
| Form 2035 (BNC réel) | Same deadline as 2042 |
| Acomptes PAS | 15th of each month (monthly) or 15 Feb/May/Aug/Nov (quarterly) |

### Penalties
| Situation | Penalty |
|---|---|
| Late declaration | 10% of tax due |
| Late payment | 10% surcharge + 0.2%/month interest |
| Fraudulent under-reporting | 40–80% surcharge |
| Missing declaration after formal notice | 100% surcharge |

---

## Section 6 — Tier 2 Catalogue

### T2-FR-1: Home Office (Bureau à Domicile)
**Why T2:** Floor area split and nature of use are facts only the client knows.

**Method:**
1. Dedicated professional room: area ÷ total area × rent/utilities/internet
2. Mixed-use room: not recommended — hard to justify to DGFiP without specific business use documentation
3. Tenant vs owner-occupier: both can claim proportional rent/charges

**Required from client:** Total floor area (m²), office room area (m²), whether room exclusively professional.

### T2-FR-2: Vehicle (Barème Kilométrique vs Frais Réels)
**Why T2:** Actual km and business use are facts only the client knows.

**Barème kilométrique (2025 — Puissance fiscale):**
| CV fiscal | Up to 5,000 km | 5,001–20,000 km | >20,000 km |
|---|---|---|---|
| 3 CV | €0.502/km | €0.300 + €1,007 | €0.350/km |
| 4 CV | €0.575/km | €0.343 + €1,165 | €0.401/km |
| 5 CV | €0.603/km | €0.361 + €1,212 | €0.422/km |
| 6 CV | €0.631/km | €0.378 + €1,263 | €0.444/km |
| 7 CV+ | €0.661/km | €0.397 + €1,320 | €0.463/km |

**Required from client:** Fiscal power (CV) of vehicle, total km driven, business km (from logbook).

### T2-FR-3: Phone & Internet
**Why T2:** Professional/personal split is client-specific.

**Guidance:** If professional only: 100%. If dual-use: document business proportion (e.g., 70% if primary business tool).
**Required from client:** Whether dedicated pro line or mixed-use; estimated business call %.

### T2-FR-4: Meals — Solo vs Business Client
**Why T2:** Business purpose and attendee details required.

- **Repas d'affaires (with client):** Actual cost, deductible — must note client name, purpose
- **Repas solo (working away from home):** Forfait: excess of meal cost over €5.20 (min value of meal at home), capped at €19.40/day total (2025 amounts)

**Required from client:** For each restaurant expense — was it with a client (names) or solo working meal?

### T2-FR-5: Madelin/PER Ceiling Calculation
**Why T2:** Ceiling depends on final BNC, which must be computed before relief is applied.

**Process:** Compute BNC first → calculate Madelin ceiling → apply deduction (up to ceiling or actual paid, whichever is lower).
**Required from client:** All Madelin/PER contribution receipts for the year.

---

## Section 7 — Excel Working Paper

### Sheet 1: Recettes (Revenue)
| Column | Content |
|---|---|
| A | Date |
| B | Client |
| C | Invoice reference |
| D | Montant HT (EUR) |
| E | TVA (if applicable) |
| F | Montant TTC |
| G | Received in bank (date) |
| H | Category (Recettes BNC / Other) |

**Total recettes HT:** `=SUMIF(H:H,"Recettes BNC",D:D)`

### Sheet 2: Charges (Expenses — Form 2035)
| Column | Content |
|---|---|
| A | Date |
| B | Fournisseur |
| C | Montant HT (EUR) |
| D | Catégorie (loyer/téléphone/déplacements etc.) |
| E | % professionnel |
| F | Montant déductible (=C×E) |
| G | Référence justificatif |

**Lignes Form 2035 mapping:**
- Line AB: Achats — materials
- Line BK: Frais de personnel (employees)
- Line BT: Impôts et taxes (CFE, etc.)
- Line BU: Loyers et charges locatives
- Line BV: Locations de matériel
- Line BW: Entretien et réparations
- Line BX: Personnel extérieur
- Line BY: Autres frais divers de gestion

### Sheet 3: BNC Computation
| Line | Form 2035 Ref | Amount |
|---|---|---|
| Recettes professionnelles | Line AA | |
| Total charges déductibles | | |
| URSSAF cotisations | | |
| **Bénéfice BNC** | Line CP | |
| CSG déductible (6.8% × prior year URSSAF) | Form 2042 | |

### Sheet 4: Impôt sur le Revenu
| Line | Amount |
|---|---|
| BNC (from Sheet 3) | |
| Other household income | |
| Revenu brut global | |
| Charges déductibles du RBG (CSG, pensions alimentaires) | |
| Revenu net global | |
| Abattements (10% for employment if applicable) | |
| Revenu imposable | |
| Nombre de parts (quotient familial) | |
| Income per part | |
| Tax per part (bracket table) | |
| × parts | |
| Réductions d'impôt | |
| Crédits d'impôt | |
| PAS acomptes déjà payés | |
| **Solde** | |

---

## Section 8 — Bank Statement Reading Guide

### Société Générale (Pro)
- Format: `Date | Libellé | Débit (€) | Crédit (€) | Solde (€)`
- Date: DD/MM/YYYY
- Income = Crédit column
- Key: VIR SEPA = SEPA credit transfer; PRLV = direct debit (prélèvement)

### BNP Paribas (Pro)
- Format: `Date | Référence | Montant débit | Montant crédit | Solde`
- Date: DD/MM/YYYY
- Income = Montant crédit

### Crédit Agricole (Pro)
- Format: `Date opération | Libellé opération | Débit | Crédit | Solde`
- Date: DD/MM/YYYY
- VIR = virement (transfer received); PRLV = prélèvement (debit)

### LCL — Le Crédit Lyonnais
- Format: `Date valeur | Libellé | Débit (€) | Crédit (€) | Solde (€)`
- Date: DD/MM/YYYY
- Uses "Date valeur" (value date) — note this may differ from operation date

### CIC
- Format: `Date | Libellé | Débit (€) | Crédit (€) | Solde (€)`
- Date: DD/MM/YYYY
- PRLV = direct debit; VIR = incoming wire

### Banque Populaire / BPCE
- Format: `Date | Libellé | Débit (€) | Crédit (€) | Solde (€)`
- Date: DD/MM/YYYY
- CB = carte bancaire (card payment)

### Exclusion Patterns (all French banks)
| Pattern | Action |
|---|---|
| VIR vers compte personnel / épargne | EXCLUDE — personal transfer |
| Prélèvement carte bancaire | EXCLUDE — individual expenses captured per CB transaction |
| TVA DGFiP prélèvement | EXCLUDE — TVA obligation, not income tax deductible |
| PRLV IR DGFiP / acompte PAS | EXCLUDE from expenses — advance income tax payment (credit on 2042) |
| Remboursement prêt | EXCLUDE — personal loan |
| AGIOS | Yes — bank charges, deductible |

---

## Section 9 — Onboarding Fallback

**Priority 1 (blocking):**
1. "What was your total gross revenue (recettes professionnelles HT) for the year?"
2. "Are you using micro-BNC or régime réel (déclaration contrôlée)?"
3. "What is your household situation — married/PACS, children?"

**Priority 2 (regime réel — needed for accurate computation):**
4. "Please provide your URSSAF annual summary (cotisations sociales paid)."
5. "Do you have receipts for all professional charges claimed?"
6. "Do you work from home? If yes: total floor area and office room area?"
7. "Do you use a personal vehicle for professional travel? If yes, fiscal horsepower and professional km driven."

**Priority 3 (reliefs and credits):**
8. "Did you contribute to a Madelin or PER retirement contract? Total amount?"
9. "Did you donate to charities? Which ones and amounts?"
10. "Did you employ domestic help (emploi à domicile) — possible crédit d'impôt?"
11. "Do you have young children in daycare — crédit garde d'enfants?"

**Conservative defaults if data gaps:**
- Use micro-BNC (34% abattement) if below threshold and expenses unconfirmed
- Exclude home office if floor area cannot be confirmed
- Use barème kilométrique over actual costs if vehicle logbook unavailable

---

## Section 10 — Reference Material

### Key Forms
| Form | Purpose |
|---|---|
| 2042 | Main income tax declaration |
| 2042-C-PRO | Revenus professionnels (BNC, BIC, BA) |
| 2035 | Déclaration BNC régime réel (attached to 2042) |
| 2035-A / 2035-B | Supporting schedules to 2035 |
| 2042-RICI | Réductions et crédits d'impôt |

### Filing Platform
- **impots.gouv.fr** — Mon Espace Particulier (login with FranceConnect or identifiants DGFiP)
- Pre-filled data: income known to DGFiP (bank interest, dividends) auto-populated; BNC must be entered manually

### Key References
- DGFiP (Direction Générale des Finances Publiques): impots.gouv.fr
- URSSAF (social charges): urssaf.fr
- Barème kilométrique: published annually in Bulletin Officiel des Finances Publiques (BOFIP)
- Madelin ceilings: bofip.impots.gouv.fr

### Social Charges (Résumé)
- URSSAF charges for BNC are ~21.1% of net BNC (2025, above PASS) or ~~22.9% for small incomes
- Note: social charges are separate from income tax — URSSAF calculates and bills independently
- CSG-CRDS: 9.7% of gross BNC income; 6.8% is income-deductible

---

## Prohibitions
- Do not advise on TVA (taxe sur la valeur ajoutée) obligations, rates, or filing — separate France VAT skill required
- Do not advise on Impôt sur les Sociétés (IS) — this skill covers individual BNC taxpayers only
- Do not advise on property tax (taxe foncière) or taxe d'habitation
- Do not advise on succession or donation taxation (droits de succession/donation)
- Do not advise on social charges (URSSAF cotisations) calculation — URSSAF jurisdiction; this skill only notes their deductibility

## Disclaimer
This skill provides general guidance for informational and planning purposes. It does not constitute tax advice. French tax law is administered by the Direction Générale des Finances Publiques (DGFiP). Clients should consult an expert-comptable or conseil fiscal for advice specific to their circumstances. Tax brackets, rates, and thresholds change annually — verify current rules at impots.gouv.fr and bofip.impots.gouv.fr.
