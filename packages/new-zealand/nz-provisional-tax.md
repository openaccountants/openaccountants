---
name: nz-provisional-tax
description: Use this skill whenever asked about New Zealand provisional tax for individuals, companies, contractors, sole traders, and small businesses. Trigger on phrases like "provisional tax", "RIT", "residual income tax", "standard option", "standard uplift", "estimation method", "AIM", "ratio option", "use of money interest", "UOMI", "provisional tax instalment", or any question about provisional tax obligations in New Zealand. Covers the $5,000 RIT threshold, standard option 105%/110% uplift rules, estimation, AIM, ratio-option routing, March balance-date instalments, 6-monthly GST two-instalment cases, and current UOMI rate handling. ALWAYS read this skill before touching any NZ provisional tax work.
version: 2.0
jurisdiction: NZ
tax_year: 2026
last_updated: 2026-09-27
authored_by: Michael Cutajar and the OpenAccountants team
review_status: pending_review
trust_label: Built by Michael Cutajar and the OpenAccountants team
depends_on:
  - income-tax-workflow-base
category: international
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# New Zealand provisional tax

## Scope

Provisional tax is income tax paid in instalments during the year instead of one lump sum after it ([IRD provisional tax](https://www.ird.govt.nz/income-tax/provisional-tax)). It is not a separate tax. This Guide covers who must pay, the four options (standard, estimation, ratio and the accounting income method, AIM), instalment dates, use-of-money interest (UOMI) and penalties, for individuals, sole traders, contractors, landlords, partners, companies and trusts.

- **Primary year:** the 2026-27 income year, 1 April 2026 to 31 March 2027 (Inland Revenue calls it the 2027 income year), for a 31 March balance date.
- **Also covered:** the 2025-26 year (1 April 2025 to 31 March 2026), whose returns are being filed and whose end-of-year tax is due in 2027 (see "Filing and payment").
- **Law:** Income Tax Act 2007 (provisional tax rules, Part RC; IRD's QB 19/04 cites ss RC 3(3) and RC 9(9)) and Tax Administration Act 1994 (interest rules, including ss 120KC and 120KE, cited in QB 19/04), as explained by Inland Revenue (IRD). The Acts on legislation.govt.nz could not be read for this revision, so any point that rests only on the statute is marked **check**.
- **Not covered:** working out the income tax itself (see `nz-income-tax-ir3`), GST returns (see `new-zealand-gst`), ACC levies (see `nz-acc-levies`), tax pooling, multi-entity groups and non-residents.

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

1. **Is provisional tax compulsory?** If RIT on the last return was more than $5,000, yes ([IRD provisional tax](https://www.ird.govt.nz/income-tax/provisional-tax)). If it was $5,000 or less, it is not, unless the new provisional taxpayer rule applies (step 2). A person can also choose to be a provisional taxpayer (see "Choosing to pay").
2. **New provisional taxpayer check.** Someone who has not paid before must still deal with provisional tax this year if current-year RIT is $60,000 or more and the start-of-business conditions in "Who must pay" are met ([IRD interest on provisional tax](https://www.ird.govt.nz/income-tax/provisional-tax/interest-on-provisional-tax)).
3. **Choose the option and check its conditions.** Standard applies unless another is chosen ([IRD standard option](https://www.ird.govt.nz/income-tax/provisional-tax/provisional-tax-options/standard-option)). Estimation suits falling or uncertain income. AIM and ratio suit uneven or seasonal income but have entry conditions.
4. **Work out each instalment.** Standard: pick the uplift for each instalment from the filing date of last year's return and whether there is an EOT, then use IRD's catch-up formulas ([IRD work out standard option](https://www.ird.govt.nz/income-tax/provisional-tax/provisional-tax-options/standard-option/work-out-provisional-tax-using-the-standard-option)). Estimation: estimated RIT divided by the instalments left. Ratio: IRD's ratio percentage times the GST taxable supplies for the period. AIM: the software's figure.
5. **Diary the dates** for the option and GST filing frequency (see "Instalment dates"). A due date on a weekend or public holiday can be met on the next business day.
6. **Test the interest exposure** against the safe harbour and the option rules in "Use-of-money interest", using the UOMI rate in force on each day ([IRD interest on provisional tax](https://www.ird.govt.nz/income-tax/provisional-tax/interest-on-provisional-tax)).
7. **Check penalties** for any late or short instalment: 1% the day after the due date and 4% on the 7th day after, with no further monthly penalty on provisional tax ([IRD late payment penalties](https://www.ird.govt.nz/managing-my-tax/penalties-and-interest/penalties-and-debt/late-payment-penalties)).
8. **After the year:** RIT less provisional tax paid is terminal tax, due 7 February after the year ends, or 7 April with a tax agent's extension of time. The same return sets next year's RIT for step 1.

## 2026-27 figures and rules

The thresholds below are not indexed. IRD's pages show no change for the 2026-27 income year (pages read 27 September 2026); each figure is labelled with the year it is shown for.

### Who must pay

| Rule (2026-27 income year unless stated) | Figure | Source |
| --- | --- | --- |
| Entry test: RIT on the last return must be MORE than | $5,000 | [IRD provisional tax](https://www.ird.govt.nz/income-tax/provisional-tax): "more than $5,000 tax at the end of the year from your last return" |
| New provisional taxpayer: current-year RIT at or above | $60,000 | [IRD interest on provisional tax](https://www.ird.govt.nz/income-tax/provisional-tax/interest-on-provisional-tax): "$60,000 or more" |
| New provisional taxpayer: RIT in each of the last 4 years below | $5,000 | [IRD interest on provisional tax](https://www.ird.govt.nz/income-tax/provisional-tax/interest-on-provisional-tax): "less than $5,000 for the last 4 years" |

- **Exactly $5,000 is not enough.** IRD: "Generally, you will not have to pay provisional tax if your residual income tax (RIT) last year was $5,000 or less" ([IRD interest on provisional tax](https://www.ird.govt.nz/income-tax/provisional-tax/interest-on-provisional-tax)).
- **Who typically pays:** self-employed, rental, contractor, partnership or overseas income; also wrong PAYE codes, untaxed lump sums, employee share scheme income or bright-line sales ([IRD provisional tax](https://www.ird.govt.nz/income-tax/provisional-tax)). Companies and trusts too.
- **New provisional taxpayer, individual** (not a trustee): RIT below $5,000 in each of the last 4 years, current-year RIT of $60,000 or more, and during the year they stopped earning employment income and started earning income from a taxable activity with no tax deducted at source. **Non-individual** (company, trust, trustee): started a taxable activity this year, had no income from a taxable activity in the last 4 years, and current-year RIT of $60,000 or more ([IRD interest on provisional tax](https://www.ird.govt.nz/income-tax/provisional-tax/interest-on-provisional-tax)). IR289 words the 4-year test as "$5,000 or less"; the web page says "less than $5,000". RIT of exactly $5,000 in a prior year is therefore unclear: **check** ([IR289](https://www.ird.govt.nz/-/media/project/ir/home/documents/forms-and-guides/ir200---ir299/ir289/ir289.pdf)).
- **Effect for a new provisional taxpayer:** interest is worked out on 1 to 3 instalments, set by the date the taxable activity started: before 29 July, 3; on or after 29 July but before 16 December, 2; on or after 16 December, 1. Interest runs from the day after the first instalment date after the start, if that date is more than 30 days after the start. Other balance dates and 6-monthly GST filers have other dates (IR289). IRD's [QB 19/04](https://www.taxtechnical.ird.govt.nz/-/media/project/ir/tt/pdfs/questions-we-ve-been-asked/2019/qb19-04.pdf) says such a person should pay in one to three equal instalments to avoid interest.
- **First year in business:** on the standard, estimation or ratio options there is no provisional tax in the first year; on AIM, tax is paid only when there is a profit ([IRD first year in business](https://www.ird.govt.nz/income-tax/provisional-tax/paying-tax-in-your-first-year-in-business)). Two exceptions: the entry test still applies, so provisional tax is due if last year's RIT (for example from rental income or an earlier business) was more than $5,000 ([IRD provisional tax](https://www.ird.govt.nz/income-tax/provisional-tax)); and the new provisional taxpayer rule above. The first year is not tax free: its tax is due by 7 February the following year (7 April with an agent), often alongside the second year's provisional tax. In IRD's Isobel example (C9), first-year RIT of $75,000 means $78,750 of year-2 provisional tax plus the $75,000 end-of-year tax in the same year (IR289).

### Choosing to pay

A person who is not a provisional taxpayer may elect to be one ([IRD choosing to be a provisional taxpayer](https://www.ird.govt.nz/income-tax/provisional-tax/choosing-to-be-a-provisional-tax-payer)). The conditions:

- expect RIT to be more than $5,000 ([IRD choosing](https://www.ird.govt.nz/income-tax/provisional-tax/choosing-to-be-a-provisional-tax-payer));
- have paid at least $5,000 by the final instalment date (7 May for most people). IR289 says "more than $5,000" instead, so a payment of exactly $5,000 is a **check** ([IR289](https://www.ird.govt.nz/-/media/project/ir/home/documents/forms-and-guides/ir200---ir299/ir289/ir289.pdf));
- have been reasonably sure, on the day of the first payment, of being liable for provisional tax;
- ask at the same time as filing that year's return (tick the election in myIR, or attach a letter to a paper return).

When it matters: IR289 frames the election for someone whose RIT "works out to be $5,000 or less" after making voluntary payments, and its effect is that "We may calculate interest on your voluntary payments" ([IR289](https://www.ird.govt.nz/-/media/project/ir/home/documents/forms-and-guides/ir200---ir299/ir289/ir289.pdf)). IR289 also says anyone choosing to be a provisional taxpayer has to use the estimation option, and individuals must estimate on or before the third instalment date to have interest calculated.

### Early payment discount (first-year businesses)

| Rule | Figure | Source |
| --- | --- | --- |
| Discount rate, 2027 income year (2026-27) | 4.25% | [IRD first year in business](https://www.ird.govt.nz/income-tax/provisional-tax/paying-tax-in-your-first-year-in-business): "The early payment discount rate for the 2027 income year is 4.25%" |
| Discount rate, 2026 income year (2025-26) | 6.30% | same page, past rates table |
| Rate formula (from the 2025 income year) | UOMI credit rate at 31 March of the previous year plus 2% | same page |
| Base: the lesser of voluntary payments or this share of the year's RIT | 105% | [IR289](https://www.ird.govt.nz/-/media/project/ir/home/documents/forms-and-guides/ir200---ir299/ir289/ir289.pdf) |

The 2026-27 rate ties out: the UOMI credit rate on 31 March 2026 was 2.25% ([IRD UOMI rates](https://www.ird.govt.nz/managing-my-tax/penalties-and-interest/interest-on-overpayments-and-underpayments)), plus 2% is 4.25%. Who qualifies: self-employed individuals, partners in a partnership and owners of a look-through company whose income comes mainly from the business; companies and trusts do not. The voluntary payment must be made before the end of the income year (tax pooling funds count), the person must have had no obligation to pay provisional tax that year or in any of the 4 years before, and the discount must be claimed by the return's due date. The discount counts as a payment towards RIT.

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
| After 28 August, on or before 15 January | (2-years-ago RIT + 10%) / 3 | (last year's RIT + 5%) x 2 / 3, less the 1st payment | last year's RIT + 5%, less the 1st and 2nd payments |
| After 15 January, on or before 7 May | (2-years-ago RIT + 10%) / 3 | (2-years-ago RIT + 10%) / 3 | last year's RIT + 5%, less the 1st and 2nd payments |
| After 7 May | (2-years-ago RIT + 10%) / 3 | (2-years-ago RIT + 10%) / 3 | expected RIT for last year + 5%, less the 1st and 2nd payments |

- **RIT from 2 years ago of $5,000 or less:** no instalment is due on the 2-years-ago basis. Provisional tax is then paid in 1 or 2 instalments, depending on when the return is filed, split evenly between the instalments still due ([IR289](https://www.ird.govt.nz/-/media/project/ir/home/documents/forms-and-guides/ir200---ir299/ir289/ir289.pdf)). See case C3.
- **Weekend or holiday filing:** if an instalment date is on a weekend or public holiday and the return is filed on the next working day, it counts as filed on the instalment date. That can change the uplift.
- **Reassessment or amendment** of last year's return within 30 days of an instalment date does not change that instalment; the change goes into later instalments. But a return filed within 30 days before an instalment date does set that instalment (IR289).
- **6-monthly GST filers** pay 2 instalments with their GST returns: divide by 2 instead of 3.
- **Final instalment top-up:** a standard-option taxpayer who expects RIT of $60,000 or more and has paid all but the final instalment in full and on time can pay a final instalment that better reflects the year's income and stay on the standard option ([IR289](https://www.ird.govt.nz/-/media/project/ir/home/documents/forms-and-guides/ir200---ir299/ir289/ir289.pdf)).

### Estimation option

| Rule | Figure | Source |
| --- | --- | --- |
| Estimated RIT above this: generally paid in 3 instalments | $60,000 | [IRD estimation option](https://www.ird.govt.nz/income-tax/provisional-tax/provisional-tax-options/estimation-option): "more than $60,000" |
| Lowest estimate allowed | $0 | same page: "you can estimate your provisional tax at $0" |

- Provisional tax is the estimated RIT for the year: expected taxable income, tax on it, less PAYE and other credits ([IRD work out estimation option](https://www.ird.govt.nz/income-tax/provisional-tax/provisional-tax-options/estimation-option/work-out-provisional-tax-using-the-estimation-option)).
- Estimate using myIR's "Estimate provisional tax" service, a myIR message, by phone or in writing, as often as needed up to the final instalment date. A re-estimate adjusts the later instalments to catch up.
- **Switching in:** standard to estimation is allowed at any time up to the final instalment date. After switching, the taxpayer cannot go back to the standard option for that year (IR289), and interest is worked out as if they had estimated for the full year ([IRD interest on provisional tax](https://www.ird.govt.nz/income-tax/provisional-tax/interest-on-provisional-tax)).
- **Risk:** interest runs from the day after each instalment date on any shortfall against the actual RIT, even if every estimated instalment was paid in full and on time. A shortfall penalty is possible if the estimate was unreasonably low.

### Accounting income method (AIM)

| Rule | Figure | Source |
| --- | --- | --- |
| Available to individuals and companies with yearly turnover under | $5 million | [IRD AIM](https://www.ird.govt.nz/aim): "yearly turnover under $5 million" |

- Needs AIM-capable accounting software from an approved provider. The software works out each payment from the period's accounting profit and files a statement of activity. It is not an income tax return. A loss can be refunded straight away ([IRD AIM](https://www.ird.govt.nz/aim)).
- **Joining:** from standard or ratio at any time, if the first statement of activity is filed before the final instalment date and all payments due so far under the current option have been made. From estimation, the first statement of activity must be filed by the first instalment date. Once on AIM for a year, the taxpayer cannot change option until the next year. If turnover passes $5 million during the year, they can ask to stay on AIM. AIM cannot be used in a year the balance date changes ([IR289](https://www.ird.govt.nz/-/media/project/ir/home/documents/forms-and-guides/ir200---ir299/ir289/ir289.pdf)).
- **Each new year** the account switches back to the standard option until the first statement of activity for that year is filed.
- Missing 2 statements of activity brings contact from IRD. Continuing to miss them can move the taxpayer to the estimation option, with interest.

### Ratio option

| Rule | Figure | Source |
| --- | --- | --- |
| Previous year's RIT must be greater than | $5,000 | [IRD ratio option](https://www.ird.govt.nz/income-tax/provisional-tax/provisional-tax-options/ratio-option): "greater than $5,000 and up to $150,000" |
| ... and up to | $150,000 | same |
| Ratio percentage IRD calculates must be between 0 and | 100% | same: "between 0 and 100%" |
| Fixed-asset sale adjustment: asset value at least the larger of | $1,000 or 5% of taxable supplies for the previous 12 months | [IR289](https://www.ird.govt.nz/-/media/project/ir/home/documents/forms-and-guides/ir200---ir299/ir289/ir289.pdf) |

- **All conditions:** in business and registered for GST for the whole of the previous year and part of the year before; RIT in the range above; GST filed monthly or 2-monthly; not a partnership; ratio in range.
- **Election:** in writing, in myIR or by phone, at or before the start of the income year it is for. For 2026-27 that means by 31 March 2026, so a new election now can only start from 2027-28. IRD cannot backdate it.
- **The ratio:** IRD divides last year's RIT by last year's total GST taxable supplies, rounded down to 1 decimal place. Each instalment is the ratio times the GST taxable supplies for the previous 2 months (for monthly filers, every second GST return), paid with the GST return ([IRD work out ratio option](https://www.ird.govt.nz/income-tax/provisional-tax/provisional-tax-options/ratio-option/work-out-provisional-tax-using-the-ratio-option)). After a new return is filed, IRD issues an updated ratio, usable 30 days from the date of its letter.
- **Must stop** ([IRD ratio option](https://www.ird.govt.nz/income-tax/provisional-tax/provisional-tax-options/ratio-option)) if GST registration ends, any GST return is 60 days or more overdue, the ratio leaves 0% to 100%, GST filing changes to 6-monthly, or a return shows RIT below $5,000 or above $150,000. Stopping before the first payment date allows a move to standard or estimation; stopping after it means estimation for the rest of the year. Interest applies from the date the option stops.

### Instalment dates (31 March balance date)

| Option | Instalments | 2026-27 dates | Source |
| --- | --- | --- | --- |
| Standard or estimation | 3 | 28 August 2026, 15 January 2027, 7 May 2027 | [IRD payment dates](https://www.ird.govt.nz/income-tax/provisional-tax/paying-your-provisional-tax/payment-dates-for-provisional-tax) |
| Standard or estimation, 6-monthly GST filer | 2 | 28 October 2026, 7 May 2027 | [IR289](https://www.ird.govt.nz/-/media/project/ir/home/documents/forms-and-guides/ir200---ir299/ir289/ir289.pdf) |
| Ratio | 6 | 28 June 2026, 28 August 2026, 28 October 2026, 15 January 2027, 28 February 2027, 7 May 2027 | [IRD payment dates](https://www.ird.govt.nz/income-tax/provisional-tax/paying-your-provisional-tax/payment-dates-for-provisional-tax) |
| AIM, monthly GST filer | 12 | the 28th of each month from May to November, then 15 January, 28 January, 28 February, 28 March and 7 May | same |
| AIM, 2-monthly or 6-monthly GST filer, or not registered | 6 | the ratio dates above | same |

- **The pattern.** 28 August, 15 January and 7 May is the standard pattern. The third instalment falls after the 31 March year end, by design.
- **GST-ratio months.** Ratio and 2-monthly AIM instalments fall on the 2-monthly GST return dates. Monthly AIM filers pay with every monthly GST return.
- **Weekends and holidays.** "If a due date falls on a weekend or public holiday you can file or pay on the next business day without incurring penalties" ([IRD IR328 2026-27 calendar](https://www.ird.govt.nz/-/media/project/ir/home/documents/forms-and-guides/ir300---ir399/ir328/ir328-2026-27.pdf)). In 2026-27: 28 June 2026 and 28 February 2027 are Sundays (ratio and AIM payments can be made on the Monday); for monthly AIM filers, 28 November 2026 is a Saturday (Monday 30 November) and 28 March 2027 is Easter Sunday with Easter Monday on 29 March per IR328 (Tuesday 30 March 2027).
- **Other balance dates:** IRD's page says to check the dates in myIR (income tax tile, "View" provisional tax). AIM software works out its own dates.
- **Payments** go to the earliest unpaid instalment, and the provisional tax owed includes any late payment penalties charged ([IRD paying your provisional tax](https://www.ird.govt.nz/income-tax/provisional-tax/paying-your-provisional-tax)). Tax pooling can be used with the standard, estimation and ratio options.

## Use-of-money interest

UOMI is interest, not a penalty. IRD works it out daily, it does not compound, and IRD works it out after the return is filed ([IRD UOMI rates](https://www.ird.govt.nz/managing-my-tax/penalties-and-interest/interest-on-overpayments-and-underpayments)).

| Rate in force from | IRD charges (underpaid) | IRD pays (overpaid) | Source |
| --- | --- | --- | --- |
| 16 January 2026 (still the latest row on 25 September 2026) | 8.97% | 2.25% | [IRD UOMI rates](https://www.ird.govt.nz/managing-my-tax/penalties-and-interest/interest-on-overpayments-and-underpayments) |
| 8 May 2025 to 15 January 2026 | 9.89% | 3.27% | same |
| 16 January 2025 to 7 May 2025 | 10.88% | 4.30% | same |

Use the rate in force on each day. Never apply one rate to a period that spans a change. Recent changes have taken effect the day after a standard instalment date. Before relying on a rate, check the table again. Formula: interest = t x r x d / 365, where t is the underpaid or overpaid tax (including late payment penalties), r the rate and d the days, counting both the first and the last day ([IR289](https://www.ird.govt.nz/-/media/project/ir/home/documents/forms-and-guides/ir200---ir299/ir289/ir289.pdf)).

| Rule | Figure | Source |
| --- | --- | --- |
| Standard option "safe harbour": RIT under this means interest only from the day after the terminal tax date | $60,000 | [IRD interest on provisional tax](https://www.ird.govt.nz/income-tax/provisional-tax/interest-on-provisional-tax): "If your residual income tax (RIT) is less than $60,000" |
| No interest charged or paid on an under- or overpayment of this or less | $100 | same: "under or overpay by $100 or less" |

### Exposure by option ([IRD interest on provisional tax](https://www.ird.govt.nz/income-tax/provisional-tax/interest-on-provisional-tax))

| Option | Interest |
| --- | --- |
| Standard, RIT under $60,000 | Charged or paid only from the day after the terminal tax date, even if instalments were late or short (rule since the 2023 income year). Late payment penalties still apply to late instalments. |
| Standard, RIT $60,000 or more | From the day after the final instalment date on the gap between RIT and provisional tax paid. An earlier instalment paid late or short is charged from the day after its due date on the lesser of (a) the instalment due less the amount paid, or (b) RIT divided by the number of instalments, less the amount paid. Credit interest is paid only if the other instalments were paid in full and on time. |
| Estimation | On any shortfall against actual RIT from the day after each instalment date, even if paid in full and on time. Credit interest from each payment date, or from the first day of the year for earlier payments. |
| AIM | None if paid in full and on time; no credit interest on overpayments. Late or short payments: interest and penalties from the day after the due date. |
| Ratio, used for the full year | None charged or paid on provisional tax. Interest if more than $100 is owed after the terminal tax date. |

- **Extension of time:** where last year's return was not filed by an instalment date and there is an EOT, the amount that "should have been paid" for that instalment is the lesser of the 10% uplift amount and the 5% uplift amount. This does not apply to the final instalment ([IR289](https://www.ird.govt.nz/-/media/project/ir/home/documents/forms-and-guides/ir200---ir299/ir289/ir289.pdf)).
- **The standard-option rules do not apply** to associated persons where one is a company and they are not all on the standard or ratio option, or to a provisional tax interest avoidance arrangement. A switch from standard to estimation is treated as estimation for the full year.
- **Tax treatment:** interest paid to IRD is deductible for business purposes. Interest received is gross income in the year it is refunded. Interest is GST exempt ([IRD UOMI rates](https://www.ird.govt.nz/managing-my-tax/penalties-and-interest/interest-on-overpayments-and-underpayments); IR289).
- **Remission** is limited, for example where IRD's wrong advice caused the problem.

## Penalties

| Penalty (current rules; no tax year) | Figure | Source |
| --- | --- | --- |
| Late payment: the day after the due date | 1% | [IRD late payment penalties](https://www.ird.govt.nz/managing-my-tax/penalties-and-interest/penalties-and-debt/late-payment-penalties): "1% penalty on the day after payment due date" |
| Late payment: on the 7th day after the due date, on the remaining tax including penalties | 4% | same: "4% penalty for remaining tax including penalties" |
| Monthly penalty: does NOT apply to income tax, including provisional tax | 1% every month | same: "except for GST, income tax including provisional tax" |

- A first late payment in a 2-year period may get a grace period and a new due date. Miss that date and the penalty runs from the original due date. An instalment arrangement can stop some penalties.
- Late payment penalties apply to late or short instalments under every option, including the standard option inside the safe harbour.
- Penalties are not deductible for income tax or GST (IR289).

**Shortfall penalties (AIM or estimation, provisional tax unreasonably low)** apply to the underpaid amount (IR289):

| Behaviour | Rate | Source |
| --- | --- | --- |
| Not taking reasonable care | 20% | [IR289](https://www.ird.govt.nz/-/media/project/ir/home/documents/forms-and-guides/ir200---ir299/ir289/ir289.pdf) |
| Unacceptable tax position | 20% | same |
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
| Choosing to pay, exactly $5,000 paid by 7 May | IRD web says "at least $5,000"; IR289 says "more than": **check** | [IRD choosing](https://www.ird.govt.nz/income-tax/provisional-tax/choosing-to-be-a-provisional-tax-payer) |
| Company or trust in its first year | No early payment discount | [IRD first year in business](https://www.ird.govt.nz/income-tax/provisional-tax/paying-tax-in-your-first-year-in-business) |

## Worked cases

### Source: [IR289](https://www.ird.govt.nz/-/media/project/ir/home/documents/forms-and-guides/ir200---ir299/ir289/ir289.pdf) for IRD's examples, unless another link is shown

Amounts from IRD's examples are as IRD prints them. C1, C8 and C10 are illustrations built on IRD's rules.

**C1. Standard option, 2026-27.** 2025-26 RIT $12,000, return filed 7 July 2026, no EOT, 2-monthly GST filer. Provisional tax = $12,000 + 5% = $12,600, paid as $4,200 on each of 28 August 2026, 15 January 2027 and 7 May 2027 ([IRD work out standard option](https://www.ird.govt.nz/income-tax/provisional-tax/provisional-tax-options/standard-option/work-out-provisional-tax-using-the-standard-option)).

**C2. Extension of time, catch-up (IRD's Ned example).** The company's 2021 RIT was $24,000; plus 10% ($2,400) is $26,400. It pays $8,800 on 28 August 2023 and $8,800 on 15 January 2024. Its 2023 return, filed 23 January 2024, shows RIT of $23,740. The final instalment on 7 May 2024 is $23,740 + 5% ($1,187) − $8,800 − $8,800 = $7,327.

**C3. EOT with a low 2-years-ago RIT, then a switch to estimation (IRD's Mary example).** Mary's 2023 RIT was under $5,000, and her 2024 return (EOT) was filed after 28 August 2024. So on the standard option she owed $0.00 on 28 August 2024, then $12,300 on 15 January 2025 and $12,300 on 7 May 2025 (total $24,600). On 1 December 2024 she estimated $15,000 instead, paid over the last 2 instalments. Her 2025 RIT came to $9,000, so interest is worked out on $3,000 per instalment. She is charged interest on $3,000 from the day after 28 August 2024, because debit interest runs from P1 once she estimates ([IRD interest on provisional tax](https://www.ird.govt.nz/income-tax/provisional-tax/interest-on-provisional-tax)).

**C4. Standard option, RIT over the safe harbour, a missed instalment (IRD's ABC Ltd example).** Provisional tax $24,000 ($8,000 per instalment); only the first was paid. RIT $66,000. For the 2nd instalment the shortfall is the lesser of the $8,000 instalment due (nothing paid) and RIT divided by 3, $22,000 (nothing paid), so $8,000. At the final date the shortfall is $66,000 − $8,000 = $58,000. Interest runs on $8,000 from 16 January to 7 May (112 days) and on $58,000 from 8 May to 9 September (125 days). Late payment penalties on each of the 2nd and 3rd instalments: 1% of $8,000 = $80 the day after the due date, then 4% of the remaining $8,080 (tax plus the first penalty) = $323.20 on the 7th day, so $403.20 per instalment and $806.40 in total ([IRD late payment penalties](https://www.ird.govt.nz/managing-my-tax/penalties-and-interest/penalties-and-debt/late-payment-penalties): "4% penalty for remaining tax including penalties"). IR289's ABC example prints $320 and $800 by applying the 4% to $8,000 only; that is inconsistent with the rule and with IR289's own Anthony example (C5), so use the figures here. At the 2026-27 charge rate of 8.97%, if unchanged through the period, the first leg would be $8,000 x 8.97% x 112 / 365 = $220.20 ([IRD UOMI rates](https://www.ird.govt.nz/managing-my-tax/penalties-and-interest/interest-on-overpayments-and-underpayments)).

**C5. Late payment penalties (IRD's Anthony example).** $7,600 due 7 May, paid 10 July: 1% on 8 May ($76.00, balance $7,676.00), then 4% on 14 May ($307.04, balance $7,983.04). Total penalties $383.04, with no further monthly penalty.

**C6. Estimation and re-estimation (IRD's Hiwi example).** Estimated RIT $59,371.50, paid as 3 instalments of $19,790.50. In February he re-estimates at $65,000. After paying $39,581.00, the final instalment is $25,419.00.

**C7. Ratio option (IRD's Leonie example).** RIT $51,000 over taxable supplies of $2,114,723 gives a ratio of 2.4% (rounded down). Her April-May supplies of $725,111 give an instalment of $17,402.66, due 28 June.

**C8. Early payment discount, 2026-27.** A first-year sole trader pays $5,000 voluntarily before 31 March 2027, and 2026-27 RIT is $8,000. 105% of RIT is $8,400, so the discount is on the lesser, $5,000: $5,000 x 4.25% = $212.50 ([IRD first year in business](https://www.ird.govt.nz/income-tax/provisional-tax/paying-tax-in-your-first-year-in-business)).

**C10. New provisional taxpayer.** An employee leaves a job and starts contracting (no tax deducted) on 1 September 2026, had RIT below $5,000 in each of the last 4 years, and expects 2026-27 RIT of $60,000 or more. The start is on or after 29 July and before 16 December, so interest is worked out on 2 instalments. The first instalment date more than 30 days after the start is 15 January 2027 ([IRD interest on provisional tax](https://www.ird.govt.nz/income-tax/provisional-tax/interest-on-provisional-tax)).

## When to refuse or refer

- **Balance date other than 31 March, a change of balance date or a transitional year:** dates and amounts differ, and IRD must approve the change. Get the dates from myIR or IRD; do not guess.
- **Tax pooling:** its own rules; outside this Guide.
- **Multi-entity groups, associated companies on mixed options, or any interest avoidance arrangement:** the standard-option interest rules may not apply. Refer.
- **Non-residents:** outside this Guide.
- **Shortfall penalty exposure** (an estimate far below actual RIT), remission requests or disputes: refer to a New Zealand chartered accountant or tax agent.
- **A client who cannot pay:** tell them to contact IRD before the due date about an instalment arrangement.
- **Anything that turns on the wording of the Income Tax Act 2007 or the Tax Administration Act 1994** (the "less than" vs "or less" and "at least" vs "more than" points above): **check** the Act.
- Working out the income tax itself: `nz-income-tax-ir3`. GST returns and filing frequency: `new-zealand-gst`. ACC levies: `nz-acc-levies`.

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
| 2026-27 terminal tax | 7 February 2028, or 7 April 2028 with a tax agent's EOT. Waitangi Day (6 February 2028) is a Sunday, so the Monday 7 February 2028 is the holiday and in practice payment is due 8 February 2028: confirm on the 2027-28 IR328 |

Sources: [IRD payment dates](https://www.ird.govt.nz/income-tax/provisional-tax/paying-your-provisional-tax/payment-dates-for-provisional-tax), [IR289](https://www.ird.govt.nz/-/media/project/ir/home/documents/forms-and-guides/ir200---ir299/ir289/ir289.pdf), [IRD interest on provisional tax](https://www.ird.govt.nz/income-tax/provisional-tax/interest-on-provisional-tax) (7 February, or 7 April with an agent's EOT) and [IRD extension of time](https://www.ird.govt.nz/topics/intermediaries/extension-of-time-arrangements).

- **How to pay:** online through myIR or by the other methods on IRD's payment pages. GST-registered ratio and AIM filers pay with their GST return (GST103B form series).
- **Bank statement coding:** a debit to Inland Revenue on or just after 28 August, 15 January or 7 May (or 28 October for 6-monthly GST filers, or the GST dates for ratio or AIM) is usually a provisional tax instalment. A debit around 7 February (or 7 April) is usually terminal tax. A debit on 7 May may be GST, not provisional tax. These debits are not provisional tax: GST, ACC levies, student loan repayments, KiwiSaver, child support, and penalty or interest charges. Always confirm against the myIR statement. Provisional tax, terminal tax and penalties are not deductible expenses. UOMI paid is deductible for business purposes.

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
