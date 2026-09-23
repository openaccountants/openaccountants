---
name: france-bookkeeping
description: Use this skill whenever asked about bookkeeping, chart of accounts, Plan Comptable Général (PCG), financial statements, P&L format, balance sheet layout, bank reconciliation, expense classification, asset capitalisation, or day-to-day accounting for a French entity. Trigger on phrases like "PCG", "Plan Comptable", "chart of accounts France", "bilan", "compte de résultat", "micro-entreprise accounting", "régime réel simplifié", "capitalise or expense France", "amortissement", "depreciation France", "bank reconciliation France", "bookkeeping France", or any question about recording transactions, classifying expenses, or preparing accounts under French law. ALWAYS read this skill before touching any bookkeeping work for France.
version: 1.0
jurisdiction: FR
tax_year: 2026
last_updated: 2026-09-23
review_status: pending_review
drafted_by: OpenAccountants
approved_by: pending
depends_on:
  - bookkeeping-workflow-base
category: bookkeeping
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Bookkeeping in France (Plan Comptable Général, books, records and retention)

Which books a French business must keep under each regime, the account structure of the Plan Comptable Général, how expenses and assets are classified, what an invoice must carry, what the accounting file handed to a tax inspector must contain, and how long everything is kept. Figures are for tax year 2026. Two sources are older on their face, the retention page checked on 1 July 2024 and the invoice page on 11 August 2026, and the tax doctrine used here carries version dates from 2012 to 2021 (depreciation rates 23 September 2013, low-value assets 1 March 2017, declining balance 12 September 2012, accounting file format 7 June 2017, accounting file production 15 December 2021).

## Section 1: Quick Reference

| Field | Value |
| --- | --- |
| Country | France (République française) |
| Currency | EUR |
| Financial year | A twelve month period. An inventory checks assets and liabilities at least every twelve months |
| Accounting standards | Plan Comptable Général, règlement 2014-03 of the Autorité des normes comptables, as modernised by règlement 2022-06 of 4 November 2022 for financial years beginning on or after 1 January 2025 |
| Governing bodies | Autorité des normes comptables; Direction générale des Finances publiques |
| Key legislation | Code de commerce articles L123-12 to L123-28; Code général des impôts; livre des procédures fiscales articles L. 47 A and A. 47 A-1 |
| Books, real regime | Livre-journal, grand-livre, manuel des procédures comptables |
| Books, micro-entrepreneur | Livre des recettes, plus a registre des achats for traders and accommodation providers |
| Record retention | Ten years from the close for the books and supporting documents; six years for the documents the tax administration may call for |
| Who may keep the books | The business itself, or an expert-comptable on the roll of the Ordre des experts-comptables |

## Which books each regime must keep

The bookkeeping duty follows the tax regime, not the legal form. A trader is in the simplified real regime only if it meets every condition below at the same time, and in the normal real regime above any of them.

| Item | Value | Note |
| --- | --- | --- |
| Source | all figures below | https://entreprendre.service-public.fr/vosdroits/F21852 |
| Simplified real regime, turnover limit for selling, catering and accommodation | EUR 945,000 | "945 000 €" |
| Simplified real regime, turnover limit for other activities | EUR 286,000 | "286 000 €" |
| Simplified real regime, the VAT owed for the previous year must stay below | EUR 15,000 | "inférieur à 15 000 €" |
| Fine for not keeping the accounting documents for the required period | EUR 10,000 | "une amende de 10 000 €" |
| Fine for a deliberate omission in the invoicing, by inaccurate or fictitious entries, on top of five years' prison | EUR 500,000 | "500 000 € d'amende" |

All the conditions, not any one: a business inside both turnover limits but owing more VAT than the limit is in the normal real regime. The three books are a livre-journal recording every movement, a grand-livre gathering the accounts and classifying the journal entries by account in the order of the Plan Comptable Général, and a manuel des procédures comptables describing the organisation and the controls. Each book gets an identification number listed by a greffier and is coté et paraphé. Every entry states the origin, the content, the account and the reference of the supporting document. Books may be electronic or handwritten, without blanks or alteration, dated and recorded as soon as they are drawn up. In the simplified real regime the livre-journal records receipts and payments day by day, with receivables and payables taken up at the close, general expenses entered at regular dates at least yearly, and the entries centralised every three months. On top of that a sole trader may elect super-simplified accounting each year by ticking the box on results return 2031, which allows a simplified valuation of stocks and work in progress.

The micro-entrepreneur keeps registers, not double-entry books.

| Item | Value | Note |
| --- | --- | --- |
| Source | all figures below | https://entreprendre.service-public.fr/vosdroits/F23266 |
| Unit amount below which retail sales and services to individuals may be entered as one daily total | EUR 76 | "inférieur à 76 €" |
| Criminal fine for a forged register or its use, on top of three years' prison | EUR 45,000 | "45 000 € d'amende" |
| Penalty for each missing turnover declaration | EUR 60.1 | "une pénalité de 60,1 €" |
| Yearly turnover which, once passed in two consecutive years, forces an account dedicated to the activity | EUR 10,000 | "dépasse 10 000 €" |

