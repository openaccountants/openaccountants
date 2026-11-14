---
name: ma-corporate-excise
description: "Compute the Massachusetts corporate excise for 2026 under M.G.L. c. 63 for C corporations and S corporations, and the elective pass-through entity excises under chapters 63D and 63E. Covers the 8% income measure, the $2.60 per $1,000 tangible property or net worth measure, the $456 minimum, single sales factor apportionment, tangible and intangible property corporations, the S corporation entity-level rates of 2% and 3% by total receipts, financial institutions and security corporations, the nexus presumption, combined reporting, net operating losses, filing and estimates, and the 5% chapter 63D and new 4% chapter 63E PTE excises with the 90% member credit. Trigger on \"Massachusetts corporate excise\", \"Form 355\", \"Form 355S\", \"Form 355U\", \"MA S corp tax\", \"Massachusetts sting tax\", \"63D\", \"63E\", \"Massachusetts PTE election\", \"Form 63-ELT\". The individual 4% surtax is in ma-income-tax."
license: "AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)"
metadata:
  source: openaccountants
  openaccountants_url: "https://www.openaccountants.com/skills/ma-corporate-excise"
  jurisdiction: "US-MA"
  tax_year: "2026"
  last_updated: "2026-11-13"
---

# Massachusetts corporate excise and pass-through entity excise, tax year 2026

> **Source-cited draft.** Built from the Massachusetts Department of Revenue (DOR) tax rates page, Corporate Excise Tax Guide, S Corporations page and Elective Pass-through Entity Excise page, 830 CMR 63.39.1 (corporate nexus), and M.G.L. c. 63, sections 30 and 38, read on 2026-11-13. No accountant has reviewed it. All outputs must be reviewed by a qualified tax professional before filing.

**Answer first.** A general business corporation pays an excise made of two parts that are added together: **8.0%** of net income apportioned to Massachusetts, plus **$2.60 per $1,000** of taxable Massachusetts tangible property (a tangible property corporation) or of apportioned net worth (an intangible property corporation), with a minimum of **$456**. Income is apportioned by the sales factor alone. An S corporation pays the non-income measure and the minimum, and an income measure only when its total receipts are **$6 million** or more: **2%** below $9 million, **3%** from $9 million, plus 8% on income taxed federally under IRC 1374 and 1375. Partnerships and S corporations may elect to pay a **5%** chapter 63D excise and, for years from 2026, a **4%** chapter 63E excise on members' income above the surtax threshold; members get a credit of **90%** of the excise paid for them.

## Scope

