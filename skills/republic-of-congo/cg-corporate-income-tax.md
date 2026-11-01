---
name: cg-corporate-income-tax
description: "Compute ordinary Republic of Congo company income tax under the initial 2026 Finance Act, distinguishing general and sector rates, the minimum perception, deductions, interest restrictions, losses and statutory filing obligations. This is a source-cited research draft for the Republic of Congo, country code CG, using fetched official law and authority material. The initial 2026 statutory baseline is distinguished from unresolved later amendments and operating procedures. Trigger phrases include Congo-Brazzaville tax, tax calculation, tax return, source verification and country compliance. It is general reference, with explicit partial coverage and no accountant attestation. Use the linked country Guides for related jobs and obtain the missing facts before calculating or filing."
jurisdiction: CG
category: international
tax_year: 2026
tax_year_notes: "Initial 2026 enacted-law baseline; later 2026 currentness and filing procedures remain partial"
last_updated: 2026-11-01
version: 1.1
review_status: pending_review
trust_label: Built by Michael Cutajar and the OpenAccountants team
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Republic of Congo Corporate Income Tax v1.1

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

**Draft scope:** Companies within IS under CGI 2; special petroleum, integration and investment approvals are outside the completed computation. This is Republic of Congo(CG), not DR Congo(CD). Independent pack review is pending. Initial 2026 law is not represented as a fully consolidated or operational 2026 position.

## Who this applies to

Companies within IS under CGI 2; special petroleum, integration and investment approvals are outside the completed computation. This is Republic of Congo(CG), not DR Congo(CD).

## Rates, bands and thresholds

