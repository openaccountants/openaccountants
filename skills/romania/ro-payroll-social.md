---
name: ro-payroll-social
description: "Use this skill to run Romanian payroll for tax year 2026: registering employees in REGES ONLINE (the successor to REVISAL) the day before they start, the monthly gross-to-net (employee pension contribution CAS 25%, health contribution CASS 10%, income tax 10% after the personal deduction), the minimum gross wage (RON 4,050 to 30 June 2026, RON 4,325 from 1 July 2026), the tax-free RON 300 then RON 200 a month for full-time minimum-wage staff under OUG 89/2025, the employer work insurance contribution (CAM 2.25%), meal vouchers and other non-taxable benefits, the minimum CAS and CASS on part-time contracts, D112 filing and payment by the 25th, quarterly filers, annual duties and penalties. Trigger phrases: salarizare, stat de plata, D112, CAM, salariul minim 2026, tichete de masa, REGES, Romanian payroll, employer cost Romania. Out of scope: self-employed CAS and CASS (ro-cas-cass), the employee's own income tax questions and other income (ro-employee-income-tax, ro-income-tax), residence and posted workers (ro-cross-border)."
version: 0.2
jurisdiction: RO
tax_year: 2026
last_updated: 2026-10-31
review_status: pending_review
trust_label: Built by Michael Cutajar and the OpenAccountants team
category: international
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Romania payroll: gross-to-net, employer CAM and D112 (2026)

Written by the OpenAccountants team. Not yet reviewed by an accountant.

