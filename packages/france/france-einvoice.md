---
name: france-einvoice
description: Use this skill whenever asked about French e-invoicing, facturation électronique, Chorus Pro, Factur-X, Plateforme Agréée (PA), Plateforme de Dématérialisation Partenaire (PDP), Portail Public de Facturation (PPF), e-reporting France, B2B e-invoicing mandate France 2026, lifecycle statuses, or any question about issuing, receiving, validating, or archiving electronic invoices in France. Also trigger when preparing invoices for submission via a certified platform, configuring PA/PDP connectivity, handling e-reporting obligations for B2C or cross-border transactions, or advising on Factur-X profile selection. This skill covers accepted formats (Factur-X, UBL 2.1, CII), the PPF/PA architecture, mandatory fields, validation rules, archiving, penalties, and interaction with French VAT returns. ALWAYS read this skill before touching any French e-invoicing work.
version: 1.0
jurisdiction: FR
tax_year: 2026
last_updated: 2026-09-23
review_status: pending_review
drafted_by: OpenAccountants
approved_by: pending
depends_on:
  - einvoice-workflow-base
category: invoicing
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# French e-invoicing (facturation électronique) and e-reporting

France's business-to-business e-invoicing reform is in force. The tax administration's hub page, modified on 1 September 2026, calls it "effective depuis le 1er septembre 2026". Its dates page, modified on 16 January 2026, sets the second stage at 1 September 2027. Neither page marks either date provisional, conditional or awaiting a further law. No allowed official page describes the timetables published before these, so treat any earlier date as superseded by the two dates in this Guide. Figures are for tax year 2026. The size definitions come from the administration's fiche 3, updated June 2026; the e-reporting frequency table was updated August 2026; the retention table was last checked by the business portal on 1 July 2024.

## Section 1: Quick Reference

| Field | Value |
| --- | --- |
| Status | In force since 1 September 2026 |
| How invoices move | Only through a plateforme agréée, or a compatible solution connected to one |
| B2G platform | Chorus Pro |
| Authority | DGFiP |
| Legislation | CGI art. 289 bis; penalties under CGI art. 1737 IV bis and CGI art. 1788 D |
| Receive electronically | All businesses, from 1 September 2026 |
| Issue electronically | Large enterprises and ETI from 1 September 2026; PME and micro from 1 September 2027 |

There is no free State platform and no single public portal that invoices pass through. Every business in scope chooses its own plateforme agréée. The administration's own FAQ says the market carries free or low cost offers for the simplest needs, so no free State platform does not mean no free option.

### Who Must Comply

