---
name: us-1099-k-and-payment-processors
description: Reconcile US federal Form 1099-K payment-card, payment-app and marketplace receipts for tax year 2026, retaining separate 2025 return instructions. Covers the USD 20,000 and 200-transaction TPSO test, gross receipts, duplicate Forms 1099-NEC, business, rental, hobby, personal gains and losses, gifts and reimbursements, backup withholding, tips, digital-asset forms and CP2000 replies. Use transaction records rather than platform labels. Exact 2026 individual-return line positions and unresolved historical cases are held for professional review. Triggers include PayPal, Venmo, Stripe, eBay, Etsy, 1099-K threshold and CP2000 1099-K. Federal only; payee reconciliation, not issuer compliance or entity returns.
version: "2.1"
jurisdiction: US
tax_year: 2026
last_updated: 2026-11-27
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
tier: 2
domain: income-tax
type: situation-rules
---

# US Form 1099-K: payment cards, payment apps and marketplaces (tax year 2026)

> **General reference only.** This Guide supports working papers, not a filing decision on incomplete facts. Qualified professional review is required before filing. Circular 230 §10.37 disclosure: this is general reference material, not a written opinion for a particular taxpayer.

**Answer first.** The federal TPSO reporting test is **more than USD 20,000 and more than 200 transactions**, both exceeded. Payment-card transactions have no de minimis threshold. A form can arrive below the TPSO threshold. Neither its presence nor its absence determines taxable income. Reconcile each payment by its actual nature before preparing the return. [IRS general FAQs Q2, Q5, Q7](https://www.irs.gov/newsroom/form-1099-k-faqs-general-information)

## Scope and who this is for

US individuals, sole proprietors and federally disregarded single-member LLCs reconciling 2026 Forms 1099-K, with a separately dated 2025 filing reference. Includes erroneous forms and CP2000 discrepancies. Entity returns, issuer filing/penalty compliance and specific state obligations require separate work. Load `us-tax-workflow-base`; use `us-sole-prop-bookkeeping` for records, `us-schedule-c-and-se-computation` for profit/SE tax, `us-qbi-deduction` for QBI and `us-1099-nec-issuance` for payer obligations. These routes do not certify a particular result.

**Year boundary:** the Form 1099-K instructions read are labelled December 2026. The individual-return instructions read remain **2025**. The 2025 line positions below are identified as such; they are not authority to transmit a 2026 return. The 2026 final-line mapping is a non-usable hold: Check this point with one of our partner accountants.

## Ask the client first

Obtain every 1099-K, NEC, MISC and DA, account-level transaction exports and annual statements, invoices, cash/check/ACH receipts and bank settlements. Ask what each payment bought; account labels alone do not establish its tax character. Identify refunds, chargebacks, fees, shipping, discounts, debit-card cash back, tips and sales taxes, including who legally bears each tax. Obtain personal-item cost, selling expenses, acquisition/sale dates and sale proceeds item by item; reconstruct missing cost records before deciding gain or loss.

Check names/TINs, Box 4 withholding, current and prior-year TPSO transactions, shared terminals, business sales/entity changes and all IRS notices. For hobby classification, obtain all profit-objective facts, not just an LLC, business profile, books or separate account. Missing records mean an unresolved working-paper item; never default an unidentified deposit to taxable Schedule C income or assume a sales-tax deduction.

## The method, step by step

## Rates, bands and thresholds

| Point | Federal rule and operative condition | Official source |
|---|---|---|
| TPSO goods/services payments | Required reporting only when annual gross exceeds USD 20,000 **and** transaction count exceeds 200; equality fails either test | [P.L. 119-21 §70432(a)](https://www.govinfo.gov/content/pkg/PLAW-119publ21/html/PLAW-119publ21.htm) |
| Applicable years | Restoration applies as if in ARPA §9674: calendar 2022 onward, including 2025 and 2026 | [§70432(a)(2)](https://www.govinfo.gov/content/pkg/PLAW-119publ21/html/PLAW-119publ21.htm), [§6050W effective-date note](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleF-chap61-subchapA-partIII-subpartB-sec6050W.htm) |
| Payment cards | No reporting threshold; includes credit, debit and qualifying stored-value/gift cards | [IRS general FAQs Q2–Q3](https://www.irs.gov/newsroom/form-1099-k-faqs-general-information) |
| Backup withholding | 24% on reportable payments where applicable TIN conditions are met; TPSO timing and prior-year exception below | [IRS backup withholding](https://www.irs.gov/businesses/small-businesses-self-employed/backup-withholding), [§70432(b)](https://www.govinfo.gov/content/pkg/PLAW-119publ21/html/PLAW-119publ21.htm) |
| Ordinary payee statement deadline | January 31 following the calendar year; for 2026, Monday February 1, 2027, because January 31 is Sunday; approved extensions/special relief need separate checking | [§6050W(f)](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleF-chap61-subchapA-partIII-subpartB-sec6050W.htm), [§7503](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleF-chap77-sec7503.htm) |

A TPSO is the central organization contractually obliged to settle qualifying network transactions; an app's brand is not the test. The current K instructions exclude automated clearing houses, healthcare networks and in-house accounts payable departments from TPSOs. Voluntary forms and lower state thresholds remain possible. Historical IRS phase-in targets are not the current federal test. [K instructions, definitions](https://www.irs.gov/instructions/i1099k); [IRS general FAQs Q4–Q5](https://www.irs.gov/newsroom/form-1099-k-faqs-general-information)

1. **Check each form against records.** Box 1a is gross, without adjustment for credits, cash equivalents, discounts, fees, refunds or shipping. Box 1b is card-not-present gross, a subset, not another receipt to add. Box 1c reports cash tips already included in 1a; Box 1d is the tipped-occupation code. Do not add 1b or 1c to 1a. [K instructions, boxes 1a–1d](https://www.irs.gov/instructions/i1099k)
2. **Request corrections.** Contact the filer at top left, or PSE at bottom left if unfamiliar. The IRS cannot correct the form. Request zero for a wholly erroneous personal-payment form; request correction of actual TIN/amount errors. Keep correspondence and file using the correct facts even if correction has not arrived. An individual's form for corporate/partnership income needs correction and entity-return review. [IRS correction instructions](https://www.irs.gov/businesses/what-to-do-with-form-1099-k)
3. **Build a transaction bridge.** Record each form once, identify overlap, split the categories below, and include taxable receipts absent from forms. Reconcile gross receipts, deductions and net payouts separately using the taxpayer's accounting method. Never force revenue to equal total forms or bank deposits. [IRS what to do](https://www.irs.gov/businesses/what-to-do-with-form-1099-k); [Schedule C, accounting method and line 1](https://www.irs.gov/instructions/i1040sc)
4. **Apply the category matrix.** For a cash-method business, record taxable receipts actually/constructively received and deductible expenses paid; an accounting-method/timing conflict is not resolved merely by the form. The exact 2026 return lines remain held as above. [Schedule C line F](https://www.irs.gov/instructions/i1040sc)

### Where each slice goes: federal classification and separately dated line reference

| Slice | Treatment and boundary | Official source |
|---|---|---|
| Sole-proprietor trade/business receipts | Gross receipts before ordinary, necessary processor/platform fees. For **2025**, Schedule C line 1; sales returns/allowances on line 2; fees in expenses. Substantiate deduction eligibility; a chargeback is not automatically a bad debt | [Schedule C lines 1–2](https://www.irs.gov/instructions/i1040sc), [§162(a)](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap1-subchapB-partVI-sec162.htm) |
| Rental receipts, including Airbnb/VRBO | Schedule E or C depends on the actual activity; do not decide from platform or a seven-day average stay. Separate retail/rental receipts sharing one terminal. Unresolved rental classification: Check this point with one of our partner accountants. | [IRS rental/terminal instructions](https://www.irs.gov/businesses/what-to-do-with-form-1099-k) |
| Hobby/non-profit-objective activity | **2025** Schedule 1 line 8j, rather than automatic Schedule C. Classification rules below. No miscellaneous itemized hobby-expense deduction in 2026; this does not settle COGS, basis recovery or otherwise independently allowable deductions | [2025 Form 1040](https://www.irs.gov/instructions/i1040gi), [§67(h) and effective-date notes](https://uscode.house.gov/us/usc/t26/s67/), [P.L. 119-21 §70110](https://www.govinfo.gov/content/pkg/PLAW-119publ21/html/PLAW-119publ21.htm) |
| Personal-use item sold at gain | Figure gain with supported adjusted basis and selling costs; report on Form 8949/Schedule D. Holding period and asset type matter; do not label every valuable bag/watch a collectible | [IRS personal items](https://www.irs.gov/businesses/what-to-do-with-form-1099-k), [Form 8949](https://www.irs.gov/instructions/i8949) |
| Personal-use item sold at loss | Loss is not deductible; keep gain/loss items separate. **2025**: loss-sale proceeds in the entry space at top of Schedule 1, or Form 8949 with code L, positive nondeductible-loss adjustment in (g), resulting in zero | [2025 Form 1040](https://www.irs.gov/instructions/i1040gi), [Form 8949 personal property](https://www.irs.gov/instructions/i8949) |
| Genuine gifts/shared-cost reimbursements; erroneous or duplicate K | Not goods/services merely because tagged G&S. Request correction; **2025** top-of-Schedule-1 entry only for the amount included in error, not the taxable remainder. Do not invent a Schedule C expense to wash out personal payments | [IRS FAQs Q2/Q4](https://www.irs.gov/newsroom/form-1099-k-faqs-what-to-do-if-you-receive-a-form-1099-k), [2025 Form 1040](https://www.irs.gov/instructions/i1040gi) |
| Customer debit-card cash back | Generally neither gross receipts nor a business expense; retain records | [IRS cash back](https://www.irs.gov/businesses/what-to-do-with-form-1099-k) |
| Sales tax imposed on buyer, collected and paid over | Excluded from gross receipts; no deduction. Any portion legally retained is income (**2025** Schedule C line 6) | [Schedule C line 23](https://www.irs.gov/instructions/i1040sc) |
| Sales tax imposed on seller | Collected amounts included in receipts; eligible seller sales tax deductible (**2025** lines 1/23). Establish applicable state law first; marketplace-facilitator labels do not decide federal treatment | [Schedule C line 23](https://www.irs.gov/instructions/i1040sc) |

### Duplicates, shared terminals and platform patterns

Card and qualifying third-party-network settlements are excluded from payer NEC/MISC reporting; the K de minimis test is disregarded for this coordination rule. Do not infer qualification from a brand alone. Report the underlying receipt once, compare transaction identifiers, request correction and document overlap. A different bonus or ad-revenue stream is not a duplicate just because the platform is the same. For **2025**, attach an explanation if NEC box-1 totals exceed Schedule C line 1; a bridge for other discrepancies is prudent working-paper practice, not a universal mandatory attachment or guarantee against notices. [K instructions, reporting coordination](https://www.irs.gov/instructions/i1099k); [Schedule C line 1](https://www.irs.gov/instructions/i1040sc)

For shared terminals, where required file/furnish the appropriate information return for another party's share; obtain a corrected K for a business sale, notify the acquirer of entity/TIN changes and retain dated agreements. Exact issuer obligations are held for separate professional work. [IRS shared gross amounts](https://www.irs.gov/businesses/what-to-do-with-form-1099-k)

Historical platform coverage remains an intake checklist: Stripe, Square, PayPal Commerce/Checkout/G&S/F&F, Shopify Payments, Adyen, Worldpay, Fiserv/First Data, Heartland, Toast, Clover, Lightspeed, Authorize.Net, Visa, Mastercard, American Express, Discover, Venmo personal/business, Cash App personal/business, Zelle/Plaid/ACH, eBay, Etsy, Amazon, Mercari, Poshmark, Depop, Vinted, ThredUp, Airbnb/VRBO/HomeAway, Uber/Lyft, DoorDash/Grubhub/Uber Eats/Instacart, Patreon/OnlyFans/Substack, Twitch/YouTube/AdSense/Super Chat/Super Thanks, TikTok, Meta/Instagram, StubHub/SeatGeek/Vivid Seats/Ticketmaster and crowdfunding. Obtain actual forms/contracts/transaction exports. Brand-specific fees, rails, issuance guarantees, F&F tax immunity, occupancy-tax collection agreements and creator form assignments are **not certified**. Check this point with one of our partner accountants.

### Hobby or business

**AUDIT FLASH POINT** - losses do not themselves decide classification. Evaluate all objective facts: businesslike conduct, expertise, time/effort, expected asset appreciation, success in other activities, loss/profit history, occasional profits, financial status and personal pleasure. No one factor, LLC or account label decides; profit objective alone also does not establish every trade/business requirement. [Treas. Reg. §1.183-2(a)–(b)](https://www.ecfr.gov/current/title-26/section-1.183-2)

Section 183(d) presumes profit objective, unless the IRS establishes otherwise, if gross income exceeds attributable deductions in **3 of 5 consecutive taxable years ending with the current year**; substitute **2 of 7** where the activity consists in major part of breeding, training, showing or racing horses. Failing this presumption does not itself prove hobby status. [§183(d)](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap1-subchapB-partVI-sec183.htm)

Section 67's miscellaneous itemized deduction disallowance continues after 2025 under [§67(h)](https://uscode.house.gov/us/usc/t26/s67/) and P.L. 119-21 §70110; stale publications do not override it. Hobby COGS/basis recovery, independently allowable deductions, disputed status and sustained losses need separate analysis. Check this point with one of our partner accountants.

### Backup withholding and tips

Missing TIN or an IRS incorrect-TIN notification can trigger **24%** withholding on reportable K payments. Card payments have no de minimis threshold. Provide the correct SSN/EIN/ITIN; follow the actual notice to resolve withholding, rather than assuming Box 4 always proves a particular error. Claim Box 4 federal withholding for the year the income was received. [IRS backup withholding](https://www.irs.gov/businesses/small-businesses-self-employed/backup-withholding), [K Box 4](https://www.irs.gov/instructions/i1099k)

For TPSO payments from calendar **2025**, §3406(b)(8) requires the current-year count to exceed 200 and the aggregate amount to exceed USD 20,000 at the payment time. **Exception:** this gate does not apply if one or more TPSO payments by that payor to that payee in the preceding calendar year were reportable payments. Withholding also requires an applicable §3406 trigger. Never conclude no withholding from current-year totals alone. Issuer Form 945/K reporting after withholding is outside this payee computation: Check this point with one of our partner accountants. [P.L. 119-21 §70432(b)](https://www.govinfo.gov/content/pkg/PLAW-119publ21/html/PLAW-119publ21.htm)

For **2025**, K does not separately show tips; the Form 1040 instructions allow substantiated qualified tips included in aggregate reported compensation/payments, using records such as platform statements. Physical cash absent from the information return is not included in that nonemployee deduction calculation. For 2026, K Box 1c separately states cash tips included in 1a. This does not establish deduction eligibility or amount: retain Schedule 1-A as a non-usable referral. Check this point with one of our partner accountants. [2025 Form 1040, qualified tips](https://www.irs.gov/instructions/i1040gi); [K Box 1c](https://www.irs.gov/instructions/i1099k)

### Digital assets: Form 1099-DA

Custodial brokers' gross-proceeds reporting starts with **2025** transactions; basis reporting starts for certain **2026** transactions. The IRS describes custodial platforms, certain hosted wallets, kiosks and payment processors; the cited regulations do not cover noncustodial brokers that do not take possession. A 2026 covered asset generally must be acquired after 2025 in the broker's custodial account for the specified consideration and held there until disposition. Pre-2026 or transferred-in assets are noncovered; absence of broker basis is not zero basis. Obtain transaction/basis records and identify any K/DA overlap. Digital-asset receipt income is distinct from later sale gain/loss; do not treat all flows as capital sales. [IRS digital assets](https://www.irs.gov/filing/digital-assets); [2026 DA instructions, covered security](https://www.irs.gov/instructions/i1099da)

The IRS provides good-faith filing/furnishing relief for brokers' 2025 transactions and backup-withholding relief for 2025/2026 transactions. This is broker relief, not a taxpayer exclusion. Wallet allocation safe harbors, incomplete basis, noncustodial/DeFi obligations and unresolved overlap remain non-usable here. Check this point with one of our partner accountants. [IRS transition relief](https://www.irs.gov/filing/digital-assets)

### CP2000 response

A CP2000 describes a third-party mismatch and proposed changes; it is not a bill. Reply by **the date on the notice**, using its instructions. Complete/sign an included response form, state agreement/disagreement and supply support. Include the bridge, forms, platform/bank statements, fee/refund records, personal-item evidence and correction correspondence as relevant. Neither a fixed 30-day assumption nor a bridge guarantees no notice. [IRS CP2000](https://www.irs.gov/individuals/understanding-your-cp2000-series-notice)

If the notice is correct and there are no other income/credit/expense changes, follow it without an amended return. If correct with other changes, complete 1040-X, write CP2000 at the top and submit with the response; inspect earlier years for the same error. A negligence/substantial-understatement penalty can be **20% of the affected underpayment portion**, not automatically 20% of all tax. Contested penalties/reasonable cause, bills or deficiency notices: Check this point with one of our partner accountants. [IRS CP2000](https://www.irs.gov/individuals/understanding-your-cp2000-series-notice); [§6662(a)–(b)](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleF-chap68-subchapA-partII-sec6662.htm)

## Boundary and exception table

| Situation | Result / action |
|---|---|
| USD 20,000 exactly with 201 transactions; or more than USD 20,000 with 200 exactly | Neither satisfies both TPSO tests; voluntary/state forms and taxable income remain possible ([§70432](https://www.govinfo.gov/content/pkg/PLAW-119publ21/html/PLAW-119publ21.htm)) |
| Payment card, any volume; small TPSO form | Apply card rule or voluntary/state explanation, not an automatic invalid-form complaint ([FAQs Q2/Q5](https://www.irs.gov/newsroom/form-1099-k-faqs-general-information)) |
| Gift/reimbursement labelled business; business receipt labelled F&F | Determine underlying facts, not label; never hide taxable receipts ([IRS FAQs Q2](https://www.irs.gov/newsroom/form-1099-k-faqs-what-to-do-if-you-receive-a-form-1099-k)) |
| Duplicate K/NEC; separate platform bonus | Prove overlap before exclusion; retain genuinely separate receipts (coordination rule above) |
| Mixed personal gains/losses | Item-level records; no deduction for personal losses; apply the separately dated entry instructions above |
| Unidentified payment, basis, accounting method, sales-tax bearer or rental/hobby status | Hold the affected conclusion, obtain records; Check this point with one of our partner accountants. |
| Shared terminal/entity change, foreign address/status, state reporting or crowdfunding gifts/rewards/charity | Keep topic in scope as intake; specific treatment remains non-usable. Check this point with one of our partner accountants. |

## Worked cases

**A - mixed personal items (IRS 2025 example).** Couch cost USD 1,000, sale 700; handbag cost 800, sale 1,200; K total 1,900. With the stated personal-use/cost facts, loss proceeds 700 go at the top of **2025** Schedule 1; handbag gain 400 goes on Form 8949/Schedule D. The couch loss does not offset the gain. Do not substitute this line mapping for the held 2026 final instructions. [2025 Form 1040 example](https://www.irs.gov/instructions/i1040gi)

**B - original online seller bridge, working-paper amounts retained.** K 48,000 includes a 6,000 card payment also on NEC; buyer-imposed sales tax collected/paid over 2,000; returned-goods refunds 1,500; ordinary necessary processor fees paid 1,400; cash sales absent from forms 3,000. Assume cash method, all business sales current-year, no inventory/timing complication and no other adjustments. Forms total 54,000; subtract duplicate 6,000 and buyer tax 2,000; add cash 3,000 = **49,000 gross receipts**. Sales returns 1,500 leave **47,500 after returns**, before fees/COGS/other expenses. Fees 1,400 are a separate eligible expense, not netted from gross. In the read **2025** Schedule C these are lines 1 and 2; exact 2026 line mapping is held. [Schedule C lines 1, 2, 23](https://www.irs.gov/instructions/i1040sc); [§162](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap1-subchapB-partVI-sec162.htm)

```oa-check
name: Online seller bridge from Forms 1099-K and 1099-NEC to Schedule C line 1
inputs:
  form_1099k: 48000
  form_1099nec: 6000
  duplicate_nec: 6000
  sales_tax_on_buyers: 2000
  cash_sales: 3000
  refunds: 1500
  processor_fees: 1400
steps:
  - information_returns: form_1099k + form_1099nec
  - line_1: information_returns - duplicate_nec - sales_tax_on_buyers + cash_sales
  - line_2: refunds
  - gross_income_after_returns: line_1 - line_2
expected:
  information_returns: 54000
  line_1: 49000
  line_2: 1500
  gross_income_after_returns: 47500
```

**C - roommate rent reimbursement.** Preserve the original goods/services mistag; no amount was supplied. If it is genuinely reimbursement of the roommate's shared cost, request corrected zero K and do not wait to file correctly. Use **2025** top-of-Schedule-1 error entry for 2025; hold exact 2026 entry pending final instructions. [IRS corrections](https://www.irs.gov/businesses/what-to-do-with-form-1099-k); [2025 Form 1040](https://www.irs.gov/instructions/i1040gi)

**D - marketplace, more than USD 20,000 and 150 transactions.** No federal TPSO reporting requirement from those totals alone; taxable business receipts remain reportable and a voluntary/state form can arrive. [§70432(a)](https://www.govinfo.gov/content/pkg/PLAW-119publ21/html/PLAW-119publ21.htm); [FAQs Q5/Q7](https://www.irs.gov/newsroom/form-1099-k-faqs-general-information)

**E - 2026 marketplace, USD 23,400, 150 sales, missing TIN; compare 201 sales.** Reporting test fails at 150 and passes at 201. Do not decide withholding without prior-year facts: absent prior-year reportable payments the current-year gate is unmet at 150; with a prior-year reportable payment the exception can apply. At 201 the amount must exceed the threshold at the payment time and a withholding trigger must apply; do not multiply all annual receipts by 24%. Give the platform the correct TIN and report taxable business receipts regardless of K issuance. [§70432(b)](https://www.govinfo.gov/content/pkg/PLAW-119publ21/html/PLAW-119publ21.htm)

```oa-check
name: TPSO 1099-K reporting test for 2026 (both tests must be exceeded)
inputs:
  gross_payments: 23400
  transactions: 150
  dollar_threshold: 20000
  count_threshold: 200
steps:
  - dollar_test: floor(min(gross_payments, dollar_threshold + 1) / (dollar_threshold + 1))
  - count_test: floor(min(transactions, count_threshold + 1) / (count_threshold + 1))
  - must_report: dollar_test * count_test
  - with_201_sales: dollar_test * floor(min(201, count_threshold + 1) / (count_threshold + 1))
expected:
  dollar_test: 1
  count_test: 0
  must_report: 0
  with_201_sales: 1
```

This inherited check tests the supplied whole-dollar reporting facts only; it is not a cents-precision threshold calculator or a backup-withholding engine.

### Historical cases retained: corrected arithmetic or explicitly non-usable outcomes

These are the original historical **2025** inputs, not new 2026 examples. Rows marked HOLD are not filing instructions. For every HOLD: **Check this point with one of our partner accountants.**

| Original case | Preserved inputs and disposition |
|---|---|
| Small card / TPSO illustrations | Illustrative inputs/computed amounts: USD 10 card swipe; eBay 250 × 50 = 12,500; Etsy 10 × 3,000 = 30,000. Card rule has no threshold; both TPSO illustrations fail one prong. No guaranteed non-receipt of forms ([FAQs Q2/Q5](https://www.irs.gov/newsroom/form-1099-k-faqs-general-information)) |
| §5.2 worksheet | Stripe 82,400, Square 4,150, PayPal 11,250, Etsy 3,805; cash/check 2,800; ACH 6,400; refunds/chargebacks 3,200; sales tax 4,150; purported duplicate NEC 12,000; Stripe fee 2,950. Forms 101,605; plus off-form receipts = 110,805. The old 91,455 subtracts a duplicate never added to that starting sum and nets refunds before gross. HOLD until overlap, tax bearer and chargeback facts are established; no certified replacement return total. |
| Poshmark personal clothing | Illustrative inputs: USD 1,850 over 47 sales, each below original cost. Retain cost-evidence requirement. For 2025 use top-of-Schedule-1 loss proceeds, not old 8z/24z wash ([2025 Form 1040](https://www.irs.gov/instructions/i1040gi)). |
| Personal handbag / collectibles | Bought for USD 8,000 in 2018, sold 2025 for 14,000. Difference 6,000 before selling-cost/basis adjustments. HOLD the old automatic collectible/28% rate, wrong short-term box C and automatic zero-basis outcome; determine asset, dates, basis and costs. |
| Crochet classifications | 2025 receipts 7,000, yarn 4,500, five hours/week, no separate account, three loss years and recreation; contrasted with same sales, LLC, separate Stripe, advertising, first year. Also 7,000 receipts/9,000 expenses/2,000 economic loss against wages. HOLD categorical hobby/business conclusions; apply all objective facts, not a checklist shortcut. |
| Consultant duplicate | 2025 invoice/card receipt 12,000; K and NEC each 12,000; stated payout 11,652.40 and purported fee 2.9% + 0.30. Forms 24,000; receipt counted once 12,000 if overlap proven. HOLD fee/payout claim: one such fee is 348.30, implying 11,651.70, not 11,652.40. |
| §9.3 proposed statement | Stripe K 82,400/refunds 1,200/fees 2,800; PayPal K 11,250 including shared-travel reimbursement 1,850; Poshmark loss proceeds 1,640. Original stated total 95,290 is correct; alleged gross 91,640 and unexplained residual 2,010 are not adopted. HOLD filing statement: no personal-reimbursement business-expense wash, no refund-as-bad-debt assumption and no guaranteed notice prevention. |
| Sarah, original §10.1 | Wages 85,000; Etsy begun 2023; 2025 K 7,140 = enamel pins 3,800 + personal loss proceeds 3,340; pin costs 4,200/economic loss 400; three loss years, no separate account/advertising. HOLD exact hobby COGS/AGI and classification; personal-loss entry is the 2025 top space once item-level loss substantiated. |
| Marcus, original §10.2 | Full-time 2025 driver: fares 32,800 + tolls 1,150 + tips 1,050 = K 35,000; bonus NEC 2,000; service fee 8,200 + booking fee 950 = 9,150; stated bank 26,850 conflicts with 37,000 − 9,150 = 27,850. Mileage 28,500 × stated 0.70 = 19,950; supplies 420, phone 480; amounts sum 30,000 expenses/7,000 arithmetic remainder. Original SE inputs 0.9235/15.3%, claimed 6,465/988/494: 7,000 × .9235 = 6,464.50; × .153 = 989.0685, half 494.53425 before return rounding. HOLD mileage eligibility, deduction classification, net profit and SE tax; original hypothetical Notice 2025-XX is not authority. |
| Jade, original §10.3 | 2025 K Patreon 94,200/Stripe 18,400; NEC Google 42,000/Spotify 6,800/Brand X 15,000; four other sponsorships 22,000 supposedly in Stripe too; alleged merch 3,000; fees 8,478/1,710. Forms total 176,400; asserted gross 183,000 contradicts the facts: 15,000 + 22,000 = 37,000 exceeds Stripe 18,400. HOLD entire result; do not relocate sponsorships, change inputs or assume no CP2000 risk. |
| Marketplace / crypto illustrations | Original USD 100,000 sales vs claimed 93,000 platform K; USD 200,000 crypto volume/400 gain; ride-share 35,000 + 2,000 forms vs 24,000 or 26,800 reported gross. HOLD automatic platform exclusions, asserted gains and notice predictions; reconcile actual transactions, not assumed platform output. |

## When to refuse or refer

Refuse a return that deliberately omits taxable receipts because no form arrived. For missing purchase records, unresolved classification, rental services/occupancy taxes, crowdfunding gift/reward/charity questions, state duties, foreign/nonresident status, collectibles, disputed hobby COGS, digital-asset basis or contested notices, keep the affected answer non-usable. Check this point with one of our partner accountants.

Historical state figures (Maryland/Massachusetts/Vermont/Virginia/DC USD 600; Illinois USD 1,000 or four transactions; New Jersey USD 1,000) and PayPal's purported 2.99% + 0.49 fee are **withdrawn, non-usable figures**, not current rules. Historical Wayfair/45-state/30-state assertions, platform form guarantees, wallet safe-harbor mechanics and three-/six-year record-retention shortcuts are also held. Check this point with one of our partner accountants.

## Filing and payment

For ordinary domestic calendar-year individual **2026** returns the regular filing/payment deadline is **April 15, 2027**. Exceptional relief/foreign/combat deadlines need separate review. [IRS individual tax filing](https://www.irs.gov/individual-tax-filing); [§6072(a)](https://uscode.house.gov/us/usc/t26/s6072/)

For **2025**, the ordinary filing deadline was April 15, 2026; a timely Form 4868 gave six months, ordinarily to October 15, 2026. Those dates have passed as of this read date. Filing extension did not extend payment; unpaid tax bears interest from the original due date. Late filing, special relief and amendments: Check this point with one of our partner accountants. [2025 Form 1040 filing/extension instructions](https://www.irs.gov/instructions/i1040gi)

The old two-line Schedule 1 wash is not the current method: IRS common-situations FAQ Q7 describes 8z/24z or same-line netting for 2022/2023 and the top entry from tax years beginning in 2024. A stale FAQ example still showing 8z/24z does not override the specific 2025 form instructions. Exact 2026 form positions remain held. [Common-situations Q7](https://www.irs.gov/newsroom/form-1099-k-faqs-common-situations); [2025 Form 1040](https://www.irs.gov/instructions/i1040gi)

## Completion checklist

- [ ] Every form/account/year is reconciled from transaction records; separate receipts are retained and true duplicates removed once.
- [ ] Personal basis, rental/hobby status, cash back, tax bearer, fees, returns and timing are supported; no missing-fact default has been used.
- [ ] Withholding credit and current/prior-year TPSO facts are checked; tips are not added to Box 1a twice.
- [ ] The relevant year's final return instructions control line positions; 2026 held mappings and historical HOLD cases have not been used to file.
- [ ] Keep forms, bridge, records and correction correspondence; respond to notices by their own dates. Unresolved retention/limitation periods require professional advice.

## Sources

| Official source | Scope actually read / applicability | Read on |
|---|---|---|
| [P.L. 119-21](https://www.govinfo.gov/content/pkg/PLAW-119publ21/html/PLAW-119publ21.htm) | Read for: §70432(a) threshold/restoration, (b) withholding/prior-year exception/effective date; §70110 permanent miscellaneous-deduction restriction and redesignation | 2026-11-27 |
| [26 USC 6050W, 2024 edition](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleF-chap61-subchapA-partIII-subpartB-sec6050W.htm) | Read for: (f) furnishing deadline and ARPA effective-date note only; old (e) USD 600 text superseded by §70432 | 2026-11-27 |
| [26 USC 7503](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleF-chap77-sec7503.htm) | Read for: Weekend/legal-holiday rule; calendar recomputed | 2026-11-27 |
| [K instructions, labelled 12/2026](https://www.irs.gov/instructions/i1099k) | Read for: Definitions, coordination regardless of threshold, boxes 1a–1d, 4 and shared reporting boundaries | 2026-11-27 |
| [General K FAQs](https://www.irs.gov/newsroom/form-1099-k-faqs-general-information) | Read for: Q2–Q5 card/TPSO/voluntary/state distinctions, Q7 taxable-income independence | 2026-11-27 |
| [What to do with K](https://www.irs.gov/businesses/what-to-do-with-form-1099-k) | Read for: Gross amounts, personal items, corrections, shared terminals/entity changes, cash back and multiple businesses | 2026-11-27 |
| [Receive-K FAQs](https://www.irs.gov/newsroom/form-1099-k-faqs-what-to-do-if-you-receive-a-form-1099-k) | Read for: Q1–Q4 classification/gifts/corrections; stale two-line example reconciled to 2025 form | 2026-11-27 |
| [Common-situations FAQ](https://www.irs.gov/newsroom/form-1099-k-faqs-common-situations) | Read for: Q7 2022/2023 versus 2024-onward Schedule 1 method | 2026-11-27 |
| [Schedule C, 2025](https://www.irs.gov/instructions/i1040sc) | Read for: Accounting method; lines 1, 2, 6, 23, gross/NEC statement/returns/buyer versus seller tax; 2026 line positions not certified | 2026-11-27 |
| [26 USC 67(h)](https://uscode.house.gov/us/usc/t26/s67/) | Read for: permanent miscellaneous deduction disallowance and 2025 amendment effective date | 2026-11-27 |
| [26 USC 162(a)](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap1-subchapB-partVI-sec162.htm) | Read for: Ordinary/necessary business expenses; Case B assumes eligible current expenses | 2026-11-27 |
| [Form 1040, 2025](https://www.irs.gov/instructions/i1040gi) | Read for: Schedule 1 error/loss entry and examples, line 8j/self-employment distinction; 2025 filing/extension and nonemployee tip-record transition only | 2026-11-27 |
| [Form 8949, 2025](https://www.irs.gov/instructions/i8949) | Read for: Basis/holding-period/selling-cost and personal-loss adjustment instructions; exact 2026 positions held | 2026-11-27 |
| [Reg. 1.183-2](https://www.ecfr.gov/current/title-26/section-1.183-2), [26 USC 183(d)](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap1-subchapB-partVI-sec183.htm) | Read for: Objective profit facts, all nine factors/no single factor; consecutive-year and horse presumption | 2026-11-27 |
| [Backup withholding](https://www.irs.gov/businesses/small-businesses-self-employed/backup-withholding) | Read for: 24%, TINs, triggers/resolution and income-year credit | 2026-11-27 |
| [Digital assets](https://www.irs.gov/filing/digital-assets), [2026 DA instructions](https://www.irs.gov/instructions/i1099da) | Read for: Custody/timing/broker relief, covered/noncovered security definition and basis reporting | 2026-11-27 |
| [CP2000](https://www.irs.gov/individuals/understanding-your-cp2000-series-notice), [26 USC 6662(a)–(b)](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleF-chap68-subchapA-partII-sec6662.htm) | Read for: Notice response/amendment; affected-underpayment 20% penalty trigger, not a penalty determination | 2026-11-27 |
| [Individual filing](https://www.irs.gov/individual-tax-filing), [26 USC 6072(a)](https://uscode.house.gov/us/usc/t26/s6072/) | Read for: Ordinary calendar-year 2026 deadline; specific relief excluded | 2026-11-27 |

Not yet confirmed: exact 2026 Form 1040/Schedule 1/Schedule C/Form 8949 filing positions; specific state, foreign/entity/issuer, crowdfunding, collectibles, hobby COGS, tip-deduction eligibility and historical HOLD outcomes named above. These are non-usable holds. Check this point with one of our partner accountants.
