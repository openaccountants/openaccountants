---
name: us-sole-prop-bookkeeping
description: Classify 2026 US sole-proprietor and individual-owned disregarded LLC transactions into Schedule C working papers. Reconcile processor receipts without duplication, separate personal spending, document meals and vehicle costs, and hold unresolved classifications for review. Includes the 2026 line map and two worked cases. Federal only. Trigger on "categorize my transactions", "Schedule C bookkeeping", "bank statement to Schedule C".
version: "3.2"
jurisdiction: US
tax_year: 2026
last_updated: 2026-11-26
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
tier: 2
domain: bookkeeping
type: situation-rules
---

# US sole proprietor bookkeeping into Schedule C, tax year 2026

> **Source-cited draft.** Prepare a working paper for review before filing. Sources below support the retained rules; they do not constitute professional attestation.

**Answer first.** Classify supported business transactions, reconcile receipts once, and keep unresolved items out of filing totals. A merchant name suggests a question, not a deduction.

## Scope and who this is for

Federal bookkeeping for a sole proprietor's trade or business, including an individual-owned single-member LLC that has not elected corporate treatment. Confirm ownership and elections; a DBA or LLC bank label does not establish tax classification. See [IRS LLC guidance](https://www.irs.gov/businesses/small-businesses-self-employed/single-member-limited-liability-companies).

Use the client's established accounting method. This workflow produces a cash-transaction working paper; it does not calculate accrual adjustments. For accrual accounts, inventory or a method change: Check this point with one of our partner accountants.

## Ask the client first

Obtain all 2026 business-used bank and card statements, processor settlement reports, invoices and receipts, Forms 1099, prior Schedule C/Form 4562, and relevant mileage/payroll records. Include supported business purchases made with personal funds. With no transaction records, stop. For an incomplete year, label the working paper with its actual end date.

Read the available records before asking about business activity, ownership/elections, accounting method, business-use shares, asset acquisition and service dates, vehicle history, employees, inventory or home use. Statements alone do not establish these facts. Request supporting records regardless of amount; do not use USD 75 as a universal receipt exemption.

## The method, step by step

### Step 1: the 2026 Schedule C line map

| Line | Content |
| --- | --- |
| 1 | Gross receipts or sales |
| 2 | Returns and allowances |
| 4 | Cost of goods sold (Part III, line 42) |
| 6 | Other income (including fuel tax credits or refunds) |
| 8 | Advertising |
| 9 | Car and truck expenses |
| 10 | Commissions and fees |
| 11 | Contract labor |
| 12 | Depletion |
| 13 | Depreciation and section 179 (Form 4562) |
| 14 | Employee benefit programs (other than on line 19) |
| 15 | Insurance (other than health) |
| 16a | Interest: mortgage paid to banks |
| 16b | Interest: vehicle loan (business share) |
| 16c | Interest: other |
| 17 | Legal and professional services |
| 18 | Office expense |
| 19 | Pension and profit-sharing plans |
| 20a | Rent or lease: vehicles, machinery, equipment |
| 20b | Rent or lease: other business property |
| 21 | Repairs and maintenance |
| 22 | Supplies |
| 23 | Taxes and licenses |
| 24a | Travel |
| 24b | Deductible meals |
| 25 | Utilities |
| 26 | Wages (less employment credits) |
| 27a | Energy efficient commercial buildings deduction (attach Form 7205) only |
| 27b | Other expenses, from Part V line 48 |
| 30 | Business use of home (computed in `us-schedule-c-and-se-computation`) |

