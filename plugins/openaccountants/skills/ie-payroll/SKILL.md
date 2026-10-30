---
name: ie-payroll
description: "Irish employer payroll for tax year 2026: PAYE Income Tax at 20% and 40% under the Revenue Payroll Notification (RPN), the 2026 standard rate cut-off points (EUR 44,000 single) and tax credits (EUR 2,000 personal, EUR 2,000 employee), USC 2026 bands, PRSI Class A at 4.2% employee to 30 September 2026 and 4.35% from 1 October 2026, employer 9%/11.25% then 9.15%/11.40% above EUR 552 a week, the PRSI Credit, the EUR 14.15 minimum wage, company car BIK and the EUR 1,500 small benefit exemption, auto-enrolment (MyFutureFund) at 1.5% employee and 1.5% employer from 1 January 2026, payroll submissions on or before pay day, payment by the 14th (23rd on ROS), the emergency basis, and the EUR 4,000 penalty and 0.0274% daily interest. Trigger on 'Irish payroll', 'gross to net Ireland', 'RPN', 'payroll submission', 'emergency tax', 'BIK Ireland', 'auto-enrolment', 'MyFutureFund'. Out of scope: USC in depth (ie-usc), self-employed PRSI (ie-prsi-class-s), posted workers and A1 (ie-prsi-cross-border)"
license: "AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)"
metadata:
  source: openaccountants
  openaccountants_url: "https://www.openaccountants.com/skills/ie-payroll"
  jurisdiction: "IE"
  tax_year: "2026"
  last_updated: "2026-10-27"
  authored_by: "Michael Cutajar and the OpenAccountants team"
  trust_label: "Built by Michael Cutajar and the OpenAccountants team"
  review_status: "pending_review"
---

# Ireland payroll: PAYE, USC, PRSI and auto-enrolment, tax year 2026 (v0.2)

