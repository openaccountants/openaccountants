---
name: us-new-deductions-tips-overtime-senior-car-loan
description: "Compute the four individual deductions for tax years 2025 through 2028 under Public Law 119-21: qualified tips (section 224), qualified overtime compensation (section 225), the senior deduction (section 151(d)(5)(C)), and qualified passenger vehicle loan interest (section 163(h)(4)). Covers the caps, the modified-AGI phase-outs, who qualifies, the social security number and joint-return conditions, and how the 2025 Schedule 1-A computes each one. On the 2025 Schedule 1-A the total goes to Form 1040 line 13b, or Form 1040-NR line 13c. Trigger on \"no tax on tips\", \"no tax on overtime\", \"senior deduction\", \"car loan interest deduction\", \"Schedule 1-A\". The wider 2026 change list is in us-2026-federal-tax-changes. Federal only."
license: "AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)"
metadata:
  source: openaccountants
  openaccountants_url: "https://www.openaccountants.com/skills/us-new-deductions-tips-overtime-senior-car-loan"
  jurisdiction: "US"
  tax_year: "2026"
  last_updated: "2026-11-13"
---

# Tips, overtime, senior, and car loan deductions, tax years 2025 to 2028

> **Source-cited draft.** Built from Public Law 119-21 on govinfo.gov (sections 70103, 70201, 70202, and 70203), IRS Fact Sheet FS-2026-04, and the 2025 Schedule 1-A (Form 1040), read on 2026-11-13. No accountant has reviewed it. All outputs must be reviewed by a qualified tax professional before filing.

**Answer first.** For 2026 these four deductions are allowed whether or not the person itemizes. Tips are capped at **USD 25,000** per return. Overtime is capped at **USD 12,500** (USD 25,000 on a joint return), and only the Fair Labor Standards Act premium counts. Each person who is 65 or over before year end gets **USD 6,000**. Car loan interest is capped at **USD 10,000**. A married person gets the tips, overtime, and senior deductions only on a joint return. Tips and overtime shrink by USD 100 for each full USD 1,000 of modified AGI over USD 150,000 (USD 300,000 joint). The senior deduction shrinks by 6 percent of modified AGI over USD 75,000 (USD 150,000 joint). Car loan interest shrinks by USD 200 for each USD 1,000, or part of USD 1,000, of modified AGI over USD 100,000 (USD 200,000 joint).

## Scope and who this is for

In scope: the 2026 computation of these four deductions for an individual, and the same statutory amounts for 2025, 2027, and 2028. They are claimed on Schedule 1-A (Form 1040).

Out of scope, and where it goes:

| Topic | Skill |
| --- | --- |
| The rest of the 2026 federal changes (rates, SALT cap, QBI, bonus depreciation) | `us-2026-federal-tax-changes` |
| Where Schedule 1-A sits in a full Form 1040 assembly | `us-federal-return-assembly` |
| The additional standard deduction for being 65 or blind | `us-federal-income-tax-return-1040` |
| Business interest that is not a personal-use car loan | the Schedule C or Schedule E skill for that activity |

## Ask the client first

1. **Filing status**, and whether a married couple will file jointly. Separate returns get none of the tips, overtime, or senior deduction.
2. **Modified AGI.** Adjusted gross income plus any income excluded under section 911, 931, or 933. The same definition is used for all four deductions.
3. **Qualified tips**, the occupation, and whether the tips are on a W-2, a 1099, another furnished statement, or Form 4137. For a self-employed person, the net income of that business.
4. **Qualified overtime**, and only the premium above the regular rate that the Fair Labor Standards Act requires. The whole time-and-a-half payment is not the deduction.
5. **Age at year end**, and a social security number for each person claiming the senior deduction. This deduction is not the additional standard deduction for age.
6. **The car loan:** date the debt was incurred, first lien, personal use, new vehicle, final assembly in the United States, gross vehicle weight rating under 14,000 pounds, and the vehicle identification number. Interest already deducted on Schedule C, E, or F is not deducted again here.

## The method, step by step

### Rates, bands and thresholds

The amounts are not indexed. They apply to taxable years beginning after 31 December 2024. Tips and overtime end for a taxable year beginning after 31 December 2028. The senior deduction is allowed for a taxable year beginning before 1 January 2029. Car loan interest is allowed for taxable years beginning after 31 December 2024 and before 1 January 2029, and only on debt incurred after 31 December 2024.

