---
name: france-einvoice
description: Use this skill whenever asked about French e-invoicing, facturation électronique, Chorus Pro, Factur-X, Plateforme Agréée (PA), Plateforme de Dématérialisation Partenaire (PDP), Portail Public de Facturation (PPF), e-reporting France, B2B e-invoicing mandate France 2026, lifecycle statuses, or any question about issuing, receiving, validating, or archiving electronic invoices in France. Also trigger when preparing invoices for submission via a certified platform, configuring PA/PDP connectivity, handling e-reporting obligations for B2C or cross-border transactions, or advising on Factur-X profile selection. This skill covers accepted formats (Factur-X, UBL 2.1, CII), the PPF/PA architecture, mandatory fields, validation rules, archiving, penalties, and interaction with French VAT returns. ALWAYS read this skill before touching any French e-invoicing work.
version: 1.2
jurisdiction: FR
tax_year: 2026
last_updated: 2026-10-31
review_status: pending_review
trust_label: Built by Michael Cutajar and the OpenAccountants team
drafted_by: OpenAccountants
approved_by: pending
depends_on:
  - einvoice-workflow-base
category: invoicing
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# French e-invoicing (facturation électronique) and e-reporting

France's business-to-business e-invoicing reform is in force. The tax administration's hub page, modified on 1 September 2026, calls it "effective depuis le 1er septembre 2026". Its dates page, modified on 16 January 2026, sets the second stage at 1 September 2027. Neither page marks either date provisional, conditional or awaiting a further law. No allowed official page describes the timetables published before these, so treat any earlier date as superseded by the two dates in this Guide. Figures are for tax year 2026. The administrative size footnotes come from fiche 3, now updated October 2026, with the operative nested classification and 1 January 2025 reference date supplied below. The e-reporting table is dated August 2026; the retention page was checked on 1 July 2024. The currently published rollout is 1 September 2026/2027; LFR 2022 article 26 III also contains a delegated later-date power capped at 1 December of the respective year, which is not itself a postponement.

## Section 1: Quick Reference

| Field | Value |
| --- | --- |
| Status | In force since 1 September 2026 |
| How invoices move | Only through a plateforme agréée, or a compatible solution connected to one |
| B2G platform | Chorus Pro |
| Authority | DGFiP |
| Legislation | CGI art. 289 bis; penalties under CGI art. 1737 IV bis and CGI art. 1788 D |
| Receive electronically | All businesses, from 1 September 2026 |
| Issue electronically | Large enterprises and ETI from 1 September 2026; PME/micro qualifying for the statutory deferral from 1 September 2027; see the VAT-group exclusion below |

There is no free State platform and no single public portal that invoices pass through. Every business in scope chooses its own plateforme agréée. The administration's own FAQ says the market carries free or low cost offers for the simplest needs, so no free State platform does not mean no free option.

### Who Must Comply

