---
name: india-payroll
description: >
  Use this skill whenever asked about Indian payroll processing for FY 2026-27 (tax
  year 2026-27 under the Income-tax Act 2025), employee salary calculations, TDS on
  salary under section 392, provident fund, Employees' State Insurance, employer cost,
  CTC breakdowns, gross-to-net, Indian payslip structure, Form No. 138 quarterly
  statements and Form No. 130 certificates, or any question about wages, deductions or
  employer obligations in India. Trigger on phrases like Indian payroll, TDS on salary,
  Section 192, Section 392, Form 16, Form 130, Form 24Q, Form 138, PF contribution, ESI
  contribution, CTC breakdown, new tax regime India, old tax regime, standard deduction,
  salary structure India, basic DA HRA, professional tax, gratuity, bonus India or
  minimum wages India. It covers the new and old regime rates, rebate, surcharge, cess,
  TDS deposit and statement dates, interest and penalties, the Labour Codes wages rule,
  overtime, wage payment dates, bonus and gratuity. Tier 2, not reviewed by an accountant.
version: "2.0"
jurisdiction: IN
tax_year: 2026
tax_year_notes: "FY 2026-27 (tax year 2026-27 under the Income-tax Act 2025, 1 April 2026 to 31 March 2027); labour rules as in force on 14 November 2026"
last_updated: 2026-11-14
depends_on:
  - payroll-workflow-base
category: payroll
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
tier: 2
domain: payroll
type: computation
---

# India Payroll: Salary TDS, Provident Fund, ESI, Professional Tax, Bonus and Gratuity, FY 2026-27

> **General reference only.** This skill is general reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts. Do not rely on it to file, pay or take a tax position without review by a qualified professional in India. Label every computation as an estimate.

Tax year: FY 2026-27, 1 April 2026 to 31 March 2027, the first tax year under the Income-tax Act 2025, which replaced the Income-tax Act 1961 from 1 April 2026. Salary paid up to 31 March 2026 belongs to the 1961 Act and its forms (section 192, Form 16 under section 203, Form 12BB); this skill does not cover it. The labour rules are those in force on 14 November 2026: the Code on Wages 2019 and the Code on Social Security 2020 came into force on 21 November 2025, the Social Security (Central) Rules 2026 (8 May 2026) and the Employees' Provident Funds Scheme 2026 (29 June 2026) on publication, and S.O. 5109(E) set the provident fund wage ceiling at 25,000 rupees a month from 17 September 2026. Rules, rates and section numbers from the old labour Acts (EPF Scheme 1952, ESI Act 1948, Payment of Bonus Act 1965, Payment of Gratuity Act 1972, Minimum Wages Act 1948) are out of date for current payroll unless this skill says otherwise.

## Who this applies to

Employers running payroll for employees in India, and their payroll preparers: income tax deducted from salary, provident fund, ESI, professional tax, wages, bonus, gratuity, maternity benefit, payslips and the filing calendar.

| Field | Value |
| --- | --- |
| Tax year | 1 April to 31 March; tax year 2026-27 runs from 1 April 2026 to 31 March 2027 |
| Income tax law | Income-tax Act 2025 (30 of 2025) and the Income-tax Rules 2026; old regime rates and the surcharge in the Finance Act 2026 (4 of 2026) |
| Salary TDS section | Section 392 of the Income-tax Act 2025 |
| Labour law | Code on Wages 2019 (wages, minimum wages, overtime, bonus); Code on Social Security 2020 (provident fund, ESI, gratuity, maternity) |
| Authorities | Central Board of Direct Taxes, Income Tax Department; EPFO; ESIC; State Governments for professional tax and minimum wages |
| Income tax regime | New regime under section 202(1) is the default |
| Minimum wage | Fixed by the appropriate Government under the Code on Wages, not below the floor wage; no single national figure |

Detailed provident fund and ESI procedure is in `in-pf-esi-employer` (one figure, one home: its rates are summarised here only as far as a payslip needs them). State profession tax is in `in-professional-tax`. The employee's own return and regime choice are in `india-income-tax`; TDS on contractors and professionals in `in-tds-freelance`; residence in `in-tax-residency`.

## Rates, bands and thresholds

### Income tax on salary, tax year 2026-27

