---
name: france-financial-statements
description: Use this skill when preparing, reviewing, or advising on annual financial statements (comptes annuels) for a French company. Trigger on phrases like "comptes annuels", "dépôt des comptes", "greffe", "Plan Comptable Général", "PCG", "bilan", "compte de résultat", "annexe", "commissaire aux comptes", "audit France", "petite entreprise", "micro-entreprise comptable", "liasse fiscale", or any question about preparing and filing statutory accounts under French commercial law. Covers PCG framework, size thresholds, required statements, formats, notes, filing deadlines, and audit requirements.
version: 1.0
jurisdiction: FR
tax_year: 2026
last_updated: 2026-10-19
authored_by: Michael Cutajar and the OpenAccountants team
review_status: pending_review
trust_label: Built by Michael Cutajar and the OpenAccountants team
depends_on:
  - financial-statements-workflow-base
category: financial-statements
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# France: annual accounts (comptes annuels), their filing and the statutory audit

This skill prepares, reviews and advises on the annual accounts of a French commercial company under the Plan Comptable Général (PCG): the size category, the documents to draw up, the formats, the year-end adjustments, approval by the partners, filing at the greffe, the confidentiality options and the statutory auditor (commissaire aux comptes, CAC). Figures are for tax year 2026. The accounts of financial years closed in 2025, which are approved, filed and declared in 2026, and the accounts of financial years running during 2026 use the same size and auditor thresholds, because those thresholds apply to financial years opened on or after 1 January 2024; the corporation tax return dates in Section 11 are those printed for financial years closed on 31 December 2025, and the CVAE rate in Section 5 is the one for 2026. The rules stated are those in force on 19 October 2026, read on official pages between 19 September and 19 October 2026; each page's own date stamp is given in its table, and some pages were last checked by their publisher in 2024 or 2025.

## Section 1: Quick reference

**Quick reference**

| Field | Value |
| --- | --- |
| Country | France (République française) |
| Currency | EUR |
| Filing authority | Greffe du tribunal de commerce (or tribunal des activités économiques) of the registered office; in Alsace-Moselle, the tribunal judiciaire |
| Filing channel | Online on the guichet des formalités des entreprises, or on paper at the greffe, or by registered post |
| Accounting framework | Plan Comptable Général, ANC regulation no. 2014-03 as amended (consolidated text of 1 January 2026) |
| Legal references printed by the filing page | Code de commerce, art. L. 232-21 to L. 232-26 (filing), art. R. 123-111 and R. 123-111-1 (filing deadline and confidentiality), art. D. 123-200 (size thresholds) |
| Size thresholds | Décret n° 2024-152 du 28 février 2024; see Section 3 |
| Approval of the accounts | SA, SARL and EURL: within 6 months of the year end. SAS and SASU: within a period the partners set freely. See Section 9 |
| Filing deadline | Within 1 month after approval, or within 2 months when filed electronically. See Section 9 |
| Penalties for not filing | See the table in Section 9 |
| Statutory auditor | Compulsory above the thresholds in Section 10; an SA is not audited automatically |
| Companion skills | `france-bookkeeping` (books, chart of accounts, depreciation), `france-vat-return`, `france-einvoice`, `france-formation`, `france-payroll`, `fr-tax-audit` |

## The method, step by step

