---
name: fi-corporate-income-tax
description: >
  Compute ordinary Finnish corporate income tax for tax year 2026 for limited
  liability companies and cooperatives. Reconcile accounting profit to taxable
  income, apply ordinary deduction and depreciation rules, classify corporate
  dividends and share disposals, restrict net financing costs, check group
  contributions and confirmed losses, and reconcile prepayments. Use for Form 6B,
  business tax adjustments, participation exemption, loss carryforward, ownership
  changes, interest deduction, machinery depreciation and corporate broadcasting
  tax. Includes statutory references, filing and penalty procedures and two
  recomputable examples. Corporate residence, permanent establishments, outbound
  withholding, foreign credits and exit taxation are addressed in the linked
  corporate cross-border Guide.
jurisdiction: FI
tax_year: 2026
last_updated: 2026-10-26
review_status: pending_review
trust_label: Built by Michael Cutajar and the OpenAccountants team
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
version: 1.4
category: international
---

# Finland corporate income tax v1.4

**Tax year:** 2026. Ordinary company computations; source-cited local draft awaiting fresh independent pack review. Tier 2 is not a licensed accountant's attestation.

## Who this applies to

Use for ordinary Finnish limited companies and cooperatives taxed separately from their owners. Resident corporations are taxable on worldwide income; a nonresident's Finnish income/PE and treaty position need the [corporate cross-border Guide](fi-corporate-cross-border-tax.md). Resolve residence and source first. Ordinary companies have business and, if relevant, agricultural income sources; the personal source was removed for entities within Business Income Tax Act section 1(2). This does not make every organisation a commercial company. [Income Tax Act, sections 9, 124][income-law]; [Business Income Tax Act, sections 1–3][business-law].

Treat each accounting period ending in 2026 as part of tax year 2026, but file its own return. Combining the tax-year result does not combine those filing deadlines. Corporate tax does not settle an owner's salary, dividend or private-benefit tax. [Assessment Procedure Act, section 3][assessment]; [Vero corporate income tax][income].

## Rates, bands and thresholds

| Item | 2026 rule | Statutory / official source |
|---|---|---|
| Corporate income tax | 20% of taxable income | [Income Tax Act, section 124][income-law] |
| Confirmed business losses | Following ten tax years; ownership/source restrictions apply | [Income Tax Act, sections 119, 122][income-law] |
| Machinery/equipment pool | Maximum annual depreciation 25% of residual cost; residual balance at most EUR 1,200 can be written off | [Business Income Tax Act, section 30][business-law] |
| Low-value movable item / integrated whole | Cost at most EUR 1,200; total immediate low-value deductions at most EUR 3,600/year; separate full deduction for useful life at most three years | [Business Income Tax Act, section 33][business-law] |
| Buildings | Maximum 7% shop/factory/warehouse etc.; 4% residential/office; 20% specified light structures, tanks and exclusive research buildings | [Business Income Tax Act, section 34][business-law] |
| Representation costs | 50% deductible, after correctly separating business marketing and private costs | [Business Income Tax Act, sections 7–8][business-law] |
| Net interest safe amount | At most EUR 500,000; exceeding it tests the whole net amount against the rules, not just the excess | [Business Income Tax Act, section 18a(3)][business-law] |
| Ordinary interest limitation | 25% of statutory adjusted result; separate unrelated-party route up to EUR 3 million | [Business Income Tax Act, section 18a(3)–(4)][business-law] |
| Group contribution ownership | At least 90%, with the full-year and other conditions below | [Group Contribution Act, sections 2–7][group-law] |
| Corporate broadcasting tax | If taxable income is at least EUR 50,000: EUR 140 + 0.35% of excess over EUR 50,000, capped at EUR 3,000 | [Broadcasting Tax Act, sections 1, 3][yle-law] |
| Ordinary prepayments | Minimum EUR 500; EUR 500–2,000 in two equal instalments in period months three/nine; over EUR 2,000 in twelve instalments under the decision | [Vero instalment rules][instalments] |

Do not substitute an announced future 18% rate or 25-year loss period for the applicable 2026 law. The special new-machinery 50% depreciation regime covered 2020–2025, not an ordinary 2026 acquisition. Åland corporations use the regional media fee instead of mainland broadcasting tax; exempt entities listed in section 3 do not pay it. [Vero depreciation][depreciation]; [Broadcasting Tax Act][yle-law]; [Vero broadcasting/media fee][yle].

