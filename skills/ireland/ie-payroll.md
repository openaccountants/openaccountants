---
name: ie-payroll
description: "Irish employer payroll for tax year 2026: PAYE and USC under the Revenue Payroll Notification, PRSI Class A across the October rate change, pensions, company-car benefit in kind, minimum wage, MyFutureFund auto-enrolment, payroll submissions, remittances, corrections and year-end reconciliation. Trigger on Irish payroll, gross to net Ireland, RPN, emergency tax, payslip, BIK Ireland, auto-enrolment or MyFutureFund."
version: 0.4
jurisdiction: IE
tax_year: 2026
last_updated: 2026-11-27
category: international
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
tier: 2
domain: payroll
type: computation
---

# Ireland payroll: PAYE, USC, PRSI and auto-enrolment, tax year 2026 (v0.4)

> **Built from the law · Not yet approved.** Ordinary employee payroll, in euro, for 2026. Obtain the latest RPN and, where applicable, AEPN before computing pay. The holds below are not payroll instructions.

See also: `ie-usc` (USC rules in depth, reduced rates, exempt income), `ie-prsi-class-s` (PRSI for the self-employed), `ie-prsi-cross-border` (posted workers, A1 certificates, bilateral agreements), `ie-income-tax-form11` (proprietary directors and others who file Form 11), `ie-paye-rental-nonresident` (PAYE workers with side income), `ie-cross-border` (residence).

## Who this applies to

