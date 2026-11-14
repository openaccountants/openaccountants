---
name: us-net-operating-loss-172
description: "Compute a US federal net operating loss for tax year 2026 under section 172, for individuals and for C corporations. Covers the 80 percent of taxable income limit on post-2017 losses used in a year after 2020, the indefinite carryforward, the two-year farming-loss carryback and the waiver election, and the excess business loss under section 461(l) (USD 256,000, or USD 512,000 on a joint return) which is carried forward as an NOL. Partnerships and S corporations do not have their own NOL. Trigger on \"net operating loss\", \"NOL\", \"section 172\", \"Form 172\", \"Form 1045\", \"excess business loss\", \"Form 461\", \"farming loss carryback\"."
license: "AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)"
metadata:
  source: openaccountants
  openaccountants_url: "https://www.openaccountants.com/skills/us-net-operating-loss-172"
  jurisdiction: "US"
  tax_year: "2026"
  last_updated: "2026-11-13"
---

# US net operating loss under section 172, tax year 2026

> **Source-cited draft.** Built from 26 U.S.C. 172, the Instructions for Form 172 (revised December 2024), Rev. Proc. 2025-32, and Public Law 119-21 section 70601, read on 2026-11-13. No accountant has reviewed it. All outputs must be reviewed by a qualified tax professional before filing.

**Answer first.** A loss arising in a tax year after 2020 generally cannot be carried back. It carries forward indefinitely. In a year after 2020, the deduction for losses that arose after 2017 is limited to 80 percent of taxable income computed without the NOL deduction and without the section 199A and section 250 deductions. A farming loss can be carried back two years, and the taxpayer can waive that carryback. For a noncorporate taxpayer, a 2026 business loss larger than USD 256,000 (USD 512,000 on a joint return) is an excess business loss. The excess is disallowed in 2026 and carried forward as an NOL.

## Scope and who this is for

In scope: a net operating loss of an individual, an estate, a trust, or a C corporation for a loss year beginning in 2026, and the deduction in 2026 for an NOL carried to 2026. That includes the 80 percent limit, the farming carryback, and the section 461(l) excess business loss of a noncorporate taxpayer.

Out of scope, and where it goes:

| Topic | Skill |
| --- | --- |
| The qualified business income deduction that section 172(d)(8) removes when the NOL is computed | `us-qbi-deduction` |
| The corporate return the NOL deduction is claimed on | `us-form-1120-c-corp` |
| A section 382 ownership change, which can limit how much of a corporate NOL is used each year | refer; this skill does not compute the section 382 limit |
| State NOL rules, which often do not follow section 172 | the state's income tax skill |

## Ask the client first

1. **Who had the loss.** Individual (and filing status), estate, trust, or C corporation. A partnership or an S corporation does not carry its own NOL. The partner or shareholder uses their share.
2. **The year the loss arose,** and whether any of it is a farming loss. A nonfarm loss from a year after 2020 has no carryback.
3. **Other income in the loss year.** Nonbusiness income and nonbusiness deductions, capital gains and losses, and any section 1202 exclusion. These change the NOL of an individual.
4. **What is already carried in.** Pre-2018 NOLs (20-year life, no 80 percent limit) and post-2017 NOLs, each year's remaining amount, and the order they arose.
5. **For a noncorporate taxpayer,** total business income and total business deductions for 2026, after the at-risk and passive-loss limits. This is the excess business loss test.
6. **For a farmer who wants the carryback,** whether they will waive it. The waiver is due with the loss-year return, including extensions, and it is irrevocable.

## The method, step by step

### Rates, bands and thresholds

