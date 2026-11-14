---
name: in-pf-esi-employer
description: "Use this skill whenever asked about Indian EPF (Employees' Provident Fund), EPS pension, EDLI insurance, ESI (Employees' State Insurance) or employer social security obligations in FY 2026-27. Trigger on phrases like PF contribution India, EPF employer, ESI contribution, provident fund India, PF wage ceiling, 25,000 wage ceiling, PF admin charges, EDLI, EPS pension share, ECR filing, PF return, ESI threshold, PF applicability, 12% PF, joint option higher wages, or any question about computing, depositing or filing EPF or ESI. It covers the Code on Social Security 2020 (in force 21 November 2025), the EPF, Pension and EDLI Schemes 2026, the Social Security (Central) Rules 2026, the 25,000 rupee Chapter III wage ceiling from 17 September 2026, section 2(88) wages, contribution rates, deadlines and damages. Tier 2, not reviewed by an accountant."
license: "AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)"
metadata:
  source: openaccountants
  openaccountants_url: "https://www.openaccountants.com/skills/in-pf-esi-employer"
  jurisdiction: "IN"
  tax_year: "2026"
  last_updated: "2026-11-14"
---

# India EPF and ESI: what the employer must pay and file, FY 2026-27

> **General reference only.** This skill is general reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts. Do not rely on it to pay, file or take a position without review by a qualified professional in India. Label every computation as an estimate.

This skill covers an Indian employer's provident fund (EPF), pension (EPS), deposit-linked insurance (EDLI) and Employees' State Insurance (ESI) obligations, for FY 2026-27 (1 April 2026 to 31 March 2027). Social security contributions are not set by tax year, so the skill states the rules in force on 14 November 2026 and the date each one started. The law moved three times: the Code on Social Security, 2020 came into force on 21 November 2025 and replaced the EPF Act 1952 and the ESI Act 1948 for most purposes; the Social Security (Central) Rules, 2026 (8 May 2026) and the Employees' Provident Funds Scheme, 2026, Employees' Pension Scheme, 2026 and Employees' Deposit-Linked Insurance Scheme, 2026 (all notified 29 June 2026) replaced the old rules and schemes; and S.O. 5109(E) of 17 September 2026 set the Chapter III wage ceiling at 25,000 rupees a month. Anything that still cites the 1952 Act, the 1948 Act or the EPF Scheme 1952 for a current rate is out of date.

Most rates are printed in WORDS in the law ("twelve per cent", "three and one-fourth per cent"). The rates table gives the words and the digits. Several amounts (the ESI wage ceiling under the Code, the EPF administrative charge, the EDLI contribution rate, the interest rate on late payment) are fixed by notifications that could not be read; where that is so, the skill says what to check and gives no number.

## Who this applies to

- Employers with establishments covered by Chapter III (provident fund) or Chapter IV (ESI) of the Code on Social Security, 2020, and their payroll preparers.
- Administering bodies: the Central Board (EPFO) for Chapter III; the Corporation (ESIC) for Chapter IV.
- Out of scope: salary TDS, gratuity and bonus (use `india-payroll`), profession tax (use `in-professional-tax`), benefit claims (refer to EPFO or ESIC).

| Field | Value |
| --- | --- |
| Parent law | Code on Social Security, 2020 (36 of 2020), Chapter III (provident fund) and Chapter IV (ESI) |
| EPF rules | Employees' Provident Funds Scheme, 2026 (G.S.R. 525(E)), in force on publication, superseding the EPF Scheme 1952 |
| Pension rules | Employees' Pension Scheme, 2026 (G.S.R. 527(E)), superseding the Employees' Pension Scheme 1995 |
| Insurance rules | Employees' Deposit-Linked Insurance Scheme, 2026 (G.S.R. 526(E)), superseding the 1976 scheme |
| ESI rules | Social Security (Central) Rules, 2026 (G.S.R. 344(E)), rule 19 (contribution rates) |
| Registration | Form-I of the Occupational Safety, Health and Working Conditions (Central) Rules, 2026, on the Shram Suvidha Portal (Social Security (Central) Rules, 2026, rule 5) |

### When each law started

S.O. 5319(E) brought most of the Code into force on 21 November 2025. As first printed it listed only clause (c) of section 16(1) and items 1, 2 and 4 to 9 of section 164(1). A corrigendum, S.O. 5936(E) of 19 December 2025, replaced those entries with "section 16 except the provisions of the Code specified at serial numbers (ii), (iii) and (iv) of S.O.2060(E)" and "sub-section (1) of section 164 except ... serial number (vi) of S.O.2060(E)". The excepted provisions were already in force from 3 May 2023 (S.O. 2060(E)): section 16(1)(b), section 16(1)(a) in so far as it relates to the Pension Scheme, and the repeal of the pension provisions of the EPF Act 1952. So section 16 and the repeal of the EPF Act 1952 apply from 21 November 2025. Section 164(2)(b), brought in by the same corrigendum, kept the EPF Scheme 1952, the EDLI Scheme 1976, the Pension Scheme 1995 and the ESI rules and regulations in force, to the extent not inconsistent with the Code, for one year; the 2026 schemes replaced the first three on publication.

