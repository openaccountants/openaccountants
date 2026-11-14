---
name: us-filing-status-and-dependents
description: "Decide a US individual's 2026 federal filing status (single, married filing jointly, married filing separately, head of household, qualifying surviving spouse) and who counts as a dependent under the qualifying child and qualifying relative tests, including the 2026 qualifying relative gross income limit of $5,300 from Rev. Proc. 2025-32 section 4.23. Includes a worked decision on married filing jointly against separately. Trigger on \"filing status\", \"head of household\", \"married filing separately\", \"qualifying surviving spouse\", \"can I claim my parent\", \"qualifying child\", \"qualifying relative\", \"dependent\". Federal only."
license: "AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)"
metadata:
  source: openaccountants
  openaccountants_url: "https://www.openaccountants.com/skills/us-filing-status-and-dependents"
  jurisdiction: "US"
  tax_year: "2026"
  last_updated: "2026-11-13"
---

# US filing status and dependents, tax year 2026

> **Source-cited draft.** Built from 26 U.S.C. 2, 63 and 152 and Rev. Proc. 2025-32, read on 2026-11-13. No accountant has reviewed it. All outputs must be reviewed by a qualified tax professional before filing.

**Answer first.** Marital status is fixed on 31 December 2026. A married couple files jointly or separately. An unmarried person is head of household if they pay over half the cost of a home that is, for more than half the year, the main home of a qualifying child or dependent relative (a dependent parent may live elsewhere); otherwise single. A widow or widower whose spouse died in 2024 or 2025 and who keeps a home for a dependent child is a qualifying surviving spouse. A qualifying child must pass relationship, residence (more than half the year), age (under 19, or under 24 if a student), support and joint-return tests. A qualifying relative must have 2026 gross income below **$5,300** and get over half their support from the taxpayer. Married filing separately is usually dearer; the worked case shows by how much.

## Scope and who this is for

In scope: choosing the 2026 filing status and deciding who is a dependent, for a US citizen or resident filing Form 1040.

Out of scope, and where it goes:

| Topic | Skill |
| --- | --- |
| Standard deduction and rate schedule for each status | `us-federal-income-tax-return-1040` |
| Itemizing, and the separate-return rule when a spouse itemizes | `us-schedule-a-itemized-deductions` |
| Child tax credit, earned income credit amounts | `us-federal-income-tax-return-1040` |
| Nonresident aliens and dual-status years | `us-form-1040-nr-nonresident-return` |

## Ask the client first

1. Married on 31 December 2026? If separated, is there a final decree of divorce or separate maintenance? Did the spouse die in 2026, 2025 or 2024?
2. Who lived in the home, and for how many nights of 2026?
3. Who paid the rent or mortgage, property tax, insurance, utilities and food for the home, and how much in total?
4. For each possible dependent: relationship, date of birth, student status, whether disabled, their own gross income, total support and who paid it, and whether they file a joint return.
5. Can anyone else (the other parent, a grandparent) claim the same child?
6. For married couples: each spouse's income, deductions, student loans, medical costs and any reason to keep liability separate (a spouse's unpaid tax, a doubt about their return).

## The method, step by step

### Rates, bands and thresholds

