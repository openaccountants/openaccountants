---
name: ae-payroll-social
description: "Use this skill for UAE payroll questions in tax year 2026: why wages are outside Corporate Tax, employee versus self-employed, directors' fees, Corporate Tax deduction of staff costs and private pension contributions, and VAT recovery on staff benefits, including the 1 October 2026 rules and the FTA cases for transport, food, accommodation, phones and parking. Names the pension, gratuity, Wage Protection System and unemployment insurance duties and who to confirm them with; it does not state their rates. Trigger on: UAE payroll, Dubai salary tax, gratuity, GPSSA, staff accommodation VAT, employee benefits UAE."
version: 1.2
category: PR
jurisdiction: AE
tax_year: 2026
last_updated: 2026-11-01
authored_by: Michael Cutajar and the OpenAccountants team
review_status: pending_review
trust_label: Built by Michael Cutajar and the OpenAccountants team
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# UAE payroll for tax year 2026: wages outside Corporate Tax, what the employer's tax return and VAT return do with payroll, and the pension, gratuity and insurance points to confirm

## Scope and who this is for

This skill is for anyone running or advising on a UAE payroll in calendar year 2026: an employer, a payroll provider, or an accountant answering "what do I deduct from this salary, and what does the company owe?". The operative federal tax rules were read in the precise scopes listed in Sources on 1 November 2026; social execution remains held.

What it covers:

- Why wages are outside Corporate Tax, and where the line sits between an employee (no tax) and a self-employed person (possible Corporate Tax).
- How the employer's own Corporate Tax return treats salaries, benefits, directors' pay and pension contributions.
- How the employer's VAT return treats goods and services given to staff, including the rule that changes on 1 October 2026.
- NON-OPERATIVE HOLD: pension coverage, gratuity, the Wage Protection System and unemployment insurance. This Guide does not establish any employee's coverage or run those calculations.

**Social compliance is held, including coverage.** GPSSA/Abu Dhabi pension routing, nationality and first-insurance rules, gratuity coverage and accrual, free-zone differences, WPS, unemployment insurance, rates, caps, due dates and penalties have not been confirmed from their governing sources in this repair. Do not use the old text to execute payroll. Obtain current authority confirmation through a UAE payroll specialist before processing those items. Original details remain in the immutable evidence and destination table.

Companion Skills: Corporate Tax for the employer is in `ae-corporate-tax`; the individual's own position (including when a self-employed person must register) is in `ae-income-tax`; VAT registration and returns are in `uae-vat`.

### What UAE payroll does and does not involve ([Cabinet Decision No. 49 of 2023, Articles 1 and 2](https://tax.gov.ae/DataFolder/Files/Legislation/05-06-2023/3/Cabinet%20Decision%20No.%2049%20of%202023%20-%20for%20publishing.pdf); [CTGTNP1, section 3.8.1](https://tax.gov.ae/Datafolder/Files/Guides/CT/Taxation%20of%20natural%20persons%20-%2025%2011%202023.pdf); [CTGDTI1: Determination of Taxable Income](https://tax.gov.ae/DataFolder/Files/Pdf/2024/Determination%20of%20Taxable%20Income%20-%2031%2007%202024.pdf))

**Wage exclusion from Corporate Tax.** Cabinet Decision 49/2023 excludes a natural person's Wage from Corporate Tax; a natural person's Wage is outside it "regardless of the amount of Turnover". There is no Corporate Tax calculation or Corporate Tax return on those wages. This does not determine a worker's foreign-country obligations or social deductions.

**What counts as a wage.** The official definition is wide: "the wage that is given to the employee in consideration of their services under the employment contract, whether in cash or in kind, payable annually, monthly, weekly, daily, hourly, or by piece-meal, and includes all allowances, and bonuses in addition to any other benefits provided for, in the employment contract or in accordance with the applicable legislation in the State". Allowances, bonuses, benefits in kind and benefits due under UAE legislation (such as the statutory end-of-service gratuity) all fall inside it.

**No withholding tax either.** Corporate Tax Law Article 45 sets a 0% withholding rate for a non-resident's State Sourced Income not attributable to its UAE permanent establishment or nexus, subject to the Cabinet's power to specify another rate or category. Wage remains excluded under Decision 49/2023. This Guide does not decide a cross-border recipient's PE, nexus or treaty position.