### Coverage

EPF (Chapter III) applies to every establishment in which twenty or more employees are employed; ESI (Chapter IV) to every establishment in which ten or more persons are employed, other than a seasonal factory (Code, First Schedule). ESI also applies to an establishment in a hazardous or life-threatening occupation notified by the Central Government even with a single employee (First Schedule, proviso). Once a Chapter applies, it keeps applying even if the headcount later falls (section 1(8)). Employees paid above the wage ceiling still count towards the headcount (section 2(26), proviso). An employer and a majority of employees may agree to bring a smaller establishment into EPF (section 1(5)) or ESI (section 1(7)). The government backgrounder of 21 November 2025 says there is no "notified areas" test for ESI any more and establishments with fewer than 10 employees may opt in with mutual consent; the backgrounder of 22 November 2025 says EPF now reaches "all establishments that have 20 or more employees, regardless of the type of industry", replacing the old scheduled-industry list.

### Conservative defaults

| Ambiguity | Default |
| --- | --- |
| Unknown whether the establishment is covered | Count every employee, including those above the wage ceiling; do not assume |
| Unknown wage components | Apply the section 2(88) definition of wages and the one-half add-back |
| Unknown ESI wage ceiling for the month | Do not use a remembered figure; check the ESIC portal or the Gazette for a notification after 16 March 2026 |
| Month before 17 September 2026 | The 25,000 rupee EPF ceiling does not apply; get the ceiling in force for that month (S.O. 2702(E) of 29 May 2026 or earlier) |
| Unknown whether an employee is an International Worker | Ask for passport and any certificate of coverage before computing |

## Rates, bands and thresholds

