---
name: nc-corporate-tax
description: Compute North Carolina corporate income tax and franchise tax for 2026, and the taxed partnership (pass-through entity) election. Covers the C corporation income tax rate of 2% for taxable years beginning in 2026 and 2027, 1% in 2028 and 2029 and 0% after 2029 (G.S. 105-130.3), single sales factor apportionment with market-based sourcing (G.S. 105-130.4), the 15-year State net loss carryforward (G.S. 105-130.8A), the franchise tax on apportioned net worth at $1.50 per $1,000 (C corporations a $200 minimum and $500 maximum on the first $1,000,000; S corporations $200 on the first $1,000,000; holding companies $200 to $150,000), corporate estimated tax at $500 or more, due dates, penalties and the taxed partnership tax at the individual rate of 3.99%. Trigger on "North Carolina corporate income tax", "NC franchise tax", "Form CD-405", "CD-401S", "NC PTE election", "NC taxed partnership", "NC apportionment".
version: "2.0"
jurisdiction: US-NC
tax_year: 2026
last_updated: 2026-11-13
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
tier: 2
domain: income-tax
type: computation
---

# North Carolina corporate income and franchise tax, 2026

> **Source-cited draft.** Built from G.S. 105-120.2, 105-122, 105-130.3, 105-130.4, 105-130.8A, 105-130.17, 105-154.1, 105-163.39, 105-163.40, 105-163.41 and 105-236, and the NCDOR notice and FAQs on Session Laws 2026-31 and 2026-41, read on 2026-11-13. No accountant has reviewed it. All outputs must be reviewed by a qualified tax professional before filing.

**Answer first.** A C corporation doing business in North Carolina pays income tax of **2%** of its NC-apportioned net income for taxable years beginning in **2026** (and 2027), falling to 1% for 2028 and 2029 and 0% after 2029. Every corporation, C or S, also pays **franchise tax** on its apportioned net worth at **$1.50 per $1,000**: a C corporation pays at least $200 and at most $500 on the first $1,000,000 of base, an S corporation a flat $200 on the first $1,000,000, both $1.50 per $1,000 above that. Income is apportioned by a **single sales factor**. Returns are due on the 15th day of the 4th month after year end (April 15, 2027 for calendar 2026).

## Scope and who this is for

In scope: a C corporation or S corporation doing business in NC for a taxable year beginning in 2026; a partnership considering the taxed partnership election for 2026. The skill produces NC net income, the income tax, the franchise tax base and tax, estimated payments and due dates.

Out of scope, and where it goes:

| Topic | Skill |
| --- | --- |
| Federal taxable income of a C corporation | `us-form-1120-c-corp` |
| Federal partnership return | `us-form-1065-partnership` |
| Whether to elect S status | `us-s-corp-election-decision` |
| How state pass-through entity taxes interact with the federal SALT deduction | `us-pte-state-matrix` |
| The owner's NC individual return | `nc-income-tax` |
| Insurance companies (gross premiums tax), banks, captive REITs | not covered; refer |

## Ask the client first

1. **Entity type for federal tax** (C corporation, S corporation, LLC taxed as either, partnership) and taxable year start date. The year it begins in sets the income tax rate.
2. **Federal taxable income** and the NC adjustments (bonus depreciation, section 179, R&E add-backs, state income taxes deducted).
3. **Sales in NC and everywhere** for the year, with how service and intangible receipts are sourced to the customer's market.
4. **Balance sheet at year end**: total assets before accumulated depreciation, total liabilities, debt owed to related entities. This is the franchise tax base.
5. **Is the corporation a holding company** (assets are only controlled subsidiaries, or more than 80% of gross income from them)?
6. **Prior-year NC tax and the estimated payments made**, and whether it is a "large corporation" under IRC 6655.

## The method, step by step

### Rates, bands and thresholds

