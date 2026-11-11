---
jurisdiction: PE
applicable: [IT-IND, IT-CORP, VAT, SC, PR, TP, XB]
not_applicable: {}
covered_by:
  VAT: peru-igv
  TP: peru-transfer-pricing
  XB: peru-cross-border-tax
partial:
  IT-IND: "The merged owner remains on 2025 and covers work income; an ordinary rental/capital computation is not covered."
  IT-CORP: "The merged owner remains on 2025; its 2026 rewrite is pending."
  SC: "The 2026 source correction is pending; other 2026 AFP devengue schedules still need confirmation."
  PR: "Other 2026 AFP devengue schedules need confirmation before applying the November snapshot to another month."
  XB: "Current nonresident filing fields and administrative instructions remain unconfirmed."
---

# Peru: tax pack

<!-- Maintained coverage map. Preserve its source-verified partial and out-of-scope notes. -->

Tax years: 2026 (6 skills), 2025 (3 skills).

Coverage and professional approval are separate. The table reports the
merged skills plus this overview update; pending PRs are listed below.

| Tax | Skill | Tax year | Coverage | Approval |
|---|---|---|---|---|
| Income tax | [Income tax](peru-income-tax.md) | 2025 | Partial: stale year; work income only | Not yet approved |
| Company tax | [Corporate income tax](pe-corporate-income-tax.md) | 2025 | Partial: 2026 rewrite pending | Not yet approved |
| VAT or sales tax | [IGV and IPM](peru-igv.md) | 2026 | Ordinary computation and filing covered | Not yet approved |
| Social contributions | [Social contributions](peru-social-contributions.md) | 2026 | Partial: source correction and other AFP months pending | Not yet approved |
| Payroll | [Payroll](peru-payroll.md) | 2026 | Partial: other AFP months need confirmation | Not yet approved |
| Transfer pricing | [Transfer pricing](peru-transfer-pricing.md) | 2026 | Ordinary pricing and reporting method covered | Not yet approved |
| Cross-border | [Cross-border income tax](peru-cross-border-tax.md) | 2026 | Partial: current filing instructions unconfirmed | Not yet approved |

## What still needs doing

- [Individual work-income PR #1410](https://github.com/openaccountants/openaccountants/pull/1410) updates the work-income method. It does not close the ordinary rental/capital gap.
- [Corporate-income PR #1403](https://github.com/openaccountants/openaccountants/pull/1403) updates the ordinary business regimes, computation and filing method.
- [Social-contributions PR #1437](https://github.com/openaccountants/openaccountants/pull/1437) corrects the source rules and November AFP snapshot. Other 2026 AFP devengue schedules still need confirmation for payroll and contributions.
- Confirm the current nonresident filing instructions and fields before treating the cross-border method as a completed filing workflow.

Pending PRs are not merged coverage. Tracked in [\[PE\] Complete the pack](https://github.com/openaccountants/openaccountants/issues/309).

## Other skills

- [Company formation](pe-company-formation.md) (2025)
- [Tax overview](pe-tax-overview.md) (2026)

## Out of scope

- VAT: detailed builder/land valuation; sector-specific SPOT and collection-agent administration; exporter refund and early-recovery applications; Amazonía, ZED and ZOFRATACNA; nonresident consumer-digital registration and returns. The IGV guide identifies these routes and covers ordinary imports and service exports.
