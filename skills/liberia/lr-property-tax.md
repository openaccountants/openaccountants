---
name: lr-property-tax
description: "Builds a Liberia annual real-property-tax assessment workpaper for the 2026 intake year using the published Revenue Code property chapter and the April 2026 security amendment. Use for owner-occupied versus let property, assessed value, a new building, annual payment, a land acquisition schedule, tax arrears or a proposed conveyance. It separates property value taxation from rental income tax and withholding, records the use and exemption conditions, and calculates conditional improved-property examples. Malformed unimproved farmland wording, a public-land exemption cross-reference, current valuation practice, later amendment completeness and live filing fields remain explicit holds. This draft does not establish title, approve a tax filing or certify comprehensive country coverage."
jurisdiction: LR
category: international
job: annual-real-property-tax
tax_year: 2026
tax_year_notes: "2026 intake workpaper; cited 2020 Chapter20 and April2026 security amendment, not a complete current-law consolidation."
tier: 2
last_updated: 2026-11-01
version: 0.1
---

# Liberia Annual Real Property Tax v0.1

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

Tax year: 2026 intake. Read on: 2026-11-01. This is a conditional source-cited draft independently reviewed for source fidelity on 2026-11-01. Establish the applicable amendment chain, assessment and taxpayer facts before using the computations for payment. The year label is not proof that the 2020 property chapter remains unchanged throughout 2026.

## Who this applies to

Owners, acquirers and advisers checking Liberia's annual tax on a nonexempt parcel. The published chapter distinguishes unimproved and under-improved land from improved land; geography controls the former, assessed value and use the latter. [s2000(a)](https://www.lra.gov.lr/wp-content/uploads/2021/08/REVENUE-CODE-LIBERIA-REVENUE-CODE-AMENDEMENT-2020-min.pdf) [P01]

This job concerns annual property tax, valuation and arrears clearance. Rental profit, disposal gains and income withholding remain owned by [Individual income](lr-income-tax.md), [Corporate income](lr-corporate-income-tax.md) and [Cross-border](lr-cross-border.md). Do not treat an annual property-tax receipt as proof those income obligations are settled. The distinction follows the separate property levy in s2000(a). [P01]

## Rates, bands and thresholds

These are figures in the cited text, conditional on that text governing the parcel and period. Apply exemptions and definitions before selecting a row; do not substitute rental receipts or purchase price for assessed value.