| Item | Rate or amount | Condition | Source |
| --- | --- | --- | --- |
| New regime (s 202(1)), income up to 4,00,000 | Nil | Default regime | https://egazette.gov.in/WriteReadData/2025/265620.pdf |
| New regime, over 4,00,000 to 8,00,000 | 5% | Default regime | https://egazette.gov.in/WriteReadData/2025/265620.pdf |
| New regime, over 8,00,000 to 12,00,000 | 10% | Default regime | https://egazette.gov.in/WriteReadData/2025/265620.pdf |
| New regime, over 12,00,000 to 16,00,000 | 15% | Default regime | https://egazette.gov.in/WriteReadData/2025/265620.pdf |
| New regime, over 16,00,000 to 20,00,000 | 20% | Default regime | https://egazette.gov.in/WriteReadData/2025/265620.pdf |
| New regime, over 20,00,000 to 24,00,000 | 25% | Default regime | https://egazette.gov.in/WriteReadData/2025/265620.pdf |
| New regime, over 24,00,000 | 30% | Default regime | https://egazette.gov.in/WriteReadData/2025/265620.pdf |
| Standard deduction, s 19(1) Table Sl. No. 2(a) | 75,000 or the salary, whichever is less | Tax computed under s 202(1) | https://egazette.gov.in/WriteReadData/2025/265620.pdf |
| Standard deduction, s 19(1) Table Sl. No. 2(b) | 50,000 or the salary, whichever is less | Any other case (old regime) | https://egazette.gov.in/WriteReadData/2025/265620.pdf |
| Profession tax paid, s 19(1) Table Sl. No. 1 | Entire amount | Old regime only; removed by s 202(2)(a)(iv) | https://egazette.gov.in/WriteReadData/2025/265620.pdf |
| Rebate, resident individual under s 202(1), s 156(2)(a) | Tax or 60,000, whichever is less | Income does not exceed twelve lakh rupees; marginal relief above under s 156(2)(b) | https://egazette.gov.in/WriteReadData/2025/265620.pdf |
| Rebate, resident individual, s 156(1) | Tax or 12,500, whichever is less | Total income does not exceed 5,00,000 | https://egazette.gov.in/WriteReadData/2025/265620.pdf |
| Old regime cap on Schedule XV sums (provident fund, life insurance and others), s 123 | 1,50,000 | Old regime only | https://egazette.gov.in/WriteReadData/2025/265620.pdf |
| Employer contribution to the notified pension scheme deductible for the employee, Central or State Government employer, s 124(1)(a) | 14% of salary | Both regimes | https://egazette.gov.in/WriteReadData/2025/265620.pdf |
| Same, any other employer, s 124(1)(b) | 10% of salary | Old regime | https://egazette.gov.in/WriteReadData/2025/265620.pdf |
| Same, any other employer, s 124(2) | 14% of salary | Total income taxed under s 202(1) | https://egazette.gov.in/WriteReadData/2025/265620.pdf |
| TDS where the employee gives no valid PAN, s 397(2)(b)(i)(C) | 20%, if higher than the normal rate | Any other case | https://egazette.gov.in/WriteReadData/2025/265620.pdf |
| Interest, tax not deducted, s 398(3)(a)(i) | 1% per month or part | From the date deductible to the date deducted | https://egazette.gov.in/WriteReadData/2025/265620.pdf |
| Interest, tax deducted but paid late, s 398(3)(a)(ii) | 1.5% per month or part | From deduction to payment | https://egazette.gov.in/WriteReadData/2025/265620.pdf |
| Penalty, TDS statement not delivered on time or incorrect, s 461(1) | 10,000 to 1,00,000 | None for a late statement delivered within one month with tax, fee and interest paid (s 461(2)) | https://egazette.gov.in/WriteReadData/2025/265620.pdf |
| Penalty per day, Form No. 130 certificate, perquisite statement or s 397(3)(b) statement not furnished, s 465(2)(g), (i), (k) | 500 a day | Capped at the tax deductible for the certificate and the s 397(3)(b) statement (s 465(3)) | https://egazette.gov.in/WriteReadData/2025/265620.pdf |
| Old regime, under 60, up to 2,50,000 | Nil | Opted out under s 202(4); Finance Act 2026 First Schedule Part I-B Para A (Part III for TDS) | https://egazette.gov.in/WriteReadData/2026/271439.pdf |
| Old regime, under 60, over 2,50,000 to 5,00,000 | 5% | Same | https://egazette.gov.in/WriteReadData/2026/271439.pdf |
| Old regime, under 60, over 5,00,000 to 10,00,000 | 12,500 plus 20% of the excess over 5,00,000 | Same | https://egazette.gov.in/WriteReadData/2026/271439.pdf |
| Old regime, under 60, over 10,00,000 | 1,12,500 plus 30% of the excess over 10,00,000 | Same | https://egazette.gov.in/WriteReadData/2026/271439.pdf |
| Old regime, resident aged 60 to 79 | Nil to 3,00,000; 5% to 5,00,000; 10,000 plus 20% to 10,00,000; 1,10,000 plus 30% above | Same | https://egazette.gov.in/WriteReadData/2026/271439.pdf |
| Old regime, resident aged 80 or more | Nil to 5,00,000; 20% to 10,00,000; 1,00,000 plus 30% above | Same | https://egazette.gov.in/WriteReadData/2026/271439.pdf |
| Surcharge, both regimes, total income over 50 lakh to 1 crore | 10% | Marginal relief applies | https://egazette.gov.in/WriteReadData/2026/271439.pdf |
| Surcharge, both regimes, over 1 crore to 2 crore | 15% | Marginal relief applies | https://egazette.gov.in/WriteReadData/2026/271439.pdf |
| Surcharge, new regime, income excluding dividend and ss 196 to 198 gains over 2 crore | 25% (top rate; 15% cap on dividend and those gains) | Section 3(4)(b) Table Sl. No. 10 | https://egazette.gov.in/WriteReadData/2026/271439.pdf |
| Surcharge, old regime, over 2 crore to 5 crore / over 5 crore | 25% / 37% | On income excluding dividend and ss 196 to 198 gains | https://egazette.gov.in/WriteReadData/2026/271439.pdf |
| Health and Education Cess | 4% of income-tax plus surcharge | All cases, no marginal relief | https://egazette.gov.in/WriteReadData/2026/271439.pdf |
| Fee for a late TDS statement under s 397(3)(b), s 427(1) as substituted | 200 a day | Not more than the tax deductible | https://egazette.gov.in/WriteReadData/2026/271439.pdf |
| Perquisite statement in Form No. 130 columns, rule 204 | Salary for the year not more than 1,50,000; otherwise Form No. 123 | Income-tax Rules 2026 | https://www.incometax.gov.in/iec/foportal/sites/default/files/2026-03/En-Notified-IT-Rules-2026-20-03-2026.pdf |

