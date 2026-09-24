---
name: sweden-payroll
description: Use this skill whenever asked about Swedish payroll processing, employee salary calculations, preliminärskatt (preliminary income tax / PAYE), arbetsgivaravgifter (employer social contributions), employer cost calculations, net-to-gross or gross-to-net conversions, Swedish payslip structure, arbetsgivardeklaration filings, or any question about computing wages, deductions, or employer obligations in Sweden. Trigger on phrases like "Swedish payroll", "preliminärskatt", "arbetsgivaravgifter", "employer contributions Sweden", "PAYE Sweden", "net salary Sweden", "lönespecifikation", "kommunalskatt", "municipal tax Sweden", "statlig inkomstskatt", "Skatteverket filing", "kollektivavtal", "ITP pension", or "semesterersättning".
version: 1.0
jurisdiction: SE
tax_year: 2026
last_updated: 2026-09-24
authored_by: OpenAccountants team
review_status: pending_review
depends_on:
  - payroll-workflow-base
category: payroll
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Sweden payroll and PAYE

Applies to tax year 2026. Check the payment date, current tax decision and employer-specific filing deadline before calculating or filing.

## 1. Scope

Use this method for an employer that pays remuneration for work and must operate Swedish PAYE. It covers the monthly route from payroll inputs through the individual PAYE return, tax-account payment and corrections. It identifies the ordinary foreign-employer and social-security branches. It does not calculate a flat employee tax rate: withholding depends on the payee's main/supplementary-income status and the Tax Agency tax-table or decision. [Skatteverket](https://www.skatteverket.se/servicelankar/otherlanguages/englishengelska/businessesandemployers/startingandrunningaswedishbusiness/declaringtaxesbusinesses/filingapayereturn/deductedtax.4.2fb39afe18dabf1e4d255d0.html)