| Item | Rate or amount | Condition | Source |
| --- | --- | --- | --- |
| EPF coverage, Chapter III | Twenty or more employees | Establishment headcount, First Schedule | https://egazette.gov.in/WriteReadData/2020/222111.pdf |
| ESI coverage, Chapter IV | Ten or more persons | Other than a seasonal factory; one person in a notified hazardous occupation | https://egazette.gov.in/WriteReadData/2020/222111.pdf |
| Wages: excluded items above this share of all remuneration are added back | One-half (50%) | Code s 2(88), "or such other per cent. as may be notified" | https://egazette.gov.in/WriteReadData/2020/222111.pdf |
| Wages: remuneration in kind counted as wages, up to | Fifteen per cent of total wages | Code s 2(88) Explanation | https://egazette.gov.in/WriteReadData/2020/222111.pdf |
| EPF wage ceiling, Chapter III | 25,000 rupees per month | From 17 September 2026 (date of publication), superseding S.O. 2702(E) of 29 May 2026 | https://egazette.gov.in/WriteReadData/2026/276299.pdf |
| ESI coverage wage limit | 21,000 rupees per month | Ministry of Labour FAQ of 16 March 2026, reply 12: applies "at present" until the Code's rules are finalised | https://www.labour.gov.in/static/uploads/2026/03/a4ccf4c6d97c4f1f36a6d83f8c64213d.pdf |
| EPF employer contribution | Twelve per cent (12%) of wages | EPF Scheme 2026 paragraph 18; on wages up to the ceiling unless a joint option | https://egazette.gov.in/WriteReadData/2026/273957.pdf |
| EPF employee contribution | Equal to the employer's | Paragraph 18 | https://egazette.gov.in/WriteReadData/2026/273957.pdf |
| EPF reduced rate | Ten per cent (10%) | Only for the class of establishments notified by the Central Government | https://egazette.gov.in/WriteReadData/2026/273957.pdf |
| Code s 16(1)(a) provident fund rate as printed | Ten per cent, twelve per cent for notified establishments | The Code's own text; the 2026 Scheme prints the reverse (see refer list) | https://egazette.gov.in/WriteReadData/2020/222111.pdf |
| EPS: part of employer's contribution sent to the Pension Fund | Eight and thirty-three hundredths per cent (8.33%) | Of wages up to the wage ceiling, Pension Scheme 2026 paragraph 4 | https://egazette.gov.in/WriteReadData/2026/273951.pdf |
| Central Government contribution to the Pension Fund (not an employer cost) | One and sixteen hundredths per cent (1.16%) of pay | Paragraph 4 | https://egazette.gov.in/WriteReadData/2026/273951.pdf |
| EPS employer share for members with an accepted higher-wage joint option (from 1 September 2014) | Nine and forty-nine hundredths per cent (9.49%) | The increase applies to wages above fifteen thousand rupees per month | https://egazette.gov.in/WriteReadData/2026/273951.pdf |
| EDLI contribution, upper limit set by the Code | One per cent (1%) of wages | Actual rate notified by the Central Government with the Central Board; not read | https://egazette.gov.in/WriteReadData/2020/222111.pdf |
| EDLI death benefit, twelve months' continuous employment limb | Not less than 2,50,000 and not more than 7,00,000 rupees | Paid by the EPFO to the family | https://egazette.gov.in/WriteReadData/2026/273942.pdf |
| ESI employer contribution | Three and one-fourth per cent (3.25%) of wages | Rule 19(1), rounded to the next higher rupee | https://egazette.gov.in/WriteReadData/2026/272366.pdf |
| ESI employee contribution | Three-fourth per cent (0.75%) of wages | Rule 19(1); none from an exempted employee under Code s 2(31) | https://egazette.gov.in/WriteReadData/2026/272366.pdf |
| ESI sickness benefit (paid by the Corporation) | Seventy per cent of the standard benefit rate | Rule 22(1) | https://egazette.gov.in/WriteReadData/2026/272366.pdf |
| ESI disablement benefit, daily rate | Ninety per cent of the standard benefit rate | Rule 22(5) | https://egazette.gov.in/WriteReadData/2026/272366.pdf |
| ESI funeral expenses | Twenty thousand rupees | Rule 21 | https://egazette.gov.in/WriteReadData/2026/272366.pdf |
| ESI confinement medical bonus | Fifteen thousand rupees per case | Where ESI facilities are not available, two confinements only, rule 22(4) | https://egazette.gov.in/WriteReadData/2026/272366.pdf |
| EPF damages, default of less than two months | 0.25% a month on the arrears | EPF Scheme 2026 paragraph 23(1), capped at the arrears | https://egazette.gov.in/WriteReadData/2026/273957.pdf |
| EPF damages, more than two and less than four months | 0.50% a month | Same | https://egazette.gov.in/WriteReadData/2026/273957.pdf |
| EPF damages, more than four months | 1% a month | Same | https://egazette.gov.in/WriteReadData/2026/273957.pdf |
| Deposit to dispute an ESI claim in the Employees' Insurance Court | Fifty per cent of the amount claimed | Court may waive or reduce | https://egazette.gov.in/WriteReadData/2020/222111.pdf |
| Deposit to appeal an EPF assessment under s 125 | Twenty-five per cent of the amount determined | With the Social Security Organisation concerned | https://egazette.gov.in/WriteReadData/2020/222111.pdf |

## The base

### Wages for contributions

The schemes apply their rates to "wages". The EPF Scheme 2026 says words it does not define take the Code's meaning (paragraph 2(2)), and the EDLI Scheme 2026 points to clause (88) of section 2 of the Code (paragraph 5(1)). Section 2(88) defines wages once, for every Chapter. The Ministry of Labour FAQ confirms the definition of wages applies from 21 November 2025.

| Included in wages (Code s 2(88)) | Excluded from wages (Code s 2(88)) |
| --- | --- |
| Basic pay | Statutory or other bonus that is not part of the remuneration under the terms of employment |
| Dearness allowance | Value of house accommodation, light, water, medical attendance or another excluded amenity |
| Retaining allowance, if any | Employer contribution to a pension or provident fund, and interest on it |
| Remuneration in kind, up to fifteen per cent of total wages (Explanation) | Conveyance allowance or travelling concession |
|  | Sums to defray special expenses of the job |
|  | House rent allowance |
|  | Remuneration under an award or settlement |
|  | Overtime allowance |
|  | Commission |
|  | Gratuity on termination |
|  | Retrenchment compensation, other retirement benefit, ex gratia on termination |

The one-half rule: if the excluded items in the first nine exclusions (bonus to commission) exceed one-half of total remuneration, the excess is added back into wages.

### EPF (EPF Scheme 2026, paragraph 18)

