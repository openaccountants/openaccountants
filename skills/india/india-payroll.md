---
name: india-payroll
description: Use this skill whenever asked about Indian payroll processing, employee salary calculations, TDS on salary (Section 192), Provident Fund (PF/EPF), Employee State Insurance (ESI), employer cost calculations, CTC breakdowns, net-to-gross or gross-to-net conversions, Indian payslip structure, Form 24Q/Form 138 filings, or any question about computing wages, deductions, or employer obligations in India. Trigger on phrases like "Indian payroll", "TDS on salary", "PF contribution", "ESI contribution", "EPF", "CTC breakdown", "new tax regime India", "old tax regime", "Form 16", "Form 130", "salary structure India", "basic DA HRA", "professional tax", "gratuity", "bonus India", or "minimum wages India".
version: 1.0
jurisdiction: IN
tax_year: 2026
last_updated: 2026-10-17
authored_by: Michael Cutajar and the OpenAccountants team
review_status: pending_review
trust_label: Built by Michael Cutajar and the OpenAccountants team
depends_on:
  - payroll-workflow-base
category: payroll
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# India Payroll: Salary TDS, Provident Fund, ESI, Professional Tax, Bonus and Gratuity

This Guide covers running payroll for employees in India: income tax deducted from salary, provident fund, Employees' State Insurance (ESI), professional tax, wages, bonus, gratuity, maternity benefit, payslips and the filing calendar. Figures are for tax year 2026. For income tax this means the tax year from 1 April 2026 to 31 March 2027 under the Income-tax Act 2025, which replaced the Income-tax Act 1961 from 1 April 2026. Salary paid up to 31 March 2026 belongs to the 1961 Act and its forms; this Guide does not cover it. The labour rules are those in force on 17 October 2026: the Code on Wages 2019 and the Code on Social Security 2020 came into force on 21 November 2025, the Social Security (Central) Rules 2026 (notification dated 8 May 2026) on publication, and the Employees' Provident Funds Scheme 2026 (notification dated 29 June 2026) on its publication in the Gazette. Rules, rates and section numbers from the old labour Acts (EPF Scheme 1952, ESI Act 1948, Payment of Bonus Act 1965, Payment of Gratuity Act 1972, Minimum Wages Act 1948) are out of date for current payroll unless this Guide says otherwise.

## Section 1: Quick Reference

| Field | Value |
| --- | --- |
| Country | India (Republic of India) |
| Currency | INR (Indian rupee) |
| Tax year | 1 April to 31 March. Tax year 2026-27 runs from 1 April 2026 to 31 March 2027 |
| Income tax law | Income-tax Act 2025 (30 of 2025) and the Income-tax Rules 2026; rates for the old regime and the surcharge in the Finance Act 2026 (4 of 2026) |
| Salary TDS section | Section 392 of the Income-tax Act 2025 |
| Labour law | Code on Wages 2019 (wages, minimum wages, overtime, bonus); Code on Social Security 2020 (provident fund, ESI, gratuity, maternity) |
| Provident fund law | Employees' Provident Funds Scheme 2026 (G.S.R. 525(E)), which supersedes the Employees' Provident Funds Scheme 1952 |
| ESI law | Code on Social Security 2020, Chapter IV, and the Social Security (Central) Rules 2026 (G.S.R. 344(E)) |
| Tax authority | Central Board of Direct Taxes, Income Tax Department |
| Provident fund authority | Employees' Provident Fund Organisation (EPFO) |
| ESI authority | Employees' State Insurance Corporation (ESIC) |
| Employee and employer provident fund | Twelve per cent of wages each (ten per cent for notified classes of establishment); see Section 3 |
| ESI | Employee three-fourth per cent, employer three and one-fourth per cent of wages; see Section 3 |
| Income tax regime | New regime under section 202(1) is the default; see Section 2 |
| Minimum wage | Fixed by the appropriate Government under the Code on Wages, not below the floor wage; no single national figure |

## Section 2: Income Tax Withholding (TDS on Salary)

### How the employer deducts

