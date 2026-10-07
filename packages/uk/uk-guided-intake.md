---
name: uk-freelance-intake
description: ALWAYS USE THIS SKILL when a user asks for help preparing their UK tax returns AND mentions freelancing, self-employment, sole trading, contracting, or side hustle income. Trigger on phrases like "help me do my UK taxes", "prepare my self-assessment", "I'm self-employed in the UK", "I'm a sole trader", "do my SA100", "prepare my tax return", or any similar phrasing where the user is a UK-resident self-employed individual needing tax return preparation. This is the REQUIRED entry point for the UK self-employed tax workflow -- every other skill in the stack (uk-vat-return, uk-self-employment-sa103, uk-income-tax-sa100, uk-national-insurance, uk-student-loan-repayment, uk-payments-on-account, uk-return-assembly) depends on this skill running first to produce a structured intake package. Uses upload-first workflow -- the user dumps all their documents and the skill infers as much as possible before asking questions. Uses ask_user_input_v0 for structured questions instead of one-at-a-time prose. Built for speed. UK full-year residents only; sole traders.
version: 0.1
jurisdiction: GB
tax_year: 2026
last_updated: 2026-09-27
authored_by: Michael Cutajar and the OpenAccountants team
review_status: pending_review
trust_label: Built by Michael Cutajar and the OpenAccountants team
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# UK freelancer tax intake: the questions to ask and where each answer goes (2026/27)

## Scope

This is the first Guide to run when someone in the UK says they freelance, work for themselves, contract, sell on the side or have "a bit of self-employed income". It does not compute tax. It asks the questions that decide which rules apply, records the answers, and sends each answer to the specialist Guide that holds the detail:

- **uk-income-tax-sa100**: whether a return is needed, Income Tax, payments on account, deadlines and penalties.
- **uk-national-insurance**: Class 2 and Class 4 for the self-employed, and voluntary contributions.
- **uk-vat-return**: VAT registration, schemes and returns.
- **uk-bookkeeping**: records, cash basis or traditional accounting, simplified expenses, and Making Tax Digital for Income Tax (MTD) record-keeping.
- **uk-statutory-residence-test**: whether the person is UK resident for the year.
- **uk-non-dom**: foreign income and gains, including the 4-year FIG regime that replaced the remittance basis.
- **uk-capital-gains-sa108**: disposals of shares, crypto, property and business assets.
- **uk-payroll**: anyone who employs staff, or whose own company runs a payroll.
- **uk-rental-sa105**: UK property income.

**Tax year.** The primary year is 2026/27, which runs from 6 April 2026 to 5 April 2027. HMRC writes it "2026 to 2027". Returns being filed now are for 2025/26 (6 April 2025 to 5 April 2026); a dated section near the end covers them.

**Who this is for.** Individuals who work for themselves as sole traders, or who contract through an umbrella company or their own limited company, and who want to know what they must do about tax. The intake records residence, employment status and whether an activity is a trade. It does not decide any of them. Those are questions of fact that HMRC, and in the end a tribunal, can decide differently.

