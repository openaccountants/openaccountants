---
name: kn-housing-social-development-levy
description: "Saint Kitts and Nevis payroll levy reference checked for 2026. Covers the Housing and Social Development Levy exemption thresholds introduced in July 2025, the monthly employee calculation, employer contribution and worked boundary examples. Use for ordinary payroll levy deductions after the applicable wage base is established. Explains why the exemption threshold is not a tax-free allowance and why social security ceilings must not cap this levy. Separates historical December bonus relief from current ordinary payroll. Legislative amendment reconciliation, special payments and independent accountant review remain outstanding; this is a source-cited draft."
license: "AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)"
metadata:
  source: openaccountants
  openaccountants_url: "https://www.openaccountants.com/skills/kn-housing-social-development-levy"
  jurisdiction: "KN"
  tax_year: "2026"
  last_updated: "2026-10-23"
  authored_by: "Ryan Duguid"
  trust_label: "Accountant-authored"
  review_status: "pending_review"
---

# Saint Kitts and Nevis Housing and Social Development Levy

## Scope and source date

This source-cited draft covers ordinary employment wages, checked 22 October 2026. The Board administers collection under the Housing and Social Development Levy Act 7 of 1997. [Board overview](https://socialsecurity.kn/housing-levy/). The operative administrative source for these calculations is its [16 July 2025 notice](https://socialsecurity.kn/press/change-of-levy-deduction-threshold/), effective 1 July 2025 and expressly superseding earlier releases on the matter.

## Employee exemption and monthly calculation

The notice exempts wages up to and including these amounts: weekly EC$520; fortnightly EC$1,040; twice-monthly EC$1,126.67; monthly EC$2,253.33. The monthly calculation above that cutoff is:

| Monthly wages W | Employee levy |
|---|---|
| W ≤ 2,253.33 | Zero |
| 2,253.33 < W ≤ 6,500 | 3.5% × W |
| 6,500 < W ≤ 8,000 | 227.50 + 10% × (W − 6,500) |
| W > 8,000 | 377.50 + 12% × (W − 8,000) |

The employer pays 3% of all wages, including wages below the employee cutoff. [Threshold notice](https://socialsecurity.kn/press/change-of-levy-deduction-threshold/).

## Worked monthly examples

Amounts are EC dollars, displayed to cents; the examples do not establish an official rounding rule.

| Ordinary monthly wages | Employee levy | Employer levy |
|---|---:|---:|
| 2,253.33 | 0.00 | 67.60 |
| 2,253.34 | 78.87 | 67.60 |
| 4,000 | 140.00 | 120.00 |
| 6,500 | 227.50 | 195.00 |
| 7,000 | 277.50 | 210.00 |
| 8,000 | 377.50 | 240.00 |
| 9,000 | 497.50 | 270.00 |

The jump in the first two rows follows from the exemption cutoff. Subtracting 2,253.33 before applying 3.5% would produce the wrong result. For a payroll implementation, test both sides of that cutoff and both higher-band boundaries. Keep the pay frequency with each calculation; do not substitute the weekly exemption for a monthly worker.

## Reporting and distinct payroll liabilities

The [employer booklet](https://socialsecurity.kn/wp-content/uploads/2018/05/Employers-Guide-2018.pdf), pages 19–20, states that the levy has no contribution ceiling and is reported with Form C3 alongside the other payroll contributions. It gives monthly submission within one month after month end. The booklet's old low-wage exemption figure is superseded by the 2025 notice and must not be copied into a current payroll table.

Maintain separate ledger lines for employee levy, employer levy, social security and severance contributions. Reconcile the total C3 amount to those lines and retain the payroll period and receipt. These are suggested reconciliation controls, not additional legal filing requirements.

## December payments and unresolved work

The Board's [18 December 2025 notice](https://socialsecurity.kn/press/treatment-of-bonus-paid-in-december-2/) specifically exempts December 2025 bonuses and extra salary payments from levy deductions. It does not establish December 2026 levy relief. Classify any December 2026 payment against the applicable legislation and a current notice before applying an exemption. Do not import the separate social-security bonus treatment automatically.

This Guide does not settle nonstandard wage components, irregular payroll, statutory exemptions outside the stated cutoff, penalties or a December 2026 special measure. The amended levy legislation and any later instruments need reconciliation before merge. Independent accountant review is pending.

> Contributed by Ryan Duguid.

<!-- openaccountants-cta-block -->

---

## Talk to a verified accountant

This guide is maintained by the OpenAccountants network — accountants who put
their name behind the tax answers AI gives people. The live, always-current
version (and the professional behind it) is at
[openaccountants.com](https://www.openaccountants.com).

- Use it in your AI: https://www.openaccountants.com/connect
- Meet the accountants: https://www.openaccountants.com/network

> **General reference only.** This document does not constitute tax, legal, or
> financial advice. Verify figures against the cited primary sources or with a
> licensed professional before relying on them.

## Today's figures and who stands behind this skill

This file is an AI skill (tax rules your AI follows) from OpenAccountants, copied on 2026-10-23. Rates, thresholds and deadlines change. For the current version of this skill, its official sources and the named accountant (if any) who stands behind it, call `get_skill` with slug `kn-housing-social-development-levy` on the OpenAccountants connector (https://www.openaccountants.com/connect), or read https://www.openaccountants.com/skills/kn-housing-social-development-levy. If neither is available, confirm every figure against the official source pages cited above before relying on it.