| Item | Amount | Who it applies to | Source |
| --- | --- | --- | --- |
| Deduction for post-2017 NOLs in a year beginning after 2020 | 80 percent of taxable income computed without the NOL deduction and without sections 199A and 250, after pre-2018 NOLs | Individuals and C corporations. Losses that arose before 2018 are not in this 80 percent cap | [26 U.S.C. 172(a)(2)](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap1-subchapB-partVI-sec172.htm) |
| Carryforward of a loss arising after 2017 | Indefinite, until used | Same. A loss that arose before 2018 carries forward 20 years | same |
| Carryback of a loss arising after 2020 | None, except a farming loss | A farming loss carries back 2 years. The taxpayer may waive the carryback by the loss-year due date, including extensions | [26 U.S.C. 172(b)(1)(B)](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap1-subchapB-partVI-sec172.htm) |
| Insurance company other than life | The 80 percent cap does not apply. Carryback 2 years and carryforward 20 years | An insurance company as defined in section 816(a), other than a life insurance company | [26 U.S.C. 172(f)](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap1-subchapB-partVI-sec172.htm) |
| Excess business loss threshold, 2026, other than a joint return | USD 256,000 | Noncorporate taxpayers. At-risk and passive-loss limits apply first | [Rev. Proc. 2025-32](https://www.irs.gov/pub/irs-drop/rp-25-32.pdf) |
| Excess business loss threshold, 2026, joint return | USD 512,000 | Married filing jointly | same |
| Form 1045 deadline | On or after the day the loss-year return is filed, and not later than one year after the end of the loss year | An individual, estate, or trust carrying a farming loss back and wanting a tentative refund | [Instructions for Form 172](https://www.irs.gov/instructions/i172) |

Section 461(l) is in force for 2026. Public Law 119-21 section 70601(a) removes the old expiration date for taxable years beginning after 31 December 2026. The 2026 dollar amounts above already reflect the inflation adjustment in section 70601(b), which applies to years beginning after 31 December 2025.

### Figure the 2026 NOL

An NOL is the excess of the deductions allowed for the year over gross income, after the modifications in section 172(d). Source: [26 U.S.C. 172(c) and (d)](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap1-subchapB-partVI-sec172.htm) and [Instructions for Form 172](https://www.irs.gov/instructions/i172).

1. **Individuals, estates, and trusts use Form 172, Part I.** Do not deduct an NOL from another year. Do not deduct more capital losses than capital gains, and add back any section 1202 exclusion. Do not deduct personal exemptions. Allow nonbusiness deductions only up to nonbusiness income. Casualty and theft losses are treated as business. A section 199A deduction is not allowed. A section 250 deduction is not allowed.
2. **Apply the excess business loss before the NOL of a noncorporate taxpayer.** Add up business deductions and business income (Schedule C, Schedule F, the business parts of Schedule E, and business gains and losses on Schedule D and Form 4797). The at-risk and passive-activity limits come first. The excess business loss is the amount by which business deductions exceed business income plus the threshold (USD 256,000, or USD 512,000 on a joint return). That excess is disallowed in 2026. It is reported as a positive amount on Schedule 1 and is an NOL carryover to the next year. It cannot be carried back. Source: [Instructions for Form 172, Excess Business Loss](https://www.irs.gov/instructions/i172).
3. **The loss that remains** after step 2, computed with the step 1 modifications, is the 2026 NOL. For a nonfarmer, carry it forward only. For a farmer, split out the farming loss: the smaller of the NOL and the loss computed from farming income and deductions only. Only the farming loss can be carried back.
4. **C corporations** use the same section 172(a) and (b) rules. The corporate modifications are the NOL deduction itself, the dividends-received deduction computed without the section 246(b) limit, and no section 250 deduction. A partnership or S corporation does not take an NOL deduction. Each partner or shareholder uses their own share of the entity's income and deductions on their own Form 172.
5. **Carry a farming loss back** to the second preceding year first (2024 for a 2026 loss), then to 2025, then forward. Waive the entire carryback by a statement on the original 2026 return, filed by the due date including extensions, that the taxpayer elects to waive the carryback under section 172(b). The election is irrevocable. There is no waiver after that date.

### Use an NOL in 2026, or in a later year

For a year beginning after 2020, the NOL deduction is:

1. Pre-2018 NOLs carried to the year, in full (they are outside the 80 percent cap), plus
2. The smaller of the post-2017 NOLs carried to the year, or 80 percent of the excess of taxable income (computed without the NOL deduction and without sections 199A and 250) over the pre-2018 NOLs in step 1.

Use the oldest loss first. An individual lists the carryforward as a negative figure on Schedule 1 (Form 1040) and attaches Form 172. An estate or trust uses Form 1041. Source: [26 U.S.C. 172(a)(2)](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap1-subchapB-partVI-sec172.htm).

**What is left to carry on.** Section 172(b)(2) absorbs the loss against modified taxable income of the earlier year, and that income is not below zero. For a year beginning after 2020, that modified taxable income is reduced by 20 percent of the excess described in section 172(a)(2)(B)(ii). Where there is no pre-2018 NOL, that excess is taxable income computed without the NOL deduction and without sections 199A and 250, and the 20 percent reduction leaves 80 percent of that income as the amount absorbed. The rest of the NOL stays alive. Do not treat the unused 20 percent as gone.

**Insurance companies other than life** deduct the sum of the carrybacks and carryovers, with no 80 percent cap, under section 172(f).

### Boundary and exception table

| Situation | Result |
| --- | --- |
| Loss year after 2020, not a farming loss | No carryback. Carry forward until used |
| Farming loss | Two-year carryback of the farming portion only, unless waived on a timely return |
| Pre-2018 NOL still alive | Allowed in full, ahead of the 80 percent computation. Twenty-year life, not indefinite |
| Post-2017 NOL used in a year after 2020 | Capped at 80 percent of the taxable-income base above |
| Excess business loss | Disallowed this year and carried forward as an NOL. Not a carryback |
| Partnership or S corporation | No entity-level NOL. The owner computes their own |
| Insurance company other than life | No 80 percent cap. Two-year carryback and 20-year carryforward |
| Married filing status changed across the loss year and the use year | Only the spouse who had the loss may use it. See the Form 172 instructions before splitting a joint year |

## Worked cases

**Case 1, a decision: carry a farming loss back, or waive it?** A single farmer has a 2026 NOL of USD 20,000, all of it a farming loss. The loss is under the USD 256,000 excess business loss threshold, so section 461(l) does not disallow any of it. Taxable income in 2024, computed without an NOL deduction and without sections 199A and 250, is USD 100,000. There is no pre-2018 NOL.

Carried back, the 2024 deduction is the smaller of USD 20,000 and 80 percent of USD 100,000. That is USD 20,000. Nothing is left to carry forward. Waived, the 2024 deduction from this loss is zero, and the whole USD 20,000 carries forward until it is used. The waiver has to be on the original 2026 return, by the due date including extensions. Carry the loss back unless the farmer has a reason to keep it for a later year. The tax in 2024 is recomputed with the USD 20,000 deduction; this skill stops at the deduction.

```oa-check
name: Farming loss, carry back or waive (2026 loss)
inputs:
  farming_nol: 20000
  income_2024: 100000
steps:
  - limit_2024: income_2024 * 0.80
  - deduction_if_carried_back: min(farming_nol, limit_2024)
  - deduction_if_waived: 0
  - carryforward_if_carried_back: farming_nol - deduction_if_carried_back
  - carryforward_if_waived: farming_nol
expected:
  deduction_if_carried_back: 20000.00
  deduction_if_waived: 0.00
  carryforward_if_carried_back: 0.00
  carryforward_if_waived: 20000.00
```

**Case 2, excess business loss, then the 80 percent limit.** A single filer has one 2026 Schedule C loss of USD 400,000 and no other income. The excess business loss is USD 400,000 minus USD 256,000 = USD 144,000. That USD 144,000 is disallowed in 2026 and is an NOL carryover to 2027. The remaining USD 256,000 is a 2026 NOL. It is not a farming loss, so it cannot be carried back. The total carried to 2027 is USD 400,000.

In 2027, taxable income computed without the NOL deduction and without sections 199A and 250 is USD 200,000. There is no pre-2018 NOL. The 2027 deduction is the smaller of USD 400,000 and 80 percent of USD 200,000, which is USD 160,000. Section 172(b)(2)(C) absorbs the same USD 160,000 (taxable income reduced by 20 percent of that income). The carryover to 2028 is USD 240,000.

```oa-check
name: Excess business loss and the 80 percent limit
inputs:
  business_loss: 400000
  threshold: 256000
  later_income: 200000
steps:
  - excess_business_loss: business_loss - threshold
  - allowed_loss: threshold
  - carry_to_next_year: excess_business_loss + allowed_loss
  - limit_80: later_income * 0.80
  - deduction: min(carry_to_next_year, limit_80)
  - absorbed: later_income - later_income * 0.20
  - still_carried: carry_to_next_year - absorbed
expected:
  excess_business_loss: 144000.00
  carry_to_next_year: 400000.00
  deduction: 160000.00
  still_carried: 240000.00
```

## When to refuse or refer

| Code | Situation | Action |
| --- | --- | --- |
| R-172-382 | A C corporation had an ownership change | Stop. Section 382 can limit the annual use. This skill does not compute it |
| R-172-REIT | The taxpayer is a REIT | Section 172(d)(6) changes the computation. Refer |
| R-172-LIFE | Life insurance company | The non-life rule in section 172(f) does not apply. Refer |
| R-172-MARITAL | Filing status is not the same in the loss year and the year of use | Use the Form 172 joint-and-separate steps. Do not give the whole joint NOL to one spouse |
| R-172-ENTITY | The question is an S corporation's or a partnership's own NOL | There is none. Compute the owner's NOL |
| R-172-STATE | A state return | Do not assume the state follows the federal 80 percent rule or the federal carryforward |

## Filing and payment

Individuals, estates, and trusts figure the NOL on Form 172. A carryforward is a negative amount on Schedule 1 (Form 1040), or on Form 1041 for an estate or trust, with Form 172 attached. A C corporation takes the deduction allowed by section 172 on its income tax return. The 2026 Form 1120 line for that deduction was not confirmed for this skill; see `us-form-1120-c-corp`.

A farming carryback can go on Form 1045 (a tentative refund) or on Form 1040-X. Form 1045 is filed on or after the date the 2026 return is filed, and not later than one year after the end of 2026. It is not a claim for credit or refund. If the IRS disallows it, the taxpayer still needs a claim, generally Form 1040-X. Form 1040-X for the carryback year is generally filed within 3 years after the due date, including extensions, of the return for the loss year. Filing Form 1040-X does not extend the two-year carryback window. Attach Form 172 to Form 1045 or Form 1040-X when it applies. If Form 1045 produces a refund the IRS later finds too large, the IRS may assess and collect the excess immediately.

The return is filed in the filer's ordinary way. The carryback refund, if Form 1045 is used, is a tentative adjustment of the earlier year, not a final assessment.

## Completion checklist

- Loss year identified, and farming loss split from any nonfarm loss.
- Section 172(d) modifications applied before the NOL is treated as final.
- Excess business loss tested for a noncorporate taxpayer, using USD 256,000 or USD 512,000.
- Post-2017 losses capped at 80 percent. Pre-2018 losses not put under that cap.
- Carryover reduced only by the absorbed amount under section 172(b)(2), including the 20 percent reduction.
- Farming waiver, if chosen, is on the original return by the due date including extensions.
- Form 172 attached. Form 1045 used only inside its one-year window.

## Sources

| Source | URL | Read on |
| --- | --- | --- |
| 26 U.S.C. 172 (govinfo, United States Code 2024). Read for (a)(2) the 80 percent limit, (b) the indefinite carryforward and the 2-year farming carryback, (b)(2)(C) the 20 percent absorption reduction, (d) the modifications, and (f) non-life insurance companies. | https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap1-subchapB-partVI-sec172.htm | 2026-11-13 |
| Instructions for Form 172 (December 2024). Read for who files, the 80 percent limit, farming losses, the waiver statement, Form 1045 timing, Schedule 1 reporting, and the excess business loss worksheet. | https://www.irs.gov/instructions/i172 | 2026-11-13 |
| Rev. Proc. 2025-32. Read for section 4.31: the section 461(l) amount for 2026 is $256,000 ($512,000 for joint returns). | https://www.irs.gov/pub/irs-drop/rp-25-32.pdf | 2026-11-13 |
| Public Law 119-21, section 70601. Read for making section 461(l) permanent for years beginning after 31 December 2026, and for the inflation-base change that applies to years beginning after 31 December 2025. | https://www.govinfo.gov/content/pkg/PLAW-119publ21/html/PLAW-119publ21.htm | 2026-11-13 |

Not yet confirmed: the 2026 Form 172 and the 2026 Instructions for Form 461 (the dollar amounts used here are from Rev. Proc. 2025-32, not from a 2026 Form 461); the 2026 Form 1120 line number for the NOL deduction; the 2026 Schedule 1 line number (the Form 172 instructions say to enter a negative figure on Schedule 1 and do not give a line).

## Today's figures and who stands behind this skill

This file is an AI skill (tax rules your AI follows) from OpenAccountants, copied on 2026-11-13. Rates, thresholds and deadlines change. For the current version of this skill, its official sources and the named accountant (if any) who stands behind it, call `get_skill` with slug `us-net-operating-loss-172` on the OpenAccountants connector (https://www.openaccountants.com/connect), or read https://www.openaccountants.com/skills/us-net-operating-loss-172. If neither is available, confirm every figure against the official source pages cited above before relying on it.