**What the figures here are for.** The few amounts in this Guide are the switches that decide a route: the £1,000 trading allowance and return trigger, the 5 October registration date, the £90,000 VAT threshold, the MTD thresholds, the Class 2 and Class 4 limits, and the payments on account tests. Each one is stated as the specialist Guide states it, from the same gov.uk page. For anything beyond the switch, go to the specialist Guide. ([who must send a return](https://www.gov.uk/self-assessment-tax-returns/who-must-send-a-tax-return))

## Ask the client first

Ask these in order. Several are blocking: the answer to one changes which of the rest matter. Where the person uploads documents (bank statements, invoices, last year's SA302 tax calculation, P60s, HMRC letters), read them first and ask only about the gaps.

**A. The year and where they live**

- Which tax year is this about? The UK tax year runs 6 April to 5 April.
- Were you in the UK for the whole of that year? Did you arrive, leave, or spend long periods abroad?
- Do you have income or gains from outside the UK? Did you move to the UK in the last few years?
- Do you live in Scotland? Scottish taxpayers pay different Income Tax rates on earnings.

**B. How the work is set up**

- Do you invoice clients in your own name, through your own limited company, through an umbrella company, or are you paid through an agency's payroll?
- Do you share profits with anyone as a partner?
- For each client: who is it, is it in the public sector, and roughly how big is it? Has any of them given you a "status determination statement"?
- Do you also have a job where tax is taken off through PAYE?

**C. How much, and since when**

- When did you start working for yourself? Have you told HMRC, and do you have a Unique Taxpayer Reference (UTR)?
- What were your total takings, before expenses, from self-employment in the year? And from UK property, if any?
- What were your total taxable sales over the last 12 months, month by month? Do you expect any single 30-day period ahead to bring in more than £90,000 on its own? ([register for VAT](https://www.gov.uk/register-for-vat))
- Are you VAT registered? From what date, and on which scheme?

**D. Other income and disposals**

- Did you have rental income, dividends, savings interest, foreign income, or a disposal of shares, crypto, a second property or business assets?
- Are you repaying a student or postgraduate loan? Does anyone in your household get Child Benefit?

**E. Records and past returns**

- What records do you keep: accounting software, spreadsheets, a separate business bank account?
- What did last year's SA302 say you owed, and how much of it was already paid through PAYE or taken off at source? Did you make payments on account on 31 January and 31 July?
- Has HMRC written to you about Making Tax Digital for Income Tax?

**F. People**

- Do you employ anyone, or pay anyone through a payroll?

## The method, step by step

Work through the steps in order. Each step ends with a route. Record every answer and every doubt; do not settle a doubt by assuming.

1. **Fix the tax year.** Everything below is tested year by year, 6 April to 5 April. The MTD test looks at an earlier year than the one it starts in, and payments on account look at the previous year's bill. Write down which year each document belongs to.

2. **Residence.** A person is UK resident only if both apply: they meet one or more of the automatic UK tests or the sufficient ties test, and they do not meet any of the automatic overseas tests ([tax on foreign income: residence](https://www.gov.uk/tax-foreign-income/residence)).

- Whole year in the UK, no foreign income: continue.
- Arrived, left, or long periods abroad: route to **uk-statutory-residence-test** before anything else. A split year and non-resident returns need an adviser.
- Foreign income or gains, or moved to the UK recently: route to **uk-non-dom**. Residents normally pay UK tax on all their income, whether it is from the UK or abroad ([residence](https://www.gov.uk/tax-foreign-income/residence)); the 4-year FIG regime for qualifying new residents, and what happened to the remittance basis, are in that Guide.
- Lives in Scotland: note it for **uk-income-tax-sa100**, which refers Scottish rates.

3. **How the work is set up.** This decides which tax system the income sits in.

- **Sole trader** (invoices in own name, no company): self-employment income on the Self Assessment return. Continue to step 4.
- **Also employed**: someone can be employed and self-employed at the same time, for example working for an employer during the day and running their own business in the evenings ([employment status](https://www.gov.uk/employment-status/selfemployed-contractor)). The job stays in PAYE; the business goes on the return.
- **Partner in a partnership**: a partner must file a personal return ([who must send a return](https://www.gov.uk/self-assessment-tax-returns/who-must-send-a-tax-return)), and the trading allowance does not apply to partnership income. The partnership return itself is out of scope here; refer.
- **Own limited company (personal service company)** or **umbrella company**: go to the IR35 section below. The company's own tax (Corporation Tax, accounts, payroll) is not a sole trader matter; route payroll to **uk-payroll** and refer the company accounts.
- **Paid through an agency's payroll**: that is employment income taxed through PAYE, not self-employment. Record it and route to **uk-income-tax-sa100** if a return is needed for another reason.

4. **Is the activity a trade, and is the person self-employed?**

- Self-employed or not is a question about the work, not the job title. A person is probably self-employed if most of these are true: they put in bids or give quotes to get work; they are not under direct supervision; they submit invoices; they pay their own tax and National Insurance; they get no holiday or sick pay; and their contract uses terms like "self-employed", "consultant" or "independent contractor" ([employment status](https://www.gov.uk/employment-status/selfemployed-contractor)). If the facts point the other way (one client, set hours, supervised, equipment supplied, holiday pay), record it and flag it. Do not reclassify the income yourself.
- Trade or hobby: where selling may not be a trade, HMRC looks at the badges of trade, such as profit-seeking motive, number of transactions, nature of the asset and how the sale was carried out, and decides on the overall impression ([BIM20205](https://www.gov.uk/hmrc-internal-manuals/business-income-manual/bim20205)). Record which badges point which way and flag it.
- Construction work: the Construction Industry Scheme may apply. Record any deductions shown on statements; they are tax already paid.

5. **Does the person need a return, and must they register?**

- A sole trader must send a return if they "earned more than £1,000 (before taking off anything you can claim tax relief on)" in the tax year ([who must send a return](https://www.gov.uk/self-assessment-tax-returns/who-must-send-a-tax-return)). The test is on gross takings, not profit.
- Other triggers on the same page: a partner in a partnership; Capital Gains Tax to pay; the High Income Child Benefit Charge not collected through PAYE; and an off-payroll worker repaying a student or postgraduate loan.
- Registration: the person must tell HMRC by 5 October if they need to complete a return for the previous year and have not sent one before, or registered before but did not need to send one for 2024/25 ([who must send a return](https://www.gov.uk/self-assessment-tax-returns/who-must-send-a-tax-return)). For 2025/26 that date is 5 October 2026 ([register for Self Assessment](https://www.gov.uk/register-for-self-assessment)).
- Route the return itself to **uk-income-tax-sa100**.

6. **The trading allowance.** If annual gross trading income is £1,000 or less, the person may not have to tell HMRC, though other circumstances can still require a return, and they must keep records ("full relief"). Above £1,000 the person may deduct the £1,000 allowance instead of actual expenses, but not both ("partial relief") ([trading and property allowances](https://www.gov.uk/guidance/tax-free-allowances-on-property-and-trading-income)). The allowance cannot be used in a tax year on trade or property income from a company the person or someone connected owns or controls, a partnership where they or someone connected are partners, or their employer or their spouse's or civil partner's employer (same page). Record gross income and actual expenses both, and let **uk-bookkeeping** and **uk-income-tax-sa100** make the choice.

7. **VAT.** Registration is compulsory if either: total taxable turnover for the last 12 months goes over £90,000, or the person expects taxable turnover to go over £90,000 in the next 30 days ([register for VAT](https://www.gov.uk/register-for-vat)). The 12 months are rolling, checked at every month end, not the tax year. Taxable turnover is everything sold that is not exempt or outside the scope of VAT, and includes zero-rated sales (same page).

- Over the threshold on the 12-month test: registration is due within 30 days of the end of the month when turnover went over, and the effective date is the first day of the second month after it went over (same page). Flag it at once; late registration means VAT is owed on past sales.
- Below the threshold: registration is voluntary. A registered business may cancel if taxable turnover falls below £88,000, which is optional ([VAT thresholds](https://www.gov.uk/how-vat-works/vat-thresholds)).
- Already registered: record the effective date, return periods and scheme. The Flat Rate Scheme can be joined at £150,000 or less and must be left above £230,000 (same page).
- Route everything past the threshold question to **uk-vat-return**.

8. **Making Tax Digital for Income Tax.** MTD applies to a sole trader or landlord registered for Self Assessment whose qualifying income is over the threshold for the year tested ([MTD: who needs it](https://www.gov.uk/guidance/check-if-youre-eligible-for-making-tax-digital-for-income-tax)):

| Qualifying income over | In tax year | Must use MTD from |
| --- | --- | --- |
| £50,000 | 2024 to 2025 | 6 April 2026 |
| £30,000 | 2025 to 2026 | 6 April 2027 |
| £20,000 | 2026 to 2027 | 6 April 2028 |

- Qualifying income is total self-employment and property income before expenses (turnover), based on the return submitted in the previous tax year. Employment income, a partnership profit share, dividends (including from the person's own company), the State Pension and private pensions do not count ([qualifying income](https://www.gov.uk/guidance/work-out-your-qualifying-income-for-making-tax-digital-for-income-tax)). HMRC's example: £25,000 rental income plus £27,000 self-employment income gives qualifying income of £52,000 (same page). For a sole trader whose accounting period is longer or shorter than 12 months, HMRC annualises the figure where it has the information: 6 months of trading in the first year is doubled (same page). A part year can therefore carry someone over the threshold.
- For 2026/27, a sole trader whose 2024/25 qualifying income was over £50,000 should already be using MTD. The person must still submit a Self Assessment return for the tax year before they start. To sign up they must be registered for Self Assessment and have submitted a return in the last 2 years ([MTD: who needs it](https://www.gov.uk/guidance/check-if-youre-eligible-for-making-tax-digital-for-income-tax)).
- Partnerships will join later, on a timeline HMRC has not yet set. Some people are exempt, for example if digitally excluded (same page).
- HMRC writes to people over the threshold, but a person who gets no letter must still check (qualifying income page).
- Route the software, quarterly updates and record-keeping to **uk-bookkeeping**.

9. **National Insurance.** For 2026/27 ([self-employed NI rates](https://www.gov.uk/self-employed-national-insurance-rates)):

- Profits of £7,105 or more a year: Class 2 is treated as paid, which protects the NI record. Nothing to pay.
- Profits less than £7,105: nothing to pay, but the person can choose to pay voluntary Class 2 at £3.65 a week.
- Profits more than £12,570: Class 4 at 6% on profits over £12,570 up to £50,270, and 2% on profits over £50,270.
- Most people pay Class 2 and Class 4 through Self Assessment (same page). Examiners, landlords, ministers of religion and investors have special rules.
- Route the calculation, State Pension age and voluntary contributions to **uk-national-insurance**. Record profit, date of birth and any other employment.

10. **Payments on account.** Read last year's SA302. Payments on account are payments towards the next tax bill, including Class 4 NI for the self-employed. Each is half of the tax owed last year, due by midnight on 31 January and 31 July. They are not due if either: the tax owed last year was less than £1,000, or more than 80% of it was paid outside Self Assessment, for example through a tax code ([payments on account](https://www.gov.uk/understand-self-assessment-bill/payments-on-account)). A first-year filer pays the full bill plus the first payment on account towards the next year on the same 31 January (same page). Record last year's liability and the tax paid at source; route the calculation to **uk-income-tax-sa100**.

11. **Records.** A sole trader must keep records of business income and expenses, for at least 5 years after the 31 January submission deadline of the tax year ([how long to keep records](https://www.gov.uk/self-employed-records/how-long-to-keep-your-records)). If the records will not support a return, or the person must join MTD and has no digital records, route to **uk-bookkeeping** before anything else.

12. **Other income and disposals.** Route each item and record it:

- UK rental income: **uk-rental-sa105**.
- Foreign income or gains: **uk-non-dom**.
- Disposals of shares, crypto, a second home or business assets: **uk-capital-gains-sa108**. Capital Gains Tax to pay is itself a reason to file.
- Staff, or the person's own company payroll: **uk-payroll**.
- Dividends, savings interest, Child Benefit charge, student loan: **uk-income-tax-sa100**, or refer where it has no coverage.

13. **Hand back.** Summarise what was found, list every open flag, and name the next Guide for each item. Give the filing dates from the filing section below.

## IR35 and off-payroll working: the method and when to refer

**What the rules do.** The off-payroll working rules make sure that a worker who provides services to a client through their own intermediary pays broadly the same Income Tax and National Insurance as an employee would. They apply if the worker would have been an employee had they provided the services directly to that client. The rules are sometimes called "IR35" ([understanding off-payroll working](https://www.gov.uk/guidance/understanding-off-payroll-working-ir35)).

**When they can apply.** Only where there is an intermediary: usually the worker's own limited company (a personal service company, or PSC), but also a partnership or another individual (same page).

- A sole trader contracting directly with the client has no intermediary, so the off-payroll rules do not apply. The question is ordinary employment status (step 4). If the client should be treating the person as an employee, that is the client's PAYE problem and a status dispute; flag it and refer.
- Someone employed by an umbrella company: the rules are unlikely to apply (same page). The umbrella pays them through PAYE. Their umbrella pay is employment income, not self-employment.
- Paid through an agency's payroll: employment income under PAYE.

**Who decides status.** It depends on the client, not the worker:

1. **Public sector client**: the client decides. The rules apply to all public authorities, including government departments, local authorities, schools, universities and parts of the NHS ([off-payroll working for clients](https://www.gov.uk/guidance/off-payroll-working-for-clients)).
2. **Medium or large private or voluntary sector client**: the client decides. HMRC's guidance says a client is medium or large if it meets 2 or more of: annual turnover of more than £10.2 million, balance sheet total of more than £5.1 million, more than 50 employees (same page). The law ties "small" to the Companies Act small companies regime (ITEPA 2003 [section 60A](https://www.legislation.gov.uk/ukpga/2003/1/section/60A)), whose limits in [Companies Act 2006 section 382](https://www.legislation.gov.uk/ukpga/2006/46/section/382) now read not more than £15 million turnover and £7.5 million balance sheet, with not more than 50 employees. The gov.uk page and the statute text differ. Do not work out the client's size yourself: ask the client.
3. **Small private sector client**: the worker's own company decides status, and if the rules apply it works out a "deemed employment payment" and pays the tax and Class 1 NI on it ([small clients](https://www.gov.uk/guidance/off-payroll-working-for-intermediaries-and-contractors-providing-services-to-small-clients-in-the-private-sector)).

**What the worker should get.** From a public sector or medium or large client, a status determination statement (SDS) with the reasons. A worker who gets none can ask the client to confirm its size, and the client has 45 days to reply ([public sector or medium and large clients](https://www.gov.uk/guidance/off-payroll-working-for-intermediaries-and-contractors-providing-services-to-the-public-sector-or-medium-and-large-clients-in-the-private-sector)).

**Contract by contract.** The rules apply engagement by engagement. A worker may have some contracts inside and some outside. A change in terms or working practices can mean a new determination ([understanding off-payroll working](https://www.gov.uk/guidance/understanding-off-payroll-working-ir35)).

**If the client says "inside".** The deemed employer (the client, or the agency paying the worker's company) deducts Income Tax and employee NI from the fees paid to the worker's company, and pays employer NI (same page). The company can then pay those fees on to the worker as salary without deducting tax or NI again, or as dividends that do not need to go on the worker's Self Assessment return ([public sector or medium and large clients](https://www.gov.uk/guidance/off-payroll-working-for-intermediaries-and-contractors-providing-services-to-the-public-sector-or-medium-and-large-clients-in-the-private-sector)).

**Student loans.** Deemed employers do not deduct student or postgraduate loan repayments from off-payroll fees. The worker must register for Self Assessment and file a return to pay them ([understanding off-payroll working](https://www.gov.uk/guidance/understanding-off-payroll-working-ir35)).

**The status check.** HMRC's Check Employment Status for Tax (CEST) tool gives HMRC's view of status and whether the off-payroll rules apply to an engagement. HMRC will stand by the result as long as the information given is accurate and in line with its guidance, and the result can be used as a valid SDS ([CEST](https://www.gov.uk/guidance/check-employment-status-for-tax)). There must be a contract in place or expected; it can be written, verbal or implied (same page).

**The intake method for a contractor.**

1. Record the structure: own company, umbrella, agency payroll, or direct as a sole trader.
2. For each engagement record the client's name, sector, whether the client has confirmed its size, and whether there is an SDS and what it says.
3. Ask for the contract and a description of the working practice: who decides what, when, where and how; whether the person can send a substitute; how they are paid.
4. Route: sole trader, direct: steps 4 to 12. Umbrella or agency payroll: **uk-income-tax-sa100** for the personal return if one is needed. Own company: the personal return goes to **uk-income-tax-sa100**, company payroll to **uk-payroll**, company accounts and Corporation Tax are referred.

**Refer to an adviser when:**

- the worker disagrees with a client's SDS. A disagreement can be raised until the last payment for the services, and the client has 45 days to respond; during that time the deemed employer keeps applying the rules as determined ([public sector or medium and large clients](https://www.gov.uk/guidance/off-payroll-working-for-intermediaries-and-contractors-providing-services-to-the-public-sector-or-medium-and-large-clients-in-the-private-sector));
- the worker's own company must decide status for a small client, or has to work out a deemed employment payment;
- the client's size is unclear or disputed;
- HMRC has opened an enquiry, or past years were treated as outside without a determination;
- someone is offering a scheme that claims to get around the rules. HMRC warns that such schemes exist ([understanding off-payroll working](https://www.gov.uk/guidance/understanding-off-payroll-working-ir35)).

## Figures that decide a route, with years

Every figure below is 2026/27 unless the row says otherwise. The specialist Guide named in the last column holds the detail.

| Switch | Figure | Year | Source | Detail in |
| --- | --- | --- | --- | --- |
| Sole trader return trigger: gross takings more than | £1,000 | each year | [who must send a return](https://www.gov.uk/self-assessment-tax-returns/who-must-send-a-tax-return) | uk-income-tax-sa100 |
| Trading allowance (instead of expenses, not as well) | £1,000 | each year | [trading and property allowances](https://www.gov.uk/guidance/tax-free-allowances-on-property-and-trading-income) | uk-bookkeeping, uk-income-tax-sa100 |
| Property allowance, separate from the trading allowance | £1,000 | each year | same page | uk-rental-sa105 |
| Tell HMRC you need a return (first return, or none needed for 2024/25) | by 5 October 2026 | for 2025/26 | [register for Self Assessment](https://www.gov.uk/register-for-self-assessment) | uk-income-tax-sa100 |
| VAT registration: taxable turnover more than, rolling 12 months or next 30 days alone | £90,000 | current | [register for VAT](https://www.gov.uk/register-for-vat) | uk-vat-return |
| VAT deregistration (optional): taxable turnover less than | £88,000 | current | [VAT thresholds](https://www.gov.uk/how-vat-works/vat-thresholds) | uk-vat-return |
| Flat Rate Scheme: join at or below / must leave above | £150,000 / £230,000 | current | same page | uk-vat-return |
| MTD: qualifying income over £50,000 in 2024/25 | from 6 April 2026 | 2026/27 | [MTD: who needs it](https://www.gov.uk/guidance/check-if-youre-eligible-for-making-tax-digital-for-income-tax) | uk-bookkeeping |
| MTD: over £30,000 in 2025/26 | from 6 April 2027 | 2027/28 | same page | uk-bookkeeping |
| MTD: over £20,000 in 2026/27 | from 6 April 2028 | 2028/29 | same page | uk-bookkeeping |
| Class 2 treated as paid: profits of or above | £7,105 | 2026/27 | [self-employed NI rates](https://www.gov.uk/self-employed-national-insurance-rates) | uk-national-insurance |
| Voluntary Class 2 (profits less than £7,105) | £3.65 a week | 2026/27 | same page | uk-national-insurance |
| Class 4 main rate on profits over £12,570 up to £50,270 | 6% | 2026/27 | same page | uk-national-insurance |
| Class 4 rate on profits over £50,270 | 2% | 2026/27 | same page | uk-national-insurance |
| No payments on account if last year's tax owed was less than | £1,000 | each year | [payments on account](https://www.gov.uk/understand-self-assessment-bill/payments-on-account) | uk-income-tax-sa100 |
| No payments on account if tax paid outside Self Assessment was more than | 80% | each year | same page | uk-income-tax-sa100 |
| Payments on account due | 31 January and 31 July | each year | same page | uk-income-tax-sa100 |
| Records kept at least | 5 years after the 31 January deadline | each year | [how long to keep records](https://www.gov.uk/self-employed-records/how-long-to-keep-your-records) | uk-bookkeeping |
| Off-payroll: medium or large client if 2 or more of turnover, balance sheet, employees above | £10.2 million / £5.1 million / 50 (gov.uk guidance; see the IR35 section on the statute) | current | [off-payroll working for clients](https://www.gov.uk/guidance/off-payroll-working-for-clients) | refer |

## Boundaries and exceptions

| Situation | What follows | Source |
| --- | --- | --- |
| Gross takings exactly £1,000 | Not "more than £1,000", so the sole trader trigger is not met; full relief. Another trigger can still require a return | [who must send a return](https://www.gov.uk/self-assessment-tax-returns/who-must-send-a-tax-return); [allowances](https://www.gov.uk/guidance/tax-free-allowances-on-property-and-trading-income) |
| Gross takings over £1,000 but small profit | Return needed: the test is before expenses. Choose allowance or actual expenses, not both | same pages |
| Trading income from a company the person or a connected person controls, or from their own or their spouse's employer | No trading allowance for that tax year | [allowances](https://www.gov.uk/guidance/tax-free-allowances-on-property-and-trading-income) |
| Taxable turnover exactly £90,000 on the 12-month test | Not "over £90,000"; not yet compulsory. Keep checking every month end | [register for VAT](https://www.gov.uk/register-for-vat) |
| One big contract expected to bring more than £90,000 within 30 days | Register by the end of that 30-day period; effective from the date the person realised | same page |
| Qualifying income for MTD exactly £50,000 in 2024/25 | Not "over £50,000"; not in from 6 April 2026 on that test | [MTD: who needs it](https://www.gov.uk/guidance/check-if-youre-eligible-for-making-tax-digital-for-income-tax) |
| Large salary plus small self-employment | Salary does not count for MTD; only self-employment and property turnover | [qualifying income](https://www.gov.uk/guidance/work-out-your-qualifying-income-for-making-tax-digital-for-income-tax) |
| Profits exactly £7,105 | "£7,105 or more": Class 2 treated as paid | [self-employed NI rates](https://www.gov.uk/self-employed-national-insurance-rates) |
| Profits exactly £12,570 | Class 4 is due only on profits "more than £12,570": none | same page |
| Exactly 80% of last year's tax paid outside Self Assessment | The exemption needs "more than 80%": payments on account still due | [payments on account](https://www.gov.uk/understand-self-assessment-bill/payments-on-account) |
| Last year's tax owed exactly £1,000 | The exemption needs "less than £1,000": payments on account due unless the 80% test is met | same page |
| Employed by an umbrella company | Off-payroll rules unlikely to apply; PAYE employment income | [understanding off-payroll working](https://www.gov.uk/guidance/understanding-off-payroll-working-ir35) |
| Sole trader contracting directly, no company | No intermediary, so no off-payroll rules; ordinary employment status question | same page |
| Own company working for a small private sector client | The worker's own company decides status | [small clients](https://www.gov.uk/guidance/off-payroll-working-for-intermediaries-and-contractors-providing-services-to-small-clients-in-the-private-sector) |
| Registered for Self Assessment after 5 October 2026 for 2025/26 | Return due 3 months from the date on HMRC's letter or email, but the tax is still due by 31 January 2027 | [deadlines](https://www.gov.uk/self-assessment-tax-returns/deadlines) |

## Worked cases

**Case 1. Side sales under the allowance.** An employee sells handmade goods online. Gross takings in 2025/26: £800. No other untaxed income. ([who must send a return](https://www.gov.uk/self-assessment-tax-returns/who-must-send-a-tax-return))
- £800 is not more than £1,000, so the sole trader return trigger is not met, and the income is covered by full relief. They may not need to tell HMRC but must keep records ([allowances](https://www.gov.uk/guidance/tax-free-allowances-on-property-and-trading-income)).
- Record the badges of trade in case the activity grows. Route: none needed now. Re-check each year.

**Case 2. New sole trader, first return.** A web designer started in June 2025 and has never filed. Gross takings in 2025/26: £34,000; profit £30,000. ([who must send a return](https://www.gov.uk/self-assessment-tax-returns/who-must-send-a-tax-return))
- Takings are more than £1,000: a return is needed, and they must tell HMRC by 5 October 2026 ([register for Self Assessment](https://www.gov.uk/register-for-self-assessment)). Online return and payment by 31 January 2027 ([deadlines](https://www.gov.uk/self-assessment-tax-returns/deadlines)).
- NI for 2025/26: profit is £6,845 or more, so Class 2 is treated as paid; Class 4 = (£30,000 − £12,570) × 6% = £17,430 × 6% = £1,045.80 ([NI rates and allowances](https://www.gov.uk/government/publications/rates-and-allowances-national-insurance-contributions/rates-and-allowances-national-insurance-contributions); the 6% rate and £12,570 limit are the same in 2025/26 and 2026/27).
- Payments on account: first year, so on 31 January 2027 they pay the whole 2025/26 bill plus the first payment on account for 2026/27, then the second on 31 July 2027, unless the bill is less than £1,000 ([payments on account](https://www.gov.uk/understand-self-assessment-bill/payments-on-account)).
- MTD: the 2025/26 qualifying income is £34,000 before any annualising for the part year, already over £30,000, so MTD applies from 6 April 2027 ([MTD: who needs it](https://www.gov.uk/guidance/check-if-youre-eligible-for-making-tax-digital-for-income-tax); [qualifying income](https://www.gov.uk/guidance/work-out-your-qualifying-income-for-making-tax-digital-for-income-tax)).
- Routes: uk-income-tax-sa100, uk-national-insurance, uk-bookkeeping.

**Case 3. Consultant already in MTD and crossing the VAT threshold.** Gross takings in 2024/25: £55,000. Not VAT registered. At the end of August 2026 taxable turnover for the last 12 months goes over £90,000 for the first time. ([register for VAT](https://www.gov.uk/register-for-vat))
- MTD: £55,000 is over £50,000 in 2024/25, so they should have been using MTD from 6 April 2026. If not signed up, they can still sign up (same MTD page). Route to uk-bookkeeping. ([MTD: who needs it](https://www.gov.uk/guidance/check-if-youre-eligible-for-making-tax-digital-for-income-tax))
- VAT: they must register within 30 days of the end of August, so by 30 September 2026, with an effective date of 1 October 2026, the first day of the second month after going over ([register for VAT](https://www.gov.uk/register-for-vat)). Route to uk-vat-return now; this is urgent.

**Case 4. Employee with a sideline: payments on account switched off.** Last year's total tax was £2,400, of which £2,100 was paid through PAYE. ([payments on account](https://www.gov.uk/understand-self-assessment-bill/payments-on-account))
- £2,100 ÷ £2,400 = 87.5%, which is more than 80%, so no payments on account are due ([payments on account](https://www.gov.uk/understand-self-assessment-bill/payments-on-account)).
- Had PAYE covered exactly £1,920 (80%), the test would fail and payments on account would be due, because the exemption needs more than 80%. ([payments on account](https://www.gov.uk/understand-self-assessment-bill/payments-on-account))

**Case 5. Contractor through their own company, large client.** An IT contractor works through their own limited company for a large bank. The bank's SDS says the engagement is inside the rules. They are repaying a student loan.
- The client decides status for a large private sector client. The deemed employer deducts Income Tax and employee NI from the fees and pays employer NI ([understanding off-payroll working](https://www.gov.uk/guidance/understanding-off-payroll-working-ir35)).
- The student loan is not deducted, so they must register for Self Assessment and file to repay it (same page).
- Routes: personal return to uk-income-tax-sa100; company payroll to uk-payroll; company accounts referred. If they disagree with the SDS, refer.

**Case 6. Contractor, small client.** The same contractor also works for a five-person design studio.
- A small private sector client does not decide status; the contractor's own company does, and if the rules apply it works out a deemed employment payment ([small clients](https://www.gov.uk/guidance/off-payroll-working-for-intermediaries-and-contractors-providing-services-to-small-clients-in-the-private-sector)). Refer.

**Case 7. Recent arrival.** A freelancer moved to the UK in October 2025 and still has clients abroad.
- Residence for 2025/26 may be a split year: route to uk-statutory-residence-test first. Foreign income and the 4-year FIG regime: route to uk-non-dom. Do not start the return until both are settled.

## When to refuse or refer

Stop and refer to a qualified adviser, saying why in one sentence, when:

- **Residence is in doubt**: arrival or departure in the year, split-year treatment, or non-resident with UK income. Read uk-statutory-residence-test first; a split-year or non-resident return needs an adviser.
- **Foreign income or gains**, or a claim under the 4-year FIG regime or for remittance-basis history: route to uk-non-dom; refer anything it marks out of scope.
- **Employment status is contested**: the facts point to employment but the person is invoicing, or HMRC or a client has challenged it. Record it; HMRC can reclassify. Do not decide it.
- **Any IR35 point listed in the IR35 section**: SDS disagreement, a small-client determination by the worker's own company, a deemed employment payment, an enquiry, or an avoidance scheme.
- **A partnership return** or a **limited company's** own accounts and Corporation Tax. The individual's personal return stays in scope via uk-income-tax-sa100.
- **Scottish taxpayer**: uk-income-tax-sa100 refers Scottish rates.
- **Over the VAT threshold and not registered**: route to uk-vat-return at once; registration is compulsory and late registration is costly.
- **In MTD without digital records**, or records that will not support a return: route to uk-bookkeeping first.
- **Trade or hobby in doubt** with material sums: record the badges both ways and refer.
- **Past years never reported**: refer. Disclosure of earlier years is outside this Guide.

Refuse to: file anything for the person; tell them their employment status or residence as a settled fact; or suggest a way to avoid registering for VAT, MTD or Self Assessment.

## Filing and payment

**Returns being filed now: 2025/26 (6 April 2025 to 5 April 2026)** ([deadlines](https://www.gov.uk/self-assessment-tax-returns/deadlines)):

| What | Deadline |
| --- | --- |
| Tell HMRC a return is needed (first return, or none needed for 2024/25) | 5 October 2026 |
| Paper return | 11:59pm on 31 October 2026 |
| Online return, to have a balance collected through the tax code | 11:59pm on 30 December 2026 |
| Online return | 11:59pm on 31 January 2027 |
| Pay the balance for 2025/26 and the first payment on account for 2026/27 | 11:59pm on 31 January 2027 |
| Second payment on account for 2026/27 | 31 July 2027 |

- If the person registers after 5 October 2026, HMRC sets a return deadline 3 months from the date on its letter or email, but the tax is still due by 31 January 2027 (same page). Telling HMRC late can bring a penalty ([register for Self Assessment](https://www.gov.uk/register-for-self-assessment)).
- NI on the 2025/26 return: Class 2 treated as paid on profits of £6,845 or more; voluntary Class 2 is £3.50 a week; Class 4 is 6% between £12,570 and £50,270 and 2% above ([NI rates and allowances](https://www.gov.uk/government/publications/rates-and-allowances-national-insurance-contributions/rates-and-allowances-national-insurance-contributions)). Route to uk-national-insurance.

**The current year: 2026/27.** The same pattern moves on one year: registration by 5 October after the year ends, paper return by 31 October, online return and payment by 31 January, second payment on account by 31 July. Anyone who must use MTD from 6 April 2026 keeps digital records and sends quarterly updates for 2026/27 through software; route that to uk-bookkeeping. Penalties and interest are in uk-income-tax-sa100.

## Completion checklist

- [ ] Tax year fixed, and every document tagged with its year.
- [ ] Residence recorded; any doubt routed to uk-statutory-residence-test; foreign income routed to uk-non-dom.
- [ ] Structure recorded: sole trader, partner, own company, umbrella or agency payroll.
- [ ] Employment status and trade-or-hobby recorded with the facts both ways, and flagged if unsettled.
- [ ] For each contracting engagement: client, sector, size confirmed or not, SDS held or not.
- [ ] Gross takings recorded; return trigger (more than £1,000) and 5 October registration checked. ([who must send a return](https://www.gov.uk/self-assessment-tax-returns/who-must-send-a-tax-return))
- [ ] Trading allowance or actual expenses left open for the specialist Guide, with both figures recorded.
- [ ] Rolling 12-month taxable turnover checked against £90,000; the next 30 days checked. ([register for VAT](https://www.gov.uk/register-for-vat))
- [ ] MTD status set from the earlier year's gross self-employment and property income.
- [ ] Profit recorded for Class 2 and Class 4.
- [ ] Last year's tax and tax paid at source recorded for the payments on account tests.
- [ ] Records adequate, or routed to uk-bookkeeping.
- [ ] Rental, gains, payroll, dividends, student loan and Child Benefit each routed.
- [ ] Every open flag listed, with the Guide or adviser that closes it, and the filing dates given.

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
