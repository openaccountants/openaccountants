---
name: us-schedule-a-itemized-deductions
description: "Compute a US individual's 2026 itemized deductions on Schedule A (Form 1040) and decide whether to itemize or take the standard deduction. Covers medical expenses above 7.5% of AGI, the state and local tax cap of $40,400 with the 30% phase-down above $505,000 of modified AGI and the $10,000 floor, the home mortgage interest limit of $750,000 ($375,000 married filing separately) of acquisition debt, mortgage insurance premiums, the 0.5% charitable floor and 60% cash limit, and the 2/37 reduction for itemizers in the 37% bracket under the One Big Beautiful Bill Act. Trigger on \"Schedule A\", \"itemize\", \"itemized deductions\", \"SALT cap\", \"mortgage interest deduction\", \"medical expense deduction\", \"charitable deduction\". Federal only."
license: "AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)"
metadata:
  source: openaccountants
  openaccountants_url: "https://www.openaccountants.com/skills/us-schedule-a-itemized-deductions"
  jurisdiction: "US"
  tax_year: "2026"
  last_updated: "2026-11-13"
---

# US Schedule A itemized deductions, tax year 2026

> **Source-cited draft.** Built from Public Law 119-21 (the One Big Beautiful Bill Act), Rev. Proc. 2025-32 and 26 U.S.C. 63, 163 and 213, read on 2026-11-13. No accountant has reviewed it. All outputs must be reviewed by a qualified tax professional before filing.

**Answer first.** For 2026, itemize only when the Schedule A total beats the standard deduction for the filing status (the figures live in `us-federal-income-tax-return-1040`). The main 2026 limits: medical expenses count only above **7.5% of AGI**; state and local taxes are capped at **$40,400**, cut by **30%** of modified AGI above **$505,000**, never below **$10,000**; mortgage interest is limited to **$750,000** of acquisition debt (**$375,000** married filing separately) for debt taken on after 15 December 2017; cash gifts to charity count only above **0.5%** of the contribution base; and an itemizer in the 37% bracket loses **2/37** of the lesser of the deductions and the income above where that bracket begins, which caps the value of each dollar at about 35 cents.

## Scope and who this is for

In scope: one individual's (or one married couple's) Schedule A for tax year 2026: medical and dental expenses, taxes paid, interest paid, gifts to charity, casualty losses from federally or state declared disasters, the section 68 reduction, and the choice between itemizing and the standard deduction.

Out of scope, and where it goes:

| Topic | Skill |
| --- | --- |
| Standard deduction amounts, rate schedules and the full Form 1040 | `us-federal-income-tax-return-1040` |
| Which filing status, and who is a dependent | `us-filing-status-and-dependents` |
| Planning charitable gifts (bunching, donor-advised funds, appreciated stock) | `us-charitable-giving-strategies` |
| Home office share of mortgage interest and taxes | `us-schedule-c-and-se-computation` |
| What else changed for 2026 | `us-2026-federal-tax-changes` |

## Ask the client first

1. Filing status, and if married filing separately, whether the other spouse itemizes (if so, this taxpayer must itemize too).
2. Adjusted gross income and modified AGI (AGI plus any excluded foreign earned income or possessions income) for 2026.
3. Medical and dental costs paid in 2026 and not reimbursed, including health insurance premiums paid with after-tax money.
4. State and local income tax (or general sales tax instead), real estate tax and personal property tax paid in 2026, separately.
5. Form 1098 for each mortgage: interest, mortgage insurance premiums, the loan balance, the date the debt was taken on, and what the money was used for.
6. Gifts to charity: cash and property, the recipient, and receipts or written acknowledgements.
7. Any casualty loss, and whether it came from a federally declared or state declared disaster.
8. Expected taxable income, to see whether the 37% bracket and the 2/37 reduction apply.

## The method, step by step

### Rates, bands and thresholds