- **Trader or accommodation provider.** A livre des recettes encaissées in date order, with the amount and origin of each receipt and the client's identity, the means of payment and the document reference, totalled every three months. Plus a registre des achats listing the year's purchases in date order with the means of payment and the document references.
- **Liberal profession.** The livre des recettes only, on the same terms. That page requires no registre des achats.
- **Under the VAT franchise there is more:** a yearly register detailing purchases of goods and services, a livre-journal showing professional receipts day by day, and the invoices kept.
- **Entries cannot be edited once recorded,** and the registers may be paper, official downloadable models or software, held electronically if wanted. The page says in terms there is no sanction for failing to keep them, but forgery and its use carry the prison term and the fine above.

## Section 2: Standard Chart of Accounts (Plan Comptable Général)

The class structure is the standard structure of the Plan Comptable Général as the tax doctrine describes it: a decimal codification in nine classes, classes 1 to 5 for the balance sheet, 6 and 7 for the result, 8 for the special accounts used for information duties such as the annexe (80 commitments, 88 result awaiting appropriation, 89 balance sheet), class 0 left available. It applies to every industrial and commercial business and to anyone who must draw up a bilan, a compte de résultat and an annexe. Sector plans may adapt it. See https://bofip.impots.gouv.fr/bofip/3412-PGP.html

The account numbers below are OpenAccountants' own selection of the accounts a small French business uses most, not a reproduction of the standard. They were checked against the plan de comptes published by the Autorité des normes comptables in its version at the first of January 2026. The English labels are ours.

### Classe 1: Comptes de Capitaux (Equity & Long-Term Financing)

| Code | Account |
| --- | --- |
| 101 | Capital |
| 106 | Réserves, including the legal reserve (see `france-financial-statements`) |
| 108 | Compte de l'exploitant: owner's equity, sole traders |
| 110 | Report à nouveau créditeur: retained earnings |
| 119 | Report à nouveau débiteur: accumulated losses |
| 120 | Résultat de l'exercice, bénéfice |
| 129 | Résultat de l'exercice, perte |
| 131 | Subventions d'investissement |
| 151 | Provisions pour risques |
| 164 | Emprunts auprès des établissements de crédit |

### Classe 2: Comptes d'Immobilisations (Non-Current Assets)

| Code | Account |
| --- | --- |
| 201 | Frais d'établissement |
| 205 | Concessions, brevets, licences |
| 207 | Fonds commercial: goodwill |
| 213 | Constructions |
| 2154 | Matériel industriel |
| 2155 | Outillage industriel |
| 2181 | Installations générales, agencements |
| 2182 | Matériel de transport |
| 2183 | Matériel de bureau et matériel informatique |
| 2184 | Mobilier |
| 28 | Amortissements des immobilisations |
| 29 | Dépréciations des immobilisations |

### Classe 3: Comptes de Stocks et En-Cours (Inventories)

| Code | Account |
| --- | --- |
| 31 | Matières premières |
| 35 | Stocks de produits |
| 37 | Stocks de marchandises |
| 39 | Dépréciations des stocks |

### Classe 4: Comptes de Tiers (Receivables & Payables)

| Code | Account |
| --- | --- |
| 401 | Fournisseurs |
| 411 | Clients |
| 4191 | Clients, avances et acomptes reçus |
| 421 | Personnel, rémunérations dues |
| 43 | Sécurité sociale et organismes sociaux |
| 44551 | TVA à décaisser: VAT payable |
| 44562 | TVA déductible sur immobilisations |
| 44566 | TVA déductible sur autres biens et services |
| 44571 | TVA collectée: output VAT |
| 455 | Associés, comptes courants |
| 467 | Autres comptes débiteurs ou créditeurs |

### Classe 5: Comptes Financiers (Cash & Financial Instruments)

| Code | Account |
| --- | --- |
| 512 | Banques |
| 53 | Caisse |
| 58 | Virements internes |

### Classe 6: Comptes de Charges (Expenses)

| Code | Account |
| --- | --- |
| 601 | Achats de matières premières |
| 6061 | Fournitures non stockables: water, energy |
| 6063 | Fournitures d'entretien et petit équipement |
| 6064 | Fournitures administratives |
| 607 | Achats de marchandises |
| 611 | Sous-traitance générale |
| 613 | Locations |
| 6155 | Entretien et réparations |
| 616 | Primes d'assurance |
| 6226 | Honoraires |
| 623 | Publicité, publications, relations publiques, including 6231 Annonces et insertions |
| 6234 | Cadeaux à la clientèle |
| 6251 | Voyages et déplacements |
| 6256 | Missions |
| 6257 | Réceptions |
| 626 | Frais postaux et télécommunications |
| 627 | Services bancaires |
| 635 | Autres impôts, taxes et versements assimilés, including 63511 Contribution économique territoriale |
| 641 | Rémunérations du personnel |
| 645 | Charges de sécurité sociale |
| 657 | Valeurs comptables des immobilisations incorporelles et corporelles cédées |
| 6582 | Pénalités, amendes fiscales et pénales, inside 658 Pénalités et autres charges |
| 6611 | Intérêts des emprunts et dettes |
| 681 | Dotations aux amortissements et provisions |

