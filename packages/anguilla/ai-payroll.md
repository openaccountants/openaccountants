---
name: ai-payroll
description: >
  Anguilla Universal Social Levy (USL) for ordinary monthly employee and employer
  remuneration in 2026. Covers the separate 3% employee and 3% employer liabilities,
  the XCD 2,000 monthly remuneration exemption, the XCD 12,000 employer wage limit,
  conditional telephone and travel allowances, deduction at payment, the monthly return
  and remittance within 10 days, termination remittance, nil returns and the late filing
  penalty. Use for Anguilla payroll, employee levy, employer levy, USL returns or monthly
  remuneration. Self-employed levy, Social Security, non-monthly conversion and disputed
  employment require additional sources. Built from the unofficial online consolidation
  dated 31 December 2022, checked against the IRD's 2026 USL page; later amendments
  remain unverified and the skill awaits review by a qualified professional in Anguilla.
jurisdiction: AI
category: payroll
type: situation-rules
tax_year: 2026
tax_year_notes: "2026 calendar year; statute text from the consolidation as at 31 December 2022, figures confirmed on the IRD USL page on 14 November 2026"
tier: 2
last_updated: 2026-11-14
version: 0.5
depends_on:
  - workflow-base
---

# Anguilla Universal Social Levy: employers and employees v0.5

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

Written by Ryan Duguid; imported from his fork and brought to the repository standard. Built from the law. Not yet approved by an accountant. Tax year 2026.

## Scope

Establish the operative law, employment classification, monthly remuneration and employer status before calculating Universal Social Levy (USL). This companion covers an ordinary monthly employer/employee case and the supported statutory branches. Load `workflow-base` for the procedure, four outputs, questions and universal refusals. A qualified professional reviews each position before filing or payment.

Self-employed USL, Social Security contributions, non-monthly conversion, concurrent employments, disputed worker status, benefit valuation, assessments, penalties, appeals and cross-border employment need their complete applicable sources. A salary label or company-director title does not alone resolve every classification. Keep employer and employee liabilities separate.

