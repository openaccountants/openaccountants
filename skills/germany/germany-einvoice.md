---
name: germany-einvoice
description: Use this skill whenever asked about German e-invoicing, XRechnung, ZUGFeRD, ERechV, E-Rechnungsverordnung, Peppol BIS Billing Germany, Leitweg-ID, OZG-RE invoice portal, B2B e-invoicing mandate Germany, Wachstumschancengesetz, EN 16931 Germany, GoBD e-invoice archiving, or any question about issuing, receiving, validating, or archiving electronic invoices in Germany. Also trigger when preparing XRechnung XML invoices, configuring Peppol endpoints for German public-sector invoicing, handling B2B e-invoice reception requirements, or advising on ZUGFeRD profile selection. This skill covers XRechnung CIUS, ZUGFeRD hybrid format, Peppol transmission, mandatory fields, validation rules, GoBD archiving, penalties, and interaction with German VAT returns. ALWAYS read this skill before touching any German e-invoicing work.
version: 1.3
jurisdiction: DE
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

# E-invoicing in Germany (E-Rechnung, XRechnung and ZUGFeRD)

When a German business must issue an e-invoice, when a paper or PDF invoice is still allowed, what every business must be able to receive, which formats count, how to correct, check and store e-invoices, and how invoicing federal authorities differs. It is for businesses, freelancers, landlords and associations in Germany, for foreign businesses that invoice German customers, and for the people who keep their books. Figures are for tax year 2026. The rules are read from the consolidated federal law pages (UStG, UStDV, AO, ERechV), from the finance ministry's letter of 15 October 2025, which writes the e-invoice rules into the VAT application decree (Umsatzsteuer-Anwendungserlass), from the ministry's questions and answers page (as of March 2026), and from the GoBD change letters of 11 March 2024 and 14 July 2025. The reduced VAT rate is printed as a digit only in the ministry's tax booklet, 2025 edition; the statute states it in words. The ministry's first e-invoice letter, of 15 October 2024, is no longer at its address on the ministry's site, so nothing in this Guide rests on it alone.

## Section 1: Quick Reference

| Field | Value | Source |
| --- | --- | --- |
| Country | Germany (Bundesrepublik Deutschland) | same |
| Currency | EUR | same |
| What an e-invoice is | An invoice that is issued, sent and received in a structured electronic format and that allows electronic processing (§ 14(1) UStG). Paper, a plain PDF, an image file or the text of an e-mail is an "other invoice" (sonstige Rechnung) | https://www.gesetze-im-internet.de/ustg_1980/__14.html |
| National CIUS | XRechnung. The ministry says it meets the European standard EN 16931 and § 14(1) sentence 6 no. 1 UStG | https://www.bundesfinanzministerium.de/Content/DE/FAQ/e-rechnung.html |
| Hybrid format | ZUGFeRD from version 2.0.1, without the profiles MINIMUM and BASIC-WL: a PDF that carries the structured XML data in the same file | same |
| Current XRechnung version | KoSIT lists the current 3.0.2 bundle. ELSTER’s viewer still describes its own version as 3.0.1; that viewer label does not set the normative version. See Section 3 and Sources | https://xeinkauf.de/xrechnung/versionen-und-bundles/ |
| Governing body | Bundesministerium der Finanzen (BMF) for the VAT rules | https://www.bundesfinanzministerium.de/Content/DE/FAQ/e-rechnung.html |
| Standards body | Koordinierungsstelle für IT-Standards (KoSIT) for XRechnung. Forum elektronische Rechnung Deutschland (FeRD) for ZUGFeRD | same |
| Key legislation | § 14, § 14b and § 27(38) UStG as changed by the Wachstumschancengesetz (Growth Opportunities Act); §§ 33, 34 and 34a UStDV; the E-Rechnungsverordnung (ERechV) for federal public contracts; GoBD (last changed 14 July 2025) | https://www.gesetze-im-internet.de/ustg_1980/__14.html |
| B2G portal | OZG-RE (Onlinezugangsgesetz-konforme Rechnungseingangsplattform). The ministry's questions and answers page names it as the ERechV route. See Section 5 | https://www.bundesfinanzministerium.de/Content/DE/FAQ/e-rechnung.html |
| B2G mandatory since | 27 November 2020 at federal level (§ 11(3) ERechV) | https://www.gesetze-im-internet.de/erechv/__11.html |
| B2B reception mandatory | Since 1 January 2025, for every business in Germany, Kleinunternehmer included. No transition period | https://www.bundesfinanzministerium.de/Content/DE/FAQ/e-rechnung.html |
| B2B issuance | A duty in law since 1 January 2025. Relief for sales made in 2025 and 2026: every issuer, until 31 December 2026. Relief for sales made in 2027: only issuers within the turnover limit in Section 2, or EDI, until 31 December 2027. From 2028 no relief | https://www.gesetze-im-internet.de/ustg_1980/__27.html |
| B2C | Not subject to the e-invoicing duty | https://www.bundesfinanzministerium.de/Content/DE/FAQ/e-rechnung.html |
| Current status | Invoicing federal authorities: in force. Receiving between businesses: in force. Issuing between businesses: in its transition | https://www.gesetze-im-internet.de/ustg_1980/__27.html |
| Guide version | Core tax clauses retain their recorded source history. The selected technical clauses and federal portal sources below were read on 29 October 2026 | same |

**Five things older material gets wrong**

- **The duty to RECEIVE has no exceptions.** A Kleinunternehmer, a landlord of flats, a doctor and an association with a business side must all be able to receive e-invoices since 1 January 2025. Kleinunternehmer are released from ISSUING only.
- **Paper needs no consent.** During the transition a paper invoice may always be sent. Only an invoice in another electronic format, for example a plain PDF by e-mail, needs the recipient's consent.
- **An e-invoice to a German business needs no consent.** The recipient cannot insist on paper or PDF.
- **A plain PDF is not an e-invoice.** A hybrid ZUGFeRD file, a PDF that carries the structured data, can be one.
- **The turnover limit is a test of the ISSUER, for sales made in 2027 only.** It is not a phase that starts a duty. The duty exists since 2025; the limit decides who may still use the relief in 2027.

## Section 2: Mandate Scope

### Who Must Comply

| Scope | Requirement |
| --- | --- |
| B2G (federal) | Suppliers must issue and send invoices to federal contracting authorities in electronic form (§ 3(1) ERechV, in force since 27 November 2020). The standard is XRechnung, or another standard that meets the European norm (§ 4(1) ERechV). Invoices go through a federal administration portal, after sign-up for a user account (§ 4(3) ERechV). Not for invoices after a direct award up to the amount in the ERechV table below |
| B2G (Länder) | The federal states have their own rules for invoices to state and local authorities. They are not on the pages read for this Guide. The legacy Guide said all of them were in force by 2024; that was not checked |
| B2B (reception) | Every business established in Germany must be able to receive e-invoices since 1 January 2025. No exceptions |
| B2B (issuance) | Duty under § 14(2) sentence 2 no. 1 UStG when supplier AND customer are both established in Germany and the supply is for the customer's business. Transition relief: see Transitional Rules below |
| B2C | Not covered. An invoice to a consumer may be on paper. In an electronic format, e-invoice included, it needs the consumer's consent (§ 14(1) sentence 5 UStG) |
| Outside the duty to ISSUE an e-invoice | Small invoices within the limit in the table below (§ 33 UStDV). Passenger tickets (§ 34 UStDV). Invoices issued by a Kleinunternehmer (§ 34a UStDV). Supplies exempt under § 4 nos. 8 to 29 UStG, for which there is no duty to invoice at all. Supplies to legal persons that are not businesses. Certain property-related services to consumers. Any supply where the supplier or the customer is not established in Germany |

**The core rule**, all from § 14(1) and (2) UStG at https://www.gesetze-im-internet.de/ustg_1980/__14.html

- **Duty to invoice.** For a supply to another business for its business, the supplier must issue an invoice "innerhalb von sechs Monaten nach Ausführung der Leistung" (within six months after the supply), unless the supply is exempt under § 4 nos. 8 to 29 UStG.
- **Duty to use an e-invoice.** That invoice must be an e-invoice when supplier and customer are both established in Germany (Inland) or in one of the areas named in § 1(3) UStG.
- **Established** means: seat, place of management, a fixed establishment that takes part in the supply, or, with no seat, the home or usual place of stay (§ 14(2) sentence 3 UStG). A foreign business that is only registered for VAT in Germany, with no fixed establishment here, may say so on its invoice to explain why it sends no e-invoice; the recipient may rely on that with a prudent merchant's care (ministry questions and answers, no. 3).
- **Business** is wide. The ministry's questions and answers page counts freelancers and people with exempt sales only, such as landlords of flats, Kleinunternehmer and doctors (no. 3).
- **Shorter deadlines stay.** § 14a UStG sets the fifteenth day of the following month for intra-Community supplies and for services under § 3a(2) UStG performed in another member state. See https://www.gesetze-im-internet.de/ustg_1980/__14a.html
- **Advance payments.** If money is received before the supply, the six months run from the receipt (decree section 14.1(3)).

**E-invoicing: turnover limit for the 2027 relief**

