---
name: nz-employer-payroll
description: >
  Use this guide for ordinary New Zealand employer payroll paid from 1 April
  2026 to 31 March 2027. Covers ordinary and selected extra-pay PAYE and
  student-loan calculations, tailored certificates, recovery notices, child support
  and selected court-attachment calculations,
  the ACC earners' levy, selected KiwiSaver enrolment, base, notice and refund administration, employer contributions, ESCT,
  selected employee share schemes, payday filing, selected correction/penalty rules, payment schedules and tax records. Trigger on NZ payroll,
  PAYE, payday filing, KiwiSaver employer contributions, ESCT and employer
  deductions. Distinguishes the electronic filing threshold from the large
  employer payment threshold. Requires actual pay dates, employee declarations
  and notices. Unresolved special payments, cross-border employment, leave entitlements
  and employer ACC invoice calculations require separate checks.
jurisdiction: NZ
category: payroll
tax_year: 2026
tax_year_notes: "Payroll paid 1 April 2026 to 31 March 2027; selected ordinary special-code, ESS, filing and payment rules checked 13 November 2026"
tier: 2
last_updated: 2026-11-13
version: 1.1
verified_by: pending
review_status: pending_review
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# New Zealand employer payroll v1.1

> **General reference only.** This is a source-cited draft awaiting qualified review. Confirm the employee's facts and the rules for the actual payday before filing, paying or relying on a calculation.

## Section 1 -- Scope and required inputs

