---
name: je-payroll
description: >
  Jersey employer payroll and Income Tax Instalment Scheme duties for 2026,
  including employer registration, effective-rate notices, employee deductions,
  combined employer returns, payment and year-end reporting. Use for Jersey
  ITIS, missing effective rates, long-term care deductions, payroll returns
  or employer social security. Separates tax-only and combined defaults,
  contribution earnings, withholding collected from employees
  from the employer's own contributions and the employee's final assessment.
  Includes hypothetical notice, rounding and gross-pay examples. Benefits,
  directors, contractors and special arrangements need their specific rules.
  This source-cited draft awaits professional review. It cannot generate an
  effective rate or a complete operational payroll package.
jurisdiction: JE
category: payroll
tax_year: 2026
tier: 2
last_updated: 2026-10-15
version: 1.1
review_status: pending_review
depends_on:
  - workflow-base
  - payroll-workflow-base
---

# Jersey payroll and ITIS: 2026

## Inputs and registration

This partial reference covers selected ordinary employer deductions and reporting. It does not complete the payroll base's minimum-wage, overtime, benefits, pension, termination, payslip and rounding slots. Missing mandatory rules or outputs hold the complete payroll package. Source illustrations do not establish an employee's actual eligibility.

The reused [Income Tax Law](https://www.jerseylaw.je/laws/current/l_29_1961) capture applies from 17 June 2026. The [Contributions Order](https://www.jerseylaw.je/laws/current/ro_6108) applies from 22 April 2025, and the current [Social Security Law](https://www.jerseylaw.je/laws/current/l_22_1974) capture from 1 January 2026. Use the corresponding versions for earlier events; the published contribution amounts below are calendar-2026 figures.

Register as an employer with Revenue Jersey and establish employment, insured status, contribution classification and exemptions separately. [Income Tax Law Article 19A](https://www.jerseylaw.je/laws/current/l_29_1961) requires written notification within seven days of becoming an employer. Obtain the current employee Income Tax Instalment Scheme (ITIS) notice and any later Revenue Jersey instruction. Article 41CC states the applicable day and ends a notice on the earliest of its stated end, a replacement rate taking effect or year end. See the [employer guidance](https://www.gov.je/TaxesMoney/IncomeTax/Employers/Returns/Pages/EmployingStaff.aspx).

ITIS collects amounts towards the employee's annual liability. It is not the final personal tax rate. For an employee who is an insured person under Article 49B(5), a valid combined ITIS effective rate includes LTC contributions. A tax-only rate outside that combined branch does not itself include LTC. Class 1 social contributions are a separate deduction and employer liability; see `je-social-contributions`.

## Calculation

The [employer guidance](https://www.gov.je/TaxesMoney/IncomeTax/Employers/Returns/Pages/EmployingStaff.aspx) requires the applicable effective rate on gross earnings, including relevant bonuses and overtime. [Article 41B](https://www.jerseylaw.je/laws/current/l_29_1961) uses the notice applying on the deduction day. Its tax-only missing-notice default is 20%. For an employee who is an insured person within Article 49B(5), Schedule 1A Part 1 paragraph 3 applies the combined tax/LTC rate and expressly sets its missing-notice default at **22%**. Establish that status; the guidance's general 22% summary does not replace the statutory condition. A red contribution card or pension age alone does not establish that LTC is absent.

Do not calculate the employee's effective rate from personal tax bands, cap a valid notice at 22%, or add another LTC percentage to a combined rate. Schedule 1A paragraph 2 has separate arrears/revised-rate provisions; the Comptroller determines the notice. An appeal does not itself suspend the existing rate under Article 41CD(3). Unknown notice dates, status or conflicting instructions require verification before selecting a deduction.

1. Establish the gross amounts included for ITIS and for social contributions separately. Social Security Law Schedule 1A and Contributions Order Article A2/Schedule 1 govern Class 1 earnings; they do not automatically establish the income-tax base. Use `je-social-contributions` for the selected absence, accommodation, tips, expenses and leaving-payment rules.
2. Apply the valid ITIS rate once to the relevant gross earnings. Do not add another long-term care deduction.
3. Calculate Class 1 primary contributions separately after verified classification, earnings attribution, earnings rounding, threshold and cap. The [2026 schedule](https://www.gov.je/Working/Contributions/Employers/pages/tables.aspx) and [Class 1 employer guidance](https://www.gov.je/Working/Contributions/Employers/Pages/ScheduleGuide.aspx) round monthly contribution earnings down to whole pounds and weekly earnings down to 25p. This is an earnings-base instruction, not a rule for rounding ITIS gross, contribution amounts or net pay. Complete non-monthly conversion/cumulative treatment and deduction-penny rounding remain unverified.
4. Deduct ITIS and primary contributions from the employee. Account separately for the employer's secondary contribution.
5. Reconcile deductions, payments and the combined employer return. This does not settle the employee's annual assessment.

Taxable termination payments require [Article 62D](https://www.jerseylaw.je/laws/current/l_29_1961), including its remuneration/deferred-pay distinction and conditions; the employer page's short GBP 50,000 summary does not establish a universal exemption. Benefits need Articles 65A/65B and the applicable valuation/exemption provisions. Those complete computations remain outside this partial reference. Building subcontractors have Article 41E/Schedule 1A Part 2 and certificate rules; do not run them through the employee payroll base by default.

## Hypothetical worked positions

These 2026 illustrations assume the stated bases, status and notice are established. Where Class 1 is computed, ordinary monthly contribution conditions are also established. Exact arithmetic does not validate eligibility or a rounding method.

1. **Valid combined notice.** Cash and relevant earnings are GBP 1,000, with a valid supplied 12% combined rate and no other adjustments. ITIS is GBP 120, Class 1 primary GBP 60 and cash net GBP 820. Employer secondary is GBP 65; salary plus secondary cost is GBP 1,065. The 12% is an assumed notice input. Sources: Article 41B, Schedule 1A paragraph 3 and the 2026 contribution schedule.
2. **Combined missing-notice case.** On the same facts, except the employer has received no applicable Article 41CC notice and the employee's Article 49B insured status is established, 22% gives GBP 220 combined withholding. Primary remains GBP 60, cash net GBP 720 and secondary GBP 65. No additional LTC amount is deducted. Source: Schedule 1A Part 1 paragraph 3(2).
3. **Tax-only condition.** For an established tax-only case outside Article 49B's insured-employee branch, no applicable notice and GBP 1,000 tax earnings give GBP 200 at Article 41B's 20% default. This does not establish contribution classification or a complete net-pay amount; those require separate facts. Do not select this branch merely because primary Class 1 deductions are exempt.
4. **Two different bases.** Established ITIS gross is GBP 1,000.89, with a valid 12% rate. Monthly Class 1 earnings round down to GBP 1,000, giving GBP 60 primary and GBP 65 secondary in this illustration. ITIS percentage arithmetic on GBP 1,000.89 gives GBP 120.1068. Its deduction and cash net remain held until the applicable monetary rounding is verified. Do not round ITIS gross to GBP 1,000 using the contribution rule. Sources: Article 41B and the two contribution guidance pages.
5. **Notice effective day.** A valid 12% notice is replaced by a valid 14% notice applying from 1 November. On established GBP 1,000 relevant earnings, an ordinary 15 October deduction is GBP 120 and a 15 November deduction GBP 140. Both figures exclude other adjustments and do not generate a rate. Source: Articles 41B and 41CC.
6. **Under-school-age deduction.** For an employee established to be under the upper limit of compulsory school age, Article 41B(2) does not require deduction but permits the employer to choose it at the employee's effective rate. If the employer does not choose deduction, the illustrated ITIS deduction is zero. This is not proof of a nil annual assessment or a general reporting/contribution exemption. Verify those separate duties.

## Returns and payments

The [employer guidance](https://www.gov.je/TaxesMoney/IncomeTax/Employers/Returns/Pages/EmployingStaff.aspx) and Articles 20, 41BA and 41BC provide these ordinary monthly obligations:

| Obligation | Deadline or retention |
|---|---|
| Combined employer return | Within 15 days after month end |
| ITIS payment and social contribution payment | Within 15 days after month end; pay the two liabilities separately |
| Benefits-in-kind return | 15 January following the reporting year |
| Employee summary | By 31 January following the year, or on the last employment day if leaving earlier |
| Deduction records | At least six years after deduction under Article 41BC |

The combined return includes the applicable staff, office-holder/director and labour-only subcontractor information, with separate statutory duties and certificate conditions. Article 20's company annual-return concession requires a written application, at least 25% ordinary-share ownership by each relevant employee and Comptroller agreement. Complete annual-filing/payment and director-classification branches require verification; do not extrapolate a calendar from the general monthly table. Short-term business visitors have a statutory tax exception under [Article 118B](https://www.jerseylaw.je/laws/current/l_29_1961), but licensing and social contribution treatment are separate questions.

Article 41BB permits a missing/incorrect-payment estimate with prescribed notice information, at least fifteen days to pay from the notice date, and a fifteen-day service-based appeal period. Do not replace those notice conditions with the guidance's instruction to pay an estimated bill immediately. Complete penalty, appeal and collection mechanics remain outside this batch.

## Limits and checks

Record the requested period, employment/Class 1/LTC status separately, current notice and effective dates, every cash/noncash payment, separate ITIS and contribution bases, pay dates and periods, prior monthly earnings/contributions, absence reimbursements, leaving date and payment type, remittances and return notices. Use redacted references; identifiers, identity documents, account details and submission remain with the reviewer. No factual default establishes unknown eligibility, earnings, law or a nil contribution.

| Code and trigger | Verbatim response |
|---|---|
| R-JE-PAY-1: unverified status, earnings or source condition | Needs Input: establish the Jersey employment, contribution status and separate earnings bases before computing this payroll position. |
| R-JE-PAY-2: unsupported notice or default-rate branch | Needs Input: establish the applicable notice, effective day and statutory tax-only or combined-rate condition. |
| R-JE-PAY-3: unknown monetary rounding or pay-period conversion | Needs Input: verify the applicable rounding and period treatment before producing the affected deduction or net pay. |
| R-JE-PAY-4: incomplete mandatory companion or outputs | Needs Input: the complete Jersey payroll companion and financial package are not ready. |

Every amount and classification requires reviewer attention, regardless of value; this is review policy. Extend the reviewer brief with the notice/status evidence, separate bases and earnings rounding, statutory exceptions, correction month, missing rules and reconciled collection. Check that LTC is not added twice, secondary contributions are not deducted from the employee, and the same amounts, dates, holds and citations appear across all outputs. Complete non-monthly mechanics, monetary rounding, minimum wage/overtime, benefits, pensions, termination and employment permits remain open.

Version 1.1 adds selected statute and fresh employer/contribution guidance checked on 15 October 2026. The contribution earnings rules are expanded in `je-social-contributions`; complete payroll and contribution companions remain unfinished. See `references.md` for capture hashes, contrary summaries and periods. This draft has no professional sign-off.

<!-- openaccountants-cta-block -->

---

## Talk to a verified accountant

This guide is maintained in the
[ryanduguid/openaccountants fork](https://github.com/ryanduguid/openaccountants).
Check its quality tier, recorded review status and cited sources before use.
Choose a practitioner whose credentials and engagement scope you have verified.
The links below are optional upstream services; they do not publish or verify
this fork's changes.

- Upstream connection service: https://www.openaccountants.com/connect
- Upstream accountant network: https://www.openaccountants.com/network

> **General reference only.** This document does not constitute tax, legal, or
> financial advice. Verify figures against the cited primary sources or with a
> licensed professional before relying on them.