| Item | Amount | Source |
| --- | --- | --- |
| C corporation income tax, taxable years beginning in 2026 (and in 2027) | 2% | [G.S. 105-130.3](https://www.ncleg.gov/EnactedLegislation/Statutes/HTML/BySection/Chapter_105/GS_105-130.3.html) |
| Taxable years beginning in 2025 | 2.25% | [G.S. 105-130.3](https://www.ncleg.gov/EnactedLegislation/Statutes/HTML/BySection/Chapter_105/GS_105-130.3.html) |
| Taxable years beginning in 2028 (and in 2029) | 1% | [G.S. 105-130.3](https://www.ncleg.gov/EnactedLegislation/Statutes/HTML/BySection/Chapter_105/GS_105-130.3.html) |
| Taxable years beginning after 2029 | 0% | [G.S. 105-130.3](https://www.ncleg.gov/EnactedLegislation/Statutes/HTML/BySection/Chapter_105/GS_105-130.3.html) |
| S corporation income tax | none (not subject) | [G.S. 105-130.3](https://www.ncleg.gov/EnactedLegislation/Statutes/HTML/BySection/Chapter_105/GS_105-130.3.html) |
| Franchise tax rate | $1.50 per $1,000 of tax base | [G.S. 105-122(d2)](https://www.ncleg.gov/EnactedLegislation/Statutes/HTML/BySection/Chapter_105/GS_105-122.html) |
| C corporation franchise tax on the first $1,000,000 of base: minimum / maximum | $200 / $500 | [G.S. 105-122(d2)](https://www.ncleg.gov/EnactedLegislation/Statutes/HTML/BySection/Chapter_105/GS_105-122.html) |
| S corporation franchise tax on the first $1,000,000 of base | $200 | [G.S. 105-122(d2)](https://www.ncleg.gov/EnactedLegislation/Statutes/HTML/BySection/Chapter_105/GS_105-122.html) |
| Holding company franchise tax: minimum / maximum | $200 / $150,000 | [G.S. 105-120.2(b)](https://www.ncleg.gov/EnactedLegislation/Statutes/HTML/BySection/Chapter_105/GS_105-120.2.html) |
| State net loss carryforward | 15 years | [G.S. 105-130.8A(b)](https://www.ncleg.gov/EnactedLegislation/Statutes/HTML/BySection/Chapter_105/GS_105-130.8A.html) |
| Corporate estimated tax required when estimated tax is at least | $500 | [G.S. 105-163.40(a)](https://www.ncleg.gov/EnactedLegislation/Statutes/HTML/BySection/Chapter_105/GS_105-163.40.html) |
| Estimated tax safe level (current year, or annualized) | 90% | [G.S. 105-163.41(b), (d)](https://www.ncleg.gov/EnactedLegislation/Statutes/HTML/BySection/Chapter_105/GS_105-163.41.html) |
| Taxed partnership tax rate, 2026 (the individual rate) | 3.99% | [G.S. 105-154.1(b)](https://www.ncleg.gov/EnactedLegislation/Statutes/HTML/BySection/Chapter_105/GS_105-154.1.html); [G.S. 105-153.7](https://www.ncleg.gov/EnactedLegislation/Statutes/HTML/BySection/Chapter_105/GS_105-153.7.html) |
| Add-back of domestic R&E expenditures expensed under IRC 174A(a); then 25% deducted in each of the next four years | 80% | [NCDOR notice, 23 July 2026](https://www.ncdor.gov/taxes-forms/information-tax-professionals/tax-bulletins-directives-and-other-important-notices/important-notices-and-frequently-asked-questions-personal-taxes/important-notice-impact-recently-enacted-laws-north-carolina-individual-and-corporate-income) (G.S. 105-130.5C) |
| Internal Revenue Code conformity date | July 5, 2025 | [NCDOR notice, 23 July 2026](https://www.ncdor.gov/taxes-forms/information-tax-professionals/tax-bulletins-directives-and-other-important-notices/important-notices-and-frequently-asked-questions-personal-taxes/important-notice-impact-recently-enacted-laws-north-carolina-individual-and-corporate-income) |

### Step 1: NC net income

Start from federal taxable income ("FTI") under the Internal Revenue Code as of July 5, 2025, and make the NC adjustments of G.S. 105-130.5 (for example, 80% of the R&E deduction taken under IRC 174A(a) is added back under G.S. 105-130.5C, and recovered 25% a year over the next four years). The result is State net income before apportionment.

### Step 2: apportion by the sales factor

Apportionable income is multiplied by the **sales factor**: NC sales divided by sales everywhere ([G.S. 105-130.4(i), (l)](https://www.ncleg.gov/EnactedLegislation/Statutes/HTML/BySection/Chapter_105/GS_105-130.4.html)). Casual sales of property are left out of both. Receipts from services and intangibles are in NC if the taxpayer's **market** for them is in NC; if the market cannot be determined, it is reasonably approximated, and if that is not possible the receipt is excluded. Nonapportionable income is allocated separately. Railroads, motor carriers, air carriers and other special industries use their own formulas in G.S. 105-130.4 (refer).

### Step 3: subtract the State net loss

Deduct NC net losses from the preceding **15** taxable years, oldest first ([G.S. 105-130.8A](https://www.ncleg.gov/EnactedLegislation/Statutes/HTML/BySection/Chapter_105/GS_105-130.8A.html)). The loss is apportioned to NC in the year it arose. After a merger or acquisition, NCDOR applies the IRC 381 and 382 regulations on a separate-entity basis.

### Step 4: income tax

Income tax = NC taxable income × the rate for the year the taxable year **begins** (2% for a year beginning in 2026). An S corporation pays no NC income tax.

### Step 5: franchise tax base and tax

1. **Net worth** = total assets **without** deducting accumulated depreciation, depletion and amortization, less total liabilities, under GAAP (or the corporation's own method if it does not keep GAAP books), as of year end ([G.S. 105-122(b)](https://www.ncleg.gov/EnactedLegislation/Statutes/HTML/BySection/Chapter_105/GS_105-122.html)).
2. **Then**: deduct accumulated depreciation, depletion and amortization computed as for federal tax; **add** debt owed to a parent, subsidiary, affiliate or a more-than-50%-owned noncorporate entity (unless it creates qualified interest expense); deduct investments in more-than-80%-owned insurance companies.
3. **Apportion** with the same fraction used for income tax ([G.S. 105-122(c1)](https://www.ncleg.gov/EnactedLegislation/Statutes/HTML/BySection/Chapter_105/GS_105-122.html)). From 2023 the tax base is only this apportioned net worth; the old property-value alternatives are gone ([G.S. 105-122(d)](https://www.ncleg.gov/EnactedLegislation/Statutes/HTML/BySection/Chapter_105/GS_105-122.html)).
4. **Tax** ([G.S. 105-122(d2)](https://www.ncleg.gov/EnactedLegislation/Statutes/HTML/BySection/Chapter_105/GS_105-122.html)): C corporation, $1.50 per $1,000 on the first $1,000,000 but not less than $200 or more than $500, plus $1.50 per $1,000 above $1,000,000. S corporation, $200 for the first $1,000,000 plus $1.50 per $1,000 above it. A **holding company** ([G.S. 105-120.2](https://www.ncleg.gov/EnactedLegislation/Statutes/HTML/BySection/Chapter_105/GS_105-120.2.html)) uses the same rate but pays at least $200 and at most $150,000.

Counties and cities may not levy a franchise tax on corporations ([G.S. 105-122(g)](https://www.ncleg.gov/EnactedLegislation/Statutes/HTML/BySection/Chapter_105/GS_105-122.html)).

### Step 6: estimated tax

A C corporation whose estimated tax is **$500 or more** before the 1st day of the 4th month pays it in four equal installments by the 15th day of the **4th, 6th, 9th and 12th months** (April 15, June 15, September 15 and December 15 for a calendar year). If the $500 level is first reached later, the remaining installments are three, two or one ([G.S. 105-163.40(a)](https://www.ncleg.gov/EnactedLegislation/Statutes/HTML/BySection/Chapter_105/GS_105-163.40.html)). Interest on an underpayment runs on each installment short of 90% of the year's tax, at the G.S. 105-241.21 rate. No interest is due if the payments cover the least of: the prior year's tax (12-month year, return filed), the current rates applied to the prior year's facts, or 90% of annualized income tax. A **large corporation** (IRC 6655) cannot use the two prior-year tests ([G.S. 105-163.41](https://www.ncleg.gov/EnactedLegislation/Statutes/HTML/BySection/Chapter_105/GS_105-163.41.html)). A taxed pass-through entity follows the same rules from its second taxed year ([G.S. 105-163.39(d)](https://www.ncleg.gov/EnactedLegislation/Statutes/HTML/BySection/Chapter_105/GS_105-163.39.html)). A corporation that pays federal estimates by electronic funds transfer pays NC estimates the same way.

### Step 7: taxed partnership election (pass-through entity tax)

A partnership may elect on its **timely filed** return to be taxed itself; it cannot make or revoke the election after the return is filed ([G.S. 105-154.1(a)](https://www.ncleg.gov/EnactedLegislation/Statutes/HTML/BySection/Chapter_105/GS_105-154.1.html)). A publicly traded partnership cannot elect, nor can one with a partner that is not an individual, an estate, certain trusts, a 1361(c)(6) organization, or a partnership or corporation. The tax is the individual rate of G.S. 105-153.7 (**3.99%** for 2026) on the sum of the individual-type partners' distributive shares attributable to NC, after the NC adjustments; separately stated deductions are left out. The full tax is paid with the return. Partners then deduct their NC-taxed share on Schedule S (G.S. 105-153.5(c3)); basis is figured as if no election had been made. Credits earned in an election year stay with the partnership.

## Boundary and exception table

| Situation | Treatment |
| --- | --- |
| Taxable year beginning in 2026 but ending in 2027 | 2% (the rate goes by the year the taxable year begins) |
| S corporation | No income tax; franchise tax at $200 on the first $1,000,000 |
| C corporation with a base up to about $133,333 | The $200 minimum applies |
| C corporation with a base from about $333,334 to $1,000,000 | The $500 maximum applies to the first $1,000,000 |
| Holding company | Franchise tax at least $200, at most $150,000 |
| Debt owed to a parent or affiliate | Added to the franchise base unless it creates qualified interest expense |
| Corporation in NC and other states | Net worth apportioned with the income sales factor |
| Disregarded single-member LLC | No entity-level tax; owner reports on D-400 (see `nc-income-tax`) |
| R&E expensed federally under IRC 174A(a) | Add back 80%, deduct 25% of the add-back in each of the next four years |
| Corporation ceasing NC business mid-year | Return due within 105 days after it stops business in NC |
| Losses older than 15 years | Expired |
| Large corporation (IRC 6655) | Must use the 90% current-year or annualized test for estimates |

### Defaults when a fact is missing

| Missing fact | Default, and flag it |
| --- | --- |
| Market location of service receipts | Do not guess; reasonable approximation needs facts, ask |
| Related-party debt | Assume none and flag the franchise base as provisional |
| Prior-year NC tax | Use the 90% current-year test for estimates |

## Worked cases

### Case 1: C corporation with sales in several states

Calendar 2026. NC net income before apportionment $1,000,000; NC sales $400,000 of $1,000,000 everywhere, so the sales factor is 40% and NC taxable income is $400,000. Income tax at 2%: **$8,000**. Franchise base: adjusted net worth $7,500,000 × 40% = $3,000,000. On the first $1,000,000 the $1,500 computed tax is capped at $500; on the other $2,000,000, $3,000. Franchise tax **$3,500**. Total NC tax $11,500. Estimated income tax is above $500, so four installments of $2,000 are due April 15, June 15, September 15 and December 15, 2026.

```oa-check
name: NC 2026 C corporation income and franchise tax
inputs:
  pre_income: 1000000
  nc_sales: 400000
  all_sales: 1000000
  rate: 0.02
  net_worth: 7500000
steps:
  - factor: nc_sales / all_sales
  - nc_income: pre_income * factor
  - income_tax: nc_income * rate
  - base: net_worth * factor
  - first_slice: clamp(min(base, 1000000) * 1.5 / 1000, 200, 500)
  - excess: max(base - 1000000, 0) * 1.5 / 1000
  - franchise: first_slice + excess
  - installment: income_tax / 4
expected:
  nc_income: 400000
  income_tax: 8000
  franchise: 3500
  installment: 2000
```

### Case 2: C corporation or S corporation, what changes in franchise tax

The same company has an apportioned franchise base of $600,000. As a C corporation: $1.50 per $1,000 gives $900, capped at **$500**. As an S corporation: **$200**. With a base of $100,000 the C corporation computation gives $150, raised to the **$200** minimum, so the two are equal. The franchise difference never exceeds $300 a year; the bigger difference is that the C corporation also pays 2% income tax and the S corporation's owners pay 3.99% on their share through `nc-income-tax`.

```oa-check
name: NC 2026 franchise tax, C versus S corporation
inputs:
  base_mid: 600000
  base_small: 100000
steps:
  - c_mid: clamp(min(base_mid, 1000000) * 1.5 / 1000, 200, 500) + max(base_mid - 1000000, 0) * 1.5 / 1000
  - s_mid: 200 + max(base_mid - 1000000, 0) * 1.5 / 1000
  - c_small: clamp(min(base_small, 1000000) * 1.5 / 1000, 200, 500)
  - s_small: 200
  - difference_mid: c_mid - s_mid
expected:
  c_mid: 500
  s_mid: 200
  c_small: 200
  difference_mid: 300
```

## When to refuse or refer

| Situation | Action |
| --- | --- |
| Railroad, motor carrier, air carrier, telephone or other special-industry apportionment | Refer |
| Alternative apportionment request (G.S. 105-130.4 or 105-122(c1)(2)) | Refer; the Secretary's decision is final and covers at most three years |
| Combined or consolidated return, or a forced combination | Refer |
| Insurance company, bank, captive REIT or RIC | Refer |
| Merger, acquisition or ownership change affecting losses | Refer |
| Taxed S corporation election, or partners that are not individuals | Refer; only the partnership rules were read |
| A 2025 return affected by S.L. 2026-31 (R&E add-back retroactive to 2022 for some taxpayers) | Refer; follow the NCDOR notice of 23 July 2026 |

## Filing and payment

| Obligation | When | Source |
| --- | --- | --- |
| Corporate income tax return | 15th day of the 4th month after year end (April 15, 2027 for calendar 2026) | [G.S. 105-130.17(b)](https://www.ncleg.gov/EnactedLegislation/Statutes/HTML/BySection/Chapter_105/GS_105-130.17.html) |
| Franchise tax return | Same date, signed by an officer | [G.S. 105-122(a)](https://www.ncleg.gov/EnactedLegislation/Statutes/HTML/BySection/Chapter_105/GS_105-122.html) |
| Corporation that files its federal return under IRC 6072(c) | 15th day of the 7th month | [G.S. 105-130.17(g)](https://www.ncleg.gov/EnactedLegislation/Statutes/HTML/BySection/Chapter_105/GS_105-130.17.html) |
| Extension | Available under G.S. 105-263 | [G.S. 105-130.17(d)](https://www.ncleg.gov/EnactedLegislation/Statutes/HTML/BySection/Chapter_105/GS_105-130.17.html) |
| Estimated tax | 15th day of months 4, 6, 9 and 12 | [G.S. 105-163.40](https://www.ncleg.gov/EnactedLegislation/Statutes/HTML/BySection/Chapter_105/GS_105-163.40.html) |
| Taxed partnership tax | Paid in full with the timely partnership return | [G.S. 105-154.1(f)](https://www.ncleg.gov/EnactedLegislation/Statutes/HTML/BySection/Chapter_105/GS_105-154.1.html) |
| Late filing / late payment / negligence | 5% a month up to 25%; 5% of the tax (until July 1, 2030); 10% of the deficiency | [G.S. 105-236(a)(3) to (5)](https://www.ncleg.gov/EnactedLegislation/Statutes/HTML/BySection/Chapter_105/GS_105-236.html) |
| Interest | 7% a year to 31 December 2026; 8% for 1 January to 30 June 2027 | [NCDOR interest rate](https://www.ncdor.gov/interest) |

## Completion checklist

- [ ] Rate year set by the start of the taxable year
- [ ] NC adjustments, including the R&E add-back, listed
- [ ] Sales factor built with market-based sourcing; casual sales excluded
- [ ] Losses carried forward no more than 15 years, oldest first
- [ ] Franchise base from net worth, related-party debt added, apportioned
- [ ] C or S or holding company limits applied
- [ ] Estimated payments tested against the three safe levels (not prior-year for a large corporation)

## Sources

| Source | URL | Read for | Read on |
| --- | --- | --- | --- |
| G.S. 105-130.3 | https://www.ncleg.gov/EnactedLegislation/Statutes/HTML/BySection/Chapter_105/GS_105-130.3.html | Read for corporate rates 2025 to after 2029 | 2026-11-13 |
| G.S. 105-130.4 | https://www.ncleg.gov/EnactedLegislation/Statutes/HTML/BySection/Chapter_105/GS_105-130.4.html | Read for the single sales factor and market sourcing | 2026-11-13 |
| G.S. 105-130.8A | https://www.ncleg.gov/EnactedLegislation/Statutes/HTML/BySection/Chapter_105/GS_105-130.8A.html | Read for the 15-year State net loss carryforward | 2026-11-13 |
| G.S. 105-130.17 | https://www.ncleg.gov/EnactedLegislation/Statutes/HTML/BySection/Chapter_105/GS_105-130.17.html | Read for due dates | 2026-11-13 |
| G.S. 105-122 | https://www.ncleg.gov/EnactedLegislation/Statutes/HTML/BySection/Chapter_105/GS_105-122.html | Read for the franchise tax base, apportionment and rates from 2025 | 2026-11-13 |
| G.S. 105-120.2 | https://www.ncleg.gov/EnactedLegislation/Statutes/HTML/BySection/Chapter_105/GS_105-120.2.html | Read for the holding company definition and $150,000 maximum | 2026-11-13 |
| G.S. 105-154.1 | https://www.ncleg.gov/EnactedLegislation/Statutes/HTML/BySection/Chapter_105/GS_105-154.1.html | Read for the taxed partnership election, rate and payment | 2026-11-13 |
| G.S. 105-163.39 | https://www.ncleg.gov/EnactedLegislation/Statutes/HTML/BySection/Chapter_105/GS_105-163.39.html | Read for estimated tax declarations and taxed pass-through entities | 2026-11-13 |
| G.S. 105-163.40 | https://www.ncleg.gov/EnactedLegislation/Statutes/HTML/BySection/Chapter_105/GS_105-163.40.html | Read for the $500 level and installment dates | 2026-11-13 |
| G.S. 105-163.41 | https://www.ncleg.gov/EnactedLegislation/Statutes/HTML/BySection/Chapter_105/GS_105-163.41.html | Read for underpayment and the safe levels | 2026-11-13 |
| G.S. 105-153.7 | https://www.ncleg.gov/EnactedLegislation/Statutes/HTML/BySection/Chapter_105/GS_105-153.7.html | Read for the 3.99% rate used by taxed partnerships | 2026-11-13 |
| G.S. 105-236 | https://www.ncleg.gov/EnactedLegislation/Statutes/HTML/BySection/Chapter_105/GS_105-236.html | Read for penalties | 2026-11-13 |
| NCDOR notice on S.L. 2026-31 and 2026-41 | https://www.ncdor.gov/taxes-forms/information-tax-professionals/tax-bulletins-directives-and-other-important-notices/important-notices-and-frequently-asked-questions-personal-taxes/important-notice-impact-recently-enacted-laws-north-carolina-individual-and-corporate-income | Read for IRC conformity to July 5, 2025 and the corporate R&E add-back | 2026-11-13 |
| NCDOR FAQs on recent Session Law changes | https://www.ncdor.gov/taxes-forms/corporate-income-franchise-tax/frequently-asked-questions-and-important-notices/faqs-regarding-recent-session-law-changes | Read for static conformity and the January 2027 forms | 2026-11-13 |
| NCDOR interest rate | https://www.ncdor.gov/interest | Read for 7% and 8% | 2026-11-13 |

Not yet confirmed: the 2026 form numbers and lines (CD-405 for C corporations, CD-401S for S corporations, D-403 for partnerships, CD-429 for estimates and CD-419 for extensions are the names used before; 2026 forms publish in January 2027); the G.S. 105-130.5 list of adjustments beyond R&E (not read); the extension terms of G.S. 105-263 (not read); the taxed S corporation election statute (not read); whether an LLC taxed as a corporation is a "corporation" for franchise tax (G.S. 105-114.1, not read).
