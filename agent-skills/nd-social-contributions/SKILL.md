---
name: nd-social-contributions
description: "Compute North Dakota 2026 employer unemployment insurance, the 46600 dollar wage base, positive and negative balance schedules, new construction versus nonconstruction rates, coverage elections and UI EASY quarterly filing. Trigger on ND UI, SUTA, social contributions, SFN41263, assigned rate notice and employer wage reports."
license: "AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)"
metadata:
  source: openaccountants
  openaccountants_url: "https://www.openaccountants.com/skills/nd-social-contributions"
  jurisdiction: "US-ND"
  tax_year: "2026"
  last_updated: "2026-11-13"
---

# North Dakota employer unemployment contributions, 2026

> **Built from the law. Not yet approved.** Written by Codex. Not reviewed by an accountant. A qualified professional must review the established facts and filing result. Circular 230 section 10.37: consider relevant facts and circumstances; do not assume missing facts or rely on audit risk.

**Answer first.** North Dakota UI is employer-financed and may not be deducted from employee wages. The 2026 wage base is USD 46,600. New nonconstruction rates distinguish positive from negative account balance; construction is a separate 9.67% category. Use the actual notice. [2026 Job Service schedule](https://www.jobsnd.com/sites/www/files/documents/jsnd-documents/uitaxrateschedules2026.pdf); [52-04-01](https://ndlegis.gov/cencode/t52c04.pdf).

## Scope

Ordinary contributory employers, state UI wages/rates, officer/member elections, quarterly wage reports and payments. `nd-payroll` owns wage income-tax withholding and employer reconciliation. FICA/FUTA and federal credit-reduction questions belong to `us-form-941-940-payroll`; workers' compensation is a separate state regime. This skill does not turn the absence of an employee UI deduction into proof that no other payroll obligation exists.

## Ask the client first

1. Employer entity, registration/coverage dates, account and notice; construction or nonconstruction status.
2. Workers/services/locations, officer/LLC ownership and approved exclusions, including family-employment facts.
3. 2026 quarterly paid wages and prior same-employer wages, predecessor and interstate wage-credit evidence.
4. Positive/negative account status, assigned rate, prior reports and benefits/experience transfers.
5. Contribution versus reimbursement election, UI EASY access, notices, payments and construction risk-protection requirements.

## The method, step by step

### Rates, bands and thresholds

| 2026 item / condition | Rate / threshold | Official source |
| --- | --- | --- |
| Annual taxable wage base per employee | USD 46,600; 70% of statewide average annual wage | [2026 schedule](https://www.jobsnd.com/sites/www/files/documents/jsnd-documents/uitaxrateschedules2026.pdf) |
| Employee contribution | None; employer contributions may not be deducted from wages | [52-04-01](https://ndlegis.gov/cencode/t52c04.pdf) |
| New nonconstruction, positive balance | 1.00% | [2026 schedule](https://www.jobsnd.com/sites/www/files/documents/jsnd-documents/uitaxrateschedules2026.pdf) |
| New nonconstruction, negative balance | 6.07% | [2026 schedule](https://www.jobsnd.com/sites/www/files/documents/jsnd-documents/uitaxrateschedules2026.pdf) |
| New construction, either balance | 9.67% | [2026 schedule](https://www.jobsnd.com/sites/www/files/documents/jsnd-documents/uitaxrateschedules2026.pdf) |
| New category on 2026 schedule | Nonconstruction covered after June 30, 2024; construction covered after June 30, 2023 | [2026 schedule](https://www.jobsnd.com/sites/www/files/documents/jsnd-documents/uitaxrateschedules2026.pdf) |
| Experience status | At least six nonconstruction or ten construction coverage quarters before October for next calendar year's experience rating; notice controls | [Job Service explanation](https://www.jobsnd.com/unemployment-business-tax/learn-about-taxes) |
| Ordinary liability | One or more workers in 20 weeks or USD 1,500 quarterly; special agricultural/domestic/nonprofit/public/tribal rules differ | [Job Service](https://www.jobsnd.com/unemployment-business-tax/learn-about-taxes) |

The 2026 schedule gives these reserve-ratio bands. **Positive/negative refers first to the cumulative account balance**, not simply the sign of the six-year reserve ratio; a positive-schedule employer can have a negative six-year ratio.

| Positive schedule reserve ratio | 2026 rate | Official source |
| --- | --- | --- |
| -0.90% and less | 1.10% | [2026](https://www.jobsnd.com/sites/www/files/documents/jsnd-documents/uitaxrateschedules2026.pdf) |
| -0.89% through -0.07% | 0.91% | [2026](https://www.jobsnd.com/sites/www/files/documents/jsnd-documents/uitaxrateschedules2026.pdf) |
| -0.06% through +0.22% | 0.76% | [2026](https://www.jobsnd.com/sites/www/files/documents/jsnd-documents/uitaxrateschedules2026.pdf) |
| +0.23% through +0.37% | 0.63% | [2026](https://www.jobsnd.com/sites/www/files/documents/jsnd-documents/uitaxrateschedules2026.pdf) |
| +0.38% through +0.47% | 0.53% | [2026](https://www.jobsnd.com/sites/www/files/documents/jsnd-documents/uitaxrateschedules2026.pdf) |
| +0.48% through +0.57% | 0.44% | [2026](https://www.jobsnd.com/sites/www/files/documents/jsnd-documents/uitaxrateschedules2026.pdf) |
| +0.58% through +0.62% | 0.34% | [2026](https://www.jobsnd.com/sites/www/files/documents/jsnd-documents/uitaxrateschedules2026.pdf) |
| +0.63% through +0.68% | 0.25% | [2026](https://www.jobsnd.com/sites/www/files/documents/jsnd-documents/uitaxrateschedules2026.pdf) |
| +0.69% through +0.74% | 0.16% | [2026](https://www.jobsnd.com/sites/www/files/documents/jsnd-documents/uitaxrateschedules2026.pdf) |
| +0.75% and over | 0.07% | [2026](https://www.jobsnd.com/sites/www/files/documents/jsnd-documents/uitaxrateschedules2026.pdf) |

| Negative schedule reserve ratio | 2026 rate | Official source |
| --- | --- | --- |
| -8.46% and less | 9.67% | [2026](https://www.jobsnd.com/sites/www/files/documents/jsnd-documents/uitaxrateschedules2026.pdf) |
| -8.45% through -4.74% | 9.27% | [2026](https://www.jobsnd.com/sites/www/files/documents/jsnd-documents/uitaxrateschedules2026.pdf) |
| -4.73% through -3.68% | 8.87% | [2026](https://www.jobsnd.com/sites/www/files/documents/jsnd-documents/uitaxrateschedules2026.pdf) |
| -3.67% through -2.80% | 8.47% | [2026](https://www.jobsnd.com/sites/www/files/documents/jsnd-documents/uitaxrateschedules2026.pdf) |
| -2.79% through -1.54% | 8.07% | [2026](https://www.jobsnd.com/sites/www/files/documents/jsnd-documents/uitaxrateschedules2026.pdf) |
| -1.53% through -0.82% | 7.67% | [2026](https://www.jobsnd.com/sites/www/files/documents/jsnd-documents/uitaxrateschedules2026.pdf) |
| -0.81% through -0.50% | 7.27% | [2026](https://www.jobsnd.com/sites/www/files/documents/jsnd-documents/uitaxrateschedules2026.pdf) |
| -0.49% through +0.61% | 6.87% | [2026](https://www.jobsnd.com/sites/www/files/documents/jsnd-documents/uitaxrateschedules2026.pdf) |
| +0.62% through +5.20% | 6.47% | [2026](https://www.jobsnd.com/sites/www/files/documents/jsnd-documents/uitaxrateschedules2026.pdf) |
| +5.21% and over | 6.07% | [2026](https://www.jobsnd.com/sites/www/files/documents/jsnd-documents/uitaxrateschedules2026.pdf) |

1. Register through the state login/UI EASY within 20 days after first employing workers. Ordinary coverage, acquisition/FUTA, government/tribal immediate coverage, nonprofit four-workers/20 weeks, agricultural USD 20,000-or-ten-workers/20 weeks and domestic USD 1,000-quarter rules must be checked for the employer type. Use chapter 52-01 coverage and 52-04 financing; the old reference to a nonexistent employer-financing chapter 52-8 is not the operative authority.
2. Establish covered employment. Officers and specified LLC managers are employees; a manager is covered if the LLC is taxed as a corporation or the manager is not a member. Certain owners with at least 25% may jointly apply for exclusion within 60 days of formation or in January. Family exclusions do not automatically apply to corporations/covered LLCs and require the relationship to every partner where relevant. Sole proprietors/partners are not their own employees.
3. Determine wages under 52-01-01, including remuneration before employee deductions. Employer-qualified health/retirement contributions have separate exclusions; the federal income-tax wage figure is not automatically the UI figure. Establish localized employment; MN/MT income-tax reciprocity does not transfer UI coverage merely because of residence.
4. Per employee, taxable current wages are min(current covered wages, max(46,600-prior same-employer covered wages,0)). Report gross and current-quarter excess separately; **do not accumulate prior quarters' excess** in the current report. Verify eligible predecessor/interstate credits rather than assuming every prior employer's wages count.
5. Apply the exact 2026 assigned rate. The agency uses cumulative balance to choose the schedule, then six-year reserve divided by average three-year taxable payroll for the rate ratio. New-employer duration differs for construction/nonconstruction; the old blanket three-full-fiscal-years/June 30 description is superseded by the read agency conditions and 2026 dates.
6. Review account transfers, voluntary contributions and reimbursement elections. Transfers can be mandatory for common ownership/control. Job Service permits voluntary contributions from new-rate assignment through April 30 under its stated conditions; determine whether payment actually reduces the rate before making it. Reimbursable government/tribal/nonprofit employers use their own billing method. Construction-project risk protection is separate from ordinary contribution arithmetic.

### Historical baseline retained, not 2026 rates

The old examples used 2025 USD 45,100 with 1.02% and 6.09% labelled construction, producing USD 920.04 for two employees and USD 2,746.59 for one. These arithmetic results are preserved as **obsolete assumptions**, not verified 2025 filing instructions: the repaired body itself reported 2025 rates 1.03% positive nonconstruction/6.09% negative nonconstruction and 9.69% construction. The 2024 USD 43,800 and historic 0.08%-9.97% range (the former body also stated a 2025 0.08%-9.69% range and a 0.01% statutory floor) are older comparisons only. 2025 schedule amounts beyond that existing record have not been re-read here; do not use the incorrect 1.02%/construction 6.09% examples for any filing. Use verified 2026 rates above.

## Boundary and exception table

| Facts | Treatment |
| --- | --- |
| New nonconstruction with negative balance | 6.07%, not the 1.00% positive new rate |
| New construction | 9.67% for either account balance |
| Owner/manager with 25% holding | Exclusion is application/eligibility-dependent, not automatic |
| No wages in an active account | Quarterly zero report still required |
| MN/MT reciprocal wages | Income withholding exemption does not decide UI coverage |
| Reimbursable or acquired business | Establish election/experience transfer and possible predecessor liability |

## Worked cases

**Case 1.** Invented new positive-balance nonconstruction employer has two covered employees each paid above USD 46,600 in 2026. Total taxable wages 93,200 at 1.00% gives USD 932 employer UI, with no employee deduction. The old USD 920.04 example cannot be carried into 2026.

```oa-check
name: ND 2026 new positive nonconstruction two employees
inputs:
  base: 46600
  employees: 2
  rate: 0.01
steps:
  - taxable: base * employees
  - contribution: taxable * rate
expected:
  taxable: 93200
  contribution: 932
```

**Case 2, construction decision.** Invented new construction employer pays one employee above the base. USD 46,600×9.67%= USD 4,506.22. Applying the new negative nonconstruction 6.07% would produce USD 2,828.62, understating USD 1,677.60.

```oa-check
name: ND 2026 construction versus nonconstruction category
inputs:
  base: 46600
  construction_rate: 0.0967
  nonconstruction_negative_rate: 0.0607
steps:
  - construction: base * construction_rate
  - wrong_category: base * nonconstruction_negative_rate
  - shortfall: construction - wrong_category
expected:
  construction: 4506.22
  wrong_category: 2828.62
  shortfall: 1677.6
```

## When to refuse or refer

Refer classification, mixed interstate services, acquisitions, reimbursement elections, owner exclusions, construction risk protection and rate protests. Do not deduct UI from wages or infer a complete no-SDI/PFL/retirement mandate conclusion from an absence search. Such unrelated benefit/leave mandates remain separately unconfirmed; federal payroll stays in `us-form-941-940-payroll`.

## Filing and payment

Use UI EASY state-login registration/account access. Select the quarter, enter required employee wage detail, total/gross/current-quarter excess and taxable wages, apply the notice rate, submit and retain acceptance. All required reports and contribution payments must be electronic under 52-04-01.1. The current agency also permits its approved secure-file-transfer reporting channel; the old library handbook's paper/magnetic-tape instructions are historical and do not override current law.

Quarterly report/payment is due by the last day of the following month: April 30, July 31, October 31, January 31, with next-business-day relief as applicable. File zero wages while active. Correct the erroneous quarter through the agency correction process/SFN 41270 rather than adjusting an unrelated current quarter. The inherited SOC-code mandate, annual rate-notice timing/SFN 41216 and automatic 1% delinquency-rate uplift require current confirmation; follow the actual notice.

Under 52-04-11, unpaid contributions accrue 1.5% per month/part from due date. Late-report penalty is 5% per month/part; first month minimum USD 25 for the first delinquent report in a calendar year and USD 100 for later delinquent reports. The statute separately limits subsequent-month penalties to 20% and total penalty to USD 500 per report; do not simplify this into a universal 20% total cap. Circumstances beyond employer control may support waiver. Misclassification/fraud and personal-liability provisions require separate review.

## Completion checklist

- Coverage, employer category, balance and actual 2026 notice established.
- Employee wage base and gross/excess amounts reconcile.
- Owner exclusions/experience transfers supported.
- Electronic report, separate payment and zero-quarter duty satisfied.
- Acceptance, posted payment and any protests/corrections retained.

<!-- openaccountants-cta-block -->


---

### Talk to a verified accountant

This guide is maintained by the OpenAccountants network -- accountants who put their name behind the tax answers AI gives people. The live, always-current version (and the professional behind it) is at the OpenAccountants network.

- Use it in your AI: 
- Talk to a verified accountant: https://calendly.com/openaccountants-info/30min

## Sources

| Source | URL | Read on |
| --- | --- | --- |
| Job Service 2026 rate schedule. Read for 46600 base, all positive/negative bands, new rates and precise new-employer coverage dates. | https://www.jobsnd.com/sites/www/files/documents/jsnd-documents/uitaxrateschedules2026.pdf |2026-11-13 |
| Job Service Learn About Taxes. Read for registration 20 days, coverage, owner exclusions, six/ten-quarter experience and transfers/reimbursement. | https://www.jobsnd.com/unemployment-business-tax/learn-about-taxes |2026-11-13 |
| Job Service Reporting and Payment. Read for schedule selection, reserve formula, current-quarter excess, electronic reports/payment, localization and voluntary contributions. | https://www.jobsnd.com/unemployment-business-tax/about-reporting-and-payment-taxes |2026-11-13 |
| N.D.C.C.52-04. Read for employer-only contributions, mandatory electronic filing/payment, financing, penalties and interest. | https://ndlegis.gov/cencode/t52c04.pdf |2026-11-13 |
| N.D.C.C.52-01. Read for covered employment/wage definitions and exclusions. | https://ndlegis.gov/cencode/t52c01.pdf |2026-11-13 |
| Archived state-library Employer Handbook. Read for SFN 41263, zero reports, quarter deadlines and SFN 41270 corrections; outdated filing channels superseded by current law. | https://www.library.nd.gov/statedocs/JobService/jsnd4036.pdf |2026-11-13 |

Not yet confirmed: each employer's assigned notice and eligibility/elections; inherited SOC-code mandate, automatic 1% delinquency-rate addition and notice-number/timing details;2025 historical rates not freshly read; unrelated state disability/paid-leave/retirement mandate assertions. Direct Job Service requests returned 403 and the ordinary browser PDF view was blank; the complete official 2026 PDF and agency explanations were read through the web reader and archived outside Git. No employee-side UI is imposed by this computation.

## Today's figures and who stands behind this skill

This file is an AI skill (tax rules your AI follows) from OpenAccountants, copied on 2026-11-13. Rates, thresholds and deadlines change. For the current version of this skill, its official sources and the named accountant (if any) who stands behind it, call `get_skill` with slug `nd-social-contributions` on the OpenAccountants connector (https://www.openaccountants.com/connect), or read https://www.openaccountants.com/skills/nd-social-contributions. If neither is available, confirm every figure against the official source pages cited above before relying on it.
