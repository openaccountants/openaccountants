---
name: mi-income-tax
description: Compute a full-year Michigan resident's 2026 Form MI-1040 income tax. Michigan starts from federal adjusted gross income, applies Schedule 1 additions and subtractions, deducts $5,900 per personal exemption and taxes the result at a flat 4.25% (Treasury notice of 15 April 2026, MCL 206.51). Covers sole proprietors and single-member LLCs, wage earners, the new 2026 Michigan deductions for federally claimed qualified tips and qualified overtime, the 2025 PA 24 decoupling from the federal bonus depreciation, section 179, section 174 and section 163(j) changes, the reciprocity states and the credit routing. Trigger on "Michigan income tax", "MI-1040", "Michigan Schedule 1", "Michigan personal exemption", "Michigan Treasury", "MCL 206.51". Retirement income goes to mi-pension-retirement-subtraction, city tax to mi-detroit-individual-return.
version: "1.0"
jurisdiction: US-MI
tax_year: 2026
last_updated: 2026-11-13
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
tier: 2
domain: income-tax
type: computation
---

# Michigan individual income tax (Form MI-1040), tax year 2026

> **Source-cited draft.** Built from the Michigan Treasury notice "4.25% Income Tax Rate for Individuals and Fiduciaries in 2026 Tax Year" (15 April 2026), the 2026 Michigan Income Tax Withholding Guide (Form 446), the Treasury notice on decoupling from the Internal Revenue Code (25 February 2026), the September 2026 Treasury Update on tips and overtime, the Tax Year 2025 guidance page and the 2025 Schedule 1 instructions, read on 2026-11-13. No accountant has reviewed it. All outputs must be reviewed by a qualified tax professional before filing.

**Answer first.** For 2026 Michigan tax is **4.25%** of Michigan taxable income: federal AGI, plus Schedule 1 additions, minus Schedule 1 subtractions, minus **$5,900** for each personal and dependency exemption. There are no brackets. Michigan has no standard deduction for people under 67. From 2026 a Michigan resident can also subtract the federal qualified tips and qualified overtime deductions claimed on the 2026 federal return. Michigan does not follow the federal 2025 law on bonus depreciation, section 179, research expenses or the business interest limit: those differences are added back. The return is due 15 April 2027.

## Scope and who this is for

In scope: a full-year Michigan resident (or married couple) filing Form MI-1040 for tax year 2026, with wages, Schedule C business profit, rental, interest, dividends and capital gains, and the Schedule 1 adjustments most such clients meet.

Out of scope, and where it goes:

| Topic | Skill |
| --- | --- |
| Pension, IRA and annuity subtraction, the age-67 Michigan standard deduction, Social Security for seniors (Form 4884) | `mi-pension-retirement-subtraction` |
| Homestead property tax credit (MI-1040CR) | `mi-homestead-credit` |
| Paying during the year (MI-1040ES) and the underpayment penalty (MI-2210) | `mi-estimated-tax` |
| City of Detroit income tax (Forms 5118, 5119, 5120) | `mi-detroit-individual-return` |
| Putting the federal, Michigan and city returns together | `mi-return-assembly` |
| Employer withholding and unemployment insurance | `mi-payroll` |
| Corporate income tax | `mi-corporate-income-tax` |
| Federal AGI, Schedule C and self-employment tax | `us-schedule-c-and-se-computation` and the federal skills |

## Ask the client first

