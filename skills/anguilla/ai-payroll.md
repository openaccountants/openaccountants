---
name: ai-payroll
description: >
  Anguilla Universal Social Levy for ordinary monthly employee and employer
  remuneration, using the unofficial online consolidation dated 31 December 2022.
  Covers separate liabilities, the remuneration threshold, employer wage
  limit, conditional allowances, deductions, monthly reporting and payment.
  Use for Anguilla payroll, employee levy, employer levy, USL returns or
  monthly remuneration. Includes hypothetical positions, source verification
  and professional review controls. Self-employed levy, Social Security,
  non-monthly conversion and disputed employment require additional sources.
  Later amendments remain unverified. This source-cited draft requires the
  applicable period law before an engagement calculation and awaits review
  by a qualified professional in Anguilla.
jurisdiction: AI
category: payroll
tax_year: 2022
tax_year_notes: "Unofficial consolidation as at 31 December 2022; operative law requires verification"
tier: 2
last_updated: 2026-11-10
version: 0.4
review_status: pending_review
verified_by: pending
depends_on:
  - workflow-base
---

# Anguilla Universal Social Levy: employers and employees

## Scope

Establish the operative law, employment classification, monthly remuneration and employer status before calculating Universal Social Levy (USL). This companion covers an ordinary monthly employer/employee case and the supported statutory branches. Load `workflow-base` for the procedure, four outputs, questions and universal refusals. A qualified professional reviews each position before filing or payment.

Self-employed USL, Social Security contributions, non-monthly conversion, concurrent employments, disputed worker status, benefit valuation, assessments, penalties, appeals and cross-border employment need their complete applicable sources. A salary label or company-director title does not alone resolve every classification. Keep employer and employee liabilities separate.

