---
name: nj-payroll
description: Tier 2 New Jersey content skill for employer payroll compliance covering tax year 2025. Includes the 10.75% Gross Income Tax top rate, supplemental wage rate 11.8%, NJ-927 single quarterly combined return for withholding/UI/TDI/FLI/WD, TDI rates split between employee (0.23%) and employer (0.93%), FLI 0.06% employee-only (post-2024 reduction), SUI wage base $43,300, ABC test contractor classification under NJ Wage and Hour Law, Earned Sick Leave Law 40-hour minimum, and the BAIT estimated payment schedule for PTE-electing pass-throughs.
jurisdiction: US-NJ
tax_year: 2026
last_updated: 2026-09-25
authored_by: OpenAccountants team
review_status: pending_review
trust_label: By OpenAccountants
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# New Jersey employer payroll: withholding, NJ-927, UI, TDI, FLI, workforce funds, NJ-W-3 and minimum wage (2026, with 2025 notes)

Figures are for 2026 unless a line says 2025. Worker contribution rates and wage bases run by calendar year. Employer unemployment rates run by fiscal rate year, July 1 to June 30 ([NJDOL rate information](https://www.nj.gov/labor/ea/employer-services/rate-info/)). Income tax withholding uses the rate tables in the Division of Taxation's NJ-WT booklet (September 2025 revision) and on Form NJ-W4 ([NJ-WT](https://www.nj.gov/treasury/taxation/pdf/current/njwt.pdf)). This Guide points to those tables and does not reproduce them. A dated section near the end covers 2025 payrolls.

## Scope and who this is for

- **Covers:** private employers with employees working in New Jersey. It covers:
  - New Jersey Gross Income Tax withholding, Form NJ-W4 and the NJ-WT rate tables;
  - deposits (Form NJ-500), the quarterly Form NJ-927 or NJ-927-W, and the WR-30 wage report;
  - worker and employer contributions for unemployment insurance (UI), temporary disability insurance (TDI, shown as "DI" on NJDOL tables), family leave insurance (FLI), and the Workforce Development Partnership and Supplemental Workforce funds (WF/SWF);
  - the annual reconciliation, Form NJ-W-3, and Form W-2 dates;
  - new hire reporting;
  - the minimum wage for 2025 and 2026;
  - Pennsylvania and New York residents, in summary;
  - the ABC test for UI, in summary.
- **Does not cover:**
  - federal payroll taxes (Forms 941, 940, W-2 federal rules);
  - the employee's own NJ-1040 or NJ-1040NR return;
  - the pass-through business alternative income tax (BAIT) and the Corporation Business Tax;
  - earned sick leave, pay frequency, final pay and other wage-and-hour rules apart from the minimum wage;
  - public employers, reimbursable nonprofits, agricultural employers, and household (domestic) employers beyond one boundary row;
  - private TDI or FLI plan design;
  - UI coverage of workers who work in more than one state.
- **Cross-border workers.** Where an employee lives or works outside New Jersey, residency, day allocation and the convenience rule are covered in the Guide **us-multi-state-residency-and-allocation**. Use it for any employee who is not a New Jersey resident working only in New Jersey.

## Ask the client first

- Is the business registered with New Jersey as an employer? It needs a federal employer identification number (FEIN) to withhold New Jersey tax ([NJ-WT](https://www.nj.gov/treasury/taxation/pdf/current/njwt.pdf)).
- Is it a new employer? When did it first become liable? It keeps new employer rates until it has three consecutive full or partial years of contribution experience ([NJDOL Employer Handbook, taxes and wages](https://www.nj.gov/labor/ea/help/employer_handbook/taxes_wages.shtml)).
- What rates are on its "Notice of Employer Contribution Rates" for July 2025 to June 2026, and for July 2026 to June 2027? NJDOL no longer mails individual rate notices. The employer downloads them from Employer Access ([NJDOL rate information](https://www.nj.gov/labor/ea/employer-services/rate-info/)).
- Is TDI or FLI covered by the State Plan or by an approved private plan?
- Where does each employee live, and where do they work, on how many days? Has every Pennsylvania resident signed Form NJ-165?
- Does every employee have a signed Form NJ-W4? Has anyone written "EXEMPT" on line 6, and in which year?
- How much New Jersey income tax did the employer withhold in the prior year? How much does it withhold each month now?
- Are any workers paid on Form 1099? Who decided they were contractors, and on what evidence?
- How many employees does it have? Is it a seasonal business? Both change the minimum wage.

## The method, step by step

1. **Register** online as a New Jersey employer. You need an FEIN. A corporate entity also needs its 10-digit New Jersey corporate ID from the Division of Revenue and Enterprise Services ([NJ-WT](https://www.nj.gov/treasury/taxation/pdf/current/njwt.pdf)).
   - **When an employer becomes liable:** it may be subject to the Unemployment Compensation Law once it employs one or more people and pays wages of $1,000 or more in a calendar year ([Employer Handbook, taxes and wages](https://www.nj.gov/labor/ea/help/employer_handbook/taxes_wages.shtml)).
   - An employer subject to the federal unemployment tax (FUTA) is automatically subject, unless New Jersey law excludes the services.
   - A business that acquires a subject employer's business, or substantially all its assets, becomes subject at once.
2. **Report each new hire.** Report each newly hired or rehired employee, and each employee who returns to work after a separation. Send the employee's name, address and Social Security number, and the employer's name, payroll address and FEIN, to the New Hire Operations Center run by the Department of Human Services ([Employer Handbook, UI](https://www.nj.gov/labor/ea/help/employer_handbook/ui.shtml)). Federal law requires the report no later than 20 days after the hire date. An employer that reports electronically may instead send 2 monthly transmissions, not less than 12 days nor more than 16 days apart. A state may set a shorter time ([42 U.S.C. 653a](https://www.law.cornell.edu/uscode/text/42/653a)).
3. **Collect Form NJ-W4** from each employee. Do not use the federal Form W-4 to work out New Jersey withholding: employees cannot claim personal exemptions on the federal form. Keep the NJ-W4 and send it to the Division only if asked ([NJ-WT](https://www.nj.gov/treasury/taxation/pdf/current/njwt.pdf)). Read the form this way ([Form NJ-W4](https://www.nj.gov/treasury/taxation/pdf/current/njw4.pdf)):
   - Box 1 (single) or box 3 (married/civil union partner separate) means Rate A.
   - Box 2, 4 or 5 with line 3 blank means Rate B.
   - If the employee enters a letter on line 3 from the wage chart, use the rate the employee chose (A to E). The chart is meant for joint filers, heads of household and qualifying widow(er)s where the spouse or civil union partner works, or the employee has more than one job or more than one source of income, and the combined total of all wages is greater than $50,000 ([Form NJ-W4](https://www.nj.gov/treasury/taxation/pdf/current/njw4.pdf)).
   - Line 4 gives the number of allowances. Line 5 gives any extra amount to withhold each pay.
   - **"EXEMPT" on line 6** is allowed only in these cases:
     - single, or married/civil union partner filing separately, with wages plus taxable nonwage income of $10,000 or less ([Form NJ-W4](https://www.nj.gov/treasury/taxation/pdf/current/njw4.pdf));
     - married/civil union couple filing jointly, with the couple's combined wages plus taxable nonwage income of $20,000 or less ([Form NJ-W4](https://www.nj.gov/treasury/taxation/pdf/current/njw4.pdf));
     - head of household or qualifying widow(er), with $20,000 or less ([Form NJ-W4](https://www.nj.gov/treasury/taxation/pdf/current/njw4.pdf)).
   - An exemption is good for one year only. The employee must file a new form each year.
4. **Work out whose wages are subject** ([NJ-WT](https://www.nj.gov/treasury/taxation/pdf/current/njwt.pdf)).
   - **New Jersey residents working in New Jersey:** withhold on all wages.
   - **New Jersey residents working in another state:** you need not withhold New Jersey tax only if all three of these apply:
     - the employee works totally outside New Jersey;
     - the employee is subject to the other state's withholding tax; and
     - that state's withholding equals or exceeds New Jersey's.
     If any one fails (for example, the employee works part of the time in New Jersey, or the other state's rate is lower), withhold New Jersey tax as well. Reduce it by the tax you withhold for the other state.
   - **Nonresidents:** withhold on pay for work done in New Jersey. If you do not have exact records of New Jersey earnings, allocate: days worked in New Jersey ÷ total days worked all year × total wages. If you use neither method, withhold on all pay, wherever earned.
   - **Pennsylvania residents:** do not withhold New Jersey tax if the employee gives you Form NJ-165. Otherwise, withhold (see step 5).
   - **Residents of Delaware, Nebraska, New York and similar states** who work from home for a New Jersey employer: see the convenience rule in the boundary table.
5. **Pennsylvania residents: take Form NJ-165.** New Jersey and Pennsylvania have a reciprocal agreement.
   - Keep the signed form on file. Do not send it to the Division. If the employee does not complete it, withhold New Jersey tax ([NJ-WT](https://www.nj.gov/treasury/taxation/pdf/current/njwt.pdf)).
   - By signing, the employee authorizes you to withhold Pennsylvania personal income tax instead. An employee who moves out of Pennsylvania must tell you within 10 days ([Form NJ-165](https://www.nj.gov/treasury/taxation/pdf/current/nj165.pdf)).
   - **Military spouses:** no New Jersey withholding only if both apply: the employee's spouse is a member of the armed forces present in New Jersey on military orders, and the employee files Form NJ-165 with a copy of the spousal military ID. Without both, withhold ([NJ-WT](https://www.nj.gov/treasury/taxation/pdf/current/njwt.pdf)).
6. **Compute withholding** from the NJ-WT rate tables or the percentage method, using the rate letter, allowances and any extra amount from the NJ-W4 ([NJ-WT](https://www.nj.gov/treasury/taxation/pdf/current/njwt.pdf)). See "Figures" for the allowance values and supplemental wages.
7. **Deduct worker contributions** each pay: UI, WF/SWF, TDI and FLI, at the calendar-year rates, up to each wage base. Stop each one when the employee's wages from you reach its base. TDI and FLI worker deductions apply only under the State Plan. Under an approved private plan, the worker's cost cannot be more than under the State Plan ([Employer Handbook, TDI and FLI](https://www.nj.gov/labor/ea/help/employer_handbook/tdi-fli.shtml)).
8. **Deposit withholding** under the monthly or weekly rules (see "Filing and payment"), using Form NJ-500.
9. **File Form NJ-927** (or NJ-927-W for weekly payers) and the **WR-30** each quarter, electronically, even for a quarter with no tax withheld. The NJ-927 reports income tax withheld and UI, SWF, WF, FLI and DI wages and contributions together ([NJ-WT](https://www.nj.gov/treasury/taxation/pdf/current/njwt.pdf)). The WR-30 lists each employee's Social Security number, name, gross wages paid and base weeks, for services in New Jersey only ([Employer Handbook, taxes and wages](https://www.nj.gov/labor/ea/help/employer_handbook/taxes_wages.shtml)).
10. **At year end:** give Forms W-2 to employees by the federal date, file Form NJ-W-3 with the W-2s electronically, and send New Jersey copies of 1099s where required (see "Filing and payment").
11. **Check the minimum wage** for the employer's size and type, and **test any contractor** against the ABC test.

## Figures for 2026 (and 2025 where they differ)

### Worker (employee) contributions, by calendar year ([NJDOL rate information](https://www.nj.gov/labor/ea/employer-services/rate-info/))

| Item | 2025 | 2026 |
| --- | --- | --- |
| UI | 0.3825% | 0.3825% |
| WF/SWF (combined) | 0.0425% | 0.0425% |
| TDI (DI) | 0.23% | 0.19% |
| FLI | 0.33% | 0.23% |
| Wage base for UI and WF/SWF | $43,300 | $44,800 |
| Wage base for worker TDI and FLI | $165,400 | $171,100 |

- UI and WF/SWF together are 0.425% of wages up to the UI base.
- Of the worker's 0.0425%, 0.0175% goes to the Supplemental Workforce Fund ([Employer Handbook, taxes and wages](https://www.nj.gov/labor/ea/help/employer_handbook/taxes_wages.shtml)).
- **Two bases.** Worker TDI and FLI use the higher base. Since January 1, 2020, the UI and employer DI base has been 28 times the statewide average weekly wage. The worker DI and FLI base has been 107 times that wage ([Employer Handbook, taxes and wages](https://www.nj.gov/labor/ea/help/employer_handbook/taxes_wages.shtml)).
- **2027 is already published:** $46,400 for UI, WF/SWF and employer TDI, and $177,100 for worker TDI and FLI. The 2027 worker rates are not yet published ([NJDOL rate information](https://www.nj.gov/labor/ea/employer-services/rate-info/)).
- **Two employers.** Each employer deducts up to the maximum on its own payroll. A worker whose deductions from two or more employers exceed the annual maximum claims the excess on the New Jersey income tax return with Form NJ-2450 ([Employer Handbook, taxes and wages](https://www.nj.gov/labor/ea/help/employer_handbook/taxes_wages.shtml)).

### Employer contributions, by fiscal rate year ([NJDOL rate information](https://www.nj.gov/labor/ea/employer-services/rate-info/); [Table C, July 2026 to June 2027](https://www.nj.gov/labor/ea/assets/PDFs/FY20262027%20TABLE%20C.pdf))

| New employer | July 2024 to June 2025 | July 2025 to June 2026 | July 2026 to June 2027 |
| --- | --- | --- | --- |
| UI | 2.9825% | 2.6825% | 2.6825% |
| WF/SWF | 0.1175% | 0.1175% | 0.1175% |
| Total UI plus WF/SWF | 3.1% | 2.8% | 2.8% |

- **New employer TDI (DI):** 0.5% in each of these three rate years ([NJDOL rate information](https://www.nj.gov/labor/ea/employer-services/rate-info/)).
- **The employer pays no FLI.** FLI is funded by workers ([NJDOL rate information](https://www.nj.gov/labor/ea/employer-services/rate-info/)).
- **Employer wage base:** employer UI, WF/SWF and TDI stop at $44,800 per employee for 2026 ($43,300 for 2025).
- **WF/SWF is carved out of the UI rate, not added to it.** Table C shows a total rate, of which 0.1000% goes to the Workforce Development fund and 0.0175% to the Supplemental Workforce fund. The rest is UI. So the 2.8% new employer rate for July 2026 to June 2027 is 2.6825% UI plus 0.1175% WF/SWF ([Table C](https://www.nj.gov/labor/ea/assets/PDFs/FY20262027%20TABLE%20C.pdf)).
- **Experience-rated employers.** From July 1 of the fourth year of liability, the UI rate depends on the employer's own reserve ratio ([Employer Handbook, taxes and wages](https://www.nj.gov/labor/ea/help/employer_handbook/taxes_wages.shtml)). NJDOL is using Table C for July 2026 to June 2027. On Table C, total rates for positive reserve ratios run from 0.5% (17.00% and over) to 3.6%. Deficit reserve ratios run from 5.1% to 5.8%. There is also a specially assigned rate of 5.4% (positive) or 5.8% (negative) ([Table C](https://www.nj.gov/labor/ea/assets/PDFs/FY20262027%20TABLE%20C.pdf)). Use the rate on the employer's notice.
- **Experience-rated TDI.** The employer's TDI rate is also experience-rated and shown on its notice.
- **Voluntary contribution.** An experience-rated employer may lower its UI rate by paying a voluntary contribution. NJDOL must receive it within 30 days of the date of the "Notice of Employer Contribution Rates" (Form UC-45 is the voluntary contribution report). Notices are now issued through Employer Access rather than mailed, so confirm the deadline with NJDOL. It lowers only the employer UI rate.
- **Rate years straddle calendar years.** A calendar-year payroll uses the old rate from January to June and the new rate from July to December. The wage base runs by calendar year.

### Withholding ([NJ-WT](https://www.nj.gov/treasury/taxation/pdf/current/njwt.pdf); [Form NJ-W4](https://www.nj.gov/treasury/taxation/pdf/current/njw4.pdf))

| Payroll period | Value of one allowance |
| --- | --- |
| Weekly | $19.20 |
| Biweekly | $38.40 |
| Semimonthly | $41.60 |
| Monthly | $83.30 |
| Annual | $1,000 |

- **The method.** Multiply the allowance value by the number of exemptions claimed, subtract the result from the wages for the period, and apply the rate table.
- **Rates.** The tables on Form NJ-W4 (1-21) start at 1.5%. The top rate is 11.8% on taxable wages over $1,000,000 a year. That top withholding rate is not the same as the income tax rate on the return.
- **Supplemental wages** (bonuses, commissions, overtime, tips, and payouts of unused sick or vacation time):
  - paid **at the same time** as regular wages: total the two and withhold on the combined payment;
  - paid **at a different time**: withhold without any of the employee's allowances.
  - NJ-WT sets no flat supplemental rate.
- **What is and is not in New Jersey wages** ([NJ-WT](https://www.nj.gov/treasury/taxation/pdf/current/njwt.pdf)):
  - 401(k) contributions up to the federal limit are excluded. Any excess over the federal limit is included.
  - Employee contributions to other retirement plans are included in the year they are made.
  - State Plan and private plan TDI benefits are not subject to withholding.

### Minimum wage ([NJDOL minimum wage chart, MW-571 (1/26)](https://www.nj.gov/labor/wageandhour/assets/PDFs/MW-571%20%281-26%29%20MinWageFlier.pdf))

| Employer or worker | From January 1, 2025 | From January 1, 2026 |
| --- | --- | --- |
| Most employers | $15.49 | $15.92 |
| Seasonal employers and small employers (fewer than 6 employees) | $14.53 | $15.23 |
| Agricultural employers | $13.40 | $14.20 |
| Cash wage for tipped employees | $5.62 | $6.05 |
| Long-term care facility direct care staff | $18.49 | $18.92 |

- "Small" means **fewer than 6** employees. An employer with 6 or more pays the general rate.
- The minimum wage may continue to rise each January 1 with inflation.
- **2027:** the Department's worker FAQ already says the minimum wage is $16.48 per hour for most workers from January 1, 2027, with a tipped cash wage of at least $6.61 ([Wage and Hour FAQ](https://www.nj.gov/labor/wageandhour/support/faqs/wageandhourworkerfaqs.shtml)). The chart for 2027 is not yet out, so check it before January 2027.
- **Tipped workers:** hourly pay plus tips must reach the full minimum wage. If they do not, the employer makes up the difference.
- Some workers are excluded, such as automobile salespersons and outside salespersons. Minors under 18 are also excluded, except in retail, food service and certain other listed occupations ([Wage and Hour FAQ](https://www.nj.gov/labor/wageandhour/support/faqs/wageandhourworkerfaqs.shtml)).
- **Base week (for WR-30):** a week in which the employee earned at least $310 in 2026 ($303 in 2025) ([NJDOL rate information](https://www.nj.gov/labor/ea/employer-services/rate-info/)).

## Boundaries and exceptions

| Rule | Condition that decides it | Source |
| --- | --- | --- |
| Monthly deposit (NJ-500) | Only for the first or second month of a quarter in which tax withheld was **more than $500**. The third month is always paid with the quarterly return | [NJ-WT](https://www.nj.gov/treasury/taxation/pdf/current/njwt.pdf) |
| Weekly payer (NJ-927-W) | Prior-year income tax withheld of **$10,000 or more**. Pay by the Wednesday after the pay week, on your own payroll cycle | [NJ-WT](https://www.nj.gov/treasury/taxation/pdf/current/njwt.pdf) |
| NJ resident working elsewhere | No New Jersey withholding only if **all three** apply: works totally outside New Jersey, subject to the other state's withholding, and that withholding is at least New Jersey's | [NJ-WT](https://www.nj.gov/treasury/taxation/pdf/current/njwt.pdf) |
| Pennsylvania resident | No New Jersey withholding only with a signed NJ-165 on file. The agreement covers wage income tax. It does not excuse a Pennsylvania employer from Pennsylvania local wage taxes | [NJ-WT](https://www.nj.gov/treasury/taxation/pdf/current/njwt.pdf); [Form NJ-165](https://www.nj.gov/treasury/taxation/pdf/current/nj165.pdf) |
| Convenience rule (from tax year 2023) | Applies only to residents of states with a similar test, such as Delaware, Nebraska and New York. It uses the other state's test. It reaches only an employee whose primary or assigned office is in New Jersey: a New York resident with a New Jersey office who works from home for their own convenience is taxed as working in New Jersey. If the employee performs no services in New Jersey in the year, the wages are not New Jersey-source, even with a New Jersey employer. It does not apply to Pennsylvania residents. It does not apply to a Connecticut home worker | [Convenience rule](https://www.nj.gov/treasury/taxation/conveniencerule.shtml); [Convenience rule FAQ](https://www.nj.gov/treasury/taxation/conveniencerulefaq.shtml) |
| NJ-W4 "EXEMPT" | $10,000 or less (single or separate), or $20,000 or less (joint, head of household, qualifying widow(er)), including taxable nonwage income. Valid one year only | [Form NJ-W4](https://www.nj.gov/treasury/taxation/pdf/current/njw4.pdf) |
| TDI/FLI private plan | Must be approved. While it is in force, the employer and workers pay no State Plan TDI contributions. The worker's cost cannot exceed the State Plan | [Employer Handbook, TDI and FLI](https://www.nj.gov/labor/ea/help/employer_handbook/tdi-fli.shtml) |
| Household (domestic) employer | Subject to UI once it pays **$1,000 or more** in cash to domestic labor in a calendar quarter. It files once a year: NJ-WT gives January 31 for Form NJ-927-H, while NJDOL gives January 30 for the domestic NJ-927 and four WR-30s, so file by January 30 (by Friday, January 29, 2027 for 2026, as January 30 is a Saturday). Income tax withholding for a household worker is required where federal withholding is required; otherwise the employee may choose it. With regular employees as well, it files NJ-927 quarterly | [NJ-WT](https://www.nj.gov/treasury/taxation/pdf/current/njwt.pdf); [Employer Handbook, taxes and wages](https://www.nj.gov/labor/ea/help/employer_handbook/taxes_wages.shtml) |
| Unregistered construction contractor | Anyone paying an unregistered, unincorporated contractor for construction services must get its Business Registration Certificate or withhold 7% of the payment. Exempt: government agencies, homeowners and tenants for their principal residence, and incorporated contractors | [NJ-WT](https://www.nj.gov/treasury/taxation/pdf/current/njwt.pdf) |
| Worker vs contractor (UI) | An **employee** unless **all three** ABC prongs are met. See the ABC section below | [ABC test](https://www.nj.gov/labor/ea/audit/independent-contractor-vs-employees) |

### Worker classification: the ABC test for UI ([NJDOL, independent contractors vs employees](https://www.nj.gov/labor/ea/audit/independent-contractor-vs-employees))

A worker who is paid for services is an employee under the Unemployment Compensation Law unless **all** of these apply:

- **A:** the worker has been and will stay free from control or direction over the work, both under the contract and in fact;
- **B:** the work is outside the usual course of the business, or it is done outside all of the business's places of business; and
- **C:** the worker is customarily engaged in an independently established trade, occupation, profession or business.

Failing any one prong makes the worker an employee. The law is remedial and read liberally, so a worker can be an employee even where the common-law test would say otherwise. For prong C, the business must be one that will survive the end of this relationship. NJDOL auditors use the Worker Classification Questionnaire. This Guide gives a summary only: refer any real classification decision. Refer also where the question is worker status for wage-and-hour or wage payment purposes (including the minimum wage), or construction work, which has its own Construction Industry Independent Contractor Act.

## Worked cases

The dollar amounts in these cases are made up for illustration. The rates and bases come from the sources linked in each heading.

### Case 1: 2026 worker deductions ([NJDOL rate information](https://www.nj.gov/labor/ea/employer-services/rate-info/))

- **Employee paid $60,000 in 2026, State Plan:**
  - UI and WF/SWF: 0.425% × $44,800 = $190.40 (wages above the base carry no UI deduction);
  - TDI: 0.19% × $60,000 = $114.00;
  - FLI: 0.23% × $60,000 = $138.00.
- **Employee paid $200,000 in 2026:**
  - UI and WF/SWF: $190.40;
  - TDI: 0.19% × $171,100 = $325.09;
  - FLI: 0.23% × $171,100 = $393.53;
  - total $909.02. Stop each deduction once its base is reached.
- **The same employee in 2025:**
  - UI and WF/SWF: 0.425% × $43,300 = $184.03;
  - TDI: 0.23% × $165,400 = $380.42;
  - FLI: 0.33% × $165,400 = $545.82.

### Case 2: new employer contributions in 2026 ([NJDOL rate information](https://www.nj.gov/labor/ea/employer-services/rate-info/); [Table C](https://www.nj.gov/labor/ea/assets/PDFs/FY20262027%20TABLE%20C.pdf))

- **Facts:** a new employer pays one employee $5,000 a month in 2026.
- The new employer rates are the same in both rate years that touch 2026, so one rate applies all year:
  - UI and WF/SWF: 2.8% × $44,800 = $1,254.40;
  - TDI: 0.5% × $44,800 = $224.00;
  - FLI: nothing for the employer.
- **By quarter:** taxable wages are $15,000 in Q1 and $15,000 in Q2. In Q3, only $14,800 is taxable, because $44,800 minus the $30,000 already paid leaves $14,800. Q4 has no taxable wages. The WR-30 still reports all gross wages each quarter.
- **2025 variation:** the rate was 3.1% for January to June 2025 and 2.8% from July 2025, so split the year's taxable wages by rate year.

### Case 3: deposit timing ([NJ-WT](https://www.nj.gov/treasury/taxation/pdf/current/njwt.pdf))

- **Facts:** the employer withheld less than $10,000 in 2025, so it is not a weekly payer in 2026. In Q1 2026 it withholds $650 in January and $400 in February.
- **January:** $650 is more than $500, so pay it on Form NJ-500 by February 15.
- **February:** $400 is not more than $500, so no monthly payment is due. It is paid with the Q1 NJ-927, together with March, by April 30.
- **Variation:** had the employer withheld $10,000 or more in 2025, it would be a weekly payer in 2026. It would pay by the Wednesday after each pay week and file Form NJ-927-W.

### Case 4: Pennsylvania resident working in New Jersey ([NJ-WT](https://www.nj.gov/treasury/taxation/pdf/current/njwt.pdf); [Form NJ-165](https://www.nj.gov/treasury/taxation/pdf/current/nj165.pdf))

- A Pennsylvania resident works full time at a Camden office.
- **With a signed NJ-165:** withhold no New Jersey income tax, and withhold Pennsylvania personal income tax instead.
- **Without the form:** withhold New Jersey tax.
- **Contributions still apply.** The agreement is about income tax. The employee still works in New Jersey, so New Jersey UI, WF/SWF, TDI and FLI apply, and the wages go on the WR-30. The WR-30 covers services in New Jersey ([Employer Handbook, taxes and wages](https://www.nj.gov/labor/ea/help/employer_handbook/taxes_wages.shtml)).
- **If the employee moves** to New Jersey or elsewhere, they must tell the employer within 10 days, and the NJ-165 no longer applies.

### Case 5: New York residents and New Jersey residents working in New York ([NJ-WT](https://www.nj.gov/treasury/taxation/pdf/current/njwt.pdf); [Convenience rule](https://www.nj.gov/treasury/taxation/conveniencerule.shtml))

- **New York resident, New Jersey employer.** The employee's assigned office is in Newark. They work there three days a week and two days at home in New York, by choice.
  - New Jersey applies New York's convenience test, so the home days are New Jersey-source.
  - Withhold New Jersey tax on the full wages, unless the home days are for the employer's necessity.
  - **Variation:** a fully remote New York resident who performs no services in New Jersey in the year has no New Jersey-source wages, even with a New Jersey employer ([Convenience rule FAQ](https://www.nj.gov/treasury/taxation/conveniencerulefaq.shtml)).
- **New Jersey resident working only in Manhattan**, subject to New York withholding.
  - New Jersey withholding is not needed only if New York withholding is at least equal to New Jersey's.
  - If the employee also works some days in New Jersey, withhold New Jersey tax as well, reduced by the New York tax withheld.
- Use the Guide us-multi-state-residency-and-allocation for day counts and credits.

### Case 6: minimum wage by employer size ([MW-571 (1/26)](https://www.nj.gov/labor/wageandhour/assets/PDFs/MW-571%20%281-26%29%20MinWageFlier.pdf))

- A year-round shop with 4 employees has fewer than 6 employees, so it pays at least $15.23 in 2026 ($14.53 in 2025).
- If it hires a sixth employee, it pays the general rate: $15.92 in 2026 ($15.49 in 2025).

## 2025 payrolls: corrections and late filings

- **Worker rates for 2025** ([NJDOL rate information](https://www.nj.gov/labor/ea/employer-services/rate-info/)):
  - UI 0.3825%, WF/SWF 0.0425%, TDI 0.23% and FLI 0.33% ([NJDOL rate information](https://www.nj.gov/labor/ea/employer-services/rate-info/));
  - bases $43,300 and $165,400 ([NJDOL rate information](https://www.nj.gov/labor/ea/employer-services/rate-info/)).
  - Check any 2025 payroll run that used a different FLI or TDI rate, and correct the affected quarters.
- **Employer new rates for 2025:** 3.1% total UI plus WF/SWF to June 30, 2025, then 2.8%. TDI 0.5%. Employer wage base $43,300 ([NJDOL rate information](https://www.nj.gov/labor/ea/employer-services/rate-info/)).
- **Minimum wage for 2025:** $15.49, or $14.53 for seasonal and small employers ([MW-571 (1/26)](https://www.nj.gov/labor/wageandhour/assets/PDFs/MW-571%20%281-26%29%20MinWageFlier.pdf)).
- **Corrections:** correct Forms NJ-927 online; the correction replaces the original. A prior-year refund needs an amended NJ-927 for the quarter and an amended NJ-W-3. An NJ-W-3 correction that changes the tax requires amending each affected quarter ([NJ-WT](https://www.nj.gov/treasury/taxation/pdf/current/njwt.pdf)).
- Amend a WR-30 online or by SFTP ([Employer Handbook, taxes and wages](https://www.nj.gov/labor/ea/help/employer_handbook/taxes_wages.shtml)).

## When to refuse or refer

- **Refer** any employee who lives or works outside New Jersey, works from home in another state, or moved during the year. Use the Guide us-multi-state-residency-and-allocation. Do not guess an allocation percentage.
- **Refer** which state's UI covers a worker who works in more than one state. The WR-30 includes only pay for services in New Jersey, and wages for services elsewhere go to those states.
- **Refer** every real worker classification question, including construction. Refer any NJDOL audit to an employment or tax lawyer. This Guide gives the ABC test in summary only.
- **Refer** private TDI or FLI plan approval, successor employer transfers, rate disputes and penalty abatement to NJDOL.
- **Refuse** to compute New Jersey withholding from return rate schedules or a federal W-4. Use NJ-WT and the NJ-W4.
- **Say so** when a figure is not yet set: the 2027 worker contribution rates, and the 2027 minimum wage chart.

## Filing and payment

- **Form NJ-927 / NJ-927-W:** due quarterly, electronically, even with nothing withheld. Seasonal businesses file all four quarters. All locations under one FEIN file one combined return ([NJ-WT](https://www.nj.gov/treasury/taxation/pdf/current/njwt.pdf)).

| Quarter (2026) | Due date |
| --- | --- |
| Q1, January to March | April 30, 2026 |
| Q2, April to June | July 30, 2026 |
| Q3, July to September | October 30, 2026 |
| Q4, October to December | January 30, 2027 |

- **Weekend due dates: the two agencies conflict.** The Division of Taxation says a due date on a weekend or holiday moves to the next business day ([NJ-WT](https://www.nj.gov/treasury/taxation/pdf/current/njwt.pdf)). NJDOL says the NJ-927, the WR-30 and any payment must be received by the 30th, even on a weekend or holiday, with no extension ([NJDOL rate information](https://www.nj.gov/labor/ea/employer-services/rate-info/)). As a rule, when the 30th falls on a weekend or holiday, file and pay by the last business day before it. April 30, July 30 and October 30, 2026 are weekdays. January 30, 2027 is a Saturday, so file and pay the Q4 2026 return by Friday, January 29, 2027.
- **NJ-500 monthly payments:** due by the 15th of the next month, for the first and second months of a quarter with more than $500 withheld ([NJ-WT](https://www.nj.gov/treasury/taxation/pdf/current/njwt.pdf)).
- **Weekly payments:** due by 11:59 p.m. on the Wednesday after the pay week. Weekly payers still file quarterly.
- **Payment:** NJDOL contributions are paid by electronic funds transfer, credit card or e-check ([Employer Handbook, taxes and wages](https://www.nj.gov/labor/ea/help/employer_handbook/taxes_wages.shtml)).
- **Form W-2 to employees:**
  - federal law requires employees' copies by February 1, 2027 for 2026 wages ([IRS W-2 and W-3 instructions](https://www.irs.gov/instructions/iw2w3)). NJ-WT gives February 15, so in practice the federal date governs;
  - NJ-WT also requires a W-2 within 30 days after the last wage payment to an employee who leaves and is not expected to return. Do not wait beyond the federal date.
  - Show a combined UI/WF/SWF amount, and separate TDI and FLI amounts. Show the private plan number where there is one ([NJ-WT](https://www.nj.gov/treasury/taxation/pdf/current/njwt.pdf)).
- **Form NJ-W-3 (annual reconciliation):** file electronically with all W-2s by February 15 of the next year. If that falls on a weekend or holiday, file by the next business day. An employer that stops paying wages files within 30 days after the last month wages were paid ([NJ-WT](https://www.nj.gov/treasury/taxation/pdf/current/njwt.pdf)).
- **Penalties, income tax side** ([NJ-WT](https://www.nj.gov/treasury/taxation/pdf/current/njwt.pdf)):
  - late filing: 5% per month or part month of the tax due, up to 25%, plus $100 per month or part month ([NJ-WT](https://www.nj.gov/treasury/taxation/pdf/current/njwt.pdf));
  - late payment: 5% of the tax paid late ([NJ-WT](https://www.nj.gov/treasury/taxation/pdf/current/njwt.pdf));
  - interest: 3% above the prime rate ([NJ-WT](https://www.nj.gov/treasury/taxation/pdf/current/njwt.pdf)).
  - Owners, partners and officers can be held personally liable for tax they should have withheld.
- **Penalties, contributions side** ([NJDOL interest and penalties](https://www.nj.gov/labor/ea/bill-notice/interest-penalties/)):
  - late NJ-927: $10 a day for the first five days. After that, $10 a day or 25% of the contributions due, whichever is less ([NJDOL interest and penalties](https://www.nj.gov/labor/ea/bill-notice/interest-penalties/));
  - a late "no liability" report: up to $50 ([NJDOL interest and penalties](https://www.nj.gov/labor/ea/bill-notice/interest-penalties/));
  - interest on unpaid contributions: 1.25% a month, which cannot be waived ([NJDOL interest and penalties](https://www.nj.gov/labor/ea/bill-notice/interest-penalties/));
  - late or wrong WR-30: $5 per employee for the first failure, $10 for the second and $25 for the third or later failure within eight consecutive quarters ([NJDOL interest and penalties](https://www.nj.gov/labor/ea/bill-notice/interest-penalties/)).
  - WR-30 penalties apply to failures without reasonable cause.
  - Penalty abatement is for good cause. Request it in writing within one year of the penalty notice, with a notarized affidavit showing why, and a statement that there was no fraud or intentional disregard of the law. All NJ-927 and WR-30 reports must be filed, and all other liability paid, before abatement is considered. Interest cannot be abated ([NJDOL interest and penalties](https://www.nj.gov/labor/ea/bill-notice/interest-penalties/)).
- **Form 1099 copies to New Jersey:** send copies where $1,000 or more was paid or credited in the calendar year, or where any New Jersey tax was withheld. File them electronically by February 15 of the next year, or the next business day if that falls on a weekend or holiday ([NJ-WT](https://www.nj.gov/treasury/taxation/pdf/current/njwt.pdf)).
- **New hire reports:** a state may set a penalty of up to $25 per unreported new hire, or $500 where employer and employee conspired not to report ([42 U.S.C. 653a](https://www.law.cornell.edu/uscode/text/42/653a)).
- **Records:** keep UI and wage records for the current calendar year and the four before it ([Employer Handbook, taxes and wages](https://www.nj.gov/labor/ea/help/employer_handbook/taxes_wages.shtml)).

## Completion checklist

- Registered as an employer. New hires reported within 20 days, or by the two monthly electronic transmissions ([42 U.S.C. 653a](https://www.law.cornell.edu/uscode/text/42/653a)).
- Every employee has an NJ-W4. Any "EXEMPT" claims are for the current year and within the income limits ([Form NJ-W4](https://www.nj.gov/treasury/taxation/pdf/current/njw4.pdf)).
- Pennsylvania residents have a signed NJ-165 on file, or New Jersey tax is withheld.
- Out-of-state and remote employees were checked against the Guide us-multi-state-residency-and-allocation.
- Worker deductions used the 2026 rates: UI 0.3825%, WF/SWF 0.0425%, TDI 0.19% and FLI 0.23%, stopping at $44,800 and $171,100 ([NJDOL rate information](https://www.nj.gov/labor/ea/employer-services/rate-info/)).
- Employer UI, WF/SWF and TDI used the rate for each fiscal rate year, stopping at $44,800 for 2026 ([NJDOL rate information](https://www.nj.gov/labor/ea/employer-services/rate-info/)).
- NJ-500 and weekly payments follow the $500 and $10,000 rules. NJ-927 and WR-30 are filed by the 30th after each quarter ([NJ-WT](https://www.nj.gov/treasury/taxation/pdf/current/njwt.pdf)).
- W-2s were given to employees by the federal date (February 1, 2027 for 2026) ([IRS W-2 and W-3 instructions](https://www.irs.gov/instructions/iw2w3)).
- NJ-W-3 was filed with the W-2s, and any required 1099 copies were sent, by February 15.
- Pay rates meet the 2026 minimum wage for the employer's size and type.
- Every 1099 worker has a documented ABC analysis, or has been referred.

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
