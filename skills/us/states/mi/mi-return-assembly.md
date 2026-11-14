---
name: mi-return-assembly
description: Put together the complete 2026 federal, Michigan and City of Detroit return package for a full-year Michigan resident individual, sole proprietor or single-member LLC owner. Sets the order in which the federal skills and the Michigan skills (mi-income-tax, mi-pension-retirement-subtraction, mi-homestead-credit, mi-detroit-individual-return, mi-estimated-tax) run, the pre-flight checks, the tie-outs between the federal Form 1040, the MI-1040 and Schedule 1, Form 4884, the MI-1040CR, the Detroit Form 5118 and the 2027 estimate plans, the status lines for Michigan sales tax and payroll, and what the reviewer receives. It computes no tax itself and restates no rate; every figure comes from the skill that owns it. Trigger on "assemble the Michigan return", "Michigan return package", "MI-1040 reviewer package", "Michigan and Detroit returns together", "Michigan return assembly".
version: "2.0"
jurisdiction: US-MI
tax_year: 2026
last_updated: 2026-11-14
category: orchestrator
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
tier: 2
domain: income-tax
type: router
---

# Michigan return assembly (federal, MI-1040 and Detroit), tax year 2026

> **Source-cited draft.** Built from the Michigan Treasury decoupling notice of 25 February 2026, the 2026 MI-1040ES and the 2025 City of Detroit Form 5118 instructions, read on 2026-11-14, and from the Michigan and federal skills it routes to, which own every rate and threshold. No accountant has reviewed it. All outputs must be reviewed by a qualified tax professional before filing.

**Answer first.** Run the federal skills first, then the Michigan ones in this order: `mi-income-tax`, `mi-pension-retirement-subtraction` (any retirement income, or a filer old enough for the Michigan standard deduction), `mi-homestead-credit` (if the household may qualify), `mi-detroit-individual-return` (if the client lives or works in Detroit), then `mi-estimated-tax` for the 2027 vouchers. Then tie out: federal AGI carries unchanged to the MI-1040 and to the Detroit return, and the two returns are independent of each other (neither tax feeds the other). In 2026 Michigan does **not** follow the federal 2025 law on bonus depreciation, section 179, research expensing or the business interest limit: a package with 2026 business assets and no Michigan Schedule 1 addition is wrong and goes back to `mi-income-tax`. This skill states no rate, exemption or threshold: each comes from its owning skill, listed below.

## Scope

In scope: a full-year Michigan resident individual or married couple filing jointly, with wages, Schedule C business income (sole proprietor or single-member LLC disregarded for federal tax), investment and retirement income, for tax year 2026, including a City of Detroit resident return, or a nonresident Detroit return for someone who works there, where it applies.

Out of scope: part-year residents and nonresidents of Michigan, couples with mixed residency, S corporations and partnerships, amended returns, multistate apportionment, foreign income at the state level, city returns other than Detroit, and the corporate income tax (see "When to refuse or refer").

How to run it: use the facts intake and the content skills captured and ask again only where something is missing or contradicts itself. Run the skills in order without pausing between them, then send one status message. A failed self-check is a reviewer flag, not a reason to stop, unless a refusal code below applies.

## Ask the client first

Intake normally has these; confirm only what is missing:

1. Michigan residence for all of 2026, for the taxpayer and any spouse, and whether either lived or worked in the City of Detroit (or another Michigan city with an income tax).
2. Filing status, dates of birth and dependents (the retirement route and the exemption count depend on them).
3. Business structure (sole proprietor or single-member LLC disregarded for federal tax) and every business asset placed in service in 2026, with the federal depreciation method used.
4. Whether the federal return claimed the qualified tips or qualified overtime deduction (federal Schedule 1-A).
5. Homeowner or renter, and the total household resources for the homestead credit.
6. Michigan and Detroit withholding (W-2 boxes 17 and 19, 1099-R) and every 2026 MI-1040ES and Detroit Form 5123 payment, with dates.

## The method, step by step

### Who owns each figure

This skill uses figures; it does not hold them. Take each from the owning skill's output for this client.

