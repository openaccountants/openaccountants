---
name: ga-estimated-tax-depth
description: Work out Georgia estimated tax for tax year 2026, for individuals and fiduciaries (Form 500-ES, penalty on Form 500 UET) and for corporations and electing S corporations and partnerships (Form 602-ES, penalty on Form 600 UET). Covers who must pay (the $1,000 test for individuals, net income over $25,000 for corporations), the installment dates and fewer-installment rules, the lesser of 100% of the prior year's tax or 70% of the current year's, the three individual exceptions and the corporate annualization exception, the 9% a year penalty, farmers and fishermen, the first election year rule for electing entities and the EFT rule above $10,000. Trigger on "Georgia estimated tax", "Form 500-ES", "Form 500 UET", "Form 602-ES", "Georgia underpayment penalty".
version: "1.0"
jurisdiction: US-GA
tax_year: 2026
last_updated: 2026-11-13
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
tier: 2
domain: income-tax
type: computation
---

# Georgia estimated tax, tax year 2026

> **Source-cited draft.** Built from the 2026 Form 500-ES, Form 500 UET and Form 600 UET (for tax years 2025 and later), the 2026 Form 602-ES, the 2025 IT-611 booklet and DOR's HB 149 pass-through entity tax FAQ and penalty page, read on 2026-11-13. No accountant has reviewed it. All outputs must be reviewed by a qualified tax professional before filing.

**Answer first.** An individual must pay Georgia estimated tax for 2026 if gross income not subject to withholding is expected to exceed exemptions plus deductions plus **$1,000**. Installments are due **15 April, 15 June and 15 September 2026 and 15 January 2027**. To avoid the penalty, pay by each date a quarter of the lesser of **100% of the 2025 tax** (if 2025 was a 12-month return) or **70% of the 2026 tax**. Georgia has no 110% rule for high incomes. A corporation pays if net income is expected to exceed **$25,000**, with the fourth installment on **15 December**. The penalty is **9% a year** on each shortfall.

## Scope and who this is for

In scope: 2026 estimated tax for Georgia individuals and fiduciaries, C corporations, and S corporations and partnerships that elect to pay tax at the entity level, with the penalty computation. The tax itself is computed in `ga-income-tax` (individuals) and `ga-corporate-and-ptet` (corporations and electing entities); the rates and amounts are owned there.

Out of scope: federal estimated tax (`us-quarterly-estimated-tax`); fiscal-year individual penalty computation (DOR asks fiscal-year individuals to call it); withholding by employers (`ga-payroll`).

## Ask the client first

1. **Individual, fiduciary, C corporation or electing entity?** The threshold, forms, fourth date and penalty end date differ.
2. **The prior year's Georgia tax, and did that return cover 12 months?** The prior-year option is lost if not.
3. **This year's expected Georgia tax and Georgia withholding**, and when in the year the income arises (seasonal or one-off income may support fewer installments or an exception).
4. **For an individual: is at least two thirds of gross income from farming or fishing?** A separate 1 March route applies.
5. **For an owner of an S corporation or partnership: has the entity elected to pay at the entity level this year?** The owner's own estimate then drops, and the entity pays estimates instead.
6. **Payments made so far**, with dates and amounts, and whether any single quarterly payment exceeds $10,000 (electronic payment required).

## The method, step by step

### Rates, bands and thresholds

