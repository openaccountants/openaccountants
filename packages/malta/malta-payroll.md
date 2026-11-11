---
name: malta-payroll
description: Use this skill whenever asked about Malta payroll processing for employed persons. Trigger on phrases like "Malta payroll", "FSS deduction", "employee SSC", "Class 1 contributions", "FS5", "FS3", "FS7", "payslip Malta", "net salary Malta", "PAYE Malta", "tax withholding Malta", "employer SSC Malta", "Maternity Trust Fund", "COLA Malta", "minimum wage Malta", "overtime Malta", "gross to net Malta", "salary calculation Malta", or any question about computing employee pay, withholding tax, or social security contributions for Malta-based employees. This skill covers FSS income tax withholding, Class 1 SSC (employee and employer), statutory bonuses, minimum wage, mandatory benefits, payslip requirements, and filing obligations. ALWAYS read this skill before processing any Malta payroll.
version: 1.2
jurisdiction: MT
tax_year: 2026
last_updated: 2026-11-08
depends_on:
  - payroll-workflow-base
category: payroll
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
tier: 2
domain: payroll
---

# Malta payroll: FSS tax withholding, Class 1 social security, Maternity Fund, statutory bonuses and FS3/FS5/FS7

## Scope ([FSS Rules, S.L. 372.14](https://legislation.mt/getpdf/6a6c4d3b52fe3f25d8b039d3))

This skill covers what a Maltese employer (a "payer") must do for employees (the "payees"): register, withhold income tax under the Final Settlement System (FSS), pay Class 1 social security and the Maternity Leave Fund contribution, pay the statutory bonuses and the minimum wage, and file the FS5, FS3 and FS7.

- **Primary year: emoluments paid in calendar 2026.** Malta taxes a calendar basis year. 2026 income is charged for **year of assessment 2027**, so the FSS rate tables for 2026 pay are the ones in article 56(1) of the Income Tax Act as replaced by Act III of 2026.
- **Returns being filed now:** the 2025 FS3 and FS7 were due in January and February 2026. See "2025 year-end (already due)".

**Source scope.** The law and the specific official pages identified in Sources were read on 4 November 2026 for this correction. Historical source-access failures are preserved in the evidence archive, not used as a present unavailability claim. Only the listed changed claims were rechecked; remaining specialist or form-layout gaps are explicitly held.

**Not covered:** the employee's own tax return, part-time final tax and personal reliefs (see the malta-income-tax skill), self-employed Class 2 contributions, fringe-benefit valuation, the special expatriate regimes (from 1 January 2026 the [Tax Treatment of Highly Skilled Individuals Rules, L.N. 20 of 2026](https://legislation.mt/eli/ln/2026/20/eng), which take over from the Highly Qualified Persons Rules and similar schemes), and sector Regulation Orders beyond what is named here.

## Ask the client first

