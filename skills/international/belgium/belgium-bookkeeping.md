---
name: belgium-bookkeeping
description: Use this skill whenever asked about Belgian bookkeeping, chart of accounts, PCMN/MAR, annual accounts filing, balance sheet or P&L format in Belgium. Trigger on phrases like "Belgian bookkeeping", "PCMN", "MAR", "Plan Comptable Minimum Normalisé", "minimumindeling", "jaarrekening Belgium", "comptes annuels", "NBB filing", "Nationale Bank", "micro-entity Belgium", "Belgian GAAP", "small company Belgium", "chart of accounts Belgium", "boekhoudwetgeving", "WVV", or any question about recording transactions, financial reporting, or accounting standards for Belgian entities.
version: 1.0
jurisdiction: BE
tax_year: 2025
last_updated: 2026-07-13
review_status: pending_review
depends_on: - bookkeeping-workflow-base
category: bookkeeping
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Belgium Bookkeeping

## Section 1 -- Quick Reference

**Quick Reference**

| Field | Value |
| --- | --- |
| Country | Belgium (Koninkrijk België / Royaume de Belgique) |
| Currency | EUR |
| Financial year | Flexible (most common: 1 January -- 31 December) |
| Accounting standards | Belgian GAAP; Royal Decree of 29 April 2019 (WVV/CSA execution) |
| Standard chart of accounts | PCMN / MAR (Plan Comptable Minimum Normalisé / Minimumindeling Algemeen Rekeningenstelsel) |
| Governing body | CNC/CBN (Commission des Normes Comptables / Commissie voor Boekhoudkundige Normen) |
| Key legislation | Code des Sociétés et des Associations (CSA) / Wetboek van Vennootschappen en Verenigingen (WVV); Arrêté Royal 29/04/2019 |
| Filing obligation | Nationale Bank van België (NBB/BNB) -- within 7 months of year-end |
| Tax authority | SPF Finances / FOD Financiën |
| Mandatory chart | Yes -- PCMN/MAR is legally required for all enterprises subject to bookkeeping obligations |

## Section 2 -- Standard Chart of Accounts (PCMN/MAR)

The PCMN is the legally mandated Belgian chart of accounts. It uses 7 main classes (1-7) plus optional classes 8 and 9.

### Class 1 -- Equity, Provisions and Long-Term Debt

**Class 1 -- Equity, Provisions and Long-Term Debt**

| Code | Account | Description |
| --- | --- | --- |
| 10 | Capital | Share capital |
| 11 | Contribution hors capital | Share premium and other contributions |
| 12 | Plus-values de réévaluation | Revaluation surpluses |
| 13 | Réserves | Reserves |
| 130 | Réserve légale | Legal reserve |
| 131 | Réserves indisponibles | Unavailable reserves |
| 133 | Réserves disponibles | Available reserves |
| 14 | Bénéfice/Perte reporté(e) | Retained earnings / accumulated losses |
| 15 | Subsides en capital | Capital grants |
| 16 | Provisions | Provisions for liabilities and charges |
| 17 | Dettes à plus d'un an | Amounts payable after more than one year |
| 170 | Emprunts subordonnés | Subordinated loans |
| 172 | Emprunts bancaires | Bank loans (long-term) |
| 173 | Dettes de location-financement | Finance lease obligations |
| 175 | Dettes commerciales | Trade debts (long-term) |

### Class 2 -- Formation Expenses, Fixed Assets, Long-Term Receivables

**Class 2 -- Formation Expenses, Fixed Assets, Long-Term Receivables**

