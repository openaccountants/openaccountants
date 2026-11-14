---
name: id-payroll
description: "Idaho employer payroll in 2026, including the July percentage withholding tables, zero child-credit allowance, supplemental payments, withholding registration and returns, plus unemployment insurance rates, wage base, new-employer rate, registration and quarterly reports. Confirmation gaps are explicit."
license: "AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)"
metadata:
  source: openaccountants
  openaccountants_url: "https://www.openaccountants.com/skills/id-payroll"
  jurisdiction: "US-ID"
  tax_year: "2026"
  last_updated: "2026-11-13"
---

# Idaho payroll withholding and unemployment insurance v1.0

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

**Quick reference:** published July 2026 withholding tables use 5.3% above a frequency/status amount and a zero child-credit allowance. Employer-paid UI has a $58,300 annual base and 1% new-employer standard rate in 2026. These are separate accounts. Built from the law; Not yet approved.

## Who this applies to

Employers with wages subject to Idaho withholding or covered Idaho UI employment. Federal employment-tax computations belong in `us-form-941-940-payroll`; its figures are not repeated here.

General UI coverage arises with at least $1,500 wages in a quarter or an employee in 20 different weeks in the current/prior year. Agriculture, domestic work, acquisitions, nonprofits/government and family/owner services have separate tests. Obtain Labor's determination instead of extending the ordinary test to every employer. See [Labor handbook, printed pages 4-10](https://www.labor.idaho.gov/wp-content/uploads/2025/11/Handbook_Tax-information_Nov.-2025-1.pdf).

## Rates, bands and thresholds

### Withholding: July 23, 2026 percentage method

