---
name: id-corporate-tax
description: Idaho corporate income and alternative franchise tax, Form 41 base and minimum tax, Permanent Building Fund tax, estimated-payment trigger and filing route. Uses verified 2025-2026 filing-cycle figures while final 2026 annual forms remain unconfirmed. Does not compute S corporation or partnership elections.
version: 1.0
jurisdiction: US-ID
category: state-tax
type: situation-rules
tax_year: 2026
tax_year_notes: "2025-2026 filing cycle; final annual 2026 forms not confirmed"
tier: 2
last_updated: 2026-11-13
---

# Idaho corporate income and franchise tax v1.0

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

**Quick reference:** **2025-2026 filing cycle**, verified annual 2025 Form 41. Idaho's corporate franchise tax is an alternative to its corporate income tax, not an additional general gross-receipts tax. Final 2026 annual figures/forms are not established here. Built from the law; Not yet approved.

## Who this applies to

Corporations and LLCs taxed as corporations with Idaho business, registration or attributable income. The [corporation page](https://tax.idaho.gov/taxes/income-tax/business-income/guides-for-certain-businesses/income-tax-for-corporations/) distinguishes income from franchise tax and recognizes federal corporate classification. Some otherwise protected sellers may be exempt under Public Law 86-272; do not infer protection from low turnover alone. Partnerships, S corporations, ABE elections and nonresident-owner payments need their own return analysis.

## Rates, bands and thresholds

| Item | Verified amount and condition | Official source |
|---|---|---|
| Corporate income/franchise tax | 5.3% of Idaho taxable income in 2025; the two taxes are alternatives | [Form 41 instructions, line 38](https://tax.idaho.gov/wp-content/uploads/forms/EFO00025/EFO00025_03-02-2026.pdf) |
| Minimum income/franchise tax | $20 for each corporation doing business, registered or exercising its Idaho franchise, subject to listed exceptions | [Form 41 line 38 minimum-tax instructions](https://tax.idaho.gov/wp-content/uploads/forms/EFO00025/EFO00025_03-02-2026.pdf) |
| Permanent Building Fund | $10 per C corporation required to file, separately from income/franchise tax | [Business basics; Code 63-3082](https://tax.idaho.gov/taxes/income-tax/business-income/online-guide/) |
| Estimated-payment trigger | After the first Idaho year, estimated Idaho liability at least $500 **and** federal estimated payments required | [Corporation estimated payments](https://tax.idaho.gov/taxes/income-tax/business-income/guides-for-certain-businesses/income-tax-for-corporations/) |
| Annual filing | 15th day of the fourth month after year-end; next business day if weekend/holiday | [Corporation filing deadline](https://tax.idaho.gov/taxes/income-tax/business-income/guides-for-certain-businesses/income-tax-for-corporations/) |

## The base

First compute the federal corporate result in the applicable federal owner skill. The [2025 Form 41 instructions](https://tax.idaho.gov/wp-content/uploads/forms/EFO00025/EFO00025_03-02-2026.pdf) reconcile Idaho additions, subtractions and allocations. For all-Idaho activity, line 33 uses 100%; multistate businesses require Form 42. Line 37 is Idaho taxable income, line 38 calculates tax, and line 44 adds PBF separately. Retain the reconciliation, rather than multiplying federal gross receipts by the income-tax rate.

| Boundary | Treatment | Source |
|---|---|---|
| Unitary group | Consider combined reporting; PBF applies per required corporation | [Business basics](https://tax.idaho.gov/taxes/income-tax/business-income/online-guide/) |
| Minimum-tax exceptions | Nonproductive mining corporations; qualifying nonprofits without unrelated taxable income; Form 1120-H homeowners' associations without federal taxable income; protected Public Law 86-272 corporations | [Form 41 line 38 instructions](https://tax.idaho.gov/wp-content/uploads/forms/EFO00025/EFO00025_03-02-2026.pdf) |
| S corporation / partnership | PBF can apply for owners whose Idaho tax the entity pays; do not treat all pass-throughs as C corporations | [Business basics](https://tax.idaho.gov/taxes/income-tax/business-income/online-guide/) |

Do not conclude that a minimum-tax exception also removes PBF. The [Form 41 instructions](https://tax.idaho.gov/wp-content/uploads/forms/EFO00025/EFO00025_03-02-2026.pdf) expressly include nonproductive mining corporations in PBF. Credits, losses, special-industry rules and the optional small-sales alternative require separate qualification before changing the basic result.

## Deadlines and filing

Use Form 41, required Idaho schedules and a complete federal return. The [Commission corporation page](https://tax.idaho.gov/taxes/income-tax/business-income/guides-for-certain-businesses/income-tax-for-corporations/) permits authorized electronic filing or paper submission; retain acceptance and payment records. Form 41ES handles estimates and Form 41ESR underpayment reconciliation. Installment amounts/dates and extension conditions are not computed here.

For payment, use [TAP/Quick Pay or another authorized route](https://tax.idaho.gov/taxes/income-tax/business-income/filing/), selecting the correct entity, tax type and period. TAP cannot electronically file the corporate income return itself. A payment receipt is not an accepted return.

## Penalties and interest

Late filing, late payment and insufficient estimates need separate treatment. Current numerical schedules, interest rate, installment safe harbours and extension-payment qualification remain unconfirmed. Route arrears calculations to the Commission's current instructions before advising payment.

## Cross-border points

Multistate and multinational operations require Form 42 and possible combined reporting. This skill does not establish the apportionment formula, foreign-income adjustments or Public Law 86-272 eligibility. State nexus and income sourcing are separate from sales-tax collection; load `id-sales-tax` for that job.

## Two worked examples that recompute

**Ordinary corporation.** Invented 2025 corporation with $100,000 of already reconciled Idaho taxable income, no credits or other taxes, and one required PBF payment: income tax $5,300 plus $10 PBF = $5,310.

```oa-check
name: Idaho corporation 2025-2026 filing cycle
inputs:
  idaho_taxable_income: 100000
steps:
  income_tax: max(20, idaho_taxable_income * 0.053)
  total_before_credits: income_tax + 10
expected:
  income_tax: 5300
  total_before_credits: 5310
```

**Minimum-tax boundary.** An ordinary required corporation with zero Idaho taxable income owes $20 plus $10 PBF before other items. An otherwise qualifying nonproductive mining corporation exempt from the minimum has zero income tax on the same zero base but still $10 PBF. Entity qualification, not a tax preference, determines the branch under [Form 41](https://tax.idaho.gov/wp-content/uploads/forms/EFO00025/EFO00025_03-02-2026.pdf).

```oa-check
name: Idaho minimum tax does not determine PBF
inputs:
  idaho_taxable_income: 0
steps:
  ordinary_income_tax: max(20, idaho_taxable_income * 0.053)
  ordinary_total: ordinary_income_tax + 10
  exempt_mining_total: idaho_taxable_income * 0.053 + 10
expected:
  ordinary_income_tax: 20
  ordinary_total: 30
  exempt_mining_total: 10
```

## Ask the client first

- What annual year, federal entity classification and Idaho registration apply?
- What activities, property, payroll and sales occur inside and outside Idaho?
- Is a unitary group, special-industry status or claimed filing protection involved?
- What federal-to-Idaho reconciliation, losses and credits support the taxable base?
- What estimates, prior tax, first-year status, notices and payments exist?

## Sources

| Source | URL | Read for | Read on |
|---|---|---|---|
| Commission business basics; Code 63-3082 | https://tax.idaho.gov/taxes/income-tax/business-income/online-guide/ | Read for business-filing triggers, explicitly dated 2025 rate and entity-specific PBF rules | 2026-11-13 |
| Commission corporations; Code 63-3025A | https://tax.idaho.gov/taxes/income-tax/business-income/guides-for-certain-businesses/income-tax-for-corporations/ | Read for income/franchise alternatives, corporate classification, filing route, deadline and estimate trigger | 2026-11-13 |
| Form 41 and revised instructions, 2025 | https://tax.idaho.gov/wp-content/uploads/forms/EFO00025/EFO00025_03-02-2026.pdf | Read for lines 33-44, tax/minimum, exceptions, PBF and small-sales election boundary | 2026-11-13 |
| Commission business filing | https://tax.idaho.gov/taxes/income-tax/business-income/filing/ | Read for electronic/paper filing, TAP's payment-only income-tax function and supporting schedules | 2026-11-13 |

Not yet confirmed: final annual 2026 rate/forms/conformity and adjustments; Form 42 apportionment and combined-report computation; full pass-through/ABE returns and owner payments; complete small-sales alternative, credits and losses; estimate installments/safe harbours, extension tests, penalty/interest schedules. This skill retains verified 2025-2026 filing-cycle figures rather than labelling the 2025 form as a 2026 return.