| Field | Value |
| --- | --- |
| Jurisdiction | Massachusetts (US-MA), [DOR](https://www.mass.gov/orgs/massachusetts-department-of-revenue) |
| Law | M.G.L. c. 63 (corporate excise), c. 63D and c. 63E (elective PTE excises), [DOR Corporate Excise Tax Guide](https://www.mass.gov/info-details/corporate-excise-tax-guide) |
| Portal | [MassTaxConnect](https://mtc.dor.state.ma.us/mtc/_/); corporations file and pay electronically |
| Forms | Form 355 (C corporation), 355S (S corporation), 355U (combined group), 63-ELT (PTE excise election), 355-ES (estimates), [DOR guide](https://www.mass.gov/info-details/corporate-excise-tax-guide) |

Covers: C corporations and S corporations doing business in Massachusetts; LLCs classified as corporations; the entity-level PTE excise for partnerships, S corporations and trusts. LLCs disregarded for federal tax flow to the owner (`ma-income-tax`); multi-member LLCs taxed as partnerships are not subject to the corporate excise.

Out of scope (refer): financial institution excise beyond the rate (c. 63, ss. 1 to 2B, Form 63 FI); insurance company excises; public utilities; deeds excise; sales and use tax (`ma-sales-tax`); estate tax; local property tax; the individual 4% surtax (`ma-income-tax`). Federal corporate tax is in `us-form-1120-c-corp`.

## Ask the client first

1. Entity type and federal classification: C corporation, S corporation, partnership, disregarded LLC.
2. What it does in Massachusetts: employees, property, customers, receipts from Massachusetts sources (nexus).
3. Sales everywhere and sales sourced to Massachusetts for 2026.
4. For an S corporation: total receipts for the year (the $6 million and $9 million tests).
5. Tangible property in Massachusetts not subject to local tax, total assets and book net worth at year end (tangible or intangible property corporation).
6. For a pass-through: whether members are subject to Massachusetts personal income tax and whether any member's income will exceed the surtax threshold (63D and 63E elections).

## The method, step by step

### Rates, bands and thresholds

| Item | 2026 figure | Condition | Source |
| --- | --- | --- | --- |
| Income measure, business and manufacturing corporations | 8.0% of net income | Apportioned Massachusetts net income | [DOR tax rates](https://www.mass.gov/info-details/massachusetts-tax-rates) |
| Non-income measure | $2.60 per $1,000 | Taxable Massachusetts tangible property, or net worth | [DOR tax rates](https://www.mass.gov/info-details/massachusetts-tax-rates) |
| Minimum excise | $456 | Every corporation subject to the excise | [DOR tax rates](https://www.mass.gov/info-details/massachusetts-tax-rates) |
| S corporation income measure, receipts $6 million to under $9 million | 2% of net income | Not a financial institution | [DOR S corporations](https://www.mass.gov/info-details/s-corporations) |
| S corporation income measure, receipts $9 million or more | 3% of net income | Not a financial institution | [DOR S corporations](https://www.mass.gov/info-details/s-corporations) |
| S corporation built-in gains and passive investment income | 8% | Income taxed federally under IRC 1374 or 1375 | [DOR S corporations](https://www.mass.gov/info-details/s-corporations) |
| S corporation financial institution | 2.67% ($6 million to under $9 million); 4% ($9 million or more); 9% on federally taxed income | Financial institution S corporations | [DOR S corporations](https://www.mass.gov/info-details/s-corporations) |
| Financial institutions | 9% of net income, minimum $456 | Financial institution excise | [DOR tax rates](https://www.mass.gov/info-details/massachusetts-tax-rates) |
| Security corporations | 1.32% of gross income (non-bank holding company); 0.33% (bank holding company); minimum $456 | Classified security corporations | [DOR tax rates](https://www.mass.gov/info-details/massachusetts-tax-rates) |
| Tangible property corporation test | Massachusetts tangible property not locally taxed is 10% or more of the defined total assets | Book values, last day of the year | [M.G.L. c. 63, s. 30](https://malegislature.gov/Laws/GeneralLaws/PartI/TitleIX/Chapter63/Section30) |
| Nexus presumption | Activity with 100 or more residents, $10,000,000 or more of Massachusetts assets, or more than $500,000 of Massachusetts receipts | Regular in-state activity, 830 CMR 63.39.1 | [830 CMR 63.39.1](https://www.mass.gov/regulations/830-CMR-63391-corporate-nexus) |
| Net operating loss carryforward | Not more than 20 years; no carryback | Losses from years beginning on or after 1 January 2010 | [M.G.L. c. 63, s. 30](https://malegislature.gov/Laws/GeneralLaws/PartI/TitleIX/Chapter63/Section30) |
| Estimated payments | Required if the excise is reasonably estimated above $1,000 | All corporations | [DOR Corporate Excise Tax Guide](https://www.mass.gov/info-details/corporate-excise-tax-guide) |
| Chapter 63D PTE excise | 5% of income attributable to qualified members and taxed under chapter 62 | Electing partnership, S corporation or trust | [DOR elective PTE excise](https://www.mass.gov/info-details/elective-pass-through-entity-excise) |
| Chapter 63E PTE excise | 4% of each qualified member's distributive income above the surtax threshold | Electing entity, taxable years beginning on or after 1 January 2026 | [DOR elective PTE excise](https://www.mass.gov/info-details/elective-pass-through-entity-excise) |
| PTE member credit | 90% of the member's share of the 63D or 63E excise actually paid | Qualified member | [DOR elective PTE excise](https://www.mass.gov/info-details/elective-pass-through-entity-excise) |
| Surtax threshold used for 63E | $1,107,750 (tax year 2026) | Owned by `ma-income-tax` | [DOR tax rates](https://www.mass.gov/info-details/massachusetts-tax-rates) |

### Step 1. Nexus and classification

A corporation that owns or uses property, has employees or otherwise does business in Massachusetts has nexus. Regular in-state activity is presumed to create nexus where it is conducted with 100 or more residents, or the corporation has $10,000,000 or more of Massachusetts assets, or more than $500,000 of Massachusetts receipts; the corporation may seek to rebut the presumption. Internet activity beyond the solicitation of orders for tangible goods (for example cookies that gather customer data to adjust production or develop products) is not protected by Public Law 86-272 under the regulation. Then classify: general business, manufacturing, S corporation, security corporation, financial institution.

### Step 2. Income measure

Start from federal gross income less most federal deductions (M.G.L. c. 63, s. 30.4); federal credits do not apply. Massachusetts disallows deductions for dividends received (it allows its own deduction under s. 38(a)(1)), for losses of other years except its own net operating loss under s. 30.5, and for taxes on or measured by income. Apply the Schedule E modifications in the Form 355 instructions.

### Step 3. Apportion

If the corporation has income taxable both inside and outside Massachusetts, multiply taxable net income by the sales factor: Massachusetts sales over sales everywhere (M.G.L. c. 63, s. 38(c) and (d)). "Sales" means gross receipts, excluding interest, dividends and receipts from securities. Services and intangibles are sourced to the market under 830 CMR 63.38.1. Airlines, motor carriers, courier services, mutual fund service corporations, pipelines, electric and telecommunications companies have their own apportionment regulations.

### Step 4. Net operating loss

Deduct the Massachusetts net operating loss computed under s. 30.5, after Massachusetts modifications. Losses from years beginning on or after 1 January 2010 carry forward up to 20 years and never back.

### Step 5. Non-income measure

A tangible property corporation pays $2.60 per $1,000 on Massachusetts tangible property not subject to local tax (book value). An intangible property corporation (below the 10% test) pays $2.60 per $1,000 on its net worth apportioned to Massachusetts.

### Step 6. Total excise

Income measure plus non-income measure; if the total is below $456, pay $456. The two measures are added, not compared. Subtract Massachusetts credits (determined under Massachusetts law).

### Step 7. S corporations

Test total receipts: below $6 million, no income measure on ordinary income; $6 million to under $9 million, 2%; $9 million or more, 3%. Add 8% on income taxed federally under IRC 1374 or 1375. The non-income measure and the $456 minimum apply whatever the receipts. File Form 355S with Schedule S and SK-1s; an S corporation in a combined group also files 355S as an information return.

### Step 8. Pass-through entity excise elections

An eligible pass-through entity (partnership, S corporation, LLC treated as either, or a trust for income taxed to beneficiaries) may elect each year:
- **Chapter 63D:** 5% of the entity's income attributable to qualified members and taxed under chapter 62.
- **Chapter 63E (taxable years beginning on or after 1 January 2026):** 4% of each qualified member's distributive income taxed under chapter 62 above the surtax threshold.
- Either or both. Qualified members (individuals, estates and trusts subject to Massachusetts personal income tax, resident or not) claim a credit of 90% of their share of the excise actually paid, on their return for the year in which the entity's year ends.

The entity makes the elections on its timely Form 3, 355S (Schedule S, line 23) or Form 2, confirmed by Form 63-ELT filed electronically by the return due date with extensions. Elections cannot be made on an amended return and are irrevocable; members cannot opt out. Payments are electronic and separate from any corporate excise payment. Both excises end if the federal SALT deduction limit expires or is repealed.

## Boundary and exception table

| Situation | Treatment | Source |
| --- | --- | --- |
| Corporation with zero income and no Massachusetts property | Still pays the $456 minimum | [DOR tax rates](https://www.mass.gov/info-details/massachusetts-tax-rates) |
| Sales factor numerator is zero | The factor is not inapplicable for that reason alone | [M.G.L. c. 63, s. 38](https://malegislature.gov/Laws/GeneralLaws/PartI/TitleIX/Chapter63/Section38) |
| Sole proprietor or disregarded single-member LLC | Cannot elect either PTE excise | [DOR elective PTE excise](https://www.mass.gov/info-details/elective-pass-through-entity-excise) |
| Grantor trust | Not an eligible PTE; the grantor may be a qualified member | [DOR elective PTE excise](https://www.mass.gov/info-details/elective-pass-through-entity-excise) |
| Out-of-state PTE with Massachusetts income | May elect on a timely Form 3, 355S or 2 plus Form 63-ELT | [DOR elective PTE excise](https://www.mass.gov/info-details/elective-pass-through-entity-excise) |
| Nonresident member, entity pays 63D only, member on a composite return and not subject to surtax | No own return needed | [DOR elective PTE excise](https://www.mass.gov/info-details/elective-pass-through-entity-excise) |
| Nonresident member where entity pays 63E | Must file Form 1-NR/PY; the 63E credit cannot be claimed on a composite return | [DOR elective PTE excise](https://www.mass.gov/info-details/elective-pass-through-entity-excise) |
| S corporation in a combined group (Form 355U) | Makes its own PTE elections on 355S; pays separately from the group's excise | [DOR elective PTE excise](https://www.mass.gov/info-details/elective-pass-through-entity-excise) |
| Fiscal-year PTE ending March 2027 | Calendar-year member claims the credit on the 2027 return | [DOR elective PTE excise](https://www.mass.gov/info-details/elective-pass-through-entity-excise) |

### Combined reporting

Corporations engaged in a unitary business under common ownership file one combined report on Form 355U through a principal reporting corporation (M.G.L. c. 63, s. 32B; 830 CMR 63.32B.2). Combined income is apportioned with the group's sales; each taxable member computes its excise on its share; non-taxable members are listed. The default is water's-edge, with elections for worldwide or affiliated-group reporting. The ownership percentage, the 80/20 rules and the election terms were not on the pages read and are left to a reviewer.

### Defaults when a fact is missing

| Missing fact | Default |
| --- | --- |
| Whether tangible property passes the 10% test | Compute both measures and flag; do not pick the lower |
| S corporation receipts near $6 million or $9 million | Use the full-year total receipts, not net income |
| Member residency for a PTE | Ask; nonresidents filing rules differ |

### Red flags to raise with the client

| Flag | Why it matters |
| --- | --- |
| S corporation receipts crossing $9 million | Rate moves from 2% to 3% on all net income |
| Owner income above the surtax threshold | Consider the 63E election for 2026 |
| Election missed on the original return | Cannot be made on an amended return |
| Remote seller of services with large Massachusetts receipts | Nexus presumption above $500,000 |

## Worked cases

**Case 1, a C corporation with a tangible property measure.** A Boston software company has 2026 Massachusetts net income before apportionment of USD 922,000 (federal taxable income USD 850,000 plus USD 42,000 of state income tax and USD 30,000 of other Massachusetts add-backs). Sales are USD 4,000,000 everywhere and USD 3,200,000 sourced to Massachusetts (80%). Apportioned income is USD 737,600, so the income measure is USD 59,008. It is a tangible property corporation with USD 180,000 of Massachusetts equipment not locally taxed: the non-income measure is USD 468. The excise is USD 59,476, above the USD 456 minimum.

```oa-check
name: C corporation excise with single sales factor (2026)
inputs:
  ma_net_income_before_apportionment: 922000
  ma_sales: 3200000
  sales_everywhere: 4000000
  tangible_property: 180000
  minimum: 456
steps:
  - sales_factor: ma_sales / sales_everywhere
  - apportioned_income: ma_net_income_before_apportionment * sales_factor
  - income_measure: apportioned_income * 0.08
  - property_measure: tangible_property / 1000 * 2.60
  - excise: max(income_measure + property_measure, minimum)
expected:
  sales_factor: 0.80
  apportioned_income: 737600.00
  income_measure: 59008.00
  property_measure: 468.00
  excise: 59476.00
```

**Case 2, decision: an S corporation over USD 9 million, and whether to elect 63D and 63E.** A Cambridge consulting S corporation has total receipts of USD 10,200,000 and Massachusetts income of USD 1,840,000, 95% apportioned (USD 1,748,000). It is an intangible property corporation with net worth of USD 2,200,000. Its excise: 3% income measure USD 52,440 plus net worth measure USD 5,434 (USD 2,200,000 times 95% times 2.60 per 1,000). Two equal resident shareholders each have USD 874,000 of Massachusetts share plus USD 250,000 of wages, so USD 1,124,000 each, USD 16,250 above the 2026 threshold. Electing 63D: 5% of USD 1,748,000 = USD 87,400 paid by the entity, a credit of USD 39,330 for each shareholder (90% of half). Electing 63E as well: 4% of USD 16,250 for each = USD 1,300 in total, a credit of USD 585 each. The decision turns on the federal deduction of the excise at entity level against the 10% of each excise that is not credited.

```oa-check
name: S corporation 3 percent excise and PTE elections (2026)
inputs:
  ma_income: 1840000
  apportionment: 0.95
  net_worth: 2200000
  receipts: 10200000
  shareholders: 2
  wages_each: 250000
  threshold: 1107750
steps:
  - apportioned_income: ma_income * apportionment
  - s_corp_income_measure: apportioned_income * 0.03
  - net_worth_measure: net_worth * apportionment / 1000 * 2.60
  - member_taxable: apportioned_income / shareholders + wages_each
  - member_excess: max(member_taxable - threshold, 0)
  - excise_63d: apportioned_income * 0.05
  - credit_63d_each: excise_63d / shareholders * 0.90
  - excise_63e_total: member_excess * shareholders * 0.04
  - credit_63e_each: member_excess * 0.04 * 0.90
expected:
  apportioned_income: 1748000.00
  s_corp_income_measure: 52440.00
  net_worth_measure: 5434.00
  member_taxable: 1124000.00
  member_excess: 16250.00
  excise_63d: 87400.00
  credit_63d_each: 39330.00
  excise_63e_total: 1300.00
  credit_63e_each: 585.00
```

## When to refuse or refer

| Code | Situation | Action |
| --- | --- | --- |
| REF-MACT-01 | Financial institution or insurance company | Refer: Form 63 FI or insurance excise |
| REF-MACT-02 | Combined group with foreign affiliates, worldwide or affiliated-group election | Refer |
| REF-MACT-03 | Manufacturing or R&D classification, investment tax credit | Flag for reviewer |
| REF-MACT-04 | Rebutting the nexus presumption | Refer |
| REF-MACT-05 | Special industry apportionment (airline, carrier, mutual fund service, pipeline, telecom) | Refer |
| REF-MACT-06 | PTE with nonresident, tiered or corporate members | Flag for reviewer |

## Filing and payment

| Return | Due | Source |
| --- | --- | --- |
| Form 355 (C corporation, including security corporations) | 15th day of the 4th month after year end (April 15 for calendar years) | [DOR Corporate Excise Tax Guide](https://www.mass.gov/info-details/corporate-excise-tax-guide) |
| Form 355S (S corporation) | 15th day of the 3rd month after year end (March 15 for calendar years) | [DOR Corporate Excise Tax Guide](https://www.mass.gov/info-details/corporate-excise-tax-guide) |
| Form 3 (partnership) and Form 63-ELT with it | March 15 for calendar years | [DOR elective PTE excise](https://www.mass.gov/info-details/elective-pass-through-entity-excise) |
| Form 2 (fiduciary) and Form 63-ELT with it | April 15 for calendar years | [DOR elective PTE excise](https://www.mass.gov/info-details/elective-pass-through-entity-excise) |

Corporations file and pay electronically. Extensions are available (see DOR Tax Due Dates and Extensions). Estimates are required where the excise is expected to exceed $1,000.

## Completion checklist

- [ ] Nexus tested, including the $500,000, 100-resident and $10,000,000 presumptions.
- [ ] Net income built under s. 30.4 with Massachusetts disallowances.
- [ ] Single sales factor applied; market sourcing for services.
- [ ] Massachusetts NOL within 20 years.
- [ ] Tangible or intangible property corporation decided at the 10% test; $2.60 per $1,000 applied.
- [ ] Measures added; $456 minimum.
- [ ] S corporation receipts tested at $6 million and $9 million.
- [ ] 63D and 63E elections considered and made on the original return with 63-ELT.

## Sources

| Source | URL | Read on |
| --- | --- | --- |
| DOR, Tax Rates (updated 30 Dec 2025). Read for 8.0%, $2.60 per $1,000, $456, S corporation 2% and 3%, financial institution 9%, security corporation 1.32% and 0.33%. | https://www.mass.gov/info-details/massachusetts-tax-rates | 2026-11-13 |
| DOR, S Corporations. Read for the receipts thresholds, 8% on IRC 1374 and 1375 income, financial institution S corporation rates and the 355S information return. | https://www.mass.gov/info-details/s-corporations | 2026-11-13 |
| DOR, Corporate Excise Tax Guide (updated 30 Dec 2025). Read for nexus, electronic filing, due dates, the $1,000 estimate test, the income and non-income measures and industry apportionment. | https://www.mass.gov/info-details/corporate-excise-tax-guide | 2026-11-13 |
| DOR, Elective Pass-through Entity Excise (updated 31 Jul 2026). Read for 63D 5%, 63E 4% from 2026, the 90% credit, eligibility, Form 63-ELT, irrevocability, composite returns and expiry. | https://www.mass.gov/info-details/elective-pass-through-entity-excise | 2026-11-13 |
| 830 CMR 63.39.1, Corporate Nexus. Read for the 100-resident, $10,000,000 asset and $500,000 receipts presumption and the Internet activity example. | https://www.mass.gov/regulations/830-CMR-63391-corporate-nexus | 2026-11-13 |
| M.G.L. c. 63, s. 30. Read for paragraphs 10 and 11 (10% test), 30.4 disallowances and 30.5 (20-year carryforward, no carryback). | https://malegislature.gov/Laws/GeneralLaws/PartI/TitleIX/Chapter63/Section30 | 2026-11-13 |
| M.G.L. c. 63, s. 38. Read for (c) apportionment by the sales factor and (d) its definition. | https://malegislature.gov/Laws/GeneralLaws/PartI/TitleIX/Chapter63/Section38 | 2026-11-13 |

Not yet confirmed: the 2026 Form 355 and 355-ES (the 2026 Form 355-ES page returned not found), so the corporate estimate installment percentages are not stated; the combined reporting ownership and election terms; corporate penalty rates; the Massachusetts conformity position on federal bonus depreciation and section 179 for 2026.

## Today's figures and who stands behind this skill

This file is an AI skill (tax rules your AI follows) from OpenAccountants, copied on 2026-11-13. Rates, thresholds and deadlines change. For the current version of this skill, its official sources and the named accountant (if any) who stands behind it, call `get_skill` with slug `ma-corporate-excise` on the OpenAccountants connector (https://www.openaccountants.com/connect), or read https://www.openaccountants.com/skills/ma-corporate-excise. If neither is available, confirm every figure against the official source pages cited above before relying on it.
