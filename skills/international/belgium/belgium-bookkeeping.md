---
name: belgium-bookkeeping
description: "Belgian bookkeeping for financial years running in 2026: who must keep books under the Code of Economic Law (WER / CDE art. III.82 to III.95), double-entry books for every company, the simplified three-journal method for sole traders, general partnerships and limited partnerships with turnover up to EUR 500,000 (EUR 620,000 for fuel retailers), the minimum chart of accounts (MAR / PCMN) in annex 1 to the Royal Decree of 21 October 2018, the 2019 valuation rules, the balance sheet and profit and loss schemes, the 2026 size criteria (micro, small, large), the 2026 NBB filing costs, retention periods and the links to corporate tax and VAT. Trigger on: Belgian bookkeeping, PCMN, MAR, minimumindeling, plan comptable minimum normalisé, boekhoudwet, single-entry books Belgium, jaarrekening, comptes annuels, chart of accounts Belgium. Out of scope: filing the accounts in depth (belgium-financial-statements), e-invoicing (belgium-einvoice), VAT returns (be-vat-return), corporate tax (be-corporate-tax), payroll (belgium-payroll)."
version: 1.1
jurisdiction: BE
category: bookkeeping
tax_year: 2026
last_updated: 2026-10-30
review_status: pending_review
trust_label: Built by Michael Cutajar and the OpenAccountants team
depends_on:
  - bookkeeping-workflow-base
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Belgium Bookkeeping

Figures and rules below apply to financial years running in 2026. Each line names its source; the full list is in Sources at the end. The law texts were read in the consolidated Justel database (ejustice.just.fgov.be) on 2026-10-30.

## Section 1 -- Quick Reference

**Quick Reference**

| Field | Value |
| --- | --- |
| Country | Belgium (Koninkrijk België / Royaume de Belgique) |
| Currency | EUR |
| Financial year | Normally 12 months. An exceptional year may be shorter or longer, but not longer than 24 months less one day (WVV art. 1:24 § 4) |
| Who must keep books | Every self-employed person, every Belgian company and organisation with legal personality, and Belgian branches of foreign businesses (WER art. III.82 § 1) |
| Method | Double entry for all (WER art. III.84); simplified three journals only for sole traders, organisations without legal personality, general partnerships (VOF / SNC) and ordinary limited partnerships (CommV / SComm) with turnover up to EUR 500,000 (WER art. III.85 § 1; KB 21 October 2018 art. 1) |
| Accounting rules | Valuation rules and schemes of the Royal Decree of 29 April 2019 executing the Companies and Associations Code (KB WVV / AR CSA) |
| Standard chart of accounts | Minimumindeling van het algemeen rekeningenstelsel (MAR) / Plan comptable minimum normalisé (PCMN), annex 1 to the Royal Decree of 21 October 2018 (art. 10) |
| Standard-setter | Commissie voor Boekhoudkundige Normen (CBN) / Commission des Normes Comptables (CNC) (WER art. III.93) |
| Companies law | Wetboek van vennootschappen en verenigingen (WVV) / Code des sociétés et des associations (CSA) |
| Filing of annual accounts | National Bank of Belgium (NBB / BNB), within 30 days after approval and at the latest 7 months after year-end (WVV art. 3:12 § 1) |
| Tax authority | FOD Financiën / SPF Finances |
| Retention of books | 7 years from 1 January of the year after the year-end (KB 21 October 2018 art. 8) |

## Section 2 -- Standard Chart of Accounts (MAR / PCMN)

The minimum chart binds every business that must keep books, except Belgian branches of foreign businesses that have no income of their own, and except associations and foundations, which have their own chart (KB 21 October 2018 art. 9, 10, 12). The account names may be adapted to the business, and accounts that are not needed may be left out (art. 11). The chart below follows the official CBN text. The balance sheet uses classes 1 to 5; the profit and loss account uses classes 6 and 7. Where the chart fixes no sub-account (for example 610 to 616), the business sets its own breakdown.

### Class 1 -- Equity, provisions and amounts payable after more than one year

**Class 1 -- Equity, provisions and amounts payable after more than one year**