### Classe 7: Comptes de Produits (Revenue)

| Code | Account |
| --- | --- |
| 701 | Ventes de produits finis |
| 706 | Prestations de services |
| 707 | Ventes de marchandises |
| 708 | Produits des activités annexes |
| 741 | Subventions d'exploitation, inside 74 Subventions |
| 757 | Produits des cessions d'immobilisations incorporelles et corporelles |
| 758 | Indemnités et autres produits: 7581 dédits et pénalités, 7582 libéralités reçues, 7583 rentrées sur créances amorties |
| 76 | Produits financiers |
| 77 | Produits exceptionnels |

## Section 3: Revenue Recognition

| Scenario | Treatment |
| --- | --- |
| Default | Accruals. The livre-journal records every movement, and an inventory runs at least every twelve months |
| Micro-entreprise | Receipts basis. Receipts are entered when cashed, and the taxable profit is turnover less a flat-rate allowance |
| Régime réel simplifié | Accruals, with the super-simplified option: receipts and payments in the year, receivables and payables at the close |
| Régime réel normal | Full accruals, every movement day by day, operation by operation |
| Construction contracts | Avancement or achèvement, per PCG art. 622-2 |
| Advance payments | Credited to 4191 until the performance is delivered |

### Turnover Thresholds

France taxes the previous year's income, so the micro regime has two live sets of limits. Use the row matching the year of the income. A single year over a limit does not end the regime. The limit must have been passed in both of the two preceding years, N minus one and N minus two, before the income of year N leaves the micro regime.

| Item | Value | Note |
| --- | --- | --- |
| Source | all figures below | https://entreprendre.service-public.fr/vosdroits/F23267 |
| Micro limit, goods and accommodation other than furnished tourist lettings, income of 2025 declared in 2026 | EUR 188,700 | "188 700 €" |
| Micro limit, services, income of 2025 declared in 2026 | EUR 77,700 | "77 700 €" |
| Micro limit, goods and accommodation other than furnished tourist lettings, income received in 2026 | EUR 203,100 | "203 100 €" |
| Micro limit, services, income received in 2026 | EUR 83,600 | "83 600 €" |
| Flat-rate allowance, goods and accommodation other than furnished tourist lettings | 71% | "abattement est de 71 %" |
| Flat-rate allowance, services taxed as industrial and commercial profits | 50% | "50 %" |
| Flat-rate allowance, non-commercial profits | 34% | "34 %" |

Furnished tourist lettings are on their own limits and their own allowance. Use `fr-rental-income`.

The allowance replaces actual expenses, which is why registers replace double-entry books. These are not the bookkeeping limits: leaving the micro regime moves the business to a real regime, and which real regime is the separate test in the first table of this Guide.

## Section 4: Expense Classification

| Expense | Account | Note |
| --- | --- | --- |
| Rent of professional premises | 613 | |
| Utilities | 6061 | Apportion if the premises are also a home |
| Professional fees | 6226 | |
| Insurance | 616 | Business cover only |
| Advertising | 6231 for advertisements and insertions, 623 for the rest | |
| Travel | 6251 | Business purpose, supported by a document |
| Entertainment | 6257 | Must be justified |
| Office supplies | 6064 | |
| Telecoms | 626 | Apportion the business share if mixed |
| Bank charges | 627 | |
| Loan interest | 6611 | Interest limits for companies are not covered here |
| Penalties and tax fines | 6582 | Inside 658. In the operating result since the reform, then added back on the tax return |
| Depreciation | 681 | Tax rules may differ from the accounting charge. See Section 5 |
| Gifts to clients | 6234 | Input VAT is recoverable only on objects of very low value, the amount fixed by article 28-00 A of annexe IV to the CGI. See `france-vat-return` |
| Employer social charges | 645 | Rates are in `france-payroll` and `fr-social-contributions` |

## Section 5: Asset vs Expense Thresholds

### Capitalisation Threshold

| Item | Value | Note |
| --- | --- | --- |
| Source | all figures below | https://bofip.impots.gouv.fr/bofip/2109-PGP.html |
| Unit price excluding tax up to which materials and tooling may be deducted at once | EUR 500 | "n'excédant pas 500 €" |

The tolerance covers materials and tooling belonging in accounts 2154 and 2155, small office equipment, office and shop furniture, and software whose unit value excluding tax does not exceed it. It is a tax tolerance, not an accounting rule: the Plan Comptable Général sets no minimum, and an item with a useful life of more than one year is an asset. For office and shop furniture the tolerance holds only where the purchases of a given item in one financial year run to a small number of units, and it does not cover the initial furnishing of an office building, a restaurant or a shop, nor a complete renewal. Transport equipment is outside the tooling limb and is capitalised.

### Standard Depreciation Rates (Amortissement Linéaire)

