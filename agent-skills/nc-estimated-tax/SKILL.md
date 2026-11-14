---
name: nc-estimated-tax
description: "North Carolina individual estimated income tax for tax year 2026, Form NC-40, and interest on underpayment, Form D-422. Covers the $1,000 requirement (tax after NC withholding and credits), the four installments due April 15, June 15 and September 15, 2026 and January 15, 2027, the January 31 file-and-pay rule, the required annual payment as the lesser of 90% of 2026 tax or 100% of 2025 tax (G.S. 105-163.15; there is no 110% high-income rule in NC), the annualized income installment at 22.5%, 45%, 67.5% and 90%, withholding treated as paid evenly, the farmer and fisherman single installment, and the interest rate of 7% to December 31, 2026 and 8% from January 1, 2027. Trigger on \"NC estimated tax\", \"Form NC-40\", \"NC quarterly payments\", \"Form D-422\", \"D-422A\", \"NC underpayment interest\", \"North Carolina safe harbor\"."
license: "AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)"
metadata:
  source: openaccountants
  openaccountants_url: "https://www.openaccountants.com/skills/nc-estimated-tax"
  jurisdiction: "US-NC"
  tax_year: "2026"
  last_updated: "2026-11-13"
---

# North Carolina individual estimated income tax, tax year 2026

> **Source-cited draft.** Built from G.S. 105-163.15, 105-153.7 and 105-153.5, the NCDOR Estimated Income Tax page, the NCDOR interest rate page and the NCDOR 2025 D-401 instructions, read on 2026-11-13. No accountant has reviewed it. All outputs must be reviewed by a qualified tax professional before filing.

**Answer first.** A North Carolina individual must pay estimated tax for 2026 if the tax on the return, less NC withholding and credits, will be **$1,000 or more**. Pay with Form NC-40 by **April 15, June 15 and September 15, 2026 and January 15, 2027**. Each installment is **25%** of the required annual payment, which is the smaller of **90% of the 2026 tax** or **100% of the 2025 tax** (if 2025 was a 12-month year and a return was filed). NC has no 110% rule for high incomes. Underpayment interest runs at **7%** a year to December 31, 2026 and **8%** from January 1, 2027.

## Scope and who this is for

In scope: a North Carolina resident individual (sole proprietor, investor, retiree, or employee with too little withholding) planning or reviewing estimated payments for tax year 2026, and computing the D-422 interest.

Out of scope, and where it goes:

| Topic | Skill |
| --- | --- |
| Federal estimated tax, Form 1040-ES and Form 2210 | `us-quarterly-estimated-tax` |
| Computing the 2026 NC tax itself | `nc-income-tax` |
| Corporate estimated tax and taxed pass-through entity estimates | `nc-corporate-tax` |
| Raising wage withholding instead (Form NC-4) | `nc-payroll` |
| Estates and trusts (G.S. 105-163.15(k) excludes them) | refer |

## Ask the client first

1. **Projected 2026 NC taxable income** and credits (from `nc-income-tax`), and any big income event later in the year.
2. **The 2025 NC tax on the return** (D-400 line 19 less credits), whether 2025 was a full 12-month year, and whether a 2025 NC return was filed at all.
3. **NC tax withheld in 2026**, and whether the client can show the dates it was withheld.
4. **Estimated payments already made for 2026**, with dates (and any 2025 refund applied).
5. **Is at least two-thirds of gross income from farming or fishing?**

## The method, step by step

### Rates, bands and thresholds

