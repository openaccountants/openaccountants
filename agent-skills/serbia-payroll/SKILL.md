---
name: serbia-payroll
description: "Serbian payroll for employers, tax year 2026. Covers the monthly gross-to-net for employees: salary tax at 10% on gross salary less the 2026 non-taxable amount of RSD 34,221 a month (pro rata for part-time and split between employers); employee contributions of 19.9% and employer contributions of 15.15% on a base between RSD 51,297 and RSD 732,820; non-taxable reimbursements from 1 February 2026; the PPP-PD return filed before each payment and payment on the day of payment; what happens when salary is not paid on time; the new-hire salary tax and contribution refunds; and penalties. Trigger on: obračun zarade, porez na zarade, neoporezivi iznos, bruto u neto, PPP-PD, doprinosi na zaradu, trošak poslodavca, Serbia gross to net. Out of scope: contribution rules for the self-employed and founders (serbia-social-contributions), the annual income tax (serbia-income-tax), non-residents and withholding on payments abroad (rs-cross-border)."
license: "AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)"
metadata:
  source: openaccountants
  openaccountants_url: "https://www.openaccountants.com/skills/serbia-payroll"
  jurisdiction: "RS"
  tax_year: "2026"
  last_updated: "2026-10-23"
  trust_label: "Built by Michael Cutajar and the OpenAccountants team"
  review_status: "pending_review"
---

# Serbia: payroll (2026)

Source-cited draft: not reviewed by an accountant, not for filing. Built by the OpenAccountants team.

This skill covers what a Serbian employer does each time it pays a salary in 2026: work out the salary tax and contributions, file the PPP-PD return, and pay. It links to the other Serbia skills and does not repeat them:

- [serbia-social-contributions](serbia-social-contributions.md): contribution rates and bases for everyone, including entrepreneurs, founders and contract income; the new-hire refunds in detail.
- [serbia-income-tax](serbia-income-tax.md): the salary tax rules in the wider income tax, the newly settled employee relief and the annual personal income tax.
- [rs-cross-border](rs-cross-border.md): residence, non-residents, withholding on payments abroad and treaty relief.

Laws used: **ZPDG**, the Personal Income Tax Act (Zakon o porezu na dohodak građana), as it applies in 2026 (amendments up to 109/2025; Law 80/2026 applies from 1 January 2027). **ZDOSO**, the Law on Contributions for Mandatory Social Insurance, as it applies in 2026 (up to 109/2025). **ZPPPA**, the Tax Procedure and Tax Administration Act, for the return and penalties.

## Who this applies to

- **Employers** that pay salary (zarada) to employees: Serbian companies, branches of foreign companies, entrepreneurs and flat-rate entrepreneurs with staff. The employer is the payer that calculates, withholds and pays the salary tax (ZPDG Articles 99 and 101) and the contributions from and on the salary (ZDOSO Article 51(1)).
- **Employees**, resident or not, for work done in Serbia. Salary includes pay in cash or in kind and benefits the employer provides (ZPDG Articles 13 to 14b).
- **Temporary and occasional work** contracts: contributions are paid on the agreed fee like a salary (ZDOSO Article 16). Their income tax treatment is in serbia-income-tax.

Out of scope here: entrepreneurs paying themselves a personal salary (see serbia-social-contributions), labour law beyond the 2026 minimum wage, and annual leave and sick pay rules.

## Rates, bands and thresholds

