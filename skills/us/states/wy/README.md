---
jurisdiction: US-WY
applicable:
- VAT
- SC
- PR
not_applicable:
  IT-IND: No Wyoming individual income tax or wage withholding.
  IT-CORP: No general corporate income, franchise or gross-receipts tax; the separate
    SOS annual report/license tax remains an entity maintenance obligation.
  TP: No separate state transfer-pricing documentation regime.
  XB: Interstate sales/use and payroll localization are within the owners below; complex
    interstate issues are referred.
covered_by:
  VAT: wy-sales-tax
  SC: wy-payroll
  PR: wy-payroll
partial:
  VAT: Hosted software/service classifications, current local/lodging rates, numeric2026
    interest and exact WYIFS field mapping remain unconfirmed.
  SC: Actual2026 employer notice required; industry-rate table/factors and special
    coverage computations not reproduced.
---

# Wyoming: 2026 tax skills

Wyoming has sales/use tax and employer UI, with no individual or corporate income tax. This batch rewrites sales/use and fills payroll. General corporate income/franchise/gross-receipts computation is not applicable, but SOS annual report/license tax still applies: it is an entity-maintenance job, not a profits tax. The existing `wy-formation` is retained unchanged outside this four-job tax rewrite and is not represented as refreshed2026 coverage. All tax skills are unapproved drafts. Property, minerals, wind-generation and detailed lodging compliance remain separate.

## Domains

| Job | Skill | Status |
| --- | --- | --- |
| VAT | `wy-sales-tax` | checked against the law; not accountant-reviewed |
| SC | `wy-payroll` | checked against the law; not accountant-reviewed |
| PR | `wy-payroll` | checked against the law; not accountant-reviewed |

## Official sources

- [Title39](https://www.wyoleg.gov/statutes/compress/title39.pdf), sales/use law read2026-11-13.
- [DWS2026 wage base](https://dws.wyo.gov/dws-division/unemployment-insurance/wyui/unemployment-taxable-wage-base/), read2026-11-13.
- [SOS fee schedule](https://sos.wyo.gov/Business/docs/BusinessFees.pdf), effectiveJuly1,2026, read2026-11-13; annual license obligation remains.
- [WRS withholding form](https://retirement.wyo.gov/wp-content/uploads/State-Tax-Withholding-Change-Form.pdf), read2026-11-13, Wyoming residents do not complete the state-income-tax form.
- [LSO corporate-tax analysis](https://wyoleg.gov/InterimCommittee/2024/S40-report-07-report-201_LSO_TaxationofElectricity_Final_11072024.pdf), Wyoming corporate-income-tax passage read2026-11-13.
