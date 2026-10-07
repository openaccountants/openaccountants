---
name: nz-income-tax-ir3
description: Use this skill whenever asked about New Zealand income tax for self-employed individuals filing an IR3 return. Trigger on phrases like "how much tax do I pay in NZ", "IR3", "income tax return New Zealand", "allowable deductions NZ", "provisional tax NZ", "schedular payments", "independent earner tax credit", "IETC", "ACC levies", "Working for Families", "residual income tax", "self-employed tax NZ", "schedular withholding NZ", or any question about filing or computing income tax for a self-employed individual in New Zealand. This skill covers NZ tax brackets (10.5%-39%), IR3 return structure, allowable deductions, ACC levies, provisional tax, IETC, penalties, and interaction with GST. ALWAYS read this skill before touching any NZ income tax work.
version: 2.0
jurisdiction: NZ
tax_year: 2026
last_updated: 2026-09-26
authored_by: Michael Cutajar and the OpenAccountants team
review_status: pending_review
trust_label: Built by Michael Cutajar and the OpenAccountants team
depends_on:
  - income-tax-workflow-base
category: international
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# New Zealand individual income tax return (IR3)

## Scope

This Guide covers one New Zealand tax resident individual who files an Individual income tax return (IR3): self-employed people, sole traders, contractors paid schedular payments, landlords and anyone else with income that was not taxed before they got it.

- **Primary year:** the 2026-27 tax year, 1 April 2026 to 31 March 2027 (Inland Revenue calls it the 2027 income year). Its IR3 is filed after 31 March 2027.
- **Also covered:** the 2025-26 return being filed now (see "The 2025-26 return being filed now") and the 2024-25 composite rates, which still apply to 2024-25 returns and amendments.
- **Not covered:** companies, trusts, partnerships and look-through companies; non-residents (they file an IR3NR); Working for Families calculations; GST return preparation.
- **Law:** Income Tax Act 2007 and Tax Administration Act 1994, as explained on Inland Revenue (IRD) pages. Where a 2026-27 figure is not yet published, the previous one is given, labelled.

## Ask the client first

- Were you a New Zealand tax resident for the whole year? A non-resident files an IR3NR, not an IR3.
- Which year are we doing: 2026-27 (1 April 2026 to 31 March 2027), or the 2025-26 return that is due now or overdue?
- Do you have a tax agent with an extension of time? It moves both the filing date and the terminal tax date.
- What income did you have that was not taxed before you got it: self-employment, rent, overseas income, interest or dividends with too little tax deducted?
- Did any payer deduct schedular tax, and what rate did you give them on the IR330C?
- Are you registered for GST? If so, are your figures GST-inclusive?
- Do you work from home? Is part of the home set aside and used mainly for the business, and how many square metres is it out of the whole home?
- Do you use a vehicle for business? Do you have a logbook covering at least 90 consecutive days?
- Did you, or your partner, receive Working for Families, or did you receive an income-tested benefit, NZ Super or a Veteran's Pension, in any month of the year?
- Did you own or sell residential property? When did title transfer to you, and when did you sign a binding sale agreement?
- What was your residual income tax (RIT) last year, which provisional tax option are you on, and what have you paid and when?
- Did you give to approved donee organisations and keep the receipts?

## The method, step by step

