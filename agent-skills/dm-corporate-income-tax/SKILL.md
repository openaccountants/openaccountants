---
name: dm-corporate-income-tax
description: "Commonwealth of Dominica company income tax for 2026. Covers the 25% rate on chargeable income effective 1 January 2016, the return due within three months after the financial year end with the financial statements, the three prepayments of 25%, 35% and 40% for calendar-year companies by 31 March, 30 June and 30 September, the bridge from accounting profit to chargeable income and the limits of this skill. Trigger phrases include Dominica corporate tax, Dominica company income tax, Dominica tax prepayments, Income Tax Act 67:01."
license: "AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)"
metadata:
  source: openaccountants
  openaccountants_url: "https://www.openaccountants.com/skills/dm-corporate-income-tax"
  jurisdiction: "DM"
  tax_year: "2026"
  last_updated: "2026-11-14"
---

# Dominica company income tax

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

## Scope

Ordinary company income tax in the Commonwealth of Dominica for financial years in 2026, under the Income Tax Act, Chapter 67:01, as published by the Inland Revenue Division (IRD). Covers the rate, the return, and calendar-year prepayments once chargeable income is established. Amounts are EC$. It does not decide tax residence, permanent establishment, deductible expenses, capital allowances, losses, incentives, treaty claims or withholding on distributions. Individuals: [dm-income-tax-paye](dm-income-tax-paye.md).

## Ask the client first

1. Financial year end of the company.
2. Accounting profit and the adjustments to reach chargeable income, each with its authority.
3. Prior-year tax payable, and the current-year estimate.
4. Prepayments already made, with payment references and the year each relates to.
5. Any exemption, incentive or concession claimed (with the instrument).

## The method, step by step

### Rates, bands and thresholds

| Item | 2026 figure and conditions | Official source |
|---|---|---|
| Company rate | 25% on every dollar of chargeable income, effective 1 January 2016 | [IRD current income tax rates](https://www.ird.gov.dm/customer-service/current-income-tax-rates) |
| Return | Within 3 months after the financial year end, with the financial statements | [IRD corporate income tax](https://ird.gov.dm/tax-laws/corporate-income-tax) |
| Prepayment 1 (January to December year) | 25% of prior-year tax or current-year estimate, 31 March | [IRD tax due dates](https://ird.gov.dm/customer-service/tax-due-dates) |
| Prepayment 2 | 35%, 30 June | same |
| Prepayment 3 | 40%, 30 September | same |
| Balance of previous year's tax | 31 March | same |

### Steps

1. **Bridge** accounting profit to chargeable income; record the authority for each adjustment. Never apply 25% to unadjusted book profit.
2. **Tax:** chargeable income x 25%.
3. **Credits:** subtract prepayments that are reconciled to payment records for that year.
4. **File** the return with the financial statements within three months of year end. For a year ending 31 December 2026, by 31 March 2027.
5. **Prepay** for the current year on 31 March, 30 June and 30 September. The 31 March prepayment for the current year and the previous year's balance are two separate payments: label each.

## Boundary and exception table

| Situation | Treatment | Source |
|---|---|---|
| Non-calendar financial year | Return within 3 months of its year end; do not project the calendar-year prepayment dates without IRD instructions | [IRD corporate income tax](https://ird.gov.dm/tax-laws/corporate-income-tax) |
| IRD corporate page says the rate is 25% "on the net profit" | Apply it to chargeable income after the statutory adjustments, as the rate page states | [IRD current income tax rates](https://www.ird.gov.dm/customer-service/current-income-tax-rates) |
| Late prepayment or balance | Penalty and interest under the relevant Acts | [IRD tax due dates](https://ird.gov.dm/customer-service/tax-due-dates) |
| Losses, capital allowances, incentives, related parties, distributions | Not covered; refer | not covered |

## Worked cases

### Case 1: tax and balance due

Chargeable income EC$200,000: tax 50,000. Reconciled prepayments of 40,000 leave a balance of 10,000.

```oa-check
name: Dominica company tax on 200,000 chargeable income
inputs:
  chargeable: 200000
  prepaid: 40000
steps:
  - tax: chargeable * 0.25
  - balance: tax - prepaid
expected:
  tax: 50000
  balance: 10000
```

### Case 2 (decision): prepay on last year's tax or on this year's estimate?

Last year's tax was 40,000; this year's estimate is 50,000. On last year's basis the prepayments are 10,000, 14,000 and 16,000, leaving 10,000 to pay with the return. On the estimate they are 12,500, 17,500 and 20,000, leaving nothing. Both bases are allowed by the IRD calendar; the prior-year basis keeps cash longer, the estimate avoids a large balance on 31 March.

```oa-check
name: Dominica prepayments, prior-year 40,000 against estimate 50,000
inputs:
  prior: 40000
  estimate: 50000
steps:
  - prior_q1: prior * 0.25
  - prior_q2: prior * 0.35
  - prior_q3: prior * 0.40
  - est_q1: estimate * 0.25
  - est_q2: estimate * 0.35
  - est_q3: estimate * 0.40
  - balance_on_prior: estimate - prior
expected:
  prior_q1: 10000
  prior_q2: 14000
  prior_q3: 16000
  est_q1: 12500
  est_q2: 17500
  est_q3: 20000
  balance_on_prior: 10000
```

## When to refuse or refer

- Residence, permanent establishment, foreign income and treaty claims.
- Deductibility, capital allowances, loss relief, incentives and concessions.
- Withholding on dividends and payments to nonresidents.
- Penalty and interest amounts: not on the IRD pages read.

## Filing and payment

1. File the company return with the financial statements within three months after year end ([IRD corporate income tax](https://ird.gov.dm/tax-laws/corporate-income-tax)).
2. Pay the previous year's balance and the first current-year prepayment by 31 March, then 30 June and 30 September ([IRD tax due dates](https://ird.gov.dm/customer-service/tax-due-dates)).
3. Keep the bridge, the payment references and the tax account reconciliation.

## Completion checklist

- Chargeable income bridged from accounts, each adjustment sourced.
- 25% applied; prepayments credited by year.
- Return and statements filed within three months.
- Prepayment basis chosen and recorded.

## Sources

| Source | URL | Read on |
|---|---|---|
| IRD current income tax rates: read for the 25% company rate on chargeable income effective 1 January 2016 | https://www.ird.gov.dm/customer-service/current-income-tax-rates | 2026-11-14 |
| IRD corporate income tax: read for the governing Act (Chapter 67:01), the 25%, 35% and 40% instalments and the return within 3 months with financial statements | https://ird.gov.dm/tax-laws/corporate-income-tax | 2026-11-14 |
| IRD tax due dates: read for 31 March return and balance, and the prepayment dates and percentages | https://ird.gov.dm/customer-service/tax-due-dates | 2026-11-14 |

Not yet confirmed: the Income Tax Act Chapter 67:01 text (not opened); prepayment dates for non-calendar years; penalty and interest rates; any 2026 budget change (none shown on the IRD rate page).

## Today's figures and who stands behind this skill

This file is an AI skill (tax rules your AI follows) from OpenAccountants, copied on 2026-11-14. Rates, thresholds and deadlines change. For the current version of this skill, its official sources and the named accountant (if any) who stands behind it, call `get_skill` with slug `dm-corporate-income-tax` on the OpenAccountants connector (https://www.openaccountants.com/connect), or read https://www.openaccountants.com/skills/dm-corporate-income-tax. If neither is available, confirm every figure against the official source pages cited above before relying on it.
