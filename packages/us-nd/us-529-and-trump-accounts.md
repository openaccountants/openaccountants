---
name: us-529-and-trump-accounts
description: US federal rules for 2026 on section 529 qualified tuition programs and on Trump accounts under section 530A. Covers qualified expenses after the One Big Beautiful Bill Act, including the USD 20,000 elementary and secondary cap, apprenticeship costs, the USD 10,000 lifetime student-loan limit, credentialing expenses, the taxable portion of a nonqualified distribution, and the 10 percent additional tax. Covers Trump account eligibility, the USD 5,000 annual contribution limit, the USD 1,000 pilot contribution, and the USD 2,500 employer exclusion. Trigger on "529 plan", "qualified tuition program", "529 distribution", "K-12 529", "529 to Roth", "Trump account", "Form 4547", "section 530A".
version: "1.0"
jurisdiction: US
category: federal
tax_year: 2026
last_updated: 2026-11-13
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
tier: 2
domain: income-tax
type: situation-rules
---

# Section 529 plans and Trump accounts, tax year 2026

> **Source-cited draft.** Built from IRS Topic 313, the IRS Trump Accounts pages, 26 U.S.C. 529 and 530, Public Law 119-21 sections 70204, 70413 and 70414, and Rev. Proc. 2025-32, read on 2026-11-13. No accountant has reviewed it. All outputs must be reviewed by a qualified tax professional before filing.

**Answer first.** A 2026 distribution from a 529 plan is tax-free to the extent it pays qualified education expenses. Elementary and secondary expenses from all of a beneficiary's 529 plans are capped at USD 20,000 for the year. Earnings above the qualified expenses are taxable, and that taxable part generally draws an extra 10 percent tax. A Trump account is a separate IRA for a child who will not turn 18 before the end of the year the account is set up. Before the year the child turns 18, contributions other than the exempt ones cannot exceed USD 5,000. The USD 1,000 pilot contribution does not count toward that USD 5,000.

## Scope and who this is for

In scope: a US person asking, for 2026, whether a 529 distribution is qualified, how much of the earnings are taxable, and whether a child can have a Trump account and how much can go in. Contributions to a 529 plan are not deductible for federal income tax.

Out of scope, and where it goes:

| Topic | Skill |
| --- | --- |
| The American opportunity credit and the lifetime learning credit, including expenses that cannot be used twice | `us-education-credits-8863` |
| A state's own deduction or credit for 529 contributions | that state's income tax skill |
| Coverdell education savings accounts, except the rule that the same expenses are not used twice | not this skill |
| The gift and estate tax return | `us-estate-gift-706-709` |

## Ask the client first

1. **Which account.** A 529 plan, a Trump account, or both. They are not the same account.
2. **For a 529 distribution:** Form 1099-Q boxes 1, 2 and 3, what the money paid, and whether those expenses were also used for an education credit.
3. **Whose school level.** College or other postsecondary study, a registered apprenticeship, a credential program, student-loan repayment, or kindergarten through grade 12.
4. **For a Trump account:** the child's date of birth, citizenship, and Social Security number, and who else will contribute this year (the parent, an employer, the USD 1,000 pilot).
5. **Other gifts** by the same donor to the same person in 2026, if the 529 contribution may exceed the annual exclusion.

## The method, step by step

### Rates, bands and thresholds

