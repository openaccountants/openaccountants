---
name: mi-corporate-income-tax
description: "Compute the Michigan Corporate Income Tax (CIT) for a C corporation or unitary business group for tax year 2026, on Form 4891 with Form 4893 and Form 4894 for the Small Business Alternative Credit. Covers who files (the $350,000 Michigan gross receipts and $100 liability thresholds), the 6% rate, the tax base built from federal taxable income with the MCL 206.623 additions and subtractions, the 10-year post-apportionment business loss, single sales factor apportionment with destination and market sourcing, unitary business groups, the Small Business Alternative Credit (1.8% alternative tax, $20,000,000 gross receipts limit, $180,000 allocated income limit and the reduced credit table), quarterly estimates over $800 and the April 30 due date. Points to the Flow-Through Entity Tax, the legacy MBT election and city income taxes. Trigger on \"Michigan corporate income tax\", \"MI CIT\", \"Form 4891\", \"Form 4893\", \"small business alternative credit\", \"Michigan apportionment\", \"unitary business g"
license: "AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)"
metadata:
  source: openaccountants
  openaccountants_url: "https://www.openaccountants.com/skills/mi-corporate-income-tax"
  jurisdiction: "US-MI"
  tax_year: "2026"
  last_updated: "2026-11-13"
---

# Michigan Corporate Income Tax, tax year 2026

> **Source-cited draft.** Built from the Income Tax Act of 1967, Part 2 (MCL 206.611, 206.623, 206.661, 206.663, 206.665 and 206.685, read on the Michigan Legislature site), the 2025 Form 4890 general instructions for standard taxpayers, the 2025 Form 4893 and its instructions, all read on 2026-11-13. Treasury had not published the 2026 CIT forms when read, so the indexed small business limit is the 2025-2026 filing cycle figure. No accountant has reviewed it. All outputs must be reviewed by a qualified tax professional before filing.

**Answer first.** Michigan taxes a C corporation at a flat **6.0%** of its business income after apportionment (MCL 206.623(1)). A corporation files only if its Michigan apportioned or allocated gross receipts are **$350,000 or more** and its CIT liability is more than **$100** (MCL 206.685(1)). Apportionment is by the sales factor alone (MCL 206.663(3)). A small corporation may cut its tax with the Small Business Alternative Credit: the tax is limited to **1.8% of adjusted business income**, if gross receipts are no more than **$20,000,000**, adjusted business income no more than **$1,795,300** (2025-2026 filing cycle) and no shareholder or officer has allocated income over **$180,000** (Form 4893). The annual return is due the last day of the fourth month after the year end: **April 30, 2027** for calendar 2026.

## Scope and who this is for

**In scope.** A "taxpayer" for CIT is a corporation, insurance company, financial institution or unitary business group liable for the tax (MCL 206.611(5)). This skill covers standard taxpayers: C corporations, LLCs taxed as corporations, and unitary business groups of them, filing Form 4891 (Form 4890 instructions).

- A corporation with no S election, or an LLC that elected corporate status on Form 8832 and did not make an S election, is a C corporation and is in scope.
- A corporation whose S election ended is in scope from the date it ended.
- A single-member LLC disregarded for federal tax is disregarded for CIT too (Form 4893 instructions): its activity is reported by its owner. If the owner is a C corporation, the owner reports it here; if the owner is an individual, it goes to the individual return (`mi-income-tax`).
- A tax-exempt organization is in scope only for its unrelated business activity (MCL 206.611(3), (8)).

**Out of scope.**

| Who | Where it goes |
|---|---|
| S corporations and partnerships (and LLCs taxed as partnerships) | Not CIT taxpayers. Owners report on their own returns. The entity may elect the Flow-Through Entity Tax: see the FTE section below and `us-pte-state-matrix`. |
| Sole proprietors | `mi-income-tax` |
| Insurance companies (Part 2, chapter 12) and financial institutions (chapter 13) | Separate regimes and forms. Refuse and refer. |
| Taxpayers still on the Michigan Business Tax under a certificated credit election | Refuse and refer (see "When to refuse or refer"). |
| City income taxes (Detroit and 23 other cities) | Separate city returns. See `mi-detroit-individual-return` for Detroit and the city list in `mi-payroll`. |
| Federal taxable income | `us-form-1120-c-corp` |