1. **Check the person must file an IR3.** They must if they received more than $200 (before tax) of income IRD was not told about ([IRD IR3](https://www.ird.govt.nz/income-tax/income-tax-for-individuals/what-happens-at-the-end-of-the-tax-year/individual-income-tax-return---ir3)). Confirm residence; a non-resident files an IR3NR.
2. **Fix the year and the dates.** The tax year runs 1 April to 31 March. Decide whether the return is on time, covered by a tax agent's extension of time, or late (see "Filing and payment").
3. **Gather third-party income first.** If employers, banks, benefit payers or KiwiSaver/PIE providers must report to IRD, wait until June to file.
4. **Work out business income.** Use GST-exclusive amounts if GST-registered. Gross up schedular payments to the amount before tax was deducted.
5. **Deduct business expenses.** Apply the home-office method, the vehicle rules, the entertainment split and the rental rules below. Provisional tax and GST payments are never expenses.
6. **Add other income.** Rent (net of allowable expenses, ring-fenced), interest, dividends with imputation credits, taxable bright-line sales (with an IR833), overseas income.
7. **Apply the 2026-27 rates band by band** to taxable income (table below).
8. **Take off tax credits:** PAYE, schedular tax deducted, RWT, imputation credits, the IETC if eligible, donation tax credits, and provisional tax paid. The result is tax to pay or a refund.
9. **Work out next year's provisional tax.** If RIT is more than $5,000, the person is a provisional taxpayer next year ([IRD provisional tax](https://www.ird.govt.nz/income-tax/provisional-tax)). Choose the option (standard, estimation, AIM or ratio).
10. **File and pay** by the due dates, and tell the client about use-of-money interest and penalties if a date is missed.

## 2026-27 figures

### Income tax rates, 2026-27 (and 2025-26)

The 2026-27 year uses IRD's table headed "From 1 April 2025"; no later table is published. The same table applies to 2025-26.

| Taxable income | Rate on each dollar in the band |
| --- | --- |
| Source | [IRD tax rates for individuals](https://www.ird.govt.nz/income-tax/income-tax-for-individuals/tax-codes-and-tax-rates-for-individuals/tax-rates-for-individuals) |
| $0 to $15,600 | 10.5% |
| $15,601 to $53,500 | 17.5% |
| $53,501 to $78,100 | 30% |
| $78,101 to $180,000 | 33% |
| $180,001 and over | 39% |

- Each rate applies only to the dollars inside its band. Crossing a threshold does not change the tax on the lower dollars.
- ACC earners' levy is separate from these rates (see "ACC earners' levy").

### The 31 July 2024 change and the 2024-25 composite rates

The Taxation (Budget Measures) Act 2024 raised the three lower thresholds from 31 July 2024. Because the change came part-way through the year, IRD set composite thresholds and rates for the whole 2024-25 year (1 April 2024 to 31 March 2025) ([TIB Vol 36 No 7](https://www.taxtechnical.ird.govt.nz/-/media/project/ir/tt/pdfs/tib/volume-36---2024/tib-vol36-no7.pdf)). Use them only for 2024-25 returns and amendments.

| 2024-25 taxable income (composite) | Rate |
| --- | --- |
| Source | [IRD tax rates for individuals](https://www.ird.govt.nz/income-tax/income-tax-for-individuals/tax-codes-and-tax-rates-for-individuals/tax-rates-for-individuals) |
| $0 to $14,000 | 10.5% |
| $14,001 to $15,600 | 12.82% |
| $15,601 to $48,000 | 17.5% |
| $48,001 to $53,500 | 21.64% |
| $53,501 to $70,000 | 30% |
| $70,001 to $78,100 | 30.99% |
| $78,101 to $180,000 | 33% |
| $180,001 and over | 39% |

- Before 31 July 2024 the bands ended at $14,000, $48,000 and $70,000; the new bands end at $15,600, $53,500 and $78,100; the $180,000 threshold did not change ([TIB Vol 36 No 7](https://www.taxtechnical.ird.govt.nz/-/media/project/ir/tt/pdfs/tib/volume-36---2024/tib-vol36-no7.pdf)).
- The IETC also changed on 31 July 2024 and uses a composite calculation for 2024-25 only (see "Tax credits").

### Tax credits

**Independent earner tax credit (IETC).** Rules "From July 2024", unchanged for 2026-27 ([IRD IETC](https://www.ird.govt.nz/income-tax/income-tax-for-individuals/individual-tax-credits/independent-earner-tax-credit-ietc)).

| Income before tax in the tax year | IETC |
| --- | --- |
| Source | [IRD IETC](https://www.ird.govt.nz/income-tax/income-tax-for-individuals/individual-tax-credits/independent-earner-tax-credit-ietc) |
| Below $24,000 | None |
| $24,000 to $66,000 | $10 per week, at most $520 a year |
| $66,001 to $70,000 | Reduces by 13 cents for every dollar over $66,000 |
| Over $70,000 | None |

- **Who:** New Zealand tax residents only. Income counted includes wages, self-employment, investments, ACC compensation and paid parental leave, but not losses brought forward.
- **Who cannot:** anyone who, or whose partner, is entitled to and receives Working for Families; anyone receiving an income-tested benefit, New Zealand Superannuation, a Veteran's Pension or an overseas equivalent.
- **Whole months:** any of those payments at any time in a month removes the IETC for the whole month.
- **Check:** Tax Information Bulletin Vol 36 No 7 also lists student allowance among payments that remove the IETC, while the current IRD page lists Student Allowance as income the IETC can be earned on. Refer for a student with Student Allowance months.
- **2024-25 only:** the previous settings (abating from $44,000, nil above $48,000) applied for the first three months and 30 days, and a composite calculation gives the full-year entitlement ([TIB Vol 36 No 7](https://www.taxtechnical.ird.govt.nz/-/media/project/ir/tt/pdfs/tib/volume-36---2024/tib-vol36-no7.pdf)).
- A self-employed person gets the IETC by filing the IR3.

**Donation tax credit.** Individuals can claim one third of eligible donations over $5 to approved donee organisations, up to their taxable income, and have 4 years to submit receipts ([IRD donation tax credits](https://www.ird.govt.nz/income-tax/income-tax-for-individuals/individual-tax-credits/donation-tax-credits)). Excess donations can be shared with a partner up to the partner's taxable income.

**Tax already deducted.** PAYE, schedular tax, RWT and imputation credits are credits against the year's tax.

### ACC earners' levy

| Levy year | Rate (includes GST) | Maximum liable earnings | Maximum levy |
| --- | --- | --- | --- |
| Source | [IRD earners' levy rates](https://www.ird.govt.nz/income-tax/income-tax-for-individuals/acc-clients-and-carers/acc-earners-levy-rates) | | |
| 1 April 2026 to 31 March 2027 | 1.75% | $156,641 | $2,741.22 |
| 1 April 2025 to 31 March 2026 | 1.67% | $152,790 | $2,551.59 |

- IRD's table also shows the 2027-28 row; do not use it for 2026-27.
- **Check:** for self-employed people, ACC levies are invoiced by ACC rather than calculated in the IR3, and the deductibility of the Work levy is set out by ACC. No allowed source (ird.govt.nz or legislation.govt.nz) was found that states either point; acc.co.nz is the source needed. Use the ACC invoice and do not estimate levies.

## Self-employed income and expenses

- **GST-registered:** report income and expenses without GST. The GST rate is 15% ([IRD GST guide IR295](https://www.ird.govt.nz/-/media/project/ir/home/documents/forms-and-guides/ir200---ir299/ir295/ir295.pdf)). Registration is compulsory when turnover was at least $60,000 in the last 12 months or is expected to be at least $60,000 in the next 12 months ([IRD registering for GST](https://www.ird.govt.nz/gst/registering-for-gst)). IRD's rental page says "over $60,000" for the same test ([IRD rental income](https://www.ird.govt.nz/property/renting-out-residential-property/residential-rental-income-and-paying-tax-on-it)); treat turnover of exactly $60,000 as "check".
- **Schedular payments:** income is the gross amount before tax was deducted; the tax deducted is a credit. A contractor who gives no IR330C is taxed at the no-notification rate of 45%, or 20% for non-resident contractor companies ([IRD IR330C](https://www.ird.govt.nz/-/media/project/ir/home/documents/forms-and-guides/ir300---ir399/ir330c/ir330c-2024.pdf)). A chosen rate must be at least 10%, or at least 15% for a non-resident on a temporary work or entry visa ([IRD schedular tax rate](https://www.ird.govt.nz/income-tax/withholding-taxes/schedular-payments/getting-schedular-payments/work-out-and-declare-my-tax-rate-for-schedular-payments)). Read the actual rate from the IR330C or myIR; never assume one.
- **Vehicle:** home to work is private. Without a logbook, the claim is limited to 25% of running costs, and IRD may still ask for substantiation ([IRD vehicle expenses](https://www.ird.govt.nz/income-tax/income-tax-for-businesses-and-organisations/types-of-business-expenses/claiming-vehicle-expenses)). A logbook kept for at least 90 consecutive days sets the business share for up to 3 years unless business use changes by more than 20% ([IRD logbook](https://www.ird.govt.nz/income-tax/income-tax-for-businesses-and-organisations/types-of-business-expenses/claiming-vehicle-expenses/use-a-logbook)). Kilometre rates are published after each tax year ends, so 2026-27 rates are not out yet; stay with one method (kilometre rates or actual costs) for as long as you own the vehicle.
- **Entertainment:** 50% deductible where there is a significant private element, such as meals with a business contact, sports or cultural events and parties; 100% for items such as food and drink at a conference lasting at least 4 hours ([IRD entertainment expenses](https://www.ird.govt.nz/income-tax/income-tax-for-businesses-and-organisations/types-of-business-expenses/entertainment-expenses)). Purely private entertainment is not deductible.
- **Not deductible:** provisional tax, income tax and GST payments. Use-of-money interest paid is deductible for business purposes (see "Use-of-money interest").
- **Losses:** a loss (deductible expenses greater than income) is claimed in the IR3 and carried forward to reduce taxable income in later years until used, unless an audit, voluntary disclosure, use against tax debts or bankruptcy changes it ([IRD self-employed and making a loss](https://www.ird.govt.nz/situations/i-am-self-employed-and-making-a-loss)).

### Home-office methods

A claim needs a link between the use of the home and the business income ([IRD using your home for your business](https://www.ird.govt.nz/income-tax/income-tax-for-businesses-and-organisations/types-of-business-expenses/using-your-home-for-your-business)). There are two ways.

| Method | Who can use it | What you claim |
| --- | --- | --- |
| Source | [IRD using your home for your business](https://www.ird.govt.nz/income-tax/income-tax-for-businesses-and-organisations/types-of-business-expenses/using-your-home-for-your-business) | |
| Square metre rate option | Only if the business area is set aside and used mainly for business | (a x b) + (c x d): a = mortgage interest, rates and rent paid in the year; b = c divided by the total floor area; c = the business area in square metres; d = IRD's square metre rate |
| Proportional (actual costs) | Anyone with a business connection | A share of rates, insurance, power, mortgage interest (not principal) and similar costs, based on the time and space used for business |

| Tax year | Square metre rate |
| --- | --- |
| Source | [IRD using your home for your business](https://www.ird.govt.nz/income-tax/income-tax-for-businesses-and-organisations/types-of-business-expenses/using-your-home-for-your-business) |
| 2026-27 | Not yet published on 25 September 2026: check IRD before filing |
| 2025-26 | $57.30 per square metre |
| 2024-25 | $55.60 per square metre |

- With the square metre rate option, no other home-use expenses or depreciation can be claimed. The rate covers utilities; it excludes mortgage interest, rates and rent, which are claimed through part (a x b).
- No depreciation is claimable on the home itself. Depreciation claimed before 1 April 2011 must be brought back in on sale or when business use stops. Depreciation on a computer, furniture and fittings used for business is allowed.
- Telephone: 50% of the rental of a landline that is also the private line; business toll calls in full; a separate business line in full ([IRD using your home for your business](https://www.ird.govt.nz/income-tax/income-tax-for-businesses-and-organisations/types-of-business-expenses/using-your-home-for-your-business)). Internet: any business share that gives a fair and reasonable result.
- GST-registered people claim these costs without GST; others include GST.

## Rental income

- Rent is income in the year it is earned; allowable expenses are deducted from it and the net goes in the return. Keep records for 7 years.
- **Interest deductibility (New Zealand residential property):**

| Period | Interest you can claim |
| --- | --- |
| Source | [IRD interest limitation rules](https://www.ird.govt.nz/property-interest-rules) |
| From 1 April 2025 (2025-26 and 2026-27) | 100% |
| 1 April 2024 to 31 March 2025 | 80% |
| 2022, 2023 and 2024 returns | Depends on when the funds were borrowed: refer |

- Interest must not be private and must meet the general deductibility rules. Main homes are generally outside the rules; interest relating to flatmates or boarders in a main home can be claimed in part.
- **Ring-fencing:** residential rental deductions can be claimed only up to rental income (including income from a taxable sale). Excess deductions cannot be set against salary, wages or business income; they are carried forward to a year with residential rental income ([IRD residential rental property deductions](https://www.ird.govt.nz/property/renting-out-residential-property/residential-rental-property-deductions)). Choose the portfolio basis, the individual property basis, or both. The rules do not apply to the main home, mixed-use assets, property that will be taxed on sale (after notifying IRD), farmland, business premises and some others.
- Long-term residential rent is exempt from GST. Short-stay accommodation is a taxable activity for GST.

### The bright-line test

- For residential property sold on or after 1 July 2024, profit is taxable if the bright-line end date is within 2 years of the start date, unless an exclusion or rollover relief applies ([IRD bright-line test](https://www.ird.govt.nz/property/buying-and-selling/when-you-need-to-pay/the-brightline-test)).
- **Dates:** start when title transfers to you (generally settlement); end when you enter a binding sale and purchase agreement. Off-the-plan purchases, gifts and other disposals differ.
- **Exclusions:** generally a main home when your use meets the criteria; business premises; farmland; inherited property or a sale as executor.
- **Older sales:** property sold before 1 July 2024 uses a 5-year or 10-year period depending on when it was acquired. Refer.
- Report a bright-line sale on an IR833 and show the net profit in the return. Other land-sale rules (intention to resell, dealing, building) still apply after the period ends. Interest denied under the interest limitation rules may become deductible on a taxable sale.

## Provisional tax

- **Who:** anyone whose residual income tax (RIT) on the last return was more than $5,000 pays provisional tax in the following year ([IRD provisional tax](https://www.ird.govt.nz/income-tax/provisional-tax)). RIT is the year's income tax less credits such as PAYE, schedular tax and the IETC. A person expecting RIT over $5,000 may choose to be a provisional taxpayer.
- **New provisional taxpayer:** an individual whose RIT was less than $5,000 for the last 4 years, whose current-year RIT is $60,000 or more, and who moved from employment to an activity with no tax deducted must pay in the current year ([IRD interest on provisional tax](https://www.ird.govt.nz/income-tax/provisional-tax/interest-on-provisional-tax)).
- **Dates for a 31 March balance date (standard and estimation):** 28 August, 15 January and 7 May ([IRD standard option](https://www.ird.govt.nz/income-tax/provisional-tax/provisional-tax-options/standard-option/work-out-provisional-tax-using-the-standard-option)). For 2026-27 that is 28 August 2026, 15 January 2027 and 7 May 2027. A 6-monthly GST filer on the standard option pays 2 instalments with the GST returns. A date on a weekend or public holiday moves to the next working day.

| Option | Who can use it | How it works | Use-of-money interest |
| --- | --- | --- | --- |
| Source | [IRD provisional tax options](https://www.ird.govt.nz/income-tax/provisional-tax/provisional-tax-options) and the option pages | | [IRD interest on provisional tax](https://www.ird.govt.nz/income-tax/provisional-tax/interest-on-provisional-tax) |
| Standard (the default) | Anyone | Last year's RIT plus 5%; or RIT from 2 years ago plus 10% for instalments due before last year's return is filed, if you have an extension of time | RIT under $60,000: only from the day after the terminal tax date. RIT $60,000 or more: from the day after the final instalment (earlier instalments paid late or short are charged from their own dates) |
| Estimation | Anyone; can switch in at any time up to the final instalment date | Pay your own estimate of this year's RIT; can be $0; re-estimate if income changes | On any shortfall against actual RIT from each instalment date, even if the estimate was paid; a penalty is possible if the estimate was too low |
| AIM (accounting income method) | Individuals and companies with yearly turnover under $5 million, using AIM-capable software | Pay from profit through statements of activity; resets to standard each year unless you file your first statement | None if paid in full and on time; no interest paid to you on overpayments |
| Ratio | In business and registered for GST for the whole previous year and part of the year before; previous RIT greater than $5,000 and up to $150,000; files GST monthly or 2-monthly; not a partnership; IRD's ratio percentage between 0% and 100% | IRD's ratio percentage times GST taxable supplies for the previous 2 months, paid with the GST returns; elect before the start of the income year | None if applied correctly and paid; interest if more than $100 is owing after the terminal tax date, and from the date the option stops |

- Standard-option uplift by filing date, with an extension of time ([IRD standard option](https://www.ird.govt.nz/income-tax/provisional-tax/provisional-tax-options/standard-option)): last year's return filed by the first instalment date means 3 equal instalments of last year's RIT plus 5%. Filed after the first but by the second date means the first instalment uses RIT from 2 years ago plus 10% and the rest use last year's RIT plus 5%. Filed after the second date means the first two use RIT from 2 years ago plus 10%. Without an extension of time, always use last year's RIT plus 5%, even if the return is filed late.
- Switching from standard to estimation makes interest apply as if you had estimated all year. You cannot change to the ratio option part-way through a year. AIM dates follow the AIM software's schedule.
- Ratio instalments are paid with the GST returns, on the ratio-method dates in IRD's IR328 calendar. The ratio option must stop if GST registration ends, any GST return is 60 or more days overdue, the ratio falls outside 0% to 100%, you move to 6-monthly GST, or a return shows RIT below $5,000 or above $150,000; use-of-money interest then applies from the date it stops ([IRD ratio option](https://www.ird.govt.nz/income-tax/provisional-tax/provisional-tax-options/ratio-option)).

## Boundary and exception table

| Situation | Rule | Source |
| --- | --- | --- |
| Income IRD was not told about: exactly $200 | "more than $200" triggers filing; exactly $200 does not | [IRD IR3](https://www.ird.govt.nz/income-tax/income-tax-for-individuals/what-happens-at-the-end-of-the-tax-year/individual-income-tax-return---ir3) |
| RIT exactly $5,000 | "more than $5,000" triggers provisional tax; $5,000 or less generally does not | [IRD provisional tax](https://www.ird.govt.nz/income-tax/provisional-tax) |
| RIT exactly $60,000 on the standard option | "$60,000 or more": interest from the day after the final instalment | [IRD interest on provisional tax](https://www.ird.govt.nz/income-tax/provisional-tax/interest-on-provisional-tax) |
| Under- or overpayment of $100 or less | No provisional tax interest charged or paid | [IRD interest on provisional tax](https://www.ird.govt.nz/income-tax/provisional-tax/interest-on-provisional-tax) |
| Income $66,000 vs $66,001 | Full IETC at $66,000; abatement starts on dollars over $66,000 | [IRD IETC](https://www.ird.govt.nz/income-tax/income-tax-for-individuals/individual-tax-credits/independent-earner-tax-credit-ietc) |
| Net income exactly $100,000 for a late return | Falls in the "$100,000 to $1 million" row: $250 | [IRD late filing penalties](https://www.ird.govt.nz/managing-my-tax/penalties-and-interest/penalties-and-debt/late-filing-penalties) |
| Home area used partly for private purposes | Square metre rate option not available; use the proportional method | [IRD using your home](https://www.ird.govt.nz/income-tax/income-tax-for-businesses-and-organisations/types-of-business-expenses/using-your-home-for-your-business) |
| Bright-line end date exactly 2 years after start | "within 2 years" wording; treat as "check" and refer | [IRD bright-line test](https://www.ird.govt.nz/property/buying-and-selling/when-you-need-to-pay/the-brightline-test) |
| Unacceptable tax position | Penalty only if the income tax shortfall is more than both $50,000 and 1% of the total tax figure | [IRD shortfall penalties](https://www.ird.govt.nz/managing-my-tax/penalties-and-interest/penalties-and-debt/shortfall-penalties) |

## Worked cases

Illustrations with made-up inputs, not advice.

**C1. Tax on $90,000, 2026-27.** A resident sole trader has taxable income of $90,000 for 2026-27 ([IRD tax rates](https://www.ird.govt.nz/income-tax/income-tax-for-individuals/tax-codes-and-tax-rates-for-individuals/tax-rates-for-individuals)).

| Band | Dollars in the band | Rate | Tax |
| --- | --- | --- | --- |
| Source | [IRD tax rates](https://www.ird.govt.nz/income-tax/income-tax-for-individuals/tax-codes-and-tax-rates-for-individuals/tax-rates-for-individuals) | | |
| First band | $15,600 | 10.5% | $1,638 |
| Second band | $37,900 | 17.5% | $6,632.50 |
| Third band | $24,600 | 30% | $7,380 |
| Fourth band (to taxable income) | $11,900 | 33% | $3,927 |
| Total | $90,000 | | $19,577.50 |

No IETC: income is over $70,000 ([IRD IETC](https://www.ird.govt.nz/income-tax/income-tax-for-individuals/individual-tax-credits/independent-earner-tax-credit-ietc)).

**C2. IETC abatement, 2026-27.** Income before tax $68,000, no Working for Families, benefit, NZ Super or Veteran's Pension in any month ([IRD IETC](https://www.ird.govt.nz/income-tax/income-tax-for-individuals/individual-tax-credits/independent-earner-tax-credit-ietc)). Income is $2,000 over $66,000, so the credit reduces by $260 (13 cents a dollar), from $520 to $260. If the person got NZ Super from 1 February 2027, February and March would be excluded whole months: refer for the part-year figure.

**C3. Standard provisional tax, 2026-27.** RIT on the 2025-26 return was $12,000, filed before 28 August 2026; the person files GST every two months, not six-monthly ([IRD standard option](https://www.ird.govt.nz/income-tax/provisional-tax/provisional-tax-options/standard-option/work-out-provisional-tax-using-the-standard-option)). Provisional tax is $12,000 plus 5% = $12,600, paid as 3 instalments of $4,200 on 28 August 2026, 15 January 2027 and 7 May 2027. Because RIT is under $60,000, use-of-money interest on any 2026-27 difference runs only from the day after the terminal tax date ([IRD interest on provisional tax](https://www.ird.govt.nz/income-tax/provisional-tax/interest-on-provisional-tax)).

**C4. Square metre rate, 2025-26 return.** A 12 square metre office set aside and used mainly for business, in a 120 square metre home; mortgage interest and rates of $20,000 for the year ([IRD using your home](https://www.ird.govt.nz/income-tax/income-tax-for-businesses-and-organisations/types-of-business-expenses/using-your-home-for-your-business)). b = 12 / 120, so the premises part is $2,000. The utilities part is 12 x $57.30 = $687.60. Claim $2,687.60 and no other home-use costs or depreciation on the home. For 2026-27, wait for IRD's new rate.

**C5. Late 2025-26 return and late terminal tax.** No tax agent. The 2025-26 IR3 was due 7 July 2026 and was filed on 20 September 2026 showing net income of $80,000. The late filing penalty is $50 ([IRD late filing penalties](https://www.ird.govt.nz/managing-my-tax/penalties-and-interest/penalties-and-debt/late-filing-penalties)). Terminal tax of $3,000 is due 7 February 2027, a Sunday; Monday 8 February is the Waitangi Day holiday, so IRD's IR328 calendar puts the payment on Tuesday 9 February 2027. If paid on 10 February 2027, the 1% penalty applies ($30), but not the 4% stage, which starts on the 7th day after the due date; a first late payment in 2 years may get a grace period ([IRD late payment penalties](https://www.ird.govt.nz/managing-my-tax/penalties-and-interest/penalties-and-debt/late-payment-penalties)). Use-of-money interest runs daily from 10 February 2027.

**C6. Bright-line sale.** Title to a rental flat transferred on 1 March 2025; the owner signs a binding sale agreement on 15 February 2027 ([IRD bright-line test](https://www.ird.govt.nz/property/buying-and-selling/when-you-need-to-pay/the-brightline-test)). The end date is within 2 years of the start date, so the profit is taxable (it was never the main home). Complete an IR833, show the net profit in the 2026-27 return, and check whether interest denied in 2024-25 can now be claimed. Signed on 10 March 2027 instead, the bright-line test would not apply, though the intention and dealing rules still could.

**C7. Rental interest and ring-fencing, 2026-27.** A residential rental earns $20,000 rent; interest is $15,000 and other expenses $8,000 ([IRD interest limitation rules](https://www.ird.govt.nz/property-interest-rules)). All $15,000 of interest is claimable from 1 April 2025, so expenses are $23,000 and there are excess deductions of $3,000 ([IRD residential rental property deductions](https://www.ird.govt.nz/property/renting-out-residential-property/residential-rental-property-deductions)). The $3,000 cannot reduce salary or business income; carry it forward. For 2024-25 the same interest would have been limited to 80%, or $12,000.

## When to refuse or refer

- The income belongs to a company, trust, partnership or look-through company; this Guide covers one individual's IR3.
- The person is not a New Zealand tax resident, changed residence in the year, or may be a transitional resident.
- Working for Families entitlement or abatement, or a part-year IETC with excluded months.
- Foreign income in a foreign currency, foreign tax credits, foreign investment funds, or cryptoassets: no conversion method is stated here.
- A bright-line sale before 1 July 2024, a sale near the 2-year boundary, a main-home claim, rollover relief, or a property dealing or building question.
- Rental interest for the 2022 to 2024 returns, untraceable mixed loans, mixed-use holiday homes, or a choice between portfolio and individual ring-fencing bases.
- ACC levy classification, Work levy deductibility, or a dispute about an ACC invoice.
- A shortfall penalty, voluntary disclosure, dispute, or several years of unfiled returns.
- Employee versus contractor doubt.
- The 2026-27 square metre rate or kilometre rates are needed before IRD publishes them.

## Filing and payment

- If a due date falls on a weekend or public holiday, you can file or pay on the next working day without penalties ([IRD IR328 calendar 2026-27](https://www.ird.govt.nz/-/media/project/ir/home/documents/forms-and-guides/ir300---ir399/ir328/ir328-2026-27.pdf)).

### The 2025-26 return being filed now

- **Year:** 1 April 2025 to 31 March 2026. Rates: the "From 1 April 2025" table above. IETC: the same rules. Use the 2025-26 rows of the ACC earners' levy and square metre rate tables above. Rental interest is fully deductible.
- **Filing:** due 7 July 2026 unless the person has a tax agent with an extension of time or their own extension ([IRD IR3](https://www.ird.govt.nz/income-tax/income-tax-for-individuals/what-happens-at-the-end-of-the-tax-year/individual-income-tax-return---ir3)). With a tax agent's extension, the Commissioner can allow filing up to 31 March 2027 ([IRD extension of time](https://www.ird.govt.nz/topics/intermediaries/extension-of-time-arrangements)). A return without an extension that was not filed by 7 July 2026 is already late: file now.
- **Terminal tax:** 7 February 2027, or 7 April 2027 with a tax agent's extension of time ([IRD interest on provisional tax](https://www.ird.govt.nz/income-tax/provisional-tax/interest-on-provisional-tax)). 7 February 2027 is a Sunday and 8 February is the Waitangi Day holiday, so the payment moves to 9 February 2027 (IR328).

### 2026-27 dates (31 March balance date)

| Item | Date |
| --- | --- |
| Provisional tax (standard, estimation) | 28 August 2026, 15 January 2027, 7 May 2027 |
| IR3 (no agent, no extension) | 7 July 2027 |
| IR3 (tax agent's client with an extension of time) | Up to 31 March 2028 |
| Terminal tax | 7 February 2028, the Monday holiday for Waitangi Day (6 February 2028 is a Sunday), so in practice 8 February 2028: confirm on the 2027-28 IR328 |
| Terminal tax with a tax agent's extension of time | 7 April 2028 |

- Sources: the pages cited in "The 2025-26 return being filed now" and the provisional tax section. IRD's own example: a bill for the 1 April 2024 to 31 March 2025 year is due on 7 February 2026 ([IRD timelines](https://www.ird.govt.nz/income-tax/income-tax-for-individuals/what-happens-at-the-end-of-the-tax-year/timelines-at-the-end-of-the-tax-year)).
- IRD may withdraw a client's extension for the next year if the return is not filed by 31 March, or an agent's if the agent files less than 90% of required returns on time for 2 years ([IRD extension of time](https://www.ird.govt.nz/topics/intermediaries/extension-of-time-arrangements)). A non-March balance date has other dates.

### Use-of-money interest

| Rate from | IRD charges on underpaid tax | IRD pays on overpaid tax |
| --- | --- | --- |
| Source | [IRD interest on overpayments and underpayments](https://www.ird.govt.nz/managing-my-tax/penalties-and-interest/interest-on-overpayments-and-underpayments) | |
| 16 January 2026 (current on 25 September 2026) | 8.97% | 2.25% |
| 8 May 2025 | 9.89% | 3.27% |

- Interest is daily, not compounded, and not part of penalty calculations. It starts the day after the due date and stops when the balance, including interest, is paid.
- IRD does not charge or pay provisional tax interest on an under- or overpayment of $100 or less ([IRD interest on provisional tax](https://www.ird.govt.nz/income-tax/provisional-tax/interest-on-provisional-tax)).
- Interest paid on underpaid tax is deductible for business purposes; interest received on an overpayment is gross income in the year it is refunded.
- After a notice of assessment you have up to an extra 30 days to pay without the interest added since the notice.
- Rates follow market rates: check for a newer row.

### Late filing and late payment penalties

| Late filing of an income tax return: net income | Penalty |
| --- | --- |
| Source | [IRD late filing penalties](https://www.ird.govt.nz/managing-my-tax/penalties-and-interest/penalties-and-debt/late-filing-penalties) |
| Less than $100,000 | $50 |
| $100,000 to $1 million | $250 |
| More than $1 million | $500 |

- The penalty is first charged at $50 and adjusted after the return is filed to the net income shown. It applies only if there is no extension of time or valid reason ([IRD late filing penalties](https://www.ird.govt.nz/managing-my-tax/penalties-and-interest/penalties-and-debt/late-filing-penalties)).

| Late payment stage | Penalty |
| --- | --- |
| Source | [IRD late payment penalties](https://www.ird.govt.nz/managing-my-tax/penalties-and-interest/penalties-and-debt/late-payment-penalties) |
| Day after the due date | 1% |
| 7th day after the due date, on tax and penalties still unpaid | 4% |
| Each month after | 1%, but not for income tax including provisional tax |

- A first late payment in a 2-year period may get a grace period; miss the new date and the penalty runs from the original date. A reassessment can get a new due date.

| Shortfall penalty | Share of the tax shortfall |
| --- | --- |
| Source | [IRD shortfall penalties](https://www.ird.govt.nz/managing-my-tax/penalties-and-interest/penalties-and-debt/shortfall-penalties) |
| Not taking reasonable care | 20% |
| Unacceptable tax position (income tax shortfall more than both $50,000 and 1% of the total tax figure) | 20% |
| Gross carelessness | 40% |
| Abusive tax position | 100% |
| Evasion | 150% |

- Obstructing an IRD officer can raise a shortfall penalty by 25% ([IRD shortfall penalties](https://www.ird.govt.nz/managing-my-tax/penalties-and-interest/penalties-and-debt/shortfall-penalties)). Voluntary disclosure can lower one: refer.

## Completion checklist

- [ ] Residence confirmed; IR3, not IR3NR.
- [ ] Correct year: 2026-27 figures, or 2025-26 for the return due now, or composite rates for 2024-25 only.
- [ ] Third-party income in; GST removed if GST-registered.
- [ ] Schedular payments grossed up; tax deducted taken as a credit.
- [ ] Home office: method chosen; square metre rate used only for a set-aside area, and nothing else claimed with it.
- [ ] Vehicle: logbook share or the no-logbook limit.
- [ ] Entertainment split between the full and half-deductible groups.
- [ ] Rental: interest share for the year; excess deductions ring-fenced and carried forward.
- [ ] Bright-line sales identified and IR833 completed.
- [ ] IETC checked against income and excluded months; donation receipts submitted.
- [ ] Provisional tax and GST payments excluded from expenses and credited against tax.
- [ ] Next year's provisional tax option and instalments set.
- [ ] Filing and terminal tax dates confirmed, including any tax agent's extension of time.
- [ ] Penalties and interest explained if a date was missed; figures labelled as estimates.

<!-- openaccountants-cta-block -->

---

## Talk to a verified accountant

This guide is maintained by the OpenAccountants network — accountants who put
their name behind the tax answers AI gives people. The live, always-current
version (and the professional behind it) is at
[openaccountants.com](https://www.openaccountants.com).

- Use it in your AI: https://www.openaccountants.com/connect
- Meet the accountants: https://www.openaccountants.com/network

> **General reference only.** This document does not constitute tax, legal, or
> financial advice. Verify figures against the cited primary sources or with a
> licensed professional before relying on them.