Use the [Anguilla source register](references.md#social-security-contribution-guidance) for separate 2026 Social Security Board guidance. The register also records ordinary income tax scope and the tax residence programme. General Services Tax is in [ai-gst](ai-gst.md).

### Period coverage and source currency

The online copy of the [*Universal Social Levy Act*, R.S.A. c. U12](https://laws.gov.ai/storage/pdfs/2022%20AXA%20Revised%20Statutes%20and%20Regulations/PDF%20(Acts)/U-R.S.A.s/U012-Universal%20Social%20Levy%20Act.pdf) hosted by the government states that it shows the law as at 31 December 2022. It consolidates Act 26 of 2021, in force 1 January 2022, and Act 14 of 2022, in force 22 December 2022. This dated text was read by Ryan Duguid on 11 October 2026 and re-read on 14 November 2026. The [law library's disclaimer](https://laws.gov.ai/?selected_page=disclaimer) classifies its online versions as unofficial and warns that the revision may omit laws, regulations or amendments. Complete operative provisions, later amendments and applicable regulations remain unverified. The editing date does not establish current 2026 law.

For 2026, the [IRD Universal Social Levy page](https://www.ird.gov.ai/Services/Tax/usl), read on 14 November 2026, states the same figures: 3% on gross salary or wages of employees earning over EC$2,000 per month, the employer matching 3% on remuneration not exceeding EC$12,000 per month, and the return and payment no later than 10 days after the end of each calendar month. The figures below are therefore used for tax year 2026.

Before an engagement calculation, obtain the applicable official law or authoritative confirmation of the required provisions. Verify the requested period's law, amendments, required regulations, currency and authority instructions. If the source conditions cannot be established, fire `R-AI-USL-PERIOD`; do not produce a payable estimate from this dated baseline. Apply that condition when using any figures or calculation section separately.

[Hansard for 22 September 2026](https://hansard.houseofassembly.ai/view_hansard?id=b5f59c2c-bdb9-11f1-8de9-26e8d4c008c4) records the defeat of Motion 13 seeking legislation to repeal USL. A motion's title cannot establish an enacted repeal. This record does not prove that there was no other later legislation.

Version history: version 0.3 (Ryan Duguid, 12 October 2026) was the monthly employer/employee reference using the unofficial online consolidation dated 31 December 2022, recording the library's provenance limitation and requiring official law or authoritative confirmation before an engagement calculation. Version 0.5 (14 November 2026) moved the text to the repository's method headings, made every link inline, set tax year 2026 on the IRD's 2026 page and added the statutory late filing penalty and assessment period. Complete operative provisions, post-2022 amendments, all applicable regulations, benefit valuation, operational rounding, record retention and full special-case compliance remain unverified.

## Ask the client first

1. Which month is being prepared, and how often is the employee paid?
2. Total monthly remuneration, with every component (salary, leave pay, commission, fees, bonuses, perquisites, allowances, benefits in kind).
3. Is the worker an employee, a director or working partner, or self-employed?
4. Is the employer the Government of Anguilla, a Government Agency, a Non-Governmental Organisation or a church incorporated in Anguilla?
5. Any telephone or travel allowance, and evidence that it relates directly to the job and is reasonably incurred?
6. Other employments, a termination in the month, and any earlier overpayment?

Establish the requested period, qualified reviewer, employer category, worker classification, pay frequency, all remuneration components, allowance evidence, other employment, termination dates, deductions, actual payments, prior overpayments and authority notices. Obtain the current prescribed or Comptroller-specified filing instructions. Use the base's structured fact questions and action-list document requests. Never submit identity documents, tax identifiers or bank details through this guide.

## The method, step by step

### Period-specific figures

The table gives the 31 December 2022 consolidation, confirmed for 2026 on the IRD page where the row says so. XCD is used in illustrations, consistent with the IRD's [USL guidance](https://www.ird.gov.ai/Services/Tax/usl). Confirm currency for an actual assessment.

| Rule | Figure or timing, 2026 | Primary provision |
|---|---|---|
| Employee USL | 3% of remuneration when the exemption does not apply | [Act s 4(1)(a)](https://laws.gov.ai/storage/pdfs/2022%20AXA%20Revised%20Statutes%20and%20Regulations/PDF%20(Acts)/U-R.S.A.s/U012-Universal%20Social%20Levy%20Act.pdf); [IRD USL page](https://www.ird.gov.ai/Services/Tax/usl) |
| Ordinary employer USL | 3% of remuneration, capped at XCD 12,000 for this ordinary monthly case | [Act s 4(1)(b)](https://laws.gov.ai/storage/pdfs/2022%20AXA%20Revised%20Statutes%20and%20Regulations/PDF%20(Acts)/U-R.S.A.s/U012-Universal%20Social%20Levy%20Act.pdf); [IRD USL page](https://www.ird.gov.ai/Services/Tax/usl) |
| Monthly remuneration exemption | Total remuneration at or below XCD 2,000 | [Act s 4(4)](https://laws.gov.ai/storage/pdfs/2022%20AXA%20Revised%20Statutes%20and%20Regulations/PDF%20(Acts)/U-R.S.A.s/U012-Universal%20Social%20Levy%20Act.pdf); [IRD USL page](https://www.ird.gov.ai/Services/Tax/usl) |
| Above the exemption | The exemption does not apply to the remuneration | [Act s 4(5)](https://laws.gov.ai/storage/pdfs/2022%20AXA%20Revised%20Statutes%20and%20Regulations/PDF%20(Acts)/U-R.S.A.s/U012-Universal%20Social%20Levy%20Act.pdf) |
| Eligible telephone allowance | Exemption up to XCD 400, subject to the job and cost conditions | [Act s 4(6)(a), (7)](https://laws.gov.ai/storage/pdfs/2022%20AXA%20Revised%20Statutes%20and%20Regulations/PDF%20(Acts)/U-R.S.A.s/U012-Universal%20Social%20Levy%20Act.pdf) |
| Eligible travel allowance | Exemption up to XCD 225, subject to the job and cost conditions | [Act s 4(6)(b), (7)](https://laws.gov.ai/storage/pdfs/2022%20AXA%20Revised%20Statutes%20and%20Regulations/PDF%20(Acts)/U-R.S.A.s/U012-Universal%20Social%20Levy%20Act.pdf) |
| Deduction | At payment, for each pay period | [Act s 5(1)](https://laws.gov.ai/storage/pdfs/2022%20AXA%20Revised%20Statutes%20and%20Regulations/PDF%20(Acts)/U-R.S.A.s/U012-Universal%20Social%20Levy%20Act.pdf) |
| Ordinary employer remittance | Within 10 days of the end of each pay period | [Act s 6(1)](https://laws.gov.ai/storage/pdfs/2022%20AXA%20Revised%20Statutes%20and%20Regulations/PDF%20(Acts)/U-R.S.A.s/U012-Universal%20Social%20Levy%20Act.pdf) |
| Ordinary employer monthly return and remittance | Not later than 10 days after month end | [Act s 8(1)](https://laws.gov.ai/storage/pdfs/2022%20AXA%20Revised%20Statutes%20and%20Regulations/PDF%20(Acts)/U-R.S.A.s/U012-Universal%20Social%20Levy%20Act.pdf); [IRD USL page](https://www.ird.gov.ai/Services/Tax/usl) |
| Termination remittance | Within one month from the end of the termination month | [Act s 6(2)](https://laws.gov.ai/storage/pdfs/2022%20AXA%20Revised%20Statutes%20and%20Regulations/PDF%20(Acts)/U-R.S.A.s/U012-Universal%20Social%20Levy%20Act.pdf) |
| Late filing penalty | XCD 50 for each day of default, to a maximum of XCD 2,000 | [Act s 10](https://laws.gov.ai/storage/pdfs/2022%20AXA%20Revised%20Statutes%20and%20Regulations/PDF%20(Acts)/U-R.S.A.s/U012-Universal%20Social%20Levy%20Act.pdf) |
| Assessment period | Within 2 years from the day the levy was required to be remitted, unless misrepresentation, fraud or non-disclosure | [Act s 9(1), (2)](https://laws.gov.ai/storage/pdfs/2022%20AXA%20Revised%20Statutes%20and%20Regulations/PDF%20(Acts)/U-R.S.A.s/U012-Universal%20Social%20Levy%20Act.pdf) |

The XCD 12,000 limit belongs to the employer limb. The employee limb has no corresponding cap in s 4(1)(a). The exemption is not a deduction of XCD 2,000 from a larger wage. Non-monthly and multiple-employer cases require their own statutory reconciliation before either limit is used.

### Primary source library

Use the [2022 statutory consolidation](https://laws.gov.ai/storage/pdfs/2022%20AXA%20Revised%20Statutes%20and%20Regulations/PDF%20(Acts)/U-R.S.A.s/U012-Universal%20Social%20Levy%20Act.pdf), [IRD USL guidance](https://www.ird.gov.ai/Services/Tax/usl) and the bounded [parliamentary record](https://hansard.houseofassembly.ai/view_hansard?id=b5f59c2c-bdb9-11f1-8de9-26e8d4c008c4). Section 1(3) requires reading the Act with the applicable Inland Revenue Department Act provisions. This companion does not establish their complete record, interest, service or appeal rules. `references.md` records provenance, source gaps and the country topic matrix. A current website summary cannot silently replace an operative statutory provision.

### Classification and remuneration

[Act s 1](https://laws.gov.ai/storage/pdfs/2022%20AXA%20Revised%20Statutes%20and%20Regulations/PDF%20(Acts)/U-R.S.A.s/U012-Universal%20Social%20Levy%20Act.pdf) includes company directors and working partners in the employee definition. Remuneration includes wages, salary, leave pay, acting payments, commission, fees, bonuses, perquisites other than service charge, and allowances. Section 5(3) includes remuneration in cash or kind. Resolve the legal category and valuation of a benefit; do not substitute net cash received or a bank deposit for remuneration.

Confirm each claimed allowance under s 4(6) and (7): the costs must relate directly to the nature of the job and be reasonably incurred in performing duties. Preserve its amount and evidence separately. A payroll label alone does not establish exemption. Resolve any allowance/threshold interaction, excess allowance or disputed service-charge character before calculating; the illustrations use uncomplicated facts safely above the threshold where relevant.

### Separate employee and employer calculations

For the established ordinary monthly case, let R be the verified remuneration after applicable statutory exclusions. [Act s 4](https://laws.gov.ai/storage/pdfs/2022%20AXA%20Revised%20Statutes%20and%20Regulations/PDF%20(Acts)/U-R.S.A.s/U012-Universal%20Social%20Levy%20Act.pdf) supplies these branches:

1. If total remuneration satisfies the monthly exemption at or below XCD 2,000, the exemption applies. Record zero for both ordinary limbs.
2. If remuneration exceeds XCD 2,000, employee USL is R x 3 / 100 on the full remuneration. Do not deduct an initial exempt band or impose the employer cap on the employee.
3. For an ordinary liable employer, employer USL is the lesser of R and XCD 12,000, multiplied by 3 / 100.
4. Section 4(2) excludes the Government of Anguilla, Government Agencies, Non-Governmental Organisations and churches incorporated in Anguilla from the employer meaning for that section. Establish the particular employer's statutory status. This does not erase the employee's separate liability.

The remittance reconciliation identifies the employee deduction and employer liability separately, then adds the amounts due. USL is not Social Security. Do not combine its base or cap with an SSB contribution election, ceiling or contribution rate.

### Reporting and payment rules

[Act ss 5, 6 and 8](https://laws.gov.ai/storage/pdfs/2022%20AXA%20Revised%20Statutes%20and%20Regulations/PDF%20(Acts)/U-R.S.A.s/U012-Universal%20Social%20Levy%20Act.pdf) require deduction at payment, employer pay-period remittance and monthly reporting/remittance. The ordinary monthly case must satisfy both ss 6(1) and 8(1). Section 8(3) requires a return by its ten-day pay-period deadline even if no remuneration was paid in a particular month. Confirm the prescribed or Comptroller-specified form and manner under s 8(1), and the operative online filing instructions before reporting.

Section 8(2) aggregates payments within a calendar month when remuneration is not paid monthly. That does not itself resolve all conversions and the interaction with the pay-period duty in s 6. Refer such cases under `R-AI-USL-SPECIAL`. Termination has the additional s 6(2) duty; do not treat it as a general extension for earlier liabilities.

For an employer's established good-faith overpayment, s 6(3) sets the excess against levy falling due subsequently. Reconcile actual remittance, error and later levy; do not assume a cash refund. Section 1(2) expressly excludes Interpretation and General Clauses Act s 6(1)(d) from time computation. Verify actual due dates and authority directions without assuming a weekend or holiday extension.

Self-employed deemed remuneration under s 2 uses the greater of elected prescribed remuneration and notional remuneration. Section 7 and the website's monthly payment summary differ in timing. Gross receipts, net profit and a Social Security category cannot supply an invented self-employed levy base or deadline. That calculation is excluded from this companion; the IRD page's statement that self-employed persons pay 6% on gross earnings over EC$2,000 per month is recorded here only so it is not mistaken for the employee rate.

### Conservative defaults

These treatments apply to unresolved facts inside established law. Disclose the difference, use the base's questions and obtain review. Unknown legal scope remains Needs input.

| Missing fact | Treatment and disclosure | Primary condition |
|---|---|---|
| Job/cost evidence for an otherwise identified telephone or travel allowance is missing | Treat it as included remuneration pending evidence; disclose the alternative exemption and tax effect | [Act s 4(6), (7)](https://laws.gov.ai/storage/pdfs/2022%20AXA%20Revised%20Statutes%20and%20Regulations/PDF%20(Acts)/U-R.S.A.s/U012-Universal%20Social%20Levy%20Act.pdf) |
| A claimed employer exception lacks proof of the employer's qualifying status | Use the ordinary employer limb as an Assumed position only where its legal classification is otherwise established; disclose the alternative and seek evidence | [Act s 4(1), (2)](https://laws.gov.ai/storage/pdfs/2022%20AXA%20Revised%20Statutes%20and%20Regulations/PDF%20(Acts)/U-R.S.A.s/U012-Universal%20Social%20Levy%20Act.pdf) |
| Employment status, benefit value, total remuneration or the applicable legal period is unresolved | Needs input; fire the applicable topical refusal before engagement calculation | [Act ss 1, 4 and 5](https://laws.gov.ai/storage/pdfs/2022%20AXA%20Revised%20Statutes%20and%20Regulations/PDF%20(Acts)/U-R.S.A.s/U012-Universal%20Social%20Levy%20Act.pdf) |

### Reviewer attention and question thresholds

Every position requires professional review. The companion's cash threshold for an automatic reviewer flag and a fact question is XCD 0: flag every nonzero difference. This review policy is not law. Always flag currency, period law, worker classification, employer status, allowance evidence and deadline uncertainty, including cases with no computed cash difference. Use the base's no-effect, description-answered, grouping and ten-question filters.

## Worked cases

These examples apply only the stated statutory baseline to synthetic ordinary monthly facts. All amounts are XCD. Each case assumes the operative law and status needed for its illustration, and no other remuneration, benefit, adjustment, employment or contribution. Results are exact and derived from the rule on the row; an actual case needs its rounding and source checks.

| Position and supplied hypothetical facts | Separate calculation and result (derived) | Rule and review consequence |
|---|---|---|
| 1. Ordinary employer and employee; total remuneration 2,000 | Equality satisfies the exemption. Employee zero; employer zero; combined zero | [Act s 4(4)](https://laws.gov.ai/storage/pdfs/2022%20AXA%20Revised%20Statutes%20and%20Regulations/PDF%20(Acts)/U-R.S.A.s/U012-Universal%20Social%20Levy%20Act.pdf); verify complete monthly remuneration |
| 2. Ordinary employer and employee; remuneration 3,000 | Employee 3,000 x 3 / 100 = 90; employer 3,000 x 3 / 100 = 90; combined 180 | [Act s 4(1), (5)](https://laws.gov.ai/storage/pdfs/2022%20AXA%20Revised%20Statutes%20and%20Regulations/PDF%20(Acts)/U-R.S.A.s/U012-Universal%20Social%20Levy%20Act.pdf); no initial 2,000 deduction |
| 3. Ordinary employer and employee; remuneration 15,000 | Employee 15,000 x 3 / 100 = 450; employer 12,000 x 3 / 100 = 360; combined 810 | [Act s 4(1)](https://laws.gov.ai/storage/pdfs/2022%20AXA%20Revised%20Statutes%20and%20Regulations/PDF%20(Acts)/U-R.S.A.s/U012-Universal%20Social%20Levy%20Act.pdf); applying the employer cap to the employee would understate employee levy by 90 |
| 4. Employee of the established Government of Anguilla; remuneration 4,000 | Employee 4,000 x 3 / 100 = 120; exempt employer limb zero; combined 120 | [Act s 4(1), (2)](https://laws.gov.ai/storage/pdfs/2022%20AXA%20Revised%20Statutes%20and%20Regulations/PDF%20(Acts)/U-R.S.A.s/U012-Universal%20Social%20Levy%20Act.pdf); employer status does not exempt the employee |
| 5. Ordinary employer and employee; salary 5,000 plus telephone allowance 300, with the job/cost conditions proved | Allowance exemption 300; remuneration for this straightforward calculation 5,000; employee 150 and employer 150; combined 300. Without proven eligibility, remuneration 5,300 gives 159 each and combined 318; difference 18 | [Act s 4(1), (6), (7)](https://laws.gov.ai/storage/pdfs/2022%20AXA%20Revised%20Statutes%20and%20Regulations/PDF%20(Acts)/U-R.S.A.s/U012-Universal%20Social%20Levy%20Act.pdf); disclose missing eligibility evidence if the second treatment is used as a default |

### Case 1: a high earner, employer cap against no employee cap (position 3)

An ordinary employer pays a manager XCD 15,000 for the month. The employee levy is on the full 15,000; the employer levy stops at 12,000. Employee 450, employer 360, combined remittance 810.

```oa-check
name: Anguilla USL, monthly remuneration 15,000
inputs:
  remuneration: 15000
  rate: 0.03
  employer_cap: 12000
steps:
  - employee_usl: remuneration * rate
  - employer_usl: min(remuneration, employer_cap) * rate
  - combined: employee_usl + employer_usl
  - understatement_if_capped: employee_usl - min(remuneration, employer_cap) * rate
expected:
  employee_usl: 450
  employer_usl: 360
  combined: 810
  understatement_if_capped: 90
```

### Case 2 (decision): treat the telephone allowance as exempt or not (position 5)

Salary is XCD 5,000 plus a telephone allowance of 300. If the s 4(6) and (7) job and cost conditions are proved, the allowance is exempt and each limb is 150 (combined 300). Without that evidence, the default treats it as remuneration: 5,300 gives 159 each, combined 318. The evidence decides an 18 difference.

```oa-check
name: Anguilla USL, telephone allowance exempt or included
inputs:
  salary: 5000
  allowance: 300
  rate: 0.03
steps:
  - each_limb_exempt: salary * rate
  - combined_exempt: each_limb_exempt * 2
  - each_limb_included: (salary + allowance) * rate
  - combined_included: each_limb_included * 2
  - difference: combined_included - combined_exempt
expected:
  each_limb_exempt: 150
  combined_exempt: 300
  each_limb_included: 159
  combined_included: 318
  difference: 18
```

## When to refuse or refer

Use the message verbatim when its trigger applies. Include the universal `workflow-base` codes in the refusal trace.

| Code | Trigger | Output message |
|---|---|---|
| R-AI-USL-PERIOD | Applicable period law, currency or required source conditions cannot be established | I cannot calculate an Anguilla Universal Social Levy liability until the applicable period law and required source conditions are verified. Obtain the operative sources and professional review. |
| R-AI-USL-SPECIAL | Self-employment, Social Security, non-monthly or concurrent employment, disputed status, uncertain benefit valuation, assessment, penalty or appeal is needed | This Anguilla monthly employer and employee companion does not establish the rules needed for this case. Load the applicable primary provisions and a suitable companion, or consult an Anguilla tax professional. |
| R-AI-USL-AMBIGUITY | More than ten unresolved grouped questions remain after the base's filtering rules | The Anguilla levy records contain more unresolved grouped questions than this workflow can handle. Obtain a reconciled fact schedule and professional review before calculation. |

## Filing and payment

1. Deduct employee USL from each payment of remuneration (s 5(1)).
2. File the monthly return in the prescribed or Comptroller-specified form (the IRD page links a "USL - Employee Form") and remit both limbs not later than 10 days after the end of the month (s 8(1)); remit within 10 days of the end of each pay period (s 6(1)).
3. File a return even if no remuneration was paid in the month (s 8(3)); the IRD page also says an employer must file for an employee earning less than EC$2,000 per month.
4. On termination, remit all levies for that employee within one month from the end of the termination month (s 6(2)).
5. Late filing: the Comptroller may assess XCD 50 for each day of default to a maximum of XCD 2,000 (s 10). The IRD page states the maximum as EC$2,000 per month and adds interest of 1% per month on amounts outstanding; the statute's wording governs the penalty, and the interest rate rests on the IRD page only.
6. Assessment: within 2 years from the day the levy was due, or at any time for misrepresentation, fraud or non-disclosure (s 9).

Retain all four base outputs. Add gross remuneration, component classification, excluded allowance and evidence, verified levy base, employee levy, employer capped base, employer levy, actual deduction and remittance reconciliation. The brief records legal currency, employer exception evidence and every assumption. The action list and review checklist include form/manner, actual due dates, discrepancies and refusal clearances. A refused case receives the base's refusal output, not a payable schedule.

## Completion checklist

Verify operative law and currency before applying any figure. Reconcile all remuneration components, check the threshold's equality and whole-remuneration treatment, keep the employer cap off the employee limb, preserve separate employer exemptions, verify allowance conditions, and reconcile deductions with both levy limbs. Check nil returns and both pay-period/monthly duties. Independently recompute all five illustrations and record every loaded refusal code. The eighteen base checks and professional sign-off still apply.

## Sources

| Source | URL | Read on |
|---|---|---|
| Universal Social Levy Act, R.S.A. c. U12 (unofficial online consolidation as at 31 December 2022): read for ss 1, 4 to 10, including the 3% limbs, XCD 2,000, XCD 12,000, XCD 400 and 225 allowances, 10-day deadlines and the s 10 penalty | https://laws.gov.ai/storage/pdfs/2022%20AXA%20Revised%20Statutes%20and%20Regulations/PDF%20(Acts)/U-R.S.A.s/U012-Universal%20Social%20Levy%20Act.pdf | 2026-11-14 |
| IRD, Universal Social Levy page: read for the 2026 statement of the 3% rates, EC$2,000 and EC$12,000 figures, the 10-day return and payment, the penalty and 1% interest, and the self-employed 6% | https://www.ird.gov.ai/Services/Tax/usl | 2026-11-14 |
| Law library disclaimer: read by Ryan Duguid for the unofficial status of online versions and possible omitted amendments | https://laws.gov.ai/?selected_page=disclaimer | 2026-10-11 |
| House of Assembly Hansard, 22 September 2026: read by Ryan Duguid for the defeat of Motion 13 on USL repeal | https://hansard.houseofassembly.ai/view_hansard?id=b5f59c2c-bdb9-11f1-8de9-26e8d4c008c4 | 2026-10-11 |

Not yet confirmed: amendments to the Universal Social Levy Act after 31 December 2022 and any regulations (the consolidation is unofficial and the official revised edition was not obtained); the statutory source and rate of the 1% monthly interest the IRD page states; the IRD page's "per month" wording of the XCD 2,000 penalty maximum against the statute's plain maximum; the self-employed levy (s 2 and s 7 and the IRD 6% statement); non-monthly conversion, concurrent employments and benefit valuation; operational rounding; record retention.