| Item | Amount, 2026 | Source |
| --- | --- | --- |
| Medical and dental expenses count above this share of AGI | 7.5 percent | [26 U.S.C. 213(a)](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap1-subchapB-partVII-sec213.htm) |
| State and local tax cap, tax year 2026 | USD 40,400 | [Public Law 119-21, section 70120](https://www.govinfo.gov/content/pkg/PLAW-119publ21/html/PLAW-119publ21.htm) |
| Phase-down rate on modified AGI above the threshold | 30 percent | [Public Law 119-21, section 70120](https://www.govinfo.gov/content/pkg/PLAW-119publ21/html/PLAW-119publ21.htm) |
| Phase-down threshold, tax year 2026 | USD 505,000 | [Public Law 119-21, section 70120](https://www.govinfo.gov/content/pkg/PLAW-119publ21/html/PLAW-119publ21.htm) |
| The phase-down never takes the cap below | USD 10,000 | [Public Law 119-21, section 70120](https://www.govinfo.gov/content/pkg/PLAW-119publ21/html/PLAW-119publ21.htm) |
| Mortgage acquisition debt limit, debt incurred after 15 December 2017 | USD 750,000 (USD 375,000 married filing separately) | [26 U.S.C. 163(h)(3)(F)](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap1-subchapB-partVI-sec163.htm); made permanent by [Public Law 119-21, section 70108](https://www.govinfo.gov/content/pkg/PLAW-119publ21/html/PLAW-119publ21.htm) |
| Charitable floor for individuals | 0.5 percent | [Public Law 119-21, section 70425](https://www.govinfo.gov/content/pkg/PLAW-119publ21/html/PLAW-119publ21.htm) |
| Cash gifts to public charities, limit | 60 percent | [Public Law 119-21](https://www.govinfo.gov/content/pkg/PLAW-119publ21/html/PLAW-119publ21.htm) |
| Reduction of itemized deductions in the 37% bracket | 2/37 | [Public Law 119-21, section 70111](https://www.govinfo.gov/content/pkg/PLAW-119publ21/html/PLAW-119publ21.htm) |
| Where the 37% bracket begins, married filing jointly | USD 768,700 | [Rev. Proc. 2025-32](https://www.irs.gov/pub/irs-drop/rp-25-32.pdf) |
| Where the 37% bracket begins, single and head of household | USD 640,600 | [Rev. Proc. 2025-32](https://www.irs.gov/pub/irs-drop/rp-25-32.pdf) |
| Where the 37% bracket begins, married filing separately | USD 384,350 | [Rev. Proc. 2025-32](https://www.irs.gov/pub/irs-drop/rp-25-32.pdf) |

The SALT cap rises to 101 percent of the prior year's amount each year through 2029 and falls back to USD 10,000 from 2030 (library, Public Law 119-21). The standard deduction to compare against is in `us-federal-income-tax-return-1040`.

### Step 1: medical and dental

Add unreimbursed medical and dental costs paid in 2026. Subtract 7.5% of AGI. Only the excess goes on Schedule A; a negative result is zero.

### Step 2: taxes paid

1. Add state and local income tax (or, by election, general sales tax), real estate tax and personal property tax. Foreign real estate tax is not deductible for an individual; foreign income tax goes to the foreign tax credit or here, not both.
2. Work out the cap: USD 40,400 less 30% of modified AGI above USD 505,000, but not below USD 10,000. Married filing separately: the Act uses half the cap and half the threshold for a separate return (section 70120). Modified AGI is AGI plus amounts excluded under sections 911, 931 or 933.
3. Deduct the smaller of the taxes paid and the cap.

### Step 3: interest paid

1. Home mortgage interest on a main and one second home counts only for acquisition debt (money used to buy, build or substantially improve the home that secures it). Interest on home equity debt used for anything else is not deductible.
2. If acquisition debt taken on after 15 December 2017 exceeds USD 750,000 (USD 375,000 married filing separately), deduct interest times the limit divided by the average balance. Older debt keeps the USD 1,000,000 (USD 500,000) limit.
3. From 2026 qualified mortgage insurance premiums are treated as interest again (section 70108).
4. Investment interest goes through Form 4952 and is limited to net investment income.

### Step 4: gifts to charity

1. Add cash and property gifts to qualified organizations, with receipts.
2. Apply the percentage limits (60% of the contribution base for cash to public charities; lower limits for property and private foundations; carry the excess forward up to 5 years).
3. Then subtract 0.5% of the contribution base (generally AGI). Gifts lost to this floor carry forward only from a year in which a percentage limit was also exceeded.

### Step 5: casualty and other

Personal casualty losses count only if they come from a federally declared disaster or, from 2026, a state declared disaster (section 70109). Miscellaneous itemized deductions subject to the old 2% floor stay gone (section 70110). Gambling losses and the other items on Schedule A line 16 follow their own rules.

### Step 6: the 37% bracket reduction (section 68)

If taxable income plus itemized deductions exceeds where the 37% bracket begins, reduce itemized deductions by 2/37 of the lesser of (a) the itemized deductions and (b) that excess. This applies after every other limit. It does not apply when computing the qualified business income deduction. In effect, a deduction is worth 35% instead of 37% at the top.

### Step 7: itemize or standard

Compare the total from step 6 with the standard deduction for the filing status, plus any age or blindness amount. Take the larger, unless married filing separately and the spouse itemizes. Non-itemizers can still take the cash charitable deduction (USD 1,000, USD 2,000 joint) under section 170(p) and the Schedule 1-A deductions; see `us-federal-income-tax-return-1040`.

## Boundary and exception table

| Situation | Treatment |
| --- | --- |
| Married filing separately, spouse itemizes | Must itemize, even if the standard deduction is larger (26 U.S.C. 63(c)(6)(A)) |
| Modified AGI above USD 606,333 | SALT cap is at the USD 10,000 floor (40,400 less 10,000 = 30,400; 30,400 / 0.30 = 101,333; 505,000 + 101,333 = 606,333) |
| State tax refund received in 2026 for 2025 | Taxable only to the extent the 2025 deduction gave a benefit; check the 2025 Schedule A |
| Pass-through entity tax paid by a partnership or S corporation | Deducted by the entity, not on Schedule A; not counted against the cap |
| Mortgage refinanced above the old balance | Only the part replacing acquisition debt keeps acquisition status |
| Home equity loan used to build an addition | Acquisition debt, deductible within the limit |
| Gift of appreciated stock held over a year | Fair market value, generally limited to 30% of the contribution base; see `us-charitable-giving-strategies` |

### Defaults when a fact is missing

| Missing fact | Default |
| --- | --- |
| Date the mortgage was taken on | Assume after 15 December 2017 (the lower limit) and flag |
| Modified AGI | Use AGI, and flag foreign income exclusions |
| Charity receipts | Exclude the gift until a receipt is produced |

### Red flags to raise with the client

| Red flag | Why |
| --- | --- |
| Itemized total within USD 2,000 of the standard deduction | Bunching gifts or prepaying may change the answer; see `us-charitable-giving-strategies` |
| Large medical deduction claimed with high AGI | 7.5% floor usually removes it; check the arithmetic |
| Two homes plus a home equity line | Use of funds decides deductibility; trace it |

## Worked cases

**Case 1, a decision: itemize or take the standard deduction?** A married couple filing jointly, both under 65, has AGI and modified AGI of USD 600,000. In 2026 they pay USD 45,000 of state income and property tax, USD 18,000 of mortgage interest on an average balance of USD 900,000 borrowed in 2021 to buy their home, USD 12,000 of cash gifts to public charities, and USD 20,000 of medical costs.

SALT cap: 40,400 less 30% of (600,000 less 505,000) = 40,400 less 28,500 = USD 11,900, above the USD 10,000 floor. Taxes deducted: USD 11,900. Mortgage interest: 18,000 x 750,000 / 900,000 = USD 15,000. Charity: 12,000 less 0.5% of 600,000 = USD 9,000. Medical: 20,000 is below 7.5% of 600,000 (USD 45,000), so nil. Itemized total USD 35,900. Taxable income of about USD 564,100 is below USD 768,700, so no section 68 reduction. The 2026 joint standard deduction is USD 32,200 (`us-federal-income-tax-return-1040`). Itemizing wins by USD 3,700.

```oa-check
name: Itemize or standard, married filing jointly with SALT phase-down (2026)
inputs:
  magi: 600000
  salt_paid: 45000
  mortgage_interest: 18000
  average_balance: 900000
  cash_gifts: 12000
  medical: 20000
  standard: 32200
steps:
  - salt_cap: max(40400 - 0.30 * max(magi - 505000, 0), 10000)
  - salt: min(salt_paid, salt_cap)
  - interest: mortgage_interest * min(750000, average_balance) / average_balance
  - charity: max(cash_gifts - 0.005 * magi, 0)
  - med: max(medical - 0.075 * magi, 0)
  - itemized: salt + interest + charity + med
  - itemizing_wins_by: itemized - standard
expected:
  salt_cap: 11900.00
  interest: 15000.00
  charity: 9000.00
  med: 0.00
  itemized: 35900.00
  itemizing_wins_by: 3700.00
```

**Case 2, the 37% bracket reduction, single.** A single filer has AGI of USD 900,000 and USD 100,000 of itemized deductions after every other limit (the SALT cap is at its USD 10,000 floor). Taxable income before section 68 is USD 800,000; plus the deductions, USD 900,000, which is USD 259,400 above USD 640,600. The lesser of USD 100,000 and USD 259,400 is USD 100,000. Reduction: 2/37 x 100,000 = USD 5,405.41. Allowed: USD 94,594.59. At 37%, that saves USD 35,000, which is 35% of the USD 100,000 spent.

```oa-check
name: Section 68 reduction for a single top-bracket itemizer (2026)
inputs:
  agi: 900000
  itemized_before: 100000
  bracket_37_start: 640600
steps:
  - excess: max(agi - bracket_37_start, 0)
  - reduction: round(2 / 37 * min(itemized_before, excess), 2)
  - allowed: itemized_before - reduction
  - tax_value: round(allowed * 0.37, 2)
expected:
  excess: 259400.00
  reduction: 5405.41
  allowed: 94594.59
  tax_value: 35000.00
```

## When to refuse or refer

| Code | Situation | Action |
| --- | --- | --- |
| R-SA-NRA | Nonresident alien (Form 1040-NR) | Refer: Schedule A (Form 1040-NR) rules differ; see `us-form-1040-nr-nonresident-return` |
| R-SA-INVINT | Investment interest above net investment income | Refer: Form 4952 computation |
| R-SA-CASUALTY | Disaster casualty loss | Refer: Form 4684 and disaster rules |
| R-SA-PROPERTY | Non-cash gifts over USD 5,000 | Refer: qualified appraisal and Form 8283 Section B |
| R-SA-MIXEDDEBT | Mortgage debt partly pre-2017, partly later, or mixed-use proceeds | Flag: trace and allocate before applying the limit |

## Filing and payment

Schedule A is attached to the 2026 Form 1040, due **15 April 2027**; the total goes on Form 1040 line 12e. Payment and extension rules are in `us-federal-income-tax-return-1040`.

## Completion checklist

- Filing status confirmed, and the spouse's choice known if separate.
- Medical floor at 7.5% of AGI applied.
- SALT cap computed from modified AGI, not AGI, with the USD 10,000 floor.
- Mortgage debt date and use of proceeds recorded; limit applied by average balance.
- 0.5% charitable floor applied after the percentage limits; carryforwards recorded.
- Section 68 run if taxable income plus deductions passes where the 37% bracket begins.
- Itemized total compared with the standard deduction for the filing status.

## Sources

| Source | URL | Read on |
| --- | --- | --- |
| Public Law 119-21 (One Big Beautiful Bill Act). Read for section 70108 (mortgage limit made permanent, mortgage insurance premiums), 70109 (casualty losses, state declared disasters), 70110 (miscellaneous deductions), 70111 (section 68, 2/37), 70120 (SALT cap $40,400, $505,000, 30 percent, $10,000 floor, half for a separate return, modified AGI definition) and 70425 (0.5 percent floor). | https://www.govinfo.gov/content/pkg/PLAW-119publ21/html/PLAW-119publ21.htm | 2026-11-13 |
| Rev. Proc. 2025-32. Read for the 2026 rate schedules (37% bracket starts) and standard deductions. | https://www.irs.gov/pub/irs-drop/rp-25-32.pdf | 2026-11-13 |
| 26 U.S.C. 213 (govinfo). Read for (a) the 7.5 percent of AGI floor. | https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap1-subchapB-partVII-sec213.htm | 2026-11-13 |
| 26 U.S.C. 163 (govinfo). Read for (h)(3)(F): $750,000 ($375,000) acquisition debt limit and the 15 December 2017 date. | https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap1-subchapB-partVI-sec163.htm | 2026-11-13 |
| 26 U.S.C. 63 (govinfo). Read for (c)(6)(A): no standard deduction for a separate filer whose spouse itemizes. | https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap1-subchapB-partI-sec63.htm | 2026-11-13 |

Not yet confirmed: the 2026 Schedule A and its instructions were not read, so line numbers other than Form 1040 line 12e are not quoted, and the IRS has not yet printed the halved 2026 separate-return SALT amounts, so they are not stated as figures here.

## Today's figures and who stands behind this skill

This file is an AI skill (tax rules your AI follows) from OpenAccountants, copied on 2026-11-13. Rates, thresholds and deadlines change. For the current version of this skill, its official sources and the named accountant (if any) who stands behind it, call `get_skill` with slug `us-schedule-a-itemized-deductions` on the OpenAccountants connector (https://www.openaccountants.com/connect), or read https://www.openaccountants.com/skills/us-schedule-a-itemized-deductions. If neither is available, confirm every figure against the official source pages cited above before relying on it.