### Social security and labour amounts

| Item | Rate or amount | Condition | Source |
| --- | --- | --- | --- |
| Provident fund, employer and employee each | Twelve per cent of wages (ten per cent for a notified class) | EPF Scheme 2026 para 18; full detail in `in-pf-esi-employer` | https://egazette.gov.in/WriteReadData/2026/273957.pdf |
| Provident fund wage ceiling, Chapter III | 25,000 rupees per month | From 17 September 2026 | https://egazette.gov.in/WriteReadData/2026/276299.pdf |
| ESI employer / employee | Three and one-fourth per cent / three-fourth per cent of wages | Rule 19, rounded to the next higher rupee | https://egazette.gov.in/WriteReadData/2026/272366.pdf |
| ESI coverage wage limit | 21,000 rupees per month | Ministry of Labour FAQ of 16 March 2026, "at present" | https://www.labour.gov.in/static/uploads/2026/03/a4ccf4c6d97c4f1f36a6d83f8c64213d.pdf |
| Wages: excluded pay above this share of all remuneration is added back | One-half | Code on Wages s 2(y); same rule in Code on Social Security s 2(88) | https://egazette.gov.in/WriteReadData/2019/210356.pdf |
| Overtime | Not less than twice the normal rate of wages | Code on Wages s 14 | https://egazette.gov.in/WriteReadData/2019/210356.pdf |
| Statutory bonus, minimum | Eight and one-third per cent of wages or 100 rupees, whichever is higher | Code on Wages s 26(1); establishments with twenty or more persons | https://egazette.gov.in/WriteReadData/2019/210356.pdf |
| Statutory bonus, maximum | Twenty per cent of wages | Out of allocable surplus, s 26(3) | https://egazette.gov.in/WriteReadData/2019/210356.pdf |
| Gratuity | Fifteen days' wages per completed year (monthly wages / 26 x 15) | Code on Social Security s 53; five years' service unless an exception | https://egazette.gov.in/WriteReadData/2020/222111.pdf |
| Maternity benefit | Up to twenty-six weeks | Twelve weeks with two or more surviving children; Chapter VI | https://egazette.gov.in/WriteReadData/2020/222111.pdf |
| Maternity medical bonus (backgrounder) | 3,500 rupees | Where the employer gives no free pre-natal and post-natal care | https://static.pib.gov.in/WriteReadData/specificdocs/documents/2025/nov/doc20251122702601.pdf |
| Creche allowance (backgrounder) | Not less than 500 rupees per month per child, up to two children | Where a required creche is not provided | https://static.pib.gov.in/WriteReadData/specificdocs/documents/2025/nov/doc20251122702601.pdf |
| Profession tax, constitutional maximum | 2,500 rupees a year | State slabs in `in-professional-tax` | https://www.tgct.gov.in/tgportal/AllActs/APPT/APPTAct.aspx |
| Profession tax, Telangana salary bands | Nil to 15,000; 150 a month from 15,001 to 20,000; 200 a month above 20,000 | Monthly salary or wages | https://www.tgct.gov.in/tgportal/AllActs/APPT/APPTSchedule.aspx |

## The base

### How the employer deducts salary TDS

Under section 392(1) of the Income-tax Act 2025, any person responsible for paying income chargeable under the head "Salaries" deducts income-tax at the time of payment "at the average rate of income-tax computed on the basis of the rates in force for the tax year in which the payment is made, on the estimated income of the assessee under this head for such year". In practice: estimate the year's salary income, compute the tax for the year, and spread it over the remaining pay periods.