## The base

### Build a reproducible bridge

Start with the accounts **before income tax**. Reconcile revenue, services, rents, interest, gains and other money/money's-worth receipts under sections 4–5. Apply section 19's recognition of receipts/receivables and section 22's expense-incurrence rule, with the statutory exceptions for long-term projects, insignificant items and capital expenditure. Classify each asset as financial, inventory, fixed, investment or other property before applying its gain/loss rule. Equity contributions are not operating revenue. [Business Income Tax Act, sections 4–6, 9–12a, 19, 22][business-law].

Deduct costs incurred to acquire/preserve taxable business income under section 7: evidenced business wages and employer contributions, rent, ordinary advertising, supplies and other business costs. Recoverable VAT is not part of deductible acquisition cost. Separate capital improvements from repairs, private consumption from business costs and marketing from representation. Add back income taxes, fines, penalty charges, bribes and non-deductible support/losses on nontrade receivables from companies held at least 10% under section 16(7). Ordinary trade-receivable losses have their own treatment. From 1 January 2026 the section 16(12)–(15) restriction covers specified labour-market-organisation membership fees, indirect memberships and unidentified replacement service fees; do not carry the repealed section 8(1)(9) deduction forward. [Business Income Tax Act, sections 7–8, 16–18][business-law]; [Form 6B, non-deductible costs][form6b].

Inventory cost is recognised on sale/consumption/loss. At year end compare cost with the statutory replacement/realisation measures and substantiate any lower value; a generic book provision is insufficient. Keep tax depreciation apart from book depreciation. For the movable pool: opening residual + qualifying additions brought into use + capital improvements − sale proceeds/compensation = pool before depreciation. An excess of disposal proceeds over the pool is taxable; do not depreciate a negative balance. Separate land (not depreciable) from buildings. Separately transferable intangible rights, both limited-life and indefinite-life rights, use section 37's equal annual write-off over ten years or a demonstrated shorter useful life; other qualifying long-term costs use section 24's useful period, capped at ten years. Section 54 requires the corresponding accounting deductions and limits tax depreciation to cumulative book deductions. [Business Income Tax Act, sections 24, 28, 30, 33–37, 54][business-law].

### Corporate dividends and share disposals

Classify incoming dividends under section 6a. Domestic and qualifying EU Directive-company dividends are ordinarily exempt. Another EEA company must satisfy the statutory tax-status/residence conditions, including at least 10% tax on the profits distributed without an option/exemption. An unlisted corporate recipient's dividend from a listed company is fully taxable unless it directly holds at least 10% of the payer's capital at distribution. Dividends from payers outside the section 6a(1)–(2) categories are taxable. Investment-asset dividends have their separate 75%-taxable route; do not apply it to an ordinary company's operating fixed-asset holding. A payer-side deductible dividend and non-genuine arrangements fail the exemption. Record legal form, listing, ownership, asset classification, residence, tax status and anti-abuse evidence. [Business Income Tax Act, section 6a][business-law].

For a share sale, section 6b exemption requires a qualifying non-venture-capital corporate seller, **fixed-asset** shares, at least 10% capital ownership held continuously for at least one year in a period ending no more than one year before disposal, and a Finnish, Directive-company or qualifying treaty-company target. Property/housing companies and principally property-owning/managing targets are excluded. Prior deductions, grants/reserves and intra-group deductible losses can trigger recapture. Exempt proceeds imply no deduction for the related acquisition cost/loss. Taxable fixed-asset share losses are generally restricted to taxable fixed-asset share gains in the current and next five years, with property-company, short-holding and nonqualifying foreign-target exceptions in section 6b. Other-property shares have section 8a's separate restricted-loss test. A 10% holding alone never establishes disposal exemption. [Business Income Tax Act, sections 6, 6b, 8a, 42a][business-law].

### Financing: calculate, then restrict

First establish business purpose, arm's-length amount and any anti-hybrid/avoidance restriction. Section 18a includes interest-equivalent financing charges. Before using a limitation exemption under section 18b, document its exact conditions. A standalone enterprise cannot be in an accounting group, have a foreign tax PE or have any of the statutory direct/indirect 25% ownership/profit connections; a wholly owned one-person company therefore is not automatically standalone. Financial-sector and qualifying EU infrastructure exclusions and an evidenced statutory balance-sheet exception require their own schedules. [Business Income Tax Act, sections 18–18b][business-law].