## Ask the client first

1. Is the entity a C corporation (or LLC taxed as one) for federal tax, and what is its tax year?
2. Does it own more than 50% of, or is it more than 50% owned by, other corporations it does business with? (Unitary business group test, MCL 206.611(6).)
3. Total gross receipts, and receipts sourced to Michigan under MCL 206.665, for the year.
4. Federal taxable income, and the amounts of each MCL 206.623 adjustment (state and local income taxes deducted, other states' bond interest, US obligation interest, related-party intangible expenses, foreign dividends, any federal NOL deduction).
5. For each shareholder and each officer: compensation, director fees, ownership share and share of business income (for Form 4894).
6. Michigan business losses carried forward from 2016 onwards, and last year's CIT liability (for the estimate safe harbor).

## The method, step by step

### Rates, bands and thresholds

| Item | 2026 figure | Source |
|---|---|---|
| CIT rate | 6.0% of the tax base after allocation or apportionment | [MCL 206.623(1)](https://www.legislature.mi.gov/Laws/MCL?objectName=mcl-206-623) |
| Filing threshold, gross receipts | No return or tax if apportioned or allocated gross receipts are less than $350,000 (prorated for a short year) | [MCL 206.685(1), (2)](https://legislature.mi.gov/Laws/MCL?objectName=mcl-206-685) |
| Filing threshold, liability | No return or tax if the CIT liability is $100 or less | same |
| Business loss carryforward | The year after the loss, then the next 9 years (10 years in all), applied after apportionment; no carryback | [MCL 206.623(4)](https://www.legislature.mi.gov/Laws/MCL?objectName=mcl-206-623) |
| SBAC alternative tax | 1.8% of adjusted business income | [Form 4893 (2025), line 10](https://www.michigan.gov/taxes/-/media/Project/Websites/taxes/Forms/CIT/TY2025/4893_ty2025.pdf) |
| SBAC gross receipts limit | Not available over $20,000,000; reduced over $19,000,000 | same |
| SBAC adjusted business income limit | Not available over $1,795,300 after loss adjustment (2025-2026 filing cycle; the 2026 figure was not yet published) | same |
| SBAC allocated income and compensation limit | Not available if any shareholder or officer has allocated income, or compensation and director fees, over $180,000 | same |
| SBAC reduced credit | Allocated income $160,001 to $164,999: 80%; $165,000 to $169,999: 60%; $170,000 to $174,999: 40%; $175,000 to $180,000: 20% | same |
| Estimated payments required | Estimated annual liability over $800 | [Form 4890 (2025), "Filing CIT Quarterly Tax Estimates"](https://www.michigan.gov/taxes/-/media/Project/Websites/taxes/Forms/CIT/TY2025/4890_ty2025.pdf) |
| Estimate safe harbor | At least 85% of the year's liability; or, if last year's tax was $20,000 or less, last year's tax in four equal instalments | same |
| Estimate due dates (calendar year) | April 15, July 15, October 15, January 15 | same |
| Annual return due date | Last day of the 4th month after the tax year ends | [MCL 206.685(1)](https://legislature.mi.gov/Laws/MCL?objectName=mcl-206-685) |
| Extension | 8 months, on Form 4 with payment of the estimated tax by the due date | [MCL 206.685(3), (4)](https://legislature.mi.gov/Laws/MCL?objectName=mcl-206-685); Form 4890 (2025) |

### Step 1: decide whether the corporation must file

1. Work out gross receipts apportioned or allocated to Michigan. A flow-through entity's gross receipts are imputed to its corporate members by their share of distributive income (MCL 206.685(1)).
2. Under $350,000 (prorated by months for a short year), there is no return and no tax. A return may still be filed to claim back estimates or to create a business loss carryforward (Form 4890).
3. If the computed CIT liability is $100 or less, there is no return and no tax.
4. A taxpayer protected by Public Law 86-272 (15 U.S.C. 381 to 384), whose only Michigan activity is soliciting orders for tangible goods approved and shipped from outside Michigan, owes no CIT (MCL 206.623(1)). The protection does not cover services, intangibles, or activity beyond solicitation (in-state stock, installation, repairs).

### Step 2: build the tax base from business income (MCL 206.623(2))

Start from business income: federal taxable income as defined for CIT (Form 1120, before the federal NOL deduction is added back below). Then, before apportionment:

| Adjustment | Direction | Source |
|---|---|---|
| Interest and dividends on other states' obligations, excluded federally, less the related expenses disallowed under IRC 265 and 291 | Add | MCL 206.623(2)(a) |
| Taxes on or measured by net income deducted federally, including the CIT itself and the corporation's share of Michigan FTE tax paid by a flow-through entity | Add | MCL 206.623(2)(b) |
| Any federal NOL carryback or carryover deducted | Add | MCL 206.623(2)(c) |
| Dividends and royalties from persons that are not United States persons, and from foreign operating entities, including IRC 78 and 951 to 965 amounts | Deduct | MCL 206.623(2)(d) |
| Royalty, interest or other expense paid to a related person outside the unitary group for the use of an intangible asset (unless the taxpayer shows a non-tax business purpose, arm's-length terms and one of the four exceptions: pass-through of a third-party deal, double taxation, unreasonable result, or a treaty-country recipient) | Add | MCL 206.623(2)(e) |
| Interest on United States obligations | Deduct | MCL 206.623(2)(f) |
| Oil and gas production income and expenses (severance-taxed oil and gas) | Eliminate | MCL 206.623(2)(g) |
| Mineral income and expenses, for a qualified taxpayer | Eliminate | MCL 206.623(2)(h) |
| Wages paid for organ donation leave for which a credit under section 279 or 679 is claimed | Add | MCL 206.623(2)(i), added by 2026 PA 39 |

Federal income tax is never deductible: the base starts from federal taxable income, which is already before federal tax.

For a unitary business group, business income is the sum of each member's business income, less income and deductions from transactions between members, including intercompany dividends (MCL 206.623(3)).

### Step 3: apportion

1. A taxpayer whose business activity is only in Michigan allocates its whole base to Michigan. A taxpayer subject to tax in another state apportions (MCL 206.661(2)). It is "subject to tax" in another state if it pays a net income, franchise or similar tax there, or that state could impose one even if it does not (MCL 206.661(3)).
2. Sales factor = Michigan sales / sales everywhere (MCL 206.663(1)). There is no property or payroll factor (MCL 206.663(3)).
3. A unitary business group includes every member's Michigan sales, whether or not that member has nexus, and eliminates sales between members (MCL 206.663(2)).
4. A taxpayer includes its share of the sales of a flow-through entity that is unitary with it (more than 50% owned and with a flow of value) (MCL 206.663(1)).

Sourcing (MCL 206.665(1)):

| Receipt | In Michigan when | Source |
|---|---|---|
| Tangible personal property | Shipped or delivered to a purchaser in Michigan, by ultimate destination where it comes to rest, whatever the f.o.b. point. Goods stored in transit 60 days or more are deemed to have come to rest there. | MCL 206.665(1)(a) |
| Sale, lease or licence of real property | The property is in Michigan | MCL 206.665(1)(b) |
| Lease or rental of tangible property | By days the property is in Michigan during the rental | MCL 206.665(1)(c) |
| Lease of mobile transportation property | By use in Michigan (aircraft: by landings) | MCL 206.665(1)(d) |
| Royalties for intangible property (patents, copyrights, custom software, licences) | The property is used by the purchaser in Michigan | MCL 206.665(1)(e) |
| Services | Where the recipient receives the benefit (the section's services rule; read the full subsection for multi-state benefit) | MCL 206.665 |

No throwback rule appears in MCL 206.663 or 206.665: a sale shipped from Michigan to a state that cannot tax the seller stays out of the Michigan numerator and in the denominator.

### Step 4: apply the rate, then losses

1. Apportioned base x sales factor.
2. Deduct any available business loss after apportionment (MCL 206.623(4)): a loss is a negative apportioned base, carried to the next year and then the next 9 years, oldest first. A buyer of assets in an IRC 381(a)(1) or (2) transaction may use the transferor's loss.
3. Tax = 6.0% of the result.

### Step 5: the Small Business Alternative Credit (Form 4893 with Form 4894)

1. **Eligibility.** Not available to financial institutions or insurance companies. Not available if gross receipts exceed $20,000,000, adjusted business income after loss adjustment exceeds $1,795,300 (2025-2026 filing cycle), or any shareholder or officer has allocated income after loss adjustment over $180,000, or compensation and director fees over $180,000 (Form 4893).
2. **Allocated income** is the greater of (a) the person's compensation and director fees (Form 4894 column L) or (b) for a shareholder, compensation, director fees and share of business income after loss adjustment (column N) (Form 4893 instructions). A sole shareholder-officer's allocated income therefore includes the whole business income.
3. **Adjusted business income** (Form 4893 lines 3 to 9) = business income from Form 4891 line 17 + capital loss carryback or carryover deducted + federal NOL carryback or carryover deducted + compensation and director fees of active shareholders + compensation and director fees of officers. Exclude the distributive share from a flow-through entity that files an MBT return.
4. **Credit** (lines 10 and 11) = tax before the credit minus 1.8% of adjusted business income, not below zero.
5. **Reduction for allocated income** (lines 12 to 14): use the highest allocated income of any shareholder or officer and the reduced credit table above. $160,000 or less: 100%.
6. **Reduction for gross receipts** (lines 15 to 18), only between $19,000,000 and $20,000,000: credit x (100% minus (gross receipts - $19,000,000) / $1,000,000).
7. For a short year, annualize gross receipts, adjusted business income and allocated income to test eligibility and the reduction, but report actual amounts (Form 4893 instructions).
8. **Loss adjustment** (Form 4895): if adjusted business income was negative in any of the five prior years in which an SBAC was received, it may reduce this year's adjusted business income or allocated income. It cannot cure the gross receipts test or the compensation test (Form 4893 instructions).
9. **Unitary groups** test gross receipts and adjusted business income at group level after eliminations, combine everything paid to one individual by all members, and every corporate member files Form 4894. A disqualifier or reduction for one member applies to the whole group.
10. Form 4894 must be filed with Form 4893, or the credit is denied.

The SBAC helps only where 6% of the apportioned base is more than 1.8% of adjusted business income. Because compensation is added back, a business that pays out most of its profit as salary often gets no credit at all.

### Step 6: unitary business groups

- A unitary business group is United States persons (corporations, insurance companies, financial institutions, other than a foreign operating entity) where one owns or controls, directly or indirectly, more than 50% of the voting interests of the others, and the members have a flow of value between them or are integrated with, dependent on or contribute to each other (MCL 206.611(6)). Exactly 50% is not enough.
- Both tests met means one combined filing: the group files one Form 4891 through a designated member, with each member's data on Form 4897 (Form 4890 and Form 4893 instructions).
- Only United States persons can be members, so foreign corporations stay out (water's edge). A foreign operating entity is also excluded.
- An affiliated group may elect to file as a unitary business group under MCL 206.691(2) (named in MCL 206.611(6)).
- A member that joins or leaves mid-year has a tax year ending on the date it joins or leaves and another starting the next day (MCL 206.611(4)).

### Step 7: estimates and payment

1. If the year's liability is reasonably expected to exceed $800, pay quarterly by Form 4913, EFT or Michigan Treasury Online (Form 4890).
2. Each payment is the actual CIT for the quarter or 25% of the expected annual liability.
3. To avoid interest and penalty, estimates must total at least 85% of the year's liability. If last year's tax was $20,000 or less, last year's tax paid in four equal instalments is a safe harbor; it needs a return filed for that prior year and is not available for a first CIT year.
4. Pay the balance by the annual due date. An extension extends time to file, not to pay.

### Forms

| Form | Purpose |
|---|---|
| 4891 | CIT Annual Return (also used by a unitary group through its designated member) |
| 4897 | Data on unitary business group members |
| 4893 | Small Business Alternative Credit |
| 4894 | Schedule of Shareholders and Officers (required with 4893) |
| 4895 | Loss adjustment for the SBAC |
| 4898 | Non-unitary relationships with flow-through entities |
| 4913 | Quarterly estimated return |
| 4892 | Amended return |
| 4 | Application for extension |

## Boundary and exception table

| Situation | Treatment | Source |
|---|---|---|
| Michigan gross receipts $349,000, tax computed $2,000 | No return or tax required | MCL 206.685(1) |
| Short year of 6 months | Filing threshold is $350,000 x 6/12 = $175,000 | MCL 206.685(2) |
| Federal NOL deducted on Form 1120 | Add back; use the Michigan business loss instead | MCL 206.623(2)(c), (4) |
| Dividend from a 30%-owned US corporation | No Michigan deduction beyond what federal taxable income already allows; the statutory deduction is for foreign dividends and royalties | MCL 206.623(2)(d) |
| Dividend from a unitary group member | Eliminated as an intercompany transaction | MCL 206.623(3) |
| Royalty paid to an out-of-group sister company for a trademark | Add back unless the exceptions are shown | MCL 206.623(2)(e) |
| Goods shipped to a Michigan distribution centre, then on to Ohio within 30 days | Not Michigan: they did not come to rest (under 60 days in transit) | MCL 206.665(1)(a) |
| Exactly 50% owned affiliate | Not in the unitary group | MCL 206.611(6) |
| Sole shareholder-officer, salary $100,000, business income $100,000 | Allocated income $200,000: no SBAC | Form 4893 instructions |
| Federal extension filed, no Michigan Form 4 | Treasury does not treat the federal extension as a Michigan one; file Form 4 | Form 4890 (2025) |
| Extension filed but under 90% of tax paid by the due date | 10% negligence penalty may apply | Form 4890 (2025) |

### Defaults when a fact is missing

| Missing fact | Default |
|---|---|
| Whether an affiliate is unitary | Treat as unitary if more than 50% owned and sharing management, financing or purchasing; flag for review |
| Location of a services customer's benefit | Billing address of the customer, flagged as an assumption |
| Shareholder compensation figures | Do not claim the SBAC until Form 4894 data is complete |
| Prior-year liability | Use the 85% current-year method for estimates |

### Red flags to raise with the client

- An old skill or adviser told the client the SBAC wipes out the tax: it only caps it at 1.8% of adjusted business income.
- The owner takes a large salary and the business claims the SBAC: check the $180,000 compensation test first.
- The client holds MEGA, brownfield, historic or other MBT certificated credits: possible MBT election, refer.
- Royalty or interest payments to related companies outside the group.
- Michigan e-file: Treasury enforces an e-file mandate for software-prepared CIT returns (Form 4890).

## Worked cases

**Case 1, a decision: claim the SBAC or not?** A Michigan C corporation sells only in Michigan. 2026 business income (after adjustments) is USD 120,000, gross receipts USD 900,000. Its one shareholder, also the only officer, owns 100% and is paid USD 50,000. No losses, no capital loss or NOL carryovers.

Tax before credit: USD 120,000 x 6% = USD 7,200. Adjusted business income: USD 120,000 + USD 50,000 = USD 170,000, inside the USD 1,795,300 limit. Alternative tax: USD 170,000 x 1.8% = USD 3,060. Credit before reduction: USD 7,200 - USD 3,060 = USD 4,140. Allocated income is the greater of USD 50,000 and USD 50,000 + USD 120,000 = USD 170,000, which falls in the USD 170,000 to USD 174,999 band: 40%. Credit: USD 1,656. Net CIT: USD 5,544. Decision: claim it (file Form 4893 and Form 4894); it saves USD 1,656. Moving profit into salary does not help: allocated income stays the same and adjusted business income does not change either.

```oa-check
name: Michigan SBAC decision, reduced credit (2026)
inputs:
  business_income: 120000
  officer_comp: 50000
  rate: 0.06
  alt_rate: 0.018
  reduction_pct: 0.40
steps:
  - tax_before_credit: business_income * rate
  - adjusted_business_income: business_income + officer_comp
  - alternative_tax: adjusted_business_income * alt_rate
  - credit_full: max(tax_before_credit - alternative_tax, 0)
  - allocated_income: max(officer_comp, officer_comp + business_income)
  - credit: credit_full * reduction_pct
  - net_cit: tax_before_credit - credit
expected:
  tax_before_credit: 7200.00
  adjusted_business_income: 170000.00
  alternative_tax: 3060.00
  credit_full: 4140.00
  allocated_income: 170000.00
  credit: 1656.00
  net_cit: 5544.00
```

**Case 2, a multistate corporation.** A Delaware C corporation with a Michigan sales office has 2026 business income of USD 5,000,000 and no adjustments. Sales everywhere are USD 40,000,000: USD 10,000,000 of hardware shipped to Michigan customers, USD 1,500,000 of software licences used in Michigan, USD 500,000 of consulting for Michigan clients, and the rest elsewhere. It cannot take the SBAC (gross receipts over USD 20,000,000).

Michigan sales: USD 12,000,000. Sales factor: 12 / 40 = 30%. Apportioned base: USD 1,500,000. CIT: USD 90,000. Liability is over USD 800, so it pays estimates of at least USD 22,500 on April 15, July 15 and October 15, 2026 and January 15, 2027, and files Form 4891 by April 30, 2027.

```oa-check
name: Michigan single sales factor, multistate (2026)
inputs:
  business_income: 5000000
  mi_tangible: 10000000
  mi_software: 1500000
  mi_services: 500000
  sales_everywhere: 40000000
steps:
  - mi_sales: mi_tangible + mi_software + mi_services
  - sales_factor: mi_sales / sales_everywhere
  - apportioned_base: business_income * sales_factor
  - cit: apportioned_base * 0.06
  - quarterly_estimate: cit * 0.25
expected:
  mi_sales: 12000000.00
  sales_factor: 0.30
  apportioned_base: 1500000.00
  cit: 90000.00
  quarterly_estimate: 22500.00
```

## When to refuse or refer

| Situation | Action |
|---|---|
| Bank, savings institution, other financial institution, or insurance company | Refuse: separate chapters of Part 2 and separate returns. Refer to a Michigan specialist. |
| The taxpayer holds MBT certificated credits and asks whether to stay on the MBT or move to the CIT | Refuse the trade-off analysis; refer. The MBT (2007 PA 36, MCL 208.1101 to 208.1601) still applies to taxpayers that elect it to use certificated credits. |
| Related-party intangible expense exceptions, or IRC 482 pricing | Refer to a transfer pricing specialist. |
| IRC 382 ownership change limits on losses | Refer. |
| Foreign operating entity or water's-edge membership questions | Refer. |
| Tax years before 2012 (MBT or SBT) | Refuse: different statute. |
| City corporate income tax returns | Out of scope; refer to the city return. |
| Services sourced to several states with no reasonable data | Flag for review before filing. |

## Filing and payment

1. Register for CIT with Treasury (Michigan Treasury Online, mto.treasury.michigan.gov).
2. Pay quarterly estimates if the year's liability will exceed $800 (Form 4913, EFT or MTO).
3. File Form 4891 (with 4893, 4894, 4897 as needed) by the last day of the fourth month after the year end: April 30, 2027 for calendar 2026. Software-prepared returns must be e-filed.
4. If more time is needed, file Form 4 with payment by the due date: an 8-month extension to file, not to pay.
5. To amend, file Form 4892 for that year with an explanation; a refund claim must be filed within four years of the original due date (Form 4890).

## Completion checklist

- [ ] Filing thresholds tested: $350,000 Michigan gross receipts and $100 liability.
- [ ] Every MCL 206.623(2) adjustment considered, including the 2026 organ donation leave add-back.
- [ ] Federal NOL added back; Michigan business loss applied after apportionment, within 10 years.
- [ ] Sales factor built with destination sourcing for goods and use or benefit sourcing for intangibles and services; intercompany sales eliminated.
- [ ] Unitary group membership checked (more than 50%, flow of value, US persons only).
- [ ] SBAC tested with Form 4894 data; reduced credit table and $19,000,000 to $20,000,000 reduction applied.
- [ ] Estimates and safe harbor checked; due dates April 15, July 15, October 15, January 15.
- [ ] Return e-filed by the due date or Form 4 filed with payment.

## Sources

| Source | URL | Read on |
|---|---|---|
| MCL 206.623 (Michigan Legislature). Read for (1) the 6.0% rate and P.L. 86-272, (2)(a) to (i) the adjustments including the 2026 PA 39 add-back, (3) unitary business income, (4) the 10-year business loss. | https://www.legislature.mi.gov/Laws/MCL?objectName=mcl-206-623 | 2026-11-13 |
| MCL 206.685 (Michigan Legislature). Read for (1) the due date, the $350,000 and $100 thresholds, (2) short-year proration, (3) and (4) extensions. | https://legislature.mi.gov/Laws/MCL?objectName=mcl-206-685 | 2026-11-13 |
| MCL 206.611 (Michigan Legislature). Read for (3) tax-exempt person, (4) tax year and mid-year joins, (5) taxpayer, (6) unitary business group. | https://www.legislature.mi.gov/Laws/MCL?objectName=mcl-206-611 | 2026-11-13 |
| MCL 206.661 (Michigan Legislature). Read for (2) allocation or apportionment and (3) subject to tax in another state. | https://www.legislature.mi.gov/Laws/MCL?objectName=mcl-206-661 | 2026-11-13 |
| MCL 206.663 (Michigan Legislature). Read for (1) the sales factor and unitary flow-through entities, (2) unitary group sales and eliminations, (3) sales factor only. | https://www.legislature.mi.gov/Laws/MCL?objectName=mcl-206-663 | 2026-11-13 |
| MCL 206.665 (Michigan Legislature). Read for (1)(a) to (e) sourcing of goods, real property, rentals, transportation property and intangibles; the services subsection read in part only. | https://www.legislature.mi.gov/Laws/MCL?objectName=mcl-206-665 | 2026-11-13 |
| Form 4893, 2025 Small Business Alternative Credit (Treasury). Read for the eligibility limits ($20,000,000, $1,795,300, $180,000), lines 1 to 18 and the reduced credit table. | https://www.michigan.gov/taxes/-/media/Project/Websites/taxes/Forms/CIT/TY2025/4893_ty2025.pdf | 2026-11-13 |
| Instructions for Form 4893, 2025 (Treasury). Read for allocated income, Form 4894, annualizing, loss adjustment and unitary group rules. | https://www.michigan.gov/taxes/-/media/Project/Websites/taxes/Forms/CIT/TY2025/4893_ty2025-instructions.pdf | 2026-11-13 |
| Form 4890, 2025 CIT Forms and Instructions for Standard Taxpayers (Treasury). Read for who files, quarterly estimates, e-file, due dates, extensions and amending. | https://www.michigan.gov/taxes/-/media/Project/Websites/taxes/Forms/CIT/TY2025/4890_ty2025.pdf | 2026-11-13 |

Michigan's Flow-Through Entity Tax (Part 4 of the Income Tax Act, added by 2021 PA 135) lets a partnership or S corporation elect to pay Michigan tax at entity level; MCL 206.623(2)(b) makes a corporate member add back its share of that tax. Its figures are not given here: use `us-pte-state-matrix`.

Not yet confirmed: the 2026 SBAC adjusted business income limit (2026 Form 4893 not yet published; $1,795,300 is the 2025 figure); the full text of MCL 206.665 on services sourcing; MCL 206.691 (combined filing election) and MCL 208.1500 (MBT election), which the Legislature site would not serve; all Flow-Through Entity Tax figures (rate, election date, three-year lock-in, Forms 5772 and 5774, member credit); city corporate income tax rates.

## Today's figures and who stands behind this skill

This file is an AI skill (tax rules your AI follows) from OpenAccountants, copied on 2026-11-13. Rates, thresholds and deadlines change. For the current version of this skill, its official sources and the named accountant (if any) who stands behind it, call `get_skill` with slug `mi-corporate-income-tax` on the OpenAccountants connector (https://www.openaccountants.com/connect), or read https://www.openaccountants.com/skills/mi-corporate-income-tax. If neither is available, confirm every figure against the official source pages cited above before relying on it.
