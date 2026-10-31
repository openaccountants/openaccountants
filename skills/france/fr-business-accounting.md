---
name: fr-business-accounting
description: French business accounting, VAT declarations, invoicing, and e-invoicing 2026 reform. Trigger on phrases like "comptabilité française", "expert-comptable", "TVA France", "déclaration CA3", "déclaration CA12", "TVA intracommunautaire", "facturation France", "facture électronique", "e-invoicing France", "Factur-X", "UBL", "CII", "plateforme agréée", "PDP", "PPF", "réforme facturation 2026", "e-reporting", "PEPPOL France", "mentions obligatoires facture", "avoir facture", "numérotation factures", "franchise en base TVA", "autoliquidation TVA", "régime réel simplifié TVA", "régime réel normal TVA", "FEC", "fichier des écritures comptables", "Plan Comptable Général", "PCG", "liasse fiscale", "bilan France", "compte de résultat", "clôture annuelle", "amortissements comptables", "IS France", "impôt sur les sociétés", "taux réduit PME 15%". Covers TVA regimes and rates, e-invoicing/e-reporting reform timeline, mandatory invoice mentions, IS computation, annual closing, and FEC generation.
version: 1.0
jurisdiction: FR
tax_year: 2026
last_updated: 2026-10-19
authored_by: Michael Cutajar and the OpenAccountants team
review_status: pending_review
trust_label: Built by Michael Cutajar and the OpenAccountants team
category: international
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# France: business accounting, VAT, invoicing and corporation tax

This skill gives the working map for keeping the books of a French business, invoicing, choosing and running the VAT regime, computing corporation tax (impôt sur les sociétés, IS) and closing the year. Figures are for tax year 2026. The corporation tax rates and limits below govern both the financial year closed on 31 December 2025, whose return is filed in May 2026, and a financial year closing during 2026, because the official page states them with no year limit and gives the 2026 filing dates for a year closed on 31 December 2025; the VAT franchise and regime limits are the ones in force during 2026, tested on turnover of 2025 (the basic limit) and of 2026 (the higher limit). The VAT and invoicing rules stated are those in force on 19 October 2026, read on official pages on that date; each page's own date stamp is given where it matters. For the VAT return line by line use `france-vat-return`; for electronic invoicing in depth use `france-einvoice`; for the chart of accounts and depreciation use `france-bookkeeping`; for drawing up and filing the annual accounts use `france-financial-statements`; for the income tax of a sole trader use `fr-income-tax`; for a tax audit under way use `fr-tax-audit`.

## Section 1: Quick reference

**Quick reference**

| Field | Value |
| --- | --- |
| Country | France |
| Scope | Business accounting for companies and businesses taxed under corporation tax or under income tax on a real regime, VAT, invoicing, year-end closing |
| Currency | euro only |
| Accounting framework | Plan Comptable Général (PCG), set by the Autorité des normes comptables |
| Tax authority | Direction générale des Finances publiques (DGFiP), espace professionnel on impots.gouv.fr |
| Import VAT | Managed and collected by the DGFiP since 1 January 2022 |
| Key texts | Code général des impôts (CGI), annexe II art. 242 nonies A for invoices, livre des procédures fiscales (LPF), Code de commerce |
| Companion skills | `france-vat-return`, `france-einvoice`, `france-bookkeeping`, `france-financial-statements` |

## Section 2: VAT (TVA) regimes and rates

### Rates in mainland France

**Standard, intermediate and reduced rates**

| What | Value | Note |
| --- | --- | --- |
| Source | all figures below | https://bofip.impots.gouv.fr/bofip/1013-PGP.html |
| Standard rate (CGI art. 278), the rate whenever no other rate is provided | 20% | "la seconde du taux de 20 %" |
| Intermediate rate (CGI art. 279), for example television subscriptions | 10% | "soumet au taux de 10 % de la TVA les abonnements" |
| Reduced rate (CGI art. 278-0 bis) | 5.5% | "relevant du taux réduit de 5,5 % de la TVA" |

**Particular rate**

| What | Value | Note |
| --- | --- | --- |
| Source | all figures below | https://bofip.impots.gouv.fr/bofip/1449-PGP.html |
| Particular rate in mainland France: medicines meeting the conditions of CGI art. 281 octies, and blood products | 2.1% | "Produits imposables au taux particulier de 2,10 %" |

Which supply takes which rate is not settled by these two pages, which deal with certain services and with medicines. As a working summary kept from the earlier version of this skill, to be confirmed against `france-vat-return` before use: the intermediate rate covers restaurant meals, passenger transport and most work on dwellings finished more than two years ago; the reduced rate covers most food, books and energy-efficiency work on dwellings. The earlier version also put press publications at the particular rate; no page read here says so, so check `france-vat-return` before applying it. The earlier version also put "live performances" at the particular rate; the page above does not say so, so do not apply it to a show without checking. Rates in the overseas departments are different and are in `france-vat-return`.

### Franchise en base (no VAT charged, no VAT deducted)

For 2026 the French franchise thresholds are unchanged. The single franchise threshold proposed by the 2025 finance law was abandoned, as the page below says in terms: "Pour l’année 2026 , les seuils de franchise en base de TVA française applicables restent inchangés". Any text that gives one single franchise threshold for 2026 is wrong.