1. **Michigan resident for all of 2026?** Domicile decides it: the place of the permanent home. Part-year and nonresident returns use Schedule NR and are refused here.
2. **Filing status and the number of exemptions** (the client, spouse, dependents), and whether anyone is deaf, blind, hemiplegic, paraplegic, quadriplegic or totally and permanently disabled, or a qualified disabled veteran (special exemptions).
3. **Birth year of the client and spouse.** If either has retirement income, or is 67 or older, load `mi-pension-retirement-subtraction`.
4. **Did the 2026 federal return claim the qualified tips or qualified overtime deduction?** Amounts from federal Schedule 1-A.
5. **Business assets placed in service in 2026:** did the federal return use 100% bonus depreciation, section 179 above the pre-2025 limit, immediate research expensing, or the new section 163(j) computation? Each needs a Michigan adjustment.
6. **U.S. government bond interest, and interest on bonds of other states**, and any city income tax deducted federally.
7. **Michigan withholding** (W-2 box 17, 1099-R) and **2026 MI-1040ES payments**.
8. **Does the client live or work in a city with an income tax** (for example Detroit)? That is a separate city return.

## The method, step by step

### Rates, bands and thresholds

| Item | Amount, 2026 | Source |
| --- | --- | --- |
| Individual income tax rate (flat) | 4.25% | [Treasury notice, 15 April 2026](https://www.michigan.gov/treasury/reference/taxpayer-notices/2026/04/15/425-income-tax-rate-for-individuals-and-fiduciaries-in-2026-tax-year) |
| Personal exemption, per person and per dependent | $5,900 | [2026 Michigan Income Tax Withholding Guide (Form 446)](https://www.michigan.gov/taxes/-/media/Project/Websites/taxes/Forms/SUW/TY2026/446_Withholding-Guide_2026.pdf) |
| Personal exemption, 2025 (for prior-year comparisons) | $5,800 | [Tax Year 2025 Information](https://www.michigan.gov/taxes/iit/tax-guidance/tax-year-info/tax-year-2025-guidance) |
| Special exemption (deaf, blind, hemiplegic, paraplegic, quadriplegic, totally and permanently disabled), 2025-2026 filing cycle | $3,400 | [Tax Year 2025 Information](https://www.michigan.gov/taxes/iit/tax-guidance/tax-year-info/tax-year-2025-guidance) |
| Qualified disabled veteran deduction, 2025-2026 filing cycle | $500 | [Tax Year 2025 Information](https://www.michigan.gov/taxes/iit/tax-guidance/tax-year-info/tax-year-2025-guidance) |
| Exemption for each certificate of stillbirth | equal to the personal exemption ($5,800 for 2025) | [Tax Year 2025 Information](https://www.michigan.gov/taxes/iit/tax-guidance/tax-year-info/tax-year-2025-guidance) |
| Senior interest, dividend and capital gain deduction limit, 2025-2026 filing cycle (single / joint) | $14,688 / $29,376 | [Tax Year 2025 Information](https://www.michigan.gov/taxes/iit/tax-guidance/tax-year-info/tax-year-2025-guidance) |
| Section 179 limit for the Michigan computation (pre-2025 federal law, before inflation indexing) | $1,250,000, reduced above $3,130,000 of property | [Treasury decoupling notice, 25 February 2026](https://www.michigan.gov/treasury/reference/taxpayer-notices/2026/02/25/decoupling-michigan-income-taxes-from-certain-internal-revenue-code-provisions) |
| Michigan 529 contribution subtraction cap (single / joint), 2025-2026 filing cycle | $10,000 / $20,000 | [2025 Schedule 1 instructions, line 17](https://www.michigan.gov/taxes/-/media/Project/Websites/taxes/Forms/IIT/TY2025/Schedule-1-Instr.pdf) |
| Estimated payments required if tax due on the return is expected to exceed | $500 | [2026 MI-1040ES](https://www.michigan.gov/taxes/-/media/Project/Websites/taxes/Forms/IIT/TY2025/MI-1040ES-(2026).pdf) |

The rate can only fall: MCL 206.51(1)(c) cuts it when general fund revenue growth beats inflation. Treasury found that general fund revenue fell 1.56% in fiscal 2025 while inflation was 2.70%, so the rate for 2026 stays at 4.25%. The personal exemption is indexed each year.

### From federal AGI to Michigan tax

1. **Federal AGI.** Form 1040 line 11. Schedule C profit, the deductible half of self-employment tax, self-employed health insurance and retirement plan deductions all reach Michigan through AGI; there is no separate Michigan business schedule. The federal qualified business income deduction is below AGI and has no Michigan effect.
2. **Schedule 1 additions** (2025 line numbers; the 2026 form is not out yet):
   - Line 1: interest and dividends from bonds of other states and their cities (non-Michigan municipal bonds).
   - Line 2: city income tax and other taxes on or measured by income deducted in arriving at AGI.
   - Line 3 and line 5: Michigan capital gain and loss adjustments (MI-1040D, MI-4797) where the federal and Michigan basis differ.
   - Line 4: losses from business or property outside Michigan that are allocated to another state (with MI-1040H).
   - Line 7: a federal net operating loss deduction (Michigan uses its own NOL on MI-1045).
   - Line 8, other additions, including the **2025 PA 24 decoupling adjustments**: (a) bonus depreciation: Michigan uses section 168(k) as in effect on 31 December 2024, so the excess of the federal depreciation over the pre-2025-law depreciation is added back; (b) section 179: Michigan uses the pre-2025 limit in the table above, indexed; (c) section 174 and 174A: domestic research expenses are amortized over five years for Michigan, the excess deduction is added back and then subtracted ratably over the next four years; (d) section 163(j): the business interest limit is recomputed without adding depreciation and amortization to adjusted taxable income; (e) section 168(n) qualified production property: Michigan computes depreciation as if 168(n) did not exist. Source: [Treasury decoupling notice](https://www.michigan.gov/treasury/reference/taxpayer-notices/2026/02/25/decoupling-michigan-income-taxes-from-certain-internal-revenue-code-provisions). Keep a Michigan depreciation schedule for every affected asset: the later-year subtractions depend on it.
3. **Schedule 1 subtractions:**
   - Line 10: interest on U.S. government obligations included in AGI.
   - Line 11: military retirement and railroad retirement benefits included in AGI.
   - Line 14: compensation for active duty in the U.S. Armed Forces.
   - Line 15: Renaissance Zone deduction (zone residents and businesses).
   - Line 16: Michigan state and city income tax refunds included in AGI.
   - Line 17: contributions to Michigan 529 plans (MESP, MAP), net of qualified withdrawals, up to the cap.
   - Social Security benefits included in AGI are subtracted in full.
   - Retirement and pension benefits: Form 4884, see `mi-pension-retirement-subtraction`.
   - **New for 2026: qualified tips and qualified overtime.** For tax years beginning after 31 December 2025 and before 1 January 2029, Michigan taxable income is reduced by the federal deduction for qualified tips (IRC 224) and qualified overtime compensation (IRC 225) claimed on the federal return for the same year, to the extent not already deducted in arriving at AGI. The federal deductions are taken below AGI, so in practice the full federal amount is subtracted. A 2025 federal deduction cannot be used on a Michigan return. Source: [Treasury Update, September 2026](https://www.michigan.gov/treasury/-/media/Project/Websites/treasury/Newsletters/Treasury-Update-Newsletter_Sept2026.pdf). The 2026 Schedule 1 line for it is not published yet.
   - Source for the line list: [2025 Schedule 1 instructions](https://www.michigan.gov/taxes/-/media/Project/Websites/taxes/Forms/IIT/TY2025/Schedule-1-Instr.pdf).
4. **Exemptions.** Number of exemptions times $5,900, plus special exemptions and the qualified disabled veteran deduction.
5. **Michigan taxable income** = federal AGI + additions - subtractions - exemptions (not below zero).
6. **Tax** = taxable income times 4.25%.
7. **Credits.** Nonrefundable: income tax paid to another state on the same income (for a resident), and the other MI-1040 credits. Refundable: the homestead property tax credit (`mi-homestead-credit`), the home heating credit (MI-1040CR-7) and the Michigan earned income tax credit. Then subtract withholding and estimated payments.

### Reciprocity states

Michigan has reciprocal agreements with **Illinois, Indiana, Kentucky, Minnesota, Ohio and Wisconsin**. A Michigan resident working in one of them pays income tax on those wages to Michigan only; the employer there does not withhold its state's tax (it may register to withhold Michigan tax). A resident of those states working in Michigan files a Certificate of Nonresidency with the employer. Source: [2026 Withholding Guide, "Reciprocal Agreements"](https://www.michigan.gov/taxes/-/media/Project/Websites/taxes/Forms/SUW/TY2026/446_Withholding-Guide_2026.pdf). Wages earned in any other state are taxed by both, and Michigan gives the resident a credit for the other state's tax.

### Michigan cities

Michigan cities may levy their own income tax under the City Income Tax Act. Detroit's resident rate is 2.4% and nonresident rate 1.2%: see `mi-detroit-individual-return`. A city return is separate from the MI-1040; nothing on the MI-1040 depends on it except the Schedule 1 add-back of any city tax deducted federally.

## Boundary and exception table

| Situation | Treatment |
| --- | --- |
| Federal 100% bonus depreciation on 2026 assets | Add back the excess over pre-2025-law depreciation; deduct the Michigan depreciation in later years |
| Federal section 179 above $1,250,000 (as indexed) | Add back the excess; track a Michigan carryover |
| Domestic research expenses deducted in full federally | Add back; subtract over the next four years |
| Federal qualified tips or overtime deduction claimed for 2026 | Subtract the same amount on Michigan |
| The same deduction claimed for 2025 | Not allowed on the 2025 or any Michigan return |
| Interest on Michigan municipal bonds | No adjustment (exempt federally and in Michigan) |
| Interest on another state's bonds | Add back (Schedule 1 line 1) |
| Social Security in AGI | Subtract in full |
| Wages from a reciprocity state | Taxed only by Michigan |
| Wages from a non-reciprocity state | Taxed in both; credit for the other state's tax |
| Client with pension or IRA income, or age 67+ | Route to `mi-pension-retirement-subtraction` before finishing |

### Defaults when a fact is missing

| Missing fact | Default, and flag it |
| --- | --- |
| Number of exemptions | Use the federal count of the taxpayer, spouse and dependents; ask |
| Whether federal tips or overtime deductions were claimed | None; ask for federal Schedule 1-A |
| Asset placed-in-service detail | No decoupling adjustment until the fixed asset register is seen; flag before filing |
| Birth years | Ask before any retirement subtraction |
| City of residence | Ask: Detroit residents and workers file a city return |

### Red flags to raise with the client

| Flag | Why it matters |
| --- | --- |
| Federal depreciation, section 179 or research expensing on 2026 assets | Michigan add-back and a separate Michigan depreciation schedule |
| A W-2 with Michigan wages but a reciprocity-state home address | Withholding may be wrong |
| Expected balance due over $500 and no estimates | MI-2210 penalty and interest |
| Tips or overtime on the W-2 but no federal deduction claimed | Michigan follows the federal claim only |

### Common income patterns

| Pattern | Michigan treatment |
| --- | --- |
| W-2 wages from a Michigan employer | In AGI; Michigan withholding claimed on Schedule W |
| W-2 wages from a reciprocity state | In AGI; Michigan only; ask the employer to withhold Michigan tax |
| Schedule C net profit, 1099-NEC income | In AGI; estimates likely needed |
| Rental income (Schedule E) | In AGI; Michigan property income is Michigan source |
| Capital gains | In AGI at the flat rate |
| U.S. Treasury interest | Subtract |
| Other states' municipal bond interest | Add back |
| Social Security | Subtract |

## Worked cases

**Case 1, single sole proprietor with one dependent.** Federal AGI $85,000. Interest of $500 from Ohio municipal bonds (add back). U.S. Treasury interest of $1,000 (subtract). Two exemptions: $11,800. Michigan taxable income $85,000 + $500 - $1,000 - $11,800 = $72,700. Tax at 4.25%: $3,089.75.

```oa-check
name: MI 2026 single, one dependent, Schedule 1 adjustments
inputs:
  federal_agi: 85000
  other_state_muni_interest: 500
  us_government_interest: 1000
  exemptions: 2
  exemption_amount: 5900
  rate: 0.0425
steps:
  - taxable_income: max(federal_agi + other_state_muni_interest - us_government_interest - exemptions * exemption_amount, 0)
  - tax: taxable_income * rate
expected:
  taxable_income: 72700
  tax: 3089.75
```

**Case 2, a decision: does the 2026 federal tips and overtime deduction help on Michigan?** A married couple filing jointly with two children has federal AGI of $95,000. On the 2026 federal return they deducted $12,000 of qualified tips and $3,000 of qualified overtime below AGI. Four exemptions: $23,600. Without the new subtraction Michigan taxable income would be $71,400 and the tax $3,034.50. With it, taxable income is $95,000 - $23,600 - $12,000 - $3,000 = $56,400 and the tax $2,397.00: $637.50 less. Claim it, and keep federal Schedule 1-A with the file: Michigan allows only what the federal return claimed for the same year.

```oa-check
name: MI 2026 joint, tips and overtime subtraction
inputs:
  federal_agi: 95000
  exemptions: 4
  exemption_amount: 5900
  federal_tips_deduction: 12000
  federal_overtime_deduction: 3000
  rate: 0.0425
steps:
  - tax_without: max(federal_agi - exemptions * exemption_amount, 0) * rate
  - taxable_with: max(federal_agi - exemptions * exemption_amount - federal_tips_deduction - federal_overtime_deduction, 0)
  - tax_with: taxable_with * rate
  - saving: tax_without - tax_with
expected:
  tax_without: 3034.50
  taxable_with: 56400
  tax_with: 2397.00
  saving: 637.50
```

## When to refuse or refer

| Code | Situation | Action |
| --- | --- | --- |
| MI-R-01 | Part-year or nonresident (Schedule NR) | Refuse: allocation of income is outside this skill |
| MI-R-02 | Corporate income tax or the flow-through entity tax | Refer to `mi-corporate-income-tax` |
| MI-R-03 | City income tax | Use `mi-detroit-individual-return` for Detroit; refuse other cities |
| MI-R-04 | Business income apportioned between Michigan and other states (MI-1040H) | Refuse: refer for multistate review |
| MI-R-05 | Amended returns | Refer |
| MI-R-06 | A tax year other than 2026 | Refuse: the exemption and other figures change each year |
| MI-R-07 | Michigan Business Tax carryforwards or certificated credits | Refuse: a separate regime |
| MI-R-08 | Decoupling adjustments for assets held in a flow-through entity, without the entity's statement | Refer: the entity must report each member's share |
| MI-R-09 | Michigan net operating loss (MI-1045) | Refer |
| MI-R-10 | Domicile unclear (homes in two states) | Refer: Form 3799 domicile review |

## Filing and payment

File Form MI-1040 with Schedule 1 (and Schedule W for withholding) by **15 April 2027** through Michigan Treasury eServices (free file) or approved software, or on paper. A federal extension extends the Michigan filing date; it does not extend payment, so pay the expected balance by 15 April 2027. During 2026, estimated payments are due 15 April, 15 June and 15 September 2026 and 15 January 2027 (see `mi-estimated-tax`). Source for the payment dates: [2026 MI-1040ES](https://www.michigan.gov/taxes/-/media/Project/Websites/taxes/Forms/IIT/TY2025/MI-1040ES-(2026).pdf).

### Form map

| Form | What it covers |
| --- | --- |
| MI-1040 | The return |
| Schedule 1 | Additions and subtractions |
| Schedule W | Withholding |
| Schedule NR | Part-year and nonresident (out of scope) |
| Form 4884 | Pension schedule (`mi-pension-retirement-subtraction`) |
| MI-1040CR | Homestead property tax credit (`mi-homestead-credit`) |
| MI-1040CR-7 | Home heating credit |
| MI-1040ES | Estimated payments (`mi-estimated-tax`) |

## Completion checklist

- Residency confirmed as full-year Michigan.
- Exemptions counted at $5,900 each, plus special exemptions.
- Every Schedule 1 addition considered, including the decoupling items for 2026 assets.
- Tips and overtime subtraction matches the federal 2026 claim.
- Retirement, Social Security and senior items routed to `mi-pension-retirement-subtraction`.
- Homestead credit tested (`mi-homestead-credit`).
- City return need checked.
- Withholding on Schedule W agrees with W-2 box 17 and 1099-R.

## Sources

| Source | URL | Read on |
| --- | --- | --- |
| Treasury notice: 4.25% income tax rate for individuals and fiduciaries in 2026 tax year (15 April 2026). Read for the 2026 rate and the fiscal 2025 revenue test (-1.56% against 2.70% inflation). | https://www.michigan.gov/treasury/reference/taxpayer-notices/2026/04/15/425-income-tax-rate-for-individuals-and-fiduciaries-in-2026-tax-year | 2026-11-13 |
| 2026 Michigan Income Tax Withholding Guide (Form 446). Read for the 4.25% rate, the $5,900 personal exemption and the reciprocity states. | https://www.michigan.gov/taxes/-/media/Project/Websites/taxes/Forms/SUW/TY2026/446_Withholding-Guide_2026.pdf | 2026-11-13 |
| Treasury: Tax Year 2025 Information. Read for the 2025 exemption ($5,800), special exemption ($3,400), disabled veteran deduction ($500), stillbirth exemption and senior interest limits. | https://www.michigan.gov/taxes/iit/tax-guidance/tax-year-info/tax-year-2025-guidance | 2026-11-13 |
| Treasury notice: Decoupling Michigan income taxes from certain IRC provisions (25 February 2026). Read for the 163(j), 168(k), 168(n), 174 and 179 adjustments under 2025 PA 24 and the pre-2025 section 179 limits. | https://www.michigan.gov/treasury/reference/taxpayer-notices/2026/02/25/decoupling-michigan-income-taxes-from-certain-internal-revenue-code-provisions | 2026-11-13 |
| Treasury Update newsletter, September 2026. Read for the 2026 to 2028 Michigan deductions for federal qualified tips and qualified overtime. | https://www.michigan.gov/treasury/-/media/Project/Websites/treasury/Newsletters/Treasury-Update-Newsletter_Sept2026.pdf | 2026-11-13 |
| 2025 Michigan Schedule 1 instructions. Read for the addition and subtraction line list and the 529 cap. | https://www.michigan.gov/taxes/-/media/Project/Websites/taxes/Forms/IIT/TY2025/Schedule-1-Instr.pdf | 2026-11-13 |
| 2026 MI-1040ES. Read for the $500 estimate threshold and the four 2026 due dates. | https://www.michigan.gov/taxes/-/media/Project/Websites/taxes/Forms/IIT/TY2025/MI-1040ES-(2026).pdf | 2026-11-13 |

Not yet confirmed: the 2026 MI-1040 and Schedule 1 forms and instructions were not published when read, so 2025 line numbers are used and the line for the tips and overtime subtraction is not given; the 2026 special exemption, disabled veteran deduction, senior interest limits and 529 cap (2025 figures shown, "2025-2026 filing cycle"); the Michigan earned income tax credit percentage (the old file said 30% of the federal credit; not re-read); the extension rule (taken from the old file, not re-read); MCL 206.30 and 206.51 themselves (legislature.mi.gov returned errors, so the statute text was read only as quoted by Treasury).
