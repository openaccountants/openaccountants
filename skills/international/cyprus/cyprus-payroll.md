---
name: cyprus-payroll
description: "Cyprus payroll for tax year 2026: PAYE income tax withheld by employers under the Income Tax Law 118(I)/2002 as amended by Law 244(I)/2025 and the Assessment and Collection of Taxes Law 4/1978, with the employee and employer contributions an employer deducts or pays. Covers the T.D.59A declaration, the 2026 bands with the EUR 22,000 tax-free band, the one-fifth cap, the 20% and 50% first-employment deductions through payroll, the 13 or 12 divisor, Social Insurance at 8.8% plus 8.8% up to the 2026 ceiling of EUR 5,742 a month, GHS at 2.65% and 2.90%, the Redundancy, HRDA, Social Cohesion and Central Holiday funds, the minimum wage, monthly PAYE returns through TFA, deadlines and the 1% monthly surcharge. Trigger on: Cyprus payroll 2026, PAYE Cyprus, TD59, TD7, TD63, gross to net Cyprus, employer cost Cyprus. Out of scope: cyprus-social-contributions (self-employed, voluntary, GHS on other income), cyprus-income-tax, cy-cross-border, cy-non-dom."
version: 0.2
jurisdiction: CY
tax_year: 2026
last_updated: 2026-10-26
authored_by: Michael Cutajar and the OpenAccountants team
review_status: pending_review
trust_label: Built by Michael Cutajar and the OpenAccountants team
depends_on:
  - payroll-workflow-base
category: international
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Cyprus payroll: PAYE and employer contributions (tax year 2026)

Source-cited draft: not reviewed by an accountant, not for filing.

This skill covers running payroll for employees in Cyprus in 2026: income tax withheld under PAYE, the employee's Social Insurance and GHS (GESY) contributions the employer deducts, the employer's own contributions and funds, the minimum wage, and the employer's returns and deadlines. The tax year is the calendar year. The 2026 tax reform (Law 244(I)/2025, in force 1 January 2026) applies to every 2026 pay period. Article numbers are to the Greek consolidated texts on CyLaw, which is not the official gazette.

Sibling skills: contribution detail (self-employed, voluntary contributors, GHS on rent, dividends and interest, late charges) is in `cyprus-social-contributions`; the employee's own return and personal deductions in `cyprus-income-tax`; residence, A1 forms and non-residents in `cy-cross-border`; SDC in `cy-non-dom`.

## Who this applies to

- **Every employer** that pays an employee working in Cyprus. A company director, or anyone involved in managing a company, counts as an employee for PAYE (T.D.59A note 15).
- **Registration before hiring.** The employer registers with the Tax Department as an employer (form through the Tax For All (TFA) portal) and with Social Insurance Services in the Register of Employers (form YKA 01-001) before recruiting. Each hire is notified through ERGANI no later than one day before the person starts (Business in Cyprus page).
- **Employee TIN.** Every employee's TIN must appear on every monthly PAYE return (PAYE FAQ). If an employee has none, use the Tax Department's employee registration check; for someone the employer has lost contact with, send a TFA message attaching the ERGANI terms of employment and termination. An employee without a Social Insurance number is registered on form YKA 1-008 (Social Insurance Services, registration of employees).
- **Out of scope:** the self-employed (use `cyprus-social-contributions` and `cyprus-income-tax`); employees insured in another EU or EEA state under an A1 form, posted workers and non-resident employers (refer; see `cy-cross-border`).

## Rates, bands and thresholds

