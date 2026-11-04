---
name: dm-income-tax-paye
description: "Dominica resident individual income tax and employer PAYE reference for 2026. Covers the resident allowance, post-allowance marginal tax bands, annual calculation examples, individual filing requirements and employer monthly and annual reporting. Use for Commonwealth of Dominica income tax, resident allowance, PAYE remittance or annual employee returns. It distinguishes the pre-allowance income presentation from chargeable income after allowances to prevent double deduction. Residence, special relief eligibility, benefits in kind and the detailed monthly withholding tables require separate analysis. This source-cited draft does not cover the Dominican Republic or constitute a complete personal tax assessment."
license: "AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)"
metadata:
  source: openaccountants
  openaccountants_url: "https://www.openaccountants.com/skills/dm-income-tax-paye"
  jurisdiction: "DM"
  tax_year: "2026"
  last_updated: "2026-10-23"
  authored_by: "Ryan Duguid"
  trust_label: "Accountant-authored"
  review_status: "pending_review"
---

# Dominica income tax and PAYE

## Scope

Commonwealth of Dominica (DM), not the Dominican Republic. Source-cited draft checked 22 October 2026. This Guide starts with an established taxable-income calculation for an eligible resident individual. It does not decide residence or the treatment of foreign income.

## Allowance and tax bands

IRD's [current rate schedule](https://www.ird.gov.dm/customer-service/current-income-tax-rates) grants residents an annual EC$30,000 allowance, effective from 1 January 2018. Its displayed thresholds include that allowance. The [PAYE guidance](https://ird.gov.dm/tax-laws/pay-as-you-earn-p-a-y-e) explains the separate post-allowance bands: 15% on the first EC$20,000, 25% on the next EC$30,000 and 35% thereafter.

Let C be non-negative chargeable income **after** applicable allowances:

| C | Tax before credits |
|---|---|
| Up to 20,000 | C × 15% |
| Over 20,000 to 50,000 | 3,000 + (C − 20,000) × 25% |
| Over 50,000 | 10,500 + (C − 50,000) × 35% |

Never deduct the resident allowance again when C already excludes it. Do not infer an allowance for a nonresident.

## Worked annual examples

Assume the only applicable allowance is EC$30,000 and the stated income base is already established before that allowance:

| Income base | C | Tax before credits |
|---|---:|---:|
| 50,000 | 20,000 | 3,000 |
| 80,000 | 50,000 | 10,500 |
| 100,000 | 70,000 | 17,500 |

These are annual illustrations, not monthly withholding tables. Confirm reliefs and credits before determining the final balance.

## Individual return

IRD states a 31 March filing deadline. Its guidance exempts individuals whose income is entirely employment income and below EC$30,000 from filing; do not extend that exception to business income or the exact boundary without checking the applicable provisions. Self-employed filers attach Schedule G or a statement of earnings. Income from different sources must be considered together. [IRD personal income tax guidance](https://ird.gov.dm/tax-laws/personal-income-tax).

## Employer calendar

Monthly PAYE returns and deductions are due by the 15th of the following month, including returns where no tax was deducted. The annual remuneration/PAYE return, Form TD5, is due 31 January following the year. [PAYE guidance](https://ird.gov.dm/tax-laws/pay-as-you-earn-p-a-y-e); [IRD due dates](https://ird.gov.dm/customer-service/tax-due-dates).

## Controls and unresolved scope

Reconcile employee declarations, taxable pay, allowances, monthly withholding and annual certificates. Keep social-security deductions separate. Residence tests, mortgage and student-loan relief conditions, nonresident rules, business deductions, special income and payroll rounding are not resolved here. Review the applicable law and taxpayer documents before filing; no accountant attestation is claimed.

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

This file is an AI skill (tax rules your AI follows) from OpenAccountants, copied on 2026-10-23. Rates, thresholds and deadlines change. For the current version of this skill, its official sources and the named accountant (if any) who stands behind it, call `get_skill` with slug `dm-income-tax-paye` on the OpenAccountants connector (https://www.openaccountants.com/connect), or read https://www.openaccountants.com/skills/dm-income-tax-paye. If neither is available, confirm every figure against the official source pages cited above before relying on it.
