---
name: us-installment-sale-6252
description: Compute US federal installment-sale income for tax year 2026 on Form 6252. Covers who must use the installment method, the election out, gross profit and contract price, the gross profit percentage, depreciation recapture taxed in the year of sale, related-party resales, the pledge rule, and interest on deferred tax when the sales price is over USD 150,000 and nondealer obligations outstanding at year end are more than USD 5,000,000. For individuals and for other filers who attach Form 6252. The rate on the gain is in us-capital-gains. Trigger on "installment sale", "Form 6252", "installment method", "section 453", "seller financing", "depreciation recapture installment", "related party resale".
version: "1.0"
jurisdiction: US
category: federal
tax_year: 2026
last_updated: 2026-11-13
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
tier: 2
domain: income-tax
type: computation
---

# US installment sale income, Form 6252, tax year 2026

> **Source-cited draft.** Built from IRS Topic 705, Publication 537, the 2025 Form 6252 (the latest form posted when read) and 26 U.S.C. 453, read on 2026-11-13. No accountant has reviewed it. All outputs must be reviewed by a qualified tax professional before filing.

**Answer first.** An installment sale is a sale where at least one payment is received after the tax year of the sale. Gain is reported as payments come in: each payment, after interest, is multiplied by the gross profit percentage (gross profit divided by the contract price). Depreciation recapture under sections 1245 and 1250 is ordinary income in the year of sale, even if no payment arrives that year. The taxpayer can elect out by the return due date, including extensions, and report the whole gain in the year of sale. Losses, inventory, and stock or securities traded on an established market cannot use the method.

## Scope and who this is for

In scope: a 2026 disposition of property by an individual, a trust or estate, a partnership, or a C corporation, where at least one payment falls after the tax year of sale, and the computation of installment income on Form 6252. That includes the year-of-sale recapture, a later year's payment, a related buyer's resale, and the section 453A interest charge when it applies.

Out of scope, and where it goes:

| Topic | Skill |
| --- | --- |
| The rate on long-term or short-term capital gain, and the net investment income tax | `us-capital-gains` |
| Like-kind exchange of real property | `us-section-1031-like-kind-exchange` |
| A nonresident's sale of US real property and withholding | `us-nonresident-cgt` |
| Dealer inventory and sales of stock or securities on an established market | report the whole result in the year of sale; this skill does not spread it |
| Unstated interest and original issue discount when the contract does not state adequate interest | figure interest first under Publication 537, then run this skill on the principal only |

## Ask the client first

1. **What was sold, and when.** Date acquired, date sold, and whether the asset is a capital asset, trade or business property, the seller's main home, or farm property.
2. **The price and the debt.** Selling price of principal only (money, other property, and any mortgage the buyer assumes or takes subject to). Selling expenses. Any mortgage or other debt the buyer assumed. Do not include stated interest.
3. **Basis and depreciation.** Cost or other basis, depreciation allowed or allowable, and the section 1245 or 1250 recapture from Form 4797, Part III, as if every payment were received in the year of sale.
4. **The payment schedule.** Amount of principal received in 2026 and expected later. Whether the buyer's note is payable on demand or readily tradable. Whether the seller pledged the note to secure other debt.
5. **Who the buyer is.** Related to the seller or not. If related, whether the buyer has resold, and whether the property is depreciable in the buyer's hands.
6. **The election.** Has the seller already elected out on a return for the year of sale, or do they want every dollar of gain in that year?

## The method, step by step

### Rates, bands and thresholds

These amounts are written into the statute or the form. They are not inflation-indexed.

