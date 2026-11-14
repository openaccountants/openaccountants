---
name: mi-detroit-individual-return
description: "Compute a City of Detroit individual income tax return for tax year 2026. Residents pay 2.4% on income from all sources and nonresidents 1.2% on Detroit-source income (City of Detroit rates for 2013 and later), after a $600 exemption per person; pensions, Social Security, unemployment and military pay are not taxed. Covers Form 5118 (resident), Form 5119 (nonresident), Form 5120 (part-year), Form 5121 withholding schedule, the days-worked allocation for nonresident wages, the home-working rule, the credit for tax paid to another city and the $100 estimate threshold. Trigger on \"Detroit income tax\", \"City of Detroit return\", \"Form 5118\", \"Form 5119\", \"Form 5120\", \"Form 5121\", \"days worked in Detroit\", \"Detroit nonresident\", \"Detroit estimated tax\". Returns are administered by Michigan Treasury."
license: "AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)"
metadata:
  source: openaccountants
  openaccountants_url: "https://www.openaccountants.com/skills/mi-detroit-individual-return"
  jurisdiction: "US-MI"
  tax_year: "2026"
  last_updated: "2026-11-13"
---

# City of Detroit individual income tax, tax year 2026

> **Source-cited draft.** Built from the City of Detroit Income Tax Information page, the 2025 Form 5118 and 5120 line-by-line instructions issued by Michigan Treasury, and the Michigan Treasury city income tax pages, read on 2026-11-13. The 2026 Detroit forms were not yet published. No accountant has reviewed it. All outputs must be reviewed by a qualified tax professional before filing.

**Answer first.** Detroit taxes its residents at **2.4%** of income from all sources and nonresidents at **1.2%** of income earned in Detroit. Each person and dependent gets a **$600** exemption. Pensions and annuities, Social Security, unemployment compensation, military pay, gifts and inheritances are not taxed. Michigan Treasury administers the tax: residents file Form 5118, nonresidents Form 5119, part-year residents Form 5120, with Form 5121 for any city withholding. A nonresident allocates wages by days actually worked in Detroit; working at home "for convenience" does not count as working outside the city unless documented with an employer letter and a work log. If more than $100 is expected to be owed, estimated payments are needed.

## Scope and who this is for

In scope: individuals (and married couples) with a 2026 Detroit filing obligation: residents of the City of Detroit, nonresidents who work or do business in Detroit, and part-year residents.

Out of scope, and where it goes:

| Topic | Skill |
| --- | --- |
| The Michigan state return (MI-1040) | `mi-income-tax` |
| Detroit corporate income tax, partnerships and fiduciaries | Refused here (see refusals) |
| Employer withholding of Detroit tax | `mi-payroll` |
| Other Michigan cities (Hamtramck, Highland Park, Grand Rapids, Lansing and others) | Refused: each city has its own forms |
| Federal return | the federal skills |

## Ask the client first

1. **Street address for every day of 2026.** Residency is by the city boundary, not ZIP code or "metro Detroit". Hamtramck and Highland Park are separate cities inside Detroit's borders.
2. **Did the client move in or out of Detroit in 2026?** If so, the move date: Form 5120.
3. **For each W-2: the city wages and city tax withheld** (W-2 boxes 18 and 19) and the work location.
4. **Nonresidents: total days worked in 2026 and days physically worked in Detroit**, with an employer letter and a work log or calendar.
5. **Schedule C or partnership income:** where the work was physically done, and the business's Detroit factors.
6. **Retirement, Social Security, unemployment and military pay** amounts (they are subtracted).
7. **Income tax paid to another Michigan city** on the same income, and the other city's return.
8. **2026 Detroit estimated payments** (Form 5123) and any credit carried forward.

## The method, step by step

### Rates, bands and thresholds

