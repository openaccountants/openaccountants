---
name: france-bookkeeping
description: Use this skill whenever asked about bookkeeping, chart of accounts, Plan Comptable Général (PCG), financial statements, P&L format, balance sheet layout, bank reconciliation, expense classification, asset capitalisation, or day-to-day accounting for a French entity. Trigger on phrases like "PCG", "Plan Comptable", "chart of accounts France", "bilan", "compte de résultat", "micro-entreprise accounting", "régime réel simplifié", "capitalise or expense France", "amortissement", "depreciation France", "bank reconciliation France", "bookkeeping France", or any question about recording transactions, classifying expenses, or preparing accounts under French law. ALWAYS read this skill before touching any bookkeeping work for France.
version: 1.3
jurisdiction: FR
tax_year: 2026
last_updated: 2026-10-31
review_status: pending_review
trust_label: Built by Michael Cutajar and the OpenAccountants team
drafted_by: OpenAccountants
approved_by: pending
depends_on:
  - bookkeeping-workflow-base
category: bookkeeping
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Bookkeeping in France (Plan Comptable Général, books, records and retention)

Which books a French business must keep under each regime, the account structure of the Plan Comptable Général, how expenses and assets are classified, what an invoice must carry, what the accounting file handed to a tax inspector must contain, and how long everything is kept. Figures are for tax year 2026. Two sources are older on their face, the retention page checked on 1 July 2024 and the invoice page on 11 August 2026, and the tax doctrine used here carries version dates from 2012 to 2021 (depreciation rates 23 September 2013, low-value assets 1 March 2017, declining balance 12 September 2012, accounting file format 7 June 2017, accounting file production 15 December 2021). Selected conditions and account labels were checked against the January2026 ANC compendium, the FEC specification and the retained official pages on29October2026. Publisher dates above remain historical source dates, not a claim that an old doctrine was enacted in2026.

## Section 1: Quick Reference

| Field | Value |
| --- | --- |
| Country | France (République française) |
| Currency | EUR |
| Financial year | Use the entity’s actual financial period; the inventory control runs at least every twelve months. This does not fix every financial year at twelve months. |
| Accounting standards | Plan Comptable Général, règlement 2014-03 of the Autorité des normes comptables, as modernised by règlement 2022-06 of 4 November 2022 for financial years beginning on or after 1 January 2025 |
| Governing bodies | Autorité des normes comptables; Direction générale des Finances publiques |
| Key legislation | Code de commerce articles L123-12 to L123-28; Code général des impôts; livre des procédures fiscales articles L. 47 A and A. 47 A-1 |
| Books, real regime | Livre-journal and grand-livre; documentation of the accounting procedures and organisation when needed to understand processing and controls. Apply the legal-form and simplification conditions below. |
| Books, micro-entrepreneur | Under the specified natural-person relief: livre des recettes, plus registre des achats for traders/accommodation providers; apply the legal-form conditions below. |
| Record retention | Ten years from the close for the books and supporting documents; six years for the documents the tax administration may call for |
| Who may keep the books | The business itself, or an expert-comptable on the roll of the Ordre des experts-comptables |

## Which books each regime must keep

Bookkeeping depends on the commercial-accounting duty, legal form and the applicable income-tax accounting simplifications. VAT reporting is a separate test. The turnover and prior-VAT figures immediately below describe the simplified VAT regime in the retained sole-trader administrative overview; they do not by themselves determine which books a company must keep.

| Item | Value | Note |
| --- | --- | --- |
| Source | all figures below | https://entreprendre.service-public.fr/vosdroits/F21852 |
| Simplified VAT regime, ordinary turnover ceiling for selling, catering and accommodation | EUR 945,000 | Test activity, options, prior-year VAT and taxable foreign purchases separately. |
| Simplified VAT regime, ordinary turnover ceiling for other activities | EUR 286,000 | This is not the universal income-tax/accounting-regime ceiling. |
| Prior-year VAT: statutory monthly-return trigger is strictly above | EUR 15,000 | CGI287-3bis; equality alone does not trigger that provision. The overview’s “inférieur” wording does not decide equality. |
| Communication-right sanction for refusal, obstruction or failure to preserve the documents covered by the statutory request | EUR 10,000 | CGI1734: per request under its own conditions, not an automatic fine for every missing bookkeeping document. |
| Ordinary criminal sanction for knowingly omitting or making inaccurate/fictitious entries in the journal or equivalent covered by CGI1743 | Five years’ imprisonment and EUR 500,000 | CGI1743 refers to1741; this is the ordinary penalty, subject to the proceeds-based increase and aggravation conditions, not a universal ceiling for an invoice error. |