| Item | Amount | Who it applies to | Source |
| --- | --- | --- | --- |
| Installment method | Required when at least one payment is received after the tax year of sale, unless the taxpayer elects out by the return due date including extensions | Any seller with a gain. Not for a loss, inventory, or stock or securities traded on an established securities market | [Topic 705](https://www.irs.gov/taxtopics/tc705) |
| Gross profit percentage | Gross profit divided by the contract price, entered as a decimal of at least 4 digits | Each payment after interest is removed | [2025 Form 6252, line 19](https://www.irs.gov/pub/irs-prior/f6252--2025.pdf) |
| Depreciation recapture | The full section 1245 or 1250 amount is ordinary income in the year of sale | Depreciable property. The rest of the gain uses the installment method | [26 U.S.C. 453(i)](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap1-subchapE-partII-subpartB-sec453.htm) |
| Related-party resale window | 2 years after the first sale, and no time limit for marketable securities | A related buyer who disposes of the property before the seller is paid in full | [26 U.S.C. 453(e)(2)](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap1-subchapE-partII-subpartB-sec453.htm) |
| Pledge rule | Applies when the sales price is over USD 150,000 | The net proceeds of debt secured by the installment obligation are treated as a payment. Not for an individual's personal-use property, farm property, or qualifying timeshares and residential lots | [2025 Form 6252 instructions](https://www.irs.gov/pub/irs-prior/f6252--2025.pdf) |
| Interest on deferred tax | Sales price over USD 150,000, and the total of nondealer installment obligations that arose during the tax year and are still outstanding at year end is more than USD 5,000,000 | Interest then continues while those obligations stay outstanding. Not for farm property or an individual's personal-use property | [Publication 537](https://www.irs.gov/publications/p537) |
| Late election out | An amended return no later than 6 months after the due date, excluding extensions, if the original return was filed on time | Write "Filed pursuant to section 301.9100-2" at the top. The election is otherwise only with IRS consent | [2025 Form 6252 instructions](https://www.irs.gov/pub/irs-prior/f6252--2025.pdf) |

### Compute the year of sale

Use one Form 6252 for each sale. The line numbers below are the 2025 form, the latest posted when this was written. Interest, stated or unstated, never goes on Form 6252. Report interest as ordinary income. Source: [2025 Form 6252](https://www.irs.gov/pub/irs-prior/f6252--2025.pdf) and [Publication 537, Worksheet A](https://www.irs.gov/publications/p537).

1. **Selling price (line 5).** Money to be received, the face of the installment note, the fair market value of other property or services, and any existing mortgage the buyer assumes or takes subject to. Do not include interest or original issue discount. A new mortgage the buyer gets from a bank is not on line 6.
2. **Adjusted basis (lines 8 to 10).** Cost or other basis, minus depreciation and amortization allowed or allowable.
3. **Selling expenses (line 11).** Commissions, legal fees, and other costs of the sale. The buyer-paid expenses are already in the selling price.
4. **Recapture (line 12).** Ordinary income under section 1245 or 1250 (including section 179) as if every payment were received in the year of sale. Figure it on Form 4797, Part III. It is taxed in full in the year of sale, on Form 4797, even when the buyer pays nothing that year. It is also added into the installment-sale basis, so it is not taxed again as the payments arrive. Source: [26 U.S.C. 453(i)](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap1-subchapE-partII-subpartB-sec453.htm).
5. **Gross profit (line 16).** Selling price minus adjusted basis, selling expenses, and recapture. Subtract any main-home exclusion (line 15) before this. If gross profit is zero or less, do not file Form 6252. Report the sale on Form 4797, Form 8949, or Schedule D.
6. **Contract price (line 18).** Selling price, minus mortgages and other debts the buyer assumed or took subject to, plus the amount by which those assumed debts exceed the installment-sale basis (basis plus selling expenses plus recapture). With no assumed debt, the contract price equals the selling price.
7. **Gross profit percentage (line 19).** Gross profit divided by the contract price. Keep at least four decimal places. Use the year-of-sale percentage in every later year, unless the selling price is later reduced.
8. **Payments this year (lines 20 to 22).** In the year of sale, start with the excess of assumed debt over installment-sale basis (line 20). Add money and the fair market value of property received this year. A buyer's note is not a payment unless it is payable on demand or readily tradable. Source: [26 U.S.C. 453(f)(3) and (4)](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap1-subchapE-partII-subpartB-sec453.htm).
9. **Installment income (line 24).** Payments in step 8 times the gross profit percentage. In the year of sale, also report the recapture as ordinary income. Carry the rest of line 24 (line 26) to Schedule D or Form 4797. The character (long-term, short-term, unrecaptured section 1250) follows the asset. The rate is in `us-capital-gains`.

### Later years, a resale, and the election out

File Form 6252 again in each later year through the year of the final payment or the disposition of the obligation, even in a year with no payment. Use the original gross profit percentage. Payments include a related party's resale amount from Part III and pledge-rule proceeds from an earlier year, on the prior-payments line rather than as a new payment.

**Electing out.** Report the whole selling price, and the whole gain, on a timely Form 4797, Form 8949, or Schedule D for the year of sale. Do not file Form 6252. The election can be revoked only with IRS consent, except for the 6-month automatic window above. Source: [Topic 705](https://www.irs.gov/taxtopics/tc705).

**Related buyer, second disposition (Part III).** If the buyer is related under section 453(f)(1) (section 318 attribution, other than option attribution, or a section 267(b) relationship) and disposes of the property before the seller is paid in full, the seller treats the buyer's amount realized (or fair market value, if it is not a sale) as received at that time. The amount is capped at the seller's contract price, minus payments already treated as received. The 2-year limit does not apply to marketable securities. It does not apply to a second disposition more than 2 years later (other than marketable securities), a sale of stock back to the issuing corporation, an involuntary conversion threatened only after the first sale, a transfer after the seller or the buyer dies, or a case where tax avoidance was not a principal purpose of either disposition. Source: [26 U.S.C. 453(e)](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap1-subchapE-partII-subpartB-sec453.htm) and [2025 Form 6252, lines 29 to 37](https://www.irs.gov/pub/irs-prior/f6252--2025.pdf).

**Depreciable property sold to a related person (section 453(g)).** The installment method does not apply. All payments are treated as received in the year of sale. "Related" here follows section 1239(b), and also includes certain partnerships under section 707(b)(1)(B). The seller can use the installment method only by showing the IRS that tax avoidance was not a principal purpose. Source: [26 U.S.C. 453(g)](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap1-subchapE-partII-subpartB-sec453.htm).

**Dealers.** A dealer disposition of personal property of a kind the seller regularly sells on the installment plan, or of real property held for sale to customers, is not an installment sale. Two exceptions stay on the method: property used or produced in farming, and an election for certain timeshares and residential lots sold to individuals. Source: [26 U.S.C. 453(b) and (l)](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap1-subchapE-partII-subpartB-sec453.htm).

**Disposing of the obligation.** If the note is sold, gifted, cancelled, or otherwise disposed of, gain or loss is the difference between the basis of the obligation and the amount realized (or fair market value, if it is not a sale). The character follows the property sold. Source: [26 U.S.C. 453B](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap1-subchapE-partII-subpartB-sec453B.htm).

**Section 453A interest.** This is not figured on Form 6252. Publication 537 multiplies the unrecognized gain at year end by the seller's maximum tax rate for that gain, then by the applicable percentage (face amount of the obligations that count, minus USD 5,000,000, divided by that face amount), then by the section 6621(a)(2) underpayment rate for the month in which the tax year ends. The 2026 year-end rate is not used in the examples below.

### Boundary and exception table

| Situation | Result |
| --- | --- |
| The sale produces a loss | Do not use Form 6252. Report the sale in the year of sale |
| Stock or securities traded on an established market | Every payment is treated as received in the year of sale |
| Buyer's ordinary installment note | Not a payment. A demand note or a readily tradable note is a payment |
| Assumed mortgage does not exceed installment-sale basis | Not a payment. The excess over that basis is a payment in the year of sale |
| Seller pledges the note, sales price over USD 150,000 | Net proceeds of the secured debt are a payment, capped at the contract price still unpaid |
| Selling price later reduced, debt not cancelled | Refigure the gross profit percentage and apply it to later payments. Cancelling the debt can be a disposition of the obligation |
| Several assets sold for one price | Allocate the price. Recapture property is pulled out before the installment percentage is applied |
| Contingent price with no stated maximum | Not a fixed contract price. Use the basis-recovery rule in Treas. Reg. 15a.453-1(c). Flag it |

## Worked cases

**Case 1, a decision: elect out, or use the installment method?** In 2026 a single filer sells unimproved land held as a long-term capital asset. Principal selling price USD 200,000. Adjusted basis USD 80,000. No selling expenses, no mortgage, no depreciation. The contract states adequate interest, which is kept off Form 6252 and taxed as ordinary interest when received. Principal is USD 50,000 in 2026 and USD 150,000 in 2027.

Gross profit is USD 200,000 minus USD 80,000 = USD 120,000. Contract price is USD 200,000. Gross profit percentage is 0.6000. Installment income in 2026 is USD 50,000 times 0.6000 = USD 30,000. The other USD 90,000 of gain waits for 2027.

Electing out puts all USD 120,000 of gain on the 2026 return. On these facts the gain is taxed at 15 percent (the rate that applies is computed in `us-capital-gains`, not here). Tax on the 2026 gain is USD 4,500 if the seller stays on the installment method, and USD 18,000 if the seller elects out. The same 15 percent rate in 2027 makes the total tax the same; the election decides whether USD 13,500 of that tax is paid with the 2026 return or with the 2027 return. Elect out only if the seller wants the gain in 2026 (for example, a loss that can absorb it). Otherwise stay on the installment method.

```oa-check
name: Elect out or installment, land sale (2026)
inputs:
  selling_price: 200000
  adjusted_basis: 80000
  payment_2026: 50000
  rate: 0.15
steps:
  - gross_profit: selling_price - adjusted_basis
  - gp_pct: gross_profit / selling_price
  - installment_gain_2026: payment_2026 * gp_pct
  - elect_out_gain: gross_profit
  - tax_installment_2026: installment_gain_2026 * rate
  - tax_elect_out: elect_out_gain * rate
  - tax_deferred: tax_elect_out - tax_installment_2026
expected:
  gross_profit: 120000.00
  gp_pct: 0.60
  installment_gain_2026: 30000.00
  tax_installment_2026: 4500.00
  tax_elect_out: 18000.00
  tax_deferred: 13500.00
```

**Case 2, depreciation recapture in the year of sale.** In 2026 a sole proprietor sells a machine. Cost USD 70,000. Depreciation allowed USD 30,000, so adjusted basis is USD 40,000. Selling price USD 100,000, no selling expenses, no mortgage. Section 1245 recapture is the depreciation, USD 30,000, because the realized gain of USD 60,000 is larger. The buyer pays USD 20,000 of principal in 2026 and the rest later. Interest is stated and is not on Form 6252.

Installment-sale basis is USD 40,000 plus the USD 30,000 of recapture = USD 70,000. Gross profit on the installment method is USD 100,000 minus USD 70,000 = USD 30,000. Contract price is USD 100,000. Gross profit percentage is 0.3000. Installment income in 2026 is USD 20,000 times 0.3000 = USD 6,000. The USD 30,000 of recapture is ordinary income in 2026 on Form 4797 even though most of the price is unpaid. Income from the sale in 2026 is USD 36,000. The remaining USD 24,000 of installment gain is recognized as later principal is collected.

```oa-check
name: Recapture in the year of sale (2026)
inputs:
  selling_price: 100000
  cost: 70000
  depreciation: 30000
  recapture: 30000
  payment: 20000
steps:
  - adjusted_basis: cost - depreciation
  - installment_basis: adjusted_basis + recapture
  - gross_profit: selling_price - installment_basis
  - gp_pct: gross_profit / selling_price
  - installment_income: payment * gp_pct
  - year_of_sale_income: recapture + installment_income
expected:
  adjusted_basis: 40000.00
  installment_basis: 70000.00
  gross_profit: 30000.00
  gp_pct: 0.30
  installment_income: 6000.00
  year_of_sale_income: 36000.00
```

## When to refuse or refer

| Code | Situation | Action |
| --- | --- | --- |
| R-6252-LOSS | Gross profit is zero or less | Do not file Form 6252. Report the sale in the year of sale |
| R-6252-DEALER | Inventory, or real property held for sale to customers | The installment method does not apply, unless the farming or timeshare and residential-lot exception is met |
| R-6252-MARKET | Stock or securities traded on an established market | Treat every payment as received in the year of sale |
| R-6252-453G | Depreciable property sold to a related person | The installment method does not apply unless the seller can show tax avoidance was not a principal purpose |
| R-6252-CONTINGENT | Selling price cannot be determined and there is no stated maximum | Use Treas. Reg. 15a.453-1(c). Do not invent a contract price |
| R-6252-453A | Sales price over USD 150,000 and nondealer obligations from the year still outstanding at year end are more than USD 5,000,000 | Compute the section 453A interest from Publication 537. The December 2026 underpayment rate is not in this skill |
| R-6252-HOME | The property is the seller's main home | Apply the exclusion before gross profit. The exclusion rules are not in this skill |

## Filing and payment

Form 6252 is attached to the income tax return for the year of sale and for each later year through the final payment. Individuals use Form 1040 or 1040-SR. The 2026 Form 1040 is due 15 April 2027; an extension extends filing, not payment. A corporation attaches Form 6252 to its income tax return. Electing out means the gain is on Form 4797, Form 8949, or Schedule D instead, on a return filed by the due date including extensions.

A farming loss that is carried back is not this form. Interest on an installment sale is ordinary income on the interest line, not on Form 6252. Section 453A interest is an additional amount figured from Publication 537, not a line on Form 6252.

The return is filed under the filer's usual account (individuals: IRS individual online account or the paper address in the form instructions). What happens next is the ordinary assessment of the return. A related-party second disposition can keep the assessment period open until 2 years after the seller gives the IRS the notice the regulations require.

## Completion checklist

- One Form 6252 per sale, and the same gross profit percentage in later years.
- Interest removed before the payment is entered.
- Recapture on Form 4797 in the year of sale, and included in installment-sale basis so it is not taxed twice.
- Assumed debt tested against installment-sale basis.
- Related buyer: Part III for the year of sale and the next 2 years, unless the final payment arrived earlier.
- Election out made on a timely return, or the 6-month amended-return window used and labelled.
- Section 453A tested when the sales price is over USD 150,000.

## Sources

| Source | URL | Read on |
| --- | --- | --- |
| IRS Topic 705, Installment sales. Read for the definition, the election out, what the selling price includes, Form 6252, and interest as ordinary income. | https://www.irs.gov/taxtopics/tc705 | 2026-11-13 |
| Publication 537, Installment sales. Read for Worksheet A (basis, recapture, gross profit percentage), the contract price, depreciation recapture in the year of sale, related-party resales, and the section 453A interest computation (sales price over $150,000 and obligations over $5,000,000). | https://www.irs.gov/publications/p537 | 2026-11-13 |
| 2025 Form 6252 and its instructions, the latest form posted. Read for lines 5 to 26, Part III lines 27 to 37, the pledge rule, the $150,000 and $5,000,000 interest thresholds, the 6-month election under section 301.9100-2, and dealer exceptions. | https://www.irs.gov/pub/irs-prior/f6252--2025.pdf | 2026-11-13 |
| 26 U.S.C. 453 (govinfo, United States Code 2024). Read for subsections (a) through (c), (e) related-party resale, (f) payment and related person, (g) depreciable property, (i) recapture, (k) marketable securities, and (l) dealers. | https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap1-subchapE-partII-subpartB-sec453.htm | 2026-11-13 |
| 26 U.S.C. 453B (govinfo, United States Code 2024). Read for gain or loss on disposition of an installment obligation. | https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap1-subchapE-partII-subpartB-sec453B.htm | 2026-11-13 |

Not yet confirmed: the 2026 Form 6252 had not been posted, so the line numbers are the 2025 form's; the section 6621(a)(2) underpayment rate for the month a 2026 tax year ends, which section 453A uses; any 2026 change to the USD 150,000 or USD 5,000,000 thresholds (both are stated as fixed amounts in the 2025 form and Publication 537).