- Both shares are on the wages actually drawn or payable for the month, whether paid daily, weekly, fortnightly or monthly (paragraph 18(4)).
- Each contribution is rounded to the nearest rupee: fifty paise or more goes up, less than fifty paise is ignored (paragraph 18(5)).
- Where the monthly wage is above the wage ceiling, both shares are limited to the contribution on the ceiling (paragraph 18(3)), unless the employer and the employee jointly opt in writing to contribute on the higher wage; the employer then also pays administrative charges on it (paragraph 9(4)).
- An employee whose wage is above the ceiling when he would otherwise join is an "excluded employee" (paragraph 2(f)(i)); he joins as soon as he stops being excluded (paragraph 9(3)). With the ceiling at 25,000 rupees from 17 September 2026, employees earning above the old ceiling but not above 25,000 rupees are no longer excluded.
- The ten per cent rate applies only to a class of establishments the Central Government has notified. The list was not on any page read; ask for the notification before using it.
- The ceiling is the "wage ceiling" in section 2(89) of the Code (the EDLI Scheme applies "the wage ceiling specified in clause (89) of section 2 of the Code").

### Pension share (Employees' Pension Scheme 2026, paragraph 4)

- The pension share comes out of the employer's twelve per cent; it is not an extra cost. What is left of the employer's share stays in the provident fund account.
- The pension share is on wages up to the wage ceiling only. Where the wage is above the ceiling, the employer's and the Central Government's pension contributions are limited to the amount on the ceiling.
- The higher pension share applies only to members who exercised the joint option under paragraph 11 of the old 1995 scheme and were found eligible. Do not read the "fifteen thousand rupees" in that rule as the general wage ceiling.
- The pension share is rounded to the nearest rupee, fifty paise up (paragraph 4(3)), and remitted within fifteen days of the close of every month, with the cost of remittance borne by the employer (paragraph 4(1)).

### EDLI (Employees' Deposit-Linked Insurance Scheme 2026)

- Only the employer pays EDLI. It may not deduct the contribution from wages or recover it from the employee (paragraph 8).
- The contribution is on section 2(88) wages up to the wage ceiling (paragraph 5(1)), at the notified rate (not read). The earlier fixed rate is not stated here.
- The death benefit is set by a formula on average wages and the provident fund balance; the floor and cap in the rates table apply to the limb for a member employed continuously for twelve months before death. Leave benefit claims to the EPFO.

### Administrative charges

The EPF Scheme 2026 makes the employer pay "administrative charges or other fees or charges" with the contributions (paragraph 20(1)) and extra administrative charges on wages above the ceiling where there is a joint option (paragraph 9(4)) or voluntary contributions (paragraph 19(3)). It does not print the rate. Take the current rate from the EPFO portal.

### ESI (Social Security (Central) Rules 2026, rule 19)

- Each share is a sum "rounded to the next higher rupee" on the wages payable for the wage period (rule 19(1)). That is a different rounding rule from EPF.
- For an employee who is a person with disability under the Rights of Persons with Disabilities Act, 2016 and under the National Trust Act, 1999, the employer does not pay its share for up to three years from the start of the contribution period, or such period as the Central Government specifies; the Central Government reimburses the Corporation (rule 19(2) and (3)). The employee's share is still due.
- An "exempted employee" is one "whose wage is specified in the notification by the Central Government and who is not liable to pay employee's contribution" (Code section 2(31)); the employer still pays its share. The notified wage was not read; check it before deducting the employee share.
- The employer pays both shares and may recover the employee's share only by deduction from the wages of the period it relates to (Code section 31(2)). It may never deduct its own share from wages (section 31(3)) and bears the cost of remitting (section 31(5)).
- Wages are the Code's section 2(88) wages. The earlier wider "gross wages" list (HRA, overtime, all cash payments) does not match the Code text; see "When to refuse or refer".
- For Chapter IV an employee is one "drawing wages less than or equal to the wage ceiling" (section 2(26), first proviso). S.O. 5109(E) set the 25,000 rupee ceiling for Chapter III only; the ESI coverage limit stays at 21,000 rupees per the Ministry FAQ until a Chapter IV notification is read.
- Contribution period and benefit period: each is a period "not exceeding six consecutive months", "as specified in the regulations made under section 157" (rule 2). The regulations were not readable, so no calendar dates are given.

### ESI benefits (paid by the Corporation, for context)

| Benefit | Rule in the Social Security (Central) Rules 2026 |
| --- | --- |
| Sickness | Seventy per cent of the standard benefit rate, if contributions were payable for at least seventy-eight days in the contribution period; not for the first two days of a spell (unless it follows the last paid spell within fifteen days); not more than ninety-one days in two consecutive benefit periods (rule 22(1)) |
| Maternity | Daily rate equal to the standard benefit rate, for up to twenty-six weeks, of which not more than eight weeks before the expected confinement (rule 22(3)) |
| Confinement expenses | Medical bonus in the rates table, where ESI facilities are not available, for two confinements only (rule 22(4)) |
| Disablement | Ninety per cent of the standard benefit rate, the "full rate" (rule 22(5)) |
| Dependants | Shares of the full rate: the widow three-fifths, each son until twenty-five and each unmarried daughter two-fifths (rule 22(6)) |
| Funeral expenses | Amount in the rates table (rule 21) |

