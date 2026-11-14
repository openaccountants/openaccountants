---
name: mt-reverse-charge-acquisition-intra
description: "How a person established in Malta accounts for VAT by reverse charge (self-charge) on intra-Community acquisitions of goods from another EU Member State, tax year 2026, when Article 12 registration is triggered by the EUR 10,000 acquisitions threshold, the rate, chargeability and payment dates, and how an Article 10 registered person declares the same acquisition. Services received from abroad are in mt-reverse-charge-vat-services-received-from."
license: "AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)"
metadata:
  source: openaccountants
  openaccountants_url: "https://www.openaccountants.com/skills/mt-reverse-charge-acquisition-intra"
  jurisdiction: "MT"
  tax_year: "2026"
  last_updated: "2026-11-14"
---

# Reverse charge on intra-EU acquisitions of goods in Malta

## Scope and who this is for

This Guide is for a taxable person established in Malta, including a self-employed individual, who acquires goods from a supplier in another EU Member State. In the Act an intra-Community acquisition is of goods only ([VAT Act, Second Schedule item 18(1)](https://legislation.mt/eli/cap/406/eng/pdf)). Figures cover calendar 2026.

First establish a taxable intra-Community acquisition in Malta. The supplier's EU address or an invoice without VAT is not enough ([VAT Act, arts 12, 20-21 and Third/Fourth Schedules](https://legislation.mt/eli/cap/406/eng/pdf)).

**Services are out of scope here.** A service received from a supplier not established in Malta, for which the Malta recipient is liable under article 20(2), has no monetary threshold and its own payment date; it is in `mt-reverse-charge-vat-services-received-from`.

It is not for private individuals who are not taxable persons. A person already registered under Article 10 does not need an Article 12 registration: it accounts for the same acquisition on its periodic return, as output tax, with input tax where deductible. The return itself is in `malta-vat-return`.

A point that decides the registration route: a person registered under Article 12 has no mechanism to recover the VAT it self-charges, so where the person would have a right to recover that input VAT, it should consider registration under Article 10 instead.

## Ask the client first

- Is the client already registered under Article 10, Article 11 or Article 12?
- Is it really an acquisition of goods moved from another Member State to Malta (not a service, not an import from outside the EU)?
- What is the cumulative value of intra-Community acquisitions of goods so far in this calendar year and in the previous calendar year, and does the current purchase push it over the threshold?
- Would the VAT that has to be self-charged be recoverable as input VAT if the client were registered under Article 10?
- Is the supplier established and VAT-registered in another EU Member State?
- Does the item fall under a reduced rate or an exemption rather than the standard rate, or is it a new means of transport or excise goods?

## The method, step by step

1. Establish whether the client is already registered under Article 10. If so, no Article 12 registration is needed: account for the acquisition on the periodic return, as output tax, with input tax where deductible (see `malta-vat-return`).
2. If the client is not registered under Article 10, test the acquisition against the Acquisitions Threshold in the rates table: the value of intra-Community acquisitions, measured at the Seventh Schedule taxable value, in the calendar year (Third Schedule, items 3 and 4).
3. Before registering under Article 12, check whether the client would have a right to recover the input VAT being self-charged; if so consider Article 10 instead.
4. Apply for the registration through MTCA online services (a Maltese e-ID is generally required). Article 12(1) requires the application by the date of the acquisition that crosses the threshold.
5. Determine the Maltese rate to self-charge on the acquisition. Unless a reduced rate or exemption specifically applies, the standard rate applies.
6. Work out chargeability: under Fourth Schedule item 6, acquisition VAT becomes chargeable on the earlier of the date the supplier issues the tax invoice and the 15th day of the month following the acquisition.
7. Declare and pay. An Article 12 person pays by the 15th of the month following chargeability (arts 20(1)(b) and 21(2)) and furnishes the notice of payment (arts 21(5) and 30A). Do not use the Article 10 seven-day electronic window for an Article 12 payment. Dates that fall on a Saturday, Sunday, national day or public holiday move under art. 73(5).
8. If the client also makes intra-Community supplies to VAT-registered customers in other Member States, file the recapitulative statement (rates table).

## Rates, bands and thresholds

| Item | Figure and conditions | Tax year | Source |
|---|---|---|---|
| Acquisitions Threshold, VAT Act Third Schedule item 3 | EUR 10,000 of intra-Community acquisitions of goods in a calendar year (Seventh Schedule value, item 4); above it, a person not registered under Article 10 registers under Article 12 and self-charges | Calendar 2026 | https://legislation.mt/eli/cap/406/eng/pdf |
| Standard rate, art. 19(1) | 18% of the taxable value | Current | same |
| Reduced rates, art. 19(2) | not higher than 18% or lower than 5%; MTCA lists 12%, 7% and 5%, and 0% as exemption with credit | Current | https://mtca.gov.mt/business-tax/vat1/vat-compliance/vat-rates/vat-rates |
| Chargeability of an acquisition, Fourth Schedule item 6 | earlier of the supplier's tax invoice date and the 15th day of the month after the acquisition | Current | https://legislation.mt/eli/cap/406/eng/pdf |
| Article 12 payment for goods, arts 20(1)(b) and 21(2) | by the 15th day of the month following chargeability | Current | same |
| Article 10 electronic filing window, arts 21(4A) and 42(1)(d) | no late-filing penalty and no interest if filed and paid electronically within 7 days after the due date | Current | same |
| Recapitulative statement, S.L. 406.14 reg. 3 | by the 15th day of the month after the period; quarterly only where intra-Community supplies of goods do not exceed EUR 50,000 in the quarter or any of the previous four quarters | Current | https://legislation.mt/eli/sl/406.14/eng/pdf |

## Worked cases

**Case 1: an Article 11 shop crosses the threshold.** An Article 11 shop has EUR 9,000 of relevant acquisitions before a EUR 2,000 taxable acquisition of standard-rated goods on 20 March 2026. The qualifying acquisition crosses EUR 10,000; the Article 12 application is due by that acquisition date. The tax invoice is issued the same day: chargeability is 20 March and payment is due 15 April 2026. VAT is charged on the whole qualifying acquisition, not just the EUR 1,000 excess ([Act, arts 12(1), 19(3), 20(1)(b), 21(2); Fourth Schedule item 6](https://legislation.mt/eli/cap/406/eng/pdf)). Supplier exemption and special-goods exclusions have been tested before this example.

```oa-check
name: Taxable goods acquisition crossing Article 12 threshold
inputs:
  earlier_acquisitions: 9000
  current_acquisition: 2000
  threshold: 10000
  rate: 0.18
steps:
  - cumulative_acquisitions: earlier_acquisitions + current_acquisition
  - excess_over_threshold: cumulative_acquisitions - threshold
  - vat_on_current_acquisition: current_acquisition * rate
expected:
  cumulative_acquisitions: 11000
  excess_over_threshold: 1000
  vat_on_current_acquisition: 360
```

**Case 2 (a decision): Article 12 or Article 10 for a buyer who could recover the VAT.** A trading business expects EUR 40,000 of standard-rated acquisitions in 2026, all used for taxable supplies. Under Article 12 it self-charges EUR 7,200 and recovers nothing. Under Article 10 it declares EUR 7,200 output tax and deducts EUR 7,200 input tax, net nil, but takes on periodic returns and charges VAT on its own sales. Where the sales are taxable and the input is recoverable, Article 10 saves EUR 7,200 a year; where the business makes only exempt supplies, the input is not deductible and the two routes cost the same.

```oa-check
name: Article 12 or Article 10 for recoverable acquisitions
inputs:
  acquisitions: 40000
  rate: 0.18
steps:
  - self_charged: acquisitions * rate
  - cost_article_12: self_charged
  - cost_article_10: self_charged - self_charged
  - saving_article_10: cost_article_12 - cost_article_10
expected:
  self_charged: 7200
  cost_article_12: 7200
  cost_article_10: 0
  saving_article_10: 7200
```

## When to refuse or refer

- Acquisitions from outside the EU (importations): these are not intra-Community acquisitions and are not covered here.
- Services received from abroad: `mt-reverse-charge-vat-services-received-from`.
- Distance sales, OSS and IOSS registrations and the separate thresholds attaching to them.
- New means of transport and excise goods, where the ordinary acquisition threshold does not operate in the normal way.
- Triangulation, call-off stock and chain transactions involving three or more Member States.
- Article 11 small undertaking clients whose registration status may change as a result of the acquisition.
- The Article 12 declaration fields and portal mapping, and any disputed late-penalty assessment.
- Whether a specific reduced rate item applies, which needs the relevant Schedule to the VAT Act, not the summary rate page.

## Sources

| Source and scope actually read | Official URL | Read on |
|---|---|---|
| VAT Act, Cap. 406: read for art. 12 (registration), 19 (rates), 20 and 21 (liability, payment, interest, 7-day window), 22, 30A, 42(1)(d), 73(5), Second Schedule item 18, Third Schedule items 3 and 4 (EUR 10,000 threshold and its value), Fourth Schedule item 6 | https://legislation.mt/eli/cap/406/eng/pdf | 2026-11-14 |
| MTCA, VAT rates page: read for 18%, 12%, 7%, 5% and 0% as exemption with credit | https://mtca.gov.mt/business-tax/vat1/vat-compliance/vat-rates/vat-rates | 2026-11-14 |
| Recapitulative statement regulations, S.L. 406.14: read for reg. 3 (15th day, EUR 50,000 quarterly test) | https://legislation.mt/eli/sl/406.14/eng/pdf | 2026-11-14 |
| MTCA, Registrations and De-Registrations FAQs: read on 4 November 2026 for the EUR 10,000 goods trigger and no Article 12 input recovery; not reopened today | https://mtca.gov.mt/docs/default-source/documents/registrations-and-de-registrations-faqs.pdf?sfvrsn=908511fc_1 | 2026-11-04 |

Not yet confirmed: the Article 12 declaration fields and the MTCA submission instruction; the MTCA statement that Article 12 persons cannot recover input VAT was read on 4 November 2026 and not reopened today; product classification for reduced rates; special-goods, chain and triangulation cases.

## Today's figures and who stands behind this skill

This file is an AI skill (tax rules your AI follows) from OpenAccountants, copied on 2026-11-14. Rates, thresholds and deadlines change. For the current version of this skill, its official sources and the named accountant (if any) who stands behind it, call `get_skill` with slug `mt-reverse-charge-acquisition-intra` on the OpenAccountants connector (https://www.openaccountants.com/connect), or read https://www.openaccountants.com/skills/mt-reverse-charge-acquisition-intra. If neither is available, confirm every figure against the official source pages cited above before relying on it.