The general commercial books are the livre-journal and grand-livre, with procedural documentation when needed. Entries identify their origin, content, account and supporting document. Cotation and paraphe by the greffier are available at the merchant’s request under Code de commerce R123-173; the retained administrative page states them as compulsory, and that broader wording is not adopted. Electronic records must support identification, date and integrity; validated computer entries are immutable. The ordinary auxiliary-journal centralisation rule is at least monthly. L123-25 permits qualifying natural persons under the simplified real income-tax regime to record receipts/payments during the year and receivables/payables at close, without an annexe. It separately permits qualifying commercial legal persons to use an abridged annexe. The additional permission to record receivables/payables only at close excludes entities controlled by a parent preparing consolidated accounts under L233-16; that exclusion belongs to the closing-recording permission, not automatically to the abridged annexe. L123-26 allows natural persons under the simplified real income-tax regime, by option or by right, to recognise expenses in profit or loss according to their payment date where the expense recurs at intervals no longer than one year, excluding purchases. This is a qualifying expense/payment-date rule, not permission to defer every general-expense posting to an annual entry; L123-27 permits simplified stock/work-in-progress valuation. The Service Public sole-trader branch describes quarterly centralisation and an annual super-simplified election on2031. Its exact bridge to the ordinary monthly rule is not established here: do not apply quarterly centralisation to every company or infer the income-tax regime from VAT liability.

For the natural persons within Code de commerce L123-28 and CGI50-0, the commercial-law relief replaces annual accounts with the prescribed receipts and, where relevant, purchase records. Do not apply that legal-form-specific relief to every entity described as “micro”.

| Item | Value | Note |
| --- | --- | --- |
| Source | all figures below | https://entreprendre.service-public.fr/vosdroits/F23266 |
| Unit amount below which retail sales and services to individuals may be entered as one daily total | EUR 76 | "inférieur à 76 €" |
| Maximum ordinary sanction stated for forging or using a forged register | Three years’ imprisonment and EUR 45,000 | The page states a maximum, not a fixed automatic sentence. |
| Penalty for each missing turnover declaration | EUR 60.1 | "une pénalité de 60,1 €" |
| Yearly turnover which, once passed in two consecutive years, forces an account dedicated to the activity | EUR 10,000 | "dépasse 10 000 €" |

- **Trader or accommodation provider.** A livre des recettes encaissées in date order, with the amount and origin of each receipt and the client's identity, the means of payment and the document reference, totalled every three months. Plus a registre des achats listing the year's purchases in date order with the means of payment and the document references.
- **Liberal profession.** The livre des recettes only, on the same terms. That page requires no registre des achats.
- **Under the VAT franchise there is more:** a yearly register detailing purchases of goods and services, a livre-journal showing professional receipts day by day, and the invoices kept.
- **Entries cannot be edited once recorded,** and the registers may be paper, official downloadable models or software, held electronically if wanted. The page says in terms there is no sanction for failing to keep them, but forgery and its use carry the prison term and the fine above.

## Section 2: Standard Chart of Accounts (Plan Comptable Général)

The current PCG has eight numbered classes:1–5 for balance-sheet accounts,6–7 for management/result accounts and8 for special accounts (articles1111-1 and1131-1). Its decimal plan permits suitable subdivisions and sector adaptations. The older tax-doctrine description of nine classes, free class0 and special accounts80/88/89 is preserved as a historical topic only; it is not used as the2026 mandatory plan. See https://bofip.impots.gouv.fr/bofip/3412-PGP.html and the current ANC compendium in Sources.

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
| 164 | Emprunts auprès des établissements de crédit, if not included in167 |

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