Under section 392(1) of the Income-tax Act 2025, any person responsible for paying income chargeable under the head "Salaries" deducts income-tax at the time of payment "at the average rate of income-tax computed on the basis of the rates in force for the tax year in which the payment is made, on the estimated income of the assessee under this head for such year" ([Income-tax Act 2025](https://egazette.gov.in/WriteReadData/2025/265620.pdf)). In practice: estimate the year's salary income, compute the tax for the year, and spread it over the remaining pay periods.

Under the 1961 Act the employer deducted under section 192 and issued Form 16 under section 203, and the employee's claims went on Form 12BB, as the Income Tax Department's page for AY 2026-27 shows ([ITD, Salaried Individuals for AY 2026-27](https://www.incometax.gov.in/iec/foportal/help/individual/return-applicable-1)). For tax year 2026-27 the section is 392 of the 2025 Act and the forms are those in the Rules table in Section 8 (Form No. 122, 123, 124, 130 and 138).

- The employee may give the employer details of salary from other employers in the same tax year, relief under section 157 (for a Government servant or an employee of a company, co-operative society, local authority, university, institution, association or body), a loss under "Income from house property", other income and other TDS. The employer must take them into account (section 392(4)(a); form: Form No. 122 under rule 204).
- The tax deducted from salary is never reduced except for a loss under "Income from house property" and tax deducted or collected under other provisions (section 392(4)(b)). Under the new regime, total income is computed "without set off of ... any loss under the head 'Income from house property' with any other head of income" (section 202(2)(b)(ii)), so for an employee taxed under section 202(1) such a loss does not reduce salary TDS.
- The employer obtains the evidence or particulars of the employee's claims (section 392(5)(b)) in Form No. 124 (rule 205 of the Income-tax Rules 2026).
- The employer gives the employee a statement of perquisites and profits in lieu of salary (section 392(5)(a)): in Form No. 130 where the salary for the tax year is not more than the amount in the Rules table in Section 8, otherwise in Form No. 123 (rule 204).
- For a non-monetary perquisite the employer may choose to pay the tax itself instead of deducting it (section 392(2)).
- Arrears or advance salary: relief under section 157 of the 2025 Act may apply when a sum in the nature of arrear or advance salary pushes income into a higher rate.
- An employee who does not give a valid Permanent Account Number: tax is deducted at the higher of the rate in the Act, the rates in force, or the rate in the table below (section 397(2)(b)(i)).

### Which regime

The new regime in section 202(1) applies to every individual unless the person exercises the option in section 202(4). A salaried person with no income from business or profession exercises that option "along with the return of income to be furnished under section 263(1)" for the tax year (section 202(4)(b)). Under the new regime, total income is computed without many exemptions and deductions (section 202(2)), including the deduction for tax on employment (professional tax) in section 19(1) Table Sl. No. 1, and Chapter VIII deductions other than sections 124(1), 124(2), 125(2) and 146. The pages read for this Guide do not set out how the employee tells the employer which regime to use for TDS during the year: see "When to refuse or refer".

### Income-tax Act 2025: rates and deductions for tax year 2026-27

| Item | Value | Note |
| --- | --- | --- |
| Source | all figures below | https://egazette.gov.in/WriteReadData/2025/265620.pdf |
| New regime (section 202(1)): income up to INR 400,000 | Nil | "Upto ₹400000 Nil" |
| New regime: above INR 400,000 up to INR 800,000 | 5% | "to ₹800000 5%" |
| New regime: above INR 800,000 up to INR 1,200,000 | 10% | "to ₹1200000 10%" |
| New regime: above INR 1,200,000 up to INR 1,600,000 | 15% | "to ₹1600000 15%" |
| New regime: above INR 1,600,000 up to INR 2,000,000 | 20% | "to ₹2000000 20%" |
| New regime: above INR 2,000,000 up to INR 2,400,000 | 25% | "to ₹2400000 25%" |
| New regime: above INR 2,400,000 | 30% | "Above ₹2400000 30%" |
| Standard deduction from salary where tax is computed under section 202(1) (section 19(1) Table Sl. No. 2(a)) | INR 75,000 or the salary, whichever is less | "₹ 75000 or the salary, whichever is less, where income-tax is computed under section 202(1)" |
| Standard deduction in any other case (old regime) (section 19(1) Table Sl. No. 2(b)) | INR 50,000 or the salary, whichever is less | "₹ 50000 or the salary, whichever is less, in any other case" |
| Tax on employment (professional tax) paid (section 19(1) Table Sl. No. 1); not allowed under section 202(1), see section 202(2)(a)(iv) | Entire amount | "tax on employment as per article 276(2) of the Constitution" |
| Rebate, resident individual taxed under section 202(1) (section 156(2)(a)) | INR 60,000 or the tax, whichever is less | "income-tax payable or ₹ 60000, whichever is less" |
| Income limit for that rebate (section 156(2)(a)) | twelve lakh rupees | "(a) the income does not exceed twelve lakh rupees" |
| Rebate, resident individual (section 156(1)) | INR 12,500 or the tax, whichever is less | "payable or ₹ 12500, whichever is less" |
| Total income limit for that rebate (section 156(1)) | INR 500,000 | "such total income does not exceed ₹ 500000" |
| Old regime only: cap on the Schedule XV sums (provident fund, life insurance and others) (section 123) | INR 150,000 | "Schedule XV, as does not exceed ₹ 150000" |
| Employer contribution to the notified pension scheme, deductible for the employee: Central or State Government employer (section 124(1)(a)) | 14% of salary | "(a) 14%, where such contribution is made by the employer being the Central Government" |
| Same, any other employer (section 124(1)(b)) | 10% of salary | "(b) 10%, where such contribution is made by an employer other than" |
| Same, any other employer, where total income is taxed under section 202(1) (section 124(2)) | 14% of salary | "as if for “10%” referred to in clause (b) of that sub-section, “14%” had been substituted" |
| TDS where the employee gives no valid PAN (section 397(2)(b)(i)(C)), if higher than the normal rate | 20% | "or 20% in any other case" |
| Interest, tax not deducted (from the date deductible to the date deducted) (section 398(3)(a)(i)), per month or part of a month | 1% | "(i) at 1% for every month or part of a month" |
| Interest, tax deducted but paid late (section 398(3)(a)(ii)), per month or part of a month | 1.5% | "(ii) at 1.5% for every month or part of a month" |
| Penalty the Assessing Officer may impose for not delivering the TDS statement on time or for incorrect information (section 461(1)) | INR 10,000 to INR 100,000 | "not be less than ₹10000 but which may extend to ₹100000" |
| Penalty per day while the employer fails to furnish the Form No. 130 certificate under section 395(4), the perquisite statement under section 392(5)(a) or the statement under section 397(3)(b) (section 465(2)(g), (i), (k)); for the certificate and the section 397(3)(b) statement, not more than the tax deductible (section 465(3)) | INR 500 | "₹500 for every day during which the following failures continue" |

Rebate rules, in the Act's words. The section 156(2) rebate is for a resident individual only. Where total income under section 202(1) exceeds twelve lakh rupees, section 156(2)(b) cuts the tax to the amount by which total income exceeds twelve lakh rupees, if the tax would otherwise be higher (marginal relief). A non-resident employee gets neither rebate.

The penalty in section 461(1) is not levied for a late statement if the tax, fee and interest were paid and the statement was delivered within one month of the due time (section 461(2)). Interest under section 398(3) must be paid before the statement is furnished (section 398(3)(b)).

### Finance Act 2026: old regime rates, surcharge, cess and late fee for tax year 2026-27

The old regime applies only to an employee who has opted out of section 202(1). Rates are in the First Schedule, Part I-B, Paragraph A of the Finance Act 2026; for salary TDS, section 3(10)(ii) applies the same rates printed in Part III, Paragraph A. The old regime surcharge is in Paragraph F of Part I-B (Part III for TDS); the new regime surcharge is in section 3(4)(b), Table Sl. No. 10.

| Item | Value | Note |
| --- | --- | --- |
| Source | all figures below | https://egazette.gov.in/WriteReadData/2026/271439.pdf |
| Old regime, individual under 60: income up to INR 250,000 | Nil | "where the total income does not Nil; exceed ₹ 250000" |
| Old regime, under 60: above INR 250,000 up to INR 500,000 | 5% | "exceeds 5% of the amount by which the total ₹ 250000" |
| Old regime, all ages: above INR 500,000 up to INR 1,000,000 (under 60: INR 12,500 plus 20% of the excess over INR 500,000) | 20% | "₹ 12500 plus 20% of the amount by ₹ 500000" |
| Old regime, all ages: above INR 1,000,000 (under 60: INR 112,500 plus 30% of the excess over INR 1,000,000) | 30% | "₹ 112500 plus 30% of the amount by ₹ 1000000" |
| Old regime, resident aged 60 or more but under 80: nil band | INR 300,000 | "does not Nil; exceed ₹ 300000" |
| Same age group: INR 10,000 plus 20% of income above INR 500,000 | INR 10,000 | "exceeds ₹ 10000 plus 20% of the amount by ₹ 500000" |
| Same age group: INR 110,000 plus 30% of income above INR 1,000,000 | INR 110,000 | "exceeds ₹ 110000 plus 30% of the amount by ₹ 1000000" |
| Old regime, resident aged 80 or more: nil band, then 20% | INR 500,000 | "not exceed ₹ 500000 (2) where the total income 20%" |
| Same age group: INR 100,000 plus 30% of income above INR 1,000,000 | INR 100,000 | "₹ 100000 plus 30% of the amount by" |
| Surcharge, both regimes: total income above INR 5,000,000 up to INR 10,000,000 | 10% | "not exceed ₹ 10000000, at the persons consisting of only rate of 10%" |
| Surcharge, both regimes: above INR 10,000,000 up to INR 20,000,000 | 15% | "exceeds ₹ 10000000 but does not exceed ₹ 20000000, at the" |
| Surcharge, new regime (section 202): total income, excluding dividend and certain capital gains, above INR 20,000,000 (the top rate; on dividend and those capital gains the surcharge does not go above 15%) | 25% | "198 of the said Act) exceeds ₹ 20000000, at the rate of 25%" |
| Surcharge, old regime: total income, excluding dividend and certain capital gains, above INR 50,000,000 (between INR 20,000,000 and INR 50,000,000 the rate is 25%) | 37% | "exceeds ₹ 50000000, at the rate of 37%" |
| Health and Education Cess, on income-tax plus surcharge | 4% | "calculated at the rate of 4% of such income-tax and surcharge" |
| Fee for a late TDS statement under section 397(3)(b) (section 427(1) as substituted), per day, not more than the tax deductible | INR 200 | "a sum of ₹ 200 for every day" |

Marginal relief on surcharge: where total income is just above a surcharge threshold in the table above, income-tax plus surcharge "shall not exceed" the tax and surcharge on the threshold amount plus the income above the threshold (new regime: section 3(5); old regime: Part I-B, Paragraph F, Table 2). Section 3(5), on the new regime: "the total amount payable as income-tax and surcharge thereon shall not exceed the amount determined as per the following formula" (Tn = Rn + Sn) ([Finance Act 2026](https://egazette.gov.in/WriteReadData/2026/271439.pdf)). Part I-B, Paragraph F, Table 2, on the old regime: the same words, with the formula Wn = Un + Vn.

## Section 3: Social Security: Employee Deductions

### Provident fund (Employees' Provident Funds Scheme 2026)

The Employees' Provident Funds Scheme 2026 was made under section 15(1)(a) of the Code on Social Security 2020 and supersedes the Employees' Provident Funds Scheme 1952. Paragraph 1(2): it comes into force on the date of its publication in the Official Gazette.

| Item | Value | Note |
| --- | --- | --- |
| Source | all rules below | https://egazette.gov.in/WriteReadData/2026/273957.pdf |
| Employer contribution (paragraph 18(2)) | twelve per cent of the wages payable | "at the rate of twelve per cent of the wages payable to the employee" |
| Employee contribution (paragraph 18(2)) | equal to the employer's contribution | "the employees’ contribution shall be equal to the employer’s contribution" |
| Reduced rate for notified classes of establishment (paragraph 18(2), first proviso) | ten per cent | "the rate of contribution shall be ten per cent in respect of the class of establishments notified" |
| Wage ceiling (paragraph 18(3)) | as notified by the Central Government | "subject to the wage ceiling limit, notified by the Central Government from time to time" |
| Basis (paragraph 18(4)) | wages actually drawn or payable during the month | "on the basis of wages actually drawn or payable during the month" |
| Rounding (paragraph 18(5)) | nearest rupee; fifty paise or more rounds up | "fifty paise or more to be counted as the next higher rupee" |
| Who pays first (paragraph 20(1)) | employer pays both shares plus administrative charges | "within fifteen days of the close of every month" |
| Employer share not recoverable from the employee (paragraph 21) | never deducted from wages | "the employer shall not be entitled to deduct the employer's contribution from the wages" |
| Damages for late payment, default of less than two months (paragraph 23), per month, not more than the arrears | 0.25% of arrears | "Less than two months 0.25%" |
| Damages, more than two months and less than four months | 0.50% of arrears | "0.50% less than four months" |
| Damages, more than four months | 1% of arrears | "More than four months 1%" |
| Employees' Enrolment Campaign 2026 (Annexure A) | ceases on 31 October 2026 | "cease to operate on the 31 st day of October, 2026" |

- An employee whose wage exceeds the ceiling when he would otherwise become a member is an "excluded employee" and need not join (paragraph 2(1)(f)), unless the employer and employee "jointly opt in writing" to enrol him (paragraph 9(4)); an existing member above the ceiling stays a member.
- Above the wage ceiling, employer and employee contributions are limited to the contribution on the ceiling (paragraph 18(3), first proviso). An employee may also opt to make additional voluntary contributions on wages above the ceiling; the employer may match them but has no obligation to, and pays additional administrative charges on those wages (paragraph 19).
- The amount of the wage ceiling is set by notification. No allowed official page read for this Guide prints it. Confirm it on the EPFO portal before computing contributions.
- Which establishments: Chapter III (Employees' Provident Fund) of the Code applies to "Every establishment in which twenty or more employees are employed" (First Schedule; [Code on Social Security 2020](https://egazette.gov.in/WriteReadData/2020/222111.pdf)).
- Pension part of the employer's share: section 16(1)(b)(i) of the Code pays into the Pension Fund "such sums from the employer's contribution under clause (a) not exceeding eight and one-third per cent. of the wages or such per cent. of wages as may be notified". Section 16(1)(b) has been in force since 3 May 2023 under S.O. 2060(E), and the rest of section 16 since 21 November 2025 under S.O. 5319(E) as corrected by S.O. 5936(E) ([S.O. 5936(E)](https://egazette.gov.in/WriteReadData/2025/268694.pdf)); see Section 10. Take the split of the employer's twelve per cent between the provident fund and the pension fund, and the Employees' Deposit Linked Insurance and administrative charge rates, from EPFO before filing the monthly return.
- Appeals: an employer appealing to the tribunal against an EPFO officer's order deposits the share of the amount determined shown in the table in Section 4 (Code on Social Security; government backgrounder).

### Employees' State Insurance (ESI)

| Item | Value | Note |
| --- | --- | --- |
| Source | all rules below | https://egazette.gov.in/WriteReadData/2026/272366.pdf |
| Employee contribution (rule 19(1)(b)), rounded to the next higher rupee | three-fourth per cent of the wages payable | "employee‘s contribution, a sum (rounded to the next higher rupee) equal to three-fourth per cent." |
| Employer contribution (rule 19(1)(a)), rounded to the next higher rupee | three and one-fourth per cent of the wages payable | "three and one- fourth per cent. of the wages payable to an employee" |
| Employee who is a person with disability (rule 19(2)) | no employer share for up to three years from the start of the contribution period | "the employer shall not be required to pay employer‘s share of contribution up to a maximum period of three years" |
| In force (rule 1(2)) | on publication; notification dated 8 May 2026 | "New Delhi, the 8th May, 2026 G.S.R. 344(E)" |

- Which establishments: Chapter IV of the Code applies to every establishment in which ten or more persons are employed, other than a seasonal factory, and also to an establishment in a hazardous or life-threatening occupation notified by the Central Government "in which even a single employee is employed" (First Schedule; [Code on Social Security 2020](https://egazette.gov.in/WriteReadData/2020/222111.pdf)). Contributions are payable "on and from the date on which any benefits ... are provided by the Corporation to the employees of the establishment", a date the Central Government notifies (First Schedule, Chapter IV, third proviso).
- Establishments with fewer than ten employees may join voluntarily, by mutual consent: see the table in Section 4.
- Which employees: coverage depends on a wage ceiling set by notification. No allowed official page read for this Guide prints the current amount. Confirm it with ESIC before deciding whether an employee is covered.
- Contribution due dates and the ESI return calendar are set in ESIC regulations that no allowed page carries. Confirm them on the ESIC portal.

### Professional tax

Professional tax is a State tax on employment. The Constitution caps it at the amount in the first table below per person per year. Each State sets its own slabs, due dates and returns; many States levy none. The employer deducts it from salary where the State requires and pays it to the State. Telangana is shown as one worked schedule. For other States use `in-professional-tax` and the State's own official schedule.

| Item | Value | Note |
| --- | --- | --- |
| Source | all figures below | https://www.tgct.gov.in/tgportal/AllActs/APPT/APPTAct.aspx |
| Constitutional ceiling on profession tax, per year | INR 2,500 | "subject to a maximum of Rs.2500/- p.a." |

| Item | Value | Note |
| --- | --- | --- |
| Source | all figures below | https://www.tgct.gov.in/tgportal/AllActs/APPT/APPTSchedule.aspx |
| Telangana, salary and wage earners, monthly salary or wages up to INR 15,000 | Nil | "(i) Up to 15,000 Nil" |
| Telangana, monthly salary or wages from INR 15,001 to INR 20,000 | INR 150 a month | "(ii) From 15,001 to 20,000 150 PM" |
| Telangana, monthly salary or wages above INR 20,000 | INR 200 a month | "(iii) Above 20,000 200 PM" |
| Telangana, directors of companies (other than Government nominees), per year | INR 2,500 | "Companies Registered under the Companies Act, 1956. 2500 PA" |

Income tax treatment: the employee deducts professional tax paid in full from salary income under the old regime only (Section 2, first table). Under the new regime section 202(2)(a)(iv) removes that deduction.

## Section 4: Social Security: Employer Contributions

- Provident fund: the employer pays its own twelve per cent plus the employee's equal share, plus administrative charges, within fifteen days of the close of every month (EPF Scheme 2026 paragraphs 18 and 20; table in Section 3). The employer is also responsible for employees engaged through a contractor where the contractor's establishment is not registered independently (paragraph 20(2) to (4)).
- ESI: the employer pays three and one-fourth per cent of wages and deducts the employee's three-fourth per cent (Social Security (Central) Rules 2026 rule 19; table in Section 3).
- Gratuity and bonus are employer costs; see Section 6.

### Government backgrounders on the Labour Codes

The two Press Information Bureau backgrounders below print in digits what the Codes print in words, and summarise changes. They are explanations, not law. Where the backgrounder and the Code differ, follow the Code.

| Item | Value | Note |
| --- | --- | --- |
| Source | all figures below | https://static.pib.gov.in/WriteReadData/specificdocs/documents/2025/nov/doc20251122702601.pdf |
| "Wages" for the Codes: if excluded pay-outs (bonus, HRA, conveyance, overtime, commission and similar) exceed this share of total remuneration, the excess is added back to wages | 50% | "exceed 50% of the total remuneration (or such percentage as notified by the Government), the excess amount will be added back to wages" |
| Deposit by an employer appealing to the tribunal against an EPFO officer's order | 25% of the amount determined | "deposit of 25% of the awarded amount determined by the EPFO officer" |
| Maternity medical bonus where the employer gives no free pre-natal and post-natal care | INR 3,500 | "medical bonus of ₹3,500" |
| Crèche allowance where a required crèche is not provided, per month per child, up to two children | at least INR 500 | "crèche allowance not less than ₹500 per month per child" |

| Item | Value | Note |
| --- | --- | --- |
| Source | rules below | https://static.pib.gov.in/WriteReadData/specificdocs/documents/2025/nov/doc20251121701501.pdf |
| ESI for establishments with fewer than 10 employees | voluntary, by mutual consent | "Establishments with fewer than 10 employees may voluntarily opt in with mutual consent of employers and employees" |
| Gratuity for fixed-term employees | backgrounder says after one year | "Fixed-term employees become eligible for gratuity after one year of continuous service" |

## Section 5: Minimum Wage and Overtime

All of this section is from the [Code on Wages 2019](https://egazette.gov.in/WriteReadData/2019/210356.pdf), in force from 21 November 2025 under [S.O. 5322(E)](https://egazette.gov.in/WriteReadData/2025/267885.pdf). The Code repealed the Payment of Wages Act 1936, the Minimum Wages Act 1948, the Payment of Bonus Act 1965 and the Equal Remuneration Act 1976 (section 69(1)).

India does NOT have a single national minimum wage.

| Authority | Coverage |
| --- | --- |
| Central Government | Fixes the floor wage "taking into account minimum living standards of a worker"; different floor wages may be fixed for different geographical areas (section 9(1)) |
| Appropriate Government (Central or State) | Fixes minimum rates of wages, which "shall not be less than the floor wage" (section 9(2)); reviews them "at an interval not exceeding five years" (section 8(4)) |
| Grades of work | Minimum wages take account of skill levels (unskilled, semi-skilled, skilled, highly skilled) and geographical area (government backgrounder of 21 November 2025) |

No allowed official page read for this Guide prints State minimum wage rates or the floor wage amount. Use the current notification of the appropriate Government for the employee's place of work and skill level.

### Working hours, overtime and payment of wages

| Parameter | Rule |
| --- | --- |
| Normal working day and weekly rest | Fixed by the appropriate Government (section 13(1)), "a day of rest in every period of seven days" |
| Overtime | For an employee whose minimum rate of wages is fixed under the Code, for work beyond a normal working day, "not be less than twice the normal rate of wages" (section 14) |
| Monthly-rated employees | Wages paid "before the expiry of the seventh day of the succeeding month" (section 17(1)(iv)) |
| Weekly, fortnightly, daily | Last working day of the week; before the end of the second day after the fortnight; end of the shift (section 17(1)) |
| Removal, dismissal, retrenchment, resignation, closure | Wages "within two working days" (section 17(2)) |
| Mode of payment | Coin, currency notes, cheque, credit to the bank account or electronic mode (section 15) |

### The "wages" definition (one-half rule)

Under section 2(y) of the Code on Wages, wages include basic pay, dearness allowance and retaining allowance, and exclude listed items (for example bonus, employer provident fund contributions, conveyance allowance, house rent allowance, overtime allowance and commission). But if the excluded payments under clauses (a) to (i) exceed "one-half, or such other per cent. as may be notified" of the all remuneration, the excess is added back to wages. The Code does not require a minimum basic salary; it adds the excess back into wages, which raises the base for the Code's purposes (the backgrounder in Section 4 says this increases gratuity and similar benefits). The EPF Scheme 2026 does not define wages; paragraph 2(2) gives words defined in the Code the Code's meaning, and section 2(88) of the Code on Social Security has the same one-half add-back, so provident fund contributions are on the Code's wages.

## Section 6: Mandatory Benefits

| Benefit | Rule | Law |
| --- | --- | --- |
| Earned, casual and sick leave | Not covered by this Guide; check the State's Shops and Establishments law and the Labour Code rules for the place of work | State law |
| Maternity benefit | Up to twenty-six weeks, of which not more than eight weeks before the expected delivery; twelve weeks (not more than six before) for a woman with two or more surviving children | Code on Social Security, Chapter VI |
| Maternity eligibility | Worked at least 80 days in the 12 months before the expected delivery (backgrounder) | Code on Social Security, Chapter VI |
| Maternity medical bonus; crèche allowance | Amounts in the backgrounder table in Section 4 | Code on Social Security, Chapter VI |
| Gratuity | Fifteen days' wages for each completed year (see below) | Code on Social Security, Chapter V, section 53 |
| Statutory bonus | Eight and one-third per cent of wages, up to twenty per cent (see below) | Code on Wages, Chapter IV |

Maternity benefit (Chapter VI) applies to every factory, mine or plantation and to "every shop or establishment in which ten or more employees are employed, or were employed, on any day of the preceding twelve months" (First Schedule, [Code on Social Security 2020](https://egazette.gov.in/WriteReadData/2020/222111.pdf)).

### Gratuity Calculation

| Item | Value | Note |
| --- | --- | --- |
| Source | all rules below | https://egazette.gov.in/WriteReadData/2020/222111.pdf |
| Who must pay (First Schedule, Chapter V) | every factory, mine, oilfield, plantation, port and railway company; every shop or establishment with ten or more employees on any day of the preceding twelve months | "in which ten or more employees are employed, or were employed, on any day of the preceding twelve months" |
| Qualifying service (section 53(1)) | not less than five years of continuous service, on termination by superannuation, retirement, resignation, death, disablement, end of a fixed term or a notified event | "continuous service for not less than five years" |
| No five-year condition (section 53(1), second proviso) | death, disablement, expiry of fixed-term employment, a notified event | "shall not be necessary where the termination of the employment of any employee is due to death or disablement or expiration of fixed term employment" |
| Rate (section 53(2)) | fifteen days' wages, at the rate of wages last drawn, for every completed year or part over six months | "fifteen days' wages or such number of days as may be notified by the Central Government" |
| Monthly-rated employee (section 53, Explanation) | monthly wages last drawn divided by twenty-six, multiplied by fifteen | "dividing the monthly rate of wages last drawn by him by twenty-six and multiplying the quotient by fifteen" |
| Seasonal establishment | seven days' wages for each season | "seven days' wages for each season" |
| Fixed-term employee or deceased employee | pro rata | "the employer shall pay gratuity on pro rata basis" |
| Maximum (section 53(3)) | the amount notified by the Central Government | "shall not exceed such amount as may be notified by the Central Government" |

- Formula for a monthly-rated employee: gratuity = monthly wages last drawn ÷ twenty-six × fifteen × completed years (a part year over six months counts as a year). Wages here are the Code's wages, including any add-back under the one-half rule in Section 5.
- Fixed-term employees: the backgrounder in Section 4 says they qualify after one year. The Code itself only waives the five-year condition when the fixed term expires and pays pro rata; it does not print "one year". Follow the Code text and ask for advice on a fixed term that ends early.
- The cap is set by notification; no allowed page read for this Guide prints the current amount. Notifications made under the repealed Payment of Gratuity Act continue under section 164(2)(a) of the Code to the extent not contrary to it. Confirm the cap before paying a large gratuity.
- Income tax: under section 19 of the Income-tax Act 2025, gratuity for Government employees is exempt in full (Table Sl. No. 3); gratuity received under the Payment of Gratuity Act 1972 is exempt as restricted to the amount under section 4(2) and (3) of that Act (Sl. No. 5); any other gratuity on retirement, incapacity or termination is exempt up to the least of the gratuity received, the amount the Central Government notifies, and half a month's salary for each completed year of service on the ten-month average (Sl. No. 6) ([Income-tax Act 2025](https://egazette.gov.in/WriteReadData/2025/265620.pdf)). Sl. No. 5 still names the 1972 Act, which the Code repealed: see "When to refuse or refer".

### Statutory Bonus

| Item | Value | Note |
| --- | --- | --- |
| Source | all rules below | https://egazette.gov.in/WriteReadData/2019/210356.pdf |
| Who must pay | establishments in which twenty or more persons are employed, or were employed, on any day during an accounting year | "establishment in which twenty or more persons are employed or were employed on any day during an accounting year" |
| Eligible employee (section 26(1)) | wages not above the monthly amount the appropriate Government notifies, and at least thirty days' work in the accounting year | "has put in at least thirty days work in an accounting year" |
| Minimum bonus (section 26(1)) | eight and one-third per cent of wages earned, or one hundred rupees, whichever is higher, whether or not there is allocable surplus | "eight and one-third per cent. of the wages earned by the employee or one hundred rupees, whichever is higher" |
| Calculation ceiling (section 26(2)) | where wages exceed the notified amount, bonus is calculated as if the wage were the notified amount or the minimum wage, whichever is higher | "calculated as if his wage were such amount, so determined by the appropriate Government or the minimum wage" |
| Maximum (section 26(3)) | twenty per cent of wages, out of allocable surplus | "subject to a maximum of twenty per cent. of such wages" |
| Payment deadline (section 39(1)) | credited to the employee's bank account within eight months of the close of the accounting year; extension possible, total not more than two years | "within a period of eight months from the close of the accounting year" |

The bonus eligibility wage and the calculation ceiling are both "determined by notification". No allowed page read for this Guide prints them, so this Guide gives no amount for them.

## Section 7: Payslip Requirements

Wage slips and registers are prescribed under the Labour Codes and their rules and under State Shops and Establishments law; the exact form was not on any allowed page read for this Guide. The list below is the practical content of an Indian payslip, not a statutory form.

| Element | Usual |
| --- | --- |
| Employer name and establishment code (EPFO and ESIC numbers) | Yes |
| Employee name, ID, designation, PAN | Yes |
| Pay period (month) | Yes |
| Basic salary | Yes |
| Dearness Allowance (DA) | If applicable |
| House Rent Allowance (HRA) | If applicable |
| Special and other allowances | Yes |
| Overtime earnings | If applicable |
| Gross salary | Yes |
| Provident fund employee deduction | Yes, where the employee is a member |
| ESI employee deduction | If covered |
| Professional tax | If the State levies it |
| TDS (income tax) | Yes |
| Other deductions (Labour Welfare Fund, advances, loans) | If applicable |
| Net salary payable | Yes |
| Employer provident fund and ESI contribution (shown) | Recommended |
| Leave balance | Recommended |
| Year-to-date earnings and deductions | Recommended |

### CTC (Cost to Company) structure

CTC is a contract term, not a legal one. A typical CTC includes basic salary, DA, HRA, special allowance, employer provident fund, employer ESI where applicable, a gratuity provision and insurance premiums. No official source sets percentage splits for CTC components. Check every structure against the one-half rule in Section 5, because allowances above that share count as wages for the Codes.

## Section 8: Filing Obligations

### Income-tax Rules 2026: deposit, statements and certificates

| Item | Value | Note |
| --- | --- | --- |
| Source | all figures below | https://www.incometax.gov.in/iec/foportal/sites/default/files/2026-03/En-Notified-IT-Rules-2026-20-03-2026.pdf |
| Deposit of salary TDS, non-Government deductor (rule 218(2)) | within seven days from the end of the month of deduction; salary credited or paid in March, by 30 April | "on or before seven days from the end of the month in which" |
| Deposit, Government office (rule 218(1)) | same day without challan; with challan, within seven days from the end of the month | "on the same day, where the tax is paid without production of an income-tax challan" |
| Quarterly deposit in special cases, if the Assessing Officer permits it with the prior approval of the Joint Commissioner (rule 218(4)) | 7 July, 7 October, 7 January, 30 April | "permit quarterly payment of the tax deducted under section 392(1)" |
| Quarterly TDS statement for salary (rule 219(1), Table Sl. No. 1) | Form No. 138 | "Section 392 [other than section 392(7)] and section 393(1) [Table: Sl. No. 8(iii)]. 138." |
| Statement due dates (rule 219(4)) | quarter to 30 June: 31 July; to 30 September: 31 October; to 31 December: 31 January; to 31 March: 31 May after the tax year | "30th June. 31st July of the financial year." |
| Salary TDS certificate to the employee (rule 215(1), Table Sl. No. 1) | Form No. 130, by 15 June of the financial year after the tax year | "Deduction or payment of tax under sections 130 By the 15th June of the financial year" |
| Employee with more than one employer in the year (rule 215(2)) | each employer issues Parts A and B of Form No. 130; Part C by each or by the last employer, at the employee's option | "each of the employers shall issue Part A and B of the certificate in Form No. 130" |
| Details of other salary income given by the employee (rule 204(1)) | Form No. 122 | "FORM NO. 122 [See rule 204(1)]" |
| Perquisite statement (rule 204): Form No. 130 columns if salary for the year is not more than this amount, otherwise Form No. 123 | INR 150,000 | "is not more than ₹ 150000; or (b) Form No. 123" |
| Employee's evidence of claims (rule 205) | Form No. 124 | "in Form No. 124, for the purpose of estimating his income" |

### Payroll calendar

| Filing | Frequency | Deadline | Authority |
| --- | --- | --- | --- |
| Salary TDS deposit | Monthly | Within seven days from the end of the month; March: 30 April (rule 218) | Income Tax Department |
| Provident fund contributions and charges | Monthly | Within fifteen days of the close of every month (EPF Scheme 2026 paragraph 20) | EPFO |
| ESI contributions | Monthly | Check the ESIC portal (no allowed page) | ESIC |
| Professional tax | State-specific | State law | State Government |
| Form No. 138 (quarterly TDS statement) | Quarterly | 31 July, 31 October, 31 January, 31 May (rule 219(4)) | Income Tax Department |
| Form No. 130 (TDS certificate to employees) | Annual | 15 June after the tax year (rule 215) | To employees |
| Statutory bonus | Annual | Within eight months of the close of the accounting year (Code on Wages section 39) | Paid to employees |
| Wages (monthly-rated) | Monthly | Before the expiry of the seventh day of the following month (Code on Wages section 17) | Paid to employees |

For tax year 2026-27 the Form No. 138 statement for the quarter to 30 June 2026 was due by 31 July 2026 and the one for the quarter to 30 September 2026 is due by 31 October 2026. Form No. 130 for the tax year is due by 15 June 2027.

### Penalties

| Violation | Consequence | Where |
| --- | --- | --- |
| Tax not deducted, or deducted and paid late | Interest at the monthly rates in the Income-tax Act table in Section 2 | Section 398(3) |
| Late TDS statement | Fee per day in the Finance Act table in Section 2, not more than the tax deductible | Section 427 as substituted by the Finance Act 2026 |
| Statement not delivered on time, or incorrect | Penalty in the range in the Income-tax Act table in Section 2; for a late statement, none if delivered within one month with tax, fee and interest paid | Section 461 |
| Form No. 130 certificate or perquisite statement not furnished | Penalty per day in the Income-tax Act table in Section 2, capped at the tax deductible for the certificate only (section 465(3)(b)); no cap for the perquisite statement | Section 465(2) and (3) |
| Late provident fund payment | Damages per month at the rates in the EPF Scheme table in Section 3, not more than the arrears | EPF Scheme 2026 paragraph 23 |
| Late ESI payment | Check ESIC (no allowed page) | ESIC regulations |

## Section 9: Common Payroll Patterns

All amounts in these patterns are hypothetical. They are written as plain numbers followed by "rupees" so they are not mistaken for legal limits. Rates come from the tables in Section 2.

### Pattern 1: TDS for a resident employee, new regime, salary of 15,00,000 rupees for the year

~~~
Salary for the year (hypothetical):          1,500,000 rupees
Less standard deduction (section 19):          -75,000 rupees
Taxable salary:                              1,425,000 rupees

Tax under section 202(1):
  first 400,000:                     nil
  next 400,000 at 5%:             20,000
  next 400,000 at 10%:            40,000
  remaining 225,000 at 15%:       33,750
  Tax:                            93,750 rupees
Rebate (section 156(2)): none, income above twelve lakh rupees,
  and 93,750 is not more than the excess over twelve lakh (225,000).
Cess at 4% on 93,750:              3,750
Tax for the year:                 97,500 rupees
TDS per month over twelve months:  8,125 rupees
~~~

### Pattern 2: Just above the rebate limit (marginal relief), salary of 12,85,000 rupees

~~~
Salary for the year (hypothetical):          1,285,000 rupees
Less standard deduction:                       -75,000 rupees
Taxable salary:                              1,210,000 rupees

Tax under section 202(1) before rebate:
  next 400,000 at 5%:             20,000
  next 400,000 at 10%:            40,000
  remaining 10,000 at 15%:         1,500
  Tax before rebate:              61,500 rupees
Excess of income over twelve lakh rupees:     10,000 rupees
Section 156(2)(b): tax cut to the excess:     10,000 rupees
Cess at 4% on 10,000:                            400
Tax for the year:                             10,400 rupees
~~~

The same employee at a salary of 12,75,000 rupees has taxable income of exactly twelve lakh rupees and pays no tax after the section 156(2)(a) rebate.

### Pattern 3: Non-resident employee, same regime, taxable salary of 11,00,000 rupees

~~~
Taxable salary (hypothetical):               1,100,000 rupees
  next 400,000 at 5%:             20,000
  remaining 300,000 at 10%:       30,000
  Tax:                            50,000 rupees
Rebate: none. Section 156 is for resident individuals only.
Cess at 4% on 50,000:              2,000
Tax for the year:                 52,000 rupees
~~~

### Pattern 4: Provident fund and ESI for one month

Provident fund: twelve per cent of wages from the employee and the same from the employer, both limited to the notified wage ceiling unless both opt for higher wages. ESI, where the employee is covered: three-fourth per cent of wages from the employee, three and one-fourth per cent from the employer, each rounded up to the next rupee. Confirm the wage ceilings with EPFO and ESIC before running the numbers.

## Section 10: Interaction with Other Guides

| Guide | Interaction |
| --- | --- |
| `in-pf-esi-employer` | Detailed provident fund and ESI employer procedure |
| `in-professional-tax` | State professional tax slabs and registration |
| `in-income-tax` | The employee's own return, regime choice and other income |
| `in-tds-freelance` | TDS on payments to contractors and professionals (not salary) |
| `in-tax-residency` | Whether an employee is resident, which decides the section 156 rebate |
| `india-tax-optimization` | Old versus new regime planning |
| `india-einvoice` | No direct interaction (e-invoicing is GST; payroll is separate) |

### India-specific payroll considerations

- Labour Codes: the Code on Wages and the Code on Social Security are in force from 21 November 2025. S.O. 5319(E), the commencement notification for the Code on Social Security, as first printed brought into force only clause (c) of section 16(1) and items 1, 2 and 4 to 9 of section 164(1). A corrigendum, S.O. 5936(E) of 19 December 2025, replaced those entries with "section 16 except the provisions of the Code specified at serial numbers (ii), (iii) and (iv) of S.O.2060(E), dated the 3rd May, 2023" and "sub-section (1) of section 164 except the provisions of the Code specified at serial number (vi) of S.O.2060(E), dated the 3rd May, 2023" ([S.O. 5936(E)](https://egazette.gov.in/WriteReadData/2025/268694.pdf)). The excepted provisions were already in force from 3 May 2023 under S.O. 2060(E) ([S.O. 2060(E)](https://egazette.gov.in/WriteReadData/2023/245642.pdf)): section 16(1)(b), section 16(1)(a) so far as it relates to the Employees' Pension Scheme 1995, and the repeal (under section 164(1)) of the corresponding provisions of the EPF Act 1952. So all of section 16 and the repeal of the EPF Act 1952 are in force from 21 November 2025 (the pension parts from 3 May 2023). Section 164(2)(b), brought in by the same corrigendum, kept the EPF Scheme 1952, the EDLI Scheme 1976, the Employees' Pension Scheme 1995 and the ESI rules and regulations in force, to the extent not inconsistent with the Code, "for a period of one year from the date of commencement of this Code". The EPF Scheme 2026, the Employees' Deposit-Linked Insurance Scheme 2026 ([G.S.R., Gazette 2026/273942](https://egazette.gov.in/WriteReadData/2026/273942.pdf)) and the Employees' Pension Scheme 2026 ([Gazette 2026/273951](https://egazette.gov.in/WriteReadData/2026/273951.pdf)) supersede the 1952, 1976 and 1995 schemes (the Pension Scheme 2026 also the Family Pension Scheme 1971), each in force on its publication.
- Dual tax regime: the new regime is the default; the employee opts out under section 202(4).
- State variations: minimum wages, professional tax, Shops and Establishments rules and Labour Welfare Fund all vary by State. Always identify the State of employment.
- ESI coverage: the government backgrounder of 21 November 2025 says ESIC coverage now applies pan-India, with no notified-area limit. The Code itself still starts contributions from that notified date (Section 3); confirm it with ESIC.

## The method, step by step

1. Fix the facts: State of employment, establishment headcount, each employee's residence, monthly wages and the regime the employee intends to use. Residence: `in-tax-residency`.
2. Compute wages for the Labour Codes, applying the one-half add-back in section 2(y) of the [Code on Wages 2019](https://egazette.gov.in/WriteReadData/2019/210356.pdf).
3. Provident fund: if the establishment has twenty or more employees ([Code on Social Security 2020](https://egazette.gov.in/WriteReadData/2020/222111.pdf), First Schedule), deduct the employee share and add the employer share at twelve per cent of wages up to the notified ceiling (an employee above the ceiling on joining is an excluded employee unless both opt in under paragraph 9(4)) under paragraph 18 of the [EPF Scheme 2026](https://egazette.gov.in/WriteReadData/2026/273957.pdf); pay within fifteen days of the close of the month.
4. ESI: if the establishment has ten or more persons and the employee is within the notified wage ceiling, deduct three-fourth per cent and add three and one-fourth per cent under rule 19 of the [Social Security (Central) Rules 2026](https://egazette.gov.in/WriteReadData/2026/272366.pdf).
5. Professional tax: apply the State schedule (Telangana example on the [Telangana schedule](https://www.tgct.gov.in/tgportal/AllActs/APPT/APPTSchedule.aspx); others via `in-professional-tax`).
6. Income tax: estimate the year's salary income, take the standard deduction and other allowed items under section 19, compute tax at the regime's rates plus surcharge and cess, apply the section 156 rebate for residents, and deduct the average rate each month under section 392 of the [Income-tax Act 2025](https://egazette.gov.in/WriteReadData/2025/265620.pdf), using the old regime rates in the [Finance Act 2026](https://egazette.gov.in/WriteReadData/2026/271439.pdf) only for an employee who opts out.
7. Pay wages by the seventh day of the following month for monthly-rated staff (Code on Wages section 17), deposit TDS within seven days of the month end (March: 30 April), file Form No. 138 each quarter and issue Form No. 130 by 15 June after the tax year under rules 215, 218 and 219 of the [Income-tax Rules 2026](https://www.incometax.gov.in/iec/foportal/sites/default/files/2026-03/En-Notified-IT-Rules-2026-20-03-2026.pdf).
8. Year end: pay statutory bonus within eight months of the close of the accounting year (Code on Wages section 39) and compute gratuity on exits under section 53 of the [Code on Social Security 2020](https://egazette.gov.in/WriteReadData/2020/222111.pdf).

## Ask the client first

- In which State does each employee work, and how many people does the establishment employ (twenty or more for provident fund and bonus, ten or more for ESI, gratuity and maternity)?
- Has each employee said whether they will opt out of the new regime under section 202(4), and given Form No. 124 evidence for old-regime claims?
- Is each employee resident in India for tax year 2026-27? A non-resident gets no section 156 rebate.
- Does any employee have salary from another employer this tax year (Form No. 122)?
- What are the components of pay (basic, DA, HRA, allowances, commission)? If excluded payments exceed one-half of all remuneration, the excess is added back to wages.
- Are any employees on fixed-term contracts, engaged through a contractor, or persons with disability?

## When to refuse or refer

- Salary for periods up to 31 March 2026 (1961 Act, Form 16): refer to the 1961 Act forms and the Income Tax Department; this Guide does not cover them.
- The provident fund or ESI wage ceiling, the gratuity cap or the bonus eligibility wage: no allowed page prints the current notified amounts. Do not quote a figure from memory; confirm with EPFO, ESIC or the notification.
- The split of the employer's provident fund share between the provident fund, the pension fund and insurance, and the EPFO administrative charge: confirm with EPFO.
- Which provident fund rate governs from 21 November 2025: section 16(1)(a) of the Code, now in force, prints "the contributions paid by the employer to the fund shall be ten per cent. of the wages for the time being payable", with twelve per cent. substituted only for establishments the Central Government notifies, while paragraph 18(2) of the EPF Scheme 2026 prints twelve per cent with ten per cent for a notified class (table in Section 3). No notification under the first proviso to section 16(1)(a) was read. This Guide uses the Scheme's twelve per cent; refer any dispute about the rate.
- How an employee's regime intention is given to the employer for TDS during the year: the Act ties the opt-out to the return; refer to the employer's tax adviser if an employee wants old-regime TDS.
- Gratuity tax exemption for gratuity paid under the Code: section 19 Table Sl. No. 5 still refers to the repealed Payment of Gratuity Act 1972. Refer to a Chartered Accountant.
- Expatriates, non-residents, employees seconded abroad, stock options and sweat equity (section 392(3)), and arrears relief under section 157: refer.
- The 57th GST Council proposals and the Corporate Laws (Amendment) Bill 2026 are not law and do not change payroll; no figure from them applies.

## Sources

- Income-tax Act 2025 (30 of 2025): https://egazette.gov.in/WriteReadData/2025/265620.pdf
- Finance Act 2026 (4 of 2026): https://egazette.gov.in/WriteReadData/2026/271439.pdf
- Income-tax Rules 2026 (G.S.R. 198(E), 20 March 2026): https://www.incometax.gov.in/iec/foportal/sites/default/files/2026-03/En-Notified-IT-Rules-2026-20-03-2026.pdf
- Income Tax Department, Salaried Individuals for AY 2026-27 (1961 Act forms): https://www.incometax.gov.in/iec/foportal/help/individual/return-applicable-1
- Employees' Provident Funds Scheme 2026 (G.S.R. 525(E)): https://egazette.gov.in/WriteReadData/2026/273957.pdf
- Social Security (Central) Rules 2026 (G.S.R. 344(E)): https://egazette.gov.in/WriteReadData/2026/272366.pdf
- Code on Social Security 2020: https://egazette.gov.in/WriteReadData/2020/222111.pdf
- Code on Wages 2019: https://egazette.gov.in/WriteReadData/2019/210356.pdf
- S.O. 5319(E), commencement of the Code on Social Security: https://egazette.gov.in/WriteReadData/2025/267882.pdf
- S.O. 5936(E), corrigendum to S.O. 5319(E), dated 19 December 2025: https://egazette.gov.in/WriteReadData/2025/268694.pdf
- S.O. 2060(E), commencement of pension-related provisions of the Code on Social Security, dated 3 May 2023: https://egazette.gov.in/WriteReadData/2023/245642.pdf
- Employees' Deposit-Linked Insurance Scheme 2026: https://egazette.gov.in/WriteReadData/2026/273942.pdf
- Employees' Pension Scheme 2026: https://egazette.gov.in/WriteReadData/2026/273951.pdf
- S.O. 5322(E), commencement of the Code on Wages: https://egazette.gov.in/WriteReadData/2025/267885.pdf
- Government backgrounder, Labour Codes, 21 November 2025: https://static.pib.gov.in/WriteReadData/specificdocs/documents/2025/nov/doc20251121701501.pdf
- Government backgrounder, Code on Social Security, 22 November 2025: https://static.pib.gov.in/WriteReadData/specificdocs/documents/2025/nov/doc20251122702601.pdf
- Telangana Commercial Taxes, Profession Tax Act page: https://www.tgct.gov.in/tgportal/AllActs/APPT/APPTAct.aspx
- Telangana Commercial Taxes, Profession Tax First Schedule: https://www.tgct.gov.in/tgportal/AllActs/APPT/APPTSchedule.aspx

## Disclaimer

This Guide and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this Guide. All outputs must be reviewed and signed off by a qualified professional before filing or acting upon.

The most up-to-date version of this Guide is maintained at openaccountants.com.

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
