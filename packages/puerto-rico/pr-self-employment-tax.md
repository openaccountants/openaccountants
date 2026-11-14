---
name: pr-self-employment-tax
description: >
  Work out and file federal self-employment tax for a bona fide resident of Puerto Rico for tax year 2026. Explains why Puerto Rico source income excluded from federal income tax under section 933 still carries self-employment tax, when Form 1040-SS is filed instead of Form 1040 with Schedule SE, the USD 400 net earnings test, how wages on Form 499R-2/W-2PR reduce the social security base, the Additional Medicare Tax lines on the 2026 Form 1040-SS, the additional child tax credit in Part II (limited by social security and Medicare taxes paid, not by earned income), estimated tax when self-employment tax will be USD 1,000 or more, and the 15 April 2027 due date with the Form 4868 extension that does not extend payment. The 2026 self-employment rates, wage base and Schedule SE steps are linked to us-schedule-c-and-se-computation. Trigger on "Puerto Rico self-employment tax", "Form 1040-SS", "1040-PR", "Schedule SE Puerto Rico", "Puerto Rico additional child tax credit", "do I pay social security in Puerto Rico".
version: "1.0"
jurisdiction: PR
tax_year: 2026
last_updated: 2026-11-14
category: international
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
tier: 2
domain: income-tax
type: computation
---

# Puerto Rico: federal self-employment tax, tax year 2026

> **Source-cited draft.** Built from the Instructions for Form 1040-SS (2025), the 2026 draft Form 1040-SS (created 21 September 2026, not for filing), the 2026 Schedule SE and its instructions, IRS Publication 570 (2025) and Publication 1321 (October 2026), read on 2026-11-14. No accountant has reviewed it. All outputs must be reviewed by a qualified tax professional before filing.

**Answer first.** A self-employed bona fide resident of Puerto Rico pays federal self-employment tax to the IRS on net self-employment earnings of **USD 400** or more, even though the same profit is Puerto Rico source income excluded from federal income tax. If they have no Form 1040 filing requirement, they file **Form 1040-SS** with Schedule C and Schedule SE; otherwise Schedule SE goes with Form 1040. The 2026 rates (12.4% plus 2.9%), the 92.35% factor and the USD 184,500 social security wage base are owned by `us-schedule-c-and-se-computation`. The 2026 return is due **15 April 2027**; Form 4868 extends filing to 15 October 2027, not payment. Expected self-employment tax of **USD 1,000** or more calls for estimated payments on Form 1040-ES. A bona fide resident with a qualifying child can claim the additional child tax credit on Form 1040-SS Part II, capped by the social security and Medicare taxes paid. Paying Hacienda does not pay the IRS.

## Scope and who this is for

In scope: an individual (United States citizen, resident alien, or a bona fide resident of Puerto Rico who is a nonresident alien of the United States) with self-employment income in tax year 2026 who is a bona fide resident of Puerto Rico: whether federal self-employment tax is due, which form carries it, how wages and the spouse's business interact, the Additional Medicare Tax, the additional child tax credit on Form 1040-SS, estimated tax, filing and payment.

Out of scope, and where it goes:

| Topic | Skill |
| --- | --- |
| Schedule C lines, the 2026 Schedule SE computation, optional methods, the deductible half | `us-schedule-c-and-se-computation` |
| Whether the person is a bona fide resident, and whether Form 1040 is required | `pr-federal-residence-and-filing` |
| Puerto Rico income tax on the same profit, and the Puerto Rico optional tax | `pr-individual-income-tax` |
| Child tax credit amounts and the qualifying child tests | `us-child-tax-credit-and-eitc` |
| Estimated tax safe harbours and due dates | `us-quarterly-estimated-tax` |
| Household employees (Schedule H) | `us-household-employment-schedule-h` |
| Partnership self-employment income | `us-form-1065-partnership` |

## Ask the client first

