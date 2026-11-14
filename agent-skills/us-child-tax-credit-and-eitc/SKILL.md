---
name: us-child-tax-credit-and-eitc
description: "Compute the 2026 child tax credit and the 2026 earned income credit. The child tax credit is USD 2,200 per qualifying child under 17, with a refundable cap of USD 1,700, a phase-out of USD 50 per USD 1,000 of modified AGI over USD 200,000 (USD 400,000 joint), and the social security number rules in section 24(h)(7) as amended by Public Law 119-21. The earned income credit uses the 2026 earned-income amounts, maximums, and phase-out thresholds in Rev. Proc. 2025-32, the statutory credit and phase-out percentages, the qualifying-child tests, and the USD 12,200 investment-income cliff. Trigger on \"child tax credit\", \"additional child tax credit\", \"Schedule 8812\", \"earned income credit\", \"EITC\", \"qualifying child\". Federal only."
license: "AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)"
metadata:
  source: openaccountants
  openaccountants_url: "https://www.openaccountants.com/skills/us-child-tax-credit-and-eitc"
  jurisdiction: "US"
  tax_year: "2026"
  last_updated: "2026-11-13"
---

# Child tax credit and earned income credit, tax year 2026

> **Source-cited draft.** Built from 26 U.S.C. 24, 32, and 152 (U.S. Code, 2024 edition, on govinfo.gov), Public Law 119-21 section 70104, and Rev. Proc. 2025-32, read on 2026-11-13. No accountant has reviewed it. All outputs must be reviewed by a qualified tax professional before filing.

**Answer first.** For 2026 the child tax credit is **USD 2,200** for each qualifying child who has not attained age 17. It falls by USD 50 for each USD 1,000, or fraction, of modified AGI over **USD 200,000** (USD 400,000 on a joint return). The refundable additional child tax credit is limited to **USD 1,700** per child, and also to 15 percent of earned income over USD 2,500. The earned income credit maximums are **USD 4,427** (one child), **USD 7,316** (two), **USD 8,231** (three or more), and **USD 664** (none). The credit is zero if investment income exceeds **USD 12,200**.

## Scope and who this is for

In scope: the 2026 child tax credit, the additional child tax credit, the USD 500 credit for other dependents, and the earned income credit, for a U.S. citizen or resident individual.

Out of scope, and where it goes:

| Topic | Skill |
| --- | --- |
| A nonresident alien's return, including the limited child tax credit for residents of Canada, Mexico, India, and South Korea | `us-form-1040-nr-nonresident-return` |
| The foreign earned income exclusion, which blocks the additional child tax credit and the earned income credit | `us-foreign-earned-income-2555` |
| The rest of Form 1040 | `us-federal-income-tax-return-1040` |

## Ask the client first

1. **Each child:** age at the end of 2026, relationship, whether the child lived with the client for more than half the year, student or permanently and totally disabled, and whether the child provided more than half of their own support.
2. **Who else might claim the child.** If two people could, the tie-breaker in section 152(c)(4) decides. Do not claim the child on both returns.
3. **Filing status**, and whether a married client will file jointly. The earned income credit generally requires a joint return.
4. **Earned income and adjusted gross income**, separately. The earned income credit uses the greater of the two once phase-out starts.
5. **Investment income:** taxable interest and dividends, tax-exempt interest, capital gain net income, rents and royalties not from a business, and net passive income.
6. **Social security numbers**, and whether each one was issued by the due date of the return. A person who claims the foreign earned income exclusion is not eligible for the earned income credit, and the additional child tax credit is off.

## The method, step by step

### Rates, bands and thresholds