| Item | Amount | Source |
| --- | --- | --- |
| Individual and fiduciary: income not subject to withholding above exemptions and deductions that triggers estimates | $1,000 | [2026 Form 500-ES](https://dor.georgia.gov/document/document/2026-500-es-estimated-tax-individuals-and-fiduciaries/download) |
| Individual installment dates, 2026 | 15 April, 15 June, 15 September 2026, 15 January 2027 | same |
| Required installment, individuals and corporations: lesser of prior-year option | 100% of the immediately preceding year's tax (12-month return only) | [Form 500 UET](https://dor.georgia.gov/document/document/beginning-or-after-january-1-2025-500-uet-underpayment-estimated-tax-individuals/download); [Form 600 UET](https://dor.georgia.gov/document/document/beginning-or-after-january-1-2025-600-uet-underpayment-estimated-tax/download) |
| Required installment: current-year option | 70% of the current year's tax after credits | same |
| Underpayment penalty rate | 9% a year | same |
| Individual exception 3 (actual income for 3, 5 and 8 months) | 90% of the tax on that income | [Form 500 UET](https://dor.georgia.gov/document/document/beginning-or-after-january-1-2025-500-uet-underpayment-estimated-tax-individuals/download) |
| Annualized income exception (individuals and corporations) | 70% of the tax on annualized income | [Form 500 UET](https://dor.georgia.gov/document/document/beginning-or-after-january-1-2025-500-uet-underpayment-estimated-tax-individuals/download); [Form 600 UET](https://dor.georgia.gov/document/document/beginning-or-after-january-1-2025-600-uet-underpayment-estimated-tax/download) |
| Farmers and fishermen: share of gross income from farming or fishing | at least two thirds | [2026 Form 500-ES](https://dor.georgia.gov/document/document/2026-500-es-estimated-tax-individuals-and-fiduciaries/download) |
| Corporations: net income expected to exceed | $25,000 | [2025 IT-611 booklet](https://dor.georgia.gov/document/document/2025-it611-corporate-income-tax-instruction-booklet/download) |
| Corporate installment dates, calendar 2026 | 15 April, 15 June, 15 September, 15 December 2026 | same; [2026 Form 602-ES](https://dor.georgia.gov/document/document/2026-602es-corporate-and-partnership-estimated-tax/download) |
| Quarterly payment that must be made by electronic funds transfer | more than $10,000 | [2025 IT-611 booklet](https://dor.georgia.gov/document/document/2025-it611-corporate-income-tax-instruction-booklet/download) |

### Individuals and fiduciaries (Form 500-ES and Form 500 UET)

1. **Test whether estimates are required.** A person "who reasonably expects to have gross income during the year which exceeds (1) applicable exemptions, plus (2) estimated deductions, plus (3) $1,000 of income not subject to withholding" must pay. Not required if, by agreement with the employer, extra tax is withheld to cover it. Exemptions and deductions are the 2026 amounts in `ga-income-tax`; the 2026 Form 500-ES worksheet still prints the 2025 amounts, so use the HB 463 amounts.
2. **Estimate the 2026 tax** on the Form 500-ES worksheet, less expected withholding and credits.
3. **Count the installments** by when the requirement is first met ([Form 500 UET](https://dor.georgia.gov/document/document/beginning-or-after-january-1-2025-500-uet-underpayment-estimated-tax-individuals/download), Instruction B):

   | Requirement first met | First payment due | Installments |
   | --- | --- | --- |
   | 1 January to 31 March | 15 April | 4 |
   | 1 April to 31 May | 15 June | 3 |
   | 1 June to 31 August | 15 September | 2 |
   | On or after 1 September | 15 January | 1 |

   A due date on a Saturday, Sunday or legal holiday moves to the next workday. Fiscal-year individuals use corresponding dates.
4. **Work the required installment** (Form 500 UET Lines 4 to 8): the lesser of (a) 100% of the immediately preceding year's tax, if that return covered 12 months, divided by the number of installments, and (b) 70% of the current year's tax after credits (Form 500 Line 16 less credits), divided by the number of installments.
5. **Credit payments.** Withholding is "treated equally paid for each quarter". An overpayment of one installment carries to the next.
6. **Check the exceptions** (each underpaid installment may use a different one, with a separate computation page): (1) tax on the prior year's income at the current year's rates and exemptions; (2) 70% of the tax on annualized current-year income (income to the end of the month before the installment, less deductions, times 12, divided by the months, less dependent exemptions); (3) 90% of the tax on actual income for the 3, 5 and 8 month periods (not usable for the fourth installment).
7. **Compute the penalty** on each remaining shortfall: 9% a year for the days from the installment due date to the earlier of the payment date and 15 April 2027. If the return is filed and the balance paid by 31 January 2027, the balance is treated as paid on 15 January 2027.
8. **Special cases.** Farmers and fishermen (at least two thirds of gross income) may file and pay in full by 1 March 2027 instead, entering $0 on Line 21 and ticking "500 UET Exception Attached". Estates of a decedent and testamentary trusts need no estimates for years ending before two years after death (Exception 4).

### Corporations and electing entities (Form 602-ES and Form 600 UET)

1. **Test:** every corporation subject to Georgia tax whose net income "can reasonably be expected to exceed Twenty-Five Thousand Dollars ($25,000.00)" ([2025 IT-611 booklet](https://dor.georgia.gov/document/document/2025-it611-corporate-income-tax-instruction-booklet/download)). An S corporation or partnership that elects to pay at the entity level "is required to make estimated tax payments in the same manner as a C Corporation" ([DOR HB 149 PTET FAQ](https://dor.georgia.gov/hb-149-pass-through-entity-tax-faq)); a partnership must register on the Georgia Tax Center to pay online.
2. **Dates:** 25% each on the 15th day of the 4th, 6th, 9th and 12th months (15 April, 15 June, 15 September, 15 December 2026 for a calendar year) if the requirement is met before the 4th month. Met later: after the 3rd and before the 6th month, one third each at the 6th, 9th and 12th months; after the 5th and before the 9th month, 50% at each of the 9th and 12th months; after the 8th and before the 12th month, 100% at the 12th month.
3. **Required amount (Form 600 UET):** each installment is the lesser of 100% of the prior year's tax (12-month return only) and 70% of the current year's tax after credits, each divided by the number of installments. The annualized exception applies if payments to date equal or exceed 70% of the tax on annualized income for the months before the installment.
4. **Penalty:** 9% a year on each underpaid installment, from its due date to the payment date or 15 April, whichever is earlier; for S corporations and partnerships, 15 March. DOR also lists "5% of Georgia income tax imposed for the taxable year" under O.C.G.A. §§ 48-7-120 and 48-7-126 for failure to pay estimated tax ([DOR penalty and interest rates](https://dor.georgia.gov/penalty-and-interest-rates)).
5. **First election year for an S corporation or partnership:** DOR's FAQ says the entity "must compute the penalty on Form 600 UET assuming the tax for the prior year was equal to 5.75% of the prior's year's income". 5.75% is the pre-2024 rate; the FAQ has not been updated, so ask DOR which rate it applies before relying on it. Owners' own estimates cannot be transferred to the entity; the entity may tick "UET Annualization Exception Attached" and compute the penalty as if those payments were its own.
6. **Owner side.** Once the entity elects, the owner excludes the entity-taxed income (PTEDED, see `ga-income-tax`), so the owner's expected tax and required estimate fall. An owner whose 2025 tax included that income will overpay on the 100% prior-year option; the 70% current-year option, on the lower 2026 tax, is then the lesser.
7. **Pay** through the Georgia Tax Center or with Form 602-ES. A quarterly payment of more than $10,000 must be made by EFT; DOR's booklet warns of a 10% penalty if not paid through the Georgia Tax Center.

## Boundary and exception table

| Situation | Rule |
| --- | --- |
| Prior-year Georgia return covered fewer than 12 months, or no prior return | The 100% prior-year option is not available; use 70% of the current year |
| High-income individual (prior federal AGI over $150,000) | No 110% rule in Georgia: the prior-year option stays at 100% |
| Corporation expects net income of exactly $25,000 | No estimates required: the test is "exceed" |
| Withholding only, paid late in the year | Withholding counts as paid equally each quarter, which can cure early shortfalls |
| Income arises only after 31 August | One installment, due 15 January 2027 |
| Return filed and paid by 31 January 2027 | Balance treated as paid on 15 January 2027 |
| Entity elects for the first time in 2026 | Prior-year option uses DOR's 5.75% rule; confirm with DOR |

## Worked cases

Client facts are invented; rates and amounts are those above and in `ga-income-tax`.

**Case 1, a decision: which option sets the 2026 installments?** A single sole proprietor's 2026 Georgia tax is expected to be $3,244 (see `ga-income-tax` Case 1); there is no withholding. Her 2025 Georgia tax on a 12-month return was $3,000. Option (a): 100% of $3,000 = $3,000, or $750 an installment. Option (b): 70% of $3,244 = $2,270.80, or $567.70 an installment. The required installment is the lesser, $567.70. Paying $750 a quarter (option a) is the safe route in April, when the 2026 figure is still an estimate; it costs $182.30 a quarter of cash flow, refunded or credited at filing.

```oa-check
name: GA 2026 individual required installment, lesser of 100% prior and 70% current
inputs:
  prior_year_tax: 3000
  current_year_tax: 3244
  installments: 4
steps:
  - prior_option: prior_year_tax / installments
  - current_option: current_year_tax * 0.70 / installments
  - required: min(prior_option, current_option)
  - extra_cash_per_quarter: prior_option - current_option
expected:
  prior_option: 750
  current_option: 567.70
  required: 567.70
  extra_cash_per_quarter: 182.30
```

**Case 2: penalty on a missed installment.** The same client paid nothing on 15 June 2026 and paid the $567.70 on 15 September 2026, 92 days late. Penalty: $567.70 x 9% x 92 / 365 = $12.88. A corporation with the same shortfall on its 15 June installment, paid 15 December (183 days), would owe $567.70 x 9% x 183 / 365 = $25.62.

```oa-check
name: GA 9% a year underpayment penalty by days late
inputs:
  shortfall: 567.70
  days_individual: 92
  days_corporate: 183
steps:
  - penalty_individual: shortfall * 0.09 * days_individual / 365
  - penalty_corporate: shortfall * 0.09 * days_corporate / 365
expected:
  penalty_individual: 12.88
  penalty_corporate: 25.62
```

## When to refuse or refer

| Code | Situation | Action |
| --- | --- | --- |
| R-GAES-FISCAL | Fiscal-year individual underpayment penalty | Refer: DOR asks fiscal-year individuals to call 1-877-423-6711 |
| R-GAES-PTET1 | First election year penalty where the 5.75% rule matters | Ask DOR in writing before filing Form 600 UET |
| R-GAES-WAIVER | Penalty waiver requests for reasonable cause or disaster | Refer |
| R-GAES-ANNUAL | Annualized computation for a business without interim books | Refer: the exception needs income figures for each period |

## Filing and payment

1. **Individuals:** pay through the Georgia Tax Center (gtc.dor.ga.gov) or mail Form 500-ES with a check payable to the Georgia Department of Revenue. Report the payments on Form 500 Line 26 and attach Form 500 UET if a penalty applies or an exception is claimed (tick "500 UET Exception Attached").
2. **Corporations and electing entities:** pay through the Georgia Tax Center or with Form 602-ES, by EFT for any quarterly payment over $10,000. Attach Form 600 UET to Form 600, 600S or 700.
3. **After filing:** the penalty is shown on the return (Form 500 Line 42); DOR bills any difference.

## Completion checklist

- Threshold tested ($1,000 for individuals; net income over $25,000 for corporations and electing entities).
- Number of installments set by when the requirement was first met.
- Lesser of 100% prior-year (12-month return only) and 70% current-year used; no 110% rule applied.
- Withholding spread equally across quarters.
- Each shortfall checked against the exceptions before the 9% penalty.
- Corporate fourth installment on 15 December; S corporation and partnership penalty ends 15 March.
- EFT used for quarterly payments over $10,000.

## Sources

| Source | URL | Read on |
| --- | --- | --- |
| 2026 Form 500-ES (estimated tax, individuals and fiduciaries). Read for who must pay (the $1,000 test), the employer-agreement exception, the four dates, fewer installments and the farmers and fishermen rule. | https://dor.georgia.gov/document/document/2026-500-es-estimated-tax-individuals-and-fiduciaries/download | 2026-11-13 |
| Form 500 UET, tax years 2025 and later (Rev. 07/15/25). Read for Lines 1 to 21, the 100% and 70% options, the installment chart, Exceptions 1 to 4, the 9% rate and Instructions E to G. | https://dor.georgia.gov/document/document/beginning-or-after-january-1-2025-500-uet-underpayment-estimated-tax-individuals/download | 2026-11-13 |
| Form 600 UET, tax years 2025 and later. Read for the corporate 100% and 70% options, the annualization exception, the 9% rate and the 15 April or 15 March end date. | https://dor.georgia.gov/document/document/beginning-or-after-january-1-2025-600-uet-underpayment-estimated-tax/download | 2026-11-13 |
| 2026 Form 602-ES (corporate and partnership estimated tax, Rev. 05/12/25). Read for the voucher and the fiscal-year rule. | https://dor.georgia.gov/document/document/2026-602es-corporate-and-partnership-estimated-tax/download | 2026-11-13 |
| 2025 IT-611 corporate income tax booklet. Read for the $25,000 test, the corporate installment schedule and the EFT rule. | https://dor.georgia.gov/document/document/2025-it611-corporate-income-tax-instruction-booklet/download | 2026-11-13 |
| DOR HB 149 pass-through entity tax FAQ. Read for electing-entity estimates and the 5.75% first-year rule. | https://dor.georgia.gov/hb-149-pass-through-entity-tax-faq | 2026-11-13 |
| DOR penalty and interest rates. Read for the estimated tax penalty row (O.C.G.A. §§ 48-7-120, 48-7-126). | https://dor.georgia.gov/penalty-and-interest-rates | 2026-11-13 |

Not yet confirmed: which rate DOR now applies in its first-election-year rule (its FAQ still says 5.75%); how DOR combines the 9% a year penalty with the separate 5% failure-to-pay-estimated-tax row on its penalty page; the 2026 IT-611 booklet was not published when read, so the corporate schedule is from the 2025 booklet (2025-2026 filing cycle).
