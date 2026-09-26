---
name: sweden-payroll
description: Use this skill whenever asked about Swedish payroll processing, employee salary calculations, preliminärskatt (preliminary income tax / PAYE), arbetsgivaravgifter (employer social contributions), employer cost calculations, net-to-gross or gross-to-net conversions, Swedish payslip structure, arbetsgivardeklaration filings, or any question about computing wages, deductions, or employer obligations in Sweden. Trigger on phrases like "Swedish payroll", "preliminärskatt", "arbetsgivaravgifter", "employer contributions Sweden", "PAYE Sweden", "net salary Sweden", "lönespecifikation", "kommunalskatt", "municipal tax Sweden", "statlig inkomstskatt", "Skatteverket filing", "kollektivavtal", "ITP pension", or "semesterersättning".
version: 1.0
jurisdiction: SE
tax_year: 2026
last_updated: 2026-09-25
authored_by: OpenAccountants team
review_status: pending_review
trust_label: By OpenAccountants
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

For each payee and pay date retain: contract/engagement and work-location facts; correct personal or coordination number (or the prescribed alternative identity and foreign address); the current A-tax certificate's **tax table number** (the certificate names the table; the payer picks the column from the payee's age and income type, for example column 1 for salary paid to a person who was under 66 at the start of the year), pay frequency, any adjustment decision or SINK decision, and whether income is main or supplementary; birth year and age at 1 January 2026; gross cash pay; separately itemised taxable benefits and employee net payments; expenses, holiday/final-pay character and pension/equity/severance facts; the A1/coverage/posting/agreement document, issuing authority and effective coverage dates; evidence that the employer's Swedish registration and tax-account route has been confirmed; prior PAYE reports and the employer deadline. [Skatteverket](https://www.skatteverket.se/servicelankar/otherlanguages/inenglishengelska/individualsandemployees/declaringtaxesforindividuals/ataxcertificateandtaxtables.4.2fb39afe18dabf1e4d25053.html) [Skatteverket](https://www.skatteverket.se/foretag/arbetsgivare/arbetsgivaravgifterochskatteavdrag/skattetabeller.4.96cca41179bad4b1aa8a46.html)

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
| A1, Certificate of Coverage or convention | Record the issuing authority and exact coverage period; then confirm the Swedish registration/tax-account route before selecting a contribution code or rate. A valid certificate that names this employee and covers the pay period means no Swedish social security contributions are due on that pay: report the cash pay in box 131 (not included in the basis for contributions). A certificate label alone is not enough; check the employee, the issuer and the dates. Swedish withholding is decided separately. [Skatteverket](https://www.skatteverket.se/servicelankar/otherlanguages/englishengelska/businessesandemployers/startingandrunningaswedishbusiness/declaringtaxesbusinesses/filingapayereturn/howtofillinthepayetaxreturnboxbybox.4.309a41aa1672ad0c8379f84.html) [Skatteverket](https://www.skatteverket.se/servicelankar/otherlanguages/englishengelska/businessesandemployers/nonswedishbusinesseswithoperationsinsweden/registerabusiness.4.676f4884175c97df41917fa.html) |
| No Swedish permanent establishment | Use the no-permanent-establishment rates, not the ordinary table: for 2026, 18.80% for employees born 1959 or later, 10.21% for those born 1938–1958, and 14.50% for those born 2003–2007 on pay from 1 April 2026 (check the Tax Agency instructions for code 7003 on how the SEK 25,000 monthly limit applies before using it). Tick box 302 on the individual statement. Such an employer does not pay general payroll tax. [Skatteverket](https://www.skatteverket.se/servicelankar/otherlanguages/englishengelska/businessesandemployers/startingandrunningaswedishbusiness/declaringtaxesbusinesses/filingapayereturn/employercontributions.4.2fb39afe18dabf1e4d24a3d.html) [Skatteverket](https://www.skatteverket.se/servicelankar/otherlanguages/englishengelska/businessesandemployers/startingandrunningaswedishbusiness/declaringtaxesbusinesses/filingapayereturn/howtofillinthepayetaxreturnboxbybox.4.309a41aa1672ad0c8379f84.html) |
| Social-security agreement | Available to an employer based outside Sweden with no permanent establishment here. The employee declares and pays the employer contributions, but the Tax Agency can still ask the employer to pay if the employee does not. The employer must still register, deduct preliminary tax at 30% on pay for work in Sweden (unless the Tax Agency has notified the employee of another decision) and file a monthly PAYE return. [Skatteverket](https://www.skatteverket.se/servicelankar/otherlanguages/englishengelska/businessesandemployers/startingandrunningaswedishbusiness/declaringtaxesbusinesses/filingapayereturn/socialsecurityagreementforyouasanemployer.4.2fb39afe18dabf1e4d21c41.html) |
| Third-country national | Check right to work; Tax Agency notification has its own end-of-third-month-after-start-month deadline. [Skatteverket](https://www.skatteverket.se/servicelankar/otherlanguages/englishengelska/businessesandemployers/startingandrunningaswedishbusiness/hiringworkersfromabroad.4.6532ae7518aff8c118f984.html) |
| Private individual paying for work that is not a business expense | No preliminary tax is deducted if the payer expects to pay that payee less than SEK 10,000 in the calendar year and every other condition in Tax Procedure Act chapter 10 section 4 point 3 is met. Refer the employer-contribution treatment. [Official source](https://data.riksdagen.se/dokument/sfs-2011-1244.text) |

## 4. Calculate the pay period

### 4.1 Establish the contribution base

Start with cash gross remuneration for work and add taxable non-cash benefits included in the contribution base. Enter cash gross salary in **box 011**; benefits belong in their appropriate fields, not 011. A taxable benefit is ordinarily reported for the period the employee could use it. Reduce a benefit value by the employee's documented **net** payment for it. Exception: a fuel benefit is still reported at its full marked-up value in box 018 even if the employee paid for it through net salary deductions; the payment goes in box 098. [Skatteverket](https://www.skatteverket.se/servicelankar/otherlanguages/englishengelska/businessesandemployers/startingandrunningaswedishbusiness/declaringtaxesbusinesses/filingapayereturn/howtofillinthepayetaxreturnboxbybox.4.309a41aa1672ad0c8379f84.html)

Classify cash reimbursement, pension, option/equity award, termination payment, holiday payment and expense allowance under their specific rule before treating it as ordinary salary. Before applying the rate table, track remuneration for work paid to each **A-tax** payee across the calendar year. Employer contributions are due when that remuneration totals **SEK 1,000 or more** for the year. If a later payment takes the year's total to SEK 1,000 or more, contributions are due on the whole year's amount. Report the whole amount in box 011 in the period in which you find the liability, and enter the amount you earlier reported as not contribution-liable (box 131) in box 010; do not reopen the earlier period (see Case 7). Do not treat a single payment below SEK 1,000 as an enduring exclusion. The same expected annual total also decides whether you withhold tax (see 4.3). [Skatteverket](https://www.skatteverket.se/arbetsgivaravgifter) [Skatteverket](https://www.skatteverket.se/servicelankar/otherlanguages/englishengelska/businessesandemployers/startingandrunningaswedishbusiness/declaringtaxesbusinesses/filingapayereturn/correctingapayereturn.4.13948c0e18e810bfa0c2e34.html)

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
3. **Specific decision:** the amount or rate in an adjustment (jämkning) decision; or, where the payee has a SINK decision, deduct special income tax for non-residents at the statutory 22.5% and report it in box 274, not box 001. [Skatteverket](https://www.skatteverket.se/servicelankar/otherlanguages/englishengelska/businessesandemployers/startingandrunningaswedishbusiness/hiringworkersfromabroad.4.6532ae7518aff8c118f984.html) [Official source](https://data.riksdagen.se/dokument/sfs-1991-586.text)

Before calculating net pay, lock the current table number, applicable column, pay frequency and any adjustment or SINK decision in the payroll record. Without an A-tax/SINK decision, deduct the municipal table amount for the employer's business area plus 10% (110% of the table amount). Once the decision arrives, use it prospectively and do not correct earlier reports merely because it arrived. If no cash remuneration is paid, no tax can be withheld from a taxable benefit; route the resulting issue before sign-off. For salary advances, withhold in the same proportion as the advance bears to total compensation; if the total is unknown, treat the advance as the total. [Skatteverket](https://www.skatteverket.se/servicelankar/otherlanguages/englishengelska/businessesandemployers/startingandrunningaswedishbusiness/declaringtaxesbusinesses/filingapayereturn/deductedtax.4.2fb39afe18dabf1e4d255d0.html) [Skatteverket](https://www.skatteverket.se/servicelankar/otherlanguages/inenglishengelska/individualsandemployees/declaringtaxesforindividuals/ataxcertificateandtaxtables.4.2fb39afe18dabf1e4d25053.html)

**When no preliminary tax is deducted.** Do not deduct preliminary tax from pay for work if (a) the payment is below SEK 100, or (b) you expect the total you pay that payee in the calendar year to be below SEK 1,000. In case (b), report the pay in box 131 and enter 0 in box 001. If a later payment means the year's total will reach SEK 1,000 or more, deduct tax on that payment under the ordinary rules above (see Case 7). A school or higher-education student who will earn less than SEK 25,042 in 2026 and lives in Sweden all year can give you form SKV 434; with it you do not deduct preliminary tax and you enter 0 in box 001. The SKV 434 certificate does not remove employer contributions. If you find, before filing, that you deducted more than you had to, repay the excess to the employee. If you deduct too little, you may have to pay the shortfall. [Official source](https://data.riksdagen.se/dokument/sfs-2011-1244.text) [Skatteverket](https://www.skatteverket.se/servicelankar/otherlanguages/englishengelska/businessesandemployers/startingandrunningaswedishbusiness/declaringtaxesbusinesses/filingapayereturn/deductedtax.4.2fb39afe18dabf1e4d255d0.html) [Skatteverket](https://www.skatteverket.se/servicelankar/otherlanguages/englishengelska/businessesandemployers/startingandrunningaswedishbusiness/declaringtaxesbusinesses/filingapayereturn/howtofillinthepayetaxreturnboxbybox.4.309a41aa1672ad0c8379f84.html) [Skatteverket](https://www.skatteverket.se/foretag/arbetsgivare/arbetsgivaravgifterochskatteavdrag/skattetabeller.4.96cca41179bad4b1aa8a46.html)

### Ordinary holiday-pay inputs

Check the collective agreement first: permitted variations can replace the statutory calculation. Establish earned paid days and qualifying absence from the leave record. An employee is entitled to 25 holiday days each holiday year; how many of them are paid depends on the days earned. Under the statutory same-pay rule, keep paying current weekly/monthly salary and add a holiday supplement for each paid day of 0.43% of monthly pay, or 1.82% of weekly pay. Add any fixed pay supplements to the monthly or weekly pay before applying the percentage. Variable pay components give 12% of the variable pay that fell due during the holiday year. The percentage rule instead gives 12% of the statutory earning-year base: exclude holiday pay and specified absence/shutdown payments; replace qualifying absence with normal assumed earnings. Use it for non-weekly/monthly pay, regular variable pay of at least 10%, changed working fraction, or disqualifying absence, subject to the statutory exception. It may also be elected otherwise. On termination, value unused earned leave under the same statutory rules; payment is ordinarily due within one month. Preserve any valid contractual variation and its calculation. [Official source](https://data.riksdagen.se/dokument/sfs-1977-480.html)

### Statutory sick pay inputs

The employer pays sick pay for the sick-pay period: the first day the employee's working capacity is reduced by illness and the following 13 calendar days. Sick pay is 80% of the pay and benefits lost. Deduct a qualifying deduction (karensavdrag) of 20% of the sick pay for an average working week. Do not make the deduction if the employee has already had it ten times in the past 12 months. A new sick period that starts within five days of the last one continues the same 14-day sick-pay period and gets no new deduction. From the seventh calendar day after the sickness was reported, the employer need only pay if the employee gives a doctor's or dentist's certificate. The right starts from the first day of employment; for a contract shorter than one month, it starts only after 14 consecutive calendar days of employment. A collective agreement may set the detailed calculation. Record the sick days, the deduction count and the certificate. [Official source](https://data.riksdagen.se/dokument/sfs-1991-1047.text)

### One-off and final-pay withholding

Regular pay follows the ordinary table. A bonus, retroactive pay or holiday compensation classified as a one-off payment uses the payment-year one-off table and matching column; obtain the annual-pay basis under its instructions. If paid together, calculate regular and one-off deductions separately. Without regular time-based pay, the ordinary one-off deduction is 30%. A specific adjustment or SINK decision controls instead. [Official source](https://www.skatteverket.se/foretag/arbetsgivare/arbetsgivaravgifterochskatteavdrag/skatteavdrag/engangsbelopp.4.361dc8c15312eff6fd3225e.html)

For termination, use the ordinary table for final regular salary; use the one-off table for one-off amounts paid that month and final settlement paid by the following month. The Tax Agency treats only these as main income. For a payment made later than that, confirm its status before withholding; pay that is not main income is withheld at 30%. Classify holiday salary versus holiday compensation before choosing the table. [Official source](https://www.skatteverket.se/servicelankar/otherlanguages/englishengelska/businessesandemployers/startingandrunningaswedishbusiness/declaringtaxesbusinesses/filingapayereturn/deductedtax.4.2fb39afe18dabf1e4d255d0.html)

### 4.4 Reconcile

For each payee reconcile the bank transfer as gross cash salary + separately payable cash expense reimbursements − withheld tax − authorised cash deductions. Non-cash benefits increase the relevant taxable/contribution bases but are not cash paid into the employee’s bank account. If an employee net payment for a benefit is deducted from salary, deduct it once from the cash transfer and reduce the benefit value separately; do not double-deduct it. Reconcile contribution bases and contributions to individual records, the payroll ledger, employer total and tax-account funding. The e-service calculation does not replace this reconciliation. [Skatteverket](https://www.skatteverket.se/servicelankar/otherlanguages/englishengelska/businessesandemployers/startingandrunningaswedishbusiness/declaringtaxesbusinesses/filingapayereturn/howtofillinthepayetaxreturnboxbybox.4.309a41aa1672ad0c8379f84.html)

## 5. File, pay and communicate

File per payee and employer through the PAYE e-service, or an error-checked payroll XML file. Most employers file by the 12th of the following month, except that the July return is due on 17 August and the December return on 17 January. Employers whose VAT taxable base for the year is expected to exceed SEK 40 million file by the 26th of the following month (27 December for the November return). Confirm the employer's deadline in the e-service. [Skatteverket](https://www.skatteverket.se/servicelankar/otherlanguages/englishengelska/businessesandemployers/startingandrunningaswedishbusiness/declaringtaxesbusinesses/filingapayereturn.4.2cf1b5cd163796a5c8b107cd.html) [Official source](https://data.riksdagen.se/dokument/sfs-2011-1244.text)

### Individual-statement checklist

1. Add the payee with correct identity and any prescribed foreign/alternative identity details.
2. Assign a unique non-zero specification number. Preserve it because a correction needs the same number. [Skatteverket](https://www.skatteverket.se/servicelankar/otherlanguages/englishengelska/businessesandemployers/startingandrunningaswedishbusiness/declaringtaxesbusinesses/filingapayereturn/howtofillinthepayetaxreturnboxbybox.4.309a41aa1672ad0c8379f84.html) [Skatteverket](https://www.skatteverket.se/servicelankar/otherlanguages/englishengelska/businessesandemployers/startingandrunningaswedishbusiness/declaringtaxesbusinesses/filingapayereturn/correctingapayereturn.4.13948c0e18e810bfa0c2e34.html)
3. Enter cash gross salary in **011** and benefits in their specific fields.
4. Complete exactly one preliminary-tax-block field: for example **001** preliminary tax, **274** SINK, or an applicable no-deduction reason. Enter 0 in **001** where no tax was deducted because the payee's annual pay is below SEK 1,000, or under an SKV 434 student certificate. [Skatteverket](https://www.skatteverket.se/servicelankar/otherlanguages/englishengelska/businessesandemployers/startingandrunningaswedishbusiness/declaringtaxesbusinesses/filingapayereturn/howtofillinthepayetaxreturnboxbybox.4.309a41aa1672ad0c8379f84.html)
5. Complete workplace, foreign-employer and no-permanent-establishment fields only when their conditions apply, including **302** where applicable.
6. If pay reported for the period was affected by absence that may qualify the employee for parental benefit or temporary parental benefit, submit the absence details (boxes 821–827) with the same return and tell the employee what you reported. This has applied since the January 2025 reporting period. Absence details cannot be corrected or added after the return is filed. [Skatteverket](https://www.skatteverket.se/servicelankar/otherlanguages/englishengelska/businessesandemployers/startingandrunningaswedishbusiness/declaringtaxesbusinesses/filingapayereturn.4.2cf1b5cd163796a5c8b107cd.html)
7. Review payee facts, benefit period, contribution route/code and tax field. Sign, submit and retain the receipt.

The e-service calculates employer totals. On a paper return, calculate the totals from individual statements and use main-statement **487** and **497**. [Skatteverket](https://www.skatteverket.se/servicelankar/otherlanguages/englishengelska/businessesandemployers/startingandrunningaswedishbusiness/declaringtaxesbusinesses/filingapayereturn/howtofillinthepayetaxreturnboxbybox.4.309a41aa1672ad0c8379f84.html)

Employer contributions and deducted tax must reach the tax account by the PAYE deadline. A business whose VAT taxable base for the year is expected to exceed SEK 40 million has a different payment date: pay by the 12th of the month after the reporting period (17th in January), even though its return is due on the 26th. [Official source](https://data.riksdagen.se/dokument/sfs-2011-1244.text) Do not apply that exception based on payroll size. Tell the employee the reported information by the PAYE deadline, such as through a payslip. [Skatteverket](https://www.skatteverket.se/servicelankar/otherlanguages/englishengelska/businessesandemployers/startingandrunningaswedishbusiness/payingtaxesbusinesses/howtopayemployercontributionsandtaxes.4.676f4884175c97df4191150.html) [Skatteverket](https://www.skatteverket.se/servicelankar/otherlanguages/englishengelska/businessesandemployers/startingandrunningaswedishbusiness/declaringtaxesbusinesses/filingapayereturn/deductedtax.4.2fb39afe18dabf1e4d255d0.html)

## 6. Correct a filed period

File a **new PAYE return for the affected period**. The Tax Agency says corrections can reach six years back (in 2026, 2020 onward). [Skatteverket](https://www.skatteverket.se/servicelankar/otherlanguages/englishengelska/businessesandemployers/startingandrunningaswedishbusiness/declaringtaxesbusinesses/filingapayereturn/correctingapayereturn.4.13948c0e18e810bfa0c2e34.html)

1. Rebuild the affected payee/employer figures from source evidence, identifying identity, compensation, benefit, base/rate, withholding or employer-data error.
2. Open the filed period, choose correction, amend the correct data, and use the **same specification number** so a payee correction replaces earlier data rather than adding data. Review, sign, submit and retain the receipt.
3. Contributions can be amended and deducted tax increased, but deducted tax normally cannot be reduced. For an overpayment, distinguish future-pay offsetting from a repayment demand. A repayment-demand correction reduces original compensation while leaving deducted tax unchanged.
4. Inform the payee and reconcile the revised Tax Agency decision/tax account when issued. Absence details (boxes 821–827) cannot be corrected or added through this route. [Skatteverket](https://www.skatteverket.se/servicelankar/otherlanguages/englishengelska/businessesandemployers/startingandrunningaswedishbusiness/declaringtaxesbusinesses/filingapayereturn/correctingapayereturn.4.13948c0e18e810bfa0c2e34.html)

### Penalties

- A late PAYE return costs a late-filing fee of SEK 625, or SEK 1,250 if it is filed after a Tax Agency order. Only one fee is charged if several returns due on the same date are late. [Official source](https://data.riksdagen.se/dokument/sfs-2011-1244.text)
- A tax surcharge applies to incorrect information: 20% of the tax that would have been lost, or 2% or 5% where the error only put an amount in the wrong period (2% if the reporting period is at most three months and the amount was placed within four months of the right period; otherwise 5%). [Official source](https://data.riksdagen.se/dokument/sfs-2011-1244.text)
- Failing to deduct tax that should have been deducted gives a surcharge of 5% of the tax that should have been deducted, and the employer can be made to pay the tax. [Official source](https://data.riksdagen.se/dokument/sfs-2011-1244.text) [Skatteverket](https://www.skatteverket.se/servicelankar/otherlanguages/englishengelska/businessesandemployers/startingandrunningaswedishbusiness/declaringtaxesbusinesses/filingapayereturn/deductedtax.4.2fb39afe18dabf1e4d255d0.html)
- No surcharge is charged if the employer corrects the error on its own initiative, subject to the rule on corrections made after the Tax Agency announces a general check. [Official source](https://data.riksdagen.se/dokument/sfs-2011-1244.text)

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

**Method:** Record the certificate's issuing authority and exact coverage period, check that it names this employee, and confirm the employer's Swedish registration and tax-account route. If the certificate is valid for the pay period, no Swedish social security contributions are due on that pay: report it in box 131, not box 011, and do not apply 31.42% or the no-permanent-establishment rates. If it does not cover the period or the employee, stop and resolve coverage before choosing a rate. Determine Swedish withholding separately under 4.3. [Skatteverket](https://www.skatteverket.se/servicelankar/otherlanguages/englishengelska/businessesandemployers/startingandrunningaswedishbusiness/hiringworkersfromabroad.4.6532ae7518aff8c118f984.html) [Skatteverket](https://www.skatteverket.se/servicelankar/otherlanguages/englishengelska/businessesandemployers/nonswedishbusinesseswithoperationsinsweden/registerabusiness.4.676f4884175c97df41917fa.html) [Skatteverket](https://www.skatteverket.se/servicelankar/otherlanguages/englishengelska/businessesandemployers/startingandrunningaswedishbusiness/declaringtaxesbusinesses/filingapayereturn/howtofillinthepayetaxreturnboxbybox.4.309a41aa1672ad0c8379f84.html)

### Case 5 — correction

**Facts:** May return reported SEK 20,000 contribution-liable salary; evidence shows SEK 18,000. Original specification number 17. [Skatteverket](https://www.skatteverket.se/servicelankar/otherlanguages/englishengelska/businessesandemployers/startingandrunningaswedishbusiness/declaringtaxesbusinesses/filingapayereturn/employercontributions.4.2fb39afe18dabf1e4d24a3d.html)

**Method:** File a new May return, correct the payee with specification 17, recompute contributions, assess tax under the no-reduction restriction, notify payee and reconcile revised decision/tax account. [Skatteverket](https://www.skatteverket.se/servicelankar/otherlanguages/englishengelska/businessesandemployers/startingandrunningaswedishbusiness/declaringtaxesbusinesses/filingapayereturn/correctingapayereturn.4.13948c0e18e810bfa0c2e34.html)

### Case 6 — annual amount stays below SEK 1,000

**Facts:** An A-tax payee is paid SEK 500 for work in May 2026 and receives no further remuneration for work during 2026. Ordinary Swedish coverage applies. [Skatteverket](https://www.skatteverket.se/servicelankar/otherlanguages/englishengelska/businessesandemployers/startingandrunningaswedishbusiness/declaringtaxesbusinesses/filingapayereturn/employercontributions.4.2fb39afe18dabf1e4d24a3d.html)

**Method:** The calendar-year remuneration is expected to stay below SEK 1,000, so no employer contributions are due and no preliminary tax is deducted: the same annual SEK 1,000 threshold applies to withholding. Report the SEK 500 on the individual statement in box 131 (cash compensation not included in the basis for contributions) and enter 0 in box 001. Keep the cumulative payee record; if later payments take the year to SEK 1,000 or more, follow Case 7. [Skatteverket](https://www.skatteverket.se/arbetsgivaravgifter) [Skatteverket](https://www.skatteverket.se/servicelankar/otherlanguages/englishengelska/businessesandemployers/startingandrunningaswedishbusiness/declaringtaxesbusinesses/filingapayereturn/deductedtax.4.2fb39afe18dabf1e4d255d0.html) [Skatteverket](https://www.skatteverket.se/servicelankar/otherlanguages/englishengelska/businessesandemployers/startingandrunningaswedishbusiness/declaringtaxesbusinesses/filingapayereturn/howtofillinthepayetaxreturnboxbybox.4.309a41aa1672ad0c8379f84.html) [Official source](https://data.riksdagen.se/dokument/sfs-2011-1244.text)

### Case 7 — later payment crosses the annual contribution threshold

**Facts:** The same A-tax payee received SEK 500 in May, expected to remain below the threshold, then receives SEK 1,000 in November 2026. The payee is born in 1990 and ordinary Swedish coverage applies. [Skatteverket](https://www.skatteverket.se/servicelankar/otherlanguages/englishengelska/businessesandemployers/startingandrunningaswedishbusiness/declaringtaxesbusinesses/filingapayereturn/employercontributions.4.2fb39afe18dabf1e4d24a3d.html)

**Method:** The annual remuneration is SEK 1,500, so employer contributions become due on the full remuneration. For the ordinary rate, `1,500 × 31.42% = SEK 471.30`. Rebuild the year-to-date record. The Tax Agency correction example directs the November individual statement to show SEK 1,500 in box 011 and SEK 500 in box 010 where the earlier payment had been reported as below the contribution threshold; use the actual filed-record facts and e-service validation before filing. Because the year's total now reaches SEK 1,000, deduct preliminary tax on the November payment under 4.3. [Skatteverket](https://www.skatteverket.se/arbetsgivaravgifter) [Skatteverket](https://www.skatteverket.se/servicelankar/otherlanguages/englishengelska/businessesandemployers/startingandrunningaswedishbusiness/declaringtaxesbusinesses/filingapayereturn/correctingapayereturn.4.13948c0e18e810bfa0c2e34.html)

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

A payroll input involving collective-agreement wages, disputed holiday entitlement, a pension plan, equity/options, severance, a work permit, specialised contribution relief or a country-specific social-security convention needs the applicable contract, decision and official specialist method before computation. Record the missing input and responsible reviewer. This Guide supplies the ordinary PAYE workflow; it does not supply a universal pension premium, benefit valuation or employment entitlement. Employer pension costs also carry special payroll tax on pension costs at 24.26% of the cost; it is declared in the employer's income tax return, not in the PAYE return. [Official source](https://data.riksdagen.se/dokument/sfs-1991-687.text) [Official source](https://data.riksdagen.se/dokument/sfs-2011-1244.text)

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
