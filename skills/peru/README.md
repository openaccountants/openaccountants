---
jurisdiction: PE
applicable: [IT-IND, IT-CORP, VAT, SC, PR, TP, XB]
not_applicable: {}
covered_by:
  VAT: peru-igv
  TP: peru-transfer-pricing
  XB: peru-cross-border-tax
partial:
  IT-IND: "The merged 2026 owner covers work income; an ordinary rental/capital computation is not covered."
  IT-CORP: "Current 621 fields and the 2026 annual 710 version, fields and dates remain unconfirmed."
  SC: "Other 2026 AFP devengue schedules still need confirmation; the rewritten calculation verifies the November snapshot."
  PR: "Other 2026 AFP devengue schedules need confirmation before applying the November snapshot to another month."
  XB: "Current nonresident filing fields and administrative instructions remain unconfirmed."
---

# Peru: tax pack

<!-- Maintained coverage map. Preserve its source-verified partial and out-of-scope notes. -->

Tax years: 2026 (9 skills).

Coverage and professional approval are separate. The table reports the
merged skills plus this corporate update; pending PRs are listed below.

| Tax | Skill | Tax year | Coverage | Approval |
|---|---|---|---|---|
| Income tax | [Income tax](peru-income-tax.md) | 2026 | Partial: work income only; rental/capital method missing | Not yet approved |
| Company tax | [Corporate income tax](pe-corporate-income-tax.md) | 2026 | Partial: current form fields and annual dates unconfirmed | Not yet approved |
| VAT or sales tax | [IGV and IPM](peru-igv.md) | 2026 | Ordinary computation and filing covered | Not yet approved |
| Social contributions | [Social contributions](peru-social-contributions.md) | 2026 | Partial: other AFP months need confirmation | Not yet approved |
| Payroll | [Payroll](peru-payroll.md) | 2026 | Partial: other AFP months need confirmation | Not yet approved |
| Transfer pricing | [Transfer pricing](peru-transfer-pricing.md) | 2026 | Ordinary pricing and reporting method covered | Not yet approved |
| Cross-border | [Cross-border income tax](peru-cross-border-tax.md) | 2026 | Partial: current filing instructions unconfirmed | Not yet approved |

## What still needs doing

- Income tax: complete the ordinary rental and capital-income methods alongside the merged 2026 work-income method.
- Corporate income: confirm current 621 fields and the 2026 annual 710 version, fields and dates before a live filing.
- Social contributions and payroll: confirm other 2026 AFP devengue schedules before applying the verified November snapshot to another month.
- Confirm the current nonresident filing instructions and fields before treating the cross-border method as a completed filing workflow.

Pending PRs are not merged coverage. Tracked in [\[PE\] Complete the pack](https://github.com/openaccountants/openaccountants/issues/309).

## Other skills

- [Company formation](pe-company-formation.md) (2026)
- [Tax overview](pe-tax-overview.md) (2026)

## Out of scope

- VAT: detailed builder/land valuation; sector-specific SPOT and collection-agent administration; exporter refund and early-recovery applications; Amazonía, ZED and ZOFRATACNA; nonresident consumer-digital registration and returns. The IGV guide identifies these routes and covers ordinary imports and service exports.
