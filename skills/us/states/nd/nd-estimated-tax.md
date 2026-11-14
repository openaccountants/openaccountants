---
name: nd-estimated-tax
description: Work out whether a North Dakota individual must pay 2026 estimated income tax on Form ND-1ES, how much to pay on each of the four due dates, and the 12% a year interest on Schedule ND-1UT when an installment is short or late. For full-year residents who are sole proprietors, single-member LLC owners, S corporation shareholders or employees with too little withholding, plus the nonresident and part-year worksheet lines. Built from the 2026 Form ND-1ES, the 2025 Schedule ND-1UT, N.D.C.C. 57-38-45, 57-38-62 and 57-38-63 and N.D. Admin. Code 81-03-04. Trigger on ND-1ES, North Dakota estimated tax, ND quarterly payments, ND-1UT, underpayment interest North Dakota, ND safe harbor.
version: "1.2"
jurisdiction: US-ND
tax_year: 2026
last_updated: 2026-11-14
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
tier: 2
domain: income-tax
type: computation
---

# North Dakota individual estimated income tax, tax year 2026

> **Source-cited draft.** Built from the 2026 Form ND-1ES (SFN 28709, 12-2025), the 2025 Schedule ND-1UT (SFN 28704, 12-2025), the 2025 individual income tax booklet, N.D.C.C. chapter 57-38 and N.D. Admin. Code chapter 81-03-04, read on 2026-11-14. No accountant has reviewed it. All outputs must be reviewed by a qualified tax professional before filing or payment.

**Answer first.** A North Dakota individual must pay 2026 estimated tax only if all four tests on the 2026 Form ND-1ES are met: the person must pay federal estimated tax for 2026, their 2025 North Dakota net tax liability was USD 1,000 or more, they expect to owe USD 1,000 or more for 2026 after withholding, and their withholding will be less than the smaller of 90% of the 2026 net tax liability or 100% of the 2025 net tax liability. There is no 110% high-income step-up as there is federally. A quarter of the required amount is due on 15 April, 15 June and 15 September 2026 and 15 January 2027. Short or late installments carry interest at 12% a year to the earlier of the payment date or the return due date (generally 15 April 2027). The 2026 tax itself comes from the 2026 rate schedules owned by `nd-income-tax`.

## Scope and who this is for

In scope: individual estimated income tax for tax year 2026 under N.D.C.C. 57-38-62 and 57-38-63: the four-test requirement, the required annual payment, the installment amounts and dates, fiscal-year dates, the farmer option, the part-year and nonresident worksheet lines, applying a 2025 overpayment, paying, and the Schedule ND-1UT interest computation and its waivers.

Out of scope, and where it goes:

| Topic | Skill |
| --- | --- |
| The 2026 North Dakota tax rate schedules, additions, subtractions and credits that produce the 2026 tax | `nd-income-tax` |
| Federal estimated tax (Form 1040-ES, Form 2210 and its annualization factors) | `us-quarterly-estimated-tax` |
| Corporation estimated tax (Form 40-ES, the USD 5,000 tests) | `nd-corporate-tax` |
| Putting the ND-1 return package together | `nd-return-assembly` |
| Employer withholding | `nd-payroll` |
| Nonresident sourcing, reciprocity and the credit for tax paid to another state | `nd-cross-border-tax` |

## Ask the client first

1. **The 2025 North Dakota return:** was one required, and what is the net tax liability on the 2025 Form ND-1, line 25 (or Form ND-EZ, line 2)? Did the client move into North Dakota during 2025 with no North Dakota income before the move?
2. **Expected 2026 federal taxable income** and any North Dakota additions, subtractions and credits (these feed `nd-income-tax`), and whether the client must pay federal estimated tax for 2026.
3. **Expected 2026 North Dakota withholding** (Form W-2 and Form 1099 amounts shown for North Dakota).
4. **Filing status in 2025 and 2026**, especially a change between joint and separate returns.
5. **Farming:** does more than two-thirds of gross income come from farming, and does the client qualify as a farmer for federal estimated tax?
6. **Timing of income:** is it even through the year, or lumpy enough that the federal annualized income installment method will be used? Is the client a nonresident or new resident whose North Dakota income starts after 15 April 2026?