| What | Value | Note | Source |
| --- | --- | --- | --- |
| Source | all figures below | https://www.gesetze-im-internet.de/ustg_1980/__27.html |  |
| Total turnover (Gesamtumsatz, § 19(2) UStG) of the business that issues the invoice, in the previous calendar year: not more than | EUR 800,000 | § 27(38) no. 2 UStG: "im vorangegangenen Kalenderjahr nicht mehr als 800 000 Euro betragen hat" | https://www.gesetze-im-internet.de/ustg_1980/__27.html |

- **What the limit is.** A cliff, tested on the issuer, never on the customer. At the limit or below, the relief for 2027 sales applies. One euro above, it does not, for any 2027 sale.
- **What counts.** Total turnover under § 19(2) UStG: supplies within the scope of German VAT (steuerbare Umsätze), counted on a receipts basis, less certain exempt supplies, without sales of fixed assets. See https://www.gesetze-im-internet.de/ustg_1980/__19.html
- **Same number, other rules.** The same amount appears in § 141 AO (bookkeeping duty) and § 20 UStG (VAT on receipts). They are separate tests.

**Small invoices**

| What | Value | Note | Source |
| --- | --- | --- | --- |
| Source | all figures below | https://www.gesetze-im-internet.de/ustdv_1980/__33.html |  |
| Invoice total up to which the invoice may always be an other invoice | EUR 250 | § 33 UStDV: "Eine Rechnung, deren Gesamtbetrag 250 Euro nicht übersteigt" | https://www.gesetze-im-internet.de/ustdv_1980/__33.html |

- **What the limit is.** The total of ONE invoice, VAT included. "Not more than": an invoice of exactly the amount in the table is still a small invoice.
- **The whole invoice counts.** If one invoice covers several supplies, only its total matters. Above the limit an e-invoice is due, even if the part that falls under the e-invoice duty is below it, for example because exempt or non-taxable items are billed on the same invoice (decree section 14.6(4)).
- **Not for every supply.** § 33 sentence 3 UStDV takes invoices for supplies under §§ 3c, 6a and 13b UStG (distance sales, intra-Community supplies, reverse charge) out of the small-invoice rule.
- **Cash purchases have no special rule.** A business meal in a restaurant or materials bought in a DIY store need an e-invoice once the invoice is above the limit, unless the issuer uses the transition relief. The ministry suggests a till receipt on the spot and an e-invoice by e-mail afterwards that corrects it (questions and answers, no. 10).

**The same two limits as the ministry prints them**

| What | Value | Note | Source |
| --- | --- | --- | --- |
| Source | all figures below | https://www.bundesfinanzministerium.de/Content/DE/FAQ/e-rechnung.html |  |
| Small invoices: the limit is a gross amount | EUR 250 | Questions and answers, no. 4: "bis 250 Euro Bruttobetrag" | https://www.bundesfinanzministerium.de/Content/DE/FAQ/e-rechnung.html |
| Relief for 2027: issuer's turnover of the previous year up to | EUR 800,000 | Questions and answers, no. 11: "Bei einem Vorjahresumsatz des Rechnungsausstellers bis 800.000 Euro verlängert sich diese Frist noch bis zum Ablauf des Jahres 2027" | same |

**Kleinunternehmer (small business under § 19 UStG)**

| What | Value | Note | Source |
| --- | --- | --- | --- |
| Source | all figures below | https://www.gesetze-im-internet.de/ustg_1980/__19.html |  |
| Total turnover of the previous calendar year: must not have exceeded | EUR 25,000 | § 19(1) UStG: "im vorangegangenen Kalenderjahr 25 000 Euro nicht überschritten hat" | https://www.gesetze-im-internet.de/ustg_1980/__19.html |
| Total turnover of the current calendar year: must not exceed | EUR 100,000 | § 19(1) UStG: "im laufenden Kalenderjahr 100 000 Euro nicht überschreitet" | same |

- **Both conditions must hold** (AND). Details are in the German VAT Guide, `germany-vat-return`. Older material gives lower limits: they are out of date.
- **What a Kleinunternehmer may do.** Always issue an other invoice: paper, or with the recipient's consent another electronic format (§ 34a UStDV, decree section 14.7a(3)). Issuing an e-invoice is allowed too, and needs no consent when the customer is a German business.
- **What a Kleinunternehmer must do.** Be able to receive e-invoices (decree section 14.1(5)).
- **Leaving the scheme.** A Kleinunternehmer who moves to normal taxation must issue e-invoices from that moment, under the general conditions (questions and answers, no. 4).

**Federal public contracts (ERechV)**

| What | Value | Note | Source |
| --- | --- | --- | --- |
| Source | all figures below | https://www.gesetze-im-internet.de/erechv/__3.html |  |
| No duty to invoice electronically for an invoice issued after a direct award (Direktauftrag) up to | EUR 1,000 | § 3(3) no. 1 ERechV: "die nach Erfüllung eines Direktauftrags bis zu einem Betrag von 1 000 Euro gestellt werden" | https://www.gesetze-im-internet.de/erechv/__3.html |

- **Other ERechV exceptions:** invoice data that must be kept secret (§ 8), the foreign service and other purchases abroad (§ 9), and Organleihe cases (§ 3(3) no. 3).
- **The ERechV does not say** whether its amount is net or gross.
- **Two sets of rules, side by side.** The ministry says there is no ranking between the UStG and the ERechV: each applies in its own field, and one can in practice narrow a choice the other leaves open (questions and answers, no. 4a). An invoice to a public body falls under the VAT e-invoice rules only when the body acts as a business.

### Receiving e-invoices

All from the ministry's letter of 15 October 2025, decree section 14.1(4) and (5): https://www.bundesfinanzministerium.de/Content/DE/Downloads/BMF_Schreiben/Steuerarten/Umsatzsteuer/Umsatzsteuer-Anwendungserlass/2025-10-15-einfuehrung-obligatorische-e-rechnung.pdf?__blob=publicationFile&v=5

- **The duty.** "Inländische Unternehmer müssen die technischen Voraussetzungen zum Empfang einer E-Rechnung schaffen." This also applies to a recipient under § 19 UStG.
- **Apply the consent table.** No consent is needed for the domestic e-invoice duty, or the stated domestic business-to-business § 33/34/34a UStDV cases. Remaining voluntary cases, including consumers, the stated exempt supplies and a supplier or customer abroad, require the recipient's consent.
- **E-mail.** E-invoices may come by e-mail. The letter says: "Bei einem Empfang mittels E-Mail ist kein gesondertes E-Mail-Postfach nur für den Empfang von E-Rechnungen erforderlich." The ministry's questions and answers page goes one step further and says an e-mail inbox is already enough to receive (nos. 8 and 12).
- **Refusing does not help.** A business that cannot receive an e-invoice, or refuses it, has no right to an other invoice instead. The issuer's VAT duties then count as met if it issued an e-invoice and can show that it tried to send it properly, for example with a send log.
- **Receiving is not processing.** The recipient need not process the data electronically beyond what storage demands (questions and answers, no. 9).
- **Reading the file.** An XRechnung has no picture part; a viewer is needed. The tax administration offers one for XRechnung and ZUGFeRD files at https://www.elster.de/eportal/e-rechnung and calls it a non-binding service.
- **Associations.** An association must be able to receive e-invoices so far as it acts as a business. For supplies to its non-business side it need neither receive nor issue e-invoices (questions and answers, no. 5).

### When consent is needed

| Invoice | Consent of the recipient |
| --- | --- |
| E-invoice to a German business, where the e-invoice duty applies | Not needed |
| E-invoice to a German business for a small invoice, a ticket or a Kleinunternehmer supply | Not needed (decree section 14.1(6)) |
| Paper invoice, where paper is allowed | Not needed |
| Other electronic format, for example a plain PDF, where an other invoice is allowed | Needed (§ 14(1) sentence 5 UStG, § 27(38) UStG) |
| E-invoice where there is no e-invoice duty: consumers, exempt supplies under § 4 nos. 8 to 29 UStG, a supplier or customer abroad, a legal person that is not a business | Needed |

- **Form of consent.** None. It can be implied, for example by accepting the invoice without objection, given in general terms of business, or given afterwards (decree section 14.1(7)).

### Transitional Rules (2025-2027)

All from § 27(38) UStG: https://www.gesetze-im-internet.de/ustg_1980/__27.html

| Supply made in | What may still be sent instead of an e-invoice | Invoice sent by | Who |
| --- | --- | --- | --- |
| 2025 or 2026 | A paper invoice. Or, with the recipient's consent, an invoice in another electronic format | 31 December 2026 | Every issuer. No turnover test (no. 1) |
| 2027 | The same | 31 December 2027 | Only an issuer within the turnover limit in the table above (no. 2) |
| 2027 | With the recipient's consent, an invoice in another electronic format that is sent by EDI | 31 December 2027 | Every issuer. No turnover test (no. 3) |
| 2028 onward | Nothing. An e-invoice is due wherever § 14(2) sentence 2 no. 1 UStG demands one | Not applicable | The lasting exceptions stay: small invoices, tickets, Kleinunternehmer, exempt supplies under § 4 nos. 8 to 29 UStG, non-German parties |

