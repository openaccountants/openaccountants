---
name: france-financial-statements
description: Use this skill when preparing, reviewing, or advising on annual financial statements (comptes annuels) for a French company. Trigger on phrases like "comptes annuels", "dépôt des comptes", "greffe", "Plan Comptable Général", "PCG", "bilan", "compte de résultat", "annexe", "commissaire aux comptes", "audit France", "petite entreprise", "micro-entreprise comptable", "liasse fiscale", or any question about preparing and filing statutory accounts under French commercial law. Covers PCG framework, size thresholds, required statements, formats, notes, filing deadlines, and audit requirements.
version: 1.0
jurisdiction: FR
tax_year: 2025
last_updated: 2026-07-13
review_status: pending_review
depends_on:
  - financial-statements-workflow-base
category: financial-statements
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# France Financial Statements

## Section 1 -- Quick Reference

**Quick Reference**

| Field | Value |
| --- | --- |
| Country | France (République française) |
| Currency | EUR |
| Filing authority | Greffe du Tribunal de Commerce (via Guichet Unique / Infogreffe) |
| Primary legislation | Code de Commerce, Articles L123-12 to L123-28 |
| Supporting legislation | Décret n° 2024-152 (size thresholds); Règlement ANC 2014-03 (PCG) |
| Accounting standards | Plan Comptable Général (PCG) — ANC Regulation 2014-03 |
| Financial year | Any 12-month period (calendar year most common) |
| Filing deadline | 1 month after AGM approval (2 months if electronic filing) |
| AGM deadline | Within 6 months from year-end |
| Late filing penalty | EUR 1,500 (individual); EUR 7,500 (company); possible criminal sanctions |
| Digital filing | Electronic via Guichet Unique or Infogreffe |

## Section 2 -- Reporting Framework

**Reporting Framework**

| Entity type | Applicable standard |
| --- | --- |
| All commercial companies | PCG (Règlement ANC 2014-03) |
| Micro-entreprises (accounting) | Simplified PCG with no annexe required |
| Petites entreprises | PCG with simplified annexe and presentation |
| Listed groups (consolidated) | IFRS as adopted by the EU (mandatory) |
| Non-listed groups (consolidated) | PCG or IFRS (choice) |

- **PCG as sole framework for individual accounts** — The PCG is the sole framework for individual statutory accounts in France. IFRS cannot be used for individual company accounts filed with the greffe.

## Section 3 -- Size Thresholds

Effective for financial years beginning on or after 1 January 2024 (Décret 2024-152):

**Size Thresholds**

| Criterion | Micro | Petite (Small) | Moyenne (Medium) | Grande (Large) |
| --- | --- | --- | --- | --- |
| Total du bilan (Balance sheet) | ≤ EUR 450,000 | ≤ EUR 7,500,000 | ≤ EUR 25,000,000 | > EUR 25,000,000 |
| Chiffre d'affaires net (Turnover) | ≤ EUR 900,000 | ≤ EUR 15,000,000 | ≤ EUR 50,000,000 | > EUR 50,000,000 |
| Nombre moyen de salariés (Employees) | ≤ 10 | ≤ 50 | ≤ 250 | > 250 |

- **Threshold exceedance test** — Must not exceed 2 out of 3 thresholds. Assessment based on the balance sheet date of the most recently closed financial year.

## Section 4 -- Required Financial Statements

**Required Financial Statements**