1. **Bona fide residence for all of 2026**, and whether any income is from outside Puerto Rico or is United States Government pay (this decides Form 1040 against Form 1040-SS).
2. **Net profit for each business** for 2026, and which spouse carries on each business (or whether both take part).
3. **Wages:** social security wages and Medicare wages on every Form 499R-2/W-2PR or W-2, and social security tax withheld.
4. **Filing status** and spouse's income, for the Additional Medicare Tax threshold.
5. **Children:** each child under 17 at the end of 2026 with a social security number valid for employment issued before the return's due date, and the taxpayer's own SSN.
6. **Payments:** 2026 estimated federal payments and any overpayment applied from the 2025 return.

## The method, step by step

### Rates, bands and thresholds

The 2026 self-employment tax rates, the 92.35% net earnings factor, the USD 184,500 wage base, the Additional Medicare Tax thresholds and the optional-method amounts are in `us-schedule-c-and-se-computation` and are not restated here. The figures below are the ones this pack owns.

| Item | Figure | Condition | Source |
| --- | --- | --- | --- |
| Form 1040-SS filing test | Net earnings from self-employment of USD 400 or more | Bona fide resident of Puerto Rico not required to file Form 1040 | [Instructions for Form 1040-SS (2025), Who Must File](https://www.irs.gov/pub/irs-pdf/i1040ss.pdf) |
| Church employee income test | USD 108.28 or more | Wages from an electing church or church-controlled organization | [Instructions for Form 1040-SS (2025), Employees of Churches](https://www.irs.gov/pub/irs-pdf/i1040ss.pdf) |
| Estimated tax prompt | Expected self-employment tax of USD 1,000 or more | Use Form 1040-ES; see `us-quarterly-estimated-tax` | [Instructions for Form 1040-SS (2025), Reminders](https://www.irs.gov/pub/irs-pdf/i1040ss.pdf) |
| Additional child tax credit, Part II line 2 | USD 1,700 per qualifying child | 2026 draft Form 1040-SS; child under 17 with a valid SSN | [Form 1040-SS (2026) draft, Part II](https://www.irs.gov/pub/irs-dft/f1040ss--dft.pdf) |
| Child tax credit, Part II line 7 | USD 2,200 per qualifying child, phase-out 5% of modified AGI over USD 400,000 joint or USD 200,000 other | Same | [Form 1040-SS (2026) draft, Part II](https://www.irs.gov/pub/irs-dft/f1040ss--dft.pdf) |
| Due date, calendar 2026 | 15 April 2027 | Fiscal year: 15th day of the 4th month after year end | [Instructions for Form 1040-SS (2025), When To File](https://www.irs.gov/pub/irs-pdf/i1040ss.pdf) |
| Extension for bona fide residents of Puerto Rico | Automatic 6 months, to 15 October 2027 | Form 4868 filed by the regular due date; filing only, interest runs from 15 April | [Instructions for Form 1040-SS (2025), Extension of Time To File](https://www.irs.gov/pub/irs-pdf/i1040ss.pdf) |

The 2026 child tax credit amounts on the draft form match `us-child-tax-credit-and-eitc`. The 2026 instructions for Form 1040-SS were not published on the read date; the rules here come from the 2025 instructions, and the 2026 line numbers from the 2026 draft form.

### Step 1: is self-employment tax due?

Self-employment tax is paid to the IRS on net self-employment earnings of USD 400 or more whether or not the earnings are excludable from gross income, and whether or not a federal income tax return must otherwise be filed. Bona fide residents of the territories are treated as United States residents for this purpose, and the rule also reaches a bona fide resident who is a nonresident alien of the United States. [Publication 570, Self-Employment Tax](https://www.irs.gov/pub/irs-pdf/p570.pdf). The test is net earnings after the 92.35% factor (Schedule SE line 4c), not gross receipts.

### Step 2: which form

| Situation | Form |
| --- | --- |
| Must file Form 1040 (income outside Puerto Rico above the apportioned filing test, United States Government pay, net investment income tax) | Schedule SE attached to Form 1040 or 1040-SR |
| No Form 1040 requirement, net self-employment earnings of USD 400 or more | Form 1040-SS with Schedule SE and Schedule C or F |
| No Form 1040 requirement, under USD 400, but household employment taxes, uncollected employee social security and Medicare tax, Additional Medicare Tax, excess social security withheld, or the additional child tax credit | Form 1040-SS for those items |

Never file Form 1040-SS together with Form 1040. Form 1040-PR is discontinued; from 2023 Puerto Rico filers use Form 1040-SS (English). File only one Form 1040-SS per year. [Instructions for Form 1040-SS (2025), Who Must File and Form 1040-SS redesign](https://www.irs.gov/pub/irs-pdf/i1040ss.pdf); [Publication 570, Forms to file](https://www.irs.gov/pub/irs-pdf/p570.pdf).

### Step 3: Schedule C for each business

Include the Puerto Rico source profit on Schedule C even though it is excluded from federal income tax. With two or more businesses, attach a Schedule C for each and combine the net earnings on one Schedule SE; a loss in one reduces the other. Each spouse with self-employment income completes their own Schedule SE, even on a joint Form 1040-SS. In Puerto Rico, if only one spouse takes part in the business, all of its income is that spouse's; if both take part, it is split by their distributive shares; a qualified joint venture or partnership follows the Schedule SE instructions. [Instructions for Form 1040-SS (2025), Business Owned and Operated by Spouses](https://www.irs.gov/pub/irs-pdf/i1040ss.pdf).

### Step 4: Schedule SE

Run Schedule SE Part I exactly as in `us-schedule-c-and-se-computation`. Two Puerto Rico points:
- **Wages:** social security wages and tips on Form 499R-2/W-2PR go on line 8a and use up the 2026 wage base first. Each spouse's base is their own.
- **Line 13** (the deductible half): skip it on Form 1040-SS. On Form 1040, the half is not deductible to the extent it relates to excluded Puerto Rico self-employment income. [Instructions for Schedule SE (2026), Line 13](https://www.irs.gov/pub/irs-pdf/i1040sse.pdf); [Publication 1321, Caution under Qualified Business Income Deduction](https://www.irs.gov/pub/irs-pdf/p1321.pdf).

### Step 5: Form 1040-SS Part I (2026 draft line numbers)

| Line | Entry |
| --- | --- |
| 3 | Self-employment tax from Schedule SE line 12 |
| 4 | Household employment taxes (Schedule H) |
| 5a | Additional Medicare Tax on self-employment income (Form 8959) |
| 5b | Additional Medicare Tax on Medicare wages (Form 8959) |
| 6a to 6d | Tax on unreported tips (Form 4137), uncollected tax on tips, on wages (Form 8919), on group-term life insurance |
| 7 | Total tax: lines 3, 5a and 6e |
| 8 | 2026 estimated payments and 2025 overpayment applied |
| 9 | Amount paid with Form 4868 |
| 10 | Additional child tax credit from Part II line 19 |
| 11a, 11b | Additional Medicare Tax withheld; excess social security tax withheld (more than one employer) |
| 12a to 12c | Total payments, less Schedule 3-A |
| 16 | Amount owed |

Source: [Form 1040-SS (2026) draft](https://www.irs.gov/pub/irs-dft/f1040ss--dft.pdf). Medicare wages and self-employment income are combined against the Additional Medicare Tax threshold; a self-employment loss is ignored. The Additional Medicare Tax is never part of the deductible half. [Publication 570, Additional Medicare Tax](https://www.irs.gov/pub/irs-pdf/p570.pdf).

### Step 6: additional child tax credit in Part II

Available to a bona fide resident of Puerto Rico for the whole year with one or more qualifying children (no longer three), if social security and Medicare taxes were withheld or self-employment tax was paid, the filer cannot be claimed as someone's dependent, and the filer (or one spouse on a joint return) has an SSN valid for employment issued by the due date including extensions. Modified AGI on line 3 includes excluded Puerto Rico income. The credit on line 19 is the smaller of the credit after the phase-out (line 11) and the employee and self-employment taxes paid (line 18: half of self-employment tax and half of Additional Medicare Tax on self-employment income, plus social security, Medicare and Additional Medicare Tax withheld on Form 499R-2/W-2PR and the Part I line 6 taxes, less Additional Medicare Tax withheld and excess social security tax). It does not use the 15% of earned income rule that applies on Schedule 8812. A bona fide resident who must file Form 1040 claims it on Schedule 8812 instead. The credit for other dependents cannot be taken on Form 1040-SS. [Form 1040-SS (2026) draft, Part II](https://www.irs.gov/pub/irs-dft/f1040ss--dft.pdf); [Instructions for Form 1040-SS (2025), Part II](https://www.irs.gov/pub/irs-pdf/i1040ss.pdf).

### Step 7: estimated tax

If self-employment tax (plus any Additional Medicare Tax) is expected to be USD 1,000 or more for 2026, figure estimated payments on Form 1040-ES and pay the IRS, by Direct Pay, EFTPS or card, or by check with the voucher to Internal Revenue Service, P.O. Box 1303, Charlotte, NC 28201-1303. Estimated payments to Hacienda do not count. [Publication 570, Estimated tax payments](https://www.irs.gov/pub/irs-pdf/p570.pdf). Due dates and safe harbours: `us-quarterly-estimated-tax`.

## Boundary and exception table

| Situation | Treatment |
| --- | --- |
| Net earnings under USD 400 | No self-employment tax; Form 1040-SS still filed for any of the step 2 items, including the additional child tax credit |
| Loss or low profit and the client wants social security credits | The optional methods on Schedule SE Part II may help (see `us-schedule-c-and-se-computation`) |
| Wages already at or above the 2026 wage base | Only the 2.9% Medicare part applies to self-employment earnings |
| Married, both self-employed | Two Schedules SE, each with its own wage base |
| Minister, member of a religious order, Christian Science practitioner | Self-employment tax on service income unless an approved Form 4361; Form 2031 elections cannot be revoked |
| Approved Form 4029 (religious sect) | Do not file Form 1040-SS for that income |
| Church employee income of USD 108.28 or more | Taxed on Schedule SE line 5a; skip lines 1a to 4b if it is the only income |
| United States citizen or Puerto Rico resident employed by a foreign government or international organization | Self-employment tax on that pay, reported on Schedule SE line 2 |
| Rental activity, partnership or entity income | Classify first; partnership shares follow the Schedule SE partnership rules |
| Person who is not a bona fide resident of Puerto Rico | Schedule SE with Form 1040; additional child tax credit on Schedule 8812 |
| Disaster declared in Puerto Rico | Check IRS disaster relief for postponed dates; do not assume one |
| Chapter 11 debtor | Profit goes on the estate's Form 1041, but the debtor still pays the self-employment tax |

### Defaults when a fact is missing

| Missing fact | Default, and flag it |
| --- | --- |
| Whether a Form 1040 is required | Run `pr-federal-residence-and-filing` step 8 first |
| Wage statements | Assume no wages (full base); ask for every Form 499R-2/W-2PR |
| Which spouse runs the business | Ask; do not split |
| Child's SSN issue date | No additional child tax credit until shown |
| Estimated payments made | Zero; ask for IRS account transcript |

### Red flags

| Flag | Why it matters |
| --- | --- |
| Client paid only Hacienda | IRS self-employment tax unpaid, with interest and penalties |
| Profit excluded from income tax and no Form 1040-SS on file | Unfiled federal return |
| Combined wages and self-employment income near USD 200,000 (single) | Additional Medicare Tax |
| Additional child tax credit claimed with no self-employment tax or withheld taxes | Line 18 limit makes the credit zero |
| Earlier credit denied | Form 8862 may be required |

## Worked cases

**Case 1, a decision: make estimated payments or not?** A single bona fide resident consultant, all work done in Puerto Rico, no wages and no income from outside Puerto Rico, expects 2026 Schedule C net profit of USD 50,000. Using the 2026 factors from `us-schedule-c-and-se-computation`: net earnings are USD 46,175; social security part USD 5,725.70; Medicare part USD 1,339.08; self-employment tax USD 7,064.78, on Form 1040-SS line 3. That is USD 1,000 or more, so she should pay estimated tax: four equal payments of USD 1,766.19 if she uses the current-year method. If her profit were only USD 5,000, self-employment tax would be USD 706.48, under USD 1,000: no estimated payments needed, pay with the return by 15 April 2027.

```oa-check
name: Puerto Rico consultant, estimated tax decision (2026)
inputs:
  profit: 50000
  small_profit: 5000
  factor: 0.9235
  ss_rate: 0.124
  medicare_rate: 0.029
  wage_base: 184500
  estimate_prompt: 1000
steps:
  - net_earnings: profit * factor
  - ss_part: min(net_earnings, wage_base) * ss_rate
  - medicare_part: net_earnings * medicare_rate
  - se_tax: round(ss_part + medicare_part, 2)
  - quarterly: round(se_tax / 4, 2)
  - small_se_tax: round(small_profit * factor * (ss_rate + medicare_rate), 2)
  - margin_over_prompt: se_tax - estimate_prompt
  - small_margin: small_se_tax - estimate_prompt
expected:
  net_earnings: 46175.00
  ss_part: 5725.70
  se_tax: 7064.78
  quarterly: 1766.19
  small_se_tax: 706.48
  margin_over_prompt: 6064.78
  small_margin: -293.52
```

**Case 2, wages plus a side business.** A single bona fide resident earns USD 170,000 of social security and Medicare wages on Form 499R-2/W-2PR from a Puerto Rico employer and has USD 50,000 of Schedule C net profit. Net earnings USD 46,175. Base left: USD 184,500 less USD 170,000, USD 14,500. Social security part: USD 14,500 at 12.4%, USD 1,798. Medicare part: USD 1,339.08. Self-employment tax USD 3,137.08 (line 3). Additional Medicare Tax: the USD 200,000 threshold less USD 170,000 of Medicare wages leaves USD 30,000; self-employment income above it is USD 16,175, at 0.9%, USD 145.58 (line 5a). Total tax on line 7: USD 3,282.66. No Form 1040 is needed because all income is Puerto Rico source.

```oa-check
name: Wages plus Schedule C, Form 1040-SS (2026)
inputs:
  wages: 170000
  profit: 50000
  factor: 0.9235
  wage_base: 184500
  threshold_single: 200000
steps:
  - net_earnings: profit * factor
  - base_left: max(wage_base - wages, 0)
  - ss_part: min(net_earnings, base_left) * 0.124
  - medicare_part: net_earnings * 0.029
  - line_3: round(ss_part + medicare_part, 2)
  - line_5a: round(max(net_earnings - max(threshold_single - wages, 0), 0) * 0.009, 2)
  - line_7: line_3 + line_5a
expected:
  base_left: 14500
  ss_part: 1798.00
  line_3: 3137.08
  line_5a: 145.58
  line_7: 3282.66
```

**Case 3, additional child tax credit on Part II.** A single parent, bona fide resident, two qualifying children under 17 with valid SSNs, USD 30,000 of Schedule C net profit and no other income (modified AGI USD 30,000, below USD 200,000). Self-employment tax is USD 4,238.87. Part II: line 2 is 2 times USD 1,700, USD 3,400; no phase-out, so line 11 is USD 3,400. Line 18 is half the self-employment tax, USD 2,119.44. The credit on line 19 is the smaller, USD 2,119.44. Amount owed on line 16: USD 2,119.43.

```oa-check
name: Additional child tax credit on Form 1040-SS Part II (2026)
inputs:
  profit: 30000
  children: 2
  actc_per_child: 1700
  ctc_per_child: 2200
steps:
  - se_tax: round(profit * 0.9235 * 0.153, 2)
  - line_2: children * actc_per_child
  - line_11: min(line_2, children * ctc_per_child)
  - line_18: round(se_tax / 2, 2)
  - line_19: min(line_11, line_18)
  - owed: se_tax - line_19
expected:
  se_tax: 4238.87
  line_2: 3400
  line_11: 3400
  line_18: 2119.44
  line_19: 2119.44
  owed: 2119.43
```

## When to refuse or refer

| Code | Situation | Action |
| --- | --- | --- |
| R-PRSE-RES | Bona fide residence is uncertain or the year is a move year | Use `pr-federal-residence-and-filing` first |
| R-PRSE-CLERGY | Minister, religious order or church employee income | Refer: Publication 517 rules |
| R-PRSE-PARTNER | Partnership or LLC with more than one member | Refer: `us-form-1065-partnership` and the Schedule SE partnership rules |
| R-PRSE-FARM | Farm income or the farm optional method | Refer: Schedule F and Publication 225 |
| R-PRSE-8862 | Credit previously denied or reduced | Refer: Form 8862 required unless an exception applies |
| R-PRSE-LOCAL | The question is Puerto Rico income tax or the Puerto Rico optional tax | Use `pr-individual-income-tax` |

## Filing and payment

- **Due:** Form 1040-SS for calendar 2026 by 15 April 2027 (fiscal year: 15th day of the 4th month after year end). E-filing is available.
- **Extension:** Form 4868 by 15 April 2027, on paper or by IRS e-file, gives until 15 October 2027 to file. It does not extend payment; interest runs from 15 April 2027 on any unpaid tax. The 2-month automatic extension is for residents of the other territories who are outside the United States and Puerto Rico, not for Puerto Rico residents.
- **Where:** with a payment, Internal Revenue Service, P.O. Box 1303, Charlotte, NC 28201-1303; without a payment, Department of the Treasury, Internal Revenue Service, Austin, TX 73301-0215. Form 4868 uses the same two addresses.
- **Pay:** electronically where possible (Direct Pay, debit or credit card, online account).
- Refunds that include the additional child tax credit are not issued before mid-February.

Source: [Instructions for Form 1040-SS (2025), When To File, Extension of Time To File, Where To File](https://www.irs.gov/pub/irs-pdf/i1040ss.pdf).

## Completion checklist

- Bona fide residence for all of 2026 confirmed, and Form 1040 requirement ruled out.
- A Schedule C per business, combined on one Schedule SE per spouse.
- Every Form 499R-2/W-2PR on Schedule SE line 8a.
- Schedule SE line 13 skipped on Form 1040-SS.
- Form 8959 run when wages plus self-employment income could pass the threshold.
- Part II run for each child with a valid SSN, with the line 18 limit applied.
- Estimated payments checked against the USD 1,000 prompt; IRS payments, not Hacienda payments, on line 8.
- Records kept: income and expense records, Schedule C inputs, all wage statements, each spouse's Schedule SE.

## Sources

| Source | URL | Read on |
| --- | --- | --- |
| Instructions for Form 1040-SS (2025). Read for purpose, who must file (USD 400, USD 108.28), exceptions, business owned by spouses, when to file, the Puerto Rico 6-month extension, where to file, Part I lines and Part II qualifying rules, and the USD 1,000 estimated tax reminder. | https://www.irs.gov/pub/irs-pdf/i1040ss.pdf | 2026-11-14 |
| Form 1040-SS (2026) early release draft, created 9/21/26, not for filing. Read for Part I lines 3 to 16 (5a and 5b split) and Part II lines 1 to 19 (USD 1,700, USD 2,200, USD 400,000 and USD 200,000, 5%). | https://www.irs.gov/pub/irs-dft/f1040ss--dft.pdf | 2026-11-14 |
| Schedule SE (Form 1040) 2026. Read for line 12 to Form 1040-SS Part I line 3. | https://www.irs.gov/pub/irs-pdf/f1040sse.pdf | 2026-11-14 |
| Instructions for Schedule SE (2026). Read for the territory reminder (Schedule SE filed with Form 1040-SS) and line 13 (skip on Form 1040-SS). | https://www.irs.gov/pub/irs-pdf/i1040sse.pdf | 2026-11-14 |
| IRS Publication 570 (2025). Read for chapter 3 Puerto Rico (self-employment tax, Additional Medicare Tax, estimated tax, additional child tax credit) and chapter 4 Self-Employment Tax and Additional Medicare Tax. | https://www.irs.gov/pub/irs-pdf/p570.pdf | 2026-11-14 |
| IRS Publication 1321 (October 2026). Read for the caution that half of self-employment tax on excluded income is not deductible. | https://www.irs.gov/pub/irs-pdf/p1321.pdf | 2026-11-14 |

Not yet confirmed: the 2026 Instructions for Form 1040-SS were not published on the read date, so the USD 108.28 church employee figure, the USD 1,000 estimated tax prompt, the filing addresses and the extension rules are from the 2025 instructions; the 2026 Form 1040-SS line numbers are from the early release draft and can change before release; the Puerto Rico income tax treatment of federal self-employment tax was not read.
