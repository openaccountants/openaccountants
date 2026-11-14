---
name: us-kiddie-tax-8615
description: "Work out the 2026 US kiddie tax on a child's unearned income, on Form 8615 (child's return, taxed at the parent's rate) or by the parent's election on Form 8814. Covers which children it applies to (under 18, 18 with low earned income, full-time students under 24), net unearned income above USD 2,700 (twice the USD 1,350 amount), the child's own standard deduction, the Form 8814 conditions (only interest and dividends, gross income more than USD 1,350 and less than USD 13,500), the USD 135 tax on the second USD 1,350, and the choice between the two forms. Trigger on \"kiddie tax\", \"Form 8615\", \"Form 8814\", \"child's investment income\", \"unearned income of a minor\", \"UTMA account tax\", \"child's dividends on parent's return\". Federal only."
license: "AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)"
metadata:
  source: openaccountants
  openaccountants_url: "https://www.openaccountants.com/skills/us-kiddie-tax-8615"
  jurisdiction: "US"
  tax_year: "2026"
  last_updated: "2026-11-13"
---

# US kiddie tax: Forms 8615 and 8814, tax year 2026

> **Source-cited draft.** Built from Rev. Proc. 2025-32, 26 U.S.C. 1(g), the 2025 Form 8615 and its instructions and the 2025 Form 8814, read on 2026-11-13. No accountant has reviewed it. All outputs must be reviewed by a qualified tax professional before filing.

**Answer first.** For 2026, a child's unearned income above **USD 2,700** (twice the **USD 1,350** amount in Rev. Proc. 2025-32) is taxed at the parent's rate if that is higher. The first USD 1,350 is covered by the child's standard deduction and the next USD 1,350 is taxed at the child's own rate. The child files Form 8615 with their own return. Instead, if the child had only interest and dividends and gross income of more than USD 1,350 and less than **USD 13,500**, the parent can elect to report it on Form 8814: the second USD 1,350 is taxed at 10% (at most USD 135) and anything above USD 2,700 is added to the parent's income.

## Scope and who this is for

In scope: a child's 2026 return with unearned income (interest, dividends, capital gains, taxable scholarships not reported on a W-2, UTMA and trust distributions), Form 8615, and the parent's Form 8814 election.

Out of scope, and where it goes:

| Topic | Skill |
| --- | --- |
| The parent's own return, brackets and the standard deduction for adults | `us-federal-income-tax-return-1040` |
| Capital gains rates on the child's or parent's return | `us-capital-gains` |
| Paying a child wages from the family business | `us-hiring-your-children-and-accountable-plans` |
| The AMT exemption cap for a child (earned income plus USD 9,750) | `us-alternative-minimum-tax-6251` |
| 529 plans and Trump accounts for children | `us-529-and-trump-accounts` |

## Ask the client first

1. **The child's age at 31 December 2026**, and if 18 to 23, whether a full-time student and whether the child's earned income was more than half of their own support.
2. **The child's 2026 income by type:** earned income (wages, self-employment), interest, ordinary and qualified dividends, capital gain distributions, other capital gains, other unearned income. Ask for every Form 1099.
3. **Whether either parent is alive**, and the parents' filing status. If they are married filing separately, or divorced or separated, which parent's return is used (Form 8615 instructions).
4. **The parent's 2026 taxable income and filing status**, and whether other children of the same parent have unearned income.
5. **Any estimated tax paid or tax withheld** in the child's name (this rules out Form 8814).

## The method, step by step

### Rates, bands and thresholds

