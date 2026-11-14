---
name: nyc-ubt
description: "Compute and file the New York City unincorporated business tax (UBT) for a sole proprietor or a single-member LLC owned by an individual, tax year 2026 (2025-2026 filing cycle forms). Covers the filing test (gross income from all business over $95,000), Form NYC-202 Schedule A line by line, the allowance for the owner's services (20% or $10,000), the $5,000 exemption, the 4% rate, the business tax credit that wipes out a tax of $3,400 or less and phases out at $5,400, Form NYC-202S eligibility, NYC-5UBTI estimated payments, the NYC-EXT extension, and the Form IT-219 credit a New York City resident takes against city income tax (100% falling to 23%). Trigger on \"NYC UBT\", \"unincorporated business tax\", \"NYC-202\", \"NYC-202S\", \"NYC-5UBTI\", \"IT-219\", \"freelancer in New York City tax\". Partnerships, corporations and business allocation are referred."
license: "AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)"
metadata:
  source: openaccountants
  openaccountants_url: "https://www.openaccountants.com/skills/nyc-ubt"
  jurisdiction: "US-NY"
  tax_year: "2026"
  last_updated: "2026-11-13"
---

# New York City unincorporated business tax (UBT) for individuals, tax year 2026

> **Source-cited draft.** Built from the NYC Department of Finance UBT page, the 2025 Form NYC-202 and its instructions, the 2025 Form NYC-202S instructions, the 2026 Form NYC-5UBTI and the 2025 Form IT-219 instructions, read on 2026-11-13. No accountant has reviewed it. All outputs must be reviewed by a qualified tax professional before filing.

**Answer first.** An individual or single-member LLC carrying on a business wholly or partly in New York City must file Form NYC-202 (or NYC-202S) when total gross income from all business, wherever carried on, is more than **$95,000**. The tax is **4%** of taxable income after an allowance for the owner's services (the lower of 20% of income or **$10,000**) and a **$5,000** exemption. A business tax credit removes the whole tax if it is **$3,400** or less, part of it up to **$5,400**, and none above. A New York City resident then takes a credit on Form IT-219 against city income tax: 100% of the UBT at city taxable income of $42,000 or less, falling to 23% at $142,000 or more.

