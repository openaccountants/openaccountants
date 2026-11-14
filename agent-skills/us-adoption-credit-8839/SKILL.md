---
name: us-adoption-credit-8839
description: "Compute the US adoption credit and the exclusion for employer-provided adoption assistance on Form 8839 for tax year 2026. 2026 figures from Rev. Proc. 2025-32 sections .04 and .18 - maximum credit and exclusion $17,670 per child, phase-out from modified AGI of $265,080 to $305,080, refundable part up to $5,120 (new section 23(a)(4) from Public Law 119-21 section 70402), the special needs rule that allows the full amount without expenses, when to claim domestic and foreign adoption expenses, the five-year carryforward of the nonrefundable part, and the joint return rule for married couples. Trigger on \"adoption credit\", \"Form 8839\", \"adoption tax credit 2026\", \"employer adoption assistance\", \"special needs adoption\", \"refundable adoption credit\". Federal only."
license: "AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)"
metadata:
  source: openaccountants
  openaccountants_url: "https://www.openaccountants.com/skills/us-adoption-credit-8839"
  jurisdiction: "US"
  tax_year: "2026"
  last_updated: "2026-11-13"
---

# US adoption credit and employer adoption assistance (Form 8839), tax year 2026

> **Source-cited draft.** Built from Rev. Proc. 2025-32 sections .04 and .18, Public Law 119-21 section 70402, 26 U.S.C. 23 and 137, and the 2025 Instructions for Form 8839, read on 2026-11-13. No accountant has reviewed it. All outputs must be reviewed by a qualified tax professional before filing.

**Answer first.** For 2026 the adoption credit is up to **$17,670** of qualified adoption expenses per child. It phases out between modified AGI of **$265,080** and **$305,080**. Up to **$5,120** of it is refundable, so it is paid even with no tax owed. For a US child with special needs the full $17,670 is allowed in the year the adoption becomes final, whatever was spent. Separately, up to $17,670 of employer adoption assistance can be excluded from wages, but the same expense cannot count twice.

## Scope and who this is for

In scope: an individual who paid qualified adoption expenses, or received employer-provided adoption benefits, for an eligible child, and files a 2026 Form 1040. Covers Form 8839 Part II (credit) and Part III (exclusion) logic, timing, the phase-out, the refundable part and the carryforward.

Out of scope, and where it goes:

| Topic | Skill |
| --- | --- |
| Child tax credit and other credits for the child | `us-federal-income-tax-return-1040` |
| Overview of 2026 law changes (adoption credit row) | `us-2026-federal-tax-changes` |
| Employer side: setting up and reporting an adoption assistance program (W-2 box 12 code T) | Refer (R-ADOPT-EMPLOYER) |
| Adoption of a spouse's child, surrogacy | Not qualified expenses: no credit |

## Ask the client first

1. **The child:** age (under 18, or unable to care for themselves), whether a US citizen or resident when the adoption effort began (domestic) or not (foreign), and whether a State (or, from 2025, an Indian tribal government) has determined the child has special needs.
2. **Status of the adoption:** final in 2026, final earlier, still pending, or failed. For a foreign adoption, the date it became final.
3. **Expenses by year paid:** adoption fees, court costs, attorney fees, travel (including meals and lodging away from home) directly for the adoption, from every year, with receipts.
4. **Employer benefits:** Form W-2 box 12 code T amounts, and whether the employer has a written qualified adoption assistance program.
5. **Grants and reimbursements:** any federal, State or local program funds, or other reimbursement, for the same expenses.
6. **Filing status and modified AGI:** married couples must generally file jointly; any foreign earned income exclusion or Puerto Rico or territory income excluded (added back to AGI).
7. **Prior-year Form 8839:** any credit carried forward from 2021 to 2025.

## The method, step by step

### Rates, bands and thresholds