| Item | Rate or amount | Year | Source |
|---|---|---|---|
| 0% band, chargeable income up to | EUR 22,000 | 2026 | ITL Second Schedule para. 1(γ), https://www.cylaw.org/nomoi/enop/non-ind/2002_1_118/full.html |
| 20% / 25% / 30% bands | EUR 22,001 to 32,000 / 32,001 to 42,000 / 42,001 to 72,000 | 2026 | Same URL; also T.D. FAQs 11 May 2026, https://www.gov.cy/media/sites/167/2026/05/FAQs-110526.pdf |
| 35% band | over EUR 72,000 (tax at EUR 72,000 is EUR 13,500) | 2026 | Same URLs |
| Social Insurance, employee share | 8.8% of insurable earnings | 2026 | Business in Cyprus, https://www.businessincyprus.gov.cy/social-insurance-registration-and-contributions/ |
| Social Insurance, employer share | 8.8% of insurable earnings | 2026 | Same URL |
| Social Insurance, state share (not an employer cost) | 5.2% | 2026 | Same URL |
| Maximum insurable earnings, monthly-paid | EUR 5,742 a month from 1 January 2026 | 2026 | Social Insurance Services notice, December 2025, https://sisweb.mlsi.gov.cy/anotato2025/ |
| Maximum insurable earnings, weekly-paid | EUR 1,325 a week from 5 January 2026 | 2026 | Same URL |
| GHS, employee | 2.65% of pay | 2026 | GHS Law 89(I)/2001 art. 19(1)(α), https://www.cylaw.org/nomoi/enop/non-ind/2001_1_89/full.html |
| GHS, employer | 2.90% of each employee's pay | 2026 | GHS Law art. 19(1)(β), same URL |
| GHS annual maximum per person, all income added | EUR 180,000 | 2026 | GHS Law art. 19(4)(α); T.D.59A 2026 note 22, https://www.gov.cy/media/sites/167/2026/02/IR59_2026_English__.pdf |
| Redundancy Fund (employer only, up to the ceiling) | 1.2% | 2026 | Business in Cyprus page above |
| Human Resources Development Fund (employer only, up to the ceiling) | 0.5% | 2026 | Same URL |
| Social Cohesion Fund (employer only, no ceiling) | 2% of total earnings | 2026 | Same URL; Social Insurance Services contributions page, https://www.mlsi.gov.cy/mlsi/sdg/sdg.nsf/All/EA4F396F80C4BAA8C22586A10042659F?OpenDocument |
| Central Holiday Fund (employer only, unless exempt) | 8% at 20 days of leave to 16% at 40 days (five-day week) | 2026 | Social Insurance Services, Annual Leave, https://www.mlsi.gov.cy/mlsi/sdg/sdg.nsf/All/00DDEF169CC27CAEC22586B7003F35FE?OpenDocument |
| One-fifth cap on contributions and premiums | 1/5 of the intermediary figure B6 | 2026 | ITL art. 14(2); T.D.59A note 10 |
| First-employment deduction, 20% option | 20% of pay, max EUR 8,550 | 2026 | ITL art. 8(21A); T.D.59A note 7 |
| First-employment deduction, 50% option | 50% of pay where pay exceeds EUR 55,000 (art. 8(23A)) or EUR 100,000 (old art. 8(23)) | 2026 | ITL arts. 8(23), 8(23A); T.D.59A note 7 |
| Minimum wage, full time, after 6 months' continuous employment | EUR 1,088 a month from 1 January 2026 | 2026 | Ministry of Labour statement, 27 December 2025, https://www.gov.cy/ergasia-kai-koinonikes-asfaliseis/dilosi-tou-ypourgou-ergasias-kai-koinonikon-asfaliseon-gia-tin-afxisi-tou-ethnikou-katotatou-misthou/ |
| Minimum wage, full time, before 6 months | EUR 979 a month from 1 January 2026 | 2026 | Same URL |
| PAYE late-payment surcharge | 1% for each month of delay | 2026 | ACL art. 44(2), as stated in the PAYE FAQ, https://www.gov.cy/mof-tax/documents/ypovoli-diloseon-t-f-7/dilosi-parakratisis-f-e-kai-eisforon-paye/sychnes-erotiseis-diloseon-parakratisis-f-e-kai-eisforon-paye/ |
| Late Social Insurance, Social Cohesion and GHS contributions | 3% for the first month, plus 3 points a month, max 27% | 2026 | Social Insurance Services, deadlines, https://www.mlsi.gov.cy/mlsi/sdg/sdg.nsf/All/D5322D5E5CD6F735C22586A10044EC34 |

The Social Insurance Law 59(I)/2010 art. 5(1)(στ) prints 8.9% employee, 8.9% employer and 5.3% state from 2024, with a proviso that lower rates shown by the actuarial study apply instead. Social Insurance Services and Business in Cyprus apply 8.8%, 8.8% and 5.2%. Use 8.8%. The instrument setting 8.8% was not found (see Sources).