| Item | Amount, 2026 | Source |
| --- | --- | --- |
| Amount that reduces net unearned income, and the minimum standard deduction for a dependent | USD 1,350 | [Rev. Proc. 2025-32, section 4.02](https://www.irs.gov/pub/irs-drop/rp-25-32.pdf) |
| Unearned income above which Form 8615 applies (twice USD 1,350) | USD 2,700 | [26 U.S.C. 1(g)(4)(A)(ii)](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap1-subchapA-partI-sec1.htm); [Rev. Proc. 2025-32, section 4.02](https://www.irs.gov/pub/irs-drop/rp-25-32.pdf) |
| Form 8814: child's gross income must be more than | USD 1,350 | [Rev. Proc. 2025-32, section 4.02](https://www.irs.gov/pub/irs-drop/rp-25-32.pdf) |
| Form 8814: child's gross income must be less than | USD 13,500 | [Rev. Proc. 2025-32, section 4.02](https://www.irs.gov/pub/irs-drop/rp-25-32.pdf) |
| Form 8814: rate on the child's income between USD 1,350 and USD 2,700 | 10% | [26 U.S.C. 1(g)(7)(B)](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap1-subchapA-partI-sec1.htm) |
| Dependent standard deduction: earned income plus | USD 450 | [Rev. Proc. 2025-32, section 4.14](https://www.irs.gov/pub/irs-drop/rp-25-32.pdf) |
| Age: under | 18 | [26 U.S.C. 1(g)(2)(A)](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap1-subchapA-partI-sec1.htm) |
| Full-time students: under | 24 | [26 U.S.C. 1(g)(2)(A)(ii)(II)](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap1-subchapA-partI-sec1.htm) |

The full standard deduction of a dependent (it cannot exceed the adult amount) is in `us-federal-income-tax-return-1040`. The 2026 amounts are the same as 2025 (USD 1,350, USD 2,700, USD 13,500), so the 2025 forms' dollar amounts still read correctly.

### Step 1: does the kiddie tax apply?

1. All of these must be true (Form 8615 instructions, "Who Must File"):
   - the child's unearned income is more than USD 2,700;
   - the child is under 18 at the end of 2026; or is 18 and their earned income was not more than half of their support; or is a full-time student aged 19 to 23 whose earned income was not more than half of their support;
   - at least one parent is alive at the end of 2026;
   - the child must file a return and does not file jointly.
2. If any fails, the child is taxed at their own rates and neither form is used.

### Step 2, the child's return: Form 8615

3. **Line 1:** the child's unearned income.
4. **Line 2:** USD 2,700 if the child does not itemize (otherwise the form's larger figure).
5. **Line 3, net unearned income** = line 1 minus line 2, but not more than the child's taxable income (line 5). Source: [26 U.S.C. 1(g)(4)](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap1-subchapA-partI-sec1.htm).
6. **Child's taxable income:** total income minus the child's standard deduction, which is the larger of USD 1,350 or earned income plus USD 450, capped at the adult standard deduction.
7. **Tax.** Net unearned income is taxed as if added to the parent's taxable income (the extra tax on the parent's return at the parent's rates, including the parent's capital gains rates for the child's qualified dividends and gains). The rest of the child's taxable income is taxed at the child's own rates. The child pays the higher of this and the tax figured with no kiddie tax. If the parent has more than one child with net unearned income, the extra tax is shared in proportion (Form 8615 lines 7 to 13).

### Step 3, the parent's election: Form 8814

8. **Conditions** ([Instructions for Form 8814](https://www.irs.gov/pub/irs-pdf/i8814.pdf) and [26 U.S.C. 1(g)(7)](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap1-subchapA-partI-sec1.htm)): the child is under 19, or a full-time student under 24; the child's only income is interest and dividends (including capital gain distributions and Alaska Permanent Fund dividends); gross income is more than USD 1,350 and less than USD 13,500; no estimated tax was paid and nothing was withheld in the child's name; the child does not file a return.
9. **Form 8814 line 4:** total interest and dividends. If USD 2,700 or less, nothing is added to the parent's income. Above USD 2,700, the excess is added to the parent's income (Schedule 1 line 8z, with the qualified dividends and capital gain distribution shares going to the parent's lines for those items).
10. **Lines 13 to 15:** the first USD 1,350 is not taxed; the next USD 1,350 is taxed at 10%, so at most USD 135, added to the parent's tax.

### Step 4: choose

11. Federal tax is often the same or close under both forms. Form 8814 is simpler (no return for the child) but raises the parent's AGI, which can cut credits and deductions that phase out with AGI, trigger the net investment income tax, and raise state tax. It also loses the child's own deductions (for example a penalty on early withdrawal). Form 8615 keeps the parent's AGI unchanged. Run both when the parent is near a phase-out.

## Boundary and exception table

| Situation | Treatment |
| --- | --- |
| Unearned income exactly USD 2,700 | No Form 8615: the test is "more than" |
| Child aged 18 with wages covering more than half of their own support | Not subject to the kiddie tax; taxed at own rates |
| Child turned 24 during 2026 | Not subject: the age test is under 24 at year end |
| Child has wages as well as investment income | Form 8814 not available; Form 8615 only; the standard deduction rises with earned income |
| Child sold shares at a gain | Capital gains are unearned income; Form 8814 is not available (only interest, dividends and capital gain distributions) |
| Taxable scholarship not on a W-2 | Treated as unearned income for Form 8615 |
| Parents married filing separately | Use the parent with the greater taxable income |
| Parents divorced or never married | Use the custodial parent, with the Form 8615 instructions for remarried custodial parents |

### Defaults when a fact is missing

| Missing fact | Default, and flag it |
| --- | --- |
| Parent's taxable income | Do not finish Form 8615; it needs the parent's figures (the child can file and amend, or request an extension) |
| Whether a student child's earnings cover half of support | Assume they do not (the kiddie tax applies) and ask |
| Qualified dividends share of the child's dividends | Take it from Form 1099-DIV box 1b; never assume zero |

### Red flags to raise with the client

| Flag | Why it matters |
| --- | --- |
| Gross income near USD 13,500 | Form 8814 is not allowed at or above it |
| Large UTMA or custodial account in the child's name | The kiddie tax usually applies until 18, or 24 for students |
| Parent near an AGI phase-out or the net investment income tax threshold | Form 8814 may cost more than Form 8615 |
| Tax withheld or estimates paid for the child | Form 8814 not allowed; the child must file |

## Worked cases

**Case 1, a decision: Form 8615 or Form 8814?** A 12-year-old has USD 6,000 of bank interest and no other income. The parents file jointly and their top rate is 24% (from their own return; nothing else on it changes with AGI).

Form 8615: unearned income above USD 2,700 is USD 3,300, taxed at the parent's 24% = USD 792. The child's taxable income is USD 6,000 minus USD 1,350 = USD 4,650; the other USD 1,350 is taxed at the child's 10% = USD 135. Total USD 927. Form 8814: USD 135 plus USD 3,300 added to the parents' income at 24% = USD 792. Total USD 927, the same. The parents' AGI rises by USD 3,300 under Form 8814. Recommend Form 8814 for simplicity here, because nothing on the parents' return depends on AGI; if anything did, Form 8615 would be the better choice.

```oa-check
name: Child's 6,000 interest, Form 8615 against Form 8814 (2026)
inputs:
  unearned: 6000
  parent_rate: 0.24
  child_rate: 0.10
steps:
  - nui: max(unearned - 2700, 0)
  - form8615_parent_part: nui * parent_rate
  - form8615_child_part: (min(unearned, 2700) - 1350) * child_rate
  - form8615_total: form8615_parent_part + form8615_child_part
  - form8814_child_tax: min(max(unearned - 1350, 0), 1350) * 0.10
  - form8814_total: form8814_child_tax + nui * parent_rate
  - parent_agi_increase_8814: nui
expected:
  form8615_total: 927.00
  form8814_child_tax: 135.00
  form8814_total: 927.00
  parent_agi_increase_8814: 3300
```

**Case 2, a 17-year-old with wages and dividends.** A 17-year-old has USD 3,000 of wages from a summer job and USD 10,000 of investment income. The standard deduction is the larger of USD 1,350 and USD 3,000 plus USD 450, so USD 3,450. Taxable income is USD 13,000 minus USD 3,450 = USD 9,550. Net unearned income is USD 10,000 minus USD 2,700 = USD 7,300, which is below taxable income, so USD 7,300 is taxed at the parent's rate and the remaining USD 2,250 at the child's own rates. Form 8814 is not available because the child has wages.

```oa-check
name: Child aged 17 with wages and unearned income (2026)
inputs:
  wages: 3000
  unearned: 10000
steps:
  - standard_deduction: max(1350, wages + 450)
  - taxable_income: wages + unearned - standard_deduction
  - nui: min(max(unearned - 2700, 0), taxable_income)
  - at_child_rate: taxable_income - nui
expected:
  standard_deduction: 3450
  taxable_income: 9550
  nui: 7300
  at_child_rate: 2250
```

## When to refuse or refer

| Code | Situation | Action |
| --- | --- | --- |
| R-KT-SIBLINGS | Several children of the same parent with net unearned income | Use Form 8615 lines 7 to 13 with every child's figures; a reviewer checks the allocation |
| R-KT-CUSTODY | Divorced, separated or remarried parents and it is unclear whose return is used | Refer |
| R-KT-TRUST | Income from a trust, or the child itemizes | Refer: line 2 and distributable net income need the trust return |
| R-KT-FOREIGN | The child or parent is a nonresident alien | Refer (`us-form-1040-nr-nonresident-return`) |

## Filing and payment

The child's 2026 return with Form 8615, or the parent's 2026 return with Form 8814, is due **15 April 2027**. If the parent's figures are not ready, the child can file Form 4868 for an extension; tax is still due 15 April 2027.

## Completion checklist

- Age and support test applied at 31 December 2026.
- USD 2,700 threshold used as "more than".
- Child's standard deduction worked out as the larger of USD 1,350 or earned income plus USD 450.
- Qualified dividends and capital gains kept at capital gains rates through the parent's computation.
- Form 8814 conditions all checked before electing it; AGI effects on the parent's return reviewed.

## Sources

| Source | URL | Read on |
| --- | --- | --- |
| Rev. Proc. 2025-32. Read for section 4.02 (USD 1,350; parental election requires gross income more than USD 1,350 and less than USD 13,500) and section 4.14 (dependent standard deduction: greater of USD 1,350 or USD 450 plus earned income). | https://www.irs.gov/pub/irs-drop/rp-25-32.pdf | 2026-11-13 |
| 26 U.S.C. 1(g) (govinfo, 2024 edition). Read for (2) the children covered, (4) net unearned income, (7) the parent's election and the 10% rate. | https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap1-subchapA-partI-sec1.htm | 2026-11-13 |
| Instructions for Form 8615 (2025). Read for Who Must File (more than USD 2,700; ages; support), which parent's return to use, and lines 1 to 13. | https://www.irs.gov/pub/irs-pdf/i8615.pdf | 2026-11-13 |
| Instructions for Form 8814 (2025). Read for the conditions: under age 19 (or under 24 if a full-time student), only interest and dividends, no estimated tax or backup withholding. | https://www.irs.gov/pub/irs-pdf/i8814.pdf | 2026-11-13 |
| Form 8814 (2025). Read for line 4 (USD 2,700 and USD 13,500), line 5 base amount, lines 13 to 15 (USD 1,350 not taxed; at most USD 135). | https://www.irs.gov/pub/irs-pdf/f8814.pdf | 2026-11-13 |

Not yet confirmed: the 2026 Forms 8615 and 8814 and their instructions were not yet published when read; line numbers are those of the 2025 forms, whose dollar amounts match the 2026 figures in Rev. Proc. 2025-32.

## Today's figures and who stands behind this skill

This file is an AI skill (tax rules your AI follows) from OpenAccountants, copied on 2026-11-13. Rates, thresholds and deadlines change. For the current version of this skill, its official sources and the named accountant (if any) who stands behind it, call `get_skill` with slug `us-kiddie-tax-8615` on the OpenAccountants connector (https://www.openaccountants.com/connect), or read https://www.openaccountants.com/skills/us-kiddie-tax-8615. If neither is available, confirm every figure against the official source pages cited above before relying on it.
