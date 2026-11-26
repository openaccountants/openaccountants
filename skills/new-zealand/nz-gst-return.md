---
name: nz-gst-return
description: Use this skill whenever asked about New Zealand GST returns, or to prepare, review, or classify transactions for a New Zealand GST return (GST101A form), for a self-employed individual or small business. Trigger on phrases like "prepare GST return", "do the GST", "fill in GST101A", "create the return", "New Zealand GST", "NZ GST", "GST return", "GST101A", "GST rate NZ", "input tax", "output tax", "zero-rated", "GST registration", "taxable supply", "IRD GST", "myIR GST", or any question about GST filing for sole traders in New Zealand. Also trigger when classifying transactions for GST purposes from bank statements, invoices, or other source data. Covers the 15% standard rate, zero-rated and exempt supplies, $60K registration threshold, invoice and payments basis, and GST101A return preparation. ALWAYS read this skill before touching any NZ GST work.
version: "2.7"
jurisdiction: NZ
tax_year: 2026
last_updated: 2026-11-26
depends_on:
  - vat-workflow-base
category: international
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
tier: 2
domain: vat-gst
type: situation-rules
---

# New Zealand GST return: prepare and reconcile (2026)

## Who this applies to

For New Zealand small-business GST work. Amounts are NZD. Use the registered taxable period, accounting basis and due date shown in myIR; do not infer them from the bank-statement dates. Sources below were read on 26 November 2026. Special cases have explicit referrals rather than filing instructions.

## Rates, bands and thresholds

### Rate and registration