## The taxable base

**PAYE works from the T.D.59A.** Each employee signs a T.D.59A every year and on hiring. It declares other income and the deductions and exemptions claimed. The employer fills the second column, applies the limits in the notes, and computes chargeable income (A8 less total allowances B15) and the tax on it (C1). Without a T.D.59A, the employer allows only the contributions it already knows about (B7 and B8) and still withholds (note 15).

**Pay.** All pay and benefits are taxable: wages, overtime, tips, bonuses, commissions, fees, perquisites and benefits in kind (note 16; ITL art. 5(1)(β)). Benefits in kind are valued at market value under the Tax Department leaflet (https://www.gov.cy/mof-tax/documents/paroches-se-eidos/). A loan to a director or shareholder is a deemed benefit of 9% a year on the balance (ITL art. 5(1)(ζ)); it goes in line A2.

**Order of the computation.**
1. Insurable earnings: gross pay for the period, capped at EUR 5,742 a month or EUR 1,325 a week. If the employer pays into the Central Holiday Fund, its contribution is added to earnings first (Social Insurance Services contributions page, worked example).
2. Employee Social Insurance (8.8%) on insurable earnings. Employee GHS (2.65%) on pay, uncapped until the person's income for the year passes EUR 180,000.
3. Deduct the contributions within the one-fifth cap, any documented first-employment deduction (line B2), and the personal deductions the employee declares (children, housing, green). The art. 14B personal deductions sit outside the one-fifth cap and are declared as a final amount per category, without income or children details (T.D. FAQs, questions 10 and 11).
4. Apply the 2026 bands to get C1. The employer withholds only the share for the pay it pays: C1 x (A1 + A2 + A3) / A6 (Part C line 2). It never withholds tax on rent or other non-employment income; the employee pays that through provisional tax (note 21; see `cyprus-income-tax`).
5. Monthly withholding is C2 / 13 or C2 / 12 "accordingly"; weekly is C2 / 52 (Part C line 3). Divide by 13 where a thirteenth salary is paid (this skill's reading). Tax on bonuses and other income not paid regularly is withheld in the month it is paid (note 16).

**Two employers.** Each employer withholds on its own pay, using the total income the employee declares on the T.D.59A given to that employer (PAYE FAQ).

**New-resident exemptions in payroll.** Apply only with evidence of every condition. The T.D.59A (note 7) allows one of: 20% of pay up to EUR 8,550 (art. 8(21) or 8(21A)); 50% where pay exceeds EUR 100,000 (old art. 8(23)); 50% where pay exceeds EUR 55,000 (art. 8(23A)). The 50% minimum is a cliff: in a year pay does not exceed it, nothing is exempt. For employment starting on or after 30 June 2023, art. 8(23A) needs 15 consecutive tax years without paid work in Cyprus. The 25% art. 8(21B) exemption is not listed at line B2; do not apply it through payroll, the employee claims it in the return. Full conditions are in `cyprus-income-tax`.

**Exemptions do not cut contributions.** Social Insurance is on insurable earnings and GHS on the Part A income lines, not on income after Part B deductions (note 22).

**Employer cost**, on top of gross pay: Social Insurance 8.8%, Redundancy 1.2% and HRDF 0.5% on insurable earnings; Social Cohesion 2% on total earnings with no ceiling; GHS 2.90% on pay within the EUR 180,000 maximum; the Central Holiday Fund unless the employer holds an exemption (form YKA 1-005). Never quote 22.8% as the employer's cost: it is the combined employee, employer and state rate.

**Pensionable age.** The employer's Social Insurance Fund contributions stop when the employee reaches 65, unless the employee does not yet qualify for a pension; never after 68 (Social Insurance Services, general information). The page says nothing about GHS or the other funds.

## Deadlines and filing

| What | When | Source |
|---|---|---|
| Monthly PAYE return (income tax and contributions withheld), through TFA, every employee listed with TIN | End of the month after the month of withholding | Tax Department deadlines, https://www.gov.cy/mof-tax/prothesmies/ |
| Payment of PAYE | Within one month from the end of the month of withholding; the return must be filed first because it creates the debt | PAYE FAQ |
| Annual PAYE return (T.D.7) for 2026 | 31 March 2027 | Tax Department deadlines |
| Annual PAYE return for 2025 | Extended to 30 November 2026 (notice of 16 September 2026) | Tax Department deadlines |
| GHS withheld on employee benefits and employer GHS on them, paid to the Tax Department | End of the following month | Tax Department deadlines |
| Social Insurance, GHS on pay and the employer funds, to Social Insurance Services | End of the calendar month after the month they are for | Social Insurance Services, deadlines page |
| T.D.63 certificate of earnings | Each year, to current and past employees | https://www.gov.cy/mof-tax/en/documents/certificate-of-earnings-t-d-63/ |
| T.D.59A | Each year and on hiring | https://www.gov.cy/mof-tax/en/documents/declaration-for-claiming-tax-deductions-t-d-59/ |

Monthly PAYE returns are mandatory from 1 January 2025. Amending a return is not late filing, but extra tax from it carries the surcharge and interest. At least one monthly return must exist before the annual return can be filed. A thirteenth salary is reported in the month it is paid (PAYE FAQ).

## Penalties and interest

- **Late PAYE payment:** a 1% surcharge charged on the 1st of the month after the last payment date and on every 1st of the month until paid (ACL art. 44(2), PAYE FAQ). Interest starts after one complete further month, at the public default rate, 3.50% a year from 1 January 2026 (ACL art. 39(1); K.D.P. 376/2025).
- **Late Social Insurance, Social Cohesion and GHS contributions:** an additional charge of 3% of the contributions for the first month of delay, rising 3 points a month to 27% (Social Insurance Services, deadlines page).
- **Failing to pay GHS contributions:** an offence, fine up to EUR 3,400 or imprisonment, and the court can order payment of the contribution plus up to 50% more (GHS Law art. 20(7) and (8)).
- **Business closure:** from 1 January 2027, failing to file twelve monthly withholding returns can lead to suspension of the business for up to 10 days after three registered-mail notices (ACL art. 32A); see `cyprus-income-tax`.
- Unpaid salaries on which contributions were not paid in time are not deductible for the employer until paid (ITL art. 9).

## Cross-border points

- An employee insured in another EU or EEA state or Switzerland under an A1 form does not pay Cyprus Social Insurance on that pay; Regulation 883/2004 decides which state. Refer, and see `cy-cross-border`.
- GHS: a non-resident pays GHS only on Cyprus-source income (Health Insurance Organisation, GHS financing page). Payroll GHS on Cyprus pay still applies.
- New arrivals: check the 20% and 50% deductions above before the first payroll; residence rules are in `cy-cross-border`.
- An employer with its registered office in another EU or EEA state or Switzerland registers with Social Insurance Services under a separate procedure (deadlines page menu). Refer.

## Worked examples

### Example 1: EUR 2,500 a month, 12 payments

Eleni earns EUR 2,500 a month, 12 payments, no other income, no exemption. Her pay is below the EUR 5,742 ceiling. Social Insurance is 8.8% of EUR 30,000, EUR 2,640. GHS is 2.65%, EUR 795. Both are well under the one-fifth cap of EUR 6,000. Chargeable income is EUR 26,565. Tax is 20% of the EUR 4,565 above EUR 22,000, EUR 913, or EUR 76.08 a month. Monthly net pay is EUR 2,500 less EUR 220 Social Insurance, EUR 66.25 GHS and EUR 76.08 tax: EUR 2,137.67. The employer also pays EUR 220 Social Insurance, EUR 30 Redundancy, EUR 12.50 HRDF, EUR 50 Social Cohesion and EUR 72.50 GHS a month, EUR 385 in all, before any Central Holiday Fund.

```oa-check
name: Eleni, EUR 2,500 a month, 12 payments (2026)
inputs:
  monthly: 2500
  payments: 12
steps:
  - annual: monthly * payments
  - si_employee: annual * 0.088
  - ghs_employee: annual * 0.0265
  - cap: annual / 5
  - deductible: min(si_employee + ghs_employee, cap)
  - chargeable: annual - deductible
  - tax: max(0, min(chargeable, 32000) - 22000) * 0.20 + max(0, min(chargeable, 42000) - 32000) * 0.25 + max(0, min(chargeable, 72000) - 42000) * 0.30 + max(0, chargeable - 72000) * 0.35
  - monthly_tax: round(tax / payments, 2)
  - net_monthly: monthly - monthly * 0.088 - monthly * 0.0265 - monthly_tax
  - employer_monthly: monthly * (0.088 + 0.012 + 0.005 + 0.02 + 0.029)
expected:
  si_employee: 2640
  ghs_employee: 795
  chargeable: 26565
  tax: 913
  monthly_tax: 76.08
  net_monthly: 2137.67
  employer_monthly: 385
```

### Example 2: EUR 7,000 a month, above the Social Insurance ceiling

Andreas earns EUR 7,000 a month, 12 payments, no exemption and no other income. Social Insurance stops at the EUR 5,742 ceiling: 8.8% x 5,742 is EUR 505.30 a month, EUR 6,063.60 a year. GHS has no monthly ceiling, so it is 2.65% of the full EUR 84,000, EUR 2,226. Chargeable income is EUR 75,710.40, in the 35% band. Tax is EUR 13,500 plus 35% of EUR 3,710.40, EUR 14,798.64, so EUR 1,233.22 a month. The employer pays Social Insurance, Redundancy and HRDF on EUR 5,742 only, but Social Cohesion (EUR 140) and GHS (EUR 203) on the full EUR 7,000.

```oa-check
name: Andreas, EUR 7,000 a month, above the EUR 5,742 ceiling (2026)
inputs:
  monthly: 7000
  ceiling: 5742
  payments: 12
steps:
  - insurable: min(monthly, ceiling)
  - si_month: round(insurable * 0.088, 2)
  - si_year: si_month * payments
  - ghs_year: monthly * payments * 0.0265
  - annual: monthly * payments
  - chargeable: annual - min(si_year + ghs_year, annual / 5)
  - tax: max(0, min(chargeable, 32000) - 22000) * 0.20 + max(0, min(chargeable, 42000) - 32000) * 0.25 + max(0, min(chargeable, 72000) - 42000) * 0.30 + max(0, chargeable - 72000) * 0.35
  - monthly_tax: round(tax / payments, 2)
  - employer_capped: round(insurable * (0.088 + 0.012 + 0.005), 2)
  - employer_uncapped: monthly * (0.02 + 0.029)
  - employer_monthly: employer_capped + employer_uncapped
expected:
  si_month: 505.30
  si_year: 6063.60
  ghs_year: 2226
  chargeable: 75710.40
  tax: 14798.64
  monthly_tax: 1233.22
  employer_capped: 602.91
  employer_uncapped: 343
  employer_monthly: 945.91
```

## Ask the client first

- Is pay monthly or weekly, and is there a thirteenth salary, bonuses or benefits in kind? (Ceiling, divisor and the month tax is withheld.)
- Has each employee signed a 2026 T.D.59A, and does any have another employer, a pension or rent? (Chargeable income and the share withheld.)
- Did the employee move to Cyprus for the job, when did it start, and what evidence is there for the 20% or 50% conditions? (Can cut tax sharply.)
- Does the employer hold a Central Holiday Fund exemption, and what leave does each employee get? (Employer cost and the base.)
- Is any employee insured in another EU or EEA state, a director, or 65 or over? (A1 cases, directors count as employees, contributions at pension age.)

## Sources

| Source | URL | Read on |
|---|---|---|
| Income Tax Law 118(I)/2002, consolidated (CyLaw): arts. 5, 8(21) to 8(23A), 9, 14, Second Schedule | https://www.cylaw.org/nomoi/enop/non-ind/2002_1_118/full.html | 2026-10-24 |
| Social Insurance Law 59(I)/2010, consolidated (CyLaw): arts. 4, 5 | https://www.cylaw.org/nomoi/enop/non-ind/2010_1_59/full.html | 2026-10-26 |
| General Healthcare System Law 89(I)/2001, consolidated (CyLaw): arts. 19, 20 | https://www.cylaw.org/nomoi/enop/non-ind/2001_1_89/full.html | 2026-10-26 |
| Social Insurance Services, 2026 maximum insurable earnings notice | https://sisweb.mlsi.gov.cy/anotato2025/ | 2026-10-26 |
| Business in Cyprus (government), social insurance registration and contributions | https://www.businessincyprus.gov.cy/social-insurance-registration-and-contributions/ | 2026-10-26 |
| Social Insurance Services, contributions | https://www.mlsi.gov.cy/mlsi/sdg/sdg.nsf/All/EA4F396F80C4BAA8C22586A10042659F?OpenDocument | 2026-10-26 |
| Social Insurance Services, deadlines and additional charge | https://www.mlsi.gov.cy/mlsi/sdg/sdg.nsf/All/D5322D5E5CD6F735C22586A10044EC34 | 2026-10-26 |
| Social Insurance Services, annual leave (Central Holiday Fund rates, form 1-005) | https://www.mlsi.gov.cy/mlsi/sdg/sdg.nsf/All/00DDEF169CC27CAEC22586B7003F35FE?OpenDocument | 2026-10-26 |
| Social Insurance Services, general information (age 65 and 68) | https://www.mlsi.gov.cy/mlsi/sdg/sdg.nsf/All/A0E4DA6A3979A4EAC22586A100418A7A?OpenDocument | 2026-10-26 |
| Social Insurance Services, registration of employees (form 1-008) | https://www.mlsi.gov.cy/mlsi/sdg/sdg.nsf/All/DF541D1E90F75C56C22586A10042515C?OpenDocument | 2026-10-26 |
| Health Insurance Organisation, GHS financing | https://www.gesy.org.cy/sites/Sites?d=Desktop&locale=en_US&lookuphost=/en-us/&lookuppage=hiofinancing | 2026-10-26 |
| Tax Department, T.D.59A 2026 (English) | https://www.gov.cy/media/sites/167/2026/02/IR59_2026_English__.pdf | 2026-10-26 |
| Tax Department, FAQs on the 2026 reform (11 May 2026) | https://www.gov.cy/media/sites/167/2026/05/FAQs-110526.pdf | 2026-10-24 |
| Tax Department, PAYE FAQ | https://www.gov.cy/mof-tax/documents/ypovoli-diloseon-t-f-7/dilosi-parakratisis-f-e-kai-eisforon-paye/sychnes-erotiseis-diloseon-parakratisis-f-e-kai-eisforon-paye/ | 2026-10-26 |
| Tax Department, deadlines calendar | https://www.gov.cy/mof-tax/prothesmies/ | 2026-10-26 |
| Tax Department, employer registration | https://www.gov.cy/mof-tax/en/documents/registration-deregistration-as-an-employer/ | 2026-10-16 |
| Tax Department, benefits in kind | https://www.gov.cy/mof-tax/documents/paroches-se-eidos/ | 2026-10-16 |
| Assessment and Collection of Taxes Law 4/1978, consolidated (CyLaw): arts. 32A, 39, 44 | https://www.cylaw.org/nomoi/enop/non-ind/1978_1_4/full.html | 2026-10-24 |
| Public Default Interest Rate for 2026 Order, K.D.P. 376/2025 | https://www.cylaw.org/KDP/data/2025_1_376.pdf | 2026-10-24 |
| Ministry of Labour, minimum wage statement (27 December 2025) | https://www.gov.cy/ergasia-kai-koinonikes-asfaliseis/dilosi-tou-ypourgou-ergasias-kai-koinonikon-asfaliseon-gia-tin-afxisi-tou-ethnikou-katotatou-misthou/ | 2026-10-26 |

Not yet confirmed: the instrument that sets 8.8% / 8.8% / 5.2% in place of the 8.9% / 8.9% / 5.3% printed in Social Insurance Law art. 5(1)(στ) (the actuarial-study proviso; the Order was not found on CyLaw); the Minimum Wage (Amending) Order of 2025 itself (only the ministry statement was read); whether the employer may apply the 25% art. 8(21B) exemption through PAYE; the 13 divisor reading for a thirteenth salary (the form says only "accordingly"); how the monthly ceiling applies in a month in which a thirteenth salary is paid; the Central Holiday Fund rate above 40 days of leave ("increased accordingly"); the bank-statement pattern library, payslip glossary, Excel working-paper template and onboarding checklist from v0.1 (practice notes, not law, not carried).

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