Yearly straight-line rates, given "à titre purement indicatif" and printed without the percent sign, as "Maisons d'habitation ordinaires 1 à 2".

| Asset | Rate |
| --- | --- |
| Source | https://bofip.impots.gouv.fr/bofip/4520-PGP.html |
| Ordinary dwelling houses | 1% to 2% |
| Workers' houses | 3% to 4% |
| Commercial buildings | 2% to 5% |
| Industrial buildings, land excluded | 5% |
| Plant (matériel) | 10% to 15% |
| Tooling (outillage) | 10% to 20% |
| Office equipment | 10% to 20% |
| Motor vehicles | 20% to 25% |
| Furniture | 10% |
| Fittings and installations | 5% to 10% |
| Patents and plant variety certificates | 20% |

The list is indicative and is beaten by the trade's usages and the particular conditions of use. A shorter life may be used where the effective life will very probably be shorter than the normal life, and the business must then prove the abnormal depreciation. Patents bought in financial years beginning on or after 1 January 1988 may be written off over a minimum of five years. The legacy Guide printed rates for computer hardware and software: they are not in the doctrine's list, so none is stated here, and the asset's own useful life governs.

### Declining Balance (Amortissement Dégressif)

An asset qualifies only if it falls in the categories set by article 22 of annexe II to the CGI and by article 39 A of the CGI, was not already second hand when bought, and has a normal useful life of at least three years. See https://bofip.impots.gouv.fr/bofip/4684-PGP.html and https://bofip.impots.gouv.fr/bofip/4682-PGP.html

| Normal useful life | Coefficient |
| --- | --- |
| Source | https://bofip.impots.gouv.fr/bofip/4699-PGP.html |
| Three or four years | 1.25 |
| Five or six years | 1.75 |
| More than six years | 2.25 |

The rate is the straight-line rate for the normal useful life multiplied by the coefficient. The first charge runs from the first day of the month of acquisition or construction, reduced in proportion to the part of the financial year that follows. Once the declining charge for a year falls below the residual value divided by the years still to run, the business may take that larger figure instead. Certain equipment carries increased or reduced coefficients. Dwelling buildings, worksites and the premises used to carry on the profession are outside the method by their nature, while hotel investments, movable and immovable, are inside it. Assets already second hand when bought are excluded, with a tolerance for equipment rebuilt by the maker to near new specification. Where the accounting depreciation is straight line, the excess is recorded as amortissements dérogatoires.

## Section 6: P&L Format (Compte de Résultat)

The compte de résultat gathers the income and expenses of the year and shows the profit or loss after depreciation and provisions. Règlement 2022-06 of 4 November 2022 moved accounts that fed the exceptional result into the operating result, and binds financial years beginning on or after 1 January 2025. What stays in the exceptional result is income and expenses directly linked to a major and unusual event, entries of purely tax origin such as amortissements dérogatoires and provisions réglementées, a change of accounting method taken through profit because of a tax rule, and corrections of errors other than those taken straight to equity. An event is unusual when it is not tied to the entity's normal and current activity. An event is presumed unusual when it has not happened in recent years and is unlikely to happen again. See https://bofip.impots.gouv.fr/bofip/13223-PGP.html and https://entreprendre.service-public.fr/vosdroits/F21852

The layout below follows the système de base model of the Plan Comptable Général, article 821-2. See https://www.anc.gouv.fr/files/anc/files/1_Normes_fran%C3%A7aises/Plans%20comptables/2026/PCG--1er-janvier-2026.pdf A small business, and for the compte de résultat a medium one, may use a simplified presentation; a trader in the simplified real regime need not draw up the annexe.

~~~
COMPTE DE RÉSULTAT

PRODUITS D'EXPLOITATION
  Chiffre d'affaires net
  Production stockée (variation)
  Production immobilisée
  Subventions
  Reprises sur amortissements, dépréciations et provisions
  Produits des cessions d'immobilisations incorporelles et corporelles
  Autres produits
  TOTAL PRODUITS D'EXPLOITATION

CHARGES D'EXPLOITATION
  Achats de marchandises et de matières
  Variation de stocks
  Autres achats et charges externes
  Impôts, taxes et versements assimilés
  Salaires et charges sociales
  Dotations aux amortissements et provisions
  Valeurs comptables des immobilisations incorporelles et corporelles cédées
  Autres charges
  TOTAL CHARGES D'EXPLOITATION

  RÉSULTAT D'EXPLOITATION

Quote-part de résultat sur opérations faites en commun
  Bénéfice attribué ou perte transférée
  Perte supportée ou bénéfice transféré

PRODUITS FINANCIERS
CHARGES FINANCIÈRES
  RÉSULTAT FINANCIER
  RÉSULTAT COURANT AVANT IMPÔTS

PRODUITS EXCEPTIONNELS
CHARGES EXCEPTIONNELLES
  RÉSULTAT EXCEPTIONNEL

Participation des salariés
Impôts sur les bénéfices

  RÉSULTAT NET
~~~

## Section 7: Balance Sheet Format (Bilan)

