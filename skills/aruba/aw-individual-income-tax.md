---
name: aw-individual-income-tax
description: >
  Aruba individual income tax and wage tax table calculations for 2026. Covers the distinction between taxable income, annualized net wages and table income, progressive bands, the maximum annual tax-free amount, downward rounding and worked annual calculations. Use for questions about Aruba income tax brackets, loonbelasting, inkomstenbelasting or tabelinkomen. This is a calculation reference after the income base and allowance entitlement have been established. It does not determine residence, deductions, special income treatment, credits, return deadlines, monthly payroll withholding or social contributions. Official indexed guidance still requires direct source rechecking before release.
version: 0.2
jurisdiction: AW
tax_year: 2026
last_updated: 2026-11-01
authored_by: Michael Cutajar and the OpenAccountants team
review_status: pending_review
trust_label: Built by Michael Cutajar and the OpenAccountants team
category: international
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Aruba individual income tax: 2026 table

## Scope and evidence

Source-cited draft, not accountant-reviewed. This Guide calculates the annual table amount only. The [DIMP rate page](https://www.impuesto.aw/tarief-inkomstenbelasting-en-loonbelasting) was available as indexed official text on 22 October 2026; a direct request returned a maintenance notice. Recheck the live schedule and applicable legal instrument before release or filing reliance.

## Calculation

DIMP defines table income as taxable income minus the available tax-free amount for income tax, or annualized net wages minus that amount for wage tax. The annual tax-free amount is at most Afl. 30,000. This is not permission to deduct it from every gross payment.

Apply the following 2026 schedule to established table income. Amounts are Aruban florins; upper limits are inclusive. Round the resulting tax down to whole florins. [Source: DIMP 2026 table](https://www.impuesto.aw/tarief-inkomstenbelasting-en-loonbelasting).

| Table income | Base tax | Add tax on excess above |
|---|---:|---|
| 0–34,930 | 0 | 0% |
| Over 34,930–63,904 | 0 | 21% above 34,930 |
| Over 63,904–135,527 | 6,084.54 | 42% above 63,904 |
| Over 135,527 | 36,166.20 | 52% above 135,527 |

## Worked checks

These are arithmetic examples using already established table income, before credits or other adjustments:

| Table income | Calculation | Rounded table tax |
|---|---|---:|
| 50,000 | (50,000 − 34,930) × 21% = 3,164.70 | 3,164 |
| 100,000 | 6,084.54 + (100,000 − 63,904) × 42% = 21,244.86 | 21,244 |
| 150,000 | 36,166.20 + (150,000 − 135,527) × 52% = 43,692.16 | 43,692 |

## Working-paper controls

Keep the income-base calculation, allowance evidence, table year and rounding step separately. Check continuity at each band boundary. Do not treat this annual illustration as a payslip withholding calculation or an assessment of tax still payable.

## Filing and exclusions

Annual return deadlines, residence, partial-year treatment, spousal allocation, deductions, special rates and credits are unresolved here. Obtain the relevant current return instructions and taxpayer facts before completing an assessment. Social insurance has a separate base and is outside this table.

General research reference only; professional review and the applicable official instructions are required for an actual return.

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
