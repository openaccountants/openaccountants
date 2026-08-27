---
name: france-bookkeeping
description: Use this skill whenever asked about bookkeeping, chart of accounts, Plan Comptable Général (PCG), financial statements, P&L format, balance sheet layout, bank reconciliation, expense classification, asset capitalisation, or day-to-day accounting for a French entity. Trigger on phrases like "PCG", "Plan Comptable", "chart of accounts France", "bilan", "compte de résultat", "micro-entreprise accounting", "régime réel simplifié", "capitalise or expense France", "amortissement", "depreciation France", "bank reconciliation France", "bookkeeping France", or any question about recording transactions, classifying expenses, or preparing accounts under French law. ALWAYS read this skill before touching any bookkeeping work for France.
version: 1.0
jurisdiction: FR
tax_year: 2025
last_updated: 2026-07-13
review_status: pending_review
depends_on:
  - bookkeeping-workflow-base
category: bookkeeping
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# France Bookkeeping

## Section 1 -- Quick Reference

**Quick Reference**

| Field | Value |
| --- | --- |
| Country | France (République française) |
| Currency | EUR |
| Financial year | Typically calendar year (1 Jan -- 31 Dec); companies may choose any 12-month period |
| Accounting standards | PCG (Plan Comptable Général) — ANC Regulation 2014-03, reformed effective 1 Jan 2025 |
| Governing body | ANC (Autorité des Normes Comptables); DGFiP (Direction Générale des Finances Publiques) |
| Key legislation | Code de Commerce (Art. L123-12 to L123-28); Code Général des Impôts (CGI); PCG (ANC 2014-03 as amended by ANC 2022-06) |
| Standard chart of accounts | PCG — mandatory structure with 7 classes of accounts; ~1,600 accounts (simplified from 2,000+ since 2025 reform) |
| Record retention | 10 years for accounting records (Code de Commerce L123-22) |

## Section 2 -- Standard Chart of Accounts (PCG 2025)

The PCG mandates a hierarchical account structure. Accounts in bold are mandatory; accounts in italics are optional. All French entities subject to the PCG must use this structure.

### Classe 1: Comptes de Capitaux (Equity & Long-Term Financing)

**Classe 1: Comptes de Capitaux (Equity & Long-Term Financing)**

| Code | Account | Notes |
| --- | --- | --- |
| 101 | Capital social | Share capital |
| 106 | Réserves | Legal reserve (5% of profit until 10% of capital) |
| 108 | Compte de l'exploitant | Owner's equity (sole traders) |
| 110 | Report à nouveau — créditeur | Retained earnings (credit) |
| 119 | Report à nouveau — débiteur | Accumulated losses |
| 120 | Résultat de l'exercice — bénéfice | Current year profit |
| 129 | Résultat de l'exercice — perte | Current year loss |
| 131 | Subventions d'investissement | Investment grants |
| 151 | Provisions pour risques | Provisions for risks |
| 164 | Emprunts auprès des établissements de crédit | Bank loans |

### Classe 2: Comptes d'Immobilisations (Non-Current Assets)

**Classe 2: Comptes d'Immobilisations (Non-Current Assets)**

| Code | Account | Notes |
| --- | --- | --- |
| 201 | Frais d'établissement | Formation costs (may capitalise or expense) |
| 205 | Concessions, brevets, licences | Software licences, patents |
| 2183 | Matériel de bureau et matériel informatique | Office and computer equipment |
| 2184 | Mobilier | Furniture |
| 213 | Constructions | Buildings |
| 2154 | Matériel industriel | Industrial machinery |
| 2182 | Matériel de transport | Vehicles |
| 2181 | Installations générales, agencements | Leasehold improvements, general installations |
| 28xx | Amortissements des immobilisations | Accumulated depreciation (contra-asset) |
| 29xx | Dépréciations des immobilisations | Impairment provisions |

### Classe 3: Comptes de Stocks et En-Cours (Inventories)

**Classe 3: Comptes de Stocks et En-Cours (Inventories)**