The bilan shows the assets and liabilities and sets out the equity separately. The layout below follows the système de base model of the Plan Comptable Général, article 821-1. See https://www.anc.gouv.fr/files/anc/files/1_Normes_fran%C3%A7aises/Plans%20comptables/2026/PCG--1er-janvier-2026.pdf and https://entreprendre.service-public.fr/vosdroits/F21852

~~~
ACTIF

Actif immobilisé
  Immobilisations incorporelles
  Immobilisations corporelles
  Immobilisations financières

Actif circulant
  Stocks et en-cours
  Avances et acomptes versés
  Créances clients et comptes rattachés
  Autres créances
  Charges constatées d'avance
  Valeurs mobilières de placement
  Instruments financiers à terme et jetons détenus
  Disponibilités

Frais d'émission des emprunts
Primes de remboursement des emprunts

Écarts de conversion et différences d'évaluation - Actif

PASSIF

Capitaux propres
  Capital, primes d'émission, de fusion, d'apport, réserves
  Report à nouveau, résultat de l'exercice
  Subventions d'investissement
  Provisions réglementées

Autres fonds propres

Provisions pour risques et charges

Dettes
  Emprunts et dettes auprès des établissements de crédit
  Avances et acomptes reçus
  Dettes fournisseurs et comptes rattachés
  Dettes fiscales et sociales
  Autres dettes
  Produits constatés d'avance

Écarts de conversion et différences d'évaluation - Passif
~~~

## Section 8: Bank Reconciliation Patterns

Legacy reference content. No allowed page carries it: bank file layouts are a commercial matter for each bank, not a rule of French law. Confirm the columns against the file the client actually exports.

### French Bank Statement Formats

| Bank | Format | Key fields |
| --- | --- | --- |
| BNP Paribas | QIF, CSV, OFX | Date, Libellé, Débit, Crédit, Solde |
| Crédit Agricole | CSV, OFX | Date opération, Date valeur, Libellé, Montant |
| Société Générale | CSV, QIF | Date, Libellé, Montant, Devise |
| La Banque Postale | CSV, PDF | Date, Nature, Libellé, Débit, Crédit |
| Crédit Mutuel and CIC | CSV, OFX | Date, Libellé, Débit, Crédit |
| Qonto and Shine | CSV, bank feed | Date, Tiers, Catégorie, Montant |

### Common French Transaction Descriptions

| Pattern | Likely classification |
| --- | --- |
| VIR or VIREMENT | Bank transfer. Income or expense, check |
| PRLV or PRELEVEMENT | Direct debit: utility, insurance, social charges |
| CB or CARTE | Card payment. Check the merchant |
| CHQ or CHEQUE | Cheque payment |
| REM CHQ | Cheque deposit, likely income |
| COTISATION | Social contribution (645) |
| URSSAF | Social charges, employer or self-employed (645) |
| TRESOR PUBLIC or DGFIP | Tax payment: corporation tax, VAT, CFE |
| LOYER | Rent (613) |
| ECHEANCE PRET | Loan repayment. Split principal (164) from interest (6611) |

## Section 9: Micro-Entity / Small Business Simplifications

### Size Categories (Code de Commerce)

A business falls in an accounting size class when it meets two of the three criteria of that class: a balance sheet total, a net turnover excluding VAT and an average headcount. These classes are not the micro tax regime. The bookkeeping page carries the two classes that decide a simplified presentation.

| Item | Value | Note |
| --- | --- | --- |
| Source | all figures below | https://entreprendre.service-public.fr/vosdroits/F21852 |
| Petite entreprise, balance sheet total not more than | EUR 7,500,000 | "Bilan total inférieur ou égal à 7 500 000 €" |
| Petite entreprise, net turnover excluding VAT not more than | EUR 15,000,000 | "Montant net HT du chiffre d'affaires inférieur ou égal à 15 000 000 €" |
| Moyenne entreprise, balance sheet total not more than | EUR 25,000,000 | "Bilan total inférieur ou égal à 25 000 000 €" |
| Moyenne entreprise, net turnover excluding VAT not more than | EUR 50,000,000 | "Montant net HT du chiffre d'affaires inférieur ou égal à 50 000 000 €" |

The headcount tests are fifty employees on average for a petite entreprise and two hundred and fifty for a moyenne entreprise, and two of the three criteria decide the class. See https://entreprendre.service-public.fr/vosdroits/F21852 The full set of limits, including the accounting micro class, and what each class must produce and file, is in `france-financial-statements`.

### Simplifications by Regime

| Requirement | Micro-entreprise | Réel simplifié | Réel normal |
| --- | --- | --- | --- |
| Bookkeeping | Livre des recettes, plus a registre des achats for traders and accommodation providers. No double entry | Livre-journal, grand-livre, manuel des procédures, with the super-simplified option on election | Livre-journal, grand-livre, manuel des procédures. Every movement day by day |
| Centralisation | Not applicable | Every three months under the option | See `france-financial-statements` |
| Annual accounts | None | Bilan and compte de résultat, simplified presentation allowed, no annexe required | Bilan, compte de résultat and annexe |
| VAT | Franchise en base until the limits below | Annual CA12 return plus two instalments | CA3 return |
| Income tax | Flat-rate allowance on turnover, Section 3 | Actual expenses | Actual expenses |
| Tax return package | Not required | Return 2031 for a sole trader, or return 2065 for a company, with the 2033 series | Return 2031 or 2065 with the 2050 series |

