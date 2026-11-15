---
name: nz-employer-payroll
description: "Use this skill for ordinary New Zealand employer payroll paid from 1 April 2026 to 31 March 2027: PAYE on salary and wages (tax codes M, ME, secondary codes, ND, NSW, CAE, EDW, STC tailored codes), the employee ACC earners' levy inside PAYE, extra pay and bonuses, pay on termination and ordinary student-loan deductions. Trigger on NZ payroll, PAYE, IR330, tax code, extra pay, bonus, student loan deduction, tailored tax code. Recovery, child-support, court and arrears notices, payday filing, corrections and penalties are in nz-payroll-notices-filing-penalties. KiwiSaver and ESCT are in nz-kiwisaver-esct; employee share schemes in nz-employee-share-schemes."
license: "AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)"
metadata:
  source: openaccountants
  openaccountants_url: "https://www.openaccountants.com/skills/nz-employer-payroll"
  jurisdiction: "NZ"
  tax_year: "2026"
  last_updated: "2026-11-14"
---

# New Zealand employer payroll: PAYE, student loans, deductions and payday filing (2026-27)

Figures are for tax year 2026, meaning payroll paid from 1 April 2026 to 31 March 2027 (the New Zealand 2026-27 tax year, which Inland Revenue calls the 2027 income year). All amounts are New Zealand dollars. Written by Ryan Duguid on his fork (ryanduguid/openaccountants, rules checked 12 and 13 November 2026) and imported on 14 November 2026. It has not been reviewed by an accountant.

## Scope and who this is for

