---
name: in-pf-esi-employer
description: >
  Use this skill whenever asked about Indian EPF (Employees' Provident Fund), EPS
  pension, EDLI insurance, ESI (Employees' State Insurance) or employer social security
  obligations in FY 2026-27. Trigger on phrases like PF contribution India, EPF employer,
  ESI contribution, provident fund India, PF wage ceiling, 25,000 wage ceiling, PF admin
  charges, EDLI, EPS pension share, ECR filing, PF return, ESI threshold, PF
  applicability, 12% PF, joint option higher wages, or any question about computing,
  depositing or filing EPF or ESI. It covers the Code on Social Security 2020 (in force
  21 November 2025), the EPF, Pension and EDLI Schemes 2026, the Social Security
  (Central) Rules 2026, the 25,000 rupee Chapter III wage ceiling from 17 September 2026,
  section 2(88) wages, contribution rates, deadlines and damages. Tier 2, not reviewed
  by an accountant.
version: "2.1"
jurisdiction: IN
tax_year: 2026
tax_year_notes: "FY 2026-27, checked as at 22 November 2026. Apply the rules in force for the contribution month."
last_updated: 2026-11-22
category: international
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
tier: 2
domain: payroll
type: computation
---

# India EPF and ESI: what the employer must pay and file, FY 2026-27

> **General reference only.** This skill is general reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts. Do not rely on it to pay, file or take a position without review by a qualified professional in India. Label every computation as an estimate.

This skill covers monthly EPF, EPS, EDLI and ESI obligations in FY 2026-27 (1 April 2026 to 31 March 2027), using law checked on 22 November 2026. Most provisions of the Code on Social Security, 2020 commenced on 21 November 2025. The Social Security (Central) Rules, 2026 were issued on 8 May 2026, and the 2026 EPF, EPS and EDLI schemes were notified on 29 June 2026. The Chapter III wage ceiling rose to 25,000 rupees on 17 September 2026. From 21 November 2026, the new Chapter IV wage-ceiling and employee-exemption notices apply. The ESI (General) Regulations, 2026 supersede the 1950 regulations with a saving for earlier matters.

Use the rates table for ordinary covered employment. Check the applicable period, establishment class and any exemption or higher-wage option.

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

The First Schedule sets thresholds of 20 employees for EPF and 10 persons for ESI, with the ESI seasonal-factory exception. EPF is subject to the exceptions in section 20, including certain co-operatives employing fewer than 50 people without power and certain establishments with their own statutory funds or pensions. ESI also covers a notified hazardous or life-threatening occupation with a single employee. Check the First Schedule benefit-start notification for when ESI contributions become payable for the establishment. Once a Chapter applies, it keeps applying if the headcount falls (section 1(8)). Count employees above the wage ceiling (section 2(26)). For a voluntary opt-in under section 1(5) or (7), obtain the agreement of the employer and a majority of employees and the relevant authority's notification.

### Conservative defaults

| Ambiguity | Default |
| --- | --- |
| Unknown whether the establishment is covered | Count every employee, including those above the wage ceiling; do not assume |
| Unknown wage components | Apply the section 2(88) definition of wages and the one-half add-back |
| ESI wage ceiling | From 21 November 2026 use S.O. 6339(E) and check the disability definition. For an earlier month check the then-applicable rules |
| EPF before 17 September 2026 | S.O. 2702(E) specifies 15,000 rupees per month for Chapter III from its publication on 29 May 2026. Verify the applicable rule for earlier months |
| Unknown whether an employee is an International Worker | Ask for passport and any certificate of coverage before computing |

## Rates, bands and thresholds

| Item | Rate or amount | Condition | Source |
| --- | --- | --- | --- |
| EPF coverage, Chapter III | Twenty or more employees | Establishment headcount, First Schedule | https://egazette.gov.in/WriteReadData/2020/222111.pdf |
| ESI coverage, Chapter IV | Ten or more persons | Other than a seasonal factory; one person in a notified hazardous occupation | https://egazette.gov.in/WriteReadData/2020/222111.pdf |
| Wages: excluded items above this share of all remuneration are added back | One-half (50%) | Code s 2(88), "or such other per cent. as may be notified" | https://egazette.gov.in/WriteReadData/2020/222111.pdf |
| Wages: remuneration in kind counted as wages, up to | Fifteen per cent of total wages | Code s 2(88) Explanation | https://egazette.gov.in/WriteReadData/2020/222111.pdf |
| EPF wage ceiling, Chapter III | 25,000 rupees per month | From 17 September 2026 (date of publication), superseding S.O. 2702(E) of 29 May 2026 | https://egazette.gov.in/WriteReadData/2026/276299.pdf |
| ESI coverage wage ceiling | 21,000 rupees a month, or 25,000 rupees for an employee meeting the specified disability test | From 21 November 2026, S.O. 6339(E). The proviso names the Rights of Persons with Disabilities Act, 2016 and the National Trust Act, 1999 | https://egazette.gov.in/WriteReadData/2026/278112.pdf |
| EPF employer contribution | Twelve per cent (12%) of wages | EPF Scheme 2026 paragraph 18; on wages up to the ceiling unless a joint option | https://egazette.gov.in/WriteReadData/2026/273957.pdf |
| EPF employee contribution | Equal to the employer's | Paragraph 18 | https://egazette.gov.in/WriteReadData/2026/273957.pdf |
| EPF reduced rate | Ten per cent (10%) | S.O. 3582(E) excludes specified establishments from the twelve per cent substitution, deemed effective from 21 November 2025 | https://egazette.gov.in/WriteReadData/2026/274112.pdf#page=2 |
| Code s 16(1)(a) provident fund rate | Ten per cent, with substitution of twelve per cent by notification | Apply S.O. 3582(E) for the substituted rate and excluded establishments | https://egazette.gov.in/WriteReadData/2020/222111.pdf |
| EPS: part of employer's contribution sent to the Pension Fund | Eight and thirty-three hundredths per cent (8.33%) | Of wages up to the wage ceiling, Pension Scheme 2026 paragraph 4 | https://egazette.gov.in/WriteReadData/2026/273951.pdf |
| Central Government contribution to the Pension Fund (not an employer cost) | One and sixteen hundredths per cent (1.16%) of pay | Paragraph 4 | https://egazette.gov.in/WriteReadData/2026/273951.pdf |
| EPS employer share for members with an accepted higher-wage joint option (from 1 September 2014) | Nine and forty-nine hundredths per cent (9.49%) | The increase applies to wages above fifteen thousand rupees per month | https://egazette.gov.in/WriteReadData/2026/273951.pdf |
| EDLI contribution limit in the Code | One per cent (1%) of wages, or the percentage notified by the Central Government | EDLI Scheme paragraph 5 requires the notified rate | https://egazette.gov.in/WriteReadData/2020/222111.pdf |
| EDLI employer contribution | 0.5% of wages up to the applicable ceiling | S.O. 3581(E) specifies the monthly rate with effect from 29 June 2026 | https://egazette.gov.in/WriteReadData/2026/274104.pdf#page=2 |
| Ordinary EPF administrative charge | 0.50% of applicable wages, with an establishment-wide monthly minimum | 500 rupees if there is at least one contributing member that month, or 75 rupees where there are no active contributory members. See the current EPFO employer FAQ, Q13 | https://pmvbry-cdn.epfindia.gov.in/wp-content/uploads/2025/08/Annual_Report_2023-24.pdf |
| EDLI death benefit, twelve months' continuous employment limb | Not less than 2,50,000 and not more than 7,00,000 rupees | Paid by the EPFO to the family | https://egazette.gov.in/WriteReadData/2026/273942.pdf |
| ESI employer contribution | Three and one-fourth per cent (3.25%) of wages | Rule 19(1), rounded to the next higher rupee | https://egazette.gov.in/WriteReadData/2026/272366.pdf |
| ESI employee contribution | Three-fourth per cent (0.75%) of wages | Rule 19(1). The section 2(31) exemption applies through average daily wages of 176 rupees inclusive under S.O. 6338(E) and 1950 rule 52 | https://egazette.gov.in/WriteReadData/2026/278111.pdf |
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
| Basic pay | Bonus payable under law that is outside remuneration under the terms of employment |
| Dearness allowance | Value of house accommodation, light, water, medical attendance or another excluded amenity |
| Retaining allowance, if any | Employer contribution to a pension or provident fund, and interest on it |
| Remuneration in kind, up to fifteen per cent of total wages (Explanation) | Conveyance allowance or travelling concession |
|  | Sums to defray special expenses of the job |
|  | House rent allowance |
|  | Remuneration under an award, settlement or order of a court or tribunal |
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
- Apply the ten per cent Code rate for the establishments excluded by S.O. 3582(E). They are establishments with an approved insolvency resolution or repayment plan and establishments in the jute, beedi, brick, coir other than spinning, and guar gum factory categories. Verify the establishment's actual classification. [S.O. 3582(E)](https://egazette.gov.in/WriteReadData/2026/274112.pdf#page=2)
- The ceiling is the "wage ceiling" in section 2(89) of the Code (the EDLI Scheme applies "the wage ceiling specified in clause (89) of section 2 of the Code").

### Pension share (Employees' Pension Scheme 2026, paragraph 4)

- The pension share comes out of the applicable employer contribution. The balance stays in the provident fund account.
- The pension share is on wages up to the wage ceiling. Pension Scheme paragraph 4 and the employer FAQ use 8.33%. S.O. 3580(E) specifies eight and one-third per cent. If those expressions produce different whole-rupee contributions for the actual wages, confirm the applicable figure before remittance. [S.O. 3580(E)](https://egazette.gov.in/WriteReadData/2026/274111.pdf#page=2) · [EPFO employer FAQ](https://unifiedportal-emp.epfindia.gov.in/epfo/)
- The higher pension share applies only to members who exercised the joint option under paragraph 11 of the old 1995 scheme and were found eligible. Do not read the "fifteen thousand rupees" in that rule as the general wage ceiling.
- The pension share is rounded to the nearest rupee, fifty paise up (paragraph 4(3)), and remitted within fifteen days of the close of every month, with the cost of remittance borne by the employer (paragraph 4(1)).

### EDLI (Employees' Deposit-Linked Insurance Scheme 2026)

- Only the employer pays EDLI. It may not deduct the contribution from wages or recover it from the employee (paragraph 8).
- The employer contributes 0.5% of section 2(88) wages up to the wage ceiling under paragraph 5(1). S.O. 3581(E) states 29 June 2026 as its effective date. Check the saved earlier instrument for an earlier wage month. [S.O. 3581(E)](https://egazette.gov.in/WriteReadData/2026/274104.pdf#page=2)
- Paragraph 21(4) measures the 12 months before the month of death and disregards a 60-day gap between employment spells for the qualifying service test. The assurance benefit uses the wage and balance formula or the balance-based benefit in paragraph 21(1), whichever is higher. Leave claims to the EPFO.

### Administrative charges

The ordinary employer administrative charge is 0.5% of applicable wages. Apply the minimum across the establishment for each month. The EPFO FAQ gives 500 rupees if there is a contributing member and 75 rupees if there is no active contributory member that month. Apply the higher-wage rules in paragraphs 9(4) and 19(3) where an option or voluntary contributions affect the base. Check applicable exemption-specific fees separately. [EPFO employer FAQ, Q13](https://unifiedportal-emp.epfindia.gov.in/epfo/)

### ESI (Social Security (Central) Rules 2026, rule 19)

- Each share is a sum "rounded to the next higher rupee" on the wages payable for the wage period (rule 19(1)). That is a different rounding rule from EPF.
- For an employee who is a person with disability under the Rights of Persons with Disabilities Act, 2016 and under the National Trust Act, 1999, the employer does not pay its share for up to three years from the start of the contribution period, or such period as the Central Government specifies. The Central Government reimburses the Corporation (rule 19(2) and (3)). Apply the employee-share exemption test separately.
- From 21 November 2026, S.O. 6338(E) uses 1950 rule 52 for the employee exemption. Check whether average daily wages during the wage period are 176 rupees or less. Apply the employer's share separately, including any rule 19(2) disability relief.
- The employer remits the applicable shares. Section 31(2) limits recovery from a directly employed worker to the wages of the relevant period. Section 31(8) sets the contractor's corresponding recovery limit. The employer bears its own share and the remittance costs under section 31(3) and (5).
- Wages are the Code's section 2(88) wages. The earlier wider "gross wages" list (HRA, overtime, all cash payments) does not match the Code text; see "When to refuse or refer".
- From 21 November 2026 the ESI ceiling is inclusive, at 21,000 rupees a month or 25,000 rupees for an employee within the disability proviso to S.O. 6339(E). Ministry FAQ 124 confirms contributions continue until the end of the contribution period when an existing covered employee's wages cross the ceiling during it.
- ESI regulation 5 pairs April to September contributions with January to June benefits the following year, and October to March contributions with July to December benefits. For a new employee the first contribution period starts on joining and the corresponding benefit period starts after 9 months.

### ESI benefits (paid by the Corporation, for context)

| Benefit | Rule in the Social Security (Central) Rules 2026 |
| --- | --- |
| Sickness | Normally at least 78 days of contributions payable, with a half-of-available-working-days test in the specified shorter periods. Pay 70% of the standard benefit rate rounded up. Exclude the first 2 days unless the spell follows the last paid spell within 15 days. Limit ordinary benefit to 91 days over 2 consecutive benefit periods (rule 22(1)) |
| Maternity | At least 70 contribution days payable over the preceding 2 consecutive contribution periods for confinement. Use the standard benefit rate rounded up on qualifying days without paid work. The ordinary term is 26 weeks with up to 8 before expected confinement. For 2 or more surviving children it is 12 weeks with up to 6 before expected confinement (rule 22(3)) |
| Confinement expenses | Medical bonus in the rates table, where ESI facilities are not available, for two confinements only (rule 22(4)) |
| Disablement | Full rate normally equals 90% of the standard benefit rate rounded up. For permanent partial disablement apply the loss-of-earning-capacity share. Check the pre-first-benefit-period and minimum temporary-disablement rules (rule 22(5)) |
| Dependants | For death from employment injury, the widow receives three-fifths during life until remarriage and eligible children and a widowed mother receive two-fifths each, subject to the age, dependency, sharing and full-rate limits in rule 22(6) |
| Funeral expenses | Claimants under Code section 32(1)(f) ordinarily claim within 3 months. The prescribed limit is 20,000 rupees (rule 21) |

### Edge cases

- **Establishments below 20 employees:** may be covered for EPF if the employer and a majority of employees agree (Code section 1(5)). Once a Chapter applies, it keeps applying even if numbers fall (section 1(8)).
- **Contract labour:** for EPF, paragraph 20 specifies the payment route for an independently unregistered contractor, which forwards the employee's contribution with an equal contribution for the ordinary matching case. The principal employer remains responsible under paragraph 20(4). Code section 17 covers EPF scheme recovery from contractors. ESI employer payment and contractor recovery follow Code section 31.
- **Fixed-term employees:** the Code defines fixed term employment as a written contract for a fixed period, and the worker "shall be eligible for all benefits, under any law for the time being in force, available to a permanent employee proportionately according to the period of service rendered by him" (section 2(34)). The earlier "from day one, no waiting period" is not printed on any page read; apply the same joining rules as for a permanent employee.
- **Exempted establishments (PF trust):** an establishment may be exempted under section 143 of the Code and run its own provident fund; contributions under its rules still feed the pension share (Pension Scheme paragraph 4(1)). The scheme's monthly return form for exempted PF trusts prints the contribution rate field as "Selection from 10 or 12% as applicable". The conditions of exemption were not read; refer.
- **Voluntary contributions (VPF):** an employee may opt to make an additional voluntary contribution "on wages exceeding the statutory wage ceiling at statutory rate or at any rate in excess of statutory rate", passed to the Commissioner through the Electronic Challan-cum-Return (EPF Scheme 2026, paragraph 19(1)). The employer does not have to match it (paragraph 19(2)) but pays extra administrative charges (paragraph 19(3)). Voluntary contributions may not exceed wages after the deductions allowed under section 18(2) of the Code.
- **Employees' Enrolment Campaign, 2026 and VISHWAS, 2026:** the Annexure allowed declarations through 31 October 2026 for previously unenrolled employees who joined between 1 April 2009 and 31 March 2026 and remained employed at declaration. Check the past-period employer contributions, interest, charges and inquiry rules before applying any employee-share waiver. VISHWAS, 2026 concerns defaults before 14 June 2024 and has an initial six-month term from notification, with an extension power.

## Deadlines and filing

### EPF, EPS and EDLI

| Item | Detail |
| --- | --- |
| Registration | Electronic, Form-I on the Shram Suvidha Portal; certificate within seven days of a complete application or the establishment is deemed registered (rule 5(1)); changes updated within thirty days (rule 5(6)) |
| First return | Consolidated return in Form V within fifteen days of the scheme applying to the establishment; a "Nil" return if nobody qualifies (EPF Scheme 2026, paragraph 24(1)) |
| Monthly payment | Employer and employee shares and administrative charges, within fifteen days of the close of every month (paragraph 20(1)); pension share in the same period (Pension Scheme paragraph 4(1)); EDLI contributions and charges in the same period, electronically (EDLI Scheme paragraph 6(1)) |
| Monthly return | Electronic Challan-cum-Return in Form VII and uploads of new members, transfers in and leavers within 15 days of month-end (paragraph 24(2)). EDLI paragraph 9 also requires a first return and monthly joiner and leaver details |
| Ownership return | Form VI after registration and ownership changes within 15 days (paragraph 24(2)) |
| International Workers | Monthly upload of International Workers joining, transferring in and leaving, within fifteen days of the close of each month (paragraph 24) |
| Annual return | None separate in the EPF Scheme 2026: the Form V first return and the monthly uploads are what paragraph 24 requires |

The earlier "within one month" (EPF) and "within 15 days" (ESI) registration deadlines are not printed on any page read and stay out.

### ESI

| Item | Detail |
| --- | --- |
| Who pays | The employer pays both shares, for direct and contractor employees (Code section 31(1)) |
| When due | Contributions normally fall due on the last day of the wage period under section 29(4). For part-period work or multiple employers check the regulations. Pay electronically within 15 days after the end of the calendar month in which contributions fall due, subject to the permanent closure rule (regulations 18–19) |
| Returns | File Form 2 within 15 days of month-end. File all monthly returns for the contribution period within 45 days of its end. On permanent closure pay contributions and file returns within 15 days of closure (regulations 16 and 19) |

## Penalties and interest

- EPF damages are a monthly rate on the arrears from the rates table, and may not exceed the arrears (paragraph 23(1)). The same table applies to defaults under paragraph 32-A of the 1952 scheme from 14 June 2024 (paragraph 23(2)). It replaces the earlier annual damages bands. EDLI damages follow the same table (EDLI Scheme paragraph 7(1)).
- S.O. 2357(E) sets simple interest at 12% a year under section 127 from when the amount became due until actual payment.
- ESI regulation 22 allows damages of 1% of arrears for each month of delay, capped at the contribution amount. Interest under regulation 21 is separate. The employer must have an opportunity to be heard.
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

The examples use hypothetical section 2(88) wages with no exclusions above one-half. They show EPF, EPS and ESI before employer EDLI and administration charges. In Example 1, ordinary EDLI adds 60 rupees and the employee's wages contribute 60 rupees to the establishment's percentage-based administrative charge. Apply the monthly floor to the total establishment charge.

### Example 1: Employee on 12,000 rupees a month, in both EPF and ESI

Assume November 2026, an EPS member at a 12% establishment and average daily wages above the 176 rupee ESI employee-share threshold. EPF is 12% of 12,000 = 1,440 each. EPS is 8.33% of 12,000 = 999.60, rounded to 1,000, leaving 440 in the employer's provident fund contribution. The ESI employer share is 390 and the employee share is 90. Before EDLI and charges, employer cost is 1,830 and employee deductions are 1,530. If the employer qualifies for rule 19(2) disability relief during the applicable period, the Government reimburses the Corporation's 390 and the employee share remains 90 on these facts.

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

Assume an existing EPF and EPS member at a 12% establishment who is outside ESI coverage throughout November. A new employee on 40,000 rupees is ordinarily excluded from EPF entry unless enrolled under a written joint option. For the existing member without a higher-wage option, each EPF share is 12% of 25,000 = 3,000. The pension share is 8.33% of 25,000 = 2,082.50, rounded to 2,083, leaving 917 in the provident fund. With a paragraph 9(4) written option each share is 12% of 40,000 = 4,800. The pension share stays at 2,083 absent an accepted higher-pension option, leaving 2,717 in the provident fund. The employer and employee each contribute 1,800 more a month and the employer pays the applicable higher administrative charges.

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
10. File ESI Form 2 and pay under regulations 16 and 19. For a late payment check 12% simple annual interest and the distinct EPF or ESI damages rules.

### When to refuse or refer

- A disputed S.O. 3582(E) establishment classification or a case where the Pension Scheme and notified EPS rates produce different rounded results.
- An EPF month before 29 May 2026 that needs an earlier ceiling.
- Exemption-specific fees or a contribution governed by an earlier notification that still needs checking.
- International Workers: whether the wage ceiling exclusion applies to them, totalisation and detachment under a specific agreement, and withdrawals on leaving India.
- ESI coverage at the start of a contribution period or after pay changes. Check wage components, the date the worker first qualified and the applicable ceiling.
- Exempted PF trusts (section 143), damages waivers under an insolvency plan, VISHWAS, 2026 cases, and any EPFO inquiry under section 125 or appeal.
- Benefit claims (EDLI death benefit, pension, ESI benefits): refer to the EPFO or ESIC.
- Salary TDS, gratuity and bonus: use `india-payroll`. Profession tax: use `in-professional-tax`.

### Prohibitions

- NEVER compute EPF or ESI on a component list from the old Acts: use section 2(88) wages and the one-half add-back.
- Apply the ceiling separately for each scheme and month. The Chapter III increase starts on 17 September 2026. The separate Chapter IV notice starts on 21 November 2026.
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
| S.O. 2702(E), the 15,000 rupee Chapter III wage ceiling from 29 May 2026 | https://egazette.gov.in/WriteReadData/2026/273002.pdf | 2026-11-24 |
| S.O. 6339(E), ordinary and disability ESI ceilings from 21 November 2026 | https://egazette.gov.in/WriteReadData/2026/278112.pdf | 2026-11-24 |
| S.O. 6338(E), which applies the rule 52 employee-share exemption from 21 November 2026 | https://egazette.gov.in/WriteReadData/2026/278111.pdf | 2026-11-24 |
| ESI (Central) Rules 1950, rule 52 daily wage threshold | https://www.esic.gov.in/attachments/actfile/ff565588588373dc30795058bc8aefec.pdf | 2026-11-24 |
| ESI (General) Regulations 2026, regulations 5, 16, 18–19 and 21–22 | https://egazette.gov.in/WriteReadData/2026/278125.pdf | 2026-11-24 |
| S.O. 2357(E), Code section 127 simple interest rate | https://egazette.gov.in/WriteReadData/2026/272390.pdf | 2026-11-24 |
| Ministry of Labour November 2026 FAQs 123–126, wage base, continued ESI coverage and the benefit-start gate | https://www.labour.gov.in/static/uploads/2026/11/da640b1558a315e81e22ce5ac12f463f.pdf | 2026-11-24 |
| Read for Ministry of Labour FAQ of 16 March 2026, replies 7 and 12 (wages definition from 21 November 2025, ESI limit of Rs 21,000) | https://www.labour.gov.in/static/uploads/2026/03/a4ccf4c6d97c4f1f36a6d83f8c64213d.pdf | 2026-11-14 |
| Read for the government backgrounder on the Labour Codes of 21 November 2025 (ESI opt-in below 10 employees) | https://static.pib.gov.in/WriteReadData/specificdocs/documents/2025/nov/doc20251121701501.pdf | 2026-11-14 |
| Read for the government backgrounder on the Code on Social Security of 22 November 2025 (50% add-back, 25% appeal deposit, EPF for all establishments with 20 or more) | https://static.pib.gov.in/WriteReadData/specificdocs/documents/2025/nov/doc20251122702601.pdf | 2026-11-14 |
| S.O. 3582(E), ordinary EPF rate, excluded establishments and deemed effective date, read in the original Gazette PDF | https://egazette.gov.in/WriteReadData/2026/274112.pdf#page=2 | 2026-11-24 |
| S.O. 3581(E), ordinary EDLI contribution rate and effective date, read in the original Gazette PDF | https://egazette.gov.in/WriteReadData/2026/274104.pdf#page=2 | 2026-11-24 |
| S.O. 3580(E), wording of ordinary pension contribution rate, read in the original Gazette PDF | https://egazette.gov.in/WriteReadData/2026/274111.pdf#page=2 | 2026-11-24 |
| EPFO public employer portal, September 2026 wage-ceiling FAQ Q7 and Q13, read the PDF after opening the portal | https://unifiedportal-emp.epfindia.gov.in/epfo/ | 2026-11-24 |
| EPFO employer pages (tried for the administrative charge and EDLI rate) | https://www.epfindia.gov.in/site_en/For_Employers.php | Refused (403) on 2026-11-14, not read |
| ESIC contribution page (tried for the payment due date and ESI ceiling) | https://www.esic.gov.in/contribution | Timed out on 2026-11-14, not read |

Not yet confirmed: the EPF ceiling before 29 May 2026, any earlier EDLI instrument needed for the wage month, the precise EPS rate where the published expressions affect rounding, and any exemption-specific fees or campaign extension.