| Item | Amount, 2026 | Source |
| --- | --- | --- |
| Estimated payments required, and interest possible, when tax less withholding and credits is | $1,000 or more | [G.S. 105-163.15(f)](https://www.ncleg.gov/EnactedLegislation/Statutes/HTML/BySection/Chapter_105/GS_105-163.15.html); [NCDOR Estimated Income Tax](https://www.ncdor.gov/taxes-forms/individual-income-tax/estimated-income-tax) |
| Required annual payment, current-year test | 90% of 2026 tax | [G.S. 105-163.15(d)(1)](https://www.ncleg.gov/EnactedLegislation/Statutes/HTML/BySection/Chapter_105/GS_105-163.15.html) |
| Required annual payment, prior-year test (12-month year, return filed) | 100% of 2025 tax | [G.S. 105-163.15(d)(2)](https://www.ncleg.gov/EnactedLegislation/Statutes/HTML/BySection/Chapter_105/GS_105-163.15.html) |
| Each regular installment | 25% | [G.S. 105-163.15(d)](https://www.ncleg.gov/EnactedLegislation/Statutes/HTML/BySection/Chapter_105/GS_105-163.15.html) |
| Annualized installments, cumulative share of annualized tax: 1st / 2nd / 3rd / 4th | 22.5% / 45% / 67.5% / 90% | [G.S. 105-163.15(e)](https://www.ncleg.gov/EnactedLegislation/Statutes/HTML/BySection/Chapter_105/GS_105-163.15.html) |
| Farmer or fisherman single installment (by January 15, 2027) | lesser of 66 2/3% of 2026 tax or 100% of 2025 tax | [G.S. 105-163.15(i)](https://www.ncleg.gov/EnactedLegislation/Statutes/HTML/BySection/Chapter_105/GS_105-163.15.html) |
| Interest rate on underpayments, 1 January 2025 to 31 December 2026 | 7% a year | [NCDOR interest rate](https://www.ncdor.gov/interest) |
| Interest rate, 1 January to 30 June 2027 | 8% a year | [NCDOR interest rate](https://www.ncdor.gov/interest) |
| 2026 income tax rate, for projecting the tax | 3.99% | [G.S. 105-153.7](https://www.ncleg.gov/EnactedLegislation/Statutes/HTML/BySection/Chapter_105/GS_105-153.7.html) |
| 2025 income tax rate, for the prior-year test | 4.25% | [G.S. 105-153.7](https://www.ncleg.gov/EnactedLegislation/Statutes/HTML/BySection/Chapter_105/GS_105-153.7.html) |

"Tax" here is the D-400 tax less credits, other than the credit for withholding ([G.S. 105-163.15(g)](https://www.ncleg.gov/EnactedLegislation/Statutes/HTML/BySection/Chapter_105/GS_105-163.15.html)).

### Step 1: is anything required?

Project the 2026 NC tax with `nc-income-tax`, subtract credits and expected NC withholding. If the result is under **$1,000**, no estimates are required and no interest can be charged. No interest is charged either if the individual had **no NC tax liability for 2025** ([G.S. 105-163.15(f)](https://www.ncleg.gov/EnactedLegislation/Statutes/HTML/BySection/Chapter_105/GS_105-163.15.html)).

### Step 2: required annual payment

Required annual payment = the smaller of 90% of 2026 tax and 100% of 2025 tax. If 2025 was a short year or no 2025 return was filed, only the 90% test applies.

### Step 3: installments

Each installment is 25% of the required annual payment, due:

| Installment | Due |
| --- | --- |
| 1 | April 15, 2026 |
| 2 | June 15, 2026 |
| 3 | September 15, 2026 |
| 4 | January 15, 2027 |

**Withholding** counts as estimated tax paid in equal parts on each due date, unless the client proves the actual withholding dates ([G.S. 105-163.15(g)](https://www.ncleg.gov/EnactedLegislation/Statutes/HTML/BySection/Chapter_105/GS_105-163.15.html)). So extra withholding late in the year still cures earlier quarters. Payments apply to installments in date order.

**January 31 rule:** if the 2026 return is filed and the balance paid by **January 31, 2027**, there is no interest on a short 4th installment ([G.S. 105-163.15(h)](https://www.ncleg.gov/EnactedLegislation/Statutes/HTML/BySection/Chapter_105/GS_105-163.15.html)).

### Step 4: annualized income installment (Form D-422A), if income is uneven

For an installment, if the annualized amount is lower, it may be used instead: the applicable percentage (22.5%, 45%, 67.5%, 90%) of the tax computed on annualized taxable income for the months before the due date, less earlier required installments. Any reduction is recaptured by raising the next regular installment ([G.S. 105-163.15(e)](https://www.ncleg.gov/EnactedLegislation/Statutes/HTML/BySection/Chapter_105/GS_105-163.15.html)). The Secretary sets the annualizing rules; follow the D-422A worksheet.

### Step 5: interest on underpayment (Form D-422)

For each installment: underpayment = required installment less the amount paid by its due date. Interest = underpayment × the annual rate × days ÷ 365, from the due date to the earlier of the date paid and **April 15, 2027** ([G.S. 105-163.15(a), (b)](https://www.ncleg.gov/EnactedLegislation/Statutes/HTML/BySection/Chapter_105/GS_105-163.15.html)). Use 7% for days in 2026 and 8% for days from January 1, 2027. The total goes on D-400 line 26e (2025 line number). D-422 and D-422A are kept, not attached; a farmer or fisherman, or an annualized filer, enters exception code "E" (2025 D-401).

### Step 6: pay

File Form NC-40 with each payment: online through NCDOR eServices (payments can be scheduled up to 365 days ahead), through tax software (up to 12 months ahead), or by check or money order to the North Carolina Department of Revenue, PO Box 25000, Raleigh, NC ([NCDOR Estimated Income Tax](https://www.ncdor.gov/taxes-forms/individual-income-tax/estimated-income-tax)).

## Boundary and exception table

| Situation | Treatment |
| --- | --- |
| No NC tax liability for 2025 | No underpayment interest for 2026 at all |
| 2026 tax less withholding and credits under $1,000 | No estimates required; no interest |
| High 2025 income | Still 100% of 2025 tax; NC has no 110% test |
| New NC resident with no 2025 NC return | Only the 90% of 2026 test |
| Farmer or fisherman (two-thirds or more of gross income from farming, oyster farming or fishing, this year or last) | One installment by January 15, 2027; no interest if the return is filed and paid by March 1, 2027 |
| Return filed and paid by January 31, 2027 | No interest on the 4th installment |
| Extra withholding in December | Treated as paid evenly over the four dates unless actual dates are shown |
| Overpayment in a later quarter | Applies to the earliest unpaid installment first; does not stop interest already run on an earlier one |
| Extension to file the D-400 | Does not extend estimated tax or the time to pay |
| Big gain in September | Annualized method can lower installments 1 and 2 |

### Defaults when a fact is missing

| Missing fact | Default, and flag it |
| --- | --- |
| 2025 NC tax | Use only the 90% current-year test |
| Withholding dates | Treat withholding as paid evenly |
| Payment dates | Treat a payment as made on the date NCDOR records it |

## Worked cases

### Case 1: a single freelancer with no withholding

Projected 2026 NC income after Schedule S $120,000, single, no children, no credits. Taxable income $107,250 ($120,000 less $12,750); 2026 tax at 3.99%: **$4,279.28**. 2025 NC tax was $4,000. 90% of 2026 is $3,851.35, below $4,000, so the required annual payment is **$3,851.35** and each installment **$962.84** (pay $962.84, $962.84, $962.84 and $962.83). The balance of $427.93 is due April 15, 2027.

```oa-check
name: NC 2026 estimated tax, freelancer
inputs:
  nc_income: 120000
  std: 12750
  rate: 0.0399
  prior_tax: 4000
steps:
  - tax: round((nc_income - std) * rate, 2)
  - rap: round(min(tax * 0.90, prior_tax), 2)
  - installment: round(rap / 4, 2)
  - balance: tax - rap
expected:
  tax: 4279.28
  rap: 3851.35
  installment: 962.84
  balance: 427.93
```

### Case 2: must the employee pay estimates, and what if a payment is late?

An employee's 2026 NC tax is $3,000 and NC withholding will be $2,200: the gap is $800, under $1,000, so **no estimates** and no interest. A colleague with a $1,000 shortfall on installment 1 (due April 15, 2026) pays it on June 15, 2026: 61 days at 7% gives interest of **$11.70**.

```oa-check
name: NC estimated tax threshold and D-422 interest
inputs:
  tax: 3000
  withholding: 2200
  short: 1000
  rate: 0.07
  days: 61
steps:
  - gap: tax - withholding
  - required: min(max(gap - 999.99, 0), 1)
  - interest: round(short * rate * days / 365, 2)
expected:
  gap: 800
  required: 0
  interest: 11.70
```

## When to refuse or refer

| Situation | Action |
| --- | --- |
| Estate or trust estimates | Refer; G.S. 105-163.15 does not apply to them |
| Part-year resident or nonresident projections | Refer; needs Schedule PN |
| Annualized installments across a change in filing status or residence | Refer |
| A request to waive underpayment interest | Refer; this rewrite found no waiver in G.S. 105-163.15 (v1 listed retirement, disability and casualty waivers, not supported) |
| Taxed partnership or S corporation paying tax for the owner | Use `nc-corporate-tax`; the owner's NC tax falls by the Schedule S deduction |

## Filing and payment

| Obligation | When | Source |
| --- | --- | --- |
| NC-40 installments for 2026 | April 15, June 15, September 15, 2026; January 15, 2027 | [G.S. 105-163.15(c)](https://www.ncleg.gov/EnactedLegislation/Statutes/HTML/BySection/Chapter_105/GS_105-163.15.html) |
| File and pay in full instead of the 4th installment | January 31, 2027 | [G.S. 105-163.15(h)](https://www.ncleg.gov/EnactedLegislation/Statutes/HTML/BySection/Chapter_105/GS_105-163.15.html) |
| Farmer or fisherman | January 15, 2027, or file and pay by March 1, 2027 | [G.S. 105-163.15(i)](https://www.ncleg.gov/EnactedLegislation/Statutes/HTML/BySection/Chapter_105/GS_105-163.15.html) |
| D-422 interest, on the D-400 | With the return due April 15, 2027 | [NCDOR 2025 D-401](https://www.ncdor.gov/2025-d-401-individual-income-tax-instructions/open) |

## Completion checklist

- [ ] 2026 tax projected with the 3.99% rate and the NC deductions
- [ ] $1,000 test and the no-2025-liability test run
- [ ] Required annual payment = lesser of 90% of 2026 or 100% of 2025
- [ ] Withholding spread evenly unless dates are proved
- [ ] Annualized method tested if income is uneven
- [ ] Interest computed per installment with 7% for 2026 days and 8% for 2027 days
- [ ] NC-40 payment confirmations saved

## Sources

| Source | URL | Read for | Read on |
| --- | --- | --- | --- |
| G.S. 105-163.15 | https://www.ncleg.gov/EnactedLegislation/Statutes/HTML/BySection/Chapter_105/GS_105-163.15.html | Read for installments, required annual payment, annualization, $1,000 test, January 31 and farmer rules | 2026-11-13 |
| G.S. 105-153.7 | https://www.ncleg.gov/EnactedLegislation/Statutes/HTML/BySection/Chapter_105/GS_105-153.7.html | Read for the 3.99% and 4.25% rates | 2026-11-13 |
| G.S. 105-153.5 | https://www.ncleg.gov/EnactedLegislation/Statutes/HTML/BySection/Chapter_105/GS_105-153.5.html | Read for the $12,750 standard deduction in Case 1 | 2026-11-13 |
| NCDOR Estimated Income Tax | https://www.ncdor.gov/taxes-forms/individual-income-tax/estimated-income-tax | Read for the $1,000 rule, due dates, Form NC-40 and payment options | 2026-11-13 |
| NCDOR interest rate | https://www.ncdor.gov/interest | Read for 7% through 2026 and 8% from 1 January 2027 | 2026-11-13 |
| NCDOR 2025 D-401 instructions | https://www.ncdor.gov/2025-d-401-individual-income-tax-instructions/open | Read for line 26e, D-422, D-422A and the exception code | 2026-11-13 |

Not yet confirmed: the 2026 NC-40, D-422 and D-422A form lines (2026 forms publish in January 2027); the D-422A annualization factors by period (the statute leaves them to the Secretary; v1's factors 4, 2.4, 1.5 and 1 are the federal ones and were not checked on the NC form); the interest rate from 1 July 2027.

## Today's figures and who stands behind this skill

This file is an AI skill (tax rules your AI follows) from OpenAccountants, copied on 2026-11-13. Rates, thresholds and deadlines change. For the current version of this skill, its official sources and the named accountant (if any) who stands behind it, call `get_skill` with slug `nc-estimated-tax` on the OpenAccountants connector (https://www.openaccountants.com/connect), or read https://www.openaccountants.com/skills/nc-estimated-tax. If neither is available, confirm every figure against the official source pages cited above before relying on it.