- Is the employer registered as an FSS payer? If not, when did the first emoluments start to accrue?
- How many **full-time payees** are on the payroll? Ten or more means the cumulative formula is compulsory.
- For each employee: do you hold a completed **FS4** (Payee Status Declaration)? What status does it show: single, married (joint computation), parent, or a qualifying-child category?
- For a qualifying-child status: does the employee have custody or pay maintenance? How old is each child? Is the employee or spouse an EU/EEA national or a long-term resident? If not, was the child born in Malta and resident in Malta?
- Is this job the employee's **main** source of emoluments (FSS Main method), registered **part-time** work (part-time method), or other emoluments (Other Emoluments method)?
- Date of birth: on or before 31 December 1961, or on or after 1 January 1962? Age under 18, 17 or 18+? This drives the Class 1 category and minimum wage.
- What is the **basic** weekly wage, or the weekly equivalent of the basic monthly salary, before overtime, bonuses, allowances, benefits in kind and commissions?
- Overtime: is the post managerial? Is the basic weekly wage at or below €375 ([Tax on Overtime Rules](https://legislation.mt/getpdf/62026ae5c9c73a144cfb58eb))? Has the employee opted out of the 15% overtime method?
- Any fringe benefits, tax-free (net) pay arrangements, or payments on termination?
- Any late FS5 payments or missing forms to fix?

## The method, step by step

1. **Register as a payer** "within fifteen days from the date the first emoluments due to be paid by him to a payee start to accrue" (FSS rule 4(1)). A buyer of a going concern with employees has the same duty.
2. **Collect the FS4.** The payee must give it "within seven days from the commencement of a new source" of emoluments or of any change in its information (rule 3(1)). From 1 January 2026 the form is the one "publicly available on the appropriate website" rather than a schedule to the rules ([L.N. 176 of 2026](https://legislation.mt/getpdf/6a6c4e3652fe433f00006353)). The payer completes its parts and files the original "by the last working day of the month following that during which the said form was forwarded" (rule 3(3)).
3. **No FS4? Deduct at the top rate** ([rule 3](https://legislation.mt/getpdf/6a6c4d3b52fe3f25d8b039d3)). Emoluments of a payee who has not complied are "subject to tax deduction at a rate equal to the maximum rate of tax provided under article 56(1)" (rule 3(2)), which is 35%. The payer must still complete and file the form to the best of its knowledge (rule 3(4)).
4. **Pick the deduction method** for each payment (rule 6(1)):
   - **FSS Main** for the one source the FS4 names as main, and for local pensions (rule 7);
   - **FSS Part-Time** for part-time work that qualifies under article 90A (rule 8; rates in the malta-income-tax skill);
   - **FSS Overtime** for qualifying overtime income, at 15 cents per euro (rule 7A);
   - **FSS Other Emoluments** for anything else, at 20% ([rule 9](https://legislation.mt/getpdf/6a6c4d3b52fe3f25d8b039d3)).
5. **Compute FSS Main tax** with the cumulative formula (Schedule B Part I) using the 2026 rate table for the FS4 status. A payer with fewer than ten full-time payees may instead use the Main Tax Deduction Tables, but never both in the same year (rule 7(4)).
6. **Round** the tax: "disregard any fraction of a euro being equal to or less than fifty cents, and round up to one euro any fraction of a euro exceeding fifty cents" (rule 6(3)).
7. **Cap the deduction** ([rule 11](https://legislation.mt/getpdf/6a6c4d3b52fe3f25d8b039d3)) at 50% of the cash part of the pay, unless the payee consents or a listed exception applies (rule 11; Schedule B note). Termination payments are not capped (rule 34).
8. **Compute Class 1** on the basic weekly wage: the employee's share, the employer's matching share, and the employer's Maternity Leave Fund contribution ([Cap. 318](https://legislation.mt/getpdf/69d6033d6fe5fd3994d1710c), art. 7 and Tenth Schedule).
9. **Give the payee a pay statement** showing gross pay by category (fringe benefits separately) and the tax deducted (rule 19).
10. **Remit and file the FS5** by the last working day of the next month (rules 15 and 20).
11. **Year end:** give each payee the FS3 by 31 January, and file the FS7 with the FS3 originals by 15 February (rules 21 and 22).

Order matters. If you compute tax before splitting out qualifying overtime and part-time pay, those amounts are taxed twice. If you compute Class 1 on gross pay including bonuses and overtime, you overcharge both sides.

## FSS income tax: formula and 2026 rate tables

### The cumulative formula ([FSS Rules, Schedule B](https://legislation.mt/getpdf/6a6c4d3b52fe3f25d8b039d3))

Payers "having ten or more full-time payees" must use the FSS Main Cumulative Tax Deduction Formula. For each pay period:

| Step | Formula | Meaning |
| --- | --- | --- |
| 1 | A = (E/C) N | Projected annual emoluments: main emoluments to date (E) ÷ current pay period number (C) × pay periods in the year (N) |
| 2 | P | Projected annual tax: apply the article 56(1)(a) or (b) table for the FS4 status to A |
| 3 | D = (P/N) C | Tax due to date |
| 4 | L = D − X | Deduct this period: tax due to date less tax already deducted (X) |

If L is negative, deduct nothing that period. The deduction may not exceed 50% of the cash part of the period's pay.

**Main Tax Deduction Tables (fewer than ten full-time payees).** The tables are the ones "the Commissioner may ... declare to be applicable" in a communication, circular or on a Government website. They are not in the law, so the 2026 tables are **check** on mtca.gov.mt. A year-end adjustment is normally made in the last pay period: projected annual tax on actual year-to-date main emoluments, less tax already deducted. The payer can do this only with full information, which includes FS3s from earlier employers that year.

### Rate tables for 2026 emoluments (year of assessment 2027) ([Act III of 2026](https://legislation.mt/getpdf/69d8ed326fe5fd3994d17430))

Tax = chargeable income × rate − subtraction. Act III of 2026, article 19, replaced article 56(1)(a) and (b) from year of assessment 2027. Each band is "exceeds [lower] but is less than [upper]". Every formula meets the next one at the band edge, except the parent-one-child 35% band explained below.

| FS4 status (article 56(1)) | 0% up to | 15% band (subtract) | 25% band (subtract) | 35% over €60,000 (subtract) |
| --- | --- | --- | --- | --- |
| Single / other individual, (b)(i) | €12,000 | €12,000–€16,000 (€1,800) | €16,000–€60,000 (€3,400) | €9,400 |
| Married, joint, (a)(i) | €15,000 | €15,000–€23,000 (€2,250) | €23,000–€60,000 (€4,550) | €10,550 |
| Parent, (b)(ii) | €13,000 | €13,000–€17,500 (€1,950) | €17,500–€60,000 (€3,700) | €9,700 |
| Married, 1 qualifying child, (a)(ii) | €17,500 | €17,500–€26,500 (€2,625) | €26,500–€60,000 (€5,275) | €11,275 |
| Married, 2+ qualifying children, (a)(iii) | €22,500 | €22,500–€32,000 (€3,375) | €32,000–€60,000 (€6,575) | €12,575 |
| Parent, 1 qualifying child, (b)(iv) | €14,500 | €14,500–€21,000 (€2,175) | €21,000–€60,000 (€4,275) | €10,270 (MTCA's table shows €10,275) |
| Parent, 2+ qualifying children, (b)(v) | €18,500 | €18,500–€25,500 (€2,775) | €25,500–€60,000 (€5,325) | €11,325 |

**Parent with one qualifying child above €60,000: use €10,270, the figure in the Act.** Act III of 2026, article 19, sets the subtraction in article 56(1)(b)(iv) at **€10,270**, and the consolidated Act prints the same figure. MTCA's amended 13 April 2026 communication and its current 2026 table publish **€10,275**. The Act is the law, so compute with €10,270. Tell the employee that MTCA's table shows €10,275: the Act's figure gives €5 more tax a year at every income in this band, and €10,275 is the figure that joins the 25% and 35% bands at €60,000. Act III of 2026 was read on 8 November 2026. [Act III of 2026](https://legislation.mt/getpdf/69d8ed326fe5fd3994d17430); [Consolidated Act](https://legislation.mt/getpdf/69d8a9187da37f0580d5140c); [MTCA amended table](https://mtca.gov.mt/docs/default-source/documents/2026-tax-rates.pdf?sfvrsn=37563fb2_5).

**Who may use which status.** A payer applies the status the FS4 declares. It still helps to know the conditions, because a wrong FS4 gives the employee a year-end bill.

- **Married tables** (a): a married couple resident in Malta, taxed jointly. If either spouse elected a separate return (article 49A) or a separate computation (article 50), each uses the (b) tables. An EU/EEA national whose spouse is not resident in Malta can still use the married tables (a)(i) to (iii) if the other conditions are met and "at least ninety per cent (90%) of the couple’s world-wide income is derived from Malta".
- **Parent** (b)(ii): a parent who kept a child in custody, or paid maintenance under article 12(1)(t), for a child "not over eighteen (18) years of age, or not over twenty-three (23) years of age if receiving full-time education".
- **Qualifying-child tables** (a)(ii), (a)(iii), (b)(iv), (b)(v) need **all** of: custody (for (b)(iv) and (b)(v), custody of the individual's own child, a spouse's child, or a child of a cohabitant certified under the Cohabitation Act, or maintenance under article 12(1)(t)); the same age test; and at least one of the individual or spouse being an EU/EEA national or a long-term resident. If neither is an EU/EEA national, each child must also have been "born in Malta and was resident in Malta". If any condition fails, fall back to (a)(i) or (b)(ii).
- **Single parent with sole custody** (b)(iii) is taxed on the married table (a)(i), unless (b)(iv) or (b)(v) is better. The conditions (sole custody, child income not over €3,400, sole beneficiary of children's allowance, no maintenance from and not living with the other parent) are set out in the malta-income-tax skill.

**2026 timing.** Act III of 2026 was assented on 10 March 2026. The cumulative formula recalculates tax to date each period, so any January–February under- or over-deduction unwinds through L = D − X. How MTCA told payers to handle those months is **check**.

### Other FSS methods ([FSS Rules](https://legislation.mt/getpdf/6a6c4d3b52fe3f25d8b039d3); [Tax on Overtime Rules, S.L. 123.200](https://legislation.mt/getpdf/62026ae5c9c73a144cfb58eb))

| Method | Applies to | Deduction |
| --- | --- | --- |
| Overtime (rule 7A) | Qualifying overtime income | "fifteen cents (€0.15) of every one euro (€1)", final: not part of chargeable income, not creditable, not refundable |
| Other Emoluments (rule 9) | Second jobs and other emoluments not under rules 7 or 8 | "twenty per cent"; the payee may direct a higher rate. Pensioners and full-time students may direct nil or a lower rate; anyone else needs the Commissioner's written approval for a lower rate |
| Part-Time (rule 8) | Part-time work qualifying under article 90A and the Part-time Work Rules | Rate and cap: see malta-income-tax. A payee who expects to be under the tax threshold may direct no deduction on the FS4 |

**Qualifying overtime.** Overtime is qualifying only while "the rate of basic weekly wage for that employment does not exceed three hundred and seventy-five euro (€375) per week" **and** the post is not managerial (a director, partner or officer with managerial functions). It must be done in a full-time employment registered with Jobsplus. From year of assessment 2023 the 15% treatment covers overtime income up to the **lower** of "ten thousand euro (€10,000)" and actual qualifying hours × maxrate. Maxrate is the overtime hourly rate, capped at "twice the hourly equivalent of the basic weekly wage". The hourly equivalent is the basic weekly wage divided by forty. Overtime pay above the cap is not qualifying overtime income, so it is taxed with the other emoluments under the Main method. The payee may opt out in writing at any time (rule 7A(3)), or elect on the return to be taxed at normal rates with the 15% credited (rule 7A(6)). Each spouse's overtime is tested separately.

## Class 1 social security and the Maternity Leave Fund ([Social Security Act, Cap. 318](https://legislation.mt/getpdf/69d6033d6fe5fd3994d1710c))

**Who pays.** For every person in insurable employment "three contributions per week shall be payable ... one by the employed person, one by his employer, and one out of the Consolidated Fund" (article 7(1)). The State's share is 50% of the combined employee and employer contribution. The employer is liable in the first instance for both its own and the employee's share (article 8(1)). It recovers the employee's share only by deduction from wages paid for that contribution week (article 8(3)). It must **not** deduct its own share from the employee: doing so is an offence (article 8(2)).

**What it is charged on.** The base is the "basic weekly wage", or the weekly equivalent of the basic monthly salary. That means gross wage or salary "excluding any remuneration for overtime, any form of bonus, any extra allowances, any remuneration in kind and commissions" (article 2). A person with two insurable jobs is treated as employed in the one with the higher basic wage (article 7(1) proviso). The Tenth Schedule does not say how to turn a monthly salary into a weekly equivalent. Use the conversion MTCA prescribes (check).

**Rate and categories.** Both the employee and the employer pay 10% of the basic weekly wage, "calculated to the nearest cent", between a low-wage flat rate and a weekly maximum (Tenth Schedule, Part I). The maximum is higher for people born on or after 1 January 1962 because their pensionable income is higher.

| Category | Who | Employee | Employer |
| --- | --- | --- | --- |
| A | Under 18, basic wage at or below the Category A/B threshold | flat rate | same |
| B | 18 or over, basic wage at or below the threshold | flat rate, or 10% if eligible and elected | flat rate |
| C | Basic wage between the threshold and the Category D point (the band is higher for those born 1962 or later) | 10% of basic weekly wage | 10% of basic weekly wage |
| D | Basic wage above the Category D point | fixed maximum (higher for born 1962 or later) | same |
| E / F | Under 18 / over 18 on recognised student-worker or similar schemes | 10%, capped | 10%, capped |

**2026 Class 1 authority table, read 4 November 2026 and checked again on 8 November 2026.** Use [MTCA's 2026 table](https://mtca.gov.mt/personal-tax/fss/social-security-contribution-rates/class-1---social-security-contribution-rates/2026), not the historical 2024 amounts still printed in the consolidated Act.

| Category / birth cohort | Basic weekly wage (€) | Employee weekly rate (€) | Employer weekly rate (€) | Employer maternity rate (€)  Source |
|---|---|---|---|------|
| A, under 18 | 0.10–229.44 | 6.62 | 6.62 | 0.20  [MTCA2026](https://mtca.gov.mt/personal-tax/fss/social-security-contribution-rates/class-1---social-security-contribution-rates/2026) |
| B, 18+ | 0.10–229.44 | 22.94, subject to eligible election below | 22.94 | 0.69  [MTCA2026](https://mtca.gov.mt/personal-tax/fss/social-security-contribution-rates/class-1---social-security-contribution-rates/2026) |
| C, born by 31 December 1961 | 229.45–490.38 | 10% | 10% | 0.3%  [MTCA2026](https://mtca.gov.mt/personal-tax/fss/social-security-contribution-rates/class-1---social-security-contribution-rates/2026) |
| D, born by 31 December 1961 | 490.39 and over | 49.04 | 49.04 | 1.47  [MTCA2026](https://mtca.gov.mt/personal-tax/fss/social-security-contribution-rates/class-1---social-security-contribution-rates/2026) |
| C, born from 1 January 1962 | 229.45–559.30 | 10% | 10% | 0.3%  [MTCA2026](https://mtca.gov.mt/personal-tax/fss/social-security-contribution-rates/class-1---social-security-contribution-rates/2026) |
| D, born from 1 January 1962 | 559.31 and over | 55.93 | 55.93 | 1.68  [MTCA2026](https://mtca.gov.mt/personal-tax/fss/social-security-contribution-rates/class-1---social-security-contribution-rates/2026) |
| E, qualifying student scheme under 18 | scheme category | 10%, maximum 4.38 | 10%, maximum 4.38 | 0.3%, maximum 0.13  [MTCA2026](https://mtca.gov.mt/personal-tax/fss/social-security-contribution-rates/class-1---social-security-contribution-rates/2026) |
| F, qualifying student scheme 18+ | scheme category | 10%, maximum 7.94 | 10%, maximum 7.94 | 0.3%, maximum 0.24  [MTCA2026](https://mtca.gov.mt/personal-tax/fss/social-security-contribution-rates/class-1---social-security-contribution-rates/2026) |

The base is basic weekly wage or the weekly equivalent of basic monthly salary. Percentage contributions are rounded to cents. The statute/annual-table distinction is preserved; no claim is made that the older consolidated table itself has been replaced by these administrative figures.

**Low earners.** An employee whose basic weekly earnings are below the national minimum wage for age 18+ may elect to pay 10% of the actual basic weekly wage instead of the Category B flat rate. From 1 January 2018 this is limited to part-time employees whose part-time basic earnings do not exceed the National Minimum Wage (article 7(2)(a)). Paying less than the flat rate "may ... result in the payment of a reduced contributory benefit or contributory pension" (Tenth Schedule, Note 1). From 1 January 2022, a person with more than one part-time job and no full-time job may elect to pay on all part-time jobs up to forty hours a week.

**Change of employer mid-week.** If employment ends with one employer and starts with another in the same week, the former employer pays that week's contribution (article 7(3)).

**Maternity Leave Fund (employer only).** The employer also pays "0.3% calculated to the nearest cent of their basic weekly wage", with flat amounts at the bottom and a cap at Category D (Tenth Schedule, Part IV). The 2024-dated table caps it at "€1.60" (born 1962 or later) and "€1.27" (born 1961 or before). The 2026 authority cap is **€1.47 for a person born by 31 December 1961**, and **€1.68 for a person born from 1 January 1962**, as in the table above. Nothing is deducted from the employee for this.

**Late Class 1.** From 1 January 2026, the extra contribution for Class 1 paid late or at the wrong rate under article 116(1)(c) and (d) is replaced by interest at the article 44(2A) Income Tax Management Act rate (Act III of 2026, article 27). See the malta-income-tax skill for that rate.

## Minimum wage, cost-of-living increase and statutory bonuses

### National minimum wage from 1 January 2026 ([L.N. 289 of 2025](https://legislation.mt/getpdf/696e2f8c52ff32215ce13d7b))

| Age | Weekly minimum (normal working week) |
| --- | --- |
| 18 and over | €229.44 |
| 17 | €222.66 |
| Under 17 | €219.82 |

Part-time employees get the hourly rate of a comparable whole-time employee under the relevant Wage Regulation Order. Where no Order applies, the rate is at least the weekly minimum "divided by forty (40)". For age 18 and over that is €5.736 an hour. Where a sector Order applies, 2026 wages may not be less than its 2025 wages adjusted for the cost-of-living increase. The mandatory service supplements (after one and two years with the same employer) in the older order, S.L. 452.71, are not repeated in L.N. 289 of 2025. Check with the Department for Industrial and Employment Relations whether they still apply.

### Cost-of-living increase for 2026 ([L.N. 290 of 2025](https://legislation.mt/getpdf/696e3268cc8c701d50c97020))

From 1 January 2026, "The wages of whole-time employees shall be increased by four euro and sixty-six cents (€4.66) per week". Part-time hourly rates rise by the matching hourly amount. Where there is no comparable whole-time employee or Wage Regulation Order, the rise is one-fortieth of €4.66. The increase is part of wages. It is taxable under FSS and forms part of the basic weekly wage for Class 1. It is a different thing from the statutory bonuses and income supplements below. Those are separate lump-sum payments made on top of wages at fixed times of the year.

### Statutory bonuses ([Employment and Industrial Relations Act, Cap. 452, art. 23](https://legislation.mt/getpdf/69faf83e2eb86e24207539ec))

- **Statutory bonuses.** Every employer must pay each **whole-time** employee the statutory bonuses. They are paid "between the 15th and the 30th day of the month of June and between the 15th and 23rd day of the month of December". Each payment "shall not be less than one-half of that which the Government shall have announced in the general estimates of any particular year as payable by the Government to each of its employees during that year" (article 23(1), first proviso).
- **Income supplements** are a separate obligation. The employer "shall also pay, or cause to be paid, to each of his whole-time employees any income supplements in the amount and at the times as may be established by legal notice" (article 23(1), second proviso). Do not fold them into the bonus or into wages.
- An employee who has worked for the employer for less than a year gets a proportionate amount of "the bonus or income supplement", "made on the basis of the annual hours worked". Whole-time employees with reduced hours get a pro rata share (article 24). Part-time entitlement follows the part-time employment regulations and the sector Order (check).
- **Published DIER amounts, read 4 November 2026:** statutory bonus **€135.10** at end of June and between 15–23 December; weekly allowance **€121.16** at end of March and September. DIER gives partial bonus at €0.74 per calendar day and partial allowance at €4.66 per working week or proportion. These are distinct from the weekly COLA wage increase. [DIER official amounts](https://dier.gov.mt/en/services/employment-conditions/wages/bonus-and-weekly-allowances/).
- **About the old "COLA" figure.** An earlier version of this skill listed a tax-exempt quarterly "COLA" paid as a yearly total. That total was really the two half-yearly statutory bonuses plus the two income supplements added together, under the wrong label. The bonuses and supplements are real, separate payments. The 2026 cost-of-living increase is the weekly €4.66 above.
- For tax, bonuses and income supplements are paid by the employer and go through FSS. Whether any exemption applies is **check** with MTCA. For Class 1, bonuses and extra allowances are excluded from the basic weekly wage.
- **Payslips.** Cap. 452 and its regulations set rules on itemised pay statements (payslips), including what they must show and when they are due. We have not verified them here, so treat them as **check**. The FSS pay statement under rule 19 (gross pay by category and the tax deducted) is covered above.

## Working time and leave that affect payroll

- **Annual leave** ([Organisation of Working Time Regulations, S.L. 452.87](https://legislation.mt/getpdf/67516323b52f3e3cf890a2e0), reg. 8): "four weeks and thirty-two hours calculated on the basis of a forty-hour working week", which is 192 hours. Four weeks of it "may not be replaced by an allowance in lieu, except where the employment relationship is terminated". From 1 January 2021, a whole-time employee gets an extra day of leave for each public holiday that falls on a Saturday, Sunday or weekly rest day. The hours adjust pro rata where the 17-week average is below or above forty hours.
- **Maximum hours** (reg. 7): average working time, including overtime, "shall not exceed forty-eight hours" per seven days. The default reference period is seventeen weeks, or fifty-two weeks in manufacturing and tourism. Leave and sick leave are left out of the average.
- **Overtime premium rates** come from the applicable Regulation Order or the contract. The 2026 sector Orders were reissued as "(Conditions of Work) Regulation Order, 2026" legal notices. Check the sector's Order; no general rate was verified.
- **Maternity leave** ([Protection of Maternity (Employment) Regulations, S.L. 452.91](https://legislation.mt/getpdf/6022592fbc8272018c0edf9a), reg. 6): "eighteen weeks" uninterrupted. How pay is split between the employer, the Maternity Leave Fund and the State benefit, and the 2026 benefit rate, are **check**.
- **Sick leave, birth leave, bereavement, parental and other leave**: set by the sector Order, the contract and separate regulations. They are not restated here. Check before relying on a figure.

## Boundaries and exceptions ([FSS Rules](https://legislation.mt/getpdf/6a6c4d3b52fe3f25d8b039d3))

| Situation | Rule | Source |
| --- | --- | --- |
| No FS4 from the payee | Deduct at the article 56(1) maximum (35%) until the default ends. Payer still files the form | FSS rule 3(2), (4), (5) |
| FS4 returned as unacceptable and not corrected within fourteen days | Deduct at the maximum rate until the Commissioner directs otherwise | FSS rule 3(7) |
| Payer files an FS4 late, incomplete or wrong | Schedule C additional tax, plus liability for any under-deduction not recovered by 31 December | FSS rule 3(6) |
| Ten or more full-time payees | Cumulative formula compulsory. Fewer than ten: may opt for Tables, but not both in one year | FSS rule 7(4) |
| More than one employment | Only one source can be "main". Others go under Other Emoluments at 20% | FSS rules 7(1), 9 |
| Deduction would exceed 50% of cash pay | Limit to 50% unless the payee consents, article 71 of the Income Tax Act applies, or article 46 of the Income Tax Management Act has been applied | FSS rule 11(1) |
| Termination payment | Taxed under rule 6 and/or rule 10, with no 50% limit | FSS rule 34 |
| Employer pays the employee's tax (net pay deal) | Gross up: emoluments = net pay + tax paid | FSS rule 33 |
| Any agreement not to deduct tax | Null and void (except rule 33 arrangements) | FSS rule 36 |
| Payer failed to deduct but has paid the tax | May recover only that amount from the payee, as the Commissioner approves | FSS rule 16 |
| Over-deduction remitted | Payer repays the payee from its own funds, then sets it off on the next remittance or claims a refund | FSS rule 17 |
| Basic weekly wage over €375, or managerial post | Overtime is not qualifying. Tax it under the Main method | S.L. 123.200 rule 2 |
| Payee paid after death, or after the contract ended | Deduction rules still apply | FSS rule 12 |
| Employer tries to recover its own Class 1 share | Offence | Cap. 318 art. 8(2) |

## Worked cases (2026 emoluments) ([Act III of 2026](https://legislation.mt/getpdf/69d8ed326fe5fd3994d17430); [FSS Rules](https://legislation.mt/getpdf/6a6c4d3b52fe3f25d8b039d3))

**Case 1: single employee, cumulative formula.** Basic salary €2,500 a month, FS4 status single, twelve monthly pay periods, no other pay. Month 1: A = (2,500 / 1) × 12 = €30,000. P = 30,000 × 25% − 3,400 = €4,100. D = (4,100 / 12) × 1 = €341.67, which rounds up to **€342**. Month 2: D = (4,100 / 12) × 2 = €683.33. L = 683.33 − 342 = €341.33, which rounds down to **€341**.

**Case 2: same pay, married joint status.** P = 30,000 × 25% − 4,550 = €2,950. Month 1 D = €245.83, which rounds to **€246**. Over the year the married status saves €1,150 against single (€4,100 − €2,950).

**Case 3: no FS4.** Same €2,500 monthly pay, and the employee has not handed in an FS4. Deduct 35% = **€875**. That is under the 50% cap (€1,250), so deduct it in full. File the FS4 to the best of your knowledge anyway.

**Case 4: qualifying overtime.** Full-time, Jobsplus-registered, non-managerial employee on a basic weekly wage of €360. They work 40 overtime hours in the month at €13.50 an hour, so overtime pay is €540. Hourly equivalent of basic = 360 / 40 = €9.00, and maxrate is capped at 2 × 9 = €18.00. The €13.50 rate is within the cap, and the year's qualifying overtime is under €10,000. Deduct 15% = **€81.00** as a final tax. Report the €540 and the hours separately on the FS5 and FS3. The €540 is kept out of the Main formula.

**Case 5: Class 1 and Maternity Fund.** Employee born in 1990, basic weekly wage €400. This falls within the published 2026 post-1961 Category C band (€229.45–€559.30). Employee Class 1 = 10% × 400 = **€40.00**. Employer Class 1 = **€40.00**. Maternity Leave Fund = 0.3% × 400 = **€1.20**. The employer's weekly cost on top of wages is €41.20, and €40.00 is deducted from pay.

**Case 6: parent, one qualifying child, high earner.** Projected annual emoluments €70,000. Using the Act's €10,270, P = 70,000 × 35% − 10,270 = **€14,230**. Tell the employee that MTCA's table shows €10,275, which would give €14,225, €5 less.

**Case 7: second job.** An employee whose main job is elsewhere earns €1,000 in a month from you. Other Emoluments method: deduct 20% = **€200**, unless the employee has directed a higher rate, or (as a pensioner or full-time student) a lower one.

## When to refuse or refer

- **Refer** questions about the employee's own return, part-time final tax, personal reliefs, or whether the child conditions are met in a disputed case. Use malta-income-tax or a warranted accountant.
- **Refer** expatriate regimes (the Highly Skilled Individuals Rules, L.N. 20 of 2026, which from 1 January 2026 take over from the Highly Qualified Persons Rules; key employee schemes), cross-border workers, social security for posted workers (A1 certificates), and directors' fees. They are outside this skill.
- **Refuse to extrapolate annual caps or bonuses to another year.** The published 2026 contribution table and DIER amounts are above. Main Tax Deduction Tables, sector terms and form layouts still require the applicable official publication.
- **Refuse** to set up any arrangement not to deduct FSS tax. It is void under rule 36.
- **Refer** sector pay-rate, overtime-premium and leave questions to the applicable (Conditions of Work) Regulation Order and the Department for Industrial and Employment Relations.

## Filing and payment ([FSS Rules](https://legislation.mt/getpdf/6a6c4d3b52fe3f25d8b039d3))

| What | Who gets it | Deadline | Rule |
| --- | --- | --- | --- |
| Payer registration | Commissioner | Within fifteen days of the first emoluments starting to accrue | 4(1) |
| FS4 (Payee Status Declaration) | Payee → payer; payer files the original | Payee: within seven days of a new source or a change. Payer: last working day of the following month | 3(1), 3(3) |
| FS5 (monthly payment advice) with payment of tax deducted, including a nil advice | Commissioner | Last working day of the month after the month the emoluments were paid | 15(1), 20 |
| FS3 (Payee Statement of Earnings) | Payee (two copies) | By 31 January of the following year, or within seven days of termination | 21(1)(b) |
| FS7 (Payer's Annual Reconciliation Statement) with the original FS3s | Commissioner | By 15 February of the following year | 22(1) |
| FS7 when a payer stops paying emoluments | Commissioner | Last working day of the month after the last payment | 22(1) proviso |

The FS5 shows the number of payees and gross emoluments split into part-time, qualifying overtime and other pay. Fringe benefits are shown separately. Tax deducted is shown under each method, plus any arrears collected under rule 10. The employer pays Class 1 monthly in arrears, within the time and in the form and manner the Director determines ([Cap. 318](https://legislation.mt/getpdf/69d6033d6fe5fd3994d1710c), article 9). For article 9 the Director is the Commissioner for Tax and Customs (article 2). How Class 1 appears on the FS5 is **check**. Employers with 10 or more FS3 forms must file their end-of-year documents electronically ([MTCA, FSS reporting obligations](https://mtca.gov.mt/personal-tax/fss-system/reporting-obligations)). The FS5 form layout is **check**. The Commissioner may also direct electronic payment and filing (rules 15(2) and 23).

**Tax deducted is a debt to Government** from the last working day of the following month. Late payment carries interest under article 44(2A) of the Income Tax Management Act (rule 25(1)).

**FSS additional tax (Schedule C)**, "Subject to a maximum of €1000 for each default":

| Default | Additional tax |
| --- | --- |
| FS4 not submitted to the Commissioner as required | "€2 for every form not submitted", or €23 whenever the defaults in any one month do not exceed ten |
| Failure to register or re-register as a payer | €115 |
| Monthly payment advice (FS5) not filed on time or in the right manner | €15 |
| Annual reconciliation (FS7) with FS3 originals not filed | €200 |

The Commissioner serves a default notice. The payer must rectify and pay "within ten days", and may contest by letter within ten days. Each further notice for a continuing default doubles the additional tax, up to the cap (rule 24). The Commissioner may remit it if the default was not the payer's fault.

**Records.** Keep an up-to-date record for each payee with name, address and ID or tax number, date of payment, gross pay (fringe benefits shown separately), and tax deducted, monthly and cumulative. Keep it for the period in article 23(12) of the Income Tax Management Act (rule 18).

## 2025 year-end (already due) ([FSS Rules](https://legislation.mt/getpdf/6a6c4d3b52fe3f25d8b039d3))

- 2025 emoluments are year of assessment 2026. FSS for 2025 used the article 56 tables as set by Act IX of 2025. The four qualifying-child tables did **not** apply to 2025 pay. See the malta-income-tax skill for those tables.
- The 2025 FS3s were due to payees by **31 January 2026**. The 2025 FS7, with the FS3 originals, was due by **15 February 2026**. If either is still outstanding, file now. Schedule C additional tax (€200 for the FS7) can be doubled on each further default notice, up to €1,000.
- Employees need their FS3 to file their own returns. The employee's 2025 return date is covered in malta-income-tax.

## Completion checklist

- [ ] Payer registered, and the date checked against the fifteen-day rule
- [ ] FS4 on file for every payee, the status checked against the child and nationality conditions, and the payer's copy filed with the Commissioner
- [ ] Payees with no FS4 are taxed at 35% ([FSS rule 3](https://legislation.mt/getpdf/6a6c4d3b52fe3f25d8b039d3))
- [ ] Method chosen per payment: Main, Part-Time, Overtime or Other Emoluments
- [ ] Cumulative formula used if ten or more full-time payees; Tables (MTCA 2026, check) only if fewer and never mixed
- [ ] 2026 article 56 table applied (Act III of 2026), with the parent-one-child 35% band computed with the Act's €10,270 and the employee told that MTCA's table shows €10,275 ([Act III of 2026](https://legislation.mt/getpdf/69d8ed326fe5fd3994d17430))
- [ ] Rounding to the euro and the 50% cap applied ([FSS rules 6 and 11](https://legislation.mt/getpdf/6a6c4d3b52fe3f25d8b039d3))
- [ ] Qualifying overtime tested (€375 basic, non-managerial, €10,000 and maxrate caps) at 15% ([S.L. 123.200](https://legislation.mt/getpdf/62026ae5c9c73a144cfb58eb))
- [ ] Class 1 on basic weekly wage only, using the published 2026 MTCA category table, and the employer's share not recovered from the employee
- [ ] Maternity Leave Fund 0.3% added (2026 caps above) ([Cap. 318](https://legislation.mt/getpdf/69d6033d6fe5fd3994d1710c))
- [ ] Minimum wage (€229.44 for 18+) and the €4.66 weekly cost-of-living increase reflected ([L.N. 289 of 2025](https://legislation.mt/getpdf/696e2f8c52ff32215ce13d7b))
- [ ] June and December statutory bonuses paid within the windows, pro rata where needed, with the March/September allowances also scheduled
- [ ] Pay statement to each payee showing gross by category and tax deducted
- [ ] FS5 and payment by the last working day of the following month, including nil months
- [ ] FS3 to payees by 31 January (seven days on termination); FS7 with FS3 originals by 15 February
- [ ] Any 2025 FS3 or FS7 still outstanding has been filed

## Executable worked checks

The first check uses undisputed single rates and the statutory euro-rounding rule. The second checks current post-1961 Class 1 and employer-only maternity caps, conditional on a full contribution week and correct category.

```oa-check
name: Single payroll cumulative two months with statutory rounding
inputs:
  salary: 2500
steps:
  - annual_tax: salary * 12 * 0.25 - 3400
  - month_one: ceil(annual_tax / 12)
  - month_two: floor(annual_tax / 12 * 2 - month_one)
expected:
  annual_tax: 4100
  month_one: 342
  month_two: 341
```

```oa-check
name: Post1961 weekly salary above2026cap
inputs:
  weekly_basic: 700
steps:
  - employee: min(weekly_basic * 0.10, 55.93)
  - employer: min(weekly_basic * 0.10, 55.93)
  - maternity: min(weekly_basic * 0.003, 1.68)
  - employer_extra: employer + maternity
expected:
  employee: 55.93
  employer: 55.93
  maternity: 1.68
  employer_extra: 57.61
```

## Sources

Earlier section citations and research are preserved in the full evidence archive; the dated rows below identify this correction's actual reads.


### Correction source reads, 4 November 2026

Only the identified passages were read for this delta; historical source rows keep their prior dates and are not a blanket re-verification.

| Source and passage actually read | URL | Read on |
|---|---|---|
| DIER full and proportional bonus/allowance amounts read | https://dier.gov.mt/en/services/employment-conditions/wages/bonus-and-weekly-allowances/ | 2026-11-04 |
| MTCA parent1child top-rate figure €10,275 read (the Act's €10,270 governs) | https://mtca.gov.mt/docs/default-source/documents/2026-tax-rates.pdf?sfvrsn=37563fb2_5 | 2026-11-04 |
| ConsolidatedAct parent1child10270 read | https://legislation.mt/getpdf/69d8a9187da37f0580d5140c | 2026-11-04 |
| FSS formula, euro rounding, methods and annual forms read | https://legislation.mt/getpdf/6a6c4d3b52fe3f25d8b039d3 | 2026-11-04 |
| LN2892025 minimum wage2026 read | https://legislation.mt/getpdf/696e2f8c52ff32215ce13d7b | 2026-11-04 |

### Source reads, 8 November 2026

| Source and passage actually read | URL | Read on |
|---|---|---|
| MTCA 2026 Class 1 table (the page with no year now shows 2027) | https://mtca.gov.mt/personal-tax/fss/social-security-contribution-rates/class-1---social-security-contribution-rates/2026 | 2026-11-08 |
| Act III of 2026, article 19 (parent with one qualifying child, 35% band, subtract €10,270) and article 22 (amends article 11 of Cap. 318 only) | https://legislation.mt/getpdf/69d8ed326fe5fd3994d17430 | 2026-11-08 |
| Cap. 318, article 2 ("Director"), article 9 (Class 1 paid monthly in arrears) and article 11 (Class 2) | https://legislation.mt/getpdf/69d6033d6fe5fd3994d1710c | 2026-11-08 |
| FSS Rules, rule 11(1) (50% limit; article 71 ITA, article 46 ITMA) | https://legislation.mt/getpdf/6a6c4d3b52fe3f25d8b039d3 | 2026-11-08 |
| Cap. 452, article 23(1) and its first proviso (bonus payment windows, one-half rule) | https://legislation.mt/getpdf/69faf83e2eb86e24207539ec | 2026-11-08 |
| MTCA FSS reporting obligations (10 or more FS3 forms: electronic filing) | https://mtca.gov.mt/personal-tax/fss-system/reporting-obligations | 2026-11-08 |
| L.N. 20 of 2026, Tax Treatment of Highly Skilled Individuals Rules, rules 1 and 12 (in force 1 January 2026; transition from the Highly Qualified Persons Rules) | https://legislation.mt/eli/ln/2026/20/eng | 2026-11-08 |

Correction ledger and complete old-topic destinations: [personal-malta-payroll](../../evidence/malta-deep-audit-20261104/ledgers/personal-malta-payroll.md). Full original research is archived there; this correction is not professional attestation.

Not yet confirmed: unresolved branches explicitly marked HOLD or check in this Guide; see the correction ledger and personal audit for the exact remaining scope. No whole-pack professional review is claimed.
