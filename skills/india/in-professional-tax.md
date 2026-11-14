---
name: in-professional-tax
description: >
  Use this skill whenever asked about Indian professional tax (profession tax) for
  FY 2026-27. Trigger on phrases like professional tax India, profession tax, state
  professional tax, Telangana professional tax, Maharashtra or Karnataka professional
  tax, PT registration, PT enrolment, PT return, Form V, profession tax deduction from
  salary, section 19 deduction, or any question about profession tax rates,
  registration, payment or income tax treatment in India. It gives the constitutional
  ceiling, the Telangana schedule bands most clients fall in, Telangana registration,
  payment, interest and penalties, and the income tax treatment under the Income-tax
  Act 2025 (deduction only for a person who opts out of the section 202 default
  regime). For other States it gives the steps to find their own schedule and no
  figures. Tier 2, not reviewed by an accountant.
version: "2.0"
jurisdiction: IN
tax_year: 2026
tax_year_notes: "FY 2026-27 (tax year 2026-27 under the Income-tax Act 2025; Telangana profession tax year 1 April 2026 to 31 March 2027)"
last_updated: 2026-11-14
category: international
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
tier: 2
domain: income-tax
type: computation
---

# India Professional Tax (Profession Tax), FY 2026-27

> **General reference only.** This skill is general tax reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts. Do not rely on it to file, pay or take a tax position without review by a qualified professional (such as a CA or CMA) in India. Label every computation as an estimate.

Tax year: FY 2026-27, 1 April 2026 to 31 March 2027. For income tax this is tax year 2026-27 under the Income-tax Act 2025, which replaced the Income-tax Act 1961 from 1 April 2026. For Telangana profession tax it is the profession tax year ending 31 March 2027, because the Telangana Act defines a year as the twelve months ending on 31 March. Only Telangana's profession tax pages can be read on an official site, so schedules and dates are given for Telangana only. For every other State this skill tells you where to check and gives no figures.

## Who this applies to

- Salary and wage earners, professionals, directors, partners, contractors, traders and companies engaged in a profession, trade, calling or employment in a State that levies profession tax.
- Employers who must deduct profession tax from salary and pay it over.
- Anyone asking whether profession tax paid reduces income tax for FY 2026-27.

