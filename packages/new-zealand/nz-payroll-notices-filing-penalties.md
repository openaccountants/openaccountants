---
name: nz-payroll-notices-filing-penalties
description: >
  Use this skill for New Zealand employer payroll obligations after PAYE is worked out, for paydays from 1 April 2026 to 31 March 2027: student-loan recovery notices (SLCIR) and voluntary extra deductions, employee child-support deduction notices and protected earnings, District Court attachment orders, Inland Revenue tax-arrears deduction notices, payday filing of employment information, paying deductions to Inland Revenue, correcting employment information, keeping PAYE records, late and non-electronic filing penalties, and late payment and non-payment penalties. Trigger on deduction notice, child support deduction, attachment order, arrears notice, protected earnings, payday filing, employment information, IR348, payroll correction, PAYE penalty. PAYE itself is in nz-employer-payroll.
version: 1.0
jurisdiction: NZ
tax_year: 2026
last_updated: 2026-11-14
category: payroll
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
tier: 2
domain: payroll
type: computation
---

# New Zealand payroll: deduction notices, payday filing, corrections and penalties (2026-27)

Figures are for tax year 2026, meaning payroll paid from 1 April 2026 to 31 March 2027 (the New Zealand 2026-27 tax year, which Inland Revenue calls the 2027 income year). All amounts are New Zealand dollars. Written by Ryan Duguid on his fork (ryanduguid/openaccountants, rules checked 12 and 13 November 2026) and imported on 14 November 2026. It has not been reviewed by an accountant.

## Scope and who this is for

This skill covers what a New Zealand employer does once PAYE is worked out (see `nz-employer-payroll`): deductions under recovery, child-support, court and arrears notices, filing employment information for each payday, paying the deductions, correcting errors, keeping records, and the penalties for filing and paying late.

- **Companions:** PAYE codes and calculations are in `nz-employer-payroll`; KiwiSaver and ESCT in `nz-kiwisaver-esct`; employee share schemes in `nz-employee-share-schemes`.
- **Does not cover:** competing-notice cases not resolved below, older or exceptional corrections, mixed employer-monthly-schedule debt, current interest, shortfall and criminal penalties, and full remission and collection rules.

## Ask the client first