| Code | Account | Notes |
| --- | --- | --- |
| 31 | Matières premières | Raw materials |
| 35 | Stocks de produits | Finished goods |
| 37 | Stocks de marchandises | Merchandise for resale |
| 39xx | Dépréciations des stocks | Stock provisions |

### Classe 4: Comptes de Tiers (Receivables & Payables)

**Classe 4: Comptes de Tiers (Receivables & Payables)**

| Code | Account | Notes |
| --- | --- | --- |
| 401 | Fournisseurs | Trade payables |
| 411 | Clients | Trade receivables |
| 421 | Personnel — rémunérations dues | Salaries payable |
| 43 | Sécurité sociale et organismes sociaux | Social security liabilities |
| 44551 | TVA à décaisser | VAT payable |
| 44562 | TVA déductible sur immobilisations | Input VAT on capital assets |
| 44566 | TVA déductible sur autres biens et services | Input VAT on expenses |
| 44571 | TVA collectée | Output VAT collected |
| 455 | Associés — comptes courants | Directors' loan accounts |
| 467 | Autres comptes débiteurs ou créditeurs | Sundry debtors/creditors |

### Classe 5: Comptes Financiers (Cash & Financial Instruments)

**Classe 5: Comptes Financiers (Cash & Financial Instruments)**

| Code | Account | Notes |
| --- | --- | --- |
| 512 | Banques | Bank accounts |
| 514 | Chèques postaux | Postal cheque accounts (La Banque Postale) |
| 53 | Caisse | Cash in hand |
| 58 | Virements internes | Internal transfers (clearing) |

### Classe 6: Comptes de Charges (Expenses)

**Classe 6: Comptes de Charges (Expenses)**

| Code | Account | Notes |
| --- | --- | --- |
| 601 | Achats de matières premières | Raw materials purchases |
| 607 | Achats de marchandises | Merchandise purchases |
| 6061 | Fournitures non stockables (eau, énergie) | Utilities |
| 6063 | Fournitures d'entretien et petit équipement | Supplies and small equipment |
| 6064 | Fournitures administratives | Office supplies |
| 611 | Sous-traitance générale | Subcontracting |
| 613 | Locations | Rent |
| 6155 | Entretien et réparations | Repairs and maintenance |
| 616 | Primes d'assurance | Insurance premiums |
| 6226 | Honoraires | Professional fees (accountant, lawyer) |
| 6231 | Publicité, publications | Advertising |
| 6251 | Voyages et déplacements | Travel |
| 6256 | Missions | Business trips |
| 6257 | Réceptions | Entertainment / hospitality |
| 626 | Frais postaux et télécommunications | Postage and telecoms |
| 627 | Services bancaires | Bank charges |
| 631 | Impôts, taxes et versements assimilés | Taxes (non-income) — CFE, CVAE |
| 641 | Rémunérations du personnel | Salaries |
| 645 | Charges de sécurité sociale | Employer social charges |
| 6511 | Redevances pour concessions, brevets | Royalties |
| 6611 | Intérêts des emprunts et dettes | Loan interest |
| 6712 | Pénalités, amendes fiscales | Penalties — NOT deductible |
| 681 | Dotations aux amortissements et provisions (exploitation) | Depreciation charge |

### Classe 7: Comptes de Produits (Revenue)

**Classe 7: Comptes de Produits (Revenue)**

| Code | Account | Notes |
| --- | --- | --- |
| 701 | Ventes de produits finis | Sales of finished goods |
| 706 | Prestations de services | Service revenue |
| 707 | Ventes de marchandises | Merchandise sales |
| 708 | Produits des activités annexes | Ancillary revenue |
| 7411 | Subventions d'exploitation | Operating grants |
| 76 | Produits financiers | Financial income (interest) |
| 77 | Produits exceptionnels | Exceptional income (asset disposals) |

## Section 3 -- Revenue Recognition

**Revenue Recognition Scenarios**

