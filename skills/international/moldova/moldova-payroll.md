---
name: moldova-payroll
description: "Moldova payroll for employers, tax year 2026: companies, individual entrepreneurs and other employers paying salaries and other rewards in Moldovan lei. Covers withholding of 12% income tax on salary under Fiscal Code art. 88, the employee's exemption application (personal MDL 29,700 a year, dependants MDL 9,900, the MDL 360,000 income limit), the 9% health premium withheld from pay, the employer's 24% state social insurance (29% public bodies, 32% or 39% special conditions, agriculture 18% plus 6% from the state budget), day labourers, gross-to-net, payment and the monthly return by the 25th, the year-end report and the 1 March statement to staff, the MDL 6,300 minimum wage from 1 January 2026, IT park staff, and fines. Trigger on: Moldova payroll, salariu net, gross to net Moldova, reținerea impozitului din salariu, IPC21, employer cost Moldova. Out of scope: own contributions of the self-employed (moldova-social-contributions), the annual return (moldova-income-tax)."
version: 0.2
jurisdiction: MD
tax_year: 2026
last_updated: 2026-10-31
review_status: pending_review
trust_label: Built by Michael Cutajar and the OpenAccountants team
category: international
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Moldova: payroll for employers (2026) v0.2

An employer in Moldova withholds income tax and the employee's health insurance premium from each salary payment and pays its own state social insurance contribution on top. All three are paid and reported to the State Tax Service (SFS) by the 25th of the following month. Figures below are from the Fiscal Code consolidated to Law LP235/2026, Law 489/1999 (annex 1 as replaced for 2026), Law 1593/2002, the 2026 health insurance funds law (LP321/2025) and the 2026 Government decisions on wages.

## Who this applies to

- **Employers**: every employer that pays an employee salary, bonuses and benefits must calculate and withhold income tax (Fiscal Code art. 88(1)). The same rule applies to a beneficiary of works and to a dual-education unit (art. 88(1^2)).
- **Treated as salary**: income of an individual without a business from services or works, fees of board and audit-committee members (art. 88(5)), a director's mandate with a company (art. 88(6)), and an independent entrepreneur working for a client outside the conditions of art. 24(11^1) (art. 88(8)).
- **Employees** are the payers of the 9% health premium (Law 1593/2002 annex 1 pt. 2). They pay no state social insurance contribution; Law 489/1999 annex 1 pt. 1.1 has an employer line only.
- **Day labourers** under Law 22/2018: 12% income tax with no exemptions (art. 15 a1)) and 6% social insurance paid by the beneficiary (Law 489/1999 annex 1 pt. 1.9).
- **IT park residents** pay a 7% single tax that includes salary income tax, employer social contributions and employees' health premiums. Their employees' salaries are taxed finally, without exemptions (Fiscal Code art. 370, 372(1), 377(1)-(2); Law 1593/2002 art. 4(1^1)). See [moldova-tax-optimization](moldova-tax-optimization.md).
- Not here: the annual return and other income (see [moldova-income-tax](moldova-income-tax.md)); fixed contributions of the self-employed (see [moldova-social-contributions](moldova-social-contributions.md)).

## Rates, bands and thresholds