- **Two dates and the default duty: selected combined-law interpretation.** Each § 27(38) relief tests both the supply date and the last transmission date. For an ordinary taxable domestic business-to-business supply made in December 2026, first invoiced in January 2027, the default § 14(2) e-invoice duty applies if both parties meet the domestic-establishment test, the recipient acquires for its business, the invoice total is above EUR 250, and no Kleinunternehmer, ticket or other permanent exemption applies. This fixture assumes no previously issued qualifying advance or standing invoice; those follow their specific rules below. No. 1 relief ended on 31 December 2026; nos. 2 and 3 concern supplies made after that date, so neither low issuer turnover nor the December supply date rescues this January invoice. This is a labelled reading of the own default and transition clauses, not a separate ruling. The same December supply first sent by 31 December 2026 can use paper or an agreed PDF under no. 1. A supply made on 1 January 2027 instead enters no. 2's own prior-year-turnover test and 2027 transmission window. The ministry applies the principles to post-2024 supplies, subject to the actual transition. Reapply these exact duty/relief gates to other late invoices rather than inferring a gap in all invoicing rules.
- **Issuing only.** § 27(38) UStG relieves issuers. There is no relief for receiving.
- **The issuer decides.** The choice to use the relief lies with the issuer. The ministry adds that the rules leave a recipient free to pick a supplier that, for now, still issues paper invoices (questions and answers, no. 11).
- **An other invoice still works while it is allowed.** As long as an other invoice may be issued, it remains a proper invoice for the input tax deduction (questions and answers, no. 2).
- **Supplies before 2025** follow the old rules, even if invoiced later (questions and answers, no. 2).
- **Payments on account.** Invoices for advance or part payments issued before the cut-off date need not be e-invoices, even if supply and payment come later (questions and answers, no. 7b).
- **Corrections during the transition** may still be made without an e-invoice (decree section 14.11(1); questions and answers, no. 7b).
- **After the transition an agreed format stays possible.** § 14(1) sentence 6 no. 2 UStG allows a structured format agreed between the parties, if the required data can be extracted correctly and completely into a format that meets the European standard or works with it. The ministry names EDI procedures such as EDIFACT as examples.

### Timeline Summary

| Date | Milestone |
| --- | --- |
| 27 November 2020 | Duty to invoice federal authorities electronically (§ 11(3) ERechV) |
| 1 January 2025 | New definition of the e-invoice. Every German business must be able to receive e-invoices. Duty to issue, with transition relief |
| 14 July 2025 | GoBD changed for e-invoice archiving, with immediate effect |
| September 2025 | The federal administration receives e-invoices through one platform, OZG-RE, after the older ZRE platform was merged into it. Source: the federal e-invoicing information site named in the ministry's questions and answers page. It is not an allowed host for this Guide and is not linked |
| 15 October 2025 | The ministry writes the e-invoice rules into the VAT application decree |
| 31 December 2026 | End of the relief for sales made in 2025 and 2026 |
| 31 December 2027 | End of the relief for small issuers and for EDI, for sales made in 2027 |
| 1 January 2028 | E-invoices between German businesses with no transition relief |
| Later, no date | A reporting system for invoice data to the tax administration is planned. The ministry says the government will propose the law "zu gegebener Zeit" (questions and answers, no. 1) |

## Section 3: Technical Format

### Accepted Formats

| Format | Type | Standard | Status |
| --- | --- | --- | --- |
| XRechnung | Pure XML (UBL or CII syntax) | National CIUS of the European standard EN 16931 | Named by the ministry: meets § 14(1) sentence 6 no. 1 UStG |
| ZUGFeRD from version 2.0.1, without the profiles MINIMUM and BASIC-WL | Hybrid: PDF plus embedded XML in one file | Based on the EN 16931 series | Named by the ministry as an allowed e-invoice format |
| Other European formats that meet EN 16931 | Structured | EN 16931 | Allowed: the ministry says use is not limited to national formats. It names none. The legacy Guide listed Peppol BIS Billing 3.0 here; that was not checked on an official page |
| Format agreed between issuer and recipient, for example EDI such as EDIFACT | Structured | May differ from EN 16931 | Allowed if the data required by the UStG can be extracted correctly and completely into a format that meets EN 16931 or is interoperable with it (§ 14(1) sentence 6 no. 2 UStG) |
| Plain PDF, image file, text of an e-mail, paper | Not structured | None | Not an e-invoice. An "other invoice" |

- **Which allowed format is used** is a civil law question between the parties (decree section 14.1(12)).
- **Syntax names.** The ministry says only that the standard prescribes XML. KoSIT's specification names the same two syntaxes, UBL and the UN/CEFACT Cross Industry Invoice (CII).
- **Hybrid files: the XML leads.** Before 2025 the picture part led. Now the structured part is the leading part, and if the two differ the structured data decide (decree section 14.4(3); questions and answers, no. 12a). Input tax can be deducted only from the structured part. A picture part with different invoice details can count as a further (other) invoice, for which § 14c UStG must be checked: that section makes a person owe tax that is shown wrongly or without the right to show it (decree section 14c.1(4a)). Small technical differences, such as a shortened description or rounding differences, are not objected to.
- **Everything the VAT law demands must be in the structured part.** All details under §§ 14 and 14a UStG belong there. A mere reference in the data to an attachment that holds them in unstructured form is not enough. A link to an outside target is not enough. Extra detail, such as a timesheet as a PDF, may sit in an attachment inside the e-invoice (decree section 14.5(1) and (15)).

### XRechnung Technical Details

The identifiers below are checked against KoSIT’s XRechnung 3.0.2 specification and the schemas in its bundle dated 31 August 2026. The UBL namespace is also in OASIS’s UBL 2.1 schema. These are technical source checks, not a validator execution; exact Sources and limits are below.

| Parameter | Value | Source |
| --- | --- | --- |
| Version | The ELSTER viewer states: "Es wird die aktuell gültige XRechnung Version 3.0.1 verwendet." See https://www.elster.de/eportal/e-rechnung . KoSIT's own version page, read on 19 September 2026 but not linked, also lists a release 3.0.2 as in force and announces a version 4.0 for 2027. The ERechV asks for the standard "in der jeweils aktuellen Fassung" (§ 4(1)); changes are announced in the Bundesanzeiger (§ 4(2)). Confirm the version in your software |  |
| UBL namespace | `urn:oasis:names:specification:ubl:schema:xsd:Invoice-2` |  |
| CII namespace | `urn:un:unece:uncefact:data:standard:CrossIndustryInvoice:100` |  |
| CustomizationID (UBL) | `urn:cen.eu:en16931:2017#compliant#urn:xeinkauf.de:kosit:xrechnung_3.0` | https://xeinkauf.de/app/uploads/2024/07/302-XRechnung-2024-06-20.pdf |
| ProfileID (BT-23) | `urn:fdc:peppol.eu:2017:poacc:billing:01:1.0` |  |
| Encoding | UTF-8 | https://xeinkauf.de/app/uploads/2024/07/302-XRechnung-2024-06-20.pdf |
| Validation | KoSIT Validator (open source, Java based) |  |
| Schema download | KoSIT's site xeinkauf.de (named in the ministry's questions and answers, no. 16; not linked here) | https://www.bundesfinanzministerium.de/Content/DE/FAQ/e-rechnung.html |

- **Extension.** Besides the core data model, XRechnung offers an extension for sector needs. The ministry says the VAT details are all in the core model, so using an extension does not touch the VAT rules (decree sections 14.1(13) and 14.5(1)).

### ZUGFeRD Profiles

FeRD publishes the profile definitions below. Its current FAQ distinguishes the EN 16931 (COMFORT) profile, the BASIC subset and the EXTENDED profile, and the XRECHNUNG reference profile. The ministry allows ZUGFeRD from version 2.0.1, excluding MINIMUM and BASIC-WL. Acceptance under federal ERechV remains a separate condition.

| Profile | Source-backed format scope | Use Case |
| --- | --- | --- |
| Minimum | No. Excluded by the ministry | Not an e-invoice for VAT |
| Basic WL | No. Excluded by the ministry | Without line detail. Not an e-invoice for VAT |
| Basic | A subset of EN 16931 for simple UStG-conforming invoices; BMF permits the profile | Standard use with the required invoice data |
| Comfort (EN 16931) | Fully represents EN 16931-1, according to FeRD | Full core invoice data |
| Extended | Extends EN 16931 with additional information; FeRD says to agree its exchange with the recipient | Additional business information |
| XRechnung | Reference profile for an XML file conforming to the current XRechnung specification; FeRD permits CII only inside this reference profile | XRechnung XML inside a ZUGFeRD container |

- **Profile selection guidance.** For invoices between businesses, any ZUGFeRD profile from version 2.0.1 other than the two excluded ones falls under the allowed formats. For invoices to federal authorities the ERechV asks for XRechnung, or another standard that meets the European norm (§ 4(1) ERechV). Which ZUGFeRD profile a given authority accepts is not on the pages read for this Guide: ask the authority.

### Format errors, business rule errors and content errors