- The employee may give the employer details of salary from other employers in the same tax year, relief under section 157, a loss under "Income from house property", other income and other TDS. The employer must take them into account (section 392(4)(a); Form No. 122 under rule 204).
- The tax deducted from salary is never reduced except for a loss under "Income from house property" and tax deducted or collected under other provisions (section 392(4)(b)). Under the new regime, total income is computed without set off of any loss under "Income from house property" with any other head (section 202(2)(b)(ii)), so for an employee taxed under section 202(1) such a loss does not reduce salary TDS.
- The employer obtains the evidence or particulars of the employee's claims (section 392(5)(b)) in Form No. 124 (rule 205).
- The employer gives the employee a statement of perquisites and profits in lieu of salary (section 392(5)(a)): in Form No. 130 where the salary for the tax year is not more than the rates-table amount, otherwise in Form No. 123 (rule 204).
- For a non-monetary perquisite the employer may choose to pay the tax itself instead of deducting it (section 392(2)).
- Arrears or advance salary: relief under section 157 may apply when a sum in the nature of arrear or advance salary pushes income into a higher rate.
- An employee who does not give a valid PAN: tax is deducted at the higher of the rate in the Act, the rates in force, or 20% (section 397(2)(b)(i)).

### Which regime

The new regime in section 202(1) applies to every individual unless the person exercises the option in section 202(4). A salaried person with no income from business or profession exercises that option "along with the return of income to be furnished under section 263(1)" (section 202(4)(b)). Under the new regime, total income is computed without many exemptions and deductions (section 202(2)), including the deduction for profession tax (section 19(1) Table Sl. No. 1) and Chapter VIII deductions other than sections 124(1), 124(2), 125(2) and 146. The pages read do not set out how the employee tells the employer which regime to use for TDS during the year: see the refer list.

### Rebate and marginal relief

The section 156(2) rebate is for a resident individual only. Where total income under section 202(1) exceeds twelve lakh rupees, section 156(2)(b) cuts the tax to the amount by which total income exceeds twelve lakh rupees, if the tax would otherwise be higher. A non-resident employee gets neither rebate. Marginal relief on surcharge: income-tax plus surcharge "shall not exceed" the tax and surcharge on the threshold plus the income above it (new regime: Finance Act 2026 section 3(5), Tn = Rn + Sn; old regime: Part I-B Paragraph F Table 2, Wn = Un + Vn).

### Wages for the Labour Codes

Under section 2(y) of the Code on Wages, wages include basic pay, dearness allowance and retaining allowance, and exclude listed items (for example bonus, employer provident fund contributions, conveyance allowance, house rent allowance, overtime allowance and commission). If the excluded payments under clauses (a) to (i) exceed "one-half, or such other per cent. as may be notified" of all remuneration, the excess is added back to wages. The Code does not require a minimum basic salary; it adds the excess back, which raises the base for the Codes (the government backgrounder says this increases gratuity and similar benefits). Section 2(88) of the Code on Social Security has the same add-back, so provident fund contributions are on the Code's wages. The Ministry of Labour FAQ of 16 March 2026 confirms the definition applies from 21 November 2025 and that an overtime allowance forms part of the components, with any excess over 50 percent added to wages.

### Provident fund and ESI on the payslip

- Provident fund applies to establishments with twenty or more employees (Code on Social Security, First Schedule). Both shares are twelve per cent of wages up to the 25,000 rupee ceiling (from 17 September 2026), rounded to the nearest rupee; an employee above the ceiling on joining is an excluded employee unless both opt in writing (paragraph 9(4)). The employer pays both shares plus administrative charges within fifteen days of the close of every month and may never deduct its own share from wages (paragraphs 20 and 21). The employer is responsible for employees engaged through a contractor whose establishment is not registered independently (paragraph 20(2) to (4)).
- ESI applies to establishments with ten or more persons (one in a notified hazardous occupation); contributions start "on and from the date on which any benefits ... are provided by the Corporation" in the area, a date the Central Government notifies (First Schedule, Chapter IV, third proviso), though the government backgrounder of 21 November 2025 says coverage now applies pan-India with no notified-area limit and establishments with fewer than ten employees may opt in. Employee three-fourth per cent, employer three and one-fourth per cent, each rounded up to the next rupee; no employer share for a person with disability for up to three years (rule 19(2)). ESI due dates are in ESIC regulations no allowed page carries: confirm on the ESIC portal.
- Pension split, EDLI, administrative charges and all ESI detail: `in-pf-esi-employer`.

### Profession tax

A State tax on employment, capped by the Constitution at 2,500 rupees per person per year. Each State sets its own slabs, due dates and returns; many States levy none. The employer deducts it from salary where the State requires. Telangana is in the rates table as one schedule; other States via `in-professional-tax`. Income tax: deducted in full from salary under the old regime only.

### Minimum wage, hours and payment of wages (Code on Wages 2019)

The Code on Wages is in force from 21 November 2025 under S.O. 5322(E) and repealed the Payment of Wages Act 1936, the Minimum Wages Act 1948, the Payment of Bonus Act 1965 and the Equal Remuneration Act 1976 (section 69(1)). India does NOT have a single national minimum wage.