1. **Identify the company.** Note the legal form (SAS, SASU, SA, SARL, EURL, SCI or other), whether it controls or is controlled by another entity, its tax regime (régime réel simplifié or normal, impôt sur les sociétés or impôt sur le revenu) and the date its financial year ends. A company that belongs to a group follows the group rules on the accounting obligations page (https://entreprendre.service-public.gouv.fr/vosdroits/F37169) and cannot keep simplified books.
2. **Find the size category** from the balance sheet total, the net turnover and the average headcount of the year being closed, using the table in Section 3 (https://entreprendre.service-public.gouv.fr/vosdroits/F37169). The category decides the annexe, the management report, the presentation and the confidentiality option.
3. **Close the books under the PCG.** Take an inventory of assets and liabilities (at most every 12 months, as the accounting obligations page says) and post the year-end adjustments in Section 5, using the PCG articles cited there (https://www.anc.gouv.fr/files/anc/files/1_Normes_fran%C3%A7aises/recueil/2026/Recueil-PCG-Janvier-2026.pdf).
4. **Draw up the comptes annuels** (bilan, compte de résultat and, unless exempt, annexe) in the presentation the size allows (Sections 4, 6, 7 and 8), and the rapport de gestion where Section 4 requires one (https://entreprendre.service-public.gouv.fr/actualites/A18259).
5. **File the corporation tax return** (déclaration n° 2065 with the liasse fiscale) by the date in Section 11 (https://entreprendre.service-public.gouv.fr/vosdroits/F23575). The tax deadline and the approval deadline are set separately, and the tax return can fall due before the accounts are approved.
6. **Check the auditor position** against Section 10 (https://entreprendre.service-public.gouv.fr/vosdroits/F31440). Where a CAC is in office, its report goes to the approval meeting and into the filing.
7. **Approve the accounts and appropriate the result** within the period in Section 9 (https://entreprendre.service-public.gouv.fr/vosdroits/F31214), including the transfer to the legal reserve in Section 9 (https://entreprendre.service-public.gouv.fr/vosdroits/F24024).
8. **File at the greffe** within the period in Section 9, with the documents listed for the size, and attach a confidentiality declaration if the company is entitled to one and wants it (https://entreprendre.service-public.gouv.fr/vosdroits/F31214).
9. **Keep the books and vouchers** for the period in the Section 3 table, counted from the close of the financial year (https://entreprendre.service-public.gouv.fr/vosdroits/F37169).

## Ask the client first

- What is the legal form, and for a SAS or SASU, what period do the statutes set for approving the accounts?
- Does the company control another entity, or is it controlled by one? (This changes the auditor thresholds, the management report and whether consolidated accounts are due.)
- For the year being closed and the year before: what were the balance sheet total, the net turnover excluding VAT and the average headcount?
- Is a statutory auditor in office, and when does the mandate end?
- Is the company's activity the management of shareholdings and securities? (A micro-enterprise with that activity cannot skip the annexe.)
- Does the company want its accounts, or its compte de résultat, kept out of publication?

## When to refuse or refer

- Consolidated accounts, IFRS accounts, and the choice between French standards and IFRS for a group. This skill covers individual accounts only; consolidated accounts under French standards follow ANC regulation no. 2020-01, which this skill does not cover.
- Public-interest entities (EIP) and listed companies, and banks, insurers and other entities with a sector accounting regulation of their own (the PCG applies to them only where their own regulation is silent).
- Associations, foundations and private training bodies (organismes de formation), which have their own auditor rules.
- Sustainability reporting (informations en matière de durabilité).
- A company whose equity has fallen below half of its share capital: a specific legal procedure applies (https://entreprendre.service-public.gouv.fr/vosdroits/F24024). Refer to a lawyer or accountant.
- A foreign company filing the accounts of a French branch, mergers, transformations, liquidation and a first financial year longer or shorter than 12 months.
- Signing an audit opinion. Only a commissaire aux comptes may do that.

## Section 2: Reporting framework

**Reporting framework**

| Entity | Rule |
| --- | --- |
| Every entity required to draw up annual accounts | The PCG (ANC regulation no. 2014-03) applies, unless a sector regulation of its own covers the point |
| Micro-enterprise | Bilan and compte de résultat; may skip the annexe unless its activity is managing shareholdings and securities |
| Small enterprise (petite entreprise) | May present its bilan and compte de résultat in the abridged system (système abrégé), PCG art. 811-5 |
| Medium-sized enterprise (moyenne entreprise) | May present its compte de résultat in the simplified model of PCG art. 822-2 |
| Consolidated accounts | Outside this skill (see "When to refuse or refer") |

**PCG text, consolidated version of 1 January 2026**

| Item | Rule | Note (verbatim) |
| --- | --- | --- |
| Source | all rules below | https://www.anc.gouv.fr/files/anc/files/1_Normes_fran%C3%A7aises/recueil/2026/Recueil-PCG-Janvier-2026.pdf |
| Scope of the PCG | Applies to every entity required to draw up annual accounts | "le Plan Comptable Général constitue le règlement comptable applicable à toute entité tenue d’établir des comptes annuels" |
| Presentation, small enterprises | Abridged system allowed | "Les petites entreprises définies à l’article L. 123-16 du code de commerce peuvent adopter une présentation simplifiée de leurs comptes annuels" |
| Presentation, medium enterprises | Simplified P&L model allowed | "Les moyennes entreprises définies à l’article L. 123-16 du code de commerce peuvent adopter une présentation simplifiée de leur compte de résultat suivant le modèle proposé à l’article 822-2" |

## Section 3: Size thresholds

A company belongs to a category when it meets at least 2 of the 3 criteria of that category, and each criterion is met when the figure is less than or equal to the limit (inférieur ou égal). The test uses the balance sheet total, the net turnover (excluding VAT for the small and medium tests, as the page writes it) and the average number of employees over the year. A company that does not meet 2 of the 3 medium-enterprise criteria is a large enterprise; the accounting obligations page gives no large-enterprise figures, and the news item prints them as above the medium limits ("Grandes entreprises Supérieur à 25 millions € Supérieur à 50 millions € Plus de 250 salariés"). These limits apply to the accounts and reports of financial years opened on or after 1 January 2024 (news item of 5 March 2024, now marked by the site as an older article, https://entreprendre.service-public.gouv.fr/actualites/A17100). The page does not say whether the limits must be met for one year or for two consecutive years before a company changes category; see changes.md section 6.

**Size categories, simplified regime and record keeping**

| Item | Value | Note (verbatim, page checked by its publisher on 07 septembre 2026) |
| --- | --- | --- |
| Source | all figures below | https://entreprendre.service-public.gouv.fr/vosdroits/F37169 |
| Micro-enterprise, balance sheet total, at most | EUR 450,000 | "Bilan total inférieur ou égal à 450 000 €" |
| Micro-enterprise, net turnover, at most | EUR 900,000 | "Montant net du chiffre d'affaires inférieur ou égal à 900 000 €" |
| Micro-enterprise, average headcount, at most | 10 employees | "Nombre moyen de salariés employés au cours de l'année inférieur ou égal à 10" |
| Small enterprise, balance sheet total, at most | EUR 7,500,000 | "Bilan total inférieur ou égal à 7 500 000 €" |
| Small enterprise, net turnover excluding VAT, at most | EUR 15,000,000 | "Montant net HT du chiffre d'affaires inférieur ou égal à 15 000 000 €" |
| Small enterprise, average headcount, at most | 50 employees | "Nombre moyen de salariés employés au cours de l'année inférieur ou égal à 50" |
| Medium enterprise, balance sheet total, at most | EUR 25,000,000 | "Bilan total inférieur ou égal à 25 000 000 €" |
| Medium enterprise, net turnover excluding VAT, at most | EUR 50,000,000 | "Montant net HT du chiffre d'affaires inférieur ou égal à 50 000 000 €" |
| Medium enterprise, average headcount, at most | 250 employees | "Nombre moyen de salariés employés au cours de l'année inférieur ou égal à 250" |
| How many criteria | 2 of 3 | "si elle remplit 2 des 3 critères suivants" |
| Simplified regime (régime réel simplifié, which allows simplified books), turnover, selling, catering and accommodation, at most | EUR 945,000 | "945 000 € pour les activités de vente, de restauration ou de mise à disposition de logement" |
| Simplified regime, turnover, other activities, at most | EUR 286,000 | "286 000 € pour les autres activités" |
| Simplified regime, VAT payable, below | EUR 15,000 | "Le montant de la TVA dont elle est redevable est inférieur à 15 000 €" |
| Keeping the books and vouchers, from the close of the year | at least 10 years | "au moins 10 ans à partir de la clôture de l'exercice comptable" |
| Fine for not keeping them | EUR 10,000 | "s'expose à une amende de 10 000 €" |

The simplified regime needs all its conditions together: the turnover limit for the activity AND the VAT payable limit. The EUR 15,000 in the table is the VAT payable limit, not a turnover limit. A company in a group cannot keep simplified books, whatever its size.

## Section 4: Required financial statements

**Required documents by size (individual accounts)**

| Document | Micro | Petite | Moyenne |
| --- | --- | --- | --- |
| Bilan (balance sheet) | Required | Required; may be in simplified form | Required |
| Compte de résultat (P&L) | Required | Required; may be in simplified form | Required; may use the simplified model |
| Annexe (notes) | Not required, unless the activity is managing shareholdings and securities | Required; may be abridged if the company is under the simplified corporation tax regime | Required; may be abridged if the company is under the simplified corporation tax regime |
| Rapport de gestion (management report) | Not required (loi n° 2025-391 du 30 avril 2025, art. 8) | Not required | Required |
| Rapport du CAC (auditor's report) | Filed if a CAC is in office | Filed if a CAC is in office | Filed if a CAC is in office, unless only a simplified presentation is published (Section 9) |
| Tableau des flux de trésorerie (cash flow statement) | Not one of the documents that make up the annual accounts on the official page | Same | Same |

Sources: https://entreprendre.service-public.gouv.fr/vosdroits/F37169 (composition of the accounts by size, and the group rule), https://entreprendre.service-public.gouv.fr/vosdroits/F31214 (micro annexe exemption and its exception), https://entreprendre.service-public.gouv.fr/actualites/A18259 (management report). A company that belongs to a group draws up a bilan, a compte de résultat, a rapport de gestion and an annexe whatever its size, and the controlling company also draws up consolidated accounts (F37169). The official pages give no separate large-enterprise column for the documents; for a large enterprise, apply at least the medium-enterprise documents and none of the simplifications, and have the accountant confirm.

## Section 5: Year-end adjustments checklist

**Year-end adjustments checklist**

| # | Adjustment | France-specific notes |
| --- | --- | --- |
| 1 | Amortissements (depreciation) | Straight-line, or declining balance (dégressif) where the tax rules allow it; component approach. Depreciation methods and rates in depth: `france-bookkeeping` |
| 2 | Provisions pour risques et charges | PCG art. 322-1: a liability is recognised when the entity has an obligation to a third party and an outflow of resources without at least equivalent consideration is probable or certain |
| 3 | Charges constatées d'avance (prepayments) | Strict matching of charges to the year |
| 4 | Produits constatés d'avance (deferred income) | Revenue received but not yet earned |
| 5 | Dépréciation des créances douteuses (doubtful debts) | Individual assessment. The VAT side of an unpaid invoice is a separate question: see `france-vat-return` |
| 6 | Stocks et en-cours (inventory) | Lower of cost (FIFO or weighted average cost, CUMP) and realisable value |
| 7 | Impôts différés | Not normally recognised in individual accounts; the PCG text itself refers to entities that do not recognise deferred tax in their individual accounts. Consolidated accounts are out of scope |
| 8 | Écarts de conversion (foreign currency receivables and payables) | Restated at the closing rate. Unrealised losses go to écart de conversion actif AND a provision for risks, reduced to the unhedged part of the risk where a hedge exists (PCG art. 420-6); unrealised gains go to écart de conversion passif and are not taken to profit. Foreign currency cash differences go to profit (PCG art. 420-7) |
| 9 | Participation des salariés (employee profit-sharing) | Compulsory where the company has employed at least 50 employees each month without interruption for the last 5 years; see the table below |
| 10 | Congés payés (holiday pay) | Accrue untaken leave with the related social charges |
| 11 | Indemnités de départ à la retraite (retirement benefits) | Commitment or provision under the PCG, following ANC recommendation no. 2013-02 as updated on 5 November 2021 |
| 12 | CVAE (cotisation sur la valeur ajoutée des entreprises) | Accrue the charge for the year at the 2026 rate; the rate rose for 2026; see the table below |

**PCG rules used in the checklist**

| Item | Rule | Note (verbatim) |
| --- | --- | --- |
| Source | all rules below | https://www.anc.gouv.fr/files/anc/files/1_Normes_fran%C3%A7aises/recueil/2026/Recueil-PCG-Janvier-2026.pdf |
| Provisions (art. 322-1) | Obligation to a third party; outflow probable or certain | "un passif est comptabilisé lorsque l'entité a une obligation à l'égard d'un tiers, et qu'il est probable ou certain que cette obligation provoquera une sortie de ressources" |
| Unrealised FX losses | Provision for risks, only for the part of the risk not hedged (art. 420-6) | "Les pertes de change latentes entraînent à due concurrence la constitution d’une provision pour risques, sous réserve des dispositions particulières de l’article 420-6" |
| Unrealised FX gains | Shown in liabilities | "au passif du bilan pour les différences correspondant à un gain latent" |
| Foreign currency cash (art. 420-7) | Differences go to profit, except hedging | "Les écarts de conversion constatés sont comptabilisés dans le résultat de l’exercice, sauf en cas d’application des dispositions relatives aux opérations de couverture" |
| Deferred tax in individual accounts | Text refers to entities that do not recognise it | "Lorsque l’entité ne comptabilise pas d’impôts différés dans ses comptes individuels" |
| Retirement benefits | ANC recommendation no. 2013-02 | "recommandation ANC n° 2013-02 du 7 novembre 2013 modifiée le 5 novembre 2021" |

**Employee profit-sharing (participation)**

| Item | Rule | Note (verbatim, page checked by its publisher on 21 juillet 2026) |
| --- | --- | --- |
| Source | all rules below | https://www.service-public.gouv.fr/particuliers/vosdroits/F2141 |
| When it is compulsory | At least 50 employees each month, without interruption, over the last 5 years | "La participation doit être obligatoirement instaurée dans les entreprises qui ont employé sans interruption au moins 50 salariés par mois au cours des 5 dernières années" |
| From when | The first financial year opened after that 5-year period | "Ces entreprises doivent mettre en place la participation au cours du 1 er exercice comptable" |
| Fewer than 50 employees | Optional | "Les entreprises de moins de 50 salariés peuvent choisir de mettre en place la participation" |

**CVAE for 2026**

| Item | Value | Note (verbatim) |
| --- | --- | --- |
| Source | all figures below | https://bofip.impots.gouv.fr/bofip/839-PGP.html |
| Turnover at which a business comes within the CVAE at all | EUR 152,500 | "seuil d’assujettissement à la CVAE (152 500 €)" |
| Maximum rate for 2026 (highest turnover band) | 0.28% | "> 50 000 000 € 0,19 % 0,28 %" |

The maximum rate in the table is higher than the 2025 maximum: the phase-out was put back, so a provision built on the 2025 rate understates the 2026 charge. The rate for lower turnover bands follows the formulas on the same BOFiP page.

## Section 6: Compte de résultat format (P&L)

The Code de commerce (art. R. 123-193, reproduced in the PCG compendium cited in Section 2) sets the order: operating charges and income, financial charges and income, exceptional charges and income, employee profit-sharing and income tax. PCG format, système de base (by nature):

~~~
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

  === RÉSULTAT D'EXPLOITATION ===

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

  === RÉSULTAT FINANCIER ===

PRODUITS EXCEPTIONNELS
CHARGES EXCEPTIONNELLES

  === RÉSULTAT EXCEPTIONNEL ===

Participation des salariés
Impôt sur les bénéfices
  === RÉSULTAT NET ===
~~~

What goes in the exceptional result is narrow. The current PCG text (art. 513-5) puts there only the income and charges directly linked to a major and unusual event; ordinary gains and losses stay in the operating or financial result.

| Item | Rule | Note (verbatim) |
| --- | --- | --- |
| Source | all rules below | https://www.anc.gouv.fr/files/anc/files/1_Normes_fran%C3%A7aises/recueil/2026/Recueil-PCG-Janvier-2026.pdf |
| Exceptional result (art. 513-5) | Major and unusual event only | "Sont comptabilisés en résultat exceptionnel les produits et les charges directement liés à un événement majeur et inhabituel" |
| P&L order (Code de commerce art. R. 123-193) | Operating, financial, exceptional, profit-sharing, tax | "les charges d'exploitation, les charges financières, les charges exceptionnelles ainsi que la participation des salariés aux fruits de l'exp" |

## Section 7: Bilan format (balance sheet)

PCG format, système de base:

~~~
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
  Écarts de conversion actif

-------------------------------------

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
  Écarts de conversion passif
~~~

The écarts de conversion lines are added because the PCG requires unrealised exchange losses on foreign currency receivables and payables to be shown as an asset in individual accounts ("sont obligatoirement portés à l’actif du bilan, dans les comptes individuels comme dans les comptes consolidés", PCG compendium cited in Section 2).

## Section 8: Notes to the accounts (annexe)

A micro-enterprise may skip the annexe entirely, unless its activity is managing shareholdings and securities (Section 4). For small and medium enterprises, the PCG (title VIII, chapter III, articles 831-1 onwards, in the compendium cited in Section 2) gives a table that marks which note applies to each size and to companies under the simplified tax regime. Read that table for the company's own case. The checklist below lists the main notes; it does not replace the PCG table.

**Notes checklist**

| # | Disclosure | Micro | Small and medium |
| --- | --- | --- | --- |
| 1 | Accounting principles and methods (PCG art. 831-1 onwards) | Exempt (no annexe) | Check the PCG table |
| 2 | Fixed asset, depreciation and impairment movements (PCG art. 832-1) | Exempt | Check the PCG table |
| 3 | Maturity of receivables and payables | Exempt | Check the PCG table |
| 4 | Related-party transactions not concluded on normal market terms (PCG art. 834-1) | Exempt | Check the PCG table |
| 5 | Off-balance-sheet commitments (PCG art. 836-1 onwards) | Exempt | Check the PCG table |
| 6 | Employee information (PCG art. 837-1 onwards) | Exempt | Check the PCG table |
| 7 | Advances, credits and commitments to the management bodies (PCG art. 835-1 onwards) | Exempt | Check the PCG table |
| 8 | Tax position (PCG art. 833-1 onwards) | Exempt | Check the PCG table |
| 9 | Provisions detail | Exempt | Check the PCG table |
| 10 | Financial instruments | Exempt | Check the PCG table |
| 11 | Equity movements | Exempt | Check the PCG table |
| 12 | Retirement commitments not provided for | Exempt | Check the PCG table |

## Section 9: Approval, appropriation and filing

**Approval of the accounts.** In an SA, a SARL and an EURL the accounts must be approved within 6 months of the end of the financial year. In a SAS or SASU the partners set the period freely; the page says 6 months is the usual practice because a dividend must be paid within 9 months of the year end. Where the sole partner of a SASU or EURL is also its sole manager, the approval decision does not have to be filed. A société civile immobilière (SCI) need not draw up annual accounts unless it has a commercial activity, has opted for corporation tax, is liable to VAT, has a partner subject to corporation tax or to the industrial and commercial profits regime, has a clause in its statutes, or exceeds 2 of the 3 SCI thresholds; even then, filing at the greffe is not compulsory for it (same page).

**Filing.** The legal representative files within 1 month after the approval, or within 2 months after the approval when filing electronically. Online filing is on the guichet des formalités des entreprises, by the director or an agent (for example an expert-comptable or a lawyer), in PDF with each file no larger than 10 Mo, signed with an advanced electronic signature or through FranceConnect+.

**Documents to file.** The comptes annuels (Section 4), the minutes of the meeting with the proposed and voted appropriation of the result, the CAC report if there is one, the rapport de gestion for a medium-sized company, and for a group the consolidated accounts, the group management report and the auditors' report on them. Several tabs of the page add that the rapport de gestion is not filed at the greffe but is kept available to anyone who asks.

**Confidentiality, by size.**
- Micro-enterprise: the accounts are not published if the company attaches a confidentiality declaration; the CAC report is then not published either.
- Small enterprise: the compte de résultat is not published if the company attaches a confidentiality declaration. In the SAS tab only, the page says the annual accounts as a whole; see changes.md section 6.
- Medium enterprise: the page offers no confidentiality declaration; the company may ask that only a simplified presentation of its bilan and annexe be published, in which case the CAC report need not be attached.

**Penalties and court orders**

| Item | Value | Note (verbatim, page checked by its publisher on 11 juin 2025) |
| --- | --- | --- |
| Source | all figures below | https://entreprendre.service-public.gouv.fr/vosdroits/F31214 |
| Criminal fine on the director for not filing | EUR 1,500 | "le dirigeant de la société s'expose à une amende pénale de 1 500 €" |
| Fine on a repeat failure | EUR 3,000 | "En cas de récidive, l'amende passe à 3 000 €" |
| Time limit for prosecution | 1 year from the date the accounts were due | "peut être poursuivie pendant un délai de 1 an à compter de la date à laquelle les comptes auraient dû être déposés" |
| Civil order (injonction) | The president of the tribunal de commerce may order filing within one month, often with a daily penalty (astreinte) | "le président du tribunal de commerce peut adresser au dirigeant une injonction de les déposer dans le délai d'un mois" |
| Approval deadline, SA and SARL/EURL | Within 6 months of the year end | "L’approbation des comptes doit intervenir dans les 6 mois de la clôture de l’exercice" |
| Approval deadline, SAS/SASU | Set freely by the partners | "dans un délai librement fixé par les associés" |
| Filing deadline | 1 month after approval; 2 months if electronic | "Dans les 2 mois suivant l'approbation des comptes par l'assemblée ordinaire des actionnaires ou de l’actionnaire unique lorsque le dépôt est fait par voie électronique" |

**Appropriation of the result: the legal reserve**

| Item | Value | Note (verbatim, page checked by its publisher on 10 avril 2024) |
| --- | --- | --- |
| Source | all figures below | https://entreprendre.service-public.gouv.fr/vosdroits/F24024 |
| Transfer to the legal reserve, out of each year's profit, at least | 5% | "Elle est constituée par un prélèvement d'au moins 5 % réalisé sur le bénéfice de chaque exercice" |
| The transfer stops being compulsory when the reserve reaches this share of the share capital | 10% | "Ce prélèvement cesse d'être obligatoire lorsque la réserve légale atteint 10 % du capital social" |

The legal reserve cannot be distributed. The page calls it a reserve required by law and does not list the company forms it covers; see changes.md section 6.

## Section 10: Statutory audit (commissaire aux comptes)

**When a CAC is compulsory.** A company must appoint a CAC once it crosses 2 of the 3 thresholds in the table below. The thresholds are the same for the SARL, EURL, SA, SAS, SCA, SNC and SCS: an SA is not audited automatically. The duty does not cover the year in which the thresholds are first crossed; it starts with the following financial year. A company no longer needs a CAC once it has stayed below the thresholds at the close of the 2 financial years before the mandate expires. A CAC in office stays for the whole mandate even if the company falls below the thresholds soon after the appointment, and the mandates running on 1 March 2024 continue until they expire (A17100). Entities that must prepare consolidated accounts appoint 2 independent CACs. The page covers companies only, not associations and foundations.

**Auditor thresholds and sanctions**

| Item | Value | Note (verbatim, page checked by its publisher on 10 avril 2025) |
| --- | --- | --- |
| Source | all figures below | https://entreprendre.service-public.gouv.fr/vosdroits/F31440 |
| Independent company, and parent of a small group: balance sheet total | EUR 5,000,000 | "5 000 000 € de total bilan" |
| Independent company, and parent of a small group: turnover excluding VAT | EUR 10,000,000 | "10 000 000 € de chiffre d'affaires HT" |
| Independent company, and parent of a small group: employees | 50 employees | "10 000 000 € de chiffre d'affaires HT 50 salariés" |
| Company controlled by the parent of a small group: balance sheet total | EUR 2,500,000 | "2 500 000 € de total bilan" |
| Company controlled by the parent of a small group: turnover excluding VAT | EUR 5,000,000 | "5 000 000 € de chiffre d'affaires HT 25 salariés" |
| Company controlled by the parent of a small group: employees | 25 employees | "5 000 000 € de chiffre d'affaires HT 25 salariés" |
| Société civile with an economic activity: balance sheet total | EUR 1,550,000 | "1 550 000 € de total bilan" |
| Société civile with an economic activity: turnover excluding VAT | EUR 3,100,000 | "3 100 000 € de chiffre d'affaires HT 50 salariés" |
| Société civile with an economic activity: employees | 50 employees | "3 100 000 € de chiffre d'affaires HT 50 salariés" |
| How many thresholds | 2 of 3 crossed | "dès lors que 2 des 3 seuils suivants sont franchis" |
| Mandate length | 6 years, renewable; 3 years for a voluntary appointment | "6 ans renouvelable ou 3 ans en cas de désignation volontaire" |
| Not appointing a CAC when compulsory | 2 years' imprisonment and a fine of EUR 30,000 | "passible d'un emprisonnement de 2 ans et d'une amende de 30 000 €" |
| Partners' request to a judge below the thresholds (SARL, SA, SAS, SCA) | One or more partners holding at least 10% of the capital; the judge may refuse | "un ou plusieurs associés représentant au moins 10 % du capital peuvent demander au juge la nomination d'un CAC" |

The parent-of-a-small-group row excludes public-interest entities and entities that must publish consolidated accounts. A voluntary appointment may also be decided by partners holding at least one third of the capital. In an SNC or an SCS a single partner may ask the judge.

**Auditor qualification.** Only a commissaire aux comptes may sign the audit report. The live list of CACs and their professional body should be checked on the profession's own register; this skill does not cite it.

## Section 11: The corporation tax return that goes with the accounts

**Corporation tax return (impôt sur les sociétés)**

| Item | Rule | Note (verbatim, page checked by its publisher on 17 février 2026) |
| --- | --- | --- |
| Source | all rules below | https://entreprendre.service-public.gouv.fr/vosdroits/F23575 |
| Return, simplified regime | Déclaration n° 2065 with the liasse fiscale, tables 2033 A to 2033 G | "Déclaration de résultat n° 2065 Liasse fiscale (tableaux n° 2033 A à 2033 G)" |
| Return, normal regime | Déclaration n° 2065 with the liasse fiscale, tables 2050 to 2059 | "Déclaration de résultat n° 2065 Liasse fiscale (tableaux n° 2050 à 2059)" |
| Deadline, year not ending on 31 December | Within 3 months of the year end | "La déclaration de résultat doit être souscrite, en principe, dans les 3 mois de la clôture de l’exercice" |
| Deadline, year ending on 31 December | The 2nd working day after 1 May, plus 15 calendar days for electronic filing | "L'administration fiscale accorde un délai supplémentaire de 15 jours calendaires" |
| Year closed on 31 December 2025 | 20 May 2026 | "Exercice clos le 31/12/2025 Au plus tard le 2 e jour ouvré suivant le 1 er mai 20/05/2026 (compte tenu du délai de 15 jours supp.)" |
| Filing channel | Electronic only. Simplified regime: EFI on the professional space, or EDI through an agent. Normal regime: EDI-TDFC through an EDI partner only | "La société doit obligatoirement réaliser sa déclaration par voie électronique en mode EDI-TDFC" |

## Sources

- Accounting obligations of a commercial company, size categories, simplified regime, record keeping: https://entreprendre.service-public.gouv.fr/vosdroits/F37169
- Filing the annual accounts, approval deadlines, confidentiality, penalties: https://entreprendre.service-public.gouv.fr/vosdroits/F31214
- Statutory auditor: https://entreprendre.service-public.gouv.fr/vosdroits/F31440
- Equity, reserves and the legal reserve: https://entreprendre.service-public.gouv.fr/vosdroits/F24024
- New size thresholds from 2024 (news item of 5 March 2024): https://entreprendre.service-public.gouv.fr/actualites/A17100
- Management report exemption for micro-enterprises (news item of 14 May 2025): https://entreprendre.service-public.gouv.fr/actualites/A18259
- Corporation tax return and deadlines: https://entreprendre.service-public.gouv.fr/vosdroits/F23575
- Employee profit-sharing: https://www.service-public.gouv.fr/particuliers/vosdroits/F2141
- CVAE rates and thresholds (BOFiP): https://bofip.impots.gouv.fr/bofip/839-PGP.html
- PCG and French accounting standards, consolidated compendium of 1 January 2026 (ANC): https://www.anc.gouv.fr/files/anc/files/1_Normes_fran%C3%A7aises/recueil/2026/Recueil-PCG-Janvier-2026.pdf

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional before filing or acting upon.

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
