---
name: ie-preliminary-tax
description: Use this skill whenever asked about Irish Preliminary Tax for self-employed individuals. Trigger on phrases like "preliminary tax Ireland", "Form 11", "self-assessed tax Ireland", "October 31 deadline", "ROS filing", "100% rule preliminary tax", "90% rule Ireland", or any question about estimated tax payment obligations for a self-employed client in Ireland. Covers the 100%/90% prior-year/current-year rules, payment deadlines, and surcharges. ALWAYS read this skill before touching any Ireland preliminary tax work.
version: 2.0
jurisdiction: IE
tax_year: 2026
last_updated: 2026-10-02
authored_by: OpenAccountants team
review_status: pending_review
trust_label: Written by the OpenAccountants team
depends_on:
  - income-tax-workflow-base
category: international
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Ireland preliminary tax for self-assessed individuals

This Guide covers preliminary tax for individuals in Irish Income Tax self-assessment (self-employed people, and people with rental or other non-PAYE income who file Form 11). Figures are for tax year 2026. Preliminary tax for 2026 is paid in 2026, on the same date as the 2025 Form 11 return and the 2025 balance. It does not cover companies, trusts or Capital Gains Tax (CGT) computation. Amounts in the worked examples are hypothetical arithmetic, not authority figures.

## Section 1. Quick reference

Preliminary tax is the individual's own estimate of Income Tax, PRSI and USC for the current tax year. It is due by 31 October of that tax year. To avoid interest, it must be equal to, or more than, the LOWEST of three amounts. Each amount looks at a DIFFERENT year:

| Item | Value | Note (verbatim) |
| --- | --- | --- |
| Source | all figures below | https://www.revenue.ie/en/self-assessment-and-self-employment/guide-to-self-assessment/preliminary-tax.aspx |
| Option 1: the CURRENT tax year (2026) | 90% | "90% of the tax due for that tax year" |
| Option 2: the immediately PREVIOUS tax year (2025) | 100% | "100% of the tax due for the immediately previous tax year" |
| Option 3: the PRE-PRECEDING tax year (2024), direct debit payers only | 105% | "105% of the tax due for the tax year preceding the immediately previous tax year" |
| Due date | 31 October of the tax year | "You must pay this by 31 October of the tax year in question." |
| What it covers | Income Tax, PRSI and USC | "your estimate of the Income Tax, Pay Related Social Insurance (PRSI) and Universal Social Charge (USC)" |

The 105% option in the table above applies ONLY where preliminary tax is paid by direct debit. It does NOT apply if the tax due for the pre-preceding year was nil. Revenue's page says: "This option only applies where you pay by direct debit. It does not apply if the tax due for the pre-preceding year was nil."

### The 2026 pay and file dates

| Item | Value | Note (verbatim) |
| --- | --- | --- |
| Source | all figures below | https://www.revenue.ie/en/tax-professionals/ebrief/2026/no-0342026.aspx |
| ROS extended date, 2025 Form 11 balance and the 2026 preliminary tax | 18 November 2026 | "the due date is extended to Wednesday 18 November 2026." |
| Date when only one of filing or paying (or neither) is done on ROS | 31 October 2026 | "the required date to submit both returns and payments is no later than 31 October 2026." |

The extension in the table above applies only to a customer who BOTH files the 2025 Form 11 AND pays through ROS (Revenue eBrief No. 034/26, 16 February 2026). Revenue's words: "To qualify for the extension, customers must both pay and file through ROS. Where only one of these actions is completed through ROS, the extension does not apply". A paper return, or a ROS return paid some other way, keeps 31 October 2026 for BOTH the return and the payments.

**Conservative defaults**

| Ambiguity | Default |
| --- | --- |
| Option selection unclear | Use the previous year option (no estimate of the current year needed) |
| Filing and payment method unclear | Confirm that BOTH the return and the payment go through ROS before relying on the extended date; otherwise use 31 October 2026 |
| CGT included in preliminary tax | EXCLUDE: CGT has its own payment dates |
| First year of self-assessment | Ask: the previous year option is available, and generally means nothing is payable (Section 5.5) |
| Previous year liability unknown | STOP: the previous year option needs the final figure for 2025 |
| Direct debit not confirmed | Do not use the pre-preceding year option |

## Section 2. Required inputs and refusal catalogue