| Authority or parameter | Rule |
| --- | --- |
| Central Government | Fixes the floor wage "taking into account minimum living standards of a worker"; different floor wages may be fixed for different geographical areas (section 9(1)) |
| Appropriate Government (Central or State) | Fixes minimum rates of wages, which "shall not be less than the floor wage" (section 9(2)); reviews them at an interval not exceeding five years (section 8(4)) |
| Grades of work | Minimum wages take account of skill levels (unskilled, semi-skilled, skilled, highly skilled) and geographical area (government backgrounder of 21 November 2025) |
| Normal working day and weekly rest | Fixed by the appropriate Government (section 13(1)), "a day of rest in every period of seven days" |
| Overtime | For an employee whose minimum rate of wages is fixed under the Code, beyond a normal working day, not less than twice the normal rate (section 14) |
| Monthly-rated employees | Wages paid "before the expiry of the seventh day of the succeeding month" (section 17(1)(iv)) |
| Weekly, fortnightly, daily | Last working day of the week; before the end of the second day after the fortnight; end of the shift (section 17(1)) |
| Removal, dismissal, retrenchment, resignation, closure | Wages "within two working days" (section 17(2)) |
| Mode of payment | Coin, currency notes, cheque, credit to the bank account or electronic mode (section 15) |

No allowed official page read prints State minimum wage rates or the floor wage amount. Use the current notification of the appropriate Government for the employee's place of work and skill level.

### Mandatory benefits

| Benefit | Rule | Law |
| --- | --- | --- |
| Earned, casual and sick leave | Not covered; check the State's Shops and Establishments law and the Labour Code rules for the place of work | State law |
| Maternity benefit | Up to twenty-six weeks, of which not more than eight before the expected delivery; twelve weeks (not more than six before) for a woman with two or more surviving children. Applies to every factory, mine or plantation and every shop or establishment with ten or more employees on any day of the preceding twelve months | Code on Social Security, Chapter VI and First Schedule |
| Maternity eligibility | Worked at least 80 days in the 12 months before the expected delivery (backgrounder) | Chapter VI |
| Gratuity | See below | Chapter V, section 53 |
| Statutory bonus | See below | Code on Wages, Chapter IV |

**Gratuity (Code on Social Security s 53).** Payable by every factory, mine, oilfield, plantation, port and railway company and every shop or establishment with ten or more employees on any day of the preceding twelve months. Qualifying service: not less than five years of continuous service, on termination by superannuation, retirement, resignation, death, disablement, end of a fixed term or a notified event; no five-year condition for death, disablement, expiry of fixed-term employment or a notified event (second proviso). Rate: fifteen days' wages at the rate last drawn for every completed year or part over six months; for a monthly-rated employee, monthly wages last drawn divided by twenty-six, times fifteen; seasonal establishments seven days' wages for each season; fixed-term or deceased employees pro rata. Wages include any one-half add-back. The maximum is the amount notified by the Central Government; no allowed page read prints it, and notifications under the repealed Payment of Gratuity Act continue under section 164(2)(a) to the extent not contrary to the Code. Fixed-term employees: the backgrounder of 21 November 2025 and the Ministry FAQ of 16 March 2026 (reply 14) say they qualify after one year of service under the contract; the Code itself waives the five-year condition when the fixed term expires and pays pro rata. Follow the Code text and ask for advice on a fixed term that ends early. Contract labour: the contractor pays gratuity after five years' continuous service (FAQ reply 16, citing section 53).

Income tax on gratuity: under section 19 of the Income-tax Act 2025, gratuity for Government employees is exempt in full (Table Sl. No. 3); gratuity under the Payment of Gratuity Act 1972 is exempt as restricted to the amount under section 4(2) and (3) of that Act (Sl. No. 5); any other gratuity on retirement, incapacity or termination is exempt up to the least of the gratuity received, the notified amount, and half a month's salary for each completed year on the ten-month average (Sl. No. 6). Sl. No. 5 still names the repealed 1972 Act: refer.

**Statutory bonus (Code on Wages).** Applies to establishments in which twenty or more persons are employed or were employed on any day during an accounting year. Eligible employee: wages not above the monthly amount the appropriate Government notifies, and at least thirty days' work in the accounting year (section 26(1)). Minimum: eight and one-third per cent of wages earned or 100 rupees, whichever is higher, whether or not there is allocable surplus. Where wages exceed the notified amount, bonus is calculated as if the wage were that amount or the minimum wage, whichever is higher (section 26(2)). Maximum: twenty per cent of wages out of allocable surplus (section 26(3)). Paid to the employee's bank account within eight months of the close of the accounting year; extension possible, total not more than two years (section 39(1)). The eligibility wage and calculation ceiling are "determined by notification"; no allowed page read prints them.

### Payslip contents and CTC

Wage slips and registers are prescribed under the Labour Codes and their rules and under State Shops and Establishments law; the exact form was not on any allowed page read. The practical content of an Indian payslip (not a statutory form): employer name and establishment codes (EPFO and ESIC numbers); employee name, ID, designation, PAN; pay period; basic salary; dearness allowance and house rent allowance if applicable; special and other allowances; overtime; gross salary; provident fund employee deduction where a member; ESI employee deduction if covered; profession tax if the State levies it; TDS; other deductions (Labour Welfare Fund, advances, loans); net salary payable. Recommended: employer provident fund and ESI shown, leave balance, year-to-date figures.

