---
name: il-estimated-tax
description: Work out whether an Illinois individual (sole proprietor or single-member LLC owner) must make 2026 estimated income tax payments on Form IL-1040-ES, how much each installment is, and the late-payment penalty. Covers the more-than-$1,000 test after withholding and credits, the four equal installments due 15 April, 15 June and 15 September 2026 and 15 January 2027, the required annual payment as the lesser of 90% of the 2026 tax or 100% of the 2025 tax (no 110% rule), the annualized income installment percentages, the exceptions for farmers and nursing home residents, and the 2% or 10% penalty. Trigger on "Illinois estimated tax", "IL-1040-ES", "IL-2210", "Illinois quarterly payments". Load il-income-tax for the tax computation.
version: "2.0"
jurisdiction: US-IL
tax_year: 2026
last_updated: 2026-11-13
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
tier: 2
domain: income-tax
type: computation
---

# Illinois estimated income tax for individuals (Form IL-1040-ES), tax year 2026

> **Source-cited draft.** Built from 35 ILCS 5/803 and 5/804 (Illinois General Assembly), the 2026 Form IL-1040-ES, IDOR Publication 105 and IDOR Informational Bulletin FY 2026-15, read on 2026-11-13. No accountant has reviewed it. All outputs must be reviewed by a qualified tax professional before filing.

**Answer first.** An Illinois individual must pay 2026 estimated tax if the tax expected for 2026, after Illinois withholding, pass-through withholding and credits, is **more than $1,000** (35 ILCS 5/803(a)). Pay it in four equal installments due **15 April 2026, 15 June 2026, 15 September 2026 and 15 January 2027**. No penalty arises if the four timely installments total at least the lesser of **90%** of the 2026 tax or **100%** of the 2025 tax. Illinois has no 110% rule for high incomes. A late installment draws a penalty of **2%** of the tax due if paid 1 to 30 days late, **10%** if 31 days or later.

## Scope and who this is for

In scope: an individual Illinois resident (including a Schedule C sole proprietor or a disregarded single-member LLC owner) estimating 2026 Illinois income tax, the IL-1040-ES worksheet and vouchers, and the IL-2210 penalty.

Out of scope, and where it goes:

| Topic | Skill |
| --- | --- |
| The 2026 Illinois tax itself (base income, exemption, credits) | `il-income-tax` |
| Federal estimated tax (Form 1040-ES), with its 110% rule | `us-quarterly-estimated-tax` |
| Corporation estimated tax, and pass-through entity tax estimates by partnerships and S corporations | `il-pprt` |
| Employer withholding | `il-payroll` |

## Ask the client first

1. **Expected 2026 Illinois base income** (federal adjusted gross income plus and minus Schedule M items) and the number of exemptions.
2. **The 2025 Illinois tax** (Form IL-1040 for 2025) and whether that return covered 12 months and showed a liability.
3. **Expected 2026 Illinois withholding** (W-2 jobs, retirement withholding agreements) and pass-through withholding.
4. **Credits expected for 2026**: property tax, K-12, tax paid to other states, EITC, child tax credit, pass-through entity tax credit, Schedule 1299-C.
5. **Is income earned evenly?** If not, the annualized method may lower the early installments.
6. **Farmer** (at least two-thirds of gross income from farming) or **65 or older and permanently in a nursing home**? Then no estimated payments are required.
7. **A 2025 overpayment credited forward**, and the date it was elected.

## The method, step by step

### Rates, bands and thresholds