| Code | Account | Description |
| --- | --- | --- |
| 20 | Frais d'établissement | Formation/incorporation expenses |
| 21 | Immobilisations incorporelles | Intangible fixed assets |
| 210 | Frais de R&D | Research and development costs |
| 211 | Concessions, brevets, licences | Concessions, patents, licences |
| 212 | Goodwill | Goodwill |
| 22 | Terrains et constructions | Land and buildings |
| 23 | Installations, machines | Plant, machinery and equipment |
| 24 | Mobilier et matériel roulant | Furniture and vehicles |
| 240 | Mobilier et matériel de bureau | Office furniture and equipment |
| 241 | Matériel informatique | Computer hardware |
| 242 | Matériel roulant | Vehicles |
| 25 | Immob. détenues en location-financement | Assets held under finance leases |
| 26 | Autres immob. corporelles | Other tangible fixed assets |
| 27 | Immob. financières | Financial fixed assets |
| 28 | Amortissements | Accumulated depreciation (contra) |
| 29 | Créances à plus d'un an | Amounts receivable after more than one year |

### Class 3 -- Inventories and Work in Progress

**Class 3 -- Inventories and Work in Progress**

| Code | Account | Description |
| --- | --- | --- |
| 30 | Matières premières | Raw materials |
| 31 | Fournitures | Consumables |
| 32 | En-cours de fabrication | Work in progress |
| 33 | Produits finis | Finished goods |
| 34 | Marchandises | Goods for resale |
| 35 | Immeubles destinés à la vente | Real estate for sale |
| 36 | Acomptes versés | Advance payments on inventory |
| 37 | Commandes en cours | Contracts in progress |

### Class 4 -- Receivables and Payables (within one year)

**Class 4 -- Receivables and Payables (within one year)**

| Code | Account | Description |
| --- | --- | --- |
| 40 | Créances commerciales | Trade receivables |
| 400 | Clients | Customers |
| 401 | Effets à recevoir | Bills of exchange receivable |
| 44 | Dettes commerciales | Trade payables |
| 440 | Fournisseurs | Suppliers |
| 441 | Effets à payer | Bills of exchange payable |
| 45 | Dettes fiscales, salariales, sociales | Tax and social security payables |
| 450 | Dettes fiscales estimées | Estimated tax payable |
| 451 | TVA à payer | VAT payable |
| 452 | Impôts et taxes à payer | Taxes payable |
| 453 | Précomptes retenus | Withholding taxes |
| 454 | ONSS | Social security payable |
| 455 | Rémunérations | Wages payable |
| 46 | Acomptes reçus | Advance payments received |
| 48 | Dettes diverses | Sundry payables |
| 49 | Comptes de régularisation | Accruals and deferred income |
| 490 | Charges à reporter | Deferred charges |
| 491 | Produits acquis | Accrued income |
| 492 | Charges à imputer | Accrued charges |
| 493 | Produits à reporter | Deferred income |

### Class 5 -- Cash and Short-Term Investments

**Class 5 -- Cash and Short-Term Investments**

| Code | Account | Description |
| --- | --- | --- |
| 50 | Actions propres | Own shares |
| 51 | Actions et parts | Shares and participations |
| 52 | Titres à revenu fixe | Fixed-income securities |
| 53 | Dépôts à terme | Term deposits |
| 55 | Établissements de crédit | Bank accounts |
| 550 | Compte courant | Current account |
| 56 | Office des chèques postaux | Postal account |
| 57 | Caisses | Cash in hand |
| 58 | Virements internes | Internal transfers |

### Class 6 -- Charges (Expenses)

**Class 6 -- Charges (Expenses)**