- Employer registration, actual payday, pay frequency and period covered. [Register as an employer as soon as you start employing staff](https://www.ird.govt.nz/setting-up-a-business-or-organisation).
- Employee classification, completed IR330 tax-code declaration and any Inland Revenue tax-code, tailored-rate, student-loan, child-support or arrears notice. Resolve conflicting instructions before using a rate.
- KiwiSaver membership and eligibility, valid deduction-rate instruction, employer contribution agreement (including whether it promises a gross or net-of-ESCT amount) and any valid opt-out, savings-suspension or temporary-rate-reduction notice.
- Annual PAYE and ESCT figures, any connected employers and the established filing and payment schedules. The $50,000 electronic filing test and $500,000 remittance test serve different purposes.
- Is the employer required to file electronically, and has any payday been filed or paid late?

## The method, step by step

1. **Confirm the notices held** and the order the law gives them.
2. **Work out each deduction** within the protected earnings and maximum deduction rules below.
3. **File employment information** for each payday by the due date, electronically if required.
4. **Pay the deductions** by the due date for the employer's size.
5. **Correct errors** in the period the rules allow, and keep the records.
6. **Check penalties** for any late or missed filing or payment.

### Rates, bands and thresholds

Key figures for payroll paid from 1 April 2026 to 31 March 2027. The detail and conditions are in the sections below.

| Item | Figure | Condition | Source |
| --- | --- | --- | --- |
| Electronic filing of employment information | Required at annual PAYE and ESCT of $50,000 or more | Below $50,000 the employer may file on paper | https://www.ird.govt.nz/employing-staff/payday-filing/filing-employment-information-electronically |
| Paying deductions, annual PAYE and ESCT less than $500,000 | Monthly, by the 20th of the following month |  | https://www.ird.govt.nz/employing-staff/payday-filing/paying-deductions-to-inland-revenue |
| Paying deductions, annual PAYE and ESCT more than $500,000 | Paydays 1st to 15th: by the 20th of that month; 16th to month end: by the 5th of the next month | Paydays 16 to 31 December: by 15 January. The page does not say which group applies at exactly $500,000 | https://www.ird.govt.nz/employing-staff/payday-filing/paying-deductions-to-inland-revenue |


### Student-loan recovery and voluntary extra deductions

Keep ordinary student-loan deductions, **SLCIR** recovery and **SLBOR** voluntary deductions separate. An IRD SLCIR notice states the amount to recover and the percentage to deduct until that amount has been reached. Use that notice, not an automatic extra 5% on every SL employee. For ordinary primary employment, the maximum recovery rate is **5% of gross pay above the pay-period repayment threshold**; for secondary employment it is **5% of gross pay without that threshold**. Truncate gross pay to whole dollars for this calculation and truncate the deduction to cents. For 2026-27 the weekly primary threshold is **$464**; use the corresponding period threshold already set out above. Do not recover more than the remaining amount required by the notice. [S2, section 3, PDF pages 9-10](https://www.ird.govt.nz/-/media/project/ir/home/documents/digital-service-providers/software-providers/payroll-calculations-business-rules-specifications/payroll-calculations-and-business-rules-specification.pdf?modified=20260401012317), [S25](https://www.ird.govt.nz/student-loans/living-in-new-zealand-with-a-student-loan/repaying-my-student-loan-when-i-earn-salary-or-wages/student-loan-underpayments)

A voluntary SLBOR deduction uses the employee's actual requested amount or percentage. Report ordinary loan deductions, SLCIR and SLBOR in their respective employment-information fields. These are additional loan deductions, not PAYE income tax. Keep the notice balance, effective dates, actual deduction and any cancellation or certificate change together; an SDR and its cancellation trail require the separate checks above. [S2, sections 3 and 5.9.2](https://www.ird.govt.nz/-/media/project/ir/home/documents/digital-service-providers/software-providers/payroll-calculations-business-rules-specifications/payroll-calculations-and-business-rules-specification.pdf?modified=20260401012317), [S13, PDF page 22](https://www.ird.govt.nz/-/media/project/ir/home/documents/forms-and-guides/ir300---ir399/ir335/ir335.pdf?modified=20250811232131)

### Employee child-support notices and protected earnings

Use the actual employee deduction notice, its start/amend/stop date, pay frequency and amount. Do not start early. Ask IRD to correct an incorrect payday or frequency rather than silently converting the notice yourself. The employee cannot instruct the employer to start or stop these deductions. The contractor/schedular-payment notice has a different payment and employment-information route; the employee instructions here do not establish that route. [S2, section 5.15](https://www.ird.govt.nz/-/media/project/ir/home/documents/digital-service-providers/software-providers/payroll-calculations-business-rules-specifications/payroll-calculations-and-business-rules-specification.pdf?modified=20260401012317), [S13, PDF page 23](https://www.ird.govt.nz/-/media/project/ir/home/documents/forms-and-guides/ir300---ir399/ir335/ir335.pdf?modified=20250811232131)

For the ordinary employee child-support calculation, let **G** be gross salary/wages, **P** PAYE including the employee ACC earners' levy and **A** that levy component. The protected-earnings calculation uses **N = G − (P − A)**, so its income-tax deduction excludes ACC. The normal maximum child-support deduction is **40% of N**: deduct the lesser of the notice amount and that capacity. The remaining 60% is protected for this purpose, not a guaranteed final take-home amount after student loans, ACC, KiwiSaver and other lawful deductions. Establish special payment bases separately; this formula does not resolve ESS or schedular payments. [S2, section 5.15.1, PDF pages 71-72](https://www.ird.govt.nz/-/media/project/ir/home/documents/digital-service-providers/software-providers/payroll-calculations-business-rules-specifications/payroll-calculations-and-business-rules-specification.pdf?modified=20260401012317), [S13, PDF page 24 worked example](https://www.ird.govt.nz/-/media/project/ir/home/documents/forms-and-guides/ir300---ir399/ir335/ir335.pdf?modified=20250811232131)

Where protected earnings prevent the full deduction, report variation **P** and the amount actually deducted. Do not make up the difference in a later pay; IRD arranges it with the employee. Other variation codes are A for advance payment, D for previously deducted, S for a short unpaid absence preventing any deduction and O for other reasons. If employment has ceased, **C takes priority even when P would otherwise apply**; record the employee finish date as well. Include employee child support in employment information and pay it with the ordinary employer deductions. Protect the employee's child-support information. [S1](https://www.ird.govt.nz/deductions), [S13, PDF pages 24-25](https://www.ird.govt.nz/-/media/project/ir/home/documents/forms-and-guides/ir300---ir399/ir335/ir335.pdf?modified=20250811232131)

### District Court attachment orders

Identify the statute and actual order. **Section 157 of the District Court Act 2016** governs these court attachments; **section 157 of the Tax Administration Act 1994** below is a different notice. The court order specifies the earnings period, deduction amount or percentage and minimum earnings to retain. For an ordinary District Court attachment, the protected floor is the **higher of 60% of statutory net earnings and the actual order's minimum**. Use the PAYE income-tax component for the net-earnings base, with the ACC distinction above. Confirm which payments are salary/wages for the order: the statutory definition is broader than ordinary basic pay. [S27](https://www.legislation.govt.nz/act/public/2016/49/en/latest/sections/DLM6942502/), [S28](https://www.legislation.govt.nz/act/public/2016/49/en/latest/sections/DLM6942500/), [S29](https://www.legislation.govt.nz/act/public/2016/49/en/latest/sections/DLM6942492/), [S2, section 5.15.2](https://www.ird.govt.nz/-/media/project/ir/home/documents/digital-service-providers/software-providers/payroll-calculations-business-rules-specifications/payroll-calculations-and-business-rules-specification.pdf?modified=20260401012317)

Section 157(3) requires the court attachment to be reduced or cancelled as necessary when it alone, or together with the listed other notices/orders, would take earnings below that floor. For a single ordinary court order with established prior deductions, its available capacity is **max(0, N − protected floor − applicable prior deductions)**; deduct the lesser of that capacity and the amount required by the order. Child support has priority. Section 157(2) also makes the ordinary court charge subject to the specified Family Proceedings/Summary Proceedings attachments and statutory deduction notices. Do not invent priority amongst competing orders or reduce a different statutory notice merely by applying this court formula; obtain the actual instruments and resolve their priority with the issuer/court or IRD. [S27](https://www.legislation.govt.nz/act/public/2016/49/en/latest/sections/DLM6942502/), [S13, PDF page 23](https://www.ird.govt.nz/-/media/project/ir/home/documents/forms-and-guides/ir300---ir399/ir335/ir335.pdf?modified=20250811232131)

The specification's page 72 step 5 prints the full other-attachment amount even when it exceeds remaining capacity. That instruction conflicts with section 157(3)'s protection. Apply the statutory reduction instead of copying the printed branch. The worked checks below assume the stated order, base and prior deductions are already valid; they do not determine every competing-notice combination. [S27](https://www.legislation.govt.nz/act/public/2016/49/en/latest/sections/DLM6942502/), [S2, PDF page 72](https://www.ird.govt.nz/-/media/project/ir/home/documents/digital-service-providers/software-providers/payroll-calculations-business-rules-specifications/payroll-calculations-and-business-rules-specification.pdf?modified=20260401012317)

### IRD tax-arrears notices

A Tax Administration Act section 157 notice for salary/wage arrears is separate from a student-loan SLCIR recovery notice. Obtain its required amount, instalment period, initial notified debt, payment deadline, tax reference and any notified interest. For the ordinary statutory salary/wage ceiling, compare **10% per week of the debt due at the notice date** with **20% of gross salary/wages payable**. Take the lesser, then compare it with **$10 per week** and take the greater. For non-weekly pay, scale the weekly debt instalment and minimum to the pay period; the 20% limb already uses that period's actual gross pay. This is a ceiling, not an instruction to deduct it when the actual notice requires less. Limit the deduction to the amount actually payable and required under the notice. [S30, subsections (1)-(3)](https://www.legislation.govt.nz/act/public/1994/166/en/latest/sections/DLM356984/), [S26](https://www.ird.govt.nz/employing-staff/deductions-from-income/deduction-notices-collecting-taxes-from-taxpayers-who-refuse-to-pay), [S32, paragraphs 26-28](https://www.taxtechnical.ird.govt.nz/-/media/project/ir/tt/pdfs/standard-practice-statements/processing/sps-21-01.pdf?modified=20210420044632)

IRD's SPS 21/01 says no extra deduction is required where weekly earnings are **less than $10**. It also addresses an employee request for a higher deduction. Follow the applicable notice and actual request; resolve an apparent conflict with IRD rather than creating a deduction that exceeds the wages available. The specification's page 75 flowchart shortcut of $10 when weekly gross is below $100 does not reproduce the general statutory formula: for example, 20% of $80 is $16. Other fixed-amount notices may be issued. [S32, paragraphs 27-28](https://www.taxtechnical.ird.govt.nz/-/media/project/ir/tt/pdfs/standard-practice-statements/processing/sps-21-01.pdf?modified=20210420044632), [S2, section 5.17](https://www.ird.govt.nz/-/media/project/ir/home/documents/digital-service-providers/software-providers/payroll-calculations-business-rules-specifications/payroll-calculations-and-business-rules-specification.pdf?modified=20260401012317)

Child-support arrears use a different notice and calculation, and child support takes priority over other tax arrears. Check that actual instrument separately; the ordinary employee child-support formula above does not establish all arrears or contractor cases. Do not merge different notices into one generic 40% cap. [S26](https://www.ird.govt.nz/employing-staff/deductions-from-income/deduction-notices-collecting-taxes-from-taxpayers-who-refuse-to-pay), [S32, paragraphs 29-30](https://www.taxtechnical.ird.govt.nz/-/media/project/ir/tt/pdfs/standard-practice-statements/processing/sps-21-01.pdf?modified=20210420044632)

Do not put these tax-arrears deductions in employment information or the SLCIR field. Pay them separately from PAYE using the employee's IRD number, tax type, period and amount. The general payroll instructions say by calendar month-end; the Act and SPS require payment within the time in the actual notice, so establish that deadline before processing. Notify the employee of the deduction and its purpose. The amount withheld is held in trust for the Crown. Keep the notice until the required amount is paid or IRD changes/revokes it in writing; the employee cannot cancel it. [S2, section 5.17](https://www.ird.govt.nz/-/media/project/ir/home/documents/digital-service-providers/software-providers/payroll-calculations-business-rules-specifications/payroll-calculations-and-business-rules-specification.pdf?modified=20260401012317), [S26](https://www.ird.govt.nz/employing-staff/deductions-from-income/deduction-notices-collecting-taxes-from-taxpayers-who-refuse-to-pay), [S30, subsections (1), (4), (6) and (8)](https://www.legislation.govt.nz/act/public/1994/166/en/latest/sections/DLM356984/), [S32, paragraphs 33-36](https://www.taxtechnical.ird.govt.nz/-/media/project/ir/tt/pdfs/standard-practice-statements/processing/sps-21-01.pdf?modified=20210420044632)


### Filing, remitting and records

### Employment information

File employment information for every payday using the actual pay date, not the end of the work period. Electronic filing is due within **2 working days** of payday. Allowed paper filing is due within **10 working days** of each payday, or under the permitted twice-monthly grouping within 10 working days of the 15th and month end. Filing and payment deadlines are separate; file on time even if unable to pay. [S14](https://www.ird.govt.nz/payday)

New employers may file on paper during their first 6 months. After that, electronic filing is required where annual PAYE and ESCT is **$50,000 or more**. Smaller employers can choose electronic filing. Tell Inland Revenue the required new-employee information on or before the first payday; for electronic filing this includes the employee's address and, if supplied, date of birth. Tell Inland Revenue the leaver's end date on or before their last day. Advise Inland Revenue when no wages will be paid for a month or more, including an irregular or stopped payroll. [S14](https://www.ird.govt.nz/payday), [S15](https://www.ird.govt.nz/employing-staff/payday-filing/filing-employment-information-electronically)

### Paying deductions

| Gross annual PAYE and ESCT payment category | Paydays covered | Ordinary payment deadline |
|---|---|---|
| Less than $500,000 | Whole month | 20th of the following month |
| $500,000 or more | 1st to 15th | 20th of the same month |
| $500,000 or more | 16th to month end, except December | 5th of the following month |
| $500,000 or more | 16 to 31 December | **15 January** |

For established employers the large-employer test uses the preceding year's gross PAYE and ESCT. New employers pay monthly until reaching $500,000. Gross PAYE for this test includes ESCT but excludes ACC earners' levy, student loans, KiwiSaver and child support. Check connected-employer aggregation rather than treating each entity as independent. If a payment deadline falls on a weekend or public holiday, the next working day applies. [IR335, pages 71-72](https://www.ird.govt.nz/-/media/project/ir/home/documents/forms-and-guides/ir300---ir399/ir335/ir335.pdf?modified=20250811232131)

The [payment web page](https://www.ird.govt.nz/employing-staff/payday-filing/paying-deductions-to-inland-revenue) says 'more than' $500,000, leaving equality unclear; IR335 explicitly says **$500,000 or more**. Use the latter boundary rather than classifying exactly $500,000 as a small employer. This threshold does not replace the separate $50,000 filing threshold.

Reconcile PAYE, student loans, child support, employee KiwiSaver, net employer KiwiSaver and ESCT separately before making the combined **EMP** payment. Confirm the employer account, period and reference. Other arrears notices can require a separate payment process; do not assume every withheld amount belongs in ordinary employment information or the same payment. Filing an employment-information return does not itself pay the liability. [S12](https://www.ird.govt.nz/employing-staff/deductions-from-income/employer-superannuation-contribution-tax/deduct-esct-from-each-employer-contribution), [S13](https://www.ird.govt.nz/-/media/project/ir/home/documents/forms-and-guides/ir300---ir399/ir335/ir335.pdf?modified=20250811232131), [S16](https://www.ird.govt.nz/employing-staff/payday-filing/paying-deductions-to-inland-revenue)

### Correcting employment information

Identify the employee, actual payday, original filed figures, correct figures and reason for the error before choosing a correction. In myIR, amend the relevant employment-information return; add or remove the employee where needed, then check and submit the amendment declaration. **Do not resubmit the entire original return.** A file accepted with a warning is not proof that employee details or amounts are correct. From 12 September 2026, employee-details (ED) files submitted in myIR show additional warnings, which must be acknowledged before submission but can be acknowledged without first correcting the details; gateway filing is unchanged. Resolve the underlying facts rather than treating acknowledgement as validation. [S51](https://www.ird.govt.nz/employing-staff/payday-filing/filing-employment-information-electronically/amend-an-employment-information-return), [S52](https://www.ird.govt.nz/updates/news-folder/2026/upcoming-employment-information-changes)

The **2019 correction regulations**, consolidated as at 30 March 2026, distinguish these errors. Correct an error as soon as reasonably practicable after becoming aware of it; the notification routes below use regulation 10 and the Commissioner's applicable notification process. [S53](https://www.legislation.govt.nz/secondary-legislation/pco-drafted/2019/62/en/latest/)

| Established error | Selected correction route and limit |
|---|---|
| Payroll overpayment under regulation 4, repaid or repayable under an agreement | Notify Inland Revenue or net the relevant excess gross pay, tax, employer KiwiSaver and ESCT amounts against later employment information. Treat an agreed repayable amount as repaid for this purpose. Commissioner permission is needed if netting would produce a negative reported amount. |
| Agreement used for a correction, then breached without remedy within 2 months, or future compliance no longer expected | Revisit the correction. Regulation 4(5) requires an upwards adjustment for an established unrepaid PAYE income overpayment; amounts outside that definition use notification under 4(6). Do not leave a correction based on an agreement that has failed. |
| Other incorrect PAYE income calculation under regulation 5, or income-tax/ACC calculation under regulation 6 | Notify Inland Revenue, net an excess against a later payday, or carry a shortfall only within the conditions below. Netting that produces a negative reported amount needs Commissioner permission. |
| Independently miscalculated child support, employee/employer KiwiSaver, student loan or ESCT under regulation 7 | Notify Inland Revenue. Do not automatically use the later-payday income-tax/ACC shortfall route. Where the error arose from an incorrect income calculation, first distinguish regulations 4 and 5. |
| Reporting-only error under regulation 8 | Notify Inland Revenue, even if the pay and deduction calculations were correct. |

For the shortfall option in regulations 5(2)(c) and 6(2)(c), there must be a combined income-tax and ACC withholding shortfall **strictly less than 10%** of the employee's combined income-tax and ACC withholding for the later payday. Exclude amounts attributable to earlier paydays and to the correction itself from that comparison base. Equality at 10% does not qualify for this option; use an available notification route instead. The test is not 10% of gross wages, all deductions or the later total after adding the correction. [S53](https://www.legislation.govt.nz/secondary-legislation/pco-drafted/2019/62/en/latest/)

Regulation 4 excludes an agreed and lawful reduction of a later PAYE income payment by the overpayment under 4(8). Benefit/grant and recoverable ACC overpayments have the distinct rule in 4(9)-(10). Establish the facts and the employee's lawful repayment arrangement before applying a method; this guide does not authorise recovery from wages. Regulation 11 excludes errors attributable to the employee's failure to comply with the notified-tax-code rules. Do not treat that exclusion as permission to retain an incorrect code. [S53](https://www.legislation.govt.nz/secondary-legislation/pco-drafted/2019/62/en/latest/)

IRD's operational amendment page describes an ordinary **4-year** window from sending the original return and says older child-support amendments use IR344/contact with Inland Revenue. That is not an exhaustive account of the Commissioner's assessment powers. In the TAA copy dated 1 October 2026, section 108AC includes a student-loan exception where not amending would significantly adversely affect the borrower, as well as fraud/wilful-misleading exceptions; section 108AB deals separately with KiwiSaver increases. Section 108(1C) uses the end of the relevant return-provision period, and section 108B permits prescribed, timely waivers for listed bars. Section 113 is a Commissioner power, not an employer entitlement to make any old amendment. Refer older or exceptional cases for Inland Revenue's decision rather than automatically refusing or processing them. The general small-error thresholds in section 113A do **not** supply a PAYE shortcut: that section excludes ancillary taxes other than FBT. [S51](https://www.ird.govt.nz/employing-staff/payday-filing/filing-employment-information-electronically/amend-an-employment-information-return), [S54](https://www.legislation.govt.nz/act/public/1994/166/en/latest/sections/LMS835657/), [S55](https://www.legislation.govt.nz/act/public/1994/166/en/latest/sections/LMS674865/), [S56](https://www.legislation.govt.nz/act/public/1994/166/en/latest/sections/DLM354691/), [S57](https://www.legislation.govt.nz/act/public/1994/166/en/latest/sections/DLM354915/), [S58](https://www.legislation.govt.nz/act/public/1994/166/en/latest/sections/DLM354948/), [S59](https://www.legislation.govt.nz/act/public/1994/166/en/latest/sections/DLM2669326/)

### Keeping tax records

Keep wagebook information, PAYE payment records, IR330/IR330C declarations, tax-code/rate letters, relevant written agreements and exemption/tailored certificates. IR335 also lists KiwiSaver forms. Keep sufficient supporting records to explain the amounts filed and paid. [S17](https://www.ird.govt.nz/employing-staff/deductions-from-income/paye-records), [IR335, page 7](https://www.ird.govt.nz/-/media/project/ir/home/documents/forms-and-guides/ir300---ir399/ir335/ir335.pdf?modified=20250811232131)

For the business tax records within **TAA section 22**, the ordinary minimum runs for **7 years after the end of the income year** to which they relate. A notice issued before that period expires may extend retention by up to 3 years for an audit, investigation or intended audit/investigation. Keep records in English or te reo Māori unless another language is approved. Keep them in New Zealand unless the taxpayer or an approved provider has the relevant authorisation; offshore cloud storage is not automatically authorised. Check the authorisation's scope and conditions. Other employment, holiday-pay, privacy, KiwiSaver and litigation requirements may use different periods or require longer retention. This is not a deletion instruction or a complete employment-records schedule. [S60](https://www.ird.govt.nz/records), [S61](https://www.legislation.govt.nz/act/public/1994/166/en/latest/sections/DLM350462/)

### Filing penalties

Late employment information and an unpaid deduction are separate defaults. For employment information, the selected rules in **TAA section 139A** and IRD's current guidance provide a warning process after a clean preceding 12 months, then a further late filing within the following 12 months can attract **$250 for the month**, regardless of the number of late payday filings in that month. Check the actual warning, filing history and penalty notice. Do not import the ordinary annual-return 30-day advance warning into payday filing. The EI late-filing penalty is due **30 days after the end of the month in which the information was required**, under section 142(1A). [S62](https://www.ird.govt.nz/managing-my-tax/penalties-and-interest/penalties-and-debt/late-filing-penalties), [S63](https://www.taxtechnical.ird.govt.nz/standard-practice-statements/returns-and-debt-collection/sps-1904-late-filing-penalties), [S64](https://www.legislation.govt.nz/act/public/1994/166/en/latest/sections/DLM356114/), [S65](https://www.legislation.govt.nz/act/public/1994/166/en/latest/sections/DLM356638/)

For non-electronic filing, first establish that electronic delivery was required and that no applicable exemption authorises another method. Section 139AA(4) sets the monthly maximum at the greater of **$250 or $1 per affected employee** whose information was not supplied in the prescribed format/manner during that month. Count the employees affected by that default, not automatically the employer's entire workforce. IR335 and the late-filing web summary abbreviate this as each person employed; the statutory affected-employee wording controls this distinction. Section 142G makes this EI penalty due 30 days after the end of the month in which the information was required. Do not multiply the monthly maximum by the number of offending payday returns. [S62](https://www.ird.govt.nz/managing-my-tax/penalties-and-interest/penalties-and-debt/late-filing-penalties), [S66](https://www.legislation.govt.nz/act/public/1994/166/en/latest/sections/DLM356131/), [S67](https://www.legislation.govt.nz/act/public/1994/166/en/latest/sections/DLM356681/)

SPS19/04 is dated 30 May 2019. Its initial education stage was expressed as transitional while payday filing was new, so this guide does not promise another education-only default in 2026. Its historical statutory appendix is not the current consolidated Act. Check an actual penalty and any available reversal/remission with Inland Revenue. [S63](https://www.taxtechnical.ird.govt.nz/standard-practice-statements/returns-and-debt-collection/sps-1904-late-filing-penalties)

### Late payment and non-payment penalties

For an established ordinary employer PAYE tax debt, **TAA section 139B** provides an initial **1%** charge on the unpaid tax the day after the due date and a further **4%** on the remaining tax-to-pay at the specified seventh-day point. The latter base includes unpaid late-payment penalties. Incremental **1% monthly** charges can then apply on the statutory dates; determine those dates under the section rather than assuming every month has the same number of days. Payments and statutory relief can alter the base or prevent a charge. The section's unpaid-tax definition excludes both late-payment penalties and the section 141ED non-payment penalty, while its tax-to-pay definition adds unpaid late-payment penalties. Do not compound all tax, penalties and interest together. [S68](https://www.legislation.govt.nz/act/public/1994/166/en/latest/sections/DLM356138/), [S69](https://ird.govt.nz/late-payment-penalties)

The section 183F small-debt exemption is **$100 or less**, including exactly $100; IR335's 'less than $100' wording omits that equality. Its late-payment and interest limbs test the amount outstanding after the due date. The section's non-payment-penalty limb instead tests the unpaid amount on the day before the Commissioner's section 141ED(1)(b) notice. Those are different tests and dates. Do not infer a blanket lifetime exemption for an account that once had a $100 balance. [S70](https://www.legislation.govt.nz/act/public/1994/166/en/latest/sections/DLM358771/)

A good payment history is not permission to invent a later due date: the section 139B grace process requires the Commissioner's notice and its conditions. Under **section 139BA**, a qualifying relief request before default leaves the 1% initial charge but can prevent the 4% charge; a request on or after default affects incremental penalties from the request. If relief is refused or the statutory response period expires, penalties may be reinstated retrospectively. An arrangement must be complied with; merely asking for relief does not cancel tax or interest. These selected ordinary PAYE rules do not establish child-support penalties or every EMP component's separate statutory treatment. [S68](https://www.legislation.govt.nz/act/public/1994/166/en/latest/sections/DLM356138/), [S69](https://ird.govt.nz/late-payment-penalties), [S71](https://www.legislation.govt.nz/act/public/1994/166/en/latest/sections/DLM356156/)

**Section 141ED non-payment penalties** require the established statutory debt, filed employment information, non-payment and the Commissioner's warning/notice process. For the ordinary PAYE amount required under section RD 4(1), the first penalty date is the date of the Commissioner's notice itself and subsequent dates are at 1-month intervals under the section. The usual penalty is **10% of the required amount still unpaid on the day before the penalty date**. It is not 10% of the combined tax, late-payment penalties and interest. A variation or correction made from filing through the day before the penalty date changes the required-amount base. [S72](https://www.legislation.govt.nz/act/public/1994/166/en/latest/sections/DLM1191236/)

The rate for that penalty can reduce to **5%** when payment or a qualifying instalment arrangement occurs after the penalty date and before the day that is 1 month after it, subject to the prior-agreement condition. Negotiating an instalment arrangement, a compliant arrangement made before the penalty date and specified receivership/liquidation cases have separate exceptions. The aggregate section 141ED penalty is capped at **150% of the required amount unpaid when the first penalty was imposed**. Payments are applied to the non-payment penalty before the required amount. Check the actual notices, correction, payment allocation, arrangement dates and compliance before calculating; do not automatically apply this RD 4 rule to every student-loan, KiwiSaver, child-support or ESCT balance. Non-resident cross-border exceptions and those separate streams require further checks. [S72](https://www.legislation.govt.nz/act/public/1994/166/en/latest/sections/DLM1191236/)

Use the current Inland Revenue account and applicable interest rules/rates for any actual balance. This guide does not calculate use-of-money interest, collection costs, criminal or other shortfall penalties, or the complete remission regime. Under the selected **section 183A** reasonable-cause rule, Inland Revenue may remit listed penalties where its conditions are met, including correction as soon as practicable after a beyond-control event. Financial position alone is excluded as a reasonable-cause ground, and an agent's omission is not automatically an excuse. An application is not a favourable decision. Keep the decision and its conditions. [S73](https://www.legislation.govt.nz/act/public/1994/166/en/latest/sections/DLM358729/)


## Worked cases

These fictional cases assume the stated code, eligibility, contribution base and notices have already been established. They check the arithmetic of the selected rules, not an actual person's liability. Tolerance is zero, so a cent error fails.

Before release also check an exactly $50,000 electronic-filing case, an exactly $500,000 large-employer case, the December 15 January exception and a pay period straddling 1 April. A temporary 3% employee rate does not by itself force the employer to reduce its rate.

**Case 1: primary SLCIR and separate voluntary repayment.** Assume weekly M SL pay of $875.90, a valid 5% SLCIR notice with sufficient balance and a $20 SLBOR request. Whole-dollar gross is $875; ordinary SL is $49.32, SLCIR $20.55 and SLBOR $20, totalling $89.87. [S2, section 3](https://www.ird.govt.nz/-/media/project/ir/home/documents/digital-service-providers/software-providers/payroll-calculations-business-rules-specifications/payroll-calculations-and-business-rules-specification.pdf?modified=20260401012317)

```oa-check
name: nz-2026-slcir-primary-separate
tolerance: 0
inputs:
  gross: 875.9
  threshold: 464
  ordinary_rate: 0.12
  recovery_rate: 0.05
  voluntary: 20
steps:
  whole: floor(gross)
  base: max(0, whole - threshold)
  ordinary: floor(base * ordinary_rate * 100) / 100
  recovery: floor(base * recovery_rate * 100) / 100
  total: ordinary + recovery + voluntary
expected:
  whole: 875
  ordinary: 49.32
  recovery: 20.55
  total: 89.87
```

**Case 2: primary recovery below the threshold.** Weekly M SL pay of $425.35 is below $464. Assume no different certificate: ordinary SL and SLCIR are zero. [S2, section 3](https://www.ird.govt.nz/-/media/project/ir/home/documents/digital-service-providers/software-providers/payroll-calculations-business-rules-specifications/payroll-calculations-and-business-rules-specification.pdf?modified=20260401012317)

```oa-check
name: nz-2026-slcir-below-threshold
tolerance: 0
inputs:
  gross: 425.35
  threshold: 464
steps:
  base: max(0, floor(gross) - threshold)
  ordinary: floor(base * 0.12 * 100) / 100
  recovery: floor(base * 0.05 * 100) / 100
expected:
  base: 0
  ordinary: 0
  recovery: 0
```

**Case 3: secondary recovery has no ordinary threshold.** Assume $300.99 secondary SL pay and a valid 5% recovery notice with sufficient balance. On $300 whole-dollar gross, ordinary SL is $36 and SLCIR $15. [S2, section 3](https://www.ird.govt.nz/-/media/project/ir/home/documents/digital-service-providers/software-providers/payroll-calculations-business-rules-specifications/payroll-calculations-and-business-rules-specification.pdf?modified=20260401012317)

```oa-check
name: nz-2026-slcir-secondary
tolerance: 0
inputs:
  gross: 300.99
steps:
  whole: floor(gross)
  ordinary: floor(whole * 0.12 * 100) / 100
  recovery: floor(whole * 0.05 * 100) / 100
  total: ordinary + recovery
expected:
  ordinary: 36
  recovery: 15
  total: 51
```

**Case 4: use the actual recovery percentage.** Assume weekly M SL pay of $900 and a valid notice requiring 3% above $464. Ordinary SL is $52.32 and recovery $13.08, not an assumed 5% deduction. [S2, section 3](https://www.ird.govt.nz/-/media/project/ir/home/documents/digital-service-providers/software-providers/payroll-calculations-business-rules-specifications/payroll-calculations-and-business-rules-specification.pdf?modified=20260401012317)

```oa-check
name: nz-2026-slcir-actual-rate
tolerance: 0
inputs:
  gross: 900
  threshold: 464
  notice_rate: 0.03
steps:
  base: max(0, floor(gross) - threshold)
  ordinary: floor(base * 0.12 * 100) / 100
  recovery: floor(base * notice_rate * 100) / 100
  total: ordinary + recovery
expected:
  ordinary: 52.32
  recovery: 13.08
  total: 65.4
```

**Case 5: stop at the required recovery balance.** Assume the first case has only $7 left to recover under the notice. Deduct $7 SLCIR and reconcile the completed recovery amount; do not take $20.55. [S2, section 3](https://www.ird.govt.nz/-/media/project/ir/home/documents/digital-service-providers/software-providers/payroll-calculations-business-rules-specifications/payroll-calculations-and-business-rules-specification.pdf?modified=20260401012317)

```oa-check
name: nz-2026-slcir-final-balance
tolerance: 0
inputs:
  gross: 875.9
  threshold: 464
  remaining: 7
steps:
  calculated: floor(max(0, floor(gross) - threshold) * 0.05 * 100) / 100
  recovery: min(calculated, remaining)
  balance: remaining - recovery
expected:
  calculated: 20.55
  recovery: 7
  balance: 0
```

**Case 6: child support protects the tax-only net base.** Assume ordinary weekly pay $600, PAYE including ACC $94.50, its ACC component $10.50, a $230 employee child-support notice, ordinary SL $16.32 and an eligible 3.5% KiwiSaver deduction. N is $516 and child support is $206.40. Take-home after those stated deductions is $261.78; the 60% child-support protection is not a final take-home guarantee. [S13, PDF page 24](https://www.ird.govt.nz/-/media/project/ir/home/documents/forms-and-guides/ir300---ir399/ir335/ir335.pdf?modified=20250811232131), [S8](https://www.ird.govt.nz/kiwisaver/kiwisaver-for-employers/contributions-and-deductions/kiwisaver-deductions-from-employee-pay)

```oa-check
name: nz-2026-child-support-tax-only-base
tolerance: 0
inputs:
  gross: 600
  paye: 94.5
  acc: 10.5
  notice: 230
  student: 16.32
  kiwi_rate: 0.035
steps:
  income_tax: paye - acc
  net_base: gross - income_tax
  capacity: net_base * 0.40
  support: min(notice, capacity)
  kiwi: gross * kiwi_rate
  takehome: gross - paye - support - student - kiwi
expected:
  net_base: 516
  support: 206.4
  kiwi: 21
  takehome: 261.78
```

**Case 7: reduce the ordinary court attachment.** Assume N=$516, prior valid child support $120 and a single ordinary court order requesting $100 with no higher minimum. The remaining court capacity is $86.40, so the court deduction must be reduced. [S27](https://www.legislation.govt.nz/act/public/2016/49/en/latest/sections/DLM6942502/)

```oa-check
name: nz-2026-court-residual-capacity
tolerance: 0
inputs:
  net_base: 516
  child_support: 120
  requested: 100
  notice_floor: 0
steps:
  floor: max(net_base * 0.60, notice_floor)
  capacity: max(0, net_base - floor - child_support)
  court: min(requested, capacity)
expected:
  floor: 309.6
  capacity: 86.4
  court: 86.4
```

**Case 8: the order can specify a higher protected minimum.** Assume N=$500, an actual court minimum of $400, prior valid child support $80 and an ordinary court request of $100. Court capacity is $20. [S27](https://www.legislation.govt.nz/act/public/2016/49/en/latest/sections/DLM6942502/), [S28](https://www.legislation.govt.nz/act/public/2016/49/en/latest/sections/DLM6942500/)

```oa-check
name: nz-2026-court-higher-minimum
tolerance: 0
inputs:
  net_base: 500
  notice_floor: 400
  child_support: 80
  requested: 100
steps:
  floor: max(net_base * 0.60, notice_floor)
  capacity: max(0, net_base - floor - child_support)
  court: min(requested, capacity)
expected:
  floor: 400
  capacity: 20
  court: 20
```

**Case 9: court capacity cannot be negative.** Assume N=$300 and a court-order minimum of $350. The ordinary court request of $100 reduces to zero, rather than producing a negative deduction. [S27](https://www.legislation.govt.nz/act/public/2016/49/en/latest/sections/DLM6942502/)

```oa-check
name: nz-2026-court-zero-capacity
tolerance: 0
inputs:
  net_base: 300
  notice_floor: 350
  requested: 100
steps:
  floor: max(net_base * 0.60, notice_floor)
  capacity: max(0, net_base - floor)
  court: min(requested, capacity)
expected:
  floor: 350
  capacity: 0
  court: 0
```

**Case 10: ordinary weekly arrears ceiling.** Assume a valid income-tax arrears notice with initial debt $3,000 requires the standard salary/wage formula, with sufficient balance. On weekly gross $900, the ceiling and required deduction are $180. This does not select the amount for a different actual notice. [S30](https://www.legislation.govt.nz/act/public/1994/166/en/latest/sections/DLM356984/), [S32, paragraph 28](https://www.taxtechnical.ird.govt.nz/-/media/project/ir/tt/pdfs/standard-practice-statements/processing/sps-21-01.pdf?modified=20210420044632)

```oa-check
name: nz-2026-arrears-weekly-ceiling
tolerance: 0
inputs:
  initial_debt: 3000
  gross: 900
steps:
  debt_limb: initial_debt * 0.10
  wage_limb: gross * 0.20
  ceiling: max(10, min(debt_limb, wage_limb))
expected:
  debt_limb: 300
  wage_limb: 180
  ceiling: 180
```

**Case 11: low pay does not automatically mean a $10 deduction.** Under the same assumed standard notice and sufficient balance, weekly gross $80 gives a $16 ceiling and deduction. Do not copy the specification flowchart shortcut. [S30](https://www.legislation.govt.nz/act/public/1994/166/en/latest/sections/DLM356984/), [S32, paragraphs 26-27](https://www.taxtechnical.ird.govt.nz/-/media/project/ir/tt/pdfs/standard-practice-statements/processing/sps-21-01.pdf?modified=20210420044632)

```oa-check
name: nz-2026-arrears-low-pay-sixteen
tolerance: 0
inputs:
  initial_debt: 3000
  gross: 80
steps:
  ceiling: max(10, min(initial_debt * 0.10, gross * 0.20))
expected:
  ceiling: 16
```

**Case 12: the weekly minimum limb.** Assume the standard notice, sufficient balance and weekly gross $30. The lesser percentage limb is $6, so the weekly minimum limb gives $10. [S30](https://www.legislation.govt.nz/act/public/1994/166/en/latest/sections/DLM356984/), [S32, paragraph 27.2](https://www.taxtechnical.ird.govt.nz/-/media/project/ir/tt/pdfs/standard-practice-statements/processing/sps-21-01.pdf?modified=20210420044632)

```oa-check
name: nz-2026-arrears-weekly-minimum
tolerance: 0
inputs:
  initial_debt: 3000
  gross: 30
steps:
  lesser: min(initial_debt * 0.10, gross * 0.20)
  ceiling: max(10, lesser)
expected:
  lesser: 6
  ceiling: 10
```

**Case 13: reconcile the remaining amount required.** Assume weekly gross $900 and a fixed arrears instalment of $40, but only $5 remains required under the actual notice and no further notified interest is due. The deduction is $5, not a fresh $40 or $180 ceiling. [S30, subsection (1)](https://www.legislation.govt.nz/act/public/1994/166/en/latest/sections/DLM356984/)

```oa-check
name: nz-2026-arrears-final-amount
tolerance: 0
inputs:
  gross: 900
  initial_debt: 3000
  notice: 40
  remaining_required: 5
steps:
  ceiling: max(10, min(initial_debt * 0.10, gross * 0.20))
  deduction: min(notice, ceiling, remaining_required, gross)
expected:
  ceiling: 180
  deduction: 5
```

**Case 14: a ceiling does not replace a lower notice amount.** Assume weekly gross $900, initial debt $3,000 and a valid fixed notice requiring $40, with sufficient balance. The standard ceiling is $180; the actual required deduction remains $40. [S30, subsections (1)-(3)](https://www.legislation.govt.nz/act/public/1994/166/en/latest/sections/DLM356984/)

```oa-check
name: nz-2026-arrears-actual-notice
tolerance: 0
inputs:
  initial_debt: 3000
  gross: 900
  notice: 40
steps:
  ceiling: max(10, min(initial_debt * 0.10, gross * 0.20))
  deduction: min(notice, ceiling)
expected:
  ceiling: 180
  deduction: 40
```

**Case 15: scale weekly limbs once for fortnightly pay.** Assume fortnightly gross $1,800, initial debt $3,000 and the standard notice with sufficient balance. Scale the weekly debt limb and $10 minimum by 2; the 20% limb already applies to fortnightly gross. The ceiling is $360. [S32, paragraph 27.1](https://www.taxtechnical.ird.govt.nz/-/media/project/ir/tt/pdfs/standard-practice-statements/processing/sps-21-01.pdf?modified=20210420044632), [S30](https://www.legislation.govt.nz/act/public/1994/166/en/latest/sections/DLM356984/)

```oa-check
name: nz-2026-arrears-fortnightly
tolerance: 0
inputs:
  initial_debt: 3000
  gross: 1800
  weeks: 2
steps:
  debt_limb: initial_debt * 0.10 * weeks
  wage_limb: gross * 0.20
  minimum: 10 * weeks
  ceiling: max(minimum, min(debt_limb, wage_limb))
expected:
  debt_limb: 600
  wage_limb: 360
  minimum: 20
  ceiling: 360
```

**Case 16: repaid overpayment netted without negative figures.** Assume regulation 4 applies, repayment is established and each excess amount is supported. Later ordinary gross pay is $1,000 and its correctly calculated PAYE is $180; net the $300 excess gross and $90 excess PAYE from the earlier overpayment. This is an employment-information adjustment, not a new tax-rate calculation or authority to recover wages. [S53](https://www.legislation.govt.nz/secondary-legislation/pco-drafted/2019/62/en/latest/)

```oa-check
name: nz-2026-repaid-overpayment-netting
tolerance: 0
inputs:
  later_gross: 1000
  later_paye: 180
  excess_gross: 300
  excess_paye: 90
steps:
  reported_gross: later_gross - excess_gross
  reported_paye: later_paye - excess_paye
expected:
  reported_gross: 700
  reported_paye: 90
```

**Case 17: shortfall below the strict carry-forward limit.** Assume regulation 6 applies and the combined later income-tax/ACC withholding, excluding earlier amounts and the correction, is $100. A $9 shortfall is below the $10 limit, leaving a $1 margin. Only on those established facts is the later-payday option available. [S53](https://www.legislation.govt.nz/secondary-legislation/pco-drafted/2019/62/en/latest/)

```oa-check
name: nz-2026-correction-below-ten-percent
tolerance: 0
inputs:
  later_withholding: 100
  shortfall: 9
steps:
  limit: later_withholding * 0.10
  margin: limit - shortfall
  reported_withholding: later_withholding + shortfall
expected:
  limit: 10
  margin: 1
  reported_withholding: 109
```

**Case 18: equality fails the shortfall option.** On the same established $100 comparison base, a $10 shortfall reaches the limit. The zero margin means it is not strictly below 10%; use the available notification route, rather than treating equality as permission to carry forward. [S53](https://www.legislation.govt.nz/secondary-legislation/pco-drafted/2019/62/en/latest/)

```oa-check
name: nz-2026-correction-at-ten-percent
tolerance: 0
inputs:
  later_withholding: 100
  shortfall: 10
steps:
  limit: later_withholding * 0.10
  margin: limit - shortfall
expected:
  limit: 10
  margin: 0
```

**Case 19: affected employees below the filing minimum.** Assume electronic filing was required, no exemption applies and the monthly penalty is properly imposed. Of 500 employees, only 200 have employment information supplied in the wrong format. Section 139AA uses those 200 affected employees, subject to the $250 monthly maximum calculation floor, not $500 for all staff. [S66](https://www.legislation.govt.nz/act/public/1994/166/en/latest/sections/DLM356131/)

```oa-check
name: nz-2026-non-electronic-affected-below
tolerance: 0
inputs:
  affected_employees: 200
  per_employee: 1
  minimum: 250
steps:
  employee_amount: affected_employees * per_employee
  monthly_maximum: max(minimum, employee_amount)
expected:
  employee_amount: 200
  monthly_maximum: 250
```

**Case 20: affected employees above the filing minimum.** On the same established liability conditions, 300 affected employees produce a $300 monthly maximum. Additional offending payday returns do not each create another monthly maximum. [S66](https://www.legislation.govt.nz/act/public/1994/166/en/latest/sections/DLM356131/)

```oa-check
name: nz-2026-non-electronic-affected-above
tolerance: 0
inputs:
  affected_employees: 300
  per_employee: 1
  minimum: 250
steps:
  employee_amount: affected_employees * per_employee
  monthly_maximum: max(minimum, employee_amount)
expected:
  employee_amount: 300
  monthly_maximum: 300
```

**Case 21: sequential late-payment bases.** Assume $10,000 ordinary PAYE tax remains wholly unpaid at each relevant date, no exemption/grace/relief applies and a statutory monthly charge date has been established. Calculate the initial 1%, the further 4% including the unpaid initial charge and then a 1% incremental charge. Exclude interest and non-payment penalties from these balances. This example does not compute calendar dates. [S68](https://www.legislation.govt.nz/act/public/1994/166/en/latest/sections/DLM356138/)

```oa-check
name: nz-2026-late-payment-sequential-bases
tolerance: 0
inputs:
  unpaid_tax: 10000
steps:
  first_penalty: unpaid_tax * 0.01
  seventh_day_base: unpaid_tax + first_penalty
  second_penalty: seventh_day_base * 0.04
  monthly_base: seventh_day_base + second_penalty
  monthly_penalty: monthly_base * 0.01
  balance: monthly_base + monthly_penalty
expected:
  first_penalty: 100
  seventh_day_base: 10100
  second_penalty: 404
  monthly_base: 10504
  monthly_penalty: 105.04
  balance: 10609.04
```

**Case 22: qualifying relief requested before default.** Assume an eligible pre-default section 139BA request, relief granted and its conditions maintained. For $10,000 unpaid tax, the initial 1% remains; the further 4% is not added in these circumstances. This does not waive interest or model refusal and retrospective reinstatement. [S71](https://www.legislation.govt.nz/act/public/1994/166/en/latest/sections/DLM356156/)

```oa-check
name: nz-2026-pre-default-relief-initial
tolerance: 0
inputs:
  unpaid_tax: 10000
steps:
  initial_penalty: unpaid_tax * 0.01
  tax_and_initial: unpaid_tax + initial_penalty
expected:
  initial_penalty: 100
  tax_and_initial: 10100
```

**Case 23: non-payment uses unpaid required tax.** Assume section 141ED applies after the actual warning/notice process and $10,000 is the unpaid required amount on the day before the penalty date. Separate $504 late-payment penalties do not increase this 10% base. The resulting non-payment penalty is $1,000. [S72](https://www.legislation.govt.nz/act/public/1994/166/en/latest/sections/DLM1191236/)

```oa-check
name: nz-2026-non-payment-separate-base
tolerance: 0
inputs:
  unpaid_required: 10000
  late_payment_penalties: 504
steps:
  non_payment_penalty: unpaid_required * 0.10
  combined_excluding_interest: unpaid_required + late_payment_penalties + non_payment_penalty
expected:
  non_payment_penalty: 1000
  combined_excluding_interest: 11504
```

**Case 24: timely settlement reduces that penalty.** Assume the section 141ED conditions for a reduction are satisfied, including settlement or a qualifying arrangement after the penalty date and before the day 1 month after it, with no disqualifying prior agreement. The $1,000 penalty on the same $10,000 required-amount base reduces to $500; the difference is not a reduction of tax or other charges. [S72](https://www.legislation.govt.nz/act/public/1994/166/en/latest/sections/DLM1191236/)

```oa-check
name: nz-2026-non-payment-five-percent
tolerance: 0
inputs:
  original_base: 10000
steps:
  original_penalty: original_base * 0.10
  reduced_penalty: original_base * 0.05
  reduction: original_penalty - reduced_penalty
expected:
  original_penalty: 1000
  reduced_penalty: 500
  reduction: 500
```

**Case 25: aggregate non-payment cap limits the next charge.** Assume the first-penalty unpaid required amount was $10,000 and unreduced prior section 141ED penalties total $14,900. The 150% cap leaves only $100 for a proposed $1,000 next charge. Check any real correction, reduction or allocation before using this cap history. [S72](https://www.legislation.govt.nz/act/public/1994/166/en/latest/sections/DLM1191236/)

```oa-check
name: nz-2026-non-payment-aggregate-cap
tolerance: 0
inputs:
  first_unpaid: 10000
  prior_penalties: 14900
  proposed_penalty: 1000
steps:
  cap: first_unpaid * 1.50
  remaining: max(0, cap - prior_penalties)
  next_penalty: min(proposed_penalty, remaining)
  total_penalties: prior_penalties + next_penalty
expected:
  cap: 15000
  remaining: 100
  next_penalty: 100
  total_penalties: 15000
```

**Case 26: payment pays the non-payment penalty first.** Assume $1,000 non-payment penalty and $10,000 required tax, with no competing allocations, other charges or rate reduction. Apply a $1,200 payment to the penalty first under section 141ED(5C); only $200 reduces the required tax. This isolated allocation example does not decide a live mixed-debt account. [S72](https://www.legislation.govt.nz/act/public/1994/166/en/latest/sections/DLM1191236/)

```oa-check
name: nz-2026-non-payment-allocation
tolerance: 0
inputs:
  penalty_due: 1000
  tax_due: 10000
  payment: 1200
steps:
  paid_to_penalty: min(payment, penalty_due)
  paid_to_tax: min(tax_due, max(0, payment - paid_to_penalty))
  remaining_tax: tax_due - paid_to_tax
expected:
  paid_to_penalty: 1000
  paid_to_tax: 200
  remaining_tax: 9800
```

**Case 27: correction before the penalty date changes the base.** Assume an accepted correction before the section 141ED penalty date reduces the required amount from $10,000 by $2,000 and nothing has been paid. The applicable ordinary 10% penalty uses the corrected $8,000 base, not the original filing. Actual notice, timing, correction and any exemption remain required inputs. [S72](https://www.legislation.govt.nz/act/public/1994/166/en/latest/sections/DLM1191236/)

```oa-check
name: nz-2026-non-payment-corrected-base
tolerance: 0
inputs:
  original_required: 10000
  accepted_reduction: 2000
steps:
  corrected_required: original_required - accepted_reduction
  penalty: corrected_required * 0.10
expected:
  corrected_required: 8000
  penalty: 800
```

## When to refuse or refer

Refer: unresolved competing notices or attachments, older or exceptional corrections, mixed employer debt, current interest, shortfall or criminal penalties, and remission or collection. An unknown classification, contribution base or notice is an input gap. Do not invent a resident tax code, a pension exemption or a flat PAYE percentage. Ordinary salary rules do not establish the treatment of contractors, non-residents, offshore employers, IR56 workers, benefits or paid parental leave. The selected extra-pay methods below require an established payment classification; they do not determine employment-law entitlements.


## Sources

| Source | URL | Read on | What was read |
| --- | --- | --- | --- |
| Registering as an employer | https://www.ird.govt.nz/setting-up-a-business-or-organisation | 2026-11-13 | Read for Ask the client first (read by Ryan Duguid) |
| 2026-27 payroll specification, selected sections | https://www.ird.govt.nz/-/media/project/ir/home/documents/digital-service-providers/software-providers/payroll-calculations-business-rules-specifications/payroll-calculations-and-business-rules-specification.pdf?modified=20260401012317 | 2026-11-14 | Read for Student-loan recovery and voluntary extra deductions, Employee child-support notices and protected earnings, District Court attachment orders, IRD tax-arrears notices; reopened on 2026-11-14 for the annual PAYE formula, earners' levy, student-loan threshold, NSW rate and ESCT table (2026-27 specification dated 24 March 2026, version 1.0) |
| Student-loan underpayments, updated 3 April 2024; dated specification supplies 2026-27 period | https://www.ird.govt.nz/student-loans/living-in-new-zealand-with-a-student-loan/repaying-my-student-loan-when-i-earn-salary-or-wages/student-loan-underpayments | 2026-11-13 | Read for Student-loan recovery and voluntary extra deductions (read by Ryan Duguid) |
| IR335 employer guide, September 2026, selected pages | https://www.ird.govt.nz/-/media/project/ir/home/documents/forms-and-guides/ir300---ir399/ir335/ir335.pdf?modified=20250811232131 | 2026-11-13 | Read for Student-loan recovery and voluntary extra deductions, Employee child-support notices and protected earnings, District Court attachment orders, Paying deductions (read by Ryan Duguid) |
| Salary and wage deductions | https://www.ird.govt.nz/deductions | 2026-11-13 | Read for Employee child-support notices and protected earnings (read by Ryan Duguid) |
| District Court Act 2016, section 157, as at 17 February 2026 | https://www.legislation.govt.nz/act/public/2016/49/en/latest/sections/DLM6942502/ | 2026-11-13 | Read for District Court attachment orders, Worked cases (read by Ryan Duguid) |
| District Court Act 2016, section 156, as at 17 February 2026 | https://www.legislation.govt.nz/act/public/2016/49/en/latest/sections/DLM6942500/ | 2026-11-13 | Read for District Court attachment orders, Worked cases (read by Ryan Duguid) |
| District Court Act 2016, section 154, as at 17 February 2026 | https://www.legislation.govt.nz/act/public/2016/49/en/latest/sections/DLM6942492/ | 2026-11-13 | Read for District Court attachment orders (read by Ryan Duguid) |
| Tax Administration Act 1994, section 157, as at 1 October 2026 | https://www.legislation.govt.nz/act/public/1994/166/en/latest/sections/DLM356984/ | 2026-11-13 | Read for IRD tax-arrears notices, Worked cases (read by Ryan Duguid) |
| IRD deduction notices, updated 16 April 2026 | https://www.ird.govt.nz/employing-staff/deductions-from-income/deduction-notices-collecting-taxes-from-taxpayers-who-refuse-to-pay | 2026-11-13 | Read for IRD tax-arrears notices (read by Ryan Duguid) |
| SPS 21/01 Deduction notices, paragraphs 26-36, 12 April 2021 | https://www.taxtechnical.ird.govt.nz/-/media/project/ir/tt/pdfs/standard-practice-statements/processing/sps-21-01.pdf?modified=20210420044632 | 2026-11-13 | Read for IRD tax-arrears notices, Worked cases (read by Ryan Duguid) |
| Payday filing | https://www.ird.govt.nz/payday | 2026-11-13 | Read for Employment information (read by Ryan Duguid) |
| Electronic employment information | https://www.ird.govt.nz/employing-staff/payday-filing/filing-employment-information-electronically | 2026-11-14 | Read for Employment information; reopened on 2026-11-14 for the $50,000 electronic filing threshold |
| Paying deductions | https://www.ird.govt.nz/employing-staff/payday-filing/paying-deductions-to-inland-revenue | 2026-11-14 | Read for Paying deductions; reopened on 2026-11-14 for the payment due dates and the $500,000 threshold |
| Deducting ESCT | https://www.ird.govt.nz/employing-staff/deductions-from-income/employer-superannuation-contribution-tax/deduct-esct-from-each-employer-contribution | 2026-11-13 | Read for Paying deductions (read by Ryan Duguid) |
| Amend employment information, updated 12 August 2025 | https://www.ird.govt.nz/employing-staff/payday-filing/filing-employment-information-electronically/amend-an-employment-information-return | 2026-11-13 | Read for Correcting employment information (read by Ryan Duguid) |
| Employment-information changes from 12 September 2026 | https://www.ird.govt.nz/updates/news-folder/2026/upcoming-employment-information-changes | 2026-11-13 | Read for Correcting employment information (read by Ryan Duguid) |
| Correction of Errors in Employment Income Information Regulations 2019, current copy 30 March 2026 | https://www.legislation.govt.nz/secondary-legislation/pco-drafted/2019/62/en/latest/ | 2026-11-13 | Read for Correcting employment information, Worked cases (read by Ryan Duguid) |
| Tax Administration Act section 108AC, copy 1 October 2026 | https://www.legislation.govt.nz/act/public/1994/166/en/latest/sections/LMS835657/ | 2026-11-13 | Read for Correcting employment information (read by Ryan Duguid) |
| Tax Administration Act section 108AB, copy 1 October 2026 | https://www.legislation.govt.nz/act/public/1994/166/en/latest/sections/LMS674865/ | 2026-11-13 | Read for Correcting employment information (read by Ryan Duguid) |
| Tax Administration Act section 108, copy 1 October 2026 | https://www.legislation.govt.nz/act/public/1994/166/en/latest/sections/DLM354691/ | 2026-11-13 | Read for Correcting employment information (read by Ryan Duguid) |
| Tax Administration Act section 108B, copy 1 October 2026 | https://www.legislation.govt.nz/act/public/1994/166/en/latest/sections/DLM354915/ | 2026-11-13 | Read for Correcting employment information (read by Ryan Duguid) |
| Tax Administration Act section 113, copy 1 October 2026 | https://www.legislation.govt.nz/act/public/1994/166/en/latest/sections/DLM354948/ | 2026-11-13 | Read for Correcting employment information (read by Ryan Duguid) |
| Tax Administration Act section 113A, copy 1 October 2026 | https://www.legislation.govt.nz/act/public/1994/166/en/latest/sections/DLM2669326/ | 2026-11-13 | Read for Correcting employment information (read by Ryan Duguid) |
| PAYE records | https://www.ird.govt.nz/employing-staff/deductions-from-income/paye-records | 2026-11-13 | Read for Keeping tax records (read by Ryan Duguid) |
| Keeping records, updated 14 May 2026 | https://www.ird.govt.nz/records | 2026-11-13 | Read for Keeping tax records (read by Ryan Duguid) |
| Tax Administration Act section 22, copy 1 October 2026 | https://www.legislation.govt.nz/act/public/1994/166/en/latest/sections/DLM350462/ | 2026-11-13 | Read for Keeping tax records (read by Ryan Duguid) |
| Late filing penalties, updated 17 November 2025 | https://www.ird.govt.nz/managing-my-tax/penalties-and-interest/penalties-and-debt/late-filing-penalties | 2026-11-13 | Read for Filing penalties (read by Ryan Duguid) |
| SPS19/04 Late filing penalties, 30 May 2019 | https://www.taxtechnical.ird.govt.nz/standard-practice-statements/returns-and-debt-collection/sps-1904-late-filing-penalties | 2026-11-13 | Read for Filing penalties (read by Ryan Duguid) |
| Tax Administration Act section 139A, copy 1 October 2026 | https://www.legislation.govt.nz/act/public/1994/166/en/latest/sections/DLM356114/ | 2026-11-13 | Read for Filing penalties (read by Ryan Duguid) |
| Tax Administration Act section 142, copy 1 October 2026 | https://www.legislation.govt.nz/act/public/1994/166/en/latest/sections/DLM356638/ | 2026-11-13 | Read for Filing penalties (read by Ryan Duguid) |
| Tax Administration Act section 139AA, copy 1 October 2026 | https://www.legislation.govt.nz/act/public/1994/166/en/latest/sections/DLM356131/ | 2026-11-13 | Read for Filing penalties, Worked cases (read by Ryan Duguid) |
| Tax Administration Act section 142G, copy 1 October 2026 | https://www.legislation.govt.nz/act/public/1994/166/en/latest/sections/DLM356681/ | 2026-11-13 | Read for Filing penalties (read by Ryan Duguid) |
| Tax Administration Act section 139B, copy 1 October 2026 | https://www.legislation.govt.nz/act/public/1994/166/en/latest/sections/DLM356138/ | 2026-11-13 | Read for Late payment and non-payment penalties, Worked cases (read by Ryan Duguid) |
| Late payment penalties, updated 5 September 2024 | https://ird.govt.nz/late-payment-penalties | 2026-11-13 | Read for Late payment and non-payment penalties (read by Ryan Duguid) |
| Tax Administration Act section 183F, copy 1 October 2026 | https://www.legislation.govt.nz/act/public/1994/166/en/latest/sections/DLM358771/ | 2026-11-13 | Read for Late payment and non-payment penalties (read by Ryan Duguid) |
| Tax Administration Act section 139BA, copy 1 October 2026 | https://www.legislation.govt.nz/act/public/1994/166/en/latest/sections/DLM356156/ | 2026-11-13 | Read for Late payment and non-payment penalties, Worked cases (read by Ryan Duguid) |
| Tax Administration Act section 141ED, copy 1 October 2026 | https://www.legislation.govt.nz/act/public/1994/166/en/latest/sections/DLM1191236/ | 2026-11-13 | Read for Late payment and non-payment penalties, Worked cases (read by Ryan Duguid) |
| Tax Administration Act section 183A, copy 1 October 2026 | https://www.legislation.govt.nz/act/public/1994/166/en/latest/sections/DLM358729/ | 2026-11-13 | Read for Late payment and non-payment penalties (read by Ryan Duguid) |
| Employee KiwiSaver deductions | https://www.ird.govt.nz/kiwisaver/kiwisaver-for-employers/contributions-and-deductions/kiwisaver-deductions-from-employee-pay | 2026-11-13 | Read for Worked cases (read by Ryan Duguid) |

Not yet confirmed: the rows below were read by Ryan Duguid on 12 and 13 November 2026, and only the spot-checked figures listed in the PR were reopened on 14 November 2026. Inherited sources checked 12 November 2026; selected ESS sources checked 13 November 2026. Selected District Court Act sections use the current copy dated 17 February 2026; Tax Administration Act section 157 uses the current copy dated 1 October 2026. SPS 21/01 is dated 12 April 2021 and remains linked by IRD's arrears page updated 16 April 2026. Extra-pay and deduction examples are recalculated from the stated rules; known inconsistent printed examples and boundary wording are recorded in the verification log. The technical specification is dated 24 March 2026, version 1.0, and expressly covers 1 April 2026 to 31 March 2027. IR335's cover says September 2026. KS4's cover says April 2026. Selected KiwiSaver Act provisions use the current copy dated 1 April 2026. The verification log records the selected native/image page scope, the surviving legacy default and conflicting sample-letter/example wording. The selected correction regulations use the 30 March 2026 consolidation. Selected TAA record, assessment and penalty provisions use the 1 October 2026 copy. Its full-Act page flags unincorporated amendments; the selected amendment-impact check is recorded in the verification log. SPS19/04 is dated 30 May 2019. Current statutory wording controls the affected-employee penalty base and inclusive $100 exemption. These checks do not claim full PDF or statute review. Employer ACC Work and Working Safer levy invoices are not calculated.