**Franchise thresholds in force for 2026 (CGI art. 293 B)**

| What | Value | Note |
| --- | --- | --- |
| Source | all figures below | https://entreprendre.service-public.gouv.fr/vosdroits/F21746 |
| Trade and accommodation: turnover of the previous calendar year (2025) at or below | EUR 85,000 | "est inférieur ou égal à 85 000 € (seuil de la franchise en base de TVA)" |
| Trade and accommodation: turnover of the current year (2026) at or below | EUR 93,500 | "est inférieur ou égal à 93 500 € (seuil majoré de la franchise en base de TVA)" |
| Services and liberal professions other than lawyers: previous year at or below | EUR 37,500 | "est inférieur ou égal à 37 500 € (seuil de la franchise en base de TVA)" |
| Services and liberal professions other than lawyers: current year at or below | EUR 41,250 | "est inférieur ou égal à 41 250 € (seuil majoré de la franchise en base de TVA)" |
| Lawyers' regulated activities, and authors' and performers' deliveries of works and copyright: previous year at or below | EUR 50,000 | "inférieur ou égal à 50 000 € (seuil de la franchise en base de TVA)" |
| The same activities: current year at or below | EUR 55,000 | "est inférieur ou égal à 55 000 € (seuil majoré de la franchise en base de TVA)" |
| Lawyers' and authors' other activities: previous year at or below | EUR 35,000 | "est inférieur ou égal à 35 000 € (seuil de la franchise en base de TVA)" |
| Lawyers' and authors' other activities: current year at or below | EUR 38,500 | "est inférieur ou égal à 38 500 € (seuil majoré" |
| A French business loses the franchise for its intra-EU trade when its annual turnover inside the EU (not in France) is more than | EUR 100,000 | "dépasse 100 000 €" |

How the two limits work, per the same page: a business above the basic limit of the previous year but at or below the higher limit of the current year becomes liable to VAT from 1 January of the following year ("elle est soumise à la TVA dès le 1 er janvier de l’année suivante"); a business that passes the higher limit during the year is liable from the first day of the overrun ("dès le 1 er jour de dépassement"). The higher limit is a cliff for the current year, not a margin. A business in the franchise writes on its invoices "TVA non applicable, art. 293 B du code général des impôts" (Section 4).