| Item | Rate or amount | Year | Source |
|---|---|---|---|
| Income tax on salary | 12% | 2026 | Fiscal Code art. 15 a), 88, https://www.legis.md/cautare/getResults?doc_id=157050&lang=ro |
| Personal exemption, if annual taxable income is below MDL 360,000 | MDL 29,700 a year | 2026 | art. 33(1), same URL |
| Higher personal exemption (groups in art. 33(2)) | MDL 34,620 a year | 2026 | art. 33(2), same URL |
| Spouse of a person in art. 33(2) | MDL 21,780 a year | 2026 | art. 34(2), same URL |
| Each dependant | MDL 9,900 a year (MDL 21,780 for a childhood or severe disability) | 2026 | art. 35(1), same URL |
| Health premium withheld from the employee | 9.0% of salary and other rewards | 2026 | Law LP321/2025 art. 4(1), https://www.legis.md/cautare/getResults?doc_id=156542&lang=ro |
| Employer social insurance, private sector, higher education and medical institutions | 24% | 2026 | Law 489/1999 annex 1 pt. 1.1, https://www.legis.md/cautare/getResults?doc_id=156677&lang=ro |
| Employer social insurance, public bodies | 29% | 2026 | annex 1 pt. 1.1, same URL |
| Special working conditions: private / public | 32% / 39% | 2026 | annex 1 pt. 1.2, same URL |
| Agricultural employers (70% test) | 18% employer + 6% state budget | 2026 | annex 1 pt. 1.5, same URL |
| Day labourers' social insurance, paid by the beneficiary | 6% of daily pay | 2026 | annex 1 pt. 1.9, same URL |
| Minimum social insurance base per employee | the minimum wage, in proportion to time worked; part-time or reduced hours: at least 25% of the contribution on the minimum wage | 2026 | Law 489/1999 art. 22(1), same URL |
| Minimum wage, full time (169 hours a month on average) | MDL 6,300 a month, MDL 37.28 an hour | from 1 Jan 2026 | Government Decision 771/2025, https://www.legis.md/cautare/getResults?doc_id=152064&lang=ro |
| Forecast average monthly wage | MDL 17,400 | 2026 | Government Decision 773/2025, https://www.legis.md/cautare/getResults?doc_id=152066&lang=ro |
| IT park single tax minimum per employee per month | 30% of MDL 17,400 = MDL 5,220 | 2026 | Fiscal Code art. 370(2); HG 773/2025 |
| Late-payment interest on tax | 11% a year, per day | 2026 | Fiscal Code art. 228(3); NBM base rate 6.00% on 6 Nov 2025, https://www.bnm.md/ro/content/raportul-asupra-inflatiei-nr-4-2025 |
| Late payment of social contributions | 0.1% a day | 2026 | Law LP320/2025 art. 4, https://www.legis.md/cautare/getResults?doc_id=156540&lang=ro |

## The taxable base

**Order of the calculation.**
1. Start from gross salary, including bonuses and benefits from the employer (art. 88(1); art. 18 c)).
2. Health premium: 9% of salary and other rewards before any tax is withheld (Law 1593/2002 art. 6).
3. Income tax: the employer calculates the tax taking account of the exemptions the employee claimed and of deductions, by the method set by the Government (art. 88(1)). The employee's health premium is a deduction (art. 35^2(1)). Over the year, tax = 12% x (gross pay - health premiums - exemptions claimed).
4. Employer social insurance: the employer's rate applies to the full monthly salaries and rewards (Law 489/1999 annex 1 pt. 1.1). It is not deducted from the employee's pay. The monthly base for each employee may not be lower than the minimum wage, in proportion to time worked; for part-time or reduced hours, the contribution is at least 25% of the contribution on the minimum wage (Law 489/1999 art. 22(1)). At 24% that is MDL 1,512 a month at full time and at least MDL 378 for part-time.

**Exemptions are claimed by application.** To get exemptions, the employee gives the employer a signed application, with copies of the supporting documents, no later than the first day of work. An employee who stays with the same employer does not reapply each year, unless he gains or loses a right. When the exemption amount changes during the year, the employee files a new application within 10 days. The application may be on paper or electronic (art. 88(2)-(3)). Spouse and dependant exemptions start in the month after the right arises (art. 34(3), 35(4)).

**The MDL 360,000 limit.** The personal exemption is only for residents whose annual taxable income is below MDL 360,000 (art. 33(1)). The employer is not required to track whether an employee loses the right to the personal exemption (art. 88(1)). An employee who used the exemption and earned more than MDL 360,000 must file an annual return and pay the difference (art. 83(2) a2), 87(1)).

**What is not in the social insurance base.** No contribution is due on the items in annex 3 to Law 489/1999, for example sick pay, business-trip expenses and other compensation (but pay for unused leave on dismissal is included), severance pay within Labour Code limits, employer-organised transport, meals and training under Government rules, employer payments for child care up to MDL 2,500 a month per child under 3, and dividends.

**Minimum wage.** Full-time pay may not be below MDL 6,300 a month for 169 hours on average. For a legal working week under 40 hours, the hourly minimum is the monthly minimum divided by the average monthly hours of that schedule (Government Decision 771/2025 pt. 1).

## Deadlines and filing