> **Source-cited draft.** Drafted from the Taxes Consolidation Act 1997 Part 42 Chapter 4 (Revenue's Notes for Guidance, Finance Act 2025 edition), Finance Act 2025, the Social Welfare Consolidation Act 2005 s.13 and the Acts that amend it, the National Training Fund Act 2000, the Automatic Enrolment Retirement Savings System Act 2024, and Revenue, Department of Social Protection and Department of Enterprise pages, all read on 2026-10-24. No accountant has reviewed it. Do not run a payroll from it without review by a qualified Irish payroll professional.

Authority: the Revenue Commissioners (the Collector-General collects PAYE, USC, PRSI and LPT deducted through payroll). PRSI goes on to the Department of Social Protection. Auto-enrolment contributions go to the National Automatic Enrolment Retirement Savings Authority (NAERSA), which runs MyFutureFund. Currency: euro. Section numbers are TCA 1997 unless another act is named.

See also: `ie-usc` (USC rules in depth, reduced rates, exempt income), `ie-prsi-class-s` (PRSI for the self-employed), `ie-prsi-cross-border` (posted workers, A1 certificates, bilateral agreements), `ie-income-tax-form11` (proprietary directors and others who file Form 11), `ie-paye-rental-nonresident` (PAYE workers with side income), `ie-cross-border` (residence).

## Who this applies to

- **Employers** that pay emoluments to employees in Ireland. The employer deducts Income Tax, USC and employee PRSI under the PAYE system and pays them over with employer PRSI (s.985, s.985G; Social Welfare Consolidation Act 2005 s.13). The employer stays responsible when it uses software, a payroll bureau, an agency or ROS ([Payroll submissions](https://www.revenue.ie/en/employing-people/becoming-an-employer-and-ongoing-obligations/employer-obligations-from-01-01-2019/payroll-submissions.aspx)).
- **PRSI Class A** covers employees aged 16 to 66 (or under 70 without a State Pension (Contributory)) in industrial, commercial and service-type employment under a contract of service with reckonable pay of EUR 38 or more a week from all employments, and civil and public servants recruited from 6 April 1995 ([DSP, PRSI Class A rates](https://www.gov.ie/en/department-of-social-protection/publications/prsi-class-a-rates/)).
- **Auto-enrolment** applies from 1 January 2026 to employees aged at least 23 and under 60, earning at least EUR 20,000 a year across all employments, in an employment that is not exempt. An employment is exempt where the employee or the employer pays into a qualifying occupational pension scheme, PRSA, trust RAC or PEPP through payroll (AE Act 2024 ss.50, 51; [DSP, auto-enrolment for employers](https://www.gov.ie/en/department-of-social-protection/publications/auto-enrolment-retirement-savings-system-for-employers/)). From 1 January 2026 a defined contribution occupational scheme or a PRSA qualifies only if the employer pays at least the lower of 1.5% of gross pay or EUR 1,200 a year, and employer plus employee together pay at least the lower of 3.5% of gross pay or EUR 2,800 a year; a defined benefit scheme qualifies if continuing service accrues a long service benefit (s.52; S.I. No. 668 of 2025, inserting Schedule 1A into S.I. No. 637 of 2025). An employee-only contribution to a defined contribution scheme or PRSA does not make the job exempt. NAERSA decides who is enrolled, not the employer. An employee aged 18 or over and under pensionable age in a non-exempt employment can opt in (s.53). An enrolled employee can opt out only in the window from 6 to 8 months after enrolment (s.54).
- **Out of scope here; refer:** public sector PRSI classes (B, C, D) and Classes H, J, K, M and Community Employment; proprietary directors (their PRSI class may not be Class A); share schemes and share-based pay; pension lump sums; termination payments above the basic exemption; backdated pay covering more than one tax year; Insolvency and Redundancy Payments Scheme claims; attachment of earnings orders beyond applying the order as written.

## Rates, bands and thresholds

| Item | Rate or amount | Year | Source |
|---|---|---|---|
| Income Tax standard rate / higher rate | 20% / 40% | 2026 | https://www.revenue.ie/en/personal-tax-credits-reliefs-and-exemptions/tax-relief-charts/index.aspx |
| Standard rate cut-off point: single, widowed or surviving civil partner, no qualifying children | EUR 44,000 | 2026 | same |
| Cut-off point: single person qualifying for the Single Person Child Carer Credit | EUR 48,000 | 2026 | same |
| Cut-off point: married or civil partners, one income | EUR 53,000 | 2026 | same |
| Cut-off point: married or civil partners, two incomes | EUR 53,000 plus the lower of EUR 35,000 or the lower earner's income | 2026 | same |
| Single Person Tax Credit / Married or Civil Partner Tax Credit | EUR 2,000 / EUR 4,000 | 2026 | same |
| Employee (PAYE) Tax Credit | EUR 2,000 | 2026 | same |
| USC bands (standard) | 0.5% on first EUR 12,012; 2% on next EUR 16,688; 3% on next EUR 41,344; 8% on the balance | 2026 | https://www.irishstatutebook.ie/eli/2025/act/18/section/2/enacted/en/html |
| USC exemption: total income at or below | EUR 13,000 (above it, USC on all income) | 2026 | https://www.revenue.ie/en/jobs-and-pensions/usc/index.aspx |
| USC reduced rates (aged 70+ or full Medical Card, income EUR 60,000 or less) | 0.5% on first EUR 12,012, 2% on the balance | 2026 | https://www.revenue.ie/en/jobs-and-pensions/usc/reduced-rates.aspx |
| Emergency basis, PPSN given: cut-off point weeks 1 to 4 / month 1; nil after | EUR 846.16 a week / EUR 3,666.67 a month; tax credit nil | 2026 | https://www.revenue.ie/en/jobs-and-pensions/documents/emergency-rates.pdf |
| Emergency USC | 8% on all pay, no cut-off | 2026 | same |
| PRSI Class A employee rate, weekly pay over EUR 352 | 4.1% to 30 Sep 2025; 4.2% from 1 Oct 2025 to 30 Sep 2026; 4.35% from 1 Oct 2026 | 2025-2026 | https://www.irishstatutebook.ie/pdf/2024/en.act.2024.0024.pdf |
| PRSI Class A, weekly pay EUR 38 to EUR 352 (subclass A0) | employee nil | 2026 | https://www.gov.ie/en/department-of-social-protection/publications/prsi-class-a-rates/ |
| PRSI Credit (subclass AX, EUR 352.01 to EUR 424 a week) | EUR 12 less one sixth of pay over EUR 352.01 | 2026 | https://revisedacts.lawreform.ie/eli/2005/act/26/revised/en/html |
| Employer PRSI, weekly pay up to EUR 552 / over EUR 552 (whole week's pay) | 9% / 11.25% to 30 Sep 2026; 9.15% / 11.40% from 1 Oct 2026 | 2026 | https://www.gov.ie/en/department-of-social-protection/publications/prsi-class-a-rates/ |
| Employer threshold for the higher rate (s.13(2)(d)) | EUR 552 a week from 1 Jan 2026 (was EUR 527; Act 19 of 2025 s.2, in operation 1 January 2026) | 2026 | https://www.irishstatutebook.ie/pdf/2025/en.act.2025.0019.pdf |
| National Training Fund levy, inside the employer rate | 1.0% of reckonable earnings | 2026 | https://revisedacts.lawreform.ie/eli/2000/act/41/revised/en/html |
| Monthly PRSI bands (A0 / AX / AL / A1) | to EUR 1,525 / to EUR 1,837 / to EUR 2,392 / over EUR 2,392 | 2026 | https://assets.gov.ie/static/documents/cb168977/PRSI_C20260116_Contribution_Rates_and_User_Guide_-_SW_14_-_English_Version_-_January_2026_.pdf-web.pdf |
| National minimum wage, aged 20+ / 19 / 18 / under 18 | EUR 14.15 / 12.74 / 11.32 / 9.91 an hour from 1 Jan 2026 | 2026 | https://www.gov.ie/en/department-of-enterprise-tourism-and-employment/publications/national-minimum-wage-increase-on-1-january-2025/ |
| Minimum wage: board / lodgings that may count as pay | EUR 1.27 an hour worked / EUR 33.42 a week or EUR 4.77 a day | 2026 | same |
| Auto-enrolment: employee and employer contribution each, on gross pay | 1.5% in years 1 to 3 (from 1 Jan 2026), 3% years 4 to 6, 4.5% years 7 to 9, 6% after | 2026 | https://revisedacts.lawreform.ie/eli/2024/act/20/revised/en/html |
| Auto-enrolment: State contribution | 0.5% in years 1 to 3 | 2026 | same |
| Auto-enrolment: earnings cap / entry threshold | no contribution on gross pay above EUR 80,000 in the year (s.58(3)); EUR 20,000 a year to be enrolled (s.50(3)) | 2026 | same |
| Minimum standards for an existing scheme to make the job exempt (DC scheme or PRSA) | employer at least the lower of 1.5% of gross pay or EUR 1,200 a year; employer and employee together at least the lower of 3.5% or EUR 2,800 a year | from 1 Jan 2026 | https://www.irishstatutebook.ie/eli/2025/si/668/made/en/print |
| Pension relief, % of earnings by age | under 30: 15%; 30-39: 20%; 40-49: 25%; 50-54: 30%; 55-59: 35%; 60+: 40% | 2026 | https://www.revenue.ie/en/jobs-and-pensions/pension/relief/tax-relief-limits.aspx |
| Pension relief earnings limit | EUR 115,000 a year | 2026 | same |
| Company car BIK: % of Original Market Value, 0 to 26,000 business km, categories A1 / A / B / C / D / E | 15% / 22.5% / 26.25% / 30% / 33.75% / 37.5% | 2026 | https://www.irishstatutebook.ie/eli/2025/act/18/section/24/enacted/en/html |
| Car BIK, 26,001 to 39,000 / 39,001 to 48,000 / 48,001 km and above, categories A1 to E | 12-30% / 9-22.5% / 6-15%, in the same steps | 2026 | same |
| Car OMV reduction, categories A1 to D (not E) | EUR 10,000 for 2023 to 2026; EUR 5,000 for 2027; EUR 2,500 for 2028 | 2026 | same |
| Extra OMV reduction for an electric car, on top of the reduction above | EUR 20,000 in 2026 (EUR 30,000 in total); EUR 10,000 in 2027 (EUR 15,000 in total); none in 2028 | 2026 | https://www.revenue.ie/en/tax-professionals/tdm/income-tax-capital-gains-tax-corporation-tax/part-05/05-01-01b.pdf |
| Small benefit exemption | up to 5 non-cash benefits a year, combined EUR 1,500 | 2026 | https://www.revenue.ie/en/employing-people/benefit-in-kind-for-employers/valuation-of-benefits/small-benefit-exemption.aspx |
| Termination payment basic exemption | EUR 10,160 plus EUR 765 per full year of service; lifetime limit EUR 200,000 | 2026 | https://www.revenue.ie/en/personal-tax-credits-reliefs-and-exemptions/lump-sum-payments/basic-exemption.aspx |
| Quarterly remitting allowed if yearly Income Tax, PRSI and USC are | EUR 28,800 or less | 2026 | https://www.revenue.ie/en/employing-people/paying-your-employees-tax-to-revenue/paying-tax-to-revenue.aspx |

The employer does not choose cut-off points or credits. The RPN gives each employee's yearly figures and the employer divides them by 52, 26 or 12 ([Cumulative basis](https://www.revenue.ie/en/employing-people/paying-an-employee/methods-of-calculating-tax/cumulative-basis.aspx)). Use the table to sense-check an RPN. The USC exemption and reduced rates also come through the RPN; do not apply them yourself.

**The employer PRSI rate has two parts.** Social Welfare Consolidation Act 2005 s.13(2)(d) sets 8% and 10.25% to 30 September 2026, and 8.15% and 10.4% from 1 October 2026 (Social Welfare (Miscellaneous Provisions) Act 2024 s.3). The National Training Fund Act 2000 s.4 adds a 1.0% levy. Together they give the 9% / 11.25% and 9.15% / 11.40% rates the Department prints.

**PRSI bands are cliffs.** Once weekly pay is over EUR 552 (monthly over EUR 2,392), the employer higher rate applies to the whole week's pay, not only the excess. The employee rate also applies to the whole week's pay once pay is over EUR 352.

## The taxable base

**Order of the payroll:**

1. **Gross pay:** basic, overtime, commission, bonus, taxable cash allowances, plus notional pay (benefit in kind). Gross pay is pay before any pension or salary sacrifice deduction ([Gross and taxable pay](https://www.revenue.ie/en/employing-people/what-constitutes-pay/what-are-gross-and-taxable-pay/index.aspx)).
2. **Taxable pay for Income Tax:** gross pay less employee contributions to a Revenue-approved pension scheme, PRSA, RAC or PEPP deducted by the employer, approved income continuance contributions, and salary sacrifice amounts (same page). Relief is capped at the age percentage and the EUR 115,000 earnings limit; contributions above the limits, or to a scheme not shown to be approved, go through Income Tax. Employer contributions do not count toward the employee's limit. The employee's total contributions for the limit include ordinary contributions, Additional Voluntary Contributions (AVCs) and special contributions ([Employee's pension contributions](https://www.revenue.ie/en/employing-people/what-constitutes-pay/employees-pension-payments/index.aspx)).
3. **Income Tax:** 20% up to the period cut-off point, 40% on the balance, less the period tax credits (s.985; [Rule for calculating tax](https://www.revenue.ie/en/employing-people/paying-an-employee/methods-of-calculating-tax/calculating-tax-rules.aspx)).
4. **USC on gross pay.** Employee pension contributions are not deducted: "There is no relief from USC for employee pension contributions" ([USC](https://www.revenue.ie/en/jobs-and-pensions/usc/index.aspx), [Employee's pension contributions](https://www.revenue.ie/en/employing-people/what-constitutes-pay/employees-pension-payments/index.aspx)). Rules in depth: `ie-usc`.
5. **PRSI on reckonable pay**, which includes notional pay (s.13(2)(e)). For private sector employees PRSI is "fully chargeable" on superannuation and PRSA contributions (SW14). Employer PRSI is not charged on share-based remuneration ([DSP](https://www.gov.ie/en/department-of-social-protection/publications/prsi-class-a-rates/)).
6. **Auto-enrolment:** where NAERSA has sent an Automatic Enrolment Payroll Notification (AEPN), deduct the participant contribution from pay and pay it, with the matching employer contribution, to NAERSA on or before the pay day (AE Act s.59). Contributions are on gross pay up to EUR 80,000 a year. Gross pay is the amount reported as gross pay on the payroll submission (s.47(2)), which includes notional pay; DSP: "anything included in the gross pay field of a payroll file will be assessable." In DSP's words, "Instead of tax relief on employee contributions, the State will provide a top-up." Employer contributions are deductible for the employer (s.787AF, inserted by Finance Act 2025 s.16) and are not a benefit in kind for the employee ([DSP, auto-enrolment for employers](https://www.gov.ie/en/department-of-social-protection/publications/auto-enrolment-retirement-savings-system-for-employers/)). If the employee opts out or suspends, or is on unpaid leave, the employer contribution stops too.
7. **Local Property Tax:** only where it is shown on the RPN, spread equally over the year ([Deduction of LPT](https://www.revenue.ie/en/employing-people/paying-your-employees-tax-to-revenue/deduction-of-lpt.aspx)). An employee's request alone is not enough.
8. **Net pay:** gross cash pay less employee pension, Income Tax, USC, employee PRSI, auto-enrolment contribution, LPT and voluntary deductions. Notional pay is not cash, so the tax on it comes out of cash pay.

**The tax basis comes from the RPN.** Request the latest RPN before each payroll ([RPN](https://www.revenue.ie/en/employing-people/becoming-an-employer-and-ongoing-obligations/employer-obligations-from-01-01-2019/revenue-payroll-notification.aspx)). Cumulative basis is the norm: cumulative tax is the tax due on total income from 1 January to the current date, and the tax for a pay period is that cumulative tax less the tax already deducted in the year ([Cumulative basis](https://www.revenue.ie/en/employing-people/paying-an-employee/methods-of-calculating-tax/cumulative-basis.aspx)). The RPN also carries the pay, tax and USC already deducted for any ceased employment since 1 January, unless it is on a week 1 or month 1 basis ([RPN](https://www.revenue.ie/en/employing-people/becoming-an-employer-and-ongoing-obligations/employer-obligations-from-01-01-2019/revenue-payroll-notification.aspx)). Use week 1 or month 1 basis only if the RPN says so; it never refunds unused credits ([Week 1 basis](https://www.revenue.ie/en/employing-people/paying-an-employee/methods-of-calculating-tax/week1-basis.aspx)). The emergency basis applies only where no RPN is available ([Emergency basis](https://www.revenue.ie/en/employing-people/paying-an-employee/methods-of-calculating-tax/emergency-basis.aspx)). With a PPSN: standard rate up to the emergency cut-off for weeks 1 to 4 or month 1, no credits, then all pay at 40%. Without a PPSN: all pay at 40% from the first pay day. Emergency USC is 8% on all pay. Emergency weeks count from the date the employee began working for the employer, even in weeks the employee did not work ([Emergency basis](https://www.revenue.ie/en/employing-people/paying-an-employee/methods-of-calculating-tax/emergency-basis.aspx)). Never guess credits; send the employee to myAccount.

**Benefit in kind.** Company car cash equivalent = (Original Market Value, including VAT and VRT, less any reduction for the category) times the percentage for the CO2 category and business kilometres (s.121; Finance Act 2025 s.24). If there are no records of business kilometres, the employer may assume 8,000 km private. A contribution the employee pays directly to the employer toward running costs reduces the cash equivalent. Review notional pay at least quarterly ([Revenue, company cars](https://www.revenue.ie/en/employing-people/benefit-in-kind-for-employers/private-use-company-cars/calculate-value-benefit.aspx)). Small benefits: a single benefit over EUR 1,500 is taxable in full; only the first five benefits in a year qualify; unused allowance does not carry over; a voucher redeemable in cash does not qualify; the employer reports the date and value to Revenue ([Small benefit exemption](https://www.revenue.ie/en/employing-people/benefit-in-kind-for-employers/valuation-of-benefits/small-benefit-exemption.aspx)). Salary sacrifice reduces taxable pay for Income Tax; the pages read do not say it reduces USC or PRSI, so do not assume it does.

**Bonuses and back pay.** Tax a bonus in the period it is paid under the cumulative basis. Do not reopen earlier submissions for back pay without advice.

**Lump sums on leaving.** A termination payment within the basic exemption is tax-free; above it the increased exemption or SCSB may apply (refer). A career break does not count as a full year. For PRSI, lump sums on leaving (redundancy, gratuities, ex-gratia) are not reckonable pay and are recorded under Class M (SW14).

**Minimum wage.** Check gross pay for hours worked against the hourly rates. Gross pay for this test includes basic pay, shift premium, bonus and service charge. Close relatives of a sole trader employer and certain craft apprentices are excluded ([DETE](https://www.gov.ie/en/department-of-enterprise-tourism-and-employment/publications/national-minimum-wage-increase-on-1-january-2025/)).

## Deadlines and filing

| What | When | Source |
|---|---|---|
| Payroll submission to Revenue (pay date, pay, Income Tax, USC, PRSI class and weeks, LPT, start or leaving date) | On or before the day the employee is paid | s.985G; https://www.revenue.ie/en/employing-people/becoming-an-employer-and-ongoing-obligations/employer-obligations-from-01-01-2019/payroll-submissions.aspx |
| Reportable benefits (for example small benefits) on the submission | On or before payment, from 1 January 2024 | s.985G |
| Auto-enrolment contributions to NAERSA | On or before the employee is paid (AE Act s.59) | https://revisedacts.lawreform.ie/eli/2024/act/20/revised/en/html |
| Employer passes NAERSA's enrolment notice to the employee | Within 14 days of receiving it (s.50(7)) | same |
| Revenue monthly statement available | By the 5th of the next month | https://www.revenue.ie/en/employing-people/paying-your-employees-tax-to-revenue/paying-tax-to-revenue.aspx |
| Monthly return | 14th of the next month; a statement not accepted by then is deemed the return | s.983, s.985G(3)(a), (4) |
| Payment, monthly remitter | 14th of the next month; 23rd if return and payment are both made on ROS | s.983; https://www.revenue.ie/en/employing-people/becoming-an-employer-and-ongoing-obligations/employer-obligations-from-01-01-2019/returns-and-payment-due-dates.aspx |
| Payment, quarterly remitter (yearly liability EUR 28,800 or less, registered 12 months, compliant, applied to the Collector-General) | 14 days after the quarter end (23 on ROS); monthly statements still issue | same |
| Payment, annual remitter | 14 days after the year end (23 on ROS) | same |
| December 2026 liability (monthly remitter) | 14 January 2027, or 23 January 2027 on ROS | same |

**Channels.** Direct reporting from payroll software, a ROS file upload, or the ROS "Submit payroll by online form" for employers without software; customised stationery only for employers excluded from electronic filing. Common Irish packages include BrightPay, Sage, Surf Accounts, Thesaurus and CollSoft. The MyFutureFund employer portal uses the employer's ROS credentials, and a variable direct debit is the simplest way to pay ([DSP](https://www.gov.ie/en/department-of-social-protection/publications/auto-enrolment-retirement-savings-system-for-employers/)).

**PRSI on the submission.** Report the class and the weeks in the period paid (one for weekly, two for fortnightly), never a cumulative count. Keep PRSI separate in the books because the Collector-General passes it to the Department of Social Protection. Errors can affect the employee's benefits, so correct them at once ([PRSI for employers](https://www.revenue.ie/en/employing-people/paying-your-employees-tax-to-revenue/prsi.aspx)).

**Corrections.** Fix errors by amending the payroll submission, not the statement. Before the return date a revised statement issues; after it, an amended return ([Statements](https://www.revenue.ie/en/employing-people/becoming-an-employer-and-ongoing-obligations/employer-obligations-from-01-01-2019/statements-from-revenue.aspx)).

**Starters and leavers.** A new employee is registered by an RPN request with the start date. Put the leaving date on the final submission (also for a career break or death in service). A delay can give the next employer a nil RPN and push the employee onto emergency tax ([Commencing and ceasing](https://www.revenue.ie/en/employing-people/becoming-an-employer-and-ongoing-obligations/employer-obligations-from-01-01-2019/commencing-and-ceasing-employees.aspx)). The employee can cease the job in myAccount if the old employer does not. A mid-month joiner or leaver gets actual pay for the days worked.

**Year end.** There is no separate employer year-end return; P30, P35, P45 and P60 belong to the regime before 1 January 2019. Reconcile submissions to the payroll records, the pension provider's records and the ledger; check every leaver has a leaving date, small benefits stayed within the limits, the PRSI rates switched on 1 October 2026, and USC was charged on gross pay. Make the final December submission with final notional pay, and accept or correct the December statement by 14 January. The employee's Employment Detail Summary (EDS) appears in myAccount in January; a later financial change produces a new EDS ([EDS](https://www.revenue.ie/en/jobs-and-pensions/end-of-year-process/employment-detail-summary.aspx)).

**Payslip.** The employer must give a written statement of the gross wages and the nature and amount of every deduction, and keep it confidential (Payment of Wages Act 1991 s.4). For credit transfer it is given as soon as may be after payment; for cash or cheque, at payment. Good practice adds the tax basis, PRSI class and weeks, notional pay, employer PRSI, auto-enrolment contributions and year-to-date totals.

## Penalties and interest

| Failure | Consequence | Source |
|---|---|---|
| Failure to make a return, remit tax, make a deduction or keep a register of employees under the PAYE rules | Penalty EUR 4,000; a body of persons' secretary is liable to a separate EUR 3,000 | s.987(1), (2); https://www.revenue.ie/en/tax-professionals/documents/notes-for-guidance/tca/part42.pdf |
| Late payment of PAYE, USC, PRSI and LPT deducted | Simple interest 0.0274% a day from the due date | s.991; https://www.revenue.ie/en/employing-people/paying-your-employees-tax-to-revenue/paying-tax-to-revenue.aspx |
| Direct debit payments under 90% of the year's actual tax | Direct debit agreement treated as not having effect; each month due on its own due date | s.991A |
| Late auto-enrolment contributions | Interest 0.0274% a day, payable to NAERSA, not tax-deductible | AE Act 2024 s.138 |
| Employer fails to pass on NAERSA's enrolment notice within 14 days | Offence | AE Act 2024 s.50(8) |

Revenue's pages print no separate fixed penalty for a late payroll submission beyond s.987. Refer any penalty question beyond these figures, and refer an employer that has paid late or wants to correct a prior year.

## Cross-border points

- **Work partly abroad.** Where an employee works both in and outside the State and the share of pay taxable in Ireland is not yet known, Revenue may, on the employer's application, direct the proportion on which PAYE is operated. Without a direction, the employer operates PAYE on the whole amount (s.985E). PAYE exclusion orders and other reliefs: refer.
- **Mobile workers.** Revenue may direct a person who uses another firm's workers to pay that firm under deduction of tax where PAYE is unlikely to be operated (s.985F).
- **Social insurance.** Which country's PRSI applies to posted and cross-border workers depends on EU Regulation 883/2004, an A1 certificate or a bilateral agreement: see `ie-prsi-cross-border`.
- **Auto-enrolment and other jobs.** Eligibility counts gross pay from all employments, but contributions are only on the non-exempt employment's pay ([MyFutureFund contributions](https://assets.gov.ie/static/documents/1b66f3e6/MyFutureFundContributions.pdf)).
- **Foreign currency pay.** Convert to euro and record the rate used; refer the choice of rate.
- Residence and the remittance basis: `ie-cross-border`, `ie-non-dom`.

## Worked examples

### Example 1: monthly employee with a pension, October 2026

A single employee aged 32 is paid EUR 5,000 a month in October 2026. The cumulative RPN gives a EUR 44,000 cut-off point and EUR 4,000 of credits. Pay is the same every month, so the cumulative and monthly results match. The employee pays EUR 250 a month (5%) to the employer's approved defined contribution scheme and the employer pays EUR 300 a month (6%), above the 1.5% and 3.5% standards, so the job is exempt from auto-enrolment. The employer's contribution does not enter the employee's pay below.

Taxable pay is 5,000 − 250 = 4,750. Monthly cut-off point 44,000 / 12 = 3,666.67; monthly credits 4,000 / 12 = 333.33. Income Tax = 20% × 3,666.67 + 40% × 1,083.33 − 333.33 = EUR 833.33. USC is on the full EUR 5,000: 0.5% of 1,001 + 2% of 1,390.67 + 3% of 2,608.33 = EUR 111.07. Monthly pay is over EUR 2,392, so subclass A1: employee PRSI 4.35% × 5,000 = EUR 217.50 and employer PRSI 11.40% × 5,000 = EUR 570.00 (rates from 1 October 2026). Net pay = 5,000 − 250 − 833.33 − 111.07 − 217.50 = EUR 3,588.10. Had this month been paid in September 2026, employee PRSI would be EUR 210.00 and employer PRSI EUR 562.50.

```oa-check
name: Single employee, EUR 5,000 a month, EUR 250 pension, paid October 2026
inputs:
  gross: 5000
  pension: 250
steps:
  - taxable: gross - pension
  - cutoff: 44000 / 12
  - credits: 4000 / 12
  - income_tax: round(cutoff * 0.20 + (taxable - cutoff) * 0.40 - credits, 2)
  - usc: round(12012 / 12 * 0.005 + 16688 / 12 * 0.02 + (gross - (12012 + 16688) / 12) * 0.03, 2)
  - ee_prsi: gross * 0.0435
  - er_prsi: gross * 0.114
  - net: gross - pension - income_tax - usc - ee_prsi
expected:
  taxable: 4750
  income_tax: 833.33
  usc: 111.07
  ee_prsi: 217.50
  er_prsi: 570.00
  net: 3588.10
```

### Example 2: weekly part-timer in the PRSI Credit band, auto-enrolled

A single employee aged 25 works 28 hours a week for EUR 400 (EUR 14.29 an hour, above the EUR 14.15 minimum). Yearly pay is EUR 20,800, so NAERSA enrols her and sends an AEPN; the employer has no pension scheme. The week is paid in November 2026, on a cumulative RPN with a EUR 44,000 cut-off and EUR 4,000 credits.

Income Tax: the weekly cut-off is 846.15, so all EUR 400 is at 20% = 80.00, less weekly credits 4,000 / 52 = 76.92, gives EUR 3.08. USC: her income is over EUR 13,000, so USC applies: 0.5% of 231.00 + 2% of 169.00 = EUR 4.54. PRSI: EUR 400 is in subclass AX. The charge is 4.35% × 400 = 17.40, less the PRSI Credit 12 − (400 − 352.01) / 6 = 4.00, so employee PRSI is EUR 13.40. Employer PRSI is 9.15% × 400 = EUR 36.60 (pay is under EUR 552). Auto-enrolment: EUR 6.00 from her pay and EUR 6.00 from the employer, both paid to NAERSA on pay day; the State adds EUR 2.00. Her contribution gets no Income Tax relief. Net pay = 400 − 3.08 − 4.54 − 13.40 − 6.00 = EUR 372.98.

```oa-check
name: Weekly EUR 400, AX band with PRSI Credit, auto-enrolled, paid November 2026
inputs:
  weekly_pay: 400
steps:
  - credits: 4000 / 52
  - income_tax: round(weekly_pay * 0.20 - credits, 2)
  - usc: round(12012 / 52 * 0.005 + (weekly_pay - 12012 / 52) * 0.02, 2)
  - prsi_credit: 12 - (weekly_pay - 352.01) / 6
  - ee_prsi: round(weekly_pay * 0.0435 - prsi_credit, 2)
  - er_prsi: weekly_pay * 0.0915
  - ae_employee: weekly_pay * 0.015
  - ae_employer: weekly_pay * 0.015
  - ae_state: weekly_pay * 0.005
  - net: weekly_pay - income_tax - usc - ee_prsi - ae_employee
expected:
  income_tax: 3.08
  usc: 4.54
  prsi_credit: 4.00
  ee_prsi: 13.40
  er_prsi: 36.60
  ae_employee: 6.00
  ae_employer: 6.00
  ae_state: 2.00
  net: 372.98
```

## Ask the client first

1. **RPNs and PPSNs.** Is there a current RPN for every employee, and on what basis (cumulative, week 1 or month 1, emergency)? Does anyone lack a PPSN?
2. **Pay frequency and dates.** Weekly, fortnightly or monthly, and the exact pay dates? Did any pay period straddle 1 October 2026?
3. **Who is not ordinary Class A.** Anyone under 16, 66 or over, public sector, a proprietary director, on Community Employment, or posted from or to another country?
4. **Pensions and auto-enrolment.** Which employees pay into a scheme, PRSA, RAC or PEPP through payroll, with ages and yearly pay? What do employer and employee each pay into those schemes, so we can test them against the 1.5% / 3.5% standards? Has NAERSA sent any AEPNs, and is the MyFutureFund direct debit set up?
5. **Benefits.** Company cars (OMV, CO2, electric or not, business kilometres, any contribution paid to you), vouchers and other non-cash benefits, and how many small benefits so far this year?
6. **Remitting and arrears.** Monthly, quarterly or annual remitter, filing and paying on ROS? Any late payments, attachment orders or past errors to correct?

## Sources

| Source | URL | Read on |
|---|---|---|
| Revenue, Notes for Guidance, TCA 1997 Part 42 (Finance Act 2025 edition): ss.983, 985, 985A, 985E, 985F, 985G, 987, 991, 991A | https://www.revenue.ie/en/tax-professionals/documents/notes-for-guidance/tca/part42.pdf | 2026-10-24 |
| Finance Act 2025 s.2 (USC bands, s.531AN) | https://www.irishstatutebook.ie/eli/2025/act/18/section/2/enacted/en/html | 2026-10-24 |
| Finance Act 2025 s.16 (new TCA Chapter 2E, s.787AF employer AE contributions) | https://www.irishstatutebook.ie/eli/2025/act/18/section/16/enacted/en/html | 2026-10-24 |
| Finance Act 2025 s.24 (car BIK, s.121: category A1, tables, OMV reductions to 2028) | https://www.irishstatutebook.ie/eli/2025/act/18/section/24/enacted/en/html | 2026-10-24 |
| Social Welfare Consolidation Act 2005, revised to 1 October 2026, s.13 | https://revisedacts.lawreform.ie/eli/2005/act/26/revised/en/html | 2026-10-24 |
| Social Welfare (Miscellaneous Provisions) Act 2024 (No. 24 of 2024), s.3 and Table (PRSI steps 2024 to 2028) | https://www.irishstatutebook.ie/pdf/2024/en.act.2024.0024.pdf | 2026-10-24 |
| Social Welfare and Automatic Enrolment Retirement Savings System (Amendment) Act 2025 (No. 19 of 2025), s.2 (EUR 552 from 1 January 2026) | https://www.irishstatutebook.ie/pdf/2025/en.act.2025.0019.pdf | 2026-10-24 |
| National Training Fund Act 2000, revised to 19 January 2026, s.4 | https://revisedacts.lawreform.ie/eli/2000/act/41/revised/en/html | 2026-10-24 |
| Automatic Enrolment Retirement Savings System Act 2024, revised to 1 June 2026: ss.1, 2, 47, 50, 51, 52, 53, 54, 58, 59, 61, 138 | https://revisedacts.lawreform.ie/eli/2024/act/20/revised/en/html | 2026-10-24 |
| S.I. No. 668 of 2025, Automatic Enrolment Retirement Savings System Regulations (Amendment) (Section 52) Regulations 2025 (minimum standards for exempt employment from 1 January 2026) | https://www.irishstatutebook.ie/eli/2025/si/668/made/en/print | 2026-10-24 |
| Payment of Wages Act 1991 s.4 | https://www.irishstatutebook.ie/eli/1991/act/25/section/4/enacted/en/html | 2026-10-24 |
| Revenue, tax rates, bands and reliefs | https://www.revenue.ie/en/personal-tax-credits-reliefs-and-exemptions/tax-relief-charts/index.aspx | 2026-10-24 |
| Revenue, USC standard rates (also the USC overview and reduced rates pages) | https://www.revenue.ie/en/jobs-and-pensions/usc/standard-rates-thresholds.aspx | 2026-10-24 |
| Revenue, Emergency Basis of Tax and USC Deduction 2026 | https://www.revenue.ie/en/jobs-and-pensions/documents/emergency-rates.pdf | 2026-10-24 |
| Revenue, RPN (also cumulative, week 1 and emergency basis pages) | https://www.revenue.ie/en/employing-people/becoming-an-employer-and-ongoing-obligations/employer-obligations-from-01-01-2019/revenue-payroll-notification.aspx | 2026-10-24 |
| Revenue, gross and taxable pay (also employee pension contributions and pension relief limits) | https://www.revenue.ie/en/employing-people/what-constitutes-pay/what-are-gross-and-taxable-pay/index.aspx | 2026-10-24 |
| Revenue, return and payment due dates (also payroll submissions, commencing and ceasing, statements, paying tax, PRSI for employers, LPT) | https://www.revenue.ie/en/employing-people/becoming-an-employer-and-ongoing-obligations/employer-obligations-from-01-01-2019/returns-and-payment-due-dates.aspx | 2026-10-24 |
| Revenue, Tax and Duty Manual Part 05-01-01b, employer provided vehicles (OMV reductions 2023 to 2028, electric cars) | https://www.revenue.ie/en/tax-professionals/tdm/income-tax-capital-gains-tax-corporation-tax/part-05/05-01-01b.pdf | 2026-10-24 |
| Revenue, company car BIK (also small benefit exemption, termination basic exemption, EDS) | https://www.revenue.ie/en/employing-people/benefit-in-kind-for-employers/private-use-company-cars/calculate-value-benefit.aspx | 2026-10-24 |
| DSP, PRSI Class A rates (both 2026 periods) | https://www.gov.ie/en/department-of-social-protection/publications/prsi-class-a-rates/ | 2026-10-24 |
| DSP, SW14 PRSI Contribution Rates and User Guide, January 2026 | https://assets.gov.ie/static/documents/cb168977/PRSI_C20260116_Contribution_Rates_and_User_Guide_-_SW_14_-_English_Version_-_January_2026_.pdf-web.pdf | 2026-10-24 |
| DSP, auto-enrolment for employers (also the MyFutureFund contributions examples) | https://www.gov.ie/en/department-of-social-protection/publications/auto-enrolment-retirement-savings-system-for-employers/ | 2026-10-24 |
| DETE, national minimum wage from 1 January 2026 | https://www.gov.ie/en/department-of-enterprise-tourism-and-employment/publications/national-minimum-wage-increase-on-1-january-2025/ | 2026-10-24 |

Not yet confirmed: (1) whether the pay date or the week worked decides the PRSI rate for a pay period that straddles 1 October 2026; (2) the DSP MyFutureFund examples say contributions are taken on the whole pay of the month in which yearly pay passes EUR 80,000, while AE Act s.58(3) says no contribution on the part above EUR 80,000, so follow the AEPN; (3) how salary sacrifice affects USC and PRSI; (4) the Income Tax, USC and PRSI treatment of the employee auto-enrolment contribution rests on the DSP page (no tax relief), not on a TCA section; (5) which car BIK category to use while a car's CO2 figure is unknown (no Revenue page read states a default); (6) Illness Benefit and other DSP payments through payroll follow the RPN and are not covered here; (7) Budget 2027 (6 October 2026) and Finance Bill 2026 changes for 2027 were not read; (8) an employee with more than one employment with the same employer: the earlier version said to follow the RPN for each employment and refer if the RPNs look inconsistent, but no Revenue page read for this skill states that rule. Note: the Law Reform Commission revised s.13(2)(d) still prints EUR 527 in the text, but its own annotations F115 and F117 record the substitution of EUR 552 from 1 January 2026 by Act 19 of 2025 s.2, which this skill follows.

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

## Today's figures and who stands behind this skill

This file is an AI skill (tax rules your AI follows) from OpenAccountants, copied on 2026-10-27. Rates, thresholds and deadlines change. For the current version of this skill, its official sources and the named accountant (if any) who stands behind it, call `get_skill` with slug `ie-payroll` on the OpenAccountants connector (https://www.openaccountants.com/connect), or read https://www.openaccountants.com/skills/ie-payroll. If neither is available, confirm every figure against the official source pages cited above before relying on it.