CTC is a contract term, not a legal one. A typical CTC includes basic salary, DA, HRA, special allowance, employer provident fund, employer ESI where applicable, a gratuity provision and insurance premiums. No official source sets percentage splits. Check every structure against the one-half rule, because allowances above that share count as wages for the Codes.

## Deadlines and filing

### Income-tax Rules 2026: deposit, statements and certificates

| Item | Rule |
| --- | --- |
| Deposit of salary TDS, non-Government deductor (rule 218(2)) | Within seven days from the end of the month of deduction; salary credited or paid in March, by 30 April |
| Deposit, Government office (rule 218(1)) | Same day without challan; with challan, within seven days from the end of the month |
| Quarterly deposit in special cases, if the Assessing Officer permits with the prior approval of the Joint Commissioner (rule 218(4)) | 7 July, 7 October, 7 January, 30 April |
| Quarterly TDS statement for salary (rule 219(1), Table Sl. No. 1) | Form No. 138 |
| Statement due dates (rule 219(4)) | Quarter to 30 June: 31 July; to 30 September: 31 October; to 31 December: 31 January; to 31 March: 31 May after the tax year |
| Salary TDS certificate to the employee (rule 215(1)) | Form No. 130, by 15 June of the financial year after the tax year |
| Employee with more than one employer (rule 215(2)) | Each employer issues Parts A and B of Form No. 130; Part C by each or by the last employer, at the employee's option |
| Other salary income given by the employee (rule 204(1)) | Form No. 122 |
| Employee's evidence of claims (rule 205) | Form No. 124 |

For tax year 2026-27, Form No. 138 for the quarter to 30 June 2026 was due by 31 July 2026 and for the quarter to 30 September 2026 by 31 October 2026; the quarter to 31 December 2026 is due by 31 January 2027. Form No. 130 for the tax year is due by 15 June 2027.

### Payroll calendar

| Filing | Frequency | Deadline | Authority |
| --- | --- | --- | --- |
| Wages (monthly-rated) | Monthly | Before the expiry of the seventh day of the following month (Code on Wages s 17) | Paid to employees |
| Salary TDS deposit | Monthly | Within seven days from the end of the month; March: 30 April (rule 218) | Income Tax Department |
| Provident fund contributions and charges | Monthly | Within fifteen days of the close of every month (EPF Scheme 2026 para 20) | EPFO |
| ESI contributions | Monthly | Check the ESIC portal (no allowed page) | ESIC |
| Professional tax | State-specific | State law | State Government |
| Form No. 138 | Quarterly | 31 July, 31 October, 31 January, 31 May (rule 219(4)) | Income Tax Department |
| Form No. 130 | Annual | 15 June after the tax year (rule 215) | To employees |
| Statutory bonus | Annual | Within eight months of the close of the accounting year (Code on Wages s 39) | Paid to employees |

## Penalties and interest

| Violation | Consequence | Where |
| --- | --- | --- |
| Tax not deducted, or deducted and paid late | Interest at 1% or 1.5% per month or part (rates table); must be paid before the statement is furnished (s 398(3)(b)) | Section 398(3) |
| Late TDS statement | 200 rupees a day, not more than the tax deductible | Section 427 as substituted by the Finance Act 2026 |
| Statement not delivered on time, or incorrect | 10,000 to 1,00,000; for a late statement, none if delivered within one month with tax, fee and interest paid | Section 461 |
| Form No. 130 certificate or perquisite statement not furnished | 500 rupees a day, capped at the tax deductible for the certificate and the s 397(3)(b) statement (s 465(3)); no cap for the perquisite statement | Section 465(2) and (3) |
| Late provident fund payment | Damages per month on the arrears, not more than the arrears (see `in-pf-esi-employer`) | EPF Scheme 2026 para 23 |
| Late ESI payment | Check ESIC (no allowed page) | ESIC regulations |
| EPF appeal | Deposit of 25% of the amount determined before appealing (backgrounder; Code s 125 appeal) | Code on Social Security |

## Cross-border points

- A non-resident employee gets no section 156 rebate; residence is decided under `in-tax-residency`.
- International Workers (foreign passport holders) join the provident fund from the date of joining unless an excluded employee under a social security agreement: see `in-pf-esi-employer`.
- Expatriates, employees seconded abroad, stock options and sweat equity (section 392(3)) and arrears relief under section 157: refer.

## Two worked examples that recompute

All salaries are hypothetical; rates are from the rates table.

### Example 1: Resident employee, new regime, salary of 15,00,000 rupees for the year

Taxable salary 15,00,000 less 75,000 standard deduction = 14,25,000. Tax: 5% of 4,00,000 = 20,000, 10% of 4,00,000 = 40,000, 15% of 2,25,000 = 33,750; total 93,750. No rebate: income is above twelve lakh rupees, and the tax of 93,750 is less than the excess over twelve lakh (2,25,000), so section 156(2)(b) does not cut it. Cess 4% = 3,750. Tax for the year 97,500; TDS 8,125 a month over twelve months.