This guide covers ordinary salary and wages, selected employee share schemes and selected extra-pay calculations for a New Zealand employer in NZD during **1 April 2026 to 31 March 2027**. It provides selected tax, contribution and filing rules, not complete employment-law or whole-topic coverage. Start with [Inland Revenue's salary and wage deduction instructions][S1] and its [2026-27 payroll calculation specification][S2].

Obtain the following before calculating:

- Employer registration, actual payday, pay frequency and period covered. [Register as an employer as soon as you start employing staff][S3].
- Employee classification, completed IR330 tax-code declaration and any Inland Revenue tax-code, tailored-rate, student-loan, child-support or arrears notice. Resolve conflicting instructions before using a rate.
- Gross pay and each payment's character. Determine PAYE income and KiwiSaver gross salary or wages separately; allowances, reimbursements and special payments need their own treatment.
- KiwiSaver membership and eligibility, valid deduction-rate instruction, employer contribution agreement (including whether it promises a gross or net-of-ESCT amount) and any valid opt-out, savings-suspension or temporary-rate-reduction notice.
- For ESCT, employment start date, whether the employee worked for this employer throughout the preceding tax year and the relevant salary/wages plus gross employer superannuation contributions.
- Annual PAYE and ESCT figures, any connected employers and the established filing and payment schedules. The $50,000 electronic filing test and $500,000 remittance test serve different purposes.

An unknown classification, contribution base or notice is an input gap. Do not invent a resident tax code, a pension exemption or a flat PAYE percentage. Ordinary salary rules do not establish the treatment of contractors, non-residents, offshore employers, IR56 workers, benefits or paid parental leave. The selected extra-pay methods below require an established payment classification; they do not determine employment-law entitlements.

## Section 2 -- PAYE and the employee ACC levy

Use the employee's IR330 code and any applicable Inland Revenue instruction, subject to the first-month RSE exception and other statutory exceptions explained below. For ordinary employees outside those exceptions, [Inland Revenue][S1] requires **ND at 45% plus the applicable ACC earners' levy** when no completed tax-code declaration is supplied. Do not use a zero rate or guess a standard code. Contractor schedular payments use a separate IR330C process; they are not automatically salary payroll. [S1], [S4]

Use the official PAYE calculator or actual-period deduction tables linked from [the salary/wage deductions page][S1], with the correct payday, tax code and pay frequency. PAYE calculation includes ACC earners' levy where applicable. **Do not add another ACC levy to a PAYE result that already includes it.** Annual income-tax brackets alone do not reproduce every payroll code, frequency, levy cap or rounding rule. [S1], [S2]

| Employee earners' levy period | GST-inclusive rate | Maximum annual liable earnings | Maximum annual levy |
|---|---:|---:|---:|
| 1 April 2026 to 31 March 2027 | 1.75% | $156,641 | $2,741.22 |

Source: [Inland Revenue's earners' levy table][S5]. Apply the actual payroll calculation and its cap rules; this annual table is not an instruction to charge 1.75% on uncapped pay or to combine multiple employments without checking their treatment.

Student-loan and child-support deductions need the actual code or notice and applicable calculation. Ordinary employee child support is limited to 40% of gross salary/wages less the PAYE income-tax component, excluding ACC earners' levy from that tax component. It does not cap every other deduction at 40%. The notice, protected-earnings and shortfall methods are set out below. [S1], [S2, section 5.15][S2], [S13, PDF page 24][S13]

The employee earners' levy comes from the employee's income through PAYE. The employer's **Work and Working Safer levies** are separately invoiced by ACC and require the business's classification, liable payroll and current invoice/rates. Do not add them as another generic employee deduction. This guide does not calculate those invoices. [ACC's explanation of levy responsibilities][S6] supports that distinction; use [S5] for the dated employee rate.

### Ordinary M and ME calculations

For regular positive salary or wages under **M, M SL, ME or ME SL**, use the sequence in [S2, sections 5.2-5.4][S2]. Confirm the declaration and notices first. The specification calls for 6 decimal places during calculations unless a stated truncation applies.

1. Multiply taxable period pay **including cents** by 52 for weekly pay, 26 for fortnightly, 13 for every 4 weeks or 12 for monthly. Then drop the annual amount's cents to obtain whole-dollar annual income A. Do not drop period cents before annualising M/ME pay.
2. Calculate annual income tax from the following table. Keep the result unrounded.

| Whole-dollar annual income A | Annual income tax |
|---|---|
| $1 to $15,600 | A × 10.5% |
| $15,601 to $53,500 | A × 17.5% − $1,092.00 |
| $53,501 to $78,100 | A × 30% − $7,779.50 |
| $78,101 to $180,000 | A × 33% − $10,122.50 |
| Above $180,000 | A × 39% − $20,922.50 |

3. Calculate the annual ACC component: **A × 1.75% where A < $156,641; otherwise $2,741.22**. Keep this component unrounded. Use the specification's stated maximum rather than multiplying the capped earnings and rounding independently.
4. For M/M SL, add annual tax and ACC. For ME/ME SL, subtract the applicable annual IETC from that sum. On the whole-dollar A, the payroll IETC is $0 below $24,000; **$520 from $24,000 to $66,000 inclusive**; **$520 − 13% × (A − $66,000)** from $66,001 to $69,999; and $0 from $70,000. Keep the credit unrounded.
5. Divide the annual total by **52**, then **truncate to cents**. For fortnightly, 4-weekly or monthly pay, multiply that already-truncated weekly amount by 52 and divide by 26, 13 or 12 respectively, then **truncate to cents again**. Dividing the annual total directly by 12 can give a different monthly deduction. This result is PAYE including ACC; student loans and other deductions remain separate.

The payroll credit formula does not establish IETC eligibility. Check NZ tax residence, total annual income and the exclusion where the employee or partner is entitled to and receives Working for Families, and the exclusions for income-tested benefits, NZ Superannuation, Veteran's Pension and overseas equivalents. Entitlement is tested by whole months. Use ME/ME SL only under the appropriate declaration; a main job below $24,000 with total income in the eligible range may need a tailored code or year-end credit. A year-end assessment may correct too much or too little credit. [IETC eligibility][S18], [salary/wage instructions][S19]

### Ordinary secondary codes and ND

A secondary code is chosen using **estimated annual total income from all sources**, rather than the second job alone. Follow the employee's IR330 and any Inland Revenue direction. For ordinary liable salary/wages, [S2, section 5.6][S2] gives these standard deductions, each already including the 1.75% ACC levy:

| Estimated annual total income | Secondary code, with SL where required | Standard PAYE including ACC |
|---|---|---:|
| Up to $15,600 | SB / SB SL | 12.25% |
| $15,601 to $53,500 | S / S SL | 19.25% |
| $53,501 to $78,100 | SH / SH SL | 31.75% |
| $78,101 to $180,000 | ST / ST SL | 34.75% |
| Above $180,000 | SA / SA SL | 40.75% |

Drop period pay's cents **before** multiplying by the applicable standard secondary rate, then truncate the deduction to cents. The whole payment uses that code's flat rate; these are not progressive bands within the second job. Do not add ACC again or import the M/ME annualisation algorithm. [S2, sections 5.1 and 5.6][S2], [tax-code instructions][S20]

For ordinary ND salary/wages, drop period cents, multiply by **46.75%** (45% tax plus 1.75% ACC) and truncate to cents. [S2, section 5.8][S2] These standard-code algorithms do not determine an individual's final annual ACC liability across multiple employments. Resolve a valid tailored tax code, levy adjustment or other exceptional instruction separately; do not remove ACC from a standard secondary or ND rate merely by applying the M-code cap formula.

### Ordinary NSW, CAE and EDW calculations

Establish the worker's qualifying employment before using a flat code. Inland Revenue's [tax-code instructions][S92], updated 30 April 2026, distinguish these cases:

| Code | Employment covered by the instructions |
|---|---|
| NSW | Recognised seasonal workers and holders of a work visa as foreign crew of a vessel fishing New Zealand waters. |
| CAE | YA 1 defines a casual agricultural employee as one of 3 categories. A **casual agricultural worker** is engaged day to day for no more than 3 months as a casual seasonal worker, exclusively for seasonal agricultural, horticultural, market gardening, nursery, orchard or tobacco farming work, or work the Commissioner considers similar. A **shearer** shears sheep other than in their own business and is not permanently employed on the premises where the shearing shed is. A **shearing shed-hand** is employed in or about the shed other than in their own business and is not a shearer, wool classer or person permanently employed on those premises. The 3-month limit applies only to casual agricultural workers. Inland Revenue's tax-code page also says these workers earn no other income in that time; YA 1 does not state that condition. [S98], [S92] IR335 keeps CAE for a shearer's ordinary farm work when shearing is not possible and for a farmer's part-time shearing for another farmer, but treats a normal farm employee's shearing wages as ordinary pay, not CAE. [S13, PDF page 57][S13] |
| EDW | YA 1 requires that the person is engaged, as an electoral official, interpreter, usher or otherwise, for an election or poll held under or subject to the Electoral Act 1993 or the Local Electoral Act 2001, or held simultaneously with and in the same premises as one; is paid by the authority controlling it; and is paid exclusively for work immediately before, on or immediately after its voting days. Qualifying local elections and polls are included; pay from anyone else, such as a party or candidate, is not. [S98] For a general election, Inland Revenue's tax-code page limits EDW to the 2-week advance-voting period and election day, and directs election work outside that period to the appropriate ordinary IR330 code. IR335 describes casual work immediately before, on or after polling day. [S92], [S13, PDF page 51][S13] |

The **first month of an RSE worker's period of employment in New Zealand** has a specific statutory exception. Schedule 5 Part B clause 3 supplies NSW, and sections 24B(1)(c), 24C(2)(b) and 24E(1)(c) recognise that exception to ordinary notification and non-notified treatment. It is not a general first-month exception for every foreign worker. After that first month, the ordinary tax-code notification rules apply. NSW can continue for qualifying employment with proper notification; month-end alone does not require a different code. For an ordinary worker outside section 24D, if the required name, IRD number and tax code have not been notified, no applicable Commissioner-provided code applies and the first-month exception has ended, use ND until the notification requirement is met. Resolve any Commissioner correction, changed circumstances or entitlement-ending notice under Schedule 5 Part A clauses 2-4. [S93], [S94], [S95], [S96], [S97], [S2, section 5.5][S2]

For established **ordinary** pay under these codes during 1 April 2026 to 31 March 2027, use [S2, sections 5.5 and 5.7, PDF pages 26-27 and 30][S2]:

1. Identify ordinary taxable pay for the period, including taxable allowances. Keep non-taxable allowances and separately classified extra pay out of that ordinary base.
2. Drop the ordinary base's cents to obtain whole-dollar pay. For example, $457.89 becomes $457. Do not annualise it using the M/ME method.
3. For NSW, multiply that whole-dollar pay by **12.25%**: 10.5% income tax plus 1.75% ACC. For CAE or EDW, multiply by **19.25%**: 17.5% income tax plus 1.75% ACC.
4. **Truncate the combined deduction to cents.** Do not round it to the nearest cent or add ACC again. Deduct it from actual cash pay, retaining that pay's cents. Calculate other applicable deductions and separately classified payments under their own rules.

These methods do not establish the worker's final annual ACC liability across employments or an exceptional levy adjustment. Do not import the M-code cap formula into them without an applicable instruction. The worked cases below use ordinary amounts below the standard period caps and assume no exceptional notice or adjustment. Donations, unusual pay, negative corrections and final ACC reconciliation require separate checks. [S2], [S5]

**Do not make ordinary student-loan repayment deductions from pay correctly using CAE, EDW or NSW.** IR335 expressly lists those codes as exclusions. A valid NSW employment-information line cannot contain KiwiSaver or student-loan deductions; the specification identifies these non-resident workers as ineligible for KiwiSaver and permits child support where applicable. CAE or EDW alone does not establish a KiwiSaver exemption: apply the separately established membership, contribution and notice rules in Section 3. A code exclusion does not decide the person's wider loan liability. [S13, PDF page 20][S13], [S2, section 5.5][S2]

### Ordinary student-loan deductions

For the 2026-27 period, the specification's annual repayment threshold is **$24,128**, with these primary-job period thresholds: weekly **$464**, fortnightly **$928**, every 4 weeks **$1,856** and monthly **$2,010.66**. Use the stated monthly amount rather than rounding it to $2,010.67. [S2, sections 2.2 and 5.4][S2]

For **M SL or ME SL**, drop gross period pay's cents, subtract the applicable period threshold and deduct **12% of a positive excess**, truncating the result to cents. The deduction is zero where there is no excess. For an ordinary **secondary SL code**, drop period cents and deduct **12% of that whole-dollar pay**, truncating to cents; there is **no second ordinary repayment threshold**. A valid special-deduction-rate certificate substitutes its specified percentage in the relevant algorithm. Keep the student-loan result separate from PAYE, and do not reduce taxable pay by it. [S2, sections 5.4 and 5.6][S2]

Check the actual SL declaration and any repayment exemption, special rate or extra-deduction notice before using these ordinary rules. An unused primary-job threshold does not automatically transfer to a second job; apply for the appropriate special rate. Inland Revenue's [salary/wage student-loan page][S21] explains that distinction but labels its annual threshold as the **2026 tax year**; the dated 2026-27 specification supplies this guide's period-specific figures. Exemptions, recovery deductions and irregular or special payments need their own checks.

### Tailored tax codes and student-loan certificates

Use an actual Inland Revenue certificate covering the payday. Record its PAYE rate, separate student-loan rate, whether the loan threshold applies and each start/end date. For ordinary salary or wages, truncate period pay to whole dollars, multiply by the certificate's PAYE rate and truncate the deduction to cents. The quoted salary/wage PAYE rate already includes the 1.75% earners' levy; do not add it again. Calculate the loan deduction separately on the whole-dollar base: apply the certificate rate to positive income above the period threshold for main employment, or to every dollar for secondary employment, as the certificate directs. [S2, section 5.9, PDF pages 32–33][S2]

A student-loan special deduction rate changes the loan calculation, not the PAYE tax code unless the certificate says so. It may allocate unused main-job threshold through a reduced secondary-job rate; the employer cannot invent that allocation. Follow each dated rate period. Do not backdate a special deduction rate or a repayment exemption. On expiry, follow the certificate's return-to-standard instructions. If a tailored PAYE certificate expires without a replacement or new declaration, revert to the previous IR330/IR330C code; if there was none, use ND until a valid declaration or certificate arrives. [S2, section 5.9.2, PDF pages 34–37][S2]

A full-time student expecting income below the annual repayment threshold may qualify for a repayment deduction exemption even when an individual pay exceeds its threshold. Require the IRD exemption certificate, use its specified non-SL code only for its valid period and restore its instructed SL code when it ends. Student status alone does not authorise stopping deductions. A special loan rate does not absorb voluntary SLBOR deductions; keep them separate. IRD says it cancels SLCIR notices when granting an SDR: reconcile the actual notice trail rather than silently retaining or cancelling a recovery instruction yourself. [S2, sections 5.9.2–5.9.3][S2]

### Extra pay: choose the calculation before choosing a rate

Annual or special bonuses, cashed-up leave, back pay and redundancy/retiring payments can be extra pay. Overtime and regular payments are not automatically lump sums. First establish the payment's legal character, whether it relates to ending employment, the employee's code and any election for a higher rate. NSW, ND and tailored-code payments use their applicable special rate rather than the ordinary extra-pay rate table; CAE/EDW extra pay follows the primary-income method. This guide does not establish entitlement to a termination payment or a contractor's schedular-payment treatment. Use the separate selected ESS rules below for established employee cases. [S22], [S23], [S24]

For a **non-termination** extra payment under an ordinary primary or secondary code:

1. Total regular PAYE income payments in the 4 weeks ending on the payment date, including that date but excluding all extra pays. Annualise by 13 for weekly, fortnightly or four-weekly payments and by 12 for monthly payments. An off-cycle extra payment still uses a window ending on its actual payment date. No regular payment in that window means a zero historical amount, not an assumed annual salary. Where only one prior pay period exists, use its pay amount annualised for its frequency. [S2, section 5.11][S2], [S22]
2. For a secondary code, add the low threshold below to that annualised amount. Add zero for a primary code. Call this combined amount **B**. Add the extra pay **E** to B and truncate that grossed-up total to whole dollars **G** solely to select the tax band. Retain cents in E and B for the deduction and levy calculations. [S2, sections 5.11.1–5.11.2][S2]
3. Select the income-tax rate below, or the employee's valid election for a higher permitted rate. Multiply the **whole extra payment**, with its cents, by that single rate. This is withholding on the extra pay, not a progressive allocation of the extra pay amongst annual bands. Do not truncate that tax component before adding the levy. [S2, section 5.11][S2], [S22]

| Secondary code, with or without SL | Amount added to annualised income |
|---|---:|
| SB | $0 |
| S | $15,601 |
| SH | $53,501 |
| ST | $78,101 |
| SA | $180,001 |

| Whole-dollar G | Income-tax rate, excluding ACC |
|---|---:|
| Up to $15,600 | 10.5% |
| $15,601–$53,500 | 17.5% |
| $53,501–$78,100 | 30% |
| $78,101–$180,000 | 33% |
| Above $180,000 | 39% |

Sources: [S22], [S24] and [S2, section 5.11][S2]. The web tables explicitly include the first dollar of each band. Do not copy the specification's inconsistent 'greater than $15,601/$53,501/$78,101' wording and leave those boundary amounts unassigned. An employee can elect a higher 17.5%, 30%, 33% or 39% income-tax rate where applicable; establish the instruction before using it. [S2, section 5.11][S2]

Calculate ACC separately. For an ordinary levy-liable extra payment, the levy base is the lesser of E and the positive amount remaining from **$156,641 minus B**. Multiply that base by **1.75%**. Thus a payment crossing the cap has levy only on the part below the cap; do not simply levy all or none because G crosses it. Redundancy payments, retiring allowances and ESS benefits are not liable for this earners' levy; use the selected ESS rules below for the benefit's other treatment. Add the unrounded income-tax and levy components, then truncate the total to cents. These are the specified withholding calculations; they do not determine the employee's final multi-employer annual ACC position. [S2, sections 5.11–5.12][S2], [S22], [S24]

For a tailored code, follow the certificate rather than the table. For a confirmed redundancy payment or retiring allowance, remove the earners' levy included in that rate and mark the earnings as not liable for ACC on the employment information. For example, a 24% certificate rate less the 2026-27 levy of 1.75 percentage points is **22.25%**. The specification's printed 22.58% example is an arithmetic error; do not use it. Resolve the actual certificate and payment classification before applying this adjustment. [S2, section 5.11, PDF pages 45 and 51][S2], [S22]

### Extra pay when employment ends

For payments arising from the end of employment, use the **last 2 paid regular pay periods before the period containing the extra payment**, excluding other extra pays. Skip unpaid periods and out-of-cycle payments. Do not annualise the current termination-period wage or automatically use the last 4 calendar weeks. Total the 2 paid periods and multiply by 26 for weekly, 13 for fortnightly, 6.5 for four-weekly or 6 for monthly pay. When those 2 periods have different frequencies, annualise each at its own frequency and average the 2 annual values. With only one earlier paid period, annualise that period at its frequency. If no prior period exists, resolve the applicable employee instruction and IRD method before calculating. [S2, section 5.12, PDF pages 55–64][S2], [S24]

Add the secondary low threshold where applicable, then the extra payment, and use the same rate/levy steps above. Combine other extra pay paid together with termination extra pay for this calculation; do not calculate each under a different annualisation method. Keep each component's ACC character: a normal bonus does not become levy-exempt merely because it accompanies redundancy pay. These end-of-employment instructions apply to payments on or after 1 April 2025; the rates and levy amounts here are for 2026-27. [S2, section 5.12][S2], [S24]

### Student loans, regular bonuses and reporting

For primary M SL/ME SL extra pay, combine regular and extra taxable pay for the pay period, truncate that combined pay to whole dollars, subtract the period repayment threshold once and apply 12% to any positive excess, or the valid certificate rate. Truncate the loan deduction to cents. Do not give a second threshold if wages have already used it. When the extra pay is separate and total period pay cannot be established, apply the appropriate loan rate to the entire extra pay. Secondary SL extra pay has no ordinary threshold: truncate the relevant pay to whole dollars, apply 12% or the certificate rate and truncate to cents. Tailored codes follow the certificate's threshold instruction. Keep PAYE and loan deductions separate. [S2, sections 5.11–5.12][S2], [S23]

Regular incentive/production bonuses paid with normal wages are included in normal period pay. For a monthly bonus covering several pay periods, calculate monthly PAYE on that month's wages with and without the bonus and deduct the difference. For a bonus covering several months, divide it by those months, calculate the difference between monthly PAYE with and without that monthly share, then multiply the difference by the number of months. Apply the corresponding loan method for an SL code. This is the regular-bonus method, not an annual/special lump-sum rate selection. [S2, section 5.13][S2]

For an enrolled KiwiSaver employee, a confirmed redundancy payment is excluded from employee KiwiSaver deductions; do not assume the same exclusion for every other extra payment. Check the contribution base and notices separately. Report a lowest-rate extra payment using the low-rate indicator. For separate extra-pay reporting, file within 2 working days electronically or 10 working days on paper. IRD permits inclusion in the next regular electronic schedule only when reported before the relevant deduction-payment end date: month-end for monthly remitters, or the 15th/month-end for twice-monthly remitters. Record which permitted reporting route was used. [S23], [S2, section 5.11.3][S2]

### Student-loan recovery and voluntary extra deductions

Keep ordinary student-loan deductions, **SLCIR** recovery and **SLBOR** voluntary deductions separate. An IRD SLCIR notice states the amount to recover and the percentage to deduct until that amount has been reached. Use that notice, not an automatic extra 5% on every SL employee. For ordinary primary employment, the maximum recovery rate is **5% of gross pay above the pay-period repayment threshold**; for secondary employment it is **5% of gross pay without that threshold**. Truncate gross pay to whole dollars for this calculation and truncate the deduction to cents. For 2026-27 the weekly primary threshold is **$464**; use the corresponding period threshold already set out above. Do not recover more than the remaining amount required by the notice. [S2, section 3, PDF pages 9–10][S2], [S25]

A voluntary SLBOR deduction uses the employee's actual requested amount or percentage. Report ordinary loan deductions, SLCIR and SLBOR in their respective employment-information fields. These are additional loan deductions, not PAYE income tax. Keep the notice balance, effective dates, actual deduction and any cancellation or certificate change together; an SDR and its cancellation trail require the separate checks above. [S2, sections 3 and 5.9.2][S2], [S13, PDF page 22][S13]

### Employee child-support notices and protected earnings

Use the actual employee deduction notice, its start/amend/stop date, pay frequency and amount. Do not start early. Ask IRD to correct an incorrect payday or frequency rather than silently converting the notice yourself. The employee cannot instruct the employer to start or stop these deductions. The contractor/schedular-payment notice has a different payment and employment-information route; the employee instructions here do not establish that route. [S2, section 5.15][S2], [S13, PDF page 23][S13]

For the ordinary employee child-support calculation, let **G** be gross salary/wages, **P** PAYE including the employee ACC earners' levy and **A** that levy component. The protected-earnings calculation uses **N = G − (P − A)**, so its income-tax deduction excludes ACC. The normal maximum child-support deduction is **40% of N**: deduct the lesser of the notice amount and that capacity. The remaining 60% is protected for this purpose, not a guaranteed final take-home amount after student loans, ACC, KiwiSaver and other lawful deductions. Establish special payment bases separately; this formula does not resolve ESS or schedular payments. [S2, section 5.15.1, PDF pages 71–72][S2], [S13, PDF page 24 worked example][S13]

Where protected earnings prevent the full deduction, report variation **P** and the amount actually deducted. Do not make up the difference in a later pay; IRD arranges it with the employee. Other variation codes are A for advance payment, D for previously deducted, S for a short unpaid absence preventing any deduction and O for other reasons. If employment has ceased, **C takes priority even when P would otherwise apply**; record the employee finish date as well. Include employee child support in employment information and pay it with the ordinary employer deductions. Protect the employee's child-support information. [S1], [S13, PDF pages 24–25][S13]

### District Court attachment orders

Identify the statute and actual order. **Section 157 of the District Court Act 2016** governs these court attachments; **section 157 of the Tax Administration Act 1994** below is a different notice. The court order specifies the earnings period, deduction amount or percentage and minimum earnings to retain. For an ordinary District Court attachment, the protected floor is the **higher of 60% of statutory net earnings and the actual order's minimum**. Use the PAYE income-tax component for the net-earnings base, with the ACC distinction above. Confirm which payments are salary/wages for the order: the statutory definition is broader than ordinary basic pay. [S27], [S28], [S29], [S2, section 5.15.2][S2]

Section 157(3) requires the court attachment to be reduced or cancelled as necessary when it alone, or together with the listed other notices/orders, would take earnings below that floor. For a single ordinary court order with established prior deductions, its available capacity is **max(0, N − protected floor − applicable prior deductions)**; deduct the lesser of that capacity and the amount required by the order. Child support has priority. Section 157(2) also makes the ordinary court charge subject to the specified Family Proceedings/Summary Proceedings attachments and statutory deduction notices. Do not invent priority amongst competing orders or reduce a different statutory notice merely by applying this court formula; obtain the actual instruments and resolve their priority with the issuer/court or IRD. [S27], [S13, PDF page 23][S13]

The specification's page 72 step 5 prints the full other-attachment amount even when it exceeds remaining capacity. That instruction conflicts with section 157(3)'s protection. Apply the statutory reduction instead of copying the printed branch. The worked checks below assume the stated order, base and prior deductions are already valid; they do not determine every competing-notice combination. [S27], [S2, PDF page 72][S2]

### IRD tax-arrears notices

A Tax Administration Act section 157 notice for salary/wage arrears is separate from a student-loan SLCIR recovery notice. Obtain its required amount, instalment period, initial notified debt, payment deadline, tax reference and any notified interest. For the ordinary statutory salary/wage ceiling, compare **10% per week of the debt due at the notice date** with **20% of gross salary/wages payable**. Take the lesser, then compare it with **$10 per week** and take the greater. For non-weekly pay, scale the weekly debt instalment and minimum to the pay period; the 20% limb already uses that period's actual gross pay. This is a ceiling, not an instruction to deduct it when the actual notice requires less. Limit the deduction to the amount actually payable and required under the notice. [S30, subsections (1)–(3)][S30], [S26], [S32, paragraphs 26–28][S32]

IRD's SPS 21/01 says no extra deduction is required where weekly earnings are **less than $10**. It also addresses an employee request for a higher deduction. Follow the applicable notice and actual request; resolve an apparent conflict with IRD rather than creating a deduction that exceeds the wages available. The specification's page 75 flowchart shortcut of $10 when weekly gross is below $100 does not reproduce the general statutory formula: for example, 20% of $80 is $16. Other fixed-amount notices may be issued. [S32, paragraphs 27–28][S32], [S2, section 5.17][S2]

Child-support arrears use a different notice and calculation, and child support takes priority over other tax arrears. Check that actual instrument separately; the ordinary employee child-support formula above does not establish all arrears or contractor cases. Do not merge different notices into one generic 40% cap. [S26], [S32, paragraphs 29–30][S32]

Do not put these tax-arrears deductions in employment information or the SLCIR field. Pay them separately from PAYE using the employee's IRD number, tax type, period and amount. The general payroll instructions say by calendar month-end; the Act and SPS require payment within the time in the actual notice, so establish that deadline before processing. Notify the employee of the deduction and its purpose. The amount withheld is held in trust for the Crown. Keep the notice until the required amount is paid or IRD changes/revokes it in writing; the employee cannot cancel it. [S2, section 5.17][S2], [S26], [S30, subsections (1), (4), (6) and (8)][S30], [S32, paragraphs 33–36][S32]

### Employee share schemes: establish the benefit first

These selected rules concern an established employee under a contract of service, with an ordinary New Zealand payroll code. Obtain the scheme and offer terms, employment connection, beneficiary and associate details, issue/transfer/vesting/cancellation dates, market values, consideration, any withholding election and the written funding agreement. An incentive labelled a share scheme is not enough. Section CE 7 requires an arrangement with a purpose or effect of issuing or transferring shares, connected to employment or service, and has exclusions for exempt ESS and the specified market-value arrangements. IS25/06 does not establish an independent contractor's or non-executive director's treatment. Section RD 7(1B), effective 21 February 2026, excludes its specified contractors and other statutory non-employees from extra pay. Resolve classification before applying this employee method. [S74], [S75], [S78], [S82]

A scheme that always pays cash and never has a purpose or effect of issuing or transferring shares is ordinarily a phantom scheme with an ordinary cash bonus. A mixed cash/share award does not make its cash entitlement an ESS benefit automatically. For genuine cash settlement, establish that the payment is consideration for transfer or cancellation of shares or related rights and gives rise to a CE 2 benefit. Otherwise check the ordinary bonus rules, including ACC and KiwiSaver, separately. [IS25/06, paragraphs 5-13 and 38-48][S75]

### Exempt ESS: establish the scheme before excluding payroll

An amount derived from an exempt ESS is exempt income under CW 26B. CW 26C has 2 routes: a scheme with the Commissioner's approval under former DC 12 before its 2018 repeal, or the modern notified arrangement described below. A legacy approval, an IRD receipt or meeting the dollar limits alone does not establish every applicable condition. Keep the approval or notification, complete scheme terms, offer dates, employee/associate evidence, valuations, payments and annual returns. Actual legacy approvals and their continuing effect require separate review. [S100], [S101]

For the modern route, the Commissioner must have been notified under TAA 63B(1), the arrangement must meet CW 26C(2)–(9) and the Commissioner must have **received all forms due** under TAA 63B(2) and (3). Check receipt as well as submission. These provisions do not, by themselves, settle the timing or retrospective effect of a missed form or a later cure; obtain a specific determination before treating a non-compliant scheme as exempt or reclassifying earlier payroll. [S101], [S106]

#### Purchase, value and participation conditions

For offers made **on or after 1 April 2025**, the increased limits apply for the **2025–26 and later income years**. A later purchase under an earlier offer does not establish that these limits apply. Section 27 of 2025 No 9 increased the share-value limit from $5,000 to **$7,500** and the discount limit from $2,000 to **$3,000**; earlier offers and other historical transitions need their own check. [S107, sections 2(34) and 27][S107]

| Condition | Required scheme provision or established input |
|---|---|
| Meaning of share | For CW 26C, CW 26F defines share, for a company whose shares are made available under an exempt ESS, as a **fully paid ordinary share** that **ranks equally with, and has the same designation as, an existing ordinary voting share** in the company. A partly paid share is not a share for CW 26C. Establish the offered shares' terms and designation. [S112] |
| Price and annual amounts | Shares must be available for no more than market value at purchase/subscription. Shares purchased/subscribed for by the employee or a trustee for them have market value of no more than **$7,500 in a year**. That market value less the employee's spending on the shares is no more than **$3,000 in a year**. Aggregate the relevant purchases, rather than testing each grant in isolation. [S101, subsection (2)][S101] |
| Meaning of year | YA 1 defines year as a **12-month period**. Establish the relevant period for the arrangement and its purchases; do not assume a fresh allowance on 1 April merely because the separate annual return uses a tax year. [S98], [S101] |
| Market value | CW 26DB imports YA 1 market value (a)/(b): a quoted share/option ordinarily uses the middle market quotation for the same terms, subject to the fair-reflection qualification; an unquoted one uses the arm's-length willing-purchaser amount, with a commercially acceptable, fair and reasonable valuation method. Appropriate income, cash-flow or asset methods may be relevant. CW 26DB also permits the **5-day volume weighted average price**, another Commissioner-accepted method or a comparable method for quoted shares/options. This guide does not establish an actual valuation or recognised-exchange status. [S98], [S103] |
| Employee and ownership | CW 26D requires employment by the company. It excludes a non-employed director, a company/other body and a person who, with any associated person, holds **10% or more** of issued capital. Exactly 10% is excluded. Establish association and the relevant holdings; an employee's own holding below 10% is insufficient evidence. [S102] |
| Equal participation | A full-time permanent employee receiving an offer must be eligible on an equal basis with **90% or more of other full-time permanent employees whose offers are not subject to foreign security disclosure rules**. If the arrangement applies to part-time employees or seasonal workers, apply the same statutory test separately to that class. Establish the actual comparison pool, foreign-disclosure qualification and equal terms, rather than using an unqualified whole-workforce percentage. [S101, subsection (3)(a)–(c)][S101] |
| Minimum spending/service | A required minimum spend must be no more than **$1,000 in a year**; this limits the required minimum, not an employee's voluntary spending. Any service requirement must be no more than **3 years** of full-time work, or an accumulated equivalent for other employees. [S101, subsection (3)(d)–(e)][S101] |
| Trust dividends | If a trust holds shares for an employee, the trustee must pay dividends directly to the employee and the dividends must be treated as derived by that employee. For CW 26C, CW 26G defines trustee as a group of persons appointed to administer an exempt ESS of a company that employs an employee, and to hold shares under that scheme on trust for the employee during any period of restriction described in CW 26C(7). Exemption of the scheme benefit does not establish exemption of dividends. [S101, subsection (3B)][S101], [S113] |

#### Financing, hardship, restrictions and exit

Where the employee must buy shares for **more than nominal consideration**, the arrangement must make a loan for their cost available or permit regular instalments at intervals of a month or less. Any purchase loan must be free of interest **and other charges**. Loans/regular instalments have terms of **36–60 months**. Loan repayments must be monthly or more frequent, with early repayment in full or part at the employee's discretion. For unpaid or parental leave lasting **more than a month**, regular instalments are suspended whilst on leave and the loan term is extended as appropriate; the direct-instalment alternative is also subject to that suspension provision. Keep this statutory extension qualification when testing the ordinary 60-month limit. [S101, subsection (4)][S101]

If continued participation causes or may cause serious hardship, the arrangement must provide, **with the employee's agreement**, for payment terms to be varied or withdrawal with a **market-value** buyback on the withdrawal day, subject to repayment of the outstanding loan. Ordinary withdrawal instead requires **1 month's notice** and buyback at the **lesser of market value on that day and the employee's cost**, again subject to the outstanding loan. Do not use the hardship price merely because an employee wants to leave. [S101, subsections (5)–(6)][S101]

For shares acquired below market value, the restriction period prohibits disposal except a takeover or similar share reorganisation. Its length is the **shorter** of (a) **3 years from acquisition or the loan repayment period, whichever is longer**, and (b) the period until employment ends with the employer, or the same-group employer following a transfer. A group transfer alone is not the stated employment-end event. For market-value acquisitions, the restriction is **no longer than** the shorter of that statutory period and an arrangement restriction ending on or after all loan repayment obligations cease. Preserve that separate market-value branch rather than imposing the discounted-share period on every purchase. [S101, subsection (7)][S101]

At restriction end, a subsection (8) scheme may provide transfer if needed or, at the employee's choice, buyback at the lesser of cost and then market value. If the scheme does not use that option, subsection (8B) requires that choice for a current employee but requires the lesser-value buyback for someone no longer employed. Subsection (9) overrides both where employment ends through **death, accident, sickness, redundancy or retirement at normal retiring age**: transfer to the former employee/estate as appropriate or, if the employee chooses, the lesser-value buyback. Do not presume every resignation receives that protected-exit treatment. [S101]

CW 26E defines normal retiring age as no less than **60**, with a **55** minimum for its specified female employee whose pre-**1 April 1978** employment contract entitles her to earlier retirement. It also allows an earlier age the Commissioner considers reasonable for the employment/business/occupation. Require the relevant contractual or Commissioner basis; an employee's chosen retirement date alone does not establish it. [S104]

#### Employer deductions and separate annual disclosure

DV 28 denies a party to an exempt ESS a deduction for related expenditure/loss, **except to the extent incurred in establishing or managing the scheme**. That exception removes this particular denial; it does not, by itself, establish positive deduction entitlement under all other rules. Keep acquisition/funding costs separate from evidenced establishment/management costs. [S105], [S99]

Notify Inland Revenue using **IR1211**. The October 2026 blank form requests the registered company name, company IRD number and a signed declaration that the arrangement meets CW 26C(2)–(9). The current IRD process sends that form to its published exempt-ESS address. TAA 63B(1) does not state a fixed 20-day initial deadline; do not import the separate deferred-share deadline. [S106], [S108], [S110]

For each tax year, provide the prescribed annual return **on or before 31 May following that tax year's end**. The October 2026 **IR1212** records the company, period start/end, **total value of shares granted, total employee contributions and number of employee recipients**. Reconcile those aggregates to individual scheme records and retain receipt evidence. The form's aggregate fields do not replace each employee's value/discount eligibility tests. IRD excludes exempt ESS benefits from ordinary employment information; use this separate disclosure process once exemption is established. An annual form submitted but not received is not sufficient evidence of the statutory receipt condition. [S101], [S106], [S109], [S111], [S85]

### ESS value, taxing date and 2026 deferred shares

Determine the share scheme taxing date under CE 7B from the actual scheme conditions. It is ordinarily the earlier of qualifying beneficial ownership without the stated material risks/protections, or cancellation/transfer to a person outside the specified association. Subsection (2) ignores specified rights, including certain market-value transfer rights and immaterial risks. A vesting label or an ordinary disposal restriction alone does not establish the date. [S80]

Under CE 2, calculate **share value − consideration paid + consideration received − previous income** using the statutory definitions. If transfer/cancellation triggers the taxing date, do not add a market value as share value to the consideration received. Consideration can be paid or payable; replacement-scheme consideration and historic previous income have specific limits. A positive amount is a benefit; a negative amount is dealt with as a deduction under CE 2(3), not automatically negative payroll or a refund. Valuation evidence, historic transitions, replacement schemes and foreign-service allocation require their own actual-case checks. [S79]

For shares issued or transferred on or after **1 April 2026**, EA 4B can defer the taxing date to a qualifying liquidity event. The issuing company must be unlisted and outside a group containing a listed company. Designate qualifying shares **at issue or transfer** and notify **both** the Commissioner and the beneficiary within **20 days**, or by a later date allowed by the Commissioner. An unlisted-company description or a late internal designation does not establish eligibility. [S81], [S91]

The liquidity date is generally the earliest relevant listing, sale/transfer to a person outside the specified association, or cancellation, including company cessation. If that event occurs during a restriction preventing disposal, use the restriction's end date. EA 4B(4)(c) excludes specified share-only exchanges into another qualifying unlisted company. Keep evidence for those conditions and exceptions rather than using every sale or group reorganisation as a trigger. The March 2026 IRD summary is shorter than the enacted conditions; it predates assent and is not an exhaustive eligibility test. [S81], [S83], [S91]

### Withholding, student loans and funding

| Established payment or benefit | Selected employee payroll treatment |
|---|---|
| Genuine cash-settled CE 2 ESS benefit | Withhold income tax using the applicable extra-pay method; deduct student loan where required. The employer cannot elect out of mandatory cash withholding. No ACC earners' levy or KiwiSaver deductions/employer contributions on the ESS benefit itself. |
| Share-settled benefit | The employer can ordinarily choose whether to withhold. An offer or scheme term requiring withholding creates an irrevocable RD 7B obligation for that benefit/employee and replacement benefits. A valid election requires calculation, payment and timely employment-information disclosure. If withholding applies, use extra-pay income tax and any required student-loan deduction, with no ACC or KiwiSaver on the benefit itself. |
| Share-settled benefit with no withholding | Report where required; the employee deals with income tax through their annual return and provisional tax if applicable. No withholding does not mean tax-free income. |
| Separate employer payment to fund tax or student loan on a share benefit | This is separate extra pay, outside CE 2's ESS benefit value. Establish its income-tax, ACC, student-loan and KiwiSaver treatment independently; the ESS exemptions do not extend to it. |

Sources: [S74], [IS25/06, paragraphs 5-13 and 103-125][S75], [S77], [S82], [IS25/07, paragraphs 35-71][S76], [S88]. The 2025 interpretation statements' illustrative rates are not the 2026-27 rate tables.

Apply the selected extra-pay income-tax method above to the established ESS benefit using the **excluding-ACC** rate. For student loans, first establish the notified SL/TTC code or other required notice and any special deduction certificate. The ordinary primary-pay threshold is available only once in the pay period; secondary SL extra pay has no threshold. Use the complete-dollar and cent rules in the student-loan method above, rather than a universal percentage of every benefit. [S2], [S22], [S24], [S84], [S88]

Document who funds each deduction. An employee-funded tax payment, agreed sale of their shares or agreed deduction from net salary does not itself give the employee an additional employer-funded benefit. An employer-funded payment does. For the latter, first calculate the income tax and any student-loan amount on the ESS benefit that the employer agreed to fund, then gross up that **additional payment**, not the share value. IS25/07 gives **gross additional payment = net funding required ÷ (1 − combined funded deduction rates)**. Include only deductions the employer funds, at their actual applicable rates and bases. Recheck the extra-pay band, ACC cap, loan threshold/certificate, KiwiSaver base/rate and statutory rounding after grossing up; a single flat divisor is insufficient if any boundary changes. Establish compulsory employer contributions and ESCT separately. An agreement to fund income tax alone does not fund the employee's student loan or KiwiSaver automatically. [IS25/07, paragraphs 47-67][S76]

These rules do not authorise a wage deduction or share sale without the required agreement. For child-support or competing notices on an ESS benefit, obtain Inland Revenue's direction; do not extend the ordinary protected-earnings example automatically. [S74], [IS25/06, paragraph 19][S75]

### ESS income, filing and payment dates

Where CE 2(7)'s employment-information condition applies, CE 2(8)-(9) places income recognition on the **ESS deferral date, 20 days after the share scheme taxing date**. For qualifying employee deferred shares, first substitute the EA 4B liquidity date. A former employee's share benefit without withholding has the stated reporting exclusion and is ordinarily recognised on the taxing date, without this reporting-based deferral. [S79], [S80], [S85], [S86]

Report the ESS benefit in its **employee share scheme earnings** field, also in the **earnings not liable for ACC earners' levy** field. Use the current tax code, not the retired ESS code. Show PAYE and student loan deducted. Keep an employer's separate tax-funding payment in **gross earnings**, outside the ESS field, with its own levy treatment. Do not treat the ESS reporting value as additional cash wages. [S76], [S85]

TAA 23K permits payday reporting using the ESS deferral date or the specified twice-monthly method: deferral dates on the 1st-15th use the 15th; later dates use month end. File within **2 working days** electronically or **10 working days** under allowed paper filing from the applicable reporting day. Exempt ESS benefits are excluded from this reporting regime; establish exemption separately. Former-employee share benefits without withholding are excluded, but withheld benefits must be reported. A cash payment to a former employee is not automatically covered by the share-only operational exception. [S85], [S86]

Filing and paying remain distinct. RD 6(3) supplies the deemed payment date for the elected non-cash benefit; RD 7B links the election to timely disclosure and RD 4 payment. For cash, RA 5(2) requires withholding when payment is made. Do not use an EI reporting concession as blanket authority to delay cash withholding or remittance. A separate funding payment uses its own actual payment facts; IS25/07's same-reporting-date example assumes aligned processing, rather than creating a universal ESS timing rule for the extra cash. Apply the established monthly/twice-monthly remittance schedule in Section 5 and reconcile the streams. Unusual differences between cancellation, cash payment, deferral and funding dates need a specific Inland Revenue/qualified review before processing. [S76], [S77], [S87], [S89], [S90]

## Section 3 -- KiwiSaver from 1 April 2026

For ordinary post-2009 default cases, the employee deduction and minimum compulsory employer contribution increased from 3% to **3.5% for paydays on or after 1 April 2026**. The payday determines the rate for the whole payment when a period straddles 1 April; do not prorate by days worked. A surviving historical 4% employee default is addressed below. Existing valid elections of 4%, 6%, 8% or 10% remain available. [S7], [S45, subsection (3B)][S45], [S50, subsection (4B)][S50]

### Establish membership and automatic-enrolment eligibility

Membership, automatic enrolment and compulsory employer-contribution eligibility are separate questions. For the ordinary case, establish that the person normally lives in New Zealand and is a citizen or entitled to remain indefinitely, and that the employer is within the Act. A temporary visitor, student or work permit does not establish indefinite entitlement. The State services overseas exception and other cross-border cases need their own checks. [S41], [KS4, PDF page 6][S33]

Automatic enrolment ordinarily concerns a new employee aged **18 or older and under 65** at the start of employment, with a non-exempt employer and no applicable exception. It does not automatically enrol a 16- or 17-year-old. An under-18 person joins through a provider; an existing member supplies their membership and deduction information rather than being enrolled again. Membership can continue beyond 65 even where compulsory employer contributions cease. [S42], [S44], [KS4, PDF pages 6–11][S33]

Check the exceptions before treating any new starter as automatically enrolled. A contract for no more than 28 continuous days is temporary for this purpose; count calendar days of employment, not shifts. If that employment continues, the temporary exclusion ends on day 29, described in section 12(2)(b) as the 28th day after employment started. Casual agricultural employment and qualifying irregular/intermittent employment with holiday pay have separate statutory tests. Section 14 also excludes existing members and specified situations such as private domestic service, election-day work and employment without required PAYE withholding. This is not an exhaustive classification checklist; resolve the actual section 12/14 exception, secondment or exempt-employer status first. [S43], [S44], [KS4, PDF page 7][S33]

Give a person who is automatically enrolled the KiwiSaver information pack within **7 days** of starting. Collect the applicable KS2 deduction information and retain it; do not send KS2 to IRD. Give IRD the applicable new-employee KiwiSaver details using IR346K/myIR or payroll software no later than the first employment-information return is due. Coordinate this with the separate new-employee information deadline in Section 5. Start required deductions from the first payment for an automatically enrolled employee; for an existing member or an IRD direction, section 60 applies to payments calculated after the employer receives the relevant notice. Obtain a valid savings-suspension notice before omitting otherwise required deductions. [S34], [S35], [S49], [KS4, PDF pages 8–11][S33]

### Employee rates, changes and temporary reductions

Use the valid KS2, written rate instruction or IRD notice. The ordinary elected choices are **3.5%, 4%, 6%, 8% and 10%** of KiwiSaver gross salary or wages. Apply a valid change to the first payment calculated after receipt; ordinary changes must be at least **92 days** apart unless the employer agrees to a shorter interval. Do not backdate missed employee deductions when acting on IRD's start instruction. A possible employer-contribution arrears obligation is a separate question and is not cancelled by that employee-deduction instruction. [S8], [S45, subsections (2)–(4)][S45], [KS4, PDF page 14][S33]

Do not assume every employee without a new election defaults to 3.5%. Section 64(1)(ab) retains a **4% default** where section 60(1)(a), (b) or (c) first applied to this employer in respect of this employee before 1 April 2009, subject to the statutory alternatives and any overriding election or valid temporary reduction. Section 64(1)(a) also preserves separate treatment for former section 66A transitional cases and certain pre-April-2013 2% elections. Check historical employment and rate records; the member's original joining date alone does not establish a legacy 4% case. The general IRD web/KS4 default summaries omit this surviving statutory limb. [S45, subsections (1)–(2)][S45], [S49]

A valid IRD temporary rate reduction permits **3%**. The requested approval period must be **at least 92 days and no more than 1 year**; further reductions can follow. Use the actual approval's start/end dates and the notice for the relevant employer, rather than treating one employer's notification as an instruction for every job. Track expiry and any renewed approval. A person cannot use a temporary reduction whilst on a savings suspension. An informal request does not replace approval. [S39], [S46], [S47]

An employee may revoke the temporary reduction for an employer and resume the applicable ordinary/default/elected rate. Using it for fewer than **92 days requires that employer's agreement**. Retain that agreement; a request alone does not prove consent. The payroll specification's PDF page 13 sample letter says a reduction cannot end in its first 3 months, but omits the statutory agreement exception. Follow section 101S and the consistent KS4 instruction rather than implementing an absolute ban. A later reduction for that employer requires a new application. [S48], [S39], [KS4, PDF page 18][S33]

### Identify the contribution base

Classify each payment before applying a rate. The following are selected ordinary inclusions/exclusions, not a complete ruling on an actual payment. [S38], [KS4, PDF page 12][S33], [S2, section 4.5][S2]

| Payment already correctly classified | KiwiSaver gross salary or wages | Complying-fund gross base salary or wages |
|---|---|---|
| Ordinary salary, wages and overtime | Included | Included, subject to the fund's applicable definition |
| Bonus and commission | Included | Excluded |
| Redundancy payment | Excluded | Excluded |
| Board/lodging, use of a house or an allowance instead | Excluded | Excluded |
| Overseas accommodation/living-cost allowance or reimbursement within the stated exclusion | Excluded | Excluded |
| Qualifying voluntary bonding payment or employee-share-scheme shares within the stated exclusion | Excluded | Excluded |

Check the complying fund's trust deed for other excluded amounts. KiwiSaver also excludes the specified Fire and Emergency New Zealand volunteer honoraria. Keep evidence supporting an exclusion. These exclusions do not determine PAYE, FBT, ESS, employment-law or cross-border treatment. For a person contributing to both KiwiSaver and a complying fund, establish each employee deduction rate and its own base; do not silently reuse one base for both. [S38], [KS4, PDF pages 12 and 23][S33]

### Compulsory employer contributions

The ordinary minimum is 3.5% of qualifying gross salary or wages for an eligible contributing member. From 1 April 2026 this includes eligible **16- and 17-year-old members**. The ordinary conditions include age 16 to under 65, membership, required employee deductions and no disqualifying defined-benefit arrangement. Check the actual circumstances; membership alone does not establish liability. [S7], [S9]

If an employee has an approved temporary 3% deduction rate, the employer **may choose** the 3% employer rate; it need not reduce its contribution. Record its choice and any contract requiring more. The statutory CEC rate is otherwise 3.5%. Reaching 65 may end the statutory obligation, but an agreement or voluntary contribution can continue and ESCT may still apply. Use the applicable stop instruction and evidence rather than assuming a birthday cancels all contractual obligations. [S9], [S50, subsection (4)][S50]

For a person contributing to both a KiwiSaver scheme and a complying fund, the ordinary employer minimum is shared between the funds, not an additional 3.5% minimum for each. Establish the relevant bases and agreed allocation. Do not deduct an unrelated superannuation contribution as an automatic credit: section 101D's other-contribution and hybrid-scheme offsets have detailed scheme, employment/agreement and vesting conditions. Their application remains an actual-case check here. [S9], [S50]

Employer contributions are normally additional to salary or wages. An agreed total-remuneration arrangement needs a genuine agreement and must still satisfy minimum-wage requirements excluding the employer contribution. Do not reduce contracted pay automatically. Deduct ESCT from the gross employer contribution unless employer and employee have agreed to the separate PAYE treatment. The employee's own KiwiSaver deduction is not subject to ESCT. KiwiSaver employer contributions go through IRD; complying-fund contributions go directly to that fund. [S9], [S10]

Check whether an agreed employer contribution is gross or net of ESCT. A promised net contribution requires grossing up under IR335's method before the ordinary ESCT calculation. Reconcile the promised net after the required truncation; do not treat a contractual net percentage as the gross statutory minimum. This guide does not work a contractual gross-up example. [IR335, page 27][S13]

### Savings suspensions, ACC and leave

Require a valid savings-suspension notice and track its dates. An unsupported statement that the employee is on a suspension does not justify stopping deductions. Apply IRD's restart instruction when it ends. A suspension ordinarily stops required employee deductions and compulsory employer contributions, but an agreement or voluntary employer contribution can continue; apply the appropriate ESCT or agreed PAYE treatment. Approval eligibility, including early hardship applications, is not determined here. [S8], [S9], [S2, section 4.1][S2], [KS4, PDF page 18][S33]

If the employer continues paying under an ACC partnership programme or employer reimbursement agreement, continue employee KiwiSaver deductions unless a valid suspension applies; employer contributions in that situation are voluntary. When ACC pays weekly compensation directly, the employer can stop its own deductions and contributions. If the employer continues salary or wages during parental leave, continue required employee and employer contributions unless a valid suspension applies. This does not determine deductions from government parental-leave payments or leave entitlements. [S40], [S2, section 4.5.3][S2]

Contributions normally stop on unpaid leave, but the employer may contribute voluntarily. IRD's current instructions permit including the contribution in employment information with **zero gross earnings**, or paying a lump sum through IRD after the employee returns. ESCT still applies unless the agreed salary/wages treatment applies. For a voluntary $52.50 contribution with an established 30% ESCT rate, the whole-dollar base is $52, tax is $15.60 and the fund receives $36.90. The specification's page 19 table wrongly switches its tax base to $45; use the current dedicated web example and Section 4's algorithm. [S40], [S2, section 4.5.4][S2]

### Opt-outs and separate refund streams

Only an automatically enrolled employee can use the ordinary opt-out process. A timely request is made on **days 14 to 56 inclusive** after starting employment, using KS10. Send the request/details to IRD and stop deductions/contributions under the valid opt-out instruction. A voluntary joiner or existing member cannot use KS10 merely because they started a new job. A qualifying later withdrawal or KS51 stop instruction is a separate process. [S36], [KS4, PDF page 18][S33]

After day 56, IRD decides whether to accept a late request. Its stated window is up to 3 months **after IRD received the first contribution**, subject to its specified reasons; it is not a blanket 3-month extension from employment commencement. Continue employee deductions, employer contributions and ESCT until IRD's acceptance/stop instruction applies. Do not approve the late request yourself. [S37]

Reconcile each stream before refunding. If employee deductions have not been filed and paid to IRD, the employer may refund them and report the amounts actually deducted/retained. If they have already been sent, IRD refunds the employee; avoid a second employer refund. Reconcile mixed or partly forwarded amounts with IRD before acting. Employer contributions already sent are refunded to the employer subject to amounts owing to IRD. **ESCT is a separate refund request**, using the applicable IR344 amendment/contact route; do not assume an automatic employer-contribution refund also refunds ESCT. Retain the accepted request, filing amendments, employee refund and employer/ESCT reconciliation. [S36], [S2, section 5.21.5][S2]

The announced 4% ordinary default from 1 April 2028 is a future change, not the ordinary new-default rate for 2026-27 payroll. [S7]

## Section 4 -- ESCT rate and calculation

### Set the employee's rate

If the employee worked for this employer for the whole preceding tax year, use that year's salary/wages **plus gross employer superannuation contributions before ESCT**. Otherwise estimate both amounts for the **current tax year**. A part-year new starter is not automatically assigned a full 12 months of earnings beyond 31 March. Recalculate for the next tax year; ordinary salary changes during the year do not reset the rate. [S2, sections 5.20.4-5.20.5][S2]

| ESCT rate threshold amount, last whole dollar | ESCT rate |
|---|---:|
| $0 to $18,720 | 10.5% |
| $18,721 to $64,200 | 17.5% |
| $64,201 to $93,720 | 30% |
| $93,721 to $216,000 | 33% |
| $216,001 upwards | 39% |

These are single rates on the relevant employer contribution, not progressive bands applied to salary. [Income Tax Act 2007, Schedule 1 Part D][S11] says to select the band for the **last dollar** of the threshold amount. Do not round a fractional dollar up into the next band. The current technical specification reproduces the table in section 5.20.4. Defined-benefit funds and certain past-employee contributions have separate rules and are outside the ordinary case here. [S2], [S11]

### Calculate each contribution

Under [the 2026-27 specification, sections 5.20.6 and 5.21.3][S2], and [Inland Revenue's deduction instructions][S12]:

1. Calculate the gross employer contribution using dollars and cents.
2. Drop cents from that contribution to obtain the whole-dollar ESCT base. **Do not round up.**
3. Multiply that whole-dollar base by the employee's ESCT rate.
4. Truncate the tax to cents, rather than rounding it to the nearest cent.
5. Subtract that tax from the **original contribution including cents** to obtain the net employer contribution.

The September 2026 IR335 employer guide's page 27 Matthew example taxes $204.17 directly at 17.5%, despite its page 26 whole-dollar instruction. Do not copy that example's $35.73 tax. The technical algorithm and [the dedicated deduction page][S12] require a whole-dollar base; $204.17 at 17.5% gives **$35.70 ESCT and $168.47 net contribution**. This is a recorded source discrepancy, not an alternative method. [IR335, pages 26-27][S13]

## Section 5 -- Filing, remitting and records

### Employment information

File employment information for every payday using the actual pay date, not the end of the work period. Electronic filing is due within **2 working days** of payday. Allowed paper filing is due within **10 working days** of each payday, or under the permitted twice-monthly grouping within 10 working days of the 15th and month end. Filing and payment deadlines are separate; file on time even if unable to pay. [S14]

New employers may file on paper during their first 6 months. After that, electronic filing is required where annual PAYE and ESCT is **$50,000 or more**. Smaller employers can choose electronic filing. Tell Inland Revenue the required new-employee information on or before the first payday; for electronic filing this includes the employee's address and, if supplied, date of birth. Tell Inland Revenue the leaver's end date on or before their last day. Advise Inland Revenue when no wages will be paid for a month or more, including an irregular or stopped payroll. [S14], [S15]

### Paying deductions

| Gross annual PAYE and ESCT payment category | Paydays covered | Ordinary payment deadline |
|---|---|---|
| Less than $500,000 | Whole month | 20th of the following month |
| $500,000 or more | 1st to 15th | 20th of the same month |
| $500,000 or more | 16th to month end, except December | 5th of the following month |
| $500,000 or more | 16 to 31 December | **15 January** |

For established employers the large-employer test uses the preceding year's gross PAYE and ESCT. New employers pay monthly until reaching $500,000. Gross PAYE for this test includes ESCT but excludes ACC earners' levy, student loans, KiwiSaver and child support. Check connected-employer aggregation rather than treating each entity as independent. If a payment deadline falls on a weekend or public holiday, the next working day applies. [IR335, pages 71-72][S13]

The [payment web page][S16] says 'more than' $500,000, leaving equality unclear; IR335 explicitly says **$500,000 or more**. Use the latter boundary rather than classifying exactly $500,000 as a small employer. This threshold does not replace the separate $50,000 filing threshold.

Reconcile PAYE, student loans, child support, employee KiwiSaver, net employer KiwiSaver and ESCT separately before making the combined **EMP** payment. Confirm the employer account, period and reference. Other arrears notices can require a separate payment process; do not assume every withheld amount belongs in ordinary employment information or the same payment. Filing an employment-information return does not itself pay the liability. [S12], [S13], [S16]

### Correcting employment information

Identify the employee, actual payday, original filed figures, correct figures and reason for the error before choosing a correction. In myIR, amend the relevant employment-information return; add or remove the employee where needed, then check and submit the amendment declaration. **Do not resubmit the entire original return.** A file accepted with a warning is not proof that employee details or amounts are correct. From 12 September 2026, employee-details (ED) files submitted in myIR show additional warnings, which must be acknowledged before submission but can be acknowledged without first correcting the details; gateway filing is unchanged. Resolve the underlying facts rather than treating acknowledgement as validation. [S51], [S52]

The **2019 correction regulations**, consolidated as at 30 March 2026, distinguish these errors. Correct an error as soon as reasonably practicable after becoming aware of it; the notification routes below use regulation 10 and the Commissioner's applicable notification process. [S53]

| Established error | Selected correction route and limit |
|---|---|
| Payroll overpayment under regulation 4, repaid or repayable under an agreement | Notify Inland Revenue or net the relevant excess gross pay, tax, employer KiwiSaver and ESCT amounts against later employment information. Treat an agreed repayable amount as repaid for this purpose. Commissioner permission is needed if netting would produce a negative reported amount. |
| Agreement used for a correction, then breached without remedy within 2 months, or future compliance no longer expected | Revisit the correction. Regulation 4(5) requires an upwards adjustment for an established unrepaid PAYE income overpayment; amounts outside that definition use notification under 4(6). Do not leave a correction based on an agreement that has failed. |
| Other incorrect PAYE income calculation under regulation 5, or income-tax/ACC calculation under regulation 6 | Notify Inland Revenue, net an excess against a later payday, or carry a shortfall only within the conditions below. Netting that produces a negative reported amount needs Commissioner permission. |
| Independently miscalculated child support, employee/employer KiwiSaver, student loan or ESCT under regulation 7 | Notify Inland Revenue. Do not automatically use the later-payday income-tax/ACC shortfall route. Where the error arose from an incorrect income calculation, first distinguish regulations 4 and 5. |
| Reporting-only error under regulation 8 | Notify Inland Revenue, even if the pay and deduction calculations were correct. |

For the shortfall option in regulations 5(2)(c) and 6(2)(c), there must be a combined income-tax and ACC withholding shortfall **strictly less than 10%** of the employee's combined income-tax and ACC withholding for the later payday. Exclude amounts attributable to earlier paydays and to the correction itself from that comparison base. Equality at 10% does not qualify for this option; use an available notification route instead. The test is not 10% of gross wages, all deductions or the later total after adding the correction. [S53]

Regulation 4 excludes an agreed and lawful reduction of a later PAYE income payment by the overpayment under 4(8). Benefit/grant and recoverable ACC overpayments have the distinct rule in 4(9)-(10). Establish the facts and the employee's lawful repayment arrangement before applying a method; this guide does not authorise recovery from wages. Regulation 11 excludes errors attributable to the employee's failure to comply with the notified-tax-code rules. Do not treat that exclusion as permission to retain an incorrect code. [S53]

IRD's operational amendment page describes an ordinary **4-year** window from sending the original return and says older child-support amendments use IR344/contact with Inland Revenue. That is not an exhaustive account of the Commissioner's assessment powers. In the TAA copy dated 1 October 2026, section 108AC includes a student-loan exception where not amending would significantly adversely affect the borrower, as well as fraud/wilful-misleading exceptions; section 108AB deals separately with KiwiSaver increases. Section 108(1C) uses the end of the relevant return-provision period, and section 108B permits prescribed, timely waivers for listed bars. Section 113 is a Commissioner power, not an employer entitlement to make any old amendment. Refer older or exceptional cases for Inland Revenue's decision rather than automatically refusing or processing them. The general small-error thresholds in section 113A do **not** supply a PAYE shortcut: that section excludes ancillary taxes other than FBT. [S51], [S54], [S55], [S56], [S57], [S58], [S59]

### Keeping tax records

Keep wagebook information, PAYE payment records, IR330/IR330C declarations, tax-code/rate letters, relevant written agreements and exemption/tailored certificates. IR335 also lists KiwiSaver forms. Keep sufficient supporting records to explain the amounts filed and paid. [S17], [IR335, page 7][S13]

For the business tax records within **TAA section 22**, the ordinary minimum runs for **7 years after the end of the income year** to which they relate. A notice issued before that period expires may extend retention by up to 3 years for an audit, investigation or intended audit/investigation. Keep records in English or te reo Māori unless another language is approved. Keep them in New Zealand unless the taxpayer or an approved provider has the relevant authorisation; offshore cloud storage is not automatically authorised. Check the authorisation's scope and conditions. Other employment, holiday-pay, privacy, KiwiSaver and litigation requirements may use different periods or require longer retention. This is not a deletion instruction or a complete employment-records schedule. [S60], [S61]

### Filing penalties

Late employment information and an unpaid deduction are separate defaults. For employment information, the selected rules in **TAA section 139A** and IRD's current guidance provide a warning process after a clean preceding 12 months, then a further late filing within the following 12 months can attract **$250 for the month**, regardless of the number of late payday filings in that month. Check the actual warning, filing history and penalty notice. Do not import the ordinary annual-return 30-day advance warning into payday filing. The EI late-filing penalty is due **30 days after the end of the month in which the information was required**, under section 142(1A). [S62], [S63], [S64], [S65]

For non-electronic filing, first establish that electronic delivery was required and that no applicable exemption authorises another method. Section 139AA(4) sets the monthly maximum at the greater of **$250 or $1 per affected employee** whose information was not supplied in the prescribed format/manner during that month. Count the employees affected by that default, not automatically the employer's entire workforce. IR335 and the late-filing web summary abbreviate this as each person employed; the statutory affected-employee wording controls this distinction. Section 142G makes this EI penalty due 30 days after the end of the month in which the information was required. Do not multiply the monthly maximum by the number of offending payday returns. [S62], [S66], [S67]

SPS19/04 is dated 30 May 2019. Its initial education stage was expressed as transitional while payday filing was new, so this guide does not promise another education-only default in 2026. Its historical statutory appendix is not the current consolidated Act. Check an actual penalty and any available reversal/remission with Inland Revenue. [S63]

### Late payment and non-payment penalties

For an established ordinary employer PAYE tax debt, **TAA section 139B** provides an initial **1%** charge on the unpaid tax the day after the due date and a further **4%** on the remaining tax-to-pay at the specified seventh-day point. The latter base includes unpaid late-payment penalties. Incremental **1% monthly** charges can then apply on the statutory dates; determine those dates under the section rather than assuming every month has the same number of days. Payments and statutory relief can alter the base or prevent a charge. The section's unpaid-tax definition excludes both late-payment penalties and the section 141ED non-payment penalty, while its tax-to-pay definition adds unpaid late-payment penalties. Do not compound all tax, penalties and interest together. [S68], [S69]

The section 183F small-debt exemption is **$100 or less**, including exactly $100; IR335's 'less than $100' wording omits that equality. Its late-payment and interest limbs test the amount outstanding after the due date. The section's non-payment-penalty limb instead tests the unpaid amount on the day before the Commissioner's section 141ED(1)(b) notice. Those are different tests and dates. Do not infer a blanket lifetime exemption for an account that once had a $100 balance. [S70]

A good payment history is not permission to invent a later due date: the section 139B grace process requires the Commissioner's notice and its conditions. Under **section 139BA**, a qualifying relief request before default leaves the 1% initial charge but can prevent the 4% charge; a request on or after default affects incremental penalties from the request. If relief is refused or the statutory response period expires, penalties may be reinstated retrospectively. An arrangement must be complied with; merely asking for relief does not cancel tax or interest. These selected ordinary PAYE rules do not establish child-support penalties or every EMP component's separate statutory treatment. [S68], [S69], [S71]

**Section 141ED non-payment penalties** require the established statutory debt, filed employment information, non-payment and the Commissioner's warning/notice process. For the ordinary PAYE amount required under section RD 4(1), the first penalty date is the date of the Commissioner's notice itself and subsequent dates are at 1-month intervals under the section. The usual penalty is **10% of the required amount still unpaid on the day before the penalty date**. It is not 10% of the combined tax, late-payment penalties and interest. A variation or correction made from filing through the day before the penalty date changes the required-amount base. [S72]

The rate for that penalty can reduce to **5%** when payment or a qualifying instalment arrangement occurs after the penalty date and before the day that is 1 month after it, subject to the prior-agreement condition. Negotiating an instalment arrangement, a compliant arrangement made before the penalty date and specified receivership/liquidation cases have separate exceptions. The aggregate section 141ED penalty is capped at **150% of the required amount unpaid when the first penalty was imposed**. Payments are applied to the non-payment penalty before the required amount. Check the actual notices, correction, payment allocation, arrangement dates and compliance before calculating; do not automatically apply this RD 4 rule to every student-loan, KiwiSaver, child-support or ESCT balance. Non-resident cross-border exceptions and those separate streams require further checks. [S72]

Use the current Inland Revenue account and applicable interest rules/rates for any actual balance. This guide does not calculate use-of-money interest, collection costs, criminal or other shortfall penalties, or the complete remission regime. Under the selected **section 183A** reasonable-cause rule, Inland Revenue may remit listed penalties where its conditions are met, including correction as soon as practicable after a beyond-control event. Financial position alone is excluded as a reasonable-cause ground, and an agent's omission is not automatically an excuse. An application is not a favourable decision. Keep the decision and its conditions. [S73]

## Section 6 -- Conditional worked checks

These fictional cases assume the stated code, eligibility, contribution base and notices have already been established. They check the selected contribution, PAYE and student-loan arithmetic, not an actual person's liability. Cases 1 and 2 use the ordinary ESCT method rather than an agreed PAYE alternative. Set tolerance to zero so a cent error fails.

**Case 1: truncating a half-cent tax result.** Qualifying gross salary of $3,000 at 3.5% gives a $105.00 gross employer contribution. At a confirmed 17.5% ESCT rate, $18.375 truncates to **$18.37** and the fund receives **$86.63**.

```oa-check
name: nz-2026-employer-esct-half-cent
tolerance: 0
inputs:
  salary: 3000
  contribution_rate: 3.5
  esct_rate: 17.5
steps:
  gross_contribution: pct(salary, contribution_rate)
  esct_base: floor(gross_contribution)
  esct: floor(pct(esct_base, esct_rate) * 100) / 100
  net_contribution: gross_contribution - esct
expected:
  gross_contribution: 105
  esct: 18.37
  net_contribution: 86.63
```

**Case 2: retaining contribution cents.** A confirmed $204.17 gross employer contribution at 17.5% uses a $204 ESCT base. Tax is **$35.70**, leaving **$168.47**. Dropping the contribution's cents from the amount paid to the fund would also be wrong.

```oa-check
name: nz-2026-employer-esct-whole-dollar-base
tolerance: 0
inputs:
  gross_contribution: 204.17
  esct_rate: 17.5
steps:
  esct_base: floor(gross_contribution)
  esct: floor(pct(esct_base, esct_rate) * 100) / 100
  net_contribution: gross_contribution - esct
expected:
  esct_base: 204
  esct: 35.70
  net_contribution: 168.47
```

**Case 3: M monthly, annualise before dropping cents.** Confirmed ordinary M pay of $5,000.99 a month gives annual whole-dollar income $60,011. Annual tax is $10,223.80 and ACC is $1,050.1925. Weekly truncation gives $216.80, then monthly PAYE **$939.46**. Direct annual-to-monthly truncation would give $939.49 and skips the required weekly step. [S2, section 5.2][S2]

```oa-check
name: nz-2026-m-monthly-two-stage-truncation
tolerance: 0
inputs:
  period_pay: 5000.99
  pays: 12
steps:
  annual_income: floor(period_pay * pays)
  annual_tax: pct(annual_income, 30) - 7779.50
  annual_acc: pct(annual_income, 1.75)
  weekly_paye: floor((annual_tax + annual_acc) / 52 * 100) / 100
  period_paye: floor(weekly_paye * 52 / pays * 100) / 100
expected:
  annual_income: 60011
  annual_tax: 10223.80
  annual_acc: 1050.1925
  weekly_paye: 216.80
  period_paye: 939.46
```

**Case 4: M monthly with capped ACC.** Confirmed ordinary M pay of $15,000 a month annualises to $180,000. The annual ACC component is the stated **$2,741.22** maximum. PAYE including that component is **$4,334.89** a month. [S2, section 5.2][S2]

```oa-check
name: nz-2026-m-monthly-capped-acc
tolerance: 0
inputs:
  period_pay: 15000
  pays: 12
  annual_acc_cap: 2741.22
steps:
  annual_income: floor(period_pay * pays)
  annual_tax: pct(annual_income, 33) - 10122.50
  weekly_paye: floor((annual_tax + annual_acc_cap) / 52 * 100) / 100
  period_paye: floor(weekly_paye * 52 / pays * 100) / 100
expected:
  annual_income: 180000
  annual_tax: 49277.50
  weekly_paye: 1000.36
  period_paye: 4334.89
```

**Case 5: ME weekly with IETC abatement.** An employee with a confirmed ME declaration and IETC eligibility earns $1,300 weekly. Annualised income is $67,600, so the payroll credit is **$312** after abatement. Weekly PAYE including ACC and that credit is **$257.14**. This example assumes eligibility; salary alone does not establish it. [S2, section 5.3][S2], [S18]

```oa-check
name: nz-2026-me-weekly-ietc-abatement
tolerance: 0
inputs:
  period_pay: 1300
  pays: 52
steps:
  annual_income: floor(period_pay * pays)
  annual_tax: pct(annual_income, 30) - 7779.50
  annual_acc: pct(annual_income, 1.75)
  annual_credit: 520 - pct(annual_income - 66000, 13)
  period_paye: floor((annual_tax + annual_acc - annual_credit) / 52 * 100) / 100
expected:
  annual_income: 67600
  annual_tax: 12500.50
  annual_acc: 1183
  annual_credit: 312
  period_paye: 257.14
```

**Case 6: primary monthly SL near the threshold.** Ordinary M SL monthly gross pay of $2,011.99 becomes $2,011 for the loan calculation. Subtracting the **$2,010.66** threshold leaves $0.34; 12% truncated to cents is **$0.04**. There is no exemption or special-rate notice in this example. [S2, section 5.4][S2]

```oa-check
name: nz-2026-primary-sl-monthly-threshold
tolerance: 0
inputs:
  period_pay: 2011.99
  threshold: 2010.66
steps:
  loan_pay: floor(period_pay)
  loan_deduction: floor(pct(max(loan_pay - threshold, 0), 12) * 100) / 100
expected:
  loan_pay: 2011
  loan_deduction: 0.04
```

**Case 7: primary weekly SL with no positive excess.** Ordinary M SL weekly pay of $464.99 becomes $464, matching the threshold, so the loan deduction is **$0.00**. [S2, section 5.4][S2]

```oa-check
name: nz-2026-primary-sl-weekly-no-excess
tolerance: 0
inputs:
  period_pay: 464.99
  threshold: 464
steps:
  loan_pay: floor(period_pay)
  loan_deduction: floor(pct(max(loan_pay - threshold, 0), 12) * 100) / 100
expected:
  loan_pay: 464
  loan_deduction: 0
```

**Case 8: secondary SH SL has no ordinary loan threshold.** An employee's declared total annual income is $75,000 and the confirmed code for this second job is SH SL. Ordinary weekly pay of $300.99 becomes $300 for these calculations. PAYE including ACC is **$95.25** and the separate loan deduction is **$36.00**. Being below the main-job weekly threshold does not make this secondary loan deduction zero. No special rate or exemption applies here. [S2, section 5.6][S2], [S21]

```oa-check
name: nz-2026-secondary-sh-sl-no-threshold
tolerance: 0
inputs:
  period_pay: 300.99
steps:
  whole_pay: floor(period_pay)
  period_paye: floor(pct(whole_pay, 31.75) * 100) / 100
  loan_deduction: floor(pct(whole_pay, 12) * 100) / 100
expected:
  whole_pay: 300
  period_paye: 95.25
  loan_deduction: 36
```

**Case 9: ordinary ND includes ACC.** Without a completed declaration or superseding Inland Revenue instruction, ordinary ND pay of $457.89 becomes $457. The combined 46.75% deduction truncates to **$213.64**; adding ACC again overstates the deduction. [S2, section 5.8][S2]

```oa-check
name: nz-2026-nd-whole-dollar-pay
tolerance: 0
inputs:
  period_pay: 457.89
steps:
  whole_pay: floor(period_pay)
  period_paye: floor(pct(whole_pay, 46.75) * 100) / 100
expected:
  whole_pay: 457
  period_paye: 213.64
```

**Case 10: main-job tailored certificate.** Assume a valid weekly certificate requires 20% PAYE including ACC and 8% loan deductions above $464. On $1,000.99, use the $1,000 whole-dollar base: **$200.00 PAYE** and a separate **$42.88 loan deduction**. [S2, section 5.9][S2]

```oa-check
name: nz-2026-stc-primary
tolerance: 0
inputs:
  pay: 1000.99
  paye_rate: 20
  sl_rate: 8
  threshold: 464
steps:
  base: floor(pay)
  paye: floor(pct(base, paye_rate) * 100) / 100
  loan: floor(pct(base - threshold, sl_rate) * 100) / 100
expected:
  paye: 200
  loan: 42.88
```

**Case 11: secondary certificate has no threshold.** Assume a valid secondary certificate requires 18% PAYE including ACC and 8% loan deductions on every dollar. Weekly pay of $300.99 gives **$54.00 PAYE** and **$24.00 loan deductions** on $300. Do not subtract the primary $464 threshold. [S2, section 5.9][S2]

```oa-check
name: nz-2026-stc-secondary
tolerance: 0
inputs:
  pay: 300.99
  paye_rate: 18
  sl_rate: 8
steps:
  base: floor(pay)
  paye: floor(pct(base, paye_rate) * 100) / 100
  loan: floor(pct(base, sl_rate) * 100) / 100
expected:
  paye: 54
  loan: 24
```

**Case 12: one loan threshold for combined pay.** An M SL employee receives $400 regular weekly pay and $200.99 extra pay together. Combined pay truncates to $600; subtract $464 once. The total loan deduction for this pay is **$16.32**. No special certificate applies. [S2, section 5.11][S2], [S23]

```oa-check
name: nz-2026-extra-pay-single-sl-threshold
tolerance: 0
inputs:
  wages: 400
  extra: 200.99
  threshold: 464
  sl_rate: 12
steps:
  base: floor(wages + extra)
  loan: floor(pct(base - threshold, sl_rate) * 100) / 100
expected:
  base: 600
  loan: 16.32
```

**Case 13: bonus crosses the ACC cap.** An ordinary primary-code bonus of $30,000.56 follows $10,000 of regular payments in the relevant 4-week window. Annualised pay is $130,000; G is $160,000, selecting 33%. Only $26,641 of the bonus attracts 1.75% ACC. Retain $9,900.1848 tax and $466.2175 levy until the final cent truncation: **$10,366.40 PAYE**. The specification example prints $10,366.39 after prematurely shortening components; this case follows its explicit calculation sequence. [S2, section 5.11.1, PDF pages 47–48][S2], [S22]

```oa-check
name: nz-2026-bonus-crosses-acc-cap
tolerance: 0
inputs:
  prior_four_weeks: 10000
  extra: 30000.56
  cap: 156641
  tax_rate: 33
  levy_rate: 1.75
steps:
  annual: prior_four_weeks * 13
  grossed: floor(annual + extra)
  levy_base: cap - annual
  income_tax: pct(extra, tax_rate)
  levy: pct(levy_base, levy_rate)
  paye: floor((income_tax + levy) * 100) / 100
expected:
  annual: 130000
  grossed: 160000
  levy_base: 26641
  paye: 10366.4
```

**Case 14: secondary threshold affects the cap.** An ST-code bonus of $40,000 follows $4,695 regular pay in the relevant 4 weeks. Annualised pay $61,035 plus the ST low threshold $78,101 gives B of $139,136 and G of $179,136. Tax is 33% of the bonus; ACC applies to only $17,505. Total PAYE is **$13,506.33**, leaving **$26,493.67** before other deductions. [S2, section 5.11.2, PDF pages 52–55][S2], [S22]

```oa-check
name: nz-2026-secondary-bonus-cap
tolerance: 0
inputs:
  prior_four_weeks: 4695
  low_threshold: 78101
  extra: 40000
  cap: 156641
  tax_rate: 33
  levy_rate: 1.75
steps:
  annual: prior_four_weeks * 13
  base: annual + low_threshold
  grossed: floor(base + extra)
  levy_base: cap - base
  paye: floor((pct(extra, tax_rate) + pct(levy_base, levy_rate)) * 100) / 100
  net_before_other_deductions: extra - paye
expected:
  base: 139136
  grossed: 179136
  levy_base: 17505
  paye: 13506.33
  net_before_other_deductions: 26493.67
```

**Case 15: signing bonus before any regular payment.** An M-code employee receives a $10,000 levy-liable signing bonus with no earlier regular pay in the window and no higher-rate election. Annualised pay is zero, so the 10.5% income-tax rate and 1.75% levy give **$1,225.00 PAYE**. Set the low-rate extra-pay indicator. A future contractual salary is not substituted for historical payments. [S2, section 5.11.1, PDF page 49][S2], [S22]

```oa-check
name: nz-2026-signing-bonus-low-rate
tolerance: 0
inputs:
  extra: 10000
  tax_rate: 10.5
  levy_rate: 1.75
steps:
  paye: floor((pct(extra, tax_rate) + pct(extra, levy_rate)) * 100) / 100
expected:
  paye: 1225
```

**Case 16: first dollar of a new extra-pay band.** With $52,000 annualised regular pay, a $1,500 primary bonus gives G of $53,500 and **$288.75 PAYE** at 17.5% plus levy. A $1,501 bonus gives G of $53,501 and **$476.56 PAYE** at 30% plus levy. The higher rate applies to the whole bonus, not just its last dollar. [S2, section 5.11][S2], [S22]

```oa-check
name: nz-2026-extra-pay-band-boundary
tolerance: 0
inputs:
  annual: 52000
  extra_lower: 1500
  extra_upper: 1501
  lower_rate: 17.5
  upper_rate: 30
  levy_rate: 1.75
steps:
  g_lower: floor(annual + extra_lower)
  g_upper: floor(annual + extra_upper)
  paye_lower: floor((pct(extra_lower, lower_rate) + pct(extra_lower, levy_rate)) * 100) / 100
  paye_upper: floor((pct(extra_upper, upper_rate) + pct(extra_upper, levy_rate)) * 100) / 100
expected:
  g_lower: 53500
  g_upper: 53501
  paye_lower: 288.75
  paye_upper: 476.56
```

**Case 17: termination skips unpaid and current periods.** The last 2 paid weekly periods before the termination period contain $550 and $650, with an intervening unpaid week. Ignore that unpaid week and the current $500 wage. A confirmed $1,000 redundancy payment gives annualised pay $31,200 and G $32,200: **$175.00 PAYE**, with no earners' levy on redundancy. [S2, section 5.12][S2], [S24]

```oa-check
name: nz-2026-termination-paid-periods
tolerance: 0
inputs:
  paid_older: 550
  paid_recent: 650
  extra: 1000
  tax_rate: 17.5
steps:
  annual: (paid_older + paid_recent) * 26
  grossed: floor(annual + extra)
  paye: floor(pct(extra, tax_rate) * 100) / 100
expected:
  annual: 31200
  grossed: 32200
  paye: 175
```

**Case 18: termination after a frequency change.** The last 2 paid periods before termination are $800 weekly and $1,720 fortnightly. Average their annualised values to get $43,160. A separate $1,000 levy-liable bonus paid because employment ends gives G of $44,160 and **$192.50 PAYE**. Assume no secondary code or higher-rate election. [S2, section 5.12, PDF page 64][S2], [S24]

```oa-check
name: nz-2026-termination-mixed-frequencies
tolerance: 0
inputs:
  weekly: 800
  fortnightly: 1720
  extra: 1000
  tax_rate: 17.5
  levy_rate: 1.75
steps:
  annual: (weekly * 52 + fortnightly * 26) / 2
  grossed: floor(annual + extra)
  paye: floor((pct(extra, tax_rate) + pct(extra, levy_rate)) * 100) / 100
expected:
  annual: 43160
  grossed: 44160
  paye: 192.5
```

**Case 19: combined termination payments keep their levy character.** The last 2 paid monthly periods before termination are $5,500 and $7,600; ignore a later unpaid month and the current termination-period wage. A confirmed $15,000 redundancy payment and $500 ordinary bonus are paid together. Annualised pay is $78,600; G $94,100 selects 33% on all $15,500. Only the $500 bonus attracts ACC: total **$5,123.75 PAYE**, leaving **$10,376.25** before other deductions. [S2, section 5.12, PDF pages 62–63][S2], [S24]

```oa-check
name: nz-2026-combined-termination-extra-pay
tolerance: 0
inputs:
  older_month: 7600
  recent_month: 5500
  redundancy: 15000
  bonus: 500
  tax_rate: 33
  levy_rate: 1.75
steps:
  annual: (older_month + recent_month) * 6
  extra: redundancy + bonus
  grossed: floor(annual + extra)
  paye: floor((pct(extra, tax_rate) + pct(bonus, levy_rate)) * 100) / 100
  net_before_other_deductions: extra - paye
expected:
  annual: 78600
  grossed: 94100
  paye: 5123.75
  net_before_other_deductions: 10376.25
```

**Case 20: remove the levy from a tailored redundancy rate.** Assume a valid 24% salary/wage certificate rate includes 1.75% ACC and the $1,000 payment is confirmed redundancy. The applicable rate excluding levy is **22.25%**, giving **$222.50**. Mark the earnings not liable for ACC. This is conditional arithmetic, not a determination that any actual payment qualifies. [S2, section 5.11][S2]

```oa-check
name: nz-2026-tailored-redundancy-levy-exclusion
tolerance: 0
inputs:
  extra: 1000
  certificate_rate: 24
  levy_rate: 1.75
steps:
  rate_excluding_levy: certificate_rate - levy_rate
  paye: floor(pct(extra, rate_excluding_levy) * 100) / 100
expected:
  rate_excluding_levy: 22.25
  paye: 222.5
```

**Case 21: regular bonus covering 3 months.** An ordinary M-code employee earns $5,000 monthly and receives a $1,200 regular bonus covering 3 months. The $400 monthly share gives monthly PAYE of $1,066.17 on $5,400 versus $939.20 on $5,000, using the weekly-first truncation method above. The bonus PAYE is **$380.91**: 3 times the $126.97 monthly difference. Assume the same facts for the covered months and no SL code, tailored certificate or other adjustment. [S2, sections 5.1 and 5.13][S2]

```oa-check
name: nz-2026-regular-bonus-multiple-months
tolerance: 0
inputs:
  monthly_wages: 5000
  bonus: 1200
  months: 3
steps:
  share: bonus / months
  annual_base: floor(monthly_wages * 12)
  annual_with: floor((monthly_wages + share) * 12)
  tax_base: pct(annual_base, 30) - 7779.50
  tax_with: pct(annual_with, 30) - 7779.50
  weekly_base: floor(((tax_base + pct(annual_base, 1.75)) / 52) * 100) / 100
  weekly_with: floor(((tax_with + pct(annual_with, 1.75)) / 52) * 100) / 100
  paye_base: floor((weekly_base * 52 / 12) * 100) / 100
  paye_with: floor((weekly_with * 52 / 12) * 100) / 100
  bonus_paye: (paye_with - paye_base) * months
expected:
  paye_base: 939.2
  paye_with: 1066.17
  bonus_paye: 380.91
```

Before release also check an exactly $50,000 electronic-filing case, an exactly $500,000 large-employer case, the December 15 January exception and a pay period straddling 1 April. A temporary 3% employee rate does not by itself force the employer to reduce its rate.

**Case 22: primary SLCIR and separate voluntary repayment.** Assume weekly M SL pay of $875.90, a valid 5% SLCIR notice with sufficient balance and a $20 SLBOR request. Whole-dollar gross is $875; ordinary SL is $49.32, SLCIR $20.55 and SLBOR $20, totalling $89.87. [S2, section 3][S2]

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

**Case 23: primary recovery below the threshold.** Weekly M SL pay of $425.35 is below $464. Assume no different certificate: ordinary SL and SLCIR are zero. [S2, section 3][S2]

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

**Case 24: secondary recovery has no ordinary threshold.** Assume $300.99 secondary SL pay and a valid 5% recovery notice with sufficient balance. On $300 whole-dollar gross, ordinary SL is $36 and SLCIR $15. [S2, section 3][S2]

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

**Case 25: use the actual recovery percentage.** Assume weekly M SL pay of $900 and a valid notice requiring 3% above $464. Ordinary SL is $52.32 and recovery $13.08, not an assumed 5% deduction. [S2, section 3][S2]

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

**Case 26: stop at the required recovery balance.** Assume the first case has only $7 left to recover under the notice. Deduct $7 SLCIR and reconcile the completed recovery amount; do not take $20.55. [S2, section 3][S2]

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

**Case 27: child support protects the tax-only net base.** Assume ordinary weekly pay $600, PAYE including ACC $94.50, its ACC component $10.50, a $230 employee child-support notice, ordinary SL $16.32 and an eligible 3.5% KiwiSaver deduction. N is $516 and child support is $206.40. Take-home after those stated deductions is $261.78; the 60% child-support protection is not a final take-home guarantee. [S13, PDF page 24][S13], [S8]

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

**Case 28: reduce the ordinary court attachment.** Assume N=$516, prior valid child support $120 and a single ordinary court order requesting $100 with no higher minimum. The remaining court capacity is $86.40, so the court deduction must be reduced. [S27]

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

**Case 29: the order can specify a higher protected minimum.** Assume N=$500, an actual court minimum of $400, prior valid child support $80 and an ordinary court request of $100. Court capacity is $20. [S27], [S28]

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

**Case 30: court capacity cannot be negative.** Assume N=$300 and a court-order minimum of $350. The ordinary court request of $100 reduces to zero, rather than producing a negative deduction. [S27]

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

**Case 31: ordinary weekly arrears ceiling.** Assume a valid income-tax arrears notice with initial debt $3,000 requires the standard salary/wage formula, with sufficient balance. On weekly gross $900, the ceiling and required deduction are $180. This does not select the amount for a different actual notice. [S30], [S32, paragraph 28][S32]

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

**Case 32: low pay does not automatically mean a $10 deduction.** Under the same assumed standard notice and sufficient balance, weekly gross $80 gives a $16 ceiling and deduction. Do not copy the specification flowchart shortcut. [S30], [S32, paragraphs 26–27][S32]

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

**Case 33: the weekly minimum limb.** Assume the standard notice, sufficient balance and weekly gross $30. The lesser percentage limb is $6, so the weekly minimum limb gives $10. [S30], [S32, paragraph 27.2][S32]

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

**Case 34: reconcile the remaining amount required.** Assume weekly gross $900 and a fixed arrears instalment of $40, but only $5 remains required under the actual notice and no further notified interest is due. The deduction is $5, not a fresh $40 or $180 ceiling. [S30, subsection (1)][S30]

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

**Case 35: a ceiling does not replace a lower notice amount.** Assume weekly gross $900, initial debt $3,000 and a valid fixed notice requiring $40, with sufficient balance. The standard ceiling is $180; the actual required deduction remains $40. [S30, subsections (1)–(3)][S30]

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

**Case 36: scale weekly limbs once for fortnightly pay.** Assume fortnightly gross $1,800, initial debt $3,000 and the standard notice with sufficient balance. Scale the weekly debt limb and $10 minimum by 2; the 20% limb already applies to fortnightly gross. The ceiling is $360. [S32, paragraph 27.1][S32], [S30]

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

**Case 37: different contribution bases.** Assume $1,000 ordinary wages, $50 overtime, $200 bonus, $100 commission, $300 redundancy and $100 accommodation all validly classified as above. At a stated 3.5% employee rate, the KiwiSaver base is $1,350 and the complying-fund base is $1,050. The complying fund has no additional deed exclusions. These are alternative base calculations, not an instruction to enrol in both funds. [S38], [S33]

```oa-check
name: nz-2026-kiwisaver-distinct-bases
tolerance: 0
inputs:
  ordinary: 1000
  overtime: 50
  bonus: 200
  commission: 100
  redundancy: 300
  accommodation: 100
  rate: 0.035
steps:
  total_pay: ordinary + overtime + bonus + commission + redundancy + accommodation
  kiwisaver_base: total_pay - redundancy - accommodation
  complying_base: kiwisaver_base - bonus - commission
  kiwisaver_deduction: kiwisaver_base * rate
  complying_deduction: complying_base * rate
expected:
  total_pay: 1750
  kiwisaver_base: 1350
  complying_base: 1050
  kiwisaver_deduction: 47.25
  complying_deduction: 36.75
```

**Case 38: established historical default.** Assume records establish a surviving section 64(1)(ab) case for this employer/employee, with no overriding election or temporary reduction. The $1,000 KiwiSaver base produces a $40 employee deduction, not $35. The example does not infer eligibility from a joining date alone. [S45], [S49]

```oa-check
name: nz-2026-kiwisaver-legacy-default
tolerance: 0
inputs:
  base: 1000
  rate: 0.04
steps:
  employee: base * rate
expected:
  employee: 40
```

**Case 39: valid election overrides the legacy default.** For the same established historical case, assume the employer has received a valid election of 3.5% applying to this calculated payment. On a $1,000 base, deduct $35. [S45, subsections (2)–(3)][S45]

```oa-check
name: nz-2026-kiwisaver-legacy-election
tolerance: 0
inputs:
  base: 1000
  rate: 0.035
steps:
  employee: base * rate
expected:
  employee: 35
```

**Case 40: temporary reduction with unchanged employer rate.** Assume an approved 3% employee reduction applies and the employer retains 3.5%, with a shared $1,000 base and an established 17.5% ESCT rate. Employee $30, gross employer $35, ESCT $6.12 and net employer $28.88 remain separate amounts. [S9], [S50], [S12]

```oa-check
name: nz-2026-kiwisaver-trr-employer-unchanged
tolerance: 0
inputs:
  base: 1000
  employee_rate: 0.03
  employer_rate: 0.035
  esct_rate: 0.175
steps:
  employee: base * employee_rate
  employer_gross: base * employer_rate
  esct: floor(floor(employer_gross) * esct_rate * 100) / 100
  employer_net: employer_gross - esct
expected:
  employee: 30
  employer_gross: 35
  esct: 6.12
  employer_net: 28.88
```

**Case 41: employer chooses the permitted reduced rate.** Assume the same valid temporary reduction and base, but the employer chooses 3% and no agreement requires more. At 17.5% ESCT, gross employer $30 becomes $24.75 net after $5.25 ESCT. [S50], [S12]

```oa-check
name: nz-2026-kiwisaver-trr-employer-reduced
tolerance: 0
inputs:
  base: 1000
  employer_rate: 0.03
  esct_rate: 0.175
steps:
  employer_gross: base * employer_rate
  esct: floor(floor(employer_gross) * esct_rate * 100) / 100
  employer_net: employer_gross - esct
expected:
  employer_gross: 30
  esct: 5.25
  employer_net: 24.75
```

**Case 42: shared employer minimum across 2 funds.** Assume both funds qualify, each relevant base is $1,000, the ordinary minimum is 3.5% and a valid allocation contributes 2.5% to one fund and 1% to the other. Gross contributions of $25 and $10 meet the $35 aggregate minimum. This does not establish the employee deduction rates or any legacy offset. [S9], [S50]

```oa-check
name: nz-2026-kiwisaver-two-fund-minimum
tolerance: 0
inputs:
  base: 1000
  minimum_rate: 0.035
  first_rate: 0.025
  second_rate: 0.01
steps:
  minimum: base * minimum_rate
  first: base * first_rate
  second: base * second_rate
  total: first + second
  shortfall: max(0, minimum - total)
expected:
  minimum: 35
  first: 25
  second: 10
  total: 35
  shortfall: 0
```

**Case 43: voluntary unpaid-leave contribution.** Assume zero actual wages, a voluntary employer contribution of 3.5% of usual weekly pay of $1,500 and an established 30% ESCT rate. The $52.50 contribution uses a $52 ESCT base, producing $15.60 tax and $36.90 net. Usual pay is not reported as actual gross earnings. [S40], [S12]

```oa-check
name: nz-2026-kiwisaver-unpaid-leave
tolerance: 0
inputs:
  usual_pay: 1500
  contribution_rate: 0.035
  esct_rate: 0.3
steps:
  employer_gross: usual_pay * contribution_rate
  esct_base: floor(employer_gross)
  esct: floor(esct_base * esct_rate * 100) / 100
  employer_net: employer_gross - esct
expected:
  employer_gross: 52.5
  esct_base: 52
  esct: 15.6
  employer_net: 36.9
```

**Case 44: voluntary employer contribution during a suspension.** Assume an approved suspension stops required employee deductions and the employer voluntarily contributes $30. With an established 17.5% ESCT rate and no agreed PAYE treatment, tax is $5.25 and net employer contribution $24.75. Suspension does not make the voluntary contribution tax free. [S9], [S33], [S12]

```oa-check
name: nz-2026-kiwisaver-suspension-voluntary
tolerance: 0
inputs:
  employer_gross: 30
  esct_rate: 0.175
steps:
  esct: floor(floor(employer_gross) * esct_rate * 100) / 100
  employer_net: employer_gross - esct
expected:
  esct: 5.25
  employer_net: 24.75
```

**Case 45: unforwarded employee deductions refunded once.** Assume a valid timely opt-out and 2 employee deductions of $35 each, neither filed nor paid to IRD. An employer refund of $70 clears this employee-deduction balance. It does not give the employee the employer contribution or ESCT. [S36]

```oa-check
name: nz-2026-kiwisaver-optout-unforwarded
tolerance: 0
inputs:
  first: 35
  second: 35
  refund: 70
steps:
  held: first + second
  remaining: held - refund
expected:
  held: 70
  remaining: 0
```

**Case 46: reconcile employer contribution and ESCT separately.** Assume an accepted opt-out and 2 previously remitted gross employer contributions of $35, each with $6.12 ESCT and $28.88 net to the fund. The employer-side gross total $70 reconciles to $57.76 fund contributions plus $12.24 ESCT. These are separate refund/amendment streams, subject to IRD processing and debts; they are not an employee refund and no automatic ESCT refund is assumed. [S36], [S12]

```oa-check
name: nz-2026-kiwisaver-optout-employer-streams
tolerance: 0
inputs:
  count: 2
  per_contribution: 35
  per_esct: 6.12
  per_net: 28.88
steps:
  gross_total: count * per_contribution
  fund_total: count * per_net
  esct_total: count * per_esct
  reconciled: fund_total + esct_total
expected:
  gross_total: 70
  fund_total: 57.76
  esct_total: 12.24
  reconciled: 70
```

**Case 47: repaid overpayment netted without negative figures.** Assume regulation 4 applies, repayment is established and each excess amount is supported. Later ordinary gross pay is $1,000 and its correctly calculated PAYE is $180; net the $300 excess gross and $90 excess PAYE from the earlier overpayment. This is an employment-information adjustment, not a new tax-rate calculation or authority to recover wages. [S53]

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

**Case 48: shortfall below the strict carry-forward limit.** Assume regulation 6 applies and the combined later income-tax/ACC withholding, excluding earlier amounts and the correction, is $100. A $9 shortfall is below the $10 limit, leaving a $1 margin. Only on those established facts is the later-payday option available. [S53]

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

**Case 49: equality fails the shortfall option.** On the same established $100 comparison base, a $10 shortfall reaches the limit. The zero margin means it is not strictly below 10%; use the available notification route, rather than treating equality as permission to carry forward. [S53]

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

**Case 50: affected employees below the filing minimum.** Assume electronic filing was required, no exemption applies and the monthly penalty is properly imposed. Of 500 employees, only 200 have employment information supplied in the wrong format. Section 139AA uses those 200 affected employees, subject to the $250 monthly maximum calculation floor, not $500 for all staff. [S66]

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

**Case 51: affected employees above the filing minimum.** On the same established liability conditions, 300 affected employees produce a $300 monthly maximum. Additional offending payday returns do not each create another monthly maximum. [S66]

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

**Case 52: sequential late-payment bases.** Assume $10,000 ordinary PAYE tax remains wholly unpaid at each relevant date, no exemption/grace/relief applies and a statutory monthly charge date has been established. Calculate the initial 1%, the further 4% including the unpaid initial charge and then a 1% incremental charge. Exclude interest and non-payment penalties from these balances. This example does not compute calendar dates. [S68]

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

**Case 53: qualifying relief requested before default.** Assume an eligible pre-default section 139BA request, relief granted and its conditions maintained. For $10,000 unpaid tax, the initial 1% remains; the further 4% is not added in these circumstances. This does not waive interest or model refusal and retrospective reinstatement. [S71]

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

**Case 54: non-payment uses unpaid required tax.** Assume section 141ED applies after the actual warning/notice process and $10,000 is the unpaid required amount on the day before the penalty date. Separate $504 late-payment penalties do not increase this 10% base. The resulting non-payment penalty is $1,000. [S72]

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

**Case 55: timely settlement reduces that penalty.** Assume the section 141ED conditions for a reduction are satisfied, including settlement or a qualifying arrangement after the penalty date and before the day 1 month after it, with no disqualifying prior agreement. The $1,000 penalty on the same $10,000 required-amount base reduces to $500; the difference is not a reduction of tax or other charges. [S72]

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

**Case 56: aggregate non-payment cap limits the next charge.** Assume the first-penalty unpaid required amount was $10,000 and unreduced prior section 141ED penalties total $14,900. The 150% cap leaves only $100 for a proposed $1,000 next charge. Check any real correction, reduction or allocation before using this cap history. [S72]

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

**Case 57: payment pays the non-payment penalty first.** Assume $1,000 non-payment penalty and $10,000 required tax, with no competing allocations, other charges or rate reduction. Apply a $1,200 payment to the penalty first under section 141ED(5C); only $200 reduces the required tax. This isolated allocation example does not decide a live mixed-debt account. [S72]

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

**Case 58: correction before the penalty date changes the base.** Assume an accepted correction before the section 141ED penalty date reduces the required amount from $10,000 by $2,000 and nothing has been paid. The applicable ordinary 10% penalty uses the corrected $8,000 base, not the original filing. Actual notice, timing, correction and any exemption remain required inputs. [S72]

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

**Case 59: a positive share-settled benefit.** Assume an established CE 2 benefit with market value $24,000, consideration paid $6,000, no consideration received or historic previous income, valid withholding and a derived 33% extra-pay rate. The benefit is $18,000 and income-tax withholding is $5,940, with no ACC or KiwiSaver on that benefit. This does not verify the market valuation or taxing date. [S74], [S79]

```oa-check
name: nz-2026-ess-share-value
tolerance: 0.001
inputs:
  share_value: 24000
  consideration_paid: 6000
  consideration_received: 0
  previous_income: 0
steps:
  benefit: share_value - consideration_paid + consideration_received - previous_income
  income_tax: benefit * 0.33
expected:
  benefit: 18000
  income_tax: 5940
```

**Case 60: cancellation uses consideration received.** Assume cancellation triggers the taxing date, $15,000 is paid for the rights and $2,000 was paid for them, with no previous income. Share value in this formula is zero; do not add another $15,000 market value. At an established 33% extra-pay rate the $13,000 benefit has $4,290 income tax. [S75], [S79]

```oa-check
name: nz-2026-ess-cancellation-value
tolerance: 0.001
inputs:
  share_value: 0
  consideration_paid: 2000
  consideration_received: 15000
  previous_income: 0
steps:
  benefit: share_value - consideration_paid + consideration_received - previous_income
  income_tax: benefit * 0.33
expected:
  benefit: 13000
  income_tax: 4290
```

**Case 61: a negative formula is preserved for review.** Assume the statutory formula has share value $1,000, consideration paid $2,000 and no other items. The result is negative $1,000, within CE 2(3)'s deduction rule. This arithmetic does not authorise a negative employment-information payment, offset or payroll refund. [S79]

```oa-check
name: nz-2026-ess-negative-formula
tolerance: 0.001
inputs:
  share_value: 1000
  consideration_paid: 2000
  consideration_received: 0
  previous_income: 0
steps:
  formula_result: share_value - consideration_paid + consideration_received - previous_income
expected:
  formula_result: -1000
```

**Case 62: genuine cash settlement with the loan threshold already used.** Assume a $5,000 genuine cash-settled benefit, ordinary 30% extra-pay income-tax rate, required SL deductions and no remaining primary threshold or special certificate. Income tax is $1,500, student loan $600 and net cash $2,900. No ACC, employee KiwiSaver or employer KiwiSaver applies to this benefit. The classification is an input, not established by the calculation. [S74], [S75], [S84], [S88]

```oa-check
name: nz-2026-ess-cash-with-loan
tolerance: 0.001
inputs:
  benefit: 5000
steps:
  income_tax: benefit * 0.30
  student_loan: floor(benefit) * 0.12
  net_cash: benefit - income_tax - student_loan
expected:
  income_tax: 1500
  student_loan: 600
  net_cash: 2900
```

**Case 63: employee-funded withholding creates no employer bonus.** Assume the same $5,000 value is provided in shares, with valid withholding, a 30% rate and SL on the full amount. The employee agrees to fund the $1,500 tax and $600 loan deduction from their own resources. Required funding is $2,100; it is not an additional employer-funded gross payment. No share sale, wage deduction or sufficient cash balance is proved here. [S74], [S76], [S77]

```oa-check
name: nz-2026-ess-employee-funded-withholding
tolerance: 0.001
inputs:
  benefit: 5000
steps:
  income_tax: benefit * 0.30
  student_loan: floor(benefit) * 0.12
  employee_funding: income_tax + student_loan
expected:
  income_tax: 1500
  student_loan: 600
  employee_funding: 2100
```

**Case 64: primary student loan uses only the remaining threshold.** Assume a weekly M SL employee, ordinary pay $300, $464 threshold, no other extra pay or certificate and a $1,000 genuine cash ESS benefit in that pay period. Ordinary four-week pay of $1,200 gives annualised base $15,600, so the extra-pay income-tax rate is 17.5%. Only $164 of threshold remains for the ESS benefit. Income tax is $175, loan $100.32 and net benefit cash $724.68. The regular pay itself has no standard loan deduction. [S2], [S24], [S74], [S84], [S88]

```oa-check
name: nz-2026-ess-main-loan-remaining-threshold
tolerance: 0.001
inputs:
  regular_pay: 300
  weekly_threshold: 464
  benefit: 1000
steps:
  remaining_threshold: max(0, weekly_threshold - regular_pay)
  loan_base: floor(max(0, benefit - remaining_threshold))
  student_loan: loan_base * 0.12
  income_tax: benefit * 0.175
  net_cash: benefit - income_tax - student_loan
expected:
  remaining_threshold: 164
  loan_base: 836
  student_loan: 100.32
  income_tax: 175
  net_cash: 724.68
```

**Case 65: secondary student loan has no threshold.** Assume an S SL employee with derived extra-pay income-tax rate 17.5%, a $1,000 genuine cash ESS benefit and no special certificate. Withhold $175 income tax and $120 loan, leaving $705. Do not subtract the primary weekly threshold from this secondary payment. [S2], [S24], [S74], [S84], [S88]

```oa-check
name: nz-2026-ess-secondary-loan-no-threshold
tolerance: 0.001
inputs:
  benefit: 1000
steps:
  income_tax: benefit * 0.175
  student_loan: floor(benefit) * 0.12
  net_cash: benefit - income_tax - student_loan
expected:
  income_tax: 175
  student_loan: 120
  net_cash: 705
```

**Case 66: the funding payment attracts ACC.** Assume a $4,550 share benefit, valid withholding and an employer agreement to fund its tax and the tax/ACC on the additional payment. Annualised base is $60,000, so the benefit plus the $2,000 funding gross stays in the 30% band and below the ACC cap. There is no SL, KiwiSaver membership or employer contribution obligation. The ESS tax is $1,365. Grossing that funding amount up for 30% tax and 1.75% ACC gives $2,000, including $600 tax and $35 ACC, leaving $1,365 to fund the ESS tax. The benefit remains $4,550 in the ESS field; the $2,000 is separate gross earnings. [S2], [S24], [S74], [S76], [S85]

```oa-check
name: nz-2026-ess-funded-tax-acc-separate
tolerance: 0.001
inputs:
  benefit: 4550
  annualised_base: 60000
steps:
  ess_tax: benefit * 0.30
  funding_gross: ess_tax / (1 - 0.30 - 0.0175)
  funding_tax: funding_gross * 0.30
  funding_acc: funding_gross * 0.0175
  funding_net: funding_gross - funding_tax - funding_acc
  rate_comparison_total: annualised_base + benefit + funding_gross
expected:
  ess_tax: 1365
  funding_gross: 2000
  funding_tax: 600
  funding_acc: 35
  funding_net: 1365
  rate_comparison_total: 66550
```

**Case 67: funding income tax, loan and employee KiwiSaver.** Assume a $9,800 share benefit and valid withholding, annualised base $160,000, ordinary 33% income-tax rate, required 12% SL with the primary threshold already used and a valid 6% employee KiwiSaver instruction. The employer funds both benefit deductions and all applicable deductions on the additional payment. The $9,000 additional gross keeps the combined rate comparison at $178,800, within 33%; ACC is zero because the established annualised base already exceeds $156,641. ESS tax $3,234 plus loan $1,176 needs $4,410 funding. The additional gross has $2,970 tax, $1,080 loan and $540 employee KiwiSaver, leaving $4,410. A separately established 3.5% compulsory employer contribution on that additional gross is $315 before its own ESCT; none is due on the ESS benefit. [S2], [S24], [S74], [S76], [S88]

```oa-check
name: nz-2026-ess-all-deductions-funded
tolerance: 0.001
inputs:
  benefit: 9800
  annualised_base: 160000
  employee_kiwisaver_rate: 0.06
  employer_rate: 0.035
steps:
  ess_tax: benefit * 0.33
  ess_loan: floor(benefit) * 0.12
  net_funding: ess_tax + ess_loan
  funding_gross: net_funding / (1 - 0.33 - 0.12 - employee_kiwisaver_rate)
  funding_tax: funding_gross * 0.33
  funding_loan: floor(funding_gross) * 0.12
  employee_kiwisaver: funding_gross * employee_kiwisaver_rate
  funding_net: funding_gross - funding_tax - funding_loan - employee_kiwisaver
  employer_gross: funding_gross * employer_rate
  rate_comparison_total: annualised_base + benefit + funding_gross
expected:
  ess_tax: 3234
  ess_loan: 1176
  net_funding: 4410
  funding_gross: 9000
  funding_tax: 2970
  funding_loan: 1080
  employee_kiwisaver: 540
  funding_net: 4410
  employer_gross: 315
  rate_comparison_total: 178800
```

**Case 68: tax-only funding above the ACC cap.** Assume annualised base $200,000, an established $6,100 share benefit, valid withholding and an employer agreement to fund all income tax. There is no SL or KiwiSaver obligation and no ACC on the additional payment at this established base. The 39% benefit tax is $2,379; a separate gross payment of $3,900 has $1,521 tax and leaves $2,379. The gross-up applies to the funding payment, not to $6,100 of share value. [S2], [S24], [S74], [S76]

```oa-check
name: nz-2026-ess-tax-only-above-acc-cap
tolerance: 0.001
inputs:
  benefit: 6100
steps:
  ess_tax: benefit * 0.39
  funding_gross: ess_tax / (1 - 0.39)
  funding_tax: funding_gross * 0.39
  funding_net: funding_gross - funding_tax
expected:
  ess_tax: 2379
  funding_gross: 3900
  funding_tax: 1521
  funding_net: 2379
```

**Case 69: NSW ordinary pay with cents.** Assume a valid NSW code, $457.89 weekly ordinary taxable pay, no exceptional levy adjustment and no other deduction. Whole-dollar pay is $457; $55.9825 truncates to $55.98 PAYE, leaving $401.91 of actual pay. [S2], [S13], [S92]

```oa-check
name: nz-2026-nsw-ordinary-fractional
tolerance: 0
inputs:
  gross_pay: 457.89
steps:
  whole_dollar_pay: floor(gross_pay)
  untruncated_paye: whole_dollar_pay * 0.1225
  paye: floor(untruncated_paye * 100) / 100
  net_pay: gross_pay - paye
expected:
  whole_dollar_pay: 457
  untruncated_paye: 55.9825
  paye: 55.98
  net_pay: 401.91
```

**Case 70: NSW fortnightly flat calculation.** Assume a valid NSW code and $2,000.99 fortnightly ordinary taxable pay with no other deduction or exceptional adjustment. Apply the same flat method to $2,000; do not annualise or multiply a weekly deduction. PAYE is $245 and ordinary net pay is $1,755.99. [S2], [S13], [S92]

```oa-check
name: nz-2026-nsw-fortnightly-flat
tolerance: 0
inputs:
  gross_pay: 2000.99
steps:
  whole_dollar_pay: floor(gross_pay)
  untruncated_paye: whole_dollar_pay * 0.1225
  paye: floor(untruncated_paye * 100) / 100
  net_pay: gross_pay - paye
expected:
  whole_dollar_pay: 2000
  untruncated_paye: 245
  paye: 245
  net_pay: 1755.99
```

**Case 71: RSE first-month NSW exception.** Assume the worker is within the statutory first month of an established RSE period of employment, has not yet supplied IR330 and is entitled to the clause 3 NSW exception. On $1,000.99 ordinary weekly pay, PAYE is $122.50 and net pay before any other deduction is $878.49. The arithmetic assumes the exception; it does not establish its start or end date. [S2], [S94], [S95], [S97]

```oa-check
name: nz-2026-rse-first-month-nsw
tolerance: 0
inputs:
  gross_pay: 1000.99
steps:
  whole_dollar_pay: floor(gross_pay)
  untruncated_paye: whole_dollar_pay * 0.1225
  paye: floor(untruncated_paye * 100) / 100
  net_pay: gross_pay - paye
expected:
  whole_dollar_pay: 1000
  untruncated_paye: 122.5
  paye: 122.5
  net_pay: 878.49
```

**Case 72: ND after the RSE exception ends.** Assume that first-month exception has ended, the ordinary section 24E non-notified conditions are established, no applicable Commissioner code exists and the worker still has not supplied the required notification. On $1,000.99 ordinary weekly pay, the ND method gives $467.50 PAYE and $533.49 before other deductions. A properly notified continuing NSW worker would not use this case. [S2], [S95], [S97]

```oa-check
name: nz-2026-rse-post-exception-nd
tolerance: 0
inputs:
  gross_pay: 1000.99
steps:
  whole_dollar_pay: floor(gross_pay)
  untruncated_paye: whole_dollar_pay * 0.4675
  paye: floor(untruncated_paye * 100) / 100
  net_pay: gross_pay - paye
expected:
  whole_dollar_pay: 1000
  untruncated_paye: 467.5
  paye: 467.5
  net_pay: 533.49
```

**Case 73: CAE ordinary allowances and separate extra pay.** Assume valid CAE employment, $400.37 ordinary wages, $57.52 taxable allowances, $20 non-taxable allowances and a separately classified $100 extra payment. Ordinary taxable pay is $457.89, truncated to $457; ordinary PAYE is $87.97. The ordinary cash component is $477.89, leaving $389.92 before any other deduction. The $100 extra pay and its deductions must be calculated separately and are excluded from this result; assume no KiwiSaver contribution is due on these established facts. [S2], [S13], [S92]

```oa-check
name: nz-2026-cae-ordinary-allowance-base
tolerance: 0
inputs:
  wages: 400.37
  taxable_allowance: 57.52
  non_taxable_allowance: 20
  separate_extra_pay: 100
steps:
  ordinary_taxable_pay: wages + taxable_allowance
  whole_dollar_pay: floor(ordinary_taxable_pay)
  untruncated_paye: whole_dollar_pay * 0.1925
  paye: floor(untruncated_paye * 100) / 100
  ordinary_cash: ordinary_taxable_pay + non_taxable_allowance
  ordinary_net: ordinary_cash - paye
expected:
  ordinary_taxable_pay: 457.89
  whole_dollar_pay: 457
  untruncated_paye: 87.9725
  paye: 87.97
  ordinary_cash: 477.89
  ordinary_net: 389.92
```

**Case 74: EDW ordinary pay.** Assume qualifying election work within the permitted period, a valid EDW code, $1,000.99 ordinary weekly pay, no KiwiSaver contribution due on the established facts and no other deduction or exceptional adjustment. Whole-dollar pay is $1,000, PAYE is $192.50 and net pay is $808.49. Work outside the qualifying election period needs the appropriate ordinary declaration. [S2], [S13], [S92]

```oa-check
name: nz-2026-edw-ordinary-flat
tolerance: 0
inputs:
  gross_pay: 1000.99
steps:
  whole_dollar_pay: floor(gross_pay)
  untruncated_paye: whole_dollar_pay * 0.1925
  paye: floor(untruncated_paye * 100) / 100
  net_pay: gross_pay - paye
expected:
  whole_dollar_pay: 1000
  untruncated_paye: 192.5
  paye: 192.5
  net_pay: 808.49
```

**Case 75: modern exempt ESS at both amount limits.** Assume a qualifying post-1 April 2025 offer in the current income year, an established relevant 12-month cap period, market value of $7,500 and voluntary employee spending of $4,500 across all purchases in that period. The discount is $3,000, with no headroom in either limit. A qualifying interest/charge-free $4,500 loan over 36 monthly payments is $125 a month before any statutory leave suspension, assuming equal payments; CW 26C(4)(d) requires regular instalments of a month or less, not equal ones. Assume every other scheme and receipt condition is satisfied; these amounts alone do not prove exemption. [S101], [S107]

```oa-check
name: nz-2026-exempt-ess-exact-limits
tolerance: 0
inputs:
  market_value: 7500
  employee_cost: 4500
  value_limit: 7500
  discount_limit: 3000
  loan_months: 36
steps:
  discount: market_value - employee_cost
  value_headroom: value_limit - market_value
  discount_headroom: discount_limit - discount
  monthly_payment: employee_cost / loan_months
expected:
  discount: 3000
  value_headroom: 0
  discount_headroom: 0
  monthly_payment: 125
```

**Case 76: share-value limit exceeded by a cent.** Under the same modern offer/period assumptions, total share value is $7,500.01 and employee cost is $4,500.01. The $3,000 discount meets its limit, but share value exceeds its separate limit by $0.01. Do not accept the arrangement on the discount test alone. The tax consequences of failed exemption require separate review. [S101], [S107]

```oa-check
name: nz-2026-exempt-ess-value-excess
tolerance: 0
inputs:
  market_value: 7500.01
  employee_cost: 4500.01
  value_limit: 7500
steps:
  discount: market_value - employee_cost
  value_excess: market_value - value_limit
expected:
  discount: 3000
  value_excess: 0.01
```

**Case 77: discount limit exceeded by a cent.** Under the same modern offer/period assumptions, total share value is $7,500 and employee cost is $4,499.99. Value meets its limit, but the $3,000.01 discount exceeds its separate limit by $0.01. Do not treat the value test as sufficient. [S101], [S107]

```oa-check
name: nz-2026-exempt-ess-discount-excess
tolerance: 0
inputs:
  market_value: 7500
  employee_cost: 4499.99
  discount_limit: 3000
steps:
  discount: market_value - employee_cost
  discount_excess: discount - discount_limit
expected:
  discount: 3000.01
  discount_excess: 0.01
```

**Case 78: associated holdings reach the exclusion.** Assume the employee holds 8% and a separately established associated person holds 2% of issued capital, without overlap. The combined holding is exactly 10%, so CW 26D excludes this person. This calculation does not establish association or ownership facts. [S102]

```oa-check
name: nz-2026-exempt-ess-associated-holding
tolerance: 0
inputs:
  employee_percent: 8
  associate_percent: 2
  exclusion_percent: 10
steps:
  combined_percent: employee_percent + associate_percent
  margin_to_exclusion: exclusion_percent - combined_percent
expected:
  combined_percent: 10
  margin_to_exclusion: 0
```

**Case 79: statutory equal-participation pool.** For a particular full-time permanent offeree, assume the legally established pool of other full-time permanent employees is 110, of whom 10 have offers subject to foreign security disclosure rules. Of the remaining 100, 90 are eligible on an equal basis. That is exactly 90%. This conditional pool calculation does not prove the scheme-wide test for every offeree or the separate part-time/seasonal tests. [S101]

```oa-check
name: nz-2026-exempt-ess-other-employee-pool
tolerance: 0
inputs:
  other_employees: 110
  foreign_disclosure: 10
  equal_eligible: 90
steps:
  comparison_pool: other_employees - foreign_disclosure
  eligible_percent: equal_eligible / comparison_pool * 100
expected:
  comparison_pool: 100
  eligible_percent: 90
```

**Case 80: discounted shares and actual group employment end.** Assume discounted shares, a 48-month loan repayment period and actual employment ending 24 months after acquisition, including any same-group employment following transfer. The restriction is the shorter of 48 months (the longer of 36 and 48) and 24 months, hence 24 months. The applicable exit/transfer/buyback rule still needs separate application. [S101, subsections (7)–(9)][S101]

```oa-check
name: nz-2026-exempt-ess-employment-end-restriction
tolerance: 0
inputs:
  three_year_months: 36
  loan_period_months: 48
  employment_end_months: 24
steps:
  longer_period: max(three_year_months, loan_period_months)
  restriction_months: min(longer_period, employment_end_months)
expected:
  longer_period: 48
  restriction_months: 24
```

**Case 81: early repayment does not remove the 3-year limb.** Assume discounted shares, a 36-month loan paid off voluntarily after 12 months, continuing qualifying employment until month 60 and no other exception. Even using the actual 12-month repayment period, the longer-of test retains 36 months; restriction ends at month 36 on these facts. This does not determine the effect of leave extensions or different loan terms. [S101]

```oa-check
name: nz-2026-exempt-ess-early-repayment
tolerance: 0
inputs:
  three_year_months: 36
  actual_repayment_months: 12
  employment_end_months: 60
steps:
  longer_period: max(three_year_months, actual_repayment_months)
  restriction_months: min(longer_period, employment_end_months)
expected:
  longer_period: 36
  restriction_months: 36
```

**Case 82: ordinary and qualifying hardship withdrawal prices.** Assume employee cost of $4,500, withdrawal-day market value of $6,000 and a $1,000 outstanding loan. An ordinary withdrawal with the required notice gives a $4,500 buyback and $3,500 after loan repayment. A separately established serious-hardship withdrawal with the employee agreement required by subsection (5) gives a $6,000 buyback and $5,000 after repayment. These are alternative established cases, not an employee election to claim the higher price without hardship. [S101]

```oa-check
name: nz-2026-exempt-ess-withdrawal-prices
tolerance: 0
inputs:
  employee_cost: 4500
  market_value: 6000
  loan_balance: 1000
steps:
  ordinary_price: min(employee_cost, market_value)
  ordinary_after_loan: ordinary_price - loan_balance
  hardship_price: market_value
  hardship_after_loan: hardship_price - loan_balance
expected:
  ordinary_price: 4500
  ordinary_after_loan: 3500
  hardship_price: 6000
  hardship_after_loan: 5000
```

**Case 83: annual exempt scheme aggregates.** Assume 3 distinct employee recipients in the established tax-year reporting period, shares granted with total values of $7,500, $5,000 and $3,000, and respective employee contributions of $4,500, $3,000 and $1,000. IR1212 reports $15,500 share value, $8,500 contributions and 3 recipients. The $7,000 aggregate difference is a reconciliation amount, not a per-person discount allowance or an ordinary EI amount. Assume all individual eligibility and other scheme conditions have been independently established. [S106], [S111]

```oa-check
name: nz-2026-exempt-ess-annual-aggregates
tolerance: 0
inputs:
  shares_a: 7500
  shares_b: 5000
  shares_c: 3000
  contributions_a: 4500
  contributions_b: 3000
  contributions_c: 1000
  distinct_recipients: 3
steps:
  shares_total: shares_a + shares_b + shares_c
  contributions_total: contributions_a + contributions_b + contributions_c
  aggregate_difference: shares_total - contributions_total
  recipient_count: distinct_recipients
expected:
  shares_total: 15500
  contributions_total: 8500
  aggregate_difference: 7000
  recipient_count: 3
```

## Section 7 -- Limits and sources

Still requiring separate actual-case checks: special PAYE codes beyond the selected ordinary NSW/CAE/EDW, certificate and extra-pay methods; exemption eligibility, recovery notices beyond the selected methods, other irregular pays and unresolved competing-notice/attachment cases; actual ESS scheme eligibility and receipt failures, legacy approvals and historic transitions, difficult valuations, replacement schemes and classification beyond the selected employee methods; schedular payments and payment classification; enrolment exceptions and mixed/late refund cases beyond the selected administration; historical-rate evidence, contribution classifications and legacy scheme offsets; cross-border employment and treaty/social-security questions; FBT; leave, holiday pay, minimum wage and termination entitlements; employer ACC invoices; employment-record requirements beyond selected tax retention; older/exceptional corrections, mixed EMP debt, current interest, other shortfall/criminal penalties and full remission/collection rules. No whole payroll, social-contribution or compliance topic is certified complete by this guide. It remains tier 2 and pending qualified review.

Inherited sources checked 12 November 2026; selected ESS sources checked 13 November 2026. Selected District Court Act sections use the current copy dated 17 February 2026; Tax Administration Act section 157 uses the current copy dated 1 October 2026. SPS 21/01 is dated 12 April 2021 and remains linked by IRD's arrears page updated 16 April 2026. Extra-pay and deduction examples are recalculated from the stated rules; known inconsistent printed examples and boundary wording are recorded in the verification log. The technical specification is dated 24 March 2026, version 1.0, and expressly covers 1 April 2026 to 31 March 2027. IR335's cover says September 2026. KS4's cover says April 2026. Selected KiwiSaver Act provisions use the current copy dated 1 April 2026. The verification log records the selected native/image page scope, the surviving legacy default and conflicting sample-letter/example wording. The selected correction regulations use the 30 March 2026 consolidation. Selected TAA record, assessment and penalty provisions use the 1 October 2026 copy. Its full-Act page flags unincorporated amendments; the selected amendment-impact check is recorded in the verification log. SPS19/04 is dated 30 May 2019. Current statutory wording controls the affected-employee penalty base and inclusive $100 exemption. These checks do not claim full PDF or statute review.

[S1]: https://www.ird.govt.nz/deductions "Salary and wage deductions"
[S2]: https://www.ird.govt.nz/-/media/project/ir/home/documents/digital-service-providers/software-providers/payroll-calculations-business-rules-specifications/payroll-calculations-and-business-rules-specification.pdf?modified=20260401012317 "2026-27 payroll specification, selected sections"
[S3]: https://www.ird.govt.nz/setting-up-a-business-or-organisation "Registering as an employer"
[S4]: https://www.ird.govt.nz/employing-staff/deductions-from-income "Deductions from income"
[S5]: https://www.ird.govt.nz/income-tax/income-tax-for-individuals/acc-clients-and-carers/acc-earners-levy-rates "ACC earners' levy rates"
[S6]: https://www.acc.co.nz/for-business/understanding-levies-if-you-work-or-own-a-business "Levy responsibilities; not the source for dated rates"
[S7]: https://www.ird.govt.nz/kiwisaver-changes "KiwiSaver changes"
[S8]: https://www.ird.govt.nz/kiwisaver/kiwisaver-for-employers/contributions-and-deductions/kiwisaver-deductions-from-employee-pay "Employee KiwiSaver deductions"
[S9]: https://www.ird.govt.nz/kiwisaver/kiwisaver-for-employers/contributions-and-deductions/employer-contributions-to-kiwisaver-and-complying-funds "Employer contributions"
[S10]: https://www.ird.govt.nz/esct "ESCT scope and methods"
[S11]: https://www.legislation.govt.nz/act/public/2007/97/en/latest/parts/DLM1523173/ "Income Tax Act 2007, Schedule 1 Part D, current copy dated 4 September 2026"
[S12]: https://www.ird.govt.nz/employing-staff/deductions-from-income/employer-superannuation-contribution-tax/deduct-esct-from-each-employer-contribution "Deducting ESCT"
[S13]: https://www.ird.govt.nz/-/media/project/ir/home/documents/forms-and-guides/ir300---ir399/ir335/ir335.pdf?modified=20250811232131 "IR335 employer guide, September 2026, selected pages"
[S14]: https://www.ird.govt.nz/payday "Payday filing"
[S15]: https://www.ird.govt.nz/employing-staff/payday-filing/filing-employment-information-electronically "Electronic employment information"
[S16]: https://www.ird.govt.nz/employing-staff/payday-filing/paying-deductions-to-inland-revenue "Paying deductions"
[S17]: https://www.ird.govt.nz/employing-staff/deductions-from-income/paye-records "PAYE records"

[S18]: https://www.ird.govt.nz/income-tax/income-tax-for-individuals/individual-tax-credits/independent-earner-tax-credit-ietc "ietc-eligibility"
[S19]: https://www.ird.govt.nz/income-tax/income-tax-for-individuals/individual-tax-credits/independent-earner-tax-credit-ietc/getting-the-independent-earner-tax-credit-if-you-earn-salary-or-wages "ietc-salary"
[S20]: https://www.ird.govt.nz/income-tax/income-tax-for-individuals/tax-codes-and-tax-rates-for-individuals/about-tax-codes "about-tax-codes"
[S21]: https://www.ird.govt.nz/repaying-my-student-loan-when-i-earn-salary-or-wages "student-loan-salary"

[S22]: https://www.ird.govt.nz/calculate-lump-sum-paye "Non-termination lump-sum PAYE, updated 18 May 2026"
[S23]: https://www.ird.govt.nz/employing-staff/payday-filing/non-standard-filing-of-employment-information/lump-sum-payments "Lump-sum deductions and reporting, updated 27 January 2026"
[S24]: https://www.ird.govt.nz/employing-staff/payday-filing/non-standard-filing-of-employment-information/lump-sum-payments/calculate-paye-for-a-lump-sum-payment-end-of-employment "End-of-employment lump-sum PAYE, updated 20 April 2026"

[S25]: https://www.ird.govt.nz/student-loans/living-in-new-zealand-with-a-student-loan/repaying-my-student-loan-when-i-earn-salary-or-wages/student-loan-underpayments "Student-loan underpayments, updated 3 April 2024; dated specification supplies 2026-27 period"
[S26]: https://www.ird.govt.nz/employing-staff/deductions-from-income/deduction-notices-collecting-taxes-from-taxpayers-who-refuse-to-pay "IRD deduction notices, updated 16 April 2026"
[S27]: https://www.legislation.govt.nz/act/public/2016/49/en/latest/sections/DLM6942502/ "District Court Act 2016, section 157, as at 17 February 2026"
[S28]: https://www.legislation.govt.nz/act/public/2016/49/en/latest/sections/DLM6942500/ "District Court Act 2016, section 156, as at 17 February 2026"
[S29]: https://www.legislation.govt.nz/act/public/2016/49/en/latest/sections/DLM6942492/ "District Court Act 2016, section 154, as at 17 February 2026"
[S30]: https://www.legislation.govt.nz/act/public/1994/166/en/latest/sections/DLM356984/ "Tax Administration Act 1994, section 157, as at 1 October 2026"
[S31]: https://www.taxtechnical.ird.govt.nz/standard-practice-statements/processing/sps-21-01 "SPS 21/01 issuer index, issued 12 April 2021"
[S32]: https://www.taxtechnical.ird.govt.nz/-/media/project/ir/tt/pdfs/standard-practice-statements/processing/sps-21-01.pdf?modified=20210420044632 "SPS 21/01 Deduction notices, paragraphs 26–36, 12 April 2021"

[S33]: https://www.ird.govt.nz/-/media/project/ir/home/documents/forms-and-guides/ir1---ir99/ks4/ks4.pdf?modified=20260129195326 "KS4 employer guide, cover April 2026, selected pages"
[S34]: https://www.ird.govt.nz/kiwisaver/kiwisaver-for-employers/starting-employees-in-kiwisaver "Starting employees, updated 21 October 2026"
[S35]: https://www.ird.govt.nz/kiwisaver/kiwisaver-for-employers/starting-employees-in-kiwisaver/auto-enrol-employees-into-kiwisaver "Automatic enrolment, updated 21 October 2026"
[S36]: https://www.ird.govt.nz/kiwisaver/kiwisaver-employers/employees-who-want-to-opt-out-of-kiwisaver "Employee opt-outs, updated 28 July 2026"
[S37]: https://www.ird.govt.nz/kiwisaver/kiwisaver-employers/employees-who-want-to-opt-out-of-kiwisaver/employees-who-opt-out-late-from-kiwisaver "Late opt-outs, updated 28 April 2021"
[S38]: https://www.ird.govt.nz/kiwisaver/kiwisaver-employers/contributions-and-deductions/gross-pay-for-kiwisaver-and-complying-funds "KiwiSaver and complying-fund gross pay, updated 28 April 2021"
[S39]: https://www.ird.govt.nz/kiwisaver/kiwisaver-individuals/making-changes-to-my-kiwisaver/changing-my-kiwisaver-contribution-rate/temporary-rate-reduction "Temporary rate reduction, updated 1 April 2026"
[S40]: https://www.ird.govt.nz/kiwisaver/kiwisaver-employers/contributions-and-deductions/employees-with-special-circumstances "Special employee circumstances, updated 1 October 2026"
[S41]: https://www.legislation.govt.nz/act/public/2006/40/en/latest/sections/DLM378821/ "6 Application, current copy 1 April 2026"
[S42]: https://www.legislation.govt.nz/act/public/2006/40/en/latest/sections/DLM378830/ "10 Who automatic enrolment rules apply to, current copy 1 April 2026"
[S43]: https://www.legislation.govt.nz/act/public/2006/40/en/latest/sections/DLM378834/ "12 Temporary employment, current copy 1 April 2026"
[S44]: https://www.legislation.govt.nz/act/public/2006/40/en/latest/sections/DLM378843/ "14 Other situations when automatic enrolment rules do not apply, current copy 1 April 2026"
[S45]: https://www.legislation.govt.nz/act/public/2006/40/en/latest/sections/DLM379037/ "64 Contribution rate, current copy 1 April 2026"
[S46]: https://www.legislation.govt.nz/act/public/2006/40/en/latest/sections/LMS1569986/ "101L How to apply for rate reduction, current copy 1 April 2026"
[S47]: https://www.legislation.govt.nz/act/public/2006/40/en/latest/sections/LMS1569987/ "101M Grant of rate reduction, current copy 1 April 2026"
[S48]: https://www.legislation.govt.nz/act/public/2006/40/en/latest/sections/LMS1569995/ "101S Revocation of rate reduction, current copy 1 April 2026"
[S49]: https://www.legislation.govt.nz/act/public/2006/40/en/latest/sections/DLM379032/ "KiwiSaver Act section 60, current copy 1 April 2026"
[S50]: https://www.legislation.govt.nz/act/public/2006/40/en/latest/sections/DLM1233474/ "KiwiSaver Act section 101D, current copy 1 April 2026"

[S51]: https://www.ird.govt.nz/employing-staff/payday-filing/filing-employment-information-electronically/amend-an-employment-information-return "Amend employment information, updated 12 August 2025"
[S52]: https://www.ird.govt.nz/updates/news-folder/2026/upcoming-employment-information-changes "Employment-information changes from 12 September 2026"
[S53]: https://www.legislation.govt.nz/secondary-legislation/pco-drafted/2019/62/en/latest/ "Correction of Errors in Employment Income Information Regulations 2019, current copy 30 March 2026"
[S54]: https://www.legislation.govt.nz/act/public/1994/166/en/latest/sections/LMS835657/ "Tax Administration Act section 108AC, copy 1 October 2026"
[S55]: https://www.legislation.govt.nz/act/public/1994/166/en/latest/sections/LMS674865/ "Tax Administration Act section 108AB, copy 1 October 2026"
[S56]: https://www.legislation.govt.nz/act/public/1994/166/en/latest/sections/DLM354691/ "Tax Administration Act section 108, copy 1 October 2026"
[S57]: https://www.legislation.govt.nz/act/public/1994/166/en/latest/sections/DLM354915/ "Tax Administration Act section 108B, copy 1 October 2026"
[S58]: https://www.legislation.govt.nz/act/public/1994/166/en/latest/sections/DLM354948/ "Tax Administration Act section 113, copy 1 October 2026"
[S59]: https://www.legislation.govt.nz/act/public/1994/166/en/latest/sections/DLM2669326/ "Tax Administration Act section 113A, copy 1 October 2026"
[S60]: https://www.ird.govt.nz/records "Keeping records, updated 14 May 2026"
[S61]: https://www.legislation.govt.nz/act/public/1994/166/en/latest/sections/DLM350462/ "Tax Administration Act section 22, copy 1 October 2026"
[S62]: https://www.ird.govt.nz/managing-my-tax/penalties-and-interest/penalties-and-debt/late-filing-penalties "Late filing penalties, updated 17 November 2025"
[S63]: https://www.taxtechnical.ird.govt.nz/standard-practice-statements/returns-and-debt-collection/sps-1904-late-filing-penalties "SPS19/04 Late filing penalties, 30 May 2019"
[S64]: https://www.legislation.govt.nz/act/public/1994/166/en/latest/sections/DLM356114/ "Tax Administration Act section 139A, copy 1 October 2026"
[S65]: https://www.legislation.govt.nz/act/public/1994/166/en/latest/sections/DLM356638/ "Tax Administration Act section 142, copy 1 October 2026"
[S66]: https://www.legislation.govt.nz/act/public/1994/166/en/latest/sections/DLM356131/ "Tax Administration Act section 139AA, copy 1 October 2026"
[S67]: https://www.legislation.govt.nz/act/public/1994/166/en/latest/sections/DLM356681/ "Tax Administration Act section 142G, copy 1 October 2026"
[S68]: https://www.legislation.govt.nz/act/public/1994/166/en/latest/sections/DLM356138/ "Tax Administration Act section 139B, copy 1 October 2026"
[S69]: https://ird.govt.nz/late-payment-penalties "Late payment penalties, updated 5 September 2024"
[S70]: https://www.legislation.govt.nz/act/public/1994/166/en/latest/sections/DLM358771/ "Tax Administration Act section 183F, copy 1 October 2026"
[S71]: https://www.legislation.govt.nz/act/public/1994/166/en/latest/sections/DLM356156/ "Tax Administration Act section 139BA, copy 1 October 2026"
[S72]: https://www.legislation.govt.nz/act/public/1994/166/en/latest/sections/DLM1191236/ "Tax Administration Act section 141ED, copy 1 October 2026"
[S73]: https://www.legislation.govt.nz/act/public/1994/166/en/latest/sections/DLM358729/ "Tax Administration Act section 183A, copy 1 October 2026"

[S74]: https://www.ird.govt.nz/employing-staff/deductions-from-other-payments/employee-share-schemes/deducting-tax-on-ess-benefits "IRD ESS withholding, updated 28 October 2026"
[S75]: https://www.taxtechnical.ird.govt.nz/-/media/project/ir/tt/pdfs/interpretation-statements/2025/is-25-06.pdf?modified=20250331012659 "IS25/06, 31 March 2025; selected paragraphs, employee scope"
[S76]: https://www.taxtechnical.ird.govt.nz/-/media/project/ir/tt/pdfs/interpretation-statements/2025/is-25-07.pdf?modified=20250331012754 "IS25/07, 31 March 2025; selected funding/reporting paragraphs"
[S77]: https://www.legislation.govt.nz/act/public/2007/97/en/latest/sections/DLM7269557/ "Income Tax Act RD7B, copy 4 September 2026"
[S78]: https://www.legislation.govt.nz/act/public/2007/97/en/latest/sections/DLM1512798/ "Income Tax Act CE7, copy 4 September 2026"
[S79]: https://www.legislation.govt.nz/act/public/2007/97/en/latest/sections/DLM1512781/ "Income Tax Act CE2, copy 4 September 2026"
[S80]: https://www.legislation.govt.nz/act/public/2007/97/en/latest/sections/LMS92763/ "Income Tax Act CE7B, copy 4 September 2026"
[S81]: https://www.legislation.govt.nz/act/public/2007/97/en/latest/sections/LMS1593301/ "Income Tax Act EA4B, copy 4 September 2026"
[S82]: https://www.legislation.govt.nz/act/public/2007/97/en/latest/sections/DLM1519952/ "Income Tax Act RD7, copy 4 September 2026"
[S83]: https://www.ird.govt.nz/employing-staff/deductions-from-other-payments/employee-share-schemes/ess-rules/tax-on-employee-deferred-shares "IRD employee deferred shares, updated 16 March 2026; qualify by enacted law"
[S84]: https://www.ird.govt.nz/employing-staff/payday-filing/non-standard-filing-of-employment-information/lump-sum-payments "IRD lump sum payments, updated 27 January 2026"
[S85]: https://www.ird.govt.nz/employing-staff/payday-filing/non-standard-filing-of-employment-information/employee-share-scheme-benefits "IRD ESS employment information, updated 28 October 2026"
[S86]: https://www.legislation.govt.nz/act/public/1994/166/en/latest/sections/LMS191845/ "Tax Administration Act23K, copy 1 October 2026"
[S87]: https://www.legislation.govt.nz/act/public/2007/97/en/latest/sections/DLM1519950/ "Income Tax Act RD6, copy 4 September 2026"
[S88]: https://www.legislation.govt.nz/act/public/2011/62/en/latest/ "Student Loan Scheme Act2011 s4 and ss36-37, copy 1 April 2026"
[S89]: https://www.legislation.govt.nz/act/public/2007/97/en/latest/sections/DLM1519944/ "Income Tax Act RD4, copy 4 September 2026"
[S90]: https://www.legislation.govt.nz/act/public/2007/97/en/latest/sections/DLM1519735/ "Income Tax Act RA5, copy 4 September 2026"
[S91]: https://www.legislation.govt.nz/act/public/2026/8/en/latest/ "2026 No8 sections2,10,51,114; selected commencement and application"

[S92]: https://www.ird.govt.nz/income-tax/income-tax-for-individuals/tax-codes-and-tax-rates-for-individuals/what-tax-code-should-i-use "IRD tax-code eligibility, updated 30 April 2026; includes collapsed sections"
[S93]: https://www.legislation.govt.nz/act/public/1994/166/en/latest/sections/DLM1252632/ "Tax Administration Act 24B, copy 1 October 2026"
[S94]: https://www.legislation.govt.nz/act/public/1994/166/en/latest/sections/DLM1253911/ "Tax Administration Act 24C, copy 1 October 2026"
[S95]: https://www.legislation.govt.nz/act/public/1994/166/en/latest/sections/DLM1253915/ "Tax Administration Act 24E, copy 1 October 2026"
[S96]: https://www.legislation.govt.nz/act/public/1994/166/en/latest/sections/LMS193078/ "Tax Administration Act 24D, copy 1 October 2026"
[S97]: https://www.legislation.govt.nz/act/public/1994/166/en/latest/sections/LMS195590/ "Tax Administration Act Schedule 5 Part A clauses 1-4/rows 7-9 and Part B clause 3, copy 1 October 2026"
[S98]: https://www.legislation.govt.nz/act/public/2007/97/en/latest/sections/DLM1520575/ "Income Tax Act YA 1 selected worker, market value and year definitions, copy 4 September 2026"

[S99]: https://www.ird.govt.nz/employing-staff/deductions-from-other-payments/exempt-employee-share-schemes "IRD exempt employee share schemes, updated 13 November 2026; statutory qualifications apply"
[S100]: https://www.legislation.govt.nz/act/public/2007/97/en/latest/sections/LMS32342/ "Income Tax Act CW26B, copy 4 September 2026"
[S101]: https://www.legislation.govt.nz/act/public/2007/97/en/latest/sections/LMS32492/ "Income Tax Act CW26C, copy 4 September 2026"
[S102]: https://www.legislation.govt.nz/act/public/2007/97/en/latest/sections/LMS32494/ "Income Tax Act CW26D, copy 4 September 2026"
[S103]: https://www.legislation.govt.nz/act/public/2007/97/en/latest/sections/LMS328941/ "Income Tax Act CW26DB, copy 4 September 2026"
[S104]: https://www.legislation.govt.nz/act/public/2007/97/en/latest/sections/LMS32496/ "Income Tax Act CW26E, copy 4 September 2026"
[S105]: https://www.legislation.govt.nz/act/public/2007/97/en/latest/sections/LMS33459/ "Income Tax Act DV28, copy 4 September 2026"
[S106]: https://www.legislation.govt.nz/act/public/1994/166/en/latest/sections/LMS32667/ "Tax Administration Act63B, copy 1 October 2026"
[S107]: https://www.legislation.govt.nz/act/public/2025/9/en/latest/ "2025 No9 sections2(34) and27, offer-date application of exempt ESS limits"
[S108]: https://www.ird.govt.nz/employing-staff/deductions-from-other-payments/exempt-employee-share-schemes/report-exempt-ess "IRD initial exempt ESS notification, updated 22 October 2026"
[S109]: https://www.ird.govt.nz/employing-staff/deductions-from-other-payments/exempt-employee-share-schemes/report-employee-shares-under-exempt-ess "IRD annual exempt ESS reporting, updated 22 October 2026"
[S110]: https://www.ird.govt.nz/-/media/project/ir/home/documents/forms-and-guides/ir1200---ir1299/ir1211/ir1211.pdf?modified=20261022002436 "IR1211 initial exempt ESS notification, October 2026, page1"
[S111]: https://www.ird.govt.nz/-/media/project/ir/home/documents/forms-and-guides/ir1200---ir1299/ir1212/ir1212.pdf?modified=20261022002438 "IR1212 annual exempt ESS return, October 2026, page1"
[S112]: https://www.legislation.govt.nz/act/public/2007/97/en/latest/sections/LMS32498/ "Income Tax Act CW26F, copy 4 September 2026"
[S113]: https://www.legislation.govt.nz/act/public/2007/97/en/latest/sections/LMS32500/ "Income Tax Act CW26G, copy 4 September 2026"

<!-- openaccountants-cta-block -->

---

## Talk to a verified accountant

This guide is maintained in the
[ryanduguid/openaccountants fork](https://github.com/ryanduguid/openaccountants).
Check its quality tier, recorded review status and cited sources before use.
Choose a practitioner whose credentials and engagement scope you have verified.
The links below are optional upstream services; they do not publish or verify
this fork's changes.

- Upstream connection service: https://www.openaccountants.com/connect
- Upstream accountant network: https://www.openaccountants.com/network

> **General reference only.** This document does not constitute tax, legal, or
> financial advice. Verify figures against the cited primary sources or with a
> licensed professional before relying on them.
