---
name: new_zealand-references
jurisdiction: NZ
category: orchestrator
tax_year: 2026
tax_year_notes: "Routing catalog for the New Zealand 2027 income year (1 April 2026 to 31 March 2027). Carries no operative rates or deadlines."
last_updated: 2026-11-14
version: "2.0"
type: router
description: >
  New Zealand source-routing catalog for the 2027 income year (1 April 2026 to 31 March 2027). Directs
  individual income tax, provisional tax, GST, ACC levies, residency, capital gains, crypto, vehicle
  and deduction-timing questions to the owning Guides and to the official Inland Revenue, ACC and
  legislation sources. Keeps the two openfisca-aotearoa projects as optional engineering references
  only, separate from the law. Trigger on NZ tax sources, IRD reference, New Zealand legislation
  source, openfisca aotearoa. Contains no duplicated operative tax rates or filing deadlines.
tier: 2
domain: income-tax
---

# New Zealand: primary tax sources and optional engineering references, 2027 income year v2.0

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

**Quick answer.** Use the owning New Zealand Guide and the official source it cites for any figure. This catalog helps find them. A third-party project's encoded parameters, stars or claims do not establish the law. The two open-source projects kept below are for engineering research only.

## Ask the client first

1. Which income year is being researched (IRD names the year by its end: 1 April 2026 to 31 March 2027 is the 2027 income year)?
2. Is the job legal research, a tax calculation, a filing, or building software?
3. Which taxpayer (individual, sole trader, company, trust) and which tax (income tax, GST, ACC, FBT, PAYE)?
4. Is there an actual source provision, a current IRD page, or a project commit to check?
5. If code will be reused, which exact version, files and licence govern the use?

## The method, step by step

1. **Load the owner first.** [nz-income-tax-ir3](nz-income-tax-ir3.md) for the individual return and rates; [nz-provisional-tax](nz-provisional-tax.md) for provisional tax; [nz-gst-return](nz-gst-return.md) for GST; [nz-acc-levies](nz-acc-levies.md) for ACC levies; [nz-tax-residency](nz-tax-residency.md) for residence; [nz-capital-gains](nz-capital-gains.md) for bright-line, share and FIF questions; [new-zealand-crypto-tax](new-zealand-crypto-tax.md) for cryptoassets; [nz-motor-vehicle-expenses-logbook-business-use](nz-motor-vehicle-expenses-logbook-business-use.md) for vehicles and FBT on cars; [nz-timing-deductions-when-expense-incurred](nz-timing-deductions-when-expense-incurred.md) for the year of a deduction. Company tax, PAYE and transfer pricing have no owner yet (see the pack README).
2. **Choose the right original.** Inland Revenue pages and guides (ird.govt.nz), its Tax Technical site for rulings, interpretation statements and determinations (taxtechnical.ird.govt.nz), its Tax Policy site for Bills and Budget measures (taxpolicy.ird.govt.nz), ACC for levy rates (acc.co.nz), and the Income Tax Act 2007, Goods and Services Tax Act 1985 and Tax Administration Act 1994 on legislation.govt.nz. A Tax Policy information sheet describes a proposal: confirm enactment before using its figure.
3. **Keep a research record.** Record the official URL, the section, guide or table, the income year, the exact words and the date read. legislation.govt.nz often refuses scripts; when it does, say so and rest the figure on IRD's page, or leave it unconfirmed.
4. **Bound the answer.** Return the owner and source, the question it answers and what stays open. This catalog is not a calculation, a filing or a licence clearance.

## Optional engineering references retained from the earlier catalog

These are project identities only, not tax-law authorities and not proof that the software implements current law. Licence and activity were read from GitHub on 14 November 2026; open the actual revision and licence before any reuse.

| Repository | What it encodes (per the project) and where to go instead |
|---|---|
| [BetterRules/openfisca-aotearoa](https://github.com/BetterRules/openfisca-aotearoa) | Aotearoa New Zealand legislation as computable rules on the OpenFisca framework: income tax brackets, Working for Families tax credits, Best Start, accommodation supplement, community services card, jobseeker support, sole parent support, student allowance and other social welfare rules. Licence AGPL-3.0; last push March 2025, so its parameters may predate the bracket change behind the 2024-25 composite rate table. For income tax use [nz-income-tax-ir3](nz-income-tax-ir3.md) and IRD's rate page; for welfare rules use the official agency. |
| [digitalaotearoa/openfisca-aotearoa](https://github.com/digitalaotearoa/openfisca-aotearoa) | A continuation of the BetterRules project with more legislation coverage. Licence AGPL-3.0; last push May 2025. Same limits as above. |

The earlier catalog's star and contributor counts, "same-license family, fully compatible" statement and "strong validation source for NZ tax rates" claim are not repeated: a project's parameters are not a source for a figure.

## When to refuse or refer

Refer a figure that rests only on a project file or a proposal not yet enacted; legislation text that could not be opened; and any proposed code reuse without reading the actual licence. Do not use this catalog to answer a rate, threshold or deadline question: load the owner.

## Sources

| Source and what was read | URL | Read on |
| --- | --- | --- |
| IRD, Tax rates for individuals: read for confirming the owner Guides' rate source is current (table "From 1 April 2025") | https://www.ird.govt.nz/income-tax/income-tax-for-individuals/tax-codes-and-tax-rates-for-individuals/tax-rates-for-individuals | 2026-11-14 |
| IRD Tax Technical, Determination E12 page: read for the Tax Technical route for determinations | https://www.taxtechnical.ird.govt.nz/determinations/miscellaneous/det-e12-persons-excused-from-complying-with-section-ea-3-of-the-income-tax-act-2007 | 2026-11-14 |
| IRD Tax Policy, Budget 2026 FIF information sheet: read for a proposal that needs enactment checked | https://www.taxpolicy.ird.govt.nz/-/media/project/ir/tp/publications/2026/is-foreign-investment-fund.pdf | 2026-11-14 |
| legislation.govt.nz, Income Tax Act 2007: read for the Act text; refused script access (HTTP 202 empty, then 403) | https://www.legislation.govt.nz/act/public/2007/0097/latest/DLM1520575.html | 2026-11-14 |
| GitHub API, BetterRules/openfisca-aotearoa: read for licence and last push date | https://github.com/BetterRules/openfisca-aotearoa | 2026-11-14 |
| GitHub API, digitalaotearoa/openfisca-aotearoa: read for licence and last push date | https://github.com/digitalaotearoa/openfisca-aotearoa | 2026-11-14 |

Not yet confirmed: whether either openfisca-aotearoa project encodes the current income tax brackets; legislation.govt.nz text for any section (refused script access). Tax figures and deadlines come from the owning Guides and the primary sources, not from this catalog.
