---
name: wy-payroll
description: >
  Apply Wyoming 2026 payroll obligations: no state income withholding, but employer UI with a $33,800 employee wage base. Covers industry-based new-employer rates, WYUI registration, quarterly reporting, payment and localization boundaries. Trigger on Wyoming payroll, WYUI or Wyoming unemployment tax.
jurisdiction: US-WY
category: state-tax
tax_year: 2026
last_updated: 2026-11-13
tier: 2
version: "1.0"
type: situation-rules
---

# Wyoming payroll and unemployment insurance, tax year 2026

> **Source-cited draft.** Written by Codex. Not reviewed by an accountant. This skill supports a professional working paper; review the taxpayer facts and current forms before filing. Circular 230 section 10.37: this material is not a legal opinion or a substitute for reasonable factual and legal inquiry.

**Answer first.** Wyoming has no state income-tax withholding; covered employers still pay UI on each employee's first $33,800 of 2026 wages, using the employer's full assigned rate, including adjustment factors.

## Scope and who this is for

Wyoming covered employers, including a business formed elsewhere with employees working in Wyoming. This skill owns state payroll withholding and UI. Federal payroll taxes and Forms 941/940 remain in `us-form-941-940-payroll`; workers compensation, new-hire reports and wage/hour law are separate obligations. No employee UI deduction is permitted (W.S.27-3-503(a)).

## Ask the client first

1. Where does each employee actually work and reside, including interstate or remote work?
2. What entity type, worker/owner relationship, employee counts, wage history and coverage determination apply?
3. What full 2026 UI rate notice, industry classification, experience and successor history exist?
4. What wages have already been paid to each employee this calendar year and what are the current quarter wages?
5. Is the joint business registration complete, is the out-of-state questionnaire needed, and does the employer have WYUI access?

## The method, step by step

### Rates, bands and thresholds