### TVA Franchise en Base Thresholds

The single franchise threshold announced in the 2025 finance law was abandoned. These are the limits in force for 2026.

| Activity | Basic threshold | Tolerance threshold |
| --- | --- | --- |
| Source | all figures below | https://entreprendre.service-public.fr/vosdroits/F21746 |
| Goods and accommodation | EUR 85,000 | EUR 93,500 |
| Services | EUR 37,500 | EUR 41,250 |
| Lawyers' regulated work, authors' and performers' works and copyright | EUR 50,000 | EUR 55,000 |
| Their other activities | EUR 35,000 | EUR 38,500 |

The franchise applies where the previous calendar year's turnover was at or below the basic threshold, or where the current year's turnover is at or below the tolerance threshold. Passing the basic threshold brings VAT from the first day of January of the following year. Passing the tolerance threshold brings VAT from the first day of the overrun. An invoice issued under the franchise must state "TVA non applicable, art. 293 B du code général des impôts".

## VAT bookkeeping by regime

The simplified VAT regime starts at the franchise thresholds above and runs to the turnover limits in the first table of this Guide, with the same limit on the VAT owed. Above the tolerance turnover below, the business moves to the normal regime retroactively, from the first day of January of the year in which the turnover was passed, and files a CA3 for the whole of that period. Passing the ordinary turnover limit or the limit on the VAT owed instead moves it on the first day of January of the following year.

| Item | Value | Note |
| --- | --- | --- |
| Source | all figures below | https://entreprendre.service-public.fr/vosdroits/F23575 |
| Turnover above which the simplified regime is undone back to 1 January of that year, goods and accommodation | EUR 1,040,000 | "1 040 000 €" |
| Turnover above which the simplified regime is undone back to 1 January of that year, services | EUR 323,000 | "323 000 €" |

| Item | Value | Note |
| --- | --- | --- |
| Source | all figures below | https://entreprendre.service-public.fr/vosdroits/F23566 |
| July instalment, share of the VAT of the previous year | 55% | "55 %" |
| December instalment, share of the VAT of the previous year | 40% | "40 %" |
| VAT of the previous year below which no instalment is due | EUR 1,000 | "1 000 €" |

Output VAT sits in 44571, input VAT on expenses in 44566 and on capital assets in 44562, the balance payable in 44551. Reconcile them to the return every period and clear 44551 when the payment leaves the bank. The normal regime files a CA3 return, the simplified regime one annual CA12 return with the two instalments above; boxes and mechanics are in `france-vat-return`. A franchised business has no output VAT and nothing to reclaim, which is why its bookkeeping is a purchases register and a receipts journal rather than VAT accounts.

## Invoices: the particulars every invoice must carry

An invoice is valid only if it carries the compulsory particulars, whoever the client is. See https://entreprendre.service-public.fr/vosdroits/F31808

- Date of issue; a unique number from a chronological and continuous sequence; the date of the sale, of the end of the service, or of an instalment paid.
- Seller: for an individual business the name and first name with "Entrepreneur individuel" or "EI", the address and the Siren number; for a company the name, the Siren number, the registered office address, the legal form and the share capital.
- Buyer: the name, the address, the billing address if different, and the purchase order number where one was issued.
- Each product or service: nature, quantity, precise name, unit price excluding VAT and the VAT rate, or the exemption wording.
- The total excluding VAT and the total including VAT; any increase such as carriage or packing; any rebate or discount linked to the operation.
- The payment date, the early payment discount terms or the words that there are none, and the rate of late payment penalties.

| Item | Value | Note |
| --- | --- | --- |
| Source | all figures below | https://entreprendre.service-public.fr/vosdroits/F31808 |
| Total excluding VAT at or below which the VAT identification numbers need not appear | EUR 150 | "inférieur ou égal à 150 €" |
| Fixed recovery indemnity to be mentioned on an invoice between businesses | EUR 40 | "indemnité forfaitaire de 40 €" |

Four more particulars arrive with electronic invoicing: the client's Siren number when the client is a business, the delivery address when it differs, the nature of the operations (goods, services or both), and the wording for the option to pay the tax on the debits. Every business established in France and liable to VAT must be able to receive electronic invoices since 1 September 2026; issuing starts then for large and intermediate companies and on 1 September 2027 for small, medium and micro businesses. See `france-einvoice`. Special wordings cover membership of an approved management body, the VAT franchise, "Auto-liquidation" where the customer is liable for the VAT, the electrical waste contribution, the private copying levy, "Auto-facturation" where the client raises the invoice, and a craft business's professional insurance references.

## The fichier des écritures comptables

