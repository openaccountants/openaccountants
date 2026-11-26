---
name: mt-reverse-charge-acquisition-intra
description: "How a person established in Malta accounts for VAT by reverse charge (self-charge) on intra-Community acquisitions of goods from another EU Member State, tax year 2026, when Article 12 registration is triggered by the EUR 10,000 acquisitions threshold, the rate, chargeability and payment dates, and how an Article 10 registered person declares the same acquisition. Services received from abroad are in mt-reverse-charge-vat-services-received-from."
jurisdiction: MT
tax_year: 2026
last_updated: 2026-11-26
drafted_by: OpenAccountants
approved_by: pending
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
tier: 2
version: 2.1
domain: vat-gst
type: situation-rules
---

# Reverse charge on intra-EU acquisitions of goods in Malta

## Scope and who this is for

This Guide covers ordinary intra-Community acquisitions of goods in Malta by a taxable person, including a self-employed individual, or a non-taxable legal person. The Article 10 option below requires an economic activity and the conditions in article 10(6)(b); it is not an option for every non-taxable legal person. In the Act an intra-Community acquisition is of goods only ([VAT Act, Second Schedule item 18(1)](https://legislation.mt/eli/cap/406/eng/pdf)). Figures cover calendar 2026.

First establish the right to dispose as owner of goods transported from one Member State to another, with transport ending in Malta. For ordinary goods the vendor must be a taxable person acting as such, not eligible for the Article 284 small-enterprise exemption and not covered by Articles 33 or 36 of the VAT Directive. Test the acquisition exemptions in Part Three of the Fifth Schedule before charging VAT. A supplier's EU address or an invoice without VAT is not enough ([VAT Act, arts 4(b), 9, Second Schedule item 18 and Third Schedule Part Three item 1](https://legislation.mt/eli/cap/406/eng/pdf)).

**Services are out of scope here.** A service received from a supplier not established in Malta, for which the Malta recipient is liable under article 20(2), has no monetary threshold and its own payment date; it is in `mt-reverse-charge-vat-services-received-from`.

Ordinary private purchases are outside this Guide; acquisition of a new means of transport by any person has separate rules, so the private-person exclusion must not be used for that purchase (article 4(b)(ii)). Check this point with one of our partner accountants. A person already registered under Article 10 does not need an Article 12 registration: it accounts for the same acquisition on its periodic return, as output tax, with input tax where deductible. The return itself is in `malta-vat-return`.

A point that decides the registration route: a person registered under Article 12 has no mechanism to recover the VAT it self-charges, so where the person would have a right to recover that input VAT, it should consider registration under Article 10 instead.

## Ask the client first

- Is the client already registered under Article 10, Article 11 or Article 12?
- Is it really an acquisition of goods moved from another Member State to Malta (not a service, not an import from outside the EU)?
- What is the cumulative relevant acquisition value this calendar year, does this acquisition make it exceed EUR 10,000, and is an earlier Article 12 registration still in force? A registration does not reset automatically each January (article 12(6), (7) and (10)).
- Would the VAT that has to be self-charged be recoverable as input VAT if the client were registered under Article 10?
- Is the vendor a taxable person acting as such, and do its small-enterprise exemption or the distance-sale/installation rules displace the ordinary acquisition treatment?
- Does the item fall under a reduced rate or an exemption rather than the standard rate, or is it a new means of transport or excise goods?

## The method, step by step

1. Establish whether the client is already registered under Article 10. If so, no Article 12 registration is needed: account for the acquisition on the periodic return, as output tax, with input tax where deductible (see `malta-vat-return`).
2. If the client is not registered under Article 10, check its existing Article 12 status, then test the current-year acquisition value against the threshold. Use the Seventh Schedule value; exclude new means of transport, excise goods and VAT paid or due in another Member State. Do not apply the ordinary threshold to the excluded special goods (Third Schedule Part Three, items 3 and 4).
3. Consider Article 10 only for a person carrying on or intending an economic activity who meets article 10(6)(b). Input recovery requires qualifying supplies, the Tenth Schedule evidence and restrictions, and reporting the acquisition tax as due; taxable business use alone does not guarantee a full deduction (article 22; Tenth Schedule items 1–4).
4. Apply through CFR Registrations Online Services. A Maltese e-ID is generally required; MTCA provides an alternative-access route for persons who cannot obtain one. Present the applicant’s ID/passport (or the company’s legal representative’s), and the memorandum/articles for a company or registered partnership, as specified in the [MTCA registration FAQs, page 6](https://mtca.gov.mt/docs/default-source/documents/registrations-and-de-registrations-faqs.pdf?sfvrsn=908511fc_1). Article 12(1) requires the application by the date of the threshold-crossing acquisition; the registration takes effect from that acquisition under article 12(5).
5. Determine the Maltese rate to self-charge on the acquisition. Unless a reduced rate or exemption specifically applies, the standard rate applies.
6. Work out chargeability: under Fourth Schedule item 6, acquisition VAT becomes chargeable on the earlier of the date the supplier issues the tax invoice and the 15th day of the month following the acquisition.
7. Declare and pay. An Article 12 person pays by the 15th of the month following chargeability (arts 20(1)(b) and 21(2)) and furnishes both the notice of payment and the required acquisition declaration on the prescribed form (arts 21(5) and 30A). The field mapping and submission instructions are referred below; this Guide is not a complete portal-filing instruction. Do not use the Article 10 seven-day electronic window for an Article 12 payment. Dates that fall on a Saturday, Sunday, national day or public holiday move under art. 73(5).
8. Purchases alone do not create an outbound recapitulative-statement duty. If the client also makes the reportable goods or services supplies in article 30(2), submit the statement electronically under S.L. 406.14 regulation 5; use the applicable monthly or quarterly rules below.

## Rates, bands and thresholds

| Item | Figure and conditions | Tax year | Source |
|---|---|---|---|
| Acquisitions Threshold, VAT Act Third Schedule item 3 | EUR 10,000: registration is triggered when the current-year relevant value exceeds it; includes the whole threshold-crossing acquisition. Taxable persons outside Article 10 and non-taxable legal persons are covered. Seventh Schedule values exclude new means of transport, excise goods and VAT in another Member State (item 4); existing Article 12 status must also be checked | Calendar 2026 | https://legislation.mt/eli/cap/406/eng/pdf |
| Standard rate, art. 19(1) | 18% of taxable value for ordinary standard-rated goods; acquisitions use the rate of a supply of like goods (art. 19(3)); test exemptions first | Current | same |
| Reduced rates, art. 19(2) | not higher than 18% or lower than 5%; MTCA lists 12%, 7% and 5%, and 0% as exemption with credit | Current | https://mtca.gov.mt/business-tax/vat1/vat-compliance/vat-rates/vat-rates |
| Chargeability of an acquisition, Fourth Schedule item 6 | earlier of the supplier's tax invoice date and the 15th day of the month after the acquisition | Current | https://legislation.mt/eli/cap/406/eng/pdf |
| Article 12 payment for goods, arts 20(1)(b) and 21(2) | by the 15th day of the month following chargeability | Current | same |
| Article 10 electronic filing window, arts 21(4A) and 42(1)(d) | no article 38 penalty for an article 27 return furnished electronically within 7 days after its due date; interest relief additionally requires electronic payment with that return within 7 days after the tax becomes payable. Neither relief extends Article 12 payments | Current | same |
| Recapitulative statement, S.L. 406.14 reg. 3 | monthly by the 15th of the following month; goods/mixed quarterly option only if reportable goods supplies excluding VAT do not exceed EUR 50,000 in the current quarter or any of the previous four quarters. The option ends after the threshold-crossing month and a statement covers elapsed months by the next 15th. Services-only reportable supplies may be quarterly by the 15th after quarter-end (reg. 3(3)) | Current | https://legislation.mt/eli/sl/406.14/eng/pdf |

## Worked cases

**Case 1: an Article 11 shop crosses the threshold.** An Article 11 shop has EUR 9,000 of relevant acquisitions before a EUR 2,000 taxable acquisition of standard-rated goods on 20 March 2026. The qualifying acquisition crosses EUR 10,000; the Article 12 application is due by that acquisition date. The tax invoice is issued the same day: chargeability is 20 March and payment is due 15 April 2026. VAT is charged on the whole qualifying acquisition, not just the EUR 1,000 excess ([Act, arts 12(1), 19(3), 20(1)(b), 21(2); Fourth Schedule item 6](https://legislation.mt/eli/cap/406/eng/pdf)). Assume the vendor and acquisition pass the scope tests above, no exemption applies, and the shop has no existing Article 12 registration. Supplier exemption and special-goods exclusions have been tested before this example.

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

**Case 2 (a decision): Article 12 or Article 10 for a buyer who could recover the VAT.** A trading business expects EUR 40,000 of standard-rated acquisitions in 2026, all used for taxable supplies. Assume the business qualifies for Article 10, the acquisitions are taxable at 18%, no deduction is blocked, and it holds the invoices, reports the tax due and satisfies the records requirements. Under Article 12 it self-charges EUR 7,200 and recovers nothing. Under Article 10 it declares EUR 7,200 output tax and deducts EUR 7,200 input tax, net nil, but takes on periodic returns and charges VAT on its own sales. Where the sales are taxable and the input is recoverable, the acquisition VAT difference is EUR 7,200; this is not a total annual saving after sales VAT and compliance costs. Where supplies are exempt without credit and none of article 22(4)'s qualifying exceptions applies, no acquisition input credit follows; Article 10 eligibility must still be established rather than assumed.

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
- Distance sales, OSS and IOSS registrations and their separate rules. Check this point with one of our partner accountants.
- New means of transport and excise goods: do not apply the ordinary threshold. Check this point with one of our partner accountants.
- Triangulation, call-off stock, own-goods transfers and chain transactions. Check this point with one of our partner accountants.
- Any effect on Article 11 small-enterprise status beyond the distinct Article 12 goods duty. Check this point with one of our partner accountants.
- Article 12 declaration fields, portal submission and payment-reference instructions, registration cancellation, and disputed late penalties. Check this point with one of our partner accountants.
- Product-specific rates or acquisition exemptions: establish the applicable statutory item before using a rate. Check this point with one of our partner accountants.

## Sources

| Source and scope actually read | Official URL | Read on |
|---|---|---|
| VAT Act, Cap. 406: read arts 4–10 and 12 (scope and registration), 18–23, 27, 30(2), 30A, 42(1)(d), 73(5); Second Schedule item 18; Third Schedule Part Three items 1–4; Fourth Schedule items 5–6; Fifth Schedule Part Three; Seventh Schedule items 1–4 and 9–10; Tenth Schedule items 1–4 (value, evidence and deduction limits) | https://legislation.mt/eli/cap/406/eng/pdf | 2026-11-26 |
| MTCA, VAT rates page: read for 18%, 12%, 7%, 5% and 0% as exemption with credit | https://mtca.gov.mt/business-tax/vat1/vat-compliance/vat-rates/vat-rates | 2026-11-26 |
| Recapitulative statement regulations, S.L. 406.14: read regulations 3–6, including threshold-crossing, services-only quarters and electronic submission | https://legislation.mt/eli/sl/406.14/eng/pdf | 2026-11-26 |
| MTCA, Registrations and De-Registrations FAQs (updated 20 February 2026): pages 3–6, registration routes, no Article 12 input recovery and online access | https://mtca.gov.mt/docs/default-source/documents/registrations-and-de-registrations-faqs.pdf?sfvrsn=908511fc_1 | 2026-11-26 |

Not yet confirmed: none retained as usable guidance; the partner-accountant referrals above cover portal fields, submission and payment-reference instructions, cancellation, disputed penalties, classification and specialist transactions.
