---
name: vu-income-tax
description: "Vanuatu personal income tax, tax year 2026: no ordinary personal income tax; the separate rent tax on individuals (12.5% of chargeable rent above VT 200,000 a six-month period), its periods, return dates and the VAT exclusion, from the Rent Taxation Act and DCIR."
license: "AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)"
metadata:
  source: openaccountants
  openaccountants_url: "https://www.openaccountants.com/skills/vu-income-tax"
  jurisdiction: "VU"
  tax_year: "2026"
  last_updated: "2026-11-14"
---

# Vanuatu personal income tax

> **General reference only.** Source-cited draft, not reviewed by an accountant. Do not use it to file or take a position without professional review.

## Who this applies to

Individuals living or earning in Vanuatu. Vanuatu has no ordinary domestic personal income tax: no rate, no threshold, no residence test and no annual return for salary, business or investment income. The Vanuatu Competent Authority's guide says in terms that "Vanuatu does not have an income tax system"; its residence criteria serve the Common Reporting Standard only. The one income-style charge on an individual is the rent tax on rent from leases of land in Vanuatu, set out below. Companies: see [corporate income tax](vu-corporate-income-tax.md). Employers: see [payroll](vu-payroll-social.md).

## Rates, bands and thresholds

| Item | Amount | Tax year | Official URL |
|---|---|---|---|
| Ordinary personal income tax | None | 2026 | https://vanuatucustoms.gov.vu/images/Forms/VCA/VU_AEOI_Guide_v4.pdf |
| Rent tax, natural person, chargeable rent for the period not over VT 200,000 | No tax is charged (Sch 1) | 2026 | https://vanuatucustoms.gov.vu/images/TAA/196_Rent_Taxation_Act_Consolidated_2020.pdf |
| Rent tax, natural person, chargeable rent over VT 200,000 | 12.5% of the excess over VT 200,000 (Sch 1) | 2026 | https://vanuatucustoms.gov.vu/images/TAA/196_Rent_Taxation_Act_Consolidated_2020.pdf |
| Rent tax, taxpayer not a natural person | 12.5% of all chargeable rent (Sch 1) | 2026 | https://vanuatucustoms.gov.vu/images/TAA/196_Rent_Taxation_Act_Consolidated_2020.pdf |
| Chargeable periods | 1 December to 31 May, and 1 June to 30 November (s 1) | 2026 | https://vanuatucustoms.gov.vu/images/TAA/196_Rent_Taxation_Act_Consolidated_2020.pdf |

The threshold is per six-month chargeable period, not per year.

## The base

Chargeable rent is rent from leases of land in Vanuatu for the period (ss 1, 3 to 11A). Exclude rent to the extent that a VAT-registered person derives rent that is subject to VAT. Before fixing the chargeable amount, check the Act's separate rules for trustees, joint or family arrangements, subleases, deemed rent, exemptions and bad debts. Schedule 1 allows no deduction for expenses; the natural-person threshold is its only relief.

## Deadlines and filing

Under ss 11 and 14, as substituted from 1 January 2020 by Act No. 7 of 2019, the taxpayer returns all rent within 28 days after the end of the period and pays by the return date. The unadjusted dates are 28 June (period to 31 May) and 28 December (period to 30 November). DCIR publishes an annual due-dates calendar that moves these for non-working days; check it for the actual period. Return form: DCIR's approved rent taxation return (https://vanuatucustoms.gov.vu/images/Forms/rates_taxes_forms/Approved-Rent-Taxation-Return-Form-2021.pdf).

## Penalties and interest

DCIR's rent tax guide says penalties and interest are charged for late filing and late payment (https://vanuatucustoms.gov.vu/images/Brochures/IRD/eng/Rent_Tax_Guide.pdf). The amounts sit in the Tax Administration Act and were not read for this guide.

## Cross-border points

There is no tax on a Vanuatu resident's foreign income and no tax on a non-resident's Vanuatu salary or business income. A non-resident landlord of Vanuatu land is still within the rent tax. Financial institutions report non-residents' accounts under the Common Reporting Standard; see [tax overview](vu-tax-overview.md).

## Two worked examples that recompute

**1. Individual landlord, VT 300,000 chargeable rent in one six-month period, no special adjustment.** Tax is (300,000 minus 200,000) times 12.5% = VT 12,500 (derived; DCIR's guide uses the same case).

```oa-check
name: Vanuatu rent tax natural person 300000
inputs:
  rent: 300000
  threshold: 200000
steps:
  - tax: max(rent - threshold, 0) * 0.125
expected:
  tax: 12500
```

**2. Individual landlord, VT 180,000 chargeable rent in the period.** Rent is at or below the threshold, so no tax is charged (derived).

```oa-check
name: Vanuatu rent tax under threshold
inputs:
  rent: 180000
  threshold: 200000
steps:
  - tax: max(rent - threshold, 0) * 0.125
expected:
  tax: 0
```

## Ask the client first

- Is the landlord a natural person, a company, a trust or a joint owner?
- Which six-month period, and the rent received in it?
- Is the landlord registered for VAT, and is the rent subject to VAT?
- Any sublease, deemed rent or bad debt?

## Sources

| Source | URL | Read on |
|---|---|---|
| Rent Taxation Act [Cap 196], Consolidated Edition 2020, ss 1, 4, 11, 14 and Sch 1 (Read for the rate, threshold and periods) | https://vanuatucustoms.gov.vu/images/TAA/196_Rent_Taxation_Act_Consolidated_2020.pdf | 2026-11-14 |
| DCIR rent tax guide (Read for the worked case and the penalties line) | https://vanuatucustoms.gov.vu/images/Brochures/IRD/eng/Rent_Tax_Guide.pdf | 2026-11-14 |
| Vanuatu Competent Authority, AEOI guide v4 (Read for "Vanuatu does not have an income tax system") | https://vanuatucustoms.gov.vu/images/Forms/VCA/VU_AEOI_Guide_v4.pdf | 2026-11-14 |
| Rent Taxation (Amendment) Act No. 7 of 2019, s 2 and Schedule (Read by Ryan Duguid for the 1 January 2020 commencement of ss 11 and 14) | https://vanuatucustoms.gov.vu/images/TAA/Rent_Taxation_Amendment_Act_No_7_of_2019.pdf | 2026-11-11 |
| Global Forum, Vanuatu 2026 second-round supplementary report, para 23 (Read by Ryan Duguid for no ordinary income tax) | https://www.oecd.org/content/dam/oecd/en/publications/reports/2026/04/global-forum-on-transparency-and-exchange-of-information-for-tax-purposes-vanuatu-2026-second-round-supplementary-report_7a20b670/75b3bc85-en.pdf | 2026-11-11 |

Not yet confirmed: the 2026 DCIR due-dates calendar (Ryan Duguid read the 2025 calendar as 30 June and 29 December for the two periods); rent tax penalty and interest amounts under the Tax Administration Act; the special rules for trustees, family arrangements, subleases and deemed rent; whether any Gazette instrument after the 2020 consolidation changes Schedule 1. The investment agency's summary gives 15%, which the Act does not support.

## Today's figures and who stands behind this skill

This file is an AI skill (tax rules your AI follows) from OpenAccountants, copied on 2026-11-14. Rates, thresholds and deadlines change. For the current version of this skill, its official sources and the named accountant (if any) who stands behind it, call `get_skill` with slug `vu-income-tax` on the OpenAccountants connector (https://www.openaccountants.com/connect), or read https://www.openaccountants.com/skills/vu-income-tax. If neither is available, confirm every figure against the official source pages cited above before relying on it.