| Item | Amount | Source |
| --- | --- | --- |
| Resident individuals | 2.4% | [City of Detroit Income Tax Information (rates for 2013 and later)](https://detroitmi.gov/departments/office-chief-financial-officer/ocfo-divisions/office-treasury/income-tax/income-tax-information) |
| Nonresident individuals | 1.2% | [City of Detroit Income Tax Information](https://detroitmi.gov/departments/office-chief-financial-officer/ocfo-divisions/office-treasury/income-tax/income-tax-information) |
| Corporations (not covered here) | 2.0% | [City of Detroit Income Tax Information](https://detroitmi.gov/departments/office-chief-financial-officer/ocfo-divisions/office-treasury/income-tax/income-tax-information) |
| Personal exemption, each person and dependent (not indexed; $600 since tax year 2005) | $600 | [City of Detroit Income Tax Information](https://detroitmi.gov/departments/office-chief-financial-officer/ocfo-divisions/office-treasury/income-tax/income-tax-information) |
| A person who can be claimed as a dependent: no tax if taxable income is under | $600 (at $600 or more, tax on the full amount) | [2025 Form 5118 instructions, line 6](https://www.michigan.gov/taxes/-/media/Project/Websites/taxes/Forms/City-IIT/TY2025/5118-Instr.pdf) |
| Estimated payments typically required if more than this is owed | $100 | [2025 Form 5118 instructions, line 22d](https://www.michigan.gov/taxes/-/media/Project/Websites/taxes/Forms/City-IIT/TY2025/5118-Instr.pdf) |
| Late payment interest, through 30 June 2026 (1 point above the adjusted prime rate, reset 1 January and 1 July) | 8.48% a year (0.0002324 daily) | [2025 Form 5118 instructions, line 22b](https://www.michigan.gov/taxes/-/media/Project/Websites/taxes/Forms/City-IIT/TY2025/5118-Instr.pdf) |
| Late payment penalty | 1% of the tax due for the first month, rising by 1% each further month (a part month counts as a month) | [2025 Form 5118 instructions, line 22c](https://www.michigan.gov/taxes/-/media/Project/Websites/taxes/Forms/City-IIT/TY2025/5118-Instr.pdf) |
| Balance below which no payment is required (the return is still filed) | $1 | [2025 Form 5118 instructions, line 22e](https://www.michigan.gov/taxes/-/media/Project/Websites/taxes/Forms/City-IIT/TY2025/5118-Instr.pdf) |

Additional exemptions on line 8 of Form 5118: one for age 65 or older (taxpayer and spouse only), and one each for being deaf, blind, or totally and permanently disabled (a person who was 66 by 28 February of the filing year cannot claim the disability one). Source: [2025 Form 5118 instructions, line 8](https://www.michigan.gov/taxes/-/media/Project/Websites/taxes/Forms/City-IIT/TY2025/5118-Instr.pdf).

### What Detroit taxes and does not tax

Taxed (2025 Form 5118 instructions, Part 1): compensation; net profits of an unincorporated business, profession or other activity; dividends, interest, capital gains less capital losses, income from estates and trusts, and net rental profits.

Not taxed: gifts, inheritances and bequests; pensions and annuities, including disability pensions (pre-retirement distributions **are** taxed); insurance proceeds; unemployment compensation, welfare relief and supplemental unemployment benefits; worker's compensation; interest on obligations of the United States and the states; military pay of the Armed Forces and National Guard; Social Security.

### Form 5118, resident: the computation

1. **Start from federal AGI.**
2. **Additions (Part 4, line 28 and related):** city income tax paid by partnerships, S corporations, estates or trusts on the taxpayer's behalf; S corporation losses included in AGI; deductions Detroit does not allow that reduced AGI, including the health savings account or Archer MSA deduction, the penalty on early withdrawal of savings and the student loan interest deduction; a federal net operating loss deduction.
3. **Subtractions (Part 5):** line 30 pension, annuity and other retirement benefits in AGI (not early distributions); line 31 taxable Social Security; line 32 U.S. government interest; line 33 state and city income tax refunds and homestead credit refunds in AGI; line 34 unemployment benefits; line 35 Renaissance Zone deduction (with the City's approval letter); line 36 other subtractions: S corporation income in AGI, armed forces compensation, recoveries of prior-year itemized deductions, unreimbursed employee travel, meals, lodging, transportation and outside salesperson expenses (other employee business expenses are not deductible), and the part of a gain that accrued before 1 July 1962.
4. **Exemptions:** number of exemptions times $600.
5. **Tax** = (income after adjustments - exemptions) times 2.4%.
6. **Credit for tax paid to another city (line 20):** the tax actually paid to another city on income earned there while a Detroit resident, but **no more than the tax a Detroit nonresident would pay on the same income** (1.2% of it).
7. **Payments:** city withholding from Form 5121 (W-2s are no longer accepted; without Form 5121 the withholding credit may be denied), Form 5123 estimates, extension payments, tax paid by partnerships.
8. **Balance or refund**, plus interest, penalty and the Form 5338 estimate penalty if any.

Source for steps 1 to 8: [2025 Form 5118 instructions](https://www.michigan.gov/taxes/-/media/Project/Websites/taxes/Forms/City-IIT/TY2025/5118-Instr.pdf).

### Form 5119, nonresident: Detroit-source income only

1. **Wages:** a nonresident who works partly outside Detroit allocates by days. Detroit wages = total wages times (days actually worked in Detroit divided by total days actually worked). Vacation, holiday and sick days are not working days.
2. **Documentation:** a nonresident allocating less than 100% must provide a letter from the employer on its letterhead verifying the days (with the signer's name, title and phone number) and a work log of days in and out of Detroit. Without them the return is sent back and the refund delayed. Source: [City of Detroit Income Tax Information](https://detroitmi.gov/departments/office-chief-financial-officer/ocfo-divisions/office-treasury/income-tax/income-tax-information).
3. **Working at home:** "The mere fact that a non-resident employee takes work home with him and performs such work at his home does not permit allocation of compensation" (Regulation 13.2 of the City Income Tax Ordinance, quoted on the City's page). Days the person was scheduled to work, and did work, a full day at a home outside Detroit are days outside Detroit; evening and weekend work at home on a Detroit day is not.
4. **Business income:** net profit from a business is apportioned to Detroit by the business's own factors; only the Detroit share is taxed at 1.2%.
5. **Not Detroit-source for a nonresident:** interest, dividends and gains on stocks and other intangibles; rental income from property outside Detroit.
6. **Rate:** Detroit-source income after exemptions times 1.2%.

### Form 5120, part-year resident

Income received while a resident is taxed at 2.4% on the resident rules; Detroit-source income received while a nonresident is taxed at 1.2% on the nonresident rules. Use the actual move date. Source: [2025 Form 5120 line instructions](https://www.michigan.gov/taxes/-/media/Project/Websites/taxes/Forms/City-IIT/TY2025/5119-Instr.pdf).

## Boundary and exception table

| Situation | Treatment |
| --- | --- |
| Retired Detroit resident with pension, IRA and Social Security only | No Detroit tax on those; interest and dividends are still taxed |
| IRA or 401(k) distribution before retirement (early distribution) | Taxed |
| Resident employee of a Detroit firm, all days in Detroit | 2.4% of wages less exemptions |
| Nonresident, 100% of days in Detroit | 1.2% of all the wages |
| Nonresident, regular full days worked at home outside Detroit, documented | Those days are outside Detroit |
| Nonresident who only takes work home in the evening | No allocation (Regulation 13.2) |
| Resident who works in another taxing city | Credit up to 1.2% of that income |
| Married couple, one Detroit resident and one not | Each files on their own status: 5118 for the resident, 5119 for the nonresident if they have Detroit income |
| Renaissance Zone resident | Deduction on line 35 with the City approval letter |
| S corporation shareholder | S corporation income is subtracted and losses added back on the individual return |

### Defaults when a fact is missing

| Missing fact | Default, and flag it |
| --- | --- |
| Days worked in Detroit (nonresident) | 100% Detroit until an employer letter and work log are produced |
| Exact address boundary | Ask; check the parcel against the city boundary |
| Form 5121 detail | Do not claim city withholding without it |
| Move date (part-year) | Ask; do not split income without it |

### Red flags to raise with the client

| Flag | Why it matters |
| --- | --- |
| W-2 shows Detroit withholding but the client says they worked mostly from home | Allocation needs the employer letter and log |
| A Detroit resident's W-2 shows no Detroit withholding | Tax will be due with the return; estimates if over $100 |
| Hamtramck or Highland Park address | Not Detroit: a different city |
| Large interest or dividend income for a retired resident | Still taxed by Detroit, even though the pension is not |

## Worked cases

**Case 1, resident with wages, a side business and a pension.** A married Detroit resident couple: wages $60,000, Schedule C net profit $20,000, bank interest $1,000, and a $15,000 pension (subtracted on line 30). Two exemptions: $1,200. Income subject to tax $60,000 + $20,000 + $1,000 - $1,200 = $79,800. Tax at 2.4%: $1,915.20. The pension adds nothing.

```oa-check
name: Detroit 2026 resident, wages, Schedule C, interest, pension excluded
inputs:
  wages: 60000
  schedule_c: 20000
  interest: 1000
  pension: 15000
  exemptions: 2
  exemption_amount: 600
  resident_rate: 0.024
steps:
  - agi: wages + schedule_c + interest + pension
  - taxable: max(agi - pension - exemptions * exemption_amount, 0)
  - tax: taxable * resident_rate
expected:
  taxable: 79800
  tax: 1915.20
```

**Case 2, a decision: how much credit for tax paid to another city?** A single Detroit resident earns $50,000 of wages working in another Michigan city that taxes nonresidents. Detroit tax before credit: ($50,000 - $600) x 2.4% = $1,185.60. The credit is the lesser of the other city's tax actually paid and what a Detroit nonresident would pay on the same income ($50,000 x 1.2% = $600). If the other city's return shows $250 paid, the credit is $250 and Detroit tax is $935.60. If it shows $800, the credit stops at $600 and Detroit tax is $585.60. Ask for the other city's return before choosing the figure.

```oa-check
name: Detroit 2026 resident, credit for tax paid to another city, both cases
inputs:
  wages: 50000
  exemption_amount: 600
  resident_rate: 0.024
  nonresident_rate: 0.012
  other_city_tax_low: 250
  other_city_tax_high: 800
steps:
  - tax_before_credit: (wages - exemption_amount) * resident_rate
  - credit_cap: wages * nonresident_rate
  - tax_after_low: tax_before_credit - min(other_city_tax_low, credit_cap)
  - tax_after_high: tax_before_credit - min(other_city_tax_high, credit_cap)
expected:
  tax_before_credit: 1185.60
  credit_cap: 600
  tax_after_low: 935.60
  tax_after_high: 585.60
```

## When to refuse or refer

| Code | Situation | Action |
| --- | --- | --- |
| DET-R-01 | Income also sourced to another state | Refuse: multistate work |
| DET-R-02 | Partnership or S corporation with activity in several Michigan cities | Refuse: entity-level apportionment |
| DET-R-03 | Detroit corporate income tax return | Refuse: individual skill only |
| DET-R-04 | Amended Detroit return | Refer |
| DET-R-05 | Gambling winnings of a nonresident at a Detroit casino | Refer: not confirmed in this review |
| DET-R-06 | Renaissance Zone qualification dispute or phase-out year | Refer to the City and a reviewer |
| DET-R-07 | Estate or trust Detroit return | Refuse |
| DET-R-08 | Hamtramck, Highland Park or another city's return | Refuse: different city and forms |
| DET-R-09 | A tax year other than 2026 | Refuse: check the year's forms |
| DET-R-10 | A Detroit employer applying a "convenience of the employer" rule to a remote worker outside Detroit | Refuse to apply it: Detroit allocates by days worked; flag the withholding |
| DET-R-11 | Residency dispute (two homes, boundary question) | Refer with the documents |
| DET-R-12 | Nonresident business apportionment where the business's Detroit factors are not available | Refer |

## Filing and payment

| Step | What to do |
| --- | --- |
| 1. Form | Resident 5118; nonresident 5119; part-year 5120. Attach Form 5121 for all city withholding (Form 5253 if more than eight W-2s or three partnerships). |
| 2. File | Electronically through approved software (Treasury's city e-file) or on paper to the addresses on the form; paper forms are read by machine: black or blue ink, capital letters, whole dollars. |
| 3. Pay | Balance due with the return; under $1 nothing to pay. Interest at 8.48% to 30 June 2026 and penalty as in the table. |
| 4. Estimates | Form 5123 vouchers for 2027 if more than $100 is expected to be owed; Form 5338 computes the underpayment penalty, or Treasury bills it. |
| 5. Due date | 15 April 2027 for calendar 2026 (see Not yet confirmed). |

Source: [2025 Form 5118 instructions](https://www.michigan.gov/taxes/-/media/Project/Websites/taxes/Forms/City-IIT/TY2025/5118-Instr.pdf); [2025 City Individual Income Tax Forms](https://www.michigan.gov/taxes/citytax/detroit/forms/2025/2025-city-individual-income-tax-forms).

### Form map

| Form | What it covers |
| --- | --- |
| 5118 | Resident return |
| 5119 | Nonresident return |
| 5120 | Part-year resident return |
| 5121 | City withholding schedule (required to claim withholding) |
| 5253 | Continuation schedule |
| 5123 | Estimated tax voucher |
| 5338 | Underpayment of estimated tax |
| 5209 | Application for extension (see Not yet confirmed) |

## Completion checklist

- Residency checked against the city boundary by street address.
- Right form for the residency history.
- Form 5121 completed for every W-2 with city withholding.
- Nonresident allocation below 100% backed by an employer letter and a work log.
- Pensions, Social Security, unemployment and military pay subtracted; early retirement distributions left in.
- HSA, student loan interest and early withdrawal penalty added back.
- $600 per exemption, plus age 65 and disability exemptions.
- Other-city credit capped at 1.2% of that income.
- Estimates set for 2027 if more than $100 will be owed.

## Sources

| Source | URL | Read on |
| --- | --- | --- |
| City of Detroit, Income Tax Information. Read for the rates for 2013 and later (2.4%, 1.2%, 2.0%), the $600 exemption, the nonresident documentation and Regulation 13.2. | https://detroitmi.gov/departments/office-chief-financial-officer/ocfo-divisions/office-treasury/income-tax/income-tax-information | 2026-11-13 |
| 2025 Form 5118 line-by-line instructions (Michigan Treasury). Read for what is taxed and not taxed, the additions and subtractions, line 8 exemptions, line 20 credit cap, Form 5121, interest of 8.48% to 30 June 2026, the penalty and the $100 estimate threshold. | https://www.michigan.gov/taxes/-/media/Project/Websites/taxes/Forms/City-IIT/TY2025/5118-Instr.pdf | 2026-11-13 |
| 2025 Form 5119 and 5120 instructions. Read for the part-year resident split. | https://www.michigan.gov/taxes/-/media/Project/Websites/taxes/Forms/City-IIT/TY2025/5119-Instr.pdf | 2026-11-13 |
| Michigan Treasury, 2025 City Individual Income Tax Forms (Detroit). Read for the list of Detroit forms. | https://www.michigan.gov/taxes/citytax/detroit/forms/2025/2025-city-individual-income-tax-forms | 2026-11-13 |

Not yet confirmed: the 2026 Detroit forms and instructions were not published when read, so 2025 form lines are used; the due date of 15 April 2027 and the Form 5209 extension rule (from the old file, not re-read in 2025 instructions); whether exemptions are prorated on Form 5119 for nonresidents; interest rates after 30 June 2026; any cap on the late payment penalty; the treatment of nonresidents' casino winnings; the Uniform City Income Tax Act (MCL 141.501 and following) itself, as legislature.mi.gov returned errors; the Honigman v City of Detroit (2020) sourcing rule cited in the old file (not re-read).

## Today's figures and who stands behind this skill

This file is an AI skill (tax rules your AI follows) from OpenAccountants, copied on 2026-11-13. Rates, thresholds and deadlines change. For the current version of this skill, its official sources and the named accountant (if any) who stands behind it, call `get_skill` with slug `mi-detroit-individual-return` on the OpenAccountants connector (https://www.openaccountants.com/connect), or read https://www.openaccountants.com/skills/mi-detroit-individual-return. If neither is available, confirm every figure against the official source pages cited above before relying on it.