| Item | Rate or amount | Year | Source |
|---|---|---|---|
| Salary tax | 10% | 2026 | [ZPDG Art. 16](https://www.mfin.gov.rs/propisi/zakon-o-porezu-na-dohodak-gradjana) |
| Non-taxable salary amount, full-time | RSD 34,221 a month | 2026 | [Law 109/2025, Art. 7, in the ZPDG consolidated text](https://www.mfin.gov.rs/upload/media/MOq4eO_6aa14ac8c7a47.docx) |
| Non-taxable salary amount from 2027 | RSD 37,369 a month | 2027 | [ZPDG Art. 15a(2) as amended by 80/2026](https://www.mfin.gov.rs/upload/media/MOq4eO_6aa14ac8c7a47.docx) |
| Employee contributions | PIO 14% + health 5.15% + unemployment 0.75% = 19.9% | 2026 | [ZDOSO Art. 44(2) and (3)](https://www.mfin.gov.rs/propisi/zakon-o-doprinosima-za-obavezno-socijalno-osiguranje) |
| Employer contributions | PIO 10% + health 5.15% = 15.15% | 2026 | [ZDOSO Art. 44(2)](https://www.mfin.gov.rs/propisi/zakon-o-doprinosima-za-obavezno-socijalno-osiguranje) |
| Minimum monthly contribution base | RSD 51,297 | from 1 Jan 2026 | [Minister of Finance, Sl. glasnik 112/2025](https://www.mfin.gov.rs/upload/media/nATlw2_69429ec84247a.docx) |
| Maximum monthly contribution base | RSD 732,820 | from 1 Jan 2026 | [Minister of Finance, Sl. glasnik 112/2025](https://www.mfin.gov.rs/upload/media/mYTnAm_6942704946245.docx) |
| Maximum annual contribution base | RSD 8,793,840 | 2026 | [Minister of Finance, Sl. glasnik 112/2025](https://www.mfin.gov.rs/upload/media/ZKR4zZ_6942708d56248.docx) |
| Commuting costs, documented, not taxed up to | RSD 5,782 a month | from 1 Feb 2026 | [Government, Sl. glasnik 6/2026; ZPDG Art. 18(1)(1)](https://www.mfin.gov.rs/upload/media/O1eqFP_6981bc02426f9.docx) |
| Domestic business travel daily allowance, not taxed up to | RSD 3,471 a day | from 1 Feb 2026 | [Government, Sl. glasnik 6/2026; ZPDG Art. 18(1)(2)](https://www.mfin.gov.rs/upload/media/O1eqFP_6981bc02426f9.docx) |
| Transport on a business trip, not taxed up to | RSD 10,121 | from 1 Feb 2026 | [Government, Sl. glasnik 6/2026; ZPDG Art. 18(1)(5)](https://www.mfin.gov.rs/upload/media/O1eqFP_6981bc02426f9.docx) |
| Solidarity aid for illness or disability, not taxed up to | RSD 57,827 | from 1 Feb 2026 | [Government, Sl. glasnik 6/2026; ZPDG Art. 18(1)(7)](https://www.mfin.gov.rs/upload/media/O1eqFP_6981bc02426f9.docx) |
| New Year and Christmas gift to employees' children under 15, not taxed up to | RSD 14,457 | from 1 Feb 2026 | [Government, Sl. glasnik 6/2026; ZPDG Art. 18(1)(8)](https://www.mfin.gov.rs/upload/media/O1eqFP_6981bc02426f9.docx) |
| Jubilee award, not taxed up to | RSD 28,912 | from 1 Feb 2026 | [Government, Sl. glasnik 6/2026; ZPDG Art. 18(1)(9)](https://www.mfin.gov.rs/upload/media/O1eqFP_6981bc02426f9.docx) |
| Aid on the death of an employee's family member, not taxed up to | RSD 101,194 | from 1 Feb 2026 | [Government, Sl. glasnik 6/2026; ZPDG Art. 18(1)(9a)](https://www.mfin.gov.rs/upload/media/O1eqFP_6981bc02426f9.docx) |
| Employer-paid voluntary health and pension premiums, not taxed up to | RSD 8,677 a month | from 1 Feb 2026 | [Government, Sl. glasnik 6/2026; ZPDG Art. 21a(2); ZDOSO Art. 13(3)](https://www.mfin.gov.rs/upload/media/O1eqFP_6981bc02426f9.docx) |
| New-hire refund of salary tax | 65%, 70% or 75% by number of new hires, on salary paid up to 31 Dec 2026 | 2026 | [ZPDG Art. 21v as amended by 109/2025; Law 80/2026 Art. 2](https://www.parlament.gov.rs/upload/archive/files/cir/doc/zakoni/14_saziv/2551-26.doc) |
| New-hire refund of contributions | 65%, 70% or 75%, on salary paid up to 31 Dec 2026 | 2026 | [ZDOSO Art. 45, text up to 109/2025](https://www.mfin.gov.rs/upload/media/JTHpSm_693c0cc4015d4.docx) |
| Minimum wage | RSD 371 an hour, net of tax and contributions | from 1 Jan 2026 | [Government decision of 11 September 2025](https://www.srbija.gov.rs/vest/en/257386/government-adopts-decision-on-regular-increase-in-minimum-wage.php) |
| Late payment interest | NBS reference rate plus 10 percentage points, simple | 2026 | [ZPPPA Art. 75](https://www.mfin.gov.rs/propisi/zakon-o-poreskom-postupku-i-poreskoj-administraciji-0809) |

## The taxable base

**Salary tax (ZPDG Articles 13 to 16).** The base is the gross salary paid, less RSD 34,221 a month for a full-time employee (Article 15a(2), with the 2026 amount set by Law 109/2025). For part-time work the amount is pro rata to working time. An employee with two or more employers gets one amount in total, split between the employers by working time (Article 15a(3) to (5)). If the gross salary is below the non-taxable amount, there is no salary tax. The tax is 10% of the base (Article 16).

**Contributions (ZDOSO Articles 13 and 36 to 43).** The base is the gross salary, **not** reduced by the non-taxable amount (ZDOSO Article 13(2)). It is held between RSD 51,297 and RSD 732,820 a month. A full-time or part-time employee earning less than RSD 51,297 at a single employer pays on RSD 51,297; a partial month uses a pro rata floor; the ceiling is never reduced (ZDOSO Articles 39 to 41). The full rules, including several employers and the annual cap refund, are in serbia-social-contributions.

**Gross to net.** For each payment:

1. Contribution base = gross, but not below RSD 51,297 or above RSD 732,820.
2. Employee contributions = base × 19.9%, withheld from gross.
3. Salary tax = (gross − RSD 34,221) × 10%, not below zero, withheld from gross.
4. Net pay = gross − employee contributions − salary tax.
5. Employer contributions = base × 15.15%, paid on top.
6. Employer cost = gross + employer contributions.

**Non-taxable reimbursements (ZPDG Article 18).** Commuting, business travel allowances, solidarity aid, children's gifts, jubilee awards and the other items in the table are not taxed as salary up to the amounts shown, which apply from 1 February 2026. In January 2026 the amounts published for 2025 applied. Anything above the limit is part of the salary.

**Employer-paid voluntary health and pension premiums.** Up to RSD 8,677 a month in total is not taxed as salary (ZPDG Article 21a(2)) and not added to the contribution base (ZDOSO Article 13(3)). The excess is.

**New-hire refunds.** An employer that hires a person registered as unemployed for at least six months without a break (three months for a trainee; no minimum for a person up to 30 in the Youth Guarantee programme) can reclaim 65%, 70% or 75% of the salary tax (ZPDG Article 21v) and of the employee and employer contributions (ZDOSO Article 45) on that person's salary. A micro or small company or an entrepreneur that hires at least two such people can reclaim 75% instead (ZPDG Article 21d; ZDOSO Article 45v). In 2026 all four refunds cover salary paid up to 31 December 2026; Law 80/2026 extends them to 31 December 2028 from 1 January 2027 and tightens the conditions from 1 January 2028. The employer pays in full with the salary and then claims the refund on the prescribed form. The conditions are in serbia-social-contributions. Other reliefs for people with disabilities, innovative start-ups and research staff are there too.

**Newly settled employees (ZPDG Article 15v).** 70% of a qualifying newcomer's salary is left out of the salary tax base for five years. The contribution base for the employee and the employer is reduced by 70% too, if the person is insured under the Serbian social insurance laws, including under a social security agreement (ZDOSO Article 15a). The conditions are in rs-cross-border.

## Deadlines and filing

- **Registration.** The employer registers each new employee with the Central Register of Mandatory Social Insurance (CROSO) at the latest before they start work, and reports the end of employment within three working days (CROSO Law Article 12(2)).
- **Return.** The employer files the individual withholding return, PPP-PD, electronically before each salary payment. It covers salary tax and contributions for every employee paid (ZPPPA Article 41(1) to (5)). The return counts as filed only when the Tax Administration confirms it and gives it a number and a payment reference (ZPPPA Article 41(8)).
- **Payment.** Salary tax and contributions are paid on the day the salary is paid, under the rules in force on that day (ZPDG Article 101; ZDOSO Article 51(2)).
- **Salary not paid on time.** If the salary for a month is not paid by the last day of the next month, the employer must file and pay, by that day, contributions on the minimum base of RSD 51,297 (ZDOSO Article 51(3); ZPPPA Article 41(3)). If it does not, the Tax Administration files the return in its place (ZDOSO Article 51(4); ZPPPA Article 41(9)). The difference is paid when the salary is paid (ZDOSO Article 51(5)).
- **Salary paid in parts.** If the first part is below RSD 51,297, contributions on RSD 51,297 are paid with it (ZDOSO Article 52).
- **Year-end certificate.** The employer gives each employee a certificate of the tax withheld by 31 January 2027 for 2026 (ZPPPA Article 41(11)).
- **Annual tax.** The employee, not the employer, files the annual personal income tax return if income is over the threshold. See serbia-income-tax.

## Penalties and interest

- **Interest.** Late tax and contributions carry interest at the NBS reference rate plus 10 percentage points, simple, from the day after the due date (ZPPPA Article 75).
- **Legal entity or entrepreneur (ZPPPA Article 177).**
  - No return and nothing paid: 30% to 100% of the amount due, at least RSD 500,000 for a legal entity and RSD 100,000 for an entrepreneur.
  - Return filed but not paid: 10% to 50%, at least RSD 250,000 for a legal entity and RSD 50,000 for an entrepreneur.
  - Return not filed but paid on time: RSD 100,000 to 2,000,000 for a legal entity, RSD 50,000 to 500,000 for an entrepreneur.
  - Late return, paid on time: RSD 100,000 for a legal entity and RSD 40,000 for an entrepreneur.
  - Late return and late payment, or return on time and late payment: fixed fines by amount due, up to RSD 300,000 for a legal entity.
  - The responsible person in a legal entity is fined separately.
- **Late or missing CROSO registration (CROSO Law Article 40).** RSD 300,000 to 1,500,000 for an employer that is a legal entity; RSD 10,000 to 500,000 for an entrepreneur.
- **Under-declaration (ZPPPA Article 178).** 30% to 40% of the shortfall, at least RSD 200,000 for a legal entity and RSD 100,000 for an entrepreneur.
- **Wrong data in a PPP-PD return, or no certificate to the employee by 31 January (ZPPPA Article 179(1), points 3 and 3a).** RSD 100,000 to 2,000,000 for a legal entity; RSD 50,000 to 500,000 for an entrepreneur.

## Cross-border points

The full rules are in [rs-cross-border](rs-cross-border.md). The points that touch payroll:

- **Non-resident employees.** Salary for work done in Serbia is taxed in Serbia and goes through the PPP-PD like any other salary. A treaty can move the taxing right only under its own dependent services article; see rs-cross-border.
- **Foreign employer with no Serbian payer.** The employee self-assesses the salary tax (ZPDG Article 100a) and the contributions (ZDOSO Article 51(6)).
- **Posted workers.** For an employee sent abroad who stays in the Serbian system, the contribution base is the Serbian salary for similar work and at least twice the minimum base, RSD 102,594 (ZDOSO Article 14).
- **Social security agreements** decide which country's contributions apply. They are separate from tax treaties.
- **Withholding on payments to foreign companies** is not payroll. The 25% rate applies only to companies on the preferential tax jurisdictions list, and only to royalties, interest, rent and services; dividends stay at 20%. The general rate for payments to non-resident companies is 20% unless a treaty gives less. See rs-cross-border.

## Worked examples

### Example 1: full-time employee, gross RSD 150,000

Petar works full time for a Belgrade company. His gross salary for March 2026 is RSD 150,000, between the floor and the ceiling.

- Employee contributions: 150,000 × 19.9% = RSD 29,850.
- Salary tax: (150,000 − 34,221) × 10% = 115,779 × 10% = RSD 11,577.90.
- Net pay: 150,000 − 29,850 − 11,577.90 = RSD 108,572.10.
- Employer contributions: 150,000 × 15.15% = RSD 22,725.
- Employer cost: RSD 172,725.
- The PPP-PD shows salary tax and contributions of 11,577.90 + 29,850 + 22,725 = RSD 64,152.90, paid on the salary payment date.

```oa-check
name: Example 1, full-time employee, gross RSD 150,000 (2026)
inputs:
  gross: 150000
  non_taxable: 34221
  min_base: 51297
  max_base: 732820
steps:
  - base: min(max(gross, min_base), max_base)
  - employee_contrib: base * 0.199
  - salary_tax: max(gross - non_taxable, 0) * 0.10
  - net_pay: gross - employee_contrib - salary_tax
  - employer_contrib: base * 0.1515
  - employer_cost: gross + employer_contrib
  - ppp_pd_total: salary_tax + employee_contrib + employer_contrib
expected:
  base: 150000
  employee_contrib: 29850
  salary_tax: 11577.90
  net_pay: 108572.10
  employer_contrib: 22725
  employer_cost: 172725
  ppp_pd_total: 64152.90
```

### Example 2: senior employee above the contribution ceiling

Ivana is a full-time director with a gross salary of RSD 900,000 in June 2026. That is above the maximum monthly base of RSD 732,820, so contributions stop at the ceiling. Salary tax has no ceiling.

- Contribution base: RSD 732,820.
- Employee contributions: 732,820 × 19.9% = RSD 145,831.18.
- Salary tax: (900,000 − 34,221) × 10% = 865,779 × 10% = RSD 86,577.90.
- Net pay: 900,000 − 145,831.18 − 86,577.90 = RSD 667,590.92.
- Employer contributions: 732,820 × 15.15% = RSD 111,022.23.
- Employer cost: RSD 1,011,022.23.

The edge case: the non-taxable amount reduces only the tax base, and the ceiling reduces only the contribution base. If Ivana's 2026 income, net of salary tax and her own contributions (about RSD 8.0 million from this salary), is over three times the 2026 average annual salary, she owes annual personal income tax for 2026, filed by 15 May 2027; see serbia-income-tax.

```oa-check
name: Example 2, gross RSD 900,000 above the contribution ceiling (2026)
inputs:
  gross: 900000
  non_taxable: 34221
  min_base: 51297
  max_base: 732820
steps:
  - base: min(max(gross, min_base), max_base)
  - employee_contrib: round(base * 0.199, 2)
  - salary_tax: max(gross - non_taxable, 0) * 0.10
  - net_pay: gross - employee_contrib - salary_tax
  - employer_contrib: round(base * 0.1515, 2)
  - employer_cost: gross + employer_contrib
expected:
  base: 732820
  employee_contrib: 145831.18
  salary_tax: 86577.90
  net_pay: 667590.92
  employer_contrib: 111022.23
  employer_cost: 1011022.23
```

## Ask the client first

1. Is the person employed under an employment contract, or engaged under another contract? Contract fees follow different rules (serbia-income-tax and serbia-social-contributions).
2. Full-time or part-time, and does the person work for any other employer in Serbia?
3. What is in the pay: gross salary, benefits in kind, reimbursements (commuting, travel, gifts, jubilee awards), voluntary health or pension premiums?
4. Was the person registered as unemployed before joining, for how long, and how many people has the employer hired? This decides the new-hire refunds.
5. Did the person move to Serbia for the job (newly settled employee relief), or is the employer foreign?
6. On what date is each salary actually paid? Rates, amounts and the PPP-PD follow the payment date.

## Sources

| Source | URL | Read on |
|---|---|---|
| Ministry of Finance: Zakon o porezu na dohodak građana, page and consolidated text up to 80/2026, with the 109/2025 and 80/2026 timing clauses (Arts. 13 to 18, 21a, 21v, 21d, 99 to 101) | https://www.mfin.gov.rs/propisi/zakon-o-porezu-na-dohodak-gradjana ; https://www.mfin.gov.rs/upload/media/MOq4eO_6aa14ac8c7a47.docx | 2026-10-23 |
| National Assembly: law amending the ZPDG (published as 80/2026), showing Arts. 21v and 21d ran to 2026 before it, and its 2027 and 2028 timing | https://www.parlament.gov.rs/upload/archive/files/cir/doc/zakoni/14_saziv/2551-26.doc | 2026-10-23 |
| Government of Serbia: minimum wage for 2026, decision of 11 September 2025 | https://www.srbija.gov.rs/vest/en/257386/government-adopts-decision-on-regular-increase-in-minimum-wage.php | 2026-10-23 |
| Central Register of Mandatory Social Insurance: Zakon o Centralnom registru obaveznog socijalnog osiguranja (Sl. glasnik 95/2018), Arts. 12 and 40 | https://www.croso.gov.rs/storage/files/propisi/Zakon_o_centralnom_registru.pdf | 2026-10-23 |
| Government: adjusted non-taxable amounts under the ZPDG from 1 February 2026 (Sl. glasnik 6/2026) | https://www.mfin.gov.rs/upload/media/O1eqFP_6981bc02426f9.docx | 2026-10-23 |
| Ministry of Finance: Zakon o doprinosima za obavezno socijalno osiguranje, page and consolidated text up to 80/2026 | https://www.mfin.gov.rs/propisi/zakon-o-doprinosima-za-obavezno-socijalno-osiguranje ; https://www.mfin.gov.rs/upload/media/c59gCf_6aa14bd2e2c04.docx | 2026-10-23 |
| Ministry of Finance: Zakon o doprinosima za obavezno socijalno osiguranje, consolidated text up to 109/2025 (the version for 2026) | https://www.mfin.gov.rs/upload/media/JTHpSm_693c0cc4015d4.docx | 2026-10-23 |
| Minister of Finance: minimum and maximum monthly and maximum annual contribution bases for 2026 (Sl. glasnik 112/2025) | https://www.mfin.gov.rs/upload/media/nATlw2_69429ec84247a.docx ; https://www.mfin.gov.rs/upload/media/mYTnAm_6942704946245.docx ; https://www.mfin.gov.rs/upload/media/ZKR4zZ_6942708d56248.docx | 2026-10-23 |
| Ministry of Finance: Zakon o poreskom postupku i poreskoj administraciji, consolidated text (Arts. 41, 75, 177, 178, 179) | https://www.mfin.gov.rs/propisi/zakon-o-poreskom-postupku-i-poreskoj-administraciji-0809 ; https://www.mfin.gov.rs/upload/media/2UkJa3_6a9fe325297c3.docx | 2026-10-23 |

Not yet confirmed: the non-taxable reimbursement amounts that applied in January 2026; the Sl. glasnik number of the 2026 minimum wage decision; whether the CROSO Law has been amended since 2019; the current NBS reference rate for late payment interest.

> Contributed by Ryan Duguid.

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

## Today's figures and who stands behind this skill

This file is an AI skill (tax rules your AI follows) from OpenAccountants, copied on 2026-10-23. Rates, thresholds and deadlines change. For the current version of this skill, its official sources and the named accountant (if any) who stands behind it, call `get_skill` with slug `serbia-payroll` on the OpenAccountants connector (https://www.openaccountants.com/connect), or read https://www.openaccountants.com/skills/serbia-payroll. If neither is available, confirm every figure against the official source pages cited above before relying on it.