### Edge cases

- **Establishments below 20 employees:** may be covered for EPF if the employer and a majority of employees agree (Code section 1(5)). Once a Chapter applies, it keeps applying even if numbers fall (section 1(8)).
- **Contract labour:** for EPF, the principal employer is responsible for both contributions and administrative charges for workers engaged by or through a contractor whose establishment is not registered independently; the contractor recovers the employee's share and pays it to the principal employer (EPF Scheme 2026, paragraph 20). For ESI, the employer pays for employees employed directly or through a contractor and may recover from the contractor (Code section 31); contributions may also be recovered from the contractor under section 17 of the Code.
- **Fixed-term employees:** the Code defines fixed term employment as a written contract for a fixed period, and the worker "shall be eligible for all benefits, under any law for the time being in force, available to a permanent employee proportionately according to the period of service rendered by him" (section 2(34)). The earlier "from day one, no waiting period" is not printed on any page read; apply the same joining rules as for a permanent employee.
- **Exempted establishments (PF trust):** an establishment may be exempted under section 143 of the Code and run its own provident fund; contributions under its rules still feed the pension share (Pension Scheme paragraph 4(1)). The scheme's monthly return form for exempted PF trusts prints the contribution rate field as "Selection from 10 or 12% as applicable". The conditions of exemption were not read; refer.
- **Voluntary contributions (VPF):** an employee may opt to make an additional voluntary contribution "on wages exceeding the statutory wage ceiling at statutory rate or at any rate in excess of statutory rate", passed to the Commissioner through the Electronic Challan-cum-Return (EPF Scheme 2026, paragraph 19(1)). The employer does not have to match it (paragraph 19(2)) but pays extra administrative charges (paragraph 19(3)). Voluntary contributions may not exceed wages after the deductions allowed under section 18(2) of the Code.
- **Employees' Enrolment Campaign, 2026 and VISHWAS, 2026:** the EPF Scheme 2026 Annexure let any employer, until 31 October 2026, declare and enrol employees who joined between 1 April 2009 and 31 March 2026 and were never enrolled, with compliance from the month of declaration, provided the employee's share was not already deducted and kept. VISHWAS, 2026 is a separate damages scheme for defaults before 14 June 2024, valid for six months from the scheme's notification. The campaign is closed after 31 October 2026; check whether it was extended before relying on it.

## Deadlines and filing

### EPF, EPS and EDLI

| Item | Detail |
| --- | --- |
| Registration | Electronic, Form-I on the Shram Suvidha Portal; certificate within seven days of a complete application or the establishment is deemed registered (rule 5(1)); changes updated within thirty days (rule 5(6)) |
| First return | Consolidated return in Form V within fifteen days of the scheme applying to the establishment; a "Nil" return if nobody qualifies (EPF Scheme 2026, paragraph 24(1)) |
| Monthly payment | Employer and employee shares and administrative charges, within fifteen days of the close of every month (paragraph 20(1)); pension share in the same period (Pension Scheme paragraph 4(1)); EDLI contributions and charges in the same period, electronically (EDLI Scheme paragraph 6(1)) |
| Monthly return | Electronic Challan-cum-Return (paragraph 19(1)); plus, within fifteen days of the close of each month, uploads of new members, transfers in and leavers (paragraph 24(2)) |
| Ownership return | Form VI after registration (paragraph 24) |
| International Workers | Monthly upload of International Workers joining, transferring in and leaving, within fifteen days of the close of each month (paragraph 24) |
| Annual return | None separate in the EPF Scheme 2026: the Form V first return and the monthly uploads are what paragraph 24 requires |

The earlier "within one month" (EPF) and "within 15 days" (ESI) registration deadlines are not printed on any page read and stay out.

### ESI

| Item | Detail |
| --- | --- |
| Who pays | The employer pays both shares, for direct and contractor employees (Code section 31(1)) |
| When due | Contributions for a wage period ordinarily fall due on the last day of the wage period (section 29(4)); the payment date and return periods are in the Corporation's regulations, which were not readable. Check the ESIC portal |
| Half-yearly returns | The earlier half-yearly return dates could not be read on any allowed page and stay out |

## Penalties and interest

