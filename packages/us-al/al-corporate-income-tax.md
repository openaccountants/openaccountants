---
name: al-corporate-income-tax
description: >
  Use this skill whenever asked about Alabama corporate income tax
  for tax year 2026: the flat 6.5% rate with the deduction for
  federal income tax paid or accrued, single sales factor apportionment
  for tax years beginning on or after 2021, the Form 20C due date, and
  the business privilege tax rate range. Trigger on "Alabama corporate tax",
  "Alabama 6.5 percent", "Alabama Form 20C", "Alabama single sales
  factor", "Alabama business privilege tax", "Ala Code 40-18".
jurisdiction: US-AL
category: corporate
domain: corporate-tax
type: rates-card
tax_year: 2026
tier: 2
last_updated: 2026-11-13
version: 0.5
verified_by: pending
review_status: pending_review
trust_label: Built by Michael Cutajar and the OpenAccountants team
depends_on:
  - alabama-income-tax
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Alabama corporate income tax

> **Source-cited draft.** Built from the Alabama Department of Revenue Corporate Income Tax page, Due Dates page and Business Privilege Tax Incentives page, read 2026-11-13. No accountant has reviewed it. Do not rely on it without review by a qualified Alabama professional.

## Who this applies to

- Corporations with net taxable income from business within Alabama, and foreign (out-of-state) corporations on income derived from sources within Alabama (ALDOR Corporate Income Tax page: "Corporations - Net taxable income from business within the state"; Amendment 212: "Taxes due by foreign corporations are to be based on income derived from sources within Alabama").
- For tax years beginning on or after January 1, 2021, Alabama income is determined by single sales factor apportionment (ALDOR Corporate Income Tax page).
- Corporations and other entities also file the Alabama business privilege tax, a separate tax on net worth in Alabama (ALDOR Business Privilege Tax Incentives page).
- Affiliated groups: an Alabama consolidated return is filed on Form 20C-C (ALDOR Due Dates page); see `alabama-transfer-pricing`.

## Rates, bands and thresholds