For an ordinary in-scope company:

1. Offset interest expense with interest income and determine net expense for the taxpayer across its relevant sources. At most EUR 500,000 is deductible under the safe amount.
2. Above that amount compute the statutory capacity: 25% × (business result under section 3 + interest expense + deductible tax depreciation + received group contribution − paid group contribution − qualifying final-loss group deduction), including relevant other sources under section 18a(5). This is a tax calculation, not unadjusted book EBITDA.
3. Deduct unrelated-party net interest first. The separate route allows up to EUR 3 million of such interest even where percentage capacity is lower; documented pre-17 June 2016 loan and pre-2019 capitalisation exceptions have additional conditions. Treat a nominal bank loan as related to the extent the statutory connected-receivable/security tests apply.
4. Under percentage capacity, related-party net expense uses only the remaining capacity. The EUR 3 million route is not an additional allowance for related interest. Add disallowed amounts back to taxable income.
5. Keep disallowed interest by source and related/unrelated class for later years. Claim later deduction with evidence within that year's capacity. Section 18a(8) prevents combining the percentage route and the EUR 3 million route for carried interest; deduct unrelated carried interest first. Do not treat this balance as a ten-year ordinary tax loss. [Business Income Tax Act, section 18a][business-law].

### Groups, losses and final tax

A group contribution is an expense to the payer and income to the recipient in the same year when the statutory conditions hold: eligible companies/cooperatives within business-tax scope, at least 90% qualifying direct/indirect group ownership for the **entire tax year**, matching year ends (subject to the legal exception), matching expense/income entries in both accounts and no excluded banking/credit/insurance/pension entity. Limit the contribution to the payer's business result before the contribution; it cannot itself create a loss. This is not consolidated taxation. For a foreign POEM-resident comparator, section 7 measures the relationship only during Finnish residence. Foreign-chain and PE situations need their actual treaty/non-discrimination analysis. [Group Contribution Act, sections 2–7][group-law].

Use authority-confirmed losses in the correct source, oldest usable vintages within the following ten tax years; never use the accounting retained-loss figure. A direct/indirect **more-than-50%** ownership change during/after the loss year blocks use unless a statutory exception or permit applies. The indirect test includes an at-least-20% corporate shareholder whose own majority changes; inheritance/testament and listed-company conditions are specific exceptions. Section 122(4) limits use against group contributions even with a permit. Maintain the complete ownership timeline. No ordinary carryback is provided by section 119. [Income Tax Act, sections 119, 122][income-law].

Deduct eligible confirmed losses from the adjusted same-source result, combine taxable sources and apply 20%. Compute corporate broadcasting tax separately from established taxable income after losses; it is deductible as an expense under section 8(1)(19), ordinarily in the year the final broadcasting tax is assessed under Vero's timing interpretation. Do not create a circular current-year deduction by treating the same calculated tax as already assessed. Reconcile foreign credits and prepayments after computing tax. For example, an established EUR 20,000 income-tax liability less EUR 16,000 credited prepayments leaves EUR 4,000 principal before interest/other adjustments. [Income Tax Act, sections 30, 124][income-law]; [Broadcasting Tax Act, section 3][yle-law]; [Business Income Tax Act, sections 8, 22][business-law]; [Vero broadcasting tax, section 3.3][yle-detail].

## Deadlines and filing

File Form 6B electronically within four months after the end of the calendar month in which the period ends. A 15 March 2026 end gives an ordinary 31 July deadline, moved under applicable nonbusiness-day rules. Review inactive companies' assets/liabilities and other tax-relevant events and any authority filing request. An extension must be granted; a request alone does not replace the date. Attach the relevant depreciation, dividend/disposal, financing, group and loss schedules; retain filing receipts and accounts. [Vero corporate return][return]; [Form 6B instructions][form6b].

Prepayments follow the authority decision, ordinarily due on the 23rd of the instalment month, with the business-day rule. Update forecasts in MyTax when profits change; continue paying the existing decision until changed. Corporate additional prepayment during the first month after tax-year end can avoid reduced interest if requested/paid on time; thereafter 2026 relief interest is 4.5%, subject to actual decision periods. Back-tax/refund dates are those in the assessment, not the Form 6B deadline. See [prepayments](fi-prepayments.md). [Vero instalments][instalments]; [corporate calendar][calendar]; [interest guidance][interest-guide].

