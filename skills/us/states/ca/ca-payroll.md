---
name: ca-payroll
description: California US-CA employer payroll for 2026. Compute PIT, SDI, UI and ETT; report DE 9, DE 9C, DE 34 and DE 542; determine deposits and final pay. Includes dated withholding schedules, worker classification, tips, wage statements, original worked cases and explicit holds for specialist issues.
version: "3.1"
jurisdiction: US-CA
tax_year: 2026
last_updated: 2026-11-27
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
tier: 2
domain: payroll
type: computation
---

# California payroll for employers, 2026

For an ordinary California commercial employer, withhold PIT under the **2026** EDD schedules and SDI at **1.3% of subject wages without an annual cap**; pay UI and, where applicable, ETT on each employee's first **USD 7,000** of calendar-year wages. Read the employer's DE 2088 before choosing its UI/ETT rates. [DE 44, printed p.8](https://edd.ca.gov/siteassets/files/pdf_pub_ctr/de44.pdf#page=16)

## Scope

This Guide covers ordinary, tax-rated commercial employers and California-covered employees for 2026. Load `us-tax-workflow-base`. A payroll or tax professional must review the calculation, classification and filings before use. The historical cases below keep their original years; they are not 2026 instructions.

Federal returns, other states and cross-border payroll, governmental/reimbursable employers, agriculture, households, cannabis licensing, garnishments, retirement plans, equity planning and city taxes require the handoffs under **When to refuse or refer**.

## Ask the client first

Obtain the current DE 2088 and EDD account details; federal deposit schedule; pay dates and year-to-date subject/taxable wages; each employee's DE 4 or eligible pre-2020 W-4; regular and supplemental pay; tip statements; HSA and other benefit codes; California work and residence locations; contractor contracts and federal reporting position; and any termination, vacation/PTO policy or collective bargaining agreement. Ask whether SDI is under the state plan or an approved Voluntary Plan, and whether corrections or EDD notices are outstanding. Do not infer a classification, exemption, allowance or tax rate from missing facts.

## The method, step by step

### Rates, bands and thresholds

The general rates page now leads with **2027**. Use its historical information and the dated 2026 documents for 2026 wages.

| Item and condition | 2026 value | Official source |
| --- | --- | --- |
| State-plan SDI, employee withholding on all SDI-subject wages; no cap from 2024 | 1.3% | [DE 44 p.8](https://edd.ca.gov/siteassets/files/pdf_pub_ctr/de44.pdf#page=16); [DE 3395](https://edd.ca.gov/siteassets/files/pdf_pub_ctr/de3395.pdf) |
| New employer UI, ordinarily for two to three years; successor and penalty-rate cases require separate review | 3.4% | [DE 44 p.77](https://edd.ca.gov/siteassets/files/pdf_pub_ctr/de44.pdf#page=85); [UIC 982](https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?sectionNum=982.&lawCode=UIC) |
| Ordinary experience-rated UI range; use the assigned DE 2088 rate | 1.5%–6.2% | [DE 44 p.8](https://edd.ca.gov/siteassets/files/pdf_pub_ctr/de44.pdf#page=16) |
| UI wage base, each employee, each calendar year | USD 7,000 | [UIC 930](https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?sectionNum=930.&lawCode=UIC); [DE 3395](https://edd.ca.gov/siteassets/files/pdf_pub_ctr/de3395.pdf) |
| ETT, employer contribution on UI taxable wages; new employers included. Negative reserve on computation date is exempt unless assigned the maximum rate under UIC 977(c); special/reimbursable employer exclusions also apply | 0.1% on first USD 7,000 | [UIC 976.6](https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?sectionNum=976.6&lawCode=UIC); [UIC 976.8](https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?sectionNum=976.8&lawCode=UIC); [DE 44 p.8](https://edd.ca.gov/siteassets/files/pdf_pub_ctr/de44.pdf#page=16) |
| Annual employer maxima at the ordinary highest UI rate / ETT rate | USD 434 / USD 7 | [DE 44 p.8](https://edd.ca.gov/siteassets/files/pdf_pub_ctr/de44.pdf#page=16); [EDD FUTA page](https://edd.ca.gov/en/payroll_taxes/federal-unemployment-tax-act) |
| Separate supplemental payment: bonus or stock option that constitutes wages / other supplemental wages | 10.23% / 6.6%, without allowances under the flat option | [R&TC 18663(b)–(c)](https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?sectionNum=18663.&lawCode=RTC); [DE 44 p.18](https://edd.ca.gov/siteassets/files/pdf_pub_ctr/de44.pdf#page=26) |
| Method B monthly single: low-income exemption / standard deduction / credit for one regular allowance | USD 1,575 / USD 476 / USD 14.03 | [2026 Method B Tables 1, 3, 4](https://edd.ca.gov/siteassets/files/pdf_pub_ctr/26methb.pdf#page=5) |
| State minimum wage from 1 January 2026; higher industry/local rules and statutory exemptions must be checked | USD 16.90/hour | [DIR minimum wage FAQ](https://www.dir.ca.gov/dlse/faq_minimumwage.htm) |
| FUTA credit reduction for California wages paid in 2026, federal Form 940; additional cost assumes full USD 7,000 FUTA wage base | 1.5 percentage points; up to USD 105 per employee | [EDD FUTA, 2026](https://edd.ca.gov/en/payroll_taxes/federal-unemployment-tax-act) |

UI and ETT are employer-paid; SDI and PIT are withheld from employees. PFL is part of SDI, not a separate deduction. Use **subject wages for each tax**, rather than treating gross cash pay or W-2 Box 16 as automatically the base for every tax. [DE 44 pp.8, 70](https://edd.ca.gov/siteassets/files/pdf_pub_ctr/de44.pdf#page=16)

### Register and classify

1. An ordinary commercial employer registers through [e-Services for Business](https://edd.ca.gov/eServices) or the Commercial Employer Account Registration and Update Form (DE 1) within **15 days** of paying **more than USD 100** of wages in a calendar quarter. Check an acquired business separately. [UIC 675](https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?sectionNum=675.&lawCode=UIC), [1086](https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?sectionNum=1086.&lawCode=UIC); [DE 44 p.6](https://edd.ca.gov/siteassets/files/pdf_pub_ctr/de44.pdf#page=14).
2. **AUDIT FLASH POINT: worker classification.** Where the ABC test applies, the hiring entity must establish all three conditions: freedom from control under contract and in fact; work outside its usual business; and an independently established business of the same nature. Express statutory exceptions remain effective; some use the Borello test instead. Do not apply ABC mechanically to an excepted occupation or relationship. California provides no federal safe-harbor relief. Refer a doubtful exception, corporate-officer case or dispute before treating the person as a contractor. [Labor Code 2775](https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?sectionNum=2775.&lawCode=LAB); [DE 44 p.7](https://edd.ca.gov/siteassets/files/pdf_pub_ctr/de44.pdf#page=15).
3. Obtain signed federal W-4 and state DE 4 certificates for new hires and withholding changes. Without a properly completed DE 4, use single with zero allowances. An unchanged W-4 submitted before 2020 can continue to govern California withholding; the post-2020 W-4 cannot supply California allowances. [EDD withholding certificates](https://edd.ca.gov/en/Payroll_Taxes/Rates_and_Withholding).

### Calculate each payday

Use the [2026 Method A and Method B schedules](https://edd.ca.gov/siteassets/files/pdf_pub_ctr/26methb.pdf). Method A is limited to wages or salaries **less than USD 1 million** and is not the computer method; Method B works manually or by computer. Select the actual payroll period, filing status and regular/additional allowances. For married employees with employed spouses, EDD recommends single status for both spouses' withholding or an additional flat amount to avoid underwithholding (Method B p.1).

For Method B: (1) compare gross wages with the low-income exemption; if at or below it, no PIT; (2) subtract the Table 2 estimated-deduction amount for additional allowances; (3) subtract the Table 3 standard deduction; (4) apply the correct period/status rate table; (5) subtract the Table 4 credit for **regular** allowances. Additional estimated-deduction allowances do not also earn that credit. Use the complete official tables for other pay periods, marital statuses and bands. [2026 Method B pp.1–6](https://edd.ca.gov/siteassets/files/pdf_pub_ctr/26methb.pdf#page=2).

Supplemental wages include bonuses, overtime, commissions, sales awards, vacation and severance. **Paid at the same time as regular wages:** combine and use the regular-period schedules. **Paid separately:** choose aggregate withholding (tax on combined current regular and supplemental wages, less tax already withheld on regular wages) or the category's flat rate without allowances. The stock-option rate applies only to options constituting wages; do not classify every equity payment as an option. [UIC 13043(c)–(d)](https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?sectionNum=13043.&lawCode=UIC); [DE 44 p.18](https://edd.ca.gov/siteassets/files/pdf_pub_ctr/de44.pdf#page=26).

**AUDIT FLASH POINT: large bonuses.** A withholding rate is not the employee's final annual tax rate. Do not promise the flat or aggregate method eliminates a balance due. Review the DE 4 and, for the personal return and estimated payments, load `ca-540-individual-return` and `ca-estimated-tax-540es`. Estimated payments do not replace the employer's mandatory wage withholding. [DE 44 p.18](https://edd.ca.gov/siteassets/files/pdf_pub_ctr/de44.pdf#page=26).

Check the actual pay code in [DE 231TP](https://edd.ca.gov/siteassets/files/pdf_pub_ctr/de231tp.pdf):

- HSA contributions as defined in IRC 106(d), both within and outside an IRC 125 cafeteria plan, are subject to UI/ETT, SDI and PIT withholding and reportable as California PIT wages (p.7). California excludes the federal HSA exclusions: [R&TC 17131.4](https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?sectionNum=17131.4&lawCode=RTC) and [17131.5](https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?sectionNum=17131.5&lawCode=RTC).
- Cash tips received in employment and included in the employee's written statement are subject/reportable for all four taxes when **USD 20 or more in a month**. Noncash tips are not. Employer-controlled/banquet amounts treated as regular wages are subject without waiting for employee reporting; refer service-charge or tip-pooling disputes. These are different categories (p.15). [UIC 927](https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?sectionNum=927.&lawCode=UIC).

**AUDIT FLASH POINT: an old SDI cap.** For state-plan SDI-subject wages, the history is 2024 **1.1%**, 2025 **1.2%**, 2026 **1.3%**, all uncapped. The 2023 rate was **0.9%**, capped at **USD 153,164**. Compare the payroll register's SDI-subject wages with withholding at the correct year's rate; investigate every discrepancy rather than inventing a tolerance or equating PIT and SDI wages. [DE 3395](https://edd.ca.gov/siteassets/files/pdf_pub_ctr/de3395.pdf); [UIC 985(b)](https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?sectionNum=985.&lawCode=UIC).

### Report new hires and contractors

**DE 34:** report California new hires and rehires after at least **60 consecutive days** of separation, ordinarily within **20 calendar days of first work for wages**. Acquisition hires count. A returning worker is not automatically a new hire after every absence: DE 44 p.56 specifies a return requiring new W-4/DE 4 certificates or the separation test. Include employer identifiers/contact information and employee name, SSN, address and actual start-of-work date. UIC 1088.5(d)(2) provides two monthly transmissions **12–16 days apart** for electronic/magnetic reporting; apply that cadence when filing electronically. Multistate single-state reporting elections require a separate check. [UIC 1088.5](https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?sectionNum=1088.5&lawCode=UIC); [DE 44 p.56](https://edd.ca.gov/siteassets/files/pdf_pub_ctr/de44.pdf#page=64).

**DE 542:** first establish UIC 1088.8(a)'s federal-return condition: a California-connected service-recipient **makes or is required to make** a return under IRC 6041A(a) for service compensation. The service-provider is an **individual**, not an employee for California purposes. Within that scope, report within **20 days of the earlier** of payments aggregating **USD 600 in a year** or contract(s) providing for **USD 600 in a year**. Do not treat every corporate vendor or every USD 600 payment as automatically reportable; assess the federal filing condition separately with `us-1099-nec-issuance`. The California statutory amount does not itself determine whether a 2026 federal return is required. [UIC 1088.8(a)–(c)](https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?sectionNum=1088.8&lawCode=UIC).

File through e-Services (or the permitted DE 542 mail/fax route). Supply the provider's individual name, **SSN rather than FEIN**, address, contract start, amount and expiration/ongoing status; and the recipient's name, address, phone and applicable identifying numbers. The report is additional to federal information reporting. Absent good cause, failure to report can attract **USD 24**, or **USD 490** for conspiracy to omit or falsify the report. [DE 44 p.58](https://edd.ca.gov/siteassets/files/pdf_pub_ctr/de44.pdf#page=66); [UIC 1088.8(c), (e)](https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?sectionNum=1088.8&lawCode=UIC).

### Quarterly returns, deposits and corrections

File **both DE 9 and DE 9C each quarter**, including no-wage quarters while the account is active. DE 9 reconciles taxes and deposits; DE 9C gives employee-level subject wages, PIT wages and PIT withholding. It does **not** report an individual employee's SDI withholding amount. Pay a DE 9 balance separately; an electronic payment needs no physical DE 88 coupon. Use e-Services to select the correct quarter, submit each return and payment, and retain the confirmation. [UIC 1088, 13021(a)](https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?sectionNum=13021.&lawCode=UIC); [EDD required filings](https://edd.ca.gov/en/payroll_taxes/required_filings_and_due_dates/); [DE 44 pp.64–65](https://edd.ca.gov/siteassets/files/pdf_pub_ctr/de44.pdf#page=72).

| 2026 wage quarter | Return/payment due | Last timely return date; quarterly EFT initiation date | Quarterly EFT settlement by | Official source |
| --- | --- | --- | --- | --- |
| Q1, January–March | 1 April 2026 | 30 April 2026 | 1 May 2026 | [DE 44 pp.61, 64–65](https://edd.ca.gov/siteassets/files/pdf_pub_ctr/de44.pdf#page=69) |
| Q2, April–June | 1 July 2026 | 31 July 2026 | 3 August 2026 | [DE 44 pp.61, 64–65](https://edd.ca.gov/siteassets/files/pdf_pub_ctr/de44.pdf#page=69) |
| Q3, July–September | 1 October 2026 | 2 November 2026 | 3 November 2026 | [DE 44 pp.61, 64–65](https://edd.ca.gov/siteassets/files/pdf_pub_ctr/de44.pdf#page=69) |
| Q4, October–December | 1 January 2027 | 1 February 2027 | 2 February 2027 | [DE 44 pp.61, 64–65](https://edd.ca.gov/siteassets/files/pdf_pub_ctr/de44.pdf#page=69) |

UI/ETT are quarterly, although earlier payments are allowed. PIT/SDI follow the federal schedule **and accumulated PIT**, not SDI amounts or the federal schedule alone. [UIC 1110](https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?sectionNum=1110.&lawCode=UIC), [13021](https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?sectionNum=13021.&lawCode=UIC).

| Federal schedule | Accumulated California PIT | PIT and SDI deposit deadline | Official source |
| --- | --- | --- | --- |
| Any | Less than USD 350 | Quarterly dates above | [EDD deposit table](https://edd.ca.gov/en/payroll_taxes/timely_payroll_tax_deposits/) |
| Next-day or semiweekly | USD 350–400 inclusive | 15th of following month | [EDD deposit table](https://edd.ca.gov/en/payroll_taxes/timely_payroll_tax_deposits/) |
| Next-day | More than USD 400 | Next business day | [EDD deposit table](https://edd.ca.gov/en/payroll_taxes/timely_payroll_tax_deposits/) |
| Semiweekly | More than USD 400; Wednesday–Friday payday | Following Wednesday | [EDD deposit table](https://edd.ca.gov/en/payroll_taxes/timely_payroll_tax_deposits/) |
| Semiweekly | More than USD 400; Saturday–Tuesday payday | Following Friday | [EDD deposit table](https://edd.ca.gov/en/payroll_taxes/timely_payroll_tax_deposits/) |
| Monthly, quarterly or annual | USD 350 or more | 15th of following month | [EDD deposit table](https://edd.ca.gov/en/payroll_taxes/timely_payroll_tax_deposits/) |

Accumulate PIT across payrolls; UIC 13021(h) also catches the USD 350 threshold **cumulatively for two or more months**. A monthly deadline on a weekend/legal holiday moves to the next business day. Semiweekly depositors have three business days after the end of the semiweekly period, with an additional business day when one is a legal holiday. [DE 44 p.60](https://edd.ca.gov/siteassets/files/pdf_pub_ctr/de44.pdf#page=68).

**Payment timing matters.** Quarterly ACH debit must be completed before **3 p.m. Pacific** by the initiation date in the table and settle by the listed settlement date; ACH credit follows the bank's processing requirements. Do not apply a blanket “three business days after every payday” rule. UIC 13021(d)(2) generally deems EFT complete on initiation only if settlement is by the following business day; (d)(3) gives the specific three-business-day settlement rule for one-day-rule payments. Preserve the payment confirmation and verify settlement. [UIC 13021(d)](https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?sectionNum=13021.&lawCode=UIC); [DE 44 p.61](https://edd.ca.gov/siteassets/files/pdf_pub_ctr/de44.pdf#page=69).

The e-file/e-pay mandate applies unless EDD approves a waiver. Request **DE 1245W** for lack of automation, severe economic hardship, federal exemption or other good cause; it is not retroactive. Without applicable relief, paper DE 9 costs **USD 50 per return**, DE 9C **USD 20 per wage item**, and DE 88 **15% of the amount due**. Late payments ordinarily incur **15% plus interest**; contribution penalties under UIC 1112 have a good-cause condition. UIC 13021(f) also provides relief for a nonwillful payment of at least **95%** under (c)/(d) when the remainder is paid with the next payment. Do not replace EDD interest with an FTB rate or infer the current rate; follow EDD's [interest page](https://edd.ca.gov/en/payroll_taxes/interest_rate). Unpaid balances may lead to a DE 2176 and public tax lien. Failure to remit withholding can also carry criminal consequences; check that issue with a partner accountant and counsel. [DE 44 pp.52, 61](https://edd.ca.gov/siteassets/files/pdf_pub_ctr/de44.pdf#page=60); [UIC 1112](https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?sectionNum=1112.&lawCode=UIC).

Reconcile annual DE 9C PIT wages/withholding to **W-2 Boxes 16/17**; reconcile payroll-register SDI withholding to **W-2 Box 14**, not to a nonexistent employee SDI field on DE 9C. Box 1 and Box 16 can differ. EDD/IRS compare Form 940 with DE 9 **C (subject wages)** and **D2 (UI taxable wages)**. Q4 DE 9 is a quarterly return; the separate California annual reconciliation return is no longer required for 2012 onward. [DE 44 pp.70, 78](https://edd.ca.gov/siteassets/files/pdf_pub_ctr/de44.pdf#page=78); [UIC 13021(j)(2)](https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?sectionNum=13021.&lawCode=UIC).

Correct filed DE 9/DE 9C information in e-Services or with **DE 9ADJ**, not a DE 9X. Correct a wrongly issued W-2 using W-2c instructions. Do not recover SDI/PIT from employees or refund previously reported PIT indiscriminately: the DE 44 p.63 adjustment table distinguishes timing, written permission and whether the original W-2 was correct. Check the specific adjustment with one of our partner accountants. [DE 44 pp.63, 67, 70](https://edd.ca.gov/siteassets/files/pdf_pub_ctr/de44.pdf#page=71).

Use the DE 2088 issued for the relevant year. A protest of a protestable item is generally due within **60 days of issue**; EDD may grant up to **60 additional days for good cause requested before the deadline**. SDI/ETT statutory rates are not protestable. Refer rate disputes, successor reserve transfers, penalty rates under UIC 977(c) and voluntary UI contributions rather than assuming a new-employer rate or an unconditional March deadline. [DE 44 pp.77–78](https://edd.ca.gov/siteassets/files/pdf_pub_ctr/de44.pdf#page=85); [DE 231Z p.2](https://edd.ca.gov/siteassets/files/pdf_pub_ctr/de231z.pdf#page=2).

### Wage statements, tips and final pay

For the ordinary commercial employers in scope, Labor Code **226(a)** requires an accurate written wage statement semimonthly or at each payment: gross pay; hours (subject to statutory exceptions); piece units/rates where relevant; deductions; net pay; pay-period dates; employee name and last four SSN digits or non-SSN ID; employer legal name/address; and applicable hourly rates with hours at each. Deductions on written employee orders may be aggregated. Additional temporary-service/farm-labor items and the hours exceptions must be checked in the statute. Refer wage-statement penalties and PAGA; a missing item does not automatically prove every penalty condition. [Labor Code 226(a), (e), (j)](https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?sectionNum=226.&lawCode=LAB).

Tips belong to employees; no employer tip credit against wages is allowed. Pay credit-card tips in full without deducting processing costs, no later than the next regular payday after authorization. [Labor Code 351](https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?sectionNum=351.&lawCode=LAB). Apply the higher applicable state, industry or local minimum wage; refer exempt-worker or disputed service-charge/tip-pool cases.

| Ordinary final-pay situation | Rule and conditions | Official source |
| --- | --- | --- |
| Discharge | Earned, unpaid wages immediately; industry/statutory exceptions must be checked before using this default | [Labor Code 201](https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?sectionNum=201.&lawCode=LAB) |
| Quit, no written fixed-period contract | At quitting if at least 72 hours' notice; otherwise within 72 hours. If the employee without that notice requests mailing and supplies an address, mailing date is payment date | [Labor Code 202](https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?sectionNum=202.&lawCode=LAB) |
| Earned unused vacation | Where policy/contract provides paid vacation, vested balance at final rate, subject to a collective bargaining agreement; no forfeiture of vested vacation | [Labor Code 227.3](https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?sectionNum=227.3&lawCode=LAB) |
| Final direct deposit | Employee voluntarily authorizes the account; deposit must still comply with termination/quit payment deadlines | [Labor Code 213(d)](https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?sectionNum=213.&lawCode=LAB) |

**AUDIT FLASH POINT: waiting time.** For a willful failure within Labor Code 203, penalty wages run at the daily wage rate from the due date until payment or commencement of a court action, **at most 30 calendar days**. Avoiding or refusing a fully tendered payment excludes that period. A genuine good-faith wage dispute can prevent the penalty; a DLSE complaint does not itself stop accrual. Earned vacation is wages; business expense reimbursement is not wages for this penalty. Daily-rate calculations and disputes need counsel. The original numerical illustration of **USD 1,000/day**, **USD 50 unpaid**, up to **USD 30,000** is arithmetic only if all penalty conditions hold; the penalty is not capped at the USD 50 debt. [Labor Code 203](https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?sectionNum=203.&lawCode=LAB); [DIR waiting-time FAQ](https://www.dir.ca.gov/dlse/FAQ_WaitingTimePenalty.htm).

Workers' compensation must be secured through authorized insurance or approved self-insurance; do not say every employer must buy an insurance policy regardless of its self-insurance approval. Check coverage for the actual employees/work location. Premium/class-code estimates and coverage disputes: check this point with one of our partner accountants and the insurer. [Labor Code 3700](https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?sectionNum=3700.&lawCode=LAB).

## Boundary and exception table

| Situation | Action |
| --- | --- |
| Missing input, disputed contractor status, doubtful exemption or wage base | Hold the calculation; obtain facts or refer. Do not substitute an unsupported “conservative” legal answer |
| Separate bonus versus bonus with salary | Apply the two distinct rules above; classification of the payment comes before the rate |
| UI/ETT annual base exhausted | Stop those contributions on subsequent wages; state-plan SDI continues on all SDI-subject wages |
| Approved Voluntary Plan or special employer | Hold the ordinary state-plan calculation; check with one of our partner accountants |
| Different year | Use that year's source; historical inputs below are not relabelled 2026 |

## Worked cases

All people and businesses in these cases are hypothetical. No case is a taxpayer declaration. Round computed withholding to cents. The federal side is outside the California-only net amounts.

### Ana: monthly salary, January 2026

Preserved inputs: single, **one regular DE 4 allowance**, no additional deduction allowances, monthly **USD 6,000**; new employer with ETT applicable. Method B gives taxable wages **6,000 − 476 = 5,524**; Table 20 band **over 4,796 through 6,060** gives **182.24 + (5,524 − 4,796) × 8.8% = 246.30**, less **14.03** = **PIT 232.27**. SDI **78.00**; pay after California deductions **5,689.73**. January employer UI **204.00**, ETT **6.00**; February remaining base **1,000**, UI **34.00**, ETT **1.00**; no more UI/ETT for Ana that year after the base is used. Annual UI **238**, ETT **7**. [2026 Method B Tables 1, 3, 4, 20](https://edd.ca.gov/siteassets/files/pdf_pub_ctr/26methb.pdf); [DE 44 p.8](https://edd.ca.gov/siteassets/files/pdf_pub_ctr/de44.pdf#page=16).

```oa-check
name: CA payroll 2026, monthly single employee, Method B and employer UI and ETT
inputs:
  gross: 6000
  std_deduction: 476
  band_floor: 4796
  band_base: 182.24
  allowance_credit: 14.03
steps:
  - taxable: gross - std_deduction
  - tax_before_credit: round((taxable - band_floor) * 0.088 + band_base, 2)
  - pit: tax_before_credit - allowance_credit
  - sdi: gross * 0.013
  - net_after_ca: gross - pit - sdi
  - ui_jan: min(gross, 7000) * 0.034
  - ui_feb: min(gross, 7000 - min(gross, 7000)) * 0.034
  - ett_year: 7000 * 0.001
expected:
  taxable: 5524
  tax_before_credit: 246.30
  pit: 232.27
  sdi: 78.00
  net_after_ca: 5689.73
  ui_jan: 204.00
  ui_feb: 34.00
  ett_year: 7.00
```

### Ben: tipped server, Q1 2026

Preserved inputs: **480 hours**, **USD 16.90/hour**, **USD 9,000 cash tips** in written monthly statements, each month over **USD 20**; no higher local/industry minimum applies; new employer with ETT applicable. Direct wages **8,112**, subject wages **17,112**, SDI **222.46**, UI **238**, ETT **7**. Do not invent PIT or full net pay without the payroll dates/period and DE 4. Ben's direct wages already exceed the UI base; the old assertion that this case proves tips alone make him reach the cap is incorrect. [DIR minimum wage](https://www.dir.ca.gov/dlse/faq_minimumwage.htm); [DE 231TP p.15](https://edd.ca.gov/siteassets/files/pdf_pub_ctr/de231tp.pdf#page=15); [DE 44 p.8](https://edd.ca.gov/siteassets/files/pdf_pub_ctr/de44.pdf#page=16).

```oa-check
name: CA payroll 2026, tipped server
inputs:
  hours: 480
  hourly: 16.90
  tips: 9000
steps:
  - direct: hours * hourly
  - wages: direct + tips
  - sdi: round(wages * 0.013, 2)
  - ui: min(wages, 7000) * 0.034
  - ett: min(wages, 7000) * 0.001
expected:
  direct: 8112
  wages: 17112
  sdi: 222.46
  ui: 238
  ett: 7
```

### Ana: separate March 2026 bonus

Preserved inputs: same monthly **USD 6,000** salary and allowances; separate **USD 10,000** March bonus, UI/ETT base already exhausted in February. Flat PIT **1,023**, SDI **130**, UI/ETT **zero**. Aggregate alternative: combined taxable wages **15,524**, Table 20 band **over 6,060 through 30,956**; PIT on the combined amount **1,247.61**, less salary PIT **232.27**, leaves bonus PIT **1,015.34**. Flat exceeds aggregate here by **7.66**. Neither method guarantees the employee's final tax. If bonus and salary are paid together, use aggregate withholding. [DE 44 p.18](https://edd.ca.gov/siteassets/files/pdf_pub_ctr/de44.pdf#page=26); [2026 Method B Table 20](https://edd.ca.gov/siteassets/files/pdf_pub_ctr/26methb.pdf#page=9).

```oa-check
name: CA payroll 2026, separate bonus, flat rate against aggregate method
inputs:
  bonus: 10000
  salary: 6000
  std_deduction: 476
  band_floor: 6060
  band_base: 293.47
  allowance_credit: 14.03
  pit_on_salary: 232.27
steps:
  - flat: bonus * 0.1023
  - taxable_total: salary + bonus - std_deduction
  - pit_total: round((taxable_total - band_floor) * 0.1023 + band_base, 2) - allowance_credit
  - aggregate_on_bonus: pit_total - pit_on_salary
  - difference: flat - aggregate_on_bonus
  - sdi_bonus: bonus * 0.013
expected:
  flat: 1023.00
  pit_total: 1247.61
  aggregate_on_bonus: 1015.34
  difference: 7.66
  sdi_bonus: 130.00
```

### Original 2025 inputs retained on a non-usable hold

**Do not use these historical cases to calculate, file, claim an exemption or quote a liability.** Their earlier PIT estimates, net/remittance totals, federal/equity assumptions, CalSavers conclusions and insurance estimates are withdrawn. Check each point with one of our partner accountants. The original facts remain available for a proper year-specific calculation. The original CalSavers exposure illustrations for **5 and 50 employees** are also on hold; do not use the withdrawn penalty amounts:

- **Acme Consulting LLC**, Mountain View, single-member LLC with no S election: five W-2 employees from **1 January 2025**; annual salaries/filing status/DE 4 allowances: **Ada (CEO) 250,000 / MFJ / 2; Ben (Senior Dev) 180,000 / single / 1; Carol (Dev) 120,000 / HOH / 2; Dan (Designer) 90,000 / single / 1; Eve (Office Mgr) 60,000 / MFJ / 3**. Corresponding stipulated Q1 wages **62,500; 45,000; 30,000; 22,500; 15,000**. No bonuses/equity; founder-only Solo 401(k), no employee retirement plan; federal monthly deposit schedule assumed from prior-year aggregate below **50,000**. These are historical case assumptions, not findings that such a plan or schedule was lawful. Hold CalSavers, owner-plan eligibility and insurance/class-code costing.
- **Bella's Bistro LLC**, Sacramento, Q1 **2025**: ten W-2 staff (**4 servers, 2 cooks, 1 dishwasher, 2 bartenders, 1 salaried manager**). **Sarah**, single with **one allowance**, works **480 hours at USD 16.50**, reports **USD 5,000 cash tips** and receives **USD 4,000 credit-card tips**; direct pay **7,920**, combined amount **16,920**. The original automatic **20% service charge for parties of six or more**, tip-pool and exempt-manager assumptions need separate review. No historical PIT approximation or penalty is usable.
- **Crescent Robotics Inc.**, Delaware C corporation registered in California with sole headquarters in San Francisco: **Frank USD 250,000 annual salary**, **8 engineers at USD 200,000–400,000**, all receiving RSU grants vesting quarterly; Q1 **2025** Frank cliff-vest **USD 400,000 FMV** from a **2021 grant**, engineers' vests **USD 2,800,000**, aggregate base salaries **USD 625,000**; original projection assumes **four** Frank vests of that amount and a **401(k) with company match**. Hold RSU tax timing/category, federal deductions, annual personal-tax exposure, CalSavers exemption/attestation and wage-statement treatment; do not apply a stock-option rate to every RSU.

The earlier inline SDI illustration is preserved separately: **USD 5 million of stipulated SDI-subject 2025 wages × 1.2% = USD 60,000**; the 2023 maximum comparison is **153,164 × 0.9% = 1,378.48**. This is a comparison of different years, not a claim that the employee's facts were identical or an employer expense. [DE 3395](https://edd.ca.gov/siteassets/files/pdf_pub_ctr/de3395.pdf).

## When to refuse or refer

Each hold below means **do not use an earlier rate, deadline, exclusion or legal conclusion**. Check this point with one of our partner accountants; obtain employment counsel for a legal dispute.

- CalSavers: mandate, employer/employee thresholds, phase dates, eligibility/exemptions, contribution/escalation rates, census/remittance duties and enforcement. The historical Acme/Crescent cases do not establish compliance.
- Voluntary SDI/PFL plans (approval, employee consent, benefits, contributions, security), elective coverage, PFL benefit amounts and recovery of an employee withholding shortfall.
- Successor reserve transfers, SUTA dumping/UIC 977(c), voluntary UI contribution eligibility/deadlines and contested DE 2088 items.
- ABC/Borello exceptions, business-to-business/professional/freelancer cases, disputed employee status, wage-statement or PAGA damages, limitation periods, workers' compensation penalties/premiums, and wage/commission/bonus disputes.
- Special final-pay industries, including seasonal perishable foods, film, oil drilling and hiring-hall arrangements; vacation accrual caps, sick leave/combined PTO, and penalty tax reporting.
- San Francisco, Los Angeles and other local business/payroll taxes, city thresholds, exemptions and filing dates; use the actual work location for local wage questions.
- Multistate/nonresident/cross-border payroll and reciprocal elections (`us-state-payroll-matrix`); other-state new hires (`us-state-new-hire-reporting-matrix`); federal payroll and returns (`us-form-941-940-payroll`); federal contractor reporting (`us-1099-nec-issuance`).
- Public/reimbursable, agricultural, household or cannabis-specific employment, garnishments/child support, retirement/ERISA, visas/totalization, equity/83(b)/409A (`us-equity-compensation-restricted-stock-units-and`), and FTB DE 4 copy/exemption requirements or personal-return penalties. Use `us-s-corp-election-decision`, `ca-llc-fee-and-tax` and `us-ca-return-assembly` for their separate owner/entity/return jobs; a route is not a determination that an owner is or is not an employee.

## Filing and payment

Use the reporting/deposit tables above and keep filing separate from payment. Do not wait for quarterly filing when PIT/SDI deposits are due more often. For 2026 FUTA, EDD now states a **1.5 percentage-point reduction** of the normal **5.4% credit against 6.0%**, leaving **3.9% credit**; the incremental cost is **USD 105** on a full **USD 7,000** FUTA base. This replaces the old “2026 not set until after year end” text. Complete Form 940 and the federal credit computation in the federal payroll Guide; California UI taxable wages are not a substitute for checking the federal base/exclusions. [EDD FUTA 2026](https://edd.ca.gov/en/payroll_taxes/federal-unemployment-tax-act).

## Completion checklist

- [ ] Verify employer category, state-plan/VP coverage, DE 2088 rates and the correct year's source.
- [ ] Recompute subject wages for each tax, PIT method/allowances, SDI and remaining UI/ETT bases.
- [ ] Apply contractor/new-hire scope and reporting deadlines; hold unresolved classification cases.
- [ ] Submit both quarterly reports, required deposits and separate balances; retain confirmations and verify EFT settlement.
- [ ] Reconcile DE 9/DE 9C, payroll registers, W-2 and Form 940; use the actual correction instructions.
- [ ] Review wage statements, local/industry wage requirements, termination and vacation facts; escalate held topics.

**Reviewer responsibility.** This is a professional reference. For written advice on federal tax matters, apply the facts-and-law requirements in [Circular 230 §10.37](https://www.irs.gov/pub/irs-pdf/pcir230.pdf#page=26); it does not replace the reviewer's judgment or an engagement. This Guide's workflow requires competent payroll/tax review before advice or filing. Do not describe that internal review requirement as a separate federal licensing rule for every California payroll calculation.

## Sources

Read on **2026-11-27**. Page numbers below are printed page numbers unless marked PDF page. Official PDFs were read in memory; a successful download alone was not treated as a read. Legislature pages were read in the ordinary browser after direct-reader failures.

| Official source | Portions actually read | Read date |
| --- | --- | --- |
| [2026 California Employer's Guide, DE 44 Rev.52 (4-26)](https://edd.ca.gov/siteassets/files/pdf_pub_ctr/de44.pdf) | Read for pp.6–8 employer/classification/taxes; p.18 supplemental wages; pp.52–53 e-filing; pp.56,58 reporting; pp.60–65 deposits/returns; p.67 corrections; pp.70–71 W-2; pp.77–78 rates/protests | 2026-11-27 |
| [2026 Method B](https://edd.ca.gov/siteassets/files/pdf_pub_ctr/26methb.pdf) | Read for pp.1–6 instructions/allowances; p.7 annual bands; p.9 monthly Table 20 and neighbouring headings | 2026-11-27 |
| [DE 3395 Rev.69 (1-26)](https://edd.ca.gov/siteassets/files/pdf_pub_ctr/de3395.pdf) | Read for 2023–2026 UI/SDI/ETT rows and no-cap footnote | 2026-11-27 |
| [DE 231TP](https://edd.ca.gov/siteassets/files/pdf_pub_ctr/de231tp.pdf) | Read for pp.7,15–16 HSA, tip categories, related footnotes | 2026-11-27 |
| [DE 231Z](https://edd.ca.gov/siteassets/files/pdf_pub_ctr/de231z.pdf#page=2) | Read for p.2 DE 2088 notification, non-protestable statutory rates and ETT exclusions | 2026-11-27 |
| [EDD rates and withholding](https://edd.ca.gov/en/Payroll_Taxes/Rates_and_Withholding) | Read for Year headings, DE 2088, W-4/DE 4 and pre-2020 exception | 2026-11-27 |
| [EDD required filings](https://edd.ca.gov/en/payroll_taxes/required_filings_and_due_dates/) | Read for DE 9, DE 9C, DE 88, no-wage quarters and submission requirements | 2026-11-27 |
| [EDD deposit requirements](https://edd.ca.gov/en/payroll_taxes/timely_payroll_tax_deposits/) | Read for Complete 2026 deposit table | 2026-11-27 |
| [EDD 2026 calendar](https://edd.ca.gov/en/payroll_taxes/Due_Dates_Calendar/) | Read for Quarterly dates and weekend/holiday rule | 2026-11-27 |
| [EDD FUTA](https://edd.ca.gov/en/payroll_taxes/federal-unemployment-tax-act) | Read for Wages paid in 2026, credit reduction and Form 940 reconciliation | 2026-11-27 |
| [DIR minimum wage](https://www.dir.ca.gov/dlse/faq_minimumwage.htm) | Read for 2026 USD 16.90, higher industry/local rates and exemptions | 2026-11-27 |
| [DIR waiting-time FAQ](https://www.dir.ca.gov/dlse/FAQ_WaitingTimePenalty.htm) | Read for Willfulness/good faith, daily rate, calendar-day cap, stopping accrual, expenses/vacation | 2026-11-27 |
| [California Unemployment Insurance Code](https://leginfo.legislature.ca.gov/faces/codes.xhtml) | Read for Sections 675, 926–927, 930, 976, 976.6, 976.8, 982, 984–985, 1086, 1088, 1088.5, 1088.8, 1110, 1112, 13021, 13043; exact section links accompany the rules | 2026-11-27 |
| [California Revenue and Taxation Code](https://leginfo.legislature.ca.gov/faces/codes.xhtml) | Read for Sections 17131.4, 17131.5, 18663, operative HSA/supplemental rules | 2026-11-27 |
| [IRS Circular 230](https://www.irs.gov/pub/irs-pdf/pcir230.pdf#page=26) | Read for Section 10.37, federal written advice; internal payroll-review policy distinguished | 2026-11-27 |
| [California Labor Code](https://leginfo.legislature.ca.gov/faces/codes.xhtml) | Read for Sections 201–203, 213, 226, 227.3, 351, 1182.12(c), 2775, 3700; exact section links accompany the rules | 2026-11-27 |

**Not yet confirmed for usable guidance:** all topics explicitly held under When to refuse or refer, including the three historical 2025 cases' withdrawn conclusions. Annual personal-income-tax brackets are not payroll withholding tables; do not resurrect the earlier annual-return bracket table or 2027 payroll figures for 2026.