| Item | Amount, 2025 to 2028 | Source |
| --- | --- | --- |
| Qualified tips, maximum deduction per return | USD 25,000 | [Public Law 119-21, section 224(b)(1)](https://www.govinfo.gov/content/pkg/PLAW-119publ21/html/PLAW-119publ21.htm) |
| Tips and overtime, modified AGI where the reduction starts, other than joint | USD 150,000 | [Public Law 119-21, section 224(b)(2)](https://www.govinfo.gov/content/pkg/PLAW-119publ21/html/PLAW-119publ21.htm) |
| Tips and overtime, modified AGI where the reduction starts, joint return | USD 300,000 | [Public Law 119-21, section 224(b)(2)](https://www.govinfo.gov/content/pkg/PLAW-119publ21/html/PLAW-119publ21.htm) |
| Tips and overtime, reduction for each USD 1,000 of modified AGI over the start | USD 100 | [Public Law 119-21, section 224(b)(2)](https://www.govinfo.gov/content/pkg/PLAW-119publ21/html/PLAW-119publ21.htm) |
| Qualified overtime, maximum, other than a joint return | USD 12,500 | [Public Law 119-21, section 225(b)(1)](https://www.govinfo.gov/content/pkg/PLAW-119publ21/html/PLAW-119publ21.htm) |
| Qualified overtime, maximum on a joint return | USD 25,000 | [Public Law 119-21, section 225(b)(1)](https://www.govinfo.gov/content/pkg/PLAW-119publ21/html/PLAW-119publ21.htm) |
| Senior deduction, per person age 65 before year end | USD 6,000 | [Public Law 119-21, section 151(d)(5)(C)](https://www.govinfo.gov/content/pkg/PLAW-119publ21/html/PLAW-119publ21.htm) |
| Senior deduction, modified AGI where the reduction starts, other than joint | USD 75,000 | [Public Law 119-21, section 151(d)(5)(C)](https://www.govinfo.gov/content/pkg/PLAW-119publ21/html/PLAW-119publ21.htm) |
| Senior deduction, modified AGI where the reduction starts, joint return | USD 150,000 | [Public Law 119-21, section 151(d)(5)(C)](https://www.govinfo.gov/content/pkg/PLAW-119publ21/html/PLAW-119publ21.htm) |
| Senior deduction, reduction rate | 6 percent | [Public Law 119-21, section 151(d)(5)(C)](https://www.govinfo.gov/content/pkg/PLAW-119publ21/html/PLAW-119publ21.htm) |
| Qualified passenger vehicle loan interest, maximum | USD 10,000 | [Public Law 119-21, section 163(h)(4)](https://www.govinfo.gov/content/pkg/PLAW-119publ21/html/PLAW-119publ21.htm) |
| Car loan interest, modified AGI where the reduction starts, other than joint | USD 100,000 | [Public Law 119-21, section 163(h)(4)](https://www.govinfo.gov/content/pkg/PLAW-119publ21/html/PLAW-119publ21.htm) |
| Car loan interest, modified AGI where the reduction starts, joint return | USD 200,000 | [Public Law 119-21, section 163(h)(4)](https://www.govinfo.gov/content/pkg/PLAW-119publ21/html/PLAW-119publ21.htm) |
| Car loan interest, reduction for each USD 1,000 or part over the start | USD 200 | [Public Law 119-21, section 163(h)(4)](https://www.govinfo.gov/content/pkg/PLAW-119publ21/html/PLAW-119publ21.htm) |

### Qualified tips (section 224)

The deduction is the qualified tips received during the year and included on the required statement, or reported on Form 4137, then limited.

Qualified tips are cash tips (including charged tips and, for an employee, tips under a tip-sharing arrangement) received in an occupation that customarily and regularly received tips on or before 31 December 2024, as the Secretary provides. A tip counts only if it is paid voluntarily, with no consequence for not paying, is not negotiated, and is set by the payer. Tips received in a specified service trade or business, as section 199A(d)(2) defines it, do not count. For a person who is not an employee, tips count only up to the point that the gross income of that business (including the tips) exceeds the deductions allocable to that business, other than this deduction.

The return must include the social security number of the individual who received the tips. A married person must file a joint return. IRS Fact Sheet FS-2026-04 says the occupation is one listed at IRS.gov/TippedOccupations and that the social security number must be valid for employment.

Computation, in the order of the 2025 Schedule 1-A:

1. Start with the qualified tips.
2. Cap at USD 25,000. There is no separate, higher joint cap.
3. If modified AGI is over USD 150,000 (USD 300,000 joint), divide the excess by USD 1,000 and drop the fraction. The 2025 Schedule 1-A says to decrease a result that is not a whole number to the next lower whole number. Multiply that whole number by USD 100.
4. Subtract. Not below zero.

### Qualified overtime (section 225)

Use the same steps, with two differences. The cap is USD 12,500, or USD 25,000 on a joint return. The amount is only overtime required by section 7 of the Fair Labor Standards Act that is in excess of the regular rate. It is the premium, not the full overtime wage. Qualified tips are excluded. The same social security number and joint-return rules apply. The phase-out thresholds and the USD 100 per full USD 1,000 are the same as for tips. The 2025 Schedule 1-A uses the same "next lower whole number" step in Part III.

### Senior deduction (section 151(d)(5)(C))

A qualified individual is the taxpayer, if age 65 before the close of the year, and, on a joint return, the spouse if that spouse is also 65 before year end. The deduction is USD 6,000 for each such person. The return must include that person's social security number. A married person must file jointly.

Reduce the USD 6,000 (for each person) by 6 percent of modified AGI over USD 75,000, or over USD 150,000 on a joint return. Not below zero. This is a percentage of the whole excess, not a per-thousand step. It is allowed in addition to the additional standard deduction for age. Do not substitute one for the other. The additional standard deduction amounts are in `us-federal-income-tax-return-1040`.

On a joint return the statute reduces "the $6,000 amount" by 6 percent of the excess. The 2025 Schedule 1-A computes that reduced amount once (lines 33 to 35) and then lets each qualifying spouse enter that same amount (lines 36a and 36b). Two qualifying spouses each get the reduced USD 6,000. They do not share one reduction of a combined USD 12,000.

### Car loan interest (section 163(h)(4))

Qualified interest is interest paid or accrued on debt incurred after 31 December 2024 to buy an applicable passenger vehicle for personal use, secured by a first lien on that vehicle. The vehicle's original use must start with the taxpayer. It must be a car, minivan, van, sport utility vehicle, pickup truck, or motorcycle, manufactured primarily for use on public streets, with at least two wheels, a gross vehicle weight rating under 14,000 pounds, and final assembly in the United States. Final assembly is the process at the plant from which the vehicle is delivered to a dealer with the component parts necessary for its mechanical operation.

Excluded: fleet loans, a commercial vehicle not used personally, lease financing, a salvage title, a vehicle bought for scrap or parts, and a loan from a person related under section 267(b) or 707(b)(1). A refinance of a qualifying loan counts only up to the refinanced balance, and it must keep a first lien. The vehicle identification number must be on the return. Interest deducted on Schedule C, E, or F is not entered again in the Schedule 1-A column.

Computation, in the order of the 2025 Schedule 1-A:

1. Cap the qualified interest at USD 10,000.
2. If modified AGI is over USD 100,000 (USD 200,000 joint), divide the excess by USD 1,000 and round a fraction up. The statute says "or portion thereof". The 2025 Schedule 1-A says to increase a result that is not a whole number to the next higher whole number.
3. Multiply that whole number by USD 200 and subtract. Not below zero.

### Where it goes on the return

The 2025 Schedule 1-A says to add lines 13, 21, 30, and 37 and enter the total on Form 1040 or 1040-SR, line 13b, or on Form 1040-NR, line 13c. Part I of that form builds modified AGI from Form 1040 line 11b plus excluded Puerto Rico income, Form 2555 lines 45 and 50, and Form 4563 line 15. Those are the section 911, 931, and 933 add-backs. Attach Schedule 1-A to Form 1040, 1040-SR, or 1040-NR. The deductions are allowed whether the person itemizes or takes the standard deduction, because section 63(b) lists them for non-itemizers.

## Boundary and exception table

| Situation | Treatment |
| --- | --- |
| Married filing separately | No tips deduction, no overtime deduction, no senior deduction |
| Modified AGI at or under the start | No phase-out. The cap still applies |
| Tips in a specified service trade or business | Not qualified tips |
| Self-employed tips above the net income of that business | The excess is not deducted |
| Overtime the Fair Labor Standards Act does not require | Not qualified overtime. Only the premium counts |
| Senior deduction and the additional standard deduction for age | Both can apply. They are different amounts |
| Loan incurred on or before 31 December 2024 | No car loan deduction, including for 2026 interest on that old loan |
| Final assembly outside the United States, or a lease | No deduction |
| Interest already deducted on Schedule C, E, or F | Do not deduct it again on Schedule 1-A |
| A partial thousand of modified AGI | Drop the fraction for tips and overtime. Count it for car loan interest |

## Worked cases

**Case 1, a decision: joint return or separate returns.** A married couple has qualified tips of USD 8,000. Both have social security numbers, the occupation qualifies, and there is no section 911, 931, or 933 exclusion. Modified AGI on a joint return would be USD 160,000. That is under USD 300,000, and USD 8,000 is under the USD 25,000 cap, so the tips deduction on a joint return is USD 8,000.

If they file separate returns, section 224(f) says the deduction applies only when they file jointly. The tips deduction is zero. Overtime and the senior deduction have the same joint-return condition. The figure that decides the choice, before any other difference between joint and separate rates, is USD 8,000 of deduction or none.

```oa-check
name: Tips deduction, joint return against separate returns (2026)
inputs:
  qualified_tips: 8000
  joint_magi: 160000
  cap: 25000
  joint_threshold: 300000
steps:
  - capped: min(qualified_tips, cap)
  - excess: max(joint_magi - joint_threshold, 0)
  - thousands: floor(excess / 1000)
  - reduction: thousands * 100
  - deduction_joint: max(capped - reduction, 0)
  - deduction_separate: 0
expected:
  capped: 8000.00
  excess: 0.00
  thousands: 0.00
  reduction: 0.00
  deduction_joint: 8000.00
  deduction_separate: 0.00
```

**Case 2, car loan interest with a partial thousand.** A single filer paid USD 4,200 of otherwise qualified passenger vehicle loan interest in 2026. The loan was incurred in March 2025, it is a first lien, the vehicle is new, personal use, final assembly was in the United States, and the vehicle identification number is on the return. Modified AGI is USD 112,600. No section 911, 931, or 933 exclusion.

The interest is under the USD 10,000 cap, so the starting amount is USD 4,200. Modified AGI exceeds USD 100,000 by USD 12,600. That is 12 full thousands and a portion, so the portion rule counts 13. The reduction is 13 times USD 200, which is USD 2,600. The deduction is USD 4,200 minus USD 2,600, which is USD 1,600.

```oa-check
name: Car loan interest, a partial thousand of modified AGI (2026)
inputs:
  interest: 4200
  magi: 112600
  cap: 10000
  threshold: 100000
steps:
  - capped: min(interest, cap)
  - excess: max(magi - threshold, 0)
  - thousands: ceil(excess / 1000)
  - reduction: thousands * 200
  - deduction: max(capped - reduction, 0)
expected:
  capped: 4200.00
  excess: 12600.00
  thousands: 13.00
  reduction: 2600.00
  deduction: 1600.00
```

A senior check on the same modified-AGI idea, for a single person age 67 with modified AGI of USD 100,000: the excess over USD 75,000 is USD 25,000, 6 percent is USD 1,500, and the deduction is USD 6,000 minus USD 1,500, which is USD 4,500. That uses the percentage in the statute, not the per-thousand step.

## When to refuse or refer

| Code | Situation | Action |
| --- | --- | --- |
| R-DED-OCC | The tipped occupation is not clearly one the Secretary has listed | Do not treat the tips as qualified. Read the list at IRS.gov/TippedOccupations |
| R-DED-SSTB | The tips may be from a specified service trade or business | Resolve section 199A(d)(2) before deducting |
| R-DED-FLSA | The overtime may be a contract premium the Fair Labor Standards Act does not require | Do not count it. Only the required premium is qualified |
| R-DED-VIN | Final assembly or the vehicle identification number is unknown | No car loan deduction until both are known |
| R-DED-MFS | The client wants these deductions and is married filing separately | The tips, overtime, and senior deductions are not allowed |
| R-DED-BIZ | The interest is business interest, or part of it was deducted on Schedule C, E, or F | Split it. Do not deduct the same interest twice |

## Filing and payment

Complete Schedule 1-A and attach it to the 2026 Form 1040, 1040-SR, or 1040-NR. The 2025 Schedule 1-A puts the total on Form 1040 or 1040-SR line 13b, and on Form 1040-NR line 13c. Keep the W-2, 1099, or Form 4137 that reports the tips or the overtime premium, and the lender's interest figure and the vehicle identification number for the car loan. These deductions do not change withholding by themselves. Estimated tax and withholding are in `us-quarterly-estimated-tax`.

The failure-to-file addition on the income-tax return is 5 percent of the tax per month or fraction, not over 25 percent, and the failure-to-pay addition is 0.5 percent per month or fraction, not over 25 percent, unless the failure is due to reasonable cause and not willful neglect. Source: [26 U.S.C. 6651(a)](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleF-chap68-subchapA-partI-sec6651.htm).

## Completion checklist

- Filing status is joint if the person is married and any of the tips, overtime, or senior deductions is claimed.
- Modified AGI adds back section 911, 931, and 933 exclusions before any phase-out.
- Tips are capped at USD 25,000, then reduced by USD 100 per full thousand of excess modified AGI, fraction dropped.
- Overtime is only the Fair Labor Standards Act premium, capped at USD 12,500 or USD 25,000 joint, with the same phase-out.
- Each person age 65 or over is tested separately at USD 6,000, then reduced by 6 percent of the excess.
- Car loan interest uses the portion rule (round the thousand up) and the vehicle identification number is on the return.
- Schedule 1-A total is carried to the return, and no interest is deducted twice.

## Sources

| Source | URL | Read on |
| --- | --- | --- |
| Public Law 119-21 (govinfo). Read for section 70201 (section 224: USD 25,000 cap, USD 100 per USD 1,000 over USD 150,000 or USD 300,000 joint, qualified tips, specified service trades, self-employed net-income limit, social security number, joint return, termination after 31 December 2028, effective for years beginning after 31 December 2024), section 70202 (section 225: the USD 12,500 and USD 25,000 caps and the Fair Labor Standards Act premium), section 70203 (section 163(h)(4): USD 10,000, USD 200 per USD 1,000 or portion, vehicle tests, refinance, related lenders), and section 70103 (section 151(d)(5)(C): USD 6,000, 6 percent, USD 75,000 and USD 150,000, years beginning before 1 January 2029). | https://www.govinfo.gov/content/pkg/PLAW-119publ21/html/PLAW-119publ21.htm | 2026-11-13 |
| IRS Fact Sheet FS-2026-04 (March 2026). Read for Schedule 1-A as the form for all four deductions, the occupation list pointer, social security numbers valid for employment on tips and overtime, and the joint-return condition. | https://www.irs.gov/newsroom/schedule-1-a-additional-deductions-what-to-know-about-the-new-form | 2026-11-13 |
| Schedule 1-A (Form 1040) 2025. Read for Part I modified AGI (line 11b plus Form 2555 and Form 4563), Part II line 11 (decrease a partial thousand), Part III line 19 (same), Part IV line 28 (increase a partial thousand), Part V lines 33 to 37 (6 percent of the excess, then the same reduced amount for each spouse), and line 38 (Form 1040 line 13b, or Form 1040-NR line 13c). | https://www.irs.gov/pub/irs-pdf/f1040s1a.pdf | 2026-11-13 |
| 26 U.S.C. 6651 (govinfo, U.S. Code 2024 edition). Read for (a)(1) 5 percent a month capped at 25 percent and (a)(2) 0.5 percent a month capped at 25 percent. | https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleF-chap68-subchapA-partI-sec6651.htm | 2026-11-13 |

Not yet confirmed: the 2026 Schedule 1-A was not published as the page read, so a 2026 birth-date cutoff and any 2026 social security wage-base figure printed on a tips line are not stated. The 2025 form's wage-base check (W-2 box 5 over USD 176,100) is a 2025 amount and is not used for 2026. The contents of the tipped-occupation list at IRS.gov/TippedOccupations were not read occupation by occupation. The meaning of "social security number" in section 24(h)(7), beyond the fact sheet's "valid for employment" for tips and overtime, was not re-read.

## Today's figures and who stands behind this skill

This file is an AI skill (tax rules your AI follows) from OpenAccountants, copied on 2026-11-13. Rates, thresholds and deadlines change. For the current version of this skill, its official sources and the named accountant (if any) who stands behind it, call `get_skill` with slug `us-new-deductions-tips-overtime-senior-car-loan` on the OpenAccountants connector (https://www.openaccountants.com/connect), or read https://www.openaccountants.com/skills/us-new-deductions-tips-overtime-senior-car-loan. If neither is available, confirm every figure against the official source pages cited above before relying on it.
