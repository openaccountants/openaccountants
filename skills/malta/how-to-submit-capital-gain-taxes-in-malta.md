---
name: how-to-submit-capital-gain-taxes-in-malta
description: "Working method for the accountant supporting a seller of Malta immovable property at the deed, tax year 2026. Covers the article 5A final withholding tax on the transfer value (8% general, 10% for property acquired before 2004, 5% within five years, 2% for a first home sold within three years, 7% for property inherited before 25 November 1992, 12% on the gain election for later inheritances and donations), the own-residence exemption, brokerage deduction, the notary's DDT1 and payment, the 15% valuation tolerance, and non-resident opt-out at 7% provisional tax. Trigger on: sell property Malta, property transfer tax Malta, 8% final tax, capital gains on a house in Malta, inherited property sale Malta, notary tax Malta."
jurisdiction: MT
category: international
tax_year: 2026
last_updated: 2026-10-23
version: 1.1
verified_by: pending
authored_by: Michael Cutajar and the OpenAccountants team
review_status: pending_review
trust_label: Built by Michael Cutajar and the OpenAccountants team
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# How to submit capital gain taxes in Malta v1.1

Built by Michael Cutajar and the OpenAccountants team. **Source-cited draft: not reviewed by an accountant.**

Tax year 2026. The rates below are the article 5A rates the Malta Tax and Customs Administration (MTCA) publishes for transfers made on or after 1 January 2015; they apply unchanged to deeds in 2026. Full rules, exclusions and article 5 gains are in `mt-capital-gains` and `mt-property-transfer-tax-the-sale-immovable`.

## METHOD

### [method:scope_gate] Who this is for, and when to stop

This skill is for the ordinary case: a private individual or a Maltese company transferring immovable property situated in Malta under the Article 5A final withholding tax (FWT) regime. It is written for a competent accountant supporting the client around the deed, not for the notary, who is the actual tax collector here.

Stop and send the client to a property-tax specialist or a warranted notary before you commit to a figure when any of these appear: the property forms part of a "project" (developed or subdivided into more than one transferable unit); the transfer involves emphyteusis, usufruct, or splitting of bare ownership from usufruct; a non-resident transferor wanting to opt out of FWT via a foreign-residence certificate; a partition/division of co-owned property; a notice of a promise of sale ("konvenju") given to the Commissioner before 17 November 2014, which changes the applicable rate; or any Special Designated Area (SDA) / Acquisition of Immovable Property (AIP) permit question. These are not "harder versions" of the same computation. They change which regime applies, and the notary's deed locks the wrong answer permanently.

### [method:sequence] Order of operations

Do these in order. A wrong order corrupts the rate itself, not just the arithmetic.

1. Establish the **acquisition date** and the **means of acquisition** (purchase, inheritance, donation) FIRST. This single fact set, not the sale price, determines the rate (2% / 5% / 7% / 8% / 10% / 12%). Compute anything before this and you may apply the wrong rate to the wrong base.
2. Establish whether the property is the transferor's **own residence**, owned and occupied for at least 3 consecutive years immediately before the transfer and transferred within 12 months of vacating, and declared as the main residence. This is the exemption gate.
3. Only then confirm the **transfer value** (the higher of consideration or market value) and deduct brokerage fees paid by the transferor, where the verification conditions of the Tax on Property Transfers Rules are met.
4. Determine whether the base is the **transfer value** (FWT) or the **gain** (the 12% election on post-24 November 1992 inherited property, or donated property received more than 5 years before the transfer). These are different bases; do not mix them.
5. Confirm who collects and pays: the **notary** withholds and remits, not the client. Your job is to hand the notary a defensible computation and the supporting evidence.

### [method:intake_questions] Client intake questions