| Code | Account (NL / FR) | English |
| --- | --- | --- |
| 10 | Kapitaal / Capital | Capital |
| 100 | Geplaatst kapitaal | Issued capital |
| 101 | Niet opgevraagd kapitaal (-) | Uncalled capital |
| 11 | Inbreng buiten kapitaal / Apport hors capital | Contribution outside capital |
| 12 | Herwaarderingsmeerwaarden / Plus-values de réévaluation | Revaluation surpluses |
| 13 | Reserves / Réserves | Reserves |
| 130 | Wettelijke reserves / Réserves légales | Legal reserves |
| 131 | Andere onbeschikbare reserves / Autres réserves indisponibles | Other unavailable reserves |
| 133 | Beschikbare reserves / Réserves disponibles | Available reserves |
| 14 | Overgedragen winst of verlies / Bénéfice ou perte reporté(e) | Profit or loss brought forward |
| 15 | Kapitaalsubsidies / Subsides en capital | Capital grants |
| 16 | Voorzieningen en uitgestelde belastingen / Provisions et impôts différés | Provisions and deferred taxes |
| 160 | Voorzieningen voor pensioenen | Provisions for pensions |
| 168 | Uitgestelde belastingen | Deferred taxes |
| 17 | Schulden op meer dan één jaar / Dettes à plus d'un an | Amounts payable after more than one year |
| 170 | Achtergestelde leningen / Emprunts subordonnés | Subordinated loans |
| 172 | Leasingschulden / Dettes de location-financement | Leasing and similar obligations |
| 173 | Kredietinstellingen / Établissements de crédit | Credit institutions (bank loans) |
| 175 | Handelsschulden / Dettes commerciales | Trade debts |

### Class 2 -- Formation expenses, fixed assets and amounts receivable after more than one year

**Class 2 -- Formation expenses, fixed assets and long-term receivables**

| Code | Account (NL / FR) | English |
| --- | --- | --- |
| 20 | Oprichtingskosten / Frais d'établissement | Formation expenses |
| 200 | Kosten van oprichting of kapitaalverhoging | Formation or capital increase costs |
| 201 | Kosten bij uitgifte van leningen | Loan issue expenses |
| 204 | Herstructureringskosten | Restructuring costs |
| 21 | Immateriële vaste activa / Immobilisations incorporelles | Intangible fixed assets |
| 210 | Kosten van onderzoek en ontwikkeling | Research and development costs |
| 211 | Concessies, octrooien, licenties, knowhow, merken | Concessions, patents, licences, know-how, brands |
| 212 | Goodwill | Goodwill |
| 22 | Terreinen en gebouwen / Terrains et constructions | Land and buildings |
| 23 | Installaties, machines en uitrusting / Installations, machines et outillage | Plant, machinery and equipment |
| 24 | Meubilair en rollend materieel / Mobilier et matériel roulant | Furniture and vehicles |
| 25 | Vaste activa in leasing / Immobilisations détenues en location-financement | Assets held under leasing |
| 26 | Overige materiële vaste activa / Autres immobilisations corporelles | Other tangible fixed assets |
| 27 | Vaste activa in aanbouw en vooruitbetalingen / Immobilisations en cours et acomptes | Assets under construction and advance payments |
| 28 | Financiële vaste activa / Immobilisations financières | Financial fixed assets |
| 280 | Deelnemingen in verbonden ondernemingen | Participations in affiliated companies |
| 288 | Borgtochten betaald in contanten | Cash guarantees paid |
| 29 | Vorderingen op meer dan één jaar / Créances à plus d'un an | Amounts receivable after more than one year |

### Class 3 -- Stocks and contracts in progress

**Class 3 -- Stocks and contracts in progress**

| Code | Account (NL / FR) | English |
| --- | --- | --- |
| 30 | Grondstoffen / Matières premières | Raw materials |
| 31 | Hulpstoffen / Approvisionnements et fournitures | Consumables |
| 32 | Goederen in bewerking / En-cours de fabrication | Work in progress |
| 33 | Gereed product / Produits finis | Finished goods |
| 34 | Handelsgoederen / Marchandises | Goods for resale |
| 35 | Onroerende goederen bestemd voor verkoop / Immeubles destinés à la vente | Property held for sale |
| 36 | Vooruitbetalingen op voorraadinkopen / Acomptes versés sur achats pour stocks | Advance payments on stock purchases |
| 37 | Bestellingen in uitvoering / Commandes en cours d'exécution | Contracts in progress |

### Class 4 -- Amounts receivable and payable within one year

**Class 4 -- Amounts receivable and payable within one year**