This guide covers ordinary salary and wages, selected employee share schemes and selected extra-pay calculations for a New Zealand employer in NZD during **1 April 2026 to 31 March 2027**. It provides selected tax, contribution and filing rules, not complete employment-law or whole-topic coverage. Start with [Inland Revenue's salary and wage deduction instructions](https://www.ird.govt.nz/deductions) and its [2026-27 payroll calculation specification](https://www.ird.govt.nz/-/media/project/ir/home/documents/digital-service-providers/software-providers/payroll-calculations-business-rules-specifications/payroll-calculations-and-business-rules-specification.pdf?modified=20260401012317).

- **Covers:** PAYE and the employee earners' levy, student-loan deductions, tailored codes and certificates, extra pay and pay on termination.
- **Companions:** student-loan recovery, child-support, court and arrears notices, payday filing, paying deductions, corrections, records and penalties are in `nz-payroll-notices-filing-penalties`. KiwiSaver deductions, employer contributions and ESCT are in `nz-kiwisaver-esct`. Employee share scheme benefits through payroll, and exempt schemes, are in `nz-employee-share-schemes`. The self-employed person's own ACC levies are in `nz-acc-levies`; the employee's annual IR3 is in `nz-income-tax-ir3`.
- **Does not cover:** employment-law entitlements (leave, holiday pay, minimum wage), fringe benefit tax, cross-border employment, contractors' schedular payments and the employer's ACC invoice.

## Ask the client first

- Employer registration, actual payday, pay frequency and period covered. [Register as an employer as soon as you start employing staff](https://www.ird.govt.nz/setting-up-a-business-or-organisation).
- Employee classification, completed IR330 tax-code declaration and any Inland Revenue tax-code, tailored-rate, student-loan, child-support or arrears notice. Resolve conflicting instructions before using a rate.

## The method, step by step

1. **Confirm the employer, payday and frequency.** Registration as an employer, the actual payday, pay frequency and the period covered.
2. **Confirm the code.** Use the IR330 code and any Inland Revenue notice; with no completed IR330 use ND (45% plus the earners' levy) unless an exception applies.
3. **Classify each payment.** Ordinary pay, extra pay, pay on termination or another special payment each have their own method below.
4. **Work out PAYE, then the student loan, then notices.** Use the official tables or calculator; never add the earners' levy again on top of PAYE.
5. **Apply any deduction notices, then file and pay,** using `nz-payroll-notices-filing-penalties`.

### Rates, bands and thresholds

Key figures for payroll paid from 1 April 2026 to 31 March 2027. The detail and conditions are in the sections below.

| Item | Figure | Condition | Source |
| --- | --- | --- | --- |
| Earners' levy rate inside PAYE | 1.75% | GST-inclusive; on liable earnings up to the maximum | https://www.ird.govt.nz/income-tax/income-tax-for-individuals/acc-clients-and-carers/acc-earners-levy-rates |
| Maximum liable earnings for the earners' levy | $156,641 | Per employee for the year | https://www.ird.govt.nz/income-tax/income-tax-for-individuals/acc-clients-and-carers/acc-earners-levy-rates |
| Maximum annual earners' levy | $2,741.22 | Reached at $156,641 | https://www.ird.govt.nz/income-tax/income-tax-for-individuals/acc-clients-and-carers/acc-earners-levy-rates |
| Annual income tax for M and ME, A from $1 to $15,600 | A x 10.5% | A is whole-dollar annualised pay (specification section 5.2) | https://www.ird.govt.nz/-/media/project/ir/home/documents/digital-service-providers/software-providers/payroll-calculations-business-rules-specifications/payroll-calculations-and-business-rules-specification.pdf?modified=20260401012317 |
| Annual income tax, A from $15,601 to $53,500 | A x 17.5% - $1,092.00 | same | https://www.ird.govt.nz/-/media/project/ir/home/documents/digital-service-providers/software-providers/payroll-calculations-business-rules-specifications/payroll-calculations-and-business-rules-specification.pdf?modified=20260401012317 |
| Annual income tax, A from $53,501 to $78,100 | A x 30% - $7,779.50 | same | https://www.ird.govt.nz/-/media/project/ir/home/documents/digital-service-providers/software-providers/payroll-calculations-business-rules-specifications/payroll-calculations-and-business-rules-specification.pdf?modified=20260401012317 |
| Annual income tax, A from $78,101 to $180,000 | A x 33% - $10,122.50 | same | https://www.ird.govt.nz/-/media/project/ir/home/documents/digital-service-providers/software-providers/payroll-calculations-business-rules-specifications/payroll-calculations-and-business-rules-specification.pdf?modified=20260401012317 |
| Annual income tax, A over $180,000 | A x 39% - $20,922.50 | same | https://www.ird.govt.nz/-/media/project/ir/home/documents/digital-service-providers/software-providers/payroll-calculations-business-rules-specifications/payroll-calculations-and-business-rules-specification.pdf?modified=20260401012317 |
| NSW code | 10.5% plus the 1.75% earners' levy | Recognised seasonal workers and the other workers listed under the NSW code | https://www.ird.govt.nz/-/media/project/ir/home/documents/digital-service-providers/software-providers/payroll-calculations-business-rules-specifications/payroll-calculations-and-business-rules-specification.pdf?modified=20260401012317 |
| Student-loan annual repayment threshold | $24,128 | Primary employment; no threshold on a secondary code | https://www.ird.govt.nz/-/media/project/ir/home/documents/digital-service-providers/software-providers/payroll-calculations-business-rules-specifications/payroll-calculations-and-business-rules-specification.pdf?modified=20260401012317 |
| Student-loan deduction rate | 12% of pay over the period threshold | Weekly threshold $464, fortnightly $928 | https://www.ird.govt.nz/-/media/project/ir/home/documents/digital-service-providers/software-providers/payroll-calculations-business-rules-specifications/payroll-calculations-and-business-rules-specification.pdf?modified=20260401012317 |


### PAYE and the employee ACC levy

Use the employee's IR330 code and any applicable Inland Revenue instruction, subject to the first-month RSE exception and other statutory exceptions explained below. For ordinary employees outside those exceptions, [Inland Revenue](https://www.ird.govt.nz/deductions) requires **ND at 45% plus the applicable ACC earners' levy** when no completed tax-code declaration is supplied. Do not use a zero rate or guess a standard code. Contractor schedular payments use a separate IR330C process; they are not automatically salary payroll. [S1](https://www.ird.govt.nz/deductions), [S4](https://www.ird.govt.nz/employing-staff/deductions-from-income)

Use the official PAYE calculator or actual-period deduction tables linked from [the salary/wage deductions page](https://www.ird.govt.nz/deductions), with the correct payday, tax code and pay frequency. PAYE calculation includes ACC earners' levy where applicable. **Do not add another ACC levy to a PAYE result that already includes it.** Annual income-tax brackets alone do not reproduce every payroll code, frequency, levy cap or rounding rule. [S1](https://www.ird.govt.nz/deductions), [S2](https://www.ird.govt.nz/-/media/project/ir/home/documents/digital-service-providers/software-providers/payroll-calculations-business-rules-specifications/payroll-calculations-and-business-rules-specification.pdf?modified=20260401012317)

| Employee earners' levy period | GST-inclusive rate | Maximum annual liable earnings | Maximum annual levy | Source |
|---|---:|---:|---:|---|
| 1 April 2026 to 31 March 2027 | 1.75% | $156,641 | $2,741.22 | https://www.ird.govt.nz/income-tax/income-tax-for-individuals/acc-clients-and-carers/acc-earners-levy-rates |

Source: [Inland Revenue's earners' levy table](https://www.ird.govt.nz/income-tax/income-tax-for-individuals/acc-clients-and-carers/acc-earners-levy-rates). Apply the actual payroll calculation and its cap rules; this annual table is not an instruction to charge 1.75% on uncapped pay or to combine multiple employments without checking their treatment.

Student-loan and child-support deductions need the actual code or notice and applicable calculation. Ordinary employee child support is limited to 40% of gross salary/wages less the PAYE income-tax component, excluding ACC earners' levy from that tax component. It does not cap every other deduction at 40%. The notice, protected-earnings and shortfall methods are set out below. [S1](https://www.ird.govt.nz/deductions), [S2, section 5.15](https://www.ird.govt.nz/-/media/project/ir/home/documents/digital-service-providers/software-providers/payroll-calculations-business-rules-specifications/payroll-calculations-and-business-rules-specification.pdf?modified=20260401012317), [S13, PDF page 24](https://www.ird.govt.nz/-/media/project/ir/home/documents/forms-and-guides/ir300---ir399/ir335/ir335.pdf?modified=20250811232131)

The employee earners' levy comes from the employee's income through PAYE. The employer's **Work and Working Safer levies** are separately invoiced by ACC and require the business's classification, liable payroll and current invoice/rates. Do not add them as another generic employee deduction. This guide does not calculate those invoices. [ACC's explanation of levy responsibilities](https://www.acc.co.nz/for-business/understanding-levies-if-you-work-or-own-a-business) supports that distinction; use [S5](https://www.ird.govt.nz/income-tax/income-tax-for-individuals/acc-clients-and-carers/acc-earners-levy-rates) for the dated employee rate.

### Ordinary M and ME calculations

For regular positive salary or wages under **M, M SL, ME or ME SL**, use the sequence in [S2, sections 5.2-5.4](https://www.ird.govt.nz/-/media/project/ir/home/documents/digital-service-providers/software-providers/payroll-calculations-business-rules-specifications/payroll-calculations-and-business-rules-specification.pdf?modified=20260401012317). Confirm the declaration and notices first. The specification calls for 6 decimal places during calculations unless a stated truncation applies.

1. Multiply taxable period pay **including cents** by 52 for weekly pay, 26 for fortnightly, 13 for every 4 weeks or 12 for monthly. Then drop the annual amount's cents to obtain whole-dollar annual income A. Do not drop period cents before annualising M/ME pay.
2. Calculate annual income tax from the following table. Keep the result unrounded.

| Whole-dollar annual income A | Annual income tax | Source |
|---|---|---|
| $1 to $15,600 | A × 10.5% | https://www.ird.govt.nz/-/media/project/ir/home/documents/digital-service-providers/software-providers/payroll-calculations-business-rules-specifications/payroll-calculations-and-business-rules-specification.pdf?modified=20260401012317 |
| $15,601 to $53,500 | A × 17.5% − $1,092.00 | https://www.ird.govt.nz/-/media/project/ir/home/documents/digital-service-providers/software-providers/payroll-calculations-business-rules-specifications/payroll-calculations-and-business-rules-specification.pdf?modified=20260401012317 |
| $53,501 to $78,100 | A × 30% − $7,779.50 | https://www.ird.govt.nz/-/media/project/ir/home/documents/digital-service-providers/software-providers/payroll-calculations-business-rules-specifications/payroll-calculations-and-business-rules-specification.pdf?modified=20260401012317 |
| $78,101 to $180,000 | A × 33% − $10,122.50 | https://www.ird.govt.nz/-/media/project/ir/home/documents/digital-service-providers/software-providers/payroll-calculations-business-rules-specifications/payroll-calculations-and-business-rules-specification.pdf?modified=20260401012317 |
| Above $180,000 | A × 39% − $20,922.50 | https://www.ird.govt.nz/-/media/project/ir/home/documents/digital-service-providers/software-providers/payroll-calculations-business-rules-specifications/payroll-calculations-and-business-rules-specification.pdf?modified=20260401012317 |

3. Calculate the annual ACC component: **A × 1.75% where A < $156,641; otherwise $2,741.22**. Keep this component unrounded. Use the specification's stated maximum rather than multiplying the capped earnings and rounding independently.
4. For M/M SL, add annual tax and ACC. For ME/ME SL, subtract the applicable annual IETC from that sum. On the whole-dollar A, the payroll IETC is $0 below $24,000; **$520 from $24,000 to $66,000 inclusive**; **$520 − 13% × (A − $66,000)** from $66,001 to $69,999; and $0 from $70,000. Keep the credit unrounded.
5. Divide the annual total by **52**, then **truncate to cents**. For fortnightly, 4-weekly or monthly pay, multiply that already-truncated weekly amount by 52 and divide by 26, 13 or 12 respectively, then **truncate to cents again**. Dividing the annual total directly by 12 can give a different monthly deduction. This result is PAYE including ACC; student loans and other deductions remain separate.

The payroll credit formula does not establish IETC eligibility. Check NZ tax residence, total annual income and the exclusion where the employee or partner is entitled to and receives Working for Families, and the exclusions for income-tested benefits, NZ Superannuation, Veteran's Pension and overseas equivalents. Entitlement is tested by whole months. Use ME/ME SL only under the appropriate declaration; a main job below $24,000 with total income in the eligible range may need a tailored code or year-end credit. A year-end assessment may correct too much or too little credit. [IETC eligibility](https://www.ird.govt.nz/income-tax/income-tax-for-individuals/individual-tax-credits/independent-earner-tax-credit-ietc), [salary/wage instructions](https://www.ird.govt.nz/income-tax/income-tax-for-individuals/individual-tax-credits/independent-earner-tax-credit-ietc/getting-the-independent-earner-tax-credit-if-you-earn-salary-or-wages)

### Ordinary secondary codes and ND

A secondary code is chosen using **estimated annual total income from all sources**, rather than the second job alone. Follow the employee's IR330 and any Inland Revenue direction. For ordinary liable salary/wages, [S2, section 5.6](https://www.ird.govt.nz/-/media/project/ir/home/documents/digital-service-providers/software-providers/payroll-calculations-business-rules-specifications/payroll-calculations-and-business-rules-specification.pdf?modified=20260401012317) gives these standard deductions, each already including the 1.75% ACC levy:

| Estimated annual total income | Secondary code, with SL where required | Standard PAYE including ACC | Source |
|---|---|---:|---|
| Up to $15,600 | SB / SB SL | 12.25% | https://www.ird.govt.nz/-/media/project/ir/home/documents/digital-service-providers/software-providers/payroll-calculations-business-rules-specifications/payroll-calculations-and-business-rules-specification.pdf?modified=20260401012317 |
| $15,601 to $53,500 | S / S SL | 19.25% | https://www.ird.govt.nz/-/media/project/ir/home/documents/digital-service-providers/software-providers/payroll-calculations-business-rules-specifications/payroll-calculations-and-business-rules-specification.pdf?modified=20260401012317 |
| $53,501 to $78,100 | SH / SH SL | 31.75% | https://www.ird.govt.nz/-/media/project/ir/home/documents/digital-service-providers/software-providers/payroll-calculations-business-rules-specifications/payroll-calculations-and-business-rules-specification.pdf?modified=20260401012317 |
| $78,101 to $180,000 | ST / ST SL | 34.75% | https://www.ird.govt.nz/-/media/project/ir/home/documents/digital-service-providers/software-providers/payroll-calculations-business-rules-specifications/payroll-calculations-and-business-rules-specification.pdf?modified=20260401012317 |
| Above $180,000 | SA / SA SL | 40.75% | https://www.ird.govt.nz/-/media/project/ir/home/documents/digital-service-providers/software-providers/payroll-calculations-business-rules-specifications/payroll-calculations-and-business-rules-specification.pdf?modified=20260401012317 |

Drop period pay's cents **before** multiplying by the applicable standard secondary rate, then truncate the deduction to cents. The whole payment uses that code's flat rate; these are not progressive bands within the second job. Do not add ACC again or import the M/ME annualisation algorithm. [S2, sections 5.1 and 5.6](https://www.ird.govt.nz/-/media/project/ir/home/documents/digital-service-providers/software-providers/payroll-calculations-business-rules-specifications/payroll-calculations-and-business-rules-specification.pdf?modified=20260401012317), [tax-code instructions](https://www.ird.govt.nz/income-tax/income-tax-for-individuals/tax-codes-and-tax-rates-for-individuals/about-tax-codes)

For ordinary ND salary/wages, drop period cents, multiply by **46.75%** (45% tax plus 1.75% ACC) and truncate to cents. [S2, section 5.8](https://www.ird.govt.nz/-/media/project/ir/home/documents/digital-service-providers/software-providers/payroll-calculations-business-rules-specifications/payroll-calculations-and-business-rules-specification.pdf?modified=20260401012317) These standard-code algorithms do not determine an individual's final annual ACC liability across multiple employments. Resolve a valid tailored tax code, levy adjustment or other exceptional instruction separately; do not remove ACC from a standard secondary or ND rate merely by applying the M-code cap formula.

### Ordinary NSW, CAE and EDW calculations

Establish the worker's qualifying employment before using a flat code. Inland Revenue's [tax-code instructions](https://www.ird.govt.nz/income-tax/income-tax-for-individuals/tax-codes-and-tax-rates-for-individuals/what-tax-code-should-i-use), updated 30 April 2026, distinguish these cases:

| Code | Employment covered by the instructions | Source |
|---|---|---|
| NSW | Recognised seasonal workers and holders of a work visa as foreign crew of a vessel fishing New Zealand waters. | https://www.ird.govt.nz/income-tax/income-tax-for-individuals/tax-codes-and-tax-rates-for-individuals/what-tax-code-should-i-use |
| CAE | YA 1 defines a casual agricultural employee as one of 3 categories. A **casual agricultural worker** is engaged day to day for no more than 3 months as a casual seasonal worker, exclusively for seasonal agricultural, horticultural, market gardening, nursery, orchard or tobacco farming work, or work the Commissioner considers similar. A **shearer** shears sheep other than in their own business and is not permanently employed on the premises where the shearing shed is. A **shearing shed-hand** is employed in or about the shed other than in their own business and is not a shearer, wool classer or person permanently employed on those premises. The 3-month limit applies only to casual agricultural workers. Inland Revenue's tax-code page also says these workers earn no other income in that time; YA 1 does not state that condition. [S98](https://www.legislation.govt.nz/act/public/2007/97/en/latest/sections/DLM1520575/), [S92](https://www.ird.govt.nz/income-tax/income-tax-for-individuals/tax-codes-and-tax-rates-for-individuals/what-tax-code-should-i-use) IR335 keeps CAE for a shearer's ordinary farm work when shearing is not possible and for a farmer's part-time shearing for another farmer, but treats a normal farm employee's shearing wages as ordinary pay, not CAE. [S13, PDF page 57](https://www.ird.govt.nz/-/media/project/ir/home/documents/forms-and-guides/ir300---ir399/ir335/ir335.pdf?modified=20250811232131) | https://www.ird.govt.nz/income-tax/income-tax-for-individuals/tax-codes-and-tax-rates-for-individuals/what-tax-code-should-i-use |
| EDW | YA 1 requires that the person is engaged, as an electoral official, interpreter, usher or otherwise, for an election or poll held under or subject to the Electoral Act 1993 or the Local Electoral Act 2001, or held simultaneously with and in the same premises as one; is paid by the authority controlling it; and is paid exclusively for work immediately before, on or immediately after its voting days. Qualifying local elections and polls are included; pay from anyone else, such as a party or candidate, is not. [S98](https://www.legislation.govt.nz/act/public/2007/97/en/latest/sections/DLM1520575/) For a general election, Inland Revenue's tax-code page limits EDW to the 2-week advance-voting period and election day, and directs election work outside that period to the appropriate ordinary IR330 code. IR335 describes casual work immediately before, on or after polling day. [S92](https://www.ird.govt.nz/income-tax/income-tax-for-individuals/tax-codes-and-tax-rates-for-individuals/what-tax-code-should-i-use), [S13, PDF page 51](https://www.ird.govt.nz/-/media/project/ir/home/documents/forms-and-guides/ir300---ir399/ir335/ir335.pdf?modified=20250811232131) | https://www.ird.govt.nz/income-tax/income-tax-for-individuals/tax-codes-and-tax-rates-for-individuals/what-tax-code-should-i-use |

The **first month of an RSE worker's period of employment in New Zealand** has a specific statutory exception. Schedule 5 Part B clause 3 supplies NSW, and sections 24B(1)(c), 24C(2)(b) and 24E(1)(c) recognise that exception to ordinary notification and non-notified treatment. It is not a general first-month exception for every foreign worker. After that first month, the ordinary tax-code notification rules apply. NSW can continue for qualifying employment with proper notification; month-end alone does not require a different code. For an ordinary worker outside section 24D, if the required name, IRD number and tax code have not been notified, no applicable Commissioner-provided code applies and the first-month exception has ended, use ND until the notification requirement is met. Resolve any Commissioner correction, changed circumstances or entitlement-ending notice under Schedule 5 Part A clauses 2-4. [S93](https://www.legislation.govt.nz/act/public/1994/166/en/latest/sections/DLM1252632/), [S94](https://www.legislation.govt.nz/act/public/1994/166/en/latest/sections/DLM1253911/), [S95](https://www.legislation.govt.nz/act/public/1994/166/en/latest/sections/DLM1253915/), [S96](https://www.legislation.govt.nz/act/public/1994/166/en/latest/sections/LMS193078/), [S97](https://www.legislation.govt.nz/act/public/1994/166/en/latest/sections/LMS195590/), [S2, section 5.5](https://www.ird.govt.nz/-/media/project/ir/home/documents/digital-service-providers/software-providers/payroll-calculations-business-rules-specifications/payroll-calculations-and-business-rules-specification.pdf?modified=20260401012317)

For established **ordinary** pay under these codes during 1 April 2026 to 31 March 2027, use [S2, sections 5.5 and 5.7, PDF pages 26-27 and 30](https://www.ird.govt.nz/-/media/project/ir/home/documents/digital-service-providers/software-providers/payroll-calculations-business-rules-specifications/payroll-calculations-and-business-rules-specification.pdf?modified=20260401012317):

1. Identify ordinary taxable pay for the period, including taxable allowances. Keep non-taxable allowances and separately classified extra pay out of that ordinary base.
2. Drop the ordinary base's cents to obtain whole-dollar pay. For example, $457.89 becomes $457. Do not annualise it using the M/ME method.
3. For NSW, multiply that whole-dollar pay by **12.25%**: 10.5% income tax plus 1.75% ACC. For CAE or EDW, multiply by **19.25%**: 17.5% income tax plus 1.75% ACC.
4. **Truncate the combined deduction to cents.** Do not round it to the nearest cent or add ACC again. Deduct it from actual cash pay, retaining that pay's cents. Calculate other applicable deductions and separately classified payments under their own rules.

These methods do not establish the worker's final annual ACC liability across employments or an exceptional levy adjustment. Do not import the M-code cap formula into them without an applicable instruction. The worked cases below use ordinary amounts below the standard period caps and assume no exceptional notice or adjustment. Donations, unusual pay, negative corrections and final ACC reconciliation require separate checks. [S2](https://www.ird.govt.nz/-/media/project/ir/home/documents/digital-service-providers/software-providers/payroll-calculations-business-rules-specifications/payroll-calculations-and-business-rules-specification.pdf?modified=20260401012317), [S5](https://www.ird.govt.nz/income-tax/income-tax-for-individuals/acc-clients-and-carers/acc-earners-levy-rates)

**Do not make ordinary student-loan repayment deductions from pay correctly using CAE, EDW or NSW.** IR335 expressly lists those codes as exclusions. A valid NSW employment-information line cannot contain KiwiSaver or student-loan deductions; the specification identifies these non-resident workers as ineligible for KiwiSaver and permits child support where applicable. CAE or EDW alone does not establish a KiwiSaver exemption: apply the separately established membership, contribution and notice rules in Section 3. A code exclusion does not decide the person's wider loan liability. [S13, PDF page 20](https://www.ird.govt.nz/-/media/project/ir/home/documents/forms-and-guides/ir300---ir399/ir335/ir335.pdf?modified=20250811232131), [S2, section 5.5](https://www.ird.govt.nz/-/media/project/ir/home/documents/digital-service-providers/software-providers/payroll-calculations-business-rules-specifications/payroll-calculations-and-business-rules-specification.pdf?modified=20260401012317)

### Ordinary student-loan deductions

For the 2026-27 period, the specification's annual repayment threshold is **$24,128**, with these primary-job period thresholds: weekly **$464**, fortnightly **$928**, every 4 weeks **$1,856** and monthly **$2,010.66**. Use the stated monthly amount rather than rounding it to $2,010.67. [S2, sections 2.2 and 5.4](https://www.ird.govt.nz/-/media/project/ir/home/documents/digital-service-providers/software-providers/payroll-calculations-business-rules-specifications/payroll-calculations-and-business-rules-specification.pdf?modified=20260401012317)

For **M SL or ME SL**, drop gross period pay's cents, subtract the applicable period threshold and deduct **12% of a positive excess**, truncating the result to cents. The deduction is zero where there is no excess. For an ordinary **secondary SL code**, drop period cents and deduct **12% of that whole-dollar pay**, truncating to cents; there is **no second ordinary repayment threshold**. A valid special-deduction-rate certificate substitutes its specified percentage in the relevant algorithm. Keep the student-loan result separate from PAYE, and do not reduce taxable pay by it. [S2, sections 5.4 and 5.6](https://www.ird.govt.nz/-/media/project/ir/home/documents/digital-service-providers/software-providers/payroll-calculations-business-rules-specifications/payroll-calculations-and-business-rules-specification.pdf?modified=20260401012317)

Check the actual SL declaration and any repayment exemption, special rate or extra-deduction notice before using these ordinary rules. An unused primary-job threshold does not automatically transfer to a second job; apply for the appropriate special rate. Inland Revenue's [salary/wage student-loan page](https://www.ird.govt.nz/repaying-my-student-loan-when-i-earn-salary-or-wages) explains that distinction but labels its annual threshold as the **2026 tax year**; the dated 2026-27 specification supplies this guide's period-specific figures. Exemptions, recovery deductions and irregular or special payments need their own checks.

### Tailored tax codes and student-loan certificates

Use an actual Inland Revenue certificate covering the payday. Record its PAYE rate, separate student-loan rate, whether the loan threshold applies and each start/end date. For ordinary salary or wages, truncate period pay to whole dollars, multiply by the certificate's PAYE rate and truncate the deduction to cents. The quoted salary/wage PAYE rate already includes the 1.75% earners' levy; do not add it again. Calculate the loan deduction separately on the whole-dollar base: apply the certificate rate to positive income above the period threshold for main employment, or to every dollar for secondary employment, as the certificate directs. [S2, section 5.9, PDF pages 32-33](https://www.ird.govt.nz/-/media/project/ir/home/documents/digital-service-providers/software-providers/payroll-calculations-business-rules-specifications/payroll-calculations-and-business-rules-specification.pdf?modified=20260401012317)

A student-loan special deduction rate changes the loan calculation, not the PAYE tax code unless the certificate says so. It may allocate unused main-job threshold through a reduced secondary-job rate; the employer cannot invent that allocation. Follow each dated rate period. Do not backdate a special deduction rate or a repayment exemption. On expiry, follow the certificate's return-to-standard instructions. If a tailored PAYE certificate expires without a replacement or new declaration, revert to the previous IR330/IR330C code; if there was none, use ND until a valid declaration or certificate arrives. [S2, section 5.9.2, PDF pages 34-37](https://www.ird.govt.nz/-/media/project/ir/home/documents/digital-service-providers/software-providers/payroll-calculations-business-rules-specifications/payroll-calculations-and-business-rules-specification.pdf?modified=20260401012317)

A full-time student expecting income below the annual repayment threshold may qualify for a repayment deduction exemption even when an individual pay exceeds its threshold. Require the IRD exemption certificate, use its specified non-SL code only for its valid period and restore its instructed SL code when it ends. Student status alone does not authorise stopping deductions. A special loan rate does not absorb voluntary SLBOR deductions; keep them separate. IRD says it cancels SLCIR notices when granting an SDR: reconcile the actual notice trail rather than silently retaining or cancelling a recovery instruction yourself. [S2, sections 5.9.2-5.9.3](https://www.ird.govt.nz/-/media/project/ir/home/documents/digital-service-providers/software-providers/payroll-calculations-business-rules-specifications/payroll-calculations-and-business-rules-specification.pdf?modified=20260401012317)

### Extra pay: choose the calculation before choosing a rate

Annual or special bonuses, cashed-up leave, back pay and redundancy/retiring payments can be extra pay. Overtime and regular payments are not automatically lump sums. First establish the payment's legal character, whether it relates to ending employment, the employee's code and any election for a higher rate. NSW, ND and tailored-code payments use their applicable special rate rather than the ordinary extra-pay rate table; CAE/EDW extra pay follows the primary-income method. This guide does not establish entitlement to a termination payment or a contractor's schedular-payment treatment. Use the separate selected ESS rules below for established employee cases. [S22](https://www.ird.govt.nz/calculate-lump-sum-paye), [S23](https://www.ird.govt.nz/employing-staff/payday-filing/non-standard-filing-of-employment-information/lump-sum-payments), [S24](https://www.ird.govt.nz/employing-staff/payday-filing/non-standard-filing-of-employment-information/lump-sum-payments/calculate-paye-for-a-lump-sum-payment-end-of-employment)

For a **non-termination** extra payment under an ordinary primary or secondary code:

1. Total regular PAYE income payments in the 4 weeks ending on the payment date, including that date but excluding all extra pays. Annualise by 13 for weekly, fortnightly or four-weekly payments and by 12 for monthly payments. An off-cycle extra payment still uses a window ending on its actual payment date. No regular payment in that window means a zero historical amount, not an assumed annual salary. Where only one prior pay period exists, use its pay amount annualised for its frequency. [S2, section 5.11](https://www.ird.govt.nz/-/media/project/ir/home/documents/digital-service-providers/software-providers/payroll-calculations-business-rules-specifications/payroll-calculations-and-business-rules-specification.pdf?modified=20260401012317), [S22](https://www.ird.govt.nz/calculate-lump-sum-paye)
2. For a secondary code, add the low threshold below to that annualised amount. Add zero for a primary code. Call this combined amount **B**. Add the extra pay **E** to B and truncate that grossed-up total to whole dollars **G** solely to select the tax band. Retain cents in E and B for the deduction and levy calculations. [S2, sections 5.11.1-5.11.2](https://www.ird.govt.nz/-/media/project/ir/home/documents/digital-service-providers/software-providers/payroll-calculations-business-rules-specifications/payroll-calculations-and-business-rules-specification.pdf?modified=20260401012317)
3. Select the income-tax rate below, or the employee's valid election for a higher permitted rate. Multiply the **whole extra payment**, with its cents, by that single rate. This is withholding on the extra pay, not a progressive allocation of the extra pay amongst annual bands. Do not truncate that tax component before adding the levy. [S2, section 5.11](https://www.ird.govt.nz/-/media/project/ir/home/documents/digital-service-providers/software-providers/payroll-calculations-business-rules-specifications/payroll-calculations-and-business-rules-specification.pdf?modified=20260401012317), [S22](https://www.ird.govt.nz/calculate-lump-sum-paye)

| Secondary code, with or without SL | Amount added to annualised income | Source |
|---|---:|---|
| SB | $0 | https://www.ird.govt.nz/-/media/project/ir/home/documents/digital-service-providers/software-providers/payroll-calculations-business-rules-specifications/payroll-calculations-and-business-rules-specification.pdf?modified=20260401012317 |
| S | $15,601 | https://www.ird.govt.nz/-/media/project/ir/home/documents/digital-service-providers/software-providers/payroll-calculations-business-rules-specifications/payroll-calculations-and-business-rules-specification.pdf?modified=20260401012317 |
| SH | $53,501 | https://www.ird.govt.nz/-/media/project/ir/home/documents/digital-service-providers/software-providers/payroll-calculations-business-rules-specifications/payroll-calculations-and-business-rules-specification.pdf?modified=20260401012317 |
| ST | $78,101 | https://www.ird.govt.nz/-/media/project/ir/home/documents/digital-service-providers/software-providers/payroll-calculations-business-rules-specifications/payroll-calculations-and-business-rules-specification.pdf?modified=20260401012317 |
| SA | $180,001 | https://www.ird.govt.nz/-/media/project/ir/home/documents/digital-service-providers/software-providers/payroll-calculations-business-rules-specifications/payroll-calculations-and-business-rules-specification.pdf?modified=20260401012317 |

| Whole-dollar G | Income-tax rate, excluding ACC | Source |
|---|---:|---|
| Up to $15,600 | 10.5% | https://www.ird.govt.nz/-/media/project/ir/home/documents/digital-service-providers/software-providers/payroll-calculations-business-rules-specifications/payroll-calculations-and-business-rules-specification.pdf?modified=20260401012317 |
| $15,601-$53,500 | 17.5% | https://www.ird.govt.nz/-/media/project/ir/home/documents/digital-service-providers/software-providers/payroll-calculations-business-rules-specifications/payroll-calculations-and-business-rules-specification.pdf?modified=20260401012317 |
| $53,501-$78,100 | 30% | https://www.ird.govt.nz/-/media/project/ir/home/documents/digital-service-providers/software-providers/payroll-calculations-business-rules-specifications/payroll-calculations-and-business-rules-specification.pdf?modified=20260401012317 |
| $78,101-$180,000 | 33% | https://www.ird.govt.nz/-/media/project/ir/home/documents/digital-service-providers/software-providers/payroll-calculations-business-rules-specifications/payroll-calculations-and-business-rules-specification.pdf?modified=20260401012317 |
| Above $180,000 | 39% | https://www.ird.govt.nz/-/media/project/ir/home/documents/digital-service-providers/software-providers/payroll-calculations-business-rules-specifications/payroll-calculations-and-business-rules-specification.pdf?modified=20260401012317 |

Sources: [S22](https://www.ird.govt.nz/calculate-lump-sum-paye), [S24](https://www.ird.govt.nz/employing-staff/payday-filing/non-standard-filing-of-employment-information/lump-sum-payments/calculate-paye-for-a-lump-sum-payment-end-of-employment) and [S2, section 5.11](https://www.ird.govt.nz/-/media/project/ir/home/documents/digital-service-providers/software-providers/payroll-calculations-business-rules-specifications/payroll-calculations-and-business-rules-specification.pdf?modified=20260401012317). The web tables explicitly include the first dollar of each band. Do not copy the specification's inconsistent 'greater than $15,601/$53,501/$78,101' wording and leave those boundary amounts unassigned. An employee can elect a higher 17.5%, 30%, 33% or 39% income-tax rate where applicable; establish the instruction before using it. [S2, section 5.11](https://www.ird.govt.nz/-/media/project/ir/home/documents/digital-service-providers/software-providers/payroll-calculations-business-rules-specifications/payroll-calculations-and-business-rules-specification.pdf?modified=20260401012317)

Calculate ACC separately. For an ordinary levy-liable extra payment, the levy base is the lesser of E and the positive amount remaining from **$156,641 minus B**. Multiply that base by **1.75%**. Thus a payment crossing the cap has levy only on the part below the cap; do not simply levy all or none because G crosses it. Redundancy payments, retiring allowances and ESS benefits are not liable for this earners' levy; use the selected ESS rules below for the benefit's other treatment. Add the unrounded income-tax and levy components, then truncate the total to cents. These are the specified withholding calculations; they do not determine the employee's final multi-employer annual ACC position. [S2, sections 5.11-5.12](https://www.ird.govt.nz/-/media/project/ir/home/documents/digital-service-providers/software-providers/payroll-calculations-business-rules-specifications/payroll-calculations-and-business-rules-specification.pdf?modified=20260401012317), [S22](https://www.ird.govt.nz/calculate-lump-sum-paye), [S24](https://www.ird.govt.nz/employing-staff/payday-filing/non-standard-filing-of-employment-information/lump-sum-payments/calculate-paye-for-a-lump-sum-payment-end-of-employment)

For a tailored code, follow the certificate rather than the table. For a confirmed redundancy payment or retiring allowance, remove the earners' levy included in that rate and mark the earnings as not liable for ACC on the employment information. For example, a 24% certificate rate less the 2026-27 levy of 1.75 percentage points is **22.25%**. The specification's printed 22.58% example is an arithmetic error; do not use it. Resolve the actual certificate and payment classification before applying this adjustment. [S2, section 5.11, PDF pages 45 and 51](https://www.ird.govt.nz/-/media/project/ir/home/documents/digital-service-providers/software-providers/payroll-calculations-business-rules-specifications/payroll-calculations-and-business-rules-specification.pdf?modified=20260401012317), [S22](https://www.ird.govt.nz/calculate-lump-sum-paye)

### Extra pay when employment ends

For payments arising from the end of employment, use the **last 2 paid regular pay periods before the period containing the extra payment**, excluding other extra pays. Skip unpaid periods and out-of-cycle payments. Do not annualise the current termination-period wage or automatically use the last 4 calendar weeks. Total the 2 paid periods and multiply by 26 for weekly, 13 for fortnightly, 6.5 for four-weekly or 6 for monthly pay. When those 2 periods have different frequencies, annualise each at its own frequency and average the 2 annual values. With only one earlier paid period, annualise that period at its frequency. If no prior period exists, resolve the applicable employee instruction and IRD method before calculating. [S2, section 5.12, PDF pages 55-64](https://www.ird.govt.nz/-/media/project/ir/home/documents/digital-service-providers/software-providers/payroll-calculations-business-rules-specifications/payroll-calculations-and-business-rules-specification.pdf?modified=20260401012317), [S24](https://www.ird.govt.nz/employing-staff/payday-filing/non-standard-filing-of-employment-information/lump-sum-payments/calculate-paye-for-a-lump-sum-payment-end-of-employment)

Add the secondary low threshold where applicable, then the extra payment, and use the same rate/levy steps above. Combine other extra pay paid together with termination extra pay for this calculation; do not calculate each under a different annualisation method. Keep each component's ACC character: a normal bonus does not become levy-exempt merely because it accompanies redundancy pay. These end-of-employment instructions apply to payments on or after 1 April 2025; the rates and levy amounts here are for 2026-27. [S2, section 5.12](https://www.ird.govt.nz/-/media/project/ir/home/documents/digital-service-providers/software-providers/payroll-calculations-business-rules-specifications/payroll-calculations-and-business-rules-specification.pdf?modified=20260401012317), [S24](https://www.ird.govt.nz/employing-staff/payday-filing/non-standard-filing-of-employment-information/lump-sum-payments/calculate-paye-for-a-lump-sum-payment-end-of-employment)

### Student loans, regular bonuses and reporting

For primary M SL/ME SL extra pay, combine regular and extra taxable pay for the pay period, truncate that combined pay to whole dollars, subtract the period repayment threshold once and apply 12% to any positive excess, or the valid certificate rate. Truncate the loan deduction to cents. Do not give a second threshold if wages have already used it. When the extra pay is separate and total period pay cannot be established, apply the appropriate loan rate to the entire extra pay. Secondary SL extra pay has no ordinary threshold: truncate the relevant pay to whole dollars, apply 12% or the certificate rate and truncate to cents. Tailored codes follow the certificate's threshold instruction. Keep PAYE and loan deductions separate. [S2, sections 5.11-5.12](https://www.ird.govt.nz/-/media/project/ir/home/documents/digital-service-providers/software-providers/payroll-calculations-business-rules-specifications/payroll-calculations-and-business-rules-specification.pdf?modified=20260401012317), [S23](https://www.ird.govt.nz/employing-staff/payday-filing/non-standard-filing-of-employment-information/lump-sum-payments)

Regular incentive/production bonuses paid with normal wages are included in normal period pay. For a monthly bonus covering several pay periods, calculate monthly PAYE on that month's wages with and without the bonus and deduct the difference. For a bonus covering several months, divide it by those months, calculate the difference between monthly PAYE with and without that monthly share, then multiply the difference by the number of months. Apply the corresponding loan method for an SL code. This is the regular-bonus method, not an annual/special lump-sum rate selection. [S2, section 5.13](https://www.ird.govt.nz/-/media/project/ir/home/documents/digital-service-providers/software-providers/payroll-calculations-business-rules-specifications/payroll-calculations-and-business-rules-specification.pdf?modified=20260401012317)

For an enrolled KiwiSaver employee, a confirmed redundancy payment is excluded from employee KiwiSaver deductions; do not assume the same exclusion for every other extra payment. Check the contribution base and notices separately. Report a lowest-rate extra payment using the low-rate indicator. For separate extra-pay reporting, file within 2 working days electronically or 10 working days on paper. IRD permits inclusion in the next regular electronic schedule only when reported before the relevant deduction-payment end date: month-end for monthly remitters, or the 15th/month-end for twice-monthly remitters. Record which permitted reporting route was used. [S23](https://www.ird.govt.nz/employing-staff/payday-filing/non-standard-filing-of-employment-information/lump-sum-payments), [S2, section 5.11.3](https://www.ird.govt.nz/-/media/project/ir/home/documents/digital-service-providers/software-providers/payroll-calculations-business-rules-specifications/payroll-calculations-and-business-rules-specification.pdf?modified=20260401012317)


## Worked cases

These fictional cases assume the stated code, eligibility, contribution base and notices have already been established. They check the arithmetic of the selected rules, not an actual person's liability. Tolerance is zero, so a cent error fails.

**Case 1: M monthly, annualise before dropping cents.** Confirmed ordinary M pay of $5,000.99 a month gives annual whole-dollar income $60,011. Annual tax is $10,223.80 and ACC is $1,050.1925. Weekly truncation gives $216.80, then monthly PAYE **$939.46**. Direct annual-to-monthly truncation would give $939.49 and skips the required weekly step. [S2, section 5.2](https://www.ird.govt.nz/-/media/project/ir/home/documents/digital-service-providers/software-providers/payroll-calculations-business-rules-specifications/payroll-calculations-and-business-rules-specification.pdf?modified=20260401012317)

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

**Case 2: M monthly with capped ACC.** Confirmed ordinary M pay of $15,000 a month annualises to $180,000. The annual ACC component is the stated **$2,741.22** maximum. PAYE including that component is **$4,334.89** a month. [S2, section 5.2](https://www.ird.govt.nz/-/media/project/ir/home/documents/digital-service-providers/software-providers/payroll-calculations-business-rules-specifications/payroll-calculations-and-business-rules-specification.pdf?modified=20260401012317)

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

**Case 3: ME weekly with IETC abatement.** An employee with a confirmed ME declaration and IETC eligibility earns $1,300 weekly. Annualised income is $67,600, so the payroll credit is **$312** after abatement. Weekly PAYE including ACC and that credit is **$257.14**. This example assumes eligibility; salary alone does not establish it. [S2, section 5.3](https://www.ird.govt.nz/-/media/project/ir/home/documents/digital-service-providers/software-providers/payroll-calculations-business-rules-specifications/payroll-calculations-and-business-rules-specification.pdf?modified=20260401012317), [S18](https://www.ird.govt.nz/income-tax/income-tax-for-individuals/individual-tax-credits/independent-earner-tax-credit-ietc)

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

**Case 4: primary monthly SL near the threshold.** Ordinary M SL monthly gross pay of $2,011.99 becomes $2,011 for the loan calculation. Subtracting the **$2,010.66** threshold leaves $0.34; 12% truncated to cents is **$0.04**. There is no exemption or special-rate notice in this example. [S2, section 5.4](https://www.ird.govt.nz/-/media/project/ir/home/documents/digital-service-providers/software-providers/payroll-calculations-business-rules-specifications/payroll-calculations-and-business-rules-specification.pdf?modified=20260401012317)

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

**Case 5: primary weekly SL with no positive excess.** Ordinary M SL weekly pay of $464.99 becomes $464, matching the threshold, so the loan deduction is **$0.00**. [S2, section 5.4](https://www.ird.govt.nz/-/media/project/ir/home/documents/digital-service-providers/software-providers/payroll-calculations-business-rules-specifications/payroll-calculations-and-business-rules-specification.pdf?modified=20260401012317)

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

**Case 6: secondary SH SL has no ordinary loan threshold.** An employee's declared total annual income is $75,000 and the confirmed code for this second job is SH SL. Ordinary weekly pay of $300.99 becomes $300 for these calculations. PAYE including ACC is **$95.25** and the separate loan deduction is **$36.00**. Being below the main-job weekly threshold does not make this secondary loan deduction zero. No special rate or exemption applies here. [S2, section 5.6](https://www.ird.govt.nz/-/media/project/ir/home/documents/digital-service-providers/software-providers/payroll-calculations-business-rules-specifications/payroll-calculations-and-business-rules-specification.pdf?modified=20260401012317), [S21](https://www.ird.govt.nz/repaying-my-student-loan-when-i-earn-salary-or-wages)

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

**Case 7: ordinary ND includes ACC.** Without a completed declaration or superseding Inland Revenue instruction, ordinary ND pay of $457.89 becomes $457. The combined 46.75% deduction truncates to **$213.64**; adding ACC again overstates the deduction. [S2, section 5.8](https://www.ird.govt.nz/-/media/project/ir/home/documents/digital-service-providers/software-providers/payroll-calculations-business-rules-specifications/payroll-calculations-and-business-rules-specification.pdf?modified=20260401012317)

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

**Case 8: main-job tailored certificate.** Assume a valid weekly certificate requires 20% PAYE including ACC and 8% loan deductions above $464. On $1,000.99, use the $1,000 whole-dollar base: **$200.00 PAYE** and a separate **$42.88 loan deduction**. [S2, section 5.9](https://www.ird.govt.nz/-/media/project/ir/home/documents/digital-service-providers/software-providers/payroll-calculations-business-rules-specifications/payroll-calculations-and-business-rules-specification.pdf?modified=20260401012317)

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

**Case 9: secondary certificate has no threshold.** Assume a valid secondary certificate requires 18% PAYE including ACC and 8% loan deductions on every dollar. Weekly pay of $300.99 gives **$54.00 PAYE** and **$24.00 loan deductions** on $300. Do not subtract the primary $464 threshold. [S2, section 5.9](https://www.ird.govt.nz/-/media/project/ir/home/documents/digital-service-providers/software-providers/payroll-calculations-business-rules-specifications/payroll-calculations-and-business-rules-specification.pdf?modified=20260401012317)

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

**Case 10: one loan threshold for combined pay.** An M SL employee receives $400 regular weekly pay and $200.99 extra pay together. Combined pay truncates to $600; subtract $464 once. The total loan deduction for this pay is **$16.32**. No special certificate applies. [S2, section 5.11](https://www.ird.govt.nz/-/media/project/ir/home/documents/digital-service-providers/software-providers/payroll-calculations-business-rules-specifications/payroll-calculations-and-business-rules-specification.pdf?modified=20260401012317), [S23](https://www.ird.govt.nz/employing-staff/payday-filing/non-standard-filing-of-employment-information/lump-sum-payments)

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

**Case 11: bonus crosses the ACC cap.** An ordinary primary-code bonus of $30,000.56 follows $10,000 of regular payments in the relevant 4-week window. Annualised pay is $130,000; G is $160,000, selecting 33%. Only $26,641 of the bonus attracts 1.75% ACC. Retain $9,900.1848 tax and $466.2175 levy until the final cent truncation: **$10,366.40 PAYE**. The specification example prints $10,366.39 after prematurely shortening components; this case follows its explicit calculation sequence. [S2, section 5.11.1, PDF pages 47-48](https://www.ird.govt.nz/-/media/project/ir/home/documents/digital-service-providers/software-providers/payroll-calculations-business-rules-specifications/payroll-calculations-and-business-rules-specification.pdf?modified=20260401012317), [S22](https://www.ird.govt.nz/calculate-lump-sum-paye)

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

**Case 12: secondary threshold affects the cap.** An ST-code bonus of $40,000 follows $4,695 regular pay in the relevant 4 weeks. Annualised pay $61,035 plus the ST low threshold $78,101 gives B of $139,136 and G of $179,136. Tax is 33% of the bonus; ACC applies to only $17,505. Total PAYE is **$13,506.33**, leaving **$26,493.67** before other deductions. [S2, section 5.11.2, PDF pages 52-55](https://www.ird.govt.nz/-/media/project/ir/home/documents/digital-service-providers/software-providers/payroll-calculations-business-rules-specifications/payroll-calculations-and-business-rules-specification.pdf?modified=20260401012317), [S22](https://www.ird.govt.nz/calculate-lump-sum-paye)

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

**Case 13: signing bonus before any regular payment.** An M-code employee receives a $10,000 levy-liable signing bonus with no earlier regular pay in the window and no higher-rate election. Annualised pay is zero, so the 10.5% income-tax rate and 1.75% levy give **$1,225.00 PAYE**. Set the low-rate extra-pay indicator. A future contractual salary is not substituted for historical payments. [S2, section 5.11.1, PDF page 49](https://www.ird.govt.nz/-/media/project/ir/home/documents/digital-service-providers/software-providers/payroll-calculations-business-rules-specifications/payroll-calculations-and-business-rules-specification.pdf?modified=20260401012317), [S22](https://www.ird.govt.nz/calculate-lump-sum-paye)

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

**Case 14: first dollar of a new extra-pay band.** With $52,000 annualised regular pay, a $1,500 primary bonus gives G of $53,500 and **$288.75 PAYE** at 17.5% plus levy. A $1,501 bonus gives G of $53,501 and **$476.56 PAYE** at 30% plus levy. The higher rate applies to the whole bonus, not just its last dollar. [S2, section 5.11](https://www.ird.govt.nz/-/media/project/ir/home/documents/digital-service-providers/software-providers/payroll-calculations-business-rules-specifications/payroll-calculations-and-business-rules-specification.pdf?modified=20260401012317), [S22](https://www.ird.govt.nz/calculate-lump-sum-paye)

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

**Case 15: termination skips unpaid and current periods.** The last 2 paid weekly periods before the termination period contain $550 and $650, with an intervening unpaid week. Ignore that unpaid week and the current $500 wage. A confirmed $1,000 redundancy payment gives annualised pay $31,200 and G $32,200: **$175.00 PAYE**, with no earners' levy on redundancy. [S2, section 5.12](https://www.ird.govt.nz/-/media/project/ir/home/documents/digital-service-providers/software-providers/payroll-calculations-business-rules-specifications/payroll-calculations-and-business-rules-specification.pdf?modified=20260401012317), [S24](https://www.ird.govt.nz/employing-staff/payday-filing/non-standard-filing-of-employment-information/lump-sum-payments/calculate-paye-for-a-lump-sum-payment-end-of-employment)

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

**Case 16: termination after a frequency change.** The last 2 paid periods before termination are $800 weekly and $1,720 fortnightly. Average their annualised values to get $43,160. A separate $1,000 levy-liable bonus paid because employment ends gives G of $44,160 and **$192.50 PAYE**. Assume no secondary code or higher-rate election. [S2, section 5.12, PDF page 64](https://www.ird.govt.nz/-/media/project/ir/home/documents/digital-service-providers/software-providers/payroll-calculations-business-rules-specifications/payroll-calculations-and-business-rules-specification.pdf?modified=20260401012317), [S24](https://www.ird.govt.nz/employing-staff/payday-filing/non-standard-filing-of-employment-information/lump-sum-payments/calculate-paye-for-a-lump-sum-payment-end-of-employment)

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

**Case 17: combined termination payments keep their levy character.** The last 2 paid monthly periods before termination are $5,500 and $7,600; ignore a later unpaid month and the current termination-period wage. A confirmed $15,000 redundancy payment and $500 ordinary bonus are paid together. Annualised pay is $78,600; G $94,100 selects 33% on all $15,500. Only the $500 bonus attracts ACC: total **$5,123.75 PAYE**, leaving **$10,376.25** before other deductions. [S2, section 5.12, PDF pages 62-63](https://www.ird.govt.nz/-/media/project/ir/home/documents/digital-service-providers/software-providers/payroll-calculations-business-rules-specifications/payroll-calculations-and-business-rules-specification.pdf?modified=20260401012317), [S24](https://www.ird.govt.nz/employing-staff/payday-filing/non-standard-filing-of-employment-information/lump-sum-payments/calculate-paye-for-a-lump-sum-payment-end-of-employment)

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

**Case 18: remove the levy from a tailored redundancy rate.** Assume a valid 24% salary/wage certificate rate includes 1.75% ACC and the $1,000 payment is confirmed redundancy. The applicable rate excluding levy is **22.25%**, giving **$222.50**. Mark the earnings not liable for ACC. This is conditional arithmetic, not a determination that any actual payment qualifies. [S2, section 5.11](https://www.ird.govt.nz/-/media/project/ir/home/documents/digital-service-providers/software-providers/payroll-calculations-business-rules-specifications/payroll-calculations-and-business-rules-specification.pdf?modified=20260401012317)

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

**Case 19: regular bonus covering 3 months.** An ordinary M-code employee earns $5,000 monthly and receives a $1,200 regular bonus covering 3 months. The $400 monthly share gives monthly PAYE of $1,066.17 on $5,400 versus $939.20 on $5,000, using the weekly-first truncation method above. The bonus PAYE is **$380.91**: 3 times the $126.97 monthly difference. Assume the same facts for the covered months and no SL code, tailored certificate or other adjustment. [S2, sections 5.1 and 5.13](https://www.ird.govt.nz/-/media/project/ir/home/documents/digital-service-providers/software-providers/payroll-calculations-business-rules-specifications/payroll-calculations-and-business-rules-specification.pdf?modified=20260401012317)

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

**Case 20: NSW ordinary pay with cents.** Assume a valid NSW code, $457.89 weekly ordinary taxable pay, no exceptional levy adjustment and no other deduction. Whole-dollar pay is $457; $55.9825 truncates to $55.98 PAYE, leaving $401.91 of actual pay. [S2](https://www.ird.govt.nz/-/media/project/ir/home/documents/digital-service-providers/software-providers/payroll-calculations-business-rules-specifications/payroll-calculations-and-business-rules-specification.pdf?modified=20260401012317), [S13](https://www.ird.govt.nz/-/media/project/ir/home/documents/forms-and-guides/ir300---ir399/ir335/ir335.pdf?modified=20250811232131), [S92](https://www.ird.govt.nz/income-tax/income-tax-for-individuals/tax-codes-and-tax-rates-for-individuals/what-tax-code-should-i-use)

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

**Case 21: NSW fortnightly flat calculation.** Assume a valid NSW code and $2,000.99 fortnightly ordinary taxable pay with no other deduction or exceptional adjustment. Apply the same flat method to $2,000; do not annualise or multiply a weekly deduction. PAYE is $245 and ordinary net pay is $1,755.99. [S2](https://www.ird.govt.nz/-/media/project/ir/home/documents/digital-service-providers/software-providers/payroll-calculations-business-rules-specifications/payroll-calculations-and-business-rules-specification.pdf?modified=20260401012317), [S13](https://www.ird.govt.nz/-/media/project/ir/home/documents/forms-and-guides/ir300---ir399/ir335/ir335.pdf?modified=20250811232131), [S92](https://www.ird.govt.nz/income-tax/income-tax-for-individuals/tax-codes-and-tax-rates-for-individuals/what-tax-code-should-i-use)

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

**Case 22: RSE first-month NSW exception.** Assume the worker is within the statutory first month of an established RSE period of employment, has not yet supplied IR330 and is entitled to the clause 3 NSW exception. On $1,000.99 ordinary weekly pay, PAYE is $122.50 and net pay before any other deduction is $878.49. The arithmetic assumes the exception; it does not establish its start or end date. [S2](https://www.ird.govt.nz/-/media/project/ir/home/documents/digital-service-providers/software-providers/payroll-calculations-business-rules-specifications/payroll-calculations-and-business-rules-specification.pdf?modified=20260401012317), [S94](https://www.legislation.govt.nz/act/public/1994/166/en/latest/sections/DLM1253911/), [S95](https://www.legislation.govt.nz/act/public/1994/166/en/latest/sections/DLM1253915/), [S97](https://www.legislation.govt.nz/act/public/1994/166/en/latest/sections/LMS195590/)

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

**Case 23: ND after the RSE exception ends.** Assume that first-month exception has ended, the ordinary section 24E non-notified conditions are established, no applicable Commissioner code exists and the worker still has not supplied the required notification. On $1,000.99 ordinary weekly pay, the ND method gives $467.50 PAYE and $533.49 before other deductions. A properly notified continuing NSW worker would not use this case. [S2](https://www.ird.govt.nz/-/media/project/ir/home/documents/digital-service-providers/software-providers/payroll-calculations-business-rules-specifications/payroll-calculations-and-business-rules-specification.pdf?modified=20260401012317), [S95](https://www.legislation.govt.nz/act/public/1994/166/en/latest/sections/DLM1253915/), [S97](https://www.legislation.govt.nz/act/public/1994/166/en/latest/sections/LMS195590/)

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

**Case 24: CAE ordinary allowances and separate extra pay.** Assume valid CAE employment, $400.37 ordinary wages, $57.52 taxable allowances, $20 non-taxable allowances and a separately classified $100 extra payment. Ordinary taxable pay is $457.89, truncated to $457; ordinary PAYE is $87.97. The ordinary cash component is $477.89, leaving $389.92 before any other deduction. The $100 extra pay and its deductions must be calculated separately and are excluded from this result; assume no KiwiSaver contribution is due on these established facts. [S2](https://www.ird.govt.nz/-/media/project/ir/home/documents/digital-service-providers/software-providers/payroll-calculations-business-rules-specifications/payroll-calculations-and-business-rules-specification.pdf?modified=20260401012317), [S13](https://www.ird.govt.nz/-/media/project/ir/home/documents/forms-and-guides/ir300---ir399/ir335/ir335.pdf?modified=20250811232131), [S92](https://www.ird.govt.nz/income-tax/income-tax-for-individuals/tax-codes-and-tax-rates-for-individuals/what-tax-code-should-i-use)

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

**Case 25: EDW ordinary pay.** Assume qualifying election work within the permitted period, a valid EDW code, $1,000.99 ordinary weekly pay, no KiwiSaver contribution due on the established facts and no other deduction or exceptional adjustment. Whole-dollar pay is $1,000, PAYE is $192.50 and net pay is $808.49. Work outside the qualifying election period needs the appropriate ordinary declaration. [S2](https://www.ird.govt.nz/-/media/project/ir/home/documents/digital-service-providers/software-providers/payroll-calculations-business-rules-specifications/payroll-calculations-and-business-rules-specification.pdf?modified=20260401012317), [S13](https://www.ird.govt.nz/-/media/project/ir/home/documents/forms-and-guides/ir300---ir399/ir335/ir335.pdf?modified=20250811232131), [S92](https://www.ird.govt.nz/income-tax/income-tax-for-individuals/tax-codes-and-tax-rates-for-individuals/what-tax-code-should-i-use)

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

## When to refuse or refer

An unknown classification, contribution base or notice is an input gap. Do not invent a resident tax code, a pension exemption or a flat PAYE percentage. Ordinary salary rules do not establish the treatment of contractors, non-residents, offshore employers, IR56 workers, benefits or paid parental leave. The selected extra-pay methods below require an established payment classification; they do not determine employment-law entitlements.


Still requiring separate actual-case checks: special PAYE codes beyond the selected ordinary NSW/CAE/EDW, certificate and extra-pay methods; exemption eligibility, recovery notices beyond the selected methods, other irregular pays and unresolved competing-notice/attachment cases; actual ESS scheme eligibility and receipt failures, legacy approvals and historic transitions, difficult valuations, replacement schemes and classification beyond the selected employee methods; schedular payments and payment classification; enrolment exceptions and mixed/late refund cases beyond the selected administration; historical-rate evidence, contribution classifications and legacy scheme offsets; cross-border employment and treaty/social-security questions; FBT; leave, holiday pay, minimum wage and termination entitlements; employer ACC invoices; employment-record requirements beyond selected tax retention; older/exceptional corrections, mixed EMP debt, current interest, other shortfall/criminal penalties and full remission/collection rules. No whole payroll, social-contribution or compliance topic is certified complete by this guide. It remains tier 2 and pending qualified review.

## Sources

| Source | URL | Read on | What was read |
| --- | --- | --- | --- |
| Salary and wage deductions | https://www.ird.govt.nz/deductions | 2026-11-13 | Read for Scope and who this is for, PAYE and the employee ACC levy (read by Ryan Duguid) |
| 2026-27 payroll specification, selected sections | https://www.ird.govt.nz/-/media/project/ir/home/documents/digital-service-providers/software-providers/payroll-calculations-business-rules-specifications/payroll-calculations-and-business-rules-specification.pdf?modified=20260401012317 | 2026-11-14 | Read for Scope and who this is for, PAYE and the employee ACC levy, Ordinary M and ME calculations, Ordinary secondary codes and ND; reopened on 2026-11-14 for the annual PAYE formula, earners' levy, student-loan threshold, NSW rate and ESCT table (2026-27 specification dated 24 March 2026, version 1.0) |
| Registering as an employer | https://www.ird.govt.nz/setting-up-a-business-or-organisation | 2026-11-13 | Read for Ask the client first (read by Ryan Duguid) |
| Deductions from income | https://www.ird.govt.nz/employing-staff/deductions-from-income | 2026-11-13 | Read for PAYE and the employee ACC levy (read by Ryan Duguid) |
| ACC earners' levy rates | https://www.ird.govt.nz/income-tax/income-tax-for-individuals/acc-clients-and-carers/acc-earners-levy-rates | 2026-11-14 | Read for PAYE and the employee ACC levy, Ordinary NSW, CAE and EDW calculations; reopened on 2026-11-14 for the 2026-27 earners' levy rate, maximum earnings and maximum levy |
| IR335 employer guide, September 2026, selected pages | https://www.ird.govt.nz/-/media/project/ir/home/documents/forms-and-guides/ir300---ir399/ir335/ir335.pdf?modified=20250811232131 | 2026-11-13 | Read for PAYE and the employee ACC levy, Ordinary NSW, CAE and EDW calculations, Worked cases (read by Ryan Duguid) |
| Levy responsibilities; not the source for dated rates | https://www.acc.co.nz/for-business/understanding-levies-if-you-work-or-own-a-business | 2026-11-13 | Read for PAYE and the employee ACC levy (read by Ryan Duguid) |
| ietc-eligibility | https://www.ird.govt.nz/income-tax/income-tax-for-individuals/individual-tax-credits/independent-earner-tax-credit-ietc | 2026-11-13 | Read for Ordinary M and ME calculations, Worked cases (read by Ryan Duguid) |
| ietc-salary | https://www.ird.govt.nz/income-tax/income-tax-for-individuals/individual-tax-credits/independent-earner-tax-credit-ietc/getting-the-independent-earner-tax-credit-if-you-earn-salary-or-wages | 2026-11-13 | Read for Ordinary M and ME calculations (read by Ryan Duguid) |
| about-tax-codes | https://www.ird.govt.nz/income-tax/income-tax-for-individuals/tax-codes-and-tax-rates-for-individuals/about-tax-codes | 2026-11-13 | Read for Ordinary secondary codes and ND (read by Ryan Duguid) |
| IRD tax-code eligibility, updated 30 April 2026; includes collapsed sections | https://www.ird.govt.nz/income-tax/income-tax-for-individuals/tax-codes-and-tax-rates-for-individuals/what-tax-code-should-i-use | 2026-11-13 | Read for Ordinary NSW, CAE and EDW calculations, Worked cases (read by Ryan Duguid) |
| Income Tax Act YA 1 selected worker, market value and year definitions, copy 4 September 2026 | https://www.legislation.govt.nz/act/public/2007/97/en/latest/sections/DLM1520575/ | 2026-11-13 | Read for Ordinary NSW, CAE and EDW calculations (read by Ryan Duguid) |
| Tax Administration Act 24B, copy 1 October 2026 | https://www.legislation.govt.nz/act/public/1994/166/en/latest/sections/DLM1252632/ | 2026-11-13 | Read for Ordinary NSW, CAE and EDW calculations (read by Ryan Duguid) |
| Tax Administration Act 24C, copy 1 October 2026 | https://www.legislation.govt.nz/act/public/1994/166/en/latest/sections/DLM1253911/ | 2026-11-13 | Read for Ordinary NSW, CAE and EDW calculations, Worked cases (read by Ryan Duguid) |
| Tax Administration Act 24E, copy 1 October 2026 | https://www.legislation.govt.nz/act/public/1994/166/en/latest/sections/DLM1253915/ | 2026-11-13 | Read for Ordinary NSW, CAE and EDW calculations, Worked cases (read by Ryan Duguid) |
| Tax Administration Act 24D, copy 1 October 2026 | https://www.legislation.govt.nz/act/public/1994/166/en/latest/sections/LMS193078/ | 2026-11-13 | Read for Ordinary NSW, CAE and EDW calculations (read by Ryan Duguid) |
| Tax Administration Act Schedule 5 Part A clauses 1-4/rows 7-9 and Part B clause 3, copy 1 October 2026 | https://www.legislation.govt.nz/act/public/1994/166/en/latest/sections/LMS195590/ | 2026-11-13 | Read for Ordinary NSW, CAE and EDW calculations, Worked cases (read by Ryan Duguid) |
| student-loan-salary | https://www.ird.govt.nz/repaying-my-student-loan-when-i-earn-salary-or-wages | 2026-11-13 | Read for Ordinary student-loan deductions, Worked cases (read by Ryan Duguid) |
| Non-termination lump-sum PAYE, updated 18 May 2026 | https://www.ird.govt.nz/calculate-lump-sum-paye | 2026-11-13 | Read for Extra pay: choose the calculation before choosing a rate, Worked cases (read by Ryan Duguid) |
| IRD lump sum payments, updated 27 January 2026 | https://www.ird.govt.nz/employing-staff/payday-filing/non-standard-filing-of-employment-information/lump-sum-payments | 2026-11-13 | Read for Extra pay: choose the calculation before choosing a rate, Student loans, regular bonuses and reporting, Worked cases (read by Ryan Duguid) |
| End-of-employment lump-sum PAYE, updated 20 April 2026 | https://www.ird.govt.nz/employing-staff/payday-filing/non-standard-filing-of-employment-information/lump-sum-payments/calculate-paye-for-a-lump-sum-payment-end-of-employment | 2026-11-13 | Read for Extra pay: choose the calculation before choosing a rate, Extra pay when employment ends, Worked cases (read by Ryan Duguid) |

Not yet confirmed: the rows below were read by Ryan Duguid on 12 and 13 November 2026, and only the spot-checked figures listed in the PR were reopened on 14 November 2026. Inherited sources checked 12 November 2026; selected ESS sources checked 13 November 2026. Selected District Court Act sections use the current copy dated 17 February 2026; Tax Administration Act section 157 uses the current copy dated 1 October 2026. SPS 21/01 is dated 12 April 2021 and remains linked by IRD's arrears page updated 16 April 2026. Extra-pay and deduction examples are recalculated from the stated rules; known inconsistent printed examples and boundary wording are recorded in the verification log. The technical specification is dated 24 March 2026, version 1.0, and expressly covers 1 April 2026 to 31 March 2027. IR335's cover says September 2026. KS4's cover says April 2026. Selected KiwiSaver Act provisions use the current copy dated 1 April 2026. The verification log records the selected native/image page scope, the surviving legacy default and conflicting sample-letter/example wording. The selected correction regulations use the 30 March 2026 consolidation. Selected TAA record, assessment and penalty provisions use the 1 October 2026 copy. Its full-Act page flags unincorporated amendments; the selected amendment-impact check is recorded in the verification log. SPS19/04 is dated 30 May 2019. Current statutory wording controls the affected-employee penalty base and inclusive $100 exemption. These checks do not claim full PDF or statute review. Employer ACC Work and Working Safer levy invoices are not calculated.

## Today's figures and who stands behind this skill

This file is an AI skill (tax rules your AI follows) from OpenAccountants, copied on 2026-11-14. Rates, thresholds and deadlines change. For the current version of this skill, its official sources and the named accountant (if any) who stands behind it, call `get_skill` with slug `nz-employer-payroll` on the OpenAccountants connector (https://www.openaccountants.com/connect), or read https://www.openaccountants.com/skills/nz-employer-payroll. If neither is available, confirm every figure against the official source pages cited above before relying on it.