- When and how did you acquire this property: bought, inherited, or received as a donation? Get the exact date and the deed.
- If inherited: before 25 November 1992 or after 24 November 1992? (7% final tax vs the 12%-on-gain election.) If donated: more than 5 years before the transfer? (12%-on-gain election available only then.)
- Is this your own residence, and how long have you owned AND lived in it?
- Did you buy it within the last 3 years declaring it as your sole ordinary residence, and do you own any other residential property? (2% rate.)
- Have you rented it out, used it in a business, or carried out works needing a development permit in the last 5 years?
- Is there a promise-of-sale agreement, and when was it notified to the Commissioner?
- Where is the property: an Urban Conservation Area, a scheduled building, or a Special Designated Area?
- Are you resident in Malta for tax purposes? If not, are you tax-resident and taxable on Maltese property gains elsewhere?

### [method:evidence] Documents and evidence

Insist on seeing (file-grade): the original acquisition deed (for date, means, and declared acquisition value); the causa mortis declaration if inherited (for the declared value that becomes the 12% base); any promise-of-sale agreement; and, for the 5% restoration rate, the Planning Authority certificate confirming the restoration works were completed under the permit. Take the client's word for (draft-grade, but confirm before signing): occupancy dates for the own-residence exemption, and the split of agency fees. Never accept an oral acquisition value. It must come off the deed.

### [method:judgment_rule] Picking between routes

The main election is post-1992 inherited property, or property donated more than 5 years before the transfer: 12% final tax on the *gain* (transfer value minus the value declared in the causa mortis declaration or donation deed) versus the applicable *transfer-value* rate (10% / 8% / 5% by acquisition date). Where the property has appreciated substantially since the declared value, the transfer-value route is cheaper; where the declared value was already close to market, the 12%-on-gain route is cheaper. Model both, in writing, and put the comparison in the working paper. The notary needs to see why you chose. The election is made on the deed and cannot be undone afterwards.

### [method:conservative_default] Conservative defaults

When the occupancy period for the own-residence exemption is uncertain at draft time, assume the exemption does NOT apply and compute the FWT, then flag it for the client to substantiate before the deed. When the acquisition value on an old deed is ambiguous or the deed is missing, do not estimate. Flag [refer] and get the deed from the Public Registry. An invented acquisition value is the single most dangerous number in this whole exercise.

### [method:trap] Traps and most-missed items

- **FWT is on transfer VALUE, not on gain.** The client pays even at a loss. Non-specialists routinely tell the client "no profit, no tax". That is wrong, and it destroys trust at the deed.
- **Applying 8% by default.** 8% is the *general* rate. Property acquired *before* 1 January 2004 is 10% (unless a promise of sale was notified before 17 November 2014). Miss this and you under-collect by 2 points of the whole value.
- **The 5% quick-sale rate.** Transfers within 5 years of acquisition (not forming part of a project) are 5%, not 8%. Since 20 March 2020 (Act VIII of 2020, art. 14) the 5% rate is lost where the transferor or a related person carried out works needing development permission in those 5 years, unless the property was bought as a declared sole ordinary residence.
- **The 2% first-home rate.** An individual (or two co-owners) who declared on the purchase deed that the property was bought as their sole ordinary residence, and sells within 3 years while owning no other residential property, pays 2%.
- **Forgetting the notary is the collector.** The FWT is withheld and remitted by the notary on the deed. Late or wrong figures don't just cost interest; they can hold up the deed itself.
- **Own-residence exemption assumed, not proven.** The 3-year ownership and occupation and the 12-month transfer window are strict. Assume it and the client may face FWT they never budgeted for.
- **Undervaluing.** The department's architect can revalue. If the market value it sets exceeds the declared price by more than 15%, an assessment is issued on both buyer and seller.

### [method:cross_check] Cross-checks before signing

Before you hand the notary your figure: the acquisition date on your computation must match the acquisition deed exactly; the base (transfer value vs gain) must match the regime you selected; the transfer value must be the higher of consideration or market value; and brokerage deductions must be supported by invoices. Reconcile your FWT figure to the notary's own computation. They run it independently, and a mismatch surfaced *before* the deed is a five-minute fix; after the deed it is a permanent error.

### [method:filing_mechanics] Portal and filing mechanics