| Code | Account (NL / FR) | English |
| --- | --- | --- |
| 40 | Handelsvorderingen / Créances commerciales | Trade receivables |
| 400 | Handelsdebiteuren / Clients | Customers |
| 401 | Te innen wissels / Effets à recevoir | Bills receivable |
| 411 | Terug te vorderen btw / TVA à récupérer | VAT recoverable (input VAT) |
| 44 | Handelsschulden / Dettes commerciales | Trade payables |
| 440 | Leveranciers / Fournisseurs | Suppliers |
| 441 | Te betalen wissels / Effets à payer | Bills payable |
| 45 | Schulden m.b.t. belastingen, bezoldigingen en sociale lasten / Dettes fiscales, salariales et sociales | Tax, pay and social security payables |
| 450 | Geraamd bedrag der belastingschulden / Dettes fiscales estimées | Estimated taxes payable |
| 451 | Te betalen btw / TVA à payer | VAT payable (output VAT) |
| 452 | Te betalen belastingen en taksen / Impôts et taxes à payer | Taxes payable |
| 453 | Ingehouden voorheffingen / Précomptes retenus | Withholding taxes |
| 454 | Rijksdienst voor Sociale Zekerheid / Office national de la Sécurité sociale | Social security (RSZ / ONSS) |
| 455 | Bezoldigingen / Rémunérations | Wages payable |
| 46 | Vooruitbetalingen op bestellingen / Acomptes sur commandes | Advance payments received |
| 48 | Diverse schulden / Dettes diverses | Sundry payables |
| 49 | Overlopende rekeningen / Comptes de régularisation | Accruals and deferred income |
| 490 | Over te dragen kosten / Charges à reporter | Deferred charges |
| 491 | Verkregen opbrengsten / Produits acquis | Accrued income |
| 492 | Toe te rekenen kosten / Charges à imputer | Accrued charges |
| 493 | Over te dragen opbrengsten / Produits à reporter | Deferred income |

### Class 5 -- Current investments and cash

**Class 5 -- Current investments and cash**

| Code | Account (NL / FR) | English |
| --- | --- | --- |
| 50 | Eigen aandelen / Actions propres | Own shares |
| 51 | Aandelen en geldbeleggingen / Actions, parts et placements | Shares and other investments |
| 52 | Vastrentende effecten / Titres à revenu fixe | Fixed-income securities |
| 53 | Termijndeposito's / Dépôts à terme | Term deposits |
| 55 | Kredietinstellingen / Établissements de crédit (550 to 559) | Bank accounts, one sub-account per bank |
| 57 | Kassen / Caisses (570 to 577) | Cash in hand |
| 58 | Interne overboekingen / Virements internes | Internal transfers |

### Class 6 -- Charges

**Class 6 -- Charges**

| Code | Account (NL / FR) | English |
| --- | --- | --- |
| 60 | Handelsgoederen, grond- en hulpstoffen / Approvisionnements et marchandises | Purchases of goods and materials |
| 600 | Aankopen van grondstoffen | Purchases of raw materials |
| 601 | Aankopen van hulpstoffen | Purchases of consumables |
| 604 | Aankopen van handelsgoederen | Purchases of goods for resale |
| 609 | Voorraadwijzigingen | Changes in stock |
| 61 | Diensten en diverse goederen / Services et biens divers | Services and other goods (rent, maintenance, energy, insurance, fees, advertising, telecoms: the business sets the breakdown) |
| 617 | Uitzendkrachten / Personnel intérimaire | Temporary staff and staff made available |
| 618 | Bezoldigingen van bestuurders en zaakvoerders (niet onder arbeidsovereenkomst) | Pay of directors and managers not under an employment contract |
| 62 | Bezoldigingen, sociale lasten en pensioenen / Rémunérations, charges sociales et pensions | Staff costs |
| 620 | Bezoldigingen en rechtstreekse sociale voordelen | Wages and direct benefits |
| 621 | Werkgeversbijdragen voor sociale verzekeringen | Employer social security contributions |
| 622 | Werkgeverspremies voor bovenwettelijke verzekeringen | Employer premiums for extra-legal insurance (group insurance) |
| 623 | Andere personeelskosten | Other staff costs |
| 624 | Ouderdoms- en overlevingspensioenen | Retirement and survivor pensions |
| 63 | Afschrijvingen, waardeverminderingen en voorzieningen | Depreciation, write-downs and provisions |
| 630 | Afschrijvingen en waardeverminderingen op vaste activa | Depreciation and write-downs on fixed assets |
| 631 | Waardeverminderingen op voorraden | Write-downs on stock |
| 634 | Waardeverminderingen op handelsvorderingen | Write-downs on trade receivables |
| 635 | Voorzieningen voor pensioenen | Provisions for pensions |
| 64 | Andere bedrijfskosten / Autres charges d'exploitation | Other operating charges |
| 640 | Bedrijfsbelastingen | Operating taxes |
| 641 | Minderwaarden op courante realisatie van vaste activa | Losses on ordinary disposal of fixed assets |
| 65 | Financiële kosten / Charges financières | Financial charges |
| 650 | Kosten van schulden | Interest and debt charges |
| 653 | Discontokosten op vorderingen | Discount charges on receivables |
| 654 | Wisselresultaten | Exchange differences |
| 66 | Niet-recurrente bedrijfs- of financiële kosten / Charges non récurrentes | Non-recurring operating or financial charges |
| 67 | Belastingen op het resultaat / Impôts sur le résultat | Income taxes |
| 670 | Belgische belastingen op het resultaat van het boekjaar | Belgian income tax for the year |
| 68 | Overboeking naar uitgestelde belastingen en belastingvrije reserves | Transfer to deferred taxes and untaxed reserves |
| 69 | Resultaatverwerking | Appropriation of profit |