| Scenario | Treatment |
| --- | --- |
| **Default (PCG)** | Accruals basis — revenue recognised when goods delivered or service performed |
| **Micro-entreprise (micro-BIC/BNC)** | No real revenue recognition — flat-rate deduction on turnover; simplified cash-basis bookkeeping |
| **Régime réel simplifié** | Accruals basis with simplified filing (annual TVA, simplified liasse fiscale) |
| **Régime réel normal** | Full accruals basis with monthly TVA declarations |
| **Construction contracts** | Percentage-of-completion (avancement) or completed-contract (achèvement), per PCG Art. 622-2 |
| **Advance payments** | Credit to 4191 (Clients — avances et acomptes reçus) until performance delivered |

### Turnover Thresholds (2025)

**Turnover Thresholds (2025)**

| Regime | Ventes (goods/accommodation) | Services (BIC) | BNC (professions libérales) |
| --- | --- | --- | --- |
| Micro-entreprise | ≤ EUR 188,700 | ≤ EUR 77,700 | ≤ EUR 77,700 |
| Réel simplifié | EUR 188,701 -- 876,000 | EUR 77,701 -- 264,000 | N/A |
| Réel normal | > EUR 876,000 | > EUR 264,000 | N/A |

- **Micro threshold exceeded 2 years** — Exceeding the micro threshold for 2 consecutive years triggers move to réel simplifié.

## Section 4 -- Expense Classification

**Expense Classification**

| Expense Type | PCG Code | Tax Deductibility | Notes |
| --- | --- | --- | --- |
| Rent (professional premises) | 613 | Fully deductible |  |
| Utilities | 6061 | Fully deductible (business premises); apportion if home |  |
| Professional fees | 6226 | Fully deductible |  |
| Insurance | 616 | Fully deductible | Business insurance only |
| Advertising | 6231 | Fully deductible |  |
| Travel | 6251 | Fully deductible | Business purpose; per-diem rates per barème fiscal |
| Entertainment (réceptions) | 6257 | Deductible if reasonable and documented | No blanket block as in Malta, but must be justified |
| Office supplies | 6064 | Fully deductible |  |
| Telecoms | 626 | Business portion deductible | Apportion if mixed |
| Bank charges | 627 | Fully deductible |  |
| Loan interest | 6611 | Deductible (subject to thin-cap rules for companies) |  |
| Penalties and fines | 6712 | NOT deductible for tax |  |
| Depreciation | 681 | Deductible per fiscal rules | May differ from accounting depreciation |
| Gifts to clients | 6234 | Deductible if reasonable; TVA not recoverable if > EUR 73 per recipient per year |  |
| CSG/CRDS (non-deductible portion) | 637 | Partially non-deductible | CSG déductible: 6.8%; CSG non-déductible: 2.4% + CRDS 0.5% |

## Section 5 -- Asset vs Expense Thresholds

### Capitalisation Threshold

**Capitalisation Threshold**

| Rule | Amount | Treatment |
| --- | --- | --- |
| **Fiscal tolerance (biens de faible valeur)** | ≤ EUR 500 HT per item | May be expensed directly (small equipment, office supplies, tools, software) |
| **PCG accounting rule** | No formal minimum — capitalise if future economic benefit > 1 year | Accounting judgement applies |
| **Above EUR 500 HT** | Must capitalise and depreciate | Immobilisation accounts (Classe 2) |

- **EUR 500 HT tolerance scope** — The EUR 500 HT tolerance applies only to: small tools, small office equipment, small furniture, and standard software. Other assets (even under EUR 500) must be capitalised if they have a useful life > 1 year.

### Standard Depreciation Rates (Amortissement Linéaire)

**Standard Depreciation Rates (Amortissement Linéaire)**

| Asset Category | Useful Life | Annual Rate | Notes |
| --- | --- | --- | --- |
| Commercial buildings | 20--50 years | 2--5% | Depending on type |
| Leasehold improvements | Lease term or 10 years | 10% typical |  |
| Industrial machinery | 5--10 years | 10--20% |  |
| Motor vehicles | 4--5 years | 20--25% |  |
| Computer hardware | 3 years | 33% |  |
| Computer software | 1--3 years | 33--100% | Internally developed: 3 years |
| Office furniture | 10 years | 10% |  |
| Office equipment | 5--10 years | 10--20% |  |