**Formation costs, the retained accounting choice.** Under PCG212-9, expenditure conditioning the entity's existence or overall development that cannot be linked to specific goods or services follows the stated route: constitution, transformation and first-establishment costs may be capitalised as frais d'établissement, but recognition in profit or loss is the reference method. Capitalised frais d'établissement are amortised under a plan within five years. This restores the original account201 topic; it is not the EUR500 equipment tolerance or a universal permission to capitalise operating costs. The same article gives capital-increase, merger and division costs their distinct capitalisation/share-premium route, with any premium shortfall expensed. Source: https://www.anc.gouv.fr/files/anc/files/1_Normes_fran%C3%A7aises/recueil/2026/Recueil-PCG-Janvier-2026.pdf

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
| 467 | Divers comptes débiteurs et produits à recevoir; distinguish468 Divers comptes créditeurs et charges à payer |

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
| 6155 | Entretien et réparations sur biens mobiliers |
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
| 645 | Cotisations de sécurité sociale et de prévoyance |
| 6511 | Redevances pour concessions, brevets, licences, marques, procédés, solutions informatiques |
| 657 | Valeurs comptables des immobilisations incorporelles et corporelles cédées |
| 6582 | Pénalités, amendes fiscales et pénales, inside 658 Pénalités et autres charges |
| 6611 | Intérêts des emprunts et dettes |
| 681 | Dotations aux amortissements, aux dépréciations et aux provisions, charges d’exploitation |

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
| Commercial annual accounts, default | Accruals. Record the movements and control assets/liabilities by inventory at least every twelve months. BNC cash accounting is a separate tax route. |
| Micro-entreprise | Receipts basis. Receipts are entered when cashed, and the taxable profit is turnover less a flat-rate allowance |
| Qualifying simplified income-tax accounting | Apply L123-25’s separate natural-person/legal-person conditions above; receipts/payments during the year and receivables/payables at close do not remove every company’s annexe. |
| Régime réel normal | Full accruals, every movement day by day, operation by operation |
| Qualifying long-term contracts | A specifically negotiated project spanning at least two accounting periods under PCG622-1; achèvement or avancement under622-2, with the method’s actual conditions. This is not every construction invoice. |
| Advance payments | Credit received advances to4191; clear that account against411 after invoicing. Separately test revenue recognition and VAT: the bank receipt alone does not establish either. |

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

The allowance replaces actual expenses for the applicable micro income-tax computation; its minimum, mixed-activity allocation and exact computation belong in `fr-income-tax`. These income-tax limits are separate from VAT thresholds and do not themselves remove a company’s commercial accounting duties. Use the legal-form gates above; leaving micro taxation requires the applicable real income-tax regime, not merely the VAT table.

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

The tax tolerance covers qualifying materials/tooling in2154/2155, small office equipment, office/shop furniture and software whose unit value excluding tax does not exceed EUR500. Transport equipment is excluded from the tooling limb; connected components are assessed together. Furniture normally qualifies for limited renewal purchases of the same item; initial furnishings or a complete renewal qualify only if their total price does not exceed EUR500 excluding tax. These are category-specific tax conditions, not a universal accounting threshold. PCG212-1 separately requires probable future economic benefits and reliable cost measurement, and212-6 permits nonsignificant assets to be expensed. An otherwise qualifying small item can still be capitalised.

### Standard Depreciation Rates (Amortissement Linéaire)

The following are indicative tax-doctrine yearly straight-line rates, not mandatory accounting lives. The source gives them “à titre purement indicatif” and prints “Maisons d’habitation ordinaires1à2” without the percent sign. Accounting depreciation follows the asset’s actual expected consumption/useful life.

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

For ordinary qualifying acquisitions from1January2010, use the coefficients above; the source separately preserves older acquisition-date bands. Multiply the linear rate for the normal useful life by the coefficient. Start at the first day of the acquisition/construction month with financial-period proration; switch to residual value divided by remaining years where that produces the greater permitted charge. Special equipment coefficients require their own provision. The general exclusions for dwellings/worksites/professional premises must be tested with the actual statutory categories: qualifying industrial buildings with normal useful life no more than fifteen years are a named exception. The hotel limb covers businesses providing accommodation or accommodation with meals, not restaurants/cafés alone, clinics, private retirement-home buildings or camping investment merely because they provide lodging. Newness, ownership and incorporation/separability conditions still apply, especially work on old or rented hotel buildings. Used assets are excluded unless an actual stated exception applies; the manufacturer-rebuilt tolerance requires latest technical improvements and a price approaching new equipment. Do not extend that tolerance to any refurbished purchase. If accounting depreciation is linear, record the tax excess as amortissements dérogatoires.