### Class 7 -- Income

**Class 7 -- Income**

| Code | Account (NL / FR) | English |
| --- | --- | --- |
| 70 | Omzet / Chiffre d'affaires (700 to 707 sales and services) | Turnover |
| 71 | Wijzigingen in de voorraden en bestellingen in uitvoering | Change in stocks and contracts in progress |
| 72 | Geproduceerde vaste activa / Production immobilisée | Own work capitalised |
| 74 | Andere bedrijfsopbrengsten / Autres produits d'exploitation | Other operating income |
| 740 | Bedrijfssubsidies en compenserende bedragen | Operating subsidies |
| 75 | Financiële opbrengsten / Produits financiers | Financial income |
| 750 | Opbrengsten uit financiële vaste activa | Income from financial fixed assets |
| 751 | Opbrengsten uit vlottende activa | Income from current assets (for example interest received) |
| 753 | Kapitaal- en interestsubsidies | Capital and interest subsidies |
| 754 | Wisselresultaten | Exchange differences |
| 76 | Niet-recurrente bedrijfs- of financiële opbrengsten | Non-recurring income |
| 77 | Regularisering van belastingen en terugneming van fiscale voorzieningen | Tax adjustments and release of tax provisions |
| 78 | Onttrekkingen aan belastingvrije reserves en uitgestelde belastingen | Release of untaxed reserves and deferred taxes |
| 79 | Resultaatverwerking | Appropriation of profit |

Corrections against the 2025 version of this skill: 172 is leasing and 173 is credit institutions (not the reverse); 27 is assets under construction and 28 financial fixed assets (28 is not accumulated depreciation); 617 is temporary staff and 618 directors' pay (not fees and advertising); 631 is the stock write-down and 634 the trade receivables write-down; 622 is group insurance and 623 other staff costs; 653 is discount charges, not bank charges; 753 is capital and interest subsidies, not interest received; classes 66 and 76 are "non-recurring", not "exceptional"; the chart has no postal account 56 and no fixed sub-accounts 610 to 616 or 240 to 242.

## Section 3 -- Revenue Recognition and the Books

### Which method

**Which method**

| Entity | Method | Source |
| --- | --- | --- |
| Every company with legal personality (NV / SA, BV / SRL, CV / SC and others) | Double entry, always | WER art. III.84 |
| Sole trader (natural person), organisation without legal personality, VOF / SNC, ordinary CommV / SComm | Simplified (three journals) if last year's turnover excluding VAT is at most EUR 500,000; otherwise double entry | WER art. III.85 § 1; KB 21 October 2018 art. 1 |
| Same, if the main activity is retail sale of road fuel | Simplified if turnover is at most EUR 620,000 | KB 21 October 2018 art. 1, second paragraph |
| Natural person whose only self-employed activity is holding director mandates | No bookkeeping obligation | WER art. III.82 § 1, second paragraph, 1° |

- **Simplified books.** At least three journals: (1) cash and bank movements, with withdrawals not for the business shown separately and daily cash balances; (2) purchases, imports and services received; (3) sales, exports and services supplied, with withdrawals in kind (WER art. III.85 § 1).
- **Year not 12 months.** The EUR 500,000 and EUR 620,000 limits are scaled by the number of months, each started month counting in full (KB 21 October 2018 art. 2).
- **Starters.** In the first year the simplified method may be used if a good-faith forecast shows turnover will not exceed the limit (KB 21 October 2018 art. 3).
- **Double-entry books.** All transactions are booked without delay, faithfully, completely and in date order in a journal or sub-journals, and summarised in a central ledger at least once a month (WER art. III.84). Every entry refers to a dated supporting document (WER art. III.86).
- **Inventory and annual accounts.** At least once a year the business takes stock of all assets and liabilities (WER art. III.89 § 1) and summarises the reconciled accounts in annual accounts (WER art. III.90 § 1).
- **Prudence and accruals.** Valuations must meet the requirements of prudence, sincerity and good faith (KB WVV art. 3:10). All foreseeable risks, possible losses and falls in value of the year or earlier years are taken into account, even if they become known only between the balance sheet date and the date the accounts are drawn up; income and charges of the year are booked whatever the day they are paid or received, unless collection of the income is uncertain (KB WVV art. 3:11).
- **Stock.** Stock is valued at cost, or at market value at the balance sheet date if lower (KB WVV art. 3:47).
- **Contracts in progress.** Valued at cost plus margin as the work progresses, where the margin is reasonably certain. A company may instead keep them at cost until completion (KB WVV art. 3:49). Both methods are allowed; the 2025 version said completed contract was "the norm", which the decree does not say.
- **Cost of identical items.** Specific identification, weighted average, FIFO or LIFO (KB WVV art. 3:21).
- **VAT and invoices.** VAT timing and invoicing are in [be-vat-return](be-vat-return.md) and [belgium-vat-return](belgium-vat-return.md). From 1 January 2026 invoices between Belgian VAT-registered businesses are structured e-invoices: see [belgium-einvoice](belgium-einvoice.md).

