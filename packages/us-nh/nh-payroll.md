---
name: nh-payroll
description: >
  New Hampshire employer payroll in 2026: no state wage withholding, UI registration, USD 14,000 wage base, 1.7% new-employer net rate for all four quarters, merit-rating adjustments, quarterly WebTax reporting and penalties.
jurisdiction: US-NH
category: payroll
tax_year: 2026
tier: 2
last_updated: 2026-11-13
version: "0.2"
type: filing-howto
domain: tax
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
depends_on:
  - us-form-941-940-payroll
  - nh-bpt-bet
---

# New Hampshire payroll withholding and unemployment insurance, 2026

> **Source-cited draft.** Built from NH Employment Security (NHES) employer pages, its published 2026 quarterly rate chart, Employer Handbook and RSA 282-A, read 2026-11-13. No accountant has reviewed this skill. General reference only; have a qualified professional review filing outputs and worker classification. Circular 230 section 10.37 requires the actual work, wage and rate-notice facts.

**Answer first.** New Hampshire has no state personal wage-income withholding. Employers still register and pay employer-only unemployment insurance. The first USD 14,000 per employee per calendar year is taxable; a newly established account pays a net **1.7% in each 2026 quarter**, subject to its actual account determination. Federal withholding, FICA and FUTA belong in `us-form-941-940-payroll`.

## Scope

Ordinary private employers with New Hampshire covered employment, including corporations paying owner wages. This covers the absence of NH wage withholding and the state's UI registration, base, rates, return, payment and enforcement workflow. Business-level BPT/BET compensation belongs in `nh-bpt-bet` and is not withheld from employees.

## Ask the client first

1. When did NH employment begin, and was another employer's business or workforce acquired?
2. Where does each worker actually work, and where are the base of operations and direction/control?
3. What do the liability determination, merit-rate letter and each quarter's WebTax screen show?
4. What are gross wages and calendar-year wages already paid to each worker by this employer?
5. Are workers employees, corporate officers, proprietors/partners, household/agricultural staff, or claimed independent contractors?
6. Are earlier reports or payments missing, and is the account eligible for the fund-balance reduction?

## The method, step by step

### Rates, bands and thresholds