| Item and conditions | Amount / treatment | Official source |
| --- | --- | --- |
| 2026 UI wage base per employee | $33,800 (2025 was $32,400) | [official text](https://dws.wyo.gov/dws-division/unemployment-insurance/wyui/unemployment-taxable-wage-base/) |
| New employer, less than three years experience | Industry average base, at least 1%, plus W.S.27-3-505 adjustment factors; use actual notice | [27-3-503(f)](https://www.wyoleg.gov/statutes/compress/title27.pdf) |
| Experienced employer, at least three years | Benefit-ratio base plus four adjustment factors; use actual total notice rate | [official text](https://dws.wyo.gov/dws-division/unemployment-insurance/employers/unemployment-tax-rates/) |
| Unregistered employer base | 8.5% before adjustments; do not treat as normal new-employer rate | [official text](https://dws.wyo.gov/dws-division/unemployment-insurance/employers/unemployment-tax-rates/) |
| UI contribution deducted from employee | Prohibited | [27-3-503(a)](https://www.wyoleg.gov/statutes/compress/title27.pdf) |
| Late-contribution interest | 2% per month or fractional month | [27-3-510(a)](https://www.wyoleg.gov/statutes/compress/title27.pdf) |

1. Establish Wyoming UI coverage and wage localization before applying any rate. An employer qualifying during a year is generally subject for the entire year under W.S.27-3-502(b); do not assume that registering late makes earlier wages disappear. Farm, domestic, nonprofit, owner and family-member exclusions require the applicable coverage provisions. Source: [27-3-103 to 109 and 502](https://www.wyoleg.gov/statutes/compress/title27.pdf).
2. Complete the **Joint Business Registration**, plus the **Out of State Questionnaire** for a non-Wyoming business. DWS issues the new-employer rate after registration. The base is industry-specific and is not a universal flat rate. Retrieve the full 2026 rate notice, including all four adjustment factors, in WYUI. Source: [official text](https://dws.wyo.gov/dws-division/unemployment-insurance/employers/unemployment-tax-rates/).
3. Use [DWS WYUI entry page](https://dws.wyo.gov/dws-division/unemployment-insurance/wyui/) to enter [WYUI](https://wyui.wyo.gov). Establish employer access and select the correct account and quarter. Employer services include wage reports, amendments, rate notices and payments. Source: [official text](https://dws.wyo.gov/dws-division/unemployment-insurance/employers/).
4. Build a wage schedule containing each employee's identity, full quarterly covered wages, previously reported year-to-date wages and excess wages. Taxable current wages = min(current wages, max(33,800 - earlier covered wages, 0)). Multiply the total taxable base by the **full notice rate**, not a base-only component. Review the portal's reported wages, rate, credits and tax before submitting. Sources: [official text](https://dws.wyo.gov/dws-division/unemployment-insurance/wyui/unemployment-taxable-wage-base/), [official text](https://dws.wyo.gov/dws-division/unemployment-insurance/employers/unemployment-tax-rates/), [official text](https://dws.wyo.gov/dws-division/unemployment-insurance/wyui/).
5. File the quarterly report in WYUI; then pay online or print the tax-payment voucher for check payment. Save the submitted report and payment evidence, and confirm the account balance. A draft, uploaded wage file or pending payment is not proof of an accepted return and payment. Source: [employer portal services](https://dws.wyo.gov/dws-division/unemployment-insurance/wyui/).

## Boundary and exception table

| Situation | Treatment |
| --- | --- |
| Wyoming wages with no state income tax | Federal payroll duties and UI continue. |
| Worker lives elsewhere or works in multiple states | Determine income withholding in the other state and UI localization; incorporation does not decide. |
| Employee reaches $33,800 | Report covered wages; only excess wages cease producing Wyoming UI for that year. |
| Successor or acquired payroll | Do not independently reset the employee base or experience rate without DWS determination. |
| Delinquent reports/contributions | W.S.27-3-503(b) can add two percentage points to base rating, subject to maximum and cure provisions. |
| Public/nonprofit employer choosing reimbursement | Contribution-rate examples do not apply; analyze W.S.27-3-509. |

Sources: [27-3-503, 507, 509](https://www.wyoleg.gov/statutes/compress/title27.pdf), [official text](https://dws.wyo.gov/dws-division/unemployment-insurance/employers/unemployment-tax-rates/).

## Worked cases

**Case 1.** A hypothetical employer has a full notice rate of 2.00% and one employee paid $40,000 in covered 2026 wages. Taxable wages stop at $33,800, so annual UI is **$676**, paid by the employer. The 2.00% is a client notice assumption, not a claimed statewide new-employer rate.

```oa-check
name: WY 2026 annual UI base
inputs:
  covered_wages: 40000
  notice_rate: 0.02
steps:
- taxable: min(covered_wages, 33800)
- tax: taxable * notice_rate
expected:
  taxable: 33800
  tax: 676
```

**Case 2, a cap decision.** At an assumed full 2.00% rate and current-quarter wages $6,000, prior wages $32,000 leave $1,800 taxable and **$36** UI. With prior wages $20,000 instead, all $6,000 is taxable and **$120** UI. Both branches report $6,000 gross wages.

```oa-check
name: WY cap branch comparison
inputs:
  current: 6000
  prior_high: 32000
  prior_low: 20000
  notice_rate: 0.02
steps:
- base_high: min(current, max(33800 - prior_high, 0))
- base_low: min(current, max(33800 - prior_low, 0))
- tax_high: base_high * notice_rate
- tax_low: base_low * notice_rate
expected:
  base_high: 1800
  base_low: 6000
  tax_high: 36
  tax_low: 120
```


## When to refuse or refer

Refer disputed worker coverage, owners/family members, interstate localization, successors, benefit charges, rate appeals and reimbursing public/nonprofit employers. An absent rate notice blocks a final tax computation; do not insert a vendor estimate.

## Filing and payment

Reports and taxes are due April 30, July 31, October 31 and January 31 for the preceding quarter. DWS moves weekend/holiday dates to the next business day, so 2026 quarters end with deadlines April 30, July 31, November 2, 2026 and February 1, 2027. Source: [official text](https://dws.wyo.gov/dws-division/unemployment-insurance/employers/reporting-due-dates/).

Past-due contributions bear 2% monthly or fraction-of-month interest under W.S.27-3-510(a). Delinquent reports can affect the assigned rate as described above. Use WYUI to amend reporting errors, review notices and request closure; do not assume inactivity closes the account. Source: [27-3-503 and 510](https://www.wyoleg.gov/statutes/compress/title27.pdf), [official text](https://dws.wyo.gov/dws-division/unemployment-insurance/wyui/).

## Completion checklist

- Confirm coverage, work locations and full notice rate.
- Reconcile each employee's 2026 wage-base history.
- Retain quarterly report acceptance and payment records.
- Keep federal, Wyoming UI and workers compensation liabilities separate.

## Sources

| Source | URL | Read on |
| --- | --- | --- |
| DWS UI wage base table. Read for the 2026 $33,800 row and adjacent 2025 row; opened through web reader after direct download returned 403. | https://dws.wyo.gov/dws-division/unemployment-insurance/wyui/unemployment-taxable-wage-base/ | 2026-11-13 |
| DWS unemployment tax rates. Read for industry/new-employer rule, four adjustment factors and registration default; web reader after direct-download 403. | https://dws.wyo.gov/dws-division/unemployment-insurance/employers/unemployment-tax-rates/ | 2026-11-13 |
| DWS reporting dates. Read for quarterly deadlines and weekend/holiday adjustment; web reader after direct-download 403. | https://dws.wyo.gov/dws-division/unemployment-insurance/employers/reporting-due-dates/ | 2026-11-13 |
| DWS employer services and WYUI. Read for employer report, payment, rate-notice and closure functions. | https://dws.wyo.gov/dws-division/unemployment-insurance/wyui/ | 2026-11-13 |
| Wyoming Statutes Title 27. Read for 27-3-502, 503, 507, 509 and 510: coverage, rate rules, employee deduction ban and delinquency. | https://www.wyoleg.gov/statutes/compress/title27.pdf | 2026-11-13 |
| Wyoming Retirement System state withholding form. Read for Wyoming residents excluded from state-income-tax withholding form. | https://retirement.wyo.gov/wp-content/uploads/State-Tax-Withholding-Change-Form.pdf | 2026-11-13 |

Not yet confirmed: Published numerical 2026 industry-rate tables and the four adjustment-factor values were not confirmed; the actual full DWS rate notice is required. Exact current authenticated WYUI screen labels and special-employer coverage/exclusion computations are not reproduced; use the DWS-linked employer reporting instructions.
