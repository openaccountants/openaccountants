---
name: albania-payroll
description: "Albanian monthly payroll for tax year 2026: how an employer computes and pays employment income tax (TAP) at 13% and 23% with the art. 22 monthly deductions, employee and employer social and health contributions within the ALL 50,000 floor and ALL 186,416 social ceiling, net pay and total employer cost, and files the monthly listëpagesa (E-SIG 025/a) with payment by the 20th. Covers the personal status declaration, second employers, part-time staff, new-hire notice (E-SIG 027/a), the annual position on the employee's DVAP return, and Law 9920/2008 penalties and interest. Trigger on 'Albania payroll', 'listëpagesa', 'gross to net Albania', 'TAP Albania', 'employer cost Albania', 'E-SIG 025'. Out of scope: contribution rules for the self-employed and special categories (albania-social-contributions), the annual return and other income (albania-income-tax), companies (al-corporate-tax), treaties (al-cross-border)."
version: 0.2
jurisdiction: AL
tax_year: 2026
last_updated: 2026-10-23
review_status: pending_review
trust_label: Built by Michael Cutajar and the OpenAccountants team
verified_by: pending
depends_on:
  - payroll-workflow-base
category: international
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Albania payroll, tax year 2026

> **Source-cited draft.** Built by Michael Cutajar and the OpenAccountants team from Law No. 29/2023, General Instruction No. 26/2023, Law No. 9920/2008, Council of Ministers Decisions No. 77/2015 and No. 776/2025, and General Directorate of Taxes notices, read on 2026-10-23. No accountant has reviewed it. Do not run a payroll from it without review by a qualified Albanian professional.

Tax year: the calendar year. Currency: Albanian lek (ALL). The General Directorate of Taxes (tatime.gov.al) collects employment income tax and both social and health contributions on one return, the listëpagesa, filed on e-Filing. The Social Insurance Institute (issh.gov.al) and the Compulsory Health Insurance Fund (fsdksh.gov.al) receive the contributions.

See also: `albania-social-contributions` (contribution rules in full, self-employed, special categories), `albania-income-tax` (scales, deductions, the annual DVAP return), `al-cross-border`.

## Who this applies to

**Employers.** Every employer that pays employment income is a payroll tax agent (agjent tatimor i listëpagesës). It must withhold the tax, file the listëpagesa and pay the tax over (Law 29/2023 art. 65(1)). It also calculates, declares and pays employee and employer social and health contributions for every employee, full or part time, from the first day of work (Law 7703/1993 art. 13; Law 10383/2011 art. 6(1); ISSH, compulsory insurance page). The employer is liable for the tax as if it were its own debt (art. 65(4)).

**Employees.** Anyone paid under an employment or similar relationship, including directors and partners paid for work in their company (Law 29/2023 art. 12). Foreign nationals working in Albania are covered on the same terms (Law 7703/1993 art. 7). Self-employed persons who meet the art. 12(1)(ç) disguised-employment test are taxed as employees on their annual return, not through a payroll: see `albania-income-tax`.

**Not payroll.** A one-off payment to an individual who is not an employee (a board member employed elsewhere, an occasional consultant or trainer) bears 15% withholding on the gross, not the payroll scale. No tax is withheld if that individual is self-employed with a NIPT (Law 29/2023 art. 65(1)(b); Instruction 26 para. 65).

## Rates, bands and thresholds