- `mi-income-tax`: Michigan rate, personal and special exemptions, Schedule 1 additions and subtractions, decoupling depreciation, tips and overtime subtraction, filing date and extension.
- `mi-pension-retirement-subtraction`: retirement and pension subtraction limits, the Michigan standard deduction by birth year, Form 4884.
- `mi-homestead-credit`: homestead property tax credit limits and household resources (MI-1040CR).
- `mi-detroit-individual-return`: Detroit resident and nonresident rates, Detroit exemption, credit for tax paid to another city, Detroit estimate threshold (Form 5123), Detroit due date.
- `mi-estimated-tax`: Michigan estimate threshold, the safe harbors and their AGI test, installment dates, MI-2210 penalty and interest.
- `mi-sales-tax`: Michigan sales and use tax rates and returns.
- `mi-payroll`: Michigan withholding tables and unemployment insurance.
- The federal skills in Step 2: federal AGI, Schedule C, self-employment tax, QBI, 1099-NEC threshold.

### Step 1: pre-flight checks

| Check | Question | If it fails |
| --- | --- | --- |
| PF-1 | Has the federal Form 1040 been completed by the federal skills? | R-MIA-01 |
| PF-2 | Full-year Michigan residency confirmed for both spouses? | R-MIA-06 |
| PF-3 | Business is a sole proprietorship or disregarded single-member LLC? | R-MIA-10 |
| PF-4 | Tax year 2026, original return? | R-MIA-12, R-MIA-09 |
| PF-5 | Dates of birth, filing status and dependents known? | R-MIA-05 |
| PF-6 | Detroit link: resident, worker, or none? | Resident: Detroit skill, Form 5118; nonresident worker: Detroit skill, Form 5119; none: skip |
| PF-7 | 2026 assets placed in service listed with their federal depreciation method? | Hold the MI-1040 until it is |
| PF-8 | Another Michigan city's income tax applies? | R-MIA-07 |

### Step 2: order of skills

1. Federal: `us-sole-prop-bookkeeping`, `us-schedule-c-and-se-computation`, `us-section-179-and-bonus-depreciation`, `us-qbi-deduction`, `us-self-employed-health-insurance`, `us-self-employed-retirement`, `us-quarterly-estimated-tax`, then `us-federal-return-assembly` for the Form 1040. `us-1099-nec-issuance` runs alongside.
2. `mi-income-tax`: MI-1040, Schedule 1 (including the 2025 PA 24 decoupling additions and the tips and overtime subtraction), Schedule W.
3. `mi-pension-retirement-subtraction`: Form 4884, or the Michigan standard deduction route.
4. `mi-homestead-credit`: MI-1040CR.
5. `mi-detroit-individual-return`: Form 5118 (or 5119), with Form 5121 for city withholding, and the Form 5123 plan for 2027.
6. `mi-estimated-tax`: the 2027 MI-1040ES schedule, and the MI-2210 check for 2026.
7. Status only, no entry on the MI-1040: `mi-sales-tax` (if the business sells taxable goods or holds a sales tax licence) and `mi-payroll` (if the client has employees).
8. This skill: tie out and package.

Each skill hands over its line figures, its checks, any refusal it triggered and its reviewer flags.

### Step 3: tie-outs (tolerance $1)

**Federal to Michigan**

| Check | Equation | Owner |
| --- | --- | --- |
| C-1 | MI-1040 filing status = Form 1040 filing status | `mi-income-tax` |
| C-2 | MI-1040 federal AGI = Form 1040 line 11 | `mi-income-tax` |
| C-3 | MI exemption count = taxpayer (and spouse) + dependents, plus any special exemptions; amount = count times the exemption in `mi-income-tax` | `mi-income-tax` |
| C-4 | Federal bonus depreciation, section 179 and research expensing on 2026 assets: Schedule 1 addition = federal deduction minus the Michigan deduction under the pre-2025 rules | `mi-income-tax` |
| C-5 | Federal qualified tips and overtime deduction on Schedule 1-A = Michigan subtraction | `mi-income-tax` |
| C-6 | Taxable Social Security (Form 1040 line 6b) subtracted in full | `mi-income-tax` |
| C-7 | U.S. government interest subtracted; other states' municipal interest added | `mi-income-tax` |
| C-8 | The federal QBI deduction does not appear on the MI-1040 (it is below AGI) | `mi-income-tax` |
| C-9 | Business interest limit recomputed under the pre-2025 section 163(j) where the business has interest expense | `mi-income-tax` |