Use the [Anguilla source register](references.md#social-security-contribution-guidance) for separate 2026 Social Security Board guidance. The register also records ordinary income tax scope and the tax residence programme. The USL examples below retain their 31 December 2022 source period.

## Period coverage and source currency

The online copy of the [*Universal Social Levy Act*, R.S.A. c. U12][U1] hosted by the government states that it shows the law as at 31 December 2022. It consolidates Act 26 of 2021, in force 1 January 2022, and Act 14 of 2022, in force 22 December 2022. This dated text was read on 11 October 2026. The [law library's disclaimer](https://laws.gov.ai/?selected_page=disclaimer) classifies its online versions as unofficial and warns that the revision may omit laws, regulations or amendments. Complete operative provisions, later amendments and applicable regulations remain unverified. The editing date does not establish current 2026 law.

Before an engagement calculation, obtain the applicable official law or authoritative confirmation of the required provisions. Verify the requested period's law, amendments, required regulations, currency and authority instructions. If the source conditions cannot be established, fire `R-AI-USL-PERIOD`; do not produce a payable estimate from this dated baseline. Apply that condition when using any figures or calculation section separately.

[Hansard for 22 September 2026][U3] records the defeat of Motion 13 seeking legislation to repeal USL. A motion's title cannot establish an enacted repeal. This record does not prove that there was no other later legislation.

## Period-specific figures

The table describes the 31 December 2022 consolidation. XCD is used in illustrations, consistent with the IRD's [USL guidance][U2]. Confirm currency for an actual assessment.

| Rule | Figure or timing | Primary provision |
|---|---|---|
| Employee USL | 3% of remuneration when the exemption does not apply | [Act][U1] s 4(1)(a) |
| Ordinary employer USL | 3% of remuneration, capped at XCD 12,000 for this ordinary monthly case | [Act][U1] s 4(1)(b) |
| Monthly remuneration exemption | Total remuneration at or below XCD 2,000 | [Act][U1] s 4(4) |
| Above the exemption | The exemption does not apply to the remuneration | [Act][U1] s 4(5) |
| Eligible telephone allowance | Exemption up to XCD 400, subject to the job and cost conditions | [Act][U1] s 4(6)(a), (7) |
| Eligible travel allowance | Exemption up to XCD 225, subject to the job and cost conditions | [Act][U1] s 4(6)(b), (7) |
| Deduction | At payment, for each pay period | [Act][U1] s 5(1) |
| Ordinary employer remittance | Within 10 days of the end of each pay period | [Act][U1] s 6(1) |
| Ordinary employer monthly return and remittance | Not later than 10 days after month end | [Act][U1] s 8(1) |
| Termination remittance | Within one month from the end of the termination month | [Act][U1] s 6(2) |

The XCD 12,000 limit belongs to the employer limb. The employee limb has no corresponding cap in s 4(1)(a). The exemption is not a deduction of XCD 2,000 from a larger wage. Non-monthly and multiple-employer cases require their own statutory reconciliation before either limit is used.

## Primary source library

Use the [2022 statutory consolidation][U1], [IRD USL guidance][U2] and the bounded [parliamentary record][U3]. Section 1(3) requires reading the Act with the applicable Inland Revenue Department Act provisions. This companion does not establish their complete record, interest, service or appeal rules. `references.md` records provenance, source gaps and the country topic matrix. A current website summary cannot silently replace an operative statutory provision.

## Position rules

### Classification and remuneration

[Act s 1][U1] includes company directors and working partners in the employee definition. Remuneration includes wages, salary, leave pay, acting payments, commission, fees, bonuses, perquisites other than service charge, and allowances. Section 5(3) includes remuneration in cash or kind. Resolve the legal category and valuation of a benefit; do not substitute net cash received or a bank deposit for remuneration.

Confirm each claimed allowance under s 4(6) and (7): the costs must relate directly to the nature of the job and be reasonably incurred in performing duties. Preserve its amount and evidence separately. A payroll label alone does not establish exemption. Resolve any allowance/threshold interaction, excess allowance or disputed service-charge character before calculating; the illustrations use uncomplicated facts safely above the threshold where relevant.

### Separate employee and employer calculations

For the established ordinary monthly case, let R be the verified remuneration after applicable statutory exclusions. [Act s 4][U1] supplies these branches:

1. If total remuneration satisfies the monthly exemption at or below XCD 2,000, the exemption applies. Record zero for both ordinary limbs.
2. If remuneration exceeds XCD 2,000, employee USL is R x 3 / 100 on the full remuneration. Do not deduct an initial exempt band or impose the employer cap on the employee.
3. For an ordinary liable employer, employer USL is the lesser of R and XCD 12,000, multiplied by 3 / 100.
4. Section 4(2) excludes the Government of Anguilla, Government Agencies, Non-Governmental Organisations and churches incorporated in Anguilla from the employer meaning for that section. Establish the particular employer's statutory status. This does not erase the employee's separate liability.

The remittance reconciliation identifies the employee deduction and employer liability separately, then adds the amounts due. USL is not Social Security. Do not combine its base or cap with an SSB contribution election, ceiling or contribution rate.

### Reporting and payment

[Act ss 5, 6 and 8][U1] require deduction at payment, employer pay-period remittance and monthly reporting/remittance. The ordinary monthly case must satisfy both ss 6(1) and 8(1). Section 8(3) requires a return by its ten-day pay-period deadline even if no remuneration was paid in a particular month. Confirm the prescribed or Comptroller-specified form and manner under s 8(1), and the operative online filing instructions before reporting.

Section 8(2) aggregates payments within a calendar month when remuneration is not paid monthly. That does not itself resolve all conversions and the interaction with the pay-period duty in s 6. Refer such cases under `R-AI-USL-SPECIAL`. Termination has the additional s 6(2) duty; do not treat it as a general extension for earlier liabilities.

For an employer's established good-faith overpayment, s 6(3) sets the excess against levy falling due subsequently. Reconcile actual remittance, error and later levy; do not assume a cash refund. Section 1(2) expressly excludes Interpretation and General Clauses Act s 6(1)(d) from time computation. Verify actual due dates and authority directions without assuming a weekend or holiday extension.

Self-employed deemed remuneration under s 2 uses the greater of elected prescribed remuneration and notional remuneration. Section 7 and the website's monthly payment summary differ in timing. Gross receipts, net profit and a Social Security category cannot supply an invented self-employed levy base or deadline. That calculation is excluded from this companion.

## Topical refusal catalogue

Use the message verbatim when its trigger applies. Include the universal `workflow-base` codes in the refusal trace.

| Code | Trigger | Output message |
|---|---|---|
| R-AI-USL-PERIOD | Applicable period law, currency or required source conditions cannot be established | I cannot calculate an Anguilla Universal Social Levy liability until the applicable period law and required source conditions are verified. Obtain the operative sources and professional review. |
| R-AI-USL-SPECIAL | Self-employment, Social Security, non-monthly or concurrent employment, disputed status, uncertain benefit valuation, assessment, penalty or appeal is needed | This Anguilla monthly employer and employee companion does not establish the rules needed for this case. Load the applicable primary provisions and a suitable companion, or consult an Anguilla tax professional. |
| R-AI-USL-AMBIGUITY | More than ten unresolved grouped questions remain after the base's filtering rules | The Anguilla levy records contain more unresolved grouped questions than this workflow can handle. Obtain a reconciled fact schedule and professional review before calculation. |

## Conservative defaults

These treatments apply to unresolved facts inside established law. Disclose the difference, use the base's questions and obtain review. Unknown legal scope remains Needs input.

| Missing fact | Treatment and disclosure | Primary condition |
|---|---|---|
| Job/cost evidence for an otherwise identified telephone or travel allowance is missing | Treat it as included remuneration pending evidence; disclose the alternative exemption and tax effect | [Act s 4(6), (7)][U1] |
| A claimed employer exception lacks proof of the employer's qualifying status | Use the ordinary employer limb as an Assumed position only where its legal classification is otherwise established; disclose the alternative and seek evidence | [Act s 4(1), (2)][U1] |
| Employment status, benefit value, total remuneration or the applicable legal period is unresolved | Needs input; fire the applicable topical refusal before engagement calculation | [Act ss 1, 4 and 5][U1] |

## Reviewer attention and question thresholds

Every position requires professional review. The companion's cash threshold for an automatic reviewer flag and a fact question is XCD 0: flag every nonzero difference. This review policy is not law. Always flag currency, period law, worker classification, employer status, allowance evidence and deadline uncertainty, including cases with no computed cash difference. Use the base's no-effect, description-answered, grouping and ten-question filters.

## Worked hypothetical positions

These examples apply only the stated 31 December 2022 statutory baseline to synthetic ordinary monthly facts. All amounts are XCD. Each case assumes the operative law and status needed for its illustration, and no other remuneration, benefit, adjustment, employment or contribution. Results are exact; an actual case needs its rounding and source checks.

| Position and supplied hypothetical facts | Separate calculation and result | Rule and review consequence |
|---|---|---|
| 1. Ordinary employer and employee; total remuneration 2,000 | Equality satisfies the exemption. Employee zero; employer zero; combined zero | [Act s 4(4)][U1]; verify complete monthly remuneration |
| 2. Ordinary employer and employee; remuneration 3,000 | Employee 3,000 x 3 / 100 = 90; employer 3,000 x 3 / 100 = 90; combined 180 | [Act s 4(1), (5)][U1]; no initial 2,000 deduction |
| 3. Ordinary employer and employee; remuneration 15,000 | Employee 15,000 x 3 / 100 = 450; employer 12,000 x 3 / 100 = 360; combined 810 | [Act s 4(1)][U1]; applying the employer cap to the employee would understate employee levy by 90 |
| 4. Employee of the established Government of Anguilla; remuneration 4,000 | Employee 4,000 x 3 / 100 = 120; exempt employer limb zero; combined 120 | [Act s 4(1), (2)][U1]; employer status does not exempt the employee |
| 5. Ordinary employer and employee; salary 5,000 plus telephone allowance 300, with the job/cost conditions proved | Allowance exemption 300; remuneration for this straightforward calculation 5,000; employee 150 and employer 150; combined 300. Without proven eligibility, remuneration 5,300 gives 159 each and combined 318; difference 18 | [Act s 4(1), (6), (7)][U1]; disclose missing eligibility evidence if the second treatment is used as a default |

## Output extension

Retain all four base outputs. Add gross remuneration, component classification, excluded allowance and evidence, verified levy base, employee levy, employer capped base, employer levy, actual deduction and remittance reconciliation. The brief records legal currency, employer exception evidence and every assumption. The action list and review checklist include form/manner, actual due dates, discrepancies and refusal clearances. A refused case receives the base's refusal output, not a payable schedule.

## Intake additions

Establish the requested period, qualified reviewer, employer category, worker classification, pay frequency, all remuneration components, allowance evidence, other employment, termination dates, deductions, actual payments, prior overpayments and authority notices. Obtain the current prescribed or Comptroller-specified filing instructions. Use the base's structured fact questions and action-list document requests. Never submit identity documents, tax identifiers or bank details through this guide.

## Additional self-checks

Verify operative law and currency before applying any figure. Reconcile all remuneration components, check the threshold's equality and whole-remuneration treatment, keep the employer cap off the employee limb, preserve separate employer exemptions, verify allowance conditions, and reconcile deductions with both levy limbs. Check nil returns and both pay-period/monthly duties. Independently recompute all five illustrations and record every loaded refusal code. The eighteen base checks and professional sign-off still apply.

## Currency and revisions

Version 0.3, edited 12 October 2026. Corrects the fork referral notice. Monthly employer/employee reference using the unofficial online consolidation dated 31 December 2022. Records the library's provenance limitation and requires official law or authoritative confirmation before an engagement calculation. Complete operative provisions, post-2022 amendments, all applicable regulations, benefit valuation, operational rounding, record retention and full special-case compliance remain unverified. This companion is a Tier 2 draft pending professional review.

[U1]: https://laws.gov.ai/storage/pdfs/2022%20AXA%20Revised%20Statutes%20and%20Regulations/PDF%20(Acts)/U-R.S.A.s/U012-Universal%20Social%20Levy%20Act.pdf
[U2]: https://www.ird.gov.ai/Services/Tax/usl
[U3]: https://hansard.houseofassembly.ai/view_hansard?id=b5f59c2c-bdb9-11f1-8de9-26e8d4c008c4

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