In the first year of activity the turnover is restated to a full year before testing: 'son CA doit être ajusté et calculé au prorata de son temps d'activité (entre la date de démarrage et le dernier jour de l'année) afin d'obtenir un CA sur une année complète'.

### Simplified regime (régime réel simplifié)

**Simplified VAT regime limits for 2026**

| What | Value | Note |
| --- | --- | --- |
| Source | all figures below | https://entreprendre.service-public.gouv.fr/vosdroits/F23575 |
| Trade, catering and accommodation other than furnished lets: turnover excluding VAT of the previous year (N-1) between | EUR 85,000 | "doit être compris entre : 85 000 € et 945 000 €" |
| ... and | EUR 945,000 | "85 000 € et 945 000 €" |
| Other services, furnished lets included: turnover excluding VAT of N-1 between | EUR 37,500 | "37 500 € et 286 000 €" |
| ... and | EUR 286,000 | "37 500 € et 286 000 €" |
| Trade, catering and accommodation: turnover of the current year (N) must not pass | EUR 1,040,000 | "1 040 000 €" |
| Other services: turnover of N must not pass | EUR 323,000 | "323 000 €" |
| VAT due for N-1 must be below | EUR 15,000 | "doit être inférieur à 15 000 €" |

The page says these turnover limits "sont valables pour l’année 2026 (année N)". Both conditions apply together: turnover inside the band AND VAT due below the VAT limit. The live version of this skill gave older and lower turnover limits for this regime; they are replaced by the table above. The impots.gouv.fr page "Les régimes d'imposition à la TVA" may still print the band it labels as applying from 2025: `france-vat-return` sets out that difference.

Overrun, per the same page: a business that passes the basic band of year N-1 or the VAT-due limit moves to the régime réel normal from 1 January of the year after the overrun; a business that passes one of the higher ceilings in year N moves to the normal regime retroactively from 1 January of year N, and must file a CA3 for the month (or quarter) of the overrun in the following month.

### Returns and payment

**Return frequency and instalments**

| What | Value | Note |
| --- | --- | --- |
| Source | all figures below | https://entreprendre.service-public.gouv.fr/vosdroits/F23566 |
| Régime réel normal: the CA3 is filed every three months instead of monthly where the VAT payable each year is below | EUR 4,000 | "le montant de la TVA exigible chaque année est inférieur à 4 000 €" |
| Régime réel simplifié, year ending 31 December: July instalment, share of the VAT due for the previous year | 55% | "l'entreprise doit verser 55 % de la taxe due l'année précédente" |
| Régime réel simplifié, year ending 31 December: December instalment, share of the VAT due for the previous year | 40% | "l'entreprise doit verser 40 % de la taxe due l'année précédente" |
| A simplified-regime business whose VAT for the previous year was below this amount pays no instalments | EUR 1,000 | "un montant de TVA inférieur à 1 000 € l'année précédente est dispensée" |

Under the simplified regime a business whose financial year ends on 31 December files the annual return CA12 at the latest on the second working day after 1 May for the previous calendar year, and pays the balance with it. A business whose year does not end on 31 December files the CA12 within 3 months of its close, and its instalment months follow the table on the same page. The live version of this skill said the simplified regime pays quarterly advances: that is wrong, it pays two instalments, in July and December, as the table shows. Under the normal regime the CA3 is filed and paid monthly, or quarterly below the limit in the table. The exact day of the month depends on the department, the legal form and the first letters of the name or of the SIREN number; the DGFiP shows it only through a selector (https://www.impots.gouv.fr/le-regime-reel-normal-dates-limites-de-transmission-des-ca3) and in the espace professionnel. Do not state a single day. The page gives the window: 'entre le 15 et le 24 du mois suivant le fait générateur'.

### Intra-EU and international operations

**Intra-EU and international treatment (working summary)**

| Scenario | Treatment |
| --- | --- |
| Service bought from a supplier established in another EU state | The French business customer self-assesses the VAT (autoliquidation) on its own return; see `france-vat-return` for the CA3 lines |
| Service sold to a business customer established in another EU state | Invoice without French VAT; the customer accounts for the VAT; the invoice carries the mention "Auto-liquidation" (Section 4) |
| Service sold to a consumer in another EU state | Place of supply depends on the type of service; electronic, telecom and broadcasting services and distance sales of goods follow the EU distance-selling rules and the OSS. Refer to `france-vat-return` and the EU rules; this skill does not set the threshold |
| Goods imported from outside the EU | Import VAT self-assessment, see below |

**Import VAT self-assessment**

| Rule | Detail |
| --- | --- |
| Source | https://www.impots.gouv.fr/sites/default/files/media/1_metier/2_professionnel/EV/2_gestion/210_declarer_payer/tva_a_limportation_-_notice.pdf |
| Who | Every business identified for VAT in France: "désormais obligatoire pour tout redevable identifié à la TVA en France" |
| Since | 1 January 2022, when the management and collection of import VAT moved to the DGFiP |
| How | Import VAT is collected and deducted on the VAT return itself (line A4 of the CA3 for goods other than petroleum products), no longer with the customs declaration; no prior authorisation is needed. The online return is pre-filled with the import bases each month |

## Section 3: Electronic invoicing reform (réforme de la facturation électronique)

### Timeline

**Who must do what, and from when**

| Date | Obligation | Who |
| --- | --- | --- |
| Source | all rows below | https://www.impots.gouv.fr/professionnel/questions/partir-de-quand-suis-je-concerne-par-la-reforme-de-la-facturation |
| 1 September 2026 | Receive invoices in electronic form, where the supplier is obliged to issue them that way | All businesses, whatever their size: "toutes les entreprises quelle que soit leur taille" |
| 1 September 2026 | Issue electronic invoices and transmit transaction and payment data (e-reporting) | Large companies (grandes entreprises) and intermediate-size companies (ETI) |
| 1 September 2027 | Issue electronic invoices and transmit transaction and payment data | Small and medium companies (PME) and micro-enterprises |

The page was modified on 16 January 2026. A business that issues no invoices is still concerned: it must be able to receive electronic invoices from 1 September 2026, and businesses in the franchise en base and micro-entrepreneurs are inside the reform (https://www.impots.gouv.fr/professionnel/je-decouvre-la-facturation-electronique).

### Key concepts

**Key concepts**

| Concept | Description |
| --- | --- |
| Source | https://www.impots.gouv.fr/professionnel/je-decouvre-la-facturation-electronique |
| Plateforme agréée (PA) | A private company registered by the State as a partner of the administration. Invoices between French businesses must pass through one: "par l’intermédiaire d’un tiers , appelé plateforme agréée". Every business chooses one to issue and receive its invoices and to send its data |
| E-invoicing | Covers purchases and sales of goods and services between businesses established in France and liable to French VAT, franchise en base included. The data goes to the administration from the electronic invoice, through the platform |
| E-reporting of transactions | Covers sales and services to persons who are not liable to VAT, such as individuals, and transactions with operators established abroad (exports, intra-EU acquisitions and supplies) |
| E-reporting of payments | Covers operations whose VAT falls due on receipt of payment, for example services where the business has not opted to pay VAT on the debits and the operation is not reverse-charged |

The live version of this skill listed the accepted formats, a European network as a delivery channel, and a role for the public invoicing portal. Those are not printed on the pages read here; take them, the directory and the platform list from `france-einvoice`.

### New mandatory invoice mentions

**The four new mentions, and when they bind**

| Mention | Detail |
| --- | --- |
| Source | https://entreprendre.service-public.gouv.fr/vosdroits/F31808 |
| When | From 1 September 2026 for large companies and ETI, then for PME and micro-enterprises from 1 September 2027: "Cette obligation concerne d’abord les grandes entreprises et les ETI" |
| Client SIREN | The SIREN number of the client, when the client is a business |
| Delivery address | The delivery address of the goods, if it differs from the client's address |
| Nature of the operations | Whether the invoice covers deliveries of goods, services, or both |
| VAT on debits option | The mention "Option pour le paiement de la taxe d’après les débits" where the supplier has opted to pay VAT on the debits |

The live version of this skill said the client SIREN and the transaction category are required on all domestic business invoices from 1 September 2026, and listed only two new mentions. The page above lists four and ties them to the issuing calendar: an SME is not bound before 1 September 2027.

## Section 4: Invoice requirements (mentions obligatoires)

### Mentions on every invoice

The page below (Vérifié le 11 août 2026) lists these mentions for every invoice, "que le client soit un particulier, un professionnel ou une entité publique".

**General mandatory mentions (CGI annexe II art. 242 nonies A, Code de commerce art. L441-9)**

| Mention | Value | Note |
| --- | --- | --- |
| Source | all figures below | https://entreprendre.service-public.gouv.fr/vosdroits/F31808 |
| Date of issue | | Date the invoice is issued |
| Unique invoice number | | "basé sur une séquence chronologique et continue" |
| Date of the sale or of the service | | Day of delivery or end of the service, or date the deposit is paid |
| Seller's identity | | Company: name, SIREN, registered office address, legal form and amount of share capital. Sole trader: name preceded or followed by "Entrepreneur individuel" or "EI", address, SIREN. A company being registered invoices in its own name with "Siret en cours d'attribution" |
| Buyer's identity | | Business: its name. Individual: full name and address, unless the individual objects |
| Purchase order number | | Where the buyer issued one first |
| VAT identification number of the seller, and of the business client liable to VAT, except on invoices whose total excluding VAT is at or below | EUR 150 | "inférieur ou égal à 150 €" |
| Description, quantity, unit price excluding VAT, VAT rate or the exemption relied on | | One line for each product and service |
| Totals excluding VAT and including VAT | | With any price supplement, and any discount earned at the date of sale |
| Payment date, and the early-payment discount terms | | With no discount, write "Escompte pour paiement anticipé : néant" |
| Late-payment penalty rate | | Due without any reminder |
| Fixed recovery indemnity for late payment, which applies only where the client is a business ("ne peut être réclamée que par un client professionnel") | EUR 40 | "indemnité forfaitaire de 40 €" |

**Particular mentions (same page)**

| Case | Mention |
| --- | --- |
| Seller in the franchise en base | "TVA non applicable, art. 293 B du code général des impôts" |
| Buyer is the person liable for the VAT | "Auto-liquidation" |
| The client draws up the invoice for the supplier | "Auto-facturation" |
| Member of an approved management centre or association | The wording on the page |
| Craft activity | The professional insurance details |

### Credit notes (avoirs)

- **Credit note requirements**: a credit note refers to the invoice it corrects by its number and states why the amount is reduced. This is kept from the earlier version of this skill; the pages read here do not set it out, so check the rule in CGI annexe II art. 242 nonies A before relying on its exact wording.

### Numbering

- **Invoice numbering**: one unique number per invoice, in a chronological and continuous sequence (page above). A yearly series with a prefix, for example F-2026-001, F-2026-002, is a common way to keep it continuous; the page does not prescribe a format.

### Retention

**How long to keep the records**

| What | Value | Note |
| --- | --- | --- |
| Source | all figures below | https://entreprendre.service-public.gouv.fr/vosdroits/F37169 |
| A commercial company keeps its accounting documents and supporting documents, invoices included, for at least this period from the close of the financial year | 10 years | "au moins 10 ans à partir de la clôture de l'exercice comptable" |
| Fine for a company that has not kept its documents | EUR 10,000 | "s'expose à une amende de 10 000 €" |

**Tax retention period**

| What | Value | Note |
| --- | --- | --- |
| Source | all figures below | https://entreprendre.service-public.gouv.fr/vosdroits/F10029 |
| Books, registers and documents open to the administration's rights of inspection, counted from the last operation entered or the date the document was drawn up | 6 years | "doivent être conservés pendant un délai de 6 ans" |

The two periods run side by side: keep for the longer one. The earlier version cited art. L123-22 of the Code de commerce for invoices; the commercial period is set out on the first page above.

## Section 5: Corporation tax (impôt sur les sociétés, IS)

### Rates and the reduced rate

**Corporation tax rates (CGI art. 219)**

| What | Value | Note |
| --- | --- | --- |
| Source | all figures below | https://entreprendre.service-public.gouv.fr/vosdroits/F23575 |
| Standard rate on profits made in France in the financial year | 25% | "imposée au taux normal de 25 %" |
| Reduced rate, on the first slice of profit only | 15% | "un taux réduit fixé à 15 %" |
| The slice of profit the reduced rate covers; the profit above it is taxed at the standard rate | EUR 42,500 | "la part des bénéfices allant jusqu'à 42 500 €" |
| Reduced rate, first condition: turnover of the financial year, restated to 12 months where needed, at or below | EUR 10,000,000 | "Chiffre d'affaires inférieur ou égal à 10 000 000 €" |
| Reduced rate, second condition: share capital fully paid up AND held to at least this share by individuals, or by a company itself held to at least this share by individuals | 75% | "détenu pour au moins 75 % par des personnes physiques" |
| No quarterly instalments where the corporation tax is below | EUR 3,000 | "Le montant de l'IS est inférieur à 3 000 €" |
| Surcharge for filing the results return other than electronically, share of the tax | 0.2% | "une majoration de 0,2 % du montant de l'impôt" |
| Minimum of that surcharge | EUR 60 | "ne peut pas être inférieure à 60 €" |

Both conditions of the reduced rate must be met (AND). The page, checked on 17 February 2026, says the shares the company holds in itself are left out when testing the ownership condition. A company that fails either condition pays the standard rate on all its profit. Newly created companies, and companies in their first period within corporation tax, make no instalments either.

The live version of this skill said that in a short financial year the reduced-rate slice is prorated by days. The page above does not say so; it restates only the turnover to 12 months. Check BOI-IS-LIQ-20-10 before prorating the slice for a short or long year.

### Social contribution on corporation tax

**Contribution sociale sur l'IS (CGI art. 235 ter ZC)**

| What | Value | Note |
| --- | --- | --- |
| Source | all figures below | https://bofip.impots.gouv.fr/bofip/3492-PGP.html |
| Rate, applied to the corporation tax (not to the profit) after the abatement | 3.3% | "x 3,3 %" |
| Annual abatement deducted from the corporation tax before the rate | EUR 763,000 | "diminué d’un abattement annuel de 763 000 €" |

**Who is exempt**

| What | Value | Note |
| --- | --- | --- |
| Source | all figures below | https://bofip.impots.gouv.fr/bofip/3491-PGP.html |
| Companies whose turnover for the period, restated to 12 months, is below this amount, AND which meet the capital conditions | EUR 7,630,000 | "chiffre d’affaires de moins de 7 630 000 €" |

A company whose corporation tax is not above the abatement owes no contribution, because the rate applies only to the tax left after the abatement.

### Corporation tax is not deductible

- **IS non-deductibility**: corporation tax itself (account 695) is not a deductible charge and is added back when moving from the accounting result to the taxable result. The basis is CGI art. 213, which "dispose par ailleurs que l'impôt sur les sociétés, l'impôt sur le revenu et la taxe sur les voitures des sociétés visée à l' article 1010 du CGI ne sont pas admis dans les charges déductibles" (https://bofip.impots.gouv.fr/bofip/2102-PGP.html). The earlier version of this skill cited art. 39-1-4°, which is the general rule that taxes are deductible; the exclusion of corporation tax is art. 213.

### Non-deductible charges (common traps)

**Non-deductible charges (common traps)**

| Charge | Rule | Note |
| --- | --- | --- |
| Source | all rows below | https://entreprendre.service-public.gouv.fr/vosdroits/F31973 |
| Luxury spending (hunting, yachts and similar) | Not deductible | "la chasse de loisirs, la pêche non professionnelle, l'achat ou la location de résidence de plaisance, de yacht et de bateau de plaisance" |
| Personal spending of a shareholder or director paid by the company | Not deductible; risk of "acte anormal de gestion" | "Les dépenses personnelles de l'exploitant individuel, du dirigeant ou d'un associé ne sont pas déductibles" |
| Corporation tax itself | Not deductible (CGI art. 213, above) | See the art. 213 line above (https://bofip.impots.gouv.fr/bofip/2102-PGP.html) |
| Directors' remuneration in a company under corporation tax | Deductible only where it corresponds to actual work and is not excessive | "déductibles lorsqu'elles correspondent à un travail effectif et ne sont pas excessives" |

Rows are as printed on the page above (Vérifié le 02 juin 2023) and on BOI-BIC-CHG-40-30 for corporation tax.

### General conditions for deducting a charge

- **Conditions for deducting a charge**: per BOFiP BOI-BIC-CHG-10 (https://bofip.impots.gouv.fr/bofip/3848-PGP.html), a charge must, as a rule, meet all of these: be incurred in the direct interest of the business or belong to its normal management; correspond to an actual charge and be backed by sufficient evidence ("correspondre à une charge effective et être appuyées de justifications suffisantes"); and belong to the charges of the financial year in which it was incurred. It must also not be excluded by a specific provision. The earlier version listed a "decrease of net assets" condition, which is not on that page.

### Small equipment taken to expense

**The small-equipment tolerance**

| What | Value | Note |
| --- | --- | --- |
| Source | all figures below | https://bofip.impots.gouv.fr/bofip/2109-PGP.html |
| Unit value excluding VAT up to which materials and tooling may be deducted at once instead of being capitalised | EUR 500 | "d'une valeur unitaire hors taxes n'excédant pas 500 €" |

This is a tax tolerance, not a general capitalisation threshold. It covers materials and tooling of accounts 2154 and 2155, and the other categories BOFiP names on that page; an item above the limit, or outside those categories, is capitalised if it is an asset. The business may choose to capitalise even below the limit.

## Section 6: Annual closing (clôture annuelle), summary

### Workflow

1. **Collect all transactions for the financial year.**
2. **Categorise expenses** (supplier to PCG account; see `france-bookkeeping`).
3. **Bank reconciliation.**
4. **Inventory entries**: depreciation, prepaid income and prepaid charges, provisions.
5. **Taxable result and corporation tax**: add back non-deductible items (Section 5), compute the tax with the rates table.
6. **Journal entries** for the closing.
7. **Financial statements**: balance sheet (bilan), income statement (compte de résultat), trial balance; notes where required (`france-financial-statements`).
8. **The accounting entries file (FEC)** for the year, kept ready for an audit (below).
9. **Liasse fiscale**: tables 2033-A to 2033-G under the simplified regime, tables 2050 to 2059 under the normal regime (https://entreprendre.service-public.gouv.fr/vosdroits/F23575).
10. **Results return 2065** for corporation tax, or 2031 (2035 for a liberal activity) where the company is taxed under income tax (same page).
11. **Approval minutes and the filing of the accounts**, with a confidentiality declaration where the company may and wants to use one (https://entreprendre.service-public.gouv.fr/vosdroits/F31214).
12. **Produce the final documents** (PDFs for signature and filing).

### FEC (fichier des écritures comptables)

- **When it is due**: a business that keeps its accounts on a computer meets its duty to present its books by handing over "au début des opérations de contrôle, une copie des fichiers des écritures comptables" (BOI-CF-IOR-60-40-10, https://bofip.impots.gouv.fr/bofip/9026-PGP.html). It is handed over at the start of an audit, not filed each year. It covers corporation tax payers and income tax payers taxed on industrial and commercial, non-commercial or agricultural profits under a real regime.
- **Format**: either a flat sequential file meeting the criteria of art. A. 47 A-1 of the LPF, or an XML file matching the published XSD; the fields and their order are set out in BOI-CF-IOR-60-40-20 (https://bofip.impots.gouv.fr/bofip/9028-PGP.html). The earlier version stated a fixed column count and a pipe separator; those are not printed on the pages read here, so take the field list and the separator from the BOFiP page and the XSD (https://www.impots.gouv.fr/fichiers-standards-des-ecritures-comptables), and see `france-bookkeeping` for the field list.
- **Conformity checks before release**: total debits equal total credits; each entry number is balanced; entry numbers run without a gap; dates fall inside the financial year; the document reference is filled for every entry; account numbers follow the PCG roots. These are working checks kept from the earlier version.

**Penalty for a file not in the required form (CGI art. 1729 D)**

| What | Value | Note |
| --- | --- | --- |
| Source | all figures below | https://bofip.impots.gouv.fr/bofip/9026-PGP.html |
| Fine where the accounts are not presented in the required form | EUR 5,000 | "d’une amende égale à 5 000 €" |
| Or, where the tax is adjusted and the amount is higher, an increase of the tax charged | 10% | "majoration de 10 % des droits" |

The earlier version said a non-compliant file makes the accounts unreliable and shifts the burden of proof under art. L. 192 LPF; that is not on the pages read here. The sanction on the page is the one in the table.

## Section 7: Shareholder current account (compte courant d'associé, account 455)

High fiscal risk zone, especially for a SASU or an EURL.

**Interest paid on a shareholder's advances (CGI art. 39-1-3°)**

| What | Value | Note |
| --- | --- | --- |
| Source | all figures below | https://bofip.impots.gouv.fr/bofip/5505-PGP.html |
| Highest deductible rate for a 12-month financial year closed between 30 June 2026 and 29 September 2026 | 4.33% | "Entre le 30 juin 2026 et le 30 juillet 2026 4,33 %" |

The ceiling is the yearly average of the effective average rates charged by credit institutions on variable-rate loans to businesses with an initial term of more than two years, published each quarter in the Journal officiel. Interest is deductible only within the limit of that rate ("sont déductibles dans la limite du taux"), tested on the gross rate and the gross amount of the interest. The page's worked examples use older rates; use the table above, not the examples. A year closed on 31 December 2026 needs a rate not yet printed on that page: take it from the page once it is updated. Before any interest is deducted at all, the share capital must be fully paid up: BOI-BIC-CHG-50-50-10 (https://bofip.impots.gouv.fr/bofip/2113-PGP.html) says the condition on paid-up capital of CGI art. 39-1-3° al. 2 'est en principe opposable à l'ensemble des sociétés'. The same page sets which advances the rate limit covers; the detail of the paid-up-capital condition is in BOI-BIC-CHG-50-50-20, not read here.

**Other current-account checks (working checks)**

| Check | Rule |
| --- | --- |
| Expenses before incorporation | Check that the company has formally taken over the acts done for it before registration; the conditions are company law and are not on the pages read here |
| Home office | A professional share by floor area, with a plan; personal utilities and mortgage capital are not charges of the company |
| Mixed-use expenses | Only the professional share is a charge |
| Currency conversion | Record the rate used and where it came from, and use one method consistently |

These checks are kept from the earlier version and are not set out on the pages read here. The earlier version gave a time limit for taking over pre-incorporation acts and a rule on accepted exchange rates; neither is on an allowed page, so both are removed.

## Section 8: Fiscal calendar (key deadlines)

**Key deadlines**

| Deadline | Obligation | Source |
| --- | --- | --- |
| Each month, on the day shown in the espace professionnel | CA3 under the régime réel normal | https://www.impots.gouv.fr/le-regime-reel-normal-dates-limites-de-transmission-des-ca3 |
| Each quarter, same rule | CA3 under the régime réel normal where the yearly VAT is below the limit in Section 2 | https://entreprendre.service-public.gouv.fr/vosdroits/F23566 |
| July and December | Simplified-regime VAT instalments (year ending 31 December) | https://entreprendre.service-public.gouv.fr/vosdroits/F23566 |
| Second working day after 1 May | CA12 annual VAT return under the simplified regime | https://entreprendre.service-public.gouv.fr/vosdroits/F23566 |
| 15 March, 15 June, 15 September, 15 December | Corporation tax instalments, form 2571; which date is the first depends on the closing date | https://entreprendre.service-public.gouv.fr/vosdroits/F23575 |
| Within 3 months of the close; for a year closed on 31 December, the second working day after 1 May | Results return 2065 with the liasse fiscale; the administration allows a further 15 calendar days for electronic filing, which gave 20 May 2026 for a year closed on 31 December 2025 | https://entreprendre.service-public.gouv.fr/vosdroits/F23575 |
| 15th day of the 4th month after the close; 15 May for a year closed on 31 December | Corporation tax balance, form 2572 | https://entreprendre.service-public.gouv.fr/vosdroits/F23575 |
| Within 6 months of the close for an SA and a SARL or EURL; for an SAS or SASU, within the period the partners set | Approval of the accounts | https://entreprendre.service-public.gouv.fr/vosdroits/F31214 |
| Within 1 month of approval, or within 2 months where filed electronically | Filing of the accounts with the registry | https://entreprendre.service-public.gouv.fr/vosdroits/F31214 |

The earlier version gave the results return as "3 months plus a 1-month extension". The page gives 3 months, or the second working day after 1 May for a 31 December close, plus 15 calendar days for electronic filing.

## Section 9: Conservative defaults

**Conservative defaults**

| Ambiguity | Default |
| --- | --- |
| VAT regime unknown | Do not assume the franchise: test turnover of 2025 and of 2026 against the franchise table in Section 2, and treat the business as liable to VAT until both are shown to be within it |
| Deductibility of a charge doubtful | Not deductible |
| Professional share of a mixed-use expense unclear | Treat it as wholly private and flag it for the accountant |
| Corporation tax rate unclear | The standard rate on all profit; the reduced rate only once both conditions in Section 5 are evidenced |
| Asset or expense | Capitalise, unless the item falls inside the small-equipment tolerance in Section 5 |
| Electronic invoicing start date unclear | Prepare to receive from 1 September 2026; for issuing, confirm the company's size class in `france-einvoice` |

The earlier default "franchise en base if turnover permits" is reversed: crossing the higher limit makes VAT due from the day of the overrun, so assuming the franchise risks uncollected VAT.

## Section 10: Key legal references

**Key legal references**

| Rule | Article |
| --- | --- |
| Taxable profit | CGI art. 38 |
| Deductible charges | CGI art. 39-1; BOI-BIC-CHG-10 |
| Corporation tax not deductible | CGI art. 213 |
| Corporation tax rates, reduced rate | CGI art. 219 |
| Social contribution on corporation tax | CGI art. 235 ter ZC |
| VAT franchise en base | CGI art. 293 B |
| Simplified regime | CGI art. 302 septies A |
| Reverse charge on services from abroad | CGI art. 283-2 |
| Current-account interest ceiling | CGI art. 39-1-3° |
| Invoice mentions | CGI annexe II art. 242 nonies A; Code de commerce art. L441-9 |
| FEC | LPF art. L. 47 A and art. A. 47 A-1; CGI art. 1729 D |
| Commercial retention | Code de commerce art. L123-12 to L123-24 |

## The method, step by step

1. **Fix the entity and its tax regimes.** Corporation tax or income tax; then the VAT regime from the franchise and simplified-regime tables, using turnover of the previous year and of the current year (https://entreprendre.service-public.gouv.fr/vosdroits/F21746 and https://entreprendre.service-public.gouv.fr/vosdroits/F23575).
2. **Keep the books under the PCG** and keep records for the periods in Section 4 (https://entreprendre.service-public.gouv.fr/vosdroits/F37169 and https://entreprendre.service-public.gouv.fr/vosdroits/F10029).
3. **Invoice correctly**: the mentions in Section 4, the four new mentions on the company's start date, and receive electronic invoices through a plateforme agréée from 1 September 2026 (https://entreprendre.service-public.gouv.fr/vosdroits/F31808 and https://www.impots.gouv.fr/professionnel/questions/partir-de-quand-suis-je-concerne-par-la-reforme-de-la-facturation).
4. **File and pay VAT**: CA3 monthly or quarterly, or CA12 with two instalments, in the espace professionnel; import VAT self-assessed on the VAT return (https://entreprendre.service-public.gouv.fr/vosdroits/F23566 and https://www.impots.gouv.fr/sites/default/files/media/1_metier/2_professionnel/EV/2_gestion/210_declarer_payer/tva_a_limportation_-_notice.pdf). Line-level work is in `france-vat-return`.
5. **Close the year**: the workflow in Section 6, add back corporation tax and other non-deductible items, apply the small-equipment tolerance and the current-account interest ceiling (https://bofip.impots.gouv.fr/bofip/2102-PGP.html and https://bofip.impots.gouv.fr/bofip/2109-PGP.html and https://bofip.impots.gouv.fr/bofip/5505-PGP.html).
6. **Compute corporation tax** with the rates table, test both reduced-rate conditions, then the social contribution (https://entreprendre.service-public.gouv.fr/vosdroits/F23575 and https://bofip.impots.gouv.fr/bofip/3492-PGP.html).
7. **File the 2065 and the liasse 2033 or 2050** electronically, pay the balance on form 2572, and set the next year's instalments on form 2571 (https://entreprendre.service-public.gouv.fr/vosdroits/F23575).
8. **Approve and file the accounts** with the registry within the periods in Section 8 (https://entreprendre.service-public.gouv.fr/vosdroits/F31214).
9. **Keep the FEC ready** in the required format for any audit (https://bofip.impots.gouv.fr/bofip/9026-PGP.html and https://bofip.impots.gouv.fr/bofip/9028-PGP.html).

## Ask the client first

- Is the business a company under corporation tax, a company that opted for income tax, or a sole trader? What is its legal form?
- What was its turnover excluding VAT in 2025, and what is it so far in 2026, split between trade or accommodation and services?
- Who holds the share capital, in what proportions, and is it fully paid up?
- On what date does the financial year close, and is this year shorter or longer than 12 months?
- Is the company a large company, an ETI, a PME or a micro-enterprise for the electronic invoicing calendar, and which plateforme agréée has it chosen?
- Does it sell to individuals, abroad or within the EU, and does it import goods?

## When to refuse or refer

- Groups under the tax consolidation regime, companies with turnover near or above the reduced-rate limit with complex shareholdings, and any company whose corporation tax may be above the social contribution abatement: refer to an expert-comptable.
- Partial VAT exemption, the margin scheme, property VAT, VAT groups and overseas departments: refer, or use `france-vat-return` within its own limits.
- Transfer pricing and cross-border group charges: use `france-transfer-pricing` and refer.
- A tax audit under way, or a request to produce the FEC: use `fr-tax-audit` and refer.
- Choosing a plateforme agréée, or the electronic invoicing size class where it is not clear: use `france-einvoice`.
- Any figure in this skill that the client's own position contradicts, and any short or long financial year when applying the reduced-rate slice: refer.

## Sources

- Taux réduits, services (BOI-TVA-LIQ-30-20-100): https://bofip.impots.gouv.fr/bofip/1013-PGP.html
- Taux particulier (BOI-TVA-LIQ-40-10): https://bofip.impots.gouv.fr/bofip/1449-PGP.html
- Franchise en base de TVA: https://entreprendre.service-public.gouv.fr/vosdroits/F21746
- Impôt sur les sociétés, taux, déclaration, paiement (also the simplified VAT regime limits): https://entreprendre.service-public.gouv.fr/vosdroits/F23575
- Déclarer et payer la TVA: https://entreprendre.service-public.gouv.fr/vosdroits/F23566
- Dates limites de transmission des CA3: https://www.impots.gouv.fr/le-regime-reel-normal-dates-limites-de-transmission-des-ca3
- Notice, TVA à l'importation: https://www.impots.gouv.fr/sites/default/files/media/1_metier/2_professionnel/EV/2_gestion/210_declarer_payer/tva_a_limportation_-_notice.pdf
- Facturation électronique, start dates: https://www.impots.gouv.fr/professionnel/questions/partir-de-quand-suis-je-concerne-par-la-reforme-de-la-facturation
- Je découvre la facturation électronique: https://www.impots.gouv.fr/professionnel/je-decouvre-la-facturation-electronique
- Mentions obligatoires sur une facture: https://entreprendre.service-public.gouv.fr/vosdroits/F31808
- Obligations comptables d'une société commerciale: https://entreprendre.service-public.gouv.fr/vosdroits/F37169
- Délais de conservation des documents: https://entreprendre.service-public.gouv.fr/vosdroits/F10029
- Dépôt des comptes annuels: https://entreprendre.service-public.gouv.fr/vosdroits/F31214
- Charges déductibles du résultat fiscal: https://entreprendre.service-public.gouv.fr/vosdroits/F31973
- Contribution sociale sur l'IS, calcul (BOI-IS-AUT-10-20): https://bofip.impots.gouv.fr/bofip/3492-PGP.html
- Contribution sociale sur l'IS, exonérations (BOI-IS-AUT-10-10): https://bofip.impots.gouv.fr/bofip/3491-PGP.html
- Impôts et taxes, art. 213 (BOI-BIC-CHG-40-30): https://bofip.impots.gouv.fr/bofip/2102-PGP.html
- Conditions générales de déduction (BOI-BIC-CHG-10): https://bofip.impots.gouv.fr/bofip/3848-PGP.html
- Petits matériels et outillages (BOI-BIC-CHG-20-30-10): https://bofip.impots.gouv.fr/bofip/2109-PGP.html
- Intérêts des comptes courants, champ (BOI-BIC-CHG-50-50-10): https://bofip.impots.gouv.fr/bofip/2113-PGP.html
- Intérêts des comptes courants, taux limite (BOI-BIC-CHG-50-50-30): https://bofip.impots.gouv.fr/bofip/5505-PGP.html
- FEC, remise de la copie (BOI-CF-IOR-60-40-10): https://bofip.impots.gouv.fr/bofip/9026-PGP.html
- FEC, format (BOI-CF-IOR-60-40-20): https://bofip.impots.gouv.fr/bofip/9028-PGP.html
- Fichiers standards des écritures comptables: https://www.impots.gouv.fr/fichiers-standards-des-ecritures-comptables

## Disclaimer

This skill is for informational purposes only and does not constitute tax advice. All positions must be reviewed and signed off by a qualified expert-comptable before filing. Get this reviewed at openaccountants.com.

*OpenAccountants: open-source accounting skills for AI. This output must be reviewed by a qualified professional before filing or acting upon. Latest skills: openaccountants.com.*

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
