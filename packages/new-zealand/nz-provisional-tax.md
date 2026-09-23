---
name: nz-provisional-tax
description: Use this skill whenever asked about New Zealand provisional tax for individuals, companies, contractors, sole traders, and small businesses. Trigger on phrases like "provisional tax", "RIT", "residual income tax", "standard option", "standard uplift", "estimation method", "AIM", "ratio option", "use of money interest", "UOMI", "provisional tax instalment", or any question about provisional tax obligations in New Zealand. Covers the $5,000 RIT threshold, standard option 105%/110% uplift rules, estimation, AIM, ratio-option routing, March balance-date instalments, 6-monthly GST two-instalment cases, and current UOMI rate handling. ALWAYS read this skill before touching any NZ provisional tax work.
version: 2.0
jurisdiction: NZ
tax_year: 2026
last_updated: 2026-09-22
review_status: pending_review
drafted_by: OpenAccountants
approved_by: pending
depends_on:
  - income-tax-workflow-base
category: international
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# New Zealand provisional tax

Provisional tax is income tax paid in instalments during the year instead of a lump sum after it. This Guide covers who must pay, the standard, estimation, ratio and AIM options, instalment dates, use-of-money interest (UOMI) and penalties, for individuals, sole traders, contractors, landlords and companies. Figures are for tax year 2026. In New Zealand that is the income year from 1 April 2026 to 31 March 2027, which Inland Revenue calls the 2027 income year. Most figures come from Inland Revenue (IRD) web pages read on 22 September 2026. The shortfall penalty rates, the worked example and the first-year rules come from IRD's provisional tax guide IR289, dated April 2025, the latest edition IRD links. UOMI rates and penalties have no tax year: each stands until IRD changes it, and the UOMI rate changes during the year (Section 6.1).

## Section 1: Quick reference

**Quick reference field table**