- **Employers** that pay emoluments to employees in Ireland. The employer deducts Income Tax, USC and employee PRSI under the PAYE system and pays them over with employer PRSI (s.985, s.985G; Social Welfare Consolidation Act 2005 s.13). The employer stays responsible when it uses software, a payroll bureau, an agency or ROS ([Payroll submissions](https://www.revenue.ie/en/employing-people/becoming-an-employer-and-ongoing-obligations/employer-obligations-from-01-01-2019/payroll-submissions.aspx)).
- **PRSI Class A** covers employees aged 16 to under 66 (or born on or after 1 January 1958, aged 66 to under 70, and not awarded a State Pension (Contributory)) in industrial, commercial and service-type employment under a contract of service with reckonable pay of EUR 38 or more a week from all employments, and civil and public servants recruited from 6 April 1995 ([DSP, PRSI Class A rates](https://assets.gov.ie/static/documents/cb168977/PRSI_C20260116_Contribution_Rates_and_User_Guide_-_SW_14_-_English_Version_-_January_2026_.pdf-web.pdf)).
- **Auto-enrolment** applies from 1 January 2026 to employees aged at least 23 and under 60, with gross pay across all employments at least EUR 20,000 for a yearly pay reference period (proportionately adjusted for a shorter or longer period), in an employment that is not exempt. An employment is exempt where the employee or the employer pays into a qualifying occupational pension scheme, PRSA, trust RAC or PEPP through payroll (AE Act 2024 ss.50, 51; [DSP, auto-enrolment for employers](https://www.gov.ie/en/department-of-social-protection/publications/auto-enrolment-retirement-savings-system-for-employers/)). From 1 January 2026 a defined contribution occupational scheme or a PRSA qualifies only if the employer pays at least the lower of 1.5% of gross pay or EUR 1,200 a year, and employer plus employee together pay at least the lower of 3.5% of gross pay or EUR 2,800 a year (the PRSA combined-pay test is retrospective over preceding months, pro rata for shorter service); a defined benefit scheme qualifies if continuing service accrues a long service benefit (s.52; S.I. No. 668 of 2025, inserting Schedule 1A into S.I. No. 637 of 2025). An employee-only contribution to a defined contribution scheme or PRSA does not make the job exempt. NAERSA decides who is enrolled, not the employer. An employee aged 18 or over and under pensionable age in a non-exempt employment can opt in (s.53). The first opt-out window is more than 6 but not more than 8 months after the employer gives notice of enrolment to the employee, not after the enrolment date; s.54 also provides windows after notice of re-enrolment and after each scheduled contribution-rate step. Use the dates assigned by NAERSA. An opt-out or suspension stops employer contributions too (ss.57–59).
- **Out of scope here; refer:** public sector PRSI classes (B, C, D) and Classes H, J, K, M and Community Employment; proprietary directors (their PRSI class may not be Class A); share schemes and share-based pay; pension lump sums; termination settlements; backdated pay covering more than one tax year; Insolvency and Redundancy Payments Scheme claims; attachment of earnings orders beyond applying the order as written.

## Rates, bands and thresholds

| Item | Rate or amount | Year | Source |
|---|---|---|---|
| Income Tax standard rate / higher rate | 20% / 40% | 2026 | https://www.revenue.ie/en/personal-tax-credits-reliefs-and-exemptions/tax-relief-charts/index.aspx |
| Standard rate cut-off point: single, widowed or surviving civil partner, no qualifying children | EUR 44,000 | 2026 | https://www.revenue.ie/en/personal-tax-credits-reliefs-and-exemptions/tax-relief-charts/index.aspx |
| Cut-off point: single person qualifying for the Single Person Child Carer Credit | EUR 48,000 | 2026 | https://www.revenue.ie/en/personal-tax-credits-reliefs-and-exemptions/tax-relief-charts/index.aspx |
| Cut-off point: married or civil partners, one income | EUR 53,000 | 2026 | https://www.revenue.ie/en/personal-tax-credits-reliefs-and-exemptions/tax-relief-charts/index.aspx |
| Cut-off point: married or civil partners, two incomes | EUR 53,000 plus the lower of EUR 35,000 or the lower earner's income; increase not transferable between partners | 2026 | https://www.revenue.ie/en/personal-tax-credits-reliefs-and-exemptions/tax-relief-charts/index.aspx |
| Single Person Tax Credit / Married or Civil Partner Tax Credit | EUR 2,000 / EUR 4,000 | 2026 | https://www.revenue.ie/en/personal-tax-credits-reliefs-and-exemptions/tax-relief-charts/index.aspx |
| Employee (PAYE) Tax Credit | EUR 2,000 | 2026 | https://www.revenue.ie/en/personal-tax-credits-reliefs-and-exemptions/tax-relief-charts/index.aspx |
| USC bands (standard) | 0.5% on first EUR 12,012; 2% on next EUR 16,688; 3% on next EUR 41,344; 8% on the balance | 2026 | https://www.irishstatutebook.ie/eli/2025/act/18/section/2/enacted/en/html |
| USC exemption: total income at or below | EUR 13,000 (above it, USC on all income) | 2026 | https://www.revenue.ie/en/jobs-and-pensions/usc/index.aspx |
| USC reduced rates (aged 70+ or full Medical Card, income EUR 60,000 or less) | 0.5% on first EUR 12,012, 2% on the balance | 2026 | https://www.revenue.ie/en/jobs-and-pensions/usc/reduced-rates.aspx |
| Emergency basis, PPSN given: cut-off point weeks 1 to 4 / month 1; nil after | EUR 846.16 a week / EUR 3,666.67 a month; tax credit nil | 2026 | https://www.revenue.ie/en/jobs-and-pensions/documents/emergency-rates.pdf |
| Emergency USC | 8% on all pay, no cut-off | 2026 | https://www.revenue.ie/en/jobs-and-pensions/documents/emergency-rates.pdf |
| PRSI Class A employee rate, weekly pay over EUR 352 | 4.2% to 30 Sep 2026; 4.35% from 1 Oct 2026 | 2026 | https://www.irishstatutebook.ie/eli/2024/act/24/section/3/enacted/en/html |
| PRSI Class A, weekly pay EUR 38 to EUR 352 (subclass A0) | employee nil | 2026 | https://assets.gov.ie/static/documents/cb168977/PRSI_C20260116_Contribution_Rates_and_User_Guide_-_SW_14_-_English_Version_-_January_2026_.pdf-web.pdf |
| PRSI Credit (subclass AX, EUR 352.01 to EUR 424 a week) | EUR 12 less one sixth of pay over EUR 352.01 | 2026 | https://assets.gov.ie/static/documents/cb168977/PRSI_C20260116_Contribution_Rates_and_User_Guide_-_SW_14_-_English_Version_-_January_2026_.pdf-web.pdf |
| Employer PRSI, weekly pay up to EUR 552 / over EUR 552 (whole week's pay) | 9% / 11.25% to 30 Sep 2026; 9.15% / 11.40% from 1 Oct 2026 | 2026 | https://assets.gov.ie/static/documents/cb168977/PRSI_C20260116_Contribution_Rates_and_User_Guide_-_SW_14_-_English_Version_-_January_2026_.pdf-web.pdf |
| Employer threshold for the higher rate (s.13(2)(d)) | EUR 552 a week from 1 Jan 2026 (was EUR 527; Act 19 of 2025 s.2, in operation 1 January 2026) | 2026 | https://www.irishstatutebook.ie/eli/2025/act/19/section/2/enacted/en/html |
| Monthly PRSI bands (A0 / AX / AL / A1) | EUR 165 to 1,525 / EUR 1,525.01 to 1,837 / EUR 1,837.01 to 2,392 / over EUR 2,392 (Class A lower threshold requires at least EUR 38 in each week) | 2026 | https://assets.gov.ie/static/documents/cb168977/PRSI_C20260116_Contribution_Rates_and_User_Guide_-_SW_14_-_English_Version_-_January_2026_.pdf-web.pdf |
| National minimum wage, aged 20+ / 19 / 18 / under 18 | EUR 14.15 / 12.74 / 11.32 / 9.91 an hour from 1 Jan 2026 | 2026 | https://www.workplacerelations.ie/media/334fojsq/national-minimum-wage-poster.pdf |
| Minimum wage: board / lodgings that may count as pay | EUR 1.27 an hour worked / EUR 33.42 a week or EUR 4.77 a day | 2026 | https://www.irishstatutebook.ie/eli/2025/si/472/made/en/print |
| Auto-enrolment: employee and employer contribution each, on gross pay | 1.5% in years 1 to 3 (from 1 Jan 2026), 3% years 4 to 6, 4.5% years 7 to 9, 6% after | 2026 | https://revisedacts.lawreform.ie/eli/2024/act/20/revised/en/html |
| Auto-enrolment: State contribution | 0.5% in years 1 to 3 | 2026 | https://revisedacts.lawreform.ie/eli/2024/act/20/revised/en/html |
| Auto-enrolment: earnings cap / entry threshold | no contribution on the part exceeding EUR 80,000 across non-exempt employments in the financial year (s.58(3)); EUR 20,000 yearly entry test, proportionately adjusted to NAERSA’s pay reference period (s.50(3)) | 2026 | https://revisedacts.lawreform.ie/eli/2024/act/20/revised/en/html |
| Minimum standards for an existing scheme to make the job exempt (DC scheme or PRSA) | employer at least the lower of 1.5% of gross pay or EUR 1,200 a year; employer and employee together at least the lower of 3.5% or EUR 2,800 a year (PRSA: retrospective preceding months/pro rata shorter service) | from 1 Jan 2026 | https://www.irishstatutebook.ie/eli/2025/si/668/made/en/print |
| Pension relief, % of earnings by age | under 30: 15%; 30-39: 20%; 40-49: 25%; 50-54: 30%; 55-59: 35%; 60+: 40% | 2026 | https://www.revenue.ie/en/jobs-and-pensions/pension/relief/tax-relief-limits.aspx |
| Pension relief earnings limit | EUR 115,000 a year | 2026 | https://www.revenue.ie/en/jobs-and-pensions/pension/relief/tax-relief-limits.aspx |
| Company car BIK: % of Original Market Value, 0 to 26,000 business km, categories A1 / A / B / C / D / E | 15% / 22.5% / 26.25% / 30% / 33.75% / 37.5% | 2026 | https://www.irishstatutebook.ie/eli/2025/act/18/section/24/enacted/en/html |
| Car BIK, 26,001–39,000 business km, categories A1 / A / B / C / D / E | 12% / 18% / 21% / 24% / 27% / 30% | 2026 | https://www.irishstatutebook.ie/eli/2025/act/18/section/24/enacted/en/html |
| Car BIK, 39,001–48,000 business km, same category order | 9% / 13.5% / 15.75% / 18% / 20.25% / 22.5% | 2026 | https://www.irishstatutebook.ie/eli/2025/act/18/section/24/enacted/en/html |
| Car BIK, 48,001 business km and above, same category order | 6% / 9% / 10.5% / 12% / 13.5% / 15% | 2026 | https://www.irishstatutebook.ie/eli/2025/act/18/section/24/enacted/en/html |
| Car CO2 categories (g/km): A1 / A / B / C / D / E | 0 / over 0 to 59 / over 59 to 99 / over 99 to 139 / over 139 to 179 / over 179 | 2026 | https://www.irishstatutebook.ie/eli/2025/act/18/section/24/enacted/en/html |
| Car OMV reduction, categories A1 to D (not E) | EUR 10,000 for 2023 to 2026; EUR 5,000 for 2027; EUR 2,500 for 2028 | 2026 | https://www.irishstatutebook.ie/eli/2025/act/18/section/24/enacted/en/html |
| Extra OMV reduction for an electricity-only car (not a hybrid), on top of the reduction above | EUR 20,000 in 2026 (computed total: EUR 30,000); EUR 10,000 in 2027 (computed total: EUR 15,000); none in 2028 | 2026 | https://www.revenue.ie/en/employing-people/benefit-in-kind-for-employers/private-use-company-cars/exemptions.aspx |
| Small benefit exemption | up to 5 non-cash benefits a year, combined EUR 1,500 | 2026 | https://www.revenue.ie/en/employing-people/benefit-in-kind-for-employers/valuation-of-benefits/small-benefit-exemption.aspx |
| Quarterly remitting allowed if yearly Income Tax, PRSI and USC are | EUR 28,800 or less | 2026 | https://www.revenue.ie/en/employing-people/paying-your-employees-tax-to-revenue/paying-tax-to-revenue.aspx |

The employer does not choose cut-off points or credits. The RPN gives each employee's yearly figures and the employer divides them by 52, 26 or 12 ([Cumulative basis](https://www.revenue.ie/en/employing-people/paying-an-employee/methods-of-calculating-tax/cumulative-basis.aspx)). Use the table to sense-check an RPN. The USC exemption and reduced rates also come through the RPN; do not apply them yourself.

**PRSI bands are cliffs.** Once weekly pay is over EUR 552 (monthly over EUR 2,392), the employer higher rate applies to the whole week's pay, not only the excess. The employee rate also applies to the whole week's pay once pay is over EUR 352, less the AX credit where applicable.

## The taxable base

**Order of the payroll:**

1. **Gross pay:** basic, overtime, commission, bonus, taxable cash allowances, plus notional pay (benefit in kind). Gross pay is pay before any pension or salary sacrifice deduction ([Gross and taxable pay](https://www.revenue.ie/en/employing-people/what-constitutes-pay/what-are-gross-and-taxable-pay/index.aspx)).
2. **Taxable pay for Income Tax:** gross pay less qualifying employee contributions to a Revenue-approved pension scheme, PRSA, RAC or PEPP deducted by the employer (same page). For RAC net-pay relief there must be no occupational pension scheme; with an occupational scheme, apply tax before deducting the RAC premium. Approved income-continuance deductions require their separate relief conditions; hold that calculation here. Check this point with one of our partner accountants. Salary sacrifice is held below; do not apply a general deduction for sacrificed salary. Pension relief is capped at the age percentage and the EUR 115,000 earnings limit, and relates to the income source in respect of which the contribution is made; contributions above the limits, or to a scheme not shown to be approved, go through Income Tax. Employer contributions do not count toward the employee's limit. The employee's total contributions for the limit include ordinary contributions, Additional Voluntary Contributions (AVCs) and special contributions ([Employee's pension contributions](https://www.revenue.ie/en/employing-people/what-constitutes-pay/employees-pension-payments/index.aspx)).
3. **Income Tax:** 20% up to the period cut-off point, 40% on the balance, less the period tax credits (s.985; [Rule for calculating tax](https://www.revenue.ie/en/employing-people/paying-an-employee/methods-of-calculating-tax/calculating-tax-rules.aspx)).
4. **USC on gross pay.** Employee pension contributions are not deducted: "There is no relief from USC for employee pension contributions" ([USC](https://www.revenue.ie/en/jobs-and-pensions/usc/index.aspx), [Employee's pension contributions](https://www.revenue.ie/en/employing-people/what-constitutes-pay/employees-pension-payments/index.aspx)). Rules in depth: `ie-usc`.
5. **PRSI on reckonable pay**, which includes notional pay (s.13(2)(e)). For private sector employees PRSI is "fully chargeable" on superannuation and PRSA contributions (SW14). Employer PRSI is not charged on share-based remuneration ([DSP](https://assets.gov.ie/static/documents/cb168977/PRSI_C20260116_Contribution_Rates_and_User_Guide_-_SW_14_-_English_Version_-_January_2026_.pdf-web.pdf)).
6. **Auto-enrolment:** where NAERSA has sent an Automatic Enrolment Payroll Notification (AEPN), deduct the participant contribution from pay and pay it, with the matching employer contribution, to NAERSA on or before the pay day (AE Act s.59). Contributions are on gross pay, subject to the aggregate non-exempt-employment cap in s.58(3). Do not charge on the part crossing EUR 80,000 merely because a summary example charges the whole crossing month. If an AEPN conflicts with the statutory cap, hold that calculation for NAERSA clarification; do not override the law. Check this point with one of our partner accountants. Gross pay is the amount reported as gross pay on the payroll submission (s.47(2)), which includes notional pay; DSP: "anything included in the gross pay field of a payroll file will be assessable." The employee contribution is taken after tax; do not deduct it as an ordinary pension contribution. The State provides a top-up instead of employee tax relief. Employer contributions actually paid are deductible in the payment period, limited to contributions for employees in the employer’s taxable trade or undertaking (TCA s.787AF(2)–(3), inserted by [Finance Act 2025 s.16](https://www.irishstatutebook.ie/eli/2025/act/18/section/16/enacted/en/html)) and are not a benefit in kind for the employee ([DSP, auto-enrolment for employers](https://www.gov.ie/en/department-of-social-protection/publications/auto-enrolment-retirement-savings-system-for-employers/)). If the employee opts out or suspends, or is on unpaid leave, the employer contribution stops too.
7. **Local Property Tax:** only where it is shown on the RPN, spread equally over the year ([Deduction of LPT](https://www.revenue.ie/en/employing-people/paying-your-employees-tax-to-revenue/deduction-of-lpt.aspx)). An employee's request alone is not enough.
8. **Net pay:** gross cash pay less employee pension, Income Tax, USC, employee PRSI, auto-enrolment contribution, LPT and voluntary deductions. Notional pay is not cash, so the tax on it comes out of cash pay.

**The tax basis comes from the RPN.** Request the latest RPN before each payroll ([RPN](https://www.revenue.ie/en/employing-people/becoming-an-employer-and-ongoing-obligations/employer-obligations-from-01-01-2019/revenue-payroll-notification.aspx)). Cumulative basis is the norm: cumulative tax is the tax due on total income from 1 January to the current date, and the tax for a pay period is that cumulative tax less the tax already deducted in the year ([Cumulative basis](https://www.revenue.ie/en/employing-people/paying-an-employee/methods-of-calculating-tax/cumulative-basis.aspx)). The RPN also carries the pay, tax and USC already deducted for any ceased employment since 1 January, unless it is on a week 1 or month 1 basis ([RPN](https://www.revenue.ie/en/employing-people/becoming-an-employer-and-ongoing-obligations/employer-obligations-from-01-01-2019/revenue-payroll-notification.aspx)). Use week 1 or month 1 basis only if the RPN says so; it never refunds unused credits ([Week 1 basis](https://www.revenue.ie/en/employing-people/paying-an-employee/methods-of-calculating-tax/week1-basis.aspx)). The emergency basis applies only where no RPN is available ([Emergency basis](https://www.revenue.ie/en/employing-people/paying-an-employee/methods-of-calculating-tax/emergency-basis.aspx)). With a PPSN: standard rate up to the emergency cut-off for weeks 1 to 4 or month 1, no credits, then all pay at 40%. Without a PPSN: all pay at 40% from the first pay day. Emergency USC is 8% on all pay. Emergency weeks count from the date the employee began working for the employer, even in weeks the employee did not work ([Emergency basis](https://www.revenue.ie/en/employing-people/paying-an-employee/methods-of-calculating-tax/emergency-basis.aspx)). Never guess credits; send the employee to myAccount.

**Benefit in kind.** For an ordinary car available for the full year, with no employee purchase contribution or special exemption, company car cash equivalent = (Original Market Value, including VAT and VRT, less any reduction for the category) times the percentage for the CO2 category and business kilometres (s.121; Finance Act 2025 s.24). Where there are no documents proving business or private kilometres, Revenue permits an assumption of 8,000 private km; this does not establish missing total mileage or CO2 data. A contribution the employee pays directly to the employer toward running costs reduces the cash equivalent. Review notional pay at least quarterly ([Revenue, company cars](https://www.revenue.ie/en/employing-people/benefit-in-kind-for-employers/private-use-company-cars/calculate-value-benefit.aspx)). Small benefits must not be provided through salary sacrifice ([TDM 05-01-01e](https://www.revenue.ie/en/tax-professionals/tdm/income-tax-capital-gains-tax-corporation-tax/part-05/05-01-01e.pdf)). A single benefit over EUR 1,500 is taxable in full; only the first five benefits in a year qualify; unused allowance does not carry over; a voucher redeemable in cash does not qualify; the employer reports the date and value to Revenue ([Small benefit exemption](https://www.revenue.ie/en/employing-people/benefit-in-kind-for-employers/valuation-of-benefits/small-benefit-exemption.aspx)). Salary sacrifice, including Cycle-to-Work and TaxSaver: non-usable hold on the scheme conditions and tax/USC/PRSI treatment. Check this point with one of our partner accountants.

**Bonuses and back pay.** Tax a bonus in the period it is paid under the cumulative basis. Do not reopen earlier submissions for back pay without advice.

**Lump sums on leaving; non-usable hold.** Preserve the former basic-exemption inputs (EUR 10,160 plus EUR 765 per full service year, lifetime EUR 200,000), but do not apply them to contractual pay, notice pay or a termination settlement without determining its character. Increased exemption, SCSB, service/career-break counting, PRSI Class M and pension lump sums are referred together. Check this point with one of our partner accountants.

**Minimum wage.** Check reckonable pay and hours, rather than treating every gross-pay item as qualifying. WRC includes basic pay, shift premium and piece/incentive rates, but excludes overtime/weekend/public-holiday premiums, tips and benefits in kind. Registered apprentices and close relatives of the employer are excluded; a sectoral order may require higher pay ([WRC](https://www.workplacerelations.ie/media/334fojsq/national-minimum-wage-poster.pdf)).

## Deadlines and filing

| What | When | Source |
|---|---|---|
| Payroll submission to Revenue (pay date, pay, Income Tax, USC, PRSI class and weeks, LPT, start or leaving date) | On or before the day the employee is paid | s.985G; https://www.revenue.ie/en/employing-people/becoming-an-employer-and-ongoing-obligations/employer-obligations-from-01-01-2019/payroll-submissions.aspx |
| Small benefits: report date and value under Enhanced Reporting Requirements (ERR) | On or before payment, from 1 January 2024; use the ERR submission in ROS | TCA s.897C; https://www.revenue.ie/en/employing-people/becoming-an-employer-and-ongoing-obligations/err-jan-2024/index.aspx |
| Auto-enrolment contributions to NAERSA | On or before the employee is paid (AE Act s.59) | https://revisedacts.lawreform.ie/eli/2024/act/20/revised/en/html |
| Employer passes NAERSA's enrolment notice to the employee | As soon as possible, no later than 14 days after receiving it (s.50(7)) | https://revisedacts.lawreform.ie/eli/2024/act/20/revised/en/html |
| Revenue monthly statement available | By the 5th of the next month | https://www.revenue.ie/en/employing-people/paying-your-employees-tax-to-revenue/paying-tax-to-revenue.aspx |
| Monthly return | 14th of the next month; a statement not accepted by then is deemed the return | s.983, s.985G; https://www.revenue.ie/en/employing-people/becoming-an-employer-and-ongoing-obligations/employer-obligations-from-01-01-2019/returns-and-payment-due-dates.aspx |
| Payment, monthly remitter | 14th of the next month; 23rd if return and payment are both made on ROS | s.983; https://www.revenue.ie/en/employing-people/becoming-an-employer-and-ongoing-obligations/employer-obligations-from-01-01-2019/returns-and-payment-due-dates.aspx |
| Payment, quarterly remitter (yearly liability EUR 28,800 or less, registered 12 months, compliant, applied to the Collector-General) | 14 days after the quarter end (23 on ROS); monthly statements still issue | https://www.revenue.ie/en/employing-people/paying-your-employees-tax-to-revenue/paying-tax-to-revenue.aspx |
| Payment, annual remitter | 14 days after the year end (23 on ROS) | https://www.revenue.ie/en/employing-people/becoming-an-employer-and-ongoing-obligations/employer-obligations-from-01-01-2019/returns-and-payment-due-dates.aspx |
| December 2026 liability (monthly remitter) | 14 January 2027, or 23 January 2027 on ROS | https://www.revenue.ie/en/employing-people/becoming-an-employer-and-ongoing-obligations/employer-obligations-from-01-01-2019/returns-and-payment-due-dates.aspx |

**Channels.** Direct reporting from payroll software, a ROS file upload, or the ROS "Submit payroll by online form" for employers without software; customised stationery only for employers excluded from electronic filing. The MyFutureFund employer portal uses the employer's ROS credentials, and a variable direct debit is the simplest way to pay ([DSP](https://www.gov.ie/en/department-of-social-protection/publications/auto-enrolment-retirement-savings-system-for-employers/)).

**PRSI on the submission.** Report the class and the weeks in the period paid (one for weekly, two for fortnightly), never a cumulative count. Keep PRSI separate in the books because the Collector-General passes it to the Department of Social Protection. Errors can affect the employee's benefits, so correct them at once ([PRSI for employers](https://www.revenue.ie/en/employing-people/paying-your-employees-tax-to-revenue/prsi.aspx)).

**Corrections.** Fix errors by amending the payroll submission, not the statement. Before the return date a revised statement issues; after it, an amended return ([Statements](https://www.revenue.ie/en/employing-people/becoming-an-employer-and-ongoing-obligations/employer-obligations-from-01-01-2019/statements-from-revenue.aspx)).

**Starters and leavers.** Register a new employee by an RPN request with the correct start date; for a first job in Ireland, the employee first registers the employment in myAccount. Put the leaving date on the final submission (also for a career break or death in service). A delay can give the next employer a nil RPN and push the employee onto emergency tax ([Commencing and ceasing](https://www.revenue.ie/en/employing-people/becoming-an-employer-and-ongoing-obligations/employer-obligations-from-01-01-2019/commencing-and-ceasing-employees.aspx)). For a mid-month joiner or leaver, establish the actual contractual pay before applying the RPN; do not substitute a full month’s pay.

**Year end.** There is no separate employer year-end return; P30, P35, P45 and P60 belong to the regime before 1 January 2019. Reconcile submissions to the payroll records, the pension provider's records and the ledger; check every leaver has a leaving date, small benefits stayed within the limits, the PRSI rates switched on 1 October 2026, and USC was charged on gross pay. Make the final December submission with final notional pay, and accept or correct the December statement by 14 January. The employee's Employment Detail Summary (EDS) appears in myAccount in January; a later financial change produces a new EDS ([EDS](https://www.revenue.ie/en/jobs-and-pensions/end-of-year-process/employment-detail-summary.aspx)).

**Payslip.** The employer must give a written statement of the gross wages and the nature and amount of every deduction, and keep it confidential (Payment of Wages Act 1991 s.4). For credit transfer it is given as soon as may be after payment; for cash or cheque, at payment. Good practice adds the tax basis, PRSI class and weeks, notional pay, employer PRSI, auto-enrolment contributions and year-to-date totals.

## Penalties and interest

| Failure | Consequence | Source |
|---|---|---|
| Failure to make a return, remit tax, make a deduction or keep a register of employees under the PAYE rules | Penalty EUR 4,000; a body of persons' secretary is liable to a separate EUR 3,000 | s.987(1), (2); https://www.revenue.ie/en/tax-professionals/documents/notes-for-guidance/tca/part42.pdf |
| Late payment of PAYE, USC, PRSI and LPT deducted | Simple interest 0.0274% per day or part-day; if paid after the ROS 23rd-day limit, interest runs from the 14th because the electronic extension conditions were not met | ss.983, 991; https://www.revenue.ie/en/tax-professionals/documents/notes-for-guidance/tca/part42.pdf |
| Estimated-payment direct debit agreement under s.991A pays less than 90% of actual annual tax | Agreement treated as not having effect; each month due on its own due date. Do not apply this estimate rule as a description of Revenue’s exact-liability Variable Direct Debit scheme | s.991A; https://www.revenue.ie/en/tax-professionals/documents/notes-for-guidance/tca/part42.pdf |
| Late auto-enrolment contributions | Interest 0.0274% per day or part-day, payable to NAERSA, not tax-deductible | AE Act 2024 s.138; https://revisedacts.lawreform.ie/eli/2024/act/20/revised/en/html |
| Employer fails to pass on NAERSA's enrolment notice within 14 days | Offence; prescribed fixed-payment notice amount EUR 250 from 1 June 2026, not a universal limit on prosecution | AE Act s.50(8); S.I. 215/2026 art.7; https://www.irishstatutebook.ie/eli/2026/si/215/made/en/print |

A late payroll notification falls within s.987; do not promise a penalty-free submission or automatic self-correction immunity. Revenue’s interest-from-the-14th instruction is consistent with the conditional ROS extension: TCA s.983 requires both the return and remittance by the 23rd. A payment after the 23rd fails that condition; the extended due date cannot then be used to defer interest. Penalty disputes, criminal sanctions, late payment and prior-year correction outcomes: Check this point with one of our partner accountants.

## Cross-border points

- **Work partly abroad.** Where an employee works both in and outside the State and the share of pay taxable in Ireland is not yet known, Revenue may, on the employer's application, direct the proportion on which PAYE is operated. Without a direction, the employer operates PAYE on the whole amount (s.985E). PAYE exclusion orders and other reliefs: refer.
- **Third-party labour payments.** Revenue may direct a person who uses another firm's workers to pay that firm under deduction of tax where PAYE is unlikely to be operated (s.985F).
- **Social insurance.** Posted workers, A1 certificates, bilateral agreements and residence/remittance-basis outcomes are non-usable here; route to `ie-prsi-cross-border`, `ie-cross-border` or `ie-non-dom`. Check this point with one of our partner accountants.
- **Auto-enrolment and other jobs.** Eligibility counts gross pay from all employments, but contributions are only on the non-exempt employment's pay ([MyFutureFund contributions](https://revisedacts.lawreform.ie/eli/2024/act/20/revised/en/html)).
- **Foreign currency pay.** Non-usable hold on the exchange-rate choice; preserve the original currency and payment date. Check this point with one of our partner accountants.
- Residence and the remittance basis: `ie-cross-border`, `ie-non-dom`.

## Worked examples

### Example 1: monthly employee with a pension, October 2026

A single employee aged 32 is paid EUR 5,000 a month in October 2026. The cumulative RPN gives a EUR 44,000 cut-off point and EUR 4,000 of credits. Pay and pension are the same every month. At 30 September, cumulative gross is EUR 45,000, taxable pay EUR 42,750, Income Tax already deducted EUR 7,500 and USC EUR 999.62. These explicit prior totals make the October cumulative result below reproducible. The employee pays EUR 250 a month (5%) to the employer's approved defined contribution scheme and the employer pays EUR 300 a month (6%), above the 1.5% and 3.5% standards, so the job is exempt from auto-enrolment. The employer's occupational-scheme contribution is not a taxable benefit and does not enter the employee's pay below ([Revenue](https://www.revenue.ie/en/employing-people/benefit-in-kind-for-employers/other-benefits/pension-contributions.aspx)).

Taxable pay is 5,000 − 250 = 4,750. Monthly cut-off point 44,000 / 12 = 3,666.67; monthly credits 4,000 / 12 = 333.33. Income Tax = 20% × 3,666.67 + 40% × 1,083.33 − 333.33 = EUR 833.33. USC is on gross pay before pension: cumulative gross EUR 50,000 gives cumulative USC EUR 1,110.68, less EUR 999.62 previously deducted = EUR 111.06. Computing a standalone monthly share instead would round to EUR 111.07; use the cumulative history. Monthly pay is over EUR 2,392, so subclass A1: employee PRSI 4.35% × 5,000 = EUR 217.50 and employer PRSI 11.40% × 5,000 = EUR 570.00 (rates from 1 October 2026). Net pay = 5,000 − 250 − 833.33 − 111.06 − 217.50 = EUR 3,588.11. For the original September 2026 variant, employee PRSI is EUR 210.00 and employer PRSI EUR 562.50. With prior August Income Tax EUR 6,666.67 and USC EUR 888.55, September cumulative Income Tax EUR 7,500.00 and USC EUR 999.62 give period deductions EUR 833.33 and EUR 111.07; net pay is EUR 3,595.60. This preserves the September case without treating a standalone monthly share as a guaranteed cumulative result.

```oa-check
name: Single employee, EUR 5,000 a month, EUR 250 pension, paid October 2026
inputs:
  gross: 5000
  pension: 250
steps:
  - taxable: gross - pension
  - cutoff: 44000 / 12
  - credits: 4000 / 12
  - income_tax: round((44000 * 10 / 12) * 0.20 + ((taxable * 10) - 44000 * 10 / 12) * 0.40 - 4000 * 10 / 12, 2) - 7500
  - usc: round(12012 * 10 / 12 * 0.005 + 16688 * 10 / 12 * 0.02 + (gross * 10 - (12012 + 16688) * 10 / 12) * 0.03, 2) - 999.62
  - ee_prsi: gross * 0.0435
  - er_prsi: gross * 0.114
  - net: gross - pension - income_tax - usc - ee_prsi
expected:
  taxable: 4750
  income_tax: 833.33
  usc: 111.06
  ee_prsi: 217.50
  er_prsi: 570.00
  net: 3588.11
```

### Example 2: weekly part-timer in the PRSI Credit band, auto-enrolled

A single employee aged 25 works 28 hours a week for EUR 400 (EUR 14.29 an hour, above the EUR 14.15 minimum). Yearly pay is EUR 20,800, so NAERSA enrols her and sends an AEPN; the employer has no pension scheme. The week is tax week 45, paid in November 2026, on a cumulative RPN with a EUR 44,000 cut-off and EUR 4,000 credits. For this illustration she earned EUR 400 in each earlier week: prior gross EUR 17,600, Income Tax EUR 135.38 and USC EUR 199.54. NAERSA has already enrolled her; projected earnings alone are not an instruction to start deductions.

Income Tax: the weekly cut-off is EUR 44,000 / 52, so all EUR 400 is at 20% = 80.00, less weekly credits 4,000 / 52 = 76.92, gives EUR 3.08. USC: her income is over EUR 13,000, so USC applies: 0.5% of 231.00 + 2% of 169.00 = EUR 4.54. PRSI: EUR 400 is in subclass AX. The charge is 4.35% × 400 = 17.40, less the PRSI Credit 12 − (400 − 352.01) / 6 = 4.00, so employee PRSI is EUR 13.40. Employer PRSI is 9.15% × 400 = EUR 36.60 (pay is under EUR 552). Auto-enrolment: EUR 6.00 from her pay and EUR 6.00 from the employer, both paid to NAERSA on pay day; the State contribution is EUR 2.00, paid under NAERSA’s separate State-contribution notification. Her contribution gets no Income Tax relief. Net pay = 400 − 3.08 − 4.54 − 13.40 − 6.00 = EUR 372.98.

```oa-check
name: Weekly EUR 400, AX band with PRSI Credit, auto-enrolled, paid November 2026
inputs:
  weekly_pay: 400
steps:
  - credits: 4000 / 52
  - income_tax: round(weekly_pay * 45 * 0.20 - 4000 * 45 / 52, 2) - 135.38
  - usc: round(12012 * 45 / 52 * 0.005 + (weekly_pay * 45 - 12012 * 45 / 52) * 0.02, 2) - 199.54
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

## When to refuse or refer

- Non-ordinary PRSI classes B/C/D/H/J/K/M, Community Employment, under-16s, pension-age cases, uncertain employment status and proprietary directors; share schemes/RSUs/ESOP/KEEP/APSS/SAYE, insolvency/redundancy claims and attachment-order priorities: do not guess a class or tax result. Check this point with one of our partner accountants.
- Pay periods straddling 1 October 2026: the sources read state the rate periods but do not settle allocation between work dates and pay dates. Hold the affected computation before paying. Check this point with one of our partner accountants.
- Illness Benefit/PUP or other DSP-payment adjustments; multiple concurrent jobs with the same employer or inconsistent RPNs; cross-year back pay; unapproved/over-limit pension relief and unusual employer matching; low-business-mileage, part-year, pooled, discounted-OMV, employee-purchase-contribution or missing-CO2 car cases: no default category, credit or tax-free treatment is authorised here. Check this point with one of our partner accountants.
- Archived 2025 case, not a 2026 calculation: Dublin-resident single developer, age 32, salary EUR 70,000/year paid EUR 5,833.33/month, medical-insurance BIK EUR 1,200/year (EUR 100/month), employee/employer pension each 6% of cash salary (EUR 350/month), Class A1, cumulative basis, no car or LPT; sample pay date 28 May 2025. Preserve these inputs, but the old illustrative payslip, May remittance and annual snapshot are not usable: they reduced USC for pension and counted notional BIK as cash. Medical-insurance valuation/gross-up, exact historic cumulative deductions, employer costs and scheme remittance date require a separate historical calculation. Check this point with one of our partner accountants.
- 2027/2028: the car reductions expressly labelled for those years below are the schedule enacted in Finance Act 2025, not a complete update for those tax years. Budget 2027/Finance Bill 2026 payroll outcomes are not usable from this 2026 Guide. Check this point with one of our partner accountants.

## Sources

Official texts read on **2026-11-27**. Where a summary conflicts with the operative Act, the Act controls. Section numbers without another Act specified refer to TCA 1997.

| Source | URL | Read on |
|---|---|---|
| Revenue payroll submissions; read for fields, responsibility, channels and pay-day deadline | https://www.revenue.ie/en/employing-people/becoming-an-employer-and-ongoing-obligations/employer-obligations-from-01-01-2019/payroll-submissions.aspx | 2026-11-27 |
| DSP SW14, January 2026, pp.1–5 and 16–23 | https://assets.gov.ie/static/documents/cb168977/PRSI_C20260116_Contribution_Rates_and_User_Guide_-_SW_14_-_English_Version_-_January_2026_.pdf-web.pdf | 2026-11-27 |
| DSP auto enrolment; read for AEPN, gross-pay basis, no employee relief, employer portal and contribution payment | https://www.gov.ie/en/department-of-social-protection/publications/auto-enrolment-retirement-savings-system-for-employers/ | 2026-11-27 |
| Revenue tax relief charts; read for 2026 bands and credits | https://www.revenue.ie/en/personal-tax-credits-reliefs-and-exemptions/tax-relief-charts/index.aspx | 2026-11-27 |
| Act 18/2025, section 2 | https://www.irishstatutebook.ie/eli/2025/act/18/section/2/enacted/en/html | 2026-11-27 |
| Revenue USC; read for exemption cliff and pension contributions | https://www.revenue.ie/en/jobs-and-pensions/usc/index.aspx | 2026-11-27 |
| Revenue reduced rates; read for income, age and full-card conditions | https://www.revenue.ie/en/jobs-and-pensions/usc/reduced-rates.aspx | 2026-11-27 |
| Revenue emergency rates; read for the 2026 table | https://www.revenue.ie/en/jobs-and-pensions/documents/emergency-rates.pdf | 2026-11-27 |
| Act 24/2024, section 3 | https://www.irishstatutebook.ie/eli/2024/act/24/section/3/enacted/en/html | 2026-11-27 |
| Act 19/2025, section 2 | https://www.irishstatutebook.ie/eli/2025/act/19/section/2/enacted/en/html | 2026-11-27 |
| WRC minimum-wage poster, 2026 | https://www.workplacerelations.ie/media/334fojsq/national-minimum-wage-poster.pdf | 2026-11-27 |
| S.I. 472/2025 | https://www.irishstatutebook.ie/eli/2025/si/472/made/en/print | 2026-11-27 |
| AE Act 2024, revised to 1 June 2026, ss.1, 47–62 and 138 | https://revisedacts.lawreform.ie/eli/2024/act/20/revised/en/html | 2026-11-27 |
| S.I. 668/2025 | https://www.irishstatutebook.ie/eli/2025/si/668/made/en/print | 2026-11-27 |
| Revenue pension limits; read for age bands, earnings ceiling and income-source restriction | https://www.revenue.ie/en/jobs-and-pensions/pension/relief/tax-relief-limits.aspx | 2026-11-27 |
| Act 18/2025, section 24 | https://www.irishstatutebook.ie/eli/2025/act/18/section/24/enacted/en/html | 2026-11-27 |
| Revenue car exemptions; read for electricity-only relief, OMV floor and dated taper | https://www.revenue.ie/en/employing-people/benefit-in-kind-for-employers/private-use-company-cars/exemptions.aspx | 2026-11-27 |
| Revenue small benefits; read for first-five, non-cash, annual ceiling and reporting conditions | https://www.revenue.ie/en/employing-people/benefit-in-kind-for-employers/valuation-of-benefits/small-benefit-exemption.aspx | 2026-11-27 |
| Revenue paying tax; read for statements, quarterly eligibility and interest | https://www.revenue.ie/en/employing-people/paying-your-employees-tax-to-revenue/paying-tax-to-revenue.aspx | 2026-11-27 |
| Revenue cumulative basis; read for prior deductions and frequency conversions | https://www.revenue.ie/en/employing-people/paying-an-employee/methods-of-calculating-tax/cumulative-basis.aspx | 2026-11-27 |
| Revenue gross and taxable pay; read for gross definition and qualifying deduction types | https://www.revenue.ie/en/employing-people/what-constitutes-pay/what-are-gross-and-taxable-pay/index.aspx | 2026-11-27 |
| Revenue employee pensions; read for USC/PRSI base and total contributions | https://www.revenue.ie/en/employing-people/what-constitutes-pay/employees-pension-payments/index.aspx | 2026-11-27 |
| Revenue tax calculation; read for rate slices and credits | https://www.revenue.ie/en/employing-people/paying-an-employee/methods-of-calculating-tax/calculating-tax-rules.aspx | 2026-11-27 |
| Act 18/2025, section 16 | https://www.irishstatutebook.ie/eli/2025/act/18/section/16/enacted/en/html | 2026-11-27 |
| Revenue LPT; read for RPN instruction and annual spreading | https://www.revenue.ie/en/employing-people/paying-your-employees-tax-to-revenue/deduction-of-lpt.aspx | 2026-11-27 |
| Revenue RPN; read for latest-notification obligation, exemptions and ceased-employment totals | https://www.revenue.ie/en/employing-people/becoming-an-employer-and-ongoing-obligations/employer-obligations-from-01-01-2019/revenue-payroll-notification.aspx | 2026-11-27 |
| Revenue Week 1; read for non-cumulative calculation and no credit refunds | https://www.revenue.ie/en/employing-people/paying-an-employee/methods-of-calculating-tax/week1-basis.aspx | 2026-11-27 |
| Revenue emergency basis; read for RPN/PPSN conditions and continuous weeks | https://www.revenue.ie/en/employing-people/paying-an-employee/methods-of-calculating-tax/emergency-basis.aspx | 2026-11-27 |
| Revenue company cars; read for 2026 tables, OMV, contributions, mileage records and quarterly review | https://www.revenue.ie/en/employing-people/benefit-in-kind-for-employers/private-use-company-cars/calculate-value-benefit.aspx | 2026-11-27 |
| Revenue TDM Part 05-01-01e; read for relevant-incentive definition and salary-sacrifice exclusion | https://www.revenue.ie/en/tax-professionals/tdm/income-tax-capital-gains-tax-corporation-tax/part-05/05-01-01e.pdf | 2026-11-27 |
| Revenue ERR; read for small-benefit reporting date and ROS process | https://www.revenue.ie/en/employing-people/becoming-an-employer-and-ongoing-obligations/err-jan-2024/index.aspx | 2026-11-27 |
| Revenue return/payment dates; read for monthly, quarterly and annual remitters and VDD | https://www.revenue.ie/en/employing-people/becoming-an-employer-and-ongoing-obligations/employer-obligations-from-01-01-2019/returns-and-payment-due-dates.aspx | 2026-11-27 |
| Revenue PRSI; read for period weeks, correction and separate records | https://www.revenue.ie/en/employing-people/paying-your-employees-tax-to-revenue/prsi.aspx | 2026-11-27 |
| Revenue statements; read for revision before and amendment after return date | https://www.revenue.ie/en/employing-people/becoming-an-employer-and-ongoing-obligations/employer-obligations-from-01-01-2019/statements-from-revenue.aspx | 2026-11-27 |
| Revenue starters/leavers; read for first Irish job registration, dates and nil-RPN risk | https://www.revenue.ie/en/employing-people/becoming-an-employer-and-ongoing-obligations/employer-obligations-from-01-01-2019/commencing-and-ceasing-employees.aspx | 2026-11-27 |
| Revenue EDS; read for January availability, myAccount and corrected versions | https://www.revenue.ie/en/jobs-and-pensions/end-of-year-process/employment-detail-summary.aspx | 2026-11-27 |
| Revenue Part 42; read ss.983–985A, 985E–985G, 987 and 991–991A | https://www.revenue.ie/en/tax-professionals/documents/notes-for-guidance/tca/part42.pdf | 2026-11-27 |
| S.I. 215/2026 | https://www.irishstatutebook.ie/eli/2026/si/215/made/en/print | 2026-11-27 |
| Act 25/1991, section 4 | https://www.irishstatutebook.ie/eli/1991/act/25/section/4/enacted/en/html | 2026-11-27 |
| Revenue USC rates; read for 2026 band widths and rates | https://www.revenue.ie/en/jobs-and-pensions/usc/standard-rates-thresholds.aspx | 2026-11-27 |
| Revenue employer pensions; read for OPS/AE non-BIK treatment and PRSA/PEPP boundary | https://www.revenue.ie/en/employing-people/benefit-in-kind-for-employers/other-benefits/pension-contributions.aspx | 2026-11-27 |
| Revenue RAC; read for net-pay relief and USC/PRSI base | https://www.revenue.ie/en/employing-people/what-constitutes-pay/employees-pension-payments/retirement-annuity-contracts-racs.aspx | 2026-11-27 |
| Payment of Wages Act 1991 s.2(1)(f), credit transfer | https://www.irishstatutebook.ie/eli/1991/act/25/section/2/enacted/en/html | 2026-11-27 |

Not yet confirmed: the computations expressly held under “When to refuse or refer”, salary sacrifice, income-continuance relief and termination payments remain non-usable. No guessed result is authorised for those cases. Check this point with one of our partner accountants.