| Item | Amount, 2026 | Source |
| --- | --- | --- |
| Qualifying relative gross income limit (section 152(d)(1)(B)) | USD 5,300 | [Rev. Proc. 2025-32, section 4.23](https://www.irs.gov/pub/irs-drop/rp-25-32.pdf) |
| Qualifying child age limit | under 19 at year end, or under 24 if a student | [26 U.S.C. 152(c)(3)](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap1-subchapB-partV-sec152.htm) |
| Residence test, qualifying child and head of household | more than one-half of the taxable year | [26 U.S.C. 152(c)(1)(B)](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap1-subchapB-partV-sec152.htm) |
| Support test, qualifying relative | over one-half of support from the taxpayer | [26 U.S.C. 152(d)(1)(C)](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap1-subchapB-partV-sec152.htm) |
| Qualifying surviving spouse: spouse died within | two taxable years before the year | [26 U.S.C. 2(a)](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap1-subchapA-partI-sec2.htm) |
| Standard deduction, married filing jointly and surviving spouses | USD 32,200 | [Rev. Proc. 2025-32](https://www.irs.gov/pub/irs-drop/rp-25-32.pdf) |
| Standard deduction, head of household | USD 24,150 | [Rev. Proc. 2025-32](https://www.irs.gov/pub/irs-drop/rp-25-32.pdf) |
| Standard deduction, single | USD 16,100 | [Rev. Proc. 2025-32](https://www.irs.gov/pub/irs-drop/rp-25-32.pdf) |
| Standard deduction, married filing separately | USD 16,100 | [Rev. Proc. 2025-32](https://www.irs.gov/pub/irs-drop/rp-25-32.pdf) |

Rate schedules for each status are in `us-federal-income-tax-return-1040`.

### Step 1: married or not on 31 December

A person is married for the whole year if married on the last day of it. A person legally separated under a final decree of divorce or separate maintenance is unmarried. If the spouse died during 2026, the survivor may still file jointly for 2026.

### Step 2: married, so joint or separate

Joint: one return, both incomes, both spouses liable for all the tax. Separate: each spouse reports their own income. Separate filers lose or are limited on many items (for example, the senior, tips and overtime deductions need a joint return; see `us-federal-income-tax-return-1040`), and if one spouse itemizes the other cannot take the standard deduction (26 U.S.C. 63(c)(6)(A)). Run both and compare (Case 1). A married person living apart from the spouse for the last six months of the year who keeps a home for a qualifying child may be treated as unmarried and file as head of household; refer if relying on this.

### Step 3: not married, so head of household, surviving spouse or single

1. **Qualifying surviving spouse:** spouse died in 2024 or 2025, not remarried, and the taxpayer keeps a home that is the main home all year of a son, daughter, stepson or stepdaughter the taxpayer can claim. Uses the joint rate schedule and standard deduction.
2. **Head of household:** not married, not a surviving spouse, pays over half the cost of keeping up the home, and the home is for more than half the year the main home of a qualifying child (or other dependent relative); or the taxpayer keeps up a home that is the main home of a dependent father or mother, which need not be the taxpayer's own home (26 U.S.C. 2(b)).
3. Otherwise **single**.

### Step 4: dependents

**Qualifying child** (26 U.S.C. 152(c)), all five tests:
1. Relationship: child, stepchild, foster child, sibling, step-sibling, or a descendant of any of them.
2. Residence: same main home as the taxpayer for more than half the year (temporary absences count as time at home).
3. Age: younger than the taxpayer and under 19 at year end, or a student under 24; any age if permanently and totally disabled.
4. Support: the child did not provide over half of their own support.
5. Joint return: the child did not file a joint return, other than only to claim a refund.

Where two people can claim the same child, the tie-breaker rules in 152(c)(4) apply: a parent over a non-parent; between parents, the one the child lived with longer, then higher AGI.

**Qualifying relative** (26 U.S.C. 152(d)), all four tests:
1. Not anyone's qualifying child.
2. Relationship (parent, grandparent, sibling, in-law and others listed) or a member of the household all year.
3. Gross income for 2026 below USD 5,300.
4. The taxpayer provides over half of the person's total support for the year (a multiple support agreement can assign it).

Every dependent must also be a US citizen, national or resident, or a resident of Canada or Mexico (adopted children have a special rule), and must not file a joint return.

## Boundary and exception table

| Situation | Treatment |
| --- | --- |
| Divorced parents, child lives with the mother, father has a signed Form 8332 | Father claims the child for the child tax credit; mother keeps head of household if she meets it (head of household uses 152(c) without 152(e)) |
| Parent in a nursing home paid for by the taxpayer | Taxpayer may file head of household if the parent is a dependent (26 U.S.C. 2(b)(1)(B)) |
| Spouse is a nonresident alien | Joint return only by election to treat as resident; otherwise separate; refer |
| Child born or died in 2026 | Treated as living with the taxpayer all year if the home was the child's home while alive |
| Adult child aged 25 earning USD 6,000 | Fails qualifying child (age) and qualifying relative (gross income above USD 5,300) |

### Defaults when a fact is missing

| Missing fact | Default |
| --- | --- |
| Separation decree status | Treat as married; flag |
| Support figures | Ask; do not assume the over-half test is met |
| Nights in the home | Ask; school and medical absences count as time at home |

### Red flags to raise with the client

| Red flag | Why |
| --- | --- |
| Both parents claim the same child | IRS matches SSNs; the tie-breaker decides; second return is rejected |
| Head of household with no dependent named | Most common status error; the qualifying person must be shown |
| Married filing separately chosen "to be fair" | Usually costs tax; run Case 1 |

## Worked cases

**Case 1, a decision: married filing jointly or separately?** A married couple with no dependents and no other income or adjustments: spouse A earns USD 150,000 and spouse B USD 30,000. Both take the standard deduction.

Joint: taxable income 180,000 less 32,200 = USD 147,800. Tax on the 2026 joint schedule: USD 11,600 plus 22% of the excess over USD 100,800 = 11,600 + 10,340 = USD 21,940. Separate (the separate schedule matches single up to the 35% band): A's taxable income 150,000 less 16,100 = USD 133,900; tax USD 17,966 plus 24% of the excess over USD 105,700 = USD 24,734. B's taxable income 30,000 less 16,100 = USD 13,900; tax USD 1,240 plus 12% of the excess over USD 12,400 = USD 1,420. Separate total USD 26,154. Filing jointly saves USD 4,214. Recommend joint unless a non-tax reason (separate liability) outweighs USD 4,214.

```oa-check
name: Married filing jointly against separately (2026)
inputs:
  wages_a: 150000
  wages_b: 30000
  std_joint: 32200
  std_separate: 16100
steps:
  - joint_taxable: wages_a + wages_b - std_joint
  - joint_tax: 11600 + 0.22 * (joint_taxable - 100800)
  - a_taxable: wages_a - std_separate
  - a_tax: 17966 + 0.24 * (a_taxable - 105700)
  - b_taxable: wages_b - std_separate
  - b_tax: 1240 + 0.12 * (b_taxable - 12400)
  - separate_tax: a_tax + b_tax
  - joint_saves: separate_tax - joint_tax
expected:
  joint_taxable: 147800.00
  joint_tax: 21940.00
  a_tax: 24734.00
  b_tax: 1420.00
  separate_tax: 26154.00
  joint_saves: 4214.00
```

**Case 2, a parent as qualifying relative, and head of household.** An unmarried taxpayer pays USD 13,000 of the USD 24,000 total support of her mother, who lives in her own flat that the taxpayer pays to keep up. The mother's 2026 gross income is USD 5,000 (her Social Security benefits are not gross income here if untaxed). Support test: 13,000 is more than half of 24,000 (USD 12,000) by USD 1,000. Gross income test: 5,000 is USD 300 below the USD 5,300 limit. The mother is a qualifying relative, and because the taxpayer keeps up the mother's home, the taxpayer files as head of household: standard deduction USD 24,150 against USD 16,100 single, USD 8,050 more.

```oa-check
name: Qualifying relative tests and head of household gain (2026)
inputs:
  taxpayer_support: 13000
  total_support: 24000
  parent_gross_income: 5000
  gi_limit: 5300
  std_hoh: 24150
  std_single: 16100
steps:
  - support_margin: taxpayer_support - total_support / 2
  - income_margin: gi_limit - parent_gross_income
  - hoh_gain: std_hoh - std_single
expected:
  support_margin: 1000.00
  income_margin: 300.00
  hoh_gain: 8050.00
```

## When to refuse or refer

| Code | Situation | Action |
| --- | --- | --- |
| R-FS-NRA | Either spouse a nonresident alien, or a dual-status year | Refer: election under section 6013(g) or (h); see `us-form-1040-nr-nonresident-return` |
| R-FS-ABANDON | Married, living apart, wants head of household | Refer: confirm the six-month and home tests before filing |
| R-FS-INNOCENT | Spouse's joint-return liability in doubt | Refer: innocent spouse relief (Form 8857) |
| R-FS-MULTISUPPORT | No one person pays over half of a relative's support | Refer: multiple support agreement (Form 2120) |

## Filing and payment

Filing status is chosen on the 2026 Form 1040, due **15 April 2027**. Joint filers can switch to separate only until the due date; separate filers can amend to joint within the time for an amended return. Dependents are listed on Form 1040 with their SSN or other identifying number. See `us-federal-income-tax-return-1040`.

## Completion checklist

- Marital status on 31 December 2026 confirmed, with any decree.
- Both joint and separate computed for married couples.
- Head of household: cost of the home and the qualifying person recorded.
- Each dependent tested against every qualifying child or relative test, with nights and support figures.
- Tie-breaker or Form 8332 applied where two people could claim the same child.

## Sources

| Source | URL | Read on |
| --- | --- | --- |
| Rev. Proc. 2025-32. Read for section 4.23 (qualifying relative gross income limit $5,300), the 2026 standard deductions and rate schedules. | https://www.irs.gov/pub/irs-drop/rp-25-32.pdf | 2026-11-13 |
| 26 U.S.C. 152 (govinfo). Read for (c) qualifying child tests, (c)(4) tie-breakers, (d) qualifying relative tests. | https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap1-subchapB-partV-sec152.htm | 2026-11-13 |
| 26 U.S.C. 2 (govinfo). Read for (a) surviving spouse and (b) head of household, including a parent's home. | https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap1-subchapA-partI-sec2.htm | 2026-11-13 |
| 26 U.S.C. 63 (govinfo). Read for (c)(6)(A): no standard deduction for a separate filer whose spouse itemizes. | https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap1-subchapB-partI-sec63.htm | 2026-11-13 |

Not yet confirmed: IRS Pub. 501 for 2026 was not read; the abandoned-spouse rule (section 7703(b)), the citizenship test and the birth or death rule are stated from the general law and should be checked against the 2026 Pub. 501 before relying on them.

## Today's figures and who stands behind this skill

This file is an AI skill (tax rules your AI follows) from OpenAccountants, copied on 2026-11-13. Rates, thresholds and deadlines change. For the current version of this skill, its official sources and the named accountant (if any) who stands behind it, call `get_skill` with slug `us-filing-status-and-dependents` on the OpenAccountants connector (https://www.openaccountants.com/connect), or read https://www.openaccountants.com/skills/us-filing-status-and-dependents. If neither is available, confirm every figure against the official source pages cited above before relying on it.