- EPF damages are a monthly rate on the arrears from the rates table, and may not exceed the arrears (paragraph 23(1)). The same table applies to defaults under paragraph 32-A of the 1952 scheme from 14 June 2024 (paragraph 23(2)). It replaces the earlier annual damages bands. EDLI damages follow the same table (EDLI Scheme paragraph 7(1)).
- Interest on late payment: the Code charges simple interest "at such rate as may be notified from time to time by the Central Government" (section 127). No notification printing the rate was read, so no annual rate is stated.
- ESI: simple interest at the notified rate (section 127); damages not exceeding the arrears, in the manner the regulations specify (section 128).
- Disputes: deposit fifty per cent of the ESI amount claimed with the Employees' Insurance Court before raising a dispute (the Court may waive or reduce it); deposit twenty-five per cent of an EPF amount determined under section 125 before appealing. The government backgrounder of 22 November 2025 states the 25% EPF appeal deposit in digits.

## Cross-border points

### International Workers (EPF Scheme 2026, paragraphs 2, 9 and 10)

| Scenario | Treatment |
| --- | --- |
| Foreign passport holder working for a covered establishment in India | An "International Worker"; must join the Fund from the date of joining the establishment (or the date the scheme applies to it, whichever is later) |
| Indian employee who has worked or will work in a country with a social security agreement and can get benefits there | Also an "International Worker" under paragraph 2(j)(ii) |
| International Worker who contributes at home under a social security agreement and holds detached-worker status | An excluded employee for the period and terms of the agreement |
| International Worker covered by a pre-1 October 2008 comprehensive economic agreement that exempts contributions | An excluded employee |
| Nepalese or Bhutanese national under the 1950 and 2007 treaties | Treated as an Indian worker |
| Worker in a country listed in the paragraph 9(6) table who wants detachment under that agreement | Pays, with the employer, on total wages under section 2(88). The table lists one country: the United Kingdom |

No allowed page prints the number of social security agreements, so none is given. Whether the general wage ceiling exclusion applies to an International Worker is not settled by the text read; refer.

## Two worked examples that recompute

All wages are hypothetical section 2(88) wages with no exclusions above one-half. EDLI and administrative charges are left out because their rates are notified and not read: add them from the EPFO portal.

### Example 1: Employee on 12,000 rupees a month, in both EPF and ESI

The wage is under the 25,000 rupee EPF ceiling and the 21,000 rupee ESI limit. EPF: 12% of 12,000 = 1,440 from the employee and 1,440 from the employer. Pension share: 8.33% of 12,000 = 999.60, rounded to the nearest rupee = 1,000; the other 440 of the employer's share stays in the provident fund. ESI: employer 3.25% = 390, employee 0.75% = 90 (both already whole rupees). Employer cost before EDLI and charges: 1,440 + 390 = 1,830. Deducted from the employee: 1,440 + 90 = 1,530. If this employee has a disability under the 2016 Act and is in the first three years of the contribution period, the employer's 390 is not payable (the Central Government reimburses it) but the 90 is still deducted.

```oa-check
name: EPF and ESI on 12,000 rupees a month (EPF Scheme 2026, Pension Scheme 2026, rule 19)
inputs:
  wages: 12000
steps:
  - epf_employee: round(wages * 0.12)
  - epf_employer: round(wages * 0.12)
  - eps_share: round(wages * 0.0833)
  - pf_left: epf_employer - eps_share
  - esi_employer: ceil(wages * 0.0325)
  - esi_employee: ceil(wages * 0.0075)
  - employer_cost: epf_employer + esi_employer
  - employee_deduction: epf_employee + esi_employee
expected:
  eps_share: 1000
  pf_left: 440
  employer_cost: 1830
  employee_deduction: 1530
```

### Example 2: Employee on 40,000 rupees a month in November 2026, joint option or not

The wage is above the 25,000 rupee EPF ceiling (in force from 17 September 2026) and above the 21,000 rupee ESI limit, so no ESI. Without a joint option, both EPF shares are 12% of 25,000 = 3,000; the pension share is 8.33% of 25,000 = 2,082.50, rounded to 2,083; 917 of the employer's share stays in the fund. With a written joint option under paragraph 9(4), both shares are 12% of 40,000 = 4,800, the pension share stays at 2,083 (no accepted higher-pension option), so 2,717 goes to the provident fund, and administrative charges also apply to the higher wage. The decision: the option costs the employer 1,800 more a month (4,800 less 3,000) plus charges, and puts 1,800 more of the employee's pay into the fund each month.

```oa-check
name: EPF on 40,000 rupees a month, ceiling 25,000, with and without a joint option
inputs:
  wages: 40000
  ceiling: 25000
steps:
  - base_capped: min(wages, ceiling)
  - share_capped: round(base_capped * 0.12)
  - eps_share: round(base_capped * 0.0833)
  - pf_left_capped: share_capped - eps_share
  - share_joint: round(wages * 0.12)
  - pf_left_joint: share_joint - eps_share
  - extra_employer_cost: share_joint - share_capped
expected:
  share_capped: 3000
  eps_share: 2083
  pf_left_capped: 917
  share_joint: 4800
  pf_left_joint: 2717
  extra_employer_cost: 1800
```

