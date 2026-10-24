---
name: fi-corporate-income-tax
description: >
  Prepare Finnish corporate income-tax workpapers for tax year 2026 for ordinary
  limited liability companies and cooperatives. Reconcile accounting results to the
  tax base, apply the current corporate rate, check confirmed loss vintages and
  ownership changes, and distinguish return filing from prepayments. Use for Finnish
  corporate tax, Form 6B, loss carryforward, ownership-change screening, corporate
  tax-year allocation and outbound-payment triage. Includes primary-source links,
  read dates and executable arithmetic examples. It does not complete participation
  exemptions, financing restrictions, reorganisations, group relief, international
  minimum tax, treaty eligibility, live filing or named Finnish accountant review.
jurisdiction: FI
tax_year: 2026
last_updated: 2026-10-23
review_status: pending_review
trust_label: Built by Michael Cutajar and the OpenAccountants team
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
version: 1.2
category: international
---

# Finland corporate income tax v1.2

## Who this applies to

Use this source-cited draft for ordinary Finnish limited liability companies and registered cooperatives. They are separate taxpayers: corporate tax does not itself settle shareholders' taxes on salary, dividends or other benefits. Identify the legal entity and tax year before using a computation. [Vero corporate income tax][income]

Tax residence and a permanent establishment are separate questions. A foreign entity's Finnish registration for one purpose does not settle every tax obligation. Collect incorporation, effective-management, activity and treaty evidence before using the domestic-company computation. [Corporate residence guidance][residence]

## Rates, bands and thresholds

| Item | Current preparation rule | Official source |
|---|---|---|
| Ordinary corporate income-tax rate for 2026 | 20% of established taxable income | [Vero corporate tax][income] |
| Confirmed loss carryforward | Next 10 tax years, subject to source and ownership conditions | [Vero losses][losses] |
| Corporate prepayment minimum | EUR 500; below this, collected in final assessment | [Prepayment instalments][instalments] |
| Ordinary corporate prepayments of EUR 500–2,000 | Two equal instalments, in the third and ninth accounting-period months | [Prepayment instalments][instalments] |
| Ordinary corporate prepayments over EUR 2,000 | Twelve equal instalments under the decision | [Prepayment instalments][instalments] |

The official future-changes page describes an **18% corporate rate and 25-year business-loss period as proposals**. Those figures do not replace the 2026 computation. Check enactment, commencement and transition rules before preparing any later tax year. [Vero changes in taxation][changes]

Income Tax Act sections 124, 119 and 122 confirm the current rate, loss period and ownership restrictions. The listed-company exception has its own unlisted-share ownership test; listing is not a blanket exemption. A loss-use permit also has group-contribution limits under section 122(4). [Income Tax Act][income-law]

## Establish the base

Bridge the accounting result to taxable income by income source, with evidence for additions, exclusions, depreciation and other timing differences. Vero distinguishes business and agricultural sources; ordinary limited companies/cooperatives no longer have a separate personal source. Allowed earlier losses are deducted in the appropriate source before the taxable amounts are combined. [Vero corporate tax][income]

Use separate book and tax columns. Income tax booked as an expense, public-law fines and specified tax penalties/interest require non-deductible-cost treatment in Form 6B; do not infer that every accounting expense is deductible. Participation income, related-party support, reserves and asset write-downs need their specific rules. [Form 6B instructions, non-deductible costs][form6b]

The workpaper should identify the ledger amount, adjustment, source, period, return field and supporting document for each difference. The examples assume those legal classifications have already been established; they are not a deduction engine.

## Losses and ownership changes

Use authority-confirmed tax losses rather than an accounting retained-loss balance. Keep a source-by-source vintage schedule, remaining life and prior use. Vero describes automatic deduction over the next ten tax years. [Loss guidance][losses]

A direct or indirect transfer of **more than 50%** of shares during or after the loss year can forfeit loss deductions; inheritance/testament transfers and listed-company cases have separate rules. An indirect test involves a shareholder with at least 20% ownership whose own majority changes. A special permit can preserve loss use. The screen is not satisfied just because the immediate shareholder list is unchanged. Check the complete history and any permit before using the balance. [Loss guidance][losses]

## Deadlines and filing