## Section 4 -- Expense Classification

### Deductible expenses (key categories)

Business costs are booked in class 6 under the chart above. For company tax, the starting point is the accounting profit, adjusted by the disallowed expenses (verworpen uitgaven / dépenses non admises): see [be-corporate-tax](be-corporate-tax.md).

**Typical bookings**

| Category | MAR code | Tax note |
| --- | --- | --- |
| Rent, maintenance, energy, insurance, fees, advertising, telecoms, software | 61 (own breakdown) | Deductible when incurred for the business |
| Temporary staff | 617 | Deductible |
| Directors' pay outside an employment contract | 618 | Deductible; also drives the director pay test for the 20% rate in be-corporate-tax |
| Wages and employer social security | 620, 621 | Deductible |
| Group insurance premiums | 622 | Deductible within the limits in be-corporate-tax |
| Interest | 650 | Deductible subject to the interest limits in be-corporate-tax |
| Operating taxes (for example property tax) | 640 | Deductible |
| Income tax | 670 | Not deductible |

### Partly or non-deductible expenses

**Partly or non-deductible expenses (company tax)**

| Category | Rule | Source |
| --- | --- | --- |
| Restaurant costs | 31% disallowed (69% deductible) | WIB 92 art. 53, 8°bis; FOD Financiën notes to the corporate tax return, AY 2026 |
| Reception costs and business gifts | 50% disallowed | WIB 92 art. 53, 8°; same notes |
| Restaurant, reception and gift costs recharged to a third party and shown separately on the invoice | Stay deductible | WIB 92 art. 53/1; same notes |
| Fines, including administrative fines, and increases of social contributions | Not deductible | WIB 92 art. 53, 6°; same notes |
| Non-specific work clothing (and allowances paid to others for it) | Not deductible, unless recharged to a third party and shown separately on the invoice | WIB 92 art. 53, 7° and 53/1; same notes |
| Car costs | Deductible share set by a CO2 formula and the date the car was bought, leased or rented | WIB 92 art. 66 and 198bis; details in be-corporate-tax and be-income-tax |

- **Car formula, for reference.** The non-deductible share is 60% where emissions are 200 g CO2/km or more or unknown. Otherwise it is 100% - [120% - (0.5% x coefficient x g CO2/km)], with coefficient 1 for diesel-only cars and 0.95 for other cars (0.90 for natural gas cars under 12 fiscal HP). For cars bought, leased or rented before 1 July 2023 the non-deductible share from the formula cannot exceed 50% (FOD Financiën notes, AY 2026). For cars bought, leased or rented from 1 July 2023 to 31 December 2025 the AY 2026 notes (income 2025) set the non-deductible share at no less than 25%, unless the car emits no CO2. That floor is for income 2025 only: the Law of 18 December 2025 rewrote the transitional rule for cars bought, leased or rented before 1 January 2026 (art. 26, WIB 92 art. 550), and the 2026 percentage for these cars is in be-corporate-tax and be-income-tax. The same law (art. 23) added deduction caps for plug-in hybrids in a new art. 66 § 1/1. Use be-corporate-tax for the 2026 percentage of a given car.

## Section 5 -- Asset vs Expense Thresholds

### Capitalisation rules

**Capitalisation rules**

| Rule | Detail | Source |
| --- | --- | --- |
| Fixed assets with limited life | Depreciated under a plan set in the valuation rules | KB WVV art. 3:42 § 1 |
| Formation expenses | Either expensed in the year or capitalised and written off by yearly instalments of at least 20% (so over at most 5 years); loan issue costs may follow the loan term | KB WVV art. 3:36, 3:37 |
| Self-made intangibles (development) | Capitalised at cost only up to a prudent estimate of value in use or future return | KB WVV art. 3:38 |
| Development costs and goodwill | Written off over at most 10 years where the useful life cannot be estimated reliably; goodwill write-offs are never reversed | KB WVV art. 3:39 § 1 |
| Assets with unlimited life (land) | Not depreciated; written down only for a lasting loss in value | KB WVV art. 3:42 § 2 |
| Revaluation | Allowed for tangible and financial fixed assets whose value durably exceeds book value; the surplus goes to the revaluation surplus (Herwaarderingsmeerwaarden) in equity, and depreciation follows the revalued amount over the remaining life | KB WVV art. 3:35 |
| De minimis threshold | The law sets none | No threshold appears in WER, the KB of 21 October 2018 or the KB WVV |

