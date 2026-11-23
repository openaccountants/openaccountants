---
name: nz-provisional-tax
description: "Use this skill whenever asked about New Zealand provisional tax for individuals, companies, contractors, sole traders, and small businesses. Trigger on phrases like \"provisional tax\", \"RIT\", \"residual income tax\", \"standard option\", \"standard uplift\", \"estimation method\", \"AIM\", \"ratio option\", \"use of money interest\", \"UOMI\", \"provisional tax instalment\", or any question about provisional tax obligations in New Zealand. Covers the $5,000 RIT threshold, standard option 105%/110% uplift rules, estimation, AIM, ratio-option routing, March balance-date instalments, 6-monthly GST two-instalment cases, and current UOMI rate handling. ALWAYS read this skill before touching any NZ provisional tax work."
license: "AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)"
metadata:
  source: openaccountants
  openaccountants_url: "https://www.openaccountants.com/skills/nz-provisional-tax"
  jurisdiction: "NZ"
  tax_year: "2026"
  last_updated: "2026-11-22"
---

# New Zealand provisional tax

## Scope

Provisional tax is income tax paid in instalments during the year instead of one lump sum after it ([IRD provisional tax](https://www.ird.govt.nz/income-tax/provisional-tax)). It is not a separate tax. This skill covers who must pay, the four options (standard, estimation, ratio and the accounting income method, AIM), instalment dates, use-of-money interest (UOMI) and penalties, for individuals, sole traders, contractors, landlords, partners, companies and trusts.

- **Primary year:** the 2026-27 income year, 1 April 2026 to 31 March 2027 (Inland Revenue calls it the 2027 income year), for a 31 March balance date.
- **Also covered:** the 2025-26 year (1 April 2025 to 31 March 2026), whose returns are being filed and whose end-of-year tax is due in 2027 (see "Filing and payment").
- **Law:** [Income Tax Act 2007, Part RC](https://www.legislation.govt.nz/act/public/2007/97/en/latest/sections/DLM1519805/) governs provisional tax. [Tax Administration Act 1994, Part 7](https://www.legislation.govt.nz/act/public/1994/166/en/latest/sections/DLM355313/) governs use-of-money interest.
- **Not covered:** working out the income tax itself (see `nz-income-tax-ir3`), GST returns (see `nz-gst-return`), ACC levies (see `nz-acc-levies`), tax pooling, multi-entity groups and non-residents.

Key terms:

- **Residual income tax (RIT):** the tax on taxable income, less PAYE and other income tax credits, but not counting Working for Families and not counting provisional tax or voluntary payments ([IR289](https://www.ird.govt.nz/-/media/project/ir/home/documents/forms-and-guides/ir200---ir299/ir289/ir289.pdf)). The test is on RIT, not on total income tax.
- **Terminal tax (end-of-year tax):** RIT for the year less the provisional tax paid.
- **Extension of time (EOT):** a tax agent's client may file a return up to 31 March of the following year instead of 7 July ([IRD extension of time](https://www.ird.govt.nz/topics/intermediaries/extension-of-time-arrangements)). An EOT changes which uplift the standard option uses. It does not change the instalment dates.

## Ask the client first

- What was the RIT on last year's return? If a tax agent has an extension of time and last year's return is not filed yet, what was the RIT on the return before that?
- Do you have a tax agent with an extension of time? When will last year's return be filed (before 28 August, before 15 January, before 7 May, or later)?
- Are you registered for GST? Do you file monthly, 2-monthly or 6-monthly?
- What is your balance date, if not 31 March? Have you changed it or asked to?
- Which option are you on now (standard is the default), and have you already switched this year?
- Do you expect this year's income to be much higher or lower than last year's? Is RIT likely to reach the interest line in "Use-of-money interest"?
- Did you start a business this year, or move from wages to self-employment? When did the activity start?
- Which instalments have you paid, how much, and on what dates? (Your myIR statement shows this.)
- Is the taxpayer an individual, a partnership, a company or a trust? Are any associated companies on a different option?
- For a first-year sole trader: have you made voluntary payments this year, and do you want the early payment discount?

## The method, step by step

1. **Is provisional tax compulsory?** Last-year RIT above $5,000 ordinarily triggers provisional tax. RIT of $5,000 or less removes the obligation. Check the exclusions and voluntary election separately. [Income Tax Act, s RC 3](https://www.legislation.govt.nz/act/public/2007/97/en/latest/sections/DLM1519805/).
2. **Check first-year interest.** RIT of $60,000 or more may trigger interest on deemed instalments for a taxpayer starting a taxable activity. Use the conditions and dates under "Who must pay". [Income Tax Act, s RC 9(9)](https://www.legislation.govt.nz/act/public/2007/97/en/latest/sections/DLM1519822/).
3. **Choose the option and check its conditions.** Standard applies unless another is chosen ([IRD standard option](https://www.ird.govt.nz/income-tax/provisional-tax/provisional-tax-options/standard-option)). Estimation suits falling or uncertain income. AIM and ratio suit uneven or seasonal income but have entry conditions.
4. **Work out each instalment.** Standard: use the applicable uplift and subtract earlier instalment liabilities from the cumulative amount for this instalment. Estimation: apply the same cumulative formula to estimated RIT, using the applicable instalment count. Truncate each instalment to whole dollars. Ratio: multiply the ratio by GST-inclusive taxable supplies for the period. AIM: use the software calculation. [Income Tax Act, s RC 10](https://www.legislation.govt.nz/act/public/2007/97/en/latest/sections/DLM1519824/), [s RC 11](https://www.legislation.govt.nz/act/public/2007/97/en/latest/sections/DLM1519833/), [s RC 10B](https://www.legislation.govt.nz/act/public/2007/97/en/latest/sections/LMS42733/).
5. **Diary the dates** for the option and GST filing frequency (see "Instalment dates"). A due date on a weekend or public holiday can be met on the next business day.
6. **Test the interest exposure** against the safe harbour and the option rules in "Use-of-money interest", using the UOMI rate in force on each day ([IRD interest on provisional tax](https://www.ird.govt.nz/income-tax/provisional-tax/interest-on-provisional-tax)).
7. **Check penalties** for any late or short instalment. If more than $100 of tax remains outstanding after the due date, the initial penalty is 1% the next day and 4% on the 7th day after the due date, on the balance including the first penalty. There is no further monthly penalty on provisional tax. [Tax Administration Act, s 139B](https://www.legislation.govt.nz/act/public/1994/166/en/latest/sections/DLM356138/), [s 183F](https://www.legislation.govt.nz/act/public/1994/166/en/latest/sections/DLM358771/).
8. **After the year:** RIT less provisional tax paid is terminal tax, due 7 February after the year ends, or 7 April with a tax agent's extension of time. The same return sets next year's RIT for step 1.

## 2026-27 figures and rules

The thresholds below apply to the 2026-27 income year. Historical amounts are labelled with their income year.

### Who must pay

| Rule (2026-27 income year unless stated) | Figure | Source |
| --- | --- | --- |
| Entry test: RIT on the last return must be MORE than | $5,000 | [IRD provisional tax](https://www.ird.govt.nz/income-tax/provisional-tax): "more than $5,000 tax at the end of the year from your last return" |
| New provisional taxpayer: current-year RIT at or above | $60,000 | [IRD interest on provisional tax](https://www.ird.govt.nz/income-tax/provisional-tax/interest-on-provisional-tax): "$60,000 or more" |
| Individual first-year interest test: RIT in each of the preceding 4 years at or below | $5,000 | [Income Tax Act, s YA 1, initial provisional tax liability](https://www.legislation.govt.nz/act/public/2007/97/en/latest/sections/DLM1520575/) |

- **Exactly $5,000 is not enough.** IRD: "Generally, you will not have to pay provisional tax if your residual income tax (RIT) last year was $5,000 or less" ([IRD interest on provisional tax](https://www.ird.govt.nz/income-tax/provisional-tax/interest-on-provisional-tax)).
- **Who typically pays:** self-employed, rental, contractor, partnership or overseas income; also wrong PAYE codes, untaxed lump sums, employee share scheme income or bright-line sales ([IRD provisional tax](https://www.ird.govt.nz/income-tax/provisional-tax)). Companies and trusts too.
- **New provisional taxpayer, individual** (excluding trustees acting as trustees): RIT of $5,000 or less in each of the preceding 4 years and at least $60,000 this year. During the year the individual stopped earning employment income and started deriving income from a taxable activity without tax deducted at source. **Non-individual:** starts deriving taxable activity income this year, derived none in the preceding 4 years and has RIT of at least $60,000 this year. [Income Tax Act, s YA 1, initial provisional tax liability](https://www.legislation.govt.nz/act/public/2007/97/en/latest/sections/DLM1520575/).
- **Effect for a new provisional taxpayer:** for UOMI, RIT is treated as due in 1 to 3 equal instalments. For a 31 March balance date outside the 6-month GST cycle, a start before 29 July gives 3 dates, a start from 29 July to 15 December gives 2 dates, and a start from 16 December gives 1 date. Debit interest starts the day after each applicable date on unpaid amounts. Apply the separate C and F or F-only schedule to 6-monthly GST filers. [Income Tax Act, s RC 9(9)](https://www.legislation.govt.nz/act/public/2007/97/en/latest/sections/DLM1519822/), [Tax Administration Act, s 120KC](https://www.legislation.govt.nz/act/public/1994/166/en/latest/sections/DLM355313/).
- **First year in business:** the previous year’s RIT normally determines the obligation. A new business with no obligation can usually pay its first year’s tax at terminal tax time. A qualifying initial provisional tax liability gives an earlier interest date, and eligible taxpayers can use AIM. In C9, first-year RIT of $75,000 gives $78,750 of second-year standard provisional tax. Both years’ scheduled payments can fall in the same year. [Income Tax Act, s RC 3](https://www.legislation.govt.nz/act/public/2007/97/en/latest/sections/DLM1519805/), [s RC 9](https://www.legislation.govt.nz/act/public/2007/97/en/latest/sections/DLM1519822/).

### Choosing to pay

A person who is not a provisional taxpayer may elect to be one ([IRD choosing to be a provisional taxpayer](https://www.ird.govt.nz/income-tax/provisional-tax/choosing-to-be-a-provisional-tax-payer)). The conditions:

- have been reasonably sure, on the day of the first payment, that they would be liable for provisional tax without the election;
- have paid more than $5,000 on or before instalment F (normally 7 May) or, for a transitional year, on or before its final instalment date. [Income Tax Act, s RC 4](https://www.legislation.govt.nz/act/public/2007/97/en/latest/sections/DLM1519807/).
- make the election on the first return filed for the year (tick the election in myIR, or attach a letter to a paper return).

When it matters: IR289 frames the election for someone whose RIT "works out to be $5,000 or less" after making voluntary payments, and its effect is that "We may calculate interest on your voluntary payments" ([IR289](https://www.ird.govt.nz/-/media/project/ir/home/documents/forms-and-guides/ir200---ir299/ir289/ir289.pdf)). IR289 also says anyone choosing to be a provisional taxpayer has to use the estimation option, and individuals must estimate on or before the third instalment date to have interest calculated.

### Early payment discount (first-year businesses)

| Rule | Figure | Source |
| --- | --- | --- |
| Discount rate, 2027 income year (2026-27) | 4.25% | [IRD first year in business](https://www.ird.govt.nz/income-tax/provisional-tax/paying-tax-in-your-first-year-in-business): "The early payment discount rate for the 2027 income year is 4.25%" |
| Discount rate, 2026 income year (2025-26) | 6.30% | same page, past rates table |
| Rate formula (from the 2025 income year) | UOMI credit rate at 31 March of the previous year plus 2% | same page |
| Base: the lesser of voluntary payments or this share of the year's RIT | 105% | [IR289](https://www.ird.govt.nz/-/media/project/ir/home/documents/forms-and-guides/ir200---ir299/ir289/ir289.pdf) |

The 2026-27 rate is 2.25% plus 2 percentage points. The discount is for eligible sole traders, partners and owners of look-through companies who derive income mainly from their business. Check the exclusions in RC 40. The person must have no provisional tax obligation for the year. If they were previously liable for compulsory provisional tax, they need 4 income years without assessable business income after the last year of liability. If they were never liable but previously received the discount, apply the same 4-year break after the last discounted year. Pay by the balance date and keep a credit at least equal to the lower of the qualifying payments and terminal tax from balance date to terminal tax date. Eligible tax pooling payments count. File the return and claim by its due date. The discount is credited towards income tax. [Income Tax Act, s RC 37](https://www.legislation.govt.nz/act/public/2007/97/en/latest/sections/DLM1519920/), [s RC 38](https://www.legislation.govt.nz/act/public/2007/97/en/latest/sections/DLM1519922/), [s RC 40](https://www.legislation.govt.nz/act/public/2007/97/en/latest/sections/DLM1519926/).

### Standard option (the default)

| Rule | Figure | Source |
| --- | --- | --- |
| Uplift on the previous year's RIT | 5% | [IRD standard option](https://www.ird.govt.nz/income-tax/provisional-tax/provisional-tax-options/standard-option): "your previous year's residual income tax (RIT) plus 5%" |
| Uplift on the RIT from 2 years ago (EOT, last year's return not yet filed) | 10% | same page: "your RIT from 2 years ago plus 10%" |

- **No extension of time:** last year's RIT plus the 5% uplift, "This includes if you file your return after any of your provisional tax dates." The 10% uplift never applies ([IRD standard option](https://www.ird.govt.nz/income-tax/provisional-tax/provisional-tax-options/standard-option)).
- **With an extension of time**, it depends on when last year's return is filed ([IRD work out standard option](https://www.ird.govt.nz/income-tax/provisional-tax/provisional-tax-options/standard-option/work-out-provisional-tax-using-the-standard-option)):

| Last year's return filed ([IR289](https://www.ird.govt.nz/-/media/project/ir/home/documents/forms-and-guides/ir200---ir299/ir289/ir289.pdf)) | 1st instalment (28 Aug) | 2nd instalment (15 Jan) | 3rd instalment (7 May) |
| --- | --- | --- | --- |
| On or before 28 August | (last year's RIT + 5%) / 3 | same | same |
| After 28 August, on or before 15 January | (2-years-ago RIT + 10%) / 3 | (last year's RIT + 5%) x 2 / 3, less the 1st instalment liability | last year's RIT + 5%, less the 1st and 2nd instalment liabilities |
| After 15 January, on or before 7 May | (2-years-ago RIT + 10%) / 3 | (2-years-ago RIT + 10%) / 3 | last year's RIT + 5%, less the 1st and 2nd instalment liabilities |
| After 7 May | (2-years-ago RIT + 10%) / 3 | (2-years-ago RIT + 10%) / 3 | expected RIT for last year + 5%, less the 1st and 2nd instalment liabilities |

- **RIT from 2 years ago of $5,000 or less:** no instalment is due on the 2-years-ago basis. Provisional tax is then paid in 1 or 2 instalments, depending on when the return is filed, split evenly between the instalments still due ([IR289](https://www.ird.govt.nz/-/media/project/ir/home/documents/forms-and-guides/ir200---ir299/ir289/ir289.pdf)). See case C3.
- **Weekend or holiday filing:** if an instalment date is on a weekend or public holiday and the return is filed on the next working day, it counts as filed on the instalment date. That can change the uplift.
- **Previous-year assessment:** a Commissioner assessment sent at least 30 days before the instalment date can set the RIT. Under RC 6(3), it can set RIT regardless of when made, including when a required preceding-year return is overdue on the instalment date. A later Commissioner assessment increasing RIT leaves the earlier instalment unchanged. [Income Tax Act, s RC 6](https://www.legislation.govt.nz/act/public/2007/97/en/latest/sections/DLM1519812/).
- **6-monthly GST filers** pay 2 instalments with their GST returns: divide by 2 instead of 3.
- **Final standard instalment:** at expected RIT of $60,000 or more, the taxpayer can use expected RIT less earlier instalment liabilities. Paying earlier instalments in full and on time can preserve the interest concession. [Income Tax Act, s RC 10(5)–(7)](https://www.legislation.govt.nz/act/public/2007/97/en/latest/sections/DLM1519824/), [Tax Administration Act, s 120KBB](https://www.legislation.govt.nz/act/public/1994/166/en/latest/sections/DLM7227374/).

### Estimation option

| Rule | Figure | Source |
| --- | --- | --- |
| Ordinary instalment count for standard or estimation with monthly, 2-monthly or no GST filing | 3 | [Income Tax Act, s RC 9(3)–(4)](https://www.legislation.govt.nz/act/public/2007/97/en/latest/sections/DLM1519822/) |
| Lowest estimate allowed | $0 | same page: "you can estimate your provisional tax at $0" |

- Provisional tax is the estimated RIT for the year: expected taxable income, tax on it, less PAYE and other credits ([IRD work out estimation option](https://www.ird.govt.nz/income-tax/provisional-tax/provisional-tax-options/estimation-option/work-out-provisional-tax-using-the-estimation-option)).
- Give the estimate in myIR, by phone or in writing. Use a fair and reasonable estimate and revise it if it stops being fair and reasonable. You can revise up to the final instalment date. [Income Tax Act, s RC 7](https://www.legislation.govt.nz/act/public/2007/97/en/latest/sections/DLM1519814/).
- **Switching in:** standard to estimation is allowed at any time up to the final instalment date. After switching, the taxpayer cannot go back to the standard option for that year (IR289), and interest is worked out as if they had estimated for the full year ([IRD interest on provisional tax](https://www.ird.govt.nz/income-tax/provisional-tax/interest-on-provisional-tax)).
- **Risk:** interest runs from the day after each instalment date on any shortfall against the actual RIT, even if every estimated instalment was paid in full and on time. A shortfall penalty is possible if the estimate was unreasonably low.

### Accounting income method (AIM)

| Rule | Figure | Source |
| --- | --- | --- |
| Ordinary entry test: annual gross income in the preceding tax year | $5 million or less | [Income Tax Act, s RC 5(5B)](https://www.legislation.govt.nz/act/public/2007/97/en/latest/sections/DLM1519810/) |

- Use up-to-date AIM-capable software. Check approved systems and the eligible taxpayer class, any AIM-related shortfall penalty in the preceding 4 tax years and the remaining statutory conditions. The software adjusts the financial accounts for tax, calculates the payment and files a statement of activity. An overpayment can be refunded during the year. [Income Tax Act, s RC 5(5B)](https://www.legislation.govt.nz/act/public/2007/97/en/latest/sections/DLM1519810/), [s RC 10B](https://www.legislation.govt.nz/act/public/2007/97/en/latest/sections/LMS42733/), [IRD AIM](https://www.ird.govt.nz/aim).
- **Joining:** choose by the first AIM instalment date, or switch from standard or ratio during the year after meeting the prior obligations under that method. For the first remaining date, calculate year-to-date AIM provisional tax and deduct the provisional tax already paid under the earlier method. Approval to continue above $5 million requires gross income of $5 million or less in the first AIM year, unless the taxpayer qualifies with a large-business AIM system. A transitional year is ineligible. [Income Tax Act, s RC 5(5B)–(5C)](https://www.legislation.govt.nz/act/public/2007/97/en/latest/sections/DLM1519810/), [s RC 10B](https://www.legislation.govt.nz/act/public/2007/97/en/latest/sections/LMS42733/).
- **Each new year** the account switches back to the standard option until the first statement of activity for that year is filed.
- Inland Revenue contacts taxpayers after 2 missed activity statements. More than 2 missed statements in the tax year disqualify the taxpayer. If they cease to qualify during the year, apply estimation for the whole year and assess interest on that basis. [Income Tax Act, s RC 5(5B)(g), (5C)](https://www.legislation.govt.nz/act/public/2007/97/en/latest/sections/DLM1519810/), [IRD AIM](https://www.ird.govt.nz/aim).

### Ratio option

| Rule | Figure | Source |
| --- | --- | --- |
| Previous year's RIT must be greater than | $5,000 | [IRD ratio option](https://www.ird.govt.nz/income-tax/provisional-tax/provisional-tax-options/ratio-option): "greater than $5,000 and up to $150,000" |
| ... and up to | $150,000 | same |
| Ratio percentage IRD calculates must be between 0 and | 100% | same: "between 0 and 100%" |
| Fixed-asset sale adjustment: asset value at least the larger of | $1,000 or 5% of taxable supplies for the previous 12 months | [IR289](https://www.ird.govt.nz/-/media/project/ir/home/documents/forms-and-guides/ir200---ir299/ir289/ir289.pdf) |

- **All conditions:** in business and registered for GST for the whole of the previous year and part of the year before; RIT in the range above; GST filed monthly or 2-monthly; not a partnership; ratio in range.
- **Election:** in writing, in myIR or by phone, before the start of the income year. The 2026-27 election had to reach Inland Revenue by 31 March 2026. The earliest start for a new election now is 2027-28. [IRD ratio option](https://www.ird.govt.nz/income-tax/provisional-tax/provisional-tax-options/ratio-option).
- **The ratio:** Inland Revenue divides prior-year RIT by that year’s GST-inclusive taxable supplies, rounded down to 1 decimal place. Section RC 8 specifies substitute years if base amounts are unknown. Multiply the rate by GST-inclusive supplies for the relevant 2 months and truncate to whole dollars. Monthly GST filers add the current and previous periods’ supplies. An updated ratio applies to instalment dates occurring 30 days after notification. [Income Tax Act, s RC 8](https://www.legislation.govt.nz/act/public/2007/97/en/latest/sections/DLM1519816/), [s RC 9(13)](https://www.legislation.govt.nz/act/public/2007/97/en/latest/sections/DLM1519822/), [s RC 11](https://www.legislation.govt.nz/act/public/2007/97/en/latest/sections/DLM1519833/).
- **When to stop:** GST deregistration, a shift to 6-month filing or a new or amended assessment that makes the taxpayer ineligible, including RIT of $5,000 or less or above $150,000. If a GST return is still unfiled after 60 days from the due date, stop unless Inland Revenue approves continued use under RC 17(4). Before instalment A, an obliged taxpayer can use standard or estimation. After an instalment, use estimation for the remaining dates unless eligible for another permitted switch. For the ratio period, determine the UOMI date from the later of the day after notification or statutory cessation and the day after the last ratio instalment. For the estimation period, test the instalments after the 30-day exclusion and apply the ordinary day-after rule. [Income Tax Act, s RC 17](https://www.legislation.govt.nz/act/public/2007/97/en/latest/sections/DLM1519848/), [s RC 18](https://www.legislation.govt.nz/act/public/2007/97/en/latest/sections/DLM1519850/), [Tax Administration Act, s 120KE(5)–(7)](https://www.legislation.govt.nz/act/public/1994/166/en/latest/sections/DLM355315/).

### Instalment dates (31 March balance date)

| Option | Instalments | 2026-27 dates | Source |
| --- | --- | --- | --- |
| Standard or estimation | 3 | 28 August 2026, 15 January 2027, 7 May 2027 | [IRD payment dates](https://www.ird.govt.nz/income-tax/provisional-tax/paying-your-provisional-tax/payment-dates-for-provisional-tax) |
| Standard or estimation, 6-monthly GST filer | 2 | 28 October 2026, 7 May 2027 | [IR289](https://www.ird.govt.nz/-/media/project/ir/home/documents/forms-and-guides/ir200---ir299/ir289/ir289.pdf) |
| Ratio | 6 | 28 June 2026, 28 August 2026, 28 October 2026, 15 January 2027, 28 February 2027, 7 May 2027 | [IRD payment dates](https://www.ird.govt.nz/income-tax/provisional-tax/paying-your-provisional-tax/payment-dates-for-provisional-tax) |
| AIM, monthly GST filer | 12 | the 28th of each month from May to November, then 15 January, 28 January, 28 February, 28 March and 7 May | same |
| AIM, 6-monthly GST filer or unregistered | 6 | the ratio dates above | [Income Tax Act, s RC 9(4B)(a)](https://www.legislation.govt.nz/act/public/2007/97/en/latest/sections/DLM1519822/) |
| AIM, 2-monthly GST filer | 6 | use the GST return dates for the filer’s cycle. The other statutory cycle is 28 July, 28 September and 28 November 2026, then 28 January, 28 March and 28 May 2027 | [Income Tax Act, s RC 9(4B)(b)](https://www.legislation.govt.nz/act/public/2007/97/en/latest/sections/DLM1519822/), [Schedule 3 Part A](https://www.legislation.govt.nz/act/public/2007/97/en/latest/parts/DLM1523173/) |

- **The pattern.** 28 August, 15 January and 7 May is the standard pattern. The third instalment falls after the 31 March year end, by design.
- **GST-ratio months.** Ratio and 2-monthly AIM instalments fall on the 2-monthly GST return dates. Monthly AIM filers pay with every monthly GST return.
- **Weekends and holidays.** A due date on a weekend or public holiday can be met the next working day. In 2026-27 this moves 28 June to 29 June, 28 November to 30 November, 28 February to 1 March, and Easter Sunday 28 March to Tuesday 30 March, as applicable to the instalment cycle. [IRD IR328 2026-27 calendar](https://www.ird.govt.nz/-/media/project/ir/home/documents/forms-and-guides/ir300---ir399/ir328/ir328-2026-27.pdf), [Legislation Act, s 55](https://www.legislation.govt.nz/act/public/2019/0058/latest/LMS274714.html).
- **Other balance dates:** IRD's page says to check the dates in myIR (income tax tile, "View" provisional tax). AIM software works out its own dates.
- **Payments** go to the earliest unpaid instalment, and the provisional tax owed includes any late payment penalties charged ([IRD paying your provisional tax](https://www.ird.govt.nz/income-tax/provisional-tax/paying-your-provisional-tax)). Tax pooling can be used with the standard, estimation and ratio options.

## Use-of-money interest

UOMI is interest, not a penalty. IRD works it out daily, it does not compound, and IRD works it out after the return is filed ([IRD UOMI rates](https://www.ird.govt.nz/managing-my-tax/penalties-and-interest/interest-on-overpayments-and-underpayments)).

| Rate in force from | IRD charges (underpaid) | IRD pays (overpaid) | Source |
| --- | --- | --- | --- |
| 16 January 2026 (current at 22 November 2026) | 8.97% | 2.25% | [IRD UOMI rates](https://www.ird.govt.nz/managing-my-tax/penalties-and-interest/interest-on-overpayments-and-underpayments) |
| 8 May 2025 to 15 January 2026 | 9.89% | 3.27% | same |
| 16 January 2025 to 7 May 2025 | 10.88% | 4.30% | same |

Use the rate in force on each day. The 16 January 2026 rates continue under s 227I until a determination under s 120H applies. Formula for a constant rate and balance is unpaid or overpaid tax × annual rate × days ÷ 365. Include applicable late payment penalties in the balance and count both first and last interest days. [Tax Administration Act, s 120H](https://www.legislation.govt.nz/act/public/1994/166/en/latest/sections/DLM355158/), [2026 amending Act, s 212, inserting s 227I](https://www.legislation.govt.nz/act/public/2007/97/en/latest/LMS1443274/), [s 120E](https://www.legislation.govt.nz/act/public/1994/166/en/latest/sections/DLM355143/).

| Rule | Figure | Source |
| --- | --- | --- |
| Standard option "safe harbour": RIT under this means interest only from the day after the terminal tax date | $60,000 | [IRD interest on provisional tax](https://www.ird.govt.nz/income-tax/provisional-tax/interest-on-provisional-tax): "If your residual income tax (RIT) is less than $60,000" |
| No interest charged or paid on an under- or overpayment of this or less | $100 | same: "under or overpay by $100 or less" |

### Exposure by option ([IRD interest on provisional tax](https://www.ird.govt.nz/income-tax/provisional-tax/interest-on-provisional-tax))

| Option | Interest |
| --- | --- |
| Standard, RIT under $60,000 | Interest from the day after terminal tax, including where instalments were late or short. The concession requires no estimation, AIM, ratio or interest avoidance arrangement. Late payment penalties can still apply. [Tax Administration Act, s 120KE](https://www.legislation.govt.nz/act/public/1994/166/en/latest/sections/DLM355315/) |
| Standard, RIT $60,000 or more | From the day after the final instalment date on the gap between RIT and provisional tax paid. For a late or short earlier instalment, use the lower of (a) the instalment due less payment and (b) RIT divided by the number of instalments, less payment. Treat a negative earlier shortfall as zero. A negative final amount is overpaid tax, including if an earlier instalment was short. No credit interest under this concession before the last instalment. [Tax Administration Act, s 120KBB](https://www.legislation.govt.nz/act/public/1994/166/en/latest/sections/DLM7227374/), [s 120VC](https://www.legislation.govt.nz/act/public/1994/166/en/latest/sections/DLM7227703/) |
| Estimation | On any shortfall against actual RIT from the day after each instalment date, even if paid in full and on time. Credit interest from each payment date, or from the first day of the year for earlier payments. |
| AIM | None if paid in full and on time; no credit interest on overpayments. Late or short payments: interest and penalties from the day after the due date. |
| Ratio, used for the full year | None charged or paid on provisional tax. Interest if more than $100 is owed after the terminal tax date. |

- **Extension of time:** where last year's return was not filed by an instalment date and there is an EOT, the amount that "should have been paid" for that instalment is the lesser of the 10% uplift amount and the 5% uplift amount. This does not apply to the final instalment ([IR289](https://www.ird.govt.nz/-/media/project/ir/home/documents/forms-and-guides/ir200---ir299/ir289/ir289.pdf)).
- **The standard-option rules do not apply** to associated persons where one is a company and they are not all on the standard or ratio option, or to a provisional tax interest avoidance arrangement. A switch from standard to estimation is treated as estimation for the full year.
- **Tax treatment:** UOMI payable to Inland Revenue is deductible under the specific deduction. It overrides the capital, private and employment limitations. Apply the timing and other general limitations. UOMI received is income. Check the timing of a reassessment. [Income Tax Act, s DB 3B](https://www.legislation.govt.nz/act/public/2007/97/en/latest/sections/DLM3996301/), [s CC 4](https://www.legislation.govt.nz/act/public/2007/97/en/latest/sections/DLM1512514/), [IRD UOMI](https://www.ird.govt.nz/managing-my-tax/penalties-and-interest/interest-on-overpayments-and-underpayments).
- **Remission** is limited, for example where IRD's wrong advice caused the problem.

## Penalties

| Penalty (current rules; no tax year) | Figure | Source |
| --- | --- | --- |
| Late payment: the day after the due date | 1% | [IRD late payment penalties](https://www.ird.govt.nz/managing-my-tax/penalties-and-interest/penalties-and-debt/late-payment-penalties): "1% penalty on the day after payment due date" |
| Late payment: on the 7th day after the due date, on the remaining tax including penalties | 4% | same: "4% penalty for remaining tax including penalties" |
| Monthly penalty: does NOT apply to income tax, including provisional tax | 1% every month | same: "except for GST, income tax including provisional tax" |

- The first-default 2-year grace rule excludes unpaid provisional tax and related penalties. A qualifying instalment arrangement can stop some penalties. [Tax Administration Act, s 139B(1)](https://www.legislation.govt.nz/act/public/1994/166/en/latest/sections/DLM356138/).
- Late payment penalties can apply to late or short instalments under every option, including the standard option inside the safe harbour. They do not apply where tax outstanding after the due date is $100 or less. [Tax Administration Act, s 183F(1)(a)](https://www.legislation.govt.nz/act/public/1994/166/en/latest/sections/DLM358771/).
- Penalties are not deductible for income tax or GST (IR289).

**Shortfall penalties (AIM or estimation)** can apply to the tax shortfall when the statutory conditions for the relevant behaviour are met.

| Behaviour | Rate | Source |
| --- | --- | --- |
| Not taking reasonable care | 20% | [IR289](https://www.ird.govt.nz/-/media/project/ir/home/documents/forms-and-guides/ir200---ir299/ir289/ir289.pdf) |
| Unacceptable tax position, subject to statutory conditions | 20% | [Tax Administration Act, s 141B](https://www.legislation.govt.nz/act/public/1994/166/en/latest/sections/DLM356435/). The shortfall must exceed both $50,000 and 1% of the taxpayer’s relevant total tax figure. |
| Gross carelessness | 40% | same |
| Abusive tax position | 100% | same |
| Evasion | 150% | same |

**Late filing penalty on the income tax return:** see `nz-income-tax-ir3`. A late return does not delay the instalments; under the standard option without an EOT the 5% uplift still applies ([IRD standard option](https://www.ird.govt.nz/income-tax/provisional-tax/provisional-tax-options/standard-option)).

## Boundary and exception table

| Situation | Treatment | Source |
| --- | --- | --- |
| Last year's RIT exactly $5,000 | Not compulsory: the test is "more than $5,000" | [IRD provisional tax](https://www.ird.govt.nz/income-tax/provisional-tax) |
| Standard option, RIT exactly $60,000 | "$60,000 or more": interest from the day after the final instalment date | [IRD interest on provisional tax](https://www.ird.govt.nz/income-tax/provisional-tax/interest-on-provisional-tax) |
| Under- or overpayment of exactly $100 | No interest ("$100 or less") | same |
| No EOT, return filed late | Still last year's RIT + 5%; never the 10% uplift | [IRD standard option](https://www.ird.govt.nz/income-tax/provisional-tax/provisional-tax-options/standard-option) |
| EOT, 2-years-ago RIT $5,000 or less | Nothing on that basis; pay in 1 or 2 even instalments | [IR289](https://www.ird.govt.nz/-/media/project/ir/home/documents/forms-and-guides/ir200---ir299/ir289/ir289.pdf) |
| Two instalment dates | Only 6-monthly GST filers have 2 dates (28 October, 7 May). An EOT never changes the dates; with an EOT and a 2-years-ago RIT of $5,000 or less, the tax falls on the 1 or 2 dates still due, split evenly (row above) | same |
| Standard to ratio mid-year | Not allowed; ratio must be elected before the year starts | [IRD standard option](https://www.ird.govt.nz/income-tax/provisional-tax/provisional-tax-options/standard-option) |
| Estimation back to standard | Not allowed in the same year | [IR289](https://www.ird.govt.nz/-/media/project/ir/home/documents/forms-and-guides/ir200---ir299/ir289/ir289.pdf) |
| Ratio, previous RIT exactly $150,000 | Allowed ("up to $150,000"); exactly $5,000 is not ("greater than") | [IRD ratio option](https://www.ird.govt.nz/income-tax/provisional-tax/provisional-tax-options/ratio-option) |
| Partnership wanting ratio | Not allowed | same |
| AIM turnover passes $5 million in the year | May ask IRD to stay on AIM | [IR289](https://www.ird.govt.nz/-/media/project/ir/home/documents/forms-and-guides/ir200---ir299/ir289/ir289.pdf) |
| Choosing to pay, exactly $5,000 paid by 7 May | The election requires payment above $5,000 by the final instalment date. | [Income Tax Act, s RC 4](https://www.legislation.govt.nz/act/public/2007/97/en/latest/sections/DLM1519807/) |
| Company or trust in its first year | No early payment discount | [IRD first year in business](https://www.ird.govt.nz/income-tax/provisional-tax/paying-tax-in-your-first-year-in-business) |

## Worked cases

### Source: [IR289](https://www.ird.govt.nz/-/media/project/ir/home/documents/forms-and-guides/ir200---ir299/ir289/ir289.pdf) for IRD's examples, unless another link is shown

Where the historical Inland Revenue examples differ from the statutory calculation, the cases below use the statutory figures. C1, C8 and C10 are illustrations.

**C1. Standard option, 2026-27.** 2025-26 RIT $12,000, return filed 7 July 2026, no EOT, 2-monthly GST filer. Provisional tax = $12,000 + 5% = $12,600, paid as $4,200 on each of 28 August 2026, 15 January 2027 and 7 May 2027 ([IRD work out standard option](https://www.ird.govt.nz/income-tax/provisional-tax/provisional-tax-options/standard-option/work-out-provisional-tax-using-the-standard-option)).

```oa-check
name: Standard option, 2026-27
inputs:
  rit: 12000
steps:
  - provisional: rit * 1.05
  - instalment: provisional / 3
expected:
  provisional: 12600.00
  instalment: 4200.00
```

**C2. Extension of time, catch-up.** For 2023-24, the company’s 2022 RIT was $24,000. The 110% uplift gives $26,400. The company owes $8,800 each on 28 August 2023 and 15 January 2024. The 2023 return filed 23 January 2024 shows RIT of $23,740. Final liability on 7 May 2024 is $23,740 × 105% − $17,600 = $7,327. [Income Tax Act, s RC 5](https://www.legislation.govt.nz/act/public/2007/97/en/latest/sections/DLM1519810/), [s RC 10](https://www.legislation.govt.nz/act/public/2007/97/en/latest/sections/DLM1519824/).

**C3. EOT with a low 2-years-ago RIT, then a switch to estimation.** The taxpayer’s 2023 RIT was below $5,000. The 2024 return with an EOT was filed after 28 August 2024 and by 15 January 2025. On standard, $0 was due on 28 August. The 105% total of $24,600 gives $12,300 each on 15 January and 7 May. A 1 December estimate of $15,000 gives $7,500 on each of the two remaining dates. Actual RIT of $9,000 gives $3,000 per instalment for interest. The missing first instalment carries debit interest on $3,000 from 29 August until covered. [Income Tax Act, s RC 13](https://www.legislation.govt.nz/act/public/2007/97/en/latest/sections/DLM1519839/), [Tax Administration Act, s 120KB](https://www.legislation.govt.nz/act/public/1994/166/en/latest/sections/DLM355312/).

**C4. Standard option, a missed instalment.** Of $24,000 provisional tax ($8,000 each), only the first instalment was paid. Actual RIT was $66,000. The second instalment shortfall uses the lower of $8,000 and $22,000 ($66,000 ÷ 3). At the final date the tax principal is $58,000 ($66,000 − $8,000). In a non-leap year the periods 16 January to 7 May and 8 May to 9 September are 112 and 125 days inclusive. At a flat 8.97% for illustration, UOMI on the tax principal alone is $220.20 and $1,781.71 respectively. Include the penalties in the interest balance from their applicable dates. Each missed instalment accrues $80 (1% × $8,000) and $323.20 (4% × $8,080), giving $403.20 each and $806.40 in total. [Tax Administration Act, s 120KBB](https://www.legislation.govt.nz/act/public/1994/166/en/latest/sections/DLM7227374/), [s 120E](https://www.legislation.govt.nz/act/public/1994/166/en/latest/sections/DLM355143/), [s 139B](https://www.legislation.govt.nz/act/public/1994/166/en/latest/sections/DLM356138/).

**C5. Late payment penalties.** $7,600 due 7 May, paid 10 July: 1% on 8 May ($76.00, balance $7,676.00), then 4% on 14 May ($307.04, balance $7,983.04). Total penalties $383.04, with no further monthly penalty.

**C6. Estimation and re-estimation.** Estimated RIT is $59,371.50. The first third is $19,790.50, truncated to $19,790. The second is $39,581 less $19,790 = $19,791. A February re-estimate of $65,000 reduces the final calculation by the $39,581 already due, leaving $25,419. [Income Tax Act, s RC 10(2), (7)](https://www.legislation.govt.nz/act/public/2007/97/en/latest/sections/DLM1519824/).

**C7. Ratio option.** RIT of $51,000 divided by $2,114,723 of GST-inclusive taxable supplies gives approximately 2.411663%, rounded down to 2.4%. On April-May 2019 supplies of $725,111, the calculation gives $17,402.664. The whole-dollar instalment is $17,402, due 28 June 2019. [Income Tax Act, s RC 9(13)](https://www.legislation.govt.nz/act/public/2007/97/en/latest/sections/DLM1519822/), [s RC 11](https://www.legislation.govt.nz/act/public/2007/97/en/latest/sections/DLM1519833/).

**C8. Early payment discount, 2026-27.** An eligible first-year sole trader pays $5,000 voluntarily by 31 March 2027, holds the required credit and claims on time. For RIT of $8,000, 105% is $8,400. The lower amount is $5,000, giving $212.50 at 4.25%. [Income Tax Act, s RC 38](https://www.legislation.govt.nz/act/public/2007/97/en/latest/sections/DLM1519922/), [IRD first year in business](https://www.ird.govt.nz/income-tax/provisional-tax/paying-tax-in-your-first-year-in-business).

```oa-check
name: Early payment discount, 2026-27
inputs:
  voluntary: 5000
  rit: 8000
  rate: 0.0425
steps:
  - base: min(voluntary, rit * 1.05)
  - discount: base * rate
expected:
  discount: 212.50
```

**C9. First and second years in business.** First-year RIT is $75,000 and no voluntary tax was paid. The following year’s standard provisional tax is $75,000 × 105% = $78,750, or $26,250 on each of 3 ordinary dates. The $75,000 terminal tax and those provisional instalments are scheduled in the same year. Test first-year interest separately if the initial provisional tax liability rules apply. [Income Tax Act, s RC 5](https://www.legislation.govt.nz/act/public/2007/97/en/latest/sections/DLM1519810/), [Tax Administration Act, s 120KC](https://www.legislation.govt.nz/act/public/1994/166/en/latest/sections/DLM355313/).

**C10. New provisional taxpayer.** An employee leaves work to derive taxable activity income without deduction on 1 September 2026. Each of the preceding 4 years has RIT of $5,000 or less. With actual 2026-27 RIT of $60,000, a 31 March balance date and no 6-monthly GST cycle, interest is calculated on deemed $30,000 instalments on 15 January and 7 May 2027. Debit interest starts on 16 January and 8 May on amounts unpaid. [Income Tax Act, s RC 13](https://www.legislation.govt.nz/act/public/2007/97/en/latest/sections/DLM1519839/), [Tax Administration Act, s 120KC](https://www.legislation.govt.nz/act/public/1994/166/en/latest/sections/DLM355313/).

## When to refuse or refer

- **Balance date other than 31 March, a change of balance date or a transitional year:** dates and amounts differ, and IRD must approve the change. Get the dates from myIR or IRD; do not guess.
- **Tax pooling:** its own rules; outside this skill.
- **Multi-entity groups, associated companies on mixed options, or any interest avoidance arrangement:** the standard-option interest rules may not apply. Refer.
- **Non-residents:** outside this skill.
- **Shortfall penalty exposure** (an estimate far below actual RIT), remission requests or disputes: refer to a New Zealand chartered accountant or tax agent.
- **A client who cannot pay:** tell them to contact IRD before the due date about an instalment arrangement.
- Where the applicable instalment or credit depends on the dates of an assessment, election, switch or payment, obtain those dates before calculating.
- Working out the income tax itself: `nz-income-tax-ir3`. GST returns and filing frequency: `nz-gst-return`. ACC levies: `nz-acc-levies`.

## Filing and payment

### The 2025-26 year being finished now

- **Year:** 1 April 2025 to 31 March 2026 (IRD's 2026 income year). Its provisional tax instalments fell on 28 August 2025, 15 January 2026 and 7 May 2026.
- **Return:** due 7 July 2026 without an extension of time. A tax agent's client with an EOT can file up to 31 March 2027 ([IRD extension of time](https://www.ird.govt.nz/topics/intermediaries/extension-of-time-arrangements)).
- **Terminal tax:** 7 February 2027, or 7 April 2027 for tax agents' clients with a valid extension of time ([IRD IR328 2026-27 calendar](https://www.ird.govt.nz/-/media/project/ir/home/documents/forms-and-guides/ir300---ir399/ir328/ir328-2026-27.pdf)). 7 February 2027 is a Sunday, and the calendar shows 8 February 2027 as the Waitangi Day day off, so payment on 9 February 2027 is on time.
- **Interest:** UOMI on 2025-26 is worked out when the return is filed, at the rates in force on each day; the rate changed on 16 January 2026 (see the UOMI table).
- **It also sets 2026-27:** the 2025-26 RIT is "last year's RIT" for the 2026-27 standard option and the entry test ([IRD provisional tax](https://www.ird.govt.nz/income-tax/provisional-tax)).

### 2026-27 dates (31 March balance date)

| Item | Date |
| --- | --- |
| Instalments | see "Instalment dates" |
| 2026-27 return, no EOT | 7 July 2027 |
| 2026-27 return, tax agent's EOT | up to 31 March 2028 |
| 2026-27 terminal tax | 7 February 2028, or 7 April 2028 with a tax agent's EOT. Waitangi Day (6 February 2028) is a Sunday, so the Monday 7 February 2028 is the holiday. Payment can be made on Tuesday 8 February 2028. [Legislation Act, s 55](https://www.legislation.govt.nz/act/public/2019/0058/latest/LMS274714.html) |

Sources: [IRD payment dates](https://www.ird.govt.nz/income-tax/provisional-tax/paying-your-provisional-tax/payment-dates-for-provisional-tax), [IR289](https://www.ird.govt.nz/-/media/project/ir/home/documents/forms-and-guides/ir200---ir299/ir289/ir289.pdf), [IRD interest on provisional tax](https://www.ird.govt.nz/income-tax/provisional-tax/interest-on-provisional-tax) (7 February, or 7 April with an agent's EOT) and [IRD extension of time](https://www.ird.govt.nz/topics/intermediaries/extension-of-time-arrangements).

- **How to pay:** online through myIR or by the other methods on IRD's payment pages. GST-registered ratio and AIM filers pay with their GST return (GST103B form series).
- **Bank statement coding:** a debit to Inland Revenue on or just after 28 August, 15 January or 7 May (or 28 October for 6-monthly GST filers, or the GST dates for ratio or AIM) is usually a provisional tax instalment. A debit around 7 February (or 7 April) is usually terminal tax. A debit on 7 May may be GST, not provisional tax. These debits are not provisional tax: GST, ACC levies, student loan repayments, KiwiSaver, child support, and penalty or interest charges. Always confirm against the myIR statement. Provisional tax, terminal tax and penalties are not deductible expenses. UOMI payable may be deductible under the specific rule in s DB 3B.

## Completion checklist

- [ ] Last year's RIT confirmed from the return and tested as "more than" the entry threshold.
- [ ] New provisional taxpayer rule checked for a new business or a move off wages.
- [ ] Option and its entry conditions confirmed; any switch this year allowed.
- [ ] Standard option: EOT status, return filing date and uplift for each instalment checked.
- [ ] Number of instalments and 2026-27 dates right for the option and GST frequency.
- [ ] Interest exposure stated, with the UOMI rate in force on each day re-checked.
- [ ] Late payment penalties limited to the two stages; no monthly penalty.
- [ ] Early payment discount considered for eligible first-year individuals.
- [ ] Terminal tax date given.
- [ ] Output labelled as an estimate for a New Zealand tax agent or chartered accountant to confirm.

## Sources

| Source | URL | Read |
| --- | --- | --- |
| IRD provisional tax. Read for Scope, The method, step by step, Who must pay | https://www.ird.govt.nz/income-tax/provisional-tax | 2026-11-14 |
| IR289. Read for Scope, Who must pay, Choosing to pay | https://www.ird.govt.nz/-/media/project/ir/home/documents/forms-and-guides/ir200---ir299/ir289/ir289.pdf | 2026-11-14 |
| IRD extension of time. Read for Scope, The 2025-26 year being finished now, 2026-27 dates (31 March balance date) | https://www.ird.govt.nz/topics/intermediaries/extension-of-time-arrangements | 2026-11-14 |
| IRD interest on provisional tax. Read for The method, step by step, Who must pay, Estimation option | https://www.ird.govt.nz/income-tax/provisional-tax/interest-on-provisional-tax | 2026-11-14 |
| IRD standard option. Read for The method, step by step, Standard option (the default), Penalties | https://www.ird.govt.nz/income-tax/provisional-tax/provisional-tax-options/standard-option | 2026-11-14 |
| IRD work out standard option. Read for The method, step by step, Standard option (the default), Source: [IR289](https://www.ird.govt.nz/-/media/project/ir/home/documents/forms-and-guides/ir200---ir299/ir289/ir289.pdf) for IRD's examples, unless another link is shown | https://www.ird.govt.nz/income-tax/provisional-tax/provisional-tax-options/standard-option/work-out-provisional-tax-using-the-standard-option | 2026-11-14 |
| IRD late payment penalties. Read for The method, step by step, Penalties, Source: [IR289](https://www.ird.govt.nz/-/media/project/ir/home/documents/forms-and-guides/ir200---ir299/ir289/ir289.pdf) for IRD's examples, unless another link is shown | https://www.ird.govt.nz/managing-my-tax/penalties-and-interest/penalties-and-debt/late-payment-penalties | 2026-11-14 |
| QB 19/04. Read for Who must pay | https://www.taxtechnical.ird.govt.nz/-/media/project/ir/tt/pdfs/questions-we-ve-been-asked/2019/qb19-04.pdf | 2026-11-14 |
| IRD first year in business. Read for Who must pay, Early payment discount (first-year businesses), Boundary and exception table | https://www.ird.govt.nz/income-tax/provisional-tax/paying-tax-in-your-first-year-in-business | 2026-11-14 |
| IRD choosing to be a provisional taxpayer. Read for Choosing to pay, Boundary and exception table | https://www.ird.govt.nz/income-tax/provisional-tax/choosing-to-be-a-provisional-tax-payer | 2026-11-14 |
| IRD UOMI rates. Read for Early payment discount (first-year businesses), Use-of-money interest, Exposure by option | https://www.ird.govt.nz/managing-my-tax/penalties-and-interest/interest-on-overpayments-and-underpayments | 2026-11-14 |
| IRD estimation option. Read for Estimation option | https://www.ird.govt.nz/income-tax/provisional-tax/provisional-tax-options/estimation-option | 2026-11-14 |
| IRD work out estimation option. Read for Estimation option | https://www.ird.govt.nz/income-tax/provisional-tax/provisional-tax-options/estimation-option/work-out-provisional-tax-using-the-estimation-option | 2026-11-14 |
| IRD AIM. Read for Accounting income method (AIM) | https://www.ird.govt.nz/aim | 2026-11-14 |
| IRD ratio option. Read for Ratio option, Boundary and exception table | https://www.ird.govt.nz/income-tax/provisional-tax/provisional-tax-options/ratio-option | 2026-11-14 |
| IRD work out ratio option. Read for Ratio option | https://www.ird.govt.nz/income-tax/provisional-tax/provisional-tax-options/ratio-option/work-out-provisional-tax-using-the-ratio-option | 2026-11-14 |
| IRD payment dates. Read for Instalment dates (31 March balance date), 2026-27 dates (31 March balance date) | https://www.ird.govt.nz/income-tax/provisional-tax/paying-your-provisional-tax/payment-dates-for-provisional-tax | 2026-11-14 |
| IRD IR328 2026-27 calendar. Read for Instalment dates (31 March balance date), The 2025-26 year being finished now | https://www.ird.govt.nz/-/media/project/ir/home/documents/forms-and-guides/ir300---ir399/ir328/ir328-2026-27.pdf | 2026-11-14 |
| IRD paying your provisional tax. Read for Instalment dates (31 March balance date) | https://www.ird.govt.nz/income-tax/provisional-tax/paying-your-provisional-tax | 2026-11-14 |

Not yet confirmed: none beyond the points this skill refers out.

## Today's figures and who stands behind this skill

This file is an AI skill (tax rules your AI follows) from OpenAccountants, copied on 2026-11-14. Rates, thresholds and deadlines change. For the current version of this skill, its official sources and the named accountant (if any) who stands behind it, call `get_skill` with slug `nz-provisional-tax` on the OpenAccountants connector (https://www.openaccountants.com/connect), or read https://www.openaccountants.com/skills/nz-provisional-tax. If neither is available, confirm every figure against the official source pages cited above before relying on it.