## Penalties and interest

Assessment Procedure Act sections 32–32b distinguish tax increases from section 33's EUR 100 corporate late fee for relevant reporting before assessment closes. The ordinary increase is 2% of added income, aggravated repeated/manifest disregard 3–10%, estimated-assessment income 5%, specified unclear/unreasonable cases 1%, qualifying voluntary correction after assessment 0.5%. Section 32b uses added-tax bases where the income basis cannot be used. A corporation's minimum is EUR 150, subject to statutory nonimposition exceptions; these are not optional interchangeable rates. [Assessment Procedure Act, sections 32–33][assessment].

Ordinary late-paid tax in 2026 bears 9.5% annual interest, calculated for actual days after the due date through payment, using 365 days. Relief interest for additional prepayments/back tax is distinct, 4.5% for 2026; the assessment determines its period. Tax interest/penalties are not ordinary financing costs. [Vero interest][interest-guide]; [Form 6B, non-deductible costs][form6b].

## Cross-border points

Use the [corporate cross-border Guide](fi-corporate-cross-border-tax.md) for residence, PE, source tax, EU/treaty relief, foreign-tax credits and exit transfers. A dividend receipt's participation exemption is different from an outbound dividend's source-tax exemption. Use [transfer pricing](fi-transfer-pricing.md) for related-party pricing and [CbCR](fi-country-by-country-reporting.md) for the separate reporting test. Preserve gross foreign income/taxes and exempt-income cost allocations. Domestic group contributions do not automatically export losses abroad. CFC, hybrids, restructurings, final foreign subsidiary losses, minimum tax and incentive-specific claims require separate scoped work. [Business Income Tax Act, sections 6a, 18a, 51e][business-law]; [Group Contribution Act][group-law].

## Two worked examples that recompute

**1. Ordinary book-to-tax bridge.** Assume EUR 100,000 book profit before income tax, EUR 5,000 verified non-deductible expenses, EUR 2,000 exempt income, EUR 20,000 usable confirmed same-source losses, all other adjustments already reconciled. Taxable income is EUR 83,000, income tax EUR 16,600. A liable mainland company also has EUR 255.50 broadcasting tax on that established base; this is separate from income tax and not assumed already assessed/deductible in this year.

```oa-check
name: Finland corporate bridge and broadcasting tax
inputs:
  book_profit_before_income_tax: 100000
  nondeductible_costs: 5000
  exempt_income: 2000
  usable_same_source_losses: 20000
steps:
  adjusted_profit: book_profit_before_income_tax + nondeductible_costs - exempt_income
  taxable_income: adjusted_profit - usable_same_source_losses
  income_tax: taxable_income * 0.20
  broadcasting_tax: min(3000, 140 + max(0, taxable_income - 50000) * 0.0035)
expected:
  adjusted_profit: 103000
  taxable_income: 83000
  income_tax: 16600
  broadcasting_tax: 255.50
```

**2. Interest restriction above the safe amount.** Assume one business source, no exemption/grandfathering or carried interest, all interest arm's-length: expense EUR 900,000, income EUR 100,000, net unrelated interest EUR 200,000 and related EUR 600,000. Statutory adjusted result is EUR 2 million, so 25% capacity is EUR 500,000. Deduct EUR 200,000 unrelated and EUR 300,000 related net expense. EUR 300,000 related interest is added back/carried; together with the EUR 100,000 interest offset, total current interest expense deducted is EUR 600,000. The safe EUR 500,000 is not added to capacity.

```oa-check
name: Finland ordinary net interest restriction
inputs:
  interest_expense: 900000
  interest_income: 100000
  unrelated_net_interest: 200000
  related_net_interest: 600000
  statutory_adjusted_result: 2000000
steps:
  net_interest: interest_expense - interest_income
  percentage_capacity: statutory_adjusted_result * 0.25
  unrelated_deducted: min(unrelated_net_interest, percentage_capacity)
  related_deducted: min(related_net_interest, max(0, percentage_capacity - unrelated_deducted))
  related_disallowed: related_net_interest - related_deducted
  total_current_interest_expense_deducted: interest_income + unrelated_deducted + related_deducted
expected:
  net_interest: 800000
  percentage_capacity: 500000
  unrelated_deducted: 200000
  related_deducted: 300000
  related_disallowed: 300000
  total_current_interest_expense_deducted: 600000
```