### Declining Balance (Amortissement Dégressif)

Available for new assets with useful life ≥ 3 years (not buildings, vehicles, or furniture). Coefficients applied to straight-line rate:

**Declining Balance Coefficients**

| Useful Life | Coefficient |
| --- | --- |
| 3--4 years | 1.25 |
| 5--6 years | 1.75 |
| ≥ 7 years | 2.25 |

## Section 6 -- P&L Format (Compte de Résultat)

Since 2025, the PCG prescribes a single format — a vertical (en liste) income statement:

```
COMPTE DE RÉSULTAT
Exercice clos le [date]

PRODUITS D'EXPLOITATION
  Chiffre d'affaires net                                     xxx
  Production stockée (variation)                              xxx
  Production immobilisée                                      xxx
  Subventions d'exploitation                                  xxx
  Reprises sur provisions, transferts de charges              xxx
  Autres produits                                             xxx
                                                             -----
  TOTAL PRODUITS D'EXPLOITATION                               xxx

CHARGES D'EXPLOITATION
  Achats de marchandises / matières                          (xxx)
  Variation de stocks                                        (xxx)
  Autres achats et charges externes                          (xxx)
  Impôts, taxes et versements assimilés                      (xxx)
  Salaires et charges sociales                               (xxx)
  Dotations aux amortissements et provisions                 (xxx)
  Autres charges                                             (xxx)
                                                             -----
  TOTAL CHARGES D'EXPLOITATION                               (xxx)

  RÉSULTAT D'EXPLOITATION                                     xxx

PRODUITS FINANCIERS                                           xxx
CHARGES FINANCIÈRES                                          (xxx)
  RÉSULTAT FINANCIER                                          xxx

PRODUITS EXCEPTIONNELS                                        xxx
CHARGES EXCEPTIONNELLES                                      (xxx)
  RÉSULTAT EXCEPTIONNEL                                       xxx

Impôts sur les bénéfices                                     (xxx)
                                                             -----
RÉSULTAT NET                                                  xxx
```

The 2025 reform replaced the former "système de base", "système abrégé", and "système développé" with a single unified format. Mandatory accounts are in bold in the PCG; optional accounts may be added for detail.

## Section 7 -- Balance Sheet Format (Bilan)

**Balance Sheet Format (Bilan)**

| Net             xxx | PROVISIONS                    xxx |
| --- | --- |
| xxx | DETTES |
| Emprunts et dettes          xxx |  |
| ACTIF CIRCULANT | Fournisseurs                xxx |
| Stocks            xxx | Dettes fiscales et sociales xxx |
| Créances          xxx | Autres dettes               xxx |
| Disponibilités    xxx | ----- |
| ----- | xxx |
| xxx |  |
| PRODUITS CONSTATÉS D'AVANCE   xxx |  |
| CHARGES CONSTATÉES D'AVANCE  xxx |  |
| ----- | ----- |
| TOTAL ACTIF         xxx | TOTAL PASSIF                  xxx |

## Section 7 -- Balance Sheet Format (Bilan)

The PCG prescribes a tabular (horizontal) balance sheet with assets on the left and equity/liabilities on the right. Since 2025, a single format applies — bilan en tableau avant répartition:

## Section 8 -- Bank Reconciliation Patterns

### French Bank Statement Formats

**French Bank Statement Formats**

| Bank | Format | Standard | Key Fields |
| --- | --- | --- | --- |
| BNP Paribas | QIF, CSV, OFX | CFONB/SEPA | Date, Libellé, Débit, Crédit, Solde |
| Crédit Agricole | CSV, OFX | CFONB | Date opération, Date valeur, Libellé, Montant |
| Société Générale | CSV, QIF | CFONB | Date, Libellé, Montant, Devise |
| La Banque Postale | CSV, PDF | CFONB | Date, Nature, Libellé, Débit, Crédit |
| Crédit Mutuel / CIC | CSV, OFX | CFONB | Date, Libellé, Débit, Crédit |
| Qonto / Shine (néobanques) | CSV, API | Proprietary | Date, Tiers, Catégorie, Montant |