Profession tax is charged by a State under its own Act and schedule. In Telangana, section 4 of the 1987 Act levies the tax "for the benefit of the State" on every person engaged in a profession, trade, calling or employment in the State who falls in a class in the First Schedule, at the rate in that entry ([section 4](https://www.tgct.gov.in/tgportal/AllActs/APPT/APPTAct/04Levy.html)). Telangana's schedule and procedure bind only Telangana. Another State's rates, forms, dates and exemptions come from that State's own Act, so the State where the person is employed or works decides which schedule applies. Andhra Pradesh and Telangana have separate schedules: never apply the Telangana table to Andhra Pradesh.

Out of scope: figures for any State other than Telangana (see "Other States" below), disputes, assessments and appeals.

### Conservative defaults

| Ambiguity | Default |
| --- | --- |
| Unknown State of employment or practice | Do not compute. Confirm the State first |
| State other than Telangana | Do not compute. Send the client to that State's own schedule (see "Other States") |
| Unknown monthly salary or wages | Do not compute. Get the monthly figure as defined in the State's Act |
| Unknown whether the employer deducts | In Telangana the employer must deduct and is liable even if it does not (section 5). Check payslips |
| Unknown income tax regime | Assume the default regime under section 202(1) of the 2025 Act, where the salary deduction for profession tax (section 19(1), Table serial 1) is not allowed, until the client confirms an opt-out |

## Rates, bands and thresholds

Telangana First Schedule "as amended upto date", as printed on the Telangana Commercial Taxes Department site, read 14 November 2026. Salary bands are by MONTHLY salary or wages. "PM" means per month, "PA" per year. Band edges: "up to" includes the edge, "from ... to" includes both ends, "above" means strictly more than.

| Item | Amount (INR) | Condition | Source |
| --- | --- | --- | --- |
| Constitutional maximum profession tax, per year | 2,500 | Yearly, not monthly. The department page says the Constitution sets this maximum; it does not quote the article | https://www.tgct.gov.in/tgportal/AllActs/APPT/APPTAct.aspx |
| Entry 1, salary or wage earner, monthly salary or wages up to 15,000 | Nil | Monthly band | https://www.tgct.gov.in/tgportal/AllActs/APPT/APPTSchedule.aspx |
| Entry 1, monthly salary or wages from 15,001 to 20,000 | 150 PM | Monthly band | https://www.tgct.gov.in/tgportal/AllActs/APPT/APPTSchedule.aspx |
| Entry 1, monthly salary or wages above 20,000 | 200 PM | Monthly band; no February top-up is printed | https://www.tgct.gov.in/tgportal/AllActs/APPT/APPTSchedule.aspx |
| Entry 2, listed professionals (legal practitioners, chartered accountants, tax consultants, engineers, architects, doctors, journalists, agents and others in the entry), standing up to 5 years | Nil | Standing in the profession | https://www.tgct.gov.in/tgportal/AllActs/APPT/APPTSchedule.aspx |
| Entry 2, standing more than 5 years | 2,500 PA | Standing in the profession | https://www.tgct.gov.in/tgportal/AllActs/APPT/APPTSchedule.aspx |
| Entries 4 (contractors) and 8 (registered dealers, shopkeeper employers), annual turnover below 10 lakh | Nil | Annual turnover | https://www.tgct.gov.in/tgportal/AllActs/APPT/APPTSchedule.aspx |
| Entries 4 and 8, annual turnover from 10 lakh to 50 lakh | 1,250 PA | Annual turnover | https://www.tgct.gov.in/tgportal/AllActs/APPT/APPTSchedule.aspx |
| Entries 4 and 8, annual turnover above 50 lakh | 2,500 PA | Annual turnover | https://www.tgct.gov.in/tgportal/AllActs/APPT/APPTSchedule.aspx |
| Entry 5, director drawing remuneration from a company (not a Government nominee) | 2,500 PA | Per director | https://www.tgct.gov.in/tgportal/AllActs/APPT/APPTSchedule.aspx |
| Entry 20, company not a dealer under the VAT Act, in a profession, trade or calling, turnover 10 lakh and above | 2,500 PA | Turnover | https://www.tgct.gov.in/tgportal/AllActs/APPT/APPTSchedule.aspx |
| Entry 21, each partner of a firm drawing remuneration from the firm | 1,250 PA | Per partner | https://www.tgct.gov.in/tgportal/AllActs/APPT/APPTSchedule.aspx |
| Entry 39, exempt classes include physically handicapped persons with this degree of disability or more | 40% | Exempt | https://www.tgct.gov.in/tgportal/AllActs/APPT/APPTSchedule.aspx |
| Entry 40, any other person with annual income more than 1,80,000 (unless exempt under section 31 or entry 39) | 2,500 PA | Annual income over 1,80,000 | https://www.tgct.gov.in/tgportal/AllActs/APPT/APPTSchedule.aspx |
| Interest on unpaid tax (employer or enrolled person) | 2 rupees per 100 rupees or part, per month or part | From the due date | https://www.tgct.gov.in/tgportal/AllActs/APPT/APPTAct/11Consequences.html |
| Penalty, tax not paid by the date in a notice of demand without reasonable cause | 25% to 50% of the tax due | On top of interest | https://www.tgct.gov.in/tgportal/AllActs/APPT/APPTAct/12Penalty.html |
| Penalty, wilful late registration (employer) | 10 to 20 rupees a day | Each day of delay | https://www.tgct.gov.in/tgportal/AllActs/APPT/APPTAct/06Registration.html |
| Penalty, wilful late enrolment (others) | Up to 5 rupees a day | Each day of delay | https://www.tgct.gov.in/tgportal/AllActs/APPT/APPTAct/06Registration.html |
| Penalty, deliberately false information in the application | 100 to 1,000 rupees | Per application | https://www.tgct.gov.in/tgportal/AllActs/APPT/APPTAct/06Registration.html |
| Penalty, return late without reasonable cause | 5 to 100 rupees a day | Each day of delay | https://www.tgct.gov.in/tgportal/AllActs/APPT/APPTAct/07Returns.html |
| Penalty, wilful failure to keep books as directed | Up to 5 rupees a day | Employer | https://www.tgct.gov.in/tgportal/AllActs/APPT/APPTAct/17Accounts.html |
| Income tax: salary deduction for profession tax paid, Income-tax Act 2025 s 19(1) Table Sl. No. 1 | Entire amount paid | Only for a person who opted out of s 202(1) under s 202(4); nil on the default regime (s 202(2)) | https://egazette.gov.in/WriteReadData/2025/265620.pdf |

### Rules that go with the table

- Salary means monthly "salary or wages" as defined in section 2: pay, wages, dearness allowance and all other remuneration received on a regular basis, in cash or kind, including perquisites and profits in lieu of salary, but NOT bonus or gratuity ([section 2](https://www.tgct.gov.in/tgportal/AllActs/APPT/APPTAct/02Definitions.html)).
- A person who earns wages on a casual basis is not a "person" under section 2 and is not charged. Every branch of a firm, company, corporation or other corporate body, society, club or association is deemed a separate person (section 2, Explanation).
- The salary entry prints a monthly amount only and no different amount for February. Do not add a February top-up for Telangana.
- The schedule has 40 entries. Entries 3, 6, 7, 9 to 19 and 22 to 38 cover other trades (stock exchange members, film industry, factories, hospitals, hotels, banks, transport, call centres, landlords of commercial premises and others), mostly at the entry 2 or entry 4 amounts. Read the client's entry on the schedule page itself.
- Entry 39 also exempts agriculturists, persons performing religious duties, listed skilled persons (goldsmith, blacksmith, potter, basket maker, washerman, barber, cobbler, tailor, carpenter, mason, plumber, book binder, toddy tapper, electrician) and dry cleaners. Section 31 lets the Government exempt or reduce the tax for a class by notification ([section 31](https://www.tgct.gov.in/tgportal/AllActs/APPT/APPTAct/31Power.html)); notifications are on the department's PT "GO's & Notifications" page.
- The schedule still uses the old Andhra Pradesh names (APVAT Act 2005, A.P. Shops and Establishment Act, Companies Act 1956). That is how the page prints it.

### Other States (Maharashtra, Karnataka, West Bengal, Andhra Pradesh, Tamil Nadu, Gujarat, Madhya Pradesh and the rest)

No official page read for this skill prints these States' schedules, so no slabs, amounts, due dates or forms are given. Earlier versions carried slabs for seven States; none could be proven and some contradicted each other. For each such State:

1. Find that State's own profession tax Act and the schedule "as amended" on the website of the department the Act names as assessing authority.
2. Read the entry for the client's class (salary, profession, trade) and whether bands are monthly, half-yearly or yearly.
3. Read the State's registration, enrolment, payment and return dates from that Act and its rules.
4. Check whether the State has notified any exemption for the client's class.

Whether a State or Union Territory charges profession tax at all is a matter of its own law. This skill does not list which States levy it, because no allowed page proves either list. Ask the State's tax department and record its answer.

## The base

### Salary and wage earners (Telangana)

Take the monthly salary or wages as defined in section 2 (excluding bonus and gratuity), read the entry 1 band, and multiply the monthly amount by the months employed in Telangana.

### Self-employed and others (Telangana)

Find the entry for the class (entry 2 professional, entry 4 contractor, entry 5 director, entry 21 partner, entry 40 residual) and apply the yearly amount. A professional named in entry 2 pays nothing for the first 5 years of standing. A person in no specific entry falls in entry 40 only if annual income is more than 1,80,000.

### Income tax treatment (Income-tax Act 2025)

The section number changed with the new Act. For tax year 2026-27 the salary deduction is in section 19(1), Table serial 1: "Sum paid by the assessee as a tax on employment as per article 276(2) of the Constitution, leviable by or under any law", amount of deduction "Entire amount" ([Income-tax Act 2025](https://egazette.gov.in/WriteReadData/2025/265620.pdf)). The Finance Act 2026 does not amend that serial.

Section 202(1) sets the default rates for individuals, HUFs, associations of persons (other than co-operative societies), bodies of individuals and artificial juridical persons, unless the person exercises the option in section 202(4). Under section 202(2)(a)(iv), total income on those rates is computed without any exemption or deduction under section 19(1) (Table: Sl. No. 1). So:

- On the default regime, profession tax paid is NOT deducted from salary. The standard deduction does not "cover" it; it is simply not allowed.
- Only a person who has opted out of section 202(1) under section 202(4) deducts profession tax paid from salary.
- The standard deduction is a separate serial (Table serial 2) with its own amounts for each regime: see `india-income-tax`.

Business or profession income: a person who pays profession tax as an enrolled person is not claiming a salary deduction. Section 37 of the 2025 Act allows a "tax, duty, cess, surcharge or fee, by whatever named called, levied under any law in force" that is otherwise allowable only in the tax year in which it is actually paid. Whether the client's own profession tax is otherwise allowable under the general rule in section 34 (expenditure laid out wholly and exclusively for the business or profession) is a question for the accountant. Never claim the same payment both as a salary deduction and as a business expense.

## Deadlines and filing

Everything here is Telangana law. For any other State, read that State's Act.

### Employer obligations

| Obligation | Telangana rule |
| --- | --- |
| Deduct | The employer deducts the tax from salary or wages before paying, and is liable to pay it "irrespective of whether such deduction has been made or not" ([section 5](https://www.tgct.gov.in/tgportal/AllActs/APPT/APPTAct/05Employer.html)) |
| Register | Every employer liable under section 5 (other than a State or Central Government officer) obtains a certificate of registration, Form I ([section 6](https://www.tgct.gov.in/tgportal/AllActs/APPT/APPTAct/06Registration.html)) |
| Pay | By treasury challan in quadruplicate; the duplicate goes to the assessing authority with the return (rule 13 of the [Telangana PT Rules](https://www.tgct.gov.in/tgportal/AllActs/APPT/APPTRules.aspx)) |
| Return | Form V, for the periods and by the dates prescribed, showing salaries and wages paid and tax deducted, with the challan proving full payment. A return without proof of payment is not "duly submitted" ([section 7](https://www.tgct.gov.in/tgportal/AllActs/APPT/APPTAct/07Returns.html); rule 12) |
| Employee with several employers, or in a higher entry | If the employee works for more than one employer, or also falls in another entry with a higher rate, and gives each employer a certificate (Form III or IV) that he will enrol and pay himself, the employers do not deduct and are not liable for him (section 5, second proviso; rule 10) |
| Books | The assessing authority may direct an employer how to keep books ([section 17](https://www.tgct.gov.in/tgportal/AllActs/APPT/APPTAct/17Accounts.html)); every employer keeps a register of salary paid and tax deducted for each employee (rule 20) |

The online Rules do not print the return period or the payment due date for a private employer. Rule 15 sets a monthly deduction duty and a 30 April statement only for Government drawing and disbursing officers. Confirm a private employer's period and due date with the Commercial Taxes Department.

### Self-employed and professional obligations

| Obligation | Telangana rule |
| --- | --- |
| Enrol | Every assessee other than a salary or wage earner whose employer pays for him obtains a certificate of enrolment, Form II (section 6) |
| Amount | The enrolment certificate states the tax payable under the First Schedule and the date to pay it, and serves as the notice of demand (section 6) |
| Pay | Before 30 June, if enrolled before the year starts or on or before 31 May of the year; within one month of enrolment if enrolled after 31 May ([section 10](https://www.tgct.gov.in/tgportal/AllActs/APPT/APPTAct/10Payment.html)) |
| How | Treasury challan in quadruplicate; the duplicate goes to the assessing authority (rule 14) |

Insurance agents in entry 2 have tax deducted by the insurer from commission, remitted on the next working day (section 5-B). Licensed horse owners, trainers, book-makers and jockeys pay through the turf club (section 5-A).

### Filing summary

| Item | Telangana |
| --- | --- |
| Employer registration | Certificate of registration, Form I (section 6(1)) |
| Self-employed enrolment | Certificate of enrolment, Form II (section 6(2)) |
| Employer return | Form V with treasury challan (section 7, rule 12) |
| Employee opting to pay himself | Certificate to employer, Form III or IV (section 5, rule 10) |
| Refund of excess | Section 21, rule 29, Form XV |
| Proof for an income tax deduction | Evidence that the sum was paid as a tax on employment (the section 19(1) wording is "Sum paid") |

Earlier versions listed employer deposit and return dates for Maharashtra, Karnataka, West Bengal, Andhra Pradesh and Gujarat. None could be proven, so they stay out. Use each State's own Act and rules.

## Penalties and interest

The figures are in the rates table. How they apply in Telangana:

| Default | Consequence |
| --- | --- |
| Late application for registration or enrolment (wilful) | Per-day penalty, employer and other rates in the rates table (section 6) |
| Deliberately false information in the application | Penalty range in the rates table (section 6) |
| Return late without reasonable cause | Per-day penalty in the rates table (section 7) |
| Employer fails to deduct, or deducts and fails to pay | Deemed assessee in default, plus interest at the rates-table rate from the due date ([section 11](https://www.tgct.gov.in/tgportal/AllActs/APPT/APPTAct/11Consequences.html); rule 24) |
| Enrolled person fails to pay | Interest at the same rate (section 11(2)) |
| Tax not paid by the date in a notice of demand, without reasonable cause | Penalty of 25% to 50% of the tax due, on top of interest ([section 12](https://www.tgct.gov.in/tgportal/AllActs/APPT/APPTAct/12Penalty.html)) |
| Wilful failure to enrol | Best judgment assessment and a demand in Form XIV payable within fifteen days (rule 23) |

## Cross-border points

### Multiple employments

In Telangana, a person employed by more than one employer can give each employer a certificate (Form III or IV), enrol under section 6(2) and pay the tax himself; the employers then stop deducting (section 5, second proviso). If too much was paid anyway, section 21 requires the assessing authority to refund the excess, or set it off against another period's dues at the assessee's option ([section 21](https://www.tgct.gov.in/tgportal/AllActs/APPT/APPTAct/21Refund.html)). The assessing authority first applies the excess to any amount due under a section 8 notice (section 21, proviso).

### Multi-State employment

Telangana's Act charges people engaged in a profession, trade, calling or employment in Telangana (section 4); another State's Act sets its own reach. A person who moves State mid-year must check the second State's Act for its own registration and payment rules. This skill cannot say how a second State treats profession tax already paid to the first. For income tax, section 19(1), Table serial 1 refers to a tax on employment "leviable by or under any law".

### Directors

In Telangana, a director drawing remuneration from a company, other than a Government nominee, falls in entry 5. A director who is also a salaried employee may give the employer the section 5 certificate (Form III or IV) only where the rate under entry 5 is more than the rate under entry 1 for that salary (section 5, second proviso).

### Freelancers and gig workers

In Telangana, a self-employed person enrols under section 6(2) and pays under section 10. The entry 2 five-year rule and the entry 40 income limit decide whether anything is due.

### Exemptions

In Telangana: the entry 39 classes, professionals in entry 2 with up to 5 years' standing, salary earners in the nil band, and any class exempted by notification under section 31. The earlier list of exemptions in other States (parents of disabled children, armed forces, people over 65 in Maharashtra, textile badli workers) could not be proven and stays out. Check the other State's Act.

### Non-residents

Profession tax follows where the person works under section 4, not income tax residence. A non-resident working in Telangana falls in the schedule like anyone else.

## Two worked examples that recompute

### Example 1: Telangana employee on 25,000 a month, which regime gets the deduction

A Hyderabad employee earns 25,000 a month all year. That is above 20,000, so entry 1 charges 200 a month: 2,400 for the year. On the default regime (s 202(1)) the deduction is nil. If the employee opted out under s 202(4) and the top slab of 30% applies, the 2,400 reduces tax by 2,400 x 30% x 1.04 (4% cess) = 748.80. The choice of regime is made on the whole return (see `india-income-tax`); this deduction is one input to it.

```oa-check
name: Telangana entry 1, 25,000 a month, deduction value on opt-out at 30% plus cess
inputs:
  monthly_pt: 200
  months: 12
  slab_rate: 0.30
  cess: 0.04
steps:
  - annual_pt: monthly_pt * months
  - deduction_default: 0
  - deduction_optout: annual_pt
  - tax_saved_optout: deduction_optout * slab_rate * (1 + cess)
expected:
  annual_pt: 2400
  deduction_default: 0
  tax_saved_optout: 748.80
```

### Example 2: Chartered accountant with 7 years' standing pays late

A Telangana chartered accountant (entry 2, more than 5 years' standing, 2,500 a year) was enrolled before the year began, so the tax was due before 30 June 2026. He pays on 15 September 2026: two full months and part of a third, so 3 months count. Interest is 2 rupees per 100 or part per month or part: 2,500 is 25 hundreds, so 25 x 2 x 3 = 150. If the assessing authority finds no reasonable cause, the section 12 penalty is 25% to 50% of 2,500: 625 to 1,250.

```oa-check
name: Telangana entry 2 late payment, 3 months, interest and penalty range
inputs:
  tax: 2500
  months_or_part: 3
steps:
  - hundreds: ceil(tax / 100)
  - interest: hundreds * 2 * months_or_part
  - penalty_min: tax * 0.25
  - penalty_max: tax * 0.50
expected:
  interest: 150
  penalty_min: 625
  penalty_max: 1250
```

## Ask the client first

- In which State do you work or carry on your profession or business, and did that change during the year?
- Are you salaried, a professional, a director, a partner, a contractor or a trader, and how many years have you practised?
- What is your regular monthly pay, leaving out bonus and gratuity?
- Do you work for more than one employer, or do you also pay profession tax yourself under an enrolment certificate?
- For income tax, have you opted out of the default regime under section 202 for this tax year?
- Do you have payslips or challans showing the profession tax actually paid?

### When to refuse or refer

- Refuse to compute profession tax for any State other than Telangana from this skill. Give the "Other States" steps instead.
- Refer when a Telangana client may be covered by a section 31 notification, an exemption entry not clearly met, or two entries at once.
- Refer disputes, assessments, best judgment notices, appeals and penalty proceedings to an accountant.
- Refer the question whether a self-employed person's own profession tax is a business expense under section 34.
- Refer any case where profession tax was paid to two States in one year.

### Prohibitions

- NEVER compute profession tax without knowing the State of employment or practice.
- NEVER apply Telangana's schedule, or any remembered slab, to another State.
- NEVER state any State's slabs, due dates or exemptions that are not on an official page you have read.
- NEVER treat the constitutional ceiling as a monthly amount.
- NEVER add a February top-up to Telangana salary deductions.
- NEVER give the section 19(1), Table serial 1 salary deduction to a person on the default regime under section 202(1).
- NEVER claim the same profession tax both under section 19(1), Table serial 1 and as a business expense.
- NEVER assert that a State does or does not levy profession tax without its own law in hand.
- NEVER present a computation as final. Label it as an estimate.

## Sources

| Source | URL | Read on |
| --- | --- | --- |
| Read for the constitutional maximum of Rs 2,500 a year and the list of sections: Telangana Commercial Taxes Department, PT Act page | https://www.tgct.gov.in/tgportal/AllActs/APPT/APPTAct.aspx | 2026-11-14 |
| Read for entries 1, 2, 4, 5, 8, 20, 21, 39 and 40 of the First Schedule as amended | https://www.tgct.gov.in/tgportal/AllActs/APPT/APPTSchedule.aspx | 2026-11-14 |
| Read for section 2, definition of salary or wages and casual workers | https://www.tgct.gov.in/tgportal/AllActs/APPT/APPTAct/02Definitions.html | 2026-11-14 |
| Read for section 4, the levy | https://www.tgct.gov.in/tgportal/AllActs/APPT/APPTAct/04Levy.html | 2026-11-14 |
| Read for section 5, employer deduction and liability, second proviso | https://www.tgct.gov.in/tgportal/AllActs/APPT/APPTAct/05Employer.html | 2026-11-14 |
| Read for section 6, registration, enrolment and their penalties | https://www.tgct.gov.in/tgportal/AllActs/APPT/APPTAct/06Registration.html | 2026-11-14 |
| Read for section 7, returns and the late return penalty | https://www.tgct.gov.in/tgportal/AllActs/APPT/APPTAct/07Returns.html | 2026-11-14 |
| Read for section 10, payment dates for enrolled persons | https://www.tgct.gov.in/tgportal/AllActs/APPT/APPTAct/10Payment.html | 2026-11-14 |
| Read for section 11, interest at two rupees per hundred per month | https://www.tgct.gov.in/tgportal/AllActs/APPT/APPTAct/11Consequences.html | 2026-11-14 |
| Read for section 12, the 25% to 50% penalty | https://www.tgct.gov.in/tgportal/AllActs/APPT/APPTAct/12Penalty.html | 2026-11-14 |
| Read for section 17, books and the daily penalty | https://www.tgct.gov.in/tgportal/AllActs/APPT/APPTAct/17Accounts.html | 2026-11-14 |
| Read for section 21, refunds and set-off | https://www.tgct.gov.in/tgportal/AllActs/APPT/APPTAct/21Refund.html | 2026-11-14 |
| Read for section 31, power to exempt | https://www.tgct.gov.in/tgportal/AllActs/APPT/APPTAct/31Power.html | 2026-11-14 |
| Read for rules 10, 12, 13, 14, 15, 20, 23, 24 and 29 of the Telangana PT Rules | https://www.tgct.gov.in/tgportal/AllActs/APPT/APPTRules.aspx | 2026-11-14 |
| Read for Income-tax Act 2025 sections 19(1) Table Sl. Nos. 1 and 2, 34, 37 and 202 (Gazette, Act 30 of 2025) | https://egazette.gov.in/WriteReadData/2025/265620.pdf | 2026-11-14 |

Not yet confirmed: the return period and payment due date for a private Telangana employer (the online Rules print only the Government drawing officer duty); every other State's schedule, dates, forms and exemptions; which States and Union Territories levy profession tax at all; whether a Telangana section 31 notification after the schedule page's last amendment changes any entry.