## Ask the client first

1. Which entity, residence, income sources and accounting periods are involved?
2. Which ledgers, asset costs, book/tax depreciation and nonbusiness items support the bridge?
3. What are the payer/target, legal form, listing, asset classification, holding percentages and dates for dividends/share sales?
4. What loan charges, interest income, beneficial lenders, security, group structure and carried financing balances exist?
5. Which group-contribution entries, tax-loss decisions, ownership changes and permits support relief?
6. Which returns, prepayment decisions, credited payments and assessments establish the deadlines and balance?

## Sources

| Primary source | Provisions / purpose | Read on |
|---|---|---|
| [Income Tax Act 1535/1992][income-law] | Sections 9, 30, 119, 122, 124; residence, losses and 20% rate | 2026-10-26 |
| [Business Income Tax Act 360/1968][business-law] | Sections 1–8a, 12a, 16–19, 22, 24–25, 28, 30, 33–37, 42a, 54; ordinary base and adjustments | 2026-10-26 |
| [Group Contribution Act 825/1986][group-law] | Sections 2–7; ownership, accounts, full-year and amount tests | 2026-10-26 |
| [Broadcasting Tax Act 484/2012][yle-law] | Sections 1, 3; corporate charge/exemptions | 2026-10-26 |
| [Assessment Procedure Act 1558/1995][assessment] | Sections 3, 32–33; tax year and sanctions | 2026-10-26 |
| [Vero corporate income tax][income]; [return][return]; [Form 6B][form6b] | Return and book/tax classifications | 2026-10-26 |
| [Vero depreciation][depreciation] | Ordinary depreciation and end of 2020–2025 accelerated regime | 2026-10-26 |
| [Vero broadcasting/media fee][yle]; [detailed broadcasting guidance][yle-detail] | Mainland/Åland and expense timing | 2026-10-26 |
| [Vero instalments][instalments]; [calendar][calendar]; [interest][interest-guide] | Payments and 2026 interest | 2026-10-26 |

Not yet confirmed: separately scoped specialist incentives, reorganisations, financial-sector/fund treatment, final foreign subsidiary losses, CFC/hybrid and minimum-tax computations. Fresh independent whole-pack review is pending. No named professional sign-off is claimed.

[income-law]: https://www.finlex.fi/fi/lainsaadanto/1992/1535
[business-law]: https://www.finlex.fi/fi/lainsaadanto/1968/360
[group-law]: https://www.finlex.fi/fi/lainsaadanto/1986/825
[yle-law]: https://www.finlex.fi/fi/lainsaadanto/2012/484
[assessment]: https://www.finlex.fi/fi/lainsaadanto/1995/1558
[income]: https://www.vero.fi/en/businesses-and-corporations/taxes-and-charges/limited-companies-and-cooperatives/income-tax/
[return]: https://www.vero.fi/en/businesses-and-corporations/taxes-and-charges/limited-companies-and-cooperatives/tax-return/
[form6b]: https://vero.fi/en/businesses-and-corporations/taxes-and-charges/limited-companies-and-cooperatives/tax-return/instructions_for_completing_the_income_tax_return/
[depreciation]: https://www.vero.fi/en/businesses-and-corporations/taxes-and-charges/limited-companies-and-cooperatives/income-tax/depreciation-expenses/
[yle]: https://vero.fi/en/About-us/newsroom/visual_aids_for_presentations_and_for_t/public_broadcasting_tax/
[yle-detail]: https://www.vero.fi/syventavat-vero-ohjeet/ohje-hakusivu/48391/yleisradiovero5/
[instalments]: https://www.vero.fi/en/businesses-and-corporations/taxes-and-charges/tax-prepayment/instructions-for-making-prepayments/how-many-instalments/
[calendar]: https://www.vero.fi/en/businesses-and-corporations/important_dates_and_deadlines_for_corporate_taxpayers/
[interest-guide]: https://www.vero.fi/en/individuals/payments/paying-taxes/interest-on-late-payments/

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