Before using an ordinary Swedish contribution calculation, establish where work is done, the employer's Swedish permanent-establishment status, the employee's social-security coverage, and whether an A1/Certificate of Coverage or social-security agreement applies. An A1 or convention fact can change contributions while Swedish withholding/reporting remains relevant. [Skatteverket](https://www.skatteverket.se/servicelankar/otherlanguages/englishengelska/businessesandemployers/startingandrunningaswedishbusiness/hiringworkersfromabroad.4.6532ae7518aff8c118f984.html) [Skatteverket](https://www.skatteverket.se/servicelankar/otherlanguages/englishengelska/businessesandemployers/nonswedishbusinesseswithoperationsinsweden/registerabusiness.4.676f4884175c97df41917fa.html)

## Ask the client first

- What are the pay date, cash/benefit components, tax-table decision, birth year and coverage facts? Obtain the evidence below.

### Gather and lock the payroll record

For each payee and pay date retain: contract/engagement and work-location facts; correct personal or coordination number (or the prescribed alternative identity and foreign address); the current A-tax certificate's **table number and column**, pay frequency, any adjustment decision or SINK decision, and whether income is main or supplementary; birth year and age at 1 January 2026; gross cash pay; separately itemised taxable benefits and employee net payments; expenses, holiday/final-pay character and pension/equity/severance facts; the A1/coverage/posting/agreement document, issuing authority and effective coverage dates; evidence that the employer's Swedish registration and tax-account route has been confirmed; prior PAYE reports and the employer deadline. [Skatteverket](https://www.skatteverket.se/servicelankar/otherlanguages/inenglishengelska/individualsandemployees/declaringtaxesforindividuals/ataxcertificateandtaxtables.4.2fb39afe18dabf1e4d25053.html)

Do not use a payslip or payroll-system default as evidence of a tax table, social-security jurisdiction, benefit value or employment-law entitlement. The correct identity is material because individual PAYE data pre-fill the payee's tax return. [Skatteverket](https://www.skatteverket.se/servicelankar/otherlanguages/englishengelska/businessesandemployers/startingandrunningaswedishbusiness/declaringtaxesbusinesses/filingapayereturn/howtofillinthepayetaxreturnboxbybox.4.309a41aa1672ad0c8379f84.html)

## The method, step by step

1. Confirm employer registration, work location, coverage and employee tax decision.
2. Classify cash pay and non-cash benefits, establish contribution bases and apply the correct payment-year rules.
3. Determine withholding, reconcile the bank transfer, submit PAYE and reconcile the tax-account payment.
4. Correct filed errors using the affected period and original specification number.

### Registration and routing

### Ordinary route

Register as an employer before the first salary payment if not already registered. Ordinary employers with employees in Sweden register, deduct tax from salaries/benefits, declare and pay employer contributions. Foreign businesses use the Tax Agency foreign-business registration route when its conditions apply. [Skatteverket](https://www.skatteverket.se/servicelankar/otherlanguages/englishengelska/businessesandemployers/startingandrunningaswedishbusiness/hiringworkersfromabroad.4.6532ae7518aff8c118f984.html) [Skatteverket](https://www.skatteverket.se/servicelankar/otherlanguages/englishengelska/businessesandemployers/nonswedishbusinesseswithoperationsinsweden/registerabusiness.4.676f4884175c97df41917fa.html)

While employer registration remains live, submit a PAYE return for every reporting period. Where there is nothing to report, select the e-service zero-return option. [Skatteverket](https://www.skatteverket.se/servicelankar/otherlanguages/englishengelska/businessesandemployers/startingandrunningaswedishbusiness/declaringtaxesbusinesses/filingapayereturn/howtofillinthepayetaxreturnboxbybox.4.309a41aa1672ad0c8379f84.html)

### Boundary routes

| Facts | Route |
| --- | --- |
| Foreign employer / work in Sweden | Confirm Swedish registration, A-tax or SINK decision, withholding and PAYE obligations. [Skatteverket](https://www.skatteverket.se/servicelankar/otherlanguages/englishengelska/businessesandemployers/startingandrunningaswedishbusiness/hiringworkersfromabroad.4.6532ae7518aff8c118f984.html) |
| A1, Certificate of Coverage or convention | Record the issuing authority and exact coverage period; then confirm the Swedish registration/tax-account route before selecting a contribution code or rate. A certificate label alone does not establish a zero Swedish contribution. Swedish PAYE can be separate. [Skatteverket](https://www.skatteverket.se/servicelankar/otherlanguages/englishengelska/businessesandemployers/nonswedishbusinesseswithoperationsinsweden/registerabusiness.4.676f4884175c97df41917fa.html) |
| No Swedish permanent establishment | Use the distinct Tax Agency foreign-employer table/status rules, including box 302 where applicable. [Skatteverket](https://www.skatteverket.se/servicelankar/otherlanguages/englishengelska/businessesandemployers/startingandrunningaswedishbusiness/declaringtaxesbusinesses/filingapayereturn/employercontributions.4.2fb39afe18dabf1e4d24a3d.html) [Skatteverket](https://www.skatteverket.se/servicelankar/otherlanguages/englishengelska/businessesandemployers/startingandrunningaswedishbusiness/declaringtaxesbusinesses/filingapayereturn/howtofillinthepayetaxreturnboxbybox.4.309a41aa1672ad0c8379f84.html) |
| Social-security agreement | It reallocates the practical contribution task but does not automatically remove employer withholding responsibility. [Skatteverket](https://www.skatteverket.se/servicelankar/otherlanguages/englishengelska/businessesandemployers/startingandrunningaswedishbusiness/declaringtaxesbusinesses/filingapayereturn/socialsecurityagreementforyouasanemployer.4.2fb39afe18dabf1e4d21c41.html) |
| Third-country national | Check right to work; Tax Agency notification has its own end-of-third-month-after-start-month deadline. [Skatteverket](https://www.skatteverket.se/servicelankar/otherlanguages/englishengelska/businessesandemployers/startingandrunningaswedishbusiness/hiringworkersfromabroad.4.6532ae7518aff8c118f984.html) |

## 4. Calculate the pay period

### 4.1 Establish the contribution base

Start with cash gross remuneration for work and add taxable non-cash benefits included in the contribution base. Enter cash gross salary in **box 011**; benefits belong in their appropriate fields, not 011. A taxable benefit is ordinarily reported for the period the employee could use it. Reduce a benefit value by the employee's documented **net** payment for it. [Skatteverket](https://www.skatteverket.se/servicelankar/otherlanguages/englishengelska/businessesandemployers/startingandrunningaswedishbusiness/declaringtaxesbusinesses/filingapayereturn/howtofillinthepayetaxreturnboxbybox.4.309a41aa1672ad0c8379f84.html)

Classify cash reimbursement, pension, option/equity award, termination payment, holiday payment and expense allowance under their specific rule before treating it as ordinary salary. Before applying the rate table, track remuneration for work paid to each **A-tax** payee across the calendar year. Employer contributions are due when that remuneration totals **SEK 1,000 or more** for the year. If a later payment reaches the threshold, rebuild the year-to-date contribution-liable amount and use the PAYE correction/reporting route for the earlier amount as applicable. Do not treat a single payment below SEK 1,000 as an enduring exclusion. [Skatteverket](https://www.skatteverket.se/arbetsgivaravgifter) [Skatteverket](https://www.skatteverket.se/servicelankar/otherlanguages/englishengelska/businessesandemployers/startingandrunningaswedishbusiness/declaringtaxesbusinesses/filingapayereturn/correctingapayereturn.4.13948c0e18e810bfa0c2e34.html)

### 4.2 Apply 2026 employer contributions

The full ordinary 2026 rate is **31.42% of gross salary and benefits**. Apply it only after the A-tax/SEK 1,000 annual gate and the route screen above. [Skatteverket](https://www.skatteverket.se/servicelankar/otherlanguages/englishengelska/businessesandemployers/startingandrunningaswedishbusiness/declaringtaxesbusinesses/filingapayereturn/employercontributions.4.2fb39afe18dabf1e4d24a3d.html) [Skatteverket](https://www.skatteverket.se/arbetsgivaravgifter)

| Employee category / payment period | Rate and calculation |
| --- | --- |
| Born 1959 or later, ordinary work-in-Sweden case | 31.42%; `base × 0.3142`  [Skatteverket](https://www.skatteverket.se/servicelankar/otherlanguages/englishengelska/businessesandemployers/startingandrunningaswedishbusiness/declaringtaxesbusinesses/filingapayereturn/employercontributions.4.2fb39afe18dabf1e4d24a3d.html) |
| Born 1938–1958 | 10.21% pension-only rate  [Skatteverket](https://www.skatteverket.se/servicelankar/otherlanguages/englishengelska/businessesandemployers/startingandrunningaswedishbusiness/declaringtaxesbusinesses/filingapayereturn/employercontributions.4.2fb39afe18dabf1e4d24a3d.html) |
| Born 1937 or earlier | 0%  [Skatteverket](https://www.skatteverket.se/servicelankar/otherlanguages/englishengelska/businessesandemployers/startingandrunningaswedishbusiness/declaringtaxesbusinesses/filingapayereturn/employercontributions.4.2fb39afe18dabf1e4d24a3d.html) |
| Born 2003–2007, pay from 1 April to 31 December 2026 | 20.81% on first SEK 25,000 per calendar month; 31.42% on excess  [Skatteverket](https://www.skatteverket.se/servicelankar/otherlanguages/englishengelska/businessesandemployers/startingandrunningaswedishbusiness/declaringtaxesbusinesses/filingapayereturn/employercontributions.4.2fb39afe18dabf1e4d24a3d.html) |

The temporary measure runs until 30 September 2027, but the birth-year cohort shown here is the 2026 cohort; obtain the applicable 2027 cohort before processing 2027 pay. For the youth band calculate `min(monthly base, 25,000) × 20.81% + max(monthly base − 25,000, 0) × 31.42%`. Do not apply a special payroll-system code, regional support, R&D deduction, growth support, shipping adjustment or posting rate without the applicable eligibility, basis, cap and minimum-contribution evidence. [Skatteverket](https://www.skatteverket.se/servicelankar/otherlanguages/englishengelska/businessesandemployers/startingandrunningaswedishbusiness/declaringtaxesbusinesses/filingapayereturn/employercontributions.4.2fb39afe18dabf1e4d24a3d.html) [Skatteverket](https://www.skatteverket.se/servicelankar/otherlanguages/englishengelska/businessesandemployers/startingandrunningaswedishbusiness/declaringtaxesbusinesses/filingapayereturn/howtofillinthepayetaxreturnboxbybox.4.309a41aa1672ad0c8379f84.html)

### 4.3 Deduct preliminary tax

Use the Tax Agency route that applies:

1. **Main income:** use the current A-tax certificate's table number and the correct column for the payee and pay frequency.
2. **Supplementary income:** 30%. [Skatteverket](https://www.skatteverket.se/servicelankar/otherlanguages/englishengelska/businessesandemployers/startingandrunningaswedishbusiness/declaringtaxesbusinesses/filingapayereturn/deductedtax.4.2fb39afe18dabf1e4d255d0.html)
3. **Specific decision:** the Tax Agency amount/rate, including adjustment or SINK.

Before calculating net pay, lock the current table number, applicable column, pay frequency and any adjustment or SINK decision in the payroll record. Without an A-tax/SINK decision, deduct the municipal table amount for the employer's business area plus 10% (110% of the table amount). Once the decision arrives, use it prospectively and do not correct earlier reports merely because it arrived. If no cash remuneration is paid, no tax can be withheld from a taxable benefit; route the resulting issue before sign-off. For salary advances, withhold in the same proportion as the advance bears to total compensation; if the total is unknown, treat the advance as the total. [Skatteverket](https://www.skatteverket.se/servicelankar/otherlanguages/englishengelska/businessesandemployers/startingandrunningaswedishbusiness/declaringtaxesbusinesses/filingapayereturn/deductedtax.4.2fb39afe18dabf1e4d255d0.html) [Skatteverket](https://www.skatteverket.se/servicelankar/otherlanguages/inenglishengelska/individualsandemployees/declaringtaxesforindividuals/ataxcertificateandtaxtables.4.2fb39afe18dabf1e4d25053.html)

### Ordinary holiday-pay inputs

Check the collective agreement first: permitted variations can replace the statutory calculation. Establish earned paid days and qualifying absence from the leave record. Under the statutory same-pay rule, retain current weekly/monthly salary and fixed supplements; add 0.43% of monthly pay per paid day, or 1.82% for weekly pay. Variable components receive 12%. The percentage rule instead gives 12% of the statutory earning-year base: exclude holiday pay and specified absence/shutdown payments; replace qualifying absence with normal assumed earnings. Use it for non-weekly/monthly pay, regular variable pay of at least 10%, changed working fraction, or disqualifying absence, subject to the statutory exception. It may also be elected otherwise. On termination, value unused earned leave under the same statutory rules; payment is ordinarily due within one month. Preserve any valid contractual variation and its calculation. [Official source](https://data.riksdagen.se/dokument/sfs-1977-480.html)

### One-off and final-pay withholding

Regular pay follows the ordinary table. A bonus, retroactive pay or holiday compensation classified as a one-off payment uses the payment-year one-off table and matching column; obtain the annual-pay basis under its instructions. If paid together, calculate regular and one-off deductions separately. Without regular time-based pay, the ordinary one-off deduction is 30%. A specific adjustment or SINK decision controls instead. [Official source](https://www.skatteverket.se/foretag/arbetsgivare/arbetsgivaravgifterochskatteavdrag/skatteavdrag/engangsbelopp.4.361dc8c15312eff6fd3225e.html)

For termination, use the ordinary table for final regular salary; use the one-off table for one-off amounts paid that month and final settlement paid by the following month. Later payments require a fresh main/supplementary-income assessment. Classify holiday salary versus holiday compensation before choosing the table. [Official source](https://www.skatteverket.se/servicelankar/otherlanguages/englishengelska/businessesandemployers/startingandrunningaswedishbusiness/declaringtaxesbusinesses/filingapayereturn/deductedtax.4.2fb39afe18dabf1e4d255d0.html)

### 4.4 Reconcile

For each payee reconcile the bank transfer as gross cash salary + separately payable cash expense reimbursements − withheld tax − authorised cash deductions. Non-cash benefits increase the relevant taxable/contribution bases but are not cash paid into the employee’s bank account. If an employee net payment for a benefit is deducted from salary, deduct it once from the cash transfer and reduce the benefit value separately; do not double-deduct it. Reconcile contribution bases and contributions to individual records, the payroll ledger, employer total and tax-account funding. The e-service calculation does not replace this reconciliation. [Skatteverket](https://www.skatteverket.se/servicelankar/otherlanguages/englishengelska/businessesandemployers/startingandrunningaswedishbusiness/declaringtaxesbusinesses/filingapayereturn/howtofillinthepayetaxreturnboxbybox.4.309a41aa1672ad0c8379f84.html)

## 5. File, pay and communicate

File per payee and employer through the PAYE e-service, or an error-checked payroll XML file. Most employers file by the 12th of the following month; confirm the employer's deadline. [Skatteverket](https://www.skatteverket.se/servicelankar/otherlanguages/englishengelska/businessesandemployers/startingandrunningaswedishbusiness/declaringtaxesbusinesses/filingapayereturn.4.2cf1b5cd163796a5c8b107cd.html)

### Individual-statement checklist

1. Add the payee with correct identity and any prescribed foreign/alternative identity details.
2. Assign a unique non-zero specification number. Preserve it because a correction needs the same number. [Skatteverket](https://www.skatteverket.se/servicelankar/otherlanguages/englishengelska/businessesandemployers/startingandrunningaswedishbusiness/declaringtaxesbusinesses/filingapayereturn/howtofillinthepayetaxreturnboxbybox.4.309a41aa1672ad0c8379f84.html) [Skatteverket](https://www.skatteverket.se/servicelankar/otherlanguages/englishengelska/businessesandemployers/startingandrunningaswedishbusiness/declaringtaxesbusinesses/filingapayereturn/correctingapayereturn.4.13948c0e18e810bfa0c2e34.html)
3. Enter cash gross salary in **011** and benefits in their specific fields.
4. Complete exactly one preliminary-tax-block field: for example **001** preliminary tax, **274** SINK, or an applicable no-deduction reason. Record zero where the instructions require it. [Skatteverket](https://www.skatteverket.se/servicelankar/otherlanguages/englishengelska/businessesandemployers/startingandrunningaswedishbusiness/declaringtaxesbusinesses/filingapayereturn/howtofillinthepayetaxreturnboxbybox.4.309a41aa1672ad0c8379f84.html)
5. Complete workplace, foreign-employer and no-permanent-establishment fields only when their conditions apply, including **302** where applicable.
6. Review payee facts, benefit period, contribution route/code and tax field. Sign, submit and retain the receipt.

The e-service calculates employer totals. On a paper return, calculate the totals from individual statements and use main-statement **487** and **497**. [Skatteverket](https://www.skatteverket.se/servicelankar/otherlanguages/englishengelska/businessesandemployers/startingandrunningaswedishbusiness/declaringtaxesbusinesses/filingapayereturn/howtofillinthepayetaxreturnboxbybox.4.309a41aa1672ad0c8379f84.html)

Employer contributions and deducted tax must reach the tax account by the PAYE deadline. A VAT-registered business with annual turnover over SEK 40 million has a different payment date: the 12th of the VAT-filing month, or 17 January. Do not apply that exception based on payroll size. Tell the employee the reported information by the PAYE deadline, such as through a payslip. [Skatteverket](https://www.skatteverket.se/servicelankar/otherlanguages/englishengelska/businessesandemployers/startingandrunningaswedishbusiness/payingtaxesbusinesses/howtopayemployercontributionsandtaxes.4.676f4884175c97df4191150.html) [Skatteverket](https://www.skatteverket.se/servicelankar/otherlanguages/englishengelska/businessesandemployers/startingandrunningaswedishbusiness/declaringtaxesbusinesses/filingapayereturn/deductedtax.4.2fb39afe18dabf1e4d255d0.html)

## 6. Correct a filed period

File a **new PAYE return for the affected period**. The Tax Agency says corrections can reach six years back (in 2026, 2020 onward). [Skatteverket](https://www.skatteverket.se/servicelankar/otherlanguages/englishengelska/businessesandemployers/startingandrunningaswedishbusiness/declaringtaxesbusinesses/filingapayereturn/correctingapayereturn.4.13948c0e18e810bfa0c2e34.html)

1. Rebuild the affected payee/employer figures from source evidence, identifying identity, compensation, benefit, base/rate, withholding or employer-data error.
2. Open the filed period, choose correction, amend the correct data, and use the **same specification number** so a payee correction replaces earlier data rather than adding data. Review, sign, submit and retain the receipt.
3. Contributions can be amended and deducted tax increased, but deducted tax normally cannot be reduced. For an overpayment, distinguish future-pay offsetting from a repayment demand. A repayment-demand correction reduces original compensation while leaving deducted tax unchanged.
4. Inform the payee and reconcile the revised Tax Agency decision/tax account when issued. [Skatteverket](https://www.skatteverket.se/servicelankar/otherlanguages/englishengelska/businessesandemployers/startingandrunningaswedishbusiness/declaringtaxesbusinesses/filingapayereturn/correctingapayereturn.4.13948c0e18e810bfa0c2e34.html)

## 7. Worked checks and boundaries

Examples use assumed pay amounts and once-at-the-end decimal rounding to illustrate the calculation. The filed amount follows the current PAYE field and rounding instructions.

### Case 1 — ordinary monthly Swedish payroll

**Facts:** Employee born 1988 receives SEK 40,000 cash salary in May 2026, no taxable benefits, reliefs or foreign facts. A-tax says main income but table amount is not supplied. [Skatteverket](https://www.skatteverket.se/servicelankar/otherlanguages/englishengelska/businessesandemployers/startingandrunningaswedishbusiness/declaringtaxesbusinesses/filingapayereturn/employercontributions.4.2fb39afe18dabf1e4d24a3d.html)

**Method:** Contribution base is SEK 40,000 in box 011. Employer contribution is `40,000 × 31.42% = SEK 12,568.00`. Before calculating net pay, obtain the employee's actual current table number, correct table column and pay frequency from the A-tax certificate or an adjustment decision; they are not supplied in these facts. Withhold under that input, not at the 31.42% employer rate. File May PAYE and fund withheld tax plus SEK 12,568 by the applicable June deadline. [Skatteverket](https://www.skatteverket.se/servicelankar/otherlanguages/englishengelska/businessesandemployers/startingandrunningaswedishbusiness/declaringtaxesbusinesses/filingapayereturn/employercontributions.4.2fb39afe18dabf1e4d24a3d.html) [Skatteverket](https://www.skatteverket.se/servicelankar/otherlanguages/englishengelska/businessesandemployers/startingandrunningaswedishbusiness/declaringtaxesbusinesses/filingapayereturn/howtofillinthepayetaxreturnboxbybox.4.309a41aa1672ad0c8379f84.html) [Skatteverket](https://www.skatteverket.se/servicelankar/otherlanguages/englishengelska/businessesandemployers/startingandrunningaswedishbusiness/declaringtaxesbusinesses/filingapayereturn/deductedtax.4.2fb39afe18dabf1e4d255d0.html) [Skatteverket](https://www.skatteverket.se/servicelankar/otherlanguages/inenglishengelska/individualsandemployees/declaringtaxesforindividuals/ataxcertificateandtaxtables.4.2fb39afe18dabf1e4d25053.html)

### Case 2 — youth threshold

**Facts:** Employee born 2005 receives SEK 32,000 in May 2026, no benefits or special coverage facts. [Skatteverket](https://www.skatteverket.se/servicelankar/otherlanguages/englishengelska/businessesandemployers/startingandrunningaswedishbusiness/declaringtaxesbusinesses/filingapayereturn/employercontributions.4.2fb39afe18dabf1e4d24a3d.html)

**Method:** `25,000 × 20.81% = SEK 5,202.50`; `7,000 × 31.42% = SEK 2,199.40`; total employer contribution **SEK 7,401.90**. Report/withhold tax independently using the decision. [Skatteverket](https://www.skatteverket.se/servicelankar/otherlanguages/englishengelska/businessesandemployers/startingandrunningaswedishbusiness/declaringtaxesbusinesses/filingapayereturn/employercontributions.4.2fb39afe18dabf1e4d24a3d.html)

### Case 3 — official illustrative example before a tax decision

**Facts:** Gross SEK 28,000. No A-tax/SINK decision. Relevant table deduction is SEK 5,604. [Skatteverket](https://www.skatteverket.se/servicelankar/otherlanguages/englishengelska/businessesandemployers/startingandrunningaswedishbusiness/declaringtaxesbusinesses/filingapayereturn/deductedtax.4.2fb39afe18dabf1e4d255d0.html)

**Method:** Deduct `5,604 × 110% = SEK 6,164.40`; the official example presents SEK 6,164 after its table rounding. Use the decision prospectively when it arrives, without correcting this payment merely because it arrives. This reproduces the authority’s illustrative figures; do not use that example table amount as the employee’s current deduction. [Skatteverket](https://www.skatteverket.se/servicelankar/otherlanguages/englishengelska/businessesandemployers/startingandrunningaswedishbusiness/declaringtaxesbusinesses/filingapayereturn/deductedtax.4.2fb39afe18dabf1e4d255d0.html)

### Case 4 — cross-border exclusion

**Facts:** A foreign employer pays a person working in Sweden who presents an A1/Certificate of Coverage for foreign social-security coverage.

**Method:** Record the certificate's issuing authority and exact coverage period, then determine the convention/coverage facts and confirm the employer's Swedish registration and tax-account route. Do not apply 31.42%, a foreign-employer table or a zero-Swedish-contribution result solely from the certificate label. Determine Swedish withholding/reporting separately and choose a contribution route only where the evidence supports it. [Skatteverket](https://www.skatteverket.se/servicelankar/otherlanguages/englishengelska/businessesandemployers/startingandrunningaswedishbusiness/hiringworkersfromabroad.4.6532ae7518aff8c118f984.html) [Skatteverket](https://www.skatteverket.se/servicelankar/otherlanguages/englishengelska/businessesandemployers/nonswedishbusinesseswithoperationsinsweden/registerabusiness.4.676f4884175c97df41917fa.html)

### Case 5 — correction

**Facts:** May return reported SEK 20,000 contribution-liable salary; evidence shows SEK 18,000. Original specification number 17. [Skatteverket](https://www.skatteverket.se/servicelankar/otherlanguages/englishengelska/businessesandemployers/startingandrunningaswedishbusiness/declaringtaxesbusinesses/filingapayereturn/employercontributions.4.2fb39afe18dabf1e4d24a3d.html)

**Method:** File a new May return, correct the payee with specification 17, recompute contributions, assess tax under the no-reduction restriction, notify payee and reconcile revised decision/tax account. [Skatteverket](https://www.skatteverket.se/servicelankar/otherlanguages/englishengelska/businessesandemployers/startingandrunningaswedishbusiness/declaringtaxesbusinesses/filingapayereturn/correctingapayereturn.4.13948c0e18e810bfa0c2e34.html)

### Case 6 — annual amount stays below the contribution threshold

**Facts:** An A-tax payee is paid SEK 500 for work in May 2026 and receives no further remuneration for work during 2026. Ordinary Swedish coverage applies. [Skatteverket](https://www.skatteverket.se/servicelankar/otherlanguages/englishengelska/businessesandemployers/startingandrunningaswedishbusiness/declaringtaxesbusinesses/filingapayereturn/employercontributions.4.2fb39afe18dabf1e4d24a3d.html)

**Method:** The calendar-year remuneration is below SEK 1,000, so do not calculate employer contributions under the ordinary contribution rate table. Keep the cumulative payee record and still determine PAYE withholding/reporting from the applicable tax facts; this contribution threshold does not itself decide withholding. [Skatteverket](https://www.skatteverket.se/arbetsgivaravgifter) [Skatteverket](https://www.skatteverket.se/servicelankar/otherlanguages/englishengelska/businessesandemployers/startingandrunningaswedishbusiness/declaringtaxesbusinesses/filingapayereturn/deductedtax.4.2fb39afe18dabf1e4d255d0.html)

### Case 7 — later payment crosses the annual contribution threshold

**Facts:** The same A-tax payee received SEK 500 in May, expected to remain below the threshold, then receives SEK 1,000 in November 2026. The payee is born in 1990 and ordinary Swedish coverage applies. [Skatteverket](https://www.skatteverket.se/servicelankar/otherlanguages/englishengelska/businessesandemployers/startingandrunningaswedishbusiness/declaringtaxesbusinesses/filingapayereturn/employercontributions.4.2fb39afe18dabf1e4d24a3d.html)

**Method:** The annual remuneration is SEK 1,500, so employer contributions become due on the full remuneration. For the ordinary rate, `1,500 × 31.42% = SEK 471.30`. Rebuild the year-to-date record. The Tax Agency correction example directs the November individual statement to show SEK 1,500 in box 011 and SEK 500 in box 010 where the earlier payment had been reported as below the contribution threshold; use the actual filed-record facts and e-service validation before filing. [Skatteverket](https://www.skatteverket.se/arbetsgivaravgifter) [Skatteverket](https://www.skatteverket.se/servicelankar/otherlanguages/englishengelska/businessesandemployers/startingandrunningaswedishbusiness/declaringtaxesbusinesses/filingapayereturn/correctingapayereturn.4.13948c0e18e810bfa0c2e34.html)

### Case 8 — taxable benefit is not bank pay

Illustrative assumptions: cash salary SEK 40,000, correctly valued non-cash benefit SEK 4,000, no reimbursements or other cash deductions, ordinary contributions and an independently established withholding amount of SEK 10,000. Contribution base is SEK 44,000; employer contributions are SEK 13,824.80. The cash transfer is SEK 30,000. The withholding amount is a hypothetical supplied result, not a tax-table calculation. [Skatteverket](https://www.skatteverket.se/servicelankar/otherlanguages/englishengelska/businessesandemployers/startingandrunningaswedishbusiness/declaringtaxesbusinesses/filingapayereturn/howtofillinthepayetaxreturnboxbybox.4.309a41aa1672ad0c8379f84.html) [Skatteverket](https://www.skatteverket.se/servicelankar/otherlanguages/englishengelska/businessesandemployers/startingandrunningaswedishbusiness/declaringtaxesbusinesses/filingapayereturn/employercontributions.4.2fb39afe18dabf1e4d24a3d.html)

### Case 9 — complete ordinary monthly bank pay

Assumptions: employee born 1988, monthly main salary SEK 40,000 in 2026, no benefits or deductions, A-tax decision specifies table 38 and no adjustment. Column 1 applies to ordinary salary for a person below 66 at the start of the year. The official monthly table row 39801–40000 gives withholding SEK 9,655. Cash paid is SEK 30,345. Employer contribution remains SEK 12,568.00, funded separately from employee net pay. [Official source](https://www.skatteverket.se/foretag/arbetsgivare/arbetsgivaravgifterochskatteavdrag/skattetabeller.4.96cca41179bad4b1aa8a46.html) [Official source](https://skatteverket.se/download/18.1522bf3f19aea8075ba625/1765290530129/allmanna-tabeller-manad-tabell-38.pdf)

### Case 10 — statutory paid holiday supplement

Assumptions: unchanged monthly pay SEK 30,000, no fixed/variable supplements, five earned paid days, same-pay rule applies and no collective variation. The extra holiday supplement is SEK 645; current monthly salary continues. Choose the correct withholding treatment for the actual payment type. [Official source](https://data.riksdagen.se/dokument/sfs-1977-480.html)

### Case 11 — one-off payment alongside regular salary

Assumptions: regular monthly employee, column 1, independently established annual-pay basis SEK 500,000, one-off bonus SEK 10,000, no special decision. The 2026 band 477601–660000 uses 34%, so bonus withholding is SEK 3,400 and bonus cash is SEK 6,600. Regular salary withholding is calculated separately. [Official source](https://www.skatteverket.se/foretag/arbetsgivare/arbetsgivaravgifterochskatteavdrag/skatteavdrag/engangsbelopp.4.361dc8c15312eff6fd3225e.html)

## When to refuse or refer

- Stop a calculation when the applicable decision, benefit valuation, social-security coverage or contractual pay entitlement is missing.
- Refer pensions, employment-law and specialist cross-border questions for the evidence described below.

### Completion record

Retain the signed payroll calculation, tax-table/decision evidence, benefit valuations, coverage certificates, payee statements, bank-payment control, submitted PAYE receipt and tax-account reconciliation. Close the payroll only when the cash, tax and contribution records agree.

A payroll input involving collective-agreement wages, disputed holiday entitlement, a pension plan, equity/options, severance, a work permit, specialised contribution relief or a country-specific social-security convention needs the applicable contract, decision and official specialist method before computation. Record the missing input and responsible reviewer. This Guide supplies the ordinary PAYE workflow; it does not supply a universal pension premium, benefit valuation or employment entitlement.

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