File Form 6B within **four months after the end of the calendar month in which the accounting period ends**. For a period ending 15 March 2026, the ordinary deadline is 31 July 2026, subject to business-day rules. File electronically under the applicable rules and preserve the receipt. An extension request and its outcome must be tracked separately. [Corporate return page][return]; [Foreign-business filing example][foreign]

Vero requires a separate return for each accounting period ending in a calendar year and combines those periods for the tax year. For instance, periods ending in March and December 2026 both belong to tax year 2026. Do not replace the separate filing obligations with one combined return. [Corporate tax-year guidance][income]

Review filing even for an inactive company: taxable income, expenses, assets, liabilities or other tax-relevant events trigger the return requirement, and an authority filing request must be followed. [Corporate return page][return]

Prepayments are payments toward the assessment, not deductible operating expenses. Reconcile the decision, actual payments and assessment separately from the return calculation. Use the [prepayments Guide](fi-prepayments.md) for forecast changes and payment preparation. [Corporate tax guidance][income]

## Penalties and interest

Vero's corporate summary distinguishes a **EUR 100 late-filing penalty** for relevant reporting before assessment finishes from a punitive increase for omissions remaining at completion. The latter has a **EUR 150 minimum**; the summary describes a 0.5–10% route based on increased income, with circumstances determining the percentage and whether a charge is waived. Check the notice, assessment end date and statutory basis rather than automatically charging every correction. [Corporate sanctions][sanctions]

Ordinary late-paid corporate tax uses the official **9.5% annual late-payment rate in 2026**. Reduced interest on additional prepayments/back taxes is separate. Use the actual tax type and dates in the official calculator/MyTax. [Interest calculator][interest]

## Cross-border and outbound payments

Determine residence, Finnish-source income and any PE attribution before selecting the return or withholding route. The [transfer-pricing Guide](fi-transfer-pricing.md) and [CbCR Guide](fi-country-by-country-reporting.md) address separate documentation/reporting screens; neither establishes an arm's-length price or PE result. [Corporate residence guidance][residence]

For nonresident recipients, Vero's dividend/interest/royalty guidance distinguishes ordinary corporate dividend source tax of 20% from individual taxation, treaty/EU relief and special cases. Unidentified recipients of nominee-registered listed shares can require 35%; identification insufficient to establish corporate status can instead lead to 30%. Most qualifying nonresident interest is domestically exempt, but this is not a universal exemption for every financing payment. Classify the instrument, recipient, PE connection and evidence before withholding. Royalty, treaty, beneficial-owner and relief procedures remain open here. [Nonresident investment-income guidance][outbound]

## Worked examples

### 1. Bridge from book profit to tax

Assume EUR 100,000 book profit before income tax, EUR 5,000 verified non-deductible costs, EUR 2,000 verified exempt income and EUR 20,000 deductible confirmed losses in the correct source, with no other adjustments. Taxable income is EUR 83,000 and 2026 income tax is EUR 16,600. All legal classifications are assumptions.

```oa-check
name: Finland assumed corporate book to tax bridge
inputs:
  book_profit_before_income_tax: 100000
  established_nondeductible_costs: 5000
  established_exempt_income: 2000
  usable_confirmed_losses: 20000
  corporate_rate: 0.20
steps:
  adjusted_profit: book_profit_before_income_tax + established_nondeductible_costs - established_exempt_income
  taxable_income: adjusted_profit - usable_confirmed_losses
  corporate_income_tax: taxable_income * corporate_rate
expected:
  adjusted_profit: 103000
  taxable_income: 83000
  corporate_income_tax: 16600
```

### 2. Loss limitation and remaining balance

Assume an unexpired, fully usable same-source loss of EUR 80,000 and current adjusted profit of EUR 50,000. Use EUR 50,000, leaving EUR 30,000 subject to its original remaining life. No new ten-year period starts because some loss was used. This assumes ownership and other restrictions have already been cleared.

```oa-check
name: Finland assumed corporate loss balance
inputs:
  confirmed_available_loss: 80000
  adjusted_same_source_profit: 50000
  corporate_rate: 0.20
steps:
  loss_used: min(confirmed_available_loss, adjusted_same_source_profit)
  remaining_loss: confirmed_available_loss - loss_used
  taxable_income: adjusted_same_source_profit - loss_used
  corporate_income_tax: taxable_income * corporate_rate
expected:
  loss_used: 50000
  remaining_loss: 30000
  taxable_income: 0
  corporate_income_tax: 0
```