**Employee or not is a question of fact.** The FTA says "whether a natural person is an employee and earns a salary or other form of remuneration as such, is a question of fact to be determined on a case-by-case basis". A person working under an employment contract is paid a Wage. A person who works for themselves and is not employed by the payer is running a Business, and if that person's business turnover exceeds AED 1,000,000 in a calendar year, that person is within natural-person Corporate Tax scope; apply registration and relief rules before calculating tax. The payer withholds nothing either way; the obligation is the contractor's own.

**Directors' fees.** "Generally, director fees will not be considered as a Business or Business Activity, and therefore would not be subject to Corporate Tax." Where a director is also an employee, the FTA's example treats both the salary and the board fees as a Wage.

**What payroll does involve:**

| Obligation | Who it applies to | Who runs it | Status in this skill |
|---|---|---|---|
| Income tax withholding | Nobody | None | Not applicable; wages outside Corporate Tax |
| Corporate Tax deduction for payroll | Employers that are Taxable Persons | FTA | Covered below |
| VAT on staff benefits | VAT-registered employers | FTA | Covered below |

## Ask the client first

- Is the worker employed under an employment contract, or engaged as a contractor or freelancer? If a contractor, how much business turnover do they have in the calendar year?
- What is the worker's nationality: UAE national, another GCC nationality, or expatriate? Keep this for the specialist's coverage check. For a UAE national: in which emirate are they employed? Pension-fund routing is held pending authority confirmation. For a UAE national: when were they first insured? The coverage and regime are held pending authority confirmation.
- Is the employer on the mainland or in a free zone, and which authority licensed it? Ask the specialist to establish the applicable employment and payroll regime.
- Is the employer a Taxable Person for Corporate Tax, and what is its Tax Period? Is it VAT-registered?
- Which benefits does the employer give beyond cash salary: accommodation, health insurance (and for which family members), cars, flights, staff events? Does the employer pay into a private pension or end-of-service savings fund for staff? How much, and has it actually been paid in the Tax Period?
- Are any employees or directors also shareholders, or related to shareholders?

## The method, step by step