The 2026 Form NYC-202 is not published yet. The rate and the credit thresholds were the same on the 2025 return and the 2026 estimated tax form ([Form NYC-5UBTI (2026)](https://www.nyc.gov/assets/finance/downloads/pdf/26pdf/business_tax_forms/nyc-5ubti_2026.pdf)). Line numbers below are from the 2025 Form NYC-202, the 2025-2026 filing cycle.

## Scope and who this is for

In scope: an individual (sole proprietor) or a single-member LLC disregarded for federal tax and owned by an individual, with a trade, business, profession or occupation carried on wholly or partly in New York City; Form NYC-202 and NYC-202S; estimated UBT on Form NYC-5UBTI; the extension on Form NYC-EXT; the Form IT-219 credit on the owner's New York City resident return.

Out of scope, and where it goes:

| Topic | Skill |
| --- | --- |
| The owner's New York State and New York City resident return (Form IT-201, where the IT-219 credit lands) | `ny-it-201-resident-return` |
| New York State estimated income tax | `ny-estimated-tax` |
| Schedule C net profit and self-employment tax | `us-schedule-c-and-se-computation` |
| The MCTMT on self-employment earnings | `ny-mctmt` |
| Partnerships and multi-member LLCs (Form NYC-204) | refer (see "When to refuse or refer") |

## Ask the client first

1. **Where is the work done?** A home office in one of the five boroughs puts the business in the city. Work done both inside and outside the city needs a business allocation (Schedule C of Form NYC-202), which this skill refers.
2. **Total gross income from all business for 2026**, before cost of goods sold or services: this decides whether a return is due at all.
3. **Net profit** from every federal Schedule C, and whether the client runs more than one business (all are combined on one return, with one exemption).
4. **Was UBT, or any income tax, deducted on the federal Schedule C?** It is added back.
5. **Was the business carried on for the whole year?** A short year prorates the exemption.
6. **Is the client a New York City resident**, and what is their city taxable income? That sets the IT-219 credit.

## The method, step by step

### Rates, bands and thresholds

| Item | Amount, 2026 | Source |
| --- | --- | --- |
| Rate on taxable income allocated to the city | 4% | [NYC DOF, Unincorporated business tax](https://www.nyc.gov/site/finance/business/business-unincorporated-business-tax-ubt.page) |
| Filing test: total gross income from all business, wherever carried on, more than | $95,000 | [NYC-202 instructions (2025), Who must file](https://www.nyc.gov/assets/finance/downloads/pdf/25pdf/business_tax_forms/nyc-202-instr_2025.pdf) |
| Allowance for the taxpayer's services: the lower of | 20% of line 12 or $10,000 | [NYC-202 instructions (2025), line 13](https://www.nyc.gov/assets/finance/downloads/pdf/25pdf/business_tax_forms/nyc-202-instr_2025.pdf) |
| Exemption (one per taxpayer, however many businesses) | $5,000 | [NYC-202 instructions (2025), line 15](https://www.nyc.gov/assets/finance/downloads/pdf/25pdf/business_tax_forms/nyc-202-instr_2025.pdf) |
| Short-year exemption proration | $416.67 per whole month or $13.70 per day | [NYC-202 instructions (2025), line 15](https://www.nyc.gov/assets/finance/downloads/pdf/25pdf/business_tax_forms/nyc-202-instr_2025.pdf) |
| Business tax credit: full credit when the tax is | $3,400 or less | [Form NYC-5UBTI (2026), line 5a](https://www.nyc.gov/assets/finance/downloads/pdf/26pdf/business_tax_forms/nyc-5ubti_2026.pdf) |
| Business tax credit: none when the tax is | $5,400 or more | [Form NYC-5UBTI (2026), line 5a](https://www.nyc.gov/assets/finance/downloads/pdf/26pdf/business_tax_forms/nyc-5ubti_2026.pdf) |
| Business tax credit between the two | tax x ($5,400 minus tax) / $2,000 | [Form NYC-5UBTI (2026), line 5a](https://www.nyc.gov/assets/finance/downloads/pdf/26pdf/business_tax_forms/nyc-5ubti_2026.pdf) |
| Estimated tax declaration required if 2026 UBT is expected to exceed | $3,400 | [Form NYC-5UBTI (2026), Who must make a declaration](https://www.nyc.gov/assets/finance/downloads/pdf/26pdf/business_tax_forms/nyc-5ubti_2026.pdf) |
| IT-219 credit: city taxable income $42,000 or less | 100% of the UBT | [IT-219-I (2025)](https://www.tax.ny.gov/pdf/current_forms/it/it219i.pdf) |
| IT-219 credit: city taxable income $142,000 or more | 23% of the UBT | [IT-219-I (2025)](https://www.tax.ny.gov/pdf/current_forms/it/it219i.pdf) |
| IT-219 credit in between | 1 minus ((city taxable income minus $42,000) / $100,000, rounded to 3 decimals) x 0.770 | [Form IT-219 (2025), Worksheet B](https://www.tax.ny.gov/pdf/current_forms/it/it219_fill_in.pdf) |

None of these amounts is indexed for inflation.

### Step 1: does the tax apply?

1. The UBT applies to trades, professions and certain occupations of an individual, partnership, LLC, fiduciary, association, estate or trust, active or being liquidated ([NYC DOF UBT page](https://www.nyc.gov/site/finance/business/business-unincorporated-business-tax-ubt.page)).
2. Not subject: a person performing services as an employee; a person (other than a dealer) only buying, holding and selling property for their own account; an owner, lessee or fiduciary holding, leasing or managing real property for their own account ([NYC DOF UBT page](https://www.nyc.gov/site/finance/business/business-unincorporated-business-tax-ubt.page)). S corporations and entities taxed as corporations pay the city corporate taxes instead.
3. Two or more unincorporated businesses of the same person are treated as one; their income and deductions go on one return ([NYC DOF UBT page](https://www.nyc.gov/site/finance/business/business-unincorporated-business-tax-ubt.page); [NYC-202S instructions (2025)](https://www.nyc.gov/assets/finance/downloads/pdf/25pdf/business_tax_forms/nyc-202s-instr_2025.pdf)).
4. File if total gross income from all business, wherever carried on, is more than $95,000, before any deduction for cost of goods sold or services performed. Individuals file Form NYC-202 or NYC-202S; a single-member LLC files Form NYC-202 ([NYC-202 instructions (2025)](https://www.nyc.gov/assets/finance/downloads/pdf/25pdf/business_tax_forms/nyc-202-instr_2025.pdf)). Gross income of $95,000 or less: no return, whatever the profit.

### Step 2: Schedule B, business income (Form NYC-202, page 3)

5. Part 1 starts from the federal net profit or loss from business (Schedule C or F, line 1), plus gains on business property, business rental or royalty income and other business income (lines 3 to 5). Line 7 takes out net income or gain from rental, sale or exchange of real property where the instructions say so ([Form NYC-202 (2025)](https://www.nyc.gov/assets/finance/downloads/pdf/25pdf/business_tax_forms/nyc-202_2025.pdf)).
6. Additions (Part 2): line 9 adds back all income taxes and unincorporated business taxes deducted federally, so a UBT payment deducted on Schedule C comes back here; line 10c adds depreciation adjustments (Forms NYC-399 and NYC-399Z); line 11 other additions. Subtractions (Part 3): line 13 income tax and UBT refunds included in Part 1; line 15 the replacement depreciation ([Form NYC-202 (2025)](https://www.nyc.gov/assets/finance/downloads/pdf/25pdf/business_tax_forms/nyc-202_2025.pdf)).
7. Amounts paid to the proprietor (salaries, wages, withdrawals, interest) and pension contributions for the proprietor are not business deductions; a client who took one federally cannot use Form NYC-202S and must adjust on Form NYC-202 ([NYC-202S instructions (2025), eligibility item 8](https://www.nyc.gov/assets/finance/downloads/pdf/25pdf/business_tax_forms/nyc-202s-instr_2025.pdf)).
8. The total is Schedule B line 27, business income, carried to Schedule A line 1. Investment income (Schedule B line 26) goes to line 7.

### Step 3: Schedule A, the tax (Form NYC-202, page 1)

9. Line 1 business income. Lines 3 to 6: if the business allocation percentage is under 100%, allocate (refer, see below); a business wholly in the city keeps 100%.
10. Line 10 total before the net operating loss deduction; line 11 the NYC NOL deduction from Form NYC-NOLD-UBTI. Losses from years beginning on or after 1 January 2018 are limited to 80% of New York City taxable income and cannot be carried back ([NYC-202 instructions (2025), line 10](https://www.nyc.gov/assets/finance/downloads/pdf/25pdf/business_tax_forms/nyc-202-instr_2025.pdf)).
11. Line 12, balance. **Line 13, allowance for the taxpayer's services:** the lower of 20% of line 12 or $10,000; zero if line 12 is a loss.
12. Line 14 = line 12 minus line 13. **Line 15, exemption:** $5,000, prorated for a short year ($416.67 per whole month, or $13.70 per day).
13. Line 16, taxable income = line 14 minus line 15. **Line 17, tax** = 4% of line 16.
14. **Line 18, business tax credit:** the whole of line 17 if it is $3,400 or less; nothing if it is $5,400 or more; in between, line 17 x ($5,400 minus line 17) / $2,000 ([NYC-202 instructions (2025), line 18](https://www.nyc.gov/assets/finance/downloads/pdf/25pdf/business_tax_forms/nyc-202-instr_2025.pdf)).
15. **Line 19, unincorporated business tax** = line 17 minus line 18. Then the other credits (lines 20a to 20g: REAP, real estate tax escalation and IBZ, LMREAP, biotechnology, beer production, child care, relocation), estimated payments (line 22) and the balance or overpayment.

### Step 4: the resident's credit on Form IT-219

16. A New York City resident sole proprietor takes a credit against city personal income tax for part of the UBT: Form IT-219, using the UBT from Form NYC-202 line 21 or Form NYC-202S line 8, and city taxable income from Form IT-201 line 47. A joint return uses the couple's joint city taxable income ([IT-219-I (2025)](https://www.tax.ny.gov/pdf/current_forms/it/it219i.pdf)).
17. The percentage is 100% at city taxable income of $42,000 or less, 23% at $142,000 or more, and in between 1.000 minus (the excess over $42,000 divided by $100,000, rounded to three decimals) x 0.770 ([Form IT-219 (2025), Worksheet B](https://www.tax.ny.gov/pdf/current_forms/it/it219_fill_in.pdf)).
18. The credit cannot exceed the city tax less the city household credit; any unused part is not refunded or carried over. It goes to Form IT-201-ATT line 8 and on to Form IT-201 line 53 (see `ny-it-201-resident-return`). Part-year residents receive a partial credit ([NYC DOF UBT page](https://www.nyc.gov/site/finance/business/business-unincorporated-business-tax-ubt.page)).

## Boundary and exception table

| Situation | Treatment |
| --- | --- |
| Gross income from all business $95,000 or less | No UBT return, even with a large profit |
| Gross income over $95,000 but tax on line 17 of $3,400 or less | File; the business tax credit makes the tax zero |
| More than one business | One return, income combined, one $5,000 exemption |
| Business carried on for part of the year | Prorate the $5,000 exemption (whole months at $416.67, otherwise $13.70 a day) |
| UBT deducted on the federal Schedule C | Add back on Schedule B line 9; on the state return add back with code A-201 (`ny-it-201-resident-return`) |
| MCTMT paid | Does not need to be added back on the UBT return ([NYC DOF UBT page](https://www.nyc.gov/site/finance/business/business-unincorporated-business-tax-ubt.page)) |
| Freelancer working from a home office in the city | The business is carried on in the city; all its income is city income unless there is a real place of business outside |
| Clients in the city but all work done outside it | Not carried on in the city on that fact alone; refer if there is any city office or regular city work |
| Employee income (W-2) | Not subject |
| Owning and renting out a two-family house for one's own account | Not subject |
| Hobby with no profit motive | Not a business; follow the federal characterization and flag |
| Client is not a city resident | Owes UBT on city business, but has no city income tax and no IT-219 credit |

### Who may use Form NYC-202S

An individual may file the shorter Form NYC-202S only if all of these hold ([NYC-202S instructions (2025)](https://www.nyc.gov/assets/finance/downloads/pdf/25pdf/business_tax_forms/nyc-202s-instr_2025.pdf)): no business allocation; no investment capital or income during the year; no change to the federal depreciation deduction; no penalty for underpaying estimated tax; filed by the due date (with extensions) with no late filing or payment penalty; no credits other than the business tax credit; no NOL deduction; no deduction federally for salaries, wages, withdrawals or interest paid to the proprietor or for pension contributions for the proprietor; no partial exemption for holding, leasing and managing real property; no New York City modifications other than adding back income and UBT taxes deducted federally; no disallowed business interest under IRC 163(j); and no income under IRC 951A or 965. A single-member LLC always uses Form NYC-202. The older version of this skill said Form NYC-202S was for gross income of $250,000 or less with no employees, vehicles or depreciation; the instructions contain no such test.

### Defaults when a fact is missing

| Missing fact | Default, and flag it |
| --- | --- |
| Total gross income | Ask: it decides whether any return is due |
| Where the work is done | Assume all in the city if the client lives and works in the city; refer if there is an outside office |
| Whether UBT was deducted federally | Check Schedule C taxes and licenses; add back what is there |
| City taxable income for IT-219 | Take Form IT-201 line 47; do not estimate the credit without it |
| Prior-year UBT for estimates | Ask for the 2025 Form NYC-202 |

## Worked cases

The clients are invented. The rates and thresholds are from the sources above.

**Case 1, a Brooklyn freelancer who pays UBT and claims the IT-219 credit.** A single designer works from a home office in Brooklyn. 2026 gross receipts USD 150,000, Schedule C net profit USD 110,000, no UBT deducted federally, no other business, whole year. City taxable income on Form IT-201 line 47 is USD 120,000.

Line 12 USD 110,000. Line 13: 20% is USD 22,000, so the USD 10,000 cap applies. Line 14 USD 100,000; less the USD 5,000 exemption, line 16 is USD 95,000. Line 17: 4% = USD 3,800. That is over USD 3,400 and under USD 5,400, so line 18 = 3,800 x (5,400 minus 3,800) / 2,000 = USD 3,040. Line 19 UBT: USD 760. On Form IT-219: (120,000 minus 42,000) / 100,000 = 0.780; 0.780 x 0.770 = 0.6006; the percentage is 0.3994, and the credit is USD 760 x 0.3994 = USD 303.54, well under her 2026 city tax of USD 4,526.20 (single rate schedule, [IT-2105-I (2026)](https://www.tax.ny.gov/pdf/current_forms/it/it2105i.pdf)).

```oa-check
name: NYC UBT and IT-219 credit, Brooklyn freelancer (2026)
inputs:
  net_profit: 110000
  city_taxable_income: 120000
steps:
  - allowance: min(net_profit * 0.20, 10000)
  - taxable: net_profit - allowance - 5000
  - tax: taxable * 0.04
  - credit: tax * (5400 - tax) / 2000
  - ubt: tax - credit
  - ratio: round((city_taxable_income - 42000) / 100000, 3)
  - percentage: 1 - ratio * 0.77
  - city_tax: 1813 + 0.03876 * (city_taxable_income - 50000)
  - it219_credit: min(ubt * percentage, city_tax)
expected:
  allowance: 10000
  taxable: 95000
  tax: 3800.00
  credit: 3040.00
  ubt: 760.00
  percentage: 0.3994
  city_tax: 4526.20
  it219_credit: 303.54
```

**Case 2, a decision: must she file, pay, and make estimates?** A Queens consultant has 2026 gross receipts of USD 120,000 and net profit of USD 80,000. Gross income is over USD 95,000, so a return is due. Line 13 USD 10,000 (20% would be USD 16,000); line 16 = 80,000 minus 10,000 minus 5,000 = USD 65,000; line 17 = USD 2,600. That is USD 3,400 or less, so the business tax credit is the whole USD 2,600 and the UBT is zero. Decision: file Form NYC-202S (if every eligibility item holds) or NYC-202 by 15 April 2027; no payment; no 2026 declaration on Form NYC-5UBTI, because the estimated tax does not exceed USD 3,400. Had gross receipts been USD 95,000 or less, no return at all would be due. For comparison, a net profit of USD 250,000 gives line 17 of USD 9,400, no business tax credit, and estimates are required.

```oa-check
name: NYC UBT filing and estimate decision, Queens consultant (2026)
inputs:
  gross_income: 120000
  net_profit: 80000
steps:
  - must_file: min(max(gross_income - 95000, 0), 1)
  - allowance: min(net_profit * 0.20, 10000)
  - tax: (net_profit - allowance - 5000) * 0.04
  - credit: min(tax, 3400)
  - ubt: tax - credit
  - estimates_required: min(max(ubt - 3400, 0), 1)
expected:
  must_file: 1
  allowance: 10000
  tax: 2600.00
  credit: 2600.00
  ubt: 0.00
  estimates_required: 0
```

## When to refuse or refer

| Code | Situation | Action |
| --- | --- | --- |
| R-UBT-ALLOC | Business carried on both inside and outside the city (Schedule C business allocation) | Refer: a fair and equitable allocation is required |
| R-UBT-PART | Partnership or multi-member LLC | Refer: Form NYC-204 |
| R-UBT-CORP | S corporation or entity taxed as a corporation | Refer: city corporate taxes |
| R-UBT-INV | Investment capital or investment income | Refer: Schedule D investment allocation |
| R-UBT-NOL | NYC net operating loss deduction | Refer: Form NYC-NOLD-UBTI and the 80% limit |
| R-UBT-RE | Partial exemption for holding, leasing or managing real property | Refer |
| R-UBT-AMEND | Amended return after an IRS or state change | Refer: due within 90 days of the final determination, with the UBT worksheet |
| R-UBT-OBBBA | A 2025 return with decoupling modifications from Chapter 59 of the Laws of 2026 | Refer: special condition code OB and the DOF worksheet (Finance Memorandum 26-2) |

## Filing and payment

- **Due date:** Form NYC-202 for calendar 2026 is due on or before 15 April 2027 (the 15th day of the fourth month after a fiscal year ends) ([NYC-202 instructions (2025), When to file](https://www.nyc.gov/assets/finance/downloads/pdf/25pdf/business_tax_forms/nyc-202-instr_2025.pdf)).
- **Extension:** an automatic six-month extension needs Form NYC-EXT filed by the due date with the tax properly estimated and paid; a federal or New York State extension does **not** extend the city return ([Form NYC-5UBTI (2026)](https://www.nyc.gov/assets/finance/downloads/pdf/26pdf/business_tax_forms/nyc-5ubti_2026.pdf)). The older version of this skill said the federal extension carried over; that was wrong.
- **Estimated UBT, Form NYC-5UBTI:** required if the 2026 tax is reasonably expected to exceed USD 3,400. Calendar-year installments of one quarter each are due 15 April, 15 June and 15 September 2026 and 15 January 2027. If the requirement arises later, the declaration is due 15 June (one third), 15 September (one half) or 15 January (all). Filing the 2026 return by 16 February 2027 and paying in full removes the 15 January installment ([Form NYC-5UBTI (2026)](https://www.nyc.gov/assets/finance/downloads/pdf/26pdf/business_tax_forms/nyc-5ubti_2026.pdf)).
- **Underpayment:** Form NYC-221 computes any penalty for underpaid estimates. Interest runs from the original due date on late payment ([NYC-202 instructions (2025)](https://www.nyc.gov/assets/finance/downloads/pdf/25pdf/business_tax_forms/nyc-202-instr_2025.pdf)).
- **How:** file and pay through NYC e-Services, or mail declarations to NYC Department of Finance, Unincorporated Business Tax, P.O. Box 3923, New York, NY 10008-3923 ([Form NYC-5UBTI (2026)](https://www.nyc.gov/assets/finance/downloads/pdf/26pdf/business_tax_forms/nyc-5ubti_2026.pdf)).
- **Next:** the UBT paid goes to Form IT-219 on the owner's Form IT-201 (city residents), and any UBT deducted on Schedule C is added back on Form IT-225 with code A-201.

## Completion checklist

- Gross income from all business compared with USD 95,000 before deciding whether a return is due.
- All businesses combined; one USD 5,000 exemption, prorated for a short year.
- Income taxes and UBT deducted federally added back (Schedule B line 9).
- Allowance for services capped at the lower of 20% or USD 10,000.
- Business tax credit computed from line 17 with the USD 3,400 and USD 5,400 tests.
- Form NYC-202S eligibility checked item by item, or Form NYC-202 used.
- NYC-EXT filed if more time is needed; a federal extension does not count.
- NYC-5UBTI estimates set up for 2027 if the tax will exceed USD 3,400.
- IT-219 credit computed from IT-201 line 47 and capped at the city tax.

## Sources

| Source | URL | Read on |
| --- | --- | --- |
| NYC Department of Finance, Unincorporated business tax (UBT). Read for the 4% rate, who is exempt, the $3,400 and $5,400 credit, the resident credit and the MCTMT add-back note. | https://www.nyc.gov/site/finance/business/business-unincorporated-business-tax-ubt.page | 2026-11-13 |
| Instructions for Form NYC-202 (2025). Read for Who must file ($95,000), When to file, line 10 NOL, line 13 ($10,000 or 20%), line 15 ($5,000, $416.67, $13.70), lines 17 to 19 and estimated tax. | https://www.nyc.gov/assets/finance/downloads/pdf/25pdf/business_tax_forms/nyc-202-instr_2025.pdf | 2026-11-13 |
| Form NYC-202 (2025). Read for Schedule A lines 1 to 19 and Schedule B lines 1 to 15. | https://www.nyc.gov/assets/finance/downloads/pdf/25pdf/business_tax_forms/nyc-202_2025.pdf | 2026-11-13 |
| Instructions for Form NYC-202S (2025). Read for the twelve eligibility conditions and combining businesses. | https://www.nyc.gov/assets/finance/downloads/pdf/25pdf/business_tax_forms/nyc-202s-instr_2025.pdf | 2026-11-13 |
| Form NYC-5UBTI (2026). Read for the $3,400 declaration test, the line 5a credit formula, installment dates, the 16 February 2027 rule and the extension caution. | https://www.nyc.gov/assets/finance/downloads/pdf/26pdf/business_tax_forms/nyc-5ubti_2026.pdf | 2026-11-13 |
| IT-219-I (2025). Read for the 100% to 23% credit and the $42,000 and $142,000 points. | https://www.tax.ny.gov/pdf/current_forms/it/it219i.pdf | 2026-11-13 |
| Form IT-219 (2025). Read for Worksheet B and lines 12 to 16. | https://www.tax.ny.gov/pdf/current_forms/it/it219_fill_in.pdf | 2026-11-06 |
| IT-2105-I (2026). Read for the 2026 New York City single rate schedule used in Case 1. | https://www.tax.ny.gov/pdf/current_forms/it/it2105i.pdf | 2026-11-13 |

Not yet confirmed: the 2026 Form NYC-202, NYC-202S and IT-219 and their instructions are not published, so the line numbers, the $95,000 filing test, the $10,000 and 20% allowance, the $5,000 exemption and its proration and the IT-219 Worksheet B formula are the 2025-2026 filing cycle values (the $3,400 and $5,400 credit points and the 4% rate are confirmed on the 2026 Form NYC-5UBTI and the DOF page); the NYC Administrative Code sections themselves (Title 11, Chapter 5) were not read.

## Today's figures and who stands behind this skill

This file is an AI skill (tax rules your AI follows) from OpenAccountants, copied on 2026-11-13. Rates, thresholds and deadlines change. For the current version of this skill, its official sources and the named accountant (if any) who stands behind it, call `get_skill` with slug `nyc-ubt` on the OpenAccountants connector (https://www.openaccountants.com/connect), or read https://www.openaccountants.com/skills/nyc-ubt. If neither is available, confirm every figure against the official source pages cited above before relying on it.