## Ask the client first

- How many employees and other persons are on the payroll, including contract workers and anyone paid above the wage ceiling, and was the number ever at or above twenty (EPF) or ten (ESI)?
- What is each employee's pay broken down by component (basic, dearness allowance, HRA, conveyance, overtime, commission, bonus, in-kind benefits), so you can apply section 2(88) and the one-half test?
- Which month is being computed (before or after 17 September 2026), and does any employee have a written joint option to contribute on wages above the ceiling, or an accepted higher-pension option under the old 1995 scheme?
- Is any employee a foreign passport holder, or an Indian posted abroad, and do they hold a certificate of coverage under a social security agreement?
- Is the establishment exempted under section 143 (own PF trust), notified for the ten per cent rate, or in a notified hazardous occupation?
- Does any employee have a disability under the 2016 Act, and when did their ESI contribution period start? Could any employee fall in a notified exempted-employee band under section 2(31)?

### The method, step by step

1. Confirm the establishment is covered (rates table), counting employees above the wage ceiling (Code First Schedule, section 1(8)).
2. Register on the Shram Suvidha Portal in Form-I if not registered (rule 5).
3. Work out each employee's wages under section 2(88): basic pay, dearness allowance and retaining allowance, plus any excess of the listed exclusions over one-half of total remuneration.
4. Take the EPF wage ceiling for the month (25,000 rupees from 17 September 2026) and confirm the ESI limit, EPF administrative charge and EDLI rate from the current notifications or the EPFO and ESIC portals.
5. EPF: employee and employer shares of twelve per cent of wages up to the ceiling (or actual wages under a joint option; or ten per cent for a notified class), rounded to the nearest rupee.
6. Split the employer's share: 8.33% of wages up to the ceiling to the Pension Fund, the rest to the provident fund.
7. Add EDLI at the notified rate on wages up to the ceiling, and EPF administrative charges.
8. ESI, for employees within the ESI limit: employer 3.25% and employee 0.75% of wages (none from an exempted employee), each rounded up to the next rupee; no employer share for a person with disability for up to three years.
9. Pay EPF, EPS and EDLI and file the Electronic Challan-cum-Return within fifteen days of the close of the month; upload joiners, transfers and leavers in the same period.
10. Pay ESI by the date in the Corporation's regulations (check the ESIC portal). If any payment is late, expect simple interest at the notified rate and damages (EPF: the monthly table).

### When to refuse or refer

- Which provident fund rate governed a month from 21 November 2025 until the EPF Scheme 2026: section 16(1)(a) of the Code prints ten per cent with twelve per cent only for notified establishments, while paragraph 18(2) of the 2026 Scheme prints twelve per cent with ten per cent for a notified class. No notification under the first proviso to section 16(1)(a) was read. Refer any dispute about the rate for those months.
- Any month before 17 September 2026 that needs the EPF wage ceiling then in force (S.O. 2702(E) of 29 May 2026 and earlier were not read).
- Any computation that needs the EPF administrative charge, EDLI rate, interest rate, a Chapter IV ESI wage ceiling notification, or the list of ten per cent establishments, until the client provides the notification.
- International Workers: whether the wage ceiling exclusion applies to them, totalisation and detachment under a specific agreement, and withdrawals on leaving India.
- ESI wages: whether ESIC still applies a wider "gross wages" base than section 2(88) in practice; and when an employee who crosses the ESI limit mid-period leaves coverage. Both sit in regulations that could not be read.
- ESI payment due date and return periods (regulations not readable).
- Exempted PF trusts (section 143), damages waivers under an insolvency plan, VISHWAS, 2026 cases, and any EPFO inquiry under section 125 or appeal.
- Benefit claims (EDLI death benefit, pension, ESI benefits): refer to the EPFO or ESIC.
- Salary TDS, gratuity and bonus: use `india-payroll`. Profession tax: use `in-professional-tax`.

### Prohibitions

- NEVER compute EPF or ESI on a component list from the old Acts: use section 2(88) wages and the one-half add-back.
- NEVER use a remembered ESI wage ceiling, EPF administrative charge, EDLI rate or interest rate: each is notified.
- NEVER apply the 25,000 rupee EPF ceiling to a month before 17 September 2026, or to ESI.
- NEVER put more than 8.33% of wages up to the ceiling into the pension share, except for an accepted higher-pension joint option.
- NEVER deduct the employer's EPF, EDLI or ESI share from the employee's wages.
- NEVER apply EPF damages as an annual rate: the table is per month on the arrears, capped at the arrears.
- NEVER miss the fifteen-day deadline after the close of the month for EPF, EPS and EDLI.
- NEVER treat the ten per cent EPF rate as available without the notification covering the establishment's class.
- NEVER present calculations as definitive; label them as estimates.