| Item | Amount, 2026 | Source |
| --- | --- | --- |
| Child tax credit, maximum per qualifying child under 17 | USD 2,200 | [Rev. Proc. 2025-32, section 4.05](https://www.irs.gov/pub/irs-drop/rp-25-32.pdf) |
| Additional child tax credit, refundable cap per child | USD 1,700 | [Rev. Proc. 2025-32, section 4.05](https://www.irs.gov/pub/irs-drop/rp-25-32.pdf) |
| Child tax credit phase-out, per USD 1,000 or fraction of modified AGI over the threshold | USD 50 | [26 U.S.C. 24(b)](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap1-subchapA-partIV-subpartA-sec24.htm) |
| Child tax credit phase-out starts, joint return | USD 400,000 | [26 U.S.C. 24(h)(3)](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap1-subchapA-partIV-subpartA-sec24.htm) |
| Child tax credit phase-out starts, any other return | USD 200,000 | [26 U.S.C. 24(h)(3)](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap1-subchapA-partIV-subpartA-sec24.htm) |
| Earned income floor for the additional child tax credit | USD 2,500 | [26 U.S.C. 24(h)(6)](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap1-subchapA-partIV-subpartA-sec24.htm) |
| Additional child tax credit, percent of earned income over that floor | 15 percent | [26 U.S.C. 24(d)(1)(B)](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap1-subchapA-partIV-subpartA-sec24.htm) |
| Credit for each dependent who is not a qualifying child under 17 | USD 500 | [26 U.S.C. 24(h)(4)](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap1-subchapA-partIV-subpartA-sec24.htm) |
| Earned income credit, maximum, three or more qualifying children | USD 8,231 | [Rev. Proc. 2025-32, section 4.06](https://www.irs.gov/pub/irs-drop/rp-25-32.pdf) |
| Earned income credit, maximum, two qualifying children | USD 7,316 | [Rev. Proc. 2025-32, section 4.06](https://www.irs.gov/pub/irs-drop/rp-25-32.pdf) |
| Earned income credit, maximum, one qualifying child | USD 4,427 | [Rev. Proc. 2025-32, section 4.06](https://www.irs.gov/pub/irs-drop/rp-25-32.pdf) |
| Earned income credit, maximum, no qualifying child | USD 664 | [Rev. Proc. 2025-32, section 4.06](https://www.irs.gov/pub/irs-drop/rp-25-32.pdf) |
| Earned income amount, one child | USD 13,020 | [Rev. Proc. 2025-32, section 4.06](https://www.irs.gov/pub/irs-drop/rp-25-32.pdf) |
| Earned income amount, two or more children | USD 18,290 | [Rev. Proc. 2025-32, section 4.06](https://www.irs.gov/pub/irs-drop/rp-25-32.pdf) |
| Earned income amount, no qualifying child | USD 8,680 | [Rev. Proc. 2025-32, section 4.06](https://www.irs.gov/pub/irs-drop/rp-25-32.pdf) |
| Phase-out starts, one or more children, not a joint return | USD 23,890 | [Rev. Proc. 2025-32, section 4.06](https://www.irs.gov/pub/irs-drop/rp-25-32.pdf) |
| Phase-out starts, one or more children, joint return | USD 31,160 | [Rev. Proc. 2025-32, section 4.06](https://www.irs.gov/pub/irs-drop/rp-25-32.pdf) |
| Phase-out starts, no qualifying child, not a joint return | USD 10,860 | [Rev. Proc. 2025-32, section 4.06](https://www.irs.gov/pub/irs-drop/rp-25-32.pdf) |
| Phase-out starts, no qualifying child, joint return | USD 18,140 | [Rev. Proc. 2025-32, section 4.06](https://www.irs.gov/pub/irs-drop/rp-25-32.pdf) |
| Credit percentage, one child; phase-out percentage | 34 percent; 15.98 percent | [26 U.S.C. 32(b)(1)](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap1-subchapA-partIV-subpartC-sec32.htm) |
| Credit percentage, two children; phase-out percentage | 40 percent; 21.06 percent | [26 U.S.C. 32(b)(1)](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap1-subchapA-partIV-subpartC-sec32.htm) |
| Credit percentage, three or more children; phase-out percentage | 45 percent; 21.06 percent | [26 U.S.C. 32(b)(1)](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap1-subchapA-partIV-subpartC-sec32.htm) |
| Credit percentage and phase-out percentage, no qualifying child | 7.65 percent | [26 U.S.C. 32(b)(1)](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap1-subchapA-partIV-subpartC-sec32.htm) |
| No earned income credit if investment income exceeds | USD 12,200 | [Rev. Proc. 2025-32, section 4.06](https://www.irs.gov/pub/irs-drop/rp-25-32.pdf) |

Public Law 119-21 section 70104 replaced the USD 2,000 credit amount with USD 2,200 and removed the rule that stopped section 24(h) before 2026. Rev. Proc. 2025-32 then says the 2026 maximum is still USD 2,200, and the refundable amount used in section 24(d)(1)(A) is USD 1,700. The USD 400,000 and USD 200,000 thresholds, the USD 50 step, the USD 2,500 floor, and the USD 500 other-dependent credit were not amended by that section. The earned income credit dollar amounts are the 2026 indexed figures. The percentages are not indexed.

### Qualifying child

Section 152(c) requires all of the following. Relationship: a child or descendant of a child, or a brother, sister, stepbrother, or stepsister, or a descendant of any of them. Abode: the same principal place of abode as the taxpayer for more than half the year. Age: younger than the taxpayer, and under 19 at year end, or a student under 24, or permanently and totally disabled at any time during the year. Support: the child did not provide more than half of their own support. Joint return: the child did not file a joint return, other than a claim for refund only.

For the child tax credit, section 24(c) adds a harder age test: the child has not attained age 17. A 17-year-old can still be a dependent. The credit for that dependent is USD 500 under section 24(h)(4), not USD 2,200. A child who fails the child tax credit only because of the social security number rule is also treated as a dependent for the USD 500 credit.

For the earned income credit, section 32 uses section 152(c) without the support test and without section 152(e), and the abode must be in the United States. There is no age-17 cap. A child under 19, a student under 24, or a person who is permanently and totally disabled can be a qualifying child. The child must be younger than the taxpayer unless disabled.

### Child tax credit computation

1. Count qualifying children under 17 who have a qualifying social security number. Multiply by USD 2,200.
2. Modified AGI is adjusted gross income plus any income excluded under section 911, 931, or 933. If it exceeds USD 200,000 (USD 400,000 joint), divide the excess by USD 1,000 and round a fraction up. Multiply by USD 50. Subtract from the credit. Not below zero.
3. The credit is nonrefundable except for the additional child tax credit. That additional amount cannot exceed USD 1,700 per qualifying child. It also cannot exceed 15 percent of earned income (as section 32 defines it) over USD 2,500, unless the taxpayer has three or more qualifying children and the excess of social security taxes over the earned income credit is larger. A taxpayer who elects the foreign earned income exclusion does not get the additional child tax credit.
4. Social security numbers, as amended by Public Law 119-21 section 70104: the return must include the taxpayer's social security number (on a joint return, at least one spouse) and the qualifying child's social security number. Each number must be issued by the Social Security Administration to a citizen, or under the work-authorized clause of the Social Security Act, before the due date of the return.

### Earned income credit computation

1. Stop if investment income exceeds USD 12,200. That is a cliff. At exactly USD 12,200 the credit is still allowed, because both the statute and Rev. Proc. 2025-32 use "exceeds". Investment income is interest (including tax-exempt interest), dividends, capital gain net income, net rents and royalties not from a business, and net passive income, as section 32(i) lists them.
2. Stop if the person is a nonresident alien for any part of the year and did not elect resident treatment under section 6013(g) or (h). Stop if the person claims the foreign earned income exclusion. A married person must file jointly unless the separated-spouse rule in section 32(d)(2) applies: a qualifying child lived with the person for more than half the year, and the person lived apart from the spouse for the last six months or is separated under a decree or agreement and not in the same household at year end. Rev. Proc. 2025-32 says the non-joint phase-out thresholds also apply to a married person who meets that rule.
3. With no qualifying child, the person must have a principal place of abode in the United States for more than half the year, must be at least 25 and not yet 65 before year end (either spouse, if married), and must not be another taxpayer's dependent. A person who is someone else's qualifying child is not an eligible individual.
4. Credit before phase-out: the credit percentage times earned income, but not more than the maximum in the table. The maximum applies once earned income reaches the earned income amount.
5. Phase-out: the phase-out percentage times the amount by which the greater of adjusted gross income or earned income exceeds the threshold phase-out amount. Subtract. Not below zero.
6. Social security numbers: section 32(m) says the taxpayer identification number, for the person and for a spouse, and for a qualifying child who is taken into account, is a Social Security Administration number other than one issued under the non-work clause, and it must be issued on or before the due date of the return.

The statute tells the Secretary to publish tables in brackets of not more than USD 50. A bracket table can differ from the exact formula by less than one bracket. The 2026 Form 1040 instructions' table was not the page read. Use the formula here, then check the table when it is published.

## Boundary and exception table

| Situation | Treatment |
| --- | --- |
| Child attained age 17 in 2026, still a dependent | No USD 2,200 credit. USD 500 other-dependent credit if the dependent tests are met |
| Child under 17, no work-authorized social security number by the due date | No child tax credit for that child. The child can still support the USD 500 credit |
| Modified AGI at or under USD 200,000 (USD 400,000 joint) | Full child tax credit, before the refundable limit |
| Earned income at or under USD 2,500, fewer than three qualifying children | Additional child tax credit from the 15 percent formula is zero |
| Foreign earned income exclusion claimed | No additional child tax credit. Not an eligible individual for the earned income credit |
| Investment income of USD 12,200 | Earned income credit still allowed. One dollar more and it is zero |
| Investment income over USD 12,200 | Earned income credit is zero. Not a phase-out |
| Married, no joint return, separated-spouse rule not met | No earned income credit |
| No qualifying child, under 25 or 65 or older | No earned income credit |
| Two people could claim the same child | Section 152(c)(4). Only one taxpayer's return |
| Credit denied in a deficiency proceeding | No later-year credit until the person gives the information the Secretary requires. Fraud: 10 years. Reckless or intentional disregard: 2 years |

## Worked cases

**Case 1, a decision: the child is 16, or the child is 17.** One unmarried parent, modified AGI USD 100,000, one child who meets every section 152(c) test and has a work-authorized social security number issued before the due date. The only fact that changes is age at the end of 2026.

Modified AGI is under USD 200,000, so there is no phase-out. At age 16 the child has not attained age 17. The child tax credit is USD 2,200. At age 17 the child has attained age 17, so section 24(c) excludes the child from the USD 2,200 credit. If the child is still a dependent, section 24(h)(4) allows USD 500. The figure that decides the year is USD 2,200 or USD 500, a difference of USD 1,700, before any limit on how much of the USD 2,200 is refundable.

```oa-check
name: Child tax credit, age 16 against age 17 (2026)
inputs:
  magi: 100000
  ctc: 2200
  other_dependent: 500
  threshold: 200000
steps:
  - excess: max(magi - threshold, 0)
  - thousands: ceil(excess / 1000)
  - reduction: thousands * 50
  - credit_age_16: max(ctc - reduction, 0)
  - credit_age_17: other_dependent
expected:
  excess: 0.00
  thousands: 0.00
  reduction: 0.00
  credit_age_16: 2200.00
  credit_age_17: 500.00
```

**Case 2, earned income credit, one child, in the phase-out.** An unmarried parent has one qualifying child, earned income and adjusted gross income of USD 28,890, and investment income of USD 400. The investment income does not exceed USD 12,200. Earned income is above the earned income amount of USD 13,020, so the credit before phase-out is the maximum, USD 4,427. The phase-out threshold for one child, other than a joint return, is USD 23,890. The excess is USD 5,000. The phase-out percentage is 15.98 percent, so the reduction is USD 799. The credit is USD 4,427 minus USD 799, which is USD 3,628.

```oa-check
name: Earned income credit, one child, inside the phase-out (2026)
inputs:
  earned: 28890
  agi: 28890
  maximum: 4427
  threshold: 23890
  phaseout_rate: 0.1598
steps:
  - excess: max(agi, earned) - threshold
  - reduction: excess * phaseout_rate
  - credit: max(maximum - reduction, 0)
expected:
  excess: 5000.00
  reduction: 799.00
  credit: 3628.00
```

## When to refuse or refer

| Code | Situation | Action |
| --- | --- | --- |
| R-CTC-TIE | Two taxpayers could claim the same child | Apply section 152(c)(4) before either credit |
| R-CTC-NR | The client was a nonresident alien for any part of 2026 and did not elect resident treatment | Earned income credit is off. Child tax credit limits for nonresidents are in `us-form-1040-nr-nonresident-return` |
| R-CTC-911 | The client claims the foreign earned income exclusion | No additional child tax credit and no earned income credit. See `us-foreign-earned-income-2555` |
| R-CTC-PRIOR | The credit was denied in a deficiency proceeding, or a fraud or reckless finding is in the disallowance window | Do not compute a current credit until eligibility is re-established |
| R-EITC-TABLE | The client needs the IRS dollar table rather than the formula | The 2026 Form 1040 instructions' table was not published when this skill was written. The formula above is the statute |

## Filing and payment

Both credits are claimed on the individual return, Form 1040 or 1040-SR. The child tax credit and the additional child tax credit are figured with Schedule 8812. The 2026 Schedule 8812 line numbers were not read. The earned income credit is refundable. It is not a deduction. A married person's earned income credit requires a joint return unless the separated-spouse rule applies.

The failure-to-file addition on the income-tax return is 5 percent of the tax per month or fraction, not over 25 percent, and the failure-to-pay addition is 0.5 percent per month or fraction, not over 25 percent, unless the failure is due to reasonable cause and not willful neglect. Source: [26 U.S.C. 6651(a)](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleF-chap68-subchapA-partI-sec6651.htm).

## Completion checklist

- Each child's age tested against 17 for the child tax credit, and against 19, 24, or disability for the earned income credit.
- Social security numbers are work-authorized and issued by the due date, including the taxpayer (or one spouse on a joint return) for the child tax credit.
- Child tax credit phase-out uses USD 50 per USD 1,000 or fraction over USD 200,000 or USD 400,000.
- Additional child tax credit is the smaller of the remaining credit, USD 1,700 per child, and 15 percent of earned income over USD 2,500, with the three-child social-security-tax alternative checked when it applies.
- Investment income tested against USD 12,200 before any earned income credit math. Over that amount, the credit is zero.
- Phase-out uses the greater of adjusted gross income and earned income, and the joint threshold only on a joint return.
- A person claiming the foreign earned income exclusion is removed from both the additional child tax credit and the earned income credit.

## Sources

| Source | URL | Read on |
| --- | --- | --- |
| 26 U.S.C. 24 (govinfo, U.S. Code 2024 edition). Read for (b) the USD 50 phase-out per USD 1,000 or fraction, (c) a qualifying child under 17, (d) the 15 percent additional credit and the three-child social-security-tax alternative, and (h) the USD 400,000 and USD 200,000 thresholds, the USD 500 other-dependent credit, the USD 1,400 refundable base, and the USD 2,500 earned-income floor. The edition still prints USD 2,000 and an end date before 2026. Those two points were changed by Public Law 119-21. | https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap1-subchapA-partIV-subpartA-sec24.htm | 2026-11-13 |
| 26 U.S.C. 32 (govinfo, U.S. Code 2024 edition). Read for (a) and (b) the credit and phase-out percentages, (c) eligible individual, qualifying child, and the age 25 to 64 test with no child, (d) the joint-return rule and the separated spouse, (i) investment income over the indexed USD 10,000 base, and (m) the social security number rule. The 2026 dollar amounts are in Rev. Proc. 2025-32, not in this edition's base table. | https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap1-subchapA-partIV-subpartC-sec32.htm | 2026-11-13 |
| 26 U.S.C. 152 (govinfo, U.S. Code 2024 edition). Read for (c) relationship, abode, age (under 19, student under 24, or disabled), the support test, the joint-return test, and the tie-breaker. | https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap1-subchapB-partV-sec152.htm | 2026-11-13 |
| Public Law 119-21, section 70104 (govinfo). Read for the substitution of USD 2,200 for USD 2,000, the removal of the pre-2026 end date, the social security number rule for the taxpayer (or one spouse) and the child, and the inflation rule for the refundable amount and, from 2026, the credit amount. | https://www.govinfo.gov/content/pkg/PLAW-119publ21/html/PLAW-119publ21.htm | 2026-11-13 |
| Rev. Proc. 2025-32. Read for section 4.05 (2026 child tax credit USD 2,200 and refundable amount USD 1,700) and section 4.06 (the 2026 earned income credit table and the USD 12,200 investment-income limit). | https://www.irs.gov/pub/irs-drop/rp-25-32.pdf | 2026-11-13 |
| 26 U.S.C. 6651 (govinfo, U.S. Code 2024 edition). Read for (a)(1) 5 percent a month capped at 25 percent and (a)(2) 0.5 percent a month capped at 25 percent. | https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleF-chap68-subchapA-partI-sec6651.htm | 2026-11-13 |

Not yet confirmed: the 2026 Instructions for Form 1040 and the 2026 Schedule 8812 were not published as the pages read, so the IRS earned income credit table (brackets of not more than USD 50) and the 2026 form line numbers are not in this skill. The formula above is the statute plus Rev. Proc. 2025-32. Completed phase-out amounts printed in Rev. Proc. 2025-32 were read and are not restated, because the phase-out percentage reaches zero at those amounts and the skill computes from the threshold instead. The form number the Secretary uses after a denied credit was not read.

## Today's figures and who stands behind this skill

This file is an AI skill (tax rules your AI follows) from OpenAccountants, copied on 2026-11-13. Rates, thresholds and deadlines change. For the current version of this skill, its official sources and the named accountant (if any) who stands behind it, call `get_skill` with slug `us-child-tax-credit-and-eitc` on the OpenAccountants connector (https://www.openaccountants.com/connect), or read https://www.openaccountants.com/skills/us-child-tax-credit-and-eitc. If neither is available, confirm every figure against the official source pages cited above before relying on it.