## The method, step by step

### Rates, bands and thresholds

| Item | Amount, tax year 2026 | Official source |
| --- | --- | --- |
| Estimated tax not required if the prior-year (2025) net tax liability was below this | USD 1,000 | [N.D.C.C. 57-38-62(1)](https://ndlegis.gov/cencode/t57c38.pdf); [2026 Form ND-1ES, condition 2 and worksheet line 12](https://www.tax.nd.gov/sites/www/files/documents/forms/software-developer/individual-income-forms/28709-form-nd-1es-2026%20final.pdf) |
| Estimated tax not required if the expected 2026 balance after withholding is below this | USD 1,000 | [2026 Form ND-1ES, condition 3 and worksheet line 10](https://www.tax.nd.gov/sites/www/files/documents/forms/software-developer/individual-income-forms/28709-form-nd-1es-2026%20final.pdf) |
| Current-year test: share of 2026 net tax liability | 90% | [N.D.C.C. 57-38-62(1)(a)](https://ndlegis.gov/cencode/t57c38.pdf); [2026 Form ND-1ES, line 11](https://www.tax.nd.gov/sites/www/files/documents/forms/software-developer/individual-income-forms/28709-form-nd-1es-2026%20final.pdf) |
| Current-year test for a qualified farmer | 66 2/3% (.6667 on the worksheet) | [2026 Form ND-1ES, condition 4(a) and line 11](https://www.tax.nd.gov/sites/www/files/documents/forms/software-developer/individual-income-forms/28709-form-nd-1es-2026%20final.pdf) |
| Prior-year test: share of 2025 net tax liability (flat, no high-income step-up) | 100% | [N.D.C.C. 57-38-62(1)(b)](https://ndlegis.gov/cencode/t57c38.pdf); same form, line 12 |
| Share of the minimum annual payment due on each due date | 25% (one-fourth) | [N.D.C.C. 57-38-63](https://ndlegis.gov/cencode/t57c38.pdf); [2026 Form ND-1ES, "Payment amounts and due dates"](https://www.tax.nd.gov/sites/www/files/documents/forms/software-developer/individual-income-forms/28709-form-nd-1es-2026%20final.pdf) |
| Calendar-year due dates | 15 April 2026, 15 June 2026, 15 September 2026, 15 January 2027 | same form, page 1 and voucher record |
| Interest on an underpaid or late installment | 12% per year | [2026 Form ND-1ES, "Underpayment or late payment interest"](https://www.tax.nd.gov/sites/www/files/documents/forms/software-developer/individual-income-forms/28709-form-nd-1es-2026%20final.pdf); [N.D.C.C. 57-38-62(3) and 57-38-45(1)](https://ndlegis.gov/cencode/t57c38.pdf) |
| No interest at all if the estimated tax is below this per return | USD 1,000 ("less than one thousand dollars per income tax return filed") (in words on the page) | [N.D.C.C. 57-38-62(3)](https://ndlegis.gov/cencode/t57c38.pdf) |
| Interest waived if current-year liability exceeds withholding by less than this per return and no estimates were paid | USD 500 | [N.D. Admin. Code 81-03-04-02(3)(d)](https://ndlegis.gov/prod/acdata/pdf/81-03-04.pdf) |
| Farmer waiver: share of gross income from farming that must be exceeded | two-thirds | [N.D. Admin. Code 81-03-04-02(3)(a) and (b)](https://ndlegis.gov/prod/acdata/pdf/81-03-04.pdf) |
| Schedule ND-1UT interest that must be paid with the return when there is no overpayment or tax due (2025 form, 2025-2026 filing cycle) | USD 5.00 or more | [2025 Schedule ND-1UT, line 17 instructions](https://www.tax.nd.gov/sites/www/files/documents/forms/individual/2025-iit/28704-schedule-nd-1ut-2025.pdf) |
| Short tax year with no estimated payment due | fewer than 120 days | [N.D.C.C. 57-38-63](https://ndlegis.gov/cencode/t57c38.pdf) |

### Step 1: definitions that decide the tests

- **Net tax liability** is the income tax for the year as shown on the return less allowable credits, but not less tax withheld or estimated tax paid ([N.D.C.C. 57-38-62(5)](https://ndlegis.gov/cencode/t57c38.pdf)). On the 2025 return it is Form ND-1, line 25. Withholding is not subtracted to get it; withholding is compared with it.
- **Estimated tax** is the expected tax for the year less credits, including tax withheld ([N.D.C.C. 57-38-62(4)](https://ndlegis.gov/cencode/t57c38.pdf)).
- An amended return filed by the due date, including extensions, is the return for the year; a later audit assessment does not change the estimated-tax computation ([N.D. Admin. Code 81-03-04-02(2)](https://ndlegis.gov/prod/acdata/pdf/81-03-04.pdf)).

### Step 2: run the four tests (2026 Form ND-1ES, page 1)

1. Is the client required to pay federal estimated tax for 2026 (under IRC 6654)? This applies whether or not they actually pay it. If not, stop: no North Dakota estimated tax. Married people filing a joint federal return are each treated as subject to the federal rule ([N.D.C.C. 57-38-62(1)](https://ndlegis.gov/cencode/t57c38.pdf)). The federal test belongs to `us-quarterly-estimated-tax`.
2. Was the 2025 North Dakota net tax liability USD 1,000 or more? If no 2025 North Dakota return was required, the 2025 liability is zero, so no estimates are required.
3. Does the client expect to owe USD 1,000 or more for 2026 after subtracting North Dakota withholding?
4. Will 2026 North Dakota withholding be less than the smaller of 90% of the 2026 net tax liability (66 2/3% for a qualified farmer) and 100% of the 2025 net tax liability?

All four must be yes.

### Step 3: the 2026 worksheet (Form ND-1ES, page 2)

| Line | What goes on it |
| --- | --- |
| 1 | Estimated 2026 federal taxable income (from the 2026 Form 1040-ES worksheet) |
| 2 | Addition adjustments (2025 Form ND-1 instructions, lines 2 to 3) |
| 3 | Line 1 plus line 2 |
| 4 | Subtraction adjustments (2025 Form ND-1 instructions, lines 5 to 16) |
| 5 | North Dakota taxable income (line 3 less line 4) |
| 6 | North Dakota tax: full-year residents use the 2026 tax rate schedule (owned by `nd-income-tax`); nonresidents and part-year residents complete lines 15 to 19 |
| 7 | Credits (2025 Form ND-1 instructions, lines 21 to 23) |
| 8 | Net tax liability (line 6 less line 7) |
| 9 | Estimated 2026 North Dakota withholding |
| 10 | Line 8 less line 9. If below USD 1,000, stop: no estimated tax |
| 11 | Line 8 times 90% (or 66 2/3% for a qualified farmer) |
| 12 | 2025 net tax liability from the 2025 Form ND-1, line 25 (0 if no 2025 return was required). If below USD 1,000, stop |
| 13 | Smaller of line 11 and line 12; but use line 11 if the client moved into North Dakota during 2025 with no North Dakota income before the move. If line 9 is equal to or more than line 13, stop |
| 14 | Minimum annual payment: line 13 less line 9. Divide by 4 for each installment |
| 15 | Nonresident or part-year: tax on line 5 using the 2026 rate schedule |
| 16 | Portion of estimated federal adjusted gross income reportable to North Dakota (reduced by line 4) |
| 17 | Estimated federal adjusted gross income (reduced by US obligation interest) |
| 18 | North Dakota income ratio: line 16 divided by line 17, rounded to two decimal places; 1.00 if line 16 is more than line 17 |
| 19 | Line 15 times line 18; this goes on line 6 |

Source for every row: [2026 Form ND-1ES, page 2](https://www.tax.nd.gov/sites/www/files/documents/forms/software-developer/individual-income-forms/28709-form-nd-1es-2026%20final.pdf). The worksheet does not take into account three-year farm income averaging on Schedule ND-1FA.

### Step 4: married couples whose filing status changes

- Filing separate North Dakota returns for 2026: each spouse makes separate estimated payments based on their own income and completes their own ND-1ES ([2026 Form ND-1ES](https://www.tax.nd.gov/sites/www/files/documents/forms/software-developer/individual-income-forms/28709-form-nd-1es-2026%20final.pdf)).
- Joint 2025, separate 2026: for the prior-year test each spouse uses the net tax liability that would have been computed for 2025 on separate returns ([N.D.C.C. 57-38-62(1)(b)(2)](https://ndlegis.gov/cencode/t57c38.pdf)).
- Separate 2025, joint 2026: the prior-year test uses the sum of the two separate 2025 net tax liabilities; joint payments must reach 100% of that sum ([N.D.C.C. 57-38-62(1)(b)(3)](https://ndlegis.gov/cencode/t57c38.pdf); [N.D. Admin. Code 81-03-04-02(4)](https://ndlegis.gov/prod/acdata/pdf/81-03-04.pdf)).

### Step 5: due dates and the exceptions to four equal payments

- Calendar year: 15 April, 15 June, 15 September 2026 and 15 January 2027. A date on a Saturday, Sunday or legal holiday moves to the next business day ([2026 Form ND-1ES](https://www.tax.nd.gov/sites/www/files/documents/forms/software-developer/individual-income-forms/28709-form-nd-1es-2026%20final.pdf)).
- Fiscal year: the 15th day of the 4th, 6th and 9th months of the tax year and the 15th day of the 1st month of the next tax year ([N.D.C.C. 57-38-63](https://ndlegis.gov/cencode/t57c38.pdf)).
- Short tax year: if it ends before a remaining due date, the final payment is due on the 15th day of the last month of the short year; a tax year shorter than 120 days needs no estimated payment ([N.D.C.C. 57-38-63](https://ndlegis.gov/cencode/t57c38.pdf)).
- Farmer: a person who qualifies as a farmer for federal estimated tax for 2026 may follow the general rules or pay the whole estimated tax by 15 January 2027; the return is still due by the regular due date, generally 15 April 2027 ([2026 Form ND-1ES](https://www.tax.nd.gov/sites/www/files/documents/forms/software-developer/individual-income-forms/28709-form-nd-1es-2026%20final.pdf)).
- Full-year nonresident or new resident with no North Dakota income until after 15 April 2026: pay the required estimated tax in equal payments over the remaining due dates after the North Dakota income starts (same form).

### Step 6: applying a 2025 overpayment

A 2025 overpayment can be applied as a 2026 estimated payment (2025 Form ND-1, line 30). If the client does not name the installment, it is applied to the first installment ([N.D.C.C. 57-38-62(6)](https://ndlegis.gov/cencode/t57c38.pdf)); a statement attached to the 2025 return can apply it to another quarter ([2026 Form ND-1ES, payment record note 2](https://www.tax.nd.gov/sites/www/files/documents/forms/software-developer/individual-income-forms/28709-form-nd-1es-2026%20final.pdf)). Once made, the election cannot be changed after the return is filed ([2025 booklet, line 30](https://www.tax.nd.gov/sites/www/files/documents/forms/individual/2025-iit/2025-individual-income-tax-booklet.pdf)). An amount designated as an estimated payment may not be used by the Commissioner, or at the client's request, to offset another North Dakota liability, though before crediting an overpayment the Commissioner may offset unpaid child support and other debts named in the Admin. Code ([N.D. Admin. Code 81-03-04-03](https://ndlegis.gov/prod/acdata/pdf/81-03-04.pdf)).

### Step 7: pay

- Online: go to tax.nd.gov and select "Make A Payment" (electronic check, debit or credit card). Do not use the paper vouchers when paying electronically ([2026 Form ND-1ES](https://www.tax.nd.gov/sites/www/files/documents/forms/software-developer/individual-income-forms/28709-form-nd-1es-2026%20final.pdf)).
- Check or money order: payable to "ND State Tax Commissioner", with the last four digits of the social security number and "2026 ND-1ES" written on it, mailed with that installment's voucher to Office of State Tax Commissioner, PO Box 5622, Bismarck, ND 58506-5622. The check must be drawn on a US or Canadian bank, in US dollars, with a standard 9-digit routing number (same form).
- Keep the payment record on page 3 of the form (date paid, check number, amount, overpayment applied).

### Step 8: interest on Schedule ND-1UT (2025 form, 2025-2026 filing cycle; the 2026 schedule is not yet published)

Complete Schedule ND-1UT only if the client was required to pay federal estimated tax for the year. On the 2025 schedule ([SFN 28704](https://www.tax.nd.gov/sites/www/files/documents/forms/individual/2025-iit/28704-schedule-nd-1ut-2025.pdf)):

1. Line 1: net tax liability (Form ND-1, line 25). Line 2: 90% of line 1 (66 2/3% for a qualified farmer). Line 3: withholding (Form ND-1, line 26). Line 4: line 1 less line 3; below USD 1,000 means no estimates were required, so do not file the schedule.
2. Line 5: prior-year net tax liability; below USD 1,000 means no estimates were required. Line 6: required payment, the smaller of line 2 and line 5 (line 2 if the client moved into North Dakota during the prior year).
3. Line 7: 25% of line 6 in each quarter, unless a Part 1 exception applies. Line 8: estimated tax paid and tax withheld for each quarter; unless the client shows otherwise, one-fourth of the year's withholding is treated as withheld by each due date.
4. Lines 9 to 15: carry overpayments forward and compute the underpayment for each quarter. A payment is applied first to its own quarter, then to the earliest earlier underpayment.
5. Line 16: interest runs from the due date to the earlier of the payment date or the regular return due date. Days divided by 365, rounded to three decimals; times 12%, rounded to three decimals; times the underpayment.
6. Line 17: total interest goes to Form ND-1, line 37. An overpayment on the return is reduced by it; a tax due includes it.

Part 1 exceptions on the 2025 schedule: A, qualified farmer (whole required payment in the 4th quarter column); B, federal annualized income installment method (attach the federal Form 2210 worksheet and compute annualized North Dakota taxable income with North Dakota adjustments); C, federal 4th quarter exception (the client filed the federal return and paid the remaining federal tax by the date on the schedule, so the 4th column is zero); D, partial year (a nonresident or new resident whose North Dakota income started after 15 April: the required payment is spread over the remaining quarters).

## Boundary and exception table

| Situation | Rule | Source |
| --- | --- | --- |
| Liability exceeds withholding by less than USD 500 and no estimates paid | Interest must be waived (per return) | [N.D. Admin. Code 81-03-04-02(3)(d)](https://ndlegis.gov/prod/acdata/pdf/81-03-04.pdf) |
| Estimated tax below USD 1,000 per return | No interest is due (in words on the page) | [N.D.C.C. 57-38-62(3)](https://ndlegis.gov/cencode/t57c38.pdf) |
| Farmer (over two-thirds of gross income from farming) files the federal return by 1 March and pays the federal tax in full by then, with no state estimates | Interest must be waived; the state return need not be filed or paid by 1 March | [N.D. Admin. Code 81-03-04-02(3)(a)](https://ndlegis.gov/prod/acdata/pdf/81-03-04.pdf) |
| Farmer makes the single federal installment on 15 January, files federally after 1 March, and pays the state estimate due on 15 January | Interest must be waived; the April, June and September state payments are not required | [N.D. Admin. Code 81-03-04-02(3)(b)](https://ndlegis.gov/prod/acdata/pdf/81-03-04.pdf) |
| Client uses the federal annualized income installment method and pays the state estimates based on it | Interest must be waived | [N.D. Admin. Code 81-03-04-02(3)(c)](https://ndlegis.gov/prod/acdata/pdf/81-03-04.pdf) |
| Illness, casualty or other good cause | The Commissioner may waive all or part of any civil penalty or interest for good cause shown | [N.D.C.C. 57-38-45(5)](https://ndlegis.gov/cencode/t57c38.pdf) |
| Refund due on the return but an installment was short | Interest may still be charged, even with a refund | [2026 Form ND-1ES](https://www.tax.nd.gov/sites/www/files/documents/forms/software-developer/individual-income-forms/28709-form-nd-1es-2026%20final.pdf) |
| No 2025 North Dakota return was required | 2025 net tax liability is zero, so no 2026 estimates are required | same form, condition 2 and line 12 |
| Moved into North Dakota during 2025 with no North Dakota income before the move | Prior-year test does not apply; meet the 90% test | [2026 Form ND-1ES, condition 4(b) and line 13](https://www.tax.nd.gov/sites/www/files/documents/forms/software-developer/individual-income-forms/28709-form-nd-1es-2026%20final.pdf); [N.D.C.C. 57-38-62(1)(b)(1)](https://ndlegis.gov/cencode/t57c38.pdf) |
| High-income client (federal 110% prior-year rule) | North Dakota keeps 100% of the prior-year liability; the federal and state required payments differ | same form, line 12 |
| Federal safe harbor met by withholding | The state tests are separate: check North Dakota withholding (state box of Form W-2 and Form 1099) against the state liability | same form, condition 4 |
| Oil or gas royalty with North Dakota extraction or production tax withheld | Not income tax withholding: do not count it on worksheet line 9 or Form ND-1, line 26 | [2025 booklet, line 26](https://www.tax.nd.gov/sites/www/files/documents/forms/individual/2025-iit/2025-individual-income-tax-booklet.pdf) |

### Judgement calls

| Situation | Guidance |
| --- | --- |
| Income spikes in the 3rd or 4th quarter (contract close, year-end distribution, Roth conversion, large capital gain) | Consider the federal annualized income installment method; keep the federal worksheet, because Schedule ND-1UT exception B and the 81-03-04-02(3)(c) waiver rest on it. |
| First year of self-employment with no 2025 return required | No 2026 estimates are required (condition 2); interest risk returns in 2027. Recommend voluntary payments if a large balance is expected. |
| Out-of-state pass-through income or wages | Size the estimate after the credit for income tax paid to another state (`nd-cross-border-tax`). |
| Client wants to skip installments and pay at year end | Show the interest cost (worked case B) against the cash benefit. |
| Spouses changing between joint and separate returns | Recompute the prior-year figure under Step 4 before relying on the 100% test. |

## Worked cases

**Case A: single Bismarck freelancer, regular installments.** Full-year resident, single. 2025 North Dakota net tax liability USD 1,420. Expected 2026 North Dakota taxable income USD 120,000 after federal taxable income and state adjustments, no credits, no withholding, required to pay federal estimates. The 2026 tax from the single schedule in `nd-income-tax` (0% to USD 49,575, then 1.95%) is (120,000 - 49,575) x 1.95% = USD 1,373.29 (line 8). Line 10 is USD 1,373.29, at least USD 1,000, so continue. Line 11 is 90% = USD 1,235.96; line 12 is USD 1,420; line 13 is the smaller, USD 1,235.96; line 14 is USD 1,235.96, so USD 308.99 on each of the four dates.

```oa-check
name: ND-1ES 2026 single resident, regular installments
inputs:
  nd_taxable_income: 120000
  zero_band_top: 49575
  rate: 0.0195
  prior_year_liability: 1420
  withholding: 0
steps:
  - net_tax_liability: round((nd_taxable_income - zero_band_top) * rate, 2)
  - balance_after_withholding: net_tax_liability - withholding
  - current_year_test: round(net_tax_liability * 0.90, 2)
  - required: min(current_year_test, prior_year_liability)
  - minimum_annual_payment: required - withholding
  - installment: round(minimum_annual_payment / 4, 2)
expected:
  net_tax_liability: 1373.29
  balance_after_withholding: 1373.29
  current_year_test: 1235.96
  required: 1235.96
  installment: 308.99
```

**Case B: decision, pay each quarter or pay it all on 15 January 2027?** Married couple filing jointly, both full-year residents. 2026 net tax liability USD 6,775, North Dakota withholding USD 4,800, 2025 net tax liability USD 5,900. Line 10 is USD 1,975, so estimates are required. Line 11 is USD 6,097.50, line 12 is USD 5,900, line 13 is USD 5,900, and line 14 is USD 1,100: USD 275 per quarter. (Federally the 110% rule could apply to them; North Dakota stays at 100%.)

- **Option 1, pay USD 275 on each date:** no interest.
- **Option 2, pay nothing until 15 January 2027, then USD 1,100:** the 4th installment is on time and the excess clears the three earlier underpayments on 15 January 2027. Using the Schedule ND-1UT rounding: 1st quarter 275 days (0.753 years, 0.090 after the 12% step) = USD 24.75; 2nd quarter 214 days (0.586, 0.070) = USD 19.25; 3rd quarter 122 days (0.334, 0.040) = USD 11.00; total USD 55.00. The USD 500 waiver does not apply because liability exceeds withholding by USD 1,975.
- **The figure that decides:** USD 55.00 of interest against the value of holding USD 825 for an average of about seven months. Recommend Option 1 unless the cash is genuinely needed.

```oa-check
name: ND-1UT interest, three missed quarters paid on 15 January 2027
inputs:
  net_tax_liability: 6775
  prior_year_liability: 5900
  withholding: 4800
  q1_rate_factor: 0.090
  q2_rate_factor: 0.070
  q3_rate_factor: 0.040
steps:
  - required: min(net_tax_liability * 0.90, prior_year_liability)
  - minimum_annual_payment: required - withholding
  - installment: minimum_annual_payment / 4
  - interest_q1: installment * q1_rate_factor
  - interest_q2: installment * q2_rate_factor
  - interest_q3: installment * q3_rate_factor
  - total_interest: interest_q1 + interest_q2 + interest_q3
expected:
  required: 5900
  minimum_annual_payment: 1100
  installment: 275
  total_interest: 55.00
```

The rate factors are the Schedule ND-1UT line 16d results: 275/365 = 0.753 x 0.12 = 0.090; 214/365 = 0.586 x 0.12 = 0.070; 122/365 = 0.334 x 0.12 = 0.040, each rounded to three decimals as the schedule instructs.

## When to refuse or refer

- **Estates and trusts:** they fall under N.D.C.C. 57-38-62 too, but the fiduciary forms and rules are not covered here. Refer.
- **Corporations:** corporate estimated tax (Form 40-ES and its USD 5,000 tests) belongs to `nd-corporate-tax`.
- **Pass-through entity payments:** not covered by this skill.
- **Part-year and nonresident cases** beyond worksheet lines 15 to 19 and exception D (allocation of income between states): use `nd-cross-border-tax` and the Schedule ND-1NR instructions.
- **Farm income averaging (Schedule ND-1FA)** interaction: the worksheet ignores it; refer for specialist review.
- **Years before 2025 or amended estimate computations:** different schedules; refer.
- **Drafting the good-cause waiver request:** the client or their representative writes and signs it; this skill states only the rule.

## Filing and payment

- 2026 installments: 15 April, 15 June, 15 September 2026 and 15 January 2027, paid through tax.nd.gov "Make A Payment" or by check with the 2026 ND-1ES voucher to PO Box 5622, Bismarck, ND 58506-5622.
- Reconciliation on the 2026 Form ND-1 (due generally 15 April 2027): on the 2025 form the lines were 25 (net tax liability), 26 (withholding), 27 (estimated payments, including Form ND-1EXT payments and an overpayment left on deposit) and 37 (interest from Schedule ND-1UT). Confirm the 2026 line numbers when the 2026 form is published.
- Federal coordination: the North Dakota calendar matches the federal Form 1040-ES calendar; schedule both on the same four dates. If the federal annualized method is used, carry it to Schedule ND-1UT exception B.
- Questions: 701-328-1247; individualtax@nd.gov ([2026 Form ND-1ES, page 3](https://www.tax.nd.gov/sites/www/files/documents/forms/software-developer/individual-income-forms/28709-form-nd-1es-2026%20final.pdf)).

## Completion checklist

- [ ] Federal estimated-tax requirement confirmed (from `us-quarterly-estimated-tax`).
- [ ] 2025 Form ND-1, line 25 net tax liability obtained (or no-return-required confirmed).
- [ ] 2026 tax computed with `nd-income-tax`, credits subtracted, withholding estimated.
- [ ] Worksheet lines 10, 12 and 13 stop points checked; move-in rule checked.
- [ ] Filing-status change handled under Step 4.
- [ ] Installment amounts and the four dates given; farmer or partial-year option recorded where it applies.
- [ ] 2025 overpayment application and its quarter recorded.
- [ ] Payment method and voucher details given.
- [ ] Where an installment was missed, Schedule ND-1UT interest and every waiver tested.

## Sources

| Source | URL | Read on |
| --- | --- | --- |
| 2026 Form ND-1ES (SFN 28709, 12-2025). Read for all four conditions, the page 2 worksheet lines 1 to 19, the 2026 due dates, fiscal-year, farmer and part-year rules, payment methods and mailing address, 12% interest and contact details. | https://www.tax.nd.gov/sites/www/files/documents/forms/software-developer/individual-income-forms/28709-form-nd-1es-2026%20final.pdf | 2026-11-14 |
| N.D.C.C. chapter 57-38. Read for sections 57-38-45 (interest, penalties, good-cause waiver in subsection 5), 57-38-62 (requirement, tests, joint and separate rules, interest rule, definitions, overpayment application) and 57-38-63 (due dates, fiscal and short years). | https://ndlegis.gov/cencode/t57c38.pdf | 2026-11-14 |
| N.D. Admin. Code chapter 81-03-04. Read for section 81-03-04-02 (amended return, interest waivers in subsection 3, joint prior-year rule in subsection 4) and section 81-03-04-03 (no offset of estimated payments). | https://ndlegis.gov/prod/acdata/pdf/81-03-04.pdf | 2026-11-14 |
| 2025 Schedule ND-1UT (SFN 28704, 12-2025), 2025-2026 filing cycle. Read for Parts 1 to 3, the exceptions A to D, line 8 withholding rule, line 16 rounding steps and line 17 USD 5.00 rule. | https://www.tax.nd.gov/sites/www/files/documents/forms/individual/2025-iit/28704-schedule-nd-1ut-2025.pdf | 2026-11-14 |
| 2025 individual income tax booklet, 2025-2026 filing cycle. Read for "Estimated tax requirement (for 2026)" and Form ND-1 line 26, 27, 30 and 37 instructions. | https://www.tax.nd.gov/sites/www/files/documents/forms/individual/2025-iit/2025-individual-income-tax-booklet.pdf | 2026-11-14 |

Not yet confirmed: the 2026 Schedule ND-1UT and 2026 Form ND-1 line numbers (the 2025 forms are used, labelled 2025-2026 filing cycle); the exact date in the federal 4th quarter exception C for 2026; whether any electronic-payment mandate applies to individual estimated tax (none was found in the sources read); card processing fees; and the fiduciary and pass-through estimated payment forms, which this skill does not cover.