## Sources

| Source | URL | Read on |
| --- | --- | --- |
| Read for Code on Social Security, 2020 sections 1, 2(26), 2(31), 2(34), 2(88), 2(89), 16, 17, 29, 31, 125, 127, 128, 143 and the First Schedule thresholds | https://egazette.gov.in/WriteReadData/2020/222111.pdf | 2026-11-14 |
| Read for S.O. 5319(E), commencement of the Code on 21 November 2025 | https://egazette.gov.in/WriteReadData/2025/267882.pdf | 2026-11-14 |
| Read for the corrigendum S.O. 5936(E) of 19 December 2025 to S.O. 5319(E) | https://egazette.gov.in/WriteReadData/2025/268694.pdf | 2026-11-14 |
| Read for S.O. 2060(E), commencement on 3 May 2023 of s 16(1)(b) and the pension parts | https://egazette.gov.in/WriteReadData/2023/245642.pdf | 2026-11-14 |
| Read for Social Security (Central) Rules, 2026 (G.S.R. 344(E)) rules 2, 5, 19, 21 and 22 | https://egazette.gov.in/WriteReadData/2026/272366.pdf | 2026-11-14 |
| Read for EPF Scheme, 2026 (G.S.R. 525(E)) paragraphs 2, 9, 10, 18, 19, 20, 23, 24 and the Enrolment Campaign Annexure | https://egazette.gov.in/WriteReadData/2026/273957.pdf | 2026-11-14 |
| Read for Employees' Pension Scheme, 2026 (G.S.R. 527(E)) paragraph 4 | https://egazette.gov.in/WriteReadData/2026/273951.pdf | 2026-11-14 |
| Read for EDLI Scheme, 2026 (G.S.R. 526(E)) paragraphs 5 to 8 and the assurance benefit limits | https://egazette.gov.in/WriteReadData/2026/273942.pdf | 2026-11-14 |
| Read for S.O. 5109(E) of 17 September 2026, the 25,000 rupee Chapter III wage ceiling | https://egazette.gov.in/WriteReadData/2026/276299.pdf | 2026-11-14 |
| Read for Ministry of Labour FAQ of 16 March 2026, replies 7 and 12 (wages definition from 21 November 2025, ESI limit of Rs 21,000) | https://www.labour.gov.in/static/uploads/2026/03/a4ccf4c6d97c4f1f36a6d83f8c64213d.pdf | 2026-11-14 |
| Read for the government backgrounder on the Labour Codes of 21 November 2025 (ESI opt-in below 10 employees) | https://static.pib.gov.in/WriteReadData/specificdocs/documents/2025/nov/doc20251121701501.pdf | 2026-11-14 |
| Read for the government backgrounder on the Code on Social Security of 22 November 2025 (50% add-back, 25% appeal deposit, EPF for all establishments with 20 or more) | https://static.pib.gov.in/WriteReadData/specificdocs/documents/2025/nov/doc20251122702601.pdf | 2026-11-14 |
| EPFO employer pages (tried for the administrative charge and EDLI rate) | https://www.epfindia.gov.in/site_en/For_Employers.php | Refused (403) on 2026-11-14, not read |
| ESIC contribution page (tried for the payment due date and ESI ceiling) | https://www.esic.gov.in/contribution | Timed out on 2026-11-14, not read |

Not yet confirmed: the ESI (Chapter IV) wage ceiling under the Code after 16 March 2026 (S.O. 2702(E) of 29 May 2026 was not read); the EPF wage ceiling for months before 17 September 2026; the EPF administrative charge and its minimum; the EDLI contribution rate; the interest rate under section 127; the list of establishments notified for the ten per cent EPF rate; the ESI payment due date, return periods, contribution and benefit period dates (regulations under section 157); the wage band for an ESI exempted employee under section 2(31); exemption conditions under section 143; whether the Enrolment Campaign was extended past 31 October 2026.

## Today's figures and who stands behind this skill

This file is an AI skill (tax rules your AI follows) from OpenAccountants, copied on 2026-11-14. Rates, thresholds and deadlines change. For the current version of this skill, its official sources and the named accountant (if any) who stands behind it, call `get_skill` with slug `in-pf-esi-employer` on the OpenAccountants connector (https://www.openaccountants.com/connect), or read https://www.openaccountants.com/skills/in-pf-esi-employer. If neither is available, confirm every figure against the official source pages cited above before relying on it.