The transfer is executed on a notarial deed. A promise of sale is presented at the Property Tax Directorate within 21 days of signing. On the deed, the **notary** submits the DDT1 notice of transfer to the Property Tax Directorate with a copy of the contract, site plans, the Public Registry note, the buyer's duty, the seller's tax and, for residential property, Schedule 8. Receipts normally issue within 3 weeks. The seller does not file separately for a pure FWT transfer. It is *final*, so it does not go into the annual income tax return. The deed is the lock point: once published, the rate and election are fixed. Your working papers should reach the notary before the deed date, not on it.

### [method:cross_check] What must reconcile

(covered above: computation vs deed, base vs regime, figure vs notary's independent calc)

## FACT CORRECTIONS

**FACT CORRECTIONS**  _(Income Tax Act, Cap. 123, art. 5A; Income Tax Management Act, Cap. 372, art. 43; MTCA "New Property Tax System - FAQ"; MTCA "Selling Property"; MTCA "General Information on Duty")_

| fact_key | current | correct | source |
| --- | --- | --- | --- |
| general_fwt | 8% | General FWT from 1 January 2015: 8% of transfer value (the higher of consideration and market value) | ITA art. 5A(5)(a), 5A(6)(a) |
| pre_2004_fwt | 10% | Property acquired before 1 January 2004 (no promise of sale notified before 17 November 2014): 10% of transfer value | ITA art. 5A(5)(f) |
| quick_sale_fwt | 5% | Transfer within 5 years of acquisition, not part of a project: 5%. Lost from 20 March 2020 where permit works were done in those 5 years, unless bought as a declared sole ordinary residence | ITA art. 5A(5)(e); Act VIII of 2020, art. 14 |
| first_home_fwt | (missing) | Property bought as declared sole ordinary residence, sold within 3 years, seller owns no other residential property: 2% | ITA art. 5A(5)(g) |
| restoration_fwt | 5%, property acquired after 1 Jan 2016 | Property in a UCA or scheduled, restored under a permit applied for on or after 1 January 2015, transferred on or after 1 January 2016, completion certificate produced to the notary, rate not used on a previous transfer: 5% | ITA art. 5A(5)(h) |
| pre_1992_inheritance | 7% (incl. judicial auction) | Inherited before 25 November 1992: 7% of the transfer value. A judicial sale by auction is outside art. 5A, except a judicial auction of property inherited on or after 25 November 1992, which is taxed at 7% | ITA art. 5A(3)(f) and (5)(c) |
| post_1992_inheritance | 12% on gain | Inherited after 24 November 1992: 12% on (transfer value less value in the causa mortis declaration), unless the seller elects on the deed for the transfer-value rate (10%, 8% or 5%) | ITA art. 5A(5)(b) |
| donation | 12% on gain | Donated more than 5 years before the transfer: 12% on the excess over acquisition value (not for a project), unless the seller elects on the deed for the transfer-value rate. Within 5 years: the donor's acquisition date counts | ITA art. 5A(5)(b) |
| non_resident | 12% default FWT | No separate non-resident rate. A non-resident taxable on the gain in their country of residence may opt out of art. 5A with a certificate from that country's tax authority, and is then taxed under art. 5 with 7% provisional tax that is not refundable | ITA art. 5A(3)(h); Income Tax Management Act art. 43(1)(b) |
| own_residence | exempt | Owned and occupied as own residence 3 consecutive years before the transfer, sold within 12 months of vacating, declared as main residence: exempt | ITA art. 5A(4) and art. 5(5)(c); MTCA FAQ, Q9 |
| brokerage | deductible with notary fee | Brokerage fees paid by the transferor are deductible from the transfer value if the Tax on Property Transfers Rules' verification conditions are met | MTCA FAQ, Q18 |
| buyer_duty | 5% | Buyer's duty: general 5% (MTCA example: EUR 10,000 on EUR 200,000), 1% provisional duty at promise of sale | MTCA General Information on Duty |
| valuation_tolerance | (missing) | 15% tolerance between declared value and the department's valuation; above that, assessment on buyer and seller | MTCA Selling Property |

## FLAGS

- [unsettled] First-time buyer and other duty reliefs change with the Budget. The first-time buyer duty exemption was widened for transfers from 28 October 2025 (LN 305/2025). Confirm the relief in force at the deed date. (These are buyer-side, but clients ask.)
- [unsettled] LN 284/2025 extends to the end of 2026 relief from income tax and duty on transfers of property built at least 20 years earlier and vacant for at least 7 years, property in an urban conservation area, and property developed in Maltese traditional style. Check the conditions before relying on it.
- [refer] Any "project" property, emphyteusis/usufruct split, partition of co-owned property, non-resident opt-out via foreign-residence certificate, SDA/AIP permit question, or a promise of sale notified before 17 November 2014: refer to a property-tax specialist or warranted notary.
- [refer] Missing or ambiguous acquisition deed / acquisition value: pull the deed from the Public Registry; do not estimate.

## NOTES

Selling real estate situated in Malta is taxed under a **final withholding tax** (Article 5A of the Income Tax Act) on the **transfer value**, not on the capital gain, and payable even where the seller makes no profit. Since 1 January 2015 the general rate is 8%. The tax is withheld and remitted by the **notary** on the deed of transfer; for a pure FWT transfer it is final and does not enter the seller's annual return.

Worked example: an individual sells an apartment for EUR 300,000 that they bought in 2010 (acquired after 1 January 2004, held more than 5 years, not their own residence). Agency fee EUR 9,000. Base = EUR 300,000 - EUR 9,000 = EUR 291,000. FWT at 8% = EUR 23,280, withheld by the notary at the deed. Had they instead sold within 5 years of acquisition with no permit works, the rate would be 5% (EUR 14,550). Had it been their own residence owned and occupied 3+ years and sold within 12 months of moving out, it would be exempt.

```oa-check
name: Apartment bought 2010, sold for EUR 300,000 with EUR 9,000 agency fee (2026)
inputs:
  price: 300000
  agency_fee: 9000
steps:
  - base: price - agency_fee
  - fwt_general: base * 0.08
  - fwt_within_5_years: base * 0.05
expected:
  base: 291000.00
  fwt_general: 23280.00
  fwt_within_5_years: 14550.00
```

## Sources

| Source | URL | Read on |
|---|---|---|
| MTCA, New Property Tax System - FAQ (art. 5A rates, exemptions, elections) | https://mtca.gov.mt/personal-tax/property-taxes/faqs/new-property-tax-system---faq | 2026-10-23 |
| MTCA, Selling Property (DDT1, 21 days, 15% tolerance) | https://mtca.gov.mt/personal-tax/property-taxes/selling-property | 2026-10-23 |
| MTCA, General Information on Duty (5% duty, 1% provisional) | https://mtca.gov.mt/personal-tax/property-taxes/general-information-on-duty | 2026-10-23 |
| MTCA, Overview of Legal Notices July to December 2025 (LN 284/2025, LN 305/2025) | https://mtca.gov.mt/docs/default-source/documents/legislative-developments/2026/overview-of-recently-published-legal-notices-july-to-december-2025-memo.pdf?sfvrsn=eaa8dda1_1 | 2026-10-23 |
| Income Tax Act, Cap. 123, art. 5A (rates, exclusions, transfer value) | https://legislation.mt/eli/cap/123/eng | 2026-10-23 |
| Income Tax Management Act, Cap. 372, art. 43 (7% provisional tax) | https://legislation.mt/eli/cap/372/eng | 2026-10-23 |
| Act VIII of 2020, art. 14 (permit-works proviso to the 5% rate, assented 20 March 2020) | https://legislation.mt/eli/act/2020/8/eng | 2026-10-23 |

Not yet confirmed:
- The brokerage deduction conditions (Tax on Property Transfers Rules) and the 21-day promise-of-sale and DDT1 steps were taken from MTCA pages, not re-read in the rules themselves.
- Budget 2027 is presented on 26 October 2026. Any change to art. 5A rates or reliefs for 2027 is not reflected here.

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
