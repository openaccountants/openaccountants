---
name: by-corporate-income-tax
description: Compute 2026 Belarus profit tax for ordinary resident companies, separately liable branches and foreign permanent establishments. Trigger on Belarus corporate tax, nalog na pribyl, taxable profit, the 25000000 base threshold, loss carry-forward, controlled indebtedness, deductible costs and quarterly profit-tax returns. This skill reconciles the accounting result to the statutory base, distinguishes the whole-base increased rate from a marginal band, explains loss and foreign-tax-credit limitations, and screens simplified-system eligibility. It includes annual and quarterly compliance, interest and administrative sanctions and two recomputing examples. Transfer pricing and nonresident gross-basis withholding are handled by the linked country skills. Special investment-zone and sector regimes require their own calculation. Tier 2, checked against the law.
jurisdiction: BY
tax_year: 2026
last_updated: 2026-10-30
review_status: pending_review
trust_label: Built by Michael Cutajar and the OpenAccountants team
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
version: 0.1
category: international
---

# Belarus corporate income tax, 2026 v0.1

## Who this applies to

Calendar-year 2026 ordinary Belarus organisations, separately liable branches under General Code art. 14 and foreign organisations operating through a Belarus PE. Identify the taxpayer and separate regime before consolidating any figures; the increased-rate test is applied separately to the organisation excluding branches, each branch and each foreign PE (art. 184(1)). Resident organisations' gross profit includes foreign activity; foreign PEs compute attributable Belarus profit under art. 180. [General Code arts. 14-16](https://pravo.by/document/?guid=3871&p0=hk0200166); [Special Code arts. 166-167, 180, 184](https://pravo.by/document/?guid=3871&p0=hk0900071).