## Section 6: P&L Format (Compte de Résultat)

The compte de résultat gathers the income and expenses of the year and shows the profit or loss after depreciation and provisions. Règlement 2022-06 of 4 November 2022 moved accounts that fed the exceptional result into the operating result, and binds financial years beginning on or after 1 January 2025. What stays in the exceptional result is income and expenses directly linked to a major and unusual event, entries of purely tax origin such as amortissements dérogatoires and provisions réglementées, a change of accounting method taken through profit because of a tax rule, and corrections of errors other than those taken straight to equity. An event is unusual when it is not tied to the entity's normal and current activity. An event is presumed unusual when it has not happened in recent years and is unlikely to happen again. See https://bofip.impots.gouv.fr/bofip/13223-PGP.html and https://entreprendre.service-public.fr/vosdroits/F21852

The outline below is a working summary, not the complete statutory statement. Use the full système de base model in PCG821-2, its required columns and the entity’s applicable presentation options. See https://www.anc.gouv.fr/files/anc/files/1_Normes_fran%C3%A7aises/Plans%20comptables/2026/PCG--1er-janvier-2026.pdf Small entities and, for the income statement, medium entities have conditional simplified-presentation options. The no-annexe simplification under L123-25 applies to the specified natural persons; qualifying commercial legal persons have an abridged annexe, while the separate accounting-micro exemption has its own exclusions. Use `france-financial-statements`.

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

The bilan shows assets, liabilities and equity separately. The outline below is a working summary; use the full statutory modèle in PCG821-1 and the entity’s applicable columns and options. See https://www.anc.gouv.fr/files/anc/files/1_Normes_fran%C3%A7aises/Plans%20comptables/2026/PCG--1er-janvier-2026.pdf and https://entreprendre.service-public.fr/vosdroits/F21852

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

Historical illustrative bank-file fixtures, retained from the predecessor. These examples are not verified current specifications for the named banks. Confirm the format and columns against the actual client export; they are not rules of French law.

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
| REM CHQ | Cheque deposit. Match the underlying receivable or transaction; do not recognise new revenue from the bank label alone. |
| COTISATION | Identify the recipient and underlying document. The word alone does not establish a social contribution or account645. |
| URSSAF | Establish whose liability is paid: employer social contributions can use645; personal contributions of the exploitant use646. A manager’s status requires its own analysis. |
| TRESOR PUBLIC or DGFIP | Tax payment: corporation tax, VAT, CFE |
| LOYER | Rent (613) |
| ECHEANCE PRET | Match the loan schedule; split principal to the appropriate borrowing account (164 only where applicable), and interest to6611. |

## Section 9: Micro-Entity / Small Business Simplifications

### Size Categories (Code de Commerce)

An entity’s accounting size class uses two of three criteria: balance-sheet total, net turnover and average headcount. These are separate from micro taxation. Apply the two-consecutive-financial-years change rule and statutory entity exclusions; a holding/financial or otherwise excluded entity cannot take a simplification merely because it meets a number. The selected small/medium figures below do not replace the complete eligibility test in `france-financial-statements`.

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
| Bookkeeping | Natural-person micro relief: prescribed receipts/purchases records | Journal/ledger; documentation when needed; qualifying L123-25 relief and sole-trader election above | Journal/ledger, documentation when needed; ordinary chronological entries |
| Centralisation | No double-entry centralisation under the specified register relief | Ordinary rule at least monthly; administrative sole-trader quarterly branch remains specifically qualified above | At least monthly for auxiliary journals |
| Annual accounts | No annual accounts only for the specified L123-28 natural persons | Natural-person L123-25 no-annexe rule; legal-person abridged-annexe conditions; actual presentation options | Bilan, compte de résultat and annexe, subject to any separate applicable exemption |
| VAT | Independent franchise, option and foreign-purchase tests | Independent simplified-VAT conditions and qualified CA12/instalment route | Normal VAT reporting where its conditions apply; a VAT label does not determine the books |
| Income tax | Flat-rate allowance on turnover, Section 3 | Actual expenses | Actual expenses |
| Tax return package | Apply the actual micro reporting duties; no real-regime results package under the specified relief | BIC2031 or IS2065, with the applicable2033 series; do not infer the return from legal form alone | Applicable BIC2031 or IS2065 with2050 series; BNC/other income-tax routes belong in `fr-income-tax` |

