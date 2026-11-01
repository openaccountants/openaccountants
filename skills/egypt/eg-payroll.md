---
name: eg-payroll
description: Use this skill for running payroll for an employer in Egypt for tax year 2026, including a sole proprietor who hires staff. It covers salary tax withholding, the unified payroll system, monthly calculation form, Form 4 and annual settlement, gross to net, employer cost and employee versus freelancer. Trigger on "Egypt payroll", "salary tax Egypt", "ضريبة كسب العمل", "payroll tax Egypt", "hiring employees Egypt", "withholding tax on salaries Egypt", "Form 4 Egypt", "نموذج 4", "gross to net salary Egypt", "employer cost Egypt", "end of service Egypt" or "employee vs freelancer Egypt". Read this skill before any Egypt payroll work. Social insurance computation sits in eg-social-insurance.
version: 1.1
jurisdiction: EG
tax_year: 2026
last_updated: 2026-11-01
review_status: pending_review
trust_label: Built by Michael Cutajar and the OpenAccountants team
depends_on:
  - income-tax-workflow-base
category: international
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Egypt Payroll v1.1

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

Tax year: calendar 2026 (the annual settlement runs January to December whatever the company's financial year, [ETA FAQ](https://eta.gov.eg/sites/default/files/2026-05/faqs-payroll-system-v4.pdf) general q.120). All amounts are EGP. Reply in the user's language; use the Arabic terms where they help.

## Who this applies to

- **Employers in Egypt** running monthly payroll, including a sole proprietor (منشأة فردية) with staff. The owner's own tax is in eg-income-tax and eg-sme-tax; the owner's own social insurance is in eg-social-insurance.
- **Every worker paid by the employer**, regular or irregular, insured or not, must be on the monthly calculation form under the right tax treatment ([ETA FAQ](https://eta.gov.eg/sites/default/files/2026-05/faqs-payroll-system-v4.pdf) q.83).
- **Foreign employees**: same tax treatment as Egyptians; the treatment code decides the method, not nationality (q.52, q.77). A passport number replaces the national ID.
- **Professionals (lawyer, doctor)**: if there is a relationship of subordination (تبعية), the pay goes through payroll; if they work independently, it goes on their own professional return (q.60).
- **The unified payroll system** (منظومة توحيد أسس ومعايير احتساب ضريبة الأجور والمرتبات): the last phase of mandatory joining was 15 December 2024 under Finance Minister decree 386 of 2023 (q.25). Once a body joins, Form 4 and the annual settlement go only through this system ([Form 4 guide](https://eta.gov.eg/sites/default/files/2025-11/UPTCP_Quarterly_Payroll_Form_Submission_Guide_v.1.2.pdf)).
- **Law 6 of 2025 simplified regime**: see Deadlines and filing; it changes when tax is paid, not how it is computed.

## Rates, bands and thresholds

| Item | Amount | Tax year | Conditions | Official URL |
|---|---|---|---|---|
| Personal exemption | EGP 20,000 a year | 2026 | Each employee; prorated if days worked in a month are under 30 (FAQ q.93). Law 91 art. 13(1) as replaced by Law 7/2024 | https://eta.gov.eg/sites/default/files/2024-03/law_no.7-2024.pdf |
| Exemption, disabled worker or carer | 150% of the personal exemption (EGP 30,000) | 2026 | Integrated services card from Social Solidarity; treatment code 4 (Law 10/2018 art. 23(1)) | https://eta.gov.eg/sites/default/files/2026-05/faqs-payroll-system-v4.pdf |
| Annual net income rounding | Down to the nearest EGP 10 | 2026 | Applied before the bands. Law 91 art. 8 | https://eta.gov.eg/sites/default/files/2024-03/law_no.7-2024.pdf |
| Withholding by a non-original employer | 10% on account | 2026 | Treatment code 2; a payment on account, no longer final (art. 72 bis, Law 30/2023, from January 2024) | https://eta.gov.eg/sites/default/files/2026-05/faqs-payroll-system-v4.pdf |
| Economic zone treatment | 5% of the annual base | 2026 | Suez Canal zone companies set up before 24 June 2015 whose status still runs; codes 6 and 7 | https://eta.gov.eg/sites/default/files/2026-05/faqs-payroll-system-v4.pdf |
| Insurance, pension and health premiums cap | Lower of 15% of net income or EGP 10,000 a year, within the amount paid | 2026 | Law 54/1975 funds, health premiums, life cover for self, spouse, minor children, pension premiums. Excess is taxed. Art. 13(3) and (4) | https://eta.gov.eg/sites/default/files/2026-05/faqs-payroll-system-v4.pdf |
| Law 155/2024 insurance fund contributions | Fully exempt | 2026 | Funds set up or regularised under Law 155/2024, art. 75 last paragraph, from regularisation | https://eta.gov.eg/sites/default/files/2026-05/faqs-payroll-system-v4.pdf |
| Employee profit share | Exempt up to 100% of annual wages | 2026 | After general assembly approval. Excess goes in other earnings. Art. 13(6) | https://eta.gov.eg/sites/default/files/2026-05/faqs-payroll-system-v4.pdf |
| Martyrs fund contribution | EGP 5 per EGP 10,000 | 2026 | Basic pay runs only; all workers except Egyptian daily workers | https://eta.gov.eg/sites/default/files/2026-05/faqs-payroll-system-v4.pdf |
| Employee social insurance | 11% of the insurance wage | 2026 | Owned by eg-social-insurance; 2026 band EGP 2,700 to 16,700 | https://www.nosi.gov.eg/ar/news/Pages/2025-11-30.aspx |
| Private sector minimum wage | EGP 7,000 a month | From 1 March 2025 | National Wages Council decision; later change on the Not yet confirmed line | https://mped.gov.eg/singlenews?id=6009 |
| Periodic raise, private sector | Minimum 3% of the insurance wage, at least EGP 250 a month | From 2025 | National Wages Council decision | https://mped.gov.eg/singlenews?id=6009 |

### Salary tax table, Law 91 art. 8 as replaced by Law 7/2024

This is one table with a column for each income level. **Pick the column by total annual net income, then apply the whole column from the first pound.** It is not a plain ladder: above EGP 600,000 the lower bands vanish. In force for salaries from 1 March 2024, the first of the month after the 21 February 2024 Gazette, and still the law for 2026: Laws 5 to 7 of 2025 and 149 to 153 of 2026 add no replacement of art. 8.

| Annual net income | 0% | 10% | 15% | 20% | 22.5% | 25% | 27.5% | Official URL |
|---|---|---|---|---|---|---|---|---|
| Up to 600,000 | 1 to 40,000 | to 55,000 | to 70,000 | to 200,000 | to 400,000 | above 400,000 | none | https://eta.gov.eg/sites/default/files/2024-03/law_no.7-2024.pdf |
| 600,001 to 700,000 | none | 1 to 55,000 | to 70,000 | to 200,000 | to 400,000 | above 400,000 | none | same |
| 700,001 to 800,000 | none | none | 1 to 70,000 | to 200,000 | to 400,000 | above 400,000 | none | same |
| 800,001 to 900,000 | none | none | none | 1 to 200,000 | to 400,000 | above 400,000 | none | same |
| 900,001 to 1,200,000 | none | none | none | none | 1 to 400,000 | above 400,000 | none | same |
| Above 1,200,000 | none | none | none | none | none | 1 to 1,200,000 | above 1,200,000 | same |

## The base

The eight treatment codes (المعاملة الضريبية), [ETA FAQ](https://eta.gov.eg/sites/default/files/2026-05/faqs-payroll-system-v4.pdf) q.26 to q.34:

| Code | Use when | Effect |
|---|---|---|
| 1 | Permanent or temporary staff at their original employer | Cumulative method below; add income and tax from other employers |
| 2 | Filer is not the original employer | 10% on account; the original employer's 9-digit tax number is mandatory (an insurance number will not do); notify the original employer |
| 3 | Non-original employer where the worker earns or spends over 50% of income or time | Treated as original employer |
| 4 | Disabled worker or carer | Exemption up 50% |
| 5 | Chronic illness under Health Minister decree 259/1995 and absent from work | Insurance wage exempted from net income (Finance Minister decree 285/2023) |
| 6 | Economic zone company described above | 5% |
| 7 | Codes 4 and 6 together | Exemption up 50%, then 5% |
| 8 | Arrears of pay for past periods | Rules frozen; the base and tax are entered by hand and checked at audit |

**Taxable earnings** (24 elements, q.38): basic pay; bonuses and incentives; non-exempt raises; commissions; pay of board chairs and managers for administrative work; leave paid in cash; taxable end-of-service pay; quarterly, half-yearly and annual sums; other taxable allowances; tips; service charge. Cash benefits: employee social insurance or salary tax borne by the employer. In-kind benefits: cars, mobile phones, loans and advances, employer life insurance, shares below market value in or outside Egypt after any restriction lifts, other benefits.

**Rules on specific items:**

- Net-pay contracts: salary tax is personal and cannot be shifted, so tax or insurance the employer bears is added as a cash benefit and the tax recomputed (q.50, q.51).
- Benefits are taxable if not repayment of real expenses and of personal benefit (q.53); value at market value less what the worker paid (q.54). For cars and phones, the benefit is 20% of the cost on the company's books, entered for tax only, not paid (q.55, q.58).
- Group benefits exempt under art. 13(5) stay off the form: meals, group transport, health care, work tools and clothes, housing provided for work ([Law 91](https://eta.gov.eg/sites/default/files/2024-03/law_no.91-2005.pdf) art. 13, 2005 text). Each individual benefit is entered per employee (q.109).
- Transport allowances paid are taxable; reimbursement of actual cost stays off the form (q.17).
- End-of-service pay is untaxed only when the relationship ends for good; on rehire it is taxable (q.96, art. 12). Untaxed sums go on the additions and deductions screen.
- Cash for leave balance during service is taxed wholly in the current period. Other lump-sum arrears are spread over the years earned (art. 10; q.72, q.99).
- Pay from abroad for work in Egypt, and pay the local entity does not book, is still reported (q.6, q.99).
- Law 151/2026 added the comprehensive health solidarity contribution to arts. 23(10) and 33(5) of Law 91, not to the salary articles ([Law 151/2026](https://eta.gov.eg/sites/default/files/2026-08/law.no_.151.of_.2026.pdf) art. 2). It is not a payroll deduction.

**Deductions from earnings** (q.92): past-period instalments; employee social insurance; employee comprehensive health insurance; exempt profit share; Law 155/2024 funds; capped insurance premiums; personal exemption; raises exempt up to 2013; sums exempt under special laws; stamp duty under Law 111/1980 art. 79.

**Method, per pay run** (q.15, q.76, art. 10):

1. Period net income = earnings less deductions. Period days: 30 a month, 360 a year, shorter for joiners and leavers, actual for daily workers (q.39, q.40).
2. Cumulative net income = this period plus earlier periods.
3. Annual base = cumulative net income x 360 / days worked to date. Round down to EGP 10.
4. Apply the table to the annual base.
5. Tax to date = annual tax x days worked / 360.
6. Tax for this run = tax to date less tax already computed.
7. Net pay = gross less employee insurance less tax. Employer cost = gross plus employer insurance (eg-social-insurance). Tax is the employee's, not an extra cost.

**Employee or freelancer.** Decide on substance, not the contract label. Default to employee when unclear.

- Points to employee: direction, hours and supervision by the employer; integration, employer's tools or premises; regular fixed salary; exclusivity and no business risk; employer answers for the worker's mistakes.
- Points to contractor: project engagement at own risk; several clients; own tools; invoices; controls how and when; own tax registration.
- Wrong classification exposes the employer to back salary tax, back insurance and penalties, and labour claims under Labour Law 14 of 2025.

## Deadlines and filing

| Duty | When | Form and place | Source |
|---|---|---|---|
| Pay tax withheld | First 15 days of the following month | Claim on the Core system from the monthly form | [Law 91 art. 14](https://eta.gov.eg/sites/default/files/2024-03/law_no.91-2005.pdf), [FAQ q.9](https://eta.gov.eg/sites/default/files/2026-05/faqs-payroll-system-v4.pdf) |
| Monthly calculation form | With each pay run, or once a month for all runs; payment deadline governs | نموذج الاحتساب الشهري, unified payroll system | [FAQ](https://eta.gov.eg/sites/default/files/2026-05/faqs-payroll-system-v4.pdf) q.9, q.10 |
| Form 4 | Quarterly, in January, April, July, October | Quarterly return, unified payroll system | [Law 91 art. 15](https://eta.gov.eg/sites/default/files/2024-03/law_no.91-2005.pdf), [guide](https://eta.gov.eg/sites/default/files/2025-11/UPTCP_Quarterly_Payroll_Form_Submission_Guide_v.1.2.pdf) |
| Annual settlement | After all monthly forms for the year | Form 9 settlements, replaces forms 6, 7, 8 | [FAQ](https://eta.gov.eg/sites/default/files/2026-05/faqs-payroll-system-v4.pdf) q.75, [guide](https://eta.gov.eg/sites/default/files/2026-01/uptcp_annual_payroll_claculation_form_guide_v_2.2_1.pdf) |
| Proportional stamp on pay | Where the entity is subject | Form 21/خ, filed separately | [FAQ](https://eta.gov.eg/sites/default/files/2026-05/faqs-payroll-system-v4.pdf) q.66, q.88 |
| Pay statement | On the worker's request | Name, amount and type of income, tax withheld | [Law 91 art. 15](https://eta.gov.eg/sites/default/files/2024-03/law_no.91-2005.pdf) |

**How to file the monthly form** ([FAQ](https://eta.gov.eg/sites/default/files/2026-05/faqs-payroll-system-v4.pdf) general q.33, data q.23; [monthly guide](https://eta.gov.eg/sites/default/files/2026-01/uptcp_submitting_payroll_claculation_form_guide_v_1.7_highlights.pdf)):

1. Go to eta.gov.eg, press the taxpayer portal (بوابة الممول), enter the Core user name and password, press the taxpayer's name, then Tax Services (الخدمات الضريبية), then the unified payroll system. There is no separate login (q.24).
2. Open Forms (النماذج), Add new form (إضافة نموذج), choose the monthly calculation form, choose the period, press OK.
3. Choose one of three routes (q.17): system integration, the Excel template, or manual entry. For Excel, download the [2026 private sector form](https://eta.gov.eg/sites/default/files/2026-03/nmwdhj_alqta_alkhas_2026.xlsx) from the [forms page](https://www.eta.gov.eg/ar/payroll-forms), fill it, delete the first row, save as CSV UTF-8 (comma delimited) and upload.
4. Complete the screens (q.97): basic data (code, national ID or passport, treatment, days); insurance (status, comprehensive wage from form 2, insurance wage, comprehensive health status); earnings. Exemptions and salary tax fill themselves. Additions and deductions is last and does not touch the tax. Enter the head office insurance number once (q.98).
5. Press Calculate (احتساب), read the alerts, fix errors; the form cannot go with errors (q.25). Save draft if needed.
6. Press Submit (تقديم).

**What happens next.** The system files the monthly payment form and Form 2 salaries on Core and issues a claim when tax is due (q.6, q.13). Treatments 1 and 2 on one form give separate claims (q.101). The martyrs fund has its own claim (data q.12). Pay the claim through Core by the 15th. Insurance is not claimed here; it goes to NOSI. A run entered after the 15th is recomputed and carries delay interest (q.23). No negative figures (q.14), and no amended form exists: fix next month, by additional run, or on the settlement treatment sheet (data q.57). Basic runs cannot repeat an employee; additional runs have no limit (q.68). Employees get payslips from the employee portal, created with their national ID and the mobile on the form (q.10).

**Form 4** ([guide](https://eta.gov.eg/sites/default/files/2025-11/UPTCP_Quarterly_Payroll_Form_Submission_Guide_v.1.2.pdf)): Forms, Add new form, quarterly salary tax calculation, pick the period. One page. Choose entity type in field 5: 01 not under the Civil Service Law, private sector, other; 02 under the Civil Service Law. Other header fields fill themselves; the monthly tax paid, electronic code and supply date under each month are optional. Press Calculate, check alerts, Submit, confirm OK, then print to PDF. No amended Form 4 exists, only a supplementary one. It opens only once the quarter's monthly forms are in (data q.73).

**Annual settlement** ([guide](https://eta.gov.eg/sites/default/files/2026-01/uptcp_annual_payroll_claculation_form_guide_v_2.2_1.pdf); FAQ q.18, q.113): add the annual salary tax settlement form or open it from filing obligations. It has four pages and fills from the monthly forms. Reductions go on the treatment sheet, CSV UTF-8, and lower the figures, except Law 155/2024 premiums, which raise them for 2025 only (q.115). Distribute tax paid outside the system among employees first, or the settlement is refused. Calculate, then Submit. After that no amendment and no further run for the year (q.103, q.104). Differences due are paid with it; overpayments are dealt with at audit (data q.56). Before filing, a December leaver with zero days needs an additional December run (data q.14).

**Law 6/2025 simplified regime** (q.100, q.117 to q.119): from the first month of the quarter after joining, no monthly payment and no Form 4; monthly forms are still needed to build the settlement, on no monthly deadline; no claims issue until the settlement, and payment comes only with it. If the regime ends, normal deadlines return.

**Before payroll starts for a new employer:** a first registration on the ETA portal is the prerequisite ([monthly guide](https://eta.gov.eg/sites/default/files/2026-01/uptcp_submitting_payroll_claculation_form_guide_v_1.7_highlights.pdf)). Those not on Core get link codes (data q.76).

## Penalties and interest

| Item | Rule | Source |
|---|---|---|
| Late or part payment | Delay charge under art. 110 of Law 91 from the day after the deadline, run by the Core system | [FAQ](https://eta.gov.eg/sites/default/files/2026-05/faqs-payroll-system-v4.pdf) q.19, q.23 |
| Employer that fails to withhold | Still owes the differences, with its right to recover from the employee | [Law 91 art. 14](https://eta.gov.eg/sites/default/files/2024-03/law_no.91-2005.pdf) |
| Late insurance | See eg-social-insurance | https://www.nosi.gov.eg/ar/news/Pages/2025-11-30.aspx |

Audit continues after the system (q.21). An employee disputes the computation under art. 57 of the Unified Tax Procedures Law (q.28).

## Cross-border points

- Foreign staff follow the same method by treatment code; a stay under 183 days does not change the form (q.77).
- Tax runs on actual days, even one day (q.78).
- A foreign payer or a parent's payment is reported locally even if not in local books (q.6).
- A non-resident employer with no establishment in Egypt: the recipient must pay over the tax ([Law 91 art. 16](https://eta.gov.eg/sites/default/files/2024-03/law_no.91-2005.pdf), 2005 text).
- Seconded staff are filed by the entity booking the wage cost, under the matching code (q.63, q.70). All units on one tax number count as one employer (q.73).
- A foreign work permit status is a dropdown: valid, in process or none (data q.28).
- Foreign currency loans are valued at the rate on the due date (q.21).

## Two worked examples that recompute

### Example 1: EGP 20,000 a month, full year

Insurance wage capped at 16,700. Employee share 1,837 a month. Annual net income 240,000 less 22,044 less 20,000 is 197,956, rounded down to 197,950. Top row: 1,500 + 2,250 + 25,590 = 29,340, or 2,445 a month. Net pay 15,718. Employer cost 23,131.25.

```oa-check
name: Gross to net, EGP 20,000 a month, 2026
inputs:
  gross: 20000
steps:
  - ins_wage: min(gross, 16700)
  - employee_si: ins_wage * 0.11
  - employer_si: ins_wage * 0.1875
  - net_income: gross * 12 - employee_si * 12 - 20000
  - base: floor(net_income / 10) * 10
  - tax: 15000 * 0.10 + 15000 * 0.15 + (base - 70000) * 0.20
  - monthly_tax: tax / 12
  - net_pay: gross - employee_si - monthly_tax
  - cost: gross + employer_si
expected:
  base: 197950
  tax: 29340.00
  monthly_tax: 2445.00
  net_pay: 15718.00
  cost: 23131.25
```

### Example 2: decision, pay a EGP 20,000 year-end bonus or not?

An employee's annual net income is EGP 890,000. A taxable bonus of 20,000 takes it to 910,000 and over the 900,000 line, which moves the whole income to the next row.

- Without: 200,000 at 20%, 200,000 at 22.5%, 490,000 at 25% = 207,500.
- With: 400,000 at 22.5%, 510,000 at 25% = 217,500.

Extra tax 10,000 on a 20,000 bonus, a 50% marginal rate. The decision: at a genuine bonus of 10,000 or under the income stays in the row and the rate is 25%; at 20,000 the employee keeps 10,000. Do not reshape pay by sham allowances.

```oa-check
name: Bonus across the 900,000 line
inputs:
  before: 890000
  bonus: 20000
steps:
  - after: before + bonus
  - tax_before: 200000 * 0.20 + 200000 * 0.225 + (before - 400000) * 0.25
  - tax_after: 400000 * 0.225 + (after - 400000) * 0.25
  - extra: tax_after - tax_before
  - rate: extra / bonus
expected:
  tax_before: 207500.00
  tax_after: 217500.00
  extra: 10000.00
  rate: 0.50
```

### Further cases (all 2026, code 1, full year)

- **Low earner**, EGP 7,000 a month: insurance 770; net income 84,000 less 9,240 less 20,000 = 54,760; rounded 54,760; tax 1,476 a year, 123 a month. A part-time worker on EGP 4,000: net income 22,720, in the 0% band, tax nil, insurance still due.
- **Mid earner with bonus**, 12,000 a month plus 24,000: insurance 1,320 a month, 15,840 a year; net income 132,160; tax 1,500 + 2,250 + 12,432 = 16,182. Bonus goes in the annual sums field; the cumulative method collects the tax in that month. Employer insurance 2,250 a month.
- **High earner**, 80,000 a month: net income 917,956, rounded 917,950, row 900,001 to 1,200,000: 90,000 + 129,487.50 = 219,487.50.
- **Sole proprietor's assistant**, 8,000 a month: insurance 880, employer 1,500; net income 65,440; tax 1,500 + 1,566 = 3,066, 255.50 a month. Separate from the owner's return.

## Ask the client first

1. Is the entity on the unified payroll system and Core, or under Law 6/2025?
2. For each worker: original employer or not, nationality, days worked, special status (treatment code)?
3. Gross pay split by element, benefits in kind, and who bears tax or insurance?
4. Insurance status and insurance wage on form 2; comprehensive health status?
5. Year to date income and tax, and income from other employers?
6. Is the worker truly under direction, or independent?

**Defaults when a fact is missing:** choose the option that does not under-withhold. Status unclear: employee. Residency unclear: same method, no treaty relief without papers. Insurance wage unknown: gross wage clamped to the band. Benefit taxability unclear: taxable. Show the assumption.

**Refuse:** a final filing figure when treatment code or year-to-date data is missing; relabelling a genuine employee as a freelancer; off-book pay, split salary or sham allowances; an insurance wage below the true wage or the minimum; binding labour-law or termination advice (refer to an Egyptian labour lawyer). Output needs a qualified Egyptian accountant's review before filing.

**Owner of related topics:** social insurance and NOSI penalties in eg-social-insurance; owner's tax in eg-income-tax and eg-sme-tax; VAT on freelancer invoices in egypt-vat; payroll journals in eg-bookkeeping.

## Sources

| Source | URL | Read on |
|---|---|---|
| Law 7/2024, arts. 8 and 13(1) of Law 91, Gazette 21 Feb 2024, both pages read | https://eta.gov.eg/sites/default/files/2024-03/law_no.7-2024.pdf | 2026-11-01 |
| Law 91/2005, arts. 10, 12 to 16, 110, original 2005 text from OCR | https://eta.gov.eg/sites/default/files/2024-03/law_no.91-2005.pdf | 2026-11-01 |
| ETA FAQ on the payroll system, 4th edition, March 2026, all 44 pages | https://eta.gov.eg/sites/default/files/2026-05/faqs-payroll-system-v4.pdf | 2026-11-01 |
| ETA Form 4 guide v1.2, whole | https://eta.gov.eg/sites/default/files/2025-11/UPTCP_Quarterly_Payroll_Form_Submission_Guide_v.1.2.pdf | 2026-11-01 |
| ETA annual settlement guide for 2025, overview, steps and first field tables (pages 1 to 11) | https://eta.gov.eg/sites/default/files/2026-01/uptcp_annual_payroll_claculation_form_guide_v_2.2_1.pdf | 2026-11-01 |
| ETA monthly form guide, overview and steps to page 9 | https://eta.gov.eg/sites/default/files/2026-01/uptcp_submitting_payroll_claculation_form_guide_v_1.7_highlights.pdf | 2026-11-01 |
| ETA 2026 private sector monthly form, all column headers | https://eta.gov.eg/sites/default/files/2026-03/nmwdhj_alqta_alkhas_2026.xlsx | 2026-11-01 |
| Law 151/2026, art. 2 page read | https://eta.gov.eg/sites/default/files/2026-08/law.no_.151.of_.2026.pdf | 2026-11-01 |
| NOSI notice on 2026 band, 30 Nov 2025, whole page | https://www.nosi.gov.eg/ar/news/Pages/2025-11-30.aspx | 2026-11-01 |
| National Wages Council, Ministry of Planning, 2025, headline decision | https://mped.gov.eg/singlenews?id=6009 | 2026-11-01 |

Not yet confirmed: the private sector minimum wage after March 2025; delay charge rate under art. 110 as amended and the Unified Tax Procedures Law penalties (the old "up to 80%" could not be traced); the exact annual settlement due date (old text said end January) and the day of the month for Form 4; whether the martyrs contribution base is gross pay and who bears it (the form has an employee and a company field); whether the old 0.05% wording matches EGP 5 per 10,000 on every run type; Law 91 arts. 12 to 16 as amended since 2005 where only the original text was read; Labour Law 14 of 2025 end-of-service formulas (half a month a year for five years, then a full month), not read in the law; Civil Code Law 131/1948 as the contractor test; employee comprehensive health insurance rate; the commencement date of Labour Law 14 of 2025 (old text: 1 September 2025).

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