Screen the simplified system before ordinary profit tax: only eligible organisations under arts. 324-327 qualify. Entrepreneurs cannot use this company regime. Do not apply ordinary profit tax to receipts replaced by the simplified tax, or treat the replacement as removing dividend, withholding or import/reverse-charge VAT obligations. [Arts. 324-326](https://pravo.by/document/?guid=3871&p0=hk0900071).

## Rates, bands and thresholds

| Item | Amount | Period | Official act/article |
|---|---|---|---|
| Ordinary profit tax | 20% | 2026 | [Code art. 184(1)](https://pravo.by/document/?guid=3871&p0=hk0900071) |
| Increased whole-base rate | 25% once cumulative tax base exceeds BYN 25,000,000, not only on excess | 2026 | [Art. 184(1)](https://pravo.by/document/?guid=3871&p0=hk0900071) |
| Banks, insurers, insurance brokers; specified forex profit | 25% | 2026 | [Art. 184(4),(9)](https://pravo.by/document/?guid=3871&p0=hk0900071) |
| Specified microfinance profit; cellular/universal telecom operators | 30% | 2026 | [Art. 184(5),(11)](https://pravo.by/document/?guid=3871&p0=hk0900071) |
| Dividends to Belarus organisations | 12%; qualifying five-year nondistribution relief 0%; former 6% clause repealed | 2026 | [Art. 184(6)-(8); MNS 2026 commencement](https://nalog.gov.by/clarifications/comments/33570/) |
| Loss life | Pre-2022 losses: 10 following years; 2022 onward: 5 following years | Loss vintage controls | [Art. 183(5)](https://pravo.by/document/?guid=3871&p0=hk0900071) |
| Ordinary controlled-debt trigger | Debt at least 3 times statutory equity; specified excisable producers: greater than 1 time | Year end | [Art. 172(1)-(2)](https://pravo.by/document/?guid=3871&p0=hk0900071) |
| Investment deduction maximum | 20% qualifying production buildings/structures/transmission assets; 40% qualifying machinery/equipment/vehicles | 2026 rules for qualifying new depreciation/reconstruction | [Art. 170(2.2); MNS commencement](https://nalog.gov.by/clarifications/comments/33570/) |
| Simplified-system tax and in-year limits | 6% gross revenue; 50 employees and BYN 3,735,000 cumulative gross revenue | 2026 | [Arts. 327(6), 329](https://pravo.by/document/?guid=3871&p0=hk0900071) |
| Transition into simplified system | BYN 2,625,000 first-nine-months 2025 revenue for entry in 2026; BYN 2,800,000 first-nine-months 2026 for entry in 2027; average staff no more than 50 | Entry year distinguished | [Art. 327(2); MNS transition](https://nalog.gov.by/clarifications/comments/33838/) |

## The base

1. Start with revenue from sales less taxes from revenue and allowable production/selling costs, plus taxable non-operating income less allowable non-operating expenses. Reconcile separately disposed depreciable assets, investment property and intangible assets using proceeds less residual value and sale costs under art. 168. Do not treat all accounting income/expenses as taxable/deductible. [Arts. 167-175](https://pravo.by/document/?guid=3871&p0=hk0900071).
2. Recognise revenue and costs at the statutory dates, document business purpose and matching, and depreciate qualifying capital expenditure. Add back art. 173 nondeductible costs, including tax sanctions and private expenditure. Apply art. 171(1)'s separate limits to travel, fuel, management and the other listed controlled costs. Pool the art. 171(2) other costs, including listed employee retirement/health payments, representation, board fees, official events, non-travelling staff's private-car compensation, association fees, late-loan interest, promotional gifts and employee transport. Their combined deduction is at most 1% of revenue from goods/work/services/IP and other assets, INCLUDING VAT, under art. 171(3); test the exact listed inclusions/exceptions before pooling. [Arts. 168-175](https://pravo.by/document/?guid=3871&p0=hk0900071).
3. Apply the investment deduction only to qualifying assets and reconstruction, within the statutory ceiling and two-year claim window beginning with the reporting period containing the qualifying depreciation or reconstruction-capitalisation month. Ordinary passenger cars are excluded unless within the specified special-purpose, taxi or carsharing categories. Test the other excluded assets and recapture on disqualifying disposal/use changes under art. 170(2.2). For the 2026 reform, depreciation must start from 1 January 2026 or reconstruction must increase original cost after that date; do not retroactively apply the expanded timing to older assets. An investment deduction not claimed before an appointed inspection is unavailable for the inspected period. [Art. 170(2.2)](https://pravo.by/document/?guid=3871&p0=hk0900071); [MNS reform commentary](https://nalog.gov.by/clarifications/comments/33570/).
4. Calculate controlled indebtedness at year end across the counterparties in art. 172(2.1), including qualifying related-party borrowings and specified service/IP/penalty obligations. Equity excludes the statutory tax, contribution and budget-loan liabilities. For an ordinary company with positive equity, `capitalisation coefficient = controlled debt / equity / 3`; if the trigger applies, divide the affected otherwise deductible costs and interest by that coefficient. With nonpositive equity, none of those affected costs is deductible. Excisable producers use the alternative coefficient; banking, insurance and qualifying majority-rental businesses have art. 172(4) exclusions. This is a cost cap, separate from arm's-length TP. [Art. 172](https://pravo.by/document/?guid=3871&p0=hk0900071).
5. Separate exempt profit, dividends and special-rate bases. Apply TP adjustments under General Code arts. 87-97. Compute the cumulative ordinary rate from the statutory tax base, not revenue, accounting profit or only the excess above the increased-rate threshold. [Arts. 182, 184, 186](https://pravo.by/document/?guid=3871&p0=hk0900071); [General Code ch. 11](https://pravo.by/document/?guid=3871&p0=hk0200166).
6. Claim carried losses only in the final annual/fourth-quarter computation under art. 186(1). Maintain losses by vintage, expiry, taxpayer and statutory basket. Securities/financial-instrument losses and fixed/investment-asset disposal losses are generally usable against their corresponding basket; residual losses follow art. 183(3.2). Use oldest eligible losses first, within current qualifying profit. Exclude foreign separately registered activity, exempt/regime-period losses and undocumented losses as art. 183 requires. A loss not claimed before an appointed non-desk inspection cannot be introduced during that inspection. Do not carry a subsidiary's loss to another company or assume all reorganisations transfer it. [Art. 183](https://pravo.by/document/?guid=3871&p0=hk0900071).
7. Multiply each remaining rate-specific base by its rate; subtract allowable art. 187 foreign-tax credit and earlier cumulative tax payments. Corporate foreign credit is capped at Belarus tax on the corresponding qualifying foreign income. Preserve foreign authority/payment evidence and the timing/translation rules of art. 187, rather than subtracting all overseas cash tax. [Arts. 186-187](https://pravo.by/document/?guid=3871&p0=hk0900071).

**Simplified route.** Screen all art. 324 exclusions, including regulated activities, prohibited property use/subletting, and ownership/entity categories. Test employee and revenue limits separately. For existing 2025 users, revenue above BYN 3,500,000 in 2025 blocks continuation in 2026 despite the higher 2026 limit. An eligible newly registered company with no more than 50 employees can notify within 20 working days; ordinary next-year entry notification is 1 October-31 December. Exit is from the month after the reporting period of an employee/revenue excess, or from the relevant disqualifying month under art. 327(6.1). Compute 6% of gross revenue determined under art. 328 on its prescribed receipt basis, including taxable non-operating receipts, rather than profit after expenses; keep returns, adjustments and transitional uncollected revenue under arts. 328-333. [Arts. 324-333](https://pravo.by/document/?guid=3871&p0=hk0900071); [MNS transition rule](https://nalog.gov.by/clarifications/comments/33838/).

## Deadlines and filing

| Obligation | Deadline/rule | Official source |
|---|---|---|
| Ordinary quarters 1-3 | Cumulative return by 20th; payment by 22nd of following month | [Arts. 185-186](https://pravo.by/document/?guid=3871&p0=hk0900071) |
| Fourth-quarter advance | By 22 December, two thirds of tax for the third quarter, followed by final reconciliation | [Art. 186(9.1)](https://pravo.by/document/?guid=3871&p0=hk0900071) |
| Annual/fourth-quarter return and balance | Return by 20 March, balance by 22 March following year | [Art. 186(7),(9.3)](https://pravo.by/document/?guid=3871&p0=hk0900071) |
| Resident corporate dividend tax | Return by 20th, remittance by 22nd of month after accrual | [Art. 186(6),(9.2)](https://pravo.by/document/?guid=3871&p0=hk0900071) |
| Simplified-system return/payment | Quarterly return by 20th and payment by 22nd following quarter | [Arts. 330, 332](https://pravo.by/document/?guid=3871&p0=hk0900071) |
| New company tax registration | Registrar information supplies registration under the one-window rules; verify assigned UNP and inspectorate | [General Code arts. 69-70](https://pravo.by/document/?guid=3871&p0=hk0200166) |

File the MNS profit-tax declaration for Belarus organisations or the foreign-organisation form, as appropriate, electronically where General Code art. 40 requires. Zero-object/no-relevant-amount relief is subject to art. 40 and the specific art. 186 exceptions; do not discontinue filings solely because cash tax is zero. Liquidation, reorganisation and PE cessation require actual-profit final computations (art. 186(2), General Code art. 44). Apply General Code art. 4 to nonworking-day tax deadlines. [General Code arts. 4, 40, 44](https://pravo.by/document/?guid=3871&p0=hk0200166); [MNS 2026 filing changes](https://nalog.gov.by/clarifications/comments/33570/).

## Penalties and interest

Late-payment interest under General Tax Code art. 55 is computed separately for each period of constant unpaid tax and National Bank refinancing rate: `unpaid tax × overdue calendar days × annual rate / 360 / 100`. Count from the day after the due date through payment; interest reflected in the audit decision on audit-assessed tax is capped at that assessed tax amount; apply art. 55(3) exclusions and art. 55(4)'s four-decimal interest-rate precision. Use the rate actually in force in each period, not a single assumed 2026 rate. [General Code art. 55](https://pravo.by/document/?guid=3871&p0=hk0200166).

For a business/agent return, Administrative Code art. 14.2(1)-(2) sets up to 1 basic unit for no more than 3 working days late; otherwise 2 basic units plus 0.5 per complete month, capped at 10. Repetition within a year invokes art. 14.2(4), 3 per complete or incomplete month, capped at 20. Under art. 14.4(1), business tax underpayment carries 40% of unpaid tax, minimum 2 basic units for an entrepreneur or 10 for a company, subject to the statutory notes, including timely voluntary correction/payment. Do not apply these amounts automatically to an ordinary individual or to a withholding default. [Administrative Code arts. 14.2 and 14.4](https://pravo.by/document/?guid=3871&p0=hk2100091). The basic unit is BYN 45 from 1 January 2026 ([Council Resolution 651 of 20 November 2025](https://pravo.by/document/?guid=12551&p0=C22500651)).

The rate and minimum for withholding defaults come from Administrative Code art. 14.5 instead. A TP adjustment is additional profit tax; it is not an automatic separate percentage fine. Determine voluntary-correction and audit status before assessing sanctions. [Administrative Code arts. 14.4-14.5](https://pravo.by/document/?guid=3871&p0=hk2100091).

## Cross-border points

A foreign branch/office registration is not the complete PE test. Art. 180 also covers dependent-agent activity, work/services exceeding 180 days in any twelve-month period and construction lasting more than 180 days, retrospectively from commencement. Apply an actually operative treaty after checking suspensions. Attribute income and documented allowable expenses under art. 180; use the separate non-PE withholding system in arts. 188-194 where relevant. Read `belarus-cross-border-tax` for credits, withholding and cessation; `belarus-transfer-pricing` for related-party transactions. [Arts. 180, 187-194](https://pravo.by/document/?guid=3871&p0=hk0900071).

## Two worked examples that recompute

### 1. Ordinary resident company

Tax-exclusive sales are BYN 1,000,000, deductible current costs 700,000, taxable non-operating income 20,000 and allowable non-operating expenses 10,000. With no reliefs, losses, special rates or foreign tax, taxable profit is 310,000 and tax is 62,000.

```oa-check
name: BY 2026 ordinary corporate profit
inputs:
  sales: 1000000
  costs: 700000
  other_income: 20000
  other_expenses: 10000
steps:
  base: sales - costs + other_income - other_expenses
  tax: base * 0.20
expected:
  base: 310000
  tax: 62000
```

### 2. Whole-base increased rate and final-year loss use

The annual statutory base before carried losses is BYN 26,000,000, above the increased-rate trigger. A supported, unexpired BYN 1,000,000 ordinary-basket loss from 2023 is available and used at year end. The remaining 25,000,000 is taxed at 25%, producing 6,250,000, before earlier instalment credit. Do not tax only the excess at 25% or retest the trigger on profit after carried losses.

```oa-check
name: BY 2026 whole-base increased rate with annual loss
inputs:
  statutory_base: 26000000
  eligible_loss: 1000000
steps:
  loss_used: min(statutory_base, eligible_loss)
  taxable: statutory_base - loss_used
  tax: taxable * 0.25
expected:
  taxable: 25000000
  tax: 6250000
```

## Ask the client first

- What are the legal entity, separately liable branches, PE locations and tax regimes?
- Which revenue, non-operating receipts and costs reconcile to the accounts and source documents?
- What are the year-end related-party obligations, statutory equity and special cost limits?
- Which loss vintages/baskets, investment deductions, exempt profits and audit notices exist?
- What foreign tax certificates, payments and earlier Belarus instalments are available?
- What staff/revenue history and timely notices support any simplified-system election?

## Sources

| Source and read scope | Official URL | Read on |
|---|---|---|
| Tax Code Special Part, arts. 166-194 and 324-333 | https://pravo.by/document/?guid=3871&p0=hk0900071 | 2026-10-24 |
| Tax Code General Part, arts. 4, 14-16, 40, 44, 55, 69-70, 87-97 | https://pravo.by/document/?guid=3871&p0=hk0200166 | 2026-10-24 |
| Administrative Code, arts. 14.2, 14.4-14.5 | https://pravo.by/document/?guid=3871&p0=hk2100091 | 2026-10-24 |
| MNS profit-tax 2026 amendment and commencement commentary | https://nalog.gov.by/clarifications/comments/33570/ | 2026-10-24 |
| MNS simplified-system 2026/2027 transition commentary | https://nalog.gov.by/clarifications/comments/33838/ | 2026-10-24 |
| Council Resolution 651 of 20 November 2025, paras. 1, 3, official PDF, basic unit BYN 45 from 1 January 2026 | https://pravo.by/document/?guid=12551&p0=C22500651 | 2026-10-31 |

Pravo consolidated HTML was read in a normal browser after scripted access returned HTTP 403. Published PDFs were read in the official browser PDF viewer. Checked against the law (tier 2); no licensed Belarusian accountant has signed it off.

Not yet confirmed: None within the stated ordinary scope. The special regimes named out of scope are not computed.

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