| Item | Amount, 2026 | Source |
| --- | --- | --- |
| Estimated payments required if estimated tax is more than (individuals, taxable years ending on or after 31 December 2019) | $1,000 | [35 ILCS 5/803(a)](https://www.ilga.gov/legislation/ilcs/fulltext.asp?DocName=003500050K803) |
| Rate used on the worksheet | 4.95% | [2026 Form IL-1040-ES, line 4](https://tax.illinois.gov/content/dam/soi/en/web/tax/forms/incometax/documents/currentyear/individual/il-1040-es.pdf) |
| Exemption allowance per exemption, 2026 | $2,925 | [IDOR Bulletin FY 2026-15](https://tax.illinois.gov/research/publications/bulletins/fy-2026-15.html) |
| Each installment, as a share of the required annual payment | 25% | [35 ILCS 5/804(c)(1)(A)](https://www.ilga.gov/legislation/ilcs/fulltext.asp?DocName=003500050K804) |
| Required annual payment, current-year test | 90% of the 2026 tax | [35 ILCS 5/804(c)(1)(B)(i)](https://www.ilga.gov/legislation/ilcs/fulltext.asp?DocName=003500050K804) |
| Required annual payment, prior-year test (2025 return showing a liability, 12-month year) | 100% of the 2025 tax | [35 ILCS 5/804(c)(1)(B)(ii)](https://www.ilga.gov/legislation/ilcs/fulltext.asp?DocName=003500050K804) |
| Annualized installment percentages, installments 1 to 4 | 22.5%, 45%, 67.5%, 90% | [35 ILCS 5/804(c)(2)(C)](https://www.ilga.gov/legislation/ilcs/fulltext.asp?DocName=003500050K804) |
| Installment due dates for 2026 | 15 April 2026, 15 June 2026, 15 September 2026, 15 January 2027 | [2026 Form IL-1040-ES](https://tax.illinois.gov/content/dam/soi/en/web/tax/forms/incometax/documents/currentyear/individual/il-1040-es.pdf) |
| Late estimated payment penalty, paid 1 to 30 days late | 2% of the tax due | [IDOR Publication 105](https://tax.illinois.gov/research/publications/pubs/illinois-estimated-payments-requirements-for-individuals-and-businesses.html) |
| Late estimated payment penalty, paid 31 days or later | 10% of the tax due | [IDOR Publication 105](https://tax.illinois.gov/research/publications/pubs/illinois-estimated-payments-requirements-for-individuals-and-businesses.html) |
| Farmer exception: share of gross income from farming | at least two-thirds | [35 ILCS 5/803(e)](https://www.ilga.gov/legislation/ilcs/fulltext.asp?DocName=003500050K803) |

The $1,000 test, the 90% and 100% tests and the installment percentages are fixed in the statute. A due date on a weekend or holiday moves to the next business day (Publication 105).

### The 2026 IL-1040-ES worksheet

1. **Line 1**: 2026 Illinois base income expected (see `il-income-tax`).
2. **Line 2**: exemption amount expected for 2026 ($2,925 per exemption plus $1,000 per 65-or-blind box; zero if federal adjusted gross income will exceed $250,000, or $500,000 joint).
3. **Line 3** = line 1 - line 2. **Line 4** = line 3 x 4.95%.
4. **Line 5**: medical cannabis and gaming licensee surcharges, if any. **Line 6** = line 4 + line 5.
5. **Line 7**: Illinois withholding and pass-through withholding expected. **Line 8**: credits expected (property tax, volunteer emergency worker, other states, K-12, EITC, child tax, pass-through entity tax, Schedule 1299-C). **Line 9** = line 7 + line 8.
6. **Line 10** = line 6 - line 9, the estimated tax. If $1,000 or less, stop: no estimated payments are required.
7. **Line 11** = line 10 / 4, rounded to whole dollars: each installment. A 2025 overpayment credited forward by the extended due date of the 2025 return reduces the first and later installments until used.
8. **Avoiding the penalty with less**: the four installments need only reach the required annual payment, the lesser of 90% of the 2026 tax and 100% of the 2025 tax (804(c)(1)(B)). Paying 25% of that by each date protects against the penalty even if the final 2026 tax is higher.
9. **Uneven income**: an installment may instead equal the annualized income installment: 22.5%, 45%, 67.5% or 90% of the tax on income annualized to the months before the due date, less earlier installments. Any reduction is recaptured in the next installment (804(c)(2)). Compute on Form IL-2210.

### Penalty

The penalty under 35 ILCS 5/804(a) is figured at the rate of Section 3-3 of the Uniform Penalty and Interest Act on the underpayment of each installment. IDOR describes it as 2% of the tax due for a payment 1 to 30 days late and 10% for 31 days or later (Publication 105). IDOR applies each payment to the earliest due date unless told otherwise. No penalty is imposed if the taxpayer was not required to file an Illinois return for 2025, or had no Illinois tax liability for a 12-month 2025 year (804(d)).

## Boundary and exception table

| Situation | Treatment |
| --- | --- |
| Estimated tax exactly $1,000 | Not more than $1,000: no payments required |
| High income (federal adjusted gross income over $150,000) | Still 100% of the prior-year tax; Illinois has no 110% rule |
| 2025 return covered less than 12 months, or showed no liability | The 100% prior-year test is not available; use 90% of 2026. If 2025 showed no liability for a 12-month year, no penalty (804(d)) |
| Not required to file for 2025 (new resident) | No underpayment penalty for 2026 (804(d)) |
| Farmer, at least two-thirds of gross income from farming | Not required to pay estimated tax (803(a), (e)) |
| 65 or older and permanently living in a nursing home | Not required to pay estimated tax (IL-1040-ES) |
| Joint estimated payments, separate returns filed | The payments may be treated as either spouse's or divided between them, as they elect (803(c)) |
| Fiscal-year taxpayer | Shift each date to the corresponding month (803(g)) |
| Paid electronically through MyTax Illinois | Do not send the paper voucher |

### Defaults when a fact is missing

| Missing fact | Default, and flag it |
| --- | --- |
| The 2025 Illinois tax | Use 90% of the 2026 estimate; ask for the 2025 IL-1040 line for total tax |
| Expected withholding | Assume none; ask for the latest pay stub |
| Whether income is even through the year | Assume even (four equal installments) |
| Whether the 2025 overpayment was credited forward | Assume refunded; ask |

### Red flags to raise with the client

| Flag | Why it matters |
| --- | --- |
| Federal plan uses 110% of prior-year tax | The Illinois figure is 100%; do not overpay by copying the federal plan |
| Large income late in the year | Annualizing on IL-2210 may remove early-quarter penalties |
| A payment more than 30 days late | The penalty rises from 2% to 10% of the tax due |

## Worked cases

**Case 1, a freelancer with no withholding.** A single filer expects 2026 Illinois base income of $100,000 from Schedule C, one exemption, no withholding and no credits.

Line 3: $100,000 - $2,925 = $97,075. Line 4: 4.95% = $4,805.21. Line 10 is more than $1,000, so payments are required. Line 11: $4,805.21 / 4 = $1,201.30, rounded to **$1,201** for each of the four dates.

```oa-check
name: Illinois IL-1040-ES single filer, base income 100,000 (2026)
inputs:
  base_income: 100000
  exemption: 2925
  withholding_and_credits: 0
steps:
  - net_income: base_income - exemption
  - tax: round(net_income * 0.0495, 2)
  - estimated_tax: tax - withholding_and_credits
  - installment: round(estimated_tax / 4, 0)
expected:
  net_income: 97075.00
  tax: 4805.21
  estimated_tax: 4805.21
  installment: 1201
```

**Case 2, a decision: base the 2026 installments on 2025 tax or on 2026 tax?** A consultant's 2026 Illinois tax is expected to be $8,000 after a strong year. Her 2025 Illinois return (12 months) showed tax of $5,000. Ninety percent of 2026 is $7,200; 100% of 2025 is $5,000. The required annual payment is the lesser, **$5,000**, so **$1,250** per installment avoids the penalty; the remaining $3,000 is due with the return on 15 April 2027. If she pays the first installment 20 days late, the penalty is 2% of $1,250 = $25. Recommend the prior-year basis for cash flow, with the balance set aside for April 2027.

```oa-check
name: Illinois required annual payment, prior-year against current-year (2026)
inputs:
  tax_2026: 8000
  tax_2025: 5000
steps:
  - current_test: tax_2026 * 0.90
  - prior_test: tax_2025 * 1.00
  - required_annual: min(current_test, prior_test)
  - installment: required_annual * 0.25
  - balance_with_return: tax_2026 - required_annual
  - late_penalty_20_days: installment * 0.02
expected:
  current_test: 7200.00
  required_annual: 5000.00
  installment: 1250.00
  balance_with_return: 3000.00
  late_penalty_20_days: 25.00
```

## When to refuse or refer

| Code | Situation | Action |
| --- | --- | --- |
| R-ES-NR | Part-year resident or nonresident | Refer: Schedule NR allocation changes the estimate |
| R-ES-ENTITY | Partnership, S corporation or corporation | Use `il-pprt`; individuals' vouchers are not used by IL-1065, IL-1120 or IL-1120-ST filers |
| R-ES-ABATE | Penalty abatement request | Refer |
| R-ES-AUDIT | Estimates after an audit adjustment | Refer |

## Filing and payment

Pay through MyTax Illinois (mytax.illinois.gov, needs the IL-PIN), by credit card (a provider fee applies) or by electronic funds transfer after Form EFT-1; otherwise mail the IL-1040-ES voucher with a check showing the Social Security number, "2026" and "IL-1040-ES" (2026 Form IL-1040-ES). Record each payment; it is claimed on the 2026 Form IL-1040, due 15 April 2027. Compute any penalty, or claim the annualized method, on Form IL-2210 with the return.

## Completion checklist

- Worksheet run with the 2026 exemption of $2,925 (not $2,850).
- $1,000 test applied after withholding and all credits.
- Required annual payment taken as the lesser of 90% of 2026 and 100% of 2025 (no 110%).
- Due dates: 15 April, 15 June, 15 September 2026 and 15 January 2027.
- Annualized method considered for uneven income.
- Exceptions checked: farmer, nursing home, no 2025 filing requirement.

## Sources

| Source | URL | Read on |
| --- | --- | --- |
| 35 ILCS 5/803 (Illinois General Assembly). Read for (a) the $1,000 individual and $400 corporate thresholds and the exclusion of partnerships, S corporations and farmers, (c) joint payments, (d) the four installment dates, (e) farmers, (g) fiscal years. | https://www.ilga.gov/legislation/ilcs/fulltext.asp?DocName=003500050K803 | 2026-11-13 |
| 35 ILCS 5/804. Read for (a) the penalty at the Uniform Penalty and Interest Act rate, (c)(1) 25%, 90% and 100%, (c)(2) the annualized percentages, (d) the exceptions. | https://www.ilga.gov/legislation/ilcs/fulltext.asp?DocName=003500050K804 | 2026-11-13 |
| 2026 Form IL-1040-ES. Read for the more-than-$1,000 test, the 2026 due dates, the worksheet lines 1 to 11, the exceptions and the payment options. | https://tax.illinois.gov/content/dam/soi/en/web/tax/forms/incometax/documents/currentyear/individual/il-1040-es.pdf | 2026-11-13 |
| IDOR Publication 105 (December 2025). Read for the 2% and 10% penalty, the weekend rule and the application of payments. | https://tax.illinois.gov/research/publications/pubs/illinois-estimated-payments-requirements-for-individuals-and-businesses.html | 2026-11-13 |
| IDOR Informational Bulletin FY 2026-15. Read for the 2026 exemption of $2,925 and the 90% and 100% statement for 2026 estimates. | https://tax.illinois.gov/research/publications/bulletins/fy-2026-15.html | 2026-11-13 |

Illinois sites refused direct connections from this machine; every page above was read through a Firecrawl fetch of the official URL on 2026-11-13.

Not yet confirmed: the 2026 Form IL-2210 and its instructions (not read); the interest charged on unpaid tax under the Uniform Penalty and Interest Act for 2026 (not read here); whether part-year residents estimate only on income while resident (the old file marked this "unsure", and it was not checked).