| Item | Amount | Who it applies to | Source |
| --- | --- | --- | --- |
| Elementary and secondary expenses from all 529 plans | USD 20,000 per beneficiary for the year | Distributions in a taxable year beginning after 31 December 2025. The wider K-12 list applies to distributions after 4 July 2025 | [Topic 313](https://www.irs.gov/taxtopics/tc313) |
| Student-loan repayments from a 529 plan | USD 10,000 lifetime per individual | Principal or interest on a qualified education loan of the beneficiary or the beneficiary's sibling. The interest is not also a student-loan interest deduction | [26 U.S.C. 529(c)(9)](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap1-subchapF-partVIII-sec529.htm) |
| 529-to-Roth IRA rollover, lifetime | USD 35,000 per beneficiary | The account must have been open 15 years. Only contributions, and their earnings, from more than 5 years before the rollover count. Direct trustee-to-trustee transfer | [26 U.S.C. 529(c)(3)(E)](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap1-subchapF-partVIII-sec529.htm) |
| Additional tax on taxable 529 earnings | 10 percent of the amount included in income | The section 530(d)(4) tax, applied by section 529(c)(6). Exceptions include death, disability, and a scholarship | [26 U.S.C. 530(d)(4)](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap1-subchapF-partVIII-sec530.htm) |
| Gift tax annual exclusion, 2026 | USD 19,000 | Per donee, per donor. A 529 donor may elect to spread a larger gift evenly over 5 years | [Rev. Proc. 2025-32](https://www.irs.gov/pub/irs-drop/rp-25-32.pdf) |
| Trump account contributions before the year the child turns 18 | USD 5,000 per calendar year | Does not include a qualified rollover, a qualified general contribution, or the section 6434 pilot contribution. Indexed after 2027 | [Public Law 119-21, section 530A(c)(2)](https://www.govinfo.gov/content/pkg/PLAW-119publ21/html/PLAW-119publ21.htm) |
| Trump account pilot contribution | USD 1,000, once | A US citizen born after 31 December 2024 and before 1 January 2029, with a Social Security number. The election is on Form 4547 | [IRS Trump Accounts](https://www.irs.gov/trumpaccounts) |
| Employer contribution excluded from the employee's income | USD 2,500 | Paid to a Trump account of the employee or the employee's dependent under a qualifying program. It still counts toward the USD 5,000 | [Public Law 119-21, section 128](https://www.govinfo.gov/content/pkg/PLAW-119publ21/html/PLAW-119publ21.htm) |
| Penalty on a distributed excess Trump contribution | 100 percent of the net income on the excess | The excess itself is not included in income. The penalty is on the earnings | [Public Law 119-21, section 530A(d)(5)](https://www.govinfo.gov/content/pkg/PLAW-119publ21/html/PLAW-119publ21.htm) |
| Eligible-investment fee cap, before the year the child turns 18 | 0.1 percent of the balance | A mutual fund or exchange-traded fund that tracks a qualified index and does not use leverage | [Public Law 119-21, section 530A(b)(3)](https://www.govinfo.gov/content/pkg/PLAW-119publ21/html/PLAW-119publ21.htm) |

### A 529 distribution

1. **Qualified expenses.** Tuition, fees, books, supplies, and equipment required to enroll at an eligible institution, plus room and board within the cost of attendance for a student who is at least half-time, and computers, software, and internet access used primarily by the beneficiary while enrolled. Also: a registered apprenticeship's fees, books, supplies, and equipment; up to USD 10,000 lifetime of student-loan principal and interest for the beneficiary or a sibling; and qualified postsecondary credentialing expenses for distributions after 4 July 2025. For kindergarten through grade 12, the list is tuition, curriculum and curricular materials, books and instructional materials, online materials, tutoring by a tutor who is not related to the student and who is a licensed teacher, has taught at an eligible institution, or is a subject-matter expert, specified test fees, dual-enrollment fees, and educational therapies. Those K-12 amounts, from all of the beneficiary's plans together, cannot exceed USD 20,000 in 2026. Source: [Topic 313](https://www.irs.gov/taxtopics/tc313) and [Public Law 119-21, sections 70413 and 70414](https://www.govinfo.gov/content/pkg/PLAW-119publ21/html/PLAW-119publ21.htm).
2. **Take out expenses used for a credit.** Qualified expenses are reduced by expenses that produced an American opportunity or lifetime learning credit. The credit rules are in `us-education-credits-8863`. Do not use the same dollar for both. Source: [26 U.S.C. 529(c)(3)(B)(v)](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap1-subchapF-partVIII-sec529.htm).
3. **Taxable earnings.** Form 1099-Q splits the distribution into earnings and basis. If qualified expenses are at least the distribution, none of the earnings are taxed. If expenses are lower, the taxable earnings are the earnings minus the earnings times (qualified expenses divided by the distribution). Source: [26 U.S.C. 529(c)(3)(B)](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap1-subchapF-partVIII-sec529.htm).
4. **The 10 percent additional tax** applies to the taxable earnings, unless an exception in section 530(d)(4) applies (death, disability, a scholarship, attendance at a listed US service academy, or the other exceptions in that paragraph).
5. **Rollovers.** A rollover within 60 days to another 529 plan for the same beneficiary, or to a family member, is not income. Only one rollover to another plan for the same beneficiary is allowed in a 12-month period. A refund of qualified expenses recontributed within 60 days is not income. A direct rollover to the beneficiary's Roth IRA is tax-free only inside the USD 35,000 lifetime cap, the 15-year and 5-year tests, and the beneficiary's own annual Roth contribution limit under section 408A(c)(2). A 529-to-ABLE rollover in the statute applies only before 1 January 2026, so it is not available for a 2026 distribution.
6. **Gifts.** A contribution is a gift. The 2026 annual exclusion is USD 19,000 per donee. If the donor gives more than that, the donor may elect to treat the 529 gifts as made evenly over the 5-year period that starts this year. Five times USD 19,000 is USD 95,000 from one donor to one beneficiary for that election. If the donor dies during the 5 years, the portion allocated to years after death is in the donor's estate. Source: [26 U.S.C. 529(c)(2)(B) and (c)(4)](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap1-subchapF-partVIII-sec529.htm).

### A Trump account

A Trump account is an IRA that is not a Roth IRA, with extra limits until the year the beneficiary turns 18. It is not a 529 plan. Qualified education expenses do not make a Trump account distribution tax-free. Source: [Public Law 119-21, section 530A](https://www.govinfo.gov/content/pkg/PLAW-119publ21/html/PLAW-119publ21.htm) and [IRS Trump Accounts](https://www.irs.gov/trumpaccounts).

1. **Who qualifies.** The child has a valid Social Security number and will not turn 18 before the end of the calendar year the account is established. The child does not need to qualify for the USD 1,000 to have an account.
2. **When money can go in.** The governing instrument cannot accept a contribution before the date 12 months after enactment. Public Law 119-21 is dated 4 July 2025, so that date is 4 July 2026. The IRS says the Treasury's automatic enrollment starts 1 October 2026. An account opened automatically still has to be claimed before it can be managed. Claiming does not require Form 4547. The USD 1,000 does require Form 4547, even if the account was opened automatically.
3. **The USD 1,000.** One election, for a US citizen born after 31 December 2024 and before 1 January 2029. It is paid into the Trump account. It does not count toward the USD 5,000. It is not part of the child's investment in the contract, so it is not recovered tax-free on a later distribution. Do not file Form 1040-X to fix Form 4547. Follow Notice CP318 if one arrives.
4. **The USD 5,000.** Count the parent's contributions and an employer's contribution. Do not count the pilot contribution, a qualified general contribution (a government or charity contribution paid out equally to a defined class of children), or a trustee-to-trustee rollover of the whole account to another Trump account for the same child. No deduction is allowed under section 219 for a contribution before the year the child turns 18. An employer's payment of up to USD 2,500 is excluded from the employee's income and still uses the USD 5,000 cap.
5. **No distribution** before 1 January of the year the child turns 18, except a full rollover to another Trump account, a full rollover to an ABLE account in the calendar year the child turns 17, a distribution of an excess contribution, or a distribution because the child has died.
6. **Investments** before that year are limited to a mutual fund or exchange-traded fund that tracks the S&P 500 or another broad US equity index (not an industry or sector index), does not use leverage, and charges no more than 0.1 percent.

### Boundary and exception table

| Situation | Result |
| --- | --- |
| K-12 costs above USD 20,000 | Only USD 20,000 is a qualified expense. The rest follows the taxable-earnings formula |
| Same expense used for an education credit | It is not a qualified 529 expense |
| Distribution within 60 days rolled to a family member's 529 | Not income. A second plan-to-plan rollover for the same beneficiary inside 12 months does not qualify |
| 529 account open fewer than 15 years | No Roth rollover |
| Child turns 18 during 2026 | Not eligible for a new Trump account for 2026. The contribution and distribution limits that apply before the year of the 18th birthday do not govern this year |
| Employer pays USD 2,500 and the parent also pays USD 5,000 | USD 2,500 is over the cap. The excess has to come out, with a 100 percent tax on its earnings |
| Pilot contribution | Does not use the USD 5,000, and is not basis |
| 529 distribution used for college | Not a Trump account question. Use the 529 steps |

## Worked cases

**Case 1, a decision: take a 529 distribution above the K-12 cap, or stop at the cap?** In 2026 a beneficiary in grade 8 has USD 20,000 of qualified K-12 expenses, which is the whole cap. The plan distributes USD 25,000. Form 1099-Q shows earnings of USD 5,000. Qualified expenses are USD 20,000, so the taxable earnings are USD 5,000 minus USD 5,000 times (20,000 / 25,000) = USD 1,000. The additional tax is 10 percent of USD 1,000 = USD 100. No scholarship or other exception applies.

If the plan distributes only USD 20,000, and the earnings on that smaller distribution are USD 4,000 (the same one-fifth ratio), qualified expenses cover the whole distribution. Taxable earnings are zero and the additional tax is zero. Stop at USD 20,000 unless the family has another qualified expense that can absorb the extra USD 5,000. The USD 100 is the cost of going over the cap on these facts, before the income tax on the USD 1,000. The income tax rate is not computed here.

```oa-check
name: K-12 distribution at the cap or over it (2026)
inputs:
  distribution_high: 25000
  earnings_high: 5000
  qualified: 20000
  distribution_cap: 20000
  earnings_cap: 4000
steps:
  - taxable_high: earnings_high - earnings_high * qualified / distribution_high
  - additional_tax_high: taxable_high * 0.10
  - taxable_cap: earnings_cap - earnings_cap * qualified / distribution_cap
  - additional_tax_cap: taxable_cap * 0.10
expected:
  taxable_high: 1000.00
  additional_tax_high: 100.00
  taxable_cap: 0.00
  additional_tax_cap: 0.00
```

**Case 2, a Trump account: parent and employer both want to fund it.** A child born in 2026 is a US citizen with a Social Security number. The parent elects the USD 1,000 pilot on Form 4547. That USD 1,000 does not count toward the USD 5,000. The parent also contributes USD 5,000, and the employer will contribute USD 2,500, which is excluded from the employee's income.

If both are paid, non-exempt contributions are USD 7,500. The excess is USD 2,500. That excess has to be distributed, and the earnings on it are taxed at 100 percent. If the parent instead contributes USD 2,500 and the employer contributes USD 2,500, non-exempt contributions are USD 5,000, the excess is zero, and the account also receives the USD 1,000 pilot. The amount in the account from these payments is USD 6,000. Use the employer USD 2,500 and cut the parent to USD 2,500. Do not pay in both full amounts.

```oa-check
name: Trump account, parent contribution cut so the employer fits
inputs:
  parent: 5000
  employer: 2500
  cap: 5000
  pilot: 1000
steps:
  - excess_if_both: parent + employer - cap
  - parent_if_capped: cap - employer
  - excess_if_capped: parent_if_capped + employer - cap
  - funded_if_capped: parent_if_capped + employer + pilot
expected:
  excess_if_both: 2500.00
  parent_if_capped: 2500.00
  excess_if_capped: 0.00
  funded_if_capped: 6000.00
```

## When to refuse or refer

| Code | Situation | Action |
| --- | --- | --- |
| R-529-CREDIT | The same tuition is also on Form 8863 | Allocate. Do not count it as a qualified 529 expense. Use `us-education-credits-8863` |
| R-529-ROTH | A Roth rollover, and the annual contribution room is not known | The cap is section 408A(c)(2) minus other IRA contributions. This skill does not state that dollar amount |
| R-529-STATE | A state tax deduction for the contribution | Use the state's skill. Federal law gives no deduction |
| R-530A-AGE | The child turns 18 in the year at issue | The under-18 contribution and investment rules do not apply. Ordinary IRA rules may. Refer |
| R-530A-BASIS | A distribution after the child turns 18, and basis must be split | The pilot, employer exclusion, and qualified general contributions are not basis. Build the basis record before computing the taxable part |
| R-529-ABLE | A 2026 rollover from a 529 plan to an ABLE account | The statute's 529-to-ABLE rollover ended before 1 January 2026 |

## Filing and payment

A 529 plan does not file a return for the owner. The program issues Form 1099-Q. Taxable earnings go on the distributee's Form 1040. The additional 10 percent tax is reported with the return on the form the instructions name for that additional tax. The 2026 form line was not confirmed here.

A Trump account election for the USD 1,000 is Form 4547, filed through the Trump Accounts app, the Trump Accounts website, or the IRS individual online account. Claiming an account the Treasury already opened is done in the app and does not use Form 4547. Do not amend Form 1040 to correct Form 4547. There is no income tax to pay when the allowed contribution goes in. A contribution before the year the child turns 18 is not deducted. The employer's USD 2,500 is left out of the employee's wages.

The penalty for a negligent claim that a child is eligible for the pilot is USD 500. The penalty for a fraudulent claim is USD 1,000. Source: [Public Law 119-21, section 6659](https://www.govinfo.gov/content/pkg/PLAW-119publ21/html/PLAW-119publ21.htm).

Help with a Trump account: 866-872-4547, or the Trump Accounts Help Center. IRS phone staff cannot correct the election or claim the account.

## Completion checklist

- 529 and Trump account not mixed.
- K-12 total from every plan for the beneficiary tested against USD 20,000.
- Education-credit expenses removed before the 529 exclusion.
- Taxable earnings use earnings times (1 minus qualified expenses over the distribution).
- 10 percent additional tax tested against the section 530(d)(4) exceptions.
- Trump contributions other than the pilot, a general contribution, and a full rollover tested against USD 5,000.
- Form 4547 used for the USD 1,000, and not amended on Form 1040-X.

## Sources

| Source | URL | Read on |
| --- | --- | --- |
| IRS Topic 313, Qualified tuition programs. Read for the K-12 list and the USD 20,000 cap, the USD 10,000 lifetime student-loan limit, the USD 35,000 Roth rollover conditions, and Form 1099-Q. | https://www.irs.gov/taxtopics/tc313 | 2026-11-13 |
| 26 U.S.C. 529 (govinfo, United States Code 2024). Read for the earnings formula in (c)(3), the 5-year gift election, the USD 35,000 Roth cap, the USD 10,000 loan cap, and the pre-2026 ABLE rollover. The K-12 dollar cap in this edition is still USD 10,000; Public Law 119-21 changed it. | https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap1-subchapF-partVIII-sec529.htm | 2026-11-13 |
| 26 U.S.C. 530(d)(4) (govinfo, United States Code 2024). Read for the 10 percent additional tax and its exceptions. Section 529(c)(6) applies this tax to a 529 plan. | https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap1-subchapF-partVIII-sec530.htm | 2026-11-13 |
| Public Law 119-21. Read for section 70413 (K-12 list and the USD 20,000 cap), section 70414 (credentialing expenses), and section 70204 (section 530A, the USD 5,000, the USD 1,000 pilot, section 128's USD 2,500, and section 6659). | https://www.govinfo.gov/content/pkg/PLAW-119publ21/html/PLAW-119publ21.htm | 2026-11-13 |
| IRS Trump Accounts page. Read for eligibility, automatic enrollment from 1 October 2026, Form 4547 for the USD 1,000, and the phone line. | https://www.irs.gov/trumpaccounts | 2026-11-13 |
| IRS Trump Accounts frequently asked questions. Read for claiming an account, Form 4547, Notice CP318, and not using Form 1040-X. | https://www.irs.gov/faqs/trump-accounts-frequently-asked-questions | 2026-11-13 |
| Rev. Proc. 2025-32. Read for the 2026 gift tax annual exclusion of USD 19,000. | https://www.irs.gov/pub/irs-drop/rp-25-32.pdf | 2026-11-13 |

Not yet confirmed: the 2026 dollar amount of the section 408A(c)(2) annual cap on a 529-to-Roth rollover (this skill does not treat the section 219 IRA limit as that cap); the 2026 Form 1040 line for taxable 529 earnings and for the 10 percent additional tax; the due date of the 2027 Form 1099-Q; any 2026 index of the USD 5,000 or USD 2,500 (the statute first indexes them after 2027).