A business that keeps its books on a computer hands the inspector a copy of the accounting entries file at the start of a tax audit, in the format set by article A. 47 A-1 of the livre des procédures fiscales. It concerns taxpayers who keep computerised accounts, must hold and produce accounting documents under the CGI, and are audited: corporation tax payers, and income tax payers under a real regime for industrial and commercial, non-commercial or agricultural profits. A property company is released only where it is taxed exclusively on rental income and all of its members are individuals. Any other property company must produce the file. A micro-entrepreneur who keeps the registers on a computer is also released. See https://bofip.impots.gouv.fr/bofip/9026-PGP.html and https://bofip.impots.gouv.fr/bofip/9028-PGP.html

| # | Field | Note |
| --- | --- | --- |
| 1 | Code journal | The code referencing each journal in the software |
| 2 | Libellé journal | The journal's full name |
| 3 | Numéro d'écriture | One number per double-entry item, the same on each of its lines, rising in time without a gap |
| 4 | Date de comptabilisation | When the operation was posted |
| 5 | Numéro de compte | To the standard of the Plan Comptable Général, with the business's subdivisions |
| 6 | Libellé de compte | The account name |
| 7 | Numéro de compte auxiliaire | Third-party account coding. Blank if not used |
| 8 | Libellé de compte auxiliaire | The third party's name. Blank if not used |
| 9 | Référence de la pièce justificative | Reference of the document behind the entry |
| 10 | Date de la pièce justificative | The date on that document |
| 11 | Libellé de l'écriture | The literal reason for the entry |
| 12 | Montant au débit | A signed amount in euros |
| 13 | Montant au crédit | A signed amount in euros |
| 14 | Sens | Where a direction replaces debit and credit, only "D" and "C", or "+1" and "-1" |
| 15 | Lettrage | The mark matching two entries. Blank if not used |
| 16 | Date de lettrage | When the matching was validated. Blank if not used |
| 17 | Date de validation | When a draft entry became final by receiving a unique identifier. Equals the posting date where there is no draft mode |
| 18 | Montant en devise and identifiant de la devise | The foreign currency amount on the document, and the currency. Blank if not used |

Where the doctrine says "à blanc si non utilisé" the column must be present; the cell may be empty if the software does not hold the data, and must never be filled with a zero or with spaces. The débit and crédit columns are not among them: both must always carry a figure, and the side not used carries a zero. Two file shapes are accepted: a flat sequential file meeting the criteria of the article, or a structured file in the markup language whose schema is published at https://www.impots.gouv.fr/fichiers-standards-des-ecritures-comptables

| Item | Value | Note |
| --- | --- | --- |
| Source | all figures below | https://bofip.impots.gouv.fr/bofip/9026-PGP.html |
| Fine for not producing the accounting file in the required form | EUR 5,000 | "une amende égale à 5 000 €" |
| Increase of the duties charged, applied instead where an adjustment is made and it is higher | 10% | "majoration de 10 % des droits" |

## Record retention

Keep the accounting books and the supporting documents for ten years from the close. The tax documents the administration may call for are kept for six years, counted from the last operation entered in a book or register or from the date the document was drawn up, and the period rises to ten years where the activity is undeclared. See https://entreprendre.service-public.fr/vosdroits/F10029

| Document | Period | Counted from |
| --- | --- | --- |
| Livre-journal, grand-livre, livre d'inventaire and other books and registers | Ten years | The close of the financial year |
| Supporting documents: purchase orders, delivery notes, customer and supplier invoices | Ten years | The close of the financial year |
| Annual accounts: bilan, compte de résultat, annexe | Ten years | The close of the financial year |
| Tax documents for income tax, corporation tax, profits under a real regime, local business taxes and turnover taxes | Six years | The last operation entered, or the date the document was drawn up |
| Commercial contracts and correspondence, bank documents | Five years | |
| Customs declarations | Three years | |
| Contracts for the purchase or sale of land and buildings | Thirty years | |

The micro-entrepreneur is on the same ten years for the receipts book, the purchases register and the supporting documents. Not keeping the documents is fined: see the first table of this Guide.

## Section 10: How this Guide connects to the other France Guides

The close, the size classes, approval of the accounts, filing at the greffe, confidentiality, the penalties and the statutory auditor thresholds are all in `france-financial-statements`. This Guide stops at the books and the entries that feed them.

| Guide | How bookkeeping connects |
| --- | --- |
| `france-financial-statements` | The trial balance from the grand-livre produces the bilan and the compte de résultat, which start the tax return package |
| `france-vat-return` | Accounts 44551, 44562, 44566 and 44571 feed the CA3 or CA12 return |
| `france-einvoice` | Invoice format, the dates receiving and issuing become compulsory, the extra particulars |
| `france-payroll` and `fr-social-contributions` | Payroll postings to 641 and 645, and the contribution rates, which are not in this Guide |
| `fr-cfe` and `france-tax-optimization` | Local business taxes in 63511, inside 635 Autres impôts, taxes et versements assimilés. The value added for the CVAE is built from the accounts of the Plan Comptable Général |
| `fr-tax-audit` | The accounting file above is what an audit opens with |