**Michigan internal**

| Check | Equation | Owner |
| --- | --- | --- |
| M-1 | Michigan taxable income = AGI + additions - subtractions - exemptions | `mi-income-tax` |
| M-2 | Michigan tax = taxable income times the rate in `mi-income-tax` | `mi-income-tax` |
| M-3 | Form 4884 or standard deduction result = the Schedule 1 retirement line | `mi-pension-retirement-subtraction` |
| M-4 | MI-1040CR credit = the MI-1040 property tax credit line | `mi-homestead-credit` |
| M-5 | Schedule W total = W-2 box 17 + 1099-R Michigan withholding | `mi-income-tax` |
| M-6 | Balance or refund = tax - credits - withholding - estimates paid | `mi-income-tax` |

**Michigan to Detroit**

| Check | Equation | Owner |
| --- | --- | --- |
| D-1 | Detroit filing status consistent with the MI-1040 | `mi-detroit-individual-return` |
| D-2 | Detroit income = federal AGI + Detroit additions - Detroit subtractions (pensions, Social Security, unemployment) | `mi-detroit-individual-return` |
| D-3 | Detroit exemption count = the MI-1040 personal and dependent count (plus age 65 and disability exemptions); amount = count times the Detroit exemption | `mi-detroit-individual-return` |
| D-4 | Detroit tax = Detroit taxable income times the Detroit rate for the filer's status | `mi-detroit-individual-return` |
| D-5 | Detroit withholding claimed = Form 5121 line 5 = W-2 box 19 Detroit amounts (W-2s alone are not accepted) | `mi-detroit-individual-return` |
| D-6 | Detroit estimates claimed = 2026 Form 5123 payments plus any credit carried forward | `mi-detroit-individual-return` |

**Estimates, contractors and status lines**

| Check | Equation | Owner |
| --- | --- | --- |
| E-1 | 2026 MI-1040ES payments reported = payments shown in Treasury eServices | `mi-estimated-tax` |
| E-2 | 2027 MI-1040ES schedule meets one of the safe harbors in `mi-estimated-tax`, or the MI-2210 result is carried to the MI-1040 | `mi-estimated-tax` |
| E-3 | 1099-NEC forms issued for every contractor paid at or above the federal threshold | `us-1099-nec-issuance` |
| S-1 | Sales tax: every return due while the licence is open is filed; nothing from it enters the MI-1040 except use tax the skill routes there | `mi-sales-tax` |
| S-2 | Payroll: withholding returns and the annual reconciliation filed; unemployment insurance reports filed | `mi-payroll` |

### Step 4: the package

1. **Workbook:** one sheet per form (Form 1040 and schedules, MI-1040 and Schedule 1, Schedule W, Form 4884, MI-1040CR, Form 5118 or 5119 with 5121, the 2027 MI-1040ES and Form 5123 schedules) and one tie-out sheet with each check, its two sides and its result.
2. **Reviewer brief:** summary of each return; positions taken (for example the retirement route chosen, Detroit allocation days, the decoupling depreciation schedule); every reviewer flag and refusal; open questions; status of sales tax and payroll.
3. **Client action list:** what to sign; amounts and due dates (the dates as given in the Filing and payment section of each owning skill); how to pay (Treasury eServices, or a check to "State of Michigan").

If context runs short, finish the figures and tie-outs first, then the brief, and say which files are partial.

## Boundary and exception table

