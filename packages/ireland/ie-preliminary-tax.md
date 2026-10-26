---
name: ie-preliminary-tax
description: "Irish preliminary tax for individuals in income tax self-assessment, tax year 2026, under Chapter 7 of Part 41A of the Taxes Consolidation Act 1997 (ss.959AM to 959AP) as amended by Finance Act 2025 s.100. Covers who pays (chargeable persons filing Form 11), what it covers (income tax, USC, PRSI), the three safe harbours (90% of 2026, 100% of 2025, 105% of 2024 for direct debit payers only), first-year nil, the 31 October 2026 date and the ROS extension to 18 November 2026, monthly direct debit, the backdating of the whole liability to 31 October and interest at 0.0219% a day, the late return surcharge, and Form 11 pay and file. Trigger on 'preliminary tax Ireland', '90% rule', '100% rule', '105% direct debit', 'pay and file', 'preliminary tax interest'. Out of scope: company preliminary tax (ie-corporation-tax), computing the Form 11 liability (ie-income-tax-form11), USC (ie-usc), PRSI (ie-prsi-class-s), CGT (ie-cgt)."
version: 2.1
jurisdiction: IE
category: international
tax_year: 2026
last_updated: 2026-10-24
authored_by: Michael Cutajar and the OpenAccountants team
review_status: pending_review
trust_label: Built by Michael Cutajar and the OpenAccountants team
depends_on:
  - income-tax-workflow-base
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Ireland preliminary tax for self-assessed individuals, tax year 2026

> **Source-cited draft.** Drafted from Chapter 7 of Part 41A of the Taxes Consolidation Act 1997 (TCA), inserted by Finance Act 2012 s.129 and Sch. 4 and amended by Finance Act 2025 s.100, read in the enacted text on irishstatutebook.ie and in Revenue's Notes for Guidance, Finance Act 2025 edition (Parts 41A and 47), with Revenue's Tax and Duty Manuals and pages, all read on 2026-10-24. There is no official consolidated text of the TCA; the section text below is the enacted text plus the enacted amendments. No accountant has reviewed this skill.

Authority: the Revenue Commissioners (the Collector-General collects). The tax year is the calendar year. Currency: euro. Section numbers are TCA 1997 unless another act is named.

See also: `ie-income-tax-form11` (computing the Form 11 liability and the return), `ie-usc` (USC), `ie-prsi-class-s` (PRSI Class S), `ie-paye-rental-nonresident` (PAYE workers with side income, non-residents), `ie-cgt` (CGT, which has no preliminary tax), `ie-corporation-tax` (company preliminary tax).

## Who this applies to