| Code | Account | Description |
| --- | --- | --- |
| 60 | Approvisionnements et marchandises | Purchases of goods/materials |
| 600 | Achats de matières premières | Purchases of raw materials |
| 604 | Achats de marchandises | Purchases of goods for resale |
| 61 | Services et biens divers | Services and miscellaneous goods |
| 610 | Loyers et charges locatives | Rent and related charges |
| 611 | Entretien et réparations | Maintenance and repairs |
| 612 | Fournitures (énergie, eau) | Utilities (energy, water) |
| 613 | Fournitures de bureau | Office supplies |
| 614 | Assurances | Insurance |
| 615 | Transports | Transport costs |
| 616 | Frais postaux et télécom | Postal and telecoms |
| 617 | Honoraires | Professional fees |
| 618 | Publicité | Advertising |
| 619 | Rétributions de tiers | Third-party remuneration |
| 62 | Rémunérations et charges sociales | Staff costs |
| 620 | Rémunérations brutes | Gross wages |
| 621 | Cotisations patronales ONSS | Employer social security |
| 623 | Assurance groupe/pension | Group insurance/pension |
| 63 | Amortissements et réductions de valeur | Depreciation and write-downs |
| 630 | Dotation aux amortissements | Depreciation charge |
| 634 | Réductions de valeur stocks | Write-down on inventory |
| 64 | Autres charges d'exploitation | Other operating charges |
| 640 | Taxes d'exploitation | Operating taxes (précompte immobilier, etc.) |
| 65 | Charges financières | Financial charges |
| 650 | Intérêts sur emprunts | Interest on borrowings |
| 653 | Frais bancaires | Bank charges |
| 66 | Charges exceptionnelles | Extraordinary charges |
| 67 | Impôts sur le résultat | Income taxes |
| 670 | Impôts belges sur le résultat | Belgian income tax |

### Class 7 -- Produits (Income)

**Class 7 -- Produits (Income)**

| Code | Account | Description |
| --- | --- | --- |
| 70 | Chiffre d'affaires | Turnover |
| 700 | Ventes de marchandises | Sales of goods |
| 701 | Ventes de produits finis | Sales of finished products |
| 706 | Prestations de services | Services rendered |
| 71 | Variation des stocks/en-cours | Change in inventories/WIP |
| 72 | Production immobilisée | Capitalised production |
| 74 | Autres produits d'exploitation | Other operating income |
| 75 | Produits financiers | Financial income |
| 750 | Produits des immob. financières | Income from financial assets |
| 751 | Produits des actifs circulants | Income from current assets |
| 753 | Intérêts créditeurs | Interest received |
| 76 | Produits exceptionnels | Extraordinary income |
| 77 | Régularisation d'impôts | Tax adjustments |

## Section 3 -- Revenue Recognition

### Cash vs Accrual Basis

**Cash vs Accrual Basis**

| Entity Type | Basis | Notes |
| --- | --- | --- |
| All companies (SA/BV/SRL/NV) | Accrual (mandatory) | WVV/CSA requires accrual under all schemes |
| Sole trader (entreprise individuelle) | Simplified if turnover < EUR 500,000 | Single-entry allowed below threshold |
| Liberal professions | Accrual (double-entry) | Must keep double-entry books if company form |

### Key Rules

- **Revenue recognition timing** — Revenue recognised at the point of delivery for goods, at completion/over time for services
- **Prudence principle** — Belgian GAAP follows prudence principle (voorzichtigheidsbeginsel): unrealised gains are not recognised, unrealised losses are provided for
- **Construction contracts method** — Construction contracts: completed-contract method is the norm under Belgian GAAP (unlike IFRS)
- **VAT trigger (factuurstelsel)** — Invoicing triggers VAT obligation regardless of payment (factuurstelsel)

### Simplified Bookkeeping Thresholds

- **Simplified single-entry bookkeeping eligibility** — EUR 500,000 EUR (Enterprises with annual turnover (excl. VAT) ≤ EUR 500,000 may use simplified single-entry bookkeeping (purchase/sales journal, financial journal, inventory once per year))
- **Full double-entry bookkeeping mandatory** — Above EUR 500,000: full double-entry bookkeeping is mandatory

## Section 4 -- Expense Classification

### Deductible Expenses (Key Categories)

**Deductible Expenses (Key Categories)**

| Category | PCMN Code | Tax Deductibility |
| --- | --- | --- |
| Office rent | 610 | 100% deductible |
| Utilities (business) | 612 | 100% deductible |
| Professional fees (accountant, lawyer) | 617 | 100% deductible |
| Insurance (business) | 614 | 100% deductible |
| Advertising | 618 | 100% deductible |
| Office supplies | 613 | 100% deductible |
| Postage and telecoms | 616 | 100% deductible (business portion) |
| Bank charges | 653 | 100% deductible |
| Software subscriptions | 613/617 | 100% deductible |
| Staff costs | 62x | 100% deductible |