| Situation | Treatment |
| --- | --- |
| No Detroit link | Skip `mi-detroit-individual-return`; say so in the brief |
| Works in Detroit, lives elsewhere in Michigan | Nonresident Form 5119 through `mi-detroit-individual-return`; the MI-1040 is unchanged |
| No retirement income and no filer old enough for the Michigan standard deduction | Skip `mi-pension-retirement-subtraction` |
| Household resources clearly above the homestead credit limit | Skip `mi-homestead-credit`; note the reason |
| 2026 business assets with federal bonus depreciation or section 179 | C-4 must show an addition; a nil addition is a hold |
| Federal Schedule 1-A tips or overtime deduction claimed | C-5 must show the same subtraction on Michigan |
| Federal QBI deduction present | Not on the MI-1040 (C-8) |
| Sales tax licence open, no taxable sales | Status line; nil returns still due under `mi-sales-tax` |

### Defaults when a fact is missing

| Missing fact | Default |
| --- | --- |
| Detroit residence or work days | No Detroit return until confirmed; flag it |
| Asset placed-in-service detail | Hold the MI-1040 (PF-7) |
| Estimate payment dates | Use Treasury eServices records; flag any difference (E-1) |
| Form 5121 detail | Claim no Detroit withholding until it is complete |

### Red flags

| Flag | Why |
| --- | --- |
| Detroit tax lower than expected with large wages | Allocation days or home-working claims to check in `mi-detroit-individual-return` |
| Michigan taxable income equal to federal AGI with 2026 assets | Decoupling addition missed |
| Withholding on Schedule W differs from the W-2s | Missing or duplicated statement |
| Estimates paid but no MI-2210 check | `mi-estimated-tax` did not run |

## Worked cases

**Case 1, a full-year Detroit resident sole proprietor: tie out the two returns.** Federal AGI of $80,000 (all Schedule C), single, no dependents, no Michigan adjustments. `mi-income-tax` returns a Michigan tax of $3,149.25 and `mi-detroit-individual-return` a Detroit tax of $1,905.60. The MI-1040 and Form 5118 both start from $80,000, so C-2 and D-2 tie with no difference. Estimates paid: Michigan $3,000, Detroit $1,800; no withholding. Balances due with the returns: Michigan $149.25, Detroit $105.60. Neither figure feeds the other.

```oa-check
name: MI 2026 assembly, Detroit resident sole proprietor, tie-outs and two balances
inputs:
  form_1040_agi: 80000
  mi_1040_agi: 80000
  detroit_start_income: 80000
  mi_tax: 3149.25
  detroit_tax: 1905.60
  mi_estimates: 3000
  detroit_estimates: 1800
steps:
  - c2_difference: abs(form_1040_agi - mi_1040_agi)
  - d2_difference: abs(form_1040_agi - detroit_start_income)
  - mi_balance: mi_tax - mi_estimates
  - detroit_balance: detroit_tax - detroit_estimates
expected:
  c2_difference: 0
  d2_difference: 0
  mi_balance: 149.25
  detroit_balance: 105.60
```

**Case 2, a decision: release or hold the package (check C-4).** The same client bought $10,000 of equipment in 2026 and took 100% bonus depreciation federally. `mi-income-tax` computes Michigan depreciation of $3,600 on that asset under the pre-2025 rules. The package's Schedule 1 shows no addition. Required addition: $10,000 - $3,600 = $6,400; the package is $6,400 short, $6,399 beyond the $1 tolerance, so the decision is hold and send it back to `mi-income-tax`, which recomputes the tax. Once Schedule 1 carries $6,400 the shortfall is nil and the package can be released.

```oa-check
name: MI 2026 assembly, decoupling add-back, hold against release
inputs:
  federal_depreciation: 10000
  michigan_depreciation: 3600
  addition_in_package: 0
  addition_after_fix: 6400
  tolerance: 1
steps:
  - required_addition: federal_depreciation - michigan_depreciation
  - shortfall_before: required_addition - addition_in_package
  - excess_over_tolerance: max(0, shortfall_before - tolerance)
  - shortfall_after_fix: required_addition - addition_after_fix
expected:
  required_addition: 6400
  shortfall_before: 6400
  excess_over_tolerance: 6399
  shortfall_after_fix: 0
```

## When to refuse or refer