The 2025 version said goodwill and intangibles are written off over a minimum of 5 years. The decree sets a maximum of 10 years for goodwill and development costs where the life cannot be estimated, and at least 20% a year only for formation expenses.

### Depreciation methods

**Depreciation methods**

| Topic | Rule | Source |
| --- | --- | --- |
| Accounting plan | Method set in the valuation rules; accelerated depreciation allowed under tax rules, with the excess over economic depreciation disclosed in the notes | KB WVV art. 3:39, 3:42 |
| Declining balance for company tax | Only for assets acquired or created before 1 January 2020 | WIB 92 art. 196 § 3, as stated in the FOD Financiën notes, AY 2026 |
| Extra or non-recurring write-off | Where technical or economic change makes book value exceed value in use | KB WVV art. 3:42 § 1 |

- The 2025 version said SMEs kept the declining-balance option after 2020. The AY 2026 notes say declining balance is only available for assets acquired or created before 1 January 2020, with no SME exception for companies.
- Usual rates per asset class are administrative practice, not law; see the "Not yet confirmed" line.

## Section 6 -- P&L Format (Resultatenrekening / Compte de résultats)

The full scheme is in annex 3 to the KB WVV (art. 3:81). Small companies use the abbreviated scheme in annex 4 (art. 3:84), which starts with the gross margin; micro companies use the same layout (art. 3:87). See [belgium-financial-statements](belgium-financial-statements.md) for the size test.

### Full scheme (by nature)

**P&L full scheme (KB WVV annex 3)**

```
I.    Bedrijfsopbrengsten (Operating income)
      A. Omzet (Turnover)
      B. Change in work in progress, finished goods and contracts in progress
      C. Geproduceerde vaste activa (Own work capitalised)
      D. Andere bedrijfsopbrengsten (Other operating income)
      E. Niet-recurrente bedrijfsopbrengsten (Non-recurring operating income)
II.   Bedrijfskosten (Operating charges)
      A. Goods for resale, raw materials and consumables
      B. Diensten en diverse goederen (Services and other goods)
      C. Pay, social security and pensions
      D. Depreciation and write-downs on formation expenses and fixed assets
      E. Write-downs on stock, contracts in progress and trade receivables
      F. Provisions for liabilities and charges
      G. Andere bedrijfskosten (Other operating charges)
      H. Operating charges capitalised as restructuring costs (-)
      I. Niet-recurrente bedrijfskosten (Non-recurring operating charges)
III.  Bedrijfswinst / Bedrijfsverlies (Operating profit or loss)
IV.   Financiële opbrengsten (recurring A to C, non-recurring D)
V.    Financiële kosten (recurring A to C, non-recurring D)
VI.   Winst / verlies van het boekjaar vóór belasting
VII.  A. Release of deferred taxes  B. Transfer to deferred taxes
VIII. Belastingen op het resultaat (Income taxes)
IX.   Winst / verlies van het boekjaar
X.    A. Release of untaxed reserves  B. Transfer to untaxed reserves
XI.   Te bestemmen winst / verlies van het boekjaar (Profit to appropriate)
```

**Abbreviated and micro scheme (KB WVV annex 4).** I.A.B gross margin (with non-recurring operating income shown inside it), then C to I as above, II operating result, III financial income, IV financial charges, V result before tax, VI deferred taxes, VII income taxes, VIII result for the year, IX untaxed reserves, X profit to appropriate.

The 2025 version showed "exceptional" income and charges as separate headings. That layout is gone: non-recurring items now sit inside operating and financial results.

## Section 7 -- Balance Sheet Format (Balans / Bilan)

The full balance sheet is in annex 3 to the KB WVV (art. 3:80); small and micro companies use the abbreviated version in annex 4 (art. 3:83, 3:86).

### Full scheme

**Balance sheet (KB WVV annex 3)**

```
ACTIVA (Assets)
  I.    Oprichtingskosten (Formation expenses)
VASTE ACTIVA (Fixed assets)
  II.   Immateriële vaste activa
  III.  Materiële vaste activa
  IV.   Financiële vaste activa
VLOTTENDE ACTIVA (Current assets)
  V.    Vorderingen op meer dan een jaar
  VI.   Voorraden en bestellingen in uitvoering
  VII.  Vorderingen op ten hoogste een jaar
  VIII. Geldbeleggingen
  IX.   Liquide middelen
  X.    Overlopende rekeningen
TOTAAL VAN DE ACTIVA

PASSIVA (Equity and liabilities)
EIGEN VERMOGEN (Equity)
  I.    Inbreng (NV: A. Kapitaal, B. Buiten kapitaal / BV and others: A. Beschikbaar, B. Onbeschikbaar)
  II.   Herwaarderingsmeerwaarden
  III.  Reserves
  IV.   Overgedragen winst / verlies
  V.    Kapitaalsubsidies
  VI.   Voorschot aan de vennoten op de verdeling van het netto-actief (-)
VOORZIENINGEN EN UITGESTELDE BELASTINGEN
  VII.  A. Voorzieningen voor risico's en kosten  B. Uitgestelde belastingen
SCHULDEN (Liabilities)
  VIII. Schulden op meer dan een jaar
  IX.   Schulden op ten hoogste een jaar
  X.    Overlopende rekeningen
TOTAAL VAN DE PASSIVA
```