### TVA Franchise en Base Thresholds

The single franchise threshold announced in the 2025 finance law was abandoned. These are the limits in force for 2026.

| Activity | Basic threshold | Tolerance threshold |
| --- | --- | --- |
| Source | all figures below | https://entreprendre.service-public.fr/vosdroits/F21746 |
| Goods and accommodation | EUR 85,000 | EUR 93,500 |
| Services | EUR 37,500 | EUR 41,250 |
| Lawyers' regulated work, authors' and performers' works and copyright | EUR 50,000 | EUR 55,000 |
| Their other activities | EUR 35,000 | EUR 38,500 |

The ordinary domestic franchise tests both periods separately: the previous calendar year must satisfy its basic ceiling, and a current-year overrun of the higher ceiling ends the franchise from that overrun date. Exceeding the previous-year basic ceiling removes the franchise from1January of the following year; satisfying only the current higher ceiling does not restore it. Startup annualisation/source conflicts remain explicitly in `france-vat-return`. Invoices under the franchise state “TVA non applicable, art.293 B du code général des impôts”.

## VAT bookkeeping by regime

Determine VAT independently of income-tax accounting: test the franchise/option, applicable turnover, prior-VAT and foreign-purchase conditions. CGI287-3bis uses a prior-year VAT trigger strictly above EUR15,000;287-3ter has separate monthly reporting for specified intra-EU acquisitions, imports and suspensive-regime exits. The administrative higher-turnover procedure below states a current-year move retroactive to1January, while the current implementing text and recapitulatory procedure are preserved in `france-vat-return`. Apply that companion’s qualified procedure; noncalendar reconciliation remains unresolved. Do not apply one effective date to every trigger or change the income-tax books solely because VAT reporting changes.

| Item | Value | Note |
| --- | --- | --- |
| Source | all figures below | https://entreprendre.service-public.fr/vosdroits/F23575 |
| Turnover above which the simplified regime is undone back to 1 January of that year, goods and accommodation | EUR 1,040,000 | "1 040 000 €" |
| Turnover above which the simplified regime is undone back to 1 January of that year, services | EUR 323,000 | "323 000 €" |

| Item | Value | Note |
| --- | --- | --- |
| Source | all figures below | https://entreprendre.service-public.fr/vosdroits/F23566 |
| Calendar-year July instalment on previous-year VAT before deduction of VAT on fixed assets | 55% | Apply the statutory base and adjustment conditions, not every prior-year balance due. |
| Calendar-year December instalment on the same statutory base | 40% | Fixed-asset VAT is excluded from that base. |
| Previous-year VAT on that statutory base below which no instalment is due | EUR 1,000 | Strictly below; assess before fixed-asset VAT deduction. |

Output VAT sits in44571, expense input VAT in44566, capital-asset input VAT in44562 and the payable balance in44551. Reconcile each reporting period and clear44551 against payment. The qualified CA3/CA12 and instalment mechanics are in `france-vat-return`. A domestic-sales franchise removes collection and associated input deduction for those operations; it does not remove commercial books, nor every VAT duty on foreign purchases. Keep the actual taxable-purchase and option analysis.

## Invoices: the particulars every invoice must carry

Apply the invoice particulars to the actual customer, transaction and VAT liability. The overview below is not a universal consumer-invoice obligation or a substitute for conditional mentions. See https://entreprendre.service-public.fr/vosdroits/F31808

