---
name: mi-return-assembly
description: Put together the complete 2026 federal, Michigan and City of Detroit return package for a full-year Michigan resident individual, sole proprietor or single-member LLC owner. Sets the order in which the federal and Michigan skills run, the pre-flight checks, the reconciliations between the federal Form 1040, the MI-1040 (4.25%, $5,900 exemptions), Form 4884, the MI-1040CR, the MI-1040ES vouchers for 2027 and the Detroit Form 5118, and what the reviewer receives. It does not compute tax itself. Trigger on "assemble the Michigan return", "Michigan return package", "MI-1040 reviewer package", "Michigan and Detroit returns together", "Michigan return assembly".
version: "1.0"
jurisdiction: US-MI
tax_year: 2026
last_updated: 2026-11-13
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
tier: 2
domain: income-tax
type: router
---

# Michigan return assembly (federal, MI-1040 and Detroit), tax year 2026

> **Source-cited draft.** Built from the Michigan Treasury 2026 rate notice, the 2026 Michigan Income Tax Withholding Guide, the Treasury decoupling notice of 25 February 2026, the 2026 MI-1040ES and the 2025 Detroit Form 5118 instructions, read on 2026-11-13, and from the Michigan skills it routes to. No accountant has reviewed it. All outputs must be reviewed by a qualified tax professional before filing.

**Answer first.** Run the federal skills first, then the Michigan ones in this order: `mi-income-tax`, `mi-pension-retirement-subtraction` (if any retirement income or age 67+), `mi-homestead-credit` (if the household may qualify), `mi-detroit-individual-return` (if the client lives or works in Detroit), then `mi-estimated-tax` for the 2027 vouchers. Then reconcile: federal AGI carries unchanged to the MI-1040; Michigan tax is 4.25% of taxable income after $5,900 per exemption; the Detroit return starts from federal AGI too but is independent of the MI-1040. In 2026 Michigan does **not** follow federal bonus depreciation, section 179 above the old limit or immediate research expensing: a package that shows no Michigan add-back for 2026 assets is wrong.

## Scope and who this is for

In scope: a full-year Michigan resident individual or married couple filing jointly, with wages, Schedule C business income (sole proprietor or single-member LLC disregarded for federal tax), investment and retirement income, for tax year 2026, including a Detroit resident return where it applies.

Out of scope: part-year residents and nonresidents, couples with mixed residency, S corporations and partnerships, amended returns, multistate apportionment, foreign income at the state level, city returns other than Detroit, and the corporate income tax (see refusals).

## The method, step by step

### Rates, bands and thresholds

