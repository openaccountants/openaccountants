---
name: nz-gst-return
description: Use this skill whenever asked about New Zealand GST returns for self-employed individuals. Trigger on phrases like "GST return", "GST101A", "GST rate NZ", "input tax", "output tax", "zero-rated", "GST registration", "taxable supply", "IRD GST", "myIR GST", or any question about GST filing for sole traders in New Zealand. Covers the 15% standard rate, zero-rated and exempt supplies, $60K registration threshold, invoice and payments basis, and GST101A return preparation. ALWAYS read this skill before touching any NZ GST work.
version: 2.0
jurisdiction: NZ
tax_year: 2026
last_updated: 2026-09-22
review_status: pending_review
drafted_by: OpenAccountants
approved_by: pending
depends_on:
  - vat-workflow-base
category: international
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# New Zealand GST Return: Preparing and Filing the GST101A

Figures are for tax year 2026. In New Zealand that is the income year from 1 April 2026 to 31 March 2027, which Inland Revenue calls the 2027 income year. GST has no tax year: it runs by taxable period, and this Guide covers GST taxable periods ending from 30 April 2026 to 31 March 2027. The rules below stand until changed and were current on 22 September 2026. The GST101A form is dated April 2023 (still IRD's current download); IR375 is dated March 2026.

## Section 1: Quick Reference

**Quick Reference**

| Field | Value |
| --- | --- |
| Country | New Zealand |
| Tax | Goods and Services Tax (GST) at the standard rate in the Rate Table below |
| Currency | NZD only |
| Tax year basis | Balance date (typically 31 March). GST taxable periods must align with it |
| Primary legislation | Goods and Services Tax Act 1985 (GSTA 1985) |
| Tax authority | Inland Revenue (IR / Te Tari Taake) |
| Filing portal | myIR, accounting software that files directly, or the paper GST101A |
| Filing deadline | 28th of the month after the period ends, with two exceptions (see 5.3) |
| Validated by | Pending: needs a New Zealand chartered accountant |

### Rate Table

**Rate Table**

| Rate | Application | Note |
| --- | --- | --- |
| Source | all figures below | https://www.ird.govt.nz/-/media/project/ir/home/documents/forms-and-guides/ir300---ir399/ir375/ir375.pdf |
| 15% | Standard rate on all taxable supplies | IR295 (April 2026): "The current rate is 15%." |
| 0% | Zero-rated supplies: exported goods, sales of going concerns, sale of land (where certain criteria are met) | IR375: "GST is charged at 0%." |
| Exempt | Financial services (such as interest), supplying a residential dwelling, donated goods and services sold by not-for-profit organisations | IR375: "not included in your GST return" |

### Tax Fraction

- **Tax fraction for GST-inclusive amounts**: 3/23. It is how Box 8 and Box 12 of the GST101A work. See [IR375](https://www.ird.govt.nz/-/media/project/ir/home/documents/forms-and-guides/ir300---ir399/ir375/ir375.pdf): "3/23rds of the GST inclusive amount".

### Key Thresholds

**Key Thresholds: registration**

| Item | Amount | Note |
| --- | --- | --- |
| Source | all figures below | https://www.ird.govt.nz/gst/registering-for-gst |
| Compulsory GST registration | NZD 60,000 | Last 12 months or expected next 12 months. Web page: "at least $60,000"; IR375: "over $60,000" |

**Key Thresholds: accounting basis and filing frequency**

| Item | Amount | Note |
| --- | --- | --- |
| Source | all figures below | https://www.ird.govt.nz/gst/registering-for-gst/which-gst-accounting-basis-and-filing-frequency-should-i-use |
| Payments basis eligibility | NZD 2 million | Last 12 months, or likely in any 12-month period |
| Six-monthly filing eligibility | NZD 500,000 | Under it in any 12-month period |
| Monthly filing compulsory | NZD 24 million | Over it in any 12-month period |

**Key Thresholds: taxable supply information (replaced tax invoices)**

| Item | Amount | Note |
| --- | --- | --- |
| Source | all figures below | https://www.ird.govt.nz/-/media/project/ir/home/documents/forms-and-guides/ir300---ir399/ir375/ir375.pdf |
| Seller need not give taxable supply information (both parties still keep records) | NZD 200 | "If the sale is $200 or less (including GST)" |
| Middle band upper limit | NZD 1,000 | "More than $200 and up to $1,000"; above NZD 1,000 full buyer details are required |

### Conservative Defaults

**Conservative Defaults**

| Ambiguity | Default |
| --- | --- |
| GST registration status unknown | STOP: do not compute |
| Accounting basis unknown | Invoice basis (IRD's default if none was chosen at registration) |
| Supply classification unknown | Standard-rated |
| Private use proportion unknown | No GST recovery on that item |
| Going concern status unknown | Not a going concern (charge GST) |

## Section 2: Required Inputs and Refusal Catalogue

### Required Inputs

**Minimum viable:** Bank statement for the GST period in CSV, PDF, or pasted text, plus confirmation of GST registration status, accounting basis and taxable period.

**Recommended:** Sales records, taxable supply information for every claim, GST number, Customs documents.

**Ideal:** Invoice register, prior period return, IR372 workings.

### Refusal Catalogue

- **R-NZ-1: Not GST-registered.** If turnover is below the registration threshold in Key Thresholds and the client is not voluntarily registered, no GST return is required. Stop.
- **R-NZ-2: Companies and partnerships.** This Guide covers individual self-employed persons only. Company and partnership GST returns may have additional requirements.
- **R-NZ-3: Financial services (complex).** Complex financial services GST treatment requires specialist review. Escalate.
- **R-NZ-4: Cross-border digital services (complex).** Non-resident digital services GST has specific registration and collection rules. Escalate if amounts are material.

## Section 3: Transaction Pattern Library

### 3.1 Income Patterns (Credits)

**Income Patterns (Credits)**

| Pattern | Tax Line | Treatment | Notes |
| --- | --- | --- | --- |
| DIRECT CREDIT [client] / DC [client] | Taxable supply | GST-inclusive revenue, Box 5 | Standard client payment |
| EFTPOS SETTLEMENT / EFTPOS CREDIT | Taxable supply | Revenue, Box 5 | Card terminal settlement |
| INTERNET BANKING CREDIT [client] | Taxable supply | Revenue, Box 5 | Online bank transfer |
| STRIPE NZ / STRIPE PAYOUT | Taxable supply | Revenue (net of fees) | Gross up fees |
| SHOPIFY PAYOUT / SHOPIFY SETTLEMENT | Taxable supply | Revenue | E-commerce platform settlement |
| XERO INVOICE PAYMENT | Taxable supply | Revenue | Xero-linked payment |
| INTEREST / INT EARNED [bank] | Exempt | NOT in the GST return | Bank interest: exempt financial service |
| DIVIDEND [company] | Exempt | NOT in the GST return | Dividend |
| IRD REFUND / TAX REFUND | EXCLUDE | Not income | Tax refund |
| LOAN DRAWDOWN | EXCLUDE | Not income | Loan proceeds |

### 3.2 Expense Patterns (Debits)

**Expense Patterns (Debits)**

| Pattern | Expense Category | Treatment | Notes |
| --- | --- | --- | --- |
| SPARK / VODAFONE / 2DEGREES | Communications | Business portion claimable | Mixed use: apportion |
| VECTOR / MERCURY / GENESIS / CONTACT ENERGY | Utilities | Business portion claimable | Home office: apportion |
| COUNTDOWN / PAK'N SAVE / NEW WORLD | NOT business | Private | Unless business entertainment (see 5.4) |
| BUNNINGS / Mitre 10 | Office supplies | Claimable if business | Keep receipts |
| GOOGLE ADS / META / LINKEDIN | Advertising | Claimable | Check the supplier charged NZ GST |
| ADOBE / MICROSOFT / XERO / SLACK | Software | Claimable | Check the supplier charged NZ GST |
| AIR NEW ZEALAND / JETSTAR | Travel | Claimable if business | Keep itinerary |
| UBER NZ / TAXI | Travel | Claimable if business | Not commuting |
| ACC LEVY | EXCLUDE | Government levy | Not in the GST return |
| IRD INCOME TAX / IRD PAYE | EXCLUDE | Tax payment | Not in the GST return |
| BANK FEE / ANZ FEE / ASB FEE / BNZ FEE / WESTPAC FEE | Exempt | No GST on bank fees | Financial service exempt |
| CUSTOMS / IMPORT GST | Imports | NOT in Box 11 | Claim from the Customs document, see 5.1 |
| PERSONAL TRANSFER / OWN ACCOUNT | EXCLUDE | Drawings | Not business |

### 3.3 Zero-Rated Supply Indicators

**Zero-Rated Supply Indicators**

| Pattern | Treatment | Notes |
| --- | --- | --- |
| EXPORT / INTERNATIONAL FREIGHT | Zero-rated output | Goods exported from NZ. In Box 5 and again in Box 6 |
| GOING CONCERN SALE | Zero-rated output | IR375: the whole or a stand-alone part of a taxable activity, "from one registered person to another", agreed in writing by both parties |
| LAND SALE (REGISTERED BUYER) | Zero-rated where certain criteria are met | Refer: specialist area |

## Section 4: Worked Examples

Examples 3 and 4 use Inland Revenue's own figures from IR375.

### Example 1: Standard Two-Monthly Return

**Input:** Two-monthly filer, 31 March balance date, period February to March. All standard-rated. No adjustments.

**Reasoning:** Box 6 is nil, so Box 7 equals Box 5 and Box 8 is Box 7 x 3/23. Box 12 is Box 11 x 3/23. Box 15 is the difference between Box 10 and Box 14.

**Classification:** Box 10 larger than Box 14: GST to pay. The period ends 31 March, so the return and payment are due 7 May, not 28 April.

### Example 2: Exporter in Refund Position

**Input:** IR375's Joe exports apples. Assume all this period's sales are exports.

**Reasoning:** The export sales go in Box 5 and again in Box 6, so Box 7 and Box 8 are nil. GST on his fertilisers and sprays goes through Box 11 and Box 12.

**Classification:** Box 14 larger than Box 10: GST refund. IRD pays refunds "within 15 working days" of a filed return ([File your GST return](https://www.ird.govt.nz/gst/filing-and-paying-gst-and-refunds/filing-gst/file-your-gst-return)).

### Example 3: Entertainment Expense

**Input:** IR375's business lunch for clients.

| Step | Amount | Note |
| --- | --- | --- |
| Source | all figures below | https://www.ird.govt.nz/-/media/project/ir/home/documents/forms-and-guides/ir300---ir399/ir375/ir375.pdf |
| Lunch cost including GST | NZD 230 | "The lunch cost $230 including GST" |
| GST in the cost (x 3/23) | NZD 30 | "$230 × 3 ÷ 23 = $30" |
| GST-exclusive cost | NZD 200 | "$230 − $30 = $200" |
| Not deductible for income tax | NZD 100 | "$200 × 50% = $100" |
| Rate applied to the non-deductible amount | 15% | "Multiply the non-deductible amount by 15% (or 0.15)" |
| GST adjustment | NZD 15.00 | "$100 × 15% = $15.00" |

**Reasoning:** The whole cost is claimed in Box 11 during the year. Once a year the adjustment goes on the IR372 and into Box 9, in the return set out in 5.4.

**Classification:** Box 9 debit adjustment. Do NOT halve the claim each period.

### Example 4: Private Use Apportionment

**Input:** IR375's Amy buys a car mainly for private use.

| Item | Amount | Note |
| --- | --- | --- |
| Source | all figures below | https://www.ird.govt.nz/-/media/project/ir/home/documents/forms-and-guides/ir300---ir399/ir375/ir375.pdf |
| Car price excluding GST | NZD 9,000 | "She buys a car for $9,000 plus GST of $1,350" |
| GST charged | NZD 1,350 | same quote |
| Business use estimate | 20% | "Using the apportionment method, Amy can claim 20%" |
| Line for the principal purpose method | NZD 10,000 | Goods and services costing NZD 10,000 or less (GST-exclusive) |

**Reasoning:** Up to the line in the table (GST-exclusive), the client chooses the principal purpose method (Amy claims nothing: the car is mainly private) or the apportionment method (she claims the business share of the GST, and must use that method for all such goods for at least 24 months).

**Classification:** Claim the business share of the GST only. Flag for reviewer on apportionment basis.

## Section 5: Tier 1 Rules (When Data Is Clear)

### 5.1 GST101A Return Line-by-Line

Taken from the GST101A form and IR375. The GST103B (GST and provisional tax) has the same Boxes 1 to 15; its page 2 is provisional tax.

**GST101A Return Line-by-Line**

| Box | Form label | How to populate |
| --- | --- | --- |
| Source | all boxes below | https://www.ird.govt.nz/-/media/project/ir/home/documents/forms-and-guides/gst100---gst199/gst101a/gst101a-2023.pdf |
| 1 to 4 | Registration no., period covered, postal address, daytime phone (the due date is printed but has no box number) | Pre-printed on paper; print Box 3 or 4 only if the details shown are wrong |
| 5 | Total sales and income for the period (including GST and any zero-rated supplies) | All taxable sales including GST, plus zero-rated sales. Exempt supplies are NOT included |
| 6 | Zero-rated supplies included in Box 5 | Exports and other 0% supplies |
| 7 | Subtract Box 6 from Box 5 and enter the difference here | Box 5 minus Box 6 |
| 8 | Multiply the amount in Box 7 by three (3) and then divide by twenty-three (23) | Box 7 x 3/23 |
| 9 | Adjustments from your calculation sheet | Debit adjustments from the IR372 (for example entertainment, private use, bad debts recovered, insurance payments received) |
| 10 | Add Box 8 and Box 9. This is your total GST collected on sales and income | Box 8 + Box 9 |
| 11 | Total purchases and expenses (including GST), excluding any imported goods | Only with taxable supply information held. No exempt, private or imported items |
| 12 | Multiply the amount in Box 11 by three (3) and then divide by twenty-three (23) | Box 11 x 3/23 |
| 13 | Credit adjustments from your calculation sheet | Credit adjustments from the IR372 (for example bad debts written off, the GST shown on a Customs document for imported goods, change-in-use increases) |
| 14 | Add Box 12 and Box 13. This is your total GST credit for purchases and expenses | Box 12 + Box 13 |
| 15 | Print the difference between Box 10 and Box 14 here | Box 14 larger: refund. Box 10 larger: GST to pay. Equal: nil return, still filed |


In myIR the same figures go under sales and income, purchases and expenses, and credit and debit adjustments ([File your GST return](https://www.ird.govt.nz/gst/filing-and-paying-gst-and-refunds/filing-gst/file-your-gst-return)).

Imported goods: "Do not include imported goods under purchases on your GST return." Instead "claim the GST content shown on the Customs document as a credit adjustment or in Box 13" (IR375).

### 5.2 Accounting Basis (s 19, 19A)

**Accounting Basis**

| Basis | Rule | Eligibility |
| --- | --- | --- |
| Source | all figures below | https://www.ird.govt.nz/gst/registering-for-gst/which-gst-accounting-basis-and-filing-frequency-should-i-use |
| Invoice basis | Sales when invoiced (or paid, if earlier); purchases when invoiced | Anyone. IRD's default |
| Payments basis | Account for GST when payment is received or made | Total sales NZD 2 million or less in the last 12 months, or likely in any 12-month period |
| Hybrid basis | Invoice basis for sales, payments basis for expenses | Anyone. IRD: "not commonly used by small businesses" |

The basis can be changed in myIR to one you are eligible for; a payments basis user whose sales pass the payments basis limit must change.

### 5.3 Filing Frequency and Deadlines (s 15, 16)

**Filing Frequency**

| Frequency | Eligibility | Note |
| --- | --- | --- |
| Source | all figures below | https://www.ird.govt.nz/gst/registering-for-gst/which-gst-accounting-basis-and-filing-frequency-should-i-use |
| Six-monthly | Sales under NZD 500,000 in any 12-month period | With a 31 March balance date: periods ending 30 September and 31 March |
| Two-monthly | Sales under NZD 24 million in any 12-month period | IRD's default if no period was chosen. With a 31 March balance date: periods ending in odd months |
| Monthly | Anyone; compulsory if sales are over NZD 24 million | Suits businesses with regular refunds |

**Deadlines** ([Filing GST](https://www.ird.govt.nz/gst/filing-and-paying-gst-and-refunds/filing-gst)):

- Return and payment are due by the 28th of the month after the taxable period ends.
- Period ending 31 March: due 7 May. Period ending 30 November: due 15 January.
- A due date on a weekend or public holiday moves to the next working day (IR375).
- "You must file a GST return for every taxable period, even if it is nil. You cannot get an extension of time to file a GST return."

### 5.4 Input Tax Rules (s 20, 21)

- **Input tax claimable conditions.** Supply by a GST-registered person, taxable supply information held (bands in Key Thresholds), used in the taxable activity. Payments basis: only what you have paid. See [IR375](https://www.ird.govt.nz/-/media/project/ir/home/documents/forms-and-guides/ir300---ir399/ir375/ir375.pdf).
- **Input tax not claimable conditions.** Not claimable: private use, and expenses relating to exempt supplies ("You cannot claim expenses relating to exempt supplies"). Mixed-use goods are apportioned (Example 4).
- **Entertainment.** Claim the full business entertainment cost in Box 11 during the year. Once a year make a debit adjustment of 15% of the GST-exclusive non-deductible amount (see Example 3; the income tax restriction is "only 50% of business entertainment expenses are deductible", IR375). It goes in the GST return covering: the earlier of the income tax return's due date or filing date (no tax agent); the earlier of its filing date or 31 March after the due date (tax agent); or its actual filing date (tax agent with an extension of time).

### 5.5 Penalties

**Late filing**

| Offence | Penalty | Note |
| --- | --- | --- |
| Source | all figures below | https://www.ird.govt.nz/managing-my-tax/penalties-and-interest/penalties-and-debt/late-filing-penalties |
| Late GST return, payments basis | NZD 50 | "There is a late filing penalty of $50 if you're on the payments basis." |
| Late GST return, invoice or hybrid basis | NZD 250 | "There is a $250 penalty for late filing on the hybrid or invoice basis." |

The basis in force when the return is due decides the penalty.

**Late payment**

| Stage | Penalty | Note |
| --- | --- | --- |
| Source | all figures below | https://www.ird.govt.nz/managing-my-tax/penalties-and-interest/penalties-and-debt/late-payment-penalties |
| Day after the due date | 1% | "1% penalty on the day after" |
| 7th day after the due date | 4% | "4% penalty for remaining tax including penalties" |
| Monthly penalty | Does NOT apply to GST | "1% penalty every month ... (except for GST, income tax including provisional tax, and Working for Families overpayments)" |

**Interest (use-of-money interest)**

| Item | Rate | Note |
| --- | --- | --- |
| Source | all figures below | https://www.ird.govt.nz/managing-my-tax/penalties-and-interest/interest-on-overpayments-and-underpayments |
| Underpaid tax, from 16 January 2026 | 8.97% | "16 January 2026 8.97% 2.25%" |
| Overpaid tax, from 16 January 2026 | 2.25% | same row |
| De minimis | NZD 100 | IRD does not apply interest to "amounts under $100" |

## Section 6: Tier 2 Catalogue (Reviewer Judgement Required)

### 6.1 Mixed-Use Assets

- **Mixed-use assets adjustment flag.** If the proportion of taxable use changes, a change-in-use adjustment may be required. Flag for reviewer any asset above the principal-purpose line.

| Item | Amount | Note |
| --- | --- | --- |
| Source | all figures below | https://www.ird.govt.nz/-/media/project/ir/home/documents/forms-and-guides/ir300---ir399/ir375/ir375.pdf |
| No adjustment periods needed (GST-exclusive cost) | NZD 10,000 | "$10,000 or less Not required" |
| Top of the 5 adjustment period band | NZD 500,000 | Lower band of 2 periods and higher band of 10: see IR375 |
| De minimis change | 10% | "within the 10% or $1,000 threshold" |
| De minimis change (amount) | NZD 1,000 | same quote |

### 6.2 Bad Debts (s 26)

- **Bad debt adjustment.** On the invoice or hybrid basis, when you write off a debt you returned GST on, show 3/23 of the amount written off on the IR372 and include it in Box 13 (credit adjustment) in the period you write it off. A bad debt later recovered is a debit adjustment (3/23 of the amount recovered, Box 9). See [IR375](https://www.ird.govt.nz/-/media/project/ir/home/documents/forms-and-guides/ir300---ir399/ir375/ir375.pdf).

| Item | Amount | Note |
| --- | --- | --- |
| Source | all figures below | https://www.ird.govt.nz/-/media/project/ir/home/documents/forms-and-guides/ir300---ir399/ir375/ir375.pdf |
| IR375 example: invoice written off (GST-inclusive) | NZD 115 | Brent shows the amount x 3 / 23 on his IR372 and in Box 13 |

### 6.3 Second-Hand Goods Input Tax

- **Second-hand goods input tax claim.** Claimable on second-hand goods bought from a non-registered person, subject to IR375's conditions and records.

### 6.4 Change of Use Adjustments

- **Change of use adjustment.** When business/private use of an asset changes, an adjustment may be required. Use the 6.1 limits; above the principal-purpose line, review use each year.

## Section 7: Working Paper Template

~~~
NZ GST WORKING PAPER (GST101A)
Taxpayer: ____________  GST Number: ___________
Period: ___________  Basis: Invoice / Payments / Hybrid
Filing Frequency: Monthly / 2-Monthly / 6-Monthly

SALES AND INCOME
  Box 5  Total sales incl. GST and zero-rated       ___________
         (exclude exempt supplies)
  Box 6  Zero-rated supplies included in Box 5      ___________
  Box 7  Box 5 minus Box 6                           ___________
  Box 8  Box 7 x 3/23                                ___________
  Box 9  Debit adjustments (IR372)                   ___________
  Box 10 Box 8 plus Box 9                            ___________

PURCHASES AND EXPENSES
  Box 11 Total purchases incl. GST                   ___________
         (exclude imported goods, exempt, private)
  Box 12 Box 11 x 3/23                               ___________
  Box 13 Credit adjustments (IR372)                  ___________
  Box 14 Box 12 plus Box 13                          ___________

RESULT
  Box 15 Difference between Box 10 and Box 14        ___________
         Box 14 larger: refund. Box 10 larger: to pay.

REVIEWER FLAGS:
  [ ] Registration status confirmed?
  [ ] Accounting basis confirmed?
  [ ] Entertainment adjustment due in this period?
  [ ] Private use apportionment applied?
  [ ] Taxable supply information held for all claims?
~~~

## Section 8: Bank Statement Reading Guide

### NZ Bank Statement Formats

Unverified: bank export layouts, not from Inland Revenue.

**NZ Bank Statement Formats**

| Bank | Format | Key Fields |
| --- | --- | --- |
| ANZ NZ | CSV / PDF | Date, Description, Amount, Balance |
| ASB | CSV | Date, Unique Id, Tran Type, Cheque Number, Payee, Memo, Amount |
| BNZ | CSV | Date, Description, Debit, Credit, Balance |
| Westpac NZ | CSV | Date, Description, Debit, Credit, Balance |
| Kiwibank | CSV | Date, Description, Amount, Balance |
| TSB | CSV | Date, Details, Debit, Credit, Balance |

### Key NZ Banking Narrations

**Key NZ Banking Narrations**

| Narration | Meaning | Classification Hint |
| --- | --- | --- |
| D/C or DIRECT CREDIT | Bank transfer in | Potential income |
| AP or AUTOPAY | Automatic payment out | Regular expense |
| EFTPOS | Card terminal payment | Expense or income |
| TFR / TRANSFER | Internal transfer | May be drawings |
| DD / DIRECT DEBIT | Direct debit | Regular expense |
| IRD / INLAND REVENUE | Tax payment or refund | Exclude |
| ACC | ACC levy | Exclude from GST |

## Section 9: Onboarding Fallback

If the client provides a bank statement but cannot answer onboarding questions immediately:

1. Classify all business-name credits as potential taxable supplies
2. Classify all regular debits to known suppliers as potential input tax claims
3. Apply conservative defaults: invoice basis, no private use recovery
4. Flag all entertainment expenses for the annual adjustment
5. Generate working paper with PENDING flags

Present these questions:

~~~
ONBOARDING QUESTIONS: NZ GST RETURN.
1. Are you GST-registered? If so, what is your GST number?
2. What is your filing frequency (monthly, 2-monthly, 6-monthly)?
3. Are you on the invoice, payments or hybrid basis?
4. What is your balance date?
5. Do you make any zero-rated supplies (exports)?
6. Do you make any exempt supplies (financial services, residential rent)?
7. Do you use a vehicle for business? What share is business use?
8. Do you work from home? What share is business use?
9. Did you import goods this period (Customs documents)?
~~~

## The method, step by step

1. Confirm registration, accounting basis and taxable period. Source: [which basis and filing frequency](https://www.ird.govt.nz/gst/registering-for-gst/which-gst-accounting-basis-and-filing-frequency-should-i-use).
2. Sort sales (taxable, zero-rated, exempt) and purchases (claimable, private, exempt, imported); exempt sales and private or exempt costs stay out of the return. Source: [IR375 GST guide](https://www.ird.govt.nz/-/media/project/ir/home/documents/forms-and-guides/ir300---ir399/ir375/ir375.pdf).
3. Work out adjustments on the IR372: debits to Box 9, credits to Box 13. Source: [IR375 GST guide](https://www.ird.govt.nz/-/media/project/ir/home/documents/forms-and-guides/ir300---ir399/ir375/ir375.pdf).
4. Fill Boxes 5 to 15 of the GST101A exactly as the form's labels say (table in 5.1). Source: [GST101A form](https://www.ird.govt.nz/-/media/project/ir/home/documents/forms-and-guides/gst100---gst199/gst101a/gst101a-2023.pdf).
5. File in myIR (or accounting software, or paper) and pay by the due date; there is no extension of time. Source: [Filing GST](https://www.ird.govt.nz/gst/filing-and-paying-gst-and-refunds/filing-gst).
6. Fix a later-found error by amending in myIR or, where IR375's conditions are met, in a later period. Source: [IR375 GST guide](https://www.ird.govt.nz/-/media/project/ir/home/documents/forms-and-guides/ir300---ir399/ir375/ir375.pdf).

## Ask the client first

- Invoice, payments or hybrid basis? (Timing of GST and the late filing penalty.)
- Taxable period and balance date? (Periods ending 31 March or 30 November have other due dates.)
- Any exempt supplies, such as residential rent or interest? (Out of Box 5; related costs not claimable.)
- Exports, or a sale of a business or land? (Possible zero-rating, Box 6.)
- Imports, or bad debts written off or recovered? (Box 9 and Box 13.)
- Tax agent, and income tax return filing date? (Timing of the entertainment adjustment.)

## When to refuse or refer

- The client is not registered and not required to register: no return to prepare.
- Land, a going concern or a commercial dwelling: refer.
- Financial services, GST groups, associated persons or non-resident digital services: refer.
- Assets above the principal-purpose line with changing use, or a final return on cancelling registration: refer.
- A tax position the client wants to change after filing: disputes process (IR770), not a correction. Refer.

## Section 10: Reference Material

### Key Legislation

Section numbers here and in the headings of 5.2, 5.3, 5.4 and 6.2 are legacy and not checked: do not cite them as verified. Only s 8, s 14 and s 51 are confirmed, in IRD interpretation statement IS 25/21.

**Key Legislation**

| Topic | Section |
| --- | --- |
| Imposition of GST | GSTA 1985, s 8 |
| Zero-rated supplies | GSTA 1985, s 11 |
| Exempt supplies | GSTA 1985, s 14 |
| Registration | GSTA 1985, s 51 |
| Accounting basis | GSTA 1985, s 19, 19A |
| Input tax | GSTA 1985, s 20, 21 |
| Filing periods | GSTA 1985, s 15, 16 |
| Bad debts | GSTA 1985, s 26 |

### Known Gaps / Out of Scope

- Company and partnership GST returns
- Complex financial services
- Cross-border digital services (non-resident supplier rules)
- Associated persons transactions
- GST grouping
- Provisional tax on the GST103B: `nz-provisional-tax`. Registration and general GST rules: `new-zealand-gst`

### Changelog

**Changelog**

| Version | Date | Change |
| --- | --- | --- |
| 2.1 | September 2026 | Box map rebuilt from the GST101A; exempt, entertainment, bad debt, import and penalty rules corrected |
| 2.0 | April 2026 | Full rewrite to v2.0 structure; NZ bank formats; local platform patterns; worked examples |
| 1.0 | 2025 | Initial version |

### Self-Check

- [ ] Registration confirmed and GST number recorded?
- [ ] Accounting basis confirmed (invoice, payments or hybrid)?
- [ ] Tax fraction 3/23 used consistently?
- [ ] Entertainment adjustment made in the right period (Box 9)?
- [ ] Exempt supplies left out of Box 5 and related costs left out of Box 11?
- [ ] Zero-rated supplies in Box 5 and again in Box 6?
- [ ] Imported goods left out of Box 11?

## Sources

- GST101A: https://www.ird.govt.nz/-/media/project/ir/home/documents/forms-and-guides/gst100---gst199/gst101a/gst101a-2023.pdf
- IR375 (March 2026): https://www.ird.govt.nz/-/media/project/ir/home/documents/forms-and-guides/ir300---ir399/ir375/ir375.pdf
- IR295 (April 2026): https://www.ird.govt.nz/-/media/project/ir/home/documents/forms-and-guides/ir200---ir299/ir295/ir295.pdf
- File your GST return: https://www.ird.govt.nz/gst/filing-and-paying-gst-and-refunds/filing-gst/file-your-gst-return
- Filing GST: https://www.ird.govt.nz/gst/filing-and-paying-gst-and-refunds/filing-gst
- Registering: https://www.ird.govt.nz/gst/registering-for-gst
- Basis and frequency: https://www.ird.govt.nz/gst/registering-for-gst/which-gst-accounting-basis-and-filing-frequency-should-i-use
- Late filing: https://www.ird.govt.nz/managing-my-tax/penalties-and-interest/penalties-and-debt/late-filing-penalties
- Late payment: https://www.ird.govt.nz/managing-my-tax/penalties-and-interest/penalties-and-debt/late-payment-penalties
- Interest: https://www.ird.govt.nz/managing-my-tax/penalties-and-interest/interest-on-overpayments-and-underpayments

## PROHIBITIONS

- NEVER charge GST if the person is not GST-registered
- NEVER claim input tax on private expenditure
- NEVER cut business entertainment claims in half each period: claim in full in Box 11 and make the annual Box 9 adjustment
- NEVER use a tax fraction other than 3/23 for the standard rate
- NEVER allow a going concern zero-rating unless both parties are registered and agree in writing (IR375)
- NEVER ignore the accounting basis: invoice vs payments basis changes when GST is accounted for
- NEVER include exempt supplies in Box 5: they are not included in the GST return
- NEVER include imported goods in Box 11
- NEVER present calculations as definitive: label as estimated and refer to IR or a NZ chartered accountant

## Disclaimer

This Guide and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this Guide. All outputs must be reviewed and signed off by a qualified professional (such as a New Zealand Chartered Accountant or equivalent licensed practitioner) before filing or acting upon.

The most up-to-date version of this Guide is maintained at openaccountants.com. Log in to access the latest version, request a professional review from a licensed accountant, and track updates as tax law changes.

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