| Parcel/use in cited text | Rate/base and conditions | Official source |
|---|---|---|
| Improved business/commercial | 1.5% assessed value; use in whole or part; definition includes letting houses/apartments | [s2000(c)(1),(d)(2)](https://www.lra.gov.lr/wp-content/uploads/2021/08/REVENUE-CODE-LIBERIA-REVENUE-CODE-AMENDEMENT-2020-min.pdf) [P02] |
| Improved industrial | 1.5% assessed value; industrial use in whole or part | [s2000(c)(2)](https://www.lra.gov.lr/wp-content/uploads/2021/08/REVENUE-CODE-LIBERIA-REVENUE-CODE-AMENDEMENT-2020-min.pdf) [P03] |
| Qualifying residential | 0.25% assessed value; exclusive residential use, applying natural-person owner/whole primary-residence occupation/no private-profit letting definition | [s2000(c)(3),(d)(11),(e)](https://www.lra.gov.lr/wp-content/uploads/2021/08/REVENUE-CODE-LIBERIA-REVENUE-CODE-AMENDEMENT-2020-min.pdf) [P04] [P05] |
| Exclusively farm-use improvements | Urban specified limits: one-third of 1% assessed value; outside those limits: 0.25%. Farmland must satisfy definition, including at least five acres | [s2000(c)(4)–(5),(d)(4)](https://www.lra.gov.lr/wp-content/uploads/2021/08/REVENUE-CODE-LIBERIA-REVENUE-CODE-AMENDEMENT-2020-min.pdf) [P06] [P33] |
| Private-controlled improvements on government public land | c(6) states residential one-seventh of 1%, commercial 1%, on improvements only; **hold** conflicting exemption cross-reference before an actual assessment | [s2000(c)(6);s2009(a)](https://www.lra.gov.lr/wp-content/uploads/2021/08/REVENUE-CODE-LIBERIA-REVENUE-CODE-AMENDEMENT-2020-min.pdf) [P07] [P25] |
| Unimproved city/town lot within specified corporate limits | 3.5% assessed value; separately owned fraction of an official lot counts as a whole lot | [s2000(b)(1)(A),(d)(3)](https://www.lra.gov.lr/wp-content/uploads/2021/08/REVENUE-CODE-LIBERIA-REVENUE-CODE-AMENDEMENT-2020-min.pdf) [P08] |

**Unimproved farmland/other acreage hold:** s2000(b)(1)(B) prints percentage-per-acre language without a sufficiently clear valuation base for the urban farmland and other-use rows; its nesting also places the outside-corporate-limits farmland dollar rule within the same paragraph. The text includes a per-acre amount and parcel minimum, but no executable formula is supplied here until the authoritative wording, applicable currency/inflation adjustments and geographical scope are reconciled. Never silently convert these to assessed-value percentages. Source: s2000(b), physical page240. This limitation is source interpretation, not a verified absence of tax.

## The base

1. Establish lot boundaries, title, geography, physical improvements and actual use. Under-improved means additions/buildings/works worth less than the land; it belongs to unimproved land. A structure alone does not prove the improved-property table applies. [s2000(d)(12)–(13)](https://www.lra.gov.lr/wp-content/uploads/2021/08/REVENUE-CODE-LIBERIA-REVENUE-CODE-AMENDEMENT-2020-min.pdf) [P09]
2. Obtain the actual assessment record and inspection/notice dates. Assessed value is taxable value under s2001; market value is the bona fide-sale capital sum at assessment. Exclude the specified removable machinery/tools from commercial/industrial valuation; it is not automatically every balance-sheet asset. [s2000(d)(1),(2),(8),(9)](https://www.lra.gov.lr/wp-content/uploads/2021/08/REVENUE-CODE-LIBERIA-REVENUE-CODE-AMENDEMENT-2020-min.pdf) [P10] [P11]
3. Ordinary inspected market-value assessment is carried for five years. Determination **and notice** on/before June15 makes it operative January1 that year; after June15, January1 next year. Newly completed usable structures follow the separate rule below. Prior market-value and construction-cost transitional assessments have their own rules; obtain the actual assessment rather than inventing a historic cost conversion. [s2001(a)–(d)](https://www.lra.gov.lr/wp-content/uploads/2021/08/REVENUE-CODE-LIBERIA-REVENUE-CODE-AMENDEMENT-2020-min.pdf) [P12] [P13]
4. A newly completed or already usable improvement needs inspection-based market value. If value becomes operative on/after February1, charge one-twelfth of annual tax per remaining month or fraction, then carry value five years from next January1. If operative by January31, charge the whole annual tax and start the five-year term that January1. Completion date alone is not a substitute for establishing the operative assessment date. [s2001(f)](https://www.lra.gov.lr/wp-content/uploads/2021/08/REVENUE-CODE-LIBERIA-REVENUE-CODE-AMENDEMENT-2020-min.pdf) [P15]
5. Reassess before a five-year term ends. Without reassessment the previous value continues; after expiry the taxpayer can request valuation review by June15 under the referenced appeal route. For previously unassessed land, s2001(e) separately addresses five years' unpaid prior tax under the law then in force. No invented current-rate backfill or completed appeal procedure is provided. [s2001(e),(g)](https://www.lra.gov.lr/wp-content/uploads/2021/08/REVENUE-CODE-LIBERIA-REVENUE-CODE-AMENDEMENT-2020-min.pdf) [P14] [P16]

Exemptions require their actual conditions:

- Specified church/mission/educational/charitable/fraternal property: qualifying nonprofit use; letting ordinarily makes the owner liable unless another exempt organisation rents and the rent exclusively serves stated purposes. Separate exemptions exist for exclusive religious/charitable/educational use and University of Liberia property. [s2009(b)–(d)](https://www.lra.gov.lr/wp-content/uploads/2021/08/REVENUE-CODE-LIBERIA-REVENUE-CODE-AMENDEMENT-2020-min.pdf) [P26] [P27]
- Statute/treaty/agreement relief requires property held and used under its conditions. A government lease already exempt by agreement on Code enactment keeps that relief only for the remaining lease period, including renewal options. [s2009(f)–(g)](https://www.lra.gov.lr/wp-content/uploads/2021/08/REVENUE-CODE-LIBERIA-REVENUE-CODE-AMENDEMENT-2020-min.pdf) [P29]
- Renewable-resource contract project property, qualifying mining/petroleum project property within the specified area, and a parcel improved only by qualifying huts have express categories. Farmland and hut definitions must be met; do not treat any farm, shed or mining-investor residence as exempt. [s2009(h)–(j);s2000(d)(4)–(5)](https://www.lra.gov.lr/wp-content/uploads/2021/08/REVENUE-CODE-LIBERIA-REVENUE-CODE-AMENDEMENT-2020-min.pdf) [P30] [P33]
- Public property has the s2009(a) exemption/cross-reference problem described above; private-controlled improvements are not cleared from tax by a blanket government-ownership assertion. [s2009(a);s2000(c)(6)](https://www.lra.gov.lr/wp-content/uploads/2021/08/REVENUE-CODE-LIBERIA-REVENUE-CODE-AMENDEMENT-2020-min.pdf) [P07] [P25]

## Deadlines and filing

The chapter covers January1–December31, due July1; payment can be made from January1 before due date. Acquisition creates a **separate thirty-day** schedule obligation at the LRA office nearest the property: description, location, area, lot/designation, use and actual consideration. [ss2002,2004](https://www.lra.gov.lr/wp-content/uploads/2021/08/REVENUE-CODE-LIBERIA-REVENUE-CODE-AMENDEMENT-2020-min.pdf) [P17] [P20]

Prepare the workpaper in this order: identify parcel/title and use; inspect the public assessment record at the relevant LRA office; obtain inspection, valuation and notice evidence; test exemptions; calculate conditional annual/prorated liability; reconcile arrears; obtain the authority's current form and payment reference; preserve accepted schedule and official payment receipt. Public records contain location, area, lot/use, inspection date, value and annual levy. Written notice is required; where impracticable the chapter allows at least two newspaper notices, deemed received ten days after the last publication. [ss2003,2006](https://www.lra.gov.lr/wp-content/uploads/2021/08/REVENUE-CODE-LIBERIA-REVENUE-CODE-AMENDEMENT-2020-min.pdf) [P19] [P22]

Registrars' first-of-month reports of the preceding month's ownership transfers and Public Lands directors' reports of grants are official duties, not a replacement for the buyer's acquisition schedule. [s2005](https://www.lra.gov.lr/wp-content/uploads/2021/08/REVENUE-CODE-LIBERIA-REVENUE-CODE-AMENDEMENT-2020-min.pdf) [P21]

For conveyance, obtain the official receipt proving all property arrears paid. Except public-land sales, it is a prerequisite to probate/registration of the deed, lease or other interest instrument; officials withhold action, and title/interest is not deemed vested until arrears are paid. This does not verify the rest of a title search or land-law requirements. [s2010](https://www.lra.gov.lr/wp-content/uploads/2021/08/REVENUE-CODE-LIBERIA-REVENUE-CODE-AMENDEMENT-2020-min.pdf) [P31]

**Operational hold:** the current property schedule form, field/box numbers, assessment appeal mechanics, portal/payment reference and successful submission were not read or tested. No complete electronic filing workflow is claimed. Stop before submission until the applicable form and instructions are obtained.

## Penalties and interest

Unpaid after July1 bears s11 market interest; no fixed current interest percentage is supplied. If unpaid by July31, s2002 adds 5% per month or part-month after July31, capped at 25% in aggregate. Obtain the actual assessment and partial-payment history before settlement. Do not substitute the separate income-return penalty examples in [Tax overview](lr-tax-overview.md#penalties-and-interest) for this property's specific rule. [s2002](https://www.lra.gov.lr/wp-content/uploads/2021/08/REVENUE-CODE-LIBERIA-REVENUE-CODE-AMENDEMENT-2020-min.pdf) [P17] [P18]

Tax becomes a preferred lien on the property when due, and assessed interest/penalties/charges also attach until paid. Justice can pursue competent-court collection and Tax Court foreclosure: proved delinquency, ordered execution, notice and public auction. Proceeds go to tax/penalty/interest, court costs, other liens by priority and then owner; the owner can bid. Obtain legal representation on an actual foreclosure. [ss2007–2008](https://www.lra.gov.lr/wp-content/uploads/2021/08/REVENUE-CODE-LIBERIA-REVENUE-CODE-AMENDEMENT-2020-min.pdf) [P23] [P24]

The amendment printed1April2026 separately permits a written Land Registry security notice for land/building in which the taxpayer has an interest, securing unpaid tax, with notice to the taxpayer within seven days. This is distinct from the annual property's due-date lien and does not by itself prove a completed foreclosure. [amended63(1)(a)](https://www.lra.gov.lr/wp-content/uploads/2026/04/LRC-Amendment-December-2025.pdf) [P32]

## Cross-border points

Do not assume diplomatic tenancy makes private property exempt. s2009(e) distinguishes foreign-government property on Republic-leased/deeded land from private property let to a foreign government: the latter remains taxable to the owner and has a withholding obligation. Use [Cross-border](lr-cross-border.md) for the income-withholding computation; this Guide does not duplicate its rates. [s2009(e)](https://www.lra.gov.lr/wp-content/uploads/2021/08/REVENUE-CODE-LIBERIA-REVENUE-CODE-AMENDEMENT-2020-min.pdf) [P28]

A particular treaty/agreement exemption needs the actual instrument and compliance with its property-use conditions. Foreign ownership, title entitlement and land-law restrictions are separate unresolved legal jobs; this annual-tax workpaper does not establish the ability to acquire title. [s2009(f)](https://www.lra.gov.lr/wp-content/uploads/2021/08/REVENUE-CODE-LIBERIA-REVENUE-CODE-AMENDEMENT-2020-min.pdf) [P29]

## Two worked examples that recompute

Both cases assume the cited property provisions govern, a valid nonexempt improved parcel, no under-improved classification, a lawfully established LRD8,000,000 assessed value, and no public-land exception. Assumed values are not an official valuation or full current-law clearance.

### New commercial building: operative value during September

Assume the newly usable building's assessed value becomes operative September15. Its annual business-use charge is LRD120,000. September's fraction plus October–December gives four months: 120,000 ×4/12 = LRD40,000 for the remainder of that year. Using only three whole months would omit the fractional month. The hypothetical date is an operative assessment assumption, not a declaration that every completion immediately starts tax. [s2000(c)(1);s2001(f)](https://www.lra.gov.lr/wp-content/uploads/2021/08/REVENUE-CODE-LIBERIA-REVENUE-CODE-AMENDEMENT-2020-min.pdf) [P02] [P15]

```oa-check
name: Newly completed commercial property includes a fractional month
inputs:
  assessed_value: 8000000
  months_including_fraction: 4
steps:
  - annual: assessed_value * 0.015
  - apportioned: annual * months_including_fraction / 12
  - whole_months_only: annual * 3 / 12
  - omitted_fraction: apportioned - whole_months_only
expected:
  annual: 120000
  apportioned: 40000
  whole_months_only: 30000
  omitted_fraction: 10000
```

### Classification decision: owner residence or rental

Assume the same established assessed value for a whole year and compare two distinct facts: a natural person's wholly occupied primary home with no letting, versus the house wholly let for private profit. The first meets the residential definition and gives LRD20,000; letting falls within business/commercial use and gives LRD120,000. The LRD100,000 difference is annual property tax only, not tax on rental income or an investment recommendation. If any part is let or ownership/use differs, the residential definition must be reconsidered before choosing the lower result. [s2000(c)(1),(3),(d)(2),(11)](https://www.lra.gov.lr/wp-content/uploads/2021/08/REVENUE-CODE-LIBERIA-REVENUE-CODE-AMENDEMENT-2020-min.pdf) [P02] [P04] [P05]

```oa-check
name: Owner residence versus business letting changes property classification
inputs:
  assessed_value: 8000000
steps:
  - qualified_home: assessed_value * 0.0025
  - business_letting: assessed_value * 0.015
  - difference: business_letting - qualified_home
expected:
  qualified_home: 20000
  business_letting: 120000
  difference: 100000
```

## Ask the client first

- Exact parcel, title/lease, owner legal form, public/private land and proposed transfer documents.
- Official boundaries, urban limits, acreage, land/improvement values, use and any letting.
- Assessment record, inspection/determination/notice/operative dates and completion or first usability.
- Claimed exemption instrument, project area and evidence of the actual qualifying use.
- Prior tax receipts, arrears/partial payments, notices, security directions and litigation.
- Governing year/amendments and the current authority form, valuation and payment instructions.

## Sources

| Source and actual scope read | Official URL | Read on |
|---|---|---|
| Revenue Code as Amended2020: full Chapter20 ss2000–2010, all definitions/exemptions and neighbouring headings, physical/printed240–245 | https://www.lra.gov.lr/wp-content/uploads/2021/08/REVENUE-CODE-LIBERIA-REVENUE-CODE-AMENDEMENT-2020-min.pdf | 2026-11-01; read in part, specific scope in first column |
| December2025 amendment, approved24March/printed1April2026: cover, preliminary/provision list, full amended63 and neighbours, final commencement; physical6 visually inspected. No fresh property-rate consolidation is asserted | https://www.lra.gov.lr/wp-content/uploads/2026/04/LRC-Amendment-December-2025.pdf | 2026-11-01; read in part, specific scope in first column |

The cached 2024 Chapter8/10, VAT1003/1066 and general2024 amendment scopes/commencement clauses were also read to locate overlays. Their identified provisions do not resolve the property-specific defects or prove no other amendments exist. URLs, source hashes and limited read scopes are in the additive property source manifest. Source fidelity for this new job was independently reviewed on 2026-11-01; no accountant attestation is claimed.

Not yet confirmed: Complete operative2026 property/amendment chain; authoritative unimproved-acreage wording/base and current currency/inflation treatment; s2009(a) public-land exemption cross-reference to2001(f) versus2000(c)(6); current valuation/zoning/classification practice and s60 appeal procedure; acquisition/annual forms, boxes, portal/payment references and successful filing; current market interest and application to particular partial payments; transfer/stamp/registration fees, title/foreign-ownership law and special concessions. All seven core country domains remain partial.