### Partially/Non-Deductible Expenses

**Partially/Non-Deductible Expenses**

| Category | Limitation |
| --- | --- |
| Restaurant expenses (business) | 69% deductible |
| Representation costs (gifts, receptions) | 50% deductible |
| Company car costs | Limited by CO₂ formula; minimum 50% deductible (decreasing for polluting vehicles) |
| Clothing (non-uniform) | 0% -- personal expense |
| Fines and penalties | 0% -- never deductible |
| Income tax (ISOC/VenB) | 0% -- never deductible |
| Social benefit in kind (excessive) | Subject to benefit-in-kind taxation |

### Company Car Formula (from 2020)

- **Company car deductibility %** — Deductibility % = 120% - (0.5% × CO₂ coefficient × CO₂ emission in g/km). Minimum 50%, maximum 100%. From 2026: fully electric = 100% deductible; fossil fuel cars purchased after 01/07/2023 face decreasing deductibility.

## Section 5 -- Asset vs Expense Thresholds

### Capitalization Rules

**Capitalization Rules**

| Rule | Detail |
| --- | --- |
| Mandatory capitalization | All assets with useful life > 1 year must be capitalized (no de minimis threshold in law) |
| Common practice threshold | Assets < EUR 1,000 often expensed directly (administrative tolerance, not law) |
| Formation expenses | May be capitalized and amortized over max 5 years |
| R&D costs | May be capitalized if conditions met (CNC/CBN Advice 138/1) |

### Depreciation Methods and Rates

**Depreciation Methods and Rates**

| Asset Type | Method | Common Rate |
| --- | --- | --- |
| Industrial buildings | Straight-line | 5% (20 years) |
| Commercial buildings | Straight-line | 3% (33 years) |
| Plant and machinery | Straight-line | 20% (5 years) |
| IT equipment (computers) | Straight-line | 33% (3 years) |
| Office furniture | Straight-line | 10-20% (5-10 years) |
| Vehicles | Straight-line | 20% (5 years) |
| Software | Straight-line | 33% (3 years) |
| Goodwill | Straight-line | Min. 5 years (max 20% p.a.) |
| Intangible assets (general) | Straight-line | Minimum 5 years (20% max) |
| Formation expenses | Straight-line | Maximum 5 years (20%) |

### Key Rules

- **Pro rata temporis depreciation** — Proportional (pro rata temporis) depreciation in year of acquisition -- calculated on daily basis
- **Declining balance restriction** — Double declining balance method was formerly allowed; now only straight-line is accepted for tax (since 2020 reform for large companies; SMEs retained declining-balance option)
- **SME declining-balance option** — SMEs may opt for declining-balance (max 2× straight-line rate, capped at 40% of acquisition cost)
- **Residual value convention** — Residual value is typically EUR 0 (Belgian practice)

## Section 6 -- P&L Format (Compte de Résultats / Resultatenrekening)

Belgium prescribes a specific P&L format in the Royal Decree. Small companies use the "abbreviated" scheme; micro-entities use the "micro" scheme.

### Full/Abbreviated Scheme (by Nature)

**P&L Full/Abbreviated Scheme (by Nature)**

```
I.    Chiffre d'affaires (Turnover)                                xxx
II.   Variation des stocks / en-cours                              xxx
III.  Production immobilisée                                       xxx
IV.   Autres produits d'exploitation                               xxx
                                                                -------
      Total produits d'exploitation                                xxx

V.    Approvisionnements et marchandises                          (xxx)
VI.   Services et biens divers                                    (xxx)
VII.  Rémunérations et charges sociales                           (xxx)
VIII. Amortissements et réductions de valeur                      (xxx)
IX.   Provisions pour risques et charges                          (xxx)
X.    Autres charges d'exploitation                               (xxx)
                                                                -------
      Bénéfice/Perte d'exploitation                                xxx

XI.   Produits financiers                                          xxx
XII.  Charges financières                                         (xxx)
                                                                -------
      Bénéfice/Perte courant(e)                                    xxx

XIII. Produits exceptionnels                                       xxx
XIV.  Charges exceptionnelles                                     (xxx)
                                                                -------
      Bénéfice/Perte de l'exercice avant impôts                    xxx

XV.   Impôts sur le résultat                                      (xxx)
                                                                -------
XVI.  Bénéfice/Perte de l'exercice                                 xxx
```

