---
jurisdiction: US-NM
applicable: [IT-IND, IT-CORP, VAT, SC, PR]
covered_by:
  IT-IND: nm-income-tax
  IT-CORP: nm-corporate-tax
  VAT: nm-sales-tax
  SC: nm-payroll
  PR: nm-payroll
partial:
  IT-IND: "Final 2026 forms/conformity and ancillary exemption/credit revisions not confirmed; complex PIT-B allocation remains outside resident computation."
  IT-CORP: "Ordinary C-corporation rate/franchise covered; final 2026 forms, full apportionment/group/loss/credit mechanics need confirmation."
  VAT: "GRT/compensating tax sourced for 2025-2026 filing cycle; July-December 2026 locality schedule and item-specific exceptions not fetched."
  SC: "UI source access failed after direct, browser and archive attempts; 2026 base, rates, registration, returns and deadlines remain unconfirmed and no indexed-only figures are used."
  PR: "2026 withholding and new quarterly report sourced; final TRD-41431 fields and workers-compensation fee details remain unconfirmed."
not_applicable:
  TP: "No separate state documentation skill; federal and state related-party/group rules can still apply."
  XB: "No separate cross-border skill in this pack; interstate/foreign issues require applicable federal skills and state allocation review."
---

# New Mexico: 2026 state tax pack

New Mexico taxes individual and corporate income and imposes a broad Gross Receipts Tax on business receipts. GRT fills the sales-tax job but is imposed on the business; complementary compensating tax covers qualifying use. Corporate franchise tax is separate from income tax. Employers have state withholding and unemployment obligations. USD applies. This pack is tier 2, not approved by an accountant.

| Job | covered_by | Coverage |
|---|---|---|
| Individual wages/business income | `nm-income-tax` | Statutory 2025-onward schedules; verified 2025-2026 filing-cycle ancillary rules and final-2026 gaps |
| Sales/use through GRT/compensating tax | `nm-sales-tax` | Base, nexus, location/rate lookup, deductions and return workflow; later-2026 local schedule gap |
| Corporate income/franchise | `nm-corporate-tax` | 5.9% statutory rate and USD 50 franchise, ordinary computation, estimates and filing-cycle limits |
| Payroll withholding and UI | `nm-payroll` | Actual 2026 withholding tables/new TRD-41431 report; UI is explicitly incomplete due to source access |

The missing UI evidence means this is not a claim of full state-pack completion. No 2026 UI figure is copied from a search snippet or invented. Final-year gaps appear under Not yet confirmed in every skill.

Separate jobs outside these skills: county property tax, oil/gas/mineral severance, cannabis excise, insurance premium, specialist entity/credit regimes, estate/fiduciary and detailed multistate allocations. No outside-scope entry establishes that a tax does not exist.

## Official sources

- [Enacted HB252](https://www.nmlegis.gov/Sessions/24%20Regular/final/HB0252.pdf), read 2026-11-13 for personal/corporate rates and 2025-onward applicability.
- [2025 PIT-1](https://realfile.tax.newmexico.gov/2025pit-1-ins.pdf) and [PIT-ADJ](https://realfile.tax.newmexico.gov/2025pit-adj-ins.pdf), read 2026-11-13 for 2025-2026 filing-cycle adjustments, exemptions, credits and filings.
- [FYI-105](https://realfile.tax.newmexico.gov/FYI-105.pdf) and [FYI-350](https://realfile.tax.newmexico.gov/FYI-350.pdf), read 2026-11-13 for stated GRT and corporate source periods.
- [FYI-104 effective 2026](https://realfile.tax.newmexico.gov/FYI-104.pdf) and [July 2026 TRD-41414 instructions](https://realfile.tax.newmexico.gov/trd-41414ins.pdf), read 2026-11-13 for withholding and quarterly-report changes.
- Workforce UI sources failed direct/browser/archive access and are recorded as unconfirmed in `nm-payroll`, not as read.