### Required inputs

- **Minimum viable inputs**: the final self-assessed liability (Income Tax, USC and PRSI) for 2025 for the previous year option, OR a reasoned estimate of the 2026 liability for the current year option.
- **Recommended inputs**: whether the client files AND pays on ROS, whether the client pays preliminary tax by direct debit (and since when), the 2024 final liability if on direct debit, PAYE already deducted, CGT disposals (separate), expected 2026 income.
- **Ideal inputs**: the 2025 and 2024 Form 11 and Revenue's acknowledgement of self-assessment, a 2026 profit projection, PAYE details.
- **Refusal policy if minimum is missing**: HARD STOP for the previous year option without the 2025 figure. For the current year option, an estimate is needed and the interest risk must be stated.

### Refusal catalogue

- **R-IE-PT-1 Trust or corporate preliminary tax**: Trigger: client asks about corporation tax or trust preliminary tax. Message: "This Guide covers individuals in Income Tax self-assessment only."
- **R-IE-PT-2 CGT computation**: Trigger: client asks how to compute CGT. Message: "CGT has its own payment dates and is NOT part of the preliminary tax payment. CGT computation is outside this Guide."
- **R-IE-PT-3 Non-resident self-assessment**: Trigger: non-resident client. Message: "Non-resident self-assessment is outside this Guide."

## Section 3. Payment pattern library

This is the deterministic pre-classifier for bank statement transactions. When a debit matches a pattern below, classify it as a preliminary tax payment, subject to the timing checks.

### 3.1 Revenue preliminary tax debits

**Revenue preliminary tax debits**

| Pattern | Treatment | Notes |
| --- | --- | --- |
| REVENUE, REVENUE COMMISSIONERS | Preliminary tax payment | Match with October or November timing |
| ROS PAYMENT, ROS DEBIT | Preliminary tax payment | ROS online payment (ROS Debit Instruction) |
| PRELIMINARY TAX, PRELIM TAX | Preliminary tax payment | Explicit description |
| FORM 11, SELF ASSESSMENT | Preliminary tax or balance payment | Distinguish by timing and amount |
| INCOME TAX REVENUE | Preliminary tax payment | Generic description |

### 3.2 Timing-based identification

**Timing-based identification**

| Debit date range | Likely payment | Confidence |
| --- | --- | --- |
| 15 October to 5 November | Preliminary tax (date without the ROS extension, 31 October) | High if Revenue payee |
| 1 November to 20 November | Preliminary tax paid on ROS (2026 extended date: see the pay and file table in Section 1) | High |
| Same date: large single debit | Combined: balance for the previous year plus preliminary tax for the current year | Flag for reviewer to split |
| Around the ninth day of each month | Preliminary tax by direct debit (Section 5.4) | High if Revenue payee |

### 3.3 Related but NOT preliminary tax

**Related but NOT preliminary tax**

| Pattern | Treatment | Notes |
| --- | --- | --- |
| CGT, CAPITAL GAINS TAX | EXCLUDE | Separate obligation, separate dates |
| PAYE, EMPLOYER PAYE | EXCLUDE | Employer PAYE payment |
| VAT, VAT3 RETURN | EXCLUDE | VAT payment |
| PRSI EMPLOYER | EXCLUDE | Employer PRSI |
| LOCAL PROPERTY TAX, LPT | EXCLUDE | Property tax (but see the surcharge note in Section 6.2) |
| USC DIRECT | EXCLUDE | USC coded through employment |
| SURCHARGE, INTEREST REVENUE | EXCLUDE | Penalty or interest |

### 3.4 Direct debit identification