1. Classify each person. Employment contract means Wage; no tax is withheld. Self-employed means the person handles their own Corporate Tax position, and you withhold nothing. If you cannot tell, treat it as a question of fact and look at the contract and how the work is done, not the label on the invoice ([CTGTNP1, section 3.8.1](https://tax.gov.ae/Datafolder/Files/Guides/CT/Taxation%20of%20natural%20persons%20-%2025%2011%202023.pdf)).
2. Before running payroll, resolve the social-compliance holds with a UAE payroll specialist. This Guide supplies no pension deductions, gratuity accrual, WPS timetable or insurance instruction.
3. For the employer's Corporate Tax return, deduct payroll costs as Business expenditure, test related-party pay at Market Value, and cap private pension fund contributions at the limit shown under the figures below ([CTGDTI1](https://tax.gov.ae/DataFolder/Files/Pdf/2024/Determination%20of%20Taxable%20Income%20-%2031%2007%202024.pdf); [Ministerial Decision No. 115 of 2023](https://mof.gov.ae/wp-content/uploads/2023/05/Ministerial-Decision-No.115-of-2023-on-Private-Pension-Funds-and-Private-Social-Security-Funds-for-Corporate-Tax-Purposes.pdf)).
4. For the employer's VAT return, block input tax on goods and services given free to staff for their personal benefit unless an exception applies, and apply the stricter accommodation wording to supplies from 1 October 2026 ([VAT Executive Regulation, Article 53](https://tax.gov.ae/Datafolder/Files/Legislation/2026/Law-No-8-of-2017-and-its-amendments--09-2026.pdf); [Cabinet Decision No. 149 of 2026, as consolidated](https://tax.gov.ae/Datafolder/Files/Legislation/2026/Law-No-8-of-2017-and-its-amendments--09-2026.pdf)).
5. File and pay each item on its own timetable (see "Filing and payment" below) and keep the payroll records that support the Corporate Tax deduction.

### Figures for tax year 2026 ([Cabinet Decision No. 49 of 2023](https://tax.gov.ae/DataFolder/Files/Legislation/05-06-2023/3/Cabinet%20Decision%20No.%2049%20of%202023%20-%20for%20publishing.pdf); [CTGDTI1](https://tax.gov.ae/DataFolder/Files/Pdf/2024/Determination%20of%20Taxable%20Income%20-%2031%2007%202024.pdf); [Ministerial Decision No. 115 of 2023](https://mof.gov.ae/wp-content/uploads/2023/05/Ministerial-Decision-No.115-of-2023-on-Private-Pension-Funds-and-Private-Social-Security-Funds-for-Corporate-Tax-Purposes.pdf))

| Item | 2026 figure | Official source |
|---|---|---|
| Income tax withheld from a Wage | None; Wage is outside Corporate Tax whatever the amount | [Cabinet Decision No. 49 of 2023, Article 2(2)(a)](https://tax.gov.ae/DataFolder/Files/Legislation/05-06-2023/3/Cabinet%20Decision%20No.%2049%20of%202023%20-%20for%20publishing.pdf) |
| Withholding Tax rate (non-resident payments, not wages) | 0% | [CTGDTI1, page 17](https://tax.gov.ae/DataFolder/Files/Pdf/2024/Determination%20of%20Taxable%20Income%20-%2031%2007%202024.pdf) |
| Business turnover above which a self-employed natural person is in Corporate Tax (calendar year) | exceeds AED 1,000,000 | [Cabinet Decision No. 49 of 2023, Article 2(1)](https://tax.gov.ae/DataFolder/Files/Legislation/05-06-2023/3/Cabinet%20Decision%20No.%2049%20of%202023%20-%20for%20publishing.pdf) |
| Maximum deductible private pension fund contribution per member | 15% of the member's total remuneration that is deductible in the Tax Period | [Ministerial Decision No. 115 of 2023, Article 5(2)](https://mof.gov.ae/wp-content/uploads/2023/05/Ministerial-Decision-No.115-of-2023-on-Private-Pension-Funds-and-Private-Social-Security-Funds-for-Corporate-Tax-Purposes.pdf) |
| Entertainment for business partners, customers and similar (not staff) | 50% deduction allowed (the other 50% is disallowed) | [CTGDTI1, section 4.5.10](https://tax.gov.ae/DataFolder/Files/Pdf/2024/Determination%20of%20Taxable%20Income%20-%2031%2007%202024.pdf) |
| Staff entertainment and benefits | Fully deductible if not excessive | [CTGDTI1, sections 4.5.2 and 4.5.10.1](https://tax.gov.ae/DataFolder/Files/Pdf/2024/Determination%20of%20Taxable%20Income%20-%2031%2007%202024.pdf) |

### Social coverage and figures are non-operative holds

Pension (GPSSA, Abu Dhabi and GCC arrangements), gratuity under the Labour Law, WPS, unemployment insurance and free-zone employment regimes are held. The old coverage assertions and instructions have been preserved in evidence/uae-2026-closeout, rather than treated as verified tax-authority guidance.

### VAT on what the employer gives to staff ([VAT Executive Regulation, Article 53, as amended](https://tax.gov.ae/Datafolder/Files/Legislation/2026/Law-No-8-of-2017-and-its-amendments--09-2026.pdf); [Cabinet Decision No. 149 of 2026, as consolidated](https://tax.gov.ae/Datafolder/Files/Legislation/2026/Law-No-8-of-2017-and-its-amendments--09-2026.pdf))

The payroll question for VAT is the input tax a VAT-registered employer pays on things it buys and hands to staff.

**The general block.** Input tax is non-recoverable "Where Goods or Services were purchased to be used by employees for no charge to them and for their personal benefit including the provision of entertainment services", unless one of the listed exceptions applies.

**Earlier periods:** the pre-1 October 2026 labour-law and contract/policy exception wording is a non-operative hold: its earlier standalone source did not open. Obtain the historical text before correcting an earlier return.

**What changes from 1 October 2026.** The September 2026 consolidated Executive Regulation records amendments to exceptions (1) and (2) by Cabinet Decision No. 149 of 2026. The Decision is "effective from 1 October 2026". The new texts:

- (1) now reads "Where the provision of those Goods or Services to the employees is mandatory under the applicable labour legislation in the State or any free zone, including financial and non- financial free zones, provided that this does not include the accommodation provided by the employer to its employees, unless the provision of such accommodation is mandatory pursuant to the decisions or directives issued by the Ministry of Human Resources and Emiratisation."
- (2) now reads "Where it is a contractual obligation or documented policy to provide those Goods or Services to the employees, in accordance with the cases and conditions specified by the Authority."

Article 53(1)(c)(3) also permits health insurance, including enhanced cover, for the employee, one spouse and up to three children younger than 18, without prejudice to the labour-law exception. Article 53(1)(c)(4) covers a provision that is a deemed supply. These exceptions remain subject to the normal invoice, payment, business-use and other VAT recovery conditions.

What this means in practice:

- **Staff accommodation.** From 1 October 2026 the labour-law exception no longer covers accommodation unless a MOHRE decision or directive makes it mandatory. Under exception (2), recovery needs a contractual obligation or documented policy and all the conditions of case 3 or case 4 in the list below. The block only matters where the accommodation carries VAT, such as a hotel stay or a hotel or serviced apartment, which are not "residential buildings" (Executive Regulation, Article 37(2)). Unless zero-rated, a lease of a residential building is exempt "where the lease is more than 6 six months or the tenant of the property is a holder of an ID card issued by Federal Authority for Identity and Citizenship" (Article 43(1)), so an ordinary long staff flat lease has no input tax to block.
- **Contract or policy benefits generally.** The old test (needed for the role, and normal business practice) is replaced by the six cases in [FTA Decision No. 17 of 2026](https://tax.gov.ae/Datafolder/Files/Pdf/2026/legislation/FTA%20Decision%20No.%2017%20of%202026%20on%20the%20Cases%20and%20Conditions%20for%20the%20Recovery%20of%20Input%20Tax%20Incurred%20on%20Employee%20Expenses%20-%20Publishing.pdf), issued 9 September 2026 and in force from 1 October 2026 (the FTA publishes it as an unofficial translation). A benefit outside these cases is not within exception (2):
  1. **Transport:** only between home and work or client premises, or directly for the job; not for personal benefit; the employee cannot opt for cash instead.
  2. **Food and drink:** the home is remote, distant or isolated; no suitable food preparation facilities at home or work and no nearby restaurants; linked to the work or required residence period; no cash option.
  3. **Accommodation:** no cash option; tied to operational needs and not part of benefits or ordinary pay; the work requires living near the workplace, site or client; for the employee alone, with no family or personal use, unless the employee must live permanently near the workplace so that this is the usual home; commensurate with the job and basic needs, with no significant recreational or personal elements.
  4. **New employees' accommodation:** temporary, no longer than 30 days, and commensurate with the job and basic needs.
  5. **Phones, airtime, data and home internet:** necessary for the job; limited to work, or personal use is incidental and insignificant and is not the primary purpose; a documented internal policy states the permitted use and consequences of misuse; reasonable monitoring to verify compliance, retaining relevant records and justifications where use is unauthorised.
  6. **Parking fees:** solely for business and tied to the job or business visits; a documented reimbursement policy specifying eligible cases and the applicable approval mechanism; receipts showing date, time, amount and tax.
- **Health insurance.** Recovery continues for the employee, one spouse and up to three children under 18. Input tax on cover for a fourth child, or a child aged 18 or over, falls outside exception (3) and is blocked unless another exception applies.
- **Entertainment of non-staff.** Input tax on entertainment for customers, potential customers, officials, shareholders or investors stays blocked for non-government employers.

Timing: the new texts and FTA Decision No. 17 of 2026 apply from 1 October 2026; where a cost straddles that date, check with the FTA which text governs it. The changes to the input-tax apportionment rules in the same Decision start later, from the first tax year commencing after 1 October 2027; they are not payroll rules and are covered in `uae-vat`.

### Corporate Tax on payroll costs for the employer ([CTGDTI1, sections 4.5.2 and 4.5.10](https://tax.gov.ae/DataFolder/Files/Pdf/2024/Determination%20of%20Taxable%20Income%20-%2031%2007%202024.pdf); [Ministerial Decision No. 115 of 2023, Article 5](https://mof.gov.ae/wp-content/uploads/2023/05/Ministerial-Decision-No.115-of-2023-on-Private-Pension-Funds-and-Private-Social-Security-Funds-for-Corporate-Tax-Purposes.pdf); [CTGEPF1: Pension Funds and Social Security Funds](https://tax.gov.ae/Datafolder/Files/Guides/CT/Exempt%20Persons%20-%20Public%20Benefit%20Entities%20Pension%20Funds%20and%20Social%20Security%20Funds%20-%2001%2012%202023.pdf))

- **Pay and benefits are deductible.** "Employee costs are generally considered to be wholly and exclusively incurred for Business purposes provided that they are not excessive". It does not matter whether an employee is paid in cash or in benefits such as a car, medical insurance or a flight allowance for family.
- **Related-party pay is tested at Market Value.** Subject to the Article 36(6) listed/regulated-person exceptions, salary or bonus paid to directors, officers or owners "would be deductible ... but only insofar as this salary corresponds with the Market Value rates for such services rendered". Any excess is added back.
- **Staff events are not entertainment.** Staff parties, away-days and performance rewards are employee costs and fully deductible. A private event, such as a family wedding for relatives who happen to work there, is not.
- **Private pension fund contributions.** An employer "may deduct the total value of contributions made to a private pension fund in respect of its employees who are Pension Plan Members in the Tax Period in which such contributions are paid", capped at 15% of that member's total deductible remuneration for the Tax Period. Contributions not paid in the period, or above the cap, are added back.
- **Funds that hold the gratuity.** A private social security fund is "a fund created by a private employer for the purposes of providing statutory end of service gratuity payments to employees". Such a fund, and a private pension fund, can apply to the FTA to be an Exempt Person if it meets the conditions. Public pension and social security funds can also apply for exemption.

## Boundary and exception table

| Situation | Treatment | Watch for |
|---|---|---|
| Employee under an employment contract, any nationality | Wage; no tax withheld | Social coverage, fund routing and deductions are held for specialist confirmation |
| Allowances, bonuses, benefits in kind | Part of the Wage; no tax | VAT input tax on the benefit may be blocked |
| Director who is also an employee | Salary and board fees both typically a Wage | Related/connected-person pay is tested under Articles 34-36, including Article 36(6) exceptions |
| Non-executive director paid fees | Generally not a Business Activity; no Corporate Tax | Confirm the facts; a director running a separate advisory business is different |
| Freelancer or contractor, business turnover not above AED 1,000,000 in the calendar year | No Corporate Tax registration for that person | The payer still withholds nothing |
| Freelancer or contractor, business turnover exceeds AED 1,000,000 in the calendar year | Taxable Person; registers and files Corporate Tax | The test is "exceeds", so exactly AED 1,000,000 is not over it; Wage, Personal Investment income and Real Estate Investment income do not count towards it |
| Health insurance for employee, one spouse, up to three children under 18 | VAT input tax recoverable (exception 3) | A fourth child or a child aged 18 or over is outside the exception |
| Staff accommodation supplied from 1 October 2026 | VAT input tax blocked unless mandatory under MOHRE decisions, or within case 3 or case 4 of FTA Decision No. 17 of 2026 | A cash option defeats case 3. Matters only for accommodation that carries VAT (hotel, hotel or serviced apartment); a residential lease over six months or to an Emirates ID holder is exempt, so there is no input tax |
| Private pension fund contribution | Deductible when paid, up to the 15% cap per member | Unpaid or excess contributions are added back |

## Worked cases

**Case 1: expatriate employee on the mainland.** A Dubai mainland company employs an expatriate on a monthly salary with housing and transport allowances. Corporate Tax result: no Corporate Tax deduction from wages; lawful social and other payroll deductions require a separate determination, because the whole package is a Wage. Social deductions, gratuity, WPS and insurance remain on hold until current coverage and execution instructions are obtained from the relevant authority or specialist. The salary and allowances are deductible in the company's Corporate Tax return if not excessive.

**Case 2: UAE national employee.** The same Wage exclusion applies. This Guide does not determine the pension fund, coverage, rates, deductions or payment timetable. Resolve the social holds before running the payroll.

**Case 3: private pension fund contributions over the cap.** In its 2026 Tax Period a company pays AED 120,000 into a private pension fund for one employee who is a Pension Plan Member. The employee's total deductible remuneration for the period is AED 600,000. The cap is 15% of AED 600,000 = AED 90,000. The company deducts AED 90,000 and adds back AED 30,000 (AED 120,000 less AED 90,000). Had any of the AED 120,000 been accrued but not paid in the period, that part would also be added back for this period.

**Case 4: consultant paid by invoice.** A company engages a self-employed consultant who invoices AED 1,200,000 in calendar year 2026 and has no employment contract. The payments are not a Wage. The company withholds nothing. The consultant's business turnover exceeds AED 1,000,000, so the consultant is within natural-person Corporate Tax scope; registration, relief and the final tax calculation must be tested separately (route the consultant to the `ae-income-tax` skill). The company deducts the fees as a business expense, at Market Value if the consultant is a related party.

**Case 5: health insurance and accommodation, VAT-registered employer.** An employer buys family health cover for an employee with a spouse and four children (ages 4, 9, 14 and 19) and, from October 2026, pays for a serviced apartment for the employee. Input tax on the cover for the employee, spouse and the three children under 18 is recoverable under exception (3). The cover for the 19-year-old is outside exception (3), so its input tax is blocked unless another exception applies. A serviced apartment is excluded from the residential-building definition. In this example assume its supplier makes a standard-rated taxable supply; the exclusion itself does not establish registration or every other VAT condition. Input tax on the October 2026 serviced-apartment charge is blocked unless a MOHRE decision or directive makes that accommodation mandatory, or a contract or documented policy provides it and every condition of case 3 of FTA Decision No. 17 of 2026 is met (or case 4, for a new employee, up to 30 days). If the employee could take a housing allowance instead, or the apartment is part of the ordinary package, it fails case 3. Had the employer instead leased an ordinary residential flat for more than six months (or to a tenant holding an Emirates ID card), the lease would be exempt: there would be no input tax on the rent, and the Article 53 change would not arise.

**Case 3 variant: part unpaid.** Same facts, but AED 40,000 of the AED 120,000 was accrued and not paid in the period. AED 80,000 was paid, which is under the AED 90,000 cap, so the company deducts AED 80,000 and adds back AED 40,000.

**Case 6: executive director with board fees.** An employee who is a senior manager also sits on the board and receives board-meeting fees. Following the FTA's own example, both the salary and the fees are typically a Wage, so neither is taxed. If the director is also a shareholder, the company deducts the pay only to the extent it matches Market Value.

```oa-check
name: Private pension contribution over the cap, Case 3 (2026)
inputs:
  paid: 120000
  remuneration: 600000
  cap_rate: 0.15
steps:
  - cap: remuneration * cap_rate
  - deducted: min(paid, cap)
  - added_back: paid - deducted
expected:
  deducted: 90000.00
  added_back: 30000.00
```

```oa-check
name: Accrued contribution not paid, Case 3 variant (2026)
inputs:
  accrued: 120000
  unpaid: 40000
  remuneration: 600000
  cap_rate: 0.15
steps:
  - paid: accrued - unpaid
  - deducted: min(paid, remuneration * cap_rate)
  - added_back: accrued - deducted
expected:
  deducted: 80000.00
  added_back: 40000.00
```

## When to refuse or refer

- Ask a UAE payroll specialist which pension fund, if any, covers this worker and employer, and which authority supplies the applicable rates, caps, deadlines and penalties. Do not assume Abu Dhabi/GPSSA routing from this Guide or quote rates from memory.
- Ask a UAE employment specialist which law and authority govern a leaving employee's gratuity, particularly with unpaid leave, part-time service, a contract change or a dispute; obtain the applicable calculation before execution.
- Ask the specialist which employment regime and authority govern a free-zone employer, including a financial free zone; do not infer the applicable rules from this Guide.
- Refer any employee who also has UAE business income, or a contractor near the AED 1,000,000 turnover line, to the `ae-income-tax` skill ([Cabinet Decision No. 49 of 2023, Article 2](https://tax.gov.ae/DataFolder/Files/Legislation/05-06-2023/3/Cabinet%20Decision%20No.%2049%20of%202023%20-%20for%20publishing.pdf)).
- Refuse to present the employer's pension, gratuity or insurance figures as confirmed by this skill. It does not contain them.
- Refer tax obligations of the employee in their home country (for example, citizens of countries that tax worldwide income) to that country's rules; UAE payroll does not handle them.

## Filing and payment ([Corporate Tax Law, Articles 48 and 53](https://mof.gov.ae/wp-content/uploads/2026/01/Federal-Decree-Law-No.-47-of-2022-and-its-amendments-en-v13.1.26.pdf); [Cabinet Decision No. 149 of 2026, as consolidated](https://tax.gov.ae/Datafolder/Files/Legislation/2026/Law-No-8-of-2017-and-its-amendments--09-2026.pdf))

- **Employee Corporate Tax:** wages alone produce no Corporate Tax return or payment.
- **Pension contributions:** NON-OPERATIVE HOLD for coverage, fund routing, deduction, frequency, due date and late-payment consequences.
- **Wage Protection System and unemployment insurance:** ask the specialist which obligations, responsible authority and timetable apply. These remain non-operative holds here.
- **Employer's Corporate Tax:** payroll costs go into the employer's Corporate Tax return, which is filed, and any tax paid, no later than nine months after the end of the Tax Period. For a calendar-year company, the 2026 return is due by 30 September 2027. Details are in `ae-corporate-tax`.
- **Employer's VAT:** input tax on staff benefits is claimed only when the VAT recovery conditions are met, in the first eligible period or the next period under VAT Law Article 55. Apply the amended Article 53 texts to periods from 1 October 2026. Details are in `uae-vat`.

### Earlier returns: calendar year 2025 ([Ministerial Decision No. 115 of 2023](https://mof.gov.ae/wp-content/uploads/2023/05/Ministerial-Decision-No.115-of-2023-on-Private-Pension-Funds-and-Private-Social-Security-Funds-for-Corporate-Tax-Purposes.pdf); [Cabinet Decision No. 49 of 2023](https://tax.gov.ae/DataFolder/Files/Legislation/05-06-2023/3/Cabinet%20Decision%20No.%2049%20of%202023%20-%20for%20publishing.pdf))

The 2025 Corporate Tax return of a calendar-year company was due by 30 September 2026. The payroll rules above were the same in 2025: Wage outside Corporate Tax, employee costs deductible if not excessive, private pension contributions deductible when paid up to the 15% cap. The VAT change of 1 October 2026 does not affect 2025 VAT periods; historical exception wording is held for separate confirmation before correcting those periods.

## Completion checklist ([Cabinet Decision No. 49 of 2023](https://tax.gov.ae/DataFolder/Files/Legislation/05-06-2023/3/Cabinet%20Decision%20No.%2049%20of%202023%20-%20for%20publishing.pdf); [Ministerial Decision No. 115 of 2023](https://mof.gov.ae/wp-content/uploads/2023/05/Ministerial-Decision-No.115-of-2023-on-Private-Pension-Funds-and-Private-Social-Security-Funds-for-Corporate-Tax-Purposes.pdf))

- [ ] Every worker classified as employee or self-employed, with the contract on file.
- [ ] No tax deducted from any Wage.
- [ ] Social coverage and fund routing independently confirmed from current authority sources; no social instruction is taken from held old text.
- [ ] Gratuity coverage, accrual and payment method independently confirmed before execution.
- [ ] Specialist asked which WPS and unemployment-insurance obligations, responsible authority and timetable apply; answers obtained from the applicable current authority sources before execution.
- [ ] Related-party salaries checked against Market Value.
- [ ] Private pension contributions: paid in the period and within 15% of each member's deductible remuneration; any excess added back.
- [ ] VAT input tax on staff benefits reviewed against Article 53, using the texts in force from 1 October 2026 for later costs; claims on transport, food, accommodation, phones and parking tested against FTA Decision No. 17 of 2026; exempt residential leases carry no input tax to claim.
- [ ] Health insurance recovery limited to the employee, one spouse and up to three children under 18.
- [ ] Contractors near the AED 1,000,000 turnover line told to check their own Corporate Tax position.

## Sources

| Source and precise scope | URL | Read on |
|---|---|---|
| S01: whole Decision, definitions and arts 1-4 | https://tax.gov.ae/DataFolder/Files/Legislation/05-06-2023/3/Cabinet%20Decision%20No.%2049%20of%202023%20-%20for%20publishing.pdf | 2026-11-01, read: the scope stated in the first column; exact capture/hashes in evidence/uae-2026-closeout/source-identities.json |
| S05: definitions; arts 2-4, 11-13, 18-22, 28-39, 43-58, 66 and 69-70 including neighbours and amendment footnotes | https://mof.gov.ae/wp-content/uploads/2026/01/Federal-Decree-Law-No.-47-of-2022-and-its-amendments-en-v13.1.26.pdf | 2026-11-01, read: the scope stated in the first column; exact capture/hashes in evidence/uae-2026-closeout/source-identities.json |
| S23: Original section 3.8.1, including the complete Example 10 conclusion on salary and board fees, re-read and captured. | https://tax.gov.ae/Datafolder/Files/Guides/CT/Taxation%20of%20natural%20persons%20-%2025%2011%202023.pdf | 2026-11-01, read: the specific scopes in the first column; corrected capture hashes in evidence/uae-2026-closeout/focused-corrections-d75b5305/source-scope-corrections.json |
| S24: Original section 4.5.2 employment expenditure and section 4.5.10.1 staff entertainment re-read and captured. Prior extract omitted these operative paragraphs. Other earlier selected sections are not expanded by this supplement. | https://tax.gov.ae/DataFolder/Files/Pdf/2024/Determination%20of%20Taxable%20Income%20-%2031%2007%202024.pdf | 2026-11-01, read: the specific scopes in the first column; corrected capture hashes in evidence/uae-2026-closeout/focused-corrections-d75b5305/source-scope-corrections.json |
| S25: whole Decision arts 1-7, private-fund definitions/exemption conditions and contributions | https://mof.gov.ae/wp-content/uploads/2023/05/Ministerial-Decision-No.115-of-2023-on-Private-Pension-Funds-and-Private-Social-Security-Funds-for-Corporate-Tax-Purposes.pdf | 2026-11-01, read: the scope stated in the first column; exact capture/hashes in evidence/uae-2026-closeout/source-identities.json |
| S26: Executive Regulation arts 1-8, 29, 31-32, 36-45, 51, 53-54, 57, 59-60, 62-65, 71-75 and 2026 amendment/commencement footnotes; apportionment method excluded | https://tax.gov.ae/Datafolder/Files/Legislation/2026/Law-No-8-of-2017-and-its-amendments--09-2026.pdf | 2026-11-01, read: the scope stated in the first column; exact capture/hashes in evidence/uae-2026-closeout/source-identities.json |
| S27: whole Decision arts 1-3, every subcondition of the six cases, commencement; paired with original Arabic A17 | https://tax.gov.ae/Datafolder/Files/Pdf/2026/legislation/FTA%20Decision%20No.%2017%20of%202026%20on%20the%20Cases%20and%20Conditions%20for%20the%20Recovery%20of%20Input%20Tax%20Incurred%20on%20Employee%20Expenses%20-%20Publishing.pdf | 2026-11-01, read: the scope stated in the first column; exact capture/hashes in evidence/uae-2026-closeout/source-identities.json |
| A17: whole original Arabic Decision arts 1-3, all six cases | https://tax.gov.ae//Datafolder/Files/Pdf/2026/legislation/FTA%20Decision%20No.%2017%20of%202026%20on%20the%20Cases%20and%20Conditions%20for%20the%20Recovery%20of%20Input%20Tax%20Incurred%20on%20Employee%20Expenses%20-%20Publishing-Arabic.pdf | 2026-11-01, read: the scope stated in the first column; exact capture/hashes in evidence/uae-2026-closeout/source-identities.json |

Not yet confirmed: NON-OPERATIVE HOLDS: the broad personal-income-tax assertion beyond the confirmed Wage/Corporate Tax exclusion; all social coverage and routing assertions (UAE/GCC/expatriate, Abu Dhabi fund, first-insurance and free-zone differences), GPSSA/Abu Dhabi contribution rates, bases, caps, deductions, frequency and due dates; Labour Law gratuity coverage, day-count, accrual and payment; WPS and unemployment insurance terms; pre-1 October 2026 employee-benefit exception wording; detailed exemption applications for pension/social security funds. The prior writer recorded blocked GPSSA and legislation-portal access, so the old assertions are preserved as holds, not verified law. The separate MoF Decision 149/2026 URL returned 404 in this repair; the current wording is read in the authority's consolidated Regulation. See immutable old text and destinations in evidence/uae-2026-closeout.

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
