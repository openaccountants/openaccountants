---
name: ca-real-estate-withholding-form-593
description: >
  California real estate withholding on Form 593 for sales and transfers of
  California real property closing in 2026. Covers who withholds (the real
  estate escrow person, the buyer, a qualified intermediary), when no
  withholding is needed (sales price USD 100,000 or less, foreclosure, the
  Part III certifications such as principal residence, loss or zero gain,
  section 351 and 721 transfers, corporations and partnerships with a
  California place of business), partial exemptions for 1031 exchanges and
  installment sales, the 3 1/3% sales price method against the optional gain
  method at 12.3%, 8.84%, 10.84%, 13.8% or 15.8%, the 20th-day filing and
  payment rule, the higher 2026 information-return penalties, trusts and
  single-member LLCs on title, and how the seller claims the credit. Trigger on
  "Form 593", "California real estate withholding", "3 1/3 percent escrow",
  "nonresident selling California property", "593 exemption".
version: 0.1
jurisdiction: US-CA
category: state-tax
tax_year: 2026
last_updated: 2026-11-21
tier: 2
domain: tax
type: computation
---

# California real estate withholding (Form 593), 2026 v0.1

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

> **Source-cited draft.** Built from the FTB 2026 Instructions for Form 593, the 2026 Form 593-V, FTB Publication 1016 (rev. 02/2026), the FTB real estate withholding page and FTB Tax News, May 2026, read on 2026-11-21. The California statute site (leginfo.legislature.ca.gov) refused our reader, so statute sections are cited only where an FTB page names them. No accountant has reviewed it.

**Answer first.** When California real estate is sold or transferred, the escrow person (or the buyer) withholds **3 1/3% (.0333) of the sales price** and sends it to the Franchise Tax Board, unless the sales price is **USD 100,000 or less**, the property is in foreclosure, or the seller certifies an exemption on Form 593 before closing. The seller can instead choose the **optional gain method**: estimated gain times **12.3%** for an individual or trust (other rates for entities). Form 593 goes to the FTB by the **20th day of the month after escrow closes**, with the payment, and Sides 1 to 3 are now filed for every transaction, exempt or not. The withholding is not a separate tax: the seller claims it as a credit on the California return for the year of sale.

