---
name: cancelling-a-vat-registration-and-the-exit-vat-charge
description: The threshold rose to R2.3 million on 1 April 2026, so many vendors can now deregister — but section 8(2) deems a supply of everything still on hand, and the exit charge decides whether it is worth doing.
jurisdiction: ZA
last_updated: 2026-09-02
review_status: pending_review
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# South Africa — Cancelling a VAT Registration

## South Africa — Cancelling a VAT Registration

> **Deregistering is not free.** On cancellation, s 8(2) deems the vendor to have supplied
> everything still held for the enterprise — trading stock, plant, equipment, vehicles,
> fixed property — and output tax falls due on it in the final return. A vendor who
> deregisters to save administration can receive a bill instead. **Compute the exit charge
> before applying, not after.**

## Section 1 — Why this matters now

- **Compulsory VAT registration threshold from 1 April 2026** — R2,300,000 (rose from R1,000,000) ZAR (Compulsory registration threshold effective 1 April 2026)
- **Voluntary VAT registration threshold from 1 April 2026** — R120,000 (rose from R50,000) ZAR (Voluntary registration threshold effective 1 April 2026)

On **1 April 2026** the compulsory VAT registration threshold rose from R1,000,000 to
**R2,300,000**, and the voluntary threshold from R50,000 to **R120,000**. It had not moved
for seventeen years.

Every vendor whose taxable supplies fall between R1,000,000 and R2,300,000 is therefore now
**below** the compulsory threshold and may apply to deregister. That is a large population,
and most of them will ask the question this year.

The answer is not automatically yes.

## Section 2 — Grounds for cancellation ([SARS, Cancellation of VAT registration](https://www.sars.gov.za/types-of-tax/value-added-tax/cancellation-of-vat-registration/))