```oa-check
name: New regime salary 15,00,000, tax year 2026-27, monthly TDS
inputs:
  salary: 1500000
  std_deduction: 75000
steps:
  - taxable: salary - std_deduction
  - slab5: (min(taxable, 800000) - 400000) * 0.05
  - slab10: (min(taxable, 1200000) - 800000) * 0.10
  - slab15: (min(taxable, 1600000) - 1200000) * 0.15
  - tax: slab5 + slab10 + slab15
  - after_relief: min(tax, taxable - 1200000)
  - with_cess: after_relief * 1.04
  - monthly_tds: with_cess / 12
expected:
  taxable: 1425000
  tax: 93750
  with_cess: 97500
  monthly_tds: 8125
```

### Example 2: Salary of 12,85,000 rupees, new regime with marginal relief or old regime with 1,50,000 of Schedule XV claims

New regime: taxable 12,85,000 less 75,000 = 12,10,000. Tax before rebate 20,000 + 40,000 + 15% of 10,000 = 61,500. Section 156(2)(b) cuts it to the excess over twelve lakh rupees, 10,000; with cess 10,400. Old regime (employee opts out under s 202(4)): taxable 12,85,000 less 50,000 standard deduction less 1,50,000 section 123 claims = 10,85,000; tax 1,12,500 plus 30% of 85,000 = 1,38,000; with cess 1,43,520. The new regime is cheaper by 1,33,120, so TDS should run on the new regime. At a salary of 12,75,000 rupees taxable income is exactly twelve lakh rupees and the new regime tax is nil after the section 156(2)(a) rebate.

```oa-check
name: Salary 12,85,000, new regime with s 156(2)(b) relief against old regime with 1,50,000 claims
inputs:
  salary: 1285000
steps:
  - new_taxable: salary - 75000
  - new_tax: (400000 * 0.05) + (400000 * 0.10) + (new_taxable - 1200000) * 0.15
  - new_relieved: min(new_tax, new_taxable - 1200000)
  - new_total: new_relieved * 1.04
  - old_taxable: salary - 50000 - 150000
  - old_tax: 112500 + (old_taxable - 1000000) * 0.30
  - old_total: old_tax * 1.04
  - saving_new: old_total - new_total
expected:
  new_tax: 61500
  new_total: 10400
  old_total: 143520
  saving_new: 133120
```

A non-resident employee with taxable salary of 11,00,000 rupees on the new regime pays 20,000 + 30,000 = 50,000 plus 2,000 cess = 52,000, because section 156 is for residents only.

## Ask the client first

- In which State does each employee work, and how many people does the establishment employ (twenty or more for provident fund and bonus, ten or more for ESI, gratuity and maternity)?
- Has each employee said whether they will opt out of the new regime under section 202(4), and given Form No. 124 evidence for old-regime claims?
- Is each employee resident in India for tax year 2026-27? A non-resident gets no section 156 rebate.
- Does any employee have salary from another employer this tax year (Form No. 122)?
- What are the components of pay (basic, DA, HRA, allowances, overtime, commission)? If excluded payments exceed one-half of all remuneration, the excess is added back to wages.
- Are any employees on fixed-term contracts, engaged through a contractor, or persons with disability?

### The method, step by step

1. Fix the facts: State of employment, establishment headcount, each employee's residence, monthly wages and the regime the employee intends to use.
2. Compute wages for the Labour Codes, applying the one-half add-back.
3. Provident fund: twelve per cent each on wages up to the 25,000 rupee ceiling (detail in `in-pf-esi-employer`); pay within fifteen days of the close of the month.
4. ESI: if covered and within the ESI limit, deduct three-fourth per cent and add three and one-fourth per cent.
5. Professional tax: apply the State schedule (`in-professional-tax`).
6. Income tax: estimate the year's salary, take the standard deduction and other allowed items under section 19, compute tax at the regime's rates plus surcharge and cess, apply the section 156 rebate for residents, and deduct the average rate each month under section 392, using old regime rates only for an employee who opts out.
7. Pay monthly-rated wages by the seventh day of the following month, deposit TDS within seven days of the month end (March: 30 April), file Form No. 138 each quarter and issue Form No. 130 by 15 June after the tax year.
8. Year end: pay statutory bonus within eight months of the close of the accounting year and compute gratuity on exits under section 53.

### When to refuse or refer

- Salary for periods up to 31 March 2026 (1961 Act, Form 16): refer to the 1961 Act forms and the Income Tax Department.
- The ESI wage ceiling after 16 March 2026, the gratuity cap, the bonus eligibility wage, the floor wage and State minimum wages: no allowed page prints the current notified amounts. Confirm with ESIC or the notification.
- The split of the employer's provident fund share, EDLI and the EPFO administrative charge: `in-pf-esi-employer`, then EPFO.
- Which provident fund rate governs from 21 November 2025: section 16(1)(a) of the Code prints ten per cent with twelve per cent for notified establishments, while paragraph 18(2) of the EPF Scheme 2026 prints twelve per cent with ten per cent for a notified class. This skill uses the Scheme's twelve per cent; refer any dispute.
- How an employee's regime intention is given to the employer for TDS during the year: the Act ties the opt-out to the return; refer if an employee wants old-regime TDS.
- Gratuity tax exemption for gratuity paid under the Code: section 19 Table Sl. No. 5 still refers to the repealed 1972 Act. Refer to a Chartered Accountant.
- Expatriates, non-residents, secondments, stock options and sweat equity, arrears relief: refer.
- The 57th GST Council proposals and the Corporate Laws (Amendment) Bill 2026 are not law and do not change payroll.

