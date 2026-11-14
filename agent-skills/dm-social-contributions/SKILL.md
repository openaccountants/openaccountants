---
name: dm-social-contributions
description: "Dominica Social Security (DSS) contributions for 2026. Covers the rates from 1 January 2026 (employee 6.75%, employer 8% with redundancy cover or 7.75% without), the EC$7,000 monthly insurable earnings ceiling, who is an employee without redundancy, multiple employers and refunds, the self-employed rate of 13.75% on the preceding year's income up to EC$84,000, voluntary contributors at 12.40%, payment by the 14th and the 10% late fee. Trigger phrases include Dominica social security, DSS contributions, redundancy contribution, Dominica self-employed social security."
license: "AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)"
metadata:
  source: openaccountants
  openaccountants_url: "https://www.openaccountants.com/skills/dm-social-contributions"
  jurisdiction: "DM"
  tax_year: "2026"
  last_updated: "2026-11-14"
---

# Dominica social security contributions 2026

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

## Scope

Dominica Social Security (DSS) contributions in 2026 under the Social Security Act and the Social Security (Amendment) Regulations, SROs 4, 7 and 8 of 2012, as published by DSS. Covers employees and employers, the redundancy split, the ceiling, the self-employed and voluntary contributors, and payment. Amounts are EC$. Income tax and PAYE: [dm-income-tax-paye](dm-income-tax-paye.md).

## Ask the client first

