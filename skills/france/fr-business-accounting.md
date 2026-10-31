---
name: fr-business-accounting
description: French business accounting, VAT declarations, invoicing, and e-invoicing 2026 reform. Trigger on phrases like "comptabilité française", "expert-comptable", "TVA France", "déclaration CA3", "déclaration CA12", "TVA intracommunautaire", "facturation France", "facture électronique", "e-invoicing France", "Factur-X", "UBL", "CII", "plateforme agréée", "PDP", "PPF", "réforme facturation 2026", "e-reporting", "PEPPOL France", "mentions obligatoires facture", "avoir facture", "numérotation factures", "franchise en base TVA", "autoliquidation TVA", "régime réel simplifié TVA", "régime réel normal TVA", "FEC", "fichier des écritures comptables", "Plan Comptable Général", "PCG", "liasse fiscale", "bilan France", "compte de résultat", "clôture annuelle", "amortissements comptables", "IS France", "impôt sur les sociétés", "taux réduit PME 15%". Covers TVA regimes and rates, e-invoicing/e-reporting reform timeline, mandatory invoice mentions, IS computation, annual closing, and FEC generation.
version: 1.3
jurisdiction: FR
tax_year: 2026
last_updated: 2026-10-31
authored_by: Michael Cutajar and the OpenAccountants team
review_status: pending_review
trust_label: Built by Michael Cutajar and the OpenAccountants team
category: international
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# France: business accounting, VAT, invoicing and corporation tax

This skill gives the working map for keeping the books of a French business, invoicing, choosing and running the VAT regime, computing corporation tax (impôt sur les sociétés, IS) and closing the year. Figures are for tax year 2026. The corporation tax rates and limits below govern both the financial year closed on 31 December 2025, whose return is filed in May 2026, and a financial year closing during 2026, because the official page states them with no year limit and gives the 2026 filing dates for a year closed on 31 December 2025; the VAT franchise and regime limits are the ones in force during 2026, tested on turnover of 2025 (the basic limit) and of 2026 (the higher limit). The VAT and invoicing rules stated are those in force on 19 October 2026, read on official pages on that date; each page's own date stamp is given where it matters. For the VAT return line by line use `france-vat-return`; for electronic invoicing in depth use `france-einvoice`; for the chart of accounts and depreciation use `france-bookkeeping`; for drawing up and filing the annual accounts use `france-financial-statements`; for the income tax of a sole trader use `fr-income-tax`; for a tax audit under way use `fr-tax-audit`. Selected source conditions, invoice particulars, tax gates and approval rules were checked on 29 October 2026; earlier source and review dates above remain preserved.