This skill covers what an employer in Romania withholds and pays on salaries each month, what it costs on top of gross pay, and how it is reported. It links to the other Romania skills and does not repeat them: `ro-employee-income-tax` (the employee's own tax position and the personal deduction in depth), `ro-income-tax` (self-employed and other income), `ro-cas-cass` (self-employed contributions) and `ro-cross-border` (residence, non-residents, foreign employers and posted workers).

The law is Legea 227/2015 (Codul fiscal, "the Fiscal Code"), Title IV chapter III (salary income tax), Title V (social contributions) and Title V chapter IX (CAM). Penalties are in Legea 207/2015 (Codul de procedură fiscală, "the Procedure Code"). Both were read on 23 October 2026 in ANAF's consolidated texts, last updated by Legea 170/2026. The 2026 minimum-wage measures are in OUG 89/2025 and HG 146/2026, read in the copies ANAF hosts.

## Who this applies to

- **Employers** (Romanian companies, PFAs and other individuals who hire, branches, and non-residents with a Romanian tax code) that pay salary income. They calculate, withhold, declare and pay income tax, CAS and CASS, and pay CAM themselves (Fiscal Code art. 78(1), 146(1), 168(1), 220^1(a)).
- **Salary income** is everything in cash or in kind received under an employment contract, a service relationship, a secondment or a special legal status, whatever it is called (art. 76(1)). Income "assimilated to salaries" is taxed the same way and includes directors' and administrators' fees, mandate contracts, board fees and profit shares paid to administrators (art. 76(2)).
- **Registration of employees.** Every employer keeps the general register of employees, REGES ONLINE (HG 295/2025), at reges.inspectiamuncii.ro. It replaced the desktop ReviSal application on 1 April 2025. A new employment contract goes into the register at the latest the day before the employee starts work. This also applies to an employer hiring its first employee and to a non-resident employer with a Romanian tax code (Inspecția Muncii, REGES ONLINE questions 42 and 44).
- **Out of this skill:** an employee paid by a foreign employer with no Romanian payroll declares and pays the tax himself under art. 82, and posted workers may stay in their home social security system. Both are in `ro-cross-border`.
- **Exempt from income tax** (contributions still apply): employees with a severe or accentuated disability, on their salary (art. 60 point 1(b)); and staff working on qualifying research and development projects, within the project's staff budget (art. 60 point 3). The former exemptions for IT, construction and agri-food staff are repealed (art. 60 points 2, 4 and 5; art. 138^1 to 138^3 are repealed).

## Rates, bands and thresholds

| Item | Rate or amount | Year | Source |
|---|---|---|---|
| CAS, employee pension contribution, withheld | 25% | 2026 | Fiscal Code art. 138(a), [ANAF consolidated Fiscal Code](https://static.anaf.ro/static/10/Anaf/legislatie/Cod_fiscal_norme_2023.htm) |
| Extra employer CAS, special working conditions / particularly hard conditions (Legea 263/2010) | 4% / 8% | 2026 | art. 138(b) and (c), same page |
| CASS, employee health contribution, withheld | 10% | 2026 | art. 156, same page |
| Income tax on salary, final, withheld monthly | 10% | 2026 | art. 78(1) and (2), same page |
| CAM, employer work insurance contribution | 2.25% | 2026 | art. 220^3(1), same page |
| Upper limit on the employee CAS or CASS base | none for employees | 2026 | art. 139 and 157 set no cap, same page |
| National minimum gross wage, 1 January to 30 June 2026 | RON 4,050 a month for 165.334 hours (RON 24.496 an hour); HG 1506/2024 stays in force until HG 146/2026 repeals it on 1 July 2026 | 2026 | [HG 1506/2024, ANAF copy](https://static.anaf.ro/static/10/Anaf/legislatie/HG_1506_2024.pdf); [OUG 89/2025 preamble, ANAF copy](https://static.anaf.ro/static/10/Anaf/legislatie/OUG_89_2025.pdf) |
| National minimum gross wage from 1 July 2026 | RON 4,325 a month for 166.667 hours (RON 25.949 an hour) | 2026 | HG 146/2026 art. 1, [ANAF copy](https://static.anaf.ro/static/10/Anaf/legislatie/HG_146_2026.pdf) |
| Tax-free and contribution-free amount, full-time staff whose base salary equals the minimum wage | RON 300 a month for January to June 2026; RON 200 a month for July to December 2026 | 2026 | OUG 89/2025 art. III(1) and (6), ANAF copy above |
| Gross pay ceiling for that amount (excluding meal vouchers, holiday vouchers and food allowance) | RON 4,300 (January to June); RON 4,600 (July to December) | 2026 | OUG 89/2025 art. III(1)(b) |
| Basic personal deduction, gross pay up to the minimum wage | 20% of the minimum wage with no dependants; 25%, 30%, 35%, 45% with 1, 2, 3, 4 or more | 2026 | art. 77(4) table |
| Basic personal deduction, gross pay above the minimum wage | falls 0.5 points of the minimum wage for each RON 50 band above it; none above minimum wage + RON 2,000 | 2026 | art. 77(3) and (4) |
| Extra deduction, employee under 26 with gross pay up to minimum wage + RON 2,000 | 15% of the minimum wage | 2026 | art. 77(10)(a) |
| Extra deduction, per child under 18 enrolled in school (one parent, any salary) | RON 100 a month | 2026 | art. 77(10)(b) and (12) |
| Gifts at Easter, Christmas, 1 June, 8 March | not taxed and not in the CAS or CASS base up to RON 300 per person per occasion | 2026 | art. 76(4)(a), art. 142(b) |
| Maximum face value of one meal voucher | RON 45, for entitlements from November 2025 to September 2026 | 2026 | Legea 165/2018 art. 14 as amended by Legea 201/2025 art. I point 1, applied to January to September 2026 by art. II(2), [text sent for promulgation, Chamber of Deputies](https://www.cdep.ro/ords/pls/proiecte/docs?2023/pl342_pr342_23.pdf) |
| Benefits within the 33% of base salary monthly ceiling (meals up to one meal voucher a day, housing up to 20% of minimum wage, holiday services, pension and health premiums up to EUR 400 a year each, sport up to EUR 100 a year, nursery up to RON 1,500 a month per child) | not taxable within the limits | 2026 | art. 76(4^1) and (4^2), art. 142(aa^1) |
| Minimum CAS and CASS on any employment contract, including part-time | as if paid the minimum wage, pro rata to working days the contract was active; for 2026 the minimum wage used here is reduced by RON 300 (January to June) and RON 200 (July to December) | 2026 | art. 146(5^6) and 168(6^1); OUG 89/2025 art. III(5) |
| Rounding on D112 | every amount is a whole leu; contributions round half up (a fraction of 50 bani or more goes up), and a contribution under RON 1 becomes RON 1 | 2026 | ANAF, D112 technical structure for July 2026 onwards, [structura_D112_0726_070926.pdf](https://static.anaf.ro/static/10/Anaf/Declaratii_R/AplicatiiDec/structura_D112_0726_070926.pdf), section "Rotunjirile" |
| Payment and filing deadline | 25th of the following month (quarterly payers: 25th of the month after the quarter) | 2026 | art. 80, 146(3), 147(1) and (4), 168(3), 220^6(1) |

The CAM receipts are split by law (15% wage guarantee fund, 20% unemployment, 5% work accidents, 40% sick pay, 20% state budget), but the employer pays one amount (art. 220^6(4)).

## The taxable base

**Step 1: gross pay.** Gross monthly salary income is everything received in the month under art. 76(1) to (3), in cash or in kind (norm 14(1) to art. 78). Benefits in kind count unless listed as non-taxable (art. 76(3) and (4)). Personal use of a company car counts, except where the car's costs are only 50% deductible (art. 76(4)(ț)).

**Step 2: the CAS base.** Gross pay (art. 139(1)), less the items in art. 141 and 142 (art. 146(5)). The main exclusions:
- meal vouchers, holiday vouchers, nursery vouchers and cultural vouchers granted under the law (art. 142(r));
- gifts within RON 300 per occasion, funeral, illness, birth and disaster aid, and employer-paid commuting (art. 142(b));
- protective equipment, training linked to the job, business phone costs (art. 142(e), (n), (o));
- delegation and secondment allowances within 2.5 times the public-sector allowance, capped at 3 base salaries a month (art. 142(g), art. 76(2)(k));
- the 33% ceiling benefits listed in the table, within their limits (art. 142(aa^1)).

**Step 3: the CASS base.** The same as the CAS base, except that **meal vouchers and holiday vouchers are included** at face value (art. 157(1)(ț) and (2)).

**Step 4: the CAM base.** Gross pay less the art. 142 items (art. 220^4(2)). Meal vouchers and holiday vouchers are therefore outside CAM.

**Step 5: the minimum-wage relief (2026 only).** It applies to a full-time employee at the main job whose contractual base salary, without bonuses, equals the minimum wage, and whose gross pay excluding meal vouchers, holiday vouchers and food allowance is no more than RON 4,300 (January to June) or RON 4,600 (July to December). For that employee, RON 300 a month (January to June) or RON 200 a month (July to December) is free of income tax, CAS, CASS and CAM (OUG 89/2025 art. III(1), which overrides art. 78, 139, 140, 157 and 220^4). The amount is reduced for part months, for new joiners and leavers, and for months when the base salary was at the minimum for only part of the month (art. III(4)). If the base salary is cut at any time up to 31 December 2026, the relief is lost (art. III(2)).

**Step 6: the minimum CAS and CASS rule.** For every employment contract, full-time or part-time, the CAS and the CASS cannot be less than 25% and 10% of the minimum wage, pro rata to the working days the contract was active in the month (art. 146(5^6), applied to CASS by art. 168(6^1)). For 2026 the minimum wage used in this test is reduced by RON 300 (January to June) or RON 200 (July to December) (OUG 89/2025 art. III(5)). So the floor is a base of RON 3,750 a month to June and RON 4,125 from July. The employer pays the shortfall in the employee's name (art. 146(5^9)). The floor does not apply to (art. 146(5^7)):
- pupils and students under 26 in education;
- apprentices under 18;
- people with disabilities or others allowed by law to work under 8 hours a day;
- old-age pensioners (with exceptions for service pensions);
- employees whose combined contracts in the month reach at least the minimum wage.

Example: a half-time employee on RON 2,100 gross for the whole of March 2026, in none of these groups, owes CAS of RON 525 on actual pay. The floor is 25% of RON 3,750, which is RON 937.50, declared as RON 938 on D112, so the employer pays the RON 413 difference. On CASS the floor is RON 375 against RON 210, so the employer adds RON 165.

**Step 7: the income tax base** at the employee's main job ("funcția de bază") is (art. 78(2)(a)):
- gross pay, including meal vouchers;
- less the RON 300 or 200 relief where it applies;
- less the employee's CAS and CASS for the month;
- less the personal deduction (art. 77);
- less union dues paid; the employee's own voluntary pension contributions, private health premiums and ETF purchases, each within EUR 400 a year; and sport subscriptions within EUR 100 a year.

The base is rounded to the leu: fractions up to 50 bani are dropped, fractions above 50 bani round up (norm 4 to art. 64). Tax is 10% of the base. CAS, CASS, CAM and the tax are declared on D112 in whole lei, rounded half up (ANAF D112 technical structure). At a second job no personal deduction is given: tax is 10% of gross less contributions (art. 78(2)(b)).

**The personal deduction** (art. 77) is given only at the main job and only to residents and newcomers taxed as residents (art. 77(1)). The basic deduction applies where gross monthly pay is no more than the minimum wage plus RON 2,000, using the lowest minimum wage in force in the month (art. 77(3)). That is RON 6,050 to June 2026 and RON 6,325 from July. The rate falls in RON 50 bands (art. 77(4) table). Fixed sums are rounded to the leu with the same rule as the base (art. 66). Dependants are a spouse or relatives up to the second degree with income up to 20% of the minimum wage; minor children always count, and each parent can claim them (art. 77(5) to (7)). The deduction is not cut for part-time work (norm 13(14) to art. 77). `ro-employee-income-tax` covers the deduction in more depth.

**Directors and mandate contracts.** Administrators' fees, mandate contract pay and board fees are in the CAS, CASS and CAM bases (art. 139(1)(d) to (f), 157(1)(e) to (g), 220^4(1)(d) and (e)).

## Deadlines and filing

| Event | What | When | Source |
|---|---|---|---|
| Before the first day of work | register the contract in REGES ONLINE | at the latest the day before work starts | HG 295/2025; [Inspecția Muncii REGES ONLINE Q&A](https://www.inspectiamuncii.ro/documents/66402/85254633/%C3%8Entreb%C4%83ri+%C8%99i+r%C4%83spunsuri+REGES+ONLINE.pdf/690a056b-bcec-49ff-85e5-8d264e7301bc), questions 42 and 44 |
| Suspension of a contract | record it in REGES ONLINE | the day before; medical leave and unjustified absence within 3 working days of the certificate or event | HG 295/2025 art. 5(1)(e), quoted in the Q&A, question 40 |
| Each payday | calculate and withhold income tax, CAS and CASS | on payment | art. 80(1), 146(1), 168(1) |
| Monthly payers | file D112 (Declarația privind obligațiile de plată a contribuțiilor sociale, impozitului pe venit și evidența nominală a persoanelor asigurate), one entry per employee, and pay income tax, CAS, CASS and CAM | by the 25th of the month after the month the salary relates to | art. 80(1), 81(1), 146(3), 147(1), 168(3), 220^6(1), 220^7(1) |
| Quarterly payers | file one D112 per month of the quarter and pay | by the 25th of the month after the quarter | art. 80(2), 147(4) and (5) |
| Who may file quarterly | non-profits; profit-tax companies with total revenue up to EUR 100,000 and an average of under 3 employees last year; micro-enterprises with an average of under 3 employees; PFAs, individual enterprises and liberal professions with staff | from last year's figures | art. 80(2) and (3), 147(6) and (7) |
| Opting out of quarterly filing | file the option on paper | by 31 January | art. 147(8) and (16) |
| Quarterly filer whose employee goes on sick leave or leaves | file D112 for that month early | by the 25th of the following month | art. 147(11) |
| How D112 is filed | electronically, on the e-România portal | n/a | art. 147(16) |
| Back pay and court awards | CAS: spread over the months they relate to, at that period's rates, with amended D112 for those months. Income tax: calculated and withheld on the payment date under the rules for income outside the main job, so no personal deduction | by the 25th of the month after payment | art. 146(9) and (9^1), 147(3) and (3^1); art. 78(3) and (4) |
| Year end | the employer computes each employee's annual salary tax; gives the employee a statement of income, deductions and tax on request | after year end; on request | art. 78(5), 81(2) |
| Employee's 3.5% of tax to a charity | the employee files a request with ANAF, or agrees with the employer that it pays the amount monthly | request by 25 May of the next year | art. 123^1(3) and (6), 122(3) |

## Penalties and interest

All from the Procedure Code ([ANAF consolidated text](https://static.anaf.ro/static/10/Anaf/cod_procedura/Cod_Procedura_Fiscala_2023.htm)):

- **Late payment interest:** 0.02% a day from the day after the due date to the day of payment (art. 174(1) and (5)).
- **Late payment penalty:** 0.01% a day on top of interest (art. 176(2) and (3)). It does not apply where the non-declaration penalty applies (art. 176(4)).
- **Non-declaration penalty:** 0.08% a day on tax that was not declared or was declared wrongly and is then assessed by ANAF (art. 181(1)). It falls by 75% if the assessed amount is paid by the due date in the assessment or put into an instalment plan (art. 181(2)). It doubles where the amount comes from tax evasion found by the judicial authorities (art. 181(3)). It is not charged below RON 50 and cannot exceed the tax (art. 181(6) and (11)).
- **Late D112 filing:** a fine of RON 1,000 to 5,000 for medium and large taxpayers, and RON 500 to 1,000 for other companies and individuals (art. 336(1)(b) and (2)(d)).
- **Not withholding tax or contributions, or withholding and not paying over** (art. 336(1)(o) and (p), (2)(f) to (h)):
  - up to RON 50,000: RON 4,000 to 6,000 for medium and large taxpayers; RON 1,000 to 1,500 for others;
  - RON 50,000 to 100,000: RON 12,000 to 14,000; RON 4,000 to 6,000;
  - over RON 100,000: RON 25,000 to 27,000; RON 6,000 to 8,000.
- **Unregistered work.** Putting a person to work without an employment contract (Labour Code art. 16(1)) is fined RON 40,000 for each person, with a cap of RON 1,000,000 per employer, from 18 December 2025 (Labour Code art. 260(1)(e) as amended by Legea 239/2025, as stated by the Labour Inspectorate, [ITM Botoșani notice 69 of 8 January 2026](https://www.inspectiamuncii.ro/documents/521316/523496/20260112_COMUNICAT+MUNCA+NEDECLARATA+01.2026.pdf/35df8a29-b7a3-4a33-854b-b6042fb55ba3)).
- **Late or missing REGES entries** carry their own fines under HG 295/2025. We did not read that text, so those fines are not given here.

## Cross-border points

- **Foreign employer, no Romanian payroll.** An employee working in Romania and paid from abroad declares and pays the income tax monthly by the 25th (art. 82(2)). Where the foreign employer has no seat or permanent establishment in Romania but Romanian social security applies under EU rules, the employee pays CAS, CASS and CAM only if there is an agreement with the employer; otherwise the employer must do it (art. 146(4), 147(13) to (15), 168(4), 220^6(2)). Details in `ro-cross-border`.
- **Employers outside the EU coordination rules.** An employee living in Romania paid by an employer from a state outside the EU rules and social security agreements calculates and pays CAS, CASS and CAM himself and files D112 (art. 146(2) and (8), 147(1), 168(2) and (8), 220^1(b), 220^6(1)).
- **Non-resident employees.** Salary for work done in Romania is Romanian income even if paid from abroad (art. 223(2)(d)). A non-resident gets no personal deduction unless taxed as a resident or a newcomer under art. 59 (art. 77(1)); EU and EEA residents can claim the same deductions as residents (art. 128). See `ro-cross-border`.
- **Posted workers and A1.** An employee posted to Romania with an A1 certificate stays in the home social security system, so no Romanian CAS, CASS or CAM (Regulation 883/2004 art. 12, applied by Fiscal Code art. 135^2). Income tax follows the treaty.
- **Work abroad for a Romanian employer.** Salary for work done abroad is not taxable in Romania whatever the foreign tax treatment, unless paid by or on behalf of a Romanian-resident employer or permanent establishment and Romania has the taxing right (art. 76(4)(o)).
- **Delegation allowances abroad** are tax-free up to 2.5 times the public-sector daily allowance, capped at 3 base salaries a month (art. 76(2)(k)(ii)).

## Worked examples

### Example 1: an employee with one child, March 2026

Maria earns a gross salary of RON 4,600 in March 2026. She is 34, has one child aged 10 enrolled in school, and claims the child as her dependant and for the school deduction. Her base salary is above the minimum wage, so the RON 300 relief does not apply. She gets no meal vouchers.

1. **CAS** 25% of RON 4,600 = RON 1,150. **CASS** 10% = RON 460.
2. **Personal deduction.** Gross pay is RON 550 above the RON 4,050 minimum wage, which is the band "minimum wage + 501 to 550 lei". With one dependant the rate is 19.5% (art. 77(4)). 19.5% of RON 4,050 = RON 789.75, rounded to RON 790 (art. 66). The child in school adds RON 100 (art. 77(10)(b)). Total deduction RON 890.
3. **Taxable base** RON 4,600 - 1,150 - 460 - 890 = RON 2,100. **Income tax** 10% = RON 210.
4. **Net pay** RON 4,600 - 1,150 - 460 - 210 = RON 2,780.
5. **CAM** 2.25% of RON 4,600 = RON 103.50, declared as RON 104 (half up). **Total employer cost** RON 4,704.
6. The employer files D112 for March and pays RON 1,150 + 460 + 210 + 104 = RON 1,924 by 25 April 2026 (monthly payer).

```oa-check
name: RO payroll, gross RON 4,600, one child in school, March 2026
inputs:
  gross: 4600
  min_wage: 4050
  deduction_rate_pct: 19.5
  child_school: 100
steps:
  - cas: gross * 0.25
  - cass: gross * 0.10
  - basic_deduction: round(min_wage * deduction_rate_pct / 100)
  - deduction: basic_deduction + child_school
  - base: gross - cas - cass - deduction
  - income_tax: base * 0.10
  - net: gross - cas - cass - income_tax
  - cam: round(gross * 0.0225)
  - employer_cost: gross + cam
  - paid_to_budget: cas + cass + income_tax + cam
expected:
  cas: 1150.00
  cass: 460.00
  basic_deduction: 790.00
  deduction: 890.00
  base: 2100.00
  income_tax: 210.00
  net: 2780.00
  cam: 104.00
  employer_cost: 4704.00
  paid_to_budget: 1924.00
```

### Example 2: a minimum-wage employee with meal vouchers, July 2026

Ion works full-time on the minimum wage of RON 4,325 from 1 July 2026 (HG 146/2026). In July he also gets 20 meal vouchers of RON 30 each, RON 600 in total (within the RON 45 cap). He is 40, has no dependants and no children in school. His gross pay excluding meal vouchers is RON 4,325, below the RON 4,600 ceiling, so RON 200 is free of tax and contributions (OUG 89/2025 art. III).

1. **CAS base** RON 4,325 - 200 = RON 4,125 (meal vouchers are outside CAS, art. 142(r)). **CAS** 25% = RON 1,031.25, declared as RON 1,031.
2. **CASS base** RON 4,125 + 600 meal vouchers = RON 4,725 (art. 157(1)(ț)). **CASS** 10% = RON 472.50, declared as RON 473 (half up).
3. **Personal deduction.** Gross monthly pay for art. 77(3) is all salary income of the month (norm 14(1)), so RON 4,325 + 600 = RON 4,925. That is RON 600 above the minimum wage: band "minimum wage + 551 to 600 lei", 14% with no dependants. 14% of RON 4,325 = RON 605.50, rounded to RON 605 (art. 66: fractions up to 50 bani are dropped). The RON 200 counts in gross pay for this test; see the note below.
4. **Taxable base** RON 4,925 - 200 - 1,031 - 473 - 605 = RON 2,616. **Income tax** 10% = RON 261.60, declared as RON 262.
5. **Cash net pay** RON 4,325 - 1,031 - 473 - 262 = RON 2,559, plus the RON 600 of meal vouchers. The tax and CASS on the vouchers come out of cash pay.
6. **CAM base** RON 4,325 - 200 = RON 4,125 (vouchers are outside CAM, art. 220^4(2)). **CAM** 2.25% = RON 92.81, declared as RON 93.
7. **Employer cost** RON 4,325 + 600 + 93 = RON 5,018. The profit-tax treatment of the vouchers is outside this skill.

Note on the band: OUG 89/2025 art. III(1) sets aside art. 78, 139, 140, 157 and 220^4 for the RON 200, but not art. 77. Gross monthly pay for art. 77 is all salary income of the month under art. 76(1) to (3) (norm 14(1)), and the RON 200 is salary income. So the RON 200 stays in gross pay when the band is chosen. Leaving it out would give RON 4,725, band "minimum wage + 351 to 400 lei", 16% and a deduction of RON 692.

```oa-check
name: RO payroll, minimum wage RON 4,325 with RON 600 meal vouchers, July 2026
inputs:
  gross_salary: 4325
  meal_vouchers: 600
  relief: 200
  min_wage: 4325
  deduction_rate_pct: 14
steps:
  - cas_base: gross_salary - relief
  - cas: round(cas_base * 0.25)
  - cass_base: cas_base + meal_vouchers
  - cass: round(cass_base * 0.10)
  - deduction: floor(min_wage * deduction_rate_pct / 100)
  - base: gross_salary + meal_vouchers - relief - cas - cass - deduction
  - income_tax: round(base * 0.10)
  - cash_net: gross_salary - cas - cass - income_tax
  - cam: round(cas_base * 0.0225)
  - employer_cost: gross_salary + meal_vouchers + cam
expected:
  cas_base: 4125.00
  cas: 1031.00
  cass_base: 4725.00
  cass: 473.00
  deduction: 605.00
  base: 2616.00
  income_tax: 262.00
  cash_net: 2559.00
  cam: 93.00
  employer_cost: 5018.00
```

## Ask the client first

1. Is this the employee's main job ("funcția de bază"), and how many dependants and school-age children does the employee claim? That decides whether the personal deduction applies and at what rate.
2. Is the contract full-time or part-time, and is the contractual base salary exactly the minimum wage? That decides the RON 300 or 200 relief and the minimum CAS and CASS floor.
3. Does a part-time employee fall into an exempt group (student under 26, pensioner, disability, another contract reaching the minimum wage)? That decides whether the employer tops up CAS and CASS.
4. What is paid besides salary: meal vouchers, gifts, housing, private health, pension, a company car? That decides what goes into each base.
5. Last year's total revenue, average headcount and tax regime (profit tax, micro-enterprise, PFA)? That decides monthly or quarterly D112.
6. Does any employee have a disability certificate, work on an R&D project, work in special conditions, or work for or from a foreign employer? That decides the exemptions, the 4% or 8% extra CAS and the cross-border rules.

## Sources

| Source | URL | Read on |
|---|---|---|
| Legea 227/2015 privind Codul fiscal, ANAF consolidated text with norms, last updated by Legea 170/2026 (art. 60, 64, 66, 76-82, 122, 123^1, 128, 135^2, 138-147, 156-157, 168, 220^1-220^7, 223; norms 4, 13 and 14 to Title IV) | https://static.anaf.ro/static/10/Anaf/legislatie/Cod_fiscal_norme_2023.htm | 2026-10-23 |
| OUG 89/2025 (Monitorul Oficial 1203 of 24 December 2025), preamble and art. III, ANAF copy | https://static.anaf.ro/static/10/Anaf/legislatie/OUG_89_2025.pdf | 2026-10-23 |
| HG 146/2026 (Monitorul Oficial 196 of 13 March 2026), minimum wage from 1 July 2026, ANAF copy | https://static.anaf.ro/static/10/Anaf/legislatie/HG_146_2026.pdf | 2026-10-23 |
| HG 1506/2024, minimum wage RON 4,050 from 1 January 2025, ANAF copy | https://static.anaf.ro/static/10/Anaf/legislatie/HG_1506_2024.pdf | 2026-10-23 |
| Legea 207/2015 privind Codul de procedură fiscală, ANAF consolidated text (art. 174, 176, 181, 336) | https://static.anaf.ro/static/10/Anaf/cod_procedura/Cod_Procedura_Fiscala_2023.htm | 2026-10-23 |
| Legea 201/2025 amending Legea 165/2018 (meal voucher cap RON 45), text sent for promulgation, Chamber of Deputies file PL-x 342/2023 | https://www.cdep.ro/ords/pls/proiecte/docs?2023/pl342_pr342_23.pdf | 2026-10-23 |
| ANAF, D112 technical structure for income from July 2026 (rounding rules, OUG 89/2025 fields) | https://static.anaf.ro/static/10/Anaf/Declaratii_R/AplicatiiDec/structura_D112_0726_070926.pdf | 2026-10-23 |
| Inspecția Muncii, ITM Botoșani notice 69 of 8 January 2026 on Labour Code art. 260 as amended by Legea 239/2025 | https://www.inspectiamuncii.ro/documents/521316/523496/20260112_COMUNICAT+MUNCA+NEDECLARATA+01.2026.pdf/35df8a29-b7a3-4a33-854b-b6042fb55ba3 | 2026-10-23 |
| Inspecția Muncii, REGES page (portal from 1 April 2025) | https://www.inspectiamuncii.ro/reges | 2026-10-23 |
| Inspecția Muncii, "Întrebări și răspunsuri REGES ONLINE" (questions 40, 42, 44) | https://www.inspectiamuncii.ro/documents/66402/85254633/%C3%8Entreb%C4%83ri+%C8%99i+r%C4%83spunsuri+REGES+ONLINE.pdf/690a056b-bcec-49ff-85e5-8d264e7301bc | 2026-10-23 |

Not yet confirmed:
- legislatie.just.ro refused connections on 23 October 2026 (command line and browser), so the Fiscal Code and Procedure Code come from ANAF's consolidations, which ANAF says are not an official republication. HG 295/2025 (REGES ONLINE) and the Labour Code were not read directly: the REGES deadlines come from the Inspecția Muncii Q&A quoting HG 295/2025, and the unregistered-work fine from a Labour Inspectorate notice.
- The maximum meal voucher value for October to December 2026. Legea 201/2025 fixes RON 45 only to September 2026; from October the indexation rule in Legea 165/2018 art. 32 applies again, and we did not find the official figure.
- ANAF guidance confirming that the RON 300 or 200 relief counts in gross pay when choosing the personal deduction band (Example 2 follows the text of OUG 89/2025 and norm 14(1)).
- Fines for late or missing REGES entries (HG 295/2025).
- Any emergency ordinance after Legea 170/2026 that changes these rules for the rest of 2026.

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
