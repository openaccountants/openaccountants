---
name: gh-payroll-social
description: >
  Use this skill to run or review Ghana payroll for tax year 2026. It covers the three-tier pension scheme, the 18.5% mandatory contribution split between employer 13% and employee 5.5%, Tier 1 at 13.5% to SSNIT and Tier 2 at 5%, the 2026 minimum and maximum insurable earnings, PAYE deductions and the new bands from 1 September 2026, bonus at 5% up to 15% of basic, overtime, casual and temporary workers, non-residents, benefits in kind, forms DT 107 and DT 108 on ETAX, and year-end checks. Trigger on "Ghana payroll", "SSNIT", "Tier 2", "PAYE return Ghana", "maximum insurable earnings", "bonus tax Ghana". The bands live in ghana-pit.
version: 0.2
jurisdiction: GH
category: payroll
tax_year: 2026
last_updated: 2026-11-01
review_status: pending_review
trust_label: Built by Michael Cutajar and the OpenAccountants team
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Ghana Payroll and Social Contributions v0.2

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

Tax year: 2026. Law: National Pensions Act, 2008 (Act 766); Income Tax Act, 2015 (Act 896) as amended. The income tax bands are in [ghana-pit](ghana-pit.md).

## Who this applies to

Every employer with at least one worker; registration of workers with SSNIT is mandatory ([SSNIT](https://www.ssnit.org.gh/faqs/)). The self-employed may join voluntarily. The PAYE duty covers all employment income in cash or kind ([GRA](https://gra.gov.gh/domestic-tax/tax-types/paye/)).

## Rates, bands and thresholds

| Item | Figure | Conditions | Tax year | Official URL |
|---|---|---|---|---|
| Employee | 5.5% of basic salary | Deducted before PAYE | 2026 | https://www.ssnit.org.gh/faqs/ |
| Employer | 13% of basic salary | On top of pay | 2026 | same |
| Total | 18.5% | Tier 1 plus Tier 2 | 2026 | same |
| Tier 1 to SSNIT | 13.5% | 2.5 points of it go to the NHIA | 2026 | same |
| Tier 2 to approved trustee | 5% | Occupational scheme | 2026 | same |
| Tier 3 | Voluntary | Deductible up to 16.5% of basic, employer and employee together | 2026 | https://gra.gov.gh/domestic-tax/tax-types/paye/ |
| Maximum insurable earnings | GHS 69,000 a month | From 1 January 2026 (2025: 61,000) | 2026 | https://www.ssnit.org.gh/wp-content/uploads/2026/01/Public-Notice-Min-Max-Insurable.pdf |
| Minimum insurable earnings | GHS 587.80 a month | From 1 January 2026 (was 539.19) | 2026 | same |
| Maximum SSNIT contribution | GHS 9,315.00 | Notice figure | 2026 | same |
| Minimum SSNIT contribution | GHS 79.40 | Notice figure | 2026 | same |
| Bonus | 5% up to 15% of annual basic | Excess goes in employment income at graduated rates | 2026 | https://gra.gov.gh/domestic-tax/tax-types/paye/ |
| Overtime, junior staff | 5% up to 50% of monthly basic; 10% on the excess | Qualifying income up to GHS 18,000 | 2026 | same |
| Non-resident employee bonus or overtime | 20% | Flat | 2026 | same |
| Casual worker | 5% | Seasonal or intermittent, not over six continuous months, paid daily | 2026 | same |
| Non-resident employee | 25% flat | Chargeable income | 2026 | same |
| Vehicle with driver and fuel | 12.5% of cash emoluments, cap GHS 1,500 a month | Benefit value | 2026 | https://gra.gov.gh/wp-content/uploads/2023/04/INCOME-TAX-AMENDMENT-ACT-2023-ACT-1094.pdf |
| Vehicle with fuel | 10%, cap GHS 1,250 a month | Benefit value | 2026 | same |
| Vehicle only | 5%, cap GHS 625 a month | Benefit value | 2026 | same |
| Fuel only | 5%, cap GHS 625 a month | Benefit value | 2026 | same |

## The base

1. Gross up cash pay: basic plus allowances such as transport, rent, risk, night duty, responsibility, child education, house help, cook and garden boy.
2. Add benefits in kind at their value. Accommodation and loan benefits follow the Fourth Schedule of Act 896.
3. Deduct employee SSNIT of 5.5% of basic, up to the ceiling; Tier 3 up to the 16.5% limit; mortgage interest on one home; worthwhile-cause donations.
4. Deduct reliefs shown on a current relief card.
5. Apply monthly bands. Use the old bands for pay to August 2026 and the new ones from September.
6. Apply flat rates to bonus and overtime separately. Unlike a bonus, overtime is not added to basic.

Temporary workers, employed for at least a month, are taxed as other employees.

## Deadlines and filing

| Obligation | Date | Official URL |
|---|---|---|
| Monthly PAYE return and payment, DT 107 with DT 107A | 15th of the next month | https://gra.gov.gh/domestic-tax/tax-types/paye/ |
| Tier 1 to SSNIT | Within 14 days after the month end | https://www.ssnit.org.gh/faqs/ |
| Annual PAYE, DT 108, DT 108A, DT 108B | 30 April | https://gra.gov.gh/wp-content/uploads/2025/11/Taxpayer-Checklist.pdf |
| Engaged and leavers schedules, DT 107B, DT 107C | With the monthly return, as form DT 107 directs | https://gra.gov.gh/domestic-tax/tax-types/paye/ |

**Monthly run:**

1. Compute pay; deduct 5.5% employee and PAYE.
2. On ETAX (www.etax.gra.gov.gh), open the PAYE return for the period. Enter staff numbers, cash emoluments and tax for Expatriate/Management and Others. Upload the DT 107A employee schedule, and DT 107B, DT 107C if staff moved. If nothing was paid, tick NIL.
3. Submit, keep the acknowledgement, pay through Ghana.gov by the 15th.
4. In the SSNIT employer portal, submit the contribution report, generate the payment advice and pay 13.5% within 14 days ([SSNIT](https://www.ssnit.org.gh/faqs/)).
5. Send 5% to the Tier 2 trustee, and any Tier 3.

**Year end ([GRA checklist](https://gra.gov.gh/wp-content/uploads/2025/11/Taxpayer-Checklist.pdf)):** every employee has a TIN, Social Security number and Ghana Card; new-hire and disengagement forms filed; relief cards renewed; twelve months of PAYE and Tier 1, 2, 3 returns filed and paid.

## Penalties and interest

| Failure | Consequence | Official URL |
|---|---|---|
| Late PAYE return | GHS 500 plus GHS 10 a day | https://gra.gov.gh/wp-content/uploads/2023/01/Revenue-Administration-Act-2016-.pdf |
| Late PAYE payment | 125% of the Bank of Ghana policy rate, compounded monthly | same |
| Failing to withhold | The withholding agent is liable for the tax | https://gra.gov.gh/domestic-tax/tax-types/withholding-tax/ |

## Cross-border points

- Non-resident employees pay 25% flat; bonus and overtime 20%.
- Residence tests are in [ghana-pit](ghana-pit.md).
- Pay of employees without a TIN or SSNIT number leaves exposure to taxes, pension contributions and penalties ([GRA](https://gra.gov.gh/wp-content/uploads/2025/11/Taxpayer-Checklist.pdf)).

## Two worked examples that recompute

**Example 1: employee, September 2026.** Basic GHS 10,000, no allowances. Employee SSNIT 550, employer 1,300, total 1,850: Tier 1 1,350 and Tier 2 500. Chargeable 9,450. PAYE is 521.50 plus 25% of 5,782, or 1,445.50: GHS 1,967.

```oa-check
name: Basic 10,000, September 2026
inputs:
  basic: 10000
steps:
  - employee: basic * 0.055
  - employer: basic * 0.13
  - tier1: basic * 0.135
  - tier2: basic * 0.05
  - chargeable: basic - employee
  - paye: 80 * 0.05 + 100 * 0.10 + 2900 * 0.175 + (chargeable - 3668) * 0.25
expected:
  tier1: 1350.00
  tier2: 500.00
  paye: 1967.00
```

**Example 2: should a GHS 150,000 bonus be split?** Annual basic GHS 800,000. The 15% limit is 120,000, taxed at 5%: GHS 6,000. The excess of 30,000 joins employment income, here at 30%: GHS 9,000. Total GHS 15,000. Keeping the bonus within 120,000 costs GHS 6,000, so each cedi over the limit costs the marginal rate rather than 5%.

```oa-check
name: Bonus above the 15% limit
inputs:
  basic: 800000
  bonus: 150000
steps:
  - limit: basic * 0.15
  - low: min(bonus, limit) * 0.05
  - excess: max(bonus - limit, 0) * 0.30
  - total: low + excess
expected:
  limit: 120000.00
  total: 15000.00
```

## Ask the client first

1. Resident or not, and citizen or not, for each worker.
2. Basic salary against allowances.
3. Junior or senior staff, permanent, temporary or casual.
4. Benefits in kind.
5. Relief cards.
6. Tier 2 trustee and any Tier 3 scheme.

## Sources

| Source | URL | Read on |
|---|---|---|
| SSNIT FAQs (contribution rates and remittance), page read in full | https://www.ssnit.org.gh/faqs/ | 2026-11-01 |
| SSNIT Public Notice, 13 Jan 2026, whole notice | https://www.ssnit.org.gh/wp-content/uploads/2026/01/Public-Notice-Min-Max-Insurable.pdf | 2026-11-01 |
| GRA, PAYE page (2026 bands, bonus, overtime, casual rules read) | https://gra.gov.gh/domestic-tax/tax-types/paye/ | 2026-11-01 |
| Income Tax (Amendment) Act, 2023 (Act 1094), whole act | https://gra.gov.gh/wp-content/uploads/2023/04/INCOME-TAX-AMENDMENT-ACT-2023-ACT-1094.pdf | 2026-11-01 |
| Revenue Administration Act, 2016 (Act 915); ss 27 to 30, 46, 47, 70 to 73 read | https://gra.gov.gh/wp-content/uploads/2023/01/Revenue-Administration-Act-2016-.pdf | 2026-11-01 |
| GRA, Employee Taxes and Pensions Year End Checklist, whole document | https://gra.gov.gh/wp-content/uploads/2025/11/Taxpayer-Checklist.pdf | 2026-11-01 |
| GRA, Withholding Tax page (rates table, last edited 2022), page read in full | https://gra.gov.gh/domestic-tax/tax-types/withholding-tax/ | 2026-11-01 |

Not yet confirmed: (1) Section 63(3) of Act 766 and the Act 766 penalties for late contributions were not opened; no SSNIT penalty is stated. Act 766 was not on a site opened. (2) Notice minimum of GHS 79.40 is above 13.5% of 587.80, which is 79.35; the notice is quoted. (3) Whether the 5.5% tax deduction stops at the ceiling is inferred from the contribution cap, not read in the law. (4) Tier 2 due date: not on any official page read. The old version had the 14th as approximate for SSNIT; SSNIT confirms 14 days. (5) Bonus and overtime rates come from the GRA page, not Act 896 as amended. (6) Whether the GHS 18,000 overtime qualifying limit changed under Act 1178.

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