## Sources

| Source | URL | Read on |
| --- | --- | --- |
| Read for Income-tax Act 2025 sections 19, 123, 124, 156, 157, 202, 392, 397, 398, 427, 461 and 465 (Gazette, Act 30 of 2025) | https://egazette.gov.in/WriteReadData/2025/265620.pdf | 2026-11-14 |
| Read for Finance Act 2026 section 3(4), 3(5), 3(10), First Schedule Part I-B Paragraphs A and F, Part III, and the substituted section 427 fee | https://egazette.gov.in/WriteReadData/2026/271439.pdf | 2026-11-14 |
| Read for Income-tax Rules 2026 rules 204, 205, 215, 218 and 219 | https://www.incometax.gov.in/iec/foportal/sites/default/files/2026-03/En-Notified-IT-Rules-2026-20-03-2026.pdf | 2026-11-14 |
| Read for EPF Scheme 2026 paragraphs 2, 9, 18, 19, 20, 21 and 23 | https://egazette.gov.in/WriteReadData/2026/273957.pdf | 2026-11-14 |
| Read for S.O. 5109(E), provident fund wage ceiling of 25,000 rupees from 17 September 2026 | https://egazette.gov.in/WriteReadData/2026/276299.pdf | 2026-11-14 |
| Read for Social Security (Central) Rules 2026 rule 19 | https://egazette.gov.in/WriteReadData/2026/272366.pdf | 2026-11-14 |
| Read for Ministry of Labour FAQ of 16 March 2026, replies 6 to 8, 11, 12, 14 and 16 | https://www.labour.gov.in/static/uploads/2026/03/a4ccf4c6d97c4f1f36a6d83f8c64213d.pdf | 2026-11-14 |
| Read for Code on Social Security 2020 sections 2(88), 16, 53, 164 and the First Schedule (Chapters III to VI) | https://egazette.gov.in/WriteReadData/2020/222111.pdf | 2026-11-14 |
| Read for Code on Wages 2019 sections 2(y), 8, 9, 13 to 17, 26, 39 and 69 | https://egazette.gov.in/WriteReadData/2019/210356.pdf | 2026-11-14 |
| Read for S.O. 5322(E), commencement of the Code on Wages on 21 November 2025 | https://egazette.gov.in/WriteReadData/2025/267885.pdf | 2026-11-14 |
| Read for S.O. 5936(E), corrigendum to S.O. 5319(E), 19 December 2025 | https://egazette.gov.in/WriteReadData/2025/268694.pdf | 2026-11-14 |
| Read for S.O. 2060(E), pension provisions in force 3 May 2023 | https://egazette.gov.in/WriteReadData/2023/245642.pdf | 2026-11-14 |
| Read for Employees' Deposit-Linked Insurance Scheme 2026, supersession of the 1976 scheme | https://egazette.gov.in/WriteReadData/2026/273942.pdf | 2026-11-14 |
| Read for Employees' Pension Scheme 2026, supersession of the 1995 scheme | https://egazette.gov.in/WriteReadData/2026/273951.pdf | 2026-11-14 |
| Read for the government backgrounder of 21 November 2025 (ESI pan-India and opt-in, fixed-term gratuity, minimum wage grades) | https://static.pib.gov.in/WriteReadData/specificdocs/documents/2025/nov/doc20251121701501.pdf | 2026-11-14 |
| Read for the government backgrounder of 22 November 2025 (50% add-back, 25% appeal deposit, maternity bonus 3,500, creche 500) | https://static.pib.gov.in/WriteReadData/specificdocs/documents/2025/nov/doc20251122702601.pdf | 2026-11-14 |
| Read for the Telangana constitutional maximum of Rs 2,500 a year | https://www.tgct.gov.in/tgportal/AllActs/APPT/APPTAct.aspx | 2026-11-14 |
| Read for the Telangana entry 1 salary bands | https://www.tgct.gov.in/tgportal/AllActs/APPT/APPTSchedule.aspx | 2026-11-14 |
| Income Tax Department, Salaried Individuals for AY 2026-27 (1961 Act forms) | https://www.incometax.gov.in/iec/foportal/help/individual/return-applicable-1 | Timed out on 2026-11-14, not read |

Not yet confirmed: the ESI wage ceiling under the Code after 16 March 2026; the gratuity cap under section 53(3); the bonus eligibility wage and calculation ceiling; the floor wage and State minimum wages; ESI payment due dates and return calendar; the statutory wage slip form; how an employee's regime choice is given to the employer for TDS during the year.