| Item | Rate or amount | Tax year | Source |
|---|---|---|---|
| Corporate income tax | 6.5% of annual net income | 2026 | [ALDOR Corporate Income Tax page](https://www.revenue.alabama.gov/tax-types/corporate-income-tax/) |
| Base modification | Deduction allowed for federal income tax paid or accrued | 2026 | [ALDOR Corporate Income Tax page](https://www.revenue.alabama.gov/tax-types/corporate-income-tax/) |
| Apportionment | Single sales factor for tax years beginning on or after January 1, 2021 | 2021 onward | [ALDOR Corporate Income Tax page](https://www.revenue.alabama.gov/tax-types/corporate-income-tax/) |
| Form 20C due date, calendar-year C corporation | Return May 15 (one month after the federal due date, Act 2022-53); the tax itself is due without that extra month | 2026 | [ALDOR Due Dates page](https://www.revenue.alabama.gov/individual-corporate/due-dates/) |
| Form 20C due date, fiscal year (not June 30) | 15th day of the 5th month after the fiscal year end; June 30 year end: October 15 | 2026 | [ALDOR Due Dates page](https://www.revenue.alabama.gov/individual-corporate/due-dates/) |
| Business privilege tax rate | $0.25 to $1.75 for each $1,000 of net worth in Alabama, graduated by federal taxable income apportioned to Alabama | 2026 | [ALDOR Business Privilege Tax Incentives page](https://www.revenue.alabama.gov/tax-incentives/business-privilege-tax-incentives/) |
| Business privilege tax return due date, C corporation | Same date as the federal income tax return: 15th day of the 4th month after the start of the taxable year (fiscal year June 30: 15th day of the 3rd month) | 2026 | [ALDOR Due Dates page](https://www.revenue.alabama.gov/individual-corporate/due-dates/) |
| Business privilege tax filing floor / maximum | For 2026, calculated privilege tax due of $100 or less has no filing requirement; ordinary C-corporation/REIT/corporate-LLE cap $15,000; specified financial-institution group/insurance cap $3 million | 2026 | [2026 CPT instructions, filing requirement and line 20](https://www.revenue.alabama.gov/wp-content/uploads/2026/01/26fcptinstr.pdf) |

Statutory authority (ALDOR Corporate Income Tax page): Sections 40-18-1 to 40-18-59 and 40-18-160 to 40-18-176, Code of Alabama 1975; franchise-tax authority Sections 40-27-1 to 40-27-6. Rate history: Amendment 212 (ratified December 18, 1963) raised the allowable maximum to 5 percent with the federal-tax deduction; Amendment 662 (ratified June 19, 2000) raised the rate to 6.5 percent beginning calendar year 2001.

The distinctive base feature: "6.5 percent of annual net income with a deduction allowed for federal income tax paid or accrued" (ALDOR page). The Alabama effective rate therefore moves with the federal bill: a restructuring that changes federal tax changes Alabama tax even with identical net income.


### 2026 business privilege tax bands and return flow

The general incentives page still says a $50 minimum. The **2026 CPT instructions** and **2026 Quick Preparation Reference** supersede that summary for this year: if the calculated privilege tax due is $100 or less, stop; no return is required. The older $50 claim is not current 2026 filing guidance.

| Federal taxable income apportioned to Alabama, before NOL/special deductions | Rate on taxable Alabama net worth | Source |
|---|---|---|
| Less than $1 | $0.25 per $1,000 (.00025) | [2026 CPT instructions, line 17b, section 40-14A-22(b)](https://www.revenue.alabama.gov/wp-content/uploads/2026/01/26fcptinstr.pdf) |
| At least $1, below $200,000 | $1.00 per $1,000 (.00100) | [2026 CPT instructions, line 17b](https://www.revenue.alabama.gov/wp-content/uploads/2026/01/26fcptinstr.pdf) |
| At least $200,000, below $500,000 | $1.25 per $1,000 (.00125) | [2026 CPT instructions, line 17b](https://www.revenue.alabama.gov/wp-content/uploads/2026/01/26fcptinstr.pdf) |
| At least $500,000, below $2,500,000 | $1.50 per $1,000 (.00150) | [2026 CPT instructions, line 17b](https://www.revenue.alabama.gov/wp-content/uploads/2026/01/26fcptinstr.pdf) |
| $2,500,000 or more | $1.75 per $1,000 (.00175) | [2026 CPT instructions, line 17b](https://www.revenue.alabama.gov/wp-content/uploads/2026/01/26fcptinstr.pdf) |

Apply the bracket to the **net-worth base**, not to the income used to choose the bracket. The federal-income-tax deduction is not allowed in selecting the privilege-tax rate. For C corporations, use Form CPT; S corporations and ordinary limited-liability/disregarded entities use Form PPT. A single-member LLC does not use its owner's FEIN/SSN. Determine the correct determination period: it generally uses the prior accounting-period balance sheet, while the privilege tax is for the current taxable/form year. A shorter determination period alone does not establish a prorated short taxable year. Sources: [2026 CPT instructions, general instructions and lines 17-20](https://www.revenue.alabama.gov/wp-content/uploads/2026/01/26fcptinstr.pdf), [2026 quick reference](https://www.revenue.alabama.gov/wp-content/uploads/2026/01/26quickrefcptpptinst.pdf).

For Form CPT, page 2 computes total net worth, exclusions and apportionment; deductions carry to line 15; line 16 is taxable Alabama net worth; 17a income selects 17b rate; 18 is gross privilege tax; 19 enterprise-zone credit; 20 privilege tax due, with the $100 stop rule. Transfer due tax to page 1 line 5, reconcile prior payments, penalty and interest, and retain the filing/payment confirmations. Pay by the original due date, using BPT-V for paper payments unless paying electronically. Newly organized/qualified entities use BPT-IN within two and one-half months if calculated tax exceeds $100; electing family LLEs have a separate $500 cap. Sources: [2026 CPT instructions](https://www.revenue.alabama.gov/wp-content/uploads/2026/01/26fcptinstr.pdf), [2026 quick reference](https://www.revenue.alabama.gov/wp-content/uploads/2026/01/26quickrefcptpptinst.pdf).

### Corporate estimates and published return mapping

The following Form 20C workflow is the **2025-2026 filing cycle**, from the latest instructions read, not confirmation of final 2026 Form 20C lines. [2025 Form 20C instructions, pages 1-3](https://www.revenue.alabama.gov/wp-content/uploads/2026/01/25f20cinstr.pdf):

- The instructions require estimates where annual corporate liability exceeds $500; the current FAQ uses $500 or more, so treat exact-boundary liability conservatively and confirm the applicable return instructions. The four instalments are on the 15th of months 4, 6, 9 and 12, each normally 25% of required annual payment.
- Ordinary required annual payment is the lesser of 100% current-year tax or 100% prior-year tax, where the prior return showed a liability and covered 12 months. Large corporations with at least $1 million taxable income in any of the prior three taxable years use current-year tax, subject to the first-instalment exception and Form 2220AL annualized/seasonal/K-1 exceptions described in the instructions.
- Form 20C line 1 begins with federal taxable income; line 2 adds federal NOL; Schedule A reconciles state differences; Schedule C allocates nonbusiness items; Schedule D handles applicable apportionment; federal income-tax deduction and Alabama NOL are applied before line 14 taxable income; line 15 applies the state rate. Do not replace this sequence with an assumed federal-to-state flat-rate shortcut.
- An Alabama NOL has its own schedule; the published instructions state a 15-year carryforward and no carryback. Schedule B and supporting prior returns are required; final 2026 conformity/return changes are not assumed here.
- Payments of $750 or more are electronic through My Alabama Taxes or an approved ACH method. Paper business-income-tax payments use BIT-V. Reconcile line 20 payments and credits to the account; keep return acknowledgment and payment reference separately. A filing extension does not extend payment, and the extra month for the corporate return is filing only. Weekend/holiday due dates move to the following business day under the published instructions.

## The taxable base

There is no minimum corporate income tax, distinct from the business privilege tax filing floor. For multistate taxpayers, the federal-income-tax deduction is limited to federal tax attributable to Alabama income; the net federal liability is after deductible/refundable credits. [ALDOR Corporate Income Tax FAQs, minimum tax and federal deduction](https://www.revenue.alabama.gov/faq-categories/corporate-income-tax/).

- Net taxable income from business within the state (ALDOR page, Application).
- A deduction is allowed for federal income tax paid or accrued (ALDOR page).
- Foreign corporations: taxes due are based on income derived from sources within Alabama (Amendment 212, as published on the ALDOR page).
- Multistate corporations apportion with the single sales factor (Alabama sales over total sales).

## Deadlines and filing

- Form 20C, calendar year: return due May 15. The one-month extra time from Act 2022-53 is "an extension for filing purposes ONLY. The full amount of the tax liability is due on or by the original due date of the return without the benefit of the additional one-month extension" (ALDOR Due Dates page). Fiscal year other than June 30: the 15th day of the 5th month after year end; June 30 year end: October 15. Form 1120-F filers: July 15 for calendar years (ALDOR Due Dates page).
- Extensions: "If an extension has been granted for federal purposes, the extension is also granted for Alabama purposes; the Federal Form 7004 must be submitted with the Form 20C or Form 20C-C" (ALDOR Due Dates page).
- An Alabama consolidated return is filed on Form 20C-C, on the same dates (ALDOR Due Dates page).
- Business privilege tax returns: C corporations on the federal return date (15th day of the 4th month for calendar years); S corporations and limited liability entities on the federal return date, the 15th day of the 3rd month after the start of the taxable year (ALDOR Due Dates page).

## Penalties and interest

- The published Form 20C instructions, **2025-2026 filing cycle**, line 21c, state late filing at 10% of tax due or $50, whichever is greater; late income-tax payment at 1% per month or part, capped at 25%, plus section 40-1-44 interest. Estimated-payment penalties have separate rules and Form 2220AL exceptions. Final 2026 form changes are not assumed. [Form 20C instructions](https://www.revenue.alabama.gov/wp-content/uploads/2026/01/25f20cinstr.pdf).
- Common failure modes to check for: (1) forgetting the federal-income-tax deduction when projecting Alabama cost on a restructuring that changes the federal bill; (2) apportioning with a pre-2021 multi-factor spreadsheet; (3) missing the business privilege tax while focused on the income tax; (4) paying the tax with the return on May 15, when the tax was due without the Act 2022-53 extra month, or filing an extended return without the federal Form 7004.

## Cross-border points

- Foreign (out-of-state) corporations are taxed only on income derived from sources within Alabama (Amendment 212, ALDOR page).
- Single sales factor means market-state sourcing of sales drives the apportionment fraction; see `alabama-cross-border` and `alabama-transfer-pricing`.

## Worked examples

Client facts in these examples are hypothetical. Only figures from the table above are used (6.5% rate, federal-tax deduction, single sales factor).

**Example 1: domestic corporation, federal-tax deduction**

A domestic corporation with $500,000 federal taxable income and $60,000 federal income tax paid, 100% Alabama sales.

```oa-check
name: AL corporate tax with federal tax deduction
inputs:
  fti: 500000
  fed_tax: 60000
  rate: 0.065
steps:
  - al_base: fti - fed_tax
  - tax: al_base * rate
expected:
  al_base: 440000.00
  tax: 28600.00
```

**Example 2: multistate single sales factor**

Same corporation, total sales $5,000,000, Alabama sales $1,200,000.

```oa-check
name: AL single sales factor apportionment
inputs:
  al_sales: 1200000
  total_sales: 5000000
  al_base: 440000
  rate: 0.065
steps:
  - factor: al_sales / total_sales
  - apportioned: al_base * factor
  - tax: apportioned * rate
expected:
  factor: 0.24
  apportioned: 105600.00
  tax: 6864.00
```

**Example 3, privilege-tax filing boundary, both outcomes**

Assume an ordinary C corporation has $250,000 income for selecting its privilege-tax rate and no credits. At taxable Alabama net worth $80,000, the .00125 rate produces $100: no filing under the 2026 CPT stop rule. At net worth $100,000, it produces $125: file and pay $125, subject to the actual return facts. A $15,000 ordinary cap does not change either result.

```oa-check
name: AL 2026 business privilege filing boundary
inputs:
  net_worth_low: 80000
  net_worth_high: 100000
  rate: 0.00125
steps:
  - calculated_low: net_worth_low * rate
  - calculated_high: net_worth_high * rate
  - high_after_cap: min(calculated_high, 15000)
expected:
  calculated_low: 100
  calculated_high: 125
  high_after_cap: 125
```

## Ask the client first

- Is the federal-income-tax deduction modelled in state projections (it moves with federal credits, NOLs, capitalization)?
- Post-2021 apportionment: is the sales-factor numerator market-based and complete (delivery state for tangible goods)?
- Is the business privilege tax return being filed alongside the income tax?
- Is the group filing separately or on an Alabama consolidated return (Form 20C-C)?
- Fiscal year end, and has a federal extension (Form 7004) been filed?

## Sources

| # | Source | URL | Read on |
|---|---|---|---|
| 1 | ALDOR Corporate Income Tax page, read for rate 6.5% with federal-tax deduction, single sales factor from tax years beginning 2021-01-01, authority sections, Amendments 212 and 662 | https://www.revenue.alabama.gov/tax-types/corporate-income-tax/ | 2026-11-13 |
| 2 | ALDOR Due Dates page, read for Form 20C and 20C-C due dates, Act 2022-53, payment timing, Form 7004 extension, business privilege tax due dates | https://www.revenue.alabama.gov/individual-corporate/due-dates/ | 2026-11-13 |
| 3 | ALDOR Business Privilege Tax Incentives page, read for the rate range and caps; its $50 minimum is superseded by the 2026 CPT instructions | https://www.revenue.alabama.gov/tax-incentives/business-privilege-tax-incentives/ | 2026-11-13 |

| 4 | 2026 CPT instructions, read for filing requirement, full rate bands, net-worth computation, determination period, lines 15-20, maximums and payment timing | https://www.revenue.alabama.gov/wp-content/uploads/2026/01/26fcptinstr.pdf | 2026-11-13 |
| 5 | 2026 Quick Preparation Reference, read for forms, identifiers, bands, BPT-IN timing, cap and payment voucher | https://www.revenue.alabama.gov/wp-content/uploads/2026/01/26quickrefcptpptinst.pdf | 2026-11-13 |
| 6 | Form 20C instructions, 2025-2026 filing cycle, read for pages 1-3 on estimates, methods/exceptions, return mapping, NOL, electronic payments and penalties | https://www.revenue.alabama.gov/wp-content/uploads/2026/01/25f20cinstr.pdf | 2026-11-13 |

| 7 | ALDOR Corporate Income Tax FAQs, read for current payment/return distinction, $500 estimate wording, no minimum corporate income tax and the Alabama-attributable net federal-tax deduction | https://www.revenue.alabama.gov/faq-categories/corporate-income-tax/ | 2026-11-13 |

Not yet confirmed: final 2026 Form 20C line mappings and any changes from the explicitly labelled 2025-2026 filing-cycle estimate/NOL workflow; resolution of the $500 estimate boundary between the FAQ and instructions; the Alabama consolidated-return eligibility and election rules; the §40-18-7 state-modification provisions; the S-corporation composite/pass-through mechanics; any changes to corporate penalty rules after the published 2025-2026 filing-cycle instructions; the Uniform Division of Income for Tax Purposes Act text under §40-18-160 onward.

<!-- openaccountants-cta-block -->

---

## Talk to a verified accountant

This guide is maintained by the OpenAccountants network -- accountants who put
their name behind the tax answers AI gives people. The live, always-current
version (and the professional behind it) is at openaccountants.com.

> **General reference only.** This document does not constitute tax, legal, or
> financial advice. Verify figures against the cited primary sources or with a
> licensed professional before relying on them.