1. Is the worker an employee with redundancy cover or without (government employee, manager who has and uses authority to hire and fire, stevedore, longshoreman, domestic, or the employer's parent, spouse, sibling or child)?
2. Monthly insurable earnings with every component (salary, overtime, commission, bonus, service charge, holiday pay).
3. Does the employee have more than one employer?
4. Is the worker a non-national (work permit), a diplomat, or covered by a reciprocal agreement?
5. For the self-employed: income for the preceding year and whether the January reassessment was done.

## The method, step by step

### Rates, bands and thresholds

| Item | 2026 figure and conditions | Official source |
|---|---|---|
| Employee share, from January 2026 | 6.75% (both categories) | [DSS rate table 2012 to 2031](https://dss.dm/wp-content/uploads/2024/12/Table-of-EE-ER-Contribution-Rates-2012-2031.pdf) |
| Employer share, employee with redundancy | 8.00% (total 14.75%) | same |
| Employer share, employee without redundancy | 7.75% (total 14.50%) | same |
| Scheduled next step, from January 2027 | Employee 7.00%; employer 8.00% with and 7.75% without redundancy | same |
| Monthly insurable earnings ceiling | EC$7,000; earnings above it are not subject to contributions | [DSS FAQ](https://dss.dm/faq/) |
| Payment date | By the 14th day after the month; next working day if a weekend or public holiday | same |
| Late fee | 10% | same |
| Self-employed rate, 2026 | 13.75% of the preceding year's income, up to EC$84,000 | [DSS self-employed payment](https://dss.dm/contributors/definition-se/pmt-contrib-se/) |
| Self-employed payment | Quarterly (monthly allowed); late after the 14th day following the quarter end: 10% plus interest | same |
| Self-employed reassessment | At the DSS office by 31 January each year | same |

### Steps

1. **Register** every employee, non-nationals included (with a work permit). Only diplomats and people covered by a reciprocal agreement are exempt.
2. **Classify** the employee: with or without redundancy cover. A job title alone does not decide it.
3. **Base:** all insurable earnings, capped at EC$7,000 a month.
4. **Contributions:** employee 6.75%; employer 8% (with redundancy) or 7.75% (without).
5. **Pay** by the 14th of the next month to avoid the 10% late fee.
6. **Voluntary contributors** pay 12.40% in 2026 (DSS notice of changes for 2026, an image: [notice](https://dss.dm/wp-content/uploads/2026/01/Changes-to-Contributions-provisions-2026.png)).
7. **Multiple employers:** each deducts up to the ceiling on its own pay; the employee claims a refund of employee contributions on combined earnings over EC$7,000.

## Boundary and exception table

| Situation | Treatment | Source |
|---|---|---|
| DSS FAQ shows older combined rates | Use the January 2026 row of the rate table | [DSS rate table](https://dss.dm/wp-content/uploads/2024/12/Table-of-EE-ER-Contribution-Rates-2012-2031.pdf) |
| Manager titled "manager" with no hiring or firing authority | An employee with redundancy cover; only managers who have and exercise authority to hire and fire are without it | [DSS FAQ](https://dss.dm/faq/) |
| 14th falls on a Saturday | Pay by the next working day | same |
| Self-employed person who starts mid-year | Ask DSS for the assessed schedule; do not assume even quarters | [DSS self-employed payment](https://dss.dm/contributors/definition-se/pmt-contrib-se/) |
| Self-employed income above the cap | Contributions on EC$84,000 only | same |

## Worked cases

### Case 1: employee at and above the ceiling, with redundancy

At EC$4,000 a month: employee 270, employer 320, total 590. At EC$9,000 the base is capped at 7,000: employee 472.50, employer 560, total 1,032.50. A self-employed person with prior-year income of 60,000 pays 8,250 for 2026; at the 84,000 cap, 11,550.

```oa-check
name: DSS 2026 contributions, 4,000 and 9,000 a month, and self-employed
inputs:
  pay_low: 4000
  pay_high: 9000
  ceiling: 7000
  se_income: 60000
steps:
  - low_employee: min(pay_low, ceiling) * 0.0675
  - low_employer: min(pay_low, ceiling) * 0.08
  - high_employee: min(pay_high, ceiling) * 0.0675
  - high_employer: min(pay_high, ceiling) * 0.08
  - high_total: high_employee + high_employer
  - se_contribution: min(se_income, 84000) * 0.1375
  - se_at_cap: 84000 * 0.1375
expected:
  low_employee: 270
  low_employer: 320
  high_employee: 472.5
  high_employer: 560
  high_total: 1032.5
  se_contribution: 8250
  se_at_cap: 11550
```

### Case 2 (decision): with or without redundancy cover?

A worker earns EC$7,000 a month. If they are a manager who actually hires and fires, the employer pays 7.75% = 542.50 (total 1,015). If the title is "manager" but there is no such authority, they are an employee with redundancy and the employer pays 8% = 560 (total 1,032.50). Misclassifying costs 17.50 a month, 210 a year, plus the 10% late fee on any shortfall found later.

```oa-check
name: DSS redundancy classification at 7,000 a month
inputs:
  pay: 7000
steps:
  - employee: pay * 0.0675
  - employer_without: pay * 0.0775
  - employer_with: pay * 0.08
  - total_without: employee + employer_without
  - total_with: employee + employer_with
  - monthly_gap: employer_with - employer_without
  - yearly_gap: monthly_gap * 12
expected:
  employee: 472.5
  employer_without: 542.5
  employer_with: 560
  total_without: 1015
  total_with: 1032.5
  monthly_gap: 17.5
  yearly_gap: 210
```

## When to refuse or refer

- Benefit claims, voluntary contributor eligibility and partial-period payroll mechanics.
- Reciprocal agreement exemptions: need the agreement and a DSS certificate.
- Age transitions: not set out on the DSS pages read.

## Filing and payment

1. Register the employer and each employee with DSS.
2. Each month remit employee and employer contributions by the 14th day after the month ([DSS FAQ](https://dss.dm/faq/)).
3. Self-employed: get the yearly reassessment by 31 January and pay quarterly within 14 days after each quarter end, or monthly ([DSS self-employed payment](https://dss.dm/contributors/definition-se/pmt-contrib-se/)).
4. Keep the classification, the earnings reconciliation, the ceiling calculation and the receipt.

## Completion checklist

- Redundancy category recorded with the reason.
- Ceiling of 7,000 applied after all earnings.
- 6.75% and 8% or 7.75% applied.
- Paid by the 14th.

## Sources

| Source | URL | Read on |
|---|---|---|
| DSS table of contribution rates 2012 to 2031 (Appendix A): read for the January 2026 and January 2027 rows, with and without redundancy | https://dss.dm/wp-content/uploads/2024/12/Table-of-EE-ER-Contribution-Rates-2012-2031.pdf | 2026-11-14 |
| DSS notice, changes to contribution provisions from 1 January 2026 (image, OCR): read for SROs 4, 7 and 8 of 2012 and the 2026 rates (employer 8.00% and 7.75%, self-employed 13.75%, voluntary 12.40%) | https://dss.dm/wp-content/uploads/2026/01/Changes-to-Contributions-provisions-2026.png | 2026-11-14 |
| DSS FAQ: read for coverage, the EC$7,000 ceiling, multiple employers and refunds, insurable earnings, the without-redundancy list, payment by the 14th and the 10% late fee | https://dss.dm/faq/ | 2026-11-14 |
| DSS payment of contributions by the self-employed: read for the 13.75% rate, the EC$84,000 cap, the 31 January reassessment, quarterly payment and the late fee | https://dss.dm/contributors/definition-se/pmt-contrib-se/ | 2026-11-14 |

Not yet confirmed: the text of SROs 4, 7 and 8 of 2012 (not opened); interest on late payment; age limits for contributions; the voluntary contributor base.

## Today's figures and who stands behind this skill

This file is an AI skill (tax rules your AI follows) from OpenAccountants, copied on 2026-11-14. Rates, thresholds and deadlines change. For the current version of this skill, its official sources and the named accountant (if any) who stands behind it, call `get_skill` with slug `dm-social-contributions` on the OpenAccountants connector (https://www.openaccountants.com/connect), or read https://www.openaccountants.com/skills/dm-social-contributions. If neither is available, confirm every figure against the official source pages cited above before relying on it.