| Item | Rule and conditions | Authority |
|---|---|---|
| General and sector rates | Initial 2026 law: general IS 28%; microfinance and private education organised as a company 25%; mines/quarries and property operations 28%; foreign legal persons 33%. Hydrocarbon exploration, production, storage and transport use their contract rate, no lower than ordinary law. Round taxable profit down to the lower XAF 1,000. | [CGI86A](https://sgg.cg/JO/2026/congo-jo-2026-3-3.pdf); ledger C01 |
| Minimum tax | Minimum perception is 1% of total operating, financial and non-ordinary receipts, excluding receipts already subject to final withholding. Compare this minimum with ordinary IS; do not use only sales turnover or reinstate the old unsupported fixed minimum floors. | [CGI86C(1)–(3)](https://sgg.cg/JO/2026/congo-jo-2026-3-3.pdf); ledger C08 |

## The base

Prepare an accounting-to-tax reconciliation. Test each cost against C04, remove IS and penalties, apply the interest limits and eligible losses, then round the taxable profit as C01 requires. Compare ordinary IS against C08 and credit only substantiated same-year payments. The examples assume no foreign credits, incentives or separate solidarity levy. The old blanket 5% surtax is not confirmed and is excluded.

| Item | Rule and conditions | Authority |
|---|---|---|
| Taxable entities | Companies including single-member SA, SAS and SARL are within IS by form; public entities and other bodies conducting taxable commercial activities are within its activity scope. Partnership options and statutory exemptions must be considered separately. | [CGI2–3](https://sgg.cg/JO/2026/congo-jo-2026-3-3.pdf); ledger C02 |
| Tax base and accounts | Determine taxable net profit from all taxable receipts less allowable costs using OHADA accounting or applicable regulated-sector rules. Accounts ordinarily close 31December; tax is assessed on the preceding financial year. | [CGI6,9](https://sgg.cg/JO/2026/congo-jo-2026-3-3.pdf); ledger C03 |
| Conditions for deductions | Costs must belong to the year, serve the business, be real and supported, reduce net assets, and not support exempt receipts or be legally excluded/abnormal management. Domestic supplier invoices require the NIU and SFEC. Cash payments of XAF 200,000 or more fail the deduction condition. Do not import VAT's strictly-greater-than boundary into IS. | [CGI25](https://sgg.cg/JO/2026/congo-jo-2026-3-3.pdf); ledger C04 |
| Tax and penalties | IS itself is not deductible; taxes borne by the enterprise and assessed during the year can be deductible. Fines, confiscations and penalties are excluded. Later refunds of deductible taxes enter receipts. | [CGI42](https://sgg.cg/JO/2026/congo-jo-2026-3-3.pdf); ledger C05 |
| Interest restriction | Interest must meet the ordinary conditions and market pricing. Related-shareholder/group interest additionally requires fully paid capital and is limited by BEAC tender rate plus 3 points. Total annual net interest is capped at 20% of OHADA gross operating surplus attributable to non-exempt activity, with disallowed interest carryforward up to 5 years subject to the same conditions. The cap excludes qualifying finance/insurance operating-charge interest. No live BEAC rate is supplied. | [CGI49](https://sgg.cg/JO/2026/congo-jo-2026-3-3.pdf); ledger C06 |
| Losses | Ordinary losses carry forward through the fifth year after the loss year. Losses from IS-exempt years cannot carry forward. Deferred depreciation is unresolved: article 53 permits properly recorded and declared deferred depreciation without a duration limit, while article 75 treats depreciation booked during loss years as ordinary losses. Hold that interaction; do not assume either unlimited carryforward or ordinary-loss expiry without a controlling reconciliation. | [CGI53,75: deferred-depreciation conflict](https://sgg.cg/JO/2026/congo-jo-2026-3-3.pdf); ledger C07 |

## Deadlines and filing

Identify the competent fiscal residence, retain the NIU, existence filing, DSF schedules, payment references and electronic acknowledgements. C10 records the unresolved filing-date conflict. Do not infer that a public calendar verifies the live portal fields or successful filing.

| Item | Rule and conditions | Authority |
|---|---|---|
| Minimum declaration and instalments | Declare the current-year minimum by 15March using preceding-year/last-closed-year receipts provisionally. Pay four minimum-tax instalments by 15March,15June,15September and 15December. The minimum credits against same-year IS, but remains with Treasury where ordinary liability is lower or nil. | [CGI86C(4)–(7)](https://sgg.cg/JO/2026/congo-jo-2026-3-3.pdf); ledger C09 |
| Annual statutory rule | CGI 86F requires the profit/loss return within 4 months of year-end; 86G requires the balance on delivery. The official 2026 ACPCE calendar instead states 15May for IS/DSF. These are conflicting sources: retain the statutory wording here, flag the administrative date, and stop short of an operative 2026 filing instruction until reconciled. | [CGI86F–G](https://sgg.cg/JO/2026/congo-jo-2026-3-3.pdf); [ACPCE2026 calendar](https://acpce.cg/wp-content/uploads/2026/02/Calendrier-des-obligations-fiscales-et-sociales-au-titre-de-lannee-2026.pdf); ledger C10 |
| Existence and filing package | For the corporate entities within 86E, make the declarations within 3 months of definitive constitution and at latest within 15 days of beginning activity; retain the separate 128 operation-start obligation. The annual DSF follows the prescribed model, with financial statements, tax reconciliation and identification schedules. CGI131 specifies 3 complete sets plus electronic statements. CGI130 requires real-regime electronic declaration/payment and appropriate accountant certification where no statutory auditor exists. Portal, current form version and field numbers remain unconfirmed. | [CGI86E,128,130–131](https://sgg.cg/JO/2026/congo-jo-2026-3-3.pdf); ledger C11 |
| Conflicting administrative calendar | The ACPCE 2026 calendar lists annual IS and IBA by 15May and DSF by 15May following year-end. Compare C10: the enacted new 86F has 4 months. The tax-year/transition/administrative basis for the different date has not been established; no date extension is assumed. | [ACPCE2026calendar pp1,4](https://acpce.cg/wp-content/uploads/2026/02/Calendrier-des-obligations-fiscales-et-sociales-au-titre-de-lannee-2026.pdf); ledger C15 |

## Penalties and interest

C12–C14 are distinct triggers. Other late-return, misstatement and enforced-collection penalties remain unconfirmed.

| Item | Rule and conditions | Authority |
|---|---|---|
| Minimum-tax default | Failure to pay the minimum attracts 50% of the unpaid minimum under 86C(8). This is not a universal rate for every late tax. | [CGI86C(8)](https://sgg.cg/JO/2026/congo-jo-2026-3-3.pdf); ledger C12 |
| Electronic filing/payment default | Non-compliance with the real-regime electronic declaration/payment obligation attracts 10% of the amount to declare. This does not establish an all-purpose annual-return penalty. | [CGI130](https://sgg.cg/JO/2026/congo-jo-2026-3-3.pdf); ledger C13 |
| Voluntary underpayment correction | Where a taxpayer corrects an underpayment before an administration claim or information request,374ter prescribes 0.5% per day capped at 20% of principal and no penalty in that particular case. It is not a general late-payment interest rate. | [CGI374ter as amended2026](https://sgg.cg/JO/2026/congo-jo-2026-3-3.pdf); ledger C14 |

## Cross-border points

Use [cross-border](cg-cross-border.md) for territoriality, PE and foreign payments, [transfer pricing](cg-transfer-pricing.md) for related parties and [income tax](cg-income-tax.md) for shareholder/individual income. Do not add a service withholding to IS mechanically without classifying the recipient.

## Two worked examples that recompute

### 1. CIT above minimum

Assume an ordinary domestic company has reconciled taxable profit XAF 20,000,800 and minimum-tax receipts XAF 100,000,000. C01 rounds profit to 20,000,000; 28% is 5,600,000. C08 gives minimum 1,000,000. Ordinary IS governs, before verified credits or any separately established levy.

```oa-check
name: CIT above minimum
inputs:
  profit: 20000800
  receipts: 100000000
steps:
  - rounded_profit: floor(profit / 1000) * 1000
  - ordinary: rounded_profit * 0.28
  - minimum: receipts * 0.01
  - is_before_credits: max(ordinary, minimum)
expected:
  is_before_credits: 5600000
```

### 2. Decision: deduction boundary changes ordinary tax

Assume pre-cost taxable profit XAF 10,000,000, an otherwise qualifying domestic cost of 200,000 and minimum receipts 20,000,000. Payment in cash fails C04 at equality, leaving IS 2,800,000. A qualifying traceable non-cash payment permits the cost, giving 2,744,000. The difference 56,000 is the ordinary IS consequence; all other deduction conditions still have to hold.

```oa-check
name: Decision: deduction boundary changes ordinary tax
inputs:
  profit_before: 10000000
  cost: 200000
  receipts: 20000000
steps:
  - cash_tax: max(profit_before * 0.28, receipts * 0.01)
  - noncash_tax: max((profit_before - cost) * 0.28, receipts * 0.01)
  - difference: cash_tax - noncash_tax
expected:
  cash_tax: 2800000
  noncash_tax: 2744000
  difference: 56000
```

## Ask the client first

- Legal form, incorporation and effective management?
- Activities and any petroleum/investment/group approval?
- Year-end, taxable receipts and full tax reconciliation?
- Cash/SFEC support, related-party debt and losses?
- Actual filings, payments and notices received?

## Sources

| Source and portion actually read | Official URL | Read on |
|---|---|---|
| ACPCE 2026 fiscal and social calendar. All five pages OCR after 180-degree correction; annual/monthly/varied deadlines and rate table. Conflicts with statute are recorded, not silently resolved. | https://acpce.cg/wp-content/uploads/2026/02/Calendrier-des-obligations-fiscales-et-sociales-au-titre-de-lannee-2026.pdf | 2026-11-01 |
| Finance Act 42-2025, official gazette special 3-2026. Enacted initial 2026 law: cover; art 5; art 47 replacement CGI 2–11,15–19,21,25,42,45–49,69–86A,86C–G,92–92E,93–99,102,104–110A,111C–116I,128–131(excerpts through part 6); amendments 374ter and VAT 24/29; state invoice rule 7.2.4; final arts 61–62. Focused provisions with neighbors, not all fiscal schedules or all 116pages read. | https://sgg.cg/JO/2026/congo-jo-2026-3-3.pdf | 2026-11-01 |

Figure/rule quotations and source hashes: [country ledger](../../evidence/ledgers/republic-of-congo-draft-20261101/cg-corporate-income-tax.md). Every worked figure is conditional on the stated example facts.

Not yet confirmed: The conflict between CGI53 and75 for deferred depreciation remains unresolved; no carryforward duration is selected.  Later 2026 rectifying law and implementation chain; the 86F four-month versus ACPCE 15May filing conflict; live electronic portal/forms/boxes; the old blanket 5% surtax and minimum floors; ordinary enforced late-return/late-payment sanctions; sector incentives and full depreciation tables. These gaps prevent operative or comprehensive 2026 coverage.

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