From the ministry's letter of 15 October 2025 (decree sections 14.1(2), 14.1(11) and 14.5(1)):

| Kind of error | What it is | Result for VAT |
| --- | --- | --- |
| Format error | The file does not follow the allowed syntax or its technical rules, or an agreed format does not allow correct and complete extraction | The file is not an e-invoice. It is an other invoice in another electronic format. Where an e-invoice was due, it is not a proper invoice |
| Business rule error on VAT content | The file breaks the format's logic checks on a detail that §§ 14 or 14a UStG demand, for example the tax amount does not agree with the stated rate | A content error: not a proper invoice until corrected |
| Business rule error on other content | For example no entry in the mandatory field "BT-10 Buyer reference" of an XRechnung | Irrelevant for VAT ("umsatzsteuerlich unbeachtlich") |
| Content error that no validator finds | For example a wrong tax rate that is consistent in itself | Not a proper invoice, even though validation passes |

## Section 4: Mandatory Fields

The field codes and cardinalities below are checked against KoSIT’s XRechnung 3.0.2 specification. The scheme examples 0204 and 9930 are checked against KoSIT’s identifier guidance dated 2 January 2025. The exact Leitweg-ID validation pattern is not supplied here: use the identifier assigned by the recipient under § 5 ERechV. The ministry’s FAQ no. 16 also points to the joint KoSIT/FeRD mapping of VAT details to BT fields.

### EN 16931 Core Fields (Required by XRechnung)

| BT Code | Field | Required |
| --- | --- | --- |
| BT-1 | Invoice number | Yes |
| BT-2 | Invoice issue date | Yes |
| BT-3 | Invoice type code (380 = commercial invoice; 384 = corrected invoice, which must refer to the earlier invoice; 381 = credit note in the commercial sense; 389 = self-billed invoice, the Gutschrift of § 14(2) UStG) | Yes |
| BT-5 | Invoice currency code | Yes |
| BT-9 | Payment due date | Optional on its own. If the amount due for payment is positive, either the payment due date (BT-9) or the payment terms (BT-20) must be present (rule BR-CO-25) |
| BT-10 | Buyer reference (Leitweg-ID for B2G) | Yes. The ministry calls it a mandatory field of an XRechnung. Between businesses no Leitweg-ID is needed, and for VAT a placeholder such as "-" is enough (questions and answers, no. 6) |
| BT-23 | Business process type (ProfileID) | Yes (mandatory since XRechnung 3.0.1, per the legacy Guide) |
| BT-24 | Specification identifier (CustomizationID) | Yes |
| BT-27 | Seller name | Yes |
| BT-40 | Seller country code | Yes |
| BT-31 | Seller VAT identifier | The law asks for the tax number OR the VAT identification number (§ 14(4) no. 2 UStG), and it must be in the structured part (decree section 14.5(9)). A Kleinunternehmer may give the Kleinunternehmer identification number instead (§ 34a UStDV). KoSIT's specification has a separate field BT-32 (Seller tax registration identifier, "eine örtliche steuerrechtliche Kennung des Verkäufers"); for the mapping see the joint KoSIT and FeRD table |
| BT-34 | Seller electronic address + scheme ID | Yes (mandatory since XRechnung 3.0.1, per the legacy Guide) |
| BT-44 | Buyer name | Yes |
| BT-55 | Buyer country code | Yes |
| BT-48 | Buyer VAT identifier | § 14a(1) and (3) UStG demand both VAT identification numbers for services under § 3a(2) UStG performed in another member state and for intra-Community supplies. For a domestic reverse-charge supply § 14a(5) UStG demands the words "Steuerschuldnerschaft des Leistungsempfängers" instead |
| BT-49 | Buyer electronic address + scheme ID | Yes (mandatory since XRechnung 3.0.1, per the legacy Guide) |

### XRechnung-Specific Additional Requirements

| Field | Description | Required |
| --- | --- | --- |
| BT-10 (Leitweg-ID) | Hierarchical routing identifier for B2G (format: coarse-fine-check digit). § 5(1) no. 1 ERechV demands a Leitweg-Identifikationsnummer on every invoice to a federal authority | Yes (B2G) |
| BT-23 (ProfileID) | Mandatory. The buyer specifies the value. If the buyer gave none, the Peppol process identifier in Section 3 may be sent as the default; inside the Peppol network the value must follow the Peppol pattern | Yes |
| BT-34 / BT-49 | Electronic addresses with scheme identifier (e.g., 0204 for Leitweg-ID, 9930 for DE VAT number) | Yes |
| Payment instructions (BG-16) | At least one payment means must be specified. § 5(1) nos. 2 and 3 ERechV demand bank details and payment terms for federal invoices | Yes |
| BT-20 | Payment terms (text description) | Optional on its own. Needed if the amount due is positive and BT-9 is empty (rule BR-CO-25). § 5(1) no. 3 ERechV demands payment terms on federal invoices |
| BT-81 | Payment means type code (e.g., 58 = SEPA credit transfer) | Yes |
| Seller contact (BG-6) | The group must be sent, with contact point (BT-41), telephone number (BT-42) and e-mail address (BT-43): rules BR-DE-2, BR-DE-5, BR-DE-6, BR-DE-7 | Yes |
| City and post code | Seller city (BT-37) and post code (BT-38), buyer city (BT-52) and post code (BT-53): rules BR-DE-3, BR-DE-4, BR-DE-8, BR-DE-9 | Yes |
| Seller tax identifier | With tax codes S, Z, E, AE, K, G, L or M at least one of seller VAT identifier (BT-31), seller tax registration identifier (BT-32) or a tax representative (BG-11) must be sent: rule BR-DE-16 | Yes |

- **Also demanded by § 5 ERechV for federal invoices:** the issuer's De-Mail or e-mail address, and the supplier number and order number if they were given with the order. See https://www.gesetze-im-internet.de/erechv/__5.html

## Section 5: Transmission Method

### B2G Transmission