Dates: [À partir de quand suis-je concerné](https://www.impots.gouv.fr/professionnel/questions/partir-de-quand-suis-je-concerne-par-la-reforme-de-la-facturation). Scope: [Je découvre](https://www.impots.gouv.fr/professionnel/je-decouvre-la-facturation-electronique).

| Scope | Requirement |
| --- | --- |
| Receive, all sizes | By 1 September 2026 every business must have chosen an approved platform for receiving. From that date it receives electronically whenever its supplier is obliged to issue that way |
| Issue, stage 1 | From 1 September 2026: large enterprises and entreprises de taille intermédiaire, with transaction and payment data |
| Issue, stage 2 | From 1 September 2027: PME and micro-enterprises eligible for the statutory deferral, excluding CGI256C VAT-group members |
| In scope | Every business established in France and liable to French VAT, whatever its turnover, legal form or regime: the franchise en base, independents, the professions and micro-entrepreneurs included. A business that issues no invoice must still receive |
| Outside e-invoicing | Sales to private individuals and to businesses established abroad. Paper or PDF stays lawful, but e-reporting may apply |
| Outside everything | Operations exempt under CGI articles 261 to 261 E and dispensed from invoicing: health, teaching, property, non-profit, banking, insurance |

A paper, PDF or e-mailed invoice received after 1 September 2026 is not void. The startup guide answers the question directly: it must not be set aside for that reason alone, so long as it matches a real operation and carries what is needed to process it. It may then be processed and paid. On the VAT, the guide is narrower: the fact that an invoice did not come through the expected electronic route does not automatically deprive the business of its right to deduct, and the right to deduct is still judged against the ordinary conditions of substance and form. The reform changes how an invoice travels, not the rules on the existence of the operation, the debt, payment, bookkeeping or deduction. Where the supplier was obliged to issue electronically, it may be invited to send or regularise the same invoice through the expected route. That request is not obligatory at the start of the reform and is not a condition of the received invoice's validity, processing, payment or deduction; a regularisation must not create a double payment, a double entry or a double deduction.

Size decides who issues first. The fiche joins the three measures differently in each class, so read the row, not a rule of thumb: headcount alone can make a grande entreprise, while the other classes join headcount to a turnover or balance sheet test.

| Size class | Definition on the official fiche |
| --- | --- |
| Source | https://www.impots.gouv.fr/sites/default/files/media/1_metier/2_professionnel/EV/2_gestion/290_facturation_electronique/fiche-3_tpe_a-partir-de-quand-mon-entreprise-doit-etre-prete.pdf |
| Grande entreprise (GE) | Headcount over 5,000, or turnover over EUR 1.5 billion with balance sheet total over EUR 2 billion |
| Taille intermédiaire (ETI) | Headcount over 250 and under 5,000, and turnover under EUR 1.5 billion or balance sheet total under EUR 2 billion |
| Petite et moyenne (PME) | Headcount over 10 and under 250, and turnover under EUR 50 million or balance sheet total under EUR 43 million |
| Microentreprise | Headcount under 10, and turnover under EUR 2 million or balance sheet total under EUR 2 million |

The fiche prints strict inequalities and leaves equality cases unclear. The operative classification is available: decree 2008-1354 article 3 defines micro as fewer than 10 people and turnover or balance sheet no more than EUR 2 million; PME as fewer than 250 and turnover no more than EUR 50 million OR balance sheet no more than EUR 43 million; ETI as not PME, fewer than 5000 and turnover no more than EUR 1.5 billion OR balance sheet no more than EUR 2 billion; GE is the residual category. Thus 10 employees can be PME, 250 can be ETI and 5000 is GE, subject to the financial tests. For this reform, current LFR 2022 article 26 III applies the category to EACH LEGAL PERSON at 1 January 2025 using its last closed financial year before that date, or its first closed year from that date if none existed. The 2027 issuing deferral for PME/micro excludes members of a CGI 256C single taxable person. The same phased dates apply to the specified transaction/payment reporting. Sources: https://www.legifrance.gouv.fr/loda/article_lc/LEGIARTI000019970722 and https://www.legifrance.gouv.fr/loda/article_lc/LEGIARTI000053546715 . The older strict fiche footnotes remain above as a disclosed administrative comparison, not the deciding equality algorithm.

Having to receive does not mean having to issue: the fiche says a small or micro-enterprise invoicing a large customer already inside the reform need not issue electronically before 1 September 2027, and that the supplier, not the customer, must know which duty binds the supplier. Early entry is allowed.

### E-Reporting Obligation

Transaction e-reporting covers sales to persons who are not taxable (private individuals, non-profit bodies) and transactions with businesses established abroad, VAT-registered here or not: exports, intra-EU acquisitions and supplies. Payment e-reporting covers operations where VAT falls due on receipt, typically services, unless the business opted for the debits or the operation is reverse-charged. The data are daily totals split by rate for non-taxable customers, invoice data with the foreign party’s SIREN replaced, where applicable, by an intra-EU VAT number OR a foreign identification number, and the date and amount received for payments.

| VAT regime | Transaction data | Payment data |
| --- | --- | --- |
| Source | all figures below | https://www.impots.gouv.fr/sites/default/files/media/1_metier/2_professionnel/EV/2_gestion/290_facturation_electronique/japprof_frequences-et-delais-de-transmission.pdf |
| Réel normal mensuel | Three filings a month (1st to 10th, 11th to 20th, 21st to month end), due the 20th, the 30th (except February) and the 10th of the next month | Monthly, before the 10th of the next month |
| Réel normal trimestriel, open to businesses paying less than EUR 4,000 of VAT a year | Monthly, before the 10th of the next month | Monthly, before the 10th of the next month |
| Régime simplifié | Monthly, between the 25th and the 30th of the next month | Same |
| Franchise en base | Every two calendar months, between the 25th and the 30th of the month after the period | Same |

### Timeline Summary

[Tout savoir sur la facturation](https://entreprendre.service-public.fr/vosdroits/F23208), checked 7 August 2026.

| Date | Milestone |
| --- | --- |
| Since 2020 | Payment requests to a public body go through Chorus Pro |
| 1 September 2026 | All businesses receive. Large enterprises and ETI also issue, and transmit data |
| 1 September 2027 | Issuing and data transmission extend to PME and micro-enterprises |

Both dates are stated flatly on the administration's own pages, with no condition and no reservation attached. If a date changes again it will change there first, so read [À partir de quand suis-je concerné](https://www.impots.gouv.fr/professionnel/questions/partir-de-quand-suis-je-concerne-par-la-reforme-de-la-facturation) before quoting either.

### Accepted Formats

Source: [Je découvre](https://www.impots.gouv.fr/professionnel/je-decouvre-la-facturation-electronique).

| Item | What the official page says |
| --- | --- |
| Requirement | "respecter un format donné (UBL, CII ou tout format mixte composé d'un fichier de données structurées et d'un fichier image)" |
| Structured formats | UBL and CII |
| Mixed (hybrid) format | A structured data file plus an image file. The current DGFiP v3.2 dossier expressly names Factur-X alongside UBL and CII |
| Not an electronic invoice | A PDF sent by e-mail |

The specifications page names the standards: formats and lifecycle statuses (XP Z12-012), interfaces (XP Z12-013), use cases (XP Z12-014). AFNOR publishes them for free download.

| What | Value | Note |
| --- | --- | --- |
| Source | all figures below | https://www.impots.gouv.fr/specifications-externes-b2b |
| Current PPF formats versus older vendor references | The current v3.2 official dossier explicitly gives UBL 2.1 and CII D22B for PPF support | Dossier edition 3.2 is dated 30/04/2026; the older dossier 2.1 dated 29/07/2022 is an edition number, not a UBL version. CII D16B remains an older technical reference, not the current PPF language selected in that dossier. Agree the applicable invoice/profile release with the platform; a PPF regulatory-data schema is not by itself a full B2B invoice validation certificate |

### Factur-X Profiles

The following ladder is a technical taxonomy from the standard maintainer FNFE-MPE, not a statute or an assertion that every profile is sufficient for a 2026 French invoice. Its current page identifies MINIMUM, BASIC WL, BASIC, EN16931 and EXTENDED; its 4 August 2026 release note describes the current Factur-X 1.09.2/ZUGFeRD 2.5.2 package and French EXTENDED-CTC-FR reference. The introductory profile list still calls EXTENDED under development while the dated release says its artefacts exist: use the actual applicable release and platform/AFNOR requirements, not that stale introductory sentence. Source: https://fnfe-mpe.org/factur-x/ and https://fnfe-mpe.org/factur-x/factur-x-et-zugferd/ .

| Profile | Use case |
| --- | --- |
| Minimum | Minimum header/footer data; the maintainer compares this to header OCR capture, without certifying that it alone meets every current French requirement |
| Basic WL | No line detail |
| Basic | With line items |
| EN16931 (formerly called Comfort in older references) | The profile containing the European semantic standard data; applicable French validation rules remain separate |
| Extended | Data beyond the European standard |

The official requirement is simpler: a structured invoice with the mandatory mentions, through an approved platform.

### Key Technical Parameters

Technical scope matters. The FNFE-MPE package describes PDF/A-3 and the current official PPF dossier specifies UTF-8 for files generated by the PPF and XML it receives. The legacy embedded filename and national-CIUS label below have not been checked against the applicable current AFNOR/Factur-X artefacts and are retained as explicit boundaries, not production configuration instructions.

| Parameter | Value |
| --- | --- |
| Hybrid container | PDF/A-3 with an embedded structured file |
| Embedded file name, not yet confirmed | Legacy reference `factur-x.xml`; verify the exact current release before configuring it |
| UBL namespace, retained original technical field | `urn:oasis:names:specification:ubl:schema:xsd:Invoice-2`, as the targetNamespace of the official v3.2 bundle’s F1 FULL UBL invoice XSD; a namespace alone does not validate an invoice |
| CII namespace, retained original technical field | `urn:un:unece:uncefact:data:standard:CrossIndustryInvoice:100`, as the targetNamespace of its F1 FULL CII D22B XSD; the namespace does not establish a profile/version by itself |
| Encoding | UTF-8 for files generated by the PPF and XML files received by it, as stated in the current official dossier |
| French profile, not yet confirmed as a general CIUS label | Legacy description: a national CIUS of EN16931. Current maintainer material instead names EXTENDED-CTC-FR within EXTENDED; do not equate these labels without the applicable artefact |
| Lifecycle statuses | Defined by XP Z12-012 |

### Core Invoice Fields (EN 16931 Business Terms)

These are semantic mapping labels, not a complete French schema or a statement that every field is mandatory in every invoice. The current official DGFiP Annex1 identifies the listed invoice/date/type/currency/due-date/specification/SIREN/VAT fields for regulatory flux1. Generic EN16931 validation clauses support the other name/address identifiers; the standards publisher OpenPeppol also labels buyer reference BT-10. Reuse of those semantic labels does not import German or Peppol-only mandatory-field rules into France. Applicable French invoice validation still needs the actual AFNOR/profile release.

| Term code | Field |
| --- | --- |
| BT-1 | Invoice number |
| BT-2 | Issue date |
| BT-3 | Invoice type code |
| BT-5 | Currency code |
| BT-9 | Payment due date |
| BT-10 | Buyer reference |
| BT-24 | Specification identifier |
| BT-27 | Seller name |
| BT-30 | Seller SIREN |
| BT-31 | Seller VAT identifier |
| BT-34 | Seller electronic address |
| BT-44 | Buyer name |
| BT-47 | Buyer SIREN |
| BT-48 | Buyer VAT identifier |
| BT-49 | Buyer electronic address |

### France-Specific Additional Fields

The reform adds four mandatory mentions so the invoice can be routed automatically. Source: [J'approfondis mes connaissances sur la réforme](https://www.impots.gouv.fr/japprofondis-mes-connaissances-sur-la-reforme), modified 6 January 2026. The count of structured data items and the routing directory come from the administration's [Foire aux questions](https://www.impots.gouv.fr/sites/default/files/media/1_metier/2_professionnel/EV/2_gestion/290_facturation_electronique/faq_tout_savoir_facturation-electronique.pdf).

| Item | What the administration says |
| --- | --- |
| New mention 1 | The customer's SIREN number |
| New mention 2 | The category of the operation: goods, services, or both as distinct items |
| New mention 3 | That the supplier has opted to pay VAT on the debits, where that applies |
| New mention 4 | The delivery address of the goods, only where it differs from the billing address |
| Everything else | The mentions required by the Code de commerce and the Code général des impôts are unchanged |
| Data carried | An electronic invoice carries 34 items of data in structured form |
| Routing | A directory (annuaire) provided by the administration routes the invoice to the recipient's platform |

| Mention | When it applies | Note |
| --- | --- | --- |
| Source | all figures below | https://entreprendre.service-public.fr/vosdroits/F31808 |
| The seller's VAT identification number, and the business customer's where the customer is liable for the VAT | Except where the invoice total excluding tax is at most EUR 150 | "inférieur ou égal à 150 €" |
| "TVA non applicable, art. 293 B du code général des impôts" | Seller under the franchise en base | Verbatim |
| "Auto-liquidation" | The customer is liable for the VAT | Verbatim |
| "Option pour le paiement de la taxe d'après les débits" | Supplier taxed on the debits | Also a new mention |
| "Auto-facturation" | Where the customer draws up the invoice in the seller's place | |
| Recovery indemnity of EUR 40 and the late-payment penalty rate | Every business-to-business invoice | "indemnité forfaitaire de 40 €" |
| Eco-participation, copie privée | Electrical, electronic or furniture products; recording media | |

### Architecture Overview

The model is distributed. The State deliberately did not build one portal that all invoices pass through.

1. The seller issues through its own plateforme agréée, or a compatible solution connected to one.
2. That platform sends the invoice to the platform the buyer chose. Platforms must be interoperable.
3. The platforms extract the data the administration needs and transmit it, with the e-reporting data.
4. The State supplies the shared plumbing, not the pipe: the annuaire, the concentrateur and the exchange system, each an "outil mis à disposition par l'État".

The Portail Public de Facturation still exists but is no longer where businesses exchange invoices: it provides directory and declaration services, and platforms must prove interoperability with it. Asked "Pourquoi n'y a-t-il pas de plateforme gratuite de l'État ?", the FAQ answers that France chose not to create a single public portal, to avoid concentrating technical risk on one crossing point. The FAQ also makes Peppol optional, not the official channel.

### Platforms

Source: [Liste des plateformes agréées](https://www.impots.gouv.fr/je-consulte-la-liste-des-plateformes-agreees).

| Platform | Role |
| --- | --- |
| Plateforme agréée (PA) | An operator registered by the State. It issues, transmits and receives electronic invoices, extracts the data the administration needs and transmits the e-reporting data. Formerly plateforme de dématérialisation partenaire (PDP) |
| Registration test | Tax compliance, security of infrastructure and data, interoperability with the PPF and other platforms, then real-condition tests |
| Two lists | Operators meeting every condition, and operators awaiting final registration. An operator on the second list is not yet approved |
| Solution compatible | Software that is not a platform but connects to one |
| Portail Public de Facturation (PPF) | Directory and declaration services, and the counterparty every platform must interoperate with. Not an exchange platform |
| Chorus Pro | The reference platform for public-sector invoicing |

### Chorus Pro (B2G) Transmission

Sources: [F23208](https://entreprendre.service-public.fr/vosdroits/F23208), [Spécifications externes](https://www.impots.gouv.fr/specifications-externes-b2b).

| Item | Detail |
| --- | --- |
| Obligation | Public bodies issue and receive through Chorus Pro. Since 2020 a business holding a public contract must request payment through it |
| Covers | State, local authorities, public establishments |
| Payment | The buyer then has a set period to pay |
| Relation to the reform | The specifications treat exchanges with Chorus Pro separately from those with the PPF |

The current official DGFiP bundle includes the Chorus Pro dossier. Its B2G section says a private supplier can use a PA or the existing Chorus Pro portal entry/upload, EDI or API routes, with its Chorus Pro account and SIRET structure created beforehand. The first three channels below therefore have current primary technical support. The separate Peppol-to-Chorus access-point route remains unconfirmed here; the administration only establishes that Peppol is optional in France.

| Channel | Current support or precise legacy boundary |
| --- | --- |
| Web portal | Manual deposit by a user signed in to the Chorus Pro portal |
| Interface | A programmatic interface for systems that submit automatically |
| Structured exchange | Bulk deposit of structured files for high-volume senders |
| Peppol | An access point connected to Chorus Pro. The administration's own FAQ says Peppol is optional in France, not the official channel |

### Invoice Lifecycle Statuses

The startup guide draws one distinction that matters more than the list: a rejection by a platform is not a refusal by the buyer.

| Status | What it means |
| --- | --- |
| Deposited | Submitted by the seller to its platform |
| Received | Delivered to the buyer's platform |
| Rejected by a platform | A technical or control failure: a party wrongly identified, a routing difficulty, a blocking anomaly. Correct and resend |
| Refused by the buyer | A lifecycle status, not a fault. It must be reasoned, and only for the reasons the standard allows |
| Accepted | The buyer accepts the invoice |
| Disputed, retained original status topic | The buyer disagrees with all or part of the invoice; the official dossier labels this optional status207 |
| Payment transmitted, retained original payment-status topic | The buyer reports payment, or supplier reports reimbursement; optional status211. This is distinct from the supplier’s collection status212 used under the payment-data conditions |
| Collected | Used for payment e-reporting: the receipt completes the invoice as a status |

If the parties keep an invoice the buyer refused, they must justify it: lifecycle data, pre-filled VAT figures and the return filed have to reconcile. There is an actual source difference: the April v3.2 general dossier says refused/rejected statuses require an internal accounting credit note without a new regulatory-data flow, while the later July startup guide distinguishes an accepted refusal from a contested refusal and says not to create a new invoice or credit solely because a refusal status was set. Do not treat the earlier blanket instruction as a universal override of that later fact-dependent workflow; the exact operational reconciliation beyond the supplied startup cases remains unconfirmed.

### Pre-Submission Validation

| Check | Description |
| --- | --- |
| Structured format | Conforms to a format the reform accepts |
| Identifiers | Both parties identified by SIREN; the customer's is now mandatory |
| VAT number format | The letters FR, two check characters and the nine-digit SIREN |
| Mandatory mentions | Present, including the four new ones, in dedicated fields |
| Internal consistency | Line amounts, VAT per rate and the totals agree |
| Addressability | The customer appears in the annuaire with a chosen platform |

### Common Rejection Reasons

| Issue | Resolution |
| --- | --- |
| The customer has no platform | The invoice cannot be delivered electronically because the customer's address is not in the annuaire, and the sending platform tells the supplier the invoice was rejected or could not be delivered. The FAQ allows the invoice to be sent by e-mail or by post as an exception, which changes nothing about when the debt falls due or about payment. Chase the customer to choose a platform |
| Party wrongly identified | Correct the SIREN or the electronic address and resend |
| Missing new mention | Add the customer's SIREN, the operation category, the debits option or the delivery address |
| Amounts do not reconcile | Make line VAT and document totals agree before sending |
| Duplicate through two channels | Compare number, supplier, customer, date, net, VAT and total; where they match, designate one |
| Refusal read as a rejection | A refusal carries a reason and is settled commercially |

### VAT Rates (2025/2026)

The invoice carries the ordinary French VAT rate; the reform changes none.

| Rate | Application | Note |
| --- | --- | --- |
| Source | all figures below | https://bofip.impots.gouv.fr/bofip/1013-PGP.html |
| 20% | Standard rate (taux normal), wherever no other rate is provided | "la seconde du taux de 20 %" |
| 10% | Intermediate rate: television subscriptions, qualifying work on residential premises completed more than two years ago, excluding the actual specified equipment, new-building/>10%extension, cleaning/green-space and fossil-boiler operations under CGI279-0bis; check `france-vat-return`, restaurant meals | "soumet au taux de 10 % de la TVA les abonnements" |
| 5.5% | Reduced rate: most food, books, qualifying CGI278-0bisA energy-renovation work on residential premises completed at least two years ago, meeting the delegated nature/performance and certification conditions; new-building/>10%extension and fossil-boiler supply/installation are excluded; check `france-vat-return` | "relevant du taux réduit de 5,5 % de la TVA" |

| Rate | Application | Note |
| --- | --- | --- |
| Source | all figures below | https://bofip.impots.gouv.fr/bofip/1449-PGP.html |
| 2.1% | Special rate: reimbursable medicines, some press, blood-prepared labile products for human research and in-vitro diagnostic devices only, subject to the direct-therapeutic whole-blood/derivatives exemption; check `france-vat-return` | "Produits imposables au taux particulier de 2,10 %" |

Exempt supplies carry no rate, only the legal mention.

### Rounding

The current official v3.2 Annex7 supplies specific controls. Its BR-CO-17 says VAT per category equals that category’s taxable base multiplied by its rate, rounded to two decimals. G1.55 allows a one-cent tolerance for the stated net-price = gross-price minus discount reconciliation. G1.53 allows a one-cent tolerance for the stated e-reporting net/TVA-total-to-category-total checks, with its euro-currency condition for the VAT-total check. These are the identified controls and flux scopes, not a universal licence to alter VAT, accept every one-cent discrepancy or apply the same tolerance to all French invoice fields. Apply the actual invoice/profile rules and reconcile the data with the VAT return.

### Multi-Rate Invoice Handling

Each VAT rate needs its own tax subtotal, and the invoice must distinguish taxable, exempt and reverse-charged amounts. A reverse-charged line carries no VAT and must carry "Auto-liquidation". Day totals for e-reporting are split by rate too.

### Discount and Charge Handling

A document-level discount or charge changes the taxable base; a line-level discount changes the line's net amount. Each must state its VAT category, or the subtotals will not reconcile. Where there is no early-payment discount the business portal expects "Escompte pour paiement anticipé : néant".

## Section 8: Archiving Requirements

The approved platform keeps the invoice, but the legal duty stays with the business. Periods: [Délais de conservation](https://entreprendre.service-public.fr/vosdroits/F10029).

| Requirement | Detail |
| --- | --- |
| Accounting records and vouchers | Books, ledgers and supporting documents, customer and supplier invoices included: 10 years from the close of the financial year |
| Tax documents | Records open to the administration's rights of communication, enquiry and audit: 6 years; the official retention page states 10 years for concealed activity |
| When the tax period runs from | The last operation recorded, or the date the document was drawn up |
| Commercial correspondence | 5 years, paper or electronic |
| Through what | The business portal says the electronic invoice is issued, transmitted, received and kept through an approved platform, or a compatible solution connected to one. No allowed official page says what the business itself must keep of the structured file and the readable image, so settle that with the platform |

## Section 9: Penalties for Non-Compliance

Current law supplies the amounts. CGI 1737 III sets EUR 50 per non-compliant issuing invoice, capped at EUR 15,000 per calendar year. Article 1737 IV bis first requires a three-month receiving-platform notice: persistence triggers EUR 500, another three-month notice can trigger EUR 1,000, and each further unsuccessful three-month notice can trigger another EUR 1,000. CGI 1788 D I/II set EUR 500 per missed transaction/payment-data transmission, each statutory obligation capped at EUR 15,000 per calendar year; platform failures have separate EUR 750/100,000 rules. The first-infringement repair safe harbour in 1737 V applies to its listed sanctions, including issuing but not the separate IV bis notice sequence; 1788 D V has its own current-year/three-previous-years first-offence and spontaneous/30-day-after-request repair rule. These are the statutory schedules, distinct from the startup administrative approach below. Sources: https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000053293950/2999-01-01 and https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000053546693/2026-09-22 . The [guide pratique de démarrage](https://www.impots.gouv.fr/sites/default/files/media/1_metier/2_professionnel/EV/2_gestion/290_facturation_electronique/guide_pratique_facturation_electronique.pdf) says this much.

| Failure | Consequence as the official guide states it |
| --- | --- |
| Not issuing electronically when required | A fine per invoice, within the limits set by CGI art. 1737 |
| No platform chosen for receiving | A formal notice to comply within three months first; the fine applies only if the failure persists. CGI art. 1737 IV bis, CGI art. 289 bis |
| Not transmitting the required data | Sanctioned under the transmission provisions; the guide names no amount |
| Startup period | The administration's FAQ answers "Y aura-t-il des sanctions en 2026 ?" with "Non", while stating that a sanctions regime does exist and that its approach will be educational and proportionate. The guide pratique says sanctions will not apply to a business in difficulty that is on a serious compliance path, and never immediately, automatically and blindly |
| The limit of that indulgence | It is neither a postponement nor a suspension of the obligation, and it does not cover ignoring the duty for long, taking no step, refusing to enter the system, deliberately keeping parallel routes without regularising, or using startup difficulty as a pretext to block payments |
| Third-party failure | No sanction for a third party's failure where the business took the steps that were its own |

### VAT Return Integration

Pre-filling the VAT return is an announced objective, not a rule in force: the administration lists it among the reform's aims, simplifying VAT obligations "à terme". Until then the business still files. What changes now is that the data behind the return reaches the administration through the platforms.

### Income Tax Integration

The allowed official pages name VAT pre-filling only, not income tax or professional income returns, so the legacy claim that e-invoicing feeds a micro-entrepreneur's revenue declaration is dropped.

### Chorus Pro and Public Accounting

Invoicing a public body stays on its own track through Chorus Pro. The allowed pages do not describe how Chorus Pro connects to internal public accounting systems, so nothing is asserted here.

### Cross-Border Considerations

An invoice to a business established abroad is outside e-invoicing and may still be paper or PDF. It is inside transaction e-reporting, as are exports and intra-EU acquisitions and supplies, with the foreign party’s SIREN replaced, where applicable, by an intra-EU VAT number or a foreign identification number.

## The method, step by step

1. Fix the two dates. Classify each legal person under the operative nested size test and 1 January 2025 reference date above, including the VAT-group exclusion from the deferred phase, then apply [À partir de quand suis-je concerné](https://www.impots.gouv.fr/professionnel/questions/partir-de-quand-suis-je-concerne-par-la-reforme-de-la-facturation): everyone receives since 1 September 2026; a grande entreprise or ETI issues since then, a PME or micro-enterprise qualifying for the statutory deferral from 1 September 2027.
2. Choose a platform and check it is registered, on the [list of plateformes agréées](https://www.impots.gouv.fr/je-consulte-la-liste-des-plateformes-agreees). An operator awaiting registration is not approved. The platform declares the choice through the annuaire.
3. Map the operations, using [J'approfondis mes connaissances sur la réforme](https://www.impots.gouv.fr/japprofondis-mes-connaissances-sur-la-reforme). Sales to French businesses are e-invoicing under CGI art. 289 bis; sales to individuals and foreign businesses are transaction e-reporting; services taxed on receipt without the debits option are payment e-reporting.
4. Add the four new mentions, check the standing ones against [Mentions obligatoires sur une facture](https://entreprendre.service-public.fr/vosdroits/F31808), and set the e-reporting calendar from the frequency table above.
5. Keep the public-sector route on Chorus Pro, per [Tout savoir sur la facturation](https://entreprendre.service-public.fr/vosdroits/F23208), and agree the archive against [the retention page](https://entreprendre.service-public.fr/vosdroits/F10029). The platform's copy does not discharge the client's duty.

## Ask the client first

- Headcount, turnover and balance sheet total? Together they decide whether the client had to issue from 1 September 2026 or has until 1 September 2027.
- Who are the customers: French businesses, private individuals, public bodies, foreign businesses? Each means a different obligation, and most clients are in more than one.
- Which VAT regime, and is the VAT under EUR 4,000 a year? The regime sets the e-reporting rhythm.
- Has the client opted to pay VAT on the debits? If not, services generate payment e-reporting and the invoice must not carry the debits mention.
- Established in France, or only VAT-registered here? A business without an establishment can still owe e-reporting.
- Which platform has the client chosen? Without one in the annuaire the client cannot receive through the mandated electronic circuit. The actual FAQ exceptionally permits e-mail/post without changing the debt or payment; this does not remove the duty to choose an approved receiving platform. Use the fallback and ordinary invoice-validity/processing/deduction conditions above.

## When to refuse or refer

- A contested penalty, first-infringement history or formal notice: use the actual statutory schedules and repair gates above, then establish the relevant facts and procedure.
- Choosing between named commercial platforms, or their contracts and pricing.
- Technical integration: schema mapping, interfaces, profile selection inside the AFNOR standards.
- Exempt activities dispensed from invoicing: they need their own advice.
- Public-sector questions beyond the duty to use Chorus Pro, such as payment delays and contract disputes.
- Any client facing an audit or a formal notice.

## Sources

- [Hub: la facturation électronique](https://www.impots.gouv.fr/professionnel/je-passe-la-facturation-electronique)
- [Je découvre](https://www.impots.gouv.fr/professionnel/je-decouvre-la-facturation-electronique)
- [J'approfondis](https://www.impots.gouv.fr/japprofondis-mes-connaissances-sur-la-reforme)
- [À partir de quand suis-je concerné](https://www.impots.gouv.fr/professionnel/questions/partir-de-quand-suis-je-concerne-par-la-reforme-de-la-facturation)
- [Liste des plateformes agréées](https://www.impots.gouv.fr/je-consulte-la-liste-des-plateformes-agreees)
- [Spécifications externes](https://www.impots.gouv.fr/specifications-externes-b2b)
- [Fiche 3: dates and sizes](https://www.impots.gouv.fr/sites/default/files/media/1_metier/2_professionnel/EV/2_gestion/290_facturation_electronique/fiche-3_tpe_a-partir-de-quand-mon-entreprise-doit-etre-prete.pdf)
- [E-reporting frequencies](https://www.impots.gouv.fr/sites/default/files/media/1_metier/2_professionnel/EV/2_gestion/290_facturation_electronique/japprof_frequences-et-delais-de-transmission.pdf)
- [Foire aux questions](https://www.impots.gouv.fr/sites/default/files/media/1_metier/2_professionnel/EV/2_gestion/290_facturation_electronique/faq_tout_savoir_facturation-electronique.pdf)
- [Guide pratique](https://www.impots.gouv.fr/sites/default/files/media/1_metier/2_professionnel/EV/2_gestion/290_facturation_electronique/guide_pratique_facturation_electronique.pdf)
- [Tout savoir sur la facturation](https://entreprendre.service-public.fr/vosdroits/F23208)
- [Mentions obligatoires](https://entreprendre.service-public.fr/vosdroits/F31808)
- [Délais de conservation](https://entreprendre.service-public.fr/vosdroits/F10029)
- [VAT rates](https://bofip.impots.gouv.fr/bofip/1013-PGP.html)
- [Taux particulier](https://bofip.impots.gouv.fr/bofip/1449-PGP.html)

Selected-source read 29 October 2026: the current official DGFiP v3.2 bundle was acquired intact; only the recorded general/Chorus/annex clauses were read. Its regulatory-data schema is not a certificate for a complete B2B invoice. FNFE-MPE is cited as the technical standard maintainer, not as tax legislation. The current statutory size/date and penalty bodies were read in the exact official selected representations recorded in the figure ledger; the older strict fiche and startup doctrine are preserved with their limits. Selected receiving-fallback, qualifying reduced-rate and BT-10 title/description scopes were reread31October2026 from the retained exact sources; the Peppol semantic label does not impose its separate validation rules on France.

## Disclaimer

This Guide and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this Guide. All outputs must be reviewed and signed off by a qualified professional (such as an expert-comptable, commissaire aux comptes, or equivalent licensed practitioner in your jurisdiction) before filing or acting upon.

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