| What | Deadline | Source |
|---|---|---|
| Pay withheld income tax | by the 25th of the month after the month of payment | Fiscal Code art. 92(1) |
| Monthly return on income tax, health premiums and social contributions | by the 25th of the month after the month of payment | art. 92(2) |
| Pay employer social insurance | monthly, by the 25th of the following month | Law 489/1999 annex 1 pt. 1.1 |
| Pay employees' health premiums | by the 25th of the month after the month of payment | Law 1593/2002 art. 12, 20(1) |
| Annual report of payments and tax withheld, per payee | by the 25th of the month after the year end (25 January 2027 for 2026); within 15 days of approval of the liquidation balance sheet on liquidation | Fiscal Code art. 92(3) |
| Unified annual report for an individual entrepreneur or farm with up to 5 staff, not VAT-registered | by 25 March of the following year | art. 92(8) |
| Statement to each employee of income, exemptions, deductions and tax withheld | by 1 March of the following year | art. 92(4) |
| Correction of a statement already given | inform the employee within 15 working days | art. 92(4^1) |
| Employee's new exemption application after a change | within 10 days of the change | art. 88(3) |

## Penalties and interest

| Breach | Penalty | Source |
|---|---|---|
| Late payment of withheld tax | interest for each day; 11% a year for 2026 | Fiscal Code art. 228(2)-(3) |
| Late payment of social contributions | 0.1% of the debt for each day | LP320/2025 art. 4; Law 489/1999 art. 28 |
| Return not filed or filed wrongly | MDL 200 to 400 or MDL 500 to 1,000 per return (caps MDL 2,000 and MDL 10,000) | Fiscal Code art. 260(1) |
| Tax, premiums or contributions reduced by false data in a return | 20% to 30% of the amount reduced (not applied to a self-corrected return) | art. 261(4), (4^1) |
| Evading calculation and payment | 80% to 100% of the undeclared amount | art. 261(5) |
| Employee gives false information in the exemption application | a fine and criminal liability under the law | art. 88(4) |

## Cross-border points

- **Non-resident employees.** Art. 71(1) n) covers salaries and similar pay of non-resident individuals under an employment contract, and payments to administrators, founders and board or management members of a resident; art. 71(1) o) covers benefits under art. 19 given to non-resident individuals by a resident employer or a permanent establishment. The 12% non-resident withholding in art. 91(1) does not apply to this income when tax is withheld under art. 88 (art. 91(2) b)). When that income comes from a payer that is not a withholding agent, it is taxed at the art. 15 a) rate with no deductions or exemptions (art. 74(1)).
- **Foreign staff and health insurance.** Foreigners with a Moldovan employment contract pay the health premium like Moldovan citizens unless a treaty provides otherwise (Law 1593/2002 art. 10(1)).
- **International organisations.** Moldovan citizens employed by international projects and organisations are covered by employer social insurance unless a treaty exempts them (Law 489/1999 annex 1 pt. 1.1; annex 3 pt. 6).
- **Posted workers and treaties**: treaty relief on employment income is in the pack's cross-border skill, [md-cross-border](md-cross-border.md); social security agreements are not covered yet.

## Worked examples

**Example 1. Standard employee, MDL 20,000 a month.** A private company pays a resident employee MDL 20,000 gross every month of 2026, MDL 240,000 for the year. The employee claimed the personal exemption only. The health premium is 9%, MDL 21,600 a year (MDL 1,800 a month). Income tax for the year is 12% of 240,000 - 21,600 - 29,700 = MDL 188,700, so MDL 22,644 (MDL 1,887 a month if spread evenly). Net pay is MDL 195,756 a year (MDL 16,313 a month). The company pays 24% social insurance, MDL 57,600 a year (MDL 4,800 a month), so the employee costs MDL 297,600. Each month's tax, premium and contribution are paid and reported by the 25th of the next month.

```oa-check
name: Moldova payroll, MDL 20,000 a month, personal exemption, 2026
inputs:
  monthly_gross: 20000
  months: 12
  personal_exemption: 29700
  health_rate: 0.09
  pit_rate: 0.12
  employer_social_rate: 0.24
steps:
  - annual_gross: monthly_gross * months
  - health: annual_gross * health_rate
  - taxable: annual_gross - health - personal_exemption
  - pit: taxable * pit_rate
  - net: annual_gross - health - pit
  - net_monthly: net / months
  - employer_social: annual_gross * employer_social_rate
  - employer_cost: annual_gross + employer_social
expected:
  annual_gross: 240000
  health: 21600
  taxable: 188700
  pit: 22644
  net: 195756
  net_monthly: 16313
  employer_social: 57600
  employer_cost: 297600
```