- Date of issue; a unique number from a chronological and continuous sequence; the date of the sale, of the end of the service, or of an instalment paid.
- Seller: for an individual business the name and first name with "Entrepreneur individuel" or "EI", the address and the Siren number; for a company the name, the Siren number, the registered office address, the legal form and the share capital.
- Buyer: the name, the address, the billing address if different, and the purchase order number where one was issued.
- Each product or service: nature, quantity, precise name, unit price excluding VAT and the VAT rate, or the exemption wording.
- The total excluding VAT and the total including VAT; any increase such as carriage or packing; any rebate or discount linked to the operation.
- The payment date, the early payment discount terms or the words that there are none, and the rate of late payment penalties.

| Item | Value | Note |
| --- | --- | --- |
| Source | all figures below | https://entreprendre.service-public.fr/vosdroits/F31808 |
| Total excluding VAT at or below which the limited CGI annexeII242 noniesA-II simplification is available | EUR 150 | Only the supplier VAT number inI-2 and exemption reference inI-12 are waived under that provision. Customer VAT numbers and reverse-charge wording have their separate conditions. |
| Fixed recovery indemnity to be mentioned on an invoice between businesses | EUR 40 | "indemnité forfaitaire de 40 €" |

Four additional particulars follow the applicable electronic-invoicing issue deadline: business customer Siren, different goods-delivery address, goods/services/both classification and the specified debit-option wording. French VAT taxable persons, including franchise businesses and persons making only exempt sales, must be able to receive in-scope electronic invoices from1September2026. Issuing/data transmission starts then for large/intermediate entities, with the statutory1September2027 extension for PME/micro entities except VAT-group members. Size is tested at legal-unit level using1January2025 and the stated accounts reference, not the transaction-year label alone. See `france-einvoice`. Other conditional mentions include approved-body membership, franchise, “Auto-liquidation”, electrical-waste contribution, private-copying levy, “Auto-facturation” and applicable craft professional-insurance references; each needs its actual scope.

## The fichier des écritures comptables

A taxpayer keeping computerised books, subject to CGI accounting-document duties and undergoing a comptabilité audit, provides its FEC at the start of control in the prescribed format. This includes IS and real-regime BIC/BNC/BA taxpayers under the actual conditions. BOI9026’s tolerance exempts SCI taxed exclusively as revenus fonciers with only natural-person members, but SCI meeting Code de commerce L612-1/R612-1 still provide an FEC regardless of tax regime; the tolerance does not exempt the other SCI described there. Computerised auto-entrepreneur registers have the stated separate tolerance. See https://bofip.impots.gouv.fr/bofip/9026-PGP.html and https://bofip.impots.gouv.fr/bofip/9028-PGP.html

The following are the eighteen leading fields for the ordinary commercial format; use the applicable BNC/BA layout for those taxpayers, including the separate cash-accounting layouts. Montant/Sens replaces fields12/13 only where Debit/Credit are absent from the accounting system; it is not an extra field inserted after Credit.

| # | Field | Note |
| --- | --- | --- |
| 1 | JournalCode | Journal code |
| 2 | JournalLib | Journal name |
| 3 | EcritureNum | Same number on each line of one double entry; increasing without gaps within the chosen global or per-journal sequence. Describe per-journal numbering; JournalCode distinguishes repeated numbers across journals. |
| 4 | EcritureDate | Posting date |
| 5 | CompteNum | Applicable account number; ordinary commercial format follows the specified PCG roots |
| 6 | CompteLib | Account name |
| 7 | CompAuxNum | Auxiliary account code; blank if unused |
| 8 | CompAuxLib | Auxiliary account name; blank if unused |
| 9 | PieceRef | Supporting-document reference |
| 10 | PieceDate | Supporting-document date; apply the specified fallback where no document/date exists |
| 11 | EcritureLib | Literal description of the entry |
| 12 | Debit | Signed euro amount; numeric zero on the unused side |
| 13 | Credit | Signed euro amount; numeric zero on the unused side |
| 14 | EcritureLet | Matching mark; blank if unused |
| 15 | DateLet | Matching date; blank if unused |
| 16 | ValidDate | Date the draft became final by unique identifier; posting date if there is no draft mode |
| 17 | Montantdevise | Foreign-currency amount; blank if unused |
| 18 | Idevise | Currency identifier; blank if unused |

