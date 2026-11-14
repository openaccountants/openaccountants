---
name: ks-social-contributions
description: "Compute Kansas 2026 employer unemployment contributions using the verified 15100 dollar wage base, statutory new nonconstruction 1.75% and construction 5.55% rates or the employer's actual experience notice. Establish coverage, state localization, quarterly K-CNS100 reporting, electronic filing, payment and penalties. Federal FUTA is routed to its federal skill."
version: "0.2"
jurisdiction: US-KS
tax_year: 2026
last_updated: 2026-11-13
depends_on:
  - ks-income-tax
category: payroll
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
tier: 2
domain: payroll
type: computation
---

# Kansas employer unemployment contributions, 2026

> **Built from the law. Not yet approved.** Written by Codex. Not reviewed by an accountant. Circular 230 section 10.37: establish relevant facts and law; do not assume missing facts or rely on audit risk. A qualified professional must review filing outputs.

**Answer first.** Kansas Department of Labor, Division of Employment Security, administers employer unemployment contributions under chapter 44. The 2026 taxable wage base is **USD 15,100**, confirmed by KDOL's January 6, 2026 presentation published on the Legislature's official site. Ordinary new employers pay 1.75%, construction 5.55%; an experience-rated employer uses its actual assigned notice. Contributions may not be deducted from employees. [KDOL effective-date table](https://kslegislature.gov/b2025_26/committees/testimony/pdf/?apn=b2025_26%2Fyear2%2Fother_committees%2Fctte_ot_unemployment_compensation_modernization_1%2Ftestimony%2Fpublished%2Fctte_ot_unemployment_compensation_modernization_1_20260106_01_testimony.html); [44-710](https://ksrevisor.gov/statutes/chapters/ch44/044_007_0010.html); [44-710a](https://ksrevisor.gov/statutes/chapters/ch44/044_007_0010a.html).

## Scope

Ordinary contributory employers, coverage/localization, wages and base, new/assigned contributions, K-CNS 100 quarterly report/payment and corrections. Withholding belongs to `ks-payroll`; federal FICA, FUTA, federal credit reduction and federal wage-base calculations belong to `us-form-941-940-payroll`. Governmental, tribal and nonprofit reimbursement/rated methods have distinct rules and must not use the ordinary wage cap indiscriminately.

The old assertion that UI is Kansas's only possible employer social cost, with no disability/leave/health mandate, was broader than the researched evidence. Those unrelated mandates remain **Not yet confirmed**; the verified rule here is employer-only UI. The former K.S.A. 79-27 citation and “KW-3 UI” trigger do not identify this state UI return or administering agency.

## Ask the client first

1. Employer entity, first Kansas services/payment date, account status, liability determination and construction classification.
2. Worker locations, classification, officers/family relationships and any approved exclusions/elections.
3. Current-quarter gross wages, prior same-employer/predecessor wages, interstate reporting and current 2026 rate notice.
4. Experience account, acquisition/common ownership, voluntary contributions and reimbursement/rated-government election.
5. Portal access, headcount/TPA client count, outstanding reports/payments and notices/protest deadlines.

## The method, step by step

### Rates, bands and thresholds

| 2026 item / condition | Rate or amount | Official source |
| --- | --- | --- |
| Ordinary contributing-employer annual wage base | USD 15,100 per employee; actual 2026 effective amount | [KDOL January 6, 2026 table](https://kslegislature.gov/b2025_26/committees/testimony/pdf/?apn=b2025_26%2Fyear2%2Fother_committees%2Fctte_ot_unemployment_compensation_modernization_1%2Ftestimony%2Fpublished%2Fctte_ot_unemployment_compensation_modernization_1_20260106_01_testimony.html) |
| Statutory base framework for 2026-2027 | 25% of the specified previous statewide average annual wage, rounded to nearest USD 100; use published amount, not a self-inflated forecast | [44-703(o)(2)](https://ksrevisor.gov/statutes/chapters/ch44/044_007_0003.html) |
| New employer not eligible for experience computation | 1.75% | [44-710a(a)(1)](https://ksrevisor.gov/statutes/chapters/ch44/044_007_0010a.html) |
| New construction industry employer | 5.55%; principal industrial activity controls classification | [44-710a(a)(1)](https://ksrevisor.gov/statutes/chapters/ch44/044_007_0010a.html) |
| Employee UI contribution | None; contribution may not be deducted from wages | [44-710(a)](https://ksrevisor.gov/statutes/chapters/ch44/044_007_0010.html) |
| Experience computation eligibility | At least 24 consecutive chargeable months immediately before June 30 computation date; actual notice controls | [44-710a(a)(1)](https://ksrevisor.gov/statutes/chapters/ch44/044_007_0010a.html) |
| Ordinary coverage test | One employee in 20 different weeks or quarterly payroll at least USD 1,500; other liability routes also apply | [44-703(h)](https://ksrevisor.gov/statutes/chapters/ch44/044_007_0003.html); [handbook section I](https://www.dol.ks.gov/home/showpublisheddocument/68/639015674355270000) |
| Mandatory electronic report/payment | Employer with at least 25 employees, or TPA with at least 25 client employees; hardship waiver possible | [44-717(k)](https://ksrevisor.gov/statutes/chapters/ch44/044_007_0017.html) |

1. Register/determine status with KDOL, not the revenue department. The handbook requires K-CNS 010 within 15 days of paying the first employee. Ordinary 20-week/USD 1,500 coverage has separate acquisition, FUTA, public/tribal and voluntary-election routes. Agricultural cash wages USD 20,000 or ten workers/20 weeks, domestic USD 1,000-quarter and qualifying nonprofit four workers/20 weeks have their stated conditions. Once liable, report all quarters of that year with employment and continue active-account reports.
2. Determine employment and localization under 44-703(i). Services wholly or localized in Kansas generally belong here; otherwise apply the statutory base-of-operations, direction/control and residence sequence. Do not split a single localized employment mechanically by state days or use income-tax residence alone. Family exclusions have relationship/entity conditions and do not automatically apply to a corporation or LLC. Corporate/S corporation officers receiving remuneration are ordinarily employees; sole proprietors/partners are not their own employees. Disputed control/classification goes to KDOL/specialist review.
3. Establish reportable wages before deductions, including applicable commissions, bonuses, vacation/severance and noncash remuneration. Qualified employer health/retirement/other benefit exclusions require actual plan/payment conditions; federal income-tax wages are not automatically UI wages. Back-pay awards have specific allocation rules. Establish eligible same-employer/predecessor/interstate wage credit from actual records.
4. For each employee, current taxable wages equal min(current covered wages, max(15,100 - prior covered wages counting toward this base, 0)). Report **current-quarter** gross and excess wages; excess cannot exceed that quarter's wages. Do not carry accumulated excess into each later quarter. Multiply total current taxable wages by the actual notice rate, not a generic new rate for an experienced employer.
5. New nonconstruction/construction rates apply only while not eligible for experience rating, subject to allowed entering-employer election and actual classification. Section 44-710a requires 24 consecutive chargeable months before the June 30 computation date. The handbook's three/four-year shorthand depends on establishment date and next calendar-year assignment; do not treat it as an unconditional new-employer duration. Experience uses account contributions less benefits divided by the statutory average annual payroll and the applicable schedule/fund adjustment. The active 2026 experienced schedule and full range have **not** been verified from the blocked full current table; actual notice is required.
6. Review successor/common-owner experience transfers before resetting a wage base or new rate. Mandatory common-control transfers, permitted other transfers, negative-balance writeoff and SUTA-dumping provisions have distinct consequences. Voluntary contributions under 44-710a(c) are permitted during the 90-day notice window and must be paid before the stated 120-day year-start limit; they are not refundable. Determine whether they actually reduce the assigned cost. Government/tribal/nonprofit reimbursement and rated-government methods use their own elections, total-wage/billing and benefit-charge rules.

## Boundary and exception table

| Facts | Treatment |
| --- | --- |
| New employer labelled construction | Confirm principal industry and actual 5.55% assignment; do not use 1.75% |
| Experienced employer or successor | Use actual notice/experience transfer; do not infer rate from a public minimum |
| No wages or zero tax in an active account | K-CNS 100 still required |
| Reimbursing or rated-government account | Separate financing/base; ordinary cap/rate example does not apply |
| Remote worker | Statutory localization sequence; separate from income withholding and federal coverage |
| Possible surcharge or SUTA penalty | Use actual legal trigger/assessment; no assumed universal financing surcharge |

## Worked cases

Client facts are invented. The original federal-only examples used one employee earning USD 10,000, then two earning 10,000 and 5,000. Those federal computations remain with `us-form-941-940-payroll`; this state skill does not restate federal rates, bases or credit amounts. With the **same wages** and an ordinary new nonconstruction Kansas employer, state UI is 175 for the first case and 262.50 for both employees together.

```oa-check
name: KS 2026 new nonconstruction same original one and two employee wages
inputs:
  wages_a: 10000
  wages_b: 5000
  ks_base: 15100
  new_rate: 0.0175
steps:
  - one_employee_tax: min(wages_a, ks_base) * new_rate
  - two_employee_taxable: min(wages_a, ks_base) + min(wages_b, ks_base)
  - two_employee_tax: two_employee_taxable * new_rate
expected:
  one_employee_tax: 175
  two_employee_taxable: 15000
  two_employee_tax: 262.50
```

**Wage-cap/construction boundary.** An invented new construction employer pays 20,000 to one employee, with no other relevant wages/credits. Taxable wages stop at 15,100; tax at 5.55% is 838.05. Incorrectly charging all 20,000 gives 1,110, overstating 271.95. Ordinary nonconstruction rate applied to that same capped base would be 264.25, a different employer classification, not a choice for this construction employer.

```oa-check
name: KS 2026 construction cap and classification boundary
inputs:
  wages: 20000
  ks_base: 15100
  construction_rate: 0.0555
  ordinary_new_rate: 0.0175
steps:
  - taxable: min(wages, ks_base)
  - tax: taxable * construction_rate
  - wrong_uncapped_tax: wages * construction_rate
  - cap_overstatement: wrong_uncapped_tax - tax
  - different_classification_tax: taxable * ordinary_new_rate
expected:
  taxable: 15100
  tax: 838.05
  wrong_uncapped_tax: 1110
  cap_overstatement: 271.95
  different_classification_tax: 264.25
```

## When to refuse or refer

Refer missing/contested notices, classification, mixed interstate services, successor/common control, special financing, negative-balance writeoff and surcharge assessments. Do not elect a rate or deduct employer UI from employees. Current federal credit-reduction status and Social Security/Medicare portability remain federal questions, not state facts supplied by this skill.

## Filing and payment

The K-CNS 100 wage/tax report and ordinary contributions are due the last day of the month following each quarter: April 30, July 31, October 31 and January 31, with business-day relief. File even with no wages/tax. Statute 44-717(k) requires electronic wage reports, returns and payment at **25 or more** employees/client employees; use that law rather than the contradictory older 26-employee FAQ wording. Other employers may use approved filing channels, including permitted paper reporting.

Under the read February 2026 portal instructions, sign into KansasLabor, select **Tax & Wage Report > File Tax & Wage Report**, choose quarter/year, verify business/account facts, enter monthly covered-worker counts and wage details or approved file, review totals and submit the report. The final screen reports wages, rate and contribution. Then make the online payment (or complete a permitted payment later by its deadline). **Submitting the report does not complete payment.** Retain the submitted tax/wage reports and payment confirmation and verify the payment credited the correct account/quarter.

Correct a prior quarter using K-CNS 111 or the permitted online adjustment, not by altering an unrelated later quarter. The handbook describes November K-CNS 404-A rate notices and a 15-day rate-review period; follow the actual notice and controlling current review process, since rate and ordinary liability-review windows differ. Its separate old “annual wage report for experience rating with Q4” claim is not established as an additional current return beyond quarterly reporting.

Under 44-717(a), late-report penalty is 0.05% of total quarter wages per month/part, minimum USD 25 and maximum USD 200 for the report; late contribution interest is 1% per month/part. New-status notification relief, good-cause abatement and interest under USD 5 have statutory conditions. Willful nonpayment and misclassification/SUTA avoidance have separate sanctions; no automatic generic penalty tier or financing surcharge is invented. Current K-CNS 100 distinguishes assessed SUTA penalty from ordinary contributions. [44-717](https://ksrevisor.gov/statutes/chapters/ch44/044_007_0017.html); [March 2026 form](https://www.dol.ks.gov/home/showpublisheddocument/20/639101043129630000).

## Completion checklist

- KDOL liability, worker coverage/localization and account financing established.
- Actual 2026 wage base/rate notice and predecessor wages supported.
- Current-quarter gross, excess and taxable amounts reconcile by employee.
- Required electronic/zero-quarter report accepted; prior corrections filed for correct periods.
- Payment credited; notices and protest deadlines retained.

## Disclaimer

Informational and computational material only. A qualified professional must review actual facts, elections, rates and filing/payment results before use.

## Sources

| Source | URL | Read on |
| --- | --- | --- |
| KDOL presentation to UCMIC, January 6, 2026, on the official Legislature host. Read for explicit USD 14,000 to 15,100 base increase effective January 1, 2026; this is an agency statement, not a proposed rate assumed enacted. | https://kslegislature.gov/b2025_26/committees/testimony/pdf/?apn=b2025_26%2Fyear2%2Fother_committees%2Fctte_ot_unemployment_compensation_modernization_1%2Ftestimony%2Fpublished%2Fctte_ot_unemployment_compensation_modernization_1_20260106_01_testimony.html | 2026-11-13 |
| K.S.A.44-703. Read for coverage/employment/wages, localization and indexed wage-base framework. | https://ksrevisor.gov/statutes/chapters/ch44/044_007_0003.html | 2026-11-13 |
| K.S.A.44-710. Read for employer-only contributions, financing and no employee deduction. | https://ksrevisor.gov/statutes/chapters/ch44/044_007_0010.html | 2026-11-13 |
| K.S.A.44-710a. Read for new rates, 24-month/June 30 experience test, assignment, successor/negative-account and voluntary-payment conditions. | https://ksrevisor.gov/statutes/chapters/ch44/044_007_0010a.html | 2026-11-13 |
| K.S.A.44-717. Read for quarterly due date, late-report penalty/interest, relief and 25-employee electronic filing/payment threshold. | https://ksrevisor.gov/statutes/chapters/ch44/044_007_0017.html | 2026-11-13 |
| KDOL Employer Handbook, revised December 2025. Read for agency, status registration, coverage/exclusions/wages, financing, quarter reporting, rate notices/protests and corrections; statutory rules control simplified duration statements. | https://www.dol.ks.gov/home/showpublisheddocument/68/639015674355270000 | 2026-11-13 |
| K-CNS 100, revised March 2026. Read for current-quarter excess, wages paid, zero returns, assessed SUTA penalty, ordinary tax and separate payment. | https://www.dol.ks.gov/home/showpublisheddocument/20/639101043129630000 | 2026-11-13 |
| KDOL portal filing instructions K-CNS-P200, revised February 2026. Read for actual Tax & Wage Report sequence, review/submit and separate online payment. | https://www.dol.ks.gov/home/showpublisheddocument/1479/639057063560000000 | 2026-11-13 |

Not yet confirmed: full active 2026 experienced rate schedule/range and any account-specific surcharge; actual employer notice, entering-employer election, negative-account/transfer or reimbursement conditions; specialized misclassification penalty tiers; a separate annual experience wage report; unrelated no-disability/no-paid-leave/no-health-mandate assertions. Direct KDOL and ordinary browser access were denied and ordinary archive returned 429; the full official handbook/forms and KDOL Legislature presentation were read through the web reader. No numeric parameter was promoted from a search snippet alone.

> Contributed by Jeff Watts.