- **Vendor may apply to cancel** — A vendor may apply where the value of taxable supplies will be less than the compulsory registration threshold of R2,300,000 in any consecutive twelve month period.  _([Value-Added Tax Act 89 of 1991 s 24; SARS, Cancellation of VAT registration](https://www.sars.gov.za/types-of-tax/value-added-tax/cancellation-of-vat-registration/))_
- **Commissioner may cancel** — The Commissioner may cancel where: - the enterprise has ceased and will not restart within twelve months - the enterprise never commenced, or will not commence within twelve months - the vendor no longer meets the registration requirements - the vendor fails to furnish required VAT returns - a voluntary registrant has no fixed place of business, no proper records, no bank account, or has previously failed VAT or Sales Tax duties  _([Value-Added Tax Act 89 of 1991 s 24; SARS, Cancellation of VAT registration](https://www.sars.gov.za/types-of-tax/value-added-tax/cancellation-of-vat-registration/))_
- **Effective date** — Cancellation generally takes effect from the last day of the tax period in which the vendor ceased to carry on all enterprises, though the Commissioner may set a different date.  _([Value-Added Tax Act 89 of 1991 s 24; SARS, Cancellation of VAT registration](https://www.sars.gov.za/types-of-tax/value-added-tax/cancellation-of-vat-registration/))_

## Section 3 — The exit charge: s 8(2) deemed supply

- **s 8(2) deemed supply on cessation** — On ceasing to be a vendor, the person is deemed to have supplied the goods and rights forming part of the enterprise's assets, immediately before cessation. Output tax is payable on that deemed supply.  _(Value-Added Tax Act 89 of 1991 s 8(2), s 10(5), s 17(2))_

### What is caught

- **What is caught** — Trading stock, consumables, plant and equipment, vehicles, fixtures, fixed property, and rights held for the enterprise — anything still on hand at the effective date.  _(Value-Added Tax Act 89 of 1991 s 8(2), s 10(5), s 17(2))_

### What is excluded

- **What is excluded** — - **Goods on which input tax was denied** under s 17(2) — most notably motor cars and entertainment. No input was claimed, so no output arises on exit. - **Assets acquired for no consideration**, such as donated goods, because the cost is nil.  _(Value-Added Tax Act 89 of 1991 s 8(2), s 10(5), s 17(2))_

### How it is valued

- **How it is valued** — The deemed consideration is the **lesser of cost and open market value** — cost including VAT. For most used plant and stock the open market value is lower and governs; for appreciating assets, notably fixed property, cost will often be lower and governs instead.  _(Value-Added Tax Act 89 of 1991 s 8(2), s 10(5), s 17(2))_

## Section 4 — Computing and declaring the exit VAT

- **Exit VAT formula** — exit VAT = deemed consideration × 15 / 115 (The deemed consideration is VAT-inclusive, so the output tax is the tax fraction of it, not 15% added on top. Applying 15% to the consideration overstates the liability by roughly 15%.)  _(Value-Added Tax Act 89 of 1991, proviso to s 8(2))_
- **Where output tax is declared** — Output tax on assets on hand is declared in field 1A of the final VAT201 — not in field 1 with ordinary standard-rated supplies.  _(Value-Added Tax Act 89 of 1991, proviso to s 8(2))_

**A worked illustration.** A vendor deregisters holding stock whose open market value is
R180,000 (cost R240,000), equipment with an open market value of R60,000 (cost R150,000),
and a motor car:

```
stock       lesser of 240,000 and 180,000        = R180,000
equipment   lesser of 150,000 and  60,000        =  R60,000
motor car   input tax denied under s 17(2)       =        —
                                       deemed    = R240,000
exit VAT    R240,000 × 15/115                    =  R31,304.35
```

That R31,304.35 is the number that decides whether deregistering is worth doing.

### You may not have to pay it all at once

- **Six-month payment relief under proviso to s 8(2)** — Where the deregistration is solely because taxable supplies fell below the threshold — as opposed to ceasing to trade — the proviso to s 8(2) allows the exit VAT to be paid over a period of six months. This materially changes the arithmetic for a vendor sitting between R1,000,000 and R2,300,000 who wants out but cannot fund the charge in one payment. Check that the ground relied on is the threshold ground before assuming the relief. A vendor who has actually ceased trading does not get it.  _(Value-Added Tax Act 89 of 1991, proviso to s 8(2))_

## Section 5 — The other exit charge: creditors under s 22(3)

- **s 22(3) creditor adjustment on cessation** — The s 8(2) deemed supply catches assets. It is not the only adjustment triggered on the way out. Under s 22(3), a vendor who claimed input tax on a supply and has not paid the creditor must make an output tax adjustment. The general rule bites where the amount remains unpaid twelve months after it fell due. On cessation, creditor balances are brought into account where the input tax was claimed within the preceding twelve months — so a vendor with a large unpaid trade creditor can face a second charge that has nothing to do with assets. Run the creditors age analysis at the effective date alongside the asset schedule. A deregistration priced on assets alone can be materially understated.  _(Value-Added Tax Act 89 of 1991 s 22(3))_

## Section 6 — The application

- **Application forms VAT123e / VAT123T** — Complete VAT123e — Application for the cancellation of registration of a person in respect of all his enterprises. Where only some enterprises are being cancelled, the form is VAT123T. Submit it to the SARS branch where the vendor is registered, by email or through a virtual appointment booked on eBooking. State the circumstances giving rise to the cancellation on the form or in an attached letter — an application that does not say why tends to come back.  _(Value-Added Tax Act 89 of 1991 s 24(3), s 24(7); SARS, Cancellation of VAT registration)_

⚠️ **The printed VAT123e still shows the old R1 million threshold.** The form version in
circulation predates the April 2026 change. It is the Act that sets the threshold, not the
form; do not let a stale form talk a client out of an application they qualify for.

- **Nothing payable on application** — Nothing is payable on application. SARS issues a cancellation notice setting the effective date and the final tax period. The vendor keeps charging VAT and filing until that date.  _(Value-Added Tax Act 89 of 1991 s 24(3), s 24(7); SARS, Cancellation of VAT registration)_
- **Two different twenty-ones** — A vendor who has ceased all enterprises must notify the Commissioner within 21 days of cessation (s 24(3)); that is a statutory duty on the vendor. Separately, SARS works to roughly 21 business days to process a cancellation; that is a service turnaround, not a deadline binding anyone.  _(Value-Added Tax Act 89 of 1991 s 24(3), s 24(7); SARS, Cancellation of VAT registration)_
- **If the application is refused** — If the application is refused, either fix the defect and re-apply, or object. The objection route is NOO/ADR1, within 80 business days.  _(Value-Added Tax Act 89 of 1991 s 24(3), s 24(7); SARS, Cancellation of VAT registration)_

## Section 7 — What does not stop

- **What does not stop** — - **Charge and account normally until the last day of the final tax period.** Output tax on supplies made, and input tax deductions, continue right up to the effective date. - **File the final return** including the s 8(2) deemed supply in field 1A. - **SARS will not finalise the cancellation until every outstanding liability and obligation under the VAT Act is resolved or settled.** Outstanding returns or debt stall the exit. - **Records must still be retained** under the Tax Administration Act. Cancellation does not end the retention obligation, and SARS can still verify a period that closed before it. - **Valuation date.** Assets and stock are valued on the day **immediately before** the effective date, not at the date of application and not at the date SARS replies.

## Section 8 — Whether to deregister at all

The statute decides eligibility. Whether it is sensible is a judgement, and these are the
factors that decide it:

**Against deregistering**

- The **s 8(2) exit charge**, payable now, in cash
- **Input tax on future purchases is lost** — it becomes a cost rather than a claim
- **Customers who are themselves vendors** can no longer claim input tax on your invoices, which is a real disadvantage where you sell business-to-business
- **Capital purchases planned soon** would carry unrecoverable VAT
- **Re-registering later** if turnover recovers means re-registration, not resumption

**For deregistering**

- The **administrative burden** ends — returns, records, reconciliations
- **Pricing flexibility** where customers are consumers or non-vendors, since output tax need no longer be built into the price
- **Cash flow**, where output tax was routinely paid before customers settled

The exit charge is a one-off; the input tax loss is permanent. A vendor near the threshold whose customers are mostly registered businesses will often be better off staying in.

## The method, step by step

1. **Confirm eligibility on the twelve month test first.** Taxable supplies below R2,300,000 in any consecutive twelve month period — measured on taxable supplies, not on total turnover, and not on the financial year.
2. **Inventory everything still held for the enterprise** before valuing anything: stock, plant, equipment, vehicles, fixtures, fixed property, rights.
3. **Tag out the exclusions.** Motor cars and entertainment where input tax was denied under s 17(2), and anything acquired for no consideration. Tag them visibly rather than deleting them — a reviewer needs to see the item was considered and excluded.
4. **Value each remaining item at the lesser of cost and open market value.** Both figures, item by item. An asset the client reports as worthless still needs confirmation it was scrapped, because SARS tests open market value.
5. **Total the deemed consideration, then apply the tax fraction** — × 15/115, not × 15%.
6. **Run the creditors age analysis at the same date.** s 22(3) can add a second charge that the asset schedule will never show. A price built on assets alone is incomplete.
7. **Decide whether to proceed**, using the total exit cost against the factors in Section 8 — and check whether the six-month payment relief in the proviso to s 8(2) is available, because it applies only where the ground is the threshold and not cessation.
8. **Apply on VAT123e, stating the grounds**, then charge and account normally to the last day of the final period, valuing assets on the day immediately before the effective date, and declare the deemed supply in field 1A of the final return.

**What breaks when the order is wrong.** Applying before computing the exit charge commits the client to a liability nobody has quantified. Pricing on assets and forgetting creditors understates it a second time. Valuing before inventorying misses assets, and every missed asset is understated output tax that surfaces on verification. Applying 15% rather than the tax fraction overstates the charge and may kill a deregistration that was worth doing. And deleting excluded items instead of tagging them leaves a working paper that cannot be reviewed.

## Edge cases

- **Fixed property is where the money is.** Cost will often be below open market value, so cost governs — but on a commercial property either figure produces a large charge. Price it before advising.
- **The threshold test is taxable supplies**, so exempt and non-supply receipts do not count toward it. A landlord with mixed residential and commercial letting may be below the threshold on taxable supplies while turning over far more.
- **Zero-rated supplies are taxable supplies** and count toward the threshold, even though no output tax arises on them. Exporters are caught by this regularly.
- **Ceasing to trade is a separate ground** from falling below the threshold, and carries the same s 8(2) consequence.
- **Deregistration does not extinguish prior-period liability.** Assessments, penalties and verifications for periods before cancellation survive it.

## Self-checks

1. **Tax fraction, not the rate.** Confirm the exit VAT is consideration × 15/115. If it is consideration × 15%, it is overstated.
2. **Every asset carries two values.** Cost and open market value, with the lesser used. A line with only one figure has not been tested.
3. **Excluded items are present and tagged**, not missing. Motor cars and entertainment should appear on the schedule with the exclusion and its reason stated.
4. **The threshold test used taxable supplies over a rolling twelve months**, not the financial year and not total turnover.
5. **Outstanding returns cleared** before applying — SARS will not finalise while anything is outstanding.
6. **Creditors tested, not just assets.** Confirm an ageing was run at the effective date and s 22(3) considered.
7. **Six-month relief checked against the ground relied on.** It is available on the threshold ground, not on cessation.

## Disclaimer

> **General reference only.** This file is general tax reference material for AI-assisted
> workflows. It has not been reviewed for any specific person's facts, documents, elections,
> deadlines, registrations or local procedures. Do not rely on it to file, pay, amend,
> deregister or take a tax position without review by a qualified professional in
> South Africa.

## Sources

Value-Added Tax Act 89 of 1991 s 8(2) and its proviso, s 10(5), s 17(2), s 22(3), s 24(1)–(3) and s 24(7). SARS — Cancellation of VAT registration: https://www.sars.gov.za/types-of-tax/value-added-tax/cancellation-of-vat-registration/ SARS — Budget 2026 FAQs (thresholds): https://www.sars.gov.za/about/sars-tax-and-customs-system/budget/budget-2026-frequently-asked-questions/ SARS — VAT 404 Guide for Vendors. Forms VAT123e / VAT123T.

> Contributed by Brandon Iverach, SAIPA 18504 / SARS PR0025122.

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