| Item | Rate or amount | Tax year | Source |
|---|---|---|---|
| National minimum wage, monthly | ALL 50,000 for 174 hours; ALL 287.3 an hour | 2026 (from 1 Jan) | [Council of Ministers Decision 776/2025](https://www.issh.gov.al/wp-content/uploads/2026/08/VKM-NR.-776-DATE-19.12.2025-PER-PERCAKTIMIN-E-PAGES-MINIMALE-NE-SHKALLE-VENDI.pdf) |
| Minimum monthly base, social and health contributions | ALL 50,000 | 2026 | [tatime.gov.al notice, 14.01.2026](https://tatime.gov.al/nga-1-janari-2026-rritet-paga-minimale-dhe-maksimale/) |
| Maximum monthly base, social contributions | ALL 186,416 (ALL 176,416 to 31.12.2025) | 2026 | [tatime.gov.al notice, 14.01.2026](https://tatime.gov.al/nga-1-janari-2026-rritet-paga-minimale-dhe-maksimale/); Law 7703/1993 art. 10 |
| Maximum base, health contribution | None: full gross pay | 2026 | [Instruction 26/2023, payroll form item 24](https://tatime.gov.al/wp-content/uploads/2026/09/Udhezimi-nr-26-date-8.9.2023-Per-tatimin-mbi-te-ardhuart.pdf); Law 10383/2011 art. 7(1) |
| Social insurance, employee working more than 87 hours a month | Employer 15.0%, employee 9.5% (total 24.5%) | 2026 | [Decision 77/2015 ch. III para. 3(a)](https://www.issh.gov.al/wp-content/uploads/2026/08/VENDIM-NR.-77-DATE-28.1.2015-PER-KONTRIBUTET-E-DETYRUESHME-DHE-PERFITIMET-NGA-SISTEMI-I-SIGURIMEVE-SHOQERORE-DHE-SIGURIMI-I-KUJDESIT-SHENDETESOR.pdf) |
| Social insurance, employee working less than 87 hours a month | Employer 13.9%, employee 9.4% (total 23.3%) | 2026 | Decision 77/2015 ch. III para. 4(a) |
| Social insurance, contract shorter than one week | 0.3% of gross, employer only | 2026 | Decision 77/2015 ch. III para. 5(a) |
| Health insurance, all employees | Employer 1.7%, employee 1.7% (total 3.4%) | 2026 | Decision 77/2015 ch. III paras. 3(b), 4(b), 5(b); [Law 10383/2011 art. 8](https://fsdksh.gov.al/project/ligji-i-fondit/) |
| Employment income tax (TAP), annual base | 13% up to ALL 2,040,000; 23% above | 2026 | [Law 29/2023 art. 24(1)](https://tatime.gov.al/wp-content/uploads/2026/09/Ligj-Nr.-29-2023-Per-Tatimin-mbi-te-Ardhurat-i-ndryshuar.pdf) |
| TAP, monthly base | 13% up to ALL 170,000; 23% above | 2026 | Instruction 26/2023 para. 24.1 |
| Monthly deduction, gross up to ALL 50,000 | ALL 50,000 (1/12 of ALL 600,000) | 2026 | Law 29/2023 arts. 22(1)(a), 65(1) |
| Monthly deduction, gross ALL 50,001 to 60,000 | ALL 35,000 (1/12 of ALL 420,000) | 2026 | Law 29/2023 arts. 22(1)(b), 65(1) |
| Monthly deduction, gross above ALL 60,000 | ALL 30,000 (1/12 of ALL 360,000) | 2026 | Law 29/2023 arts. 22(1)(c), 65(1) |
| Voluntary pension contribution withheld from pay | Deducted from the TAP base, up to the minimum wage a month | 2026 | Law 29/2023 art. 20; Instruction 26 payroll form item 26 |
| Payment to a non-employee individual (no status declaration, not employment) | 15% of the gross | 2026 | Law 29/2023 art. 65(1)(b) |
| Late-payment interest (art. 76) | 7.8% a year from 11.04.2026, confirmed from 08.10.2026 | 2026 | [tatime.gov.al: Normat e interesit](https://tatime.gov.al/institucioni/publikime/normat-e-interesit/) |

The ceiling rose by the same ALL 10,000 as the minimum wage, not by the same percentage (tatime.gov.al notice of 14.01.2026). Law 7703/1993 art. 10 sets the employer social rate for sickness, maternity and pensions at 13.8%; the 15.0% in Decision 77/2015 adds the employer-only work-accident (0.3%) and unemployment (0.9%) branches.

## The taxable base

Each monthly listëpagesa line works from the employee's gross pay for the month, cash and in kind (form item 15). Three bases follow from it.

**Social contribution base** (form item 16). Gross pay, but not less than ALL 50,000 and not more than ALL 186,416 (Decision 77/2015 ch. II para. 3(a); tatime.gov.al notice). The floor applies to part-time staff under 87 hours too (Decision 77/2015 ch. III para. 4(a)). Only absences justified by documents, such as sick leave, reduce it in proportion to days worked (tatime.gov.al payroll Q&A, answer 6). Pay for the first 14 days of sick leave, which the employer pays under the Labour Code, is included (item 16). An employee of a company in a technology park under Law 58/2022 may, with written consent in the contract, pay social and health contributions on the minimum wage whatever the gross (Law 7703/1993 art. 10; Law 10383/2011 art. 7(5)).

**Health contribution base** (form item 24). Gross pay, not less than ALL 50,000, with no ceiling.

**Employment income tax base** (form item 28). Gross pay (item 15), less any voluntary pension contribution withheld (item 26), less the monthly art. 22 deduction (item 27): [(15) − (26) − (27)]. **Employee social and health contributions do not reduce the tax base.** Items 16 to 25 feed the contribution columns only.

**The deduction depends on the personal status declaration.** Only the one employer with whom the employee has signed the declaration (Deklarata mbi statusin personal) gives the monthly art. 22 deduction. An employee may sign with only one employer for a given month: the main employer, where the employee works most or earns most. Every other employer applies 13% and 23% to the full gross with no deduction (Law 29/2023 arts. 65(1), 66; Instruction 26 paras. 65, 66.4). The child (ALL 48,000) and education deductions are claimed only on the annual return, never in payroll (art. 65(2)).

**Monthly tax in practice** (Instruction 26 para. 24.1; `albania-income-tax`):
- Gross up to ALL 50,000: deduction ALL 50,000, so no tax.
- ALL 50,001 to 60,000: 13% of (gross − 35,000).
- ALL 60,001 to 200,000: 13% of (gross − 30,000).
- Above ALL 200,000: ALL 22,100 plus 23% of (gross − 200,000).

**Benefits that are not pay** (art. 12(4); Instruction 26 para. 12.12): meals and work equipment provided in kind to all staff on similar terms; documented travel and per diem reimbursements; hardship payments within the rules; employer-paid life, health and work-accident insurance. Cash paid instead of a benefit in kind is pay. Decision 77/2015 ch. II para. 2 lists items left out of the contribution base, among them court-ordered maintenance, non-permanent bonuses for family misfortune, long illness or natural disasters, and travel costs for work away from home.

**Net pay** = gross − employee social − employee health − TAP − any voluntary pension withheld. **Employer cost** = gross + employer social + employer health.

## Deadlines and filing

| Obligation | When | Source |
|---|---|---|
| Notice of a new or returning employee, form E-SIG 027/a | At least one calendar day before work starts; a newly registered company's administrator within two working days of registration | [ISSH, compulsory insurance](https://www.issh.gov.al/sigurimi-i-detyruar/); [Instruction 23/2014 paras. 4.1, 6.3](https://www.issh.gov.al/wp-content/uploads/2026/08/UDHEZIM-NR.-23-DATE-09.12.2014-PER-MBLEDHJEN-E-KONTRIBUTEVE-TE-DETYRUESHME-TE-SIGURIMEVE-SHOQERORE-DHE-SHENDETESORE-i-perditesuar.pdf); Law 9920/2008 art. 119(1) |
| Personal status declaration signed by the employee | Before the first payment of pay | Law 29/2023 art. 66(1) |
| Monthly listëpagesa (E-SIG 025/a.1) and payment of TAP and all contributions: entities, and self-employed or traders registered for VAT | By the 20th of the following month (20 October 2026 for September 2026) | Law 29/2023 art. 65(1); Instruction 26 para. 65; [tatime.gov.al tax calendar](https://tatime.gov.al/kalendari_tatimor/listepagesa/) |
| Quarterly listëpagesa (E-SIG 025/a.2), split by month: self-employed and traders not registered for VAT | By the 20th of the month after each quarter (20 October 2026 for July to September) | Law 29/2023 art. 65(1); [tatime.gov.al tax calendar](https://tatime.gov.al/kalendari_tatimor/listepagesa/); [tatime.gov.al form models](https://tatime.gov.al/institucioni/publikime/modele-dokumentash-tatimore/) |
| Certificate from the voluntary pension fund for amounts deducted | By 20 January of the following year | Instruction 26 payroll form item 26 |
| Employee's annual return (DVAP), where required | By 31 March 2027 for 2026 | Law 29/2023 arts. 61(2), 67(1); see `albania-income-tax` |

The listëpagesa is filed electronically on e-Filing (Instruction 23/2014 para. 4.2). One listëpagesa is filed for each calendar month, and a separate one for each district where the employer works (E-SIG 025/a.1 filing notes, items 3 and 4). A month with no activity still needs a return, with zeros for the administrator (Instruction 26 payroll form item 8). Contributions are paid at banks with an agreement with the General Directorate of Taxes, or at Albanian Post (ISSH, compulsory insurance page).

**Annual reconciliation.** There is no annual employer return for payroll. The year closes on the employee's side. An employee must file DVAP by 31 March if gross income from all sources is above ALL 1,200,000, or they had more than one employer at any income, or they had more than ALL 50,000 of other income not taxed by final withholding (Law 29/2023 art. 67(1)). On DVAP, payroll tax already paid is credited and any difference is paid or refunded. DVAP is pre-filled from the listëpagesa returns (tatime.gov.al payroll Q&A, answer 4). The employer gives the employee an annual summary of the listëpagesa as evidence of tax withheld (Instruction 26 para. 9.4). Two employers each applying the scale separately often leave tax to pay on DVAP: Instruction 26 para. 65, example 3, shows ALL 17,000 a month more due. See `albania-income-tax`.

## Penalties and interest

All under Law No. 9920/2008 "On tax procedures", consolidated to Law No. 79/2025 ([tatime.gov.al copy](https://tatime.gov.al/wp-content/uploads/2026/10/Ligj-Nr-9920-Dt-2008.05.19-perditesuar-1.pdf)).

| Failure | Penalty | Source |
|---|---|---|
| Listëpagesa filed late | ALL 10,000 per return for corporate income taxpayers; ALL 5,000 for other taxpayers except individuals; ALL 3,000 for individuals | Law 9920/2008 art. 113 |
| Tax or contributions paid late | 0.06% of the unpaid amount per day, for at most 365 days | Law 9920/2008 art. 114(1) |
| Incorrect return | 0.06% of the unpaid amount per day, for at most 365 days | Law 9920/2008 art. 115(1) |
| TAP withheld and declared but not paid over | 0.06% per day, for at most 365 days | Law 9920/2008 art. 117(a) |
| TAP not withheld | 50% of the tax | Law 9920/2008 art. 117(b) |
| TAP withheld but not declared and paid | 100% of the tax | Law 9920/2008 art. 117(c) |
| Employee not notified at least one day before starting work, found at an on-site check | ALL 200,000 per employee if registered for VAT and corporate income tax; ALL 50,000 per employee for other taxpayers; plus the tax and contributions | Law 9920/2008 art. 119(1) |
| Real pay concealed (under-declared salary) | 200% of the tax and contributions for legal entities; 100% for other taxpayers; plus the amounts due for the whole period | Law 9920/2008 art. 119(3) |
| Tax evasion (false returns or documents) | 100% of the understated amount | Law 9920/2008 art. 116(1) |
| Failure to keep books and records | ALL 10,000 per breach for natural persons in business; ALL 50,000 for legal persons | Law 9920/2008 art. 118 |

**There is no flat 10% late-payment penalty.** The art. 114 penalty is 0.06% a day, capped at 365 days, so at most 21.9%. Fines linked to a tax liability cannot exceed 100% of that liability (art. 111(5)).

**Late-payment interest** (kamatëvonesë) runs on top, from the due date to the payment date, at 120% of the Bank of Albania interbank rate, reset each quarter (art. 76(1), (3)). The rate published by the General Directorate is 7.8% a year from 11.04.2026, confirmed from 08.10.2026. It cannot be waived or appealed, except for a calculation error or a change in the underlying tax (art. 76(4)).

**Employee contributions come first.** An employer that cannot pay everything must still pay in full, on time, the contributions it withheld from employees' pay (ISSH, compulsory insurance page).

## Cross-border points

- **Foreign employees** working in Albania pay contributions on the same terms as Albanians (Law 7703/1993 art. 7; [ISSH, social insurance for foreigners](https://www.issh.gov.al/sigurimet-shoqerore-per-te-huajt-ne-shqiperi/)).
- **Bilateral social security agreements.** ISSH lists agreements applied with Turkey, Belgium, North Macedonia, Hungary, Luxembourg, the Czech Republic, Germany, Austria, Canada, Kosovo, Switzerland, Croatia, Bulgaria, Romania, Montenegro and Italy. Each agreement sets which country's law applies, evidenced by a certificate of coverage ([ISSH, bilateral agreements](https://www.issh.gov.al/shtetet-me-te-cilat-shqiperia-ka-marreveshje/)). Without an agreement and a certificate, Albanian contributions apply from day one.
- **Pay for work done in Albania is Albanian-source income** for a non-resident, and so is pay owed by a resident employer even for work done abroad (Law 29/2023 art. 4). An Albanian employer posting staff abroad keeps withholding TAP. If a treaty gives the right to tax only to the other state, the employer shows the pay on the listëpagesa but computes no TAP (Instruction 26 para. 4.9). See `al-cross-border` for treaty conditions and documents.
- **Foreign employer with no Albanian payroll agent.** A resident employee paid by a non-resident employer for work in Albania declares that income and computes and pays the tax himself, subject to any treaty (Instruction 26 para. 4.8).

## Worked examples

### Example 1: full-time employee, ALL 150,000 a month

Elira works full time for a Tirana company registered for VAT. Her gross pay is ALL 150,000 a month. She has signed the personal status declaration with this employer and has no voluntary pension.

Her pay is between the floor and the ceiling, so the social base is ALL 150,000. The health base is also ALL 150,000. Her gross is above ALL 60,000, so the monthly deduction is ALL 30,000 and the TAP base is ALL 120,000. Employee contributions are not deducted from it. TAP is 13% of ALL 120,000 = ALL 15,600.

Employee: social 9.5% = ALL 14,250; health 1.7% = ALL 2,550. Net pay ALL 117,600. Employer: social 15% = ALL 22,500; health 1.7% = ALL 2,550. Employer cost ALL 175,050. The company pays ALL 57,450 by 20 November 2026 for October.

```oa-check
name: Elira, ALL 150,000 gross a month, one employer with status declaration (2026)
inputs:
  gross: 150000
  social_floor: 50000
  social_ceiling: 186416
  monthly_deduction: 30000
steps:
  - social_base: clamp(gross, social_floor, social_ceiling)
  - health_base: max(gross, social_floor)
  - employee_social: social_base * 0.095
  - employee_health: health_base * 0.017
  - tap_base: gross - monthly_deduction
  - tap: min(tap_base, 170000) * 0.13 + max(tap_base - 170000, 0) * 0.23
  - net_pay: gross - employee_social - employee_health - tap
  - employer_social: social_base * 0.15
  - employer_health: health_base * 0.017
  - employer_cost: gross + employer_social + employer_health
  - total_to_pay: tap + employee_social + employee_health + employer_social + employer_health
expected:
  employee_social: 14250
  employee_health: 2550
  tap: 15600
  net_pay: 117600
  employer_cost: 175050
  total_to_pay: 57450
```

### Example 2: senior employee above the social ceiling

Dritan earns ALL 300,000 a month from one employer and has signed the status declaration there.

His social contributions stop at the ALL 186,416 ceiling. Health has no ceiling, so it runs on ALL 300,000. The TAP base is ALL 300,000 less ALL 30,000 = ALL 270,000: the first ALL 170,000 at 13% (ALL 22,100) and ALL 100,000 at 23% (ALL 23,000), so TAP is ALL 45,100.

Employee: social 9.5% × 186,416 = ALL 17,709.52; health ALL 5,100. Net pay ALL 232,090.48. Employer: social 15% × 186,416 = ALL 27,962.40; health ALL 5,100. Employer cost ALL 333,062.40. Using the full gross for social would overstate employee social by ALL 10,790.48 a month.

If Dritan had a second job, that employer would give no deduction and would apply the scale to its full gross. His total social contributions across both jobs are capped at the amount on the ceiling (Decision 77/2015 ch. III para. 15), and he must file DVAP.

```oa-check
name: Dritan, ALL 300,000 gross a month, above the social ceiling (2026)
inputs:
  gross: 300000
  social_floor: 50000
  social_ceiling: 186416
  monthly_deduction: 30000
steps:
  - social_base: clamp(gross, social_floor, social_ceiling)
  - health_base: max(gross, social_floor)
  - employee_social: social_base * 0.095
  - employee_health: health_base * 0.017
  - tap_base: gross - monthly_deduction
  - tap: min(tap_base, 170000) * 0.13 + max(tap_base - 170000, 0) * 0.23
  - net_pay: gross - employee_social - employee_health - tap
  - employer_social: social_base * 0.15
  - employer_health: health_base * 0.017
  - employer_cost: gross + employer_social + employer_health
  - overstatement_if_uncapped: gross * 0.095 - employee_social
expected:
  employee_social: 17709.52
  employee_health: 5100
  tap: 45100
  net_pay: 232090.48
  employer_social: 27962.40
  employer_cost: 333062.40
  overstatement_if_uncapped: 10790.48
```

## Ask the client first

1. **Has the employee signed the personal status declaration with you, or with another employer?** Only one employer gives the monthly deduction.
2. **Hours a month under the contract.** Under 87 hours changes the social rates to 13.9% and 9.4%; a contract under one week is 0.3% employer only.
3. **Gross pay for the month, including benefits in kind and bonuses.** This sets all three bases and the ceiling test.
4. **Is the employer registered for VAT, and is it an entity or an individual?** This decides monthly or quarterly filing and the size of the late-filing and undeclared-worker fines.
5. **Is the employee foreign, posted from abroad, or working outside Albania?** A coverage certificate under a bilateral agreement, or a treaty, can change who collects.
6. **Any voluntary pension deducted from pay, or a technology-park employer under Law 58/2022?** Both change the bases.

## Sources

| Source | URL | Read on |
|---|---|---|
| Law No. 29/2023 "Për tatimin mbi të ardhurat", consolidated (General Directorate of Taxes copy), arts. 4, 12, 20, 22 to 24, 61, 65 to 67 | https://tatime.gov.al/wp-content/uploads/2026/09/Ligj-Nr.-29-2023-Per-Tatimin-mbi-te-Ardhurat-i-ndryshuar.pdf | 2026-10-23 |
| General Instruction No. 26 of 8.9.2023, consolidated to Instruction No. 9 of 12.3.2026, paras. 4.8, 4.9, 9.4, 24.1, 65, 66 and Annex 2 (listëpagesa filing notes, items 8 to 33) | https://tatime.gov.al/wp-content/uploads/2026/09/Udhezimi-nr-26-date-8.9.2023-Per-tatimin-mbi-te-ardhuart.pdf | 2026-10-23 |
| Law No. 9920/2008 "Për procedurat tatimore", consolidated to Law No. 79/2025, arts. 76, 111, 113 to 119 | https://tatime.gov.al/wp-content/uploads/2026/10/Ligj-Nr-9920-Dt-2008.05.19-perditesuar-1.pdf | 2026-10-23 |
| General Directorate of Taxes, "Nga 1 janari 2026, rritet paga minimale dhe maksimale" (14.01.2026) | https://tatime.gov.al/nga-1-janari-2026-rritet-paga-minimale-dhe-maksimale/ | 2026-10-23 |
| General Directorate of Taxes, tax calendar: listëpagesa | https://tatime.gov.al/kalendari_tatimor/listepagesa/ | 2026-10-23 |
| General Directorate of Taxes, form models (E-SIG 025/a.1, 025/a.2, 027/a and filing notes) | https://tatime.gov.al/institucioni/publikime/modele-dokumentash-tatimore/ | 2026-10-23 |
| General Directorate of Taxes, payroll Q&A | https://tatime.gov.al/pyetje-pergjigje-per-listepagesat/ | 2026-10-23 |
| General Directorate of Taxes, interest rates for late-payment interest | https://tatime.gov.al/institucioni/publikime/normat-e-interesit/ | 2026-10-23 |
| Council of Ministers Decision No. 776 of 19.12.2025 on the national minimum wage (ISSH copy) | https://www.issh.gov.al/wp-content/uploads/2026/08/VKM-NR.-776-DATE-19.12.2025-PER-PERCAKTIMIN-E-PAGES-MINIMALE-NE-SHKALLE-VENDI.pdf | 2026-10-23 |
| Council of Ministers Decision No. 77 of 28.1.2015 on compulsory contributions, consolidated to Decision No. 702 of 13.11.2024 (ISSH copy), chs. II and III | https://www.issh.gov.al/wp-content/uploads/2026/08/VENDIM-NR.-77-DATE-28.1.2015-PER-KONTRIBUTET-E-DETYRUESHME-DHE-PERFITIMET-NGA-SISTEMI-I-SIGURIMEVE-SHOQERORE-DHE-SIGURIMI-I-KUJDESIT-SHENDETESOR.pdf | 2026-10-23 |
| Law No. 7703/1993 "Për sigurimet shoqërore", consolidated (ISSH copy), arts. 7, 9, 10, 13 | https://www.issh.gov.al/wp-content/uploads/2026/08/LIGJ-NR.-7703-DATE-11.5.1993-PER-SIGURIMET-SHOQERORE-NE-REPUBLIKEN-E-SHQIPERISE-I-NDRYSHUAR-1-1.pdf | 2026-10-23 |
| Instruction No. 23 of 9.12.2014 on collection of compulsory contributions, consolidated to Instruction No. 16 of 8.7.2026 (ISSH copy), paras. 4 and 6 | https://www.issh.gov.al/wp-content/uploads/2026/08/UDHEZIM-NR.-23-DATE-09.12.2014-PER-MBLEDHJEN-E-KONTRIBUTEVE-TE-DETYRUESHME-TE-SIGURIMEVE-SHOQERORE-DHE-SHENDETESORE-i-perditesuar.pdf | 2026-10-23 |
| Law No. 10383/2011 on compulsory health insurance, consolidated (FSDKSH), arts. 6 to 8 | https://fsdksh.gov.al/project/ligji-i-fondit/ | 2026-10-23 |
| Social Insurance Institute, compulsory insurance | https://www.issh.gov.al/sigurimi-i-detyruar/ | 2026-10-23 |
| Social Insurance Institute, social insurance for foreigners | https://www.issh.gov.al/sigurimet-shoqerore-per-te-huajt-ne-shqiperi/ | 2026-10-23 |
| Social Insurance Institute, bilateral agreements in force | https://www.issh.gov.al/shtetet-me-te-cilat-shqiperia-ka-marreveshje/ | 2026-10-23 |

Not yet confirmed: when and on which form a resident employee of a foreign employer with no Albanian payroll agent pays the tax during the year (Instruction 26 para. 4.8 gives the duty, not the timing); how the listëpagesa rounds contribution and tax amounts (the examples here are unrounded); how the ALL 186,416 social cap is split between two employers in practice (Instruction 23 and listëpagesa categories 8 to 10 set the rules, not worked through today); whether art. 117 (withholding agents) or only art. 114 applies to employee contributions withheld but not paid; the ISSH page still says ALL 10,000 for every late listëpagesa and Instruction 23 para. 6.2 still says ALL 500,000 or 250,000 for an undeclared worker, while the consolidated Law 9920/2008 arts. 113 and 119 give the amounts in the table (this skill follows the law); whether the E-SIG 025/a form codes on tatime.gov.al match the current e-Filing screens; the E-SIG 027/a filing notes on tatime.gov.al still say the form goes in at least 48 hours before work starts, while Instruction 23/2014 para. 4.1 (consolidated to 2026) and Law 9920/2008 art. 119(1) say at least one calendar day (this skill follows the law).