Source: [Schedule C (Form 1040) 2026](https://www.irs.gov/pub/irs-pdf/f1040sc.pdf).

### Step 2: import and reconcile

Inspect the actual CSV/PDF before selecting columns, dates and debit signs. Do not assume a fixed Chase, Wells Fargo or Mercury schema. Keep the original signed bank amount; normalize amounts used in the summary separately.

Match internal transfers, owner funding and card settlements before classifying income or expenses. Classify underlying card purchases once, including supported business charges on a personal card; do not also deduct the card payment. Record owner withdrawals separately: they are not deductible pay. Bona fide loan proceeds are not income. See [Publication 334](https://www.irs.gov/publications/p334).

For processor activity, obtain gross receipts and settlement details before finalizing revenue. Reconcile gross sales, fees, refunds, reserves and payout timing; do not deduct fees twice. Report each taxable receipt once, including cash or barter receipts without a Form 1099. Reconcile incorrect, duplicate and nontaxable Form 1099 entries instead of imposing their combined total as a revenue floor. See [IRS Form 1099-K guidance](https://www.irs.gov/businesses/what-to-do-with-form-1099-k).

### Step 3: classify from evidence

Use counterparty text to find the invoice or ask about purpose. The following are working-paper category suggestions **after** the actual expense, business use, current deductibility and timing are established. Capital assets and prepayments need separate review. See [Publication 334](https://www.irs.gov/publications/p334) and the line map above.

| Evidence identifies | Proposed category |
| --- | --- |
| Bank service or merchant processing fee | Part V, line 27b |
| Recurring business software, cloud or accounting subscription | Part V, line 27b |
| Advertising or email marketing service | Line 8 |
| Office or coworking rent for the current period | Line 20b |
| Vehicle/equipment lease | Line 20a; vehicle method review first |
| Business communication costs | Line 25; allocation/phone-line review first |
| Business insurance | Line 15; identify insured risk and beneficiary |
| Legal, accounting or professional service | Line 17; identify start-up/capital costs separately |
| Established nonemployee service | Line 11; worker status and reporting reviewed separately |
| Office/admin consumables or work supplies | Line 18 or 22 according to use; inventory separately |
| Payroll-provider debit | Split from payroll reports; do not infer wages, employer taxes or fees from the debit alone |
| Government payment | Identify the actual tax/form before choosing a line |

Separate the business and personal parts of mixed costs. Hold unknown portions without a deduction until supported. This applies to subscriptions, retail purchases, phone/internet, vehicles and insurance; a brand name cannot establish the percentage. Personal living and family expenses generally are not deductible. See [Publication 334](https://www.irs.gov/publications/p334) and [26 U.S.C. 262](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap1-subchapB-partIX-sec262.htm).

### Step 4: meals, vehicles and assets

**Meals.** Ordinary qualifying business meals are generally limited to 50%. Establish a business purpose, taxpayer/employee presence, and that the meal is not lavish or extravagant; retain the amount, date, place and relevant business relationship. A restaurant descriptor alone is insufficient. Qualifying solo business-travel meals do not require a client companion. For employee meals, entertainment, gifts and other exceptions: Check this point with one of our partner accountants. See [26 U.S.C. 274(k), (n)](https://uscode.house.gov/us/usc/t26/s274/) and [Publication 463](https://www.irs.gov/publications/p463).

**Evidence.** For travel, gifts and listed property, section 274(d) permits adequate records **or sufficient evidence corroborating the taxpayer's own statement**. A missing contemporaneous log does not automatically deny the deduction; assess the required elements and supporting evidence. Hold unsupported amounts; do not estimate business miles. See [26 U.S.C. 274(d)](https://uscode.house.gov/us/usc/t26/s274/).

**Vehicle methods.** Confirm eligibility before comparing methods. For an owned car, standard mileage must be chosen in its first business-use year. It is unavailable for five or more cars used simultaneously, prior accelerated/MACRS depreciation, section 179 or bonus depreciation; leased-car continuity rules also apply. A later switch from standard mileage to actual costs requires straight-line depreciation over the remaining estimated useful life, subject to limits. See [Publication 463, Standard Mileage Rate](https://www.irs.gov/publications/p463).

| Business miles in 2026 | Rate | Source |
| --- | --- | --- |
| 1 January–30 June | 72.5 cents/mile | [IRS mileage-rate table](https://www.irs.gov/tax-professionals/standard-mileage-rates) |
| 1 July–31 December | 76 cents/mile | [IRS mileage-rate table](https://www.irs.gov/tax-professionals/standard-mileage-rates) |

For an owned car, choose standard mileage in its first business-use year by the return due date including extensions to preserve that option. A later switch to actual costs requires straight-line depreciation over remaining estimated useful life, subject to depreciation limits. Standard mileage is unavailable for five or more cars used simultaneously, prior non-straight-line/MACRS depreciation, section 179 or bonus depreciation, or a leased car with post-1997 actual expenses. A leased car using mileage must continue it throughout the lease period. See [Publication 463, Standard Mileage Rate](https://www.irs.gov/publications/p463).

Under standard mileage, do not add fuel, repairs, insurance, registration, lease payments or depreciation again. Business parking and tolls can be additional; commuting parking/tolls are excluded. Under actual costs, allocate established vehicle costs to business use and obtain the permitted depreciation separately. See [Publication 463](https://www.irs.gov/publications/p463).

**Assets.** A safe-harbor ceiling is not a mandatory capitalization threshold. Identify the property, business share, cost and actual acquisition/service dates; do not invent an earlier acquisition date or a recovery period. For the USD 2,400 no-AFS example, the USD 3,499 MacBook, an asset ordered before 20 January 2025, and a vehicle over 6,000 pounds: Check this point with one of our partner accountants. Supply the records for capitalization, de minimis eligibility/election, section 179, bonus and vehicle-cap review. The [IRS tangible-property guidance](https://www.irs.gov/businesses/small-businesses-self-employed/tangible-property-final-regulations) expressly preserves repair deductions outside the safe harbor.

### Step 4: meals and evidence

Ordinary otherwise-deductible business meals are generally limited to 50%. Establish business purpose; the owner or an employee must be present and the cost must not be lavish or extravagant. Record amount, date, place, purpose and attendees/relationship where relevant. Employer-food and other special exceptions are referred below. See [26 U.S.C. 274(k) and (n)](https://uscode.house.gov/us/usc/t26/s274/).

For section 274(d) travel, gifts and listed property (excluding qualified nonpersonal-use vehicles), adequate records or sufficient evidence corroborating the taxpayer's statement must establish the statutory elements. A contemporaneous log is useful, but its absence alone does not automatically deny a deduction. Hold unsupported amounts without estimating miles. See [26 U.S.C. 274(d)](https://uscode.house.gov/us/usc/t26/s274/).

### Step 6: the working paper

Keep transaction date, original counterparty/description, signed bank amount, source reference, proposed line, supported business amount, hold status, evidence, question and reviewer reason. Keep deductions as positive amounts; use negative amounts for same-year reversals of those deductions. Retain separate fields for gross receipts and customer returns.

Sum only supported, released amounts by the explicit line tag. Include line 19. Follow the form: line 7 = line 1 − line 2 − line 4 + line 6; line 28 = expenses on lines 8 through 27b; line 29 = line 7 − line 28; line 31 = line 29 − line 30. Obtain the home-office amount separately. See [2026 Schedule C](https://www.irs.gov/pub/irs-pdf/f1040sc.pdf).

Keep an asset register with documented cost, acquisition/service dates and unresolved elections. Recalculate the working paper, check signs and reconciliation, and inspect formula errors before delivery. Present unresolved items separately from totals.

## Worked cases

These are fictional inputs. Merchant labels are not evidence of tax treatment. All deductions below assume established ordinary business purpose, current deductibility and sufficient records.

| Date | Counterparty | USD | Working-paper action |
| --- | --- | --- | --- |
| 01/15/2026 | STRIPE TRANSFER | +4,827.50 | Hold revenue reconciliation pending gross sales/fees |
| 02/01/2026 | GITHUB INC | −19.00 | Line 27b only if confirmed recurring business subscription |
| 03/12/2026 | THE CAPITAL GRILLE | −187.42 | Hold until meal conditions and evidence are established |
| 01/22/2026 | APPLE STORE (MacBook) | −3,499.00 | Asset/expensing review; no automatic line 13 deduction |
| 04/08/2026 | SHELL OIL | −62.18 | Hold pending vehicle, method, use and evidence |
| 06/15/2026 | IRS USATAXPYMT | −5,000.00 | Identify tax/form first; exclude if confirmed personal federal income tax |

**Case 1: processor gross-up and a client meal.** January sales are USD 5,000, processing fees USD 172.50 and the payout USD 4,827.50, with no refunds, sales tax or timing differences. The business owner attended the USD 187.42 dinner with a prospective client to discuss a contract; it was not lavish or extravagant and sufficient records exist. Assume the processing fees are ordinary current business expenses.

Line 1 is USD 5,000 and line 27b fees are USD 172.50. Their net equals the USD 4,827.50 payout; this does not guarantee agreement with every Form 1099-K. The ordinary 50% meal deduction is USD 93.71.

```oa-check
name: Processor gross-up and meals limit (2026)
inputs:
  payout: 4827.50
  fees: 172.50
  meal: 187.42
steps:
  - line_1: payout + fees
  - line_27b_fees: fees
  - net_effect: line_1 - line_27b_fees - payout
  - line_24b: meal * 0.50
expected:
  line_1: 5000.00
  line_27b_fees: 172.50
  net_effect: 0
  line_24b: 93.71
```

**Case 2: standard mileage or actual costs.** An owned car first used in business in 2026 has 18,000 total miles, 12,500 supported business miles: 6,000 in January–June and 6,500 in July–December. Running costs (fuel, insurance, repairs and registration) are USD 6,500. USD 5,000 is the stipulated depreciation on a wholly business-use basis, within the applicable cap before the example's business-use allocation; it is an input, not a depreciation calculation. Assume this single car is eligible for either method, no section 179/bonus or other disqualifying depreciation has been claimed, and the choice is timely.

Standard mileage: 6,000 × USD 0.725 + 6,500 × USD 0.76 = USD 9,290. Actual: (USD 6,500 + USD 5,000) × 12,500 / 18,000 = USD 7,986.11. Standard mileage is USD 1,303.89 higher on these inputs. Add supported business parking/tolls separately under either method without duplication. Standard mileage is preferable on the stated facts; a later change to actual costs has the depreciation restriction stated above.

```oa-check
name: Standard mileage against actual costs (2026)
inputs:
  miles_h1: 6000
  miles_h2: 6500
  total_miles: 18000
  running_costs: 6500
  depreciation: 5000
steps:
  - business_miles: miles_h1 + miles_h2
  - standard: miles_h1 * 0.725 + miles_h2 * 0.76
  - actual: (running_costs + depreciation) * business_miles / total_miles
  - standard_advantage: standard - actual
expected:
  business_miles: 12500
  standard: 9290.00
  actual: 7986.11
  standard_advantage: 1303.89
```

## When to refuse or refer

### Step 5: holds and referrals

A hold is a working-paper instruction, not a conclusion that an expense is legally personal or permanently disallowed. Record the missing evidence and question beside the transaction. Do not carry held deductions or unresolved income differences into a filing-ready summary.

For each topic below: **Check this point with one of our partner accountants.**

| Topic to resolve | Records to supply |
| --- | --- |
| Contractor reporting, including USD 1,900 or USD 2,500 paid by Zelle, card/platform payments, and amounts below reporting thresholds | W-9, payee tax status, service, payment route, annual total, withholding |
| Home office, including inventory-storage/daycare situations | Use, area, activity and cost records |
| Travel, mixed domestic/foreign trips, local rides and temporary-worksite/commuting questions | Tax home, itinerary, purpose, days, receipts and work locations |
| Employee meals, snacks, entertainment and gift exceptions | Recipients, purpose, benefit/payroll treatment and invoices |
| Phone-line exceptions, life insurance, website/start-up costs and charitable/political spending | Itemized charges, purpose, beneficiary, contract and dates |
| Inventory methods, hobby/loss limits and government fines/settlements | Prior methods/returns, stock, activity history and legal documents |
| Sales taxes, income taxes, interest income, owner health/retirement and personal car-loan relief | Actual tax imposed, loan/account and benefit records |
| Prior-year refunds, recoveries, reversals or chargebacks | Original transaction, tax year and prior treatment |
| Payroll filings, worker status, partnerships/corporations, rentals, farming, crypto, depletion, foreign accounts and estates/trusts | Entity/activity records and relevant returns; stop the affected work |

Do not infer employee/contractor status or a Form 1099 obligation from a payment descriptor. Route unresolved cases rather than applying a contractor default.

## Filing and completion

Employee-plan contributions belong on line 19; the sole proprietor’s own retirement contributions are considered separately, outside Schedule C. See [Publication 334, Pension Plans](https://www.irs.gov/publications/p334).

For an ordinary calendar-year domestic individual filer, the regular 2026 Form 1040 filing/payment deadline is 15 April 2027; a timely filing-extension request ordinarily permits filing by 15 October 2027 and does not extend payment. Special overseas, disaster and other relief: Check this point with one of our partner accountants. See [IRS individual filing](https://www.irs.gov/individual-tax-filing) and [filing extensions](https://www.irs.gov/filing/get-an-extension-to-file-your-tax-return).

Where a 2026 Form 1099-NEC is required, the ordinary IRS/payee deadline is 1 February 2027: 31 January is Sunday and the instructions move it to the next business day. This does not determine which payments require the form. See [IRS instructions](https://www.irs.gov/instructions/i1099mec).

Deliver the reconciled Schedule C working paper, asset register and holds list for return preparation. Every imported transaction needs a proposed line or exclusion/hold reason; reconcile accounts and Forms 1099, confirm evidence and remove duplicate deductions. Do not call incomplete records filing-ready.

## Sources

The 2026 form and IRS mileage table establish current form lines and rates. Existing source reads from 22 November 2026 were reused only for the applicable retained rules; exact passages were recovered/read on 26 November 2026. Publication 463's 2025 edition supports structural method and evidence rules, not the 2026 rates. No inaccessible eCFR page is treated as a completed regulation read.

- [2026 Schedule C](https://www.irs.gov/pub/irs-pdf/f1040sc.pdf). Read for form lines 1–31 and Part V; read 2026-11-26.
- [IRS single-member LLC guidance](https://www.irs.gov/businesses/small-businesses-self-employed/single-member-limited-liability-companies). Read for ownership and corporate-election classification; read 2026-11-26.
- [Publication 334: business expenses and records](https://www.irs.gov/publications/p334). Read for chapter 8 business expense allocation, pensions and federal income tax; read 2026-11-26.
- [IRS Form 1099-K reconciliation](https://www.irs.gov/businesses/what-to-do-with-form-1099-k). Read for gross payments, fees and nontaxable entries; read 2026-11-26.
- [26 U.S.C. 262: personal expenses](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap1-subchapB-partIX-sec262.htm). Read for section 262(a) personal costs; read 2026-11-26.
- [Current 26 U.S.C. 274: meals and substantiation](https://uscode.house.gov/us/usc/t26/s274/). Read for sections 274(d), (k) and (n); read 2026-11-26.
- [Publication 463: vehicle methods, travel and evidence](https://www.irs.gov/publications/p463). Read for chapter 4 method choice/disqualifiers, allocation and parking/tolls; read 2026-11-26.
- [IRS 2026 mileage rates](https://www.irs.gov/tax-professionals/standard-mileage-rates). Read for the two 2026 business-rate periods; read 2026-11-26.
- [IRS tangible-property guidance](https://www.irs.gov/businesses/small-businesses-self-employed/tangible-property-final-regulations). Read for repair deductions outside the safe harbor; read 2026-11-26.
- [IRS individual filing](https://www.irs.gov/individual-tax-filing) and [extensions](https://www.irs.gov/filing/get-an-extension-to-file-your-tax-return). Read for regular filing and extension/payment deadlines; read 2026-11-26.
- [IRS Forms 1099-MISC/NEC instructions](https://www.irs.gov/instructions/i1099mec). Read for filing dates and recipient statements; read 2026-11-26.

Not yet confirmed: none in the retained rules. The listed exceptions and incomplete records are referred or held; this working paper does not resolve those questions.
