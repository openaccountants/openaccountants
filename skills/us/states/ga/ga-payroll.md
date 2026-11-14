---
name: ga-payroll
description: Run Georgia employer payroll taxes for tax year 2026, state income tax withholding administered by the Department of Revenue and state unemployment insurance administered by the Department of Labor. Covers the 4.99% withholding rate from 11 May 2026 (5.19% before), the Table E percentage method with its standard deduction and $5,000 dependent allowance, Form G-4 and the single-zero default, the payer classes and deposit dates (semi-weekly, monthly, quarterly, annual, the one-day rule over $100,000), Form G-7 and GA-V, Form G-1003 due 1 February 2027, the EFT rule above $500, overtime and tips reporting, the withholding penalties, and unemployment insurance (the $9,500 taxable wage base, the 2.70% new employer rate, liability tests, quarterly tax and wage reports, late report and interest charges) and new hire reporting within 10 days. Trigger on "Georgia payroll", "Georgia withholding", "Form G-7", "G-4", "G-1003", "Georgia SUTA", "Georgia unemployment tax".
version: "1.1"
jurisdiction: US-GA
tax_year: 2026
last_updated: 2026-11-14
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
tier: 2
domain: payroll
type: computation
---

# Georgia payroll: withholding and unemployment insurance, tax year 2026

> **Source-cited draft.** Built from the Georgia Department of Revenue 2026 Employer's Tax Guide (updated September 2026) and its penalty page, and the Georgia Department of Labor employer unemployment insurance FAQs, tax reporting and liability sheet, 2024 and 2026 tax rate notices and employer newsletter, read on 2026-11-13. No accountant has reviewed it. All outputs must be reviewed by a qualified tax professional before filing.

**Answer first.** Georgia withholding for 2026 is **4.99%** of wages after the Table E standard deduction and dependent allowances; employers withhold at **5.19% until 11 May 2026** and may use 4.99% from that date. Deposits follow the employer's class (semi-weekly over $50,000 in the lookback year, monthly over $200 a month, quarterly, or annual at $800 or less a year), and any payday over $100,000 is due the next banking day. Form G-7 is due the last day of the month after each quarter, and Form G-1003 with W-2s and 1099-NECs by **1 February 2027**. Unemployment insurance is paid on the first **$9,500** of each employee's wages; a new employer's rate is **2.70%**.

## Scope and who this is for

In scope: an employer with employees working in Georgia, or Georgia residents working elsewhere, for 2026: registration, withholding computation, deposits and returns with DOR, and unemployment insurance (UI) liability, rates, reports and new hire reporting with the Department of Labor (GDOL).