| Item | Amount, 2026 | Source |
| --- | --- | --- |
| Michigan rate | 4.25% | [Treasury notice, 15 April 2026](https://www.michigan.gov/treasury/reference/taxpayer-notices/2026/04/15/425-income-tax-rate-for-individuals-and-fiduciaries-in-2026-tax-year) |
| Michigan personal exemption | $5,900 | [2026 Withholding Guide](https://www.michigan.gov/taxes/-/media/Project/Websites/taxes/Forms/SUW/TY2026/446_Withholding-Guide_2026.pdf) |
| Michigan estimate threshold | more than $500 owed | [2026 MI-1040ES](https://www.michigan.gov/taxes/-/media/Project/Websites/taxes/Forms/IIT/TY2025/MI-1040ES-(2026).pdf) |
| Detroit resident rate | 2.4% | [City of Detroit Income Tax Information](https://detroitmi.gov/departments/office-chief-financial-officer/ocfo-divisions/office-treasury/income-tax/income-tax-information) |
| Detroit exemption | $600 | [City of Detroit Income Tax Information](https://detroitmi.gov/departments/office-chief-financial-officer/ocfo-divisions/office-treasury/income-tax/income-tax-information) |
| Detroit estimate threshold | more than $100 owed | [2025 Form 5118 instructions](https://www.michigan.gov/taxes/-/media/Project/Websites/taxes/Forms/City-IIT/TY2025/5118-Instr.pdf) |

The figures belong to the skills named below; they are repeated here only for the reconciliations.

### Step 1: pre-flight checks

| Check | Question | If it fails |
| --- | --- | --- |
| PF-1 | Has the federal Form 1040 been completed by the federal skills? | R-MIA-01 |
| PF-2 | Full-year Michigan residency confirmed for both spouses? | R-MIA-06 |
| PF-3 | Business is a sole proprietorship or disregarded single-member LLC? | R-MIA-10 |
| PF-4 | Tax year 2026, original return? | R-MIA-12 |
| PF-5 | Dates of birth, filing status and dependents known? | R-MIA-05 |
| PF-6 | Detroit link: resident, worker, or none? | Detroit resident: run Detroit skill; nonresident worker: Detroit skill Form 5119 |
| PF-7 | 2026 assets placed in service listed with their federal depreciation method? | Hold the MI-1040 until it is |

### Step 2: order of skills

1. Federal: bookkeeping, `us-schedule-c-and-se-computation`, the QBI, health insurance and retirement plan skills, `us-quarterly-estimated-tax`, the federal return assembly.
2. `mi-income-tax`: MI-1040, Schedule 1 (including the 2025 PA 24 decoupling add-backs and the new tips and overtime subtraction), Schedule W.
3. `mi-pension-retirement-subtraction`: Form 4884 or the age-67 standard deduction.
4. `mi-homestead-credit`: MI-1040CR.
5. `mi-detroit-individual-return`: Form 5118 (or 5119, 5120) with Form 5121.
6. `mi-estimated-tax`: the 2027 MI-1040ES schedule, and the Detroit Form 5123 schedule.
7. This skill: reconcile and package.

Each skill hands over its line figures, its checks, any refusal it triggered and its reviewer flags.

### Step 3: reconciliations (tolerance $1)

**Federal to Michigan**

| Check | Equation |
| --- | --- |
| C-1 | MI-1040 filing status = Form 1040 filing status |
| C-2 | MI-1040 federal AGI = Form 1040 line 11 |
| C-3 | MI exemptions = taxpayer (and spouse) + dependents, times $5,900, plus special exemptions |
| C-4 | Federal bonus depreciation, section 179 and research expensing on 2026 assets: Schedule 1 addition = federal deduction minus the Michigan (pre-2025-law) deduction |
| C-5 | Federal qualified tips and overtime deduction on Schedule 1-A = Michigan subtraction |
| C-6 | Taxable Social Security (Form 1040 line 6b) subtracted in full |
| C-7 | U.S. government interest subtracted; other states' municipal interest added |
| C-8 | The federal QBI deduction does not appear on the MI-1040 |

**Michigan internal**

| Check | Equation |
| --- | --- |
| M-1 | Michigan taxable income = AGI + additions - subtractions - exemptions |
| M-2 | Michigan tax = taxable income times 4.25% |
| M-3 | Form 4884 or standard deduction result = the Schedule 1 retirement line |
| M-4 | MI-1040CR credit = the MI-1040 property tax credit line |
| M-5 | Schedule W total = W-2 box 17 + 1099-R Michigan withholding |
| M-6 | Balance or refund = tax - credits - withholding - estimates paid |

**Michigan to Detroit**

| Check | Equation |
| --- | --- |
| D-1 | Detroit filing status consistent with the MI-1040 |
| D-2 | Detroit income = federal AGI + Detroit additions - Detroit subtractions (pensions, Social Security, unemployment) |
| D-3 | Detroit exemptions = number of exemptions times $600 (plus age 65 and disability exemptions) |
| D-4 | Detroit tax = Detroit taxable income times 2.4% |
| D-5 | Form 5121 withholding = W-2 box 19 Detroit amounts |

**Estimates and contractors**

| Check | Equation |
| --- | --- |
| E-1 | 2026 MI-1040ES payments reported = payments shown in Treasury eServices |
| E-2 | 2027 MI-1040ES schedule meets 100% (110% if 2026 AGI over $150,000) of the 2026 tax or 90% of the expected 2027 tax |
| E-3 | 1099-NEC forms issued for every contractor paid at or above the 2026 federal threshold (see `us-1099-nec-issuance`) |

### Step 4: the package

1. **Workbook:** one sheet per form (Form 1040 and schedules, MI-1040 and Schedule 1, Form 4884, MI-1040CR, Form 5118 and 5121, MI-1040ES and Form 5123 schedules) and one reconciliation sheet with each check and its result.
2. **Reviewer brief:** summary of each return; positions taken (for example the retirement route chosen, Detroit allocation days); every reviewer flag and refusal; open questions.
3. **Client action list:** what to sign; amounts and due dates (returns and balances by 15 April 2027; 2027 Michigan estimates on 15 April, 15 June and 15 September 2027 and 15 January 2028, once confirmed on the 2027 MI-1040ES); how to pay (Treasury eServices; checks to "State of Michigan").

## Worked cases

**Case 1, a full-year Detroit resident sole proprietor: reconcile the two returns.** Federal AGI $80,000 (all Schedule C), single, no dependents, no Michigan adjustments. Michigan: ($80,000 - $5,900) x 4.25% = $3,149.25. Detroit: ($80,000 - $600) x 2.4% = $1,905.60. Estimates paid: Michigan $3,000, Detroit $1,800. Balances due with the returns: Michigan $149.25, Detroit $105.60. Both returns start from the same AGI but use different exemptions and rates; neither figure feeds the other.

```oa-check
name: MI 2026 assembly, Detroit resident sole proprietor, two balances
inputs:
  federal_agi: 80000
  mi_exemption: 5900
  mi_rate: 0.0425
  detroit_exemption: 600
  detroit_rate: 0.024
  mi_estimates: 3000
  detroit_estimates: 1800
steps:
  - mi_tax: (federal_agi - mi_exemption) * mi_rate
  - detroit_tax: (federal_agi - detroit_exemption) * detroit_rate
  - mi_balance: mi_tax - mi_estimates
  - detroit_balance: detroit_tax - detroit_estimates
expected:
  mi_tax: 3149.25
  detroit_tax: 1905.60
  mi_balance: 149.25
  detroit_balance: 105.60
```

**Case 2, check C-4 catches a missing add-back.** The same client bought $10,000 of equipment in 2026 and took 100% bonus depreciation federally. The bookkeeping file shows Michigan depreciation of $3,000 on that asset under pre-2025 law. The package's Schedule 1 shows no addition. C-4 requires an addition of $10,000 - $3,000 = $7,000, which raises Michigan tax by $297.50. Send it back to `mi-income-tax` before release.

```oa-check
name: MI 2026 assembly, decoupling add-back check
inputs:
  federal_depreciation: 10000
  michigan_depreciation: 3000
  addition_in_package: 0
  rate: 0.0425
steps:
  - required_addition: federal_depreciation - michigan_depreciation
  - shortfall: required_addition - addition_in_package
  - extra_tax: shortfall * rate
expected:
  required_addition: 7000
  shortfall: 7000
  extra_tax: 297.50
```

## When to refuse or refer

| Code | Situation | Action |
| --- | --- | --- |
| R-MIA-01 | A skill in the order did not run | Refuse; name it |
| R-MIA-02 | A skill's own check failed and was not resolved | Refuse; name the check |
| R-MIA-03 | A reconciliation fails by more than $1 | Refuse; name the equation and the difference |
| R-MIA-04 | An upstream refusal was dropped from its output | Refuse; resolve it first |
| R-MIA-05 | Intake incomplete (residency, dates of birth, filing status) | Refuse; list what is missing |
| R-MIA-06 | Part-year or nonresident | Refuse |
| R-MIA-07 | City return other than Detroit | Refuse; refer |
| R-MIA-08 | Couple with mixed residency | Refuse |
| R-MIA-09 | Amended return | Refuse |
| R-MIA-10 | S corporation or partnership | Refuse; see `mi-corporate-income-tax` for the flow-through entity tax |
| R-MIA-11 | Multistate apportionment beyond the reciprocity states | Refuse |
| R-MIA-12 | A tax year other than 2026 | Refuse |
| R-MIA-13 | Foreign income or foreign tax credits at the state level | Refuse |

## Filing and payment

The federal return, the MI-1040 (with MI-1040CR and Form 4884 as needed) and the Detroit return are each due 15 April 2027 for calendar 2026 (the Detroit date is to be confirmed on the 2026 Detroit instructions). File the Michigan and Detroit returns through Michigan Treasury e-file partners or Treasury eServices; the reviewer files, not the agent. Payment is the client's act; the package gives the instructions.

## Sources

| Source | URL | Read on |
| --- | --- | --- |
| Treasury notice: 4.25% rate for 2026. Read for the rate. | https://www.michigan.gov/treasury/reference/taxpayer-notices/2026/04/15/425-income-tax-rate-for-individuals-and-fiduciaries-in-2026-tax-year | 2026-11-13 |
| 2026 Michigan Income Tax Withholding Guide. Read for the $5,900 exemption. | https://www.michigan.gov/taxes/-/media/Project/Websites/taxes/Forms/SUW/TY2026/446_Withholding-Guide_2026.pdf | 2026-11-13 |
| Treasury notice: Decoupling Michigan income taxes from certain IRC provisions. Read for the depreciation add-back behind check C-4. | https://www.michigan.gov/treasury/reference/taxpayer-notices/2026/02/25/decoupling-michigan-income-taxes-from-certain-internal-revenue-code-provisions | 2026-11-13 |
| 2026 MI-1040ES. Read for the $500 threshold and the 100% / 110% / 90% rules. | https://www.michigan.gov/taxes/-/media/Project/Websites/taxes/Forms/IIT/TY2025/MI-1040ES-(2026).pdf | 2026-11-13 |
| City of Detroit Income Tax Information. Read for 2.4% and $600. | https://detroitmi.gov/departments/office-chief-financial-officer/ocfo-divisions/office-treasury/income-tax/income-tax-information | 2026-11-13 |
| 2025 Detroit Form 5118 instructions. Read for the $100 estimate threshold and Form 5121. | https://www.michigan.gov/taxes/-/media/Project/Websites/taxes/Forms/City-IIT/TY2025/5118-Instr.pdf | 2026-11-13 |

Not yet confirmed: 2026 MI-1040 and Detroit form line numbers (not published), so the checks are written by item, not by line; the 2027 MI-1040ES due dates; the Detroit due date for 2026.