Equity heading I is "Inbreng" (contribution). A BV shows available and unavailable contribution instead of capital. Debts are headings VIII to X; the 2025 version used the old numbers IX to XI.

## Section 8 -- Bank Reconciliation Patterns

- Every booking needs a dated supporting document (WER art. III.86). Bank statements are the supporting document for class 55 entries.
- Supporting documents are kept 7 years, in original or copy; documents that are not evidence against third parties are kept 3 years (WER art. III.86).
- Bank accounts go in 550 to 559, one sub-account per bank; cash in 570 to 577; transfers between own accounts pass through 58 (MAR).
- Tax payments clear 450 to 453 and 411 / 451; RSZ / ONSS payments clear 454; net wages clear 455 (MAR).
- Statement file formats and payment references are bank practice, not law; see the "Not yet confirmed" line.

## Section 9 -- Micro-Entity / Small Business Simplifications

### Size criteria (WVV art. 1:24 and 1:25)

**Size criteria**

| Category | Annual average staff (FTE) | Net turnover excl. VAT | Balance sheet total |
| --- | --- | --- | --- |
| Micro (not a parent or subsidiary) | 10 | EUR 900,000 | EUR 450,000 |
| Small | 50 | EUR 11,250,000 | EUR 6,000,000 |
| Large | More than one small criterion exceeded | | |

- A company is small (or micro) if, on the balance sheet date of the last closed year, it exceeds no more than one criterion (WVV art. 1:24 § 1, 1:25 § 1). The EUR 11,250,000, 6,000,000, 900,000 and 450,000 amounts were set by the Law of 28 March 2024 (in force 8 April 2024).
- A change counts only when it happens two years in a row; the new class applies from the following year (art. 1:24 § 2).
- Starters estimate the figures in good faith at the start of the first year (art. 1:24 § 3).
- Turnover is scaled for a year that is not 12 months (art. 1:24 § 4). Staff is the FTE average registered in Dimona at each month-end (art. 1:24 § 5).
- Linked companies: turnover and balance sheet total are measured on a consolidated basis and staff numbers are added up (art. 1:24 § 6). This applies only to parent companies (art. 1:24 § 7).

### Simplifications

**Simplifications**

| Feature | Micro | Small | Large | Source |
| --- | --- | --- | --- | --- |
| Accounts scheme | Micro scheme | Abbreviated scheme | Full scheme | WVV art. 3:2, 3:3; KB WVV art. 3:80 to 3:88 |
| Filing with NBB | Yes | Yes | Yes | WVV art. 3:10 |
| Statutory auditor (commissaris) | No, unless listed or part of a group that must consolidate | No, same exceptions | Yes | WVV art. 3:72 |
| Management report (jaarverslag) | No, unless listed | No, unless listed | Yes | WVV art. 3:4 |
| NBB filing cost 2026, XBRL | EUR 67.00 | EUR 89.40 | EUR 379.50 | NBB, history of filing costs 2026 |
| NBB filing cost 2026, PDF | EUR 137.30 | EUR 159.50 | EUR 449.70 | Same |
| Social balance sheet | Filed with the accounts | Filed with the accounts | Filed with the accounts | WVV art. 3:12 § 1, 8° |

Late filing surcharges and the full filing procedure are in [belgium-financial-statements](belgium-financial-statements.md).

### Sole traders and the self-employed (zelfstandigen / indépendants)

- Simplified three-journal books up to EUR 500,000 turnover excluding VAT; double entry above (WER art. III.85 § 1; KB 21 October 2018 art. 1).
- The books cover only the self-employed activity; own funds used in it are shown separately (WER art. III.83).
- Sole traders file no annual accounts with the NBB; their profit goes in the personal income tax return: see [be-income-tax](be-income-tax.md).
- Social contributions are paid to a social insurance fund: see [be-social-contributions](be-social-contributions.md).

## Section 10 -- Interaction with Tax Skills

### Corporate income tax (vennootschapsbelasting / impôt des sociétés)