| Field | Value |
| --- | --- |
| Country | New Zealand |
| Tax | Provisional income tax |
| Legislation | Income Tax Act 2007, Part RC (IRD's QB 19/04 cites ss RC 3(3) and RC 9(9)); Tax Administration Act 1994, interest rules including ss 120KC and 120KE (cited in QB 19/04, 2019). The Acts were not read. |
| Authority | Inland Revenue (IR / Te Tari Taake) |
| Portal | myIR |
| Threshold | Residual income tax (RIT) from the last return must be more than the threshold in the table below |
| Default method | Standard option. IRD uses it unless the taxpayer chooses another option |
| Standard option amount | Previous year's RIT plus 5%; RIT from 2 years ago plus 10% only with an extension of time and last year's return not yet filed at that instalment date (Section 5.2) |
| Alternative methods | Estimation option, ratio option, accounting income method (AIM) |
| Standard balance date | 31 March |
| Dates | Table below; ratio in Section 5.6; AIM in Section 5.4. A payment on the next working day after a weekend or public holiday date counts as on time |
| Contributor | Open Accountants Community |
| Validated by | Pending: New Zealand Chartered Accountant (CA) sign-off |

**Who must pay**

| Rule | Value | Note |
| --- | --- | --- |
| Source | all figures below | https://www.ird.govt.nz/income-tax/provisional-tax |
| Provisional tax entry threshold: RIT from the last return must be MORE than this | NZD 5,000 | "if you had to pay more than $5,000 tax at the end of the year from your last return" |

RIT is "the tax payable on your taxable income, less PAYE and any other income tax credits" (IR289, https://www.ird.govt.nz/-/media/project/ir/home/documents/forms-and-guides/ir200---ir299/ir289/ir289.pdf). The test is a cliff on last year's RIT: exactly the threshold does not trigger it. A taxpayer below it may choose to be a provisional taxpayer. First-year rules: Section 5.1.

**Standard instalment schedule (31 March balance date)**

| Instalment | Due date for the 2027 income year | Amount |
| --- | --- | --- |
| Source | all dates below | https://www.ird.govt.nz/income-tax/provisional-tax/paying-your-provisional-tax/payment-dates-for-provisional-tax |
| 1st | 28 August 2026 | One third of the standard-option amount |
| 2nd | 15 January 2027 | One third, adjusted if the uplift changed (Section 5.2) |
| 3rd | 7 May 2027 | The balance of the standard-option amount |
| 6-monthly GST filers | 28 October 2026 and 7 May 2027 | Half each, paid with the GST returns (IR289) |

The 3rd instalment falls after the 31 March year end. That is correct.

**Conservative defaults**

| Ambiguity | Default |
| --- | --- |
| Method unclear | Standard option. Check extension of time, filing date of last year's return, GST frequency, UOMI line (Section 6.2) |
| Balance date not 31 March | Do not guess the dates. Use IRD's tax due date calculator (Section 5.2) |
| Tax agent with extension of time | Dates do not change; the uplift may (Section 5.2) |
| First year in business | Usually none compulsory; check Section 5.1 |

## Section 2: Required inputs and refusal catalogue

### Required inputs

- **Minimum viable.** Last year's RIT; extension of time status and, if any, the filing date of last year's return and the RIT from 2 years ago; balance date; GST filing frequency; chosen option. https://www.ird.govt.nz/income-tax/provisional-tax/provisional-tax-options/standard-option
- **Recommended.** Income trend, any move from wages to self-employment, business start date, myIR statement.
- **Refusal policy if minimum is missing.** HARD STOP. Without last year's RIT (and, with an unfiled return under an extension of time, the RIT from 2 years ago) the standard option cannot be worked out. Estimating needs current year projections. https://www.ird.govt.nz/income-tax/provisional-tax/provisional-tax-options/standard-option/work-out-provisional-tax-using-the-standard-option

### Refusal catalogue

- **R-NZ-PT-1: Pooling arrangements.** Trigger: client uses tax pooling. Message: "Tax pooling arrangements have specific rules outside this Guide." IRD allows pooling with the standard, estimation or ratio options. https://www.ird.govt.nz/income-tax/provisional-tax/paying-your-provisional-tax
- **R-NZ-PT-2: Multi-entity structures.** Trigger: complex multi-entity group. Message: "Multi-entity provisional tax allocation is outside this Guide."
- **R-NZ-PT-3: Non-resident provisional tax.** Trigger: non-resident client. Message: "Non-resident provisional tax is outside this Guide."

## Section 3: Payment pattern library

Pre-classifier for bank statement debits. Confirm every match against the client's myIR statement.

### 3.1 Inland Revenue provisional tax debits

**Inland Revenue provisional tax debits**

| Pattern | Treatment | Notes |
| --- | --- | --- |
| IRD, INLAND REVENUE, IR PAYMENT | Provisional tax payment | Match with Aug/Jan/May timing (or Oct/May for 6-monthly GST filers) |
| PROVISIONAL TAX, PROV TAX | Provisional tax payment | Explicit description |
| MYIR PAYMENT | Provisional tax payment | Online payment via myIR |
| TERMINAL TAX | NOT provisional tax | Year-end balance. Flag separately |

IRD applies a payment to the earliest unpaid provisional tax instalment, and the amount of provisional tax includes any late payment penalties charged. https://www.ird.govt.nz/income-tax/provisional-tax/paying-your-provisional-tax

### 3.2 Timing-based identification

**Timing-based identification**

| Debit date range | Likely instalment | Confidence |
| --- | --- | --- |
| 20 August to 5 September | 1st instalment (28 Aug) | High if IR payee |
| 8 January to 20 January | 2nd instalment (15 Jan) | High |
| 1 May to 14 May | 3rd instalment (7 May) | Medium: GST for March is also due 7 May |
| Late October | 6-monthly GST or ratio instalment (28 Oct) | Medium |
| Early February | Terminal tax (7 February) | Flag separately |

The ranges are a heuristic, not an IRD rule.

### 3.3 Related but NOT provisional tax

**Related but NOT provisional tax**

| Pattern | Treatment | Notes |
| --- | --- | --- |
| GST, GOODS AND SERVICES TAX | EXCLUDE | GST payment |
| ACC LEVY | EXCLUDE | Accident Compensation levy |
| STUDENT LOAN | EXCLUDE | Student loan repayment |
| KIWISAVER | EXCLUDE | Retirement savings |
| CHILD SUPPORT, IR CHILD | EXCLUDE | Child support via IR |
| PENALTIES AND INTEREST IR | EXCLUDE | Penalty or interest charge |
| TERMINAL TAX | Flag separately | Year-end balance, not provisional |

### 3.4 Tax agent EOT identification

- **Tax agent EOT identification.** An extension of time (EOT) does NOT create two instalments; it changes the uplift (Section 5.2). Two instalments, 28 October and 7 May, are for 6-monthly GST filers. https://www.ird.govt.nz/-/media/project/ir/home/documents/forms-and-guides/ir200---ir299/ir289/ir289.pdf

## Section 4: Worked examples

The examples show the method. Amounts appear only where IRD prints them.

### Example 1: Standard uplift, three instalments

**IRD's standard option example (IR289)**

| Item | Value | Note |
| --- | --- | --- |
| Source | all figures below | https://www.ird.govt.nz/-/media/project/ir/home/documents/forms-and-guides/ir200---ir299/ir289/ir289.pdf |
| Previous year's RIT | NZD 10,130 | "if your RIT was $10,130" |
| Next year's provisional tax (RIT plus 5%) | NZD 10,636 | "your next year's provisional tax will be $10,636" |

**Input:** no extension of time, 31 March balance date, not a 6-monthly GST filer.

**Output:** the provisional tax above, divided by 3, paid on 28 August, 15 January and 7 May.

### Example 2: Below threshold

**Input:** last year's RIT was not more than the threshold in Section 1.

**Output:** none compulsory unless Section 5.1 applies. Terminal tax at year end; voluntary payments allowed.

### Example 3: Estimation method

**Input:** last year's RIT was above the threshold. The client expects this year's RIT to be much lower.

**Output:** estimate this year's RIT (Section 5.3) and pay that. Warning: an estimate below actual RIT can bring interest from the day after each instalment date, even if paid in full and on time, and possibly a shortfall penalty.

### Example 4: Tax agent EOT (three instalments, mixed uplifts)

**Input:** extension of time; last year's return filed after the 1st but by the 2nd instalment date.

**Output:** Three instalments, not two. 1st: RIT from 2 years ago plus 10%, divided by 3. 2nd: last year's RIT plus 5%, times 2, divided by 3, less the 1st payment. 3rd: last year's RIT plus 5%, less the first two payments. https://www.ird.govt.nz/income-tax/provisional-tax/provisional-tax-options/standard-option/work-out-provisional-tax-using-the-standard-option

### Example 5: Bank statement classification

**Input line:** `28.08.2026 ; IRD PROVISIONAL TAX ; DEBIT ; amount ; NZD`

**Classification:** provisional tax, 1st instalment of the 2027 income year (1 April 2026 to 31 March 2027). A tax payment, not a deductible expense.

## Section 5: Computation rules

### 5.1 RIT threshold

- **RIT threshold formula.** RIT = income tax on taxable income, less PAYE and other income tax credits. If last year's RIT is more than the threshold in Section 1, provisional tax is payable this year. If it is equal or less, no provisional tax (end-of-year tax only). https://www.ird.govt.nz/income-tax/provisional-tax
- **First year in business.** IRD: "Your first year in business is not tax free." No compulsory provisional tax unless last year's RIT (for example from other income) was more than the threshold in Section 1, or the new provisional taxpayer rule below applies. IR289 leaves out the words 'more than' here; IRD's web pages include them, and this Guide follows the web pages. Voluntary payments may earn an early payment discount (individuals, partners, look-through company owners; not companies or trusts). https://www.ird.govt.nz/-/media/project/ir/home/documents/forms-and-guides/ir200---ir299/ir289/ir289.pdf
- **New provisional taxpayer.** IRD's web page says you have to pay provisional tax for this year, even if you have not paid it before, if RIT this year is at or above the line in the table below and: (a) for an individual (not a trustee of a trust), RIT was less than the entry threshold for each of the last 4 years, and during this year they stopped earning employment income and started earning income from a taxable activity where tax is not deducted at source; or (b) for a non-individual (including a trustee), the taxable activity started this year and there was no income from a taxable activity in the last 4 years. IR289 and IRD's QB 19/04 put the effect as interest: a new provisional taxpayer pays or receives interest on 1 to 3 equal instalments, set by the date the taxable activity started: before 29 July, 3; from 29 July to before 16 December, 2; from 16 December, 1, paid as one sum by the 3rd instalment date. Interest runs from the day after the 1st instalment date after the start, if that date is more than 30 days after the start. These dates are for a 31 March balance date; they differ for other balance dates and 6-monthly GST filers (IR289).

**New provisional taxpayer line**

| Rule | Value | Note |
| --- | --- | --- |
| Source | all figures below | https://www.ird.govt.nz/income-tax/provisional-tax/interest-on-provisional-tax |
| New provisional taxpayer: RIT for the current year at or above this | NZD 60,000 | "your residual income tax for the current year is $60,000 or more" |

### 5.2 Standard uplift method

**Standard option uplifts**

| Rule | Value | Note |
| --- | --- | --- |
| Source | all figures below | https://www.ird.govt.nz/income-tax/provisional-tax/provisional-tax-options/standard-option |
| Uplift on the previous year's RIT | 5% | "your previous year's residual income tax (RIT) plus 5%" |
| Uplift on the RIT from 2 years ago (extension of time, last year's return not yet filed) | 10% | "your RIT from 2 years ago plus 10%" |

- **No extension of time.** Last year's RIT plus 5%, "This includes if you file your return after any of your provisional tax dates." No 10% uplift.
- **Extension of time.** Return filed by the 1st date: 3 equal instalments on last year's RIT plus 5%. Filed after the 1st but by the 2nd date: Example 4. Filed after the 2nd date: 1st and 2nd on the RIT from 2 years ago plus 10%, divided by 3 each; final on last year's RIT plus 5%, less the first two payments; if filed after the final date, on the RIT expected for last year plus 5%, less the first two payments. If the RIT from 2 years ago was under the entry threshold, those instalments are nil (IR289).
- **6-monthly GST filers.** Divide by 2 and pay with the GST returns.
- **Timing.** A return filed on the next working day after a weekend or holiday instalment date counts as filed on that date. A reassessment or amendment within 30 days of an instalment date does not change that instalment.
- **Balance date other than 31 March.** IRD: "use our tax due date calculator to work out when your instalments will be due." https://www.ird.govt.nz/income-tax/provisional-tax/provisional-tax-options/standard-option/work-out-provisional-tax-using-the-standard-option
- **Changing option.** Standard to AIM or estimation at any time; not to ratio in the same year. After a switch to estimation, interest is worked out as if estimated all year.
- **Safe harbour.** See the UOMI line in Section 6.2. It is not blanket immunity: late instalments still attract late payment penalties.

### 5.3 Estimation method

- **Estimation method formula.** provisional_tax = estimated current year RIT; each instalment = provisional_tax / number of instalments. A taxpayer who expects no RIT can estimate provisional tax at zero.
- **When it fits.** Income will rise or fall a lot, a loss can be offset, or a move from self-employment to wages. Also for someone choosing to be a provisional taxpayer. An estimate can be made at any date up to the final instalment date.
- **Three instalments.** An estimate above the line in the table below is generally paid in 3 instalments.
- **Risk.** Interest on the gap between provisional tax paid and actual RIT from the day after each instalment date, even if paid on time. Shortfall penalty if unreasonably low (Section 6.3). Re-estimate if income changes. https://www.ird.govt.nz/income-tax/provisional-tax/interest-on-provisional-tax

**Estimation option line**

| Rule | Value | Note |
| --- | --- | --- |
| Source | all figures below | https://www.ird.govt.nz/income-tax/provisional-tax/provisional-tax-options/estimation-option |
| Estimated RIT above this: generally paid in 3 instalments | NZD 60,000 | "If you estimate your residual income tax will be more than $60,000" |

### 5.4 AIM method

**AIM eligibility**

| Rule | Value | Note |
| --- | --- | --- |
| Source | all figures below | https://www.ird.govt.nz/aim |
| AIM: yearly turnover must be under this (individuals and companies) | NZD 5 million | "available to individuals and companies with a yearly turnover under" |

- **AIM method.** AIM-capable software works out provisional tax from accounting income; a statement of activity is filed for each instalment. Tax is paid only on profit. Paid in full and on time: no UOMI charged. No interest paid on overpayments; a loss can be refunded at once. Late or short: interest from the day after the instalment. Missed statements can move the taxpayer to estimation.
- **Dates.** The taxpayer's GST due dates: monthly if they file GST monthly, otherwise 2-monthly (including 6-monthly GST filers). A taxpayer not registered for GST uses the 2-monthly GST dates that fit their balance date (IR289).
- **Each year.** AIM users revert to the standard option at the start of each year until they file the year's first statement of activity.

### 5.5 Terminal tax

- **Terminal tax formula.** terminal_tax = actual RIT minus provisional tax paid (IRD: end-of-year tax).
- **Terminal tax due date.** 7 February after the year ends, or 7 April if a tax agent has an extension of time. For the 2027 income year: 7 February 2028, or 7 April 2028. https://www.ird.govt.nz/income-tax/provisional-tax/interest-on-provisional-tax

### 5.6 Ratio option

**Ratio option conditions**

| Rule | Value | Note |
| --- | --- | --- |
| Source | all figures below | https://www.ird.govt.nz/income-tax/provisional-tax/provisional-tax-options/ratio-option |
| Ratio option floor: previous year's RIT greater than this | NZD 5,000 | "is greater than $5,000 and up to $150,000" |
| Ratio option ceiling: previous year's RIT up to this | NZD 150,000 | "is greater than $5,000 and up to $150,000" |
| Ratio percentage IRD calculates must be between 0 and this | 100% | "Your ratio percentage that we calculate for you is between 0 and 100%" |

- **All conditions.** In business and GST registered for the whole previous year and part of the year before; RIT and ratio inside the ranges above; GST filed monthly or 2-monthly; not a partnership. Elect in writing, in myIR or by phone, at or before the start of the income year; no backdating.
- **Dates.** 6 instalments for a 31 March balance date: 28 June, 28 August, 28 October, 15 January, 28 February, 7 May.
- **Must stop** if GST registration ends, a GST return is 60 days or more overdue, filing becomes 6-monthly, or the ratio or RIT leaves its range. Stopping after the first payment date means estimation for the rest of the year.
- **Interest.** Applied correctly and paid on time: no UOMI on provisional tax. Interest if more than the Section 6.2 de minimis is owed after the terminal tax date. Late or short instalments can attract penalties.

## Section 6: Penalties and interest

### 6.1 Use of Money Interest (UOMI)

UOMI is calculated daily and does not compound. The rate changes during the year: use the rate in force on each day, never one rate as "the" rate.

**UOMI rate table**

| Effective from | IR charges on underpayments | IR pays on overpayments |
| --- | --- | --- |
| Source | all figures below | https://www.ird.govt.nz/managing-my-tax/penalties-and-interest/interest-on-overpayments-and-underpayments |
| 16 January 2026 (still the latest row on 22 September 2026) | 8.97% | 2.25% |
| 8 May 2025 to 15 January 2026 | 9.89% | 3.27% |
| 16 January 2025 to 7 May 2025 | 10.88% | 4.30% |

### 6.2 UOMI exposure by method

**UOMI lines for provisional tax**

| Rule | Value | Note |
| --- | --- | --- |
| Source | all figures below | https://www.ird.govt.nz/income-tax/provisional-tax/interest-on-provisional-tax |
| UOMI safe harbour line (standard option): RIT less than this means interest only from the day after the terminal tax date | NZD 60,000 | "If your residual income tax (RIT) is less than $60,000" |
| No interest charged or paid on a provisional tax under or overpayment of this or less | NZD 100 | "We will not charge or pay interest if you under or overpay by $100 or less" |

**UOMI exposure by method**

| Method | UOMI exposure |
| --- | --- |
| Standard option, RIT below the safe harbour line | Interest only from the day after the terminal tax date (since the 2023 income year) |
| Standard option, RIT at or above the safe harbour line | From the day after the final instalment date on the gap between paid and RIT; late or short earlier instalments from the day after each |
| Estimation | Interest from the day after each instalment date if the estimate is too low, even if paid on time |
| AIM (correct and on time) | No UOMI charged; no interest paid on overpayments |
| Ratio option (paid on time) | No UOMI charged or paid on provisional tax |

The safe harbour line equals the GST registration threshold by coincidence; unrelated rules.

### 6.3 Late payment penalties

**Late payment penalties**

| Offence | Penalty | Note |
| --- | --- | --- |
| Source | all figures below | https://www.ird.govt.nz/managing-my-tax/penalties-and-interest/penalties-and-debt/late-payment-penalties |
| Late payment, day after the due date | 1% | "1% penalty on the day after payment due date" |
| Still unpaid on the 7th day after the due date | 4% | "4% penalty for remaining tax including penalties" |
| Monthly penalty on other taxes: does NOT apply to income tax, including provisional tax | 1% every month | "(except for GST, income tax including provisional tax, and Working for Families overpayments)" |

A first late payment in 2 years may get a grace period. Penalties can apply to late or short instalments under any option.

**Late filing penalty, income tax return**

| Net income | Penalty | Note |
| --- | --- | --- |
| Source | all figures below | https://www.ird.govt.nz/managing-my-tax/penalties-and-interest/penalties-and-debt/late-filing-penalties |
| Less than NZD 100,000 | NZD 50 | "Less than $100,000 $50" |
| NZD 100,000 to NZD 1 million | NZD 250 | Middle band of IRD's late filing table, by net income |
| More than NZD 1 million | NZD 500 | Top band of IRD's late filing table, by net income |

IRD first charges the lowest penalty, then adjusts to the net income on the late return.

**Shortfall penalties (AIM or estimation, provisional tax unreasonably low)**

| Mistake | Shortfall penalty | Note |
| --- | --- | --- |
| Source | all figures below | https://www.ird.govt.nz/-/media/project/ir/home/documents/forms-and-guides/ir200---ir299/ir289/ir289.pdf |
| Not taking reasonable care | 20% | "Not taking reasonable care 20%" |
| Unacceptable tax position | 20% | "Unacceptable tax position 20%" |
| Gross carelessness | 40% | "Gross carelessness 40%" |
| Abusive tax position | 100% | "Abusive tax position 100%" |
| Evasion | 150% | "Evasion 150%" |

The penalty is applied to the underpaid amount (IR289).

## Section 7: Method selection guidance

**Method selection guidance table**

| Situation | Recommended method | Rationale |
| --- | --- | --- |
| Income stable or growing | Standard option | Predictable; check Sections 5.2 and 6.2 |
| Income dropping significantly | Estimation | Lower payments; interest and penalty risk |
| Irregular or seasonal income | AIM or ratio option | Follows trading; check Sections 5.4 and 5.6 |
| First year of business | Usually none compulsory | Check Section 5.1; year 2 brings terminal tax and provisional tax together |

Flag the estimation method for review. Options: https://www.ird.govt.nz/income-tax/provisional-tax/provisional-tax-options

## Section 8: Edge cases

- **New sole trader, no RIT last year.** Usually none compulsory; check Section 5.1. Voluntary payments ease year 2.
- **Standard amount far above expected RIT.** Estimation is available, with interest risk.
- **Non-standard balance date.** Dates shift. Use IRD's calculator; this Guide prints no other dates.
- **3rd instalment after year end.** By design.
- **Change of balance date.** Needs IRD approval; IRD sets the transitional year's dates (IR289).

## Section 9: Self-checks

Before delivering output, check:

- [ ] RIT more than (not equal to) the threshold; Section 5.1 checked for new businesses
- [ ] Option and its conditions met
- [ ] Uplift right: 10% only with an extension of time and last year's return unfiled
- [ ] Instalments: 3 standard, 2 for 6-monthly GST, 6 for ratio, GST dates for AIM
- [ ] Dates right for the balance date
- [ ] Interest risk flagged for estimation; UOMI rate dates applied
- [ ] No monthly late payment penalty on provisional tax
- [ ] Terminal tax date included; output labelled as estimated until a New Zealand CA confirms

### Test 1: Standard uplift

**Input:** RIT above the threshold, no extension of time, 31 March balance date.
**Expected:** RIT plus 5%, divided by 3: 28 Aug, 15 Jan, 7 May.

### Test 2: Below threshold

**Input:** last year's RIT below the threshold, no new provisional taxpayer trigger.
**Expected:** no provisional tax.

### Test 3: Estimation method

**Input:** last year's RIT above the threshold; much lower RIT expected.
**Expected:** estimated RIT divided by the instalments. Interest warning.

### Test 4: Tax agent EOT

**Input:** extension of time; last year's return filed after the 2nd instalment date.
**Expected:** 3 instalments: 1st and 2nd on the RIT from 2 years ago plus 10%; 3rd on last year's RIT plus 5% less the first two.

### Test 5: First year

**Input:** new freelancer, no prior RIT, Section 5.1 not triggered.
**Expected:** none compulsory. End-of-year tax by 7 February after the year ends.

### Test 6: RIT exactly NZD 5,000

**Input:** last year's RIT equal to the Section 1 threshold.
**Expected:** no provisional tax (must be more than the threshold).

### Test 7: Mixed PAYE and SE

**Input:** salary plus self-employed income.
**Expected:** test RIT after PAYE credits, not total tax.

## Section 10: Test suite

The tests are in Section 9.

## Prohibitions

- NEVER require provisional tax when last year's RIT is not more than the threshold, unless Section 5.1 applies
- NEVER say standard-option payments remove all interest and penalties
- NEVER recommend the estimation option without flagging interest and shortfall penalty risk
- NEVER apply the 10% uplift to a taxpayer without an extension of time
- NEVER tie two instalments to an extension of time. Two instalments are for 6-monthly GST filers
- NEVER confuse RIT with total income tax
- NEVER add a 1% monthly late payment penalty to provisional tax
- NEVER quote one UOMI rate for a period that spans a rate change
- NEVER ignore the 3rd instalment date falling after year end
- NEVER present calculations as definitive

## The method, step by step

1. Find last year's RIT. More than the threshold: provisional taxpayer. If not, check Section 5.1. https://www.ird.govt.nz/income-tax/provisional-tax
2. Choose an option and check its conditions. https://www.ird.govt.nz/income-tax/provisional-tax/provisional-tax-options
3. Standard option: pick the uplift for each instalment (Section 5.2) and work out each instalment. https://www.ird.govt.nz/income-tax/provisional-tax/provisional-tax-options/standard-option/work-out-provisional-tax-using-the-standard-option
4. Diary the dates for the option and GST frequency. Use IRD's calculator for other balance dates. https://www.ird.govt.nz/income-tax/provisional-tax/paying-your-provisional-tax/payment-dates-for-provisional-tax
5. Check interest against the UOMI line, using the rate in force on each day. https://www.ird.govt.nz/income-tax/provisional-tax/interest-on-provisional-tax
6. Pay terminal tax by 7 February (7 April with an agent's extension of time); check late payment penalties. https://www.ird.govt.nz/managing-my-tax/penalties-and-interest/penalties-and-debt/late-payment-penalties

## Ask the client first

- What was your RIT on last year's return, and on the return before that?
- Do you use a tax agent with an extension of time? When will last year's return be filed?
- Are you registered for GST, and do you file monthly, 2-monthly or 6-monthly?
- What is your balance date, if not 31 March?
- Do you expect this year's income to be much higher or lower than last year?
- Did you start a business this year, or move from wages to self-employment?

## When to refuse or refer

- Tax pooling (R-NZ-PT-1), multi-entity groups (R-NZ-PT-2) and non-residents (R-NZ-PT-3).
- Other balance dates, or a change of balance date.
- Associated persons where a company does not use the standard or ratio option, or an interest avoidance arrangement: the standard-option interest rules do not apply.
- A client who cannot pay: refer (instalment arrangement with IRD).
- Working out the income tax itself: see `nz-income-tax-ir3`. GST returns: see `nz-gst-return`. ACC levies: see `nz-acc-levies`. Residence: see `nz-tax-residency`.

## Sources

- provisional tax: https://www.ird.govt.nz/income-tax/provisional-tax
- provisional tax options: https://www.ird.govt.nz/income-tax/provisional-tax/provisional-tax-options
- standard option: https://www.ird.govt.nz/income-tax/provisional-tax/provisional-tax-options/standard-option
- work out provisional tax using the standard option: https://www.ird.govt.nz/income-tax/provisional-tax/provisional-tax-options/standard-option/work-out-provisional-tax-using-the-standard-option
- estimation option: https://www.ird.govt.nz/income-tax/provisional-tax/provisional-tax-options/estimation-option
- ratio option: https://www.ird.govt.nz/income-tax/provisional-tax/provisional-tax-options/ratio-option
- AIM: https://www.ird.govt.nz/aim
- paying your provisional tax: https://www.ird.govt.nz/income-tax/provisional-tax/paying-your-provisional-tax
- payment dates for provisional tax: https://www.ird.govt.nz/income-tax/provisional-tax/paying-your-provisional-tax/payment-dates-for-provisional-tax
- interest on provisional tax: https://www.ird.govt.nz/income-tax/provisional-tax/interest-on-provisional-tax
- interest on overpayments and underpayments: https://www.ird.govt.nz/managing-my-tax/penalties-and-interest/interest-on-overpayments-and-underpayments
- late payment penalties: https://www.ird.govt.nz/managing-my-tax/penalties-and-interest/penalties-and-debt/late-payment-penalties
- late filing penalties: https://www.ird.govt.nz/managing-my-tax/penalties-and-interest/penalties-and-debt/late-filing-penalties
- provisional tax guide IR289 (April 2025): https://www.ird.govt.nz/-/media/project/ir/home/documents/forms-and-guides/ir200---ir299/ir289/ir289.pdf
- IRD Question we've been asked QB 19/04, provisional tax and use of money interest in the first year of business (2019): https://www.taxtechnical.ird.govt.nz/-/media/project/ir/tt/pdfs/questions-we-ve-been-asked/2019/qb19-04.pdf

## Disclaimer

This Guide and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this Guide. All outputs must be reviewed and signed off by a qualified professional (such as a New Zealand Chartered Accountant or equivalent licensed practitioner) before filing or acting upon.

> Contributed by OpenAccountants.

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
