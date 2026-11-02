---
name: gg-gst-transition
description: >
  Prepare Guernsey and Alderney GST transition working papers from the October 2026 approved tax reform package. Distinguish the published 2029 timetable and illustrative price calculations from enacted charging, registration and return requirements. Covers the adopted commencement safeguards, operational evidence needed before implementation, and the relationship with income-tax, social-security and benefit changes. Use for GST readiness, planned pricing and review of reform assumptions. This source-cited draft does not establish a current GST liability, a complete consumption-tax regime, customs treatment or a reviewed not-applicable determination. Enacted rules remain outstanding; the source-review record states the scope reviewed.
jurisdiction: GG
category: international
tax_year: 2026
tier: 2
last_updated: 2026-10-22
version: 0.2
verified_by: pending
sources:
  - url: "https://gov.gg/taxreform"
    title: "States of Guernsey, approved Tax Reform package and timetable"
    as_of: "2026-10-22"
  - url: "https://statesvoting-records.gov.gg/Propositions/Details/2682"
    title: "P.2026/49 Proposition 1 as amended, carried 2 October 2026"
    as_of: "2026-10-22"
  - url: "https://statesvoting-records.gov.gg/Propositions/Details/2787"
    title: "P.2026/49 Proposition 15, direction to prepare legislation"
    as_of: "2026-10-22"
---

# Guernsey GST transition: approved policy and implementation evidence

## Who this applies to

This is a planning Guide for the Guernsey and Alderney reform package, checked on 22 October 2026. It does not determine territorial application to other Bailiwick islands or liability for a particular supply. The States approved the amended package in October 2026. Proposition 15 separately directs preparation of implementing legislation: approval of policy is not itself evidence of every charging provision or its commencement. [Proposition 1](https://statesvoting-records.gov.gg/Propositions/Details/2682); [Proposition 15](https://statesvoting-records.gov.gg/Propositions/Details/2787).

## Rates, bands and thresholds

| Item | Published plan | Status and source |
|---|---|---|
| Initial GST | 3%, first quarter of 2029 | Published implementation timetable, not a current charging instruction; [reform page](https://gov.gg/taxreform) |
| Personal tax and social-security changes | 1 January 2029 | Planned timetable; do not replace 2026 rates; [reform page](https://gov.gg/taxreform) |
| Corporate changes | 1 January 2027 | Separate timetable; do not assume every reform starts together; [reform page](https://gov.gg/taxreform) |
| Food produced or grown by small independent suppliers | 0% instead of 3% in the adopted direction | Final statutory definitions and evidence requirements still needed; [Proposition 1](https://statesvoting-records.gov.gg/Propositions/Details/2682) |
| Registration and turnover threshold | Not established by this Guide | Obtain enacted registration rules; no threshold is inferred from Jersey |

The official page says monetary thresholds will be adjusted for inflation before implementation. Do not treat an illustrative calculator threshold as a fixed future statutory figure. [Reform page](https://gov.gg/taxreform).

## The base

The verified evidence does not establish comprehensive taxable supplies, valuation, input-tax recovery, exemptions, imports, tax points or transition rules. Keep proposed prices separate from a VAT/GST ledger posting. A zero-rated category in an adopted direction does not yet establish its eventual input-tax entitlement or operational test. Do not import another island's rules.

## Deadlines and filing

Before treating GST as operational, obtain the legislation, commencement instrument, territorial scope and current registration/return guidance. Record their dates and applicability to the transaction. The adopted resolution requires the associated income-tax and social-security mitigations, benefit increases and Essential Costs Relief Payment arrangements to be operational before GST becomes chargeable. Retrospective compensation or later systems completion does not satisfy that requirement. [Proposition 1(a)](https://statesvoting-records.gov.gg/Propositions/Details/2682).

The resolution directs deferral if those conditions are unmet, a revised timetable, and publication of a joint implementation assurance report by the Policy & Resources Committee and the Committee for Employment & Social Security before a commencement instrument is made or submitted. Where a required event occurs after the report, the Committees must publish confirmation before chargeability. The implementing legislation is to preserve these conditions without an administrative waiver. [Proposition 1(b)–(f)](https://statesvoting-records.gov.gg/Propositions/Details/2682).

For the working paper, retain the report, any subsequent confirmation and the legal commencement evidence. The report alone is not a substitute for the law. Registration deadlines, return periods, payment dates and forms remain unverified here.

## Penalties and interest

No GST penalty or interest schedule is established by the sources used in this Guide. Do not substitute income-tax penalties or report a zero penalty. Obtain the enacted GST compliance provisions before advising on a missed obligation.

## Cross-border points

The published plan includes an International Service Entities scheme for finance businesses with international clients, involving a fee and an End User Relief Certificate. This Guide does not establish eligibility, fees or application procedure. It also does not establish import relief or customs/excise rates. [Reform page](https://gov.gg/taxreform). An international customer alone is not evidence of an available GST exemption.

## Two worked examples that recompute

These are **planning scenarios only**, assuming a single supply becomes taxable at the published initial 3% rate. Neither example establishes that GST is currently due or that a supply belongs in that category.

**Simple exclusive price.** A hypothetical £1,000 price before GST would produce £30 GST and £1,030 total if the assumed rate and treatment apply.

```oa-check
name: Guernsey planned GST exclusive-price scenario, not current liability
inputs:
  net_price: 1000
  assumed_rate: 0.03
steps:
  - hypothetical_gst: net_price * assumed_rate
  - gross_price: net_price + hypothetical_gst
expected:
  hypothetical_gst: 30
  gross_price: 1030
```

**Fixed inclusive-price edge case.** If a contract instead holds the customer's total at £1,000, the same assumed treatment gives net revenue £970.87 and GST £29.13 after rounding. Adding £30 to that fixed total would change the contractual assumption. This example does not prescribe statutory invoice-rounding rules.

```oa-check
name: Guernsey planned GST fixed-inclusive-price scenario
inputs:
  fixed_total: 1000
  assumed_rate: 0.03
steps:
  - net_price: round(fixed_total / (1 + assumed_rate), 2)
  - hypothetical_gst: fixed_total - net_price
expected:
  net_price: 970.87
  hypothetical_gst: 29.13
```

## Ask the client first

- Which island, business activity, supply and customer location are involved?
- What are the contractual supply/payment dates and the price-change clauses?
- Is the price fixed inclusive or exclusive of any future tax?
- What facts support any claimed supplier category or international-services treatment?
- Which transactions are imports, exports or domestic supplies?

## Sources and acceptance gaps

All three sources in frontmatter were read on 22 October 2026: [official timetable](https://gov.gg/taxreform), [adopted commencement conditions](https://statesvoting-records.gov.gg/Propositions/Details/2682) and [legislation direction](https://statesvoting-records.gov.gg/Propositions/Details/2787). The latter two record votes carried on 2 October 2026. This draft records a verified policy transition, not comprehensive VAT/GST coverage, professional attestation or a determination that consumption taxes are inapplicable. Current domestic tax scope, customs/excise, enacted implementation, operational rules and current-law reconciliation remain open. Independent source review is recorded in the pack README.

## Disclaimer

General reference and planning material only. A qualified professional must verify the applicable law, commencement and facts before filing, paying or acting on this draft.