- The annual accounts are the starting point: taxable profit is the accounting profit, adjusted by the tax corrections. Use [be-corporate-tax](be-corporate-tax.md) for the rates, the small-company rate test, the return and advance payments.
- Key add-backs from Section 4: 31% of restaurant costs, 50% of reception costs and gifts, the non-deductible share of car costs, non-specific work clothing, fines.

### VAT (btw / TVA)

- Input VAT is booked in 411 and output VAT in 451 (MAR).
- Return frequency, deadlines, the annual client listing and the intra-EU listing are in [be-vat-return](be-vat-return.md); rates and the small-business exemption are in [belgium-vat-return](belgium-vat-return.md).
- VAT records are kept 7 years: the Law of 18 December 2025 (art. 97) replaced "ten" by "seven" in VAT Code art. 60 § 3 and § 4, for VAT that became due from 1 January 2023 (art. 101).

### Social contributions and payroll

- Employer and employee RSZ / ONSS rates are in [belgium-payroll](belgium-payroll.md); withholding tax on pay in [be-payroll-withholding](be-payroll-withholding.md); self-employed contributions in [be-social-contributions](be-social-contributions.md).

## Sources

| Source | URL | Read on |
| --- | --- | --- |
| Code of Economic Law (WER), Book III, Title 3, art. III.82 to III.95 (Justel, consolidated) | https://www.ejustice.just.fgov.be/eli/wet/2013/02/28/2013A11134/justel | 2026-10-30 |
| Royal Decree of 21 October 2018 executing WER art. III.82 to III.95 (Justel, consolidated) | https://www.ejustice.just.fgov.be/eli/besluit/2018/10/21/2018014350/justel | 2026-10-30 |
| CBN / CNC, minimum chart of accounts (MAR / PCMN), NL-FR-EN | https://www.cnc-cbn.be/fr/node/2250/multilingual-comparison/nl-fr-en | 2026-10-30 |
| Companies and Associations Code (WVV), art. 1:24, 1:25, 3:1 to 3:14, 3:72 (Justel, consolidated) | https://www.ejustice.just.fgov.be/eli/wet/2019/03/23/2019A40586/justel | 2026-10-30 |
| Royal Decree of 29 April 2019 executing the WVV (valuation rules, annexes 3 and 4) (Justel, consolidated) | https://www.ejustice.just.fgov.be/eli/besluit/2019/04/29/2019011967/justel | 2026-10-30 |
| NBB, history of filing costs for companies, 2026 | https://www.nbb.be/doc/ba/tarif/2026/historiek%20van%20de%20neerleggingskosten%20van%20vennootschappen_2026_nl.pdf | 2026-10-30 |
| FOD Financiën, notes to the corporate tax return, assessment year 2026 (PDF) | https://financien.belgium.be/sites/default/files/downloads/121-aangifte-venb-toelichting-2026.pdf | 2026-10-30 |
| Law of 18 December 2025 on various provisions, art. 23, 25 and 26 (car costs), art. 97 and 101 (VAT retention) | https://www.ejustice.just.fgov.be/eli/wet/2025/12/18/2025009647/staatsblad | 2026-10-30 |

Not yet confirmed: classes 0, 8 and 9 of the chart (the CBN page read covers classes 1 to 7 only); the 2026 deductible percentage for each car category (art. 550 as rewritten by the Law of 18 December 2025 is amended again by art. 11 of the Law of 25 November 2021 with later effective dates; how the new art. 66 § 1/1 hybrid caps apply in company tax (art. 25 of the same law rewrites art. 198bis); the AY 2027 notes are not yet published and Fisconet was down on 2026-10-30, so the consolidated art. 66, 198bis and 550 could not be read); the restaurant and reception percentages were read in the AY 2026 notes, which cover income 2025, and no change for income 2026 was found in the laws read; whether the declining-balance limit in art. 196 § 3 also binds sole traders (read for companies only); the 2025 version's rule that declining balance is at most twice the straight-line rate and capped at 40% of cost (KB/WIB 92 art. 36 to 43, not read); the 2025 version's revenue timing rule (goods on delivery, services on completion or over time), not found in the KB WVV text read; the 2025 version's statement that from 2026 fully electric cars are 100% deductible and fossil cars bought after 1 July 2023 lose deductibility year by year (moved to be-corporate-tax, not re-read here); usual depreciation rates per asset class (3% to 5% buildings, 20% machinery and vehicles, 33% computers and software, 10% to 20% furniture), which are administrative practice and were not found in a law text; the "assets under EUR 1,000 expensed" practice; CBN advice 138/1 on R&D; the CODA bank statement format, the 12-digit structured communication (+++xxx/xxxx/xxxxx+++) and the bank keyword table from the 2025 version, which are banking practice with no official source read; the income tax retention period for books (WIB 92 art. 315) was not read; the 2025 version's points that first-year depreciation is pro rata temporis by day, and that residual value is normally nil were not found in the texts read.

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