- **Chargeable persons.** Every chargeable person must pay preliminary tax for each chargeable period (s.959AN(1)). For income tax, a chargeable person is a person chargeable to tax for the year, other than a PAYE taxpayer excluded by s.959B(1) (s.959A). In practice: sole traders, professionals, partners, proprietary directors, landlords and others who are in self-assessment and file Form 11.
- **Who must register.** Revenue's test: register for income tax self-assessment if taxable non-PAYE income exceeds EUR 5,000, or gross non-PAYE income exceeds EUR 30,000. Below both, a PAYE worker declares the income on Form 12 through myAccount and has no preliminary tax ([Revenue, who should register](https://www.revenue.ie/en/self-assessment-and-self-employment/guide-to-self-assessment/register-it-self-assessment.aspx)). This is a different test from the Class S floor (EUR 5,000 or more of reckonable income) in `ie-prsi-class-s`.
- **What it covers.** Income tax, USC and PRSI for the year. USC is due and payable as income tax is for a chargeable person, and can sit in one assessment with income tax (s.531AS). Class S PRSI on reckonable income is charged and paid as if it were income tax, in one sum with it (Social Welfare Consolidation Act 2005 s.23(4)). Revenue says preliminary tax must cover all three ([TDM 41-00-28, para 3](https://www.revenue.ie/en/tax-professionals/tdm/income-tax-capital-gains-tax-corporation-tax/part-41/41-00-28.pdf)).
- **Not CGT.** Section 959AN does not apply to capital gains tax (s.959AN(5)). CGT has its own dates (s.959AQ): gains from 1 January to 30 November are due by 15 December of the same year; gains in December are due by 31 January of the next year. See `ie-cgt`.
- **Not companies.** Companies pay preliminary corporation tax under ss.959AR to 959AT on different dates and tests. See `ie-corporation-tax`.

## Rates, bands and thresholds

| Item | Rate or amount | Year | Source |
|---|---|---|---|
| Preliminary tax due date (not direct debit) | 31 October of the tax year: 31 October 2026 for 2026 | 2026 | s.959AO(1); https://www.irishstatutebook.ie/eli/2012/act/9/enacted/en/print |
| Safe harbour 1: current year | 90% of the income tax payable for 2026 | 2026 | s.959AO(3)(b)(i); same |
| Safe harbour 2: preceding year | 100% of the income tax payable for 2025 | 2026 | s.959AO(3)(b)(ii); same |
| Safe harbour 3: pre-preceding year, direct debit payers only | 105% of the income tax payable for 2024; not available if that was nil, or is taken as nil because the person was not a chargeable person for 2024 | 2026 | s.959AO(3)(b)(iii); same |
| Preceding or pre-preceding year when not a chargeable person then | Taken as nil | 2026 | s.959AO(4)(a); same |
| ROS extension, 2025 Form 11 balance and 2026 preliminary tax | Wednesday 18 November 2026, only if the person both pays and files through ROS | 2026 | https://www.revenue.ie/en/tax-professionals/ebrief/2026/no-0342026.aspx |
| Balance of 2026 tax (if preliminary tax was sufficient and on time) | Specified return date: 31 October 2027 | 2026 | s.959AO(2), s.959A; https://www.irishstatutebook.ie/eli/2012/act/9/enacted/en/print |
| Direct debit collection day | 9th of the month, or next working day | 2026 | Collector-General's conditions under s.959AP(1)(b); https://www.revenue.ie/en/tax-professionals/tdm/collection/direct-debit/preliminary-income-tax-direct-debit-guidelines.pdf |
| Direct debit minimum monthly amount | EUR 10 | 2026 | s.959AP(1)(b) conditions; same |
| Direct debit: minimum number of instalments in law | None. Finance Act 2025 s.100 deleted s.959AP(2) to (4) (the 3 and 8 equal monthly instalment rule) | 2026 | https://www.irishstatutebook.ie/eli/2025/act/18/section/100/enacted/en/html |
| Interest on late income tax, USC and Class S | 0.0219% a day, for each day or part of a day, from 1 July 2009 | 2026 | s.1080(2); https://www.revenue.ie/en/tax-professionals/documents/notes-for-guidance/tca/part47.pdf |
| Late return surcharge, filed within 2 months of the return date | 5% of the tax, capped at EUR 12,695 | 2026 | s.1084(2)(a); same |
| Late return surcharge, filed 2 months or more late | 10% of the tax, capped at EUR 63,485 | 2026 | s.1084(2)(a); same |
| PRSI Class S in the 2026 estimate | 4.2375% blended rate for 2026 income (4.2% to 30 September, 4.35% from 1 October 2026); EUR 650 minimum | 2026 | https://www.gov.ie/en/department-of-social-protection/publications/prsi-class-s-rates/ |
| PRSI Class S in the 2025 balance | 4.125% blended rate for 2025 income | 2025 | same |

## The taxable base

Preliminary tax is not a separate tax. It is a payment on account of the year's income tax, USC and PRSI (s.959AN(3)). The base is the liability the person expects for the year (s.959AN(2)), and the tests compare what was paid with the "income tax payable", which is tax chargeable less the tax credits the Acts give (s.959A, "amount of tax payable").

**The test.** Preliminary tax for 2026 is sufficient if it is at least the lowest of the amounts that apply:

1. 90% of the final 2026 liability. This needs an estimate. If the estimate turns out low, the test fails.
2. 100% of the final 2025 liability. No estimate needed; this is the safe choice when 2026 is uncertain.
3. 105% of the final 2024 liability, only for a person who pays by direct debit under s.959AP, and not if the 2024 liability was nil or is taken as nil under s.959AO(4)(a) (s.959AO(3)(b)(iii)).

**What counts in the earlier years' figures.**
- A person who was not a chargeable person for 2025 (or 2024) is taken to have a nil liability for that year (s.959AO(4)(a)). So in the first year of self-assessment the 100% test is normally nil and no preliminary tax is needed to avoid interest. Paying 90% of the current year is still allowed and reduces the next year's bill ([Revenue, what is preliminary tax](https://www.revenue.ie/en/self-assessment-and-self-employment/guide-to-self-assessment/preliminary-tax.aspx)).
- Additional tax for 2025 or 2024 that becomes payable after 31 October 2026, under an amended assessment or appeal where the extra tax falls due one month later (s.959AU(2), s.959AV(2)), is left out (s.959AO(4)(b)).
- The 2025 and 2024 figures are taken before any film relief (s.481) or Part 16 relief (EII and similar) (s.959AO(4)(c)).
- Extra tax for the preceding year caused by a change of accounting date under s.65(3) is due by the return date and is left out of the test (s.959AO(6)).
- Joint assessment: where a person is jointly assessed for 2026 but was not the assessable spouse or civil partner in 2025 or 2024, the earlier years are read as if the couple had been jointly assessed with that person as the chargeable person (s.959AO(5)).

**Working rule.** For each option: income tax + USC + PRSI for that year, after credits and after tax deducted at source. Use the 2026 Class S rate (4.2375%) for the current-year option and the 2025 rate (4.125%) for the 2025 figure (see `ie-prsi-class-s`). Preliminary tax is a payment of tax, never a deductible business expense.

## Deadlines and filing

- **Pay and file, 31 October.** On one date the person pays preliminary tax for the current year, files the return and self-assessment for the previous year, and pays the balance for the previous year ([TDM 41-00-28, para 2](https://www.revenue.ie/en/tax-professionals/tdm/income-tax-capital-gains-tax-corporation-tax/part-41/41-00-28.pdf)). For 2026: 2026 preliminary tax, the 2025 Form 11 and the 2025 balance are due by Saturday 31 October 2026 (s.959AO(1); s.959A "specified return date").
- **ROS extension.** If the person both files the 2025 Form 11 and pays through ROS, the date is Wednesday 18 November 2026. "Where only one of these actions is completed through ROS, the extension does not apply and the required date to submit both returns and payments is no later than 31 October 2026" ([eBrief No. 034/26, 16 February 2026](https://www.revenue.ie/en/tax-professionals/ebrief/2026/no-0342026.aspx)). The extension is a Revenue administrative date, not a change to s.959AO.
- **Balance for 2026.** If 2026 preliminary tax passes a test and is paid on time, the 2026 balance is due with the 2026 Form 11 by 31 October 2027 (s.959AO(2)).
- **How to pay.** ROS (ROS Debit Instruction, or Visa or Mastercard debit or credit card); myAccount (Single Debit Instruction, or card); or monthly direct debit set up on ROS ([Revenue, what is preliminary tax](https://www.revenue.ie/en/self-assessment-and-self-employment/guide-to-self-assessment/preliminary-tax.aspx)). A ROS bank account must be in the SEPA zone (TDM 41-00-28, para 4.1). People who registered or re-registered for self-assessment from 1 January 2015 must file and pay electronically (TDM 41-00-28, para 5.2; S.I. No. 572 of 2014).
- **Direct debit.** Section 959AP applies to a person who authorises the Collector-General to debit their bank account for preliminary tax and meets the conditions the Collector-General reasonably imposes (s.959AP(1), as amended by Finance Act 2025 s.100). If all scheduled debits are paid, the preliminary tax is treated as paid on 31 October of the tax year, so debits in November and December still count as on time (s.959AP(5)). Revenue's terms: set up and manage it on the ROS Payments Hub (from August 2025); debits on the 9th of the month or next working day; the monthly amount can be raised or lowered at any time but not below EUR 10; the total must still meet the preliminary tax due ([Direct Debit Guidelines, October 2025](https://www.revenue.ie/en/tax-professionals/tdm/collection/direct-debit/preliminary-income-tax-direct-debit-guidelines.pdf); [Revenue direct debit page](https://www.revenue.ie/en/starting-a-business/paying-your-tax/monthly-direct-debit/preliminary-income-tax.aspx)). A debit returned unpaid is the person's to pay, on ROS or by card; if the bank reason shows all future debits will fail, Revenue cancels the mandate. The account must have a SEPA-reachable IBAN.
- **Old instalment minimums.** Before Finance Act 2025 s.100, s.959AP(2) required at least 3 equal monthly instalments in the first direct debit year and 8 in later years. That rule is gone from the law. Revenue's TDM 41-00-28 (updated August 2026, para 4.3) still prints it; the statute and Revenue's October 2025 direct debit guidelines do not.
- **First return.** A person who enters self-assessment because they started to trade can file the first and second year returns by the return date for the second year. That extension is for the return only; preliminary tax and the first year's balance keep their dates (TDM 41-00-28, para 5.5).
- **Early paper filers.** A paper return filed by 31 August (concessionally extended to 30 September for recent years, including 2026) lets Revenue complete the self-assessment panel, which helps fix the balance and the next year's preliminary tax (TDM 41-00-28, para 2.1, 5.4).
- **Recognising the payments on a bank statement.** Monthly debits to Revenue on or just after the 9th are preliminary tax direct debits. A single large payment to Revenue in late October or by 18 November usually combines the previous year's balance and the current year's preliminary tax and must be split using the Form 11 and Revenue's statement. CGT, VAT, employer PAYE and LPT payments are separate tax heads.

## Penalties and interest

- **Backdating.** The whole 2026 income tax (with USC and PRSI) is treated as due on 31 October 2026 if (a) preliminary tax was not paid, (b) it was less than the lowest test that applies, or (c) it was paid after 31 October 2026 (s.959AO(3)). Breaking the direct debit arrangement has the same effect, because s.959AP(5) then does not deem the payments made on 31 October (TDM 41-00-28, para 3.4).
- **Interest.** Unpaid tax carries interest of 0.0219% for each day or part of a day from the due date until payment (s.1080(2)). With backdating, interest runs from 31 October 2026 on whatever part of the 2026 liability was unpaid at each date, until the balance is paid. Interest is not deductible for tax (s.1080(3)).
- **Late return surcharge.** A return filed after the return date adds 5% of the tax for the year (cap EUR 12,695) if filed within 2 months, or 10% (cap EUR 63,485) if 2 months or more late (s.1084(2)(a)). The surcharge follows the return, not the payment: it applies even if all tax was paid on time. The ROS extension only helps where both filing and payment are on ROS.
- **Local Property Tax.** A 10% surcharge can apply to the final income tax liability if LPT obligations are not met, even if income tax is paid and filed on time ([Revenue, pay and file](https://www.revenue.ie/en/self-assessment-and-self-employment/guide-to-self-assessment/pay-file-system.aspx)).
- **Amended assessments.** Extra tax from an amended assessment is due on the original due date, unless the return made full and true disclosure, in which case it is due one month after the amendment (s.959AU(1), (2)). From Finance Act 2025 s.101, extra tax from a second or later amendment where the return did not make full and true disclosure is due on the original date (s.959AU(3)).

## Cross-border points

- **Non-residents.** Chapter 7 applies subject to s.579(4)(b) for non-residents (s.959AM(8)). A non-resident who is a chargeable person (for example with Irish rent or an Irish trade) is in the same preliminary tax system. See `ie-paye-rental-nonresident`.
- **Which country insures for PRSI.** If an A1 certificate or a bilateral agreement puts the person in another country's social insurance, there is no Class S in the estimate. Settle that first with `ie-prsi-cross-border`.
- **Arrival and departure years.** A person who becomes a chargeable person in 2026 for the first time has a nil 2025 figure (s.959AO(4)(a)), so the 100% test is nil. Residence and split-year rules are in `ie-cross-border`.
- **Paying from abroad.** ROS debit payments and direct debits need a bank account in the SEPA zone (TDM 41-00-28, para 4.1; Direct Debit Guidelines, para 4).

## Worked examples

### Example 1: sole trader, the 100% test, paying on ROS

Niamh is a sole trader. Her final 2025 liability is income tax EUR 13,000, USC EUR 2,100 and PRSI EUR 3,300: EUR 18,400 in all. She paid EUR 16,000 preliminary tax for 2025 on time. Her final 2024 liability was EUR 15,000, so that payment met the 100% test for 2025 and her 2025 balance carries no interest. She expects her 2026 liability to be EUR 21,000. She does not pay by direct debit, so only two tests apply. 90% of 2026 is EUR 18,900. 100% of 2025 is EUR 18,400. The lower, EUR 18,400, is her minimum 2026 preliminary tax. Her 2025 balance is 18,400 - 16,000 = EUR 2,400. She files the 2025 Form 11 and pays EUR 20,800 through ROS by 18 November 2026. If she files on paper, or pays outside ROS, both are due by 31 October 2026.

```oa-check
name: Sole trader, 2025 liability EUR 18,400, 2026 estimate EUR 21,000, no direct debit
inputs:
  income_tax_2025: 13000
  usc_2025: 2100
  prsi_2025: 3300
  estimate_2026: 21000
  prelim_paid_for_2025: 16000
steps:
  - liability_2025: income_tax_2025 + usc_2025 + prsi_2025
  - test_current: estimate_2026 * 90 / 100
  - test_preceding: liability_2025
  - minimum_prelim_2026: min(test_current, test_preceding)
  - balance_2025: liability_2025 - prelim_paid_for_2025
  - pay_by_deadline: minimum_prelim_2026 + balance_2025
expected:
  liability_2025: 18400
  test_current: 18900
  minimum_prelim_2026: 18400
  balance_2025: 2400
  pay_by_deadline: 20800
```

### Example 2: direct debit payer who falls short, backdating and interest

Declan pays 2026 preliminary tax by direct debit: 10 debits of EUR 1,000 from January to October 2026, EUR 10,000 in all, each paid as scheduled, so all of it is paid by 31 October 2026. His final liabilities are EUR 12,000 for 2024, EUR 30,000 for 2025 and EUR 15,000 for 2026. Because he pays by direct debit and his 2024 liability was not nil, three tests apply: 90% of 2026 is EUR 13,500; 100% of 2025 is EUR 30,000; 105% of 2024 is EUR 12,600. The lowest is EUR 12,600. He paid EUR 10,000, which is EUR 2,600 short. So all of his 2026 liability is treated as due on 31 October 2026 (s.959AO(3)(b)). All his debits were paid by 31 October 2026, so the unpaid part from that date is 15,000 - 10,000 = EUR 5,000. He pays it with his 2026 Form 11 on 31 October 2027, 365 days later. Interest is 5,000 x 0.0219% x 365 = EUR 399.68. Had his debits totalled EUR 12,600 or more, the EUR 5,000 or less balance would have been due on 31 October 2027 with no interest.

```oa-check
name: Direct debit payer, EUR 10,000 paid against a 105% test of EUR 12,600, balance paid 365 days after 31 October 2026
inputs:
  liability_2024: 12000
  liability_2025: 30000
  liability_2026: 15000
  monthly_debit: 1000
  debits: 10
  days_late: 365
steps:
  - paid: monthly_debit * debits
  - test_current: liability_2026 * 90 / 100
  - test_preceding: liability_2025
  - test_pre_preceding: liability_2024 * 105 / 100
  - minimum_prelim: min(test_current, test_preceding, test_pre_preceding)
  - shortfall: minimum_prelim - paid
  - unpaid_from_31_oct_2026: liability_2026 - paid
  - interest: round(unpaid_from_31_oct_2026 * 0.0219 / 100 * days_late, 2)
expected:
  paid: 10000
  test_current: 13500
  test_pre_preceding: 12600
  minimum_prelim: 12600
  shortfall: 2600
  unpaid_from_31_oct_2026: 5000
  interest: 399.68
```

## Ask the client first

1. Is this your first year in self-assessment, or were you a chargeable person for 2025 (and 2024)?
2. What were your final liabilities (income tax, USC and PRSI together) for 2025 and 2024, and was 2024 nil?
3. Do you pay preliminary tax by direct debit, and has every scheduled debit in 2026 been paid?
4. Do you expect 2026 income to be well below 2025? (Only then is the 90% test worth the estimate risk.)
5. Will you both file the 2025 Form 11 and pay through ROS? If either is not on ROS, the date is 31 October 2026.
6. Were you jointly assessed in any of the three years, or did you claim film relief or EII relief in 2024 or 2025?

## Sources

| Source | URL | Read on |
|---|---|---|
| Finance Act 2012 (No. 9 of 2012), s.129 and Sch. 4 Part 1: inserts TCA Part 41A, including s.959A, ss.959AM to 959AQ, s.959AU, s.959AV; applies from tax year 2013 (s.129(3), (4)) | https://www.irishstatutebook.ie/eli/2012/act/9/enacted/en/print | 2026-10-24 |
| Finance Act 2025 (No. 18 of 2025), s.100: amends s.959AP (deletes subsections (2) to (4)); passed 23 December 2025 | https://www.irishstatutebook.ie/eli/2025/act/18/section/100/enacted/en/html | 2026-10-24 |
| Finance Act 2025, s.101: inserts s.959AU(3) | https://www.irishstatutebook.ie/eli/2025/act/18/section/101/enacted/en/html | 2026-10-24 |
| Finance Act 2025, s.107: short title, construction and commencement | https://www.irishstatutebook.ie/eli/2025/act/18/section/107/enacted/en/html | 2026-10-24 |
| Revenue, Notes for Guidance, TCA 1997 Part 41A, Finance Act 2025 edition (December 2025): ss.959AM to 959AV | https://www.revenue.ie/en/tax-professionals/documents/notes-for-guidance/tca/part41a.pdf | 2026-10-24 |
| Revenue, Notes for Guidance, TCA 1997 Part 47, Finance Act 2025 edition: s.1080 interest table, s.1084 surcharge | https://www.revenue.ie/en/tax-professionals/documents/notes-for-guidance/tca/part47.pdf | 2026-10-24 |
| Revenue, Notes for Guidance, TCA 1997 Part 18D: s.531AS (USC paid as income tax by chargeable persons) | https://www.revenue.ie/en/tax-professionals/documents/notes-for-guidance/tca/part18d.pdf | 2026-10-24 |
| Revenue, Tax and Duty Manual Part 41-00-28, A Guide to Self-Assessment (updated August 2026) | https://www.revenue.ie/en/tax-professionals/tdm/income-tax-capital-gains-tax-corporation-tax/part-41/41-00-28.pdf | 2026-10-24 |
| Revenue, Preliminary Income Tax Direct Debit Guidelines (updated October 2025) | https://www.revenue.ie/en/tax-professionals/tdm/collection/direct-debit/preliminary-income-tax-direct-debit-guidelines.pdf | 2026-10-24 |
| Revenue, Guidelines for charging interest on late payment (updated May 2025) | https://www.revenue.ie/en/tax-professionals/tdm/collection/debt-management/guidelines-for-charging-interest-on-late-payment.pdf | 2026-10-24 |
| Revenue, what is preliminary tax? (published 15 October 2026) | https://www.revenue.ie/en/self-assessment-and-self-employment/guide-to-self-assessment/preliminary-tax.aspx | 2026-10-24 |
| Revenue, preliminary Income Tax direct debit (published 19 March 2026) | https://www.revenue.ie/en/starting-a-business/paying-your-tax/monthly-direct-debit/preliminary-income-tax.aspx | 2026-10-24 |
| Revenue, eBrief No. 034/26, Pay and File extension date 2026 | https://www.revenue.ie/en/tax-professionals/ebrief/2026/no-0342026.aspx | 2026-10-24 |
| Revenue, pay and file system | https://www.revenue.ie/en/self-assessment-and-self-employment/guide-to-self-assessment/pay-file-system.aspx | 2026-10-24 |
| Revenue, who should register for income tax self-assessment? | https://www.revenue.ie/en/self-assessment-and-self-employment/guide-to-self-assessment/register-it-self-assessment.aspx | 2026-10-24 |
| Social Welfare Consolidation Act 2005, revised, s.23(4) (Class S paid with income tax) | https://revisedacts.lawreform.ie/eli/2005/act/26/revised/en/html | 2026-10-24 |
| DSP, PRSI Class S rates | https://www.gov.ie/en/department-of-social-protection/publications/prsi-class-s-rates/ | 2026-10-24 |

Not yet confirmed: (1) whether the 3 and 8 instalment minimums still apply in 2026 as a Collector-General condition under s.959AP(1)(b) after Finance Act 2025 s.100 removed them from the law (TDM 41-00-28, August 2026, still prints them; the October 2025 direct debit guidelines do not); (2) the exact commencement of Finance Act 2025 s.100 (Part 6 has no date of its own in s.107; taken as the date of passing, 23 December 2025); (3) amendments to ss.959AN to 959AP between Finance Act 2013 and Finance Act 2024, not read one by one (Revenue's Finance Act 2025 Notes for Guidance agree with the text used here); (4) the text of s.579(4)(b) on non-residents, not read; (5) whether s.1080 interest also runs on the late return surcharge; (6) the legal basis of the 10% LPT surcharge on the income tax liability (Revenue page only); (7) the S.I. for Budget 2027 or a Finance Bill 2026 change to preliminary tax, not read; (8) a minimum below which no preliminary tax is needed: none found in the law, so none is given. (9) where a direct debit payer fails every test, whether the s.959AP(5) deemed date of 31 October also sets the s.1080 interest start for debits actually collected in November and December (s.959AP(5) is stated to be for the purposes of s.959AO only); Example 2 avoids the point by ending the debits in October.

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