| Document | Micro | Petite | Moyenne/Grande |
| --- | --- | --- | --- |
| Bilan (Balance sheet) | Required (simplified) | Required (simplified option) | Required (full) |
| Compte de résultat (P&L) | Required (simplified) | Required (simplified option) | Required (full) |
| Annexe (Notes) | Not required | Required (simplified) | Required (full) |
| Tableau de flux de trésorerie (Cash flow) | Not required | Not required | Recommended (consolidated: required) |
| Rapport de gestion (Management report) | Not required (small SARL) | Required | Required |
| Rapport du CAC (Auditor's report) | If CAC appointed | If CAC appointed | Required |

## Section 5 -- Year-End Adjustments Checklist

**Year-End Adjustments Checklist**

| # | Adjustment | France-specific notes |
| --- | --- | --- |
| 1 | Amortissements (Depreciation) | Linear or dégressif (declining balance with fiscal coefficient); component approach |
| 2 | Provisions pour charges | Règlement ANC: obligation probable, amount reliably estimable |
| 3 | Charges constatées d'avance (Prepayments) | Strict matching principle |
| 4 | Produits constatés d'avance (Deferred income) | Revenue received but not yet earned |
| 5 | Provision pour créances douteuses (Bad debts) | Individual assessment; VAT on doubtful debts reversed |
| 6 | Stocks et en-cours (Inventory) | Lower of cost (FIFO/CUMP) and realisable value |
| 7 | Impôts différés | Not recognised in individual accounts under PCG (consolidated only) |
| 8 | Écarts de conversion (FX differences) | Unrealised losses provisioned (principe de prudence); gains reported but provisioned |
| 9 | Participation des salariés | Mandatory profit-sharing provision (entreprises ≥ 50 employees) |
| 10 | Congés payés (Holiday pay) | Provision for untaken leave + social charges |
| 11 | Indemnités de départ (Retirement benefits) | Engagement or provision under PCG (recommendation ANC) |
| 12 | CET/CVAE provision | Cotisation sur la Valeur Ajoutée des Entreprises |

## Section 6 -- Compte de Résultat Format (P&L)

PCG format — système de base (by nature):

```
PRODUITS D'EXPLOITATION (Operating income)
  Ventes de marchandises
  Production vendue (biens et services)
  Production stockée
  Production immobilisée
  Subventions d'exploitation
  Reprises sur provisions et amortissements
  Autres produits

CHARGES D'EXPLOITATION (Operating expenses)
  Achats de marchandises
  Variation de stocks de marchandises
  Achats de matières premières
  Variation de stocks de matières premières
  Autres achats et charges externes
  Impôts, taxes et versements assimilés
  Salaires et traitements
  Charges sociales
  Dotations aux amortissements
  Dotations aux provisions
  Autres charges

  ─── RÉSULTAT D'EXPLOITATION ───

PRODUITS FINANCIERS
  Produits de participations
  Produits des autres valeurs mobilières
  Autres intérêts et produits assimilés
  Reprises sur provisions financières
  Différences positives de change

CHARGES FINANCIÈRES
  Dotations aux amortissements et provisions financières
  Intérêts et charges assimilées
  Différences négatives de change

  ─── RÉSULTAT FINANCIER ───

PRODUITS EXCEPTIONNELS
CHARGES EXCEPTIONNELLES

  ─── RÉSULTAT EXCEPTIONNEL ───

Participation des salariés
Impôt sur les bénéfices
  ─── RÉSULTAT NET ───
```

## Section 7 -- Bilan Format (Balance Sheet)

PCG format — système de base:

```
ACTIF

Actif immobilisé (Fixed assets)
  Immobilisations incorporelles
    Frais d'établissement
    Frais de recherche et développement
    Concessions, brevets, licences
    Fonds commercial
  Immobilisations corporelles
    Terrains
    Constructions
    Installations techniques, matériel
    Autres immobilisations corporelles
    Immobilisations en cours
  Immobilisations financières
    Participations
    Créances rattachées à des participations
    Autres titres immobilisés
    Prêts

Actif circulant (Current assets)
  Stocks et en-cours
  Avances et acomptes versés
  Créances clients et comptes rattachés
  Autres créances
  Valeurs mobilières de placement
  Disponibilités

Comptes de régularisation
  Charges constatées d'avance

─────────────────────────────────────

PASSIF

Capitaux propres (Equity)
  Capital social
  Primes d'émission
  Réserves (légale, statutaires, autres)
  Report à nouveau
  Résultat de l'exercice
  Provisions réglementées

Provisions pour risques et charges

Dettes (Liabilities)
  Emprunts et dettes auprès des établissements de crédit
  Emprunts obligataires
  Avances et acomptes reçus
  Dettes fournisseurs et comptes rattachés
  Dettes fiscales et sociales
  Autres dettes

Comptes de régularisation
  Produits constatés d'avance
```

## Section 8 -- Notes to Accounts (Annexe)

**Notes to Accounts (Annexe)**

| # | Disclosure | Micro | Petite | Moyenne/Grande |
| --- | --- | --- | --- | --- |
| 1 | Accounting policies (méthodes) | Exempt | Required | Required |
| 2 | Fixed asset movements | Exempt | Simplified | Required |
| 3 | Maturity of receivables/payables | Exempt | Required | Required |
| 4 | Related party transactions | Exempt | Significant only | Required |
| 5 | Off-balance commitments (engagements) | Exempt | Required | Required |
| 6 | Employee information | Exempt | Average headcount | Detailed |
| 7 | Directors' remuneration | Exempt | Not required (SARL <) | Required (SA) |
| 8 | Tax position | Exempt | Simplified | Required |
| 9 | Provisions detail | Exempt | Required | Required |
| 10 | Financial instruments | Exempt | If applicable | Required |
| 11 | Equity movements | Exempt | Not required | Required |
| 12 | Consolidation scope (if parent) | N/A | If applicable | Required |

## Section 9 -- Filing Requirements

**Filing Requirements**

| Item | Detail |
| --- | --- |
| Filing authority | Greffe du Tribunal de Commerce |
| Filing method | Electronic (Guichet Unique / Infogreffe) or paper deposit at greffe |
| AGM approval deadline | Within 6 months from financial year-end |
| Filing deadline | 1 month after AGM (paper) or 2 months after AGM (electronic) |
| Maximum time from year-end to filing | Approximately 7–8 months |
| Filing fee | Approximately EUR 45–65 (varies by greffe) |
| Confidentiality option — Micro | Can declare total confidentiality (accounts not publicly accessible) |
| Confidentiality option — Petite | Can declare confidentiality of compte de résultat only |
| Confidentiality option — Moyenne | No confidentiality |
| Language | French |
| Format | PDF (each file ≤ 10 MB) |
| Late filing penalties | EUR 1,500 (person); EUR 7,500 (legal entity); potential injonction by tribunal |

## Section 10 -- Audit Requirements

### Mandatory appointment of Commissaire aux Comptes (CAC)

- **CAC appointment trigger** — A company must appoint a CAC when it exceeds 2 of 3 thresholds at the close of a financial year.

**CAC thresholds by entity type**

| Entity type | Balance sheet | Turnover (HT) | Employees |
| --- | --- | --- | --- |
| Independent companies (SARL, SAS, SA, etc.) | EUR 5,000,000 | EUR 10,000,000 | 50 |
| Controlled subsidiaries (significant) | EUR 2,500,000 | EUR 5,000,000 | 25 |
| Civil companies with economic activity | EUR 1,550,000 | EUR 3,100,000 | 50 |
| SA (Société Anonyme) | Always mandatory regardless of size | — | — |

### CAC mandate duration

- **Mandate duration** — 6 financial years (standard)
- **Mandate continuation despite threshold changes** — Current mandates continue until expiry even if thresholds increase

### Auditor qualification

- **Commissaire aux Comptes qualification** — Commissaire aux Comptes inscrit on the official list held by the Compagnie Nationale des Commissaires aux Comptes (CNCC) and registered with the Haut Conseil du Commissariat aux Comptes (H3C).

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional before filing or acting upon.

## Talk to a verified accountant

This skill is a tool, not an engagement. Every taxpayer's situation is
different, and the rules in the skill may not match your specific facts.

To speak with one of the licensed accountants who verifies skills for your
jurisdiction — no liability on either side until you and the accountant sign
a formal engagement letter — book a free 30-minute call:

→ [Book a call](https://calendly.com/openaccountants-info/30min)

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