### 3. Tax versus payments already made

Assume established 2026 taxable income of EUR 100,000 and credited prepayments of EUR 16,000. The principal reconciliation shows EUR 4,000 still uncovered. Interest, other credits, due dates and the assessment decision require separate checks; this is not an instruction to send that amount without a decision/reference.

```oa-check
name: Finland assumed corporate assessment payment reconciliation
inputs:
  established_taxable_income: 100000
  corporate_rate: 0.20
  credited_prepayments: 16000
steps:
  computed_income_tax: established_taxable_income * corporate_rate
  principal_uncovered: computed_income_tax - credited_prepayments
expected:
  computed_income_tax: 20000
  principal_uncovered: 4000
```

## Ask the client first

- Which entity, tax residence and accounting periods are involved?
- What supports the book-to-tax differences, income sources and deductions?
- Which tax-loss decisions, ownership changes and permits exist?
- What domestic/foreign group, financing, PE or restructuring facts apply?
- Who receives each outbound payment, and what supports classification and relief?
- Which return, prepayment decision, credited payments and assessment notices exist?

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

## Sources and review limits

Read on 23 October 2026. Corporate tax, loss, return and sanctions pages were opened directly. Detailed Form 6B, nonresident-income and instalment passages were retrieved as indexed official text. Income Tax Act sections 9, 119, 122 and 124 were subsequently read from direct official HTML statutory content; the retrieval hashes are in the country research record. The current authority summary distinguishes future proposals from current rules. Full statutory/amendment reconciliation remains open.

- [Corporate income tax][income]; [losses and ownership][losses].
- [Income Tax Act][income-law], selected sections listed above. The displayed section 9(3) amendment referring to new section 9b commences on 1 January 2027; it is not the applicable 2026 wording.
- [Corporate return][return]; [Form 6B instructions][form6b]; [foreign-business filing example][foreign].
- [Instalment table][instalments]; [corporate sanctions][sanctions]; [interest calculator][interest].
- [Corporate residence][residence]; [nonresident investment income][outbound]; [future changes][changes].

Not yet confirmed: complete current legal chain; participation exemptions, interest restrictions, group relief, restructurings, incentives, CFC/exit/minimum-tax rules; treaty/EU entitlement and withholding procedures; detailed PE attribution and foreign relief; exceptional entity and source cases; live filing; named Finnish accountant review. Corporate and cross-border domains remain partial.

[income]: https://www.vero.fi/en/businesses-and-corporations/taxes-and-charges/limited-companies-and-cooperatives/income-tax/
[income-law]: https://www.finlex.fi/fi/lainsaadanto/1992/1535
[losses]: https://www.vero.fi/en/businesses-and-corporations/taxes-and-charges/limited-companies-and-cooperatives/income-tax/losses/
[return]: https://www.vero.fi/en/businesses-and-corporations/taxes-and-charges/limited-companies-and-cooperatives/tax-return/
[form6b]: https://www.vero.fi/en/businesses-and-corporations/taxes-and-charges/limited-companies-and-cooperatives/tax-return/instructions_for_completing_the_income_tax_return/
[foreign]: https://www.vero.fi/en/businesses-and-corporations/business-operations/foreign-business-in-finland/income-tax/
[instalments]: https://www.vero.fi/en/businesses-and-corporations/taxes-and-charges/tax-prepayment/instructions-for-making-prepayments/how-many-instalments/
[sanctions]: https://www.vero.fi/en/businesses-and-corporations/taxes-and-charges/limited-companies-and-cooperatives/tax-return/Late-filing-penalty-and-punitive-tax-increase/
[interest]: https://vero.fi/en/businesses-and-corporations/taxes-and-charges/payments/interest-on-late-payments/interest-calculator/
[residence]: https://www.vero.fi/en/detailed-guidance/guidance/95551/resident-and-nonresident-tax-liability-of-corporate-entities5/
[outbound]: https://www.vero.fi/en/detailed-guidance/guidance/49133/payments-of-dividends-interest-and-royalties-to-nonresidents3/
[changes]: https://www.vero.fi/en/About-us/newsroom/changes-in-taxation/