In the permitted alternative,12 is Montant and13 is Sens. Sens accepts D/C or+1/-1, without an internal space. Keep each required column even when its value can be blank. The primary specification is listed in Sources.

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

The micro-entrepreneur retains the receipts book, purchases register and supporting documents for the stated ten years. The communication-right sanction in the first table has its own statutory request/obstruction/preservation conditions; it is not an automatic fine for failure to keep a micro register. A bank document used as accounting support can require the longer accounting retention period rather than only the general five-year bank-document category.

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
| Turnover above which the business enters the stated CVAE assessment/declaration scope | EUR 152,500 | Do not confuse this with effective payment: the checked ordinary rate is zero below EUR500,000 turnover. Apply the actual filing exemptions and conditions in `fr-cfe`. |

## The method, step by step

1. Establish legal form and the commercial-accounting duty, then the income-tax regime for the income year. Test VAT separately: https://entreprendre.service-public.fr/vosdroits/F23267 and https://entreprendre.service-public.fr/vosdroits/F21852
2. Open the prescribed registers or commercial journal/ledger under the actual legal-form conditions. Document procedures when needed; greffier cotation/paraphe is optional on request. Apply the specific sole-trader election and qualified centralisation route above: https://entreprendre.service-public.fr/vosdroits/F23266 and https://entreprendre.service-public.fr/vosdroits/F21852
3. Post from documents, not the bank alone. Every entry carries its origin, content, account and document reference, and every invoice the particulars above: https://entreprendre.service-public.fr/vosdroits/F31808
4. Test an asset against the low-value tolerance before capitalising, then set the method and rate: https://bofip.impots.gouv.fr/bofip/2109-PGP.html and https://bofip.impots.gouv.fr/bofip/4520-PGP.html
5. Reconcile the VAT accounts to the return filed for the period: https://entreprendre.service-public.fr/vosdroits/F23566
6. Inventory at least every twelve months, post the closing adjustments, then hand the trial balance to `france-financial-statements`, check the accounting file exports in the required format, and archive for the retention periods above: https://bofip.impots.gouv.fr/bofip/9028-PGP.html and https://entreprendre.service-public.fr/vosdroits/F10029

## Ask the client first

- What are the legal form, accounting duty and income-tax regime for this income year? Obtain both prior-year turnover figures; do not decide books from VAT liability alone.
- How much VAT did it owe last year on the actual statutory measure? Test the separate VAT thresholds, options and foreign purchases; a monthly VAT return does not itself change the income-tax accounting regime.
- Is this a qualifying sole trader, and has the annual super-simplified election been made on the applicable results return? Establish any separate company-law simplification rather than assuming that election applies to every entity.
- Is it under the VAT franchise, and does every invoice carry the exemption wording?
- Can its software export the applicable FEC with every required field? Check the export before an audit, reconcile it to the books and retain the format/numbering description.
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

- https://www.anc.gouv.fr/files/anc/files/1_Normes_fran%C3%A7aises/recueil/2026/Recueil-PCG-Janvier-2026.pdf
- https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000027804775
- https://bofip.impots.gouv.fr/bofip/4698-PGP.html
- https://bofip.impots.gouv.fr/bofip/4750-PGP.html
- https://www.legifrance.gouv.fr/codes/id/LEGISCTA000006162005
- Selected repair reads, 31 October 2026: the actual L123-26 reproduction in the January2026 ANC compendium supplies the payment-date/annual-recurrence/purchases-exclusion rule, separately from the agency's regular-entry/quarterly-centralisation wording. PCG212-9 supplies the restored formation-cost accounting choice. The actual earlier11eb01a4 body is included in the complete old-topic map, with its unsupported historical assertions distinguished from current methods.

Not yet confirmed here: the sole-trader quarterly-centralisation bridge to the ordinary monthly rule; startup-franchise and noncalendar simplified-VAT reconciliation; current bank-specific export layouts; and the historical class0/80/88/89 scheme as a current mandatory plan. The named companions retain their own precise specialist limits. These boundaries are not professional attestation.

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