| Code | Situation | Action |
| --- | --- | --- |
| R-MIA-01 | A skill in the order did not run | Refuse; name it |
| R-MIA-02 | A skill's own check failed and was not resolved | Refuse; name the check |
| R-MIA-03 | A tie-out fails by more than $1 | Refuse; name the equation and the difference |
| R-MIA-04 | An upstream refusal was dropped from its output | Refuse; resolve it first |
| R-MIA-05 | Intake incomplete (residency, dates of birth, filing status) | Refuse; list what is missing |
| R-MIA-06 | Part-year or nonresident of Michigan | Refuse |
| R-MIA-07 | City return other than Detroit | Refuse; refer |
| R-MIA-08 | Couple with mixed residency | Refuse |
| R-MIA-09 | Amended return | Refuse |
| R-MIA-10 | S corporation or partnership | Refuse; see `mi-corporate-income-tax` for the flow-through entity tax pointer |
| R-MIA-11 | Multistate apportionment beyond the reciprocity states | Refuse |
| R-MIA-12 | A tax year other than 2026 | Refuse |
| R-MIA-13 | Foreign income or foreign tax credits at the state level | Refuse |
| R-MIA-14 | Corporate income tax asked here | Route to `mi-corporate-income-tax` |

## Filing and payment

| Return | When and how |
| --- | --- |
| Federal Form 1040 | As in `us-federal-return-assembly` |
| MI-1040 with Schedule 1, Schedule W, Form 4884 and MI-1040CR as needed | Due date and extension rule as in `mi-income-tax`; e-file through Treasury eServices or approved software, or paper |
| Detroit Form 5118 or 5119 with Form 5121 | Due date as in `mi-detroit-individual-return`; Michigan Treasury administers it |
| 2027 MI-1040ES and Form 5123 vouchers | Dates and amounts as in `mi-estimated-tax` and `mi-detroit-individual-return` |
| Sales tax and payroll returns | Their own cycle, under `mi-sales-tax` and `mi-payroll` |

The reviewer files, not the agent. Payment is the client's act: Treasury eServices (direct debit or card) or a check payable to "State of Michigan", with the voucher for that payment.

## Completion checklist

- Every skill in Step 2 ran, or its absence is explained in the brief.
- Pre-flight checks PF-1 to PF-8 passed.
- Every tie-out (C, M, D, E, S) passed within $1, or the refusal is recorded.
- No rate, exemption or threshold was typed into the package; each came from its owning skill.
- Decoupling additions present for every 2026 asset with federal bonus or section 179.
- Detroit return included or its absence explained; Form 5121 attached for any city withholding.
- 2027 estimate plans for Michigan and Detroit included.
- Sales tax and payroll status lines included.
- Client action list dated from the owning skills.

## Sources

| Source | URL | Read on |
| --- | --- | --- |
| Treasury notice: Decoupling Michigan income taxes from certain IRC provisions (25 February 2026). Read for the PA 24 rule that individual income tax uses section 168(k) and 163(j) as in effect on 31 December 2024, and the addition equal to the federal less the pre-OB3 deduction, behind checks C-4 and C-9. | https://www.michigan.gov/treasury/reference/taxpayer-notices/2026/02/25/decoupling-michigan-income-taxes-from-certain-internal-revenue-code-provisions | 2026-11-14 |
| 2026 MI-1040ES. Read for the e-payment route through michigan.gov/iit and the check made payable to "State of Michigan". | https://www.michigan.gov/taxes/-/media/Project/Websites/taxes/Forms/IIT/TY2025/MI-1040ES-(2026).pdf | 2026-11-14 |
| 2025 City of Detroit Form 5118 instructions. Read for Form 5121 line 5 as the only accepted withholding evidence ("W-2 forms are no longer accepted"), Form 5123 payments on line 18 and Form 5338. | https://www.michigan.gov/taxes/-/media/Project/Websites/taxes/Forms/City-IIT/TY2025/5118-Instr.pdf | 2026-11-14 |

Not yet confirmed: the 2026 MI-1040, Schedule 1 and Detroit form line numbers (not published), so the checks are written by item, except Form 1040 lines and Form 5121 line 5; Treasury's decoupling notice covers tax year 2025 and says guidance for later years is forthcoming, so checks C-4 and C-9 follow `mi-income-tax` for 2026.