The ERechV demands a federal administration portal and a user account set up before the first invoice (§ 4(3) ERechV, https://www.gesetze-im-internet.de/erechv/__4.html). A formally faulty invoice is rejected automatically and the sender is told. An invoice that cannot be matched to a user account is rejected without notice (§ 4(4) ERechV). The channels below are from the legacy Guide and from the federal e-invoicing information site named in the ministry's questions and answers page (e-rechnung-bund.de, run by the procurement office of the interior ministry). Its current upload and e-mail instructions and its September 2025 consolidation statement were read on 29 October 2026 and are linked in Sources. No user account was opened or invoice submitted.

| Channel | Description |
| --- | --- |
| OZG-RE Web Portal | Entry in a web form, or upload of a finished file, in the browser |
| OZG-RE Email | Submit XRechnung XML as email attachment to designated address |
| Peppol | Machine-to-machine via Peppol Access Point using participant ID (format: 0204:{Leitweg-ID}) |

The legacy Guide said the ZRE (Zentrale Rechnungseingangsplattform) was switched off in September 2025 and that all federal submissions now go through OZG-RE. The federal e-invoicing information site says the same: since September 2025 the federal administration receives e-invoices through one central platform, OZG-RE.

### B2B Transmission

Germany does not prescribe a transmission channel for e-invoices between businesses. Which allowed channel is used is a civil law question between the parties. The ministry's letter (decree section 14.1(4)) and its questions and answers page (no. 8) name these examples:

| Channel | Description |
| --- | --- |
| Email | XRechnung or ZUGFeRD sent as email attachment. No separate inbox is needed |
| Download portal | Seller provides the structured e-invoice for download on an internet portal |
| EDI | Electronic data interchange |
| API / interface | Data made available through an electronic interface |
| Shared storage | Joint access to a central storage location, for example inside a group |
| Data carrier | Handover, for example on a USB stick |
| Peppol | Legacy row. The ministry's pages do not name Peppol for invoices between businesses. Since the law prescribes no channel, using it is a matter for the parties |

- **Sending twice is harmless.** The same e-invoice file may be sent more than once, as long as it is the same invoice and only an identical copy (decree section 14c.1(4)).

### Peppol in Germany

KoSIT’s own Peppol explanation and identifier guidance support the four points below. The identifiers address the recipient; they do not prove that a particular recipient is currently connected or that an invoice was delivered.

- KoSIT manages the German Peppol Authority
- Public authorities connected to OZG-RE are reachable via Peppol
- Peppol participant IDs for federal authorities use scheme 0204 (Leitweg-ID based)
- For B2B, scheme 9930 (DE VAT number) is commonly used

## Section 6: Validation Rules

**What the ministry says about validation** (letter of 15 October 2025, decree sections 14.1(11) and 14.5(1); questions and answers, no. 7):

- Validation is not a condition for the tax office to accept an invoice. It helps to avoid errors, and the ministry recommends it already when the e-invoice is created and sent.
- The ministry recommends no particular tool.
- A business that acts with a prudent merchant's care may rely on the technical result of a suitable validation tool as to format and business rules. Keeping the validation report as proof is advised.
- Validation does not replace the recipient's own duty to check that the invoice is complete and correct.

### KoSIT Validator

The current KoSIT bundle describes its validator as a Java tool, with configuration resources for XML schemas, EN 16931 Schematron and XRechnung CIUS/extension Schematron. The layers below describe those supplied components; no particular invoice or validator run has been tested here.

| Layer | Description |
| --- | --- |
| Schema validation | XML against the UBL or CII schema (XSD) |
| Schematron (EN 16931) | European standard business rules |
| Schematron (XRechnung) | National CIUS rules (German-specific) |
| Schematron (Extension) | Extension rules for additional national requirements |

### Common Rejection Reasons

Carried over from the legacy Guide, with the ministry's view added where it has one.

| Issue | Resolution |
| --- | --- |
| Missing BT-23 (ProfileID) | Mandatory in the checked XRechnung 3.0.2 specification. Populate the business-process identifier |
| Missing BT-34 / BT-49 (electronic addresses) | Mandatory in the checked XRechnung 3.0.2 specification. Include each with its scheme ID |
| Invalid Leitweg-ID format | Use the exact identifier assigned by the recipient (§ 5 ERechV). Not yet confirmed here: the full validation pattern. The legacy numeric-only description is not a verified constraint |
| Missing BT-10 (Buyer reference) | A mandatory field of an XRechnung. For VAT the gap is a business rule error without effect, and between businesses a placeholder is enough. A federal portal can still reject the file |
| Tax calculation inconsistency | The tax amount must agree with the stated rate. The ministry gives exactly this as its example of a business rule error, and on a VAT detail it is also a content error |
| Wrong CustomizationID | Must match the URN of the XRechnung version in use exactly |
| Mixed currency without conversion | If a VAT accounting currency code (BT-6) is given, the invoice total VAT amount in that currency (BT-111) must be given too (rule BR-53). KoSIT's specification has no field for a conversion rate |

### OZG-RE Additional Checks

- **Not yet confirmed:** whether the platform validates a Leitweg-ID against a registered directory.
- **Not yet confirmed:** whether the platform verifies that the recipient is currently connected and active.
- **Not yet confirmed:** the exact structured error-message format for rejected invoices.
- These three retained technical topics are not established by the source clauses read. The ERechV itself says only that invoices sent through the portal are checked automatically for formal correctness and that a faulty one is rejected with a notice to the sender (§ 4(3) ERechV)

## Section 7: Tax Computation Rules

### VAT Rates (2025/2026)

| What | Value | Note | Source |
| --- | --- | --- | --- |
| Source | all figures below | https://www.gesetze-im-internet.de/ustg_1980/__12.html |  |
| Standard rate (Regelsteuersatz), on every taxable supply | 19% | § 12(1) UStG: "Die Steuer beträgt für jeden steuerpflichtigen Umsatz 19 Prozent der Bemessungsgrundlage" | https://www.gesetze-im-internet.de/ustg_1980/__12.html |
| Zero rate, only for the supply and installation of solar modules and storage for certain buildings | 0% | § 12(3) UStG: "Die Steuer ermäßigt sich auf 0 Prozent für die folgenden Umsätze" | same |

| What | Value | Note | Source |
| --- | --- | --- | --- |
| Source | all figures below | https://www.bundesfinanzministerium.de/Content/DE/Downloads/Broschueren_Bestellservice/steuern-von-a-z.pdf?__blob=publicationFile&v=9 |  |
| Reduced rate (ermäßigter Steuersatz), only for the supplies listed in § 12(2) UStG and its annex | 7% | Tax booklet, 2025 edition: "den ermäßigten von 7 Prozent". The statute prints this rate in words | https://www.bundesfinanzministerium.de/Content/DE/Downloads/Broschueren_Bestellservice/steuern-von-a-z.pdf?__blob=publicationFile&v=9 |

- **Correction.** The legacy Guide listed intra-EU supplies and exports under a zero rate. In German law they are EXEMPT under § 4 UStG, not taxed at a rate of zero. In the structured data they carry their own tax category code and an exemption reason. The only zero RATE in the statute is the one in the table.
- **Which goods and services take the reduced rate** is for the German VAT Guide, `germany-vat-return`.

### Rounding

These points describe the data format. The amount datatype and line-net formula are checked against XRechnung 3.0.2 sections 8.1 and 12.5 (PEPPOL-EN16931-R120); the tax-group rule is BR-CO-17. The specification of the format in use decides, and no rounding mode is inferred.

- **Line net amount (BT-131):** quantity × (item net price / price-base quantity), plus line charges, less line allowances (PEPPOL-EN16931-R120). Amounts are expressed with two decimal places (section 8.1). Quantity × unit price alone describes only the case with a price-base quantity of one and no line charges or allowances.
- **Tax amount rounding:** the format has no tax amount per line. The tax is worked out once per VAT breakdown group (BG-23), that is per tax category and rate: the group's taxable amount (BT-116) times its rate (BT-119), divided by 100, rounded to two decimal places (rule BR-CO-17). The legacy Guide's tax amount per line was wrong
- **Category totals:** for each tax category and each rate within it, the taxable amount (BT-116) must equal the sum of the line net amounts (BT-131) with that category and rate, plus document level charges, less document level allowances with that category and rate (rule BR-S-8 for category S)
- **Validation tolerance:** the legacy Guide stated a one-cent tolerance per tax subtotal group. No allowed page prints it, so the amount was removed
- **Rounding mode:** KoSIT's specification says only "gerundet auf zwei Dezimalstellen" and names no rounding mode. The legacy Guide's line on banker's rounding is not in it and was removed
- **What the ministry says:** rounding differences between the picture part and the structured part of a hybrid invoice are not objected to (decree section 14c.1(4a)).

### Multi-Rate Invoice Handling

The following ordinary German invoice categories are checked against the named XRechnung rules and the current bundle’s code list. The list is not an exhaustive method for every foreign VAT system.

- **Separate tax subtotal group per rate:** each VAT rate requires a separate tax subtotal group (BG-23). The law demands the net amount broken down by tax rate and by exemption (§ 14(4) no. 7 UStG)
- **Tax category codes:** For ordinary German invoices, the codes are S (Standard rate), Z (Zero rated goods), E (Exempt from tax), AE (VAT Reverse Charge), K (intra-Community supply), G (export, tax not charged), O (outside scope of tax), and L and M for the Canary Islands and for Ceuta and Melilla. The current validator also recognises code B under its Italian-only conditions; that foreign method is outside this Guide. The legacy Guide's code AA for the reduced rate is not in that list. A reduced-rate line carries S with its own rate: rule BR-S-5 asks only that the rate under S be greater than zero
- **Reverse charge category code:** for reverse charge (§ 13b UStG), use category code AE with a rate of zero. The invoice must carry the words "Steuerschuldnerschaft des Leistungsempfängers", and no tax is shown (§ 14a(5) UStG). The e-invoice duty applies to reverse-charge supplies between two German businesses (decree section 14.1(4))
- **Tax exemption reason population:** the tax exemption reason (BT-120/BT-121) must be given for the categories E, AE, G and O (rules BR-E-10, BR-AE-10, BR-G-10, BR-O-10) and must NOT be given for the zero rated category Z (rule BR-Z-10). The law demands a note that an exemption applies (§ 14(4) no. 8 UStG)
- **Partly exempt invoices.** If only part of what is billed falls under the e-invoice duty, for example taxable and § 4 nos. 8 to 29 exempt items together, the whole invoice must be an e-invoice (decree section 14.1(4))

### § 14 UStG Invoice Requirements

German VAT law (§ 14(4) UStG, https://www.gesetze-im-internet.de/ustg_1980/__14.html) lists the content of an invoice. In an e-invoice all of it must be in the structured data:

1. Full name and full address of the supplier and of the customer
2. The supplier's tax number (Steuernummer) or VAT identification number (USt-IdNr.)
3. Issue date
4. A sequential invoice number, given once
5. Quantity and kind (usual trade description) of the goods, or scope and kind of the service
6. Time of the supply; for payments on account, the time of receipt if it is fixed and differs from the issue date
7. The net amount broken down by tax rate and by exemption, and any reduction agreed in advance that is not yet in the price
8. The tax rate and the tax amount, or a note that an exemption applies
9. In the cases of § 14b(1) sentence 5 UStG, a note that the recipient must keep the invoice
10. The word "Gutschrift" where the customer issues the invoice (self-billing)

- **Date of supply.** A phrase such as "Leistungsdatum entspricht Rechnungsdatum" is enough only on an other invoice. In an e-invoice the date must be in the structured field. A reference to a delivery note works only for other invoices (decree section 14.5(16)). The calendar month may be given as the time of supply, so several supplies of one month can go on one collective e-invoice (§ 31(4) UStDV; questions and answers, no. 7b).
- **Cash discount.** A note such as the agreed discount terms is enough; the discount need not be shown as an amount (decree section 14.5(19)).
- **Small invoices, tickets and Kleinunternehmer invoices** need no sequential number (decree section 14.5(14)).

## Section 8: Archiving Requirements

| Requirement | Detail |
| --- | --- |
| Retention period | 8 years for a copy of every invoice issued and for every invoice received (§ 14b(1) UStG). The period starts at the end of the calendar year in which the invoice was issued. § 147(3) AO stays untouched: under it the period does not end while the documents still matter for a tax whose assessment period is open. Start of the eight-year period: it applies to every invoice whose old retention period had not yet run out on 31 December 2024; for banks, insurers and securities institutions only to invoices whose old period had not run out on 1 January 2026 (§ 27(40) UStG, https://www.gesetze-im-internet.de/ustg_1980/__27.html) |
| Two-year duty for private recipients | A consumer, or a business buying for its private side, who receives a taxable property-related service must keep the invoice, a payment record or other proof for two years (§ 14b(1) sentence 5 UStG) |
| Format | Keep the invoice in the format in which it was received (decree section 14b.1(1); GoBD paragraph 131). For an e-invoice, at least the structured part must be kept so that it is unchanged and in its original form, and the tax office must be able to evaluate it by machine (decree section 14b.1(5)) |
| GoBD compliance | The GoBD (ministry letter of 28 November 2019, changed on 11 March 2024 and 14 July 2025) apply for income tax and bookkeeping purposes. For VAT alone, the ministry says that storing e-invoices outside a GoBD-compliant system is as a rule ("regelmäßig") no breach of § 14b(1) UStG (decree section 14b.1(1)) |
| Hybrid invoices (ZUGFeRD) | It is enough to keep the structured part. The human-readable part must be kept only if it holds extra or different information that matters for tax, for example booking notes or qualified electronic signatures (GoBD paragraphs 119 and 131). The XML must not be lost through a format change, for example to TIFF (GoBD paragraph 125) |
| Outgoing invoices | GoBD 76 permits omitting the outgoing image/PDF copy only under the preceding full-content/highest-machine-evaluability conditions and if an identical copy can be produced on request at any time. The actually processed format must carry the full content with the highest machine evaluability; otherwise keep both formats. Among the additional requirements, continuously historise master data and terms; document which terms and original format applied; retain the original layout as a template and historise changes; keep invoicing data machine-evaluable and immutable. Reproducing a current-looking image while overwriting historical customer/terms/layout data does not establish the waiver. This does not remove the separate structured-original/XML duties. |
| Content, not picture | Vouchers received as structured data need to match in content only, not in appearance (GoBD paragraph 118) |
| Immutability | Authenticity of origin, integrity of content and legibility must be secured for the whole period (§ 14b(1) sentence 2 with § 14(3) UStG). For an e-invoice, legible means machine-readable; a human-readable copy is not required (decree section 14.4(3)). A qualified electronic signature, if used, must be kept too (decree section 14b.1(6)) |
| Verfahrensdokumentation | GoBD 150–155 requires clear, current process documentation allowing a knowledgeable third party to understand and check the system within reasonable time; its extent depends on the actual business/system complexity. Describe creation, indexing, processing, storage, retrieval, machine evaluation, security and reproduction. Documentation must correspond to the programme versions actually used, with traceable dated/version history retained as long as needed to understand the records. Under paragraph 155, missing or inadequate documentation is not a substantive formal defect justifying rejection of the books where traceability and verifiability are not impaired; no automatic penalty or universal certification follows. |
| Storage location | In Germany. Electronic storage elsewhere in the EU is allowed if full online access, download and use of the data are secured; the tax office must then be told the place (§ 14b(2) and (4) UStG). Outside the EU only under § 146(2b) AO, which needs the tax office's approval on application (§ 14b(5) UStG) |
| Audit access | Three forms under § 147(6) AO: the tax office inspects the stored data and uses the system itself (Z1, direct access); it demands that the data be evaluated by machine as it specifies (Z2, indirect access); or it demands that the data be handed over in a machine-readable format (Z3, data handover, for example on a data carrier or through a data exchange platform). The legacy Guide still called Z3 a data carrier handover; the GoBD change of 11 March 2024 renamed it |
| Conversion | Under GoBD 135, the default for in-house conversion is to retain both versions, assign them to the same record/index and mark the converted one. Converted-only retention is permitted only if no image/content changes, no other retention-required information is lost, proper lossless conversion is documented, and machine evaluability/tax-authority access is unrestricted. This general exception does not permit losing mandatory original structured invoice data or the XML barred from loss by GoBD 125; keep the independent VAT structured-original rule above. Actual conversion and compliance require records, not a software-brand assumption. |
| Validation report | The ministry advises keeping it as proof (decree section 14.5(1)) |

Sources for this section: § 14b UStG at https://www.gesetze-im-internet.de/ustg_1980/__14b.html , § 147 AO at https://www.gesetze-im-internet.de/ao_1977/__147.html , and the GoBD change letter of 14 July 2025 at https://www.bundesfinanzministerium.de/Content/DE/Downloads/BMF_Schreiben/Weitere_Steuerthemen/Abgabenordnung/2025-07-14-GoBD-2-aenderung.pdf?__blob=publicationFile&v=4

## Section 9: Penalties for Non-Compliance

§ 26a UStG prints its fines in words, not digits, so they are given in words here. See https://www.gesetze-im-internet.de/ustg_1980/__26a.html

| Violation | Penalty |
| --- | --- |
| Not issuing an invoice, or not in time, against § 14(2) sentence 2 UStG, intentionally or recklessly (§ 26a(2) no. 1 UStG) | Fine of up to five thousand euros ("bis zu fünftausend Euro", § 26a(3) UStG) |
| Not keeping a copy of an issued invoice or a received invoice for at least eight years, intentionally or recklessly (§ 26a(2) no. 2 UStG) | Fine of up to five thousand euros |
| A private recipient not keeping the invoice or proof of a property-related service for at least two years, intentionally or recklessly (§ 26a(2) no. 3 UStG) | Fine of up to one thousand euros ("bis zu tausend Euro") |
| Other invoice where an e-invoice was due: input VAT deduction | The invoice is not proper under §§ 14/14a, so it gives no deduction in principle (UStAE 15.2a(1)). A later e-invoice referring specifically and clearly to it supplies the ordinary cure (15.2a(7)). Without cure, the full 15.2a(1a) strict-evidence route requires an actual invoice, although formally faulty, and objective evidence allowing easy, unambiguous verification of every material condition: actual goods/services supplied by another entrepreneur for the claimant's taxable outputs and VAT actually paid. An invoice or copy openly showing VAT is necessary to prove payment of that tax; an invoice cannot be dispensed with entirely. Establish supply timing rather than automatically assuming it equals the invoice date where there are doubts. The authority need not find missing information itself; doubts and gaps fall on the claimant. Sentences 12–14 expressly apply this to wrong-format invoices and say an otherwise correct, complete invoice regularly meets the conditions. Stipulated ordinary domestic taxable supply above the small-invoice limit: a complete PDF showing EUR 1,000 net/EUR 190 legally due VAT, actual business supply and EUR 1,190 payment, all otherwise eligible under § 15 with objective records, can support EUR 190 input despite the wrong format. A missing invoice/open VAT, unproved supply/payment or other failed material gate is not presumed to support that deduction. Contested evidence requires actual resolution; neither any-PDF credit nor all-PDF denial is the method. |
| Estimated tax assessment | The tax office estimates the tax base where books or records that must be kept cannot be presented (§ 162(2) AO) |
| GoBD non-compliance | § 158 AO makes books and records the basis of taxation if they meet §§ 140 to 148 AO, and not so far as there is reason to doubt that they are correct. Where they are not taken as the basis, the tax office estimates (§ 162(2) AO). The legacy Guide's "safety margins" and "penalty surcharges" are not on the pages read and were removed |
| Repeated/wilful violations | Tax evasion (Steuerhinterziehung) under § 370 AO for deliberate cases. Refer to a specialist |

- **Correction.** The legacy Guide gave a fine of up to thirty thousand euros for "serious" retention breaches. The statute has no such case: that ceiling belongs to § 26a(1) UStG, which is about not paying VAT prepayments and similar amounts on time. It is not an invoicing fine.
- **Not settled on the pages read:** whether sending a paper or PDF invoice where an e-invoice was due counts as "not issuing" an invoice for the fine in the first row. The statute's wording is in the table. Refer.
- **No fault of the issuer.** A breach of the e-invoice duty is not held against an issuer who did not know, and with a prudent merchant's care could not have seen, that the customer bought as a business. Use of a VAT identification number or a business identification number (W-IdNr.) can be a sign that the customer is a business (decree section 14.1(6)).

**Refusing data access**

| What | Value | Note | Source |
| --- | --- | --- | --- |
| Source | all figures below | https://www.gesetze-im-internet.de/ao_1977/__146.html |  |
| Delay payment (Verzögerungsgeld) that may be set when data access under § 147(6) AO is not granted: lowest amount | EUR 2,500 | § 146(2c) AO: "kann ein Verzögerungsgeld von 2 500 Euro bis 250 000 Euro festgesetzt werden" | https://www.gesetze-im-internet.de/ao_1977/__146.html |
| The same: highest amount | EUR 250,000 | Same sentence | same |

- **What it is.** Discretionary ("kann"). It also covers electronic books moved abroad without approval, and not moving them back on demand.

## Section 10: Interaction with Tax Skills

### VAT Return Integration

- E-invoices provide the data basis for the monthly or quarterly Umsatzsteuer-Voranmeldung (advance VAT return) via ELSTER. See the German VAT Guide, `germany-vat-return`
- The input tax deduction needs an invoice issued under §§ 14 and 14a UStG (§ 15(1) no. 1 UStG, https://www.gesetze-im-internet.de/ustg_1980/__15.html). Where an e-invoice was due, only an e-invoice meets that in principle: see Section 9
- A content error (a missing or wrong detail under § 14(4) or § 14a UStG) means the invoice is not a proper one. Unless proof under decree paragraph 15.2a(1a) can be given, it must be corrected to open the right to deduct (decree section 15.2a(7))
- The legacy Guide spoke of plans for pre-filled VAT returns. The ministry's pages say something else: a system for reporting invoice data to the tax administration, transaction by transaction, is planned for a later date, and the e-invoice prepares it (questions and answers, no. 1). No law and no date yet
- On request, e-invoices can be sent to the tax office through ELSTER, with the function "Belegnachreichung zur Steuererklärung" (questions and answers, no. 14): https://www.elster.de/eportal/formulare-leistungen/alleformulare/belegnachreichung

### Income Tax Integration

- For Einzelunternehmer (sole proprietors) and Freiberufler (freelancers), e-invoice revenue data feeds into the Einkommensteuer return (Anlage S or Anlage G)
- **Correction.** Under the EÜR (Einnahmenüberschussrechnung, cash basis, § 4(3) EStG) income counts in the calendar year in which it flows in (§ 11(1) EStG, https://www.gesetze-im-internet.de/estg/__11.html), not at the invoice date. The legacy Guide's advice to align e-invoice dates with payment dates was wrong: an invoice is dated when it is issued, and must be issued within six months of the supply
- **Correction.** Under Bilanzierung (accruals basis) income is booked whatever the payment date, and profit counts when it is realised (§ 252(1) nos. 4 and 5 HGB, https://www.gesetze-im-internet.de/hgb/__252.html). The invoice date does not decide. See the bookkeeping Guide, `germany-bookkeeping`

### Intra-EU Reporting

- An invoice to a business customer in another EU country is outside the German e-invoice duty, because the customer is not established in Germany. It may be an e-invoice if the customer agrees. The rules of § 14a UStG on content and the shorter deadline still apply
- Intra-EU supplies reported via Zusammenfassende Meldung (recapitulative statement) must reconcile with the invoices issued for them (tax category K in the structured data)
- Buyer VAT IDs on invoices (BT-48) should be checked against VIES
- Exempt supplies under § 4 nos. 1 to 7 UStG between two German businesses, for example an intra-Community supply from Germany to another German business's fixed establishment elsewhere in the EU, DO need an e-invoice (decree section 14.1(4))

### GoBD and Tax Audit

- Tax auditors may use Z1 (direct access), Z2 (machine evaluation by the taxpayer as the office specifies) or Z3 (data handover) for archived e-invoices: see Section 8
- Verfahrensdokumentation follows the actual GoBD 150–155 process/version-history method and paragraph 155 qualification in Section 8. The documentation and archive/implementation records must describe the actual workflow; no universal software certification is asserted.
- If the archive cannot be produced in an audit, the tax office can estimate (§ 162 AO, https://www.gesetze-im-internet.de/ao_1977/__162.html), and a delay payment can be set when data access is not granted: see Section 9

## Section 11: Cases the ministry has settled

All from the letter of 15 October 2025 (decree sections in brackets) at https://www.bundesfinanzministerium.de/Content/DE/Downloads/BMF_Schreiben/Steuerarten/Umsatzsteuer/Umsatzsteuer-Anwendungserlass/2025-10-15-einfuehrung-obligatorische-e-rechnung.pdf?__blob=publicationFile&v=5 or from the questions and answers page at https://www.bundesfinanzministerium.de/Content/DE/FAQ/e-rechnung.html

- **Self-billing (Gutschrift).** The e-invoice rules apply in the same way when the customer issues the invoice. If a self-billing document and an ordinary invoice cannot be combined in one e-invoice for technical reasons, separate e-invoices are issued (14.3(1) and (2)).
- **Special schemes.** The duty also covers supplies under the special rules of §§ 23a to 25c UStG (for example travel services and the margin scheme) and reverse-charge supplies under § 13b UStG between German businesses (14.1(4)).
- **Opted supplies.** A supply that is taxable only because of an option under § 9(1) UStG needs an e-invoice (14.1(4)).
- **Rent and other continuing contracts.** One e-invoice for the first part period is enough, if the contract is attached to it or the e-invoice otherwise makes clear that it is a standing invoice. When an invoice detail changes, for example a rent increase, a new e-invoice is due. A standing invoice that was properly issued as an other invoice needs no extra e-invoice as long as its details do not change (14.1(19), 14.5(17)). The invoice number may be a number from the contract, such as a flat or tenant number (14.5(12)).
- **Contracts as invoices.** A contract with all invoice details is an other invoice unless it meets the format rules. Where an e-invoice is due, an e-invoice must be issued in addition; the contract can sit in its attachment (14.1(17)).
- **Bank statements** that bill the bank's own service are invoices. They are e-invoices only if they meet the format and content rules (14.1(16)).
- **Inside one business.** Documents for movements between departments of the same business, or inside a VAT group (Organkreis), are internal vouchers, not invoices (14.1(1)). The e-invoice duty does not reach them.
- **Customer with a business and a private side.** For a legal person that buys for both sides, the e-invoice duty takes priority (14.1(8)). Where several persons buy jointly and businesses are among them, the invoice to that community must be an e-invoice once no transition relief applies (15.2a(3)).
- **Corrections.** Where an e-invoice was due, the correction must also be an e-invoice, using the invoice type for corrections. Sending the missing or wrong detail in another form is not enough (14.11(1)). Single line items may be corrected in a later e-invoice if it refers specifically and clearly to the first one (questions and answers, no. 7b).
- **Price changes are not corrections.** Cash discounts, rebates and bonuses paid later, and price cuts after a complaint that leave the supply itself unchanged, change the tax base under § 17 UStG; the invoice need not be corrected. A change in what was supplied, such as changed quantities on a building invoice, does need a correction, at least of the description (14.11(4), 17.1(3a)).
- **Building work.** For now it is enough if the structured part lists the single trades with their sums, and a human-readable attachment, clearly referred to in the structured part, gives the detailed breakdown (questions and answers, no. 7b).
- **Final invoices.** Part payments already received may be deducted in an unstructured attachment, if the structured part points to it expressly. The ministry says this can also be used after 31 December 2027 (questions and answers, no. 7b).
- **Fee notices of public bodies** that count as invoices follow the general rules, e-invoice duty included; one issued as an other invoice can be corrected by an e-invoice later (14.1(1)).

## The method, step by step

1. Check whether an invoice is due at all. § 14(2) sentence 2 UStG demands one, within six months, for supplies to another business for its business, to a legal person that is not a business, and for taxable property-related work for anyone else. No duty for supplies exempt under § 4 nos. 8 to 29 UStG. https://www.gesetze-im-internet.de/ustg_1980/__14.html
2. Check whether it must be an e-invoice. Yes, if supplier and customer are both established in Germany and the customer buys for its business (§ 14(2) sentence 2 no. 1 UStG). No, if one of them is established abroad, or the customer is a consumer or a legal person that is not a business. Same page as step 1.
3. Check the lasting exceptions: small invoices (§ 33 UStDV), passenger tickets (§ 34 UStDV), invoices of a Kleinunternehmer (§ 34a UStDV). These may always be other invoices. https://www.gesetze-im-internet.de/ustdv_1980/__33.html and https://www.gesetze-im-internet.de/ustdv_1980/__34.html and https://www.gesetze-im-internet.de/ustdv_1980/__34a.html
4. Check the transition relief in § 27(38) UStG: the year of the supply, the day the invoice is sent and, for 2027 sales, the issuer's total turnover of the previous calendar year. If the relief applies and the issuer wants to use it: paper, or with the recipient's consent another electronic format. https://www.gesetze-im-internet.de/ustg_1980/__27.html
5. If an e-invoice is due or wanted, pick an allowed format: XRechnung, ZUGFeRD from version 2.0.1 without MINIMUM and BASIC-WL, another format that meets the European standard, or an agreed format that allows full extraction. Put every detail of § 14(4) and § 14a UStG into the structured part. Ministry letter of 15 October 2025: https://www.bundesfinanzministerium.de/Content/DE/Downloads/BMF_Schreiben/Steuerarten/Umsatzsteuer/Umsatzsteuer-Anwendungserlass/2025-10-15-einfuehrung-obligatorische-e-rechnung.pdf?__blob=publicationFile&v=5
6. Validate the file, keep the validation report, and send it by a channel agreed with the customer. Apply the consent table before transmission: no consent for the domestic duty or its stated domestic § 33/34/34a cases; obtain consent for the remaining voluntary cases. Keep proof of sending. Same letter as step 5.
7. On the receiving side: make sure e-invoices can be received, display the XML with a viewer (the tax administration offers one at https://www.elster.de/eportal/e-rechnung ), and check the invoice details before deducting input tax under § 15 UStG. https://www.gesetze-im-internet.de/ustg_1980/__15.html
8. Correct a faulty invoice under § 31(5) UStDV with a document that refers specifically and clearly to it. Where an e-invoice was due, the correction is an e-invoice too. https://www.gesetze-im-internet.de/ustdv_1980/__31.html
9. Store the structured part unchanged, in the format received, for the period in § 14b(1) UStG, and keep it machine-readable for the tax office. https://www.gesetze-im-internet.de/ustg_1980/__14b.html
10. For a federal authority, follow the ERechV as well: XRechnung or an equal standard, Leitweg-ID, sign-up at the federal portal. https://www.gesetze-im-internet.de/erechv/__4.html

## Ask the client first

- Are you and your customer both established in Germany (seat, management, or a fixed establishment that takes part in the supply), and does the customer buy for its business?
- When was the supply made, and when will the invoice be sent? The relief depends on both dates.
- What was your total turnover (§ 19(2) UStG) in the previous calendar year, and are you a Kleinunternehmer?
- What is the gross total of the invoice, and is any part of the supply exempt under § 4 nos. 8 to 29 UStG?
- What does your software produce and read today: XRechnung, ZUGFeRD (which version and profile), EDI, or plain PDF? Can you receive, display and store an XML file?
- Is the customer a public authority? If so, federal or state, and do you have its Leitweg-ID?

## When to refuse or refer

- Invoices to state and local authorities: each federal state has its own rules, which this Guide does not cover.
- Technical set-up: field mapping, validator messages, Peppol access, portal sign-up. Refer to the software vendor and to the KoSIT and FeRD material.
- Whether a customer or supplier is "established" in Germany through a fixed establishment that takes part in the supply. Refer to a Steuerberater.
- Whether a supply is exempt under § 4 nos. 8 to 29 UStG, or taxable by option.
- A dispute over input tax where a paper or PDF invoice arrived although an e-invoice was due.
- Fine proceedings and anything that may be tax evasion.
- Disputes between the parties over format or channel: the ministry treats these as civil law.
- Self-billing and the 2027 turnover test, VAT groups, and any case where it is unclear whose turnover counts.
- For an ordinary December 2026 supply first invoiced in January 2027, apply the selected default-duty method in Section 2, not a blanket referral. For other late 2025/2026 invoices, test the actual § 14 duty and § 27(38) supply/transmission dates; refer only unresolved establishment, exemption, prior advance/standing-invoice or other facts outside the stated ordinary fixture.
- E-invoicing duties of other countries, and invoices under § 14(7) UStG that follow another member state's rules.
- GoBD procedural documentation and the choice of an archive system.
- The planned reporting system: there is no law yet.

## Sources

- UStG § 12, § 14, § 14a, § 14b, § 15, § 19, § 26a, § 27: https://www.gesetze-im-internet.de/ustg_1980/__12.html and https://www.gesetze-im-internet.de/ustg_1980/__14.html and https://www.gesetze-im-internet.de/ustg_1980/__14a.html and https://www.gesetze-im-internet.de/ustg_1980/__14b.html and https://www.gesetze-im-internet.de/ustg_1980/__15.html and https://www.gesetze-im-internet.de/ustg_1980/__19.html and https://www.gesetze-im-internet.de/ustg_1980/__26a.html and https://www.gesetze-im-internet.de/ustg_1980/__27.html (read 2026-10-31)
- UStDV § 31, § 33, § 34, § 34a: https://www.gesetze-im-internet.de/ustdv_1980/__31.html and https://www.gesetze-im-internet.de/ustdv_1980/__33.html and https://www.gesetze-im-internet.de/ustdv_1980/__34.html and https://www.gesetze-im-internet.de/ustdv_1980/__34a.html (read 2026-10-31)
- AO § 146, § 147, § 158, § 162, § 370: https://www.gesetze-im-internet.de/ao_1977/__146.html and https://www.gesetze-im-internet.de/ao_1977/__147.html and https://www.gesetze-im-internet.de/ao_1977/__158.html and https://www.gesetze-im-internet.de/ao_1977/__162.html and https://www.gesetze-im-internet.de/ao_1977/__370.html (read 2026-10-31)
- HGB § 252, EStG § 4 and § 11: https://www.gesetze-im-internet.de/hgb/__252.html and https://www.gesetze-im-internet.de/estg/__4.html and https://www.gesetze-im-internet.de/estg/__11.html (read 2026-10-31)
- ERechV § 3, § 4, § 5, § 11: https://www.gesetze-im-internet.de/erechv/__3.html and https://www.gesetze-im-internet.de/erechv/__4.html and https://www.gesetze-im-internet.de/erechv/__5.html and https://www.gesetze-im-internet.de/erechv/__11.html (read 2026-10-31)
- Finance ministry, e-invoice letter of 15 October 2025 (changes the VAT application decree, sections 14.1 and following): https://www.bundesfinanzministerium.de/Content/DE/Downloads/BMF_Schreiben/Steuerarten/Umsatzsteuer/Umsatzsteuer-Anwendungserlass/2025-10-15-einfuehrung-obligatorische-e-rechnung.pdf?__blob=publicationFile&v=5
- Finance ministry, questions and answers on the mandatory e-invoice, as of March 2026: https://www.bundesfinanzministerium.de/Content/DE/FAQ/e-rechnung.html (read 2026-10-31)
- Finance ministry, GoBD change letters of 11 March 2024 and 14 July 2025: https://www.bundesfinanzministerium.de/Content/DE/Downloads/BMF_Schreiben/Weitere_Steuerthemen/Abgabenordnung/AO-Anwendungserlass/2024-03-11-aenderung-gobd.pdf?__blob=publicationFile&v=4 and https://www.bundesfinanzministerium.de/Content/DE/Downloads/BMF_Schreiben/Weitere_Steuerthemen/Abgabenordnung/2025-07-14-GoBD-2-aenderung.pdf?__blob=publicationFile&v=4
- Finance ministry, tax booklet (Steuern von A-Z), 2025 edition: https://www.bundesfinanzministerium.de/Content/DE/Downloads/Broschueren_Bestellservice/steuern-von-a-z.pdf?__blob=publicationFile&v=9 (read 2026-10-31)
- ELSTER, e-invoice viewer of the tax administration, and the document upload function: https://www.elster.de/eportal/e-rechnung and https://www.elster.de/eportal/formulare-leistungen/alleformulare/belegnachreichung (viewer page read 2026-10-31; upload page holds only a form shell when tried on 2026-10-31, not read)
- Technical sources read on 29 October 2026: [KoSIT XRechnung 3.0.2 specification](https://xeinkauf.de/app/uploads/2024/07/302-XRechnung-2024-06-20.pdf), selected fields, amount datatype and PEPPOL-EN16931-R120; [current version list and bundle](https://xeinkauf.de/xrechnung/versionen-und-bundles/), whose selected schema and configuration members establish namespaces and validation layers. No full bundle execution is claimed.
- [KoSIT identifier guidance, 2 January 2025](https://xeinkauf.de/app/uploads/2025/01/2025-01-02_Germany_Identifier_v.1.1_eng.pdf), selected 0204/9930 addressing clauses; [FeRD profile FAQ](https://www.ferd-net.de/standards/zugferd-faq), selected profile definitions. These are technical publisher statements, separate from the VAT law. (read 2026-10-31)
- Federal procurement office: [current platform and consolidation explanation](https://e-rechnung-bund.de/), [upload instructions](https://e-rechnung-bund.de/ubertragungskanale/upload/) and [e-mail instructions](https://e-rechnung-bund.de/ubertragungskanale/e-mail/), selected operational clauses read on 29 October 2026. No registration, login or submission was used. (read 2026-10-31)
- [Official BMF 2026 AO annex, GoBD 76/135/150–155/185](https://usth.bundesfinanzministerium.de/ao/2026/Anhaenge/BMF-Schreiben-und-gleichlautende-Laendererlasse/Anhang-33/inhalt.html): selected operative conditions/effect actually read on 29 October 2026. This completes the stated outgoing-copy, conversion and documentation scopes; no full archive-system audit is claimed. (read 2026-10-31)
- Selected legal clauses actually read on 29 October 2026: UStG §§ 14(1)/(2),27(38),26a(2)/(3); ERechV 4(3); BMF 15 October 2025 consent/input/effect clauses. The complete strict input-evidence conditions were actually read in the [retained full UStAE, section 15.2a(1a)](https://www.bundesfinanzministerium.de/Content/DE/Downloads/BMF_Schreiben/Steuerarten/Umsatzsteuer/Umsatzsteuer-Anwendungserlass/Umsatzsteuer-Anwendungserlass-31-12-2025.pdf?__blob=publicationFile&v=2), not inferred from the amending letter alone. (read 2026-10-31)
- Not yet confirmed: the exact Leitweg-ID validation pattern and the three additional portal checks identified in Section 6; and whether wrong-format invoicing attracts the non-issue fine. These limits are not resolved by technical schema conformity.

## Disclaimer

This Guide and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this Guide. All outputs must be reviewed and signed off by a qualified professional (such as a Steuerberater or Wirtschaftsprüfer) before filing or acting upon.

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