**Tax year.** Transactions closing in 2026, on the 2026 Form 593. For taxable years beginning on or after 1 January 2026 the information-return penalties went up ([2026 Form 593 instructions, What's New](https://www.ftb.ca.gov/forms/2026/2026-593-instructions.html)).

**Circular 230 disclosure.** This material is general information, not written advice on a specific transaction under 31 CFR 10.37. It is not intended to be used, and cannot be used, to avoid penalties.

## Scope and who this is for

In scope: the withholding duty on any sale or transfer of California real property closing in 2026, for every seller type (individuals, trusts, estates, partnerships, LLCs, corporations), and the people who carry it out: the **real estate escrow person (REEP)**, meaning anyone who closes the transaction, including attorneys, escrow and title companies, qualified intermediaries, or anyone who receives and disburses the sale payments; and the **remitter**, who files the form and sends the payment for the buyer ([2026 Form 593 instructions](https://www.ftb.ca.gov/forms/2026/2026-593-instructions.html); [FTB Pub. 1016](https://www.ftb.ca.gov/forms/misc/1016.html)).

Out of scope, and where it goes:

| Topic | Skill |
| --- | --- |
| Whether the seller's actual tax on the gain is more or less than the withholding | `ca-income-tax`, `ca-540-individual-return` |
| The 1031 exchange itself and the FTB 3840 claw-back filing | `ca-like-kind-exchange-form-3840` |
| Withholding on other California-source payments to nonresidents (Forms 592, 592-B) | refer |
| Federal FIRPTA withholding on foreign sellers | refer |
| Documentary transfer taxes charged at recording | refer (county and city) |

## Ask the client first

- What is the sales price, and what is the seller's ownership percentage? Is the price USD 100,000 or less?
- Who or what is on title: an individual, a grantor or nongrantor trust, a single-member LLC, a partnership or LLC, a corporation? Is it a California entity or one registered with the Secretary of State?
- Was the property the seller's main home, and for how long in the last 5 years? Was it last used as the main home?
- What are the seller's adjusted basis and selling costs (to test for a loss and to compute the optional gain method)?
- Is this part of a 1031 exchange (simultaneous or deferred, through a QI), an installment sale, an involuntary conversion, or a transfer into a corporation or partnership?
- When does escrow close, and who is acting as the REEP?

## The method, step by step

### Rates, bands and thresholds ([2026 Form 593 instructions](https://www.ftb.ca.gov/forms/2026/2026-593-instructions.html))

| Item | Figure, 2026 | Conditions | Source |
| --- | --- | --- | --- |
| Sales price method | 3 1/3% (.0333) | Of the sales price times the ownership percentage; also applies to boot, the principal part of installment payments and a failed exchange | [2026 Form 593 instructions](https://www.ftb.ca.gov/forms/2026/2026-593-instructions.html) |
| No withholding: low sales price | USD 100,000 or less | Total sales price; parcels or units sold in one escrow are added together, so withholding applies if the total is over USD 100,000 even when each is under | same; [FTB Pub. 1016](https://www.ftb.ca.gov/forms/misc/1016.html) |
| Optional gain method, individual | 12.3% | Of the estimated gain on line 28 | [2026 Form 593 instructions](https://www.ftb.ca.gov/forms/2026/2026-593-instructions.html) |
| Optional gain method, non-California partnership | 12.3% | same | same |
| Optional gain method, corporation | 8.84% | same | same |
| Optional gain method, bank and financial corporation | 10.84% | same | same |
| Optional gain method, S corporation | 13.8% | same | same |
| Optional gain method, financial S corporation | 15.8% | same | same |
| Optional gain method, trust (grantor and nongrantor) | 12.3% | same | same |
| 1031 exchange: boot that is withheld on | more than USD 1,500 | Money or other property received beyond the like-kind property | same |
| Penalty: failure to notify the buyer in writing (REEP) | greater of USD 500 or 10% of the required withholding | Not where the buyer is a QI in a deferred exchange; excused for reasonable cause | same |
| Penalty: buyer fails to withhold after notice | greater of USD 500 or 10% of the required withholding | Not a QI in a deferred exchange | same |
| Penalty: complete and correct copies not given to the seller by the due date | up to USD 340 per Form 593; intentional disregard, greater of USD 680 or 10% | Taxable years beginning on or after 1 January 2026 | same |
| Penalty: Form 593 filed late or incomplete, per seller | USD 60 (1 to 30 days late), USD 130 (31 days to 6 months), USD 340 (over 6 months); intentional disregard, greater of USD 680 or 10% | same | same |
| Penalty: seller's false certificate to avoid withholding | greater of USD 1,000 or 20% of the required withholding | Knowingly false | same |

### Steps

1. **Check the three no-withholding cases first.** Sales price USD 100,000 or less; property in foreclosure; transferor a bank acting as trustee (other than under a deed of trust). Otherwise go on ([2026 Form 593 instructions](https://www.ftb.ca.gov/forms/2026/2026-593-instructions.html)).
2. **The REEP notifies the buyer in writing** of the withholding duty (not needed when the buyer is a QI in a deferred exchange). The seller must give the REEP or QI a signed Form 593 **before escrow closes** to claim an exemption; without it, withholding applies.
3. **Part III: full exemptions** (seller signs under penalty of perjury):
   - Line 1, principal residence: owned and lived in as the main home for at least 2 of the 5 years before the sale (IRC 121), with exceptions for a job change, health or unforeseen events. A part-residence, part-business property needs a second Form 593 for the non-residence part.
   - Line 2, last used as the principal residence, whatever the 2-year period. Not a vacation home, second home or rental.
   - Line 3, loss or zero gain: amount realized at or below adjusted basis, shown in Part VI (line 28). Getting no cash, or selling below market value, does not qualify.
   - Line 4, involuntary conversion under IRC 1033, with intent to buy similar property.
   - Line 5, nonrecognition transfer under IRC 351 or 721.
   - Line 6, corporation with a permanent California place of business (organized in California or qualified with the Secretary of State; otherwise a permanently staffed California office after the sale). An S corporation still withholds on its nonresident shareholders.
   - Line 7, title in a California partnership or one qualified to do business in California, or an LLC taxed as a partnership that is not a disregarded single-member LLC. The entity still withholds on its nonresident partners or members.
   - Line 8, tax-exempt entity. Line 9, insurance company, IRA, qualified pension or profit-sharing plan, or charitable remainder trust.
4. **Part IV: partial or no exemption.** Line 10, 1031 exchange: exempt at transfer, but boot over USD 1,500 is withheld on (by the REEP in a simultaneous exchange, by the QI in a deferred one), and a failed exchange is withheld on at 3 1/3% by the intermediary. Line 11, installment sale: see step 7. Line 12, no exemption: full withholding.
5. **Compute the withholding (line 37).** Sales price method: line 13 sales price times ownership percentage times .0333. Or, if the seller elects, the optional gain method: estimated gain (Part VI, line 28) times the rate for the seller's entity type. The estimate may not show a loss when there is a gain.
6. **Who is the seller on the form.** Grantor trust: the grantor's name and SSN or ITIN, not the trust's (a trust that became irrevocable at the grantor's death uses its own name and FEIN). Nongrantor trust: the trust's name and FEIN. Single-member LLC: the single member's name and number, with a note at the bottom of Side 1; an SMLLC taxed as a corporation is treated as a corporation ([2025 Form 593 instructions](https://www.ftb.ca.gov/forms/2025/2025-593-instructions.html); [FTB real estate withholding](https://www.ftb.ca.gov/pay/withholding/real-estate-withholding.html)).
7. **Installment sales.** A sale is an installment sale if at least one payment falls after the year of sale. At closing, withhold 3 1/3% of the down payment and send Form 593, Form 593-V and a copy of the promissory note. The buyer then withholds on the principal part of each later payment (3 1/3% or the seller's alternative percentage) and sends it by the 20th of the month after the payment. The buyer tells the FTB within 60 days if the terms change. To stop it, the seller reports the full gain in the year of sale (Schedule D or D-1) and asks the FTB in writing; the FTB answers within 30 days and withholding continues until then ([2026 Form 593 instructions](https://www.ftb.ca.gov/forms/2026/2026-593-instructions.html)).
8. **File and pay.** Complete the parts that apply and send **Sides 1 to 3 for every transaction**, exempt or not ([FTB Pub. 1016](https://www.ftb.ca.gov/forms/misc/1016.html); [2026 Form 593 instructions](https://www.ftb.ca.gov/forms/2026/2026-593-instructions.html)). The FTB does not process an incomplete form (for example the wrong year's form, a seller name or ID missing from Part II, or a payment with no amount on line 37), and the seller's credit is then not applied ([FTB Tax News, May 2026](https://www.ftb.ca.gov/about-ftb/newsroom/tax-news/2026/05.html)). See Filing and payment below.
9. **The seller's return.** The seller enters Form 593 line 37 on the California return for the year of sale as withholding from Form 592-B or 593 and attaches a copy of Form 593 to the front. Accepted returns: Forms 540, 540NR, 541, 100, 100S, 100W, 109, 565 and 568. After closing, withholding comes back only as a credit on a return, so a return must be filed even if the seller later turns out to have had an exemption.

## Boundary and exception table

| Situation | Treatment | Source |
| --- | --- | --- |
| Seller misses the Form 593 deadline before close | Withholding applies; the seller recovers any excess only by filing a return | [2026 Form 593 instructions](https://www.ftb.ca.gov/forms/2026/2026-593-instructions.html) |
| Cash-poor deferred exchange (QI holds less than the withholding due) | QI's duty limited to available funds; enter what should have been withheld on line 34, certify cash-poor on Side 3, attach support | [2025 Form 593 instructions](https://www.ftb.ca.gov/forms/2025/2025-593-instructions.html) |
| Failed exchange, optional method | Gain times ownership share times the rate, less any withholding already remitted on boot | same |
| Seller's filing status changes after escrow | Call FTB Withholding Services and Compliance (888-792-4900 or 916-845-4900) before filing | [2026 Form 593 instructions](https://www.ftb.ca.gov/forms/2026/2026-593-instructions.html) |
| S corporation or partnership seller with a California place of business | Exempt from Form 593, but the entity's own nonresident-owner withholding applies | same |
| Seller wants a reduced rate other than the optional gain method | Not by Form 589: sellers of real estate use Form 593 only | [2026 Form 589 instructions](https://www.ftb.ca.gov/forms/misc/589-instructions.html) |

**AUDIT FLASH POINT** The seller's certification is signed under penalty of perjury. A principal-residence claim on a rental, or a loss certification built on an inflated basis, carries the greater of USD 1,000 or 20% of the required withholding, on top of the tax itself.

## Worked cases

Both cases are made up for illustration; the figures come from the 2026 Form 593 instructions.

**Case 1, a decision: sales price method or optional gain method?** A nonresident individual sells a California rental she owns outright for USD 800,000, closing on 10 June 2026. Selling costs and adjusted basis leave an estimated gain of USD 150,000. No Part III exemption applies.

- Sales price method: USD 800,000 x 100% x .0333 = USD 26,640.
- Optional gain method: USD 150,000 x 12.3% = USD 18,450.
- The optional method withholds USD 8,190 less now. Both are credits on her 2026 Form 540NR, so the choice affects cash flow, not the final tax. If the estimate is too low and she files no return, the FTB keeps only what was withheld.
- Form 593 and the payment are due by 20 July 2026 (the 20th of the month after the June close).

```oa-check
name: Form 593, sales price method against optional gain method
inputs:
  sales_price: 800000
  ownership: 1.0
  estimated_gain: 150000
steps:
  - sales_price_method: sales_price * ownership * 0.0333
  - gain_method: estimated_gain * 0.123
  - difference: sales_price_method - gain_method
expected:
  sales_price_method: 26640.00
  gain_method: 18450.00
  difference: 8190.00
```

**Case 2: penalties when it goes wrong.** Same sale, but the escrow company notifies the buyer, the buyer closes without withholding (sales price method, required USD 26,640), and the remitter files the seller's Form 593 45 days late.

- Buyer's failure to withhold: greater of USD 500 or 10% x USD 26,640 = USD 2,664.
- Late information return, 31 days to 6 months, per seller: USD 130.

```oa-check
name: Form 593 penalties, 2026 amounts
inputs:
  required_withholding: 26640
  late_tier_31_days_to_6_months: 130
steps:
  - failure_to_withhold: max(500, required_withholding * 0.10)
  - total: failure_to_withhold + late_tier_31_days_to_6_months
expected:
  failure_to_withhold: 2664.00
  total: 2794.00
```

## When to refuse or refer

- A foreign seller: federal FIRPTA withholding applies as well; refer it.
- A seller who wants the FTB to waive or reduce withholding outside the Form 593 methods, or who has received an FTB notice: refer to a California practitioner.
- Mixed-use property, partial principal residence, or a sale of a partnership interest rather than the real estate: refer the allocation.
- Whether a 1031 exchange qualifies: `us-section-1031-like-kind-exchange`.

## Filing and payment

- **Form 593:** to the FTB by the **20th day of the calendar month after the month escrow closes**, Sides 1 to 3, for every transaction. The seller's copy is due on the same schedule ([2026 Form 593 instructions](https://www.ftb.ca.gov/forms/2026/2026-593-instructions.html)).
- **Payment:** the original Form 593, Form 593-V and the check within 20 days after the end of the month the transaction closed. Write "2026 Form 593-V" on the check, in US dollars drawn on a US institution; the remitter details on Form 593-V must match Form 593 Part I ([2026 Form 593-V](https://www.ftb.ca.gov/forms/2026/2026-593-v.pdf)).
- **Installments:** by the 20th of the month after each payment month.
- **Electronic filing:** through SWIFT (FTB Pub. 923, record layout in FTB Pub. 1023R); the REEP still gives the seller a copy. With an installment sale, mail the promissory note copy with the down payment only.
- **Records:** keep a copy for at least 5 years. Interest runs on late payments from the due date.

## Completion checklist

- [ ] Sales price, ownership percentage and seller type confirmed.
- [ ] No-withholding cases and Part III exemptions tested before close; signed Form 593 in hand.
- [ ] Line 37 computed by the chosen method; Part VI completed for the optional gain method.
- [ ] Trust, SMLLC or grantor details entered for the right taxpayer.
- [ ] Form 593 (Sides 1 to 3) and payment sent by the 20th of the next month; seller's copy given.
- [ ] Seller told to claim line 37 on the 2026 return.

## Sources

| Source | URL | Read on |
| --- | --- | --- |
| FTB, 2026 Instructions for Form 593. Read for What's New (penalty increase from 2026), the no-withholding cases, Part III lines 1 to 9, Part IV lines 10 to 12, the sales price and alternative rates, installment sales, due dates, records, interest, the penalties section (R&TC 19183 and related) and the seller's credit. | https://www.ftb.ca.gov/forms/2026/2026-593-instructions.html | 2026-11-21 |
| FTB, 2025 Instructions for Form 593. Read for the cash-poor exchange rule (line 34), the failed-exchange optional method, and the trust and SMLLC entries. | https://www.ftb.ca.gov/forms/2025/2025-593-instructions.html | 2026-11-21 |
| FTB, 2026 Form 593-V and instructions. Read for the payment voucher, the check notation and the matching rule. | https://www.ftb.ca.gov/forms/2026/2026-593-v.pdf | 2026-11-21 |
| FTB Publication 1016, Real Estate Withholding Guidelines (rev. 02/2026). Read for who is subject to withholding, the form changes (submitted for every transaction type), and parcels in one escrow added together for the USD 100,000 test. | https://www.ftb.ca.gov/forms/misc/1016.html | 2026-11-21 |
| FTB, Real estate withholding. Read for the single Form 593 since 2020 and the trust rules. | https://www.ftb.ca.gov/pay/withholding/real-estate-withholding.html | 2026-11-21 |
| FTB Tax News, May 2026. Read for the Form 593 processing item: incomplete forms are not processed and the credit is not applied. | https://www.ftb.ca.gov/about-ftb/newsroom/tax-news/2026/05.html | 2026-11-21 |
| FTB, 2026 Instructions for Form 589. Read for the rule that real estate sellers use Form 593, not Form 589. | https://www.ftb.ca.gov/forms/misc/589-instructions.html | 2026-11-21 |

Not yet confirmed: the text of R&TC 18662 and 19183 (leginfo.legislature.ca.gov refused our reader; cited as the FTB instructions name them); the pre-2026 penalty amounts the increase replaced, except as the 2025 instructions print them (USD 40, 80 and 130 tiers, USD 130 per copy and USD 330 for intentional disregard), and whether the 2026 amounts apply by closing date or by the remitter's taxable year; whether the 2026 instructions repeat the cash-poor exchange rule word for word.

> **Disclaimer.** This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a CPA, EA, tax attorney, or equivalent licensed practitioner in your jurisdiction) before filing or acting upon. The most up-to-date version of this skill is maintained at [openaccountants.com](https://www.openaccountants.com).