The standard rate is **15%** ([IRD: what GST is](https://www.ird.govt.nz/gst/what-gst-is)). Add 15% to a GST-exclusive price; extract **3/23** from a standard-rated GST-inclusive price. Thus $100 plus $15 GST is $115; $115 contains $15 GST. Zero-rating and reduced-value treatments need their own conditions. [IRD calculation examples](https://www.ird.govt.nz/gst/filing-and-paying-gst-and-refunds/calculating-your-gst).

For a person carrying on a taxable activity, test supplies across **all** their taxable activities against **$60,000**, looking backwards and forwards over 12 months. IS 25/21 describes the statutory test as **exceeding** $60,000. A taxable activity involves continuous or regular activity supplying, or intending to supply, goods and services for consideration, whether or not for profit. A person with a taxable activity can register voluntarily below the threshold. [IS 25/21, paragraphs 8, 11 and 66–70](https://www.taxtechnical.ird.govt.nz/-/media/project/ir/tt/pdfs/interpretation-statements/2025/is-25-21.pdf); [IR375, page 4](https://www.ird.govt.nz/-/media/project/ir/home/documents/forms-and-guides/ir300---ir399/ir375/ir375.pdf).

Apply the registration provisos before concluding registration is compulsory:

- The past threshold was exceeded but the Commissioner is satisfied the next 12 months will not exceed $60,000.
- The Commissioner is satisfied the threshold is exceeded solely because of ending, prematurely ending, or substantially and permanently reducing a taxable activity. A subdivision's intended sale proceeds are not automatically a cessation exception.
- The Commissioner is satisfied the threshold is exceeded solely because of replacing plant or another capital asset used in a taxable activity.

For a contested taxable-activity or exact-threshold case, charging GST while unregistered, voluntary-registration consequences, or cancellation: **Check this point with one of our partner accountants.** Do not treat adding GST to a price as an ordinary registration application.

## The base

### Accounting basis and period

Confirm the registered basis and period from the registration record. IRD's defaults if none was chosen are invoice basis and 2-monthly filing aligned to the balance date. Do not change either before IRD confirms the change. [IR375, page 6](https://www.ird.govt.nz/-/media/project/ir/home/documents/forms-and-guides/ir300---ir399/ir375/ir375.pdf).

For ordinary supplies, subject to the special-supply referral below:

| Basis | Sales | Eligible purchases, with taxable supply information held |
| --- | --- | --- |
| Payments | Amounts received in the period | Amounts paid in the period |
| Invoice | Amounts invoiced; if any payment precedes the invoice, the full sale price at that earlier time | Amounts paid or invoiced by suppliers, even if not fully paid |
| Hybrid | Invoice basis | Payments basis |

[IRD: calculating your GST](https://www.ird.govt.nz/gst/filing-and-paying-gst-and-refunds/calculating-your-gst); [IRD: accounting bases](https://www.ird.govt.nz/gst/registering-for-gst/which-gst-accounting-basis-and-filing-frequency-should-i-use).

For eligibility or compulsory changes of basis/frequency, seasonal or group tests, large single supplies, split agreements or hire purchase: **Check this point with one of our partner accountants.** This referral replaces the old threshold tables and exceptions; do not apply the ordinary timing table to a special supply without resolving it.

### Purchase evidence and taxable use

A GST-registered business can claim GST charged on purchases used to make taxable supplies, subject to evidence and taxable-use limits. Do not claim for private or exempt use. An unregistered supplier normally charges no GST; secondhand goods are a separate exception requiring review. [IRD: claiming GST](https://www.ird.govt.nz/gst/claiming-gst).

Taxable supply information (TSI) can be held across invoices, agreements, contracts and bank records. A record headed “tax invoice” need not be discarded. For supplies over $200, provide TSI to a GST-registered buyer within **28 days of a request**, or an alternative date agreed by the parties. [IRD: TSI](https://www.ird.govt.nz/gst/tax-invoices-for-gst/how-taxable-supply-information-for-gst-works).

| GST-inclusive supply | Required information for an ordinary standard-rated supply | Source |
| --- | --- | --- |
| $200 or less | Seller's name/trade name, invoice date (or time of supply if no invoice), description and consideration. Both parties keep records; seller need not provide TSI to the buyer. | https://www.ird.govt.nz/-/media/project/ir/home/documents/forms-and-guides/ir300---ir399/ir375/ir375.pdf |
| More than $200 and up to $1,000 | Above, plus seller's GST number; show exclusive amount, GST and inclusive amount, or inclusive amount and a statement that all listed supplies include GST at the standard rate. | https://www.ird.govt.nz/-/media/project/ir/home/documents/forms-and-guides/ir300---ir399/ir375/ir375.pdf |
| More than $1,000 | Above, plus a GST-registered buyer's name and at least one identifier: address, phone, email, different trading name, NZBN or website. | https://www.ird.govt.nz/-/media/project/ir/home/documents/forms-and-guides/ir300---ir399/ir375/ir375.pdf |

[IR375, pages 8–10](https://www.ird.govt.nz/-/media/project/ir/home/documents/forms-and-guides/ir300---ir399/ir375/ir375.pdf). Obtain the required evidence before claiming. For apportionment versus principal-purpose elections, change-of-use periods, tolerances, wash-up, asset disposal or non-taxable elections: **Check this point with one of our partner accountants.**

### Classification and adjustments

Exempt supplies stay out of the GST return and costs relating to them cannot be claimed. Ordinary residential dwelling rent and financial services such as interest and bank fees are examples; determine the actual service before applying an exemption to a fee. [IR375, page 7](https://www.ird.govt.nz/-/media/project/ir/home/documents/forms-and-guides/ir300---ir399/ir375/ir375.pdf); [IRD: exemptions](https://www.ird.govt.nz/gst/charging-gst/exempt-supplies).

- **Customs GST:** eligible GST paid to Customs on imported goods goes in credit adjustments, not ordinary purchases. Invoice basis: earlier of invoice or payment; payments/hybrid: when paid. Confirm taxable-use eligibility and import evidence. [IRD: credit adjustments](https://www.ird.govt.nz/gst/gst-adjustments/other-gst-credit-adjustments).
- **Bad debt:** if GST on the supply was already accounted for and the debt is written off, claim the credit in the write-off period; for a fully standard-rated debt use 3/23 of the amount written off. Retain recovery records. A debt never returned under payments basis gives no ordinary bad-debt credit; special agreements need review. [IRD: credit adjustments](https://www.ird.govt.nz/gst/gst-adjustments/other-gst-credit-adjustments).
- **Recovery:** after a bad-debt GST deduction, include 3/23 of the recovered standard-rated amount as a debit adjustment. [IRD: debit adjustments](https://www.ird.govt.nz/gst/gst-adjustments/other-gst-debit-adjustments).
- **Entertainment:** for business entertainment already claimed during the year, make an annual debit adjustment of 15% of the GST-exclusive income-tax non-deductible amount. Private entertainment is not claimable. Organisations not liable for income tax do not make this adjustment. Resolve income-tax deductibility separately. [IR375, page 34](https://www.ird.govt.nz/-/media/project/ir/home/documents/forms-and-guides/ir300---ir399/ir375/ir375.pdf); [IRD: debit adjustments](https://www.ird.govt.nz/gst/gst-adjustments/other-gst-debit-adjustments).

Entertainment adjustment timing: without a tax agent, use the return covering the earlier of the income-tax due date and filing date. With an agent and no extension, use the earlier of filing and 31 March after the income-tax due date. With an agent's extension, use the return covering actual filing. [IRD: timing](https://www.ird.govt.nz/gst/gst-adjustments/other-gst-debit-adjustments).

### Listed services through online marketplaces

For qualifying listed services performed, provided or received in New Zealand through an online marketplace, the marketplace collects GST. Listed services include ride-sharing, food/beverage delivery and short-stay/visitor accommodation, plus closely connected services sold through the marketplace. Confirm the platform is a marketplace rather than the direct service supplier. [IRD: listed services](https://www.ird.govt.nz/sharing-economy/sellers-of-listed-services/gst-for-listed-services).

- For an **unregistered seller**, the marketplace collects 15%, pays 6.5% to IRD and passes 8.5% to the seller as a flat-rate credit (percentages of the GST-exclusive supply value). A listing intermediary may administer the credit for accommodation. [IRD: flat-rate credit scheme](https://www.ird.govt.nz/sharing-economy/listing-intermediary-rules/flat-rate-credit-scheme).
- A **registered seller** includes qualifying listed supplies through a GST-registered marketplace as zero-rated sales and can claim eligible GST on costs. Tell the marketplace the registration status and any change. Return a flat-rate credit received while registered as a debit adjustment.
- **Direct bookings** follow normal rules: a registered host's taxable direct stays are standard-rated. Do not charge GST for an unregistered host solely because a booking is direct.

Use the gross consideration for the qualifying supply, reconciled to fees and payouts; do not automatically use the net deposit. For opt-outs, asset sales, long stays or income-tax treatment of flat-rate credits: **Check this point with one of our partner accountants.**

## Complete the return

GST101A is for a person not liable for provisional tax; the GST103 series is for a person liable for provisional tax. Confirm the issued form. The common GST calculation is below. [IR375, pages 11–15](https://www.ird.govt.nz/-/media/project/ir/home/documents/forms-and-guides/ir300---ir399/ir375/ir375.pdf).

| Boxes | Entry or calculation |
| --- | --- |
| 1–4 | Check registration number, period and contact details. Correct preprinted address/phone as necessary; complete the details if not preprinted or filing online. |
| 5–8 | Box 5: taxable sales including GST and zero-rated supplies; Box 6: zero-rated part; Box 7 = 5 − 6; Box 8 = 7 × 3/23. Exempt receipts stay out. |
| 9–10 | Box 9: evidenced debit adjustments; Box 10 = 8 + 9. |
| 11–12 | Box 11: GST-inclusive eligible purchase base, with evidence and taxable-use allocation, excluding imported goods; Box 12 = 11 × 3/23. Never extract GST from exempt or zero-rated purchases. |
| 13–14 | Box 13: evidenced credit adjustments, including eligible Customs GST and bad-debt credits; Box 14 = 12 + 13. |
| 15 | Difference between 10 and 14: payment if 10 is larger, refund if 14 is larger. Equal means nil, but still file. Keep the signed balance in the workpaper and use the form's refund/payment indicator. |

Have the responsible person read and sign the paper declaration. Keep business records supporting the return for **7 years**. [IR375, pages 8 and 12–13](https://www.ird.govt.nz/-/media/project/ir/home/documents/forms-and-guides/ir300---ir399/ir375/ir375.pdf).

## Deadlines and filing

File a return for every taxable period, including nil periods. Normally file and pay by the **28th of the following month**; periods ending **31 March** are due **7 May**, and those ending **30 November** are due **15 January**. Weekend/public-holiday due dates move to the next working day. Use the actual myIR due date and refer any proposed special variation. Filing is available in myIR, supported accounting software or on paper. [IRD: filing](https://www.ird.govt.nz/gst/filing-and-paying-gst-and-refunds/filing-gst); [IR375, page 6](https://www.ird.govt.nz/-/media/project/ir/home/documents/forms-and-guides/ir300---ir399/ir375/ir375.pdf).

## Penalties and interest

Ordinary late-payment penalties are **1% the day after the due date**, then **4% on the remaining tax including penalties on the seventh day**. The monthly 1% penalty does not apply to GST. First lateness in a 2-year period may have a notified grace period; check the notice and payment history before calculating a penalty. [IRD: late payment](https://www.ird.govt.nz/managing-my-tax/penalties-and-interest/penalties-and-debt/late-payment-penalties).

For late-filing penalties and their payment dates, grace-period entitlement, interest rates/minimums, default assessments, refund timing, return corrections, late input deductions, disputes and NOPA deadlines: **Check this point with one of our partner accountants.** Do not use the old historical interest-rate table for a current calculation. A late filing does not by itself prove tax was paid late.

## Cross-border points

These topics remain in scope for identification, but do not have a filing rule here:

| Topic | Action |
| --- | --- |
| Exports, non-resident services, remote services, international transport, foreign-currency rule uncertainty and low-value imports | Check this point with one of our partner accountants. |
| Going concerns, land transactions, residential head leases, long-rented dwelling sales, commercial-dwelling long stays, private-asset sales and body corporate levies | Check this point with one of our partner accountants. |
| Secondhand goods (including associated sellers, records, payment, valuation, return box and later export), imported-services reverse charge and associated-party pricing | Check this point with one of our partner accountants. |
| Insurance payouts, barter, financial-services zero-rating elections, GST groups, non-profit donated goods and fringe benefits | Check this point with one of our partner accountants. |
| Mixed-use holiday homes, boats/aircraft, land, non-taxable elections and all unresolved asset-use adjustments | Check this point with one of our partner accountants. |
| Income-tax issues: entertainment deductibility, flat-rate credit treatment, vehicle logbooks and provisional tax | Check this point with one of our partner accountants. |
| Returns still outstanding for 2025–26 | Check this point with one of our partner accountants. |

## Two worked examples that recompute

The following seven cases preserve the original fact patterns; Cases 3 and 5 stop at a referral.

### 1. Forward registration test

The landscaper's sales for the 12 months to **31 August 2026** were **$52,000**. On **1 September 2026**, a new contract makes expected sales **$75,000** for the next 12 months. The past amount is below $60,000; the forward amount exceeds it. Registration is required assuming no proviso above applies. If exceeding the threshold instead arose solely from replacing the old trailer and mower, apply the capital-replacement proviso only if the Commissioner is satisfied. [IS 25/21, paragraphs 66–70](https://www.taxtechnical.ird.govt.nz/-/media/project/ir/tt/pdfs/interpretation-statements/2025/is-25-21.pdf).

### 2. Tools bought for $920

A registered payments-basis plumber pays **$920 including GST** in the period for tools used wholly for taxable work. Hold the TSI for the over-$200/up-to-$1,000 band. GST is **$120**: $920 × 3/23. Put $920 in Box 11; Box 12 includes $120. If unpaid, payments basis waits; on invoice basis an invoice and the required TSI can support the claim before payment. [IRD: calculation and timing](https://www.ird.govt.nz/gst/filing-and-paying-gst-and-refunds/calculating-your-gst).

```oa-check
name: Tools purchase, GST inside the price
inputs:
  price: 920
steps:
  - gst: price * 3 / 23
expected:
  gst: 120.00
```

### 3. Overseas advice: resolve zero-rating first

An Auckland consultant invoices a Sydney company **$8,500** for advice. The company has no New Zealand presence and its staff remained in Australia. If staff instead attended Auckland workshops, that also needs review. These facts alone do not settle every zero-rating condition, including connections to land/goods and the actual recipient. **Check this point with one of our partner accountants.** Keep the $8,500 unresolved until classification is established; do not automatically put it in Box 6.

### 4. Marketplace accommodation

A host supplies **3-night stays** through a qualifying GST-registered marketplace. The GST-exclusive accommodation value is **$2,000**, before marketplace fees. For an unregistered host, GST is $300; IRD receives $130 and the host receives a $170 flat-rate credit. For a registered host, report the $2,000 qualifying supply in Boxes 5 and 6; eligible costs remain claimable. A flat-rate credit wrongly received while registered is a debit adjustment. Apply the direct-booking rule above separately. [IRD: listed services](https://www.ird.govt.nz/sharing-economy/sellers-of-listed-services/gst-for-listed-services).

```oa-check
name: Marketplace supply for an unregistered host
inputs:
  exclusive_value: 2000
steps:
  - gst: exclusive_value * 0.15
  - ird: exclusive_value * 0.065
  - host: exclusive_value * 0.085
expected:
  gst: 300.00
  ird: 130.00
  host: 170.00
```

### 5. Partly claimed van: establish previous use

A registered builder claimed **70%** of the GST on a van and sells it for **$23,000 including GST**. The original deduction percentage alone does not establish the applicable previous-use percentage at disposal or all disposal conditions. **Check this point with one of our partner accountants.** Preserve the acquisition and adjustment history; do not issue the former $900 credit calculation as filing-ready.

### 6. Entertainment

The company spent **$2,300 including GST** on business client dinners in **2026–27**, claimed during the year. The case stipulates that these dinners are **50% deductible for income tax**, not private entertainment. Exclusive cost is $2,000; the non-deductible part is $1,000; the annual debit adjustment is **$150**. Apply the agent/extension timing above. The stipulated 50% is not a conclusion about every dinner. [IR375, page 34](https://www.ird.govt.nz/-/media/project/ir/home/documents/forms-and-guides/ir300---ir399/ir375/ir375.pdf).

```oa-check
name: Entertainment with stipulated 50 percent deductibility
inputs:
  inclusive_cost: 2300
  non_deductible_share: 0.5
steps:
  - exclusive_cost: inclusive_cost * 20 / 23
  - non_deductible_cost: exclusive_cost * non_deductible_share
  - debit: non_deductible_cost * 0.15
expected:
  exclusive_cost: 2000.00
  non_deductible_cost: 1000.00
  debit: 150.00
```

### 7. Bad debt and separate late payment

An invoice-basis trader already returned GST on a fully standard-rated **$1,150** sale, then writes the insolvent customer's debt off. The credit is **$150** in Box 13 in the write-off period. If the full $1,150 is later recovered, the debit adjustment is $150 in Box 9. Keep recovery records. [IRD: credits](https://www.ird.govt.nz/gst/gst-adjustments/other-gst-credit-adjustments); [IRD: debits](https://www.ird.govt.nz/gst/gst-adjustments/other-gst-debit-adjustments).

Separately, **$4,000** GST for the period ending **30 September 2026** is due **28 October 2026** and remains unpaid. Assuming the ordinary penalties apply, with no grace period, relief, revised due date or intervening payment: $40 on 29 October; $161.60 (4% of $4,040) on 4 November; total penalties **$201.60**, excluding interest. Interest needs a separate determination. [IRD: late payment](https://www.ird.govt.nz/managing-my-tax/penalties-and-interest/penalties-and-debt/late-payment-penalties).

```oa-check
name: Ordinary late GST payment penalties, no relief or grace period
inputs:
  gst: 4000
steps:
  - first: gst * 0.01
  - second: (gst + first) * 0.04
  - total: first + second
expected:
  first: 40.00
  second: 161.60
  total: 201.60
```

## Ask the client first

Read the available records before asking for missing information. Obtain registration status and effective date, entity, taxable activities, past and expected sales, basis, frequency, balance date and provisional-tax status. Identify overseas customers, marketplace and direct sales, private use, imports, secondhand purchases, associated parties, entertainment and bad debts.

Bank-statement practice originally folded in from Ryan Duguid's `new-zealand-gst` remains an evidence-gathering workflow. A supplier name or bank narration is never enough to establish GST. Inspect the actual export columns, date format, debit signs and all narration/reference fields. Do not assume a bank's column layout or a fixed field length.

Reconcile every receipt and payment to a supported return line, an exclusion or a separately listed unresolved item. Establish the supply, counterparty, GST treatment, evidence, taxable use and timing. Review prior returns, duplicates, refunds, reversals, unpaid invoices and marketplace fees before totalling. Record the NZD conversion method, date, rate and source for foreign-currency items; refer uncertainty about the applicable conversion rule.

Use these prompts for the original supplier-pattern topics:

| Transaction family | Evidence to obtain before classification |
| --- | --- |
| Banks, fintech, card processors and instalment providers | Actual fee or subscription invoice; distinguish interest, principal and services |
| IRD, wages, PAYE, KiwiSaver, student loans, drawings, dividends, own-account transfers and cash withdrawals | Establish the underlying movement; keep any unsupported item unresolved |
| ACC, NZTA, Companies Office, NZBN, ministries and councils | Actual charge, levy, rates or service record and GST treatment; no blanket exclusion |
| Energy, phone, internet, water, software and professional services | Supplier's GST record, actual service and evidenced business/private allocation |
| Insurance | Policy type and invoice; do not infer treatment from the insurer |
| Post, couriers, freight, flights, public transport, ferries and vehicle hire | Route, service, invoice and business purpose |
| Groceries, retail, tools, fuel, vehicle costs and memberships | What was bought, invoice and business purpose; a merchant name proves no deduction |
| Restaurants, cafes and bars | Business/private purpose and entertainment treatment |
| Rent, property and body corporate levies | Nature of supply, lease/levy, supplier status and any special rules |
| Overseas receipts, marketplaces, payments to individuals and large purchases | Underlying supply chain, gross sales/fees, parties, timing and all special conditions |

Hold unsupported purchases without claiming GST. Hold uncertain receipts in the reconciliation rather than inventing a rate. Do not describe an unresolved reconciliation as a nil return or provide filing-ready figures while material items remain unresolved. Keep an adjustment schedule with evidence, legal basis, period and amount. Do not request login credentials or make the user's declaration.

## Completion review

Confirm registration, basis, period, evidence, classification, taxable use, adjustments and due date. Reconcile Boxes 5–15 to the workpaper and all source transactions. Resolve referrals before giving affected filing figures; retain the evidence and filing/payment confirmation.

The inherited reviewer settings are workflow prompts, not legal thresholds: single transaction **NZD 5,000 or more** (high); one conservative default's GST effect **NZD 400 or more** (high); counterparty concentration **more than 40%** (medium); **more than 4** defaults (medium); net GST position **NZD 10,000 or more** (low). They never justify an unsupported return entry.

## Sources

All read 2026-11-26. Inland Revenue material is Crown copyright, reproduced/adapted under [CC BY 4.0](https://www.ird.govt.nz/about-this-site/conditions-of-use/copyright). No endorsement is implied.

| Source | URL | Read |
| --- | --- | --- |
| IR375 GST guide, March 2026. Read for registration, basis defaults, TSI, return boxes, entertainment and record retention | https://www.ird.govt.nz/-/media/project/ir/home/documents/forms-and-guides/ir300---ir399/ir375/ir375.pdf | 2026-11-26 |
| IS 25/21. Read paragraphs 8, 11 and 66–70 for taxable activity, aggregation and registration provisos | https://www.taxtechnical.ird.govt.nz/-/media/project/ir/tt/pdfs/interpretation-statements/2025/is-25-21.pdf | 2026-11-26 |
| Calculating GST. Read for ordinary timing, tax fraction and Case 2 | https://www.ird.govt.nz/gst/filing-and-paying-gst-and-refunds/calculating-your-gst | 2026-11-26 |
| Accounting bases and filing frequency. Read for hybrid timing and frequency context; eligibility referred | https://www.ird.govt.nz/gst/registering-for-gst/which-gst-accounting-basis-and-filing-frequency-should-i-use | 2026-11-26 |
| Claiming GST. Read for taxable use, purchase evidence and unregistered suppliers | https://www.ird.govt.nz/gst/claiming-gst | 2026-11-26 |
| Taxable supply information. Read for request timing and value bands | https://www.ird.govt.nz/gst/tax-invoices-for-gst/how-taxable-supply-information-for-gst-works | 2026-11-26 |
| Exempt supplies. Read for financial services and residential rent | https://www.ird.govt.nz/gst/charging-gst/exempt-supplies | 2026-11-26 |
| Credit adjustments. Read for Customs GST and bad debts | https://www.ird.govt.nz/gst/gst-adjustments/other-gst-credit-adjustments | 2026-11-26 |
| Debit adjustments. Read for recoveries, entertainment and adjustment timing | https://www.ird.govt.nz/gst/gst-adjustments/other-gst-debit-adjustments | 2026-11-26 |
| Listed services. Read for marketplace roles, rates, registration and credit repayment | https://www.ird.govt.nz/sharing-economy/sellers-of-listed-services/gst-for-listed-services | 2026-11-26 |
| Filing GST. Read for due dates, nil returns and filing routes | https://www.ird.govt.nz/gst/filing-and-paying-gst-and-refunds/filing-gst | 2026-11-26 |
| Late payment penalties. Read for initial penalties, monthly exclusion and grace-period caveat | https://www.ird.govt.nz/managing-my-tax/penalties-and-interest/penalties-and-debt/late-payment-penalties | 2026-11-26 |
| What GST is. Read for standard rate | https://www.ird.govt.nz/gst/what-gst-is | 2026-11-26 |
| Flat-rate credit scheme. Read for supply-value base and listing intermediary role | https://www.ird.govt.nz/sharing-economy/listing-intermediary-rules/flat-rate-credit-scheme | 2026-11-26 |
| Change-in-use adjustments. Read for previous use at disposal in referred Case 5 | https://www.ird.govt.nz/gst/gst-adjustments/change-in-use-adjustments-for-gst | 2026-11-26 |

Not yet confirmed: referred topics have no usable filing conclusion in this Guide.