> **Based on work by [Romain Simon (@romainsimon)](https://github.com/romainsimon/paperasse)**, licensed under MIT. Adapted for the OpenAccountants format.

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
| Particular rate in mainland France: medicines meeting CGI art. 281 octies; also labile blood products for human research and in-vitro diagnostic medical devices when prepared from blood or its components | 2.1% | CGI art. 281 octies. Direct-therapeutic whole blood and its derivatives remain subject to the stated CGI art. 261, 4-2° exemption; establish the actual product/use, not a generic blood-product label |

The rates above are headline rates, not automatic product classifications. The checked companion `france-vat-return` gives the actual conditions for restaurant food and alcohol, passenger transport, qualifying renovation and energy work on dwellings, food exclusions, books, qualifying press and limited first performances. A generic label such as "live performance" does not establish the rate. Overseas rates and specialist eligibility remain in that companion.

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
| EU-wide franchise scheme | EUR 100,000 | For an EU business claiming another Member State’s franchise, test EU-wide turnover in BOTH the preceding and current year, the host-state conditions and the home-state notification/identification process. This does not by itself remove the French franchise from domestic operations. |

Test the previous calendar year against the basic ceiling: exceeding it removes the ordinary domestic franchise from 1 January of the following year. Separately, exceeding the higher ceiling during the current year removes it from the day of that overrun (CGI art.293 B, II). Retain the dated turnover and actual transaction. The invoice wording is in Section4; foreign purchases can create VAT liabilities even where the business’s own domestic sales remain franchised.

For a new activity, the Service Public annualisation wording expressly tests the following year. CGI293 D, III and the retained DGFiP first-year guidance give conflicting startup-ceiling treatments; `france-vat-return` preserves both sourced readings and conditional calculations. This Guide does not settle that conflict or infer an exact VAT start date from a year-end total.

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
| Previous-year VAT liability: the statutory monthly-return trigger is strictly above | EUR 15,000 | CGI287-3bis; equality alone does not trigger this rule. Test all the other regime conditions separately. |

These are the2026 turnover figures. Apply them together with the actual reporting-regime conditions and options. CGI287-3bis requires monthly returns where the previous-year VAT is strictly above EUR15,000; the administrative overview’s “below” wording does not decide equality. CGI287-3ter separately requires monthly returns for the specified intra-EU acquisitions, imports and suspensive-regime exits. The retained older and current indexed turnover texts, activity exceptions and options are explained in `france-vat-return`.

Overrun requires the actual statutory/administrative sequence, not just a comparison with the table. The administrative page prints a current-year higher-ceiling move retroactive to1January, while the current implementing text and calendar-year recapitulatory procedure are preserved in `france-vat-return`. Use that companion’s qualified procedure; noncalendar reconciliation remains expressly unresolved there. Do not assume that every turnover or VAT trigger has the same effective date.

### Returns and payment

**Return frequency and instalments**

| What | Value | Note |
| --- | --- | --- |
| Source | all figures below | https://entreprendre.service-public.gouv.fr/vosdroits/F23566 |
| Régime réel normal: the CA3 is filed every three months instead of monthly where the VAT payable each year is below | EUR 4,000 | "le montant de la TVA exigible chaque année est inférieur à 4 000 €" |
| Régime réel simplifié, calendar-year July instalment, calculated on the previous-year VAT before VAT on fixed assets | 55% | CGI287-3; apply the actual base, credits and adjustment conditions. |
| Régime réel simplifié, calendar-year December instalment, on the same statutory base | 40% | CGI287-3; not40% of every amount described as last year’s balance due. |
| No instalments where the previous-year VAT on that statutory base is below | EUR 1,000 | CGI287-3; fixed-asset VAT is excluded from that comparison. |

Under the simplified regime, the calendar-year annual CA12 is due on the second working day after1May and settles the balance. A noncalendar close has a three-month administrative filing rule; the remaining current cessation/recapitulation conflict is preserved in `france-vat-return`, so do not treat the old off-calendar instalment illustration as a fully reconciled method. Calendar-year instalments are July and December. Normal-regime CA3 returns and payments are monthly, or quarterly where annual VAT is strictly below EUR4,000. The account-specific deadline depends on the actual selector and professional account (https://www.impots.gouv.fr/le-regime-reel-normal-dates-limites-de-transmission-des-ca3); the administrative window is15–24of the following month, not one universal filing day.

### Intra-EU and international operations

**Intra-EU and international treatment (working summary)**

| Scenario | Treatment |
| --- | --- |
| Ordinary service bought from a supplier established in another EU state | First establish the place under the general B2B rule and any special-service exception, the receiving establishment and whether the supplier has a participating French establishment. Where the French customer owes the tax, it self-assesses it; a domestic-sales franchise does not by itself remove that duty. Use `france-vat-return` for the exact conditions and CA3 lines. |
| Ordinary service sold to a business customer established in another EU state | Apply the general B2B place rule and special-service exceptions first. Where the customer is liable under the destination rule, invoice without French VAT with “Auto-liquidation” and test the DES reporting conditions. A foreign address alone does not establish the treatment. |
| Service sold to a consumer in another EU state | Place of supply depends on the type of service; electronic, telecom and broadcasting services and distance sales of goods follow the EU distance-selling rules and the OSS. Refer to `france-vat-return` and the EU rules; this skill does not set the threshold |
| Goods imported from outside the EU | Import VAT self-assessment, see below |

**Import VAT self-assessment**

| Rule | Detail |
| --- | --- |
| Source | https://www.impots.gouv.fr/sites/default/files/media/1_metier/2_professionnel/EV/2_gestion/210_declarer_payer/tva_a_limportation_-_notice.pdf |
| Who | Every business identified for VAT in France: "désormais obligatoire pour tout redevable identifié à la TVA en France" |
| Since | 1 January 2022, when the management and collection of import VAT moved to the DGFiP |
| How | Import VAT is declared on the VAT return (A4 for non-petroleum imports). The return is prefilled with customs bases; check the actual import data. Input deduction is a separate test of eligibility and evidence, not automatic simply because output import VAT is declared. |

## Section 3: Electronic invoicing reform (réforme de la facturation électronique)

### Timeline

**Who must do what, and from when**

| Date | Obligation | Who |
| --- | --- | --- |
| Source | all rows below | https://www.impots.gouv.fr/professionnel/questions/partir-de-quand-suis-je-concerne-par-la-reforme-de-la-facturation |
| 1 September2026 | Be able to receive in-scope electronic invoices through a plateforme agréée | French VAT taxable persons, including franchise businesses and taxable persons making only exempt sales; a non-taxable person is not included merely because it is an organisation. |
| 1 September 2026 | Issue electronic invoices and transmit transaction and payment data (e-reporting) | Large companies (grandes entreprises) and intermediate-size companies (ETI) |
| 1 September2027 | Issue in-scope electronic invoices and transmit the specified transaction/payment data | PME and micro-enterprises within the statutory extension; VAT-group members are excluded from that extension. Use the actual legal-unit size reference. |

The original schedule page was modified on16January2026. A taxable person that issues no invoices must still be capable of receiving the electronic invoices addressed to it; franchise businesses and micro-entrepreneurs remain taxable persons (https://www.impots.gouv.fr/professionnel/je-decouvre-la-facturation-electronique). The size reference is the legal unit identified by SIREN, assessed at1January2025 using the last earlier closed year or, if none, the first later close. This is separate from the current annual-accounts size test.

### Key concepts

**Key concepts**

| Concept | Description |
| --- | --- |
| Source | https://www.impots.gouv.fr/professionnel/je-decouvre-la-facturation-electronique |
| Plateforme agréée (PA) | A private company registered by the State as a partner of the administration. Invoices between French businesses must pass through one: "par l’intermédiaire d’un tiers , appelé plateforme agréée". Every business chooses one to issue and receive its invoices and to send its data |
| E-invoicing | The actual domestic supplies and advances named in CGI289bis between taxable persons established in France, through an approved platform. Apply the substantive scope and exemptions; being a French business does not make every transaction reportable. |
| E-reporting of transactions | The specified consumer and international operations within CGI290 and the current scope rules, excluding the stated exemptions. Use `france-einvoice` for transaction-level eligibility; this is not an assertion that every foreign transaction is reportable. |
| E-reporting of payments | Covers operations whose VAT falls due on receipt of payment, for example services where the business has not opted to pay VAT on the debits and the operation is not reverse-charged |

The current DGFiP overview expressly names UBL, CII and a mixed format containing structured data and an image. A scanned invoice, ordinary PDF or email alone does not meet that electronic-invoice description. The detailed Factur-X profile, PEPPOL delivery route, directory and public-portal functions remain with `france-einvoice`; they are not inferred merely from those format names.

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
| Small-invoice exception | EUR150 excluding VAT, inclusive | CGI annexeII242nonies A, II permits omission of I2°(supplier VAT identification) and I12°(exemption/legal-reference wording). It does not generally waive customer VAT identification, reverse-charge wording or another independently imposed particular. |
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

- **Credit notes:** for a taxable cancellation or price reduction where the supplier seeks VAT adjustment, BOI-TVA-DED-40-10-20, II-A80 requires reference to the original invoice and the reduction’s net/VAT amounts, with the stated names, addresses and revised totals. For a year-end rebate that cannot identify one invoice, the source permits a reference to the relevant invoices or contract and their period. A “net of tax” rebate has different express conditions. Record the commercial reason as a working control; this Guide does not claim that every credit note has one universal statutory “reason” field. See https://bofip.impots.gouv.fr/bofip/1100-PGP.html and `france-vat-return`.

### Numbering

- **Invoice numbering:** use a unique chronological and continuous sequence. F-2026-001 and F-2026-002 are internal format illustrations, not a prescribed statutory format or evidence of common practice. Test any separate series against its actual justification.

### Retention

**How long to keep the records**

| What | Value | Note |
| --- | --- | --- |
| Source | all figures below | https://entreprendre.service-public.gouv.fr/vosdroits/F37169 |
| A commercial company keeps its accounting documents and supporting documents, invoices included, for at least this period from the close of the financial year | 10 years | "au moins 10 ans à partir de la clôture de l'exercice comptable" |
| CGI1734: failure to keep or premature destruction of documents within the administration’s communication right, or the stated refusal/obstruction of that right | EUR10,000 | The statutory communication-right conditions apply; this is not an automatic penalty for every commercial-document retention defect. |

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
| Reduced rate, capital condition | At least75% | The capital must be fully paid and held continuously to at least75% by individuals, or by a company satisfying the same conditions whose capital is held at least75% by individuals. Apply the statutory fund exceptions and group-turnover rule where relevant. |
| No quarterly instalments where the corporation tax is below | EUR 3,000 | "Le montant de l'IS est inférieur à 3 000 €" |
| Surcharge for filing the results return other than electronically, share of the tax | 0.2% | "une majoration de 0,2 % du montant de l'impôt" |
| Minimum of that surcharge | EUR 60 | "ne peut pas être inférieure à 60 €" |

Both conditions of the reduced rate must be met (AND). The page, checked on 17 February 2026, says the shares the company holds in itself are left out when testing the ownership condition. A company that fails either condition pays the standard rate on all its profit. Newly created companies, and companies in their first period within corporation tax, make no instalments either.

CGI219I-b states the EUR42,500 reduced-rate slice per twelve-month period, and separately restates turnover to twelve months. Keep the actual period length; a full EUR42,500 slice is not automatically available for every short period. The exact day/month convention for a nonstandard close is not computed here; use `fr-corporate-tax` within its stated limits.

### Social contribution on corporation tax

**Contribution sociale sur l'IS (CGI art. 235 ter ZC)**

| What | Value | Note |
| --- | --- | --- |
| Source | all figures below | https://bofip.impots.gouv.fr/bofip/3492-PGP.html |
| Rate, applied to the corporation tax (not to the profit) after the abatement | 3.3% | "x 3,3 %" |
| Abatement deducted from the relevant corporation-tax base before applying the contribution | EUR763,000 per twelve months | CGI235ter ZC adjusts this amount proportionately for a shorter or longer period. |

**Who is exempt**

| What | Value | Note |
| --- | --- | --- |
| Source | all figures below | https://bofip.impots.gouv.fr/bofip/3491-PGP.html |
| Exemption | Turnover strictly below EUR7,630,000 | Restate turnover to twelve months; for a tax-group parent aggregate member turnover. Company capital must be fully paid and held continuously to at least75% under the stated direct/intermediary and fund conditions. |

A company whose corporation tax is not above the abatement owes no contribution, because the rate applies only to the tax left after the abatement.

### Corporation tax is not deductible

- **IS non-deductibility**: corporation tax itself (account 695) is not a deductible charge and is added back when moving from the accounting result to the taxable result. The basis is CGI art. 213, which "dispose par ailleurs que l'impôt sur les sociétés, l'impôt sur le revenu et la taxe sur les voitures des sociétés visée à l' article 1010 du CGI ne sont pas admis dans les charges déductibles" (https://bofip.impots.gouv.fr/bofip/2102-PGP.html). The earlier version of this skill cited art. 39-1-4°, which is the general rule that taxes are deductible; the exclusion of corporation tax is art. 213.

### Non-deductible charges (common traps)

**Non-deductible charges (common traps)**

| Charge | Rule | Note |
| --- | --- | --- |
| Source | all rows below | https://entreprendre.service-public.gouv.fr/vosdroits/F31973 |
| Luxury/private leisure spending | Not deductible within the statutory scope | The source separately preserves genuinely professional hunting/fishing activities; do not extend the private-leisure exclusion to those professional operations without checking their conditions. |
| Personal spending of a shareholder or director paid by the company | Not deductible; risk of "acte anormal de gestion" | "Les dépenses personnelles de l'exploitant individuel, du dirigeant ou d'un associé ne sont pas déductibles" |
| Corporation tax itself | Not deductible (CGI art. 213, above) | See the art. 213 line above (https://bofip.impots.gouv.fr/bofip/2102-PGP.html) |
| Directors' remuneration in a company under corporation tax | Deductible only where it corresponds to actual work and is not excessive | "déductibles lorsqu'elles correspondent à un travail effectif et ne sont pas excessives" |
| Statutory fines and penalties | Not deductible under CGI39-2 | This covers sanctions for breaching legal obligations; it is not a claim that every contractual compensation payment is a statutory fine. https://bofip.impots.gouv.fr/bofip/1683-PGP.html |

Rows are as printed on the page above (Vérifié le 02 juin 2023) and on BOI-BIC-CHG-40-30 for corporation tax.

### General conditions for deducting a charge

- **Conditions for deducting a charge:** the general conditions in BOI-BIC-CHG-10 (https://bofip.impots.gouv.fr/bofip/3848-PGP.html) require business interest/normal management, an actual adequately supported charge, the correct financial year and no specific exclusion. The separate decrease-in-net-assets/asset-recognition condition is also stated in the official deduction guidance, rather than discarded because it is absent from one summary page. An asset acquisition is not made immediately deductible merely by calling it an expense.

### Small equipment taken to expense

**The small-equipment tolerance**

| What | Value | Note |
| --- | --- | --- |
| Source | all figures below | https://bofip.impots.gouv.fr/bofip/2109-PGP.html |
| Unit value excluding VAT up to which materials and tooling may be deducted at once instead of being capitalised | EUR 500 | "d'une valeur unitaire hors taxes n'excédant pas 500 €" |

This is an optional tax tolerance, not a universal EUR500 capitalisation rule. The source covers its named tools/equipment categories, excludes transport equipment, aggregates connected components and gives specific current-renewal/initial-or-complete furniture conditions; software is a separate named category. Apply those actual conditions before expensing. An otherwise qualifying item can still be capitalised.

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
10. **Results return2065** for corporation tax. Income-tax BIC/BNC filing uses the applicable2031/2035 route in `fr-income-tax`; the corporation-tax page alone is not a complete method for every income-tax entity.
11. **Approval minutes and the filing of the accounts**, with a confidentiality declaration where the company may and wants to use one (https://entreprendre.service-public.gouv.fr/vosdroits/F31214).
12. **Produce the final documents** (PDFs for signature and filing).

### FEC (fichier des écritures comptables)

- **When it is due**: a business that keeps its accounts on a computer meets its duty to present its books by handing over "au début des opérations de contrôle, une copie des fichiers des écritures comptables" (BOI-CF-IOR-60-40-10, https://bofip.impots.gouv.fr/bofip/9026-PGP.html). It is handed over at the start of an audit, not filed each year. It covers corporation tax payers and income tax payers taxed on industrial and commercial, non-commercial or agricultural profits under a real regime.
- **Format**: either a flat sequential file meeting the criteria of art. A. 47 A-1 of the LPF, or an XML file matching the published XSD; the fields and their order are set out in BOI-CF-IOR-60-40-20 (https://bofip.impots.gouv.fr/bofip/9028-PGP.html). The earlier version stated a fixed column count and a pipe separator; those are not printed on the pages read here, so take the field list and the separator from the BOFiP page and the XSD (https://www.impots.gouv.fr/fichiers-standards-des-ecritures-comptables), and see `france-bookkeeping` for the field list.
- **Conformity checks before release:** use the chronological, increasing, unbroken entry sequence and line-by-line audit trail required by the actual FEC specification. As additional working controls, reconcile global debits/credits, each entry’s balance, dates, document references and PCG account roots. The original generic “no negative amounts” claim is not adopted as a universal FEC prohibition; apply the actual debit/credit or amount/direction format and its specification in `france-bookkeeping`.

**Penalty for a file not in the required form (CGI art. 1729 D)**

| What | Value | Note |
| --- | --- | --- |
| Source | all figures below | https://bofip.impots.gouv.fr/bofip/9026-PGP.html |
| Fine where the accounts are not presented in the required form | EUR 5,000 | "d’une amende égale à 5 000 €" |
| Or, where the tax is adjusted and the amount is higher, an increase of the tax charged | 10% | "majoration de 10 % des droits" |

The FEC sanction above applies under its own statutory conditions. The older automatic chain from a format defect to “unreliable accounts” and a general LPF L192 burden-of-proof reversal is not established here and is not adopted. BOI9026 separately discusses failure-of-control consequences; a format check alone does not prove that procedure applies.

## Section 7: Shareholder current account (compte courant d'associé, account 455)

High fiscal risk zone, especially for a SASU or an EURL.

**Interest paid on a shareholder's advances (CGI art. 39-1-3°)**

| What | Value | Note |
| --- | --- | --- |
| Source | all figures below | https://bofip.impots.gouv.fr/bofip/5505-PGP.html |
| Highest deductible rate for a 12-month financial year closed between 30 June 2026 and 29 September 2026 | 4.33% | "Entre le 30 juin 2026 et le 30 juillet 2026 4,33 %" |

The reference is the annual average bank rate for variable-rate business loans with an initial term exceeding two years, not the ECB policy rate. The retained5August2026 BOFiP table prints4.33% for the three stated twelve-month closing-date bands30June–29September2026. It does not establish a31December2026 ceiling. The fully paid capital condition and its specified capital-increase/cooperative exceptions are in BOI-BIC-CHG-50-50-20 (https://bofip.impots.gouv.fr/bofip/2114-PGP.html); the scope overview remains https://bofip.impots.gouv.fr/bofip/2113-PGP.html. Other statutory interest-limitation provisions are separate tests in `fr-corporate-tax`; this dated table is not a complete interest-deduction method for every loan.

**Other current-account checks (working checks)**

| Check | Rule |
| --- | --- |
| Expenses before incorporation | Identify the acts and proposed company-law takeover. The precise adoption procedure and the old six-month assertion are not confirmed by this Guide; do not assume them from an accounting entry. |
| Home office | Establish the actual professional use and evidence. The precise floor-area/plan requirement and company reimbursement treatment are not confirmed here; no automatic deduction for a director’s household or mortgage payment is established. |
| Mixed-use expenses | Only the professional share is a charge |
| Currency conversion | Record the actual rate, date and source. VAT has its own tax-point/ECB rule; annual-account foreign-currency balances have the separate PCG rules. The old universal per-transaction/monthly-average permission is not established here. |

These are working intake checks. They do not supply the unconfirmed company-law/home-office methods. Do not replace the statutory loan reference rate with an ECB rate, or apply one universal currency-conversion method to both VAT and annual accounts.

## Section 8: Fiscal calendar (key deadlines)

**Key deadlines**

| Deadline | Obligation | Source |
| --- | --- | --- |
| Each month, on the day shown in the espace professionnel | CA3 under the régime réel normal | https://www.impots.gouv.fr/le-regime-reel-normal-dates-limites-de-transmission-des-ca3 |
| Each quarter, same rule | CA3 under the régime réel normal where the yearly VAT is below the limit in Section 2 | https://entreprendre.service-public.gouv.fr/vosdroits/F23566 |
| July and December | Simplified-regime VAT instalments (year ending 31 December) | https://entreprendre.service-public.gouv.fr/vosdroits/F23566 |
| Second working day after1May for a calendar-year close; qualified noncalendar route in `france-vat-return` | Annual simplified-regime VAT return | https://entreprendre.service-public.gouv.fr/vosdroits/F23566 |
| 15 March, 15 June, 15 September, 15 December | Corporation tax instalments, form 2571; which date is the first depends on the closing date | https://entreprendre.service-public.gouv.fr/vosdroits/F23575 |
| Within 3 months of the close; for a year closed on 31 December, the second working day after 1 May | Results return 2065 with the liasse fiscale; the administration allows a further 15 calendar days for electronic filing, which gave 20 May 2026 for a year closed on 31 December 2025 | https://entreprendre.service-public.gouv.fr/vosdroits/F23575 |
| 15th day of the 4th month after the close; 15 May for a year closed on 31 December | Corporation tax balance, form 2572 | https://entreprendre.service-public.gouv.fr/vosdroits/F23575 |
| Within6months for SA, SARL/EURL and SASU; a multi-shareholder SAS follows its actual statutory period | Approval of accounts; apply the precise deposit-as-approval conditions for qualifying sole-member entities | https://entreprendre.service-public.gouv.fr/vosdroits/F31214; the controlling SASU/EURL statutes and contrary overview are preserved in `france-financial-statements` |
| Within 1 month of approval, or within 2 months where filed electronically | Filing of the accounts with the registry | https://entreprendre.service-public.gouv.fr/vosdroits/F31214 |

The earlier version gave the results return as "3 months plus a 1-month extension". The page gives 3 months, or the second working day after 1 May for a 31 December close, plus 15 calendar days for electronic filing.

## Section 9: Conservative defaults

**Conservative defaults**

| Ambiguity | Default |
| --- | --- |
| VAT regime unknown | Obtain the required facts and establish franchise, taxable purchases, options and effective dates before deciding the invoice treatment. Do not turn missing evidence into a legal finding that the business owes VAT. |
| Deductibility of a charge doubtful | Not deductible |
| Professional share of a mixed-use expense unclear | Treat it as wholly private and flag it for the accountant |
| Corporation tax rate unclear | The standard rate on all profit; the reduced rate only once both conditions in Section 5 are evidenced |
| Asset or expense | Capitalise, unless the item falls inside the small-equipment tolerance in Section 5 |
| Electronic invoicing start date unclear | Prepare to receive from 1 September 2026; for issuing, confirm the company's size class in `france-einvoice` |

These are internal evidence controls, not substitute tax elections or legal presumptions. The franchise and overrun rules apply to the actual facts; missing records alone do not select a VAT regime.

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

## Executable checks of the existing computations

**IS fixture.** A stipulated ordinary twelve-month company has EUR 60,000 taxable French profit, EUR 1,000,000 turnover restated to twelve months, fully paid capital continuously at least 75% owned by individuals, and satisfies the reduced-rate gates in Section 5. This check calculates IS before any separate contribution, credit or instalment; it assumes no special regime. Existing CGI219/F23575 parameters give EUR 6,375 on the first EUR 42,500 plus EUR 4,375 on the remainder: EUR 10,750. A company ineligible for the reduced rate would instead owe EUR 15,000 before those separate items.

```oa-check
name: France business twelve-month eligible reduced IS
inputs:
  taxable_profit: 60000
  reduced_slice: 42500
steps:
  reduced_tax: min(taxable_profit, reduced_slice) * 0.15
  standard_tax: max(0, taxable_profit-reduced_slice) * 0.25
  corporation_tax: reduced_tax+standard_tax
  ineligible_standard_tax: taxable_profit * 0.25
expected:
  reduced_tax: 6375
  standard_tax: 4375
  corporation_tax: 10750
  ineligible_standard_tax: 15000
```

**VAT fixture.** A stipulated mainland domestic taxable supply is outside the franchise/exemptions and special-rate categories; the existing CGI278 standard 20% rate applies to EUR 2,000 excluding VAT. Output VAT is EUR 400 and the invoice total is EUR 2,400. This is invoice arithmetic, not a determination of any disputed startup-franchise date, tax point, input-deduction entitlement or net return liability.

```oa-check
name: France business ordinary standard-rate invoice
inputs:
  amount_excluding_vat: 2000
steps:
  output_vat: amount_excluding_vat * 0.20
  invoice_total: amount_excluding_vat+output_vat
expected:
  output_vat: 400
  invoice_total: 2400
```

## Sources

- Taux réduits, services (BOI-TVA-LIQ-30-20-100): https://bofip.impots.gouv.fr/bofip/1013-PGP.html Historical/navigation URL retained; this URL body has no accepted direct read claim. Replacement CGI278 current quoted standard/reduced-rate source scopes read 2026-10-29.
- Taux particulier (BOI-TVA-LIQ-40-10): https://bofip.impots.gouv.fr/bofip/1449-PGP.html ; CGI art. 281 octies: https://www.legifrance.gouv.fr/codes/id/LEGISCTA000006191656 (both literal selected blood-product scopes reread31October2026 from the retained official readers; original29October acquisition preserved) Selected cited scope read 2026-10-29.
- Franchise en base de TVA: https://entreprendre.service-public.gouv.fr/vosdroits/F21746 Selected cited scope read 2026-10-29.
- Impôt sur les sociétés, taux, déclaration, paiement (also the simplified VAT regime limits): https://entreprendre.service-public.gouv.fr/vosdroits/F23575 Selected cited scope read 2026-10-29.
- Déclarer et payer la TVA: https://entreprendre.service-public.gouv.fr/vosdroits/F23566 Selected cited scope read 2026-10-29.
- Dates limites de transmission des CA3: https://www.impots.gouv.fr/le-regime-reel-normal-dates-limites-de-transmission-des-ca3 Historical/navigation URL retained; this URL body has no accepted direct read claim. Replacement F23566 current quoted CA3 procedural source read 2026-10-29.
- Notice, TVA à l'importation: https://www.impots.gouv.fr/sites/default/files/media/1_metier/2_professionnel/EV/2_gestion/210_declarer_payer/tva_a_limportation_-_notice.pdf Selected cited scope read 2026-10-29.
- Facturation électronique, start dates: https://www.impots.gouv.fr/professionnel/questions/partir-de-quand-suis-je-concerne-par-la-reforme-de-la-facturation Selected cited scope read 2026-10-29.
- Je découvre la facturation électronique: https://www.impots.gouv.fr/professionnel/je-decouvre-la-facturation-electronique Selected cited scope read 2026-10-29.
- Mentions obligatoires sur une facture: https://entreprendre.service-public.gouv.fr/vosdroits/F31808 Selected cited scope read 2026-10-29.
- Obligations comptables d'une société commerciale: https://entreprendre.service-public.gouv.fr/vosdroits/F37169 Selected cited scope read 2026-10-29.
- Délais de conservation des documents: https://entreprendre.service-public.gouv.fr/vosdroits/F10029 Selected cited scope read 2026-10-29.
- Dépôt des comptes annuels: https://entreprendre.service-public.gouv.fr/vosdroits/F31214 Selected cited scope read 2026-10-29.
- Charges déductibles du résultat fiscal: https://entreprendre.service-public.gouv.fr/vosdroits/F31973 Selected cited scope read 2026-10-29.
- Contribution sociale sur l'IS, calcul (BOI-IS-AUT-10-20): https://bofip.impots.gouv.fr/bofip/3492-PGP.html Historical/navigation URL retained; this URL body has no accepted direct read claim. Replacement CGI235terZC current quoted contribution calculation read 2026-10-29.
- Contribution sociale sur l'IS, exonérations (BOI-IS-AUT-10-10): https://bofip.impots.gouv.fr/bofip/3491-PGP.html Historical/navigation URL retained; this URL body has no accepted direct read claim. Replacement CGI235terZC current quoted exemption conditions read 2026-10-29.
- Impôts et taxes, art. 213 (BOI-BIC-CHG-40-30): https://bofip.impots.gouv.fr/bofip/2102-PGP.html Selected cited scope read 2026-10-29.
- Conditions générales de déduction (BOI-BIC-CHG-10): https://bofip.impots.gouv.fr/bofip/3848-PGP.html Selected cited scope read 2026-10-29.
- Petits matériels et outillages (BOI-BIC-CHG-20-30-10): https://bofip.impots.gouv.fr/bofip/2109-PGP.html Selected cited scope read 2026-10-29.
- Intérêts des comptes courants, champ (BOI-BIC-CHG-50-50-10): https://bofip.impots.gouv.fr/bofip/2113-PGP.html Historical/navigation URL retained; this URL body has no accepted direct read claim. Replacement CGI39/212 current quoted shareholder-interest conditions read 2026-10-29.
- Intérêts des comptes courants, taux limite (BOI-BIC-CHG-50-50-30): https://bofip.impots.gouv.fr/bofip/5505-PGP.html Selected cited scope read 2026-10-29.
- FEC, remise de la copie (BOI-CF-IOR-60-40-10): https://bofip.impots.gouv.fr/bofip/9026-PGP.html Selected cited scope read 2026-10-29.
- FEC, format (BOI-CF-IOR-60-40-20): https://bofip.impots.gouv.fr/bofip/9028-PGP.html Selected cited scope read 2026-10-29.
- Fichiers standards des écritures comptables: https://www.impots.gouv.fr/fichiers-standards-des-ecritures-comptables Historical/navigation URL retained; this URL body has no accepted direct read claim. Replacement BOI-CF-IOR-60-40-20 current quoted FEC-format source read 2026-10-29.

Not yet confirmed: the precise startup-franchise source conflict and noncalendar simplified-VAT reconciliation; a universal credit-note reason field; exact nonstandard-period reduced-rate proration convention; pre-incorporation adoption timing; the home-office floor-area/plan and reimbursement method; a universal monthly-average currency permission; an automatic LPF L192 burden reversal from an FEC format defect; the31December2026 shareholder-interest ceiling; and specialist reduced-rate, e-invoice and consolidated/group methods routed to their named companions.

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