| Item | Value | Note |
| --- | --- | --- |
| Source | all figures below | https://bofip.impots.gouv.fr/bofip/839-PGP.html |
| Turnover above which the value added contribution is due | EUR 152,500 | "152 500 €" |

## The method, step by step

1. Fix the regime first: the micro limits for the year of the income, then the simplified real regime conditions, turnover and VAT owed together: https://entreprendre.service-public.fr/vosdroits/F23267 and https://entreprendre.service-public.fr/vosdroits/F21852
2. Open the right books. Micro: a livre des recettes, plus a registre des achats for goods and accommodation: https://entreprendre.service-public.fr/vosdroits/F23266 Real regime: livre-journal, grand-livre and manuel des procédures, numbered by the greffier, with the super-simplified option elected on results return 2031: https://entreprendre.service-public.fr/vosdroits/F21852
3. Post from documents, not the bank alone. Every entry carries its origin, content, account and document reference, and every invoice the particulars above: https://entreprendre.service-public.fr/vosdroits/F31808
4. Test an asset against the low-value tolerance before capitalising, then set the method and rate: https://bofip.impots.gouv.fr/bofip/2109-PGP.html and https://bofip.impots.gouv.fr/bofip/4520-PGP.html
5. Reconcile the VAT accounts to the return filed for the period: https://entreprendre.service-public.fr/vosdroits/F23566
6. Inventory at least every twelve months, post the closing adjustments, then hand the trial balance to `france-financial-statements`, check the accounting file exports in the required format, and archive for the retention periods above: https://bofip.impots.gouv.fr/bofip/9028-PGP.html and https://entreprendre.service-public.fr/vosdroits/F10029

## Ask the client first

- Which regime this year, micro, simplified real or normal real, and did either of the last two years cross a limit? That decides whether there are registers or double-entry books at all.
- How much VAT did it owe last year? Inside both turnover limits it is still in the normal real regime if it owed more than the VAT limit.
- Has it elected for super-simplified accounting on its results return this year? Without the election the full simplified rules apply.
- Is it under the VAT franchise, and does every invoice carry the exemption wording?
- Can its software export the accounting entries file with every required column? A package that cannot is a problem found during an audit, not before one.
- Does it sell goods or accommodation, or services? Almost every limit here splits on that line, and a mixed business needs both tested.

## When to refuse or refer

- The text of a particular line of the Plan Comptable Général that this Guide does not carry, or the posting of an unusual transaction. Read the standard at https://www.anc.gouv.fr/files/anc/files/1_Normes_fran%C3%A7aises/Plans%20comptables/2026/PCG--1er-janvier-2026.pdf
- Drawing up, approving, filing or auditing the annual accounts. Use `france-financial-statements`.
- The VAT return itself, its boxes, rates and deduction rules. Use `france-vat-return`.
- Payroll postings, contribution rates and the treatment of the CSG and the CRDS. Use `france-payroll` and `fr-social-contributions`.
- Consolidated accounts and groups, banks, insurers and listed companies. Farming, property companies and non-profit bodies: the pages used here cover traders, service providers and liberal professions.
- An audit under way, a proposed adjustment or a penalty notice. Use `fr-tax-audit`.
- Whether a given professional may sign the work. An expert-comptable must be on the roll of the Ordre des experts-comptables, and this Guide does not replace one.

## Sources

- https://entreprendre.service-public.fr/vosdroits/F21852
- https://entreprendre.service-public.fr/vosdroits/F23266
- https://entreprendre.service-public.fr/vosdroits/F23267
- https://entreprendre.service-public.fr/vosdroits/F21746
- https://entreprendre.service-public.fr/vosdroits/F23575
- https://entreprendre.service-public.fr/vosdroits/F23566
- https://entreprendre.service-public.fr/vosdroits/F31808
- https://entreprendre.service-public.fr/vosdroits/F10029
- https://bofip.impots.gouv.fr/bofip/3412-PGP.html
- https://bofip.impots.gouv.fr/bofip/2109-PGP.html
- https://bofip.impots.gouv.fr/bofip/4520-PGP.html
- https://bofip.impots.gouv.fr/bofip/4682-PGP.html
- https://bofip.impots.gouv.fr/bofip/4684-PGP.html
- https://bofip.impots.gouv.fr/bofip/4699-PGP.html
- https://bofip.impots.gouv.fr/bofip/9026-PGP.html
- https://bofip.impots.gouv.fr/bofip/9028-PGP.html
- https://www.impots.gouv.fr/fichiers-standards-des-ecritures-comptables
- https://bofip.impots.gouv.fr/bofip/13223-PGP.html
- https://bofip.impots.gouv.fr/bofip/839-PGP.html
- https://www.anc.gouv.fr/files/anc/files/1_Normes_fran%C3%A7aises/Plans%20comptables/2026/PCG--1er-janvier-2026.pdf

## Disclaimer

This Guide and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this Guide. All outputs must be reviewed and signed off by a qualified professional (such as an expert-comptable) before filing or acting upon.

> Contributed by OpenAccountants.

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
