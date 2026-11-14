---
name: wv-payroll
description: "West Virginia payroll withholding and unemployment (2026), tax year 2026: applicability, state computations, exceptions, registration, returns, payment and source-backed worked cases."
jurisdiction: US-WV
category: payroll
domain: tax
tax_year: 2026
tier: 2
last_updated: 2026-11-14
version: "1.1"
type: situation-rules
---

# West Virginia payroll withholding and unemployment (2026)

**Circular 230 §10.37 disclosure:** This skill supplies general state-tax working papers from the sources below. It is not a professional approval. A qualified tax professional must review the facts, assumptions and outputs before filing.

**Answer first:** Register separately for West Virginia wage withholding and UI. Withholding uses the March 2026 IT-100.2A tables and IT-104; UI uses the employee's remaining $9,500 annual wage base and the employer's applicable rate notice. A July 1, 2026 law changes UI contributions and creates a separate automation fee, so an older rate statement alone is insufficient. [IT-100.2A](https://tax.wv.gov/Documents/Withholding/it100.2a.pdf); [§21A-1A-28](https://code.wvlegislature.gov/21A-1A-28/); [§21A-5-5](https://code.wvlegislature.gov/21A-5-5/); [§21A-9-10](https://code.wvlegislature.gov/21A-9-10/).

## Scope

West Virginia employers in tax year 2026: state income-tax withholding and unemployment insurance, registration, periodic reports and payments. Federal FICA/FUTA, deposit schedules and Forms 941/940 belong to `us-form-941-940-payroll`; do not copy their figures here. This skill is partial for the new UI fee implementation and a complete current experience-rate schedule, identified below.

## Ask the client first

1. Work location by day, employee residence, reciprocity certificates and any multi-state employment?
2. IT-104 exemptions, single/multiple jobs, spouse employment and payroll frequency?
3. Gross pay, pretax items and the year-to-date wages for each employee and any predecessor employer?
4. Employer withholding/UI account numbers, notices, filing frequency and any acquisition or construction activity?
5. Current 2026 UI rate notices, July changes and automation-fee assessment?
6. Employees vs owners/contractors, nonprofit/government status, and prior returns/payments?

## The method, step by step

### Rates, bands and thresholds

| Item | Amount or rule | Official source |
| --- | --- | --- |
| 2026 wage withholding | Use the applicable IT-100.2A percentage table or IT-100.2B table method, with IT-104 election | [March 2026 IT-100.2A pp.1-4](https://tax.wv.gov/Documents/Withholding/it100.2a.pdf) |
| One-job monthly allowance | $166.67 per exemption; subtract before table calculation | [IT-100.2A p.4, Table 4](https://tax.wv.gov/Documents/Withholding/it100.2a.pdf) |
| One-job monthly taxable wages through $833 | 2.11% | [IT-100.2A p.4](https://tax.wv.gov/Documents/Withholding/it100.2a.pdf) |
| One-job monthly over $833 through $2,083 | $17.58 + 2.81% of excess over $833 | [IT-100.2A p.4](https://tax.wv.gov/Documents/Withholding/it100.2a.pdf) |
| One-job monthly over $2,083 through $3,333 | $52.70 + 3.16% of excess over $2,083 | [IT-100.2A p.4](https://tax.wv.gov/Documents/Withholding/it100.2a.pdf) |
| One-job monthly over $3,333 through $5,000 | $92.20 + 4.22% of excess over $3,333 | [IT-100.2A p.4](https://tax.wv.gov/Documents/Withholding/it100.2a.pdf) |
| One-job monthly over $5,000 | $162.55 + 4.58% of excess over $5,000 | [IT-100.2A p.4](https://tax.wv.gov/Documents/Withholding/it100.2a.pdf) |
| UI wage base | $9,500 per employee/calendar year; predecessor and covered other-state wages can count | [§21A-1A-28(b)(1)](https://code.wvlegislature.gov/21A-1A-28/) |
| New-employer statutory contribution before July change | 2.7% until eligible for experience rating; foreign construction entities 7.5% statutory base, with other applicable assessments to be reconciled (in words on the page) | [§21A-5-5(b)-(c)](https://code.wvlegislature.gov/21A-5-5/) |
| UI change effective July 1, 2026 | Statute reduces otherwise applicable contribution rate by seven percent, floor zero; use agency implementation and actual notice | [§21A-5-5(d)](https://code.wvlegislature.gov/21A-5-5/) |
| Automation fee from July 1, 2026 | Separate annual fee; zero-rate employers excepted; agency may reduce statutory percentage; do not treat the contribution reduction as total employer savings | [§21A-9-10(c)](https://code.wvlegislature.gov/21A-9-10/) |
| Withholding monthly remittance | 15th of succeeding month; IT-101Q quarterly by last day after quarter | [TSD 381](https://tax.wv.gov/Documents/TSD/tsd381.pdf) |
| UI report/payment | Quarterly: April 30, July 31, October 31, January 31; next business day if applicable | [WorkForce reporting; handbook p.15](https://workforcewv.org/businesses/unemployment-tax-information/tax-filing-reporting/) |

### Register and choose the withholding calculation

1. Register the business and its employer-tax accounts through the West Virginia One Stop business portal, https://business4.wv.gov, and complete the Employer's Initial Statement for WorkForce. Keep the separate withholding and UI identifiers. The agency determines UI coverage and initial rate; do not use a sales-tax account number as a UI account. [WorkForce handbook pp.5-6](https://workforcewv.org/wp-content/uploads/2024/06/Employer-Handbook-Rev.-06.24.pdf).
2. Obtain signed IT-104 and retain reciprocity/low-income elections. Identify taxable compensation: wages, salaries, commissions, bonuses, vacation/back pay, tips and other remuneration for services. Apply the actual state treatment of pretax benefits rather than deducting every payroll deduction from taxable pay. [TSD 381](https://tax.wv.gov/Documents/TSD/tsd381.pdf).
3. Select the IT-100.2A payroll period and either the two-earner/multiple-jobs tables (pp.1-2) or optional one-earner/one-job tables (pp.3-4). Subtract the per-exemption period amount, floor taxable wage at zero, and apply the applicable bracket. Do not use the optional one-job schedule for a multiple-job employee without the required facts. The source has weekly, biweekly, semimonthly, monthly, annual and daily tables. [IT-100.2A](https://tax.wv.gov/Documents/Withholding/it100.2a.pdf).
4. Reconcile tax withheld per employee to the register and tax account. The annual income-tax schedule in `wv-income-tax` is not a substitute for rounded period withholding tables.

### Cross-border withholding

A valid IT-104 can document Kentucky, Maryland, Ohio, Pennsylvania or Virginia resident wage reciprocity. A nonresident employee's short visits are not automatically exempt: TSD 381 requires duties in WV for 30 days or less, duties in more than one state, no professional-athlete/entertainer/public-figure exception, and an eligible reciprocal exclusion or no-income-tax home state. Keep day-by-day attendance evidence or the permitted reasonable written estimate. Military rules have separate exceptions for specified Guard/reserve duties. Refer a military/spouse or uncertain mobile-worker case rather than generalizing the wage exception. [TSD 381](https://tax.wv.gov/Documents/TSD/tsd381.pdf).

### UI wages, rates and July change

For each employee, taxable quarter wages = smaller of current covered wages and remaining annual wage base, never below zero. Report gross and excess wages too. Do not allocate a fresh full wage base every quarter. Transfers from the same employer's other-state unemployment-covered payroll or predecessors can reduce the remaining base under [§21A-1A-28(b)(1)](https://code.wvlegislature.gov/21A-1A-28/). Owner, agricultural/domestic, nonprofit/reimbursable and employee-classification questions need their actual coverage determination.

The current statute sets ordinary new-employer contribution at 2.7% until the required 36-month period; foreign construction has a distinct statutory rate. The June 2024 handbook calls that construction initial rate 8.5%, so its total cannot be treated as identical to the bare statutory rate. Experienced/delinquent/successor rates come from the account notice, including other applicable assessments. The handbook's 2024 $9,521 base has been superseded by the amended statute's $9,500 and must not be used. [§21A-5-5](https://code.wvlegislature.gov/21A-5-5/); [§21A-1A-28](https://code.wvlegislature.gov/21A-1A-28/); [handbook pp.12-14](https://workforcewv.org/wp-content/uploads/2024/06/Employer-Handbook-Rev.-06.24.pdf).

Read the July contribution change together with the separate automation fee. Section 21A-9-10(c) uses a statutory annual fee of seven percent of the prior June-30 twelve-month taxable wages, permits the Commissioner to reduce the percentage to limit total collections, excepts zero-contribution-rate employers, and requires individual notice by March 31 with delinquency 30 days later. It also contains collection caps, fund-balance safeguards, termination events and federal-compliance limits. Do not invent an effective fee percentage from a search summary or assume the fee equals 7% of contributions. Actual agency implementation, rate rounding and fee notices remain unconfirmed. [§21A-9-10](https://code.wvlegislature.gov/21A-9-10/).

### Returns and payment

For withholding, file IT-101Q through MyTaxes at https://mytaxes.wvtax.gov, using the employer account and correct quarter; reconcile payments made with IT-101V to the payroll totals. Monthly remittance and quarterly reporting are separate obligations. TSD 381 permits IT-101A annual filing/payment for employers withholding less than $600 annually or the specified domestic/household category; obtain the assigned status. IT-101A combines the annual return and reconciliation. Otherwise reconcile W-2 state wages/tax and file IT-103 plus required wage statements by January 31 following the year, using the current specifications. [TSD 381](https://tax.wv.gov/Documents/TSD/tsd381.pdf); [withholding forms page](https://tax.wv.gov/Business/Withholding/Pages/WithholdingTaxForms.aspx).

TSD 381 says e-file is required for 10 or more employees or use of a payroll service for periods after December 31, 2024; it also gives the general $50,000 single-business-tax electronic threshold. A non-electronic information return can incur $25 per return. The 2026 W-2 specification was marked draft on the read forms page; resolve its final form before year-end transmission. [TSD 381](https://tax.wv.gov/Documents/TSD/tsd381.pdf); [forms page](https://tax.wv.gov/Business/Withholding/Pages/WithholdingTaxForms.aspx).

For UI, sign into the WorkForce Unemployment Compensation Employer System through the agency's Tax Filing & Reporting page. Select the quarter, report employee identity, gross wages, taxable wages and excess wages; reconcile the taxable-payroll total multiplied by the applicable notice rate and any separately assessed fee. Submit the Quarterly Wage and Contribution Report and pay, retaining both confirmation records. Report inactive/no-payroll status as the agency instructs instead of silently stopping. [WorkForce filing page](https://workforcewv.org/businesses/unemployment-tax-information/tax-filing-reporting/); [handbook pp.7-15](https://workforcewv.org/wp-content/uploads/2024/06/Employer-Handbook-Rev.-06.24.pdf).

## Boundary and exception table

| Situation | Treatment |
| --- | --- |
| Employee has exceeded the annual UI base | Continue gross wage reporting; no additional base reset |
| Business acquisition | Review successorship, predecessor wages and assigned rate before applying new-employer treatment |
| Nonprofit/government/public-school account | Reimbursement election can differ from contribution method; compare actual charged benefits and notice |
| Multiple jobs or both spouses employed | Use the appropriate two-earner tables; one-job table may underwithhold |
| Wage reciprocity | Does not decide UI coverage or exempt business income |
| July 2026 UI change | Reconcile contribution reduction AND separate fee; never assume net savings |

## Worked cases

**Case 1:** An eligible one-job employee earns $3,500 monthly and claims one exemption. Taxable wage is $3,333.33. Page 4 Table 4 gives $92.20 plus 4.22% of $0.33, or $92.21 to cents. If the employee has another job, switch tables: the multiple-jobs monthly schedule gives $69.15 + 4.22% of $833.33 = $104.32. The job facts determine the appropriate branch; this is not a free tax-minimization election.

```oa-check
name: WV 2026 optional one-job monthly withholding
inputs:
  gross: 3500
  allowance: 166.67
steps:
- taxable: max(gross - allowance, 0)
- one_job: 92.20 + max(taxable - 3333, 0) * 0.0422
- multiple_jobs: 69.15 + max(taxable - 2500, 0) * 0.0422
expected:
  taxable: 3333.33
  one_job: 92.21
  multiple_jobs: 104.32
```
**Case 2:** For a first-half 2026 quarter, a covered employee has $8,000 prior wages with the same employer and $4,000 this quarter. Only $1,500 remains in the $9,500 base. Assume the employer notice confirms an applicable 2.7% contribution rate for this period and no separately assessed amount in this illustration: contribution is $40.50; $2,500 is excess wages. Without prior wages the same $4,000 would produce $108. This is not a second-half fee computation.

```oa-check
name: WV UI remaining wage base before July change
inputs:
  prior: 8000
  wages: 4000
  base: 9500
  notice_rate: 0.027
steps:
- remaining: max(base - prior, 0)
- taxable: min(wages, remaining)
- excess: wages - taxable
- contribution: taxable * notice_rate
- no_prior: min(wages, base) * notice_rate
expected:
  remaining: 1500
  taxable: 1500
  excess: 2500
  contribution: 40.5
  no_prior: 108
```

## When to refuse or refer

Refer missing rate notices, second-half 2026 UI/fee implementation, construction/successor accounts, foreign or mobile work, military/spouse elections, PEOs, exempt/reimbursable entities, disputed classification and payroll corrections. UI fraud, misclassification and unpaid withholding are not routine data-entry questions.

## Filing and payment

Keep both portals' period balances, filing acceptances and payments. The UI handbook describes delinquent-report/payment consequences, but current 2026 penalty/interest rates are unconfirmed here; use the actual assessment with reviewer oversight. Keep the annual automation notice separate from quarterly UI.

## Completion checklist

- Employee elections and work locations established.
- Correct March 2026 withholding table selected.
- Annual UI base accumulated once per employee, including applicable transferred wages.
- Rate notice reconciled for the period and July law considered.
- Withholding and UI returns, payments and year-end wages tie to the register.

## Sources

| Source and reading scope | URL | Read on |
| --- | --- | --- |
| IT-100.2A, March 2026. Read for all four pages: period allowances, one/multiple-earner tables and bracket amounts. | https://tax.wv.gov/Documents/Withholding/it100.2a.pdf | 2026-11-13 |
| TSD 381, September 2025. Read for 2025-2026 filing cycle compensation, reciprocity/mobile exceptions, filing, annual treatment and e-file. | https://tax.wv.gov/Documents/TSD/tsd381.pdf | 2026-11-13 |
| Tax Division withholding forms page. Read for 2026 table links, IT-101A combined form and draft year-end specification. | https://tax.wv.gov/Business/Withholding/Pages/WithholdingTaxForms.aspx | 2026-11-13 |
| West Virginia Code §21A-1A-28. Read for amended wages definition and annual base/predecessor/other-state rules. | https://code.wvlegislature.gov/21A-1A-28/ | 2026-11-13 |
| West Virginia Code §21A-5-5. Read for new-employer statutory rates and July 2026 reduction. | https://code.wvlegislature.gov/21A-5-5/ | 2026-11-13 |
| West Virginia Code §21A-9-10. Read for fee base, adjustment power, notices, collection limits and termination. | https://code.wvlegislature.gov/21A-9-10/ | 2026-11-13 |
| WorkForce Tax Filing & Reporting. Read for quarterly submission and online payment process. | https://workforcewv.org/businesses/unemployment-tax-information/tax-filing-reporting/ | 2026-11-13 |
| WorkForce Employer Handbook, June 2024. Read for pp.5-15 registration, rate categories, wage reporting and due dates; its 2024 indexed base is not used. | https://workforcewv.org/wp-content/uploads/2024/06/Employer-Handbook-Rev.-06.24.pdf | 2026-11-13 |

Not yet confirmed: complete 2026 experience/delinquent/construction assessment schedule, July reduction implementation/rounding and actual automation-fee percentage/first assessment; final 2026 W-2 specifications, 2026 penalty/interest amounts, specialized pretax-benefit and UI coverage rules. Obtain the agency notice before final UI output; the statutory fee must not be guessed or ignored.