For each frequency, calculate **5.3% x max(0, wages minus the applicable amount)** and round to whole dollars. Single includes head of household. The child-credit allowance is zero; the [Commission computing page](https://tax.idaho.gov/taxes/income-tax/withholding/computing/) explains the credit's sunset. These payroll amounts are not annual-return bands.

| Payroll frequency | Single / head of household | Married | Official source |
|---|---|---|---|
| Annual | $16,100 | $32,200 | [EPB00744, page 1](https://tax.idaho.gov/wp-content/uploads/pubs/EPB00744/EPB00744_07-23-2026.pdf) |
| Monthly | $1,342 | $2,683 | [EPB00744, page 1](https://tax.idaho.gov/wp-content/uploads/pubs/EPB00744/EPB00744_07-23-2026.pdf) |
| Semimonthly | $671 | $1,342 | [EPB00744, page 2](https://tax.idaho.gov/wp-content/uploads/pubs/EPB00744/EPB00744_07-23-2026.pdf) |
| Biweekly | $619 | $1,238 | [EPB00744, page 2](https://tax.idaho.gov/wp-content/uploads/pubs/EPB00744/EPB00744_07-23-2026.pdf) |
| Weekly | $310 | $619 | [EPB00744, page 3](https://tax.idaho.gov/wp-content/uploads/pubs/EPB00744/EPB00744_07-23-2026.pdf) |
| Daily / miscellaneous | $62 | $124 | [EPB00744, page 3](https://tax.idaho.gov/wp-content/uploads/pubs/EPB00744/EPB00744_07-23-2026.pdf) |
| Separately paid supplemental wages | 5.3% of the separate payment; alternatively combine with regular wages | Apply the chosen permitted method consistently to the payment | [Computing instructions](https://tax.idaho.gov/taxes/income-tax/withholding/computing/) |

### Unemployment insurance: calendar 2026

| Item | Amount and condition | Official source |
|---|---|---|
| Taxable wage base | First $58,300 per covered employee per year | [Order 682; Code 72-1347A/72-1350](https://www.labor.idaho.gov/wp-content/uploads/2024/12/AO.682.pdf) |
| New-employer standard rate | 1.000%, except cost-reimbursement employers; initial period at least six calendar quarters | [2026 Order 682](https://www.labor.idaho.gov/wp-content/uploads/2024/12/AO.682.pdf); [standard-rate qualification](https://www.labor.idaho.gov/businesses/unemployment-tax-rates/) |
| Positive classes +1 through +7 | Respectively 0.208%, 0.347%, 0.417%, 0.486%, 0.555%, 0.625%, 0.694% | [Order 682](https://www.labor.idaho.gov/wp-content/uploads/2024/12/AO.682.pdf) |
| Deficit classes -1 through -6 | Respectively 1.250%, 1.389%, 1.527%, 1.666%, 1.944%, 5.400% | [Order 682](https://www.labor.idaho.gov/wp-content/uploads/2024/12/AO.682.pdf) |
| Reserve tax | Not imposed in 2026 | [Order 682](https://www.labor.idaho.gov/wp-content/uploads/2024/12/AO.682.pdf) |
| UI report and payment | Last day of April, July, October and January for the preceding quarter; next business day if weekend/holiday | [Labor handbook, printed page 18; Code 72-1349](https://www.labor.idaho.gov/wp-content/uploads/2025/11/Handbook_Tax-information_Nov.-2025-1.pdf) |

Use the employer's assigned notice. The order's 0.729% base factor is not an extra charge added to the assigned class. The [Labor rate page](https://www.labor.idaho.gov/businesses/unemployment-tax-rates/) has older headline figures but links the 2026 array; Order 682 supplies this skill's annual values.

## The base

**Withholding:** keep the federal W-4 and obtain ID W-4 information. Select the actual frequency/status and the dated table. The [computing instructions](https://tax.idaho.gov/taxes/income-tax/withholding/computing/) say to apply new tables prospectively without adjusting earlier payroll merely for a table change. Its older annualized example uses a different annual subtraction; the dated July table above controls this percentage method.

**UI:** track covered wages paid and calendar-year taxable wages per employee. Limit current taxable wages to the remaining annual base, but report covered wages above the cap too. UI is employer-paid, not an employee deduction. See the [Labor handbook, printed pages 2 and 21-22](https://www.labor.idaho.gov/wp-content/uploads/2025/11/Handbook_Tax-information_Nov.-2025-1.pdf).

## Deadlines and filing

1. **Register withholding.** Obtain an EIN, submit Idaho Business Registration and use the correct legal entity. New ownership/entity changes need the correct account; do not use the former owner's vouchers. See [Commission registration](https://tax.idaho.gov/taxes/income-tax/withholding/apply/).
2. **Use the assigned cycle.** The [filing page](https://tax.idaho.gov/taxes/income-tax/withholding/withholding-filing/) identifies semimonthly thresholds of $25,000 a month or $300,000 over 12 months, quarterly filing at $750 or less per quarter, and annual filing below $750 annually. Monthly and farmer exceptions require the account's determination. Do not self-elect a less frequent cycle.
3. **File/pay Form 910 in TAP.** Choose Withholding Tax and the correct period's File Return link; enter the period's withholding, submit/pay and retain confirmation. File zero returns for active periods. If no confirmation appears, correct the invalid fields. See [Form 910 filing](https://tax.idaho.gov/taxes/income-tax/withholding/withholding-filing/filing-form-910/). Periodic due dates remain unconfirmed below; obtain the issued account deadline before scheduling payment.
4. **Reconcile Form 967.** Form 967/W-2s are due by the last day of January; 1099s by the last day of February, with all-in-January filing available. Include relevant 1099 withholding in total Idaho tax withheld and reconcile to payments. Uploads in TAP generate confirmation; information returns cannot be entered manually one by one. See [information-return filing](https://tax.idaho.gov/taxes/income-tax/withholding/withholding-filing/filing-information-returns-1099s-w-2s/). Confirm calendar adjustments.
5. **Register/file UI separately.** Submit IBR and use Labor's Employer Portal, not TAP, for employee wage schedules and the quarterly tax report. Reconcile total, excess and taxable wages; apply the assigned rate; submit/pay and retain confirmation/account records. Active accounts file even without wages; paper reporting needs approval. See [Labor handbook, printed pages 2-5](https://www.labor.idaho.gov/wp-content/uploads/2025/11/Handbook_Tax-information_Nov.-2025-1.pdf) and [official portal entry point](https://www.labor.idaho.gov/businesses/help-with-unemployment-tax/).

## Penalties and interest

Reconcile filing and payment postings in both accounts. Current penalty schedules and annual interest rates have not been fully checked here; obtain the relevant agency's current calculation before computing arrears.

## Cross-border points

Do not assign UI solely from residence or apply withholding to all remote work automatically. Multistate localization, military-spouse relief, wage exclusions and successor carryovers require separate authority and facts; their computations are outside this skill.

## Two worked examples that recompute

**Biweekly withholding.** Invented single employee receives $1,212 and claims four Idaho allowances. Each allowance is zero; ($1,212 - $619) x 5.3% = $31.429, rounded to $31. This follows the [Commission's current computation](https://tax.idaho.gov/taxes/income-tax/withholding/computing/), not the sunsetted credit.

```oa-check
name: Idaho biweekly withholding July 2026
inputs:
  wages: 1212
  allowances: 4
steps:
  deduction: allowances * 0
  withholding: round(max(0, wages - deduction - 619) * 0.053, 0)
expected:
  deduction: 0
  withholding: 31
```

**UI cap and rate boundary.** Invented covered employee has used $55,000 of the annual base and receives another $5,000. The report includes $5,000, with $3,300 taxable. A standard-rate employer owes $33; one actually assigned deficit class -6 owes $178.20. These are notice-based alternatives, not an election. Source: [2026 Order 682](https://www.labor.idaho.gov/wp-content/uploads/2024/12/AO.682.pdf).

```oa-check
name: Idaho UI cap crossing 2026
inputs:
  prior_taxable_wages: 55000
  current_wages: 5000
steps:
  taxable_wages: min(current_wages, max(0, 58300 - prior_taxable_wages))
  standard_tax: taxable_wages * 0.01
  deficit_class_6_tax: taxable_wages * 0.054
expected:
  taxable_wages: 3300
  standard_tax: 33
  deficit_class_6_tax: 178.20
```

## Ask the client first

- Where do employees work/live, and what worker/owner classification applies?
- What pay dates, frequencies, statuses and W-4 records apply?
- What covered wages and annual taxable wages have already been paid?
- What withholding-cycle and UI coverage/rate notices were issued?
- Is the employer new, a successor, agricultural/domestic, nonprofit or reimbursable?
- Which returns, corrections, payments and unpaid periods need reconciliation?

## Sources

| Source | URL | Read for | Read on |
|---|---|---|---|
| Commission July 23, 2026 percentage tables | https://tax.idaho.gov/wp-content/uploads/pubs/EPB00744/EPB00744_07-23-2026.pdf | Read all three pages for pay-frequency/status amounts and 5.3% formula | 2026-11-13 |
| Commission computing | https://tax.idaho.gov/taxes/income-tax/withholding/computing/ | Read for zero credit allowance, prospective updates, rounding and supplemental payments; noted old-example discrepancy | 2026-11-13 |
| Commission registration | https://tax.idaho.gov/taxes/income-tax/withholding/apply/ | Read for EIN/IBR, ownership changes and account identity | 2026-11-13 |
| Commission filing | https://tax.idaho.gov/taxes/income-tax/withholding/withholding-filing/ | Read for cycle thresholds, farmer exceptions and reconciliation | 2026-11-13 |
| Commission Form 910 | https://tax.idaho.gov/taxes/income-tax/withholding/withholding-filing/filing-form-910/ | Read for period selection, zero returns and submission confirmation | 2026-11-13 |
| Commission information returns | https://tax.idaho.gov/taxes/income-tax/withholding/withholding-filing/filing-information-returns-1099s-w-2s/ | Read for annual deadlines, reconciliation and upload confirmation | 2026-11-13 |
| Labor Order 682, November 6, 2025, effective calendar 2026 | https://www.labor.idaho.gov/wp-content/uploads/2024/12/AO.682.pdf | Read complete order for base, standard/class rates and no reserve tax; directory year is not coverage year | 2026-11-13 |
| Labor rate explanations | https://www.labor.idaho.gov/businesses/unemployment-tax-rates/ | Read for initial six-quarter standard period, notices and 2026 array link; older headline values not used | 2026-11-13 |
| Labor linked handbook, revision November 5, 2025 | https://www.labor.idaho.gov/wp-content/uploads/2025/11/Handbook_Tax-information_Nov.-2025-1.pdf | Read printed pages 2-10, 18 and 21-22 for coverage, registration, reporting, quarterly deadlines and wage-base mechanics; annual values from Order 682 | 2026-11-13 |
| Labor UI help | https://www.labor.idaho.gov/businesses/help-with-unemployment-tax/ | Read for official Employer Portal and current handbook link | 2026-11-13 |

Not yet confirmed: Form 910 periodic due dates (direct fetches and ordinary browser navigation timed out; search snippets were not treated as a read); final 2026 reconciliation specifications and calendar adjustments; full wage exclusions, multistate/military treatment and successor rules; current penalty/interest computations. This skill uses the published July table prospectively and does not reconstruct earlier 2026 tables.

## Today's figures and who stands behind this skill

This file is an AI skill (tax rules your AI follows) from OpenAccountants, copied on 2026-11-13. Rates, thresholds and deadlines change. For the current version of this skill, its official sources and the named accountant (if any) who stands behind it, call `get_skill` with slug `id-payroll` on the OpenAccountants connector (https://www.openaccountants.com/connect), or read https://www.openaccountants.com/skills/id-payroll. If neither is available, confirm every figure against the official source pages cited above before relying on it.