## Section 7 -- Balance Sheet Format (Bilan / Balans)

Belgium uses a prescribed vertical format.

### Full/Abbreviated Scheme

**Balance Sheet Full/Abbreviated Scheme**

```
ACTIF (Assets)

ACTIFS IMMOBILISÉS (Fixed assets)
  I.    Frais d'établissement                                     xxx
  II.   Immobilisations incorporelles                             xxx
  III.  Immobilisations corporelles                               xxx
  IV.   Immobilisations financières                               xxx

ACTIFS CIRCULANTS (Current assets)
  V.    Créances à plus d'un an                                   xxx
  VI.   Stocks et commandes en cours                              xxx
  VII.  Créances à un an au plus                                  xxx
  VIII. Placements de trésorerie                                  xxx
  IX.   Valeurs disponibles                                       xxx
  X.    Comptes de régularisation                                 xxx
                                                               -------
TOTAL DE L'ACTIF                                                  xxx
                                                               =======

PASSIF (Equity & Liabilities)

CAPITAUX PROPRES (Equity)
  I.    Capital/Apport                                            xxx
  II.   Primes d'émission                                         xxx
  III.  Plus-values de réévaluation                               xxx
  IV.   Réserves                                                  xxx
  V.    Bénéfice/Perte reporté(e)                                 xxx
  VI.   Subsides en capital                                       xxx

PROVISIONS ET IMPÔTS DIFFÉRÉS                                     xxx
  VII.  Provisions pour risques et charges                        xxx
  VIII. Impôts différés                                           xxx

DETTES (Liabilities)
  IX.   Dettes à plus d'un an                                     xxx
  X.    Dettes à un an au plus                                    xxx
  XI.   Comptes de régularisation                                 xxx
                                                               -------
TOTAL DU PASSIF                                                   xxx
                                                               =======
```

## Section 8 -- Bank Reconciliation Patterns

### Belgian Bank Statement Formats

**Belgian Bank Statement Formats**

| Bank | Format | Key Fields |
| --- | --- | --- |
| KBC | CSV, CODA, MT940 | Date, Amount, Counterparty, Communication (structured/free) |
| BNP Paribas Fortis | CSV, CODA | Date, Amount, Details, Counterparty name, Communication |
| Belfius | CSV, CODA | Date, Amount, Counterparty, Reference, Communication |
| ING Belgium | CSV, CODA | Date, Amount, Description, Counterparty IBAN |
| Argenta | CSV | Date, Amount, Description, Counterparty |
| Crelan | CSV, CODA | Date, Amount, Reference, Communication |

### CODA Format

- **CODA** — CODA (COdified DAily statement) is the Belgian standard bank statement format. All Belgian banks provide CODA files, which can be imported directly by accounting software (Exact, Yuki, Octopus, etc.).

### Structured Communication (+++xxx/xxxx/xxxxx+++)

- **Structured communication usage** — Belgian transfers often use structured communication (gestructureerde mededeling / communication structurée) -- a 12-digit number formatted as +++xxx/xxxx/xxxxx+++. This is used for: Tax payments to FOD/SPF; Social security (ONSS/RSZ) payments; Invoice references (OGM/VCS)

### Common Transaction Descriptions

**Common Transaction Descriptions**

| Pattern | Classification |
| --- | --- |
| DOMICILIERING, DOMICILIATION | Direct debit (recurring expense) |
| OVERSCHRIJVING, VIREMENT | Bank transfer |
| BANCONTACT, MISTER CASH | Card payment |
| FOD FINANCIEN, SPF FINANCES | Tax payment |
| RSZ, ONSS | Social security payment |
| SOCIAAL SECRETARIAAT | Payroll bureau fee |
| PROVISIE, BANKKOSTEN | Bank charges |
| INTRESTEN, INTÉRÊTS | Interest (check direction) |