**Example 2. High earner over the MDL 360,000 limit.** An employee earns MDL 35,000 a month, MDL 420,000 in 2026, and claimed the personal exemption at the start of the year. The employer applied it all year, as it is not required to track the loss of the right (art. 88(1)), and withheld 12% of 420,000 - 37,800 - 29,700 = MDL 352,500, so MDL 42,300. But her taxable income after the health premium is MDL 382,200, above MDL 360,000, so she has no right to the exemption (art. 33(1)). Her true tax is 12% of 382,200 = MDL 45,864. She must file a return and pay the MDL 3,564 difference by 30 April 2027 (art. 83(2) a2), 87(1)). The employer's 24% social insurance is MDL 100,800.

```oa-check
name: Moldova payroll, exemption lost above MDL 360,000, 2026
inputs:
  annual_gross: 420000
  personal_exemption: 29700
  health_rate: 0.09
  pit_rate: 0.12
  employer_social_rate: 0.24
  exemption_limit: 360000
steps:
  - health: annual_gross * health_rate
  - taxable_before_exemption: annual_gross - health
  - over_limit: taxable_before_exemption - exemption_limit
  - withheld_with_exemption: (taxable_before_exemption - personal_exemption) * pit_rate
  - tax_due: taxable_before_exemption * pit_rate
  - balance_due_30_april: tax_due - withheld_with_exemption
  - employer_social: annual_gross * employer_social_rate
expected:
  health: 37800
  taxable_before_exemption: 382200
  over_limit: 22200
  withheld_with_exemption: 42300
  tax_due: 45864
  balance_due_30_april: 3564
  employer_social: 100800
```

## Ask the client first

1. Is the employer private, a public body, an agricultural business (70% test) or an IT park resident?
2. Does any job fall under the special working conditions list?
3. For each person: employment contract, director's mandate, civil contract for services, or day labourer? Monthly gross pay?
4. Which exemptions has each employee claimed in writing, and is anyone likely to earn MDL 360,000 or more in the year?
5. Are any staff non-resident or foreign nationals, or working for an international project?
6. Does pay include benefits, bonuses, meals, transport or child-care payments?

## Sources

| Source | URL | Read on |
|---|---|---|
| Codul fiscal nr. 1163/1997, consolidated to LP235/2026: arts. 15, 18, 33, 34, 35, 35^2, 71, 74, 83, 87, 88, 91, 92, 228, 260, 261, 370, 372, 377 | https://www.legis.md/cautare/getResults?doc_id=157050&lang=ro | 2026-10-30 |
| Law 489/1999, consolidated to LP201/2026: annex 1 (as replaced, MO 659-661/2025), annex 3, arts. 22, 28 | https://www.legis.md/cautare/getResults?doc_id=156677&lang=ro | 2026-10-31 |
| Law LP320/2025, state social insurance budget 2026: art. 4 | https://www.legis.md/cautare/getResults?doc_id=156540&lang=ro | 2026-10-31 |
| Law 1593/2002 on compulsory health insurance premiums: arts. 4, 6, 10, 12, 20; annex 1 | https://www.legis.md/cautare/getResults?doc_id=152955&lang=ro | 2026-10-31 |
| Law LP321/2025, compulsory health insurance funds 2026: art. 4 | https://www.legis.md/cautare/getResults?doc_id=156542&lang=ro | 2026-10-31 |
| Government Decision 771/2025: minimum wage from 1 January 2026 | https://www.legis.md/cautare/getResults?doc_id=152064&lang=ro | 2026-10-31 |
| Government Decision 773/2025: forecast average monthly wage 2026 | https://www.legis.md/cautare/getResults?doc_id=152066&lang=ro | 2026-10-31 |
| National Bank of Moldova, Inflation Report no. 4, 2025 | https://www.bnm.md/ro/content/raportul-asupra-inflatiei-nr-4-2025 | 2026-10-31 |

Not yet confirmed: the Government's method for monthly withholding from salary (art. 88(1)), including whether annual exemptions are spread as one twelfth a month; the name and layout of the monthly return (the old version called it IPC21) and the year-end report forms; the special working conditions job list (annex 2 to Law 489/1999); the valuation of benefits in kind and meal tickets (Fiscal Code art. 19 not read in full); the content of art. 88^1, repealed from 1 July 2026 by Law LP318/2025; sector or real-economy minimum wages; whether non-resident employees may claim exemptions through payroll; posted workers and social security agreements.

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