Who must withhold ([2026 Employer's Tax Guide](https://dor.georgia.gov/document/document/2026-employers-tax-guide-updated-september-2026/download)): employers "are required to withhold Georgia income tax from the taxable wages of residents for services performed inside or outside of Georgia and from the taxable wages of taxable nonresidents for services performed in Georgia". Withholding is not required for residents working outside Georgia where the other state requires withholding.

Out of scope, and where it goes:

| Topic | Skill |
| --- | --- |
| Federal payroll taxes (Forms 941 and 940) | `us-form-941-940-payroll` |
| The employee's own Georgia return and the overtime and tips exclusions | `ga-income-tax` |
| Registering the business itself | `ga-formation` |
| Nonresident distribution withholding (G2-A), real property sale withholding (G2-RP), lottery and pension withholding detail | refer |
| Workers' compensation, wage and hour, final pay and leave rules | refer to the Georgia employment rules; not tax |

## Ask the client first

1. **Where do employees live and work?** Residents are withheld on all wages; nonresidents on Georgia work.
2. **Has each employee given a Form G-4,** and does any claim exempt or more than 14 allowances?
3. **Pay frequency and filing status on each G-4** (married filing joint, single or head of household, married filing separate) and dependent allowances.
4. **Total Georgia tax withheld in the lookback period** (12 months ending 30 June 2025) and per month, to set the payer class.
5. **Is the employer already registered** with DOR (withholding number on the Georgia Tax Center) and with GDOL (DOL-1A), and what UI rate is on its 2026 DOL-626 notice?
6. **Quarterly payroll and weeks with workers in 2025 and 2026**, for the UI liability test, and any hourly overtime or tipped employees (2026 reporting).

## The method, step by step

### Rates, bands and thresholds

| Item | Amount, 2026 | Source |
| --- | --- | --- |
| Withholding rate, percentage method, from 11 May 2026 | 4.99% | [2026 Employer's Tax Guide](https://dor.georgia.gov/document/document/2026-employers-tax-guide-updated-september-2026/download) |
| Withholding rate before the change takes effect (employers may move to 4.99% from 11 May 2026) | 5.19% | same |
| Table E standard deduction, annual, married filing joint | $30,000 | same |
| Table E standard deduction, annual, single or head of household, and married filing separate (also for married couples both working) | $15,000 | same |
| Table E dependent allowance, annual, each | $5,000 | same |
| Semi-weekly payer: tax withheld in the lookback period more than | $50,000 | same |
| Monthly payer: tax withheld per month more than | $200 | same |
| Annual payer: tax withheld per year at most | $800 | same |
| One-day rule: tax withheld for a payday more than | $100,000 | same |
| EFT and electronic filing required once a G-7 shows tax withheld of more than | $500 | same |
| G-4 claiming exempt or more than this many allowances is sent to DOR | 14 | same |
| UI taxable wage base per employee per year (since 1 January 2013) | $9,500 | [GDOL employer UI FAQs](https://dol.georgia.gov/faqs-employers/employers-faqs-unemployment-insurance) |
| UI rate for new or newly covered employers | 2.70% | same |
| UI liability: quarterly payroll of at least, or one worker in 20 calendar weeks | $1,500 | same |
| UI liability, domestic employers: cash wages in a calendar quarter of | $1,000 or more | same |
| UI liability, agricultural employers: gross quarterly payroll of at least | $20,000 | same |
| UI late report penalty, per month or part month | greater of $20 or 0.05% of gross payroll (in words on the page: ".05 percent") | same |
| UI interest on late contributions, per month or part month | 1.5% | same |
| UI cost of collection fee on a deficiency | 20% | same |
| New hire report deadline after hire, rehire or return to work | 10 days | [GDOL employer newsletter DOL-5137](https://dol.georgia.gov/document/unemployment-benefits/employer-newsletter-dol-5137/download) |

### Table E, by pay period

From the [2026 Employer's Tax Guide, Table E](https://dor.georgia.gov/document/document/2026-employers-tax-guide-updated-september-2026/download):

| Pay period | Married filing joint | Single or head of household | Married filing separate | Each dependent allowance | Source |
| --- | --- | --- | --- | --- | --- |
| Weekly | 576.92 | 288.46 | 288.46 | 96.15 | [2026 Employer's Tax Guide, Table E](https://dor.georgia.gov/document/document/2026-employers-tax-guide-updated-september-2026/download) |
| Bi-weekly | 1,153.85 | 576.92 | 576.92 | 192.31 | same |
| Semi-monthly | 1,250.00 | 625.00 | 625.00 | 208.33 | same |
| Monthly | 2,500.00 | 1,250.00 | 1,250.00 | 416.67 | same |
| Quarterly | 7,500.00 | 3,750.00 | 3,750.00 | 1,250.00 | same |
| Semi-annual | 15,000.00 | 7,500.00 | 7,500.00 | 2,500.00 | same |
| Annual | 30,000.00 | 15,000.00 | 15,000.00 | 5,000.00 | same |
| Daily (misc.) | 82.19 | 41.10 | 41.10 | 13.70 | same |

### Withholding

1. **Register** for a withholding number on the Georgia Tax Center (gtc.dor.ga.gov).
2. **Collect Form G-4** from each employee. With no G-4, the employer may use the federal W-4 election where the information allows; otherwise withhold as if single with zero allowances (O.C.G.A. § 48-7-102). A G-4 claiming exempt or more than 14 allowances is mailed to DOR; DOR writes if it should not be honoured. An employer who knows a G-4 is wrong withholds as single, zero allowances until a corrected form arrives. Employees may add extra withholding on the G-4.
3. **Compute each payday (percentage method):** taxable wages, less the Table E standard deduction for the G-4 status, less the dependent allowance times dependents claimed, times 4.99% (5.19% for wages paid before the employer moves to the new rate, and in any case before 11 May 2026). With zero allowances, subtract the standard deduction only. Bonuses and other compensation are withheld at the rate in effect when paid.
4. **Deposit** by payer class ([2026 Employer's Tax Guide](https://dor.georgia.gov/document/document/2026-employers-tax-guide-updated-september-2026/download)); the lookback period is the 12 months ending 30 June of the prior year:
   - Semi-weekly (more than $50,000 in the lookback period): by EFT; paydays Wednesday to Friday are due the following Wednesday, paydays Saturday to Tuesday the following Friday. Report on Form G-7 with Schedule B.
   - Monthly (more than $200 a month): by the 15th of the next month with Form GA-V, unless paying electronically.
   - Quarterly ($200 a month or less but more than $800 a year): with Form G-7 by the last day of the month after the quarter.
   - Annual ($800 or less a year, on request through the Georgia Tax Center before the first quarter's due date): with Form G-7 by 31 January.
   - Any payday over $100,000: by EFT the next banking day after payday. The filing frequency does not change automatically.
5. **File Form G-7** for every quarter, even with no tax withheld, by the last day of the month after the quarter. Once a G-7 shows more than $500, every later payment must be by EFT and every return filed electronically. Returns with series 100 credits must be filed electronically.
6. **Year end: Form G-1003** with the W-2s and 1099-NECs by 1 February 2027; other 1099s by 1 March 2027. For 2026, report qualified overtime and qualified cash tips on the year-end W-2 and 1099; do not report them on the 2026 G-7 (the G-7 changes from 2027). Reporting them does not reduce withholding or W-2 Box 16 wages.

**2026 due dates** ([2026 Employer's Tax Guide](https://dor.georgia.gov/document/document/2026-employers-tax-guide-updated-september-2026/download)):

| Period | Monthly payer GA-V | G-7 return (all payers) |
| --- | --- | --- |
| January, February, March 2026 | 17 Feb, 16 Mar, 15 Apr 2026 | Q1: 30 Apr 2026 |
| April, May, June 2026 | 15 May, 15 Jun, 15 Jul 2026 | Q2: 31 Jul 2026 |
| July, August, September 2026 | 17 Aug, 15 Sep, 15 Oct 2026 | Q3: 2 Nov 2026 |
| October, November, December 2026 | 16 Nov, 15 Dec 2026, 15 Jan 2027 | Q4: 1 Feb 2027 |
| W-2 and 1099-NEC with G-1003 | | 1 Feb 2027 |
| Other 1099s with G-1003 | | 1 Mar 2027 |

Quarterly and annual payers pay with the G-7 on the G-7 dates. A due date on a Federal Reserve or Georgia holiday or a weekend moves to the next banking day.

### Unemployment insurance

Source: [GDOL employer UI FAQs](https://dol.georgia.gov/faqs-employers/employers-faqs-unemployment-insurance); [GDOL tax reporting and liability information](https://dol.georgia.gov/document/unemployment-tax/unemployment-insurance-tax-reporting-and-liability-information-employers/download).
1. **Liability.** An employer is generally liable if it has a quarterly payroll of $1,500 or at least one worker in 20 different calendar weeks in a calendar year; agricultural employers at $20,000 of gross quarterly payroll; domestic employers paying cash wages of $1,000 or more in a quarter. File Form DOL-1A after the first Georgia payroll.
2. **Rate.** New or newly covered employers pay a total rate of 2.70% until they qualify for an experience rate. Experienced employers use the rate on their annual DOL-626 notice, posted on the GDOL Employer Portal (the 2026 notices were posted 23 December 2025 and are not mailed).
3. **Base.** Tax is due on the first $9,500 of each employee's wages in the calendar year; all wages are still reported, because they set benefit eligibility.
4. **Report and pay quarterly** on the Employer's Quarterly Tax and Wage Report by the end of the month after the quarter (30 April, 31 July, 31 October, 31 January), through the Employer Portal. Qualified employers may defer quarterly tax of $5.00 or less to 31 January of the next year. Domestic employers may file annually on Form DOL-4A by 31 January.
5. **Late:** the greater of $20 or 0.05% of gross payroll for each month or part month a report is late; interest of 1.5% a month on unpaid contributions; a 20% cost of collection fee may be added to a deficiency.

### New hire reporting

Report every new hire and rehire, and employees returning to work, to the Georgia New Hire Reporting program at ga-newhire.com within 10 days, using the same FEIN as the quarterly wage reports ([GDOL employer newsletter DOL-5137](https://dol.georgia.gov/document/unemployment-benefits/employer-newsletter-dol-5137/download); [GDOL laws and regulations FAQs](https://dol.georgia.gov/faqs-employers/employers-faqs-laws-and-regulations), O.C.G.A. § 19-11-9.2). No employer is exempt.

## Boundary and exception table

| Situation | Rule |
| --- | --- |
| Wages paid in April 2026 | 5.19%: 4.99% may be used only from 11 May 2026 |
| Married couple, both working | Each uses the married filing separate column of Table E |
| Employee claims zero allowances | Subtract the standard deduction only |
| No G-4 and no usable W-4 | Single, zero allowances |
| G-7 for a quarter with no withholding | Still due |
| One G-7 showed more than $500 | EFT and electronic filing for every later period |
| Payday withholding of $100,001 | Next banking day by EFT, whatever the payer class |
| Employee passes $9,500 of wages | No more UI tax for that employee this year, but keep reporting the wages |
| Resident working in a state that requires withholding | No Georgia withholding required on those wages; the employee claims the other-state credit on Form 500 |

## Worked cases

**Case 1: semi-monthly withholding, DOR's own example.** A married employee filing joint, paid $2,000 semi-monthly, claims one child; the spouse does not work. Standard deduction $1,250.00 (Table E, column 1), dependent allowance $208.33, wages subject to withholding $541.67, times 4.99% = $27.03. The same pay before 11 May 2026 at 5.19% is $28.11.

```oa-check
name: GA 2026 semi-monthly withholding, married filing joint, one dependent
inputs:
  wages: 2000
  standard_deduction: 1250
  dependent_allowance: 208.33
  dependents: 1
steps:
  - subject: wages - standard_deduction - dependent_allowance * dependents
  - withholding_new_rate: round(subject * 0.0499, 2)
  - withholding_old_rate: round(subject * 0.0519, 2)
expected:
  subject: 541.67
  withholding_new_rate: 27.03
  withholding_old_rate: 28.11
```

**Case 2: unemployment insurance for a new employer.** A new Atlanta employer has three employees paid $30,000, $12,000 and $6,000 in 2026. UI tax applies to the first $9,500 of each: $9,500 + $9,500 + $6,000 = $25,000 of taxable wages, times 2.70% = $675.00 for the year. Without the wage base, it would have been $1,296.00: the base caps the cost per employee at $256.50.

```oa-check
name: GA 2026 UI tax, new employer, three employees
inputs:
  wage_1: 30000
  wage_2: 12000
  wage_3: 6000
  wage_base: 9500
  rate: 0.027
steps:
  - taxable: min(wage_1, wage_base) + min(wage_2, wage_base) + min(wage_3, wage_base)
  - ui_tax: taxable * rate
  - uncapped: (wage_1 + wage_2 + wage_3) * rate
  - max_per_employee: wage_base * rate
expected:
  taxable: 25000
  ui_tax: 675.00
  uncapped: 1296.00
  max_per_employee: 256.50
```

## When to refuse or refer

| Code | Situation | Action |
| --- | --- | --- |
| R-GAPR-CLASS | Worker classification disputes (employee or contractor), including GDOL audits | Refer |
| R-GAPR-SUTA | Successor employer, acquisition or transfer of experience | Refer: rate transfer rules apply |
| R-GAPR-MULTI | Employees in several states, reciprocity questions or relocation mid-year | Refer |
| R-GAPR-CREDIT | Withholding returns using job tax credits or other series 100 credits | Refer; e-filing required |
| R-GAPR-OTHER | G2-A, G2-RP, G2-LP, lottery or pension withholding | Refer |

## Filing and payment

1. **DOR:** register and file on the Georgia Tax Center (gtc.dor.ga.gov). Pay by EFT, ACH debit on the Georgia Tax Center, or ACH credit (register on Form EFT-002); Fedwire is not accepted. Paper filers send Form GA-V with monthly payments and Form G-7 each quarter.
2. **GDOL:** register on Form DOL-1A; file quarterly tax and wage reports and pay on the GDOL Employer Portal, where the DOL-626 rate notice is posted.
3. **After filing:** keep each G-4 on file; correct W-2s and 1099s after filing with an amended G-1003.

| Penalty | Rule | Maximum | Source |
| --- | --- | --- | --- |
| Withholding, failure to file (O.C.G.A. § 48-7-126) | $25 plus 5% of the tax withheld, plus 5% each later month | $25 plus 25% | [DOR penalty and interest rates](https://dor.georgia.gov/penalty-and-interest-rates) |
| Withholding, failure to pay (§ 48-7-126) | $25 plus 5% of the tax, plus 5% each later month (minimum $25) | $25 plus 25% | same |
| Failure to withhold | $10 per employee, quarterly | $10 per employee, quarterly | same |
| Late W-2 or 1099 to payees, or to DOR (§§ 48-7-105, 48-7-106) | $10 to $50 per form, by how late | depends on lateness | same |
| Not filing electronically when required (§ 48-2-44.1) | Greater of $25 or 5% of the tax due | none stated | same |
| Not paying electronically when required (§ 48-2-32(f)) | 10% of the tax due | none stated | same |

## Completion checklist

- G-4 on file for each employee; exempt or over 14 allowances sent to DOR.
- Rate switched to 4.99% no earlier than 11 May 2026; Table E amounts used for the pay period.
- Payer class set from the lookback period; one-day rule watched.
- G-7 filed every quarter; EFT and e-filing once over $500.
- G-1003 with W-2s and 1099-NECs by 1 February 2027, with 2026 overtime and tips figures on the forms.
- UI: liability tested, 2.70% or DOL-626 rate, $9,500 base, quarterly reports by month-end after each quarter.
- New hires reported within 10 days.

## Sources

| Source | URL | Read on |
| --- | --- | --- |
| DOR 2026 Employer's Tax Guide (updated September 2026). Read for the 2026 changes, the 11 May 2026 rate switch, who must withhold, G-4 rules, the payer classes and thresholds, the one-day rule, the EFT rule, Table E and its example, the 2026 due date tables and the overtime and tips reporting rules. | https://dor.georgia.gov/document/document/2026-employers-tax-guide-updated-september-2026/download | 2026-11-13 |
| DOR penalty and interest rates. Read for the withholding tax penalty table and the mandatory electronic filing and payment penalties. | https://dor.georgia.gov/penalty-and-interest-rates | 2026-11-13 |
| GDOL employer FAQs, unemployment insurance. Read for the $9,500 wage base, the 2.70% new employer rate, liability tests, the $5.00 deferral, late report penalty, interest and collection fee. | https://dol.georgia.gov/faqs-employers/employers-faqs-unemployment-insurance | 2026-11-13 |
| GDOL unemployment insurance tax reporting and liability information for employers. Read for the quarterly report due dates, penalty and interest. | https://dol.georgia.gov/document/unemployment-tax/unemployment-insurance-tax-reporting-and-liability-information-employers/download | 2026-11-13 |
| GDOL "2026 Employer Tax Rates Available Now" (23 December 2025). Read for the DOL-626 notices on the Employer Portal. | https://dol.georgia.gov/blog-post/2025-12-23/2026-employer-tax-rates-available-now | 2026-11-13 |
| GDOL "Employer Tax Rates Released" (27 December 2023). Read for the reinstatement of the Administrative Assessment from 1 January 2024 under HB 518. | https://dol.georgia.gov/blog-post/2023-12-27/employer-tax-rates-released | 2026-11-13 |
| GDOL employer newsletter DOL-5137. Read for new hire reporting within 10 days at ga-newhire.com. | https://dol.georgia.gov/document/unemployment-benefits/employer-newsletter-dol-5137/download | 2026-11-13 |
| GDOL employer FAQs, laws and regulations. Read for the new hire reporting duty (O.C.G.A. § 19-11-9.2). | https://dol.georgia.gov/faqs-employers/employers-faqs-laws-and-regulations | 2026-11-13 |

Not yet confirmed: the experience-rated UI rate range for 2026 (the older file's 0.04% to 8.10% had no source and was dropped); whether the 0.06% Administrative Assessment reinstated from 1 January 2024 still applies in 2026 and whether it sits inside the 2.70% new employer total (GDOL's 2025 and 2026 rate posts do not say); GDOL's statute or rule for the quarterly report itself was not opened.