| Item | 2026 amount or condition | Official source |
|---|---|---|
| UI taxable wage base | First USD 14,000 paid to each employee in a calendar year; employer tax, never deducted from wages | [RSA 282-A:69 I](https://gc.nh.gov/rsa/html/XXIII/282-A/282-A-69.htm) |
| New-account base rate | 2.7%, adjusted by the applicable quarter's fund-balance reduction | [NHES employer taxes](https://www.nhes.nh.gov/employers/employer-claims-taxes) |
| Fund-balance reduction, all four 2026 quarters | 1.00 percentage point for eligible positive-rated employers; new accounts use the published reduction | [NHES 2026 quarterly chart and Q4 conditions](https://www.nhes.nh.gov/employers/employer-claims-taxes/tax-rate-chart) |
| Net new-account rate, Q1 to Q4 2026 | 2.7% minus 1.0% = 1.7% | [NHES rate FAQs](https://www.nhes.nh.gov/employers/employer-claims-taxes/tax-rate-faqs), [quarterly chart](https://www.nhes.nh.gov/employers/employer-claims-taxes/tax-rate-chart) |
| Minimum adjusted positive merit rate | 0.1%; reduction requires good standing | [NHES rate FAQs](https://www.nhes.nh.gov/employers/employer-claims-taxes/tax-rate-faqs) |
| Merit schedule range before fund adjustments | 0.1% to 7.0%; the account notice determines the applicable rate | [NHES Employer Handbook, printed pp. 8-9](https://mm.nh.gov/files/uploads/nhes/documents/nhes0041.pdf) |
| Negative-rated surcharge, all 2026 quarters | Add 0.50 percentage point to Schedule II/III rate; do not subtract the positive-account reduction | [NHES quarterly chart](https://www.nhes.nh.gov/employers/employer-claims-taxes/tax-rate-chart) |
| Emergency surcharge, all 2026 quarters | 0.00% | [NHES quarterly chart](https://www.nhes.nh.gov/employers/employer-claims-taxes/tax-rate-chart) |
| Administrative contribution allocation | 0.1% minimum to 0.4% maximum within the net tax, not an extra charge; NHES illustrates 1.7% = 0.4% AC + 1.3% UI | [NHES FAQs](https://www.nhes.nh.gov/employers/employer-claims-taxes/tax-rate-faqs), [chart](https://www.nhes.nh.gov/employers/employer-claims-taxes/tax-rate-chart) |
| Ordinary UI coverage | Employment in 20 different weeks, or USD 1,500 wages in any calendar quarter; other coverage and succession tests also apply | [Employer Handbook, printed p. 2](https://mm.nh.gov/files/uploads/nhes/documents/nhes0041.pdf) |
| Employer status report | Within 30 days of first NH employment or acquiring an existing employer's assets/unit | [NHES registration](https://www.nhes.nh.gov/employers/register-your-company-nh) |
| Quarterly report and payment | Last day of month after quarter; handbook allows two extra days for WebTax report filing, not a general payment extension | [Employer Handbook, printed pp. 7, 11](https://mm.nh.gov/files/uploads/nhes/documents/nhes0041.pdf) |
| Late contributory-employer report | Greater of 10% of contributions due or USD 25 | [RSA 282-A:142 I](https://gc.nh.gov/rsa/html/XXIII/282-A/282-A-142.htm) |
| Late contributions | 1% per month or part until payment plus accrued interest received | [RSA 282-A:141](https://gc.nh.gov/rsa/html/XXIII/282-A/282-A-141.htm) |
| Requested filing extension | USD 50 fee; 30 days for filing, no payment extension | [RSA 282-A:142 IV](https://gc.nh.gov/rsa/html/XXIII/282-A/282-A-142.htm), [handbook p. 11](https://mm.nh.gov/files/uploads/nhes/documents/nhes0041.pdf) |

### Register and establish coverage

1. Use **Employer Registration and Reports** linked from the [NHES registration page](https://www.nhes.nh.gov/employers/register-your-company-nh) to submit the Employer Status Report. Include the legal employer, ownership/entity details, first-employment date, wage/week history and predecessor/acquisition facts. Retain the submission.
2. NHES determines liability and establishes the account. Do not equate a federal S election with UI exemption. The handbook excludes proprietors and partners from their own employee wages; corporate owner/officer services need their actual coverage determination.
3. Apply the NH UI ABC test under [RSA 282-A:9 III](https://gc.nh.gov/rsa/html/XXIII/282-A/282-A-9.htm): freedom from control; service outside the usual course **or** outside all business places; and an independently established trade. All three limbs must be met. A federal contractor label alone is insufficient.
4. For interstate employees, apply localization first, then base of operations, direction/control and residence as set out in [RSA 282-A:9 I-II](https://gc.nh.gov/rsa/html/XXIII/282-A/282-A-9.htm). Do not duplicate UI contributions where another state requires them. Obtain an agency determination for unresolved cases.

### Compute each quarter

5. Report total gross covered wages per worker, including wages above the taxable base. For each employee, taxable current-quarter wages = the smaller of this quarter's covered wages and the positive remainder of the calendar-year base. Add employee amounts. Do not cap the employer's whole payroll at USD 14,000.
6. Read the applicable quarter's actual net rate. New accounts use the base less the quarterly reduction. For merit accounts, the annual determination period runs July 1 to June 30, while fund adjustments can change quarterly. The 2026 FAQ says the new merit letters cover July 1, 2026 through June 30, 2027. Late reports or account imbalance can disqualify a reduction.
7. Multiply taxable wages by the UI and AC components shown by NHES. Add them once. AC is an allocation of the displayed net rate; do not add another 0.4% to a 1.7% net rate.

### Submit and pay

8. Follow **Taxes, Wages, and Reports** from the NHES registration page into WebTax. Log in using the employer account; set up NHUIS access if needed. Select the quarter and the Employer Quarterly Tax and Wage Report.
9. Complete the **wage report (Part 2)** with employee identifying information and gross wages. Bring its total into the **tax report (Part 1)**, deduct excess wages over each employee's annual base and confirm net taxable wages, UI/AC rates and charges. Both parts must be complete. Use the authorized upload specification for bulk wages; old media/employee-count limits are not a current electronic-filing specification.
10. Review total tax, interest/fees and prior balance/credit. Submit the report, retain its confirmation, authorize payment through the available EFT option and retain the payment reference separately. A filing confirmation alone is not proof of payment.
11. File every quarter after liability is established, including zero-wage quarters unless NHES grants a waiver. Correct mistakes with the Tax and Wage Report Adjustment process described in the handbook. Keep payroll records for at least six years after the calendar year wages were paid or due (handbook p. 1).

## Boundary and exception table

| Situation | Treatment |
|---|---|
| Household employment | Handbook coverage begins at USD 1,000 cash wages in a calendar quarter; refer special exclusions |
| Agricultural labor | Handbook tests USD 20,000 in a quarter or 10 workers in 20 weeks; refer special facts |
| Nonprofit/public employer | May reimburse instead of contribute; this skill's rate computation is for contributory employers |
| Sole proprietor/partner working in own business | Not an employee for ordinary UI under handbook; distinguish a corporate officer |
| Claimed independent contractor | Apply all ABC limbs, not just contract wording |
| NH residence, work in another state | No NH wage tax does not settle other-state withholding or UI location |

Sources for these exceptions: [NHES Employer Handbook, pp. 1-4](https://mm.nh.gov/files/uploads/nhes/documents/nhes0041.pdf), [RSA 282-A:9](https://gc.nh.gov/rsa/html/XXIII/282-A/282-A-9.htm).

## Worked cases

**Case 1, annual cap with two workers.** A new employer's first employee earns USD 10,000 in Q1 and USD 10,000 in Q2; the second first earns USD 6,000 in Q2. Q2 taxable wages are USD 4,000 plus USD 6,000 = USD 10,000. At the published 1.7% new-account rate, Q2 tax is USD 170, split USD 130 UI and USD 40 AC using NHES's illustrated allocation. The USD 6,000 excess wages are still reported as gross wages.

```oa-check
name: NH new employer quarter and annual cap, 2026
inputs:
  wage_base: 14000
  worker_one_prior: 10000
  worker_one_current: 10000
  worker_two_current: 6000
steps:
  - worker_one_taxable: min(worker_one_current, max(wage_base - worker_one_prior, 0))
  - worker_two_taxable: min(worker_two_current, wage_base)
  - total_taxable: worker_one_taxable + worker_two_taxable
  - ui: total_taxable * 0.013
  - ac: total_taxable * 0.004
  - total: ui + ac
expected:
  worker_one_taxable: 4000
  total_taxable: 10000
  ui: 130
  ac: 40
  total: 170
```

**Case 2, decide whether to use a displayed reduction.** On USD 20,000 of taxable payroll a positive merit account with a 2.7% base and established eligibility pays USD 340 after the one-point reduction. A negative Schedule II account with a 3.0% base pays USD 700 after the half-point inverse surcharge. Subtracting the positive reduction from that negative account would underpay USD 300. These are alternative account determinations, not an election by the employer.

```oa-check
name: NH positive reduction versus negative surcharge
inputs:
  payroll: 20000
steps:
  - positive_net: 0.027 - 0.01
  - negative_net: 0.03 + 0.005
  - positive_tax: payroll * positive_net
  - negative_tax: payroll * negative_net
  - wrong_negative_tax: payroll * (0.03 - 0.01)
  - shortfall: negative_tax - wrong_negative_tax
expected:
  positive_tax: 340
  negative_tax: 700
  shortfall: 300
```

## When to refuse or refer

Refer disputed worker classification, successorship, employee-leasing, multistate localization and nonprofit reimbursement elections to a qualified professional/NHES determination. Do not create a personal wage-tax withholding account merely because UI registration is required. Federal payroll amounts remain in `us-form-941-940-payroll`.

## Filing and payment

For 2026 wages the ordinary quarter-end filing/payment deadlines are April 30, July 31, October 31 and January 31 following the year. Use the due date displayed on the actual report for weekends/holidays. The handbook's WebTax report-filing grace period does not extend payment. File and pay by the ordinary deadline where possible; save each receipt.

## Completion checklist

- Liability and employer account established; acquisitions disclosed.
- Every worker classified and UI state determined.
- Employee annual base applied individually, with gross wages still reported.
- Correct merit period and quarterly net rate; AC not added twice.
- Both report parts submitted, payment reference retained, zero quarters addressed.
- Federal payroll handled through its separate owner skill.

## Sources

| Source | URL | Read on |
|---|---|---|
| NHES Employer Claims & Taxes. Read for employer-only UI reporting, wage base, new-account base and the WebTax/NHUIS distinction. | https://www.nhes.nh.gov/employers/employer-claims-taxes | 2026-11-13 |
| NHES Tax Rate Chart. Read for all Q1-Q4 2026 rows, compliance conditions and the 1.7% UI/AC allocation example. | https://www.nhes.nh.gov/employers/employer-claims-taxes/tax-rate-chart | 2026-11-13 |
| NHES Tax Rate FAQs. Read for the July-June merit period, quarterly adjustments, good standing, new accounts and AC allocation. | https://www.nhes.nh.gov/employers/employer-claims-taxes/tax-rate-faqs | 2026-11-13 |
| NHES Register Your Company. Read for the 30-day registration rule, acquisition reporting, liability determination and return links. | https://www.nhes.nh.gov/employers/register-your-company-nh | 2026-11-13 |
| NHES Employer Handbook. Read printed pp. 1-11 for coverage, ABC test, localization, records, wage/base calculations, Part 1/2 reporting, due dates and grace/extension limits. Undated older handbook; current rate chart overrides historical rates and AC examples. | https://mm.nh.gov/files/uploads/nhes/documents/nhes0041.pdf | 2026-11-13 |
| RSA 282-A:9. Read for localization, other-state contributions, ABC test and excluded service classes. | https://gc.nh.gov/rsa/html/XXIII/282-A/282-A-9.htm | 2026-11-13 |
| RSA 282-A:69. Read for USD 14,000 base, employer liability and prohibition on deducting UI from employee wages. | https://gc.nh.gov/rsa/html/XXIII/282-A/282-A-69.htm | 2026-11-13 |
| RSA 282-A:141 and 142. Read for monthly interest, report penalties and filing extension fee. | https://gc.nh.gov/rsa/html/XXIII/282-A/282-A-141.htm ; https://gc.nh.gov/rsa/html/XXIII/282-A/282-A-142.htm | 2026-11-13 |

Not yet confirmed: a current public WebTax upload specification and current electronic employee-count limit, precise current screen/field labels beyond the published Part 1/Part 2 report, the continued two-day online filing grace in a 2026-specific publication, and any voluntary paid-leave insurance arrangement for the employer. Do not treat the older handbook as confirmation of a mandatory paid-leave payroll contribution. Actual account rates and holiday-adjusted dates must come from the issued report. No accountant has approved this skill.