## Section 9 -- Micro-Entity / Small Business Simplifications

### Size Categories (from financial years starting after 31 December 2023)

**Size Categories (from financial years starting after 31 December 2023)**

| Category | Balance Sheet Total | Turnover (excl. VAT) | Employees |
| --- | --- | --- | --- |
| Micro | ≤ EUR 450,000 | ≤ EUR 900,000 | ≤ 10 |
| Small (Petit/Klein) | ≤ EUR 6,000,000 | ≤ EUR 11,250,000 | ≤ 50 |
| Large | Exceeds 2+ small criteria |  |  |

- **One-criterion tolerance** — Must not exceed more than one criterion on the balance sheet date of the last completed financial year.

### Simplifications

**Simplifications**

| Feature | Micro | Small | Large |
| --- | --- | --- | --- |
| Annual accounts scheme | Micro-scheme | Abbreviated scheme | Full scheme |
| Filing with NBB | Required (micro model) | Required (abbreviated) | Required (full) |
| Statutory audit | Not required | Not required | Required |
| Management report | Not required | Not required | Required |
| Notes detail | Very limited (8 items) | Limited | Full |
| Filing fee (2025) | EUR 72.10 (online) | EUR 72.10 (online) | EUR 405.10 (online) |
| Social balance sheet | Not required | Required if employees | Required |

### Sole Traders / Self-Employed (Zelfstandigen)

- **Simplified single-entry bookkeeping eligibility** — EUR 500,000 EUR (Enterprises with annual turnover (excl. VAT) ≤ EUR 500,000 may use simplified single-entry bookkeeping (purchase/sales journal, financial journal, inventory once per year))
- **Above threshold rule** — Above EUR 500,000: full double-entry bookkeeping mandatory
- **Annual income tax filing** — All self-employed must file annual income tax (personenbelasting/IPP) with annexe for professional income
- **Social contributions payment** — Social contributions paid to social insurance fund (sociaal verzekeringsfonds)

## Section 10 -- Interaction with Tax Skills

### Corporate Income Tax (ISOC/VenB)

- **Starting point for tax computation** — Annual accounts are the starting point for the tax computation
- **Fiscal result formula** — Fiscal result = accounting profit + disallowed expenses (DNA) - tax-exempt income
- **Key add-backs** — Key add-backs: restaurant costs (31%), representation (50%), car excess, fines

Use the be-income-tax skill for detailed calculation

### VAT (TVA/BTW)

- **VAT accounts** — VAT is recorded in accounts 411 (input VAT recoverable) and 451 (output VAT payable)
- **VAT return frequency threshold** — EUR 2,500,000 EUR (Monthly or quarterly VAT returns depending on turnover threshold)
- **Annual client listing deadline** — Annual client listing (listing annuelle) due by 31 March
- **Intra-community listings frequency** — Intra-community listings due monthly

Use the belgium-vat-return skill for filing details

### Social Contributions

- **Self-employed quarterly contributions** — Self-employed: quarterly social contributions to sociaal verzekeringsfonds (accounts 62x for companies, deducted personally for sole traders)
- **Company employer contributions** — approximately 25-30% of gross salary (ONSS/RSZ) %

Use the be-social-contributions skill for details

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional before filing or acting upon.

## Talk to a verified accountant

This skill is a tool, not an engagement. Every taxpayer's situation is different, and the rules in the skill may not match your specific facts.

To speak with one of the licensed accountants who verifies skills for your jurisdiction — no liability on either side until you and the accountant sign a formal engagement letter — book a free 30-minute call:

→ [Book a call](https://calendly.com/openaccountants-info/30min)

We'll route you to the named verifier covering your country or state. You can also see the full list of verified accountants at [openaccountants.com/network](https://openaccountants.com/network).

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