| Item | Amount, 2026 | Source |
| --- | --- | --- |
| Maximum credit per eligible child (qualified adoption expenses taken into account), and the special needs credit amount | USD 17,670 | [Rev. Proc. 2025-32, section 4.04](https://www.irs.gov/pub/irs-drop/rp-25-32.pdf) |
| Phase-out starts above modified AGI of | USD 265,080 | [Rev. Proc. 2025-32, section 4.04](https://www.irs.gov/pub/irs-drop/rp-25-32.pdf) |
| Fully phased out at modified AGI of | USD 305,080 | [Rev. Proc. 2025-32, section 4.04](https://www.irs.gov/pub/irs-drop/rp-25-32.pdf) |
| Phase-out range (denominator of the reduction ratio) | USD 40,000 | [26 U.S.C. 23(b)(2)(A)](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap1-subchapA-partIV-subpartA-sec23.htm) |
| Refundable part of the credit | USD 5,120 | [Rev. Proc. 2025-32, section 4.04](https://www.irs.gov/pub/irs-drop/rp-25-32.pdf) |
| Maximum exclusion of employer-provided adoption benefits, per child (and the special needs amount) | USD 17,670 | [Rev. Proc. 2025-32, section 4.18](https://www.irs.gov/pub/irs-drop/rp-25-32.pdf) |
| Exclusion phase-out, modified AGI | USD 265,080 to USD 305,080 | [Rev. Proc. 2025-32, section 4.18](https://www.irs.gov/pub/irs-drop/rp-25-32.pdf) |
| Carryforward of unused nonrefundable credit | 5 years, first in, first out | [26 U.S.C. 23(c)(2)](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap1-subchapA-partIV-subpartA-sec23.htm) |

The four dollar amounts are indexed each year (section 23(h) as amended by Public Law 119-21 section 70402). The 2026 figures are the federal library's (`us.adoption.max`, `us.adoption.phaseout-start`, `us.adoption.refundable`).

### Step 1: is there an eligible child and are the expenses qualified?

1. **Eligible child:** under age 18, or physically or mentally incapable of caring for themselves. Source: [26 U.S.C. 23(d)(2)](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap1-subchapA-partIV-subpartA-sec23.htm).
2. **Qualified adoption expenses:** reasonable and necessary adoption fees, court costs, attorney fees and other expenses directly related to, and with the principal purpose of, the legal adoption of an eligible child. Not: expenses in violation of law, surrogate parenting arrangements, adopting a spouse's child, or amounts reimbursed by an employer or otherwise. Source: [26 U.S.C. 23(d)(1)](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap1-subchapA-partIV-subpartA-sec23.htm).
3. **No double benefit:** no credit for an expense deducted or credited elsewhere, or paid with federal, State or local program funds (section 23(b)(3)). Employer-reimbursed expenses are excluded under section 137 instead and drop out of the credit (Form 8839 instructions, Example 1).

### Step 2: which year?

4. **Domestic adoption (US child):** expenses paid before the year the adoption becomes final are claimed in the year after payment; expenses paid in or after the final year are claimed in the year paid. A credit may be allowed for a domestic adoption that never becomes final. Source: [26 U.S.C. 23(a)(2)](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap1-subchapA-partIV-subpartA-sec23.htm); [Instructions for Form 8839 (2025)](https://www.irs.gov/pub/irs-pdf/i8839.pdf).
5. **Foreign adoption:** no credit until the adoption becomes final; expenses from earlier years are claimed in the final year, later ones in the year paid.
6. **Employer benefits:** excluded in the year paid for a domestic adoption; for a foreign adoption, in the year final for amounts paid before then.

### Step 3: the amount per child

7. **Expenses taken into account** = the smaller of qualified expenses for this year (net of any used in earlier years for the same child) and USD 17,670 less amounts already used for the same child in earlier years. The USD 17,670 is a lifetime limit per child (section 23(b)(1)).
8. **Special needs:** for a US child with special needs whose adoption becomes final in 2026, treat the taxpayer as having paid enough expenses to reach USD 17,670 in total, even with no expenses. Source: [26 U.S.C. 23(a)(3)](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap1-subchapA-partIV-subpartA-sec23.htm); [Rev. Proc. 2025-32, section 4.04(1)](https://www.irs.gov/pub/irs-drop/rp-25-32.pdf).

### Step 4: phase-out

9. **Modified AGI** = AGI plus any foreign earned income or housing exclusion (section 911) and income excluded under sections 931 and 933 (territories and Puerto Rico) (section 23(b)(2)(B)).
10. **Reduction** = credit before phase-out x (modified AGI - USD 265,080) / USD 40,000, not below zero and not above the credit. At USD 305,080 or more the credit is nil. The same reduction applies separately to the exclusion (section 137(b)(2)).

### Step 5: split refundable and nonrefundable

11. Up to USD 5,120 of the credit after phase-out is refundable, determined separately for each eligible child (new section 23(a)(4), as indexed; the 2025 Form 8839 instructions say "determined separately for each eligible child"). It is paid even if it exceeds the tax.
12. The rest is nonrefundable: it reduces income tax to zero and any unused part carries forward for up to five years. The refundable part is never carried forward (section 23(c)(1) as amended by section 70402(c)). A carryforward from earlier years stays nonrefundable.

### Step 6: exclusion for employer adoption assistance

13. Benefits under a written qualified adoption assistance program (W-2 box 12 code T) are excludable up to USD 17,670 per child, phased out over the same modified AGI range. For a special needs child whose adoption becomes final in 2026, the full USD 17,670 can be excluded even if the employer paid less (where the employer has a program). Source: [Rev. Proc. 2025-32, section 4.18](https://www.irs.gov/pub/irs-drop/rp-25-32.pdf); [Instructions for Form 8839 (2025)](https://www.irs.gov/pub/irs-pdf/i8839.pdf).
14. The credit and exclusion limits are separate, so a family can use both for one child, but each dollar of expense counts only once.

## Boundary and exception table

| Situation | Treatment |
| --- | --- |
| Married filing separately | Generally no credit or exclusion; allowed if treated as unmarried (lived apart the last 6 months, child lived in the home more than half the year, paid over half the cost of the home) |
| Adoption of a spouse's child | No credit |
| Foreign adoption not yet final | No credit yet; carry the expenses to the final year |
| Failed domestic adoption | Expenses can count (US child only); if a second attempt follows, refer (R-ADOPT-MULTI) |
| Special needs determination by a State or (from 2025) an Indian tribal government | Full USD 17,670 in the year final regardless of expenses |
| Foreign child with special needs | The special needs rule does not apply (child must be a US citizen or resident) |
| Credit larger than tax | Refundable part paid; nonrefundable rest carried forward 5 years |
| Modified AGI between USD 265,080 and USD 305,080 | Partial credit and exclusion by the ratio |

### Defaults when a fact is missing

| Missing fact | Default, and flag it |
| --- | --- |
| Year expenses were paid | Ask; timing changes the claim year |
| Special needs determination | No special needs treatment without the State or tribal determination |
| Employer program written plan | No exclusion beyond W-2 box 12 code T amounts |
| Prior credits for the same child | Ask for earlier Forms 8839; the USD 17,670 is a lifetime limit |

## Worked cases

**Case 1, phase-out and refundable part.** A married couple filing jointly finalize a domestic adoption in 2026 and paid USD 20,000 of qualified expenses in 2026. Their modified AGI is USD 285,080.

Expenses taken into account: the smaller of USD 20,000 and USD 17,670, so USD 17,670. Reduction: USD 17,670 x (USD 285,080 - USD 265,080) / USD 40,000 = USD 17,670 x 0.5 = USD 8,835. Credit: USD 8,835. Refundable part: the smaller of USD 8,835 and USD 5,120, so USD 5,120. Nonrefundable part: USD 3,715, used against their tax (any excess carried forward).

```oa-check
name: Adoption credit with phase-out, joint filers (2026)
inputs:
  expenses: 20000
  max_credit: 17670
  magi: 285080
  phaseout_start: 265080
  phaseout_range: 40000
  refundable_cap: 5120
steps:
  - base: min(expenses, max_credit)
  - reduction: min(base * max(magi - phaseout_start, 0) / phaseout_range, base)
  - credit: base - reduction
  - refundable: min(credit, refundable_cap)
  - nonrefundable: credit - refundable
expected:
  base: 17670.00
  reduction: 8835.00
  credit: 8835.00
  refundable: 5120.00
  nonrefundable: 3715.00
```

**Case 2, a decision: how to use the employer program and the credit together.** A single parent finalizes a domestic adoption in 2026. Total qualified expenses USD 25,000, of which the employer's written adoption assistance program paid USD 10,000 (W-2 box 12 code T). Modified AGI USD 120,000, below the phase-out. The question is how much of the cost each relief covers.

Exclusion: the smaller of USD 10,000 and USD 17,670, so USD 10,000 excluded from wages. Those USD 10,000 are reimbursed, so they are not qualified expenses for the credit. Credit base: the smaller of the USD 15,000 the parent paid and USD 17,670, so USD 15,000. Refundable part: USD 5,120. Nonrefundable part: USD 9,880 (carried forward to the extent it exceeds tax). Using both covers all USD 25,000; claiming the credit on the employer-paid amount as well would be a double benefit and is not allowed.

```oa-check
name: Employer exclusion plus credit, single parent (2026)
inputs:
  total_expenses: 25000
  employer_paid: 10000
  limit: 17670
  refundable_cap: 5120
steps:
  - exclusion: min(employer_paid, limit)
  - own_expenses: total_expenses - employer_paid
  - credit: min(own_expenses, limit)
  - refundable: min(credit, refundable_cap)
  - nonrefundable: credit - refundable
  - covered: exclusion + credit
expected:
  exclusion: 10000.00
  own_expenses: 15000.00
  credit: 15000.00
  refundable: 5120.00
  nonrefundable: 9880.00
  covered: 25000.00
```

## When to refuse or refer

| Code | Situation | Action |
| --- | --- | --- |
| R-ADOPT-FOREIGN-FINAL | Unclear whether a foreign adoption is final (Rev. Proc. 2005-31 and 2010-31) | Refer |
| R-ADOPT-MULTI | Failed adoption followed by another attempt, or several children across years | Refer: per-child limits and timing need a working paper |
| R-ADOPT-MFS | Married, not filing jointly, and the unmarried tests are doubtful | Refer |
| R-ADOPT-EMPLOYER | Employer designing or reporting a program | Refer: Pub. 15-B and payroll |
| R-ADOPT-SURROGACY | Expenses relate to a surrogate parenting arrangement | No credit; explain |

## Filing and payment

Form 8839 is attached to the 2026 Form 1040, due **15 April 2027** (extension to 15 October 2027 extends filing, not payment). The nonrefundable part flows to Schedule 3 and the refundable part to the payments section of Form 1040; the 2026 line numbers are not yet published. Part I of Form 8839 requires the child's name, birth year, identifying number and status (special needs, foreign, finalized).

## Completion checklist

- Eligible child and qualified expenses confirmed, no reimbursed or grant-funded amounts.
- Claim year right for domestic or foreign adoption.
- Lifetime USD 17,670 limit per child applied across years.
- Modified AGI computed with section 911, 931 and 933 add-backs; phase-out applied to credit and exclusion.
- Refundable part (up to USD 5,120 per child) separated; nonrefundable carryforward recorded.
- Employer benefits excluded and removed from the credit base.

## Sources

| Source | URL | Read on |
| --- | --- | --- |
| Rev. Proc. 2025-32, section 4.04. Read for $17,670 (special needs and maximum), the phase-out from $265,080 to $305,080, and the refundable $5,120. | https://www.irs.gov/pub/irs-drop/rp-25-32.pdf | 2026-11-13 |
| Rev. Proc. 2025-32, section 4.18. Read for the section 137 exclusion of $17,670 (special needs and maximum) and the same phase-out. | https://www.irs.gov/pub/irs-drop/rp-25-32.pdf | 2026-11-13 |
| Public Law 119-21, section 70402. Read for new 23(a)(4) refundable portion ($5,000 base, indexed from 2025), 23(h) indexing, and 23(c)(1) excluding the refundable part from carryforward; effective for taxable years beginning after 31 December 2024. | https://www.govinfo.gov/content/pkg/PLAW-119publ21/html/PLAW-119publ21.htm | 2026-11-13 |
| 26 U.S.C. 23 (govinfo, 2024 edition). Read for (a)(2) timing, (a)(3) special needs, (b)(1) dollar limit, (b)(2) phase-out ratio over $40,000 and modified AGI, (b)(3) no double benefit, (c) five-year carryforward, (d) definitions. | https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap1-subchapA-partIV-subpartA-sec23.htm | 2026-11-13 |
| 26 U.S.C. 137 (govinfo, 2024 edition). Read for the exclusion for adoption assistance programs. | https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap1-subchapB-partIII-sec137.htm | 2026-11-13 |
| Instructions for Form 8839 (2025). Read for the refundable part per child, tribal special needs determinations, the domestic and foreign timing tables, employer benefits (box 12 code T) and Example 1, and married persons not filing jointly. | https://www.irs.gov/pub/irs-pdf/i8839.pdf | 2026-11-13 |

Not yet confirmed: the 2026 Form 8839 and its instructions were not published when read, so the order in which the 2026 form applies the phase-out before splitting off the refundable part is taken from the 2025 instructions and section 23, and the 2026 Form 1040 and Schedule 3 line numbers are not quoted.

## Today's figures and who stands behind this skill

This file is an AI skill (tax rules your AI follows) from OpenAccountants, copied on 2026-11-13. Rates, thresholds and deadlines change. For the current version of this skill, its official sources and the named accountant (if any) who stands behind it, call `get_skill` with slug `us-adoption-credit-8839` on the OpenAccountants connector (https://www.openaccountants.com/connect), or read https://www.openaccountants.com/skills/us-adoption-credit-8839. If neither is available, confirm every figure against the official source pages cited above before relying on it.