- **Direct debit identification**: Revenue collects the preliminary Income Tax direct debit "on the ninth day of the month, or next working day" ([Revenue: Preliminary Income Tax direct debit](https://www.revenue.ie/en/starting-a-business/paying-your-tax/monthly-direct-debit/preliminary-income-tax.aspx)). Monthly debits to Revenue on that day are direct debit preliminary tax payments. Flag for reviewer, because the client may also be using the pre-preceding year option.

## The method, step by step

1. **Confirm the client is in Income Tax self-assessment and the year.** Preliminary tax for 2026 is paid in 2026 and covers Income Tax, PRSI and USC for 2026 ([Revenue: What is preliminary tax?](https://www.revenue.ie/en/self-assessment-and-self-employment/guide-to-self-assessment/preliminary-tax.aspx)).
2. **Work out the three amounts in the first table of Section 1.** Current year: the share of the 2026 tax due. Previous year: the share of the final 2025 tax due. Pre-preceding year: the share of the final 2024 tax due, and only if the client pays by direct debit AND the 2024 tax due was not nil ([Revenue: What is preliminary tax?](https://www.revenue.ie/en/self-assessment-and-self-employment/guide-to-self-assessment/preliminary-tax.aspx)).
3. **Pick the lowest amount the client can rely on.** The payment must be equal to, or more than, the LOWEST of the amounts that apply. The previous year option needs no estimate. The current year option depends on an estimate, so a low estimate risks interest ([Tax and Duty Manual Part 41-00-28, section 3](https://www.revenue.ie/en/tax-professionals/tdm/income-tax-capital-gains-tax-corporation-tax/part-41/41-00-28.pdf)).
4. **Include PRSI Class S and USC in every amount.** For 2026 self-employed income returned through self-assessment, use the blended Class S rate in the PRSI table in Section 7, not the 2025 rate ([gov.ie: PRSI Class S rates](https://www.gov.ie/en/department-of-social-protection/publications/prsi-class-s-rates/)).
5. **Fix the payment date.** 31 October 2026, or 18 November 2026 only if the client BOTH files the 2025 Form 11 AND pays through ROS ([Revenue eBrief No. 034/26](https://www.revenue.ie/en/tax-professionals/ebrief/2026/no-0342026.aspx)).
6. **Choose the payment method.** ROS (ROS Debit Instruction or card), myAccount (Single Debit Instruction or card), or direct debit set up through ROS ([Revenue: What is preliminary tax?](https://www.revenue.ie/en/self-assessment-and-self-employment/guide-to-self-assessment/preliminary-tax.aspx)). A direct debit must meet the minimum number of monthly payments in Section 5.4 ([Tax and Duty Manual Part 41-00-28, section 4.3](https://www.revenue.ie/en/tax-professionals/tdm/income-tax-capital-gains-tax-corporation-tax/part-41/41-00-28.pdf)).
7. **Keep CGT out.** CGT has its own payment dates (Section 8) ([Revenue: When and how do you pay and file CGT?](https://www.revenue.ie/en/gains-gifts-and-inheritance/transfering-an-asset/when-and-how-do-you-pay-and-file-cgt.aspx)).
8. **Warn about interest and the surcharge.** If preliminary tax is late or too low, the due date of the whole liability goes back to 31 October of the tax year and interest runs daily (Section 6.1). A late Form 11 adds a surcharge whether or not the payment was on time (Section 6.2) ([Revenue: Pay and file system](https://www.revenue.ie/en/self-assessment-and-self-employment/guide-to-self-assessment/pay-file-system.aspx)).

## Ask the client first

- Will you file your 2025 Form 11 AND make the payment through ROS? (If either is not on ROS, the date is 31 October 2026, not 18 November 2026.)
- Do you pay preliminary tax by monthly direct debit, and has the direct debit run for the minimum number of months this year? (Only then is the pre-preceding year option open.)
- What was your final tax due for 2025, and for 2024? (Was the 2024 figure nil?)
- Is this your first year in self-assessment? Were you taxed only under PAYE last year? Is your non-PAYE income above the registration limits in Section 8?
- Do you expect 2026 income to fall well below 2025? (Only then is the current year option worth the estimation risk.)
- Did you dispose of any asset in 2026? (CGT is paid separately, on its own dates.)

## Section 4. Worked examples (hypothetical amounts)

### Example 1. Previous year option

**Input:** Final 2025 tax due (Income Tax, USC and PRSI) EUR 15,000. Expected 2026 tax due EUR 18,000. No direct debit. ([Revenue: What is preliminary tax?](https://www.revenue.ie/en/self-assessment-and-self-employment/guide-to-self-assessment/preliminary-tax.aspx))

**Output:** Current year option: 90% of EUR 18,000 = EUR 16,200. Previous year option: 100% of EUR 15,000 = EUR 15,000. The lowest is EUR 15,000. Pay at least that by 31 October 2026, or by 18 November 2026 if the 2025 return is filed AND the payment made on ROS. ([Revenue: What is preliminary tax?](https://www.revenue.ie/en/self-assessment-and-self-employment/guide-to-self-assessment/preliminary-tax.aspx))

### Example 2. Current year option, income drop

**Input:** Final 2025 tax due EUR 30,000. Expected 2026 tax due EUR 10,000. ([Revenue: What is preliminary tax?](https://www.revenue.ie/en/self-assessment-and-self-employment/guide-to-self-assessment/preliminary-tax.aspx))

**Output:** Current year option: 90% of EUR 10,000 = EUR 9,000. That is lower than the previous year option, so EUR 9,000 is enough IF the estimate holds. If the final 2026 tax due turns out to be EUR 12,000, then 90% of it is EUR 10,800. The EUR 9,000 paid is below both EUR 10,800 and EUR 30,000, so preliminary tax was too low. The due date for the whole 2026 liability then goes back to 31 October 2026 and interest runs from that date. ([Revenue: What is preliminary tax?](https://www.revenue.ie/en/self-assessment-and-self-employment/guide-to-self-assessment/preliminary-tax.aspx))

### Example 3. Direct debit, pre-preceding year option

**Input:** Client has paid preliminary tax by direct debit for several years. Final 2024 tax due EUR 8,000. ([Revenue: What is preliminary tax?](https://www.revenue.ie/en/self-assessment-and-self-employment/guide-to-self-assessment/preliminary-tax.aspx))

**Output:** Pre-preceding year option: 105% of EUR 8,000 = EUR 8,400 across the 2026 direct debit payments, if this is lower than the other options. If the 2024 tax due was nil, this option is not available. ([Revenue: What is preliminary tax?](https://www.revenue.ie/en/self-assessment-and-self-employment/guide-to-self-assessment/preliminary-tax.aspx))

### Example 4. First year in self-assessment

**Input:** Taxed only under PAYE in 2025. Started self-employment in 2026.

**Output:** The client may choose the previous year option. Revenue says that with this choice the client generally will not have to pay preliminary tax, because in the first year the previous year's liability would normally be nil. The client may instead pay on the current year option, which reduces the tax to pay in the following year. The 2026 balance is then due by 31 October 2027.

### Example 5. CGT kept separate

**Input:** 2026 preliminary tax due for Income Tax, USC and PRSI. The client also sold shares in June 2026.

**Output:** Preliminary tax is due by 31 October 2026 (or the ROS extended date). The CGT on the June disposal is due by 15 December 2026. Two separate payments.

### Example 6. Bank statement classification

**Input line:** `31.10.2026 ; REVENUE COMMISSIONERS ROS ; DEBIT ; PRELIMINARY TAX ; -15,000.00 ; EUR`

**Classification:** Preliminary tax for 2026 (it may also include the 2025 balance: flag for split). Tax payment, not a deductible expense.

## Section 5. Computation rules

### 5.1 The three options

**The three options** (percentages as in the first table of Section 1)

| Option | Year it looks at | Conditions |
| --- | --- | --- |
| Current year | 2026 (the year being paid for) | None, but it depends on an estimate |
| Previous year | 2025 | None. No estimate needed |
| Pre-preceding year | 2024 | Only if paid by direct debit, and NOT if the 2024 tax due was nil |

- **Compliance test**: the preliminary tax paid must be equal to, or more than, the LOWEST of the options that apply to the client. Paying at least that lowest amount avoids interest on preliminary tax ([Revenue: What is preliminary tax?](https://www.revenue.ie/en/self-assessment-and-self-employment/guide-to-self-assessment/preliminary-tax.aspx)).

### 5.2 What counts as "tax"

- **Definition**: preliminary tax covers Income Tax, PRSI and USC ([Tax and Duty Manual Part 41-00-28, section 3](https://www.revenue.ie/en/tax-professionals/tdm/income-tax-capital-gains-tax-corporation-tax/part-41/41-00-28.pdf)). For PRSI Class S, see Section 7.

### 5.3 Computation steps

~~~
current_option   = 0.90 x estimated 2026 tax due (Income Tax + USC + PRSI)
previous_option  = 1.00 x final 2025 tax due
preprec_option   = 1.05 x final 2024 tax due   (only if direct debit, and only if the 2024 tax due is not nil)
minimum_required = lowest of the options that apply
~~~

The multipliers above are the percentages in the first table of Section 1. Paying the previous year option is the safe choice when no reliable 2026 estimate exists.

### 5.4 Direct debit

- **Pre-preceding year option**: available only to direct debit payers (Section 1). Revenue's direct debit page: "Customers who pay preliminary Income Tax by direct debit can also apply the 105% of the pre-proceeding rule when calculating their preliminary Income Tax amount" ([Revenue: Preliminary Income Tax direct debit](https://www.revenue.ie/en/starting-a-business/paying-your-tax/monthly-direct-debit/preliminary-income-tax.aspx)).
- **Minimum payments**: a client can join at any time in the calendar year as long as they make at least 3 equal monthly payments in that year. In the second and later years there must be 8 or more monthly payments ([Tax and Duty Manual Part 41-00-28, section 4.3](https://www.revenue.ie/en/tax-professionals/tdm/income-tax-capital-gains-tax-corporation-tax/part-41/41-00-28.pdf)).
- **Set-up and changes**: apply through ROS. The client can raise or lower the monthly amount on ROS at any stage, but must still meet the expected preliminary tax amount. A payment the bank returns unpaid is the client's responsibility to pay ([Revenue: Preliminary Income Tax direct debit](https://www.revenue.ie/en/starting-a-business/paying-your-tax/monthly-direct-debit/preliminary-income-tax.aspx)).

### 5.5 First year rule

- **First year**: in the first year in self-assessment, the client can choose EITHER the previous year option (generally nothing to pay, because the previous year's liability is normally nil) OR the current year option, which reduces the tax to pay the following year ([Revenue: What is preliminary tax?](https://www.revenue.ie/en/self-assessment-and-self-employment/guide-to-self-assessment/preliminary-tax.aspx)). The live Guide said a first-year client must use the current year option. That was wrong.
- **First return**: a person who enters self-assessment because they started to trade can file the first and second year returns by the return filing date for the second year. This extension covers the RETURN only. The due date for preliminary tax and the balance for the first year does not change ([Tax and Duty Manual Part 41-00-28, section 5.5](https://www.revenue.ie/en/tax-professionals/tdm/income-tax-capital-gains-tax-corporation-tax/part-41/41-00-28.pdf)).

## Section 6. Penalties and interest

### 6.1 Interest on late or insufficient payment

If preliminary tax is not paid by 31 October, the direct debit arrangement is not kept, or the amount paid is too low, the client may be liable to interest. The due date for the full liability or the balance is then backdated to 31 October in the year of assessment. Interest under section 1080 of the Taxes Consolidation Act 1997 is due for each day, or part of a day ([Tax and Duty Manual Part 41-00-28, section 3.4](https://www.revenue.ie/en/tax-professionals/tdm/income-tax-capital-gains-tax-corporation-tax/part-41/41-00-28.pdf)).

| Item | Value | Note (verbatim) |
| --- | --- | --- |
| Source | all figures below | https://www.revenue.ie/en/tax-professionals/tdm/collection/debt-management/guidelines-for-charging-interest-on-late-payment.pdf |
| Daily interest rate, Income Tax, from 1 July 2009 | 0.0219% | "IT 0.0273% 0.0219% CT 0.0273% 0.0219%" (the second column is "Daily Rates from 1/7/2009") |

The manual prints the rate per day only. This Guide gives no annual equivalent, because no allowed page prints one.

### 6.2 Surcharge for a late return

| Item | Value | Note (verbatim) |
| --- | --- | --- |
| Source | all figures below | https://www.revenue.ie/en/self-assessment-and-self-employment/guide-to-self-assessment/pay-file-system.aspx |
| Return filed less than two months after the filing date | 5% of tax due, capped at EUR 12,695 | "a surcharge of 5% of your tax due, up to €12,695, is applied" |
| Return filed more than two months after the filing date | 10% of tax due, capped at EUR 63,485 | "a surcharge of 10% of your tax due, up to €63,485, is applied" |

- **The surcharge follows the RETURN, not the payment.** A late Form 11 triggers the surcharge in the table above even if the tax was paid on time. The cap is an ALLOWANCE limit: the surcharge is the percentage of tax due, but never more than the cap.
- **Local Property Tax**: Revenue's page also warns that a 10% surcharge "may apply to your final liability if your Local Property Tax (LPT) obligations are not met", even if Income Tax is paid and filed on time ([Revenue: Pay and file system](https://www.revenue.ie/en/self-assessment-and-self-employment/guide-to-self-assessment/pay-file-system.aspx)).

## Section 7. PRSI Class S

| Item | Value | Note (verbatim) |
| --- | --- | --- |
| Source | all figures below | https://www.gov.ie/en/department-of-social-protection/publications/prsi-class-s-rates/ |
| Blended Class S rate, 2026 self-employed income returned through self-assessment | 4.2375% | "for 2026 income the rate will be 4.2375% or min payment of €650" |
| Blended Class S rate, 2025 self-employed income (the 2025 balance paid in 2026) | 4.125% | "a blended or proportionate rate of 4.125% or a minimum payment of €650 will apply on their self-employed 2025 annual income" |
| Minimum annual Class S contribution | EUR 650 | "the minimum annual contribution for Class S is €650" |

| Item | Value | Note (verbatim) |
| --- | --- | --- |
| Source | all figures below | https://assets.gov.ie/static/documents/cb168977/PRSI_C20260116_Contribution_Rates_and_User_Guide_-_SW_14_-_English_Version_-_January_2026_.pdf-web.pdf |
| Class S applies to self-employed annual income of this amount OR MORE | EUR 5,000 | "Self-employed contributors with annual income of €5,000 or over pay Class S PRSI" |

- **Which rate for preliminary tax**: preliminary tax for 2026 estimates 2026 income, so the 2026 blended rate in the first table above applies. The 2025 rate applies to the 2025 balance paid on the same day. The live Guide applied the 2025 rate to 2026.
- **Who decides the class**: the Department of Social Protection determines the PRSI class ([Tax and Duty Manual Part 41-00-28, section 6.2](https://www.revenue.ie/en/tax-professionals/tdm/income-tax-capital-gains-tax-corporation-tax/part-41/41-00-28.pdf)).
- **PRSI collection method**: Class S PRSI is part of preliminary tax and is collected through self-assessment.

## Section 8. Edge cases

**Previous year liability was small.** No allowed page sets a minimum below which preliminary tax is not needed. Apply the three options as normal. The Form 11 must still be filed.

**Income drop.** Use the current year option only with a reasoned estimate. Risk: interest from 31 October if the estimate is too low (Example 2).

**First year.** See Section 5.5: the previous year option is available and generally means nothing is payable.

**ROS extended date.** 18 November 2026 ONLY where the client both files the 2025 Form 11 and pays through ROS. Otherwise 31 October 2026 (pay and file table, Section 1). People who registered (or re-registered) for self-assessment from 1 January 2015 must file and pay electronically ([Tax and Duty Manual Part 41-00-28, section 5.2](https://www.revenue.ie/en/tax-professionals/tdm/income-tax-capital-gains-tax-corporation-tax/part-41/41-00-28.pdf)).

**CGT.** CGT dates are separate from preliminary tax:

| Item | Value | Note (verbatim) |
| --- | --- | --- |
| Source | all figures below | https://www.revenue.ie/en/gains-gifts-and-inheritance/transfering-an-asset/when-and-how-do-you-pay-and-file-cgt.aspx |
| Disposals 1 January to 30 November | Pay by 15 December of the same year | "1 January and 30 November (the initial period), you must pay CGT by 15 December of the same year" |
| Disposals 1 December to 31 December | Pay by 31 January of the next year | "1 December and 31 December (the later period), you must pay CGT by 31 January of the next year." |

**Rental income and other non-PAYE income.** Preliminary tax arises only for a person in Income Tax self-assessment. Revenue's registration test is in the table below. Either limit alone brings the person in (Revenue joins them with "or"). Below both limits Revenue says: "To declare non-PAYE income that does not exceed the above amounts, please submit a Form 12 online using myAccount." A landlord who is in self-assessment uses the same three options on the tax due for the year.

| Item | Value | Note (verbatim) |
| --- | --- | --- |
| Source | all figures below | https://www.revenue.ie/en/self-assessment-and-self-employment/guide-to-self-assessment/register-it-self-assessment.aspx |
| Must register for self-assessment: taxable non-PAYE income MORE THAN (this is a different rule from the PRSI Class S threshold in Section 7) | EUR 5,000 | "your taxable non-PAYE income exceeds €5,000" |
| Must register for self-assessment: gross non-PAYE income MORE THAN | EUR 30,000 | "or your gross non-PAYE income exceeds €30,000" |

**Direct debit.** Monthly payments under the pre-preceding year option. Check the minimum number of payments (Section 5.4). Flag for reviewer.

**Late return, payment on time.** The surcharge still applies (Section 6.2).

**Early paper filer.** A paper return filed before 31 August lets Revenue complete the self-assessment panel. For the last few years, including 2026, that date has been concessionally extended to 30 September ([Tax and Duty Manual Part 41-00-28, section 2.1](https://www.revenue.ie/en/tax-professionals/tdm/income-tax-capital-gains-tax-corporation-tax/part-41/41-00-28.pdf)).

## Section 9. Self-checks

Before delivering output, check:

- [ ] Each option names its own year: current (2026), previous (2025), pre-preceding (2024)
- [ ] Pre-preceding year option used only with direct debit AND a non-nil 2024 figure
- [ ] Income Tax, USC and PRSI all included
- [ ] PRSI Class S uses the 2026 blended rate for 2026 income
- [ ] CGT excluded from the preliminary tax payment
- [ ] Date: 18 November 2026 only if BOTH filed and paid on ROS, otherwise 31 October 2026
- [ ] First-year client told that the previous year option is available
- [ ] Interest risk stated where the current year option is used
- [ ] Surcharge risk noted for a late return
- [ ] Output labelled as an estimate until an Irish chartered accountant or chartered tax adviser confirms

## Section 10. Test suite (hypothetical amounts)

### Test 1. Previous year option

**Input:** 2025 tax due EUR 15,000. 2026 estimate EUR 18,000. No direct debit. ([Revenue: What is preliminary tax?](https://www.revenue.ie/en/self-assessment-and-self-employment/guide-to-self-assessment/preliminary-tax.aspx))
**Expected:** Minimum EUR 15,000 (lower than EUR 16,200). Due 31 October 2026, or 18 November 2026 if filed AND paid on ROS. ([Revenue: What is preliminary tax?](https://www.revenue.ie/en/self-assessment-and-self-employment/guide-to-self-assessment/preliminary-tax.aspx))

### Test 2. Current year option

**Input:** 2025 tax due EUR 30,000. 2026 estimate EUR 10,000. ([Revenue: What is preliminary tax?](https://www.revenue.ie/en/self-assessment-and-self-employment/guide-to-self-assessment/preliminary-tax.aspx))
**Expected:** EUR 9,000. Interest risk flagged. ([Revenue: What is preliminary tax?](https://www.revenue.ie/en/self-assessment-and-self-employment/guide-to-self-assessment/preliminary-tax.aspx))

### Test 3. First year

**Input:** First year in self-assessment, PAYE only before.
**Expected:** Previous year option available; generally no preliminary tax payable. Current year option optional.

### Test 4. Direct debit

**Input:** Direct debit payer. 2024 tax due EUR 8,000. ([Revenue: What is preliminary tax?](https://www.revenue.ie/en/self-assessment-and-self-employment/guide-to-self-assessment/preliminary-tax.aspx))
**Expected:** EUR 8,400 if lowest. If 2024 tax due was nil: option not available. ([Revenue: What is preliminary tax?](https://www.revenue.ie/en/self-assessment-and-self-employment/guide-to-self-assessment/preliminary-tax.aspx))

### Test 5. CGT separate

**Input:** Preliminary tax due. Shares sold in June 2026.
**Expected:** Preliminary tax by 31 October 2026 (or ROS extended date). CGT by 15 December 2026.

### Test 6. Surcharge

**Input:** Tax due EUR 20,000. Return filed 6 weeks late. ([Revenue: Pay and file system](https://www.revenue.ie/en/self-assessment-and-self-employment/guide-to-self-assessment/pay-file-system.aspx))
**Expected:** Surcharge 5% = EUR 1,000 (below the cap). ([Revenue: Pay and file system](https://www.revenue.ie/en/self-assessment-and-self-employment/guide-to-self-assessment/pay-file-system.aspx))

### Test 7. Surcharge cap

**Input:** Tax due EUR 800,000. Return filed 3 months late. ([Revenue: Pay and file system](https://www.revenue.ie/en/self-assessment-and-self-employment/guide-to-self-assessment/pay-file-system.aspx))
**Expected:** 10% would be EUR 80,000, so the cap applies: EUR 63,485. ([Revenue: Pay and file system](https://www.revenue.ie/en/self-assessment-and-self-employment/guide-to-self-assessment/pay-file-system.aspx))

### Test 8. ROS filing, payment by other means

**Input:** 2025 Form 11 filed on ROS on 10 November 2026. Payment made through myAccount.
**Expected:** Extension does not apply. Both the return and the payments were due by 31 October 2026. The return filed on 10 November 2026 is late by less than two months, so the 5% surcharge in Section 6.2 applies.

## When to refuse or refer

- Corporation tax, trusts, or non-resident self-assessment: refuse (Section 2).
- CGT computation: refer. This Guide only keeps CGT out of the preliminary tax payment.
- The client cannot give a final 2025 figure and has no reasoned 2026 estimate: stop.
- Disputes about interest charged, or requests to waive interest: refer to an Irish chartered accountant or chartered tax adviser.
- Questions about which PRSI class applies: refer to the Department of Social Protection, which decides the class.
- Any figure for 2027 (Budget 2027 is due in October 2026): refer until Revenue publishes it.

## Prohibitions

- NEVER tell a client the previous year option needs an estimate of the current year. It does not.
- NEVER promise the ROS extended date unless the client both files AND pays through ROS
- NEVER include CGT in the preliminary tax payment
- NEVER forget USC and PRSI when computing "tax due"
- NEVER ignore the surcharge for a late return. It applies even if payment is on time
- NEVER apply the pre-preceding year option without confirming a direct debit, or where the 2024 tax due was nil
- NEVER tell a first-year client they must use the current year option
- NEVER invent a minimum below which no preliminary tax is due
- NEVER present preliminary tax as final. The balance is settled with the Form 11 for the year

## Sources

- [Revenue: What is preliminary tax?](https://www.revenue.ie/en/self-assessment-and-self-employment/guide-to-self-assessment/preliminary-tax.aspx)
- [Revenue: Who should register for Income Tax self-assessment?](https://www.revenue.ie/en/self-assessment-and-self-employment/guide-to-self-assessment/register-it-self-assessment.aspx)
- [Revenue: Pay and file system, how does it work?](https://www.revenue.ie/en/self-assessment-and-self-employment/guide-to-self-assessment/pay-file-system.aspx)
- [Revenue eBrief No. 034/26: Pay and File Extension Date 2026](https://www.revenue.ie/en/tax-professionals/ebrief/2026/no-0342026.aspx)
- [Revenue Tax and Duty Manual Part 41-00-28, A Guide to Self-Assessment](https://www.revenue.ie/en/tax-professionals/tdm/income-tax-capital-gains-tax-corporation-tax/part-41/41-00-28.pdf)
- [Revenue Tax and Duty Manual: Guidelines for charging interest on late payment](https://www.revenue.ie/en/tax-professionals/tdm/collection/debt-management/guidelines-for-charging-interest-on-late-payment.pdf)
- [Revenue: Preliminary Income Tax direct debit](https://www.revenue.ie/en/starting-a-business/paying-your-tax/monthly-direct-debit/preliminary-income-tax.aspx)
- [gov.ie: PRSI Class S rates](https://www.gov.ie/en/department-of-social-protection/publications/prsi-class-s-rates/)
- [gov.ie: SW14 PRSI Contribution Rates and User Guide, January 2026](https://assets.gov.ie/static/documents/cb168977/PRSI_C20260116_Contribution_Rates_and_User_Guide_-_SW_14_-_English_Version_-_January_2026_.pdf-web.pdf)
- [Revenue: When and how do you pay and file CGT?](https://www.revenue.ie/en/gains-gifts-and-inheritance/transfering-an-asset/when-and-how-do-you-pay-and-file-cgt.aspx)

## Disclaimer

This Guide and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this Guide. All outputs must be reviewed and signed off by a qualified professional (such as a CPA, EA, tax attorney, or equivalent licensed practitioner in your jurisdiction) before filing or acting upon.

The most up-to-date version of this Guide is maintained at openaccountants.com. Log in to access the latest version, request a professional review from a licensed accountant, and track updates as tax law changes.

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