### Common French Transaction Descriptions

**Common French Transaction Descriptions**

| Pattern | Likely Classification |
| --- | --- |
| VIR / VIREMENT | Bank transfer — check if income or expense |
| PRLV / PRELEVEMENT | Direct debit — utility, insurance, social charges |
| CB / CARTE | Card payment — check merchant name |
| CHQ / CHEQUE | Cheque payment |
| REM CHQ | Cheque deposit — potential income |
| COTISATION | Social security contribution (645) |
| URSSAF | Social charges — employer/self-employed (645) |
| TRESOR PUBLIC / DGFIP | Tax payment (IS, TVA, CFE) |
| LOYER | Rent payment (613) |
| ECHEANCE PRET | Loan repayment — split principal (164) and interest (6611) |

## Section 9 -- Micro-Entity / Small Business Simplifications

### Size Categories (Code de Commerce)

**Size Categories (Code de Commerce)**

| Criterion | Micro-entreprise (fiscal) | Petite entreprise | Moyenne entreprise |
| --- | --- | --- | --- |
| Revenue | ≤ EUR 77,700 (services) / 188,700 (goods) | ≤ EUR 12,000,000 | ≤ EUR 50,000,000 |
| Balance sheet total | N/A | ≤ EUR 6,000,000 | ≤ EUR 25,000,000 |
| Employees | N/A | ≤ 50 | ≤ 250 |

### Simplifications by Regime

**Simplifications by Regime**

| Requirement | Micro-entreprise | Réel simplifié | Réel normal |
| --- | --- | --- | --- |
| Bookkeeping | Cash receipts/payments journal only; no double-entry required | Full double-entry; simplified liasse | Full double-entry |
| Financial statements | None required | Simplified bilan + compte de résultat | Full bilan + compte de résultat + annexe |
| TVA | Franchise en base (no TVA charged, no returns) | Annual TVA + 2 interim payments | Monthly TVA declarations |
| Income tax | Flat-rate deduction on turnover (micro-BIC: 71% goods / 50% services; micro-BNC: 34%) | Actual expenses deducted | Actual expenses deducted |
| Liasse fiscale | Not required | Simplified (2033 series) | Full (2050 series) |
| Annexe comptable | Not required | Simplified | Full |

### TVA Franchise en Base Thresholds (2025)

**TVA Franchise en Base Thresholds (2025)**

| Activity | Basic threshold | Enhanced threshold |
| --- | --- | --- |
| Goods / accommodation | EUR 91,900 | EUR 101,000 |
| Services | EUR 36,800 | EUR 39,100 |

- **TVA franchise transition rule** — Below basic threshold: TVA franchise. Between basic and enhanced: TVA franchise maintained unless exceeded in prior year. Above enhanced: immediate TVA registration.

## Section 10 -- Interaction with Tax Skills

**Interaction with Tax Skills**

| Tax Skill | How Bookkeeping Connects |
| --- | --- |
| **france-income-tax** | Résultat comptable from the compte de résultat is the starting point for the liasse fiscale. Non-deductible items (fines in 6712, excess depreciation, non-deductible CSG/CRDS) are added back on tableau 2058-A. |
| **france-vat-return** | TVA accounts (44551, 44562, 44566, 44571) feed the CA3 or CA12 return. Net TVA payable = 44571 - (44562 + 44566). Reconcile monthly (réel normal) or annually (réel simplifié). |
| **france-social-charges** | Employer social charges in account 645 and CSG/CRDS computations. Cotisations URSSAF, retraite complémentaire, prévoyance. Self-employed: cotisations SSI based on bénéfice net. |
| **france-cfe-cvae** | CFE (Cotisation Foncière des Entreprises) and CVAE (Cotisation sur la Valeur Ajoutée) recorded in account 631. CVAE applies if revenue > EUR 152,500. |

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as an expert-comptable) before filing or acting upon.

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