Dates: [À partir de quand suis-je concerné](https://www.impots.gouv.fr/professionnel/questions/partir-de-quand-suis-je-concerne-par-la-reforme-de-la-facturation). Scope: [Je découvre](https://www.impots.gouv.fr/professionnel/je-decouvre-la-facturation-electronique).

| Scope | Requirement |
| --- | --- |
| Receive, all sizes | By 1 September 2026 every business must have chosen an approved platform for receiving. From that date it receives electronically whenever its supplier is obliged to issue that way |
| Issue, stage 1 | From 1 September 2026: large enterprises and entreprises de taille intermédiaire, with transaction and payment data |
| Issue, stage 2 | From 1 September 2027: petites et moyennes entreprises and micro-entreprises |
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

The fiche prints these classes as footnotes, with strict inequalities, so a business sitting exactly on 10, 250 or 5,000 employees falls in no class on its face, and the fiche does not say whether the measures are taken at entity or at group level. For the definition itself the dates page points to article 51 de la loi du 4 août 2008 de modernisation de l'économie (LME), which is on legifrance and cannot be read here. A borderline client must be classified on that statute, not on this footnote.

Having to receive does not mean having to issue: the fiche says a small or micro-enterprise invoicing a large customer already inside the reform need not issue electronically before 1 September 2027, and that the supplier, not the customer, must know which duty binds the supplier. Early entry is allowed.

### E-Reporting Obligation

Transaction e-reporting covers sales to persons who are not taxable (private individuals, non-profit bodies) and transactions with businesses established abroad, VAT-registered here or not: exports, intra-EU acquisitions and supplies. Payment e-reporting covers operations where VAT falls due on receipt, typically services, unless the business opted for the debits or the operation is reverse-charged. The data are daily totals split by rate for non-taxable customers, invoice data with the SIREN replaced by an intra-EU VAT number for a foreign customer, and the date and amount received for payments.

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
| Mixed (hybrid) format | A structured data file plus an image file. The market calls this Factur-X; the government pages do not use that name |
| Not an electronic invoice | A PDF sent by e-mail |

The specifications page names the standards: formats and lifecycle statuses (XP Z12-012), interfaces (XP Z12-013), use cases (XP Z12-014). AFNOR publishes them for free download.

| What | Value | Note |
| --- | --- | --- |
| Source | all figures below | https://www.impots.gouv.fr/specifications-externes-b2b |
| Format versions quoted by vendors | UBL 2.1, and CII D16B | No government page prints a format version. The versions this page prints are its own dossier's, the current one dated 30/04/2026 and the earlier ones listed under "Versions précédentes", among them "Version 2.1 du 29/07/2022". Agree the version with your platform |

### Factur-X Profiles

This ladder comes from the hybrid-format specification of the Forum National de la Facture Électronique. No allowed official page names these profiles: vendor reference, not law.

| Profile | Use case |
| --- | --- |
| Minimum | Invoice reference and totals only |
| Basic WL | No line detail |
| Basic | With line items |
| Comfort | Full European-standard compliance |
| Extended | Data beyond the European standard |

The official requirement is simpler: a structured invoice with the mandatory mentions, through an approved platform.

### Key Technical Parameters

From the format specifications, not an official French page, so unverified here.

| Parameter | Value |
| --- | --- |
| Hybrid container | PDF/A-3 with an embedded structured file |
| Embedded file name | `factur-x.xml` |
| Encoding | UTF-8 |
| French profile | A national CIUS of the European standard EN 16931 |
| Lifecycle statuses | Defined by XP Z12-012 |

### Core Invoice Fields (EN 16931 Business Terms)

From the European standard EN 16931, which CEN sells. No allowed official page prints these codes: a mapping aid only.

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

No Chorus Pro address is given: it is outside the hosts this Guide may link. The deposit channels below are the legacy content of this Guide. They are documented by the operator of Chorus Pro on its own portal, which is not an allowed host here, so treat them as unverified and confirm them with the platform.

| Channel | Legacy note, unverified here |
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
| Collected | Used for payment e-reporting: the receipt completes the invoice as a status |

If the parties keep an invoice the buyer refused, they must justify it: lifecycle data, pre-filled VAT figures and the return filed have to reconcile.

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
| 10% | Intermediate rate: television subscriptions, improvement work on older dwellings, restaurant meals | "soumet au taux de 10 % de la TVA les abonnements" |
| 5.5% | Reduced rate: most food, books, energy-efficiency work on dwellings | "relevant du taux réduit de 5,5 % de la TVA" |

| Rate | Application | Note |
| --- | --- | --- |
| Source | all figures below | https://bofip.impots.gouv.fr/bofip/1449-PGP.html |
| 2.1% | Special rate: reimbursable medicines, some press, blood products | "Produits imposables au taux particulier de 2,10 %" |

Exempt supplies carry no rate, only the legal mention.

### Rounding

No allowed official page states a rounding method or tolerance for electronic invoices. What the pages require is consistency: the invoice, the data extracted from it and the VAT return must reconcile. Treat no tolerance as authorised.

### Multi-Rate Invoice Handling

Each VAT rate needs its own tax subtotal, and the invoice must distinguish taxable, exempt and reverse-charged amounts. A reverse-charged line carries no VAT and must carry "Auto-liquidation". Day totals for e-reporting are split by rate too.

### Discount and Charge Handling

A document-level discount or charge changes the taxable base; a line-level discount changes the line's net amount. Each must state its VAT category, or the subtotals will not reconcile. Where there is no early-payment discount the business portal expects "Escompte pour paiement anticipé : néant".

## Section 8: Archiving Requirements

The approved platform keeps the invoice, but the legal duty stays with the business. Periods: [Délais de conservation](https://entreprendre.service-public.fr/vosdroits/F10029).

| Requirement | Detail |
| --- | --- |
| Accounting records and vouchers | Books, ledgers and supporting documents, customer and supplier invoices included: 10 years from the close of the financial year |
| Tax documents | Records open to the administration's rights of communication, enquiry and audit: 6 years |
| When the tax period runs from | The last operation recorded, or the date the document was drawn up |
| Commercial correspondence | 5 years, paper or electronic |
| Through what | The business portal says the electronic invoice is issued, transmitted, received and kept through an approved platform, or a compatible solution connected to one. No allowed official page says what the business itself must keep of the structured file and the readable image, so settle that with the platform |

## Section 9: Penalties for Non-Compliance

No allowed official page prints the amount of an e-invoicing penalty or any cap, so none is stated here. The [guide pratique de démarrage](https://www.impots.gouv.fr/sites/default/files/media/1_metier/2_professionnel/EV/2_gestion/290_facturation_electronique/guide_pratique_facturation_electronique.pdf) says this much.

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

An invoice to a business established abroad is outside e-invoicing and may still be paper or PDF. It is inside transaction e-reporting, as are exports and intra-EU acquisitions and supplies, with the SIREN replaced by an intra-EU VAT number.

## The method, step by step

1. Fix the two dates. Measure the client against the fiche 3 size table above, then apply [À partir de quand suis-je concerné](https://www.impots.gouv.fr/professionnel/questions/partir-de-quand-suis-je-concerne-par-la-reforme-de-la-facturation): everyone receives since 1 September 2026; a grande entreprise or ETI issues since then, a PME or micro-enterprise from 1 September 2027.
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
- Which platform has the client chosen? Without one in the annuaire the client cannot receive an invoice at all.

## When to refuse or refer

- Any question about the amount of a penalty. No allowed official page prints the figures; CGI art. 1737 and CGI art. 1788 D must be read in the statute.
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
