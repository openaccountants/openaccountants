---
name: cyprus-payroll
description: Use this skill whenever asked about Cyprus payroll processing for employed persons. Trigger on phrases like "Cyprus payroll", "PAYE Cyprus", "TD7", "TD63", "TD59", "TD1 Cyprus", "Social Insurance Cyprus", "GESY", "GHS contribution", "Cyprus payslip", "net salary Cyprus", "tax withholding Cyprus", "employer social cost Cyprus", "Redundancy Fund", "HRDA", "Social Cohesion Fund", "Central Holiday Fund", "insurable earnings ceiling Cyprus", "minimum wage Cyprus", "ERGANI", "50% expat exemption Cyprus", "20% new-resident exemption", "TAX FOR ALL", "TFA", "gross to net Cyprus", "salary calculation Cyprus", or any question about computing employee pay, withholding income tax, or social contributions for Cyprus-based employees. This skill covers PAYE income tax withholding, Social Insurance (employee and employer), General Healthcare System (GHS/GESY), the employer-only Redundancy / HRDA / Social Cohesion / Central Holiday funds, the new-resident 20% and 50% income-tax exemptions, minimum wage, and filing obligations. ALWAYS read this skill before processing any Cyprus payroll.
version: 0.1
jurisdiction: CY
tax_year: 2026
last_updated: 2026-10-02
authored_by: Michael Cutajar and the OpenAccountants team
review_status: pending_review
trust_label: Built by Michael Cutajar and the OpenAccountants team
depends_on:
  - payroll-workflow-base
category: payroll
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Cyprus payroll: PAYE withholding, contributions and employer filings

This Guide covers running payroll for employees in Cyprus: income tax withheld under PAYE, the employee and employer contributions an employer deducts or pays, the new-resident income tax exemptions as they affect withholding, the minimum wage, and the employer's returns and deadlines. Figures are for tax year 2026. The Cyprus tax year is the calendar year. It is a source-cited draft: every figure below sits in a table that links the official page it comes from. Full contribution rules (self-employed, voluntary contributors, late-payment charges, the Central Holiday Fund) are in the Guide `cyprus-social-contributions`. The employee's own return and personal deductions are in `cyprus-income-tax`.

## Section 1: Quick reference

| Field | Value |
| --- | --- |
| Country | Cyprus (Republic of Cyprus) |
| Currency | EUR |
| Tax year | Calendar year (1 January to 31 December) |
| Withholding system | PAYE: the employer computes the year's tax from the employee's T.D.59 declaration and withholds it monthly or weekly |
| Tax authority | Tax Department (Τμήμα Φορολογίας), Ministry of Finance |
| Social insurance authority | Social Insurance Services, Ministry of Labour and Social Insurance |
| Health system | General Healthcare System (GHS / ΓεΣΥ), run by the Health Insurance Organisation |
| Hire notification | ERGANI system (ergani.mlsi.gov.cy) |
| Key law | Income Tax Law N.118(I)/2002 (article 8 exemptions); Assessment and Collection of Taxes Law 4/1978 (late payment) |
| Filing portal | Tax For All (TFA) for all employer PAYE returns and payments |

## Section 2: Income tax withholding (PAYE)

Each employee completes and signs form T.D.59A every year and gives it to the employer. A company director, or anyone involved in managing a company, counts as an employee for this purpose. The form tells the employer about income from other sources and the deductions and exemptions the employee claims, so the employer can compute the year's tax and withhold it each month. If the employee does not hand in a T.D.59A, the employer allows no deduction other than the contributions it already knows about (lines B7 and B8 of the form). The employer still withholds; it simply grants no other allowances.

The 2026 scale applies to each employee's chargeable income. The T.D.59A prints a single scale; it has no separate scale for married people or parents.

| Item | Value | Note (verbatim) |
| --- | --- | --- |
| Source | all figures below | https://www.gov.cy/media/sites/167/2026/05/FAQs-110526.pdf |
| 0% band, chargeable income up to | EUR 22,000 | "0% από €0 μέχρι €22.000" |
| 20% band | EUR 22,001 to EUR 32,000 | "20% από €22.001 μέχρι €32.000" |
| 25% band | EUR 32,001 to EUR 42,000 | "25% από €32.001 μέχρι €42.000" |
| 30% band | EUR 42,001 to EUR 72,000 | "30% από €42.001 μέχρι €72.000" |
| 35% band | from EUR 72,001 | "35% από €72.001 και άνω" |
| Rate on the first band | 0% | "0% από €0 μέχρι €22.000" |
| Rates on the higher bands | 20%, 25%, 30%, 35% | as quoted in the rows above |
| Tax-free band before 2026 | EUR 19,500 | "έχει αυξηθεί από €19.500 σε €22.000 με εφαρμογή από το φορολογικό έτος 2026" |

The same bands are printed in Part C of the 2026 form (table below). Do not use the old EUR 19,500 band for any 2026 pay period.

| Item | Value | Note (verbatim) |
| --- | --- | --- |
| Source | all figures below | https://www.gov.cy/media/sites/167/2026/02/IR59_2026_English__.pdf |
| GHS withheld by the employer from the employee | 2.65% | "you must withhold 2.65% G.H.S." |
| GHS: stop withholding once the year's income on lines A1, A2, A9 and A10 passes | EUR 180,000 | "exceeds the amount of €180.000, stop withholding" |
| First-employment deduction: 20% option, cap per year | EUR 8,550 | "20% of your emoluments from any employment with a maximum of €8.550" |
| First-employment deduction: 50% option under circular 2017/4, salary must exceed | EUR 100,000 | "50% of your emoluments from any employment provided that your salary exceeds €100.000" |
| First-employment deduction: 50% option under circulars 2022/10 and 2024/04, salary must exceed | EUR 55,000 | "provided that your salary exceeds €55.000 in the tax year" |
| Overall cap on life insurance, approved medical fund, GHS, pension, provident and social insurance contributions | 1/5 of the intermediary calculation B6 | "must not exceed one fifth of your taxable income (i.e.1/5th of the intermediary calculation Β6)" |
| Child deduction: first, second, third and each further child (subject to income criteria; doubled for single-parent families) | EUR 1,000; EUR 1,250; EUR 1,500 | "A deduction of €1.000 is granted for the first child, €1.250 for the second child and €1.500 for the third" |
| Rent or housing-loan interest on the main residence, per spouse, civil partner or single person, under income criteria | up to EUR 2,000 | "a deduction of a) up to €2.000, under conditions, is granted to each spouse, civil partner or single person" |
| Energy upgrade of the main residence or electric vehicle, per spouse, civil partner or single person, under income criteria | up to EUR 1,000 | "b) up to €1.000, under conditions, to each spouse or civil partner or single person" |
| Home insurance for natural disasters | up to EUR 500 | "Home Insurance for natural disasters (up to €500)" |

How the form turns the declaration into monthly withholding:

- The employer fills in the second column of the form, applies the limits in the notes, and computes chargeable income (A8 less total allowances B15) and the tax on it (C1).
- The employer withholds only the share of that tax that relates to the salary it pays (and, if the employee authorises it, a Social Insurance pension). The form's formula is C1 multiplied by (A1 + A2 + A3) and divided by A6. The employer must NOT withhold tax on income from other sources, such as rent. The employee pays that tax separately through a temporary (provisional) declaration.
- Monthly withholding is the year's tax (C2) divided by 13 or by 12, "accordingly". Divide by 13 where the employee is paid a thirteenth salary (the form says only "÷13 or ÷12 accordingly"; this reading is the Guide's). Weekly withholding is C2 divided by 52.
- Tax on bonuses, "as well as other income not paid on an ad hoc basis" (the form's own words), is withheld in the month the amount is paid (note 16).
- The new 2026 personal deductions (children, housing, energy upgrade) are declared on the T.D.59 as a final amount per category. The employee does not state income criteria or the number of children on it. These deductions are NOT counted inside the one-fifth cap (Tax Department FAQ, questions 10 and 11, linked in Sources).
- Where a person works for two or more employers, each employer withholds on its own pay, using the employee's total income as declared on the T.D.59 given to that employer (PAYE FAQ, linked in Sources).

Benefits in kind (cash or non-cash benefits an employer gives an employee, or a partner or shareholder, as extra reward for work) are taxable income and are valued at market value. The Tax Department's benefits-in-kind leaflet sets the valuation methods: https://www.gov.cy/mof-tax/documents/paroches-se-eidos/

## Section 3: Contributions the employer withholds from the employee

The employer deducts the employee's social insurance and GHS contributions from pay and pays them over with its own share. The rates payroll needs are below; for everything else on contributions, use `cyprus-social-contributions`.

| Item | Value | Note (verbatim) |
| --- | --- | --- |
| Source | all figures below | https://www.businessincyprus.gov.cy/social-insurance-registration-and-contributions/ |
| Social insurance, employee share | 8.8% | "proportion of 8.8%, 8.8% and 5.2%, respectively" |
| Social insurance, employer share | 8.8% | "proportion of 8.8%, 8.8% and 5.2%, respectively" |
| Social insurance, state share (paid by the state, not by the employer) | 5.2% | "proportion of 8.8%, 8.8% and 5.2%, respectively" |
| Combined rate on insurable earnings (employee, employer and state together) | 22.8% | "Employees must contribute 22.8% on their insurable earnings" |
| Redundancy Fund (employer only) | 1.2% | "employers must contribute 1.2% to the Redundancy Fund" |
| Human Resources Development Fund (employer only) | 0.5% | "0.5% to the Human Resources Development Fund" |
| Social Cohesion Fund (employer only) | 2% | "2% to the Social Cohesion Fund for their employees" |

Do not tell an employer that social insurance costs it 22.8%. That is the combined rate. The employer's own share is 8.8%, and the employee's 8.8% is deducted from pay.

The ceiling on insurable earnings for 2026:

| Item | Value | Note (verbatim) |
| --- | --- | --- |
| Source | all figures below | https://sisweb.mlsi.gov.cy/anotato2025/ |
| Maximum insurable earnings, monthly-paid employees, from 1 January 2026 | EUR 5,742 | "€5.742 από 1/1/2026" |
| Maximum insurable earnings, weekly-paid employees, from 5 January 2026 | EUR 1,325 | "€1.325 από 5/1/2026" |

The ceiling applies to contributions to the Social Insurance Fund, the Annual Paid Leave (Central Holiday) Fund, the Redundancy Fund and the Human Resource Development levy. Those are the four funds the Social Insurance Services notice names. The Social Cohesion Fund is not among them: the Social Insurance Services page on contributions says that for the Social Cohesion Fund "the total earnings are taken into consideration without a maximum amount" (https://www.mlsi.gov.cy/mlsi/sdg/sdg.nsf/All/EA4F396F80C4BAA8C22586A10042659F?OpenDocument) (page last updated 23 March 2021). The notice states a monthly and a weekly ceiling only; it prints no annual ceiling, and this Guide does not compute one.

GHS is withheld at the rate in the T.D.59A table in Section 2, on the employee's income from this employer, until the year's income on lines A1, A2, A9 and A10 passes the GHS limit in that table. From the following month the employer stops withholding GHS on lines A2, A9a and A10a (form note 22). The GHS limit applies to all of a person's income added together; the employee may also have GHS withheld elsewhere.

## Section 4: Contributions the employer pays

| Item | Value | Note (verbatim) |
| --- | --- | --- |
| Source | all figures below | https://www.gesy.org.cy/sites/Sites?d=Desktop&locale=en_US&lookuphost=/en-us/&lookuppage=hiofinancing |
| GHS, employers (including the state as an employer), on the salaries of every person employed, full implementation from 1 March 2020 | 2.90% | "Employers (Including the State as an Employer) 1,85% 2,90% On the salaries of every person employed by them" |
| GHS, employees, full implementation | 2.65% | "Employees (Public and Private Sector) 1,70% 2,65% On their salaries" |
| Maximum annual amount on which GHS contributions are paid, per natural person | EUR 180,000 | "the total maximum annual amount on which contributions will be paid is € 180,000" |

The Health Insurance Organisation page prints the rates in the column headed "Full Implementation (As of 1/3/2020)". The 2026 T.D.59A form confirms the employee rate is unchanged. No 2026 page found prints the employer rate; see `changes.md` section 6.

Employer contributions, all paid on top of gross pay:

- Social insurance employer share, Redundancy Fund and Human Resources Development Fund: on insurable earnings up to the monthly or weekly ceiling (rates in the Section 3 table).
- Social Cohesion Fund: on total earnings, with no maximum (rate in the Section 3 table).
- GHS employer share: on salary, within the per-person GHS limit (table above).
- Central Holiday Fund (annual leave): the employer must contribute unless it holds an exemption from the Central Holiday Fund (businessincyprus.gov.cy page, Section 3 table). The rate depends on the employee's annual leave entitlement. See `cyprus-social-contributions` before adding it to a cost.

The employer pays all of these funds by the end of the calendar month after the month the contributions are for (businessincyprus.gov.cy page above).

## Section 5: Minimum wage and hiring

| Item | Value | Note (verbatim) |
| --- | --- | --- |
| Source | all figures below | https://www.gov.cy/ergasia-kai-koinonikes-asfaliseis/dilosi-tou-ypourgou-ergasias-kai-koinonikon-asfaliseon-gia-tin-afxisi-tou-ethnikou-katotatou-misthou/ |
| Monthly minimum wage, full-time, after six months' continuous employment, from 1 January 2026 | EUR 1,088 | "μετά από την συμπλήρωση έξι μηνών συνεχούς απασχόλησης αυξάνεται από τα €1.000 στα €1.088" |
| Monthly minimum wage, full-time, before six months' continuous employment, from 1 January 2026 | EUR 979 | "πριν από την συμπλήρωση έξι μηνών συνεχούς απασχόλησης αυξάνεται από τα €900 στα €979" |

The source is a gov.cy press release (Ανακοινωθέν) of the Ministry of Labour and the Council of Ministers Secretariat dated 27 December 2025. It reports the Council of Ministers' decision of 23 December 2025 to issue the Amending Minimum Wage Order of 2025 and says the new levels apply from 1 January 2026. The Order itself was not found on an allowed page. The businessincyprus.gov.cy page still prints the earlier EUR 1,000 and EUR 900 levels; do not use them for 2026 pay.

Hiring steps:

| Step | Detail | Authority |
| --- | --- | --- |
| Register with the Tax Department as an employer | Form "Registration/Deregistration as an Employer", sent as a new message through the TFA portal (topic "Tax Registry", "Registration") by a taxpayer who has a TIN and must register as an employer | Tax Department: https://www.gov.cy/mof-tax/en/documents/registration-deregistration-as-an-employer/ |
| Register with Social Insurance Services | The employer must register in the Register of Employers before recruiting personnel, using the YKA form 01-001 at the local District Social Insurance Office; it receives an employer registration number | https://www.businessincyprus.gov.cy/social-insurance-registration-and-contributions/ |
| Notify each new hire | No later than one day before recruitment, only electronically through ERGANI | https://www.businessincyprus.gov.cy/social-insurance-registration-and-contributions/ |
| Employee TIN | Mandatory for every employee on every monthly PAYE return from 2025 onward | PAYE FAQ: https://www.gov.cy/mof-tax/documents/ypovoli-diloseon-t-f-7/dilosi-parakratisis-f-e-kai-eisforon-paye/sychnes-erotiseis-diloseon-parakratisis-f-e-kai-eisforon-paye/ |

If an employee has no TIN, the employer finds or checks it with the Tax Department's employee registration check tool. For a person who never registered and with whom the employer has lost contact, the employer sends a TFA message attaching the ERGANI terms of employment and termination (https://www.gov.cy/mof-tax/documents/ypovoli-diloseon-t-f-7/dilosi-parakratisis-f-e-kai-eisforon-paye/pos-energo-se-periptoseis-poy-gia-opoiodipote-logo-den-echo-to-aft-kapoioy-ypalliloy/).

## Section 6: New-resident income tax exemptions

These exemptions reduce income tax only. GHS is withheld on the income lines of Part A of the T.D.59A, not on income after the Part B deductions (form note 22), and social insurance is charged on insurable earnings. Apply an exemption in payroll only when the employee has given the employer evidence of every condition.

The T.D.59A for 2026 (note 7, line B2) lets an employee in first employment in Cyprus claim EITHER the 20% deduction OR one of the two 50% deductions, not more than one. The amounts are in the T.D.59A table in Section 2.

### 20% exemption: articles 8(21) and 8(21A)

| Item | Value | Note (verbatim) |
| --- | --- | --- |
| Source | all figures below | https://www.gov.cy/media/sites/167/2026/01/implementation-of-sections-21-and-21A-of-article-8-24072023.pdf |
| Exemption rate, both articles | 20% | "20% exemption of the remuneration from the first" |
| Who, article 8(21A) | A person who, for 3 consecutive years immediately before starting his first employment in Cyprus, was employed outside Cyprus by an employer not resident in Cyprus; the exemption is on the remuneration from that first employment | "immediately before the commencement of his first employment in the Republic" |
| When, article 8(21A) | Employment starting between 26 July 2022 and 31 December 2027 | "Between 26/7/2022 (Law N.121(I)/2022) and 31/12/2027" |
| Who and when, article 8(21) | First employment in Cyprus, starting up to 25 July 2022, by a person not resident in Cyprus in the year before the year employment started | "Until 25/7/2022" |
| Period | 8(21A): 7 years from the year after employment starts, or until the first employment ends if earlier. 8(21): 5 years from the year after employment starts | "7 years (starting from the" |
| Minimum pay | None under either article | "No minimum remuneration required" |

Both articles apply whether or not the person becomes Cyprus tax resident after starting work. Article 8(21A) has no transitional provisions. The yearly cap is the EUR 8,550 in the T.D.59A table in Section 2.

### 50% exemption: articles 8(23) and 8(23A)

| Item | Value | Note (verbatim) |
| --- | --- | --- |
| Source | all figures below | https://www.gov.cy/media/sites/167/2026/06/%CE%A0%CE%AF%CE%BD%CE%B1%CE%BA%CE%B1%CF%82-%CE%B1%CF%80%CE%B1%CE%BB%CE%BB%CE%B1%CE%B3%CF%8E%CE%BD-823-%CE%BA%CE%B1%CE%B9-823%CE%91.pdf |
| Exemption rate | 50% | "50% απαλλαγή της αμοιβής από 50% απαλλαγή της αμοιβής από την" |
| Minimum pay: 8(23); 8(23A) | more than EUR 100,000; more than EUR 55,000 | "Ελάχιστη αμοιβή > €100.000 > €55.000 > €55.000" |
| Period | 10 years under 8(23); 17 years under 8(23A) (first-employment limb: or until the first employment ends, if earlier) | "Περίοδος απαλλαγής 10 έτη 17 έτη" |
| Non-residence before: 8(23) | not resident in 3 of the last 5 years, and not resident in the year before the year employment started | "3 από τα τελευταία 5 έτη" |
| Non-residence before: 8(23A) first employment (Law N.121(I)/2022) | at least 10 years before the year of first employment | "Τουλάχιστο 10 έτη πριν το έτος έναρξης της" |
| Non-residence before: 8(23A) after 15 years without salaried work in Cyprus (Law N.51(I)/2023) | at least 15 years before the year of first employment | "Τουλάχιστο 15 έτη πριν το έτος έναρξης της" |
| Which article by start date | 8(23): employment 1 January 2012 to 25 July 2022 (the table ticks all three columns for starts from 1 January 2022 to 25 July 2022). 8(23A) first-employment limb (Law N.121(I)/2022, at least 10 years non-resident): starts from 1 January 2022 to 29 June 2023 only. 8(23A) Law N.51(I)/2023 limb (15 consecutive tax years without salaried work in Cyprus): starts from 1 January 2022; for employment starting on or after 30 June 2023 it is the ONLY 8(23A) limb, so every 2024, 2025 and 2026 starter is tested at 15 years, never 10. | "Εργοδότηση από ✓ 01.01.2012 - 31.12.2021" |

Under the Law N.51(I)/2023 limb, a person is treated as starting first employment in Cyprus when, for the first time after 15 consecutive tax years without any salaried work in Cyprus, they start salaried work for a resident or non-resident employer. All of these exemptions apply whether or not the person becomes Cyprus tax resident. The minimum pay is a cliff: in a year when pay does not exceed it, no 50% exemption is given for that year under the form's wording ("provided that your salary exceeds").

### 25% exemption: article 8(21B)

| Item | Value | Note (verbatim) |
| --- | --- | --- |
| Source | all figures below | https://www.gov.cy/media/sites/167/2026/06/Article-8-21B-of-the-Income-Tax-Law-N.118-I-2002.pdf |
| Exemption rate, on remuneration from employment in Cyprus or profits of a business in Cyprus | 25% | "can claim an income tax exemption of 25% on- a. his/her remuneration" |
| Gross earnings must exceed, in the relevant year | EUR 30,000 | "has gross earnings exceeding €30.000 in the relevant year" |
| Maximum exemption per tax year | EUR 25,000 | "The exemption cannot exceed €25.000 in a tax year" |

The person must meet ALL of these conditions: (a) not Cyprus tax resident during the seven years before the year employment or business started (the page shows "(2019-2025)" as the example); AND (b) Cyprus tax resident in some year before those seven years; AND (c) remuneration or profits in Cyprus above the earnings threshold in the table during the first 12 months; AND (d) took up the employment or business between 1 January 2025 and 31 December 2030; AND (e) at the start, EITHER holds a recognised university degree and worked full-time abroad for a foreign employer for at least 36 of the previous 84 months, OR worked full-time abroad for a foreign employer for at least 84 months. It runs for seven consecutive tax years from the start year, but only in years when earnings exceed the threshold (a cliff for that year, not a taper) and, apart from the start year, only in years the person is Cyprus tax resident.

The T.D.59A for 2026 does not list this exemption at line B2: note 7 names only the 20% and the two 50% options. The Tax Department pages read for this Guide do not say whether an employer may apply the 25% exemption through PAYE. Do not apply it in payroll without an accountant's confirmation; the employee can claim it on the annual return.

## Section 7: Conservative defaults

When inputs are missing or unclear, apply these and flag them:

1. Use the 2026 scale (Section 2) for every pay period in 2026. Never the old EUR 19,500 band.
2. No T.D.59A: withhold, allowing only the social insurance and GHS contributions you deduct (form note 15). Do not refuse to run payroll.
3. Deduct the employee's social insurance and GHS before computing tax, within the one-fifth cap.
4. No exemption unless documented. Never apply the 25% article 8(21B) exemption through payroll without an accountant's confirmation.
5. Employer cost: social insurance, Redundancy and Human Resources Development on insurable earnings up to the ceiling; Social Cohesion on total earnings; GHS employer share on salary. Treat the Central Holiday Fund as unknown until the employer confirms whether it holds an exemption, and say so.
6. A thirteenth salary: divide the year's tax by 13 (the form says only "÷13 or ÷12 accordingly"; this reading is the Guide's), and report the thirteenth salary in the month it is paid.

## Section 8: Required inputs and refusal catalogue

### Required inputs

| Input | Why needed |
| --- | --- |
| Pay period, pay date and frequency (monthly or weekly) | Selects the 2026 scale and the monthly or weekly ceiling |
| Gross pay for the period and expected pay for the year, including any thirteenth salary, bonus or benefit in kind | Base for withholding and contributions |
| Signed T.D.59A for 2026 | Deductions, exemptions and other income; without it only known contributions are allowed |
| Employee TIN | Mandatory on monthly PAYE returns from 2025 |
| Social insurance number | Required on the T.D.59A and for contributions |
| Pay and amounts withheld so far this year | To check the GHS limit and correct withholding |
| Whether the employer holds a Central Holiday Fund exemption | Employer cost |
| Evidence for any new-resident exemption | Required before applying it |

### Refusal catalogue (stop and ask)

- No TIN for the employee: do not file the monthly return without it; use the Tax Department process in Section 5.
- Exemption claimed with no evidence: do not apply it; withhold without it.
- 25% article 8(21B) exemption to be applied through payroll: refer to an accountant.
- Pay date or year unknown: ask; the scale and ceilings depend on it.
- Central Holiday Fund status unknown: flag it; do not silently include or exclude it.
- Self-employed person: out of scope; use `cyprus-income-tax` and `cyprus-social-contributions`.

## Section 9: Transaction and payment pattern library

Cyprus bank statement lines mix Greek and English.

### Salary credits (employee side)

| Pattern (statement text) | Classification |
| --- | --- |
| MISTHOS, ΜΙΣΘΟΣ, SALARY, PAYROLL | Net salary payment |
| EMPLOYER [name] TRANSFER, WAGES | Net salary payment |
| BONUS, 13TH SALARY, ΔΩΡΟ (gift or 13th) | Bonus or thirteenth salary (taxable) |
| SI REFUND, GESY REFUND | Contribution adjustment, not income |

### Employer debits (employer side)

| Pattern (statement text) | Classification |
| --- | --- |
| TAX DEPARTMENT, TFA PAYMENT, PAYE | Income tax and contributions paid through TFA after the monthly return |
| ΚΟΙΝΩΝΙΚΕΣ ΑΣΦΑΛΙΣΕΙΣ, SOCIAL INSURANCE, SIS | Social insurance and employer-only funds |
| GESY, GHS CONTRIBUTION, ΓΕΣΥ | General Healthcare System contributions |
| REDUNDANCY FUND, HRDA, COHESION FUND | Employer-only funds (usually paid with social insurance) |
| CENTRAL HOLIDAY FUND, ΚΕΝΤΡΙΚΟ ΤΑΜΕΙΟ ΑΔΕΙΩΝ | Central Holiday Fund (only if not exempt) |
| NET WAGES, SALARY RUN, PAYROLL BATCH | Salary payments to employees |

Confirm the actual split with the employer's payment records.

## Section 10: Worked examples (hypothetical)

These examples are hypothetical. They use the 2026 rates in the tables above, a monthly-paid employee, 12 salary payments, no thirteenth salary, no other income, no exemption and no deduction other than the employee's contributions.

### Example A: EUR 2,500 a month (EUR 30,000 a year)

| Step | Amount | Basis |
| --- | --- | --- |
| Source | all figures below | https://www.gov.cy/media/sites/167/2026/02/IR59_2026_English__.pdf |
| Annual gross pay (hypothetical) | EUR 30,000 | assumption: EUR 2,500 x 12 |
| Employee social insurance, 8.8% (monthly pay is below the EUR 5,742 ceiling) | EUR 2,640.00 | Section 3 tables |
| Employee GHS, 2.65% | EUR 795.00 | T.D.59A table, Section 2 |
| One-fifth cap check | allowed in full | the two contributions are well below one fifth of the income (form note 10) |
| Chargeable income | EUR 26,565.00 | gross less the two contributions |
| Annual tax: 0% up to EUR 22,000, then 20% on the excess | EUR 913.00 | 2026 scale, Section 2 |
| Monthly income tax withheld (annual tax divided by 12) | EUR 76.08 | form Part C line 3 |
| Monthly social insurance, employee (and the same amount from the employer) | EUR 220.00 | 8.8% of EUR 2,500 |
| Monthly GHS, employee | EUR 66.25 | 2.65% of EUR 2,500 |
| Monthly net pay | EUR 2,137.67 | EUR 2,500 less the three deductions above |
| Employer: social insurance per month | EUR 220.00 | 8.8% of EUR 2,500 |
| Employer: Redundancy Fund per month | EUR 30.00 | 1.2% of EUR 2,500 |
| Employer: Human Resources Development Fund per month | EUR 12.50 | 0.5% of EUR 2,500 |
| Employer: Social Cohesion Fund per month | EUR 50.00 | 2% of EUR 2,500 |
| Employer: GHS share per month | EUR 72.50 | 2.90% of EUR 2,500 (Section 4 table) |

The employer's figures are on top of the EUR 2,500 and exclude any Central Holiday Fund contribution.

### Example B: EUR 7,000 a month, above the social insurance ceiling

| Step | Amount | Basis |
| --- | --- | --- |
| Source | all figures below | https://sisweb.mlsi.gov.cy/anotato2025/ |
| Monthly gross pay (hypothetical) | EUR 7,000 | assumption |
| Employee social insurance | EUR 505.30 | 8.8% of the EUR 5,742 ceiling, not of EUR 7,000 |
| Employer social insurance | EUR 505.30 | same base |
| Redundancy Fund | EUR 68.90 | 1.2% of the ceiling |
| Human Resources Development Fund | EUR 28.71 | 0.5% of the ceiling |
| Social Cohesion Fund | EUR 140.00 | 2% of the full EUR 7,000 (no maximum) |
| Employee GHS | EUR 185.50 | 2.65% of the full EUR 7,000 |
| Employer GHS | EUR 203.00 | 2.90% of the full EUR 7,000 |

Income tax for Example B follows the same method as Example A; compute it from the scale and the employee's T.D.59A.

## Section 11: Deterministic rules

- Each employee gives the employer a signed T.D.59A every year; without it the employer allows only the contributions it knows about (form note 15).
- Monthly withholding is the year's tax divided by 13 or 12, accordingly; weekly is divided by 52 (form Part C).
- Tax on bonuses, "as well as other income not paid on an ad hoc basis" (the form's own words), is withheld in the month the amount is paid (note 16). A thirteenth salary is reported in the month it is paid (PAYE FAQ).
- The employer withholds no tax on the employee's non-employment income (form note 21).
- Social insurance, Redundancy Fund and Human Resources Development Fund stop at the monthly or weekly ceiling; the Social Cohesion Fund has no maximum.
- Once the year's income on lines A1, A2, A9 and A10 passes the GHS limit, the employer can stop withholding GHS for the following months on income from lines A2, A9a and A10a (form note 22).
- Monthly PAYE returns are mandatory from 1 January 2025, filed and paid only through TFA, and each must list every employee's TIN and amounts withheld separately (PAYE FAQ; T.D.7 page).

## Section 12: Judgement catalogue (refer to an accountant)

| Topic | Judgement call |
| --- | --- |
| Central Holiday Fund | Whether the employer holds an exemption, and the rate for the employee's leave entitlement |
| Choice of new-resident exemption | Which of the 20%, 50% or 25% exemptions applies, and whether the 25% can go through payroll |
| Benefits in kind | Valuation under the Tax Department leaflet |
| Employee insured in another EU or EEA state | Whether Cyprus social insurance and GHS apply (A1 form) |
| Two employers or a pension alongside salary | How each employer splits withholding based on the T.D.59A |
| GHS limit across income sources | Income from other sources counts toward the same per-person limit |

## Section 13: Excel working paper template

One row per employee per month:

| Column | Formula or source |
| --- | --- |
| A. Employee name | input |
| B. Employee TIN | input (mandatory on the monthly return) |
| C. Social insurance number | input |
| D. Pay date and period | input |
| E. Gross pay for the month | input |
| F. Insurable earnings | = MIN(E, monthly ceiling from Section 3) |
| G. Employee social insurance | = F × employee rate (Section 3) |
| H. Employee GHS | = E × employee GHS rate, until the GHS limit is reached |
| I. Annual tax (from T.D.59A Part C) | scale in Section 2 applied to chargeable income |
| J. Monthly income tax | = I ÷ 12, or ÷ 13 with a thirteenth salary |
| K. Net pay | = E − G − H − J |
| L. Employer social insurance | = F × employer rate |
| M. Redundancy Fund | = F × rate |
| N. Human Resources Development Fund | = F × rate |
| O. Social Cohesion Fund | = E × rate (no ceiling) |
| P. Employer GHS | = E × employer GHS rate (Section 4) |
| Q. Central Holiday Fund | only if not exempt; rate from `cyprus-social-contributions` |
| R. Total employer cost | = E + L + M + N + O + P + Q |

## Section 14: Payslip and statement reading guide

| Term (Greek / English) | Meaning |
| --- | --- |
| Μισθός / Misthos / Salary | Gross or net salary |
| Κοινωνικές Ασφαλίσεις / Social Insurance / SIS | Social insurance contribution (employee and employer shares) |
| ΓεΣΥ / GESY / GHS | General Healthcare System contribution |
| Ταμείο Πλεονάζοντος Προσωπικού / Redundancy Fund | Employer-only fund |
| ΑνΑΔ / HRDA | Human Resources Development Fund, employer only |
| Ταμείο Κοινωνικής Συνοχής / Social Cohesion Fund | Employer-only fund, no ceiling |
| Κεντρικό Ταμείο Αδειών / Central Holiday Fund | Employer contribution unless exempt |
| Φόρος Εισοδήματος / PAYE / Income Tax | Income tax withheld |
| Ασφαλιστέες αποδοχές / Insurable earnings | Earnings up to the monthly or weekly ceiling |
| 13ος μισθός / 13th salary | Thirteenth salary (taxable; reported in the month paid) |

## Section 15: Onboarding fallback

Gather in this order and stop where blocked:

1. Pay date, frequency and year.
2. Gross monthly pay, and any thirteenth salary, bonus or benefit in kind.
3. Signed T.D.59A for 2026.
4. Employee TIN and social insurance number.
5. Pay and amounts withheld so far this year.
6. Central Holiday Fund status of the employer.
7. Evidence for any new-resident exemption claimed.

If the person turns out to be self-employed, stop and use `cyprus-income-tax` and `cyprus-social-contributions`.

## Section 16: Filing obligations and deadlines

| Item | Value | Note (verbatim) |
| --- | --- | --- |
| Source | all figures below | https://www.gov.cy/mof-tax/prothesmies/ |
| Monthly PAYE return (income tax and contributions withheld) | end of the month after the month of withholding | "2027-01-31 Προθεσμία Υποβολής Δήλωσης PAYE για τον Δεκέμβριο 2026 Τέλος του μήνα που ακολουθεί τον μήνα παρακράτησης" |
| Annual PAYE return for 2026 | 31 March 2027 | "Προθεσμία Υποβολής Ετήσιας Δήλωσης Παρακράτησης Φ.Ε. και Εισφορών (PAYE) για το έτος 2026 Τέλος Μαρτίου" |
| Annual PAYE return for 2025 (row dated 31 May 2026) | extended to 30 November 2026 | "Νέα Παράταση 2026/11/30 (Ανακοίνωση 16/09/2026)" |
| GHS withheld at source on an employee's benefit (όφελος μισθωτού) and the employer's GHS on it, paid through the Tax Department | end of the following month | "Προθεσμία παρακράτησης ΓεΣΥ στην πηγή από όφελος μισθωτού και ΓεΣΥ από εισφορά εργοδότη" |

| Item | Value | Note (verbatim) |
| --- | --- | --- |
| Source | all figures below | https://www.gov.cy/mof-tax/documents/ypovoli-diloseon-t-f-7/dilosi-parakratisis-f-e-kai-eisforon-paye/sychnes-erotiseis-diloseon-parakratisis-f-e-kai-eisforon-paye/ |
| Payment of tax and contributions withheld | within one month from the end of the month of withholding | "Η προθεσμία πληρωμής είναι ένας μήνας, από τη λήξη του μήνα" |
| Late payment surcharge, each month of delay (article 44(2) of Law 4/1978) | 1% | "επιπρόσθετη επιβάρυνση ύψους 1%), αν υπάρχει καθυστέρηση στην πληρωμή" |

The surcharge is charged on the 1st of the month after the last payment date and on every 1st of the month until paid. Interest is charged after one complete month from that date. A monthly return must be filed before the payment can be made, because the return creates the debt. Amending a return is not late filing, but extra tax that results carries interest and the surcharge. The annual PAYE return is mandatory and reconciles the monthly returns of the same year; at least one monthly return is needed before the annual return can be filed.

| Form | Purpose | Deadline or timing |
| --- | --- | --- |
| Monthly PAYE return (Δήλωση Παρακράτησης Φ.Ε. και Εισφορών) | Income tax and contributions withheld, each employee listed separately with TIN; filed only through TFA (T.D.7 page: https://www.gov.cy/mof-tax/documents/ypovoli-diloseon-t-f-7/) | End of the following month (deadline table above) |
| Annual PAYE return (T.D.7) | Reconciles the monthly returns | 2026 return: deadline table above |
| T.D.63 certificate of earnings | Given every year by the employer to current and past employees; the employer may use the Tax Department's template or its own with the same details (https://www.gov.cy/mof-tax/en/documents/certificate-of-earnings-t-d-63/) | Annually |
| T.D.59A declaration | Completed and signed by every employee every year (https://www.gov.cy/mof-tax/en/documents/declaration-for-claiming-tax-deductions-t-d-59/) | Each year, and on hiring |
| Social insurance and fund contributions | Paid to Social Insurance Services | End of the calendar month after the month they are for |
| Employee's own income tax return | See `cyprus-income-tax` | Not an employer filing |

## Section 17: Interaction with other Guides

| Scenario | Guide |
| --- | --- |
| Employee payroll (PAYE, social insurance, GHS, employer funds) | This Guide (`cyprus-payroll`) |
| Contribution detail: self-employed, voluntary, Central Holiday Fund, late charges | `cyprus-social-contributions` |
| Employee's own return, personal deductions and income criteria, residence | `cyprus-income-tax` |
| Cyprus VAT returns | `cyprus-vat-return` |
| Non-domicile and Special Defence Contribution | `cy-non-dom` |

Handoff points:

- Payroll to bookkeeping: gross wages and the employer's contributions are expenses; income tax and the employee's contributions withheld are liabilities until paid.
- Payroll to income tax: the T.D.63 certificate feeds the employee's own return.

## The method, step by step

1. Confirm the employer is registered with the Tax Department (form through TFA, https://www.gov.cy/mof-tax/en/documents/registration-deregistration-as-an-employer/) and with Social Insurance Services, and that each new hire was notified through ERGANI no later than one day before starting (https://www.businessincyprus.gov.cy/social-insurance-registration-and-contributions/).
2. Collect the employee's signed T.D.59A for 2026 and TIN (form: https://www.gov.cy/media/sites/167/2026/02/IR59_2026_English__.pdf). Without the form, allow only known contributions (note 15).
3. Compute insurable earnings: gross pay up to the 2026 monthly or weekly ceiling (https://sisweb.mlsi.gov.cy/anotato2025/). Apply the employee and employer social insurance, Redundancy and Human Resources Development rates to it, and the Social Cohesion rate to total earnings (https://www.businessincyprus.gov.cy/social-insurance-registration-and-contributions/).
4. Compute GHS on the employee's income from this employer, employee and employer shares, until the year's income passes the GHS limit (T.D.59A note 22; https://www.gesy.org.cy/sites/Sites?d=Desktop&locale=en_US&lookuphost=/en-us/&lookuppage=hiofinancing).
5. On the T.D.59A, compute chargeable income: Part A income less Part B allowances, with contributions within the one-fifth cap, any documented article 8 deduction at line B2, and the 2026 personal deductions the employee declared (https://www.gov.cy/media/sites/167/2026/02/IR59_2026_English__.pdf).
6. Apply the 2026 scale to get the year's tax, take the salary share (C2), and divide by 12 or 13 (or 52 for weekly pay) for the amount to withhold; withhold bonus tax in the month paid (https://www.gov.cy/media/sites/167/2026/05/FAQs-110526.pdf for the scale).
7. File the monthly PAYE return through TFA and pay by the end of the following month; file the annual return for 2026 by its deadline (https://www.gov.cy/mof-tax/prothesmies/). Pay Social Insurance Services by the end of the following month.
8. After the year, give each current and past employee a T.D.63 certificate (https://www.gov.cy/mof-tax/en/documents/certificate-of-earnings-t-d-63/).

## Ask the client first

- Does the employee pay a thirteenth salary, bonuses or benefits in kind? (Changes the divisor and the month tax is withheld.)
- Has each employee signed a 2026 T.D.59A, and does any have income from another employer, a pension or rent? (Changes chargeable income and the share withheld.)
- Did the employee move to Cyprus to work, and when did the job start? Do they have evidence for the 20%, 50% or 25% exemption conditions? (Can cut income tax sharply.)
- Does the employer hold an exemption from the Central Holiday Fund? (Changes the employer's cost.)
- Is any employee insured in another EU or EEA state, or a director? (Directors count as employees; foreign insurance may change contributions.)
- Is pay monthly or weekly? (Selects the ceiling.)

## When to refuse or refer

- Refer the 25% article 8(21B) exemption if the employer wants it applied through payroll: the 2026 T.D.59A does not list it.
- Refer any choice between new-resident exemptions, any transition between articles 8(21), 8(23) and 8(23A), and any case where pay hovers near an exemption's minimum pay.
- Refer employees insured in another EU or EEA state, posted workers, and employees of non-resident employers.
- Refer the Central Holiday Fund rate and exemption to `cyprus-social-contributions` or an accountant.
- Refuse to file a monthly PAYE return without each employee's TIN.
- Refuse to present any computation as final: label it an estimate for a Cyprus accountant to review.

## Sources

1. Tax Department, T.D.59A 2026 declaration (English): https://www.gov.cy/media/sites/167/2026/02/IR59_2026_English__.pdf
2. Tax Department, T.D.59 page: https://www.gov.cy/mof-tax/en/documents/declaration-for-claiming-tax-deductions-t-d-59/
3. Tax Department, Tax Reform 2026 FAQs for individuals (11 May 2026): https://www.gov.cy/media/sites/167/2026/05/FAQs-110526.pdf
4. Tax Department, PAYE FAQ: https://www.gov.cy/mof-tax/documents/ypovoli-diloseon-t-f-7/dilosi-parakratisis-f-e-kai-eisforon-paye/sychnes-erotiseis-diloseon-parakratisis-f-e-kai-eisforon-paye/
5. Tax Department, employee TIN procedure: https://www.gov.cy/mof-tax/documents/ypovoli-diloseon-t-f-7/dilosi-parakratisis-f-e-kai-eisforon-paye/pos-energo-se-periptoseis-poy-gia-opoiodipote-logo-den-echo-to-aft-kapoioy-ypalliloy/
6. Tax Department, T.D.7 returns page: https://www.gov.cy/mof-tax/documents/ypovoli-diloseon-t-f-7/
7. Tax Department, deadlines calendar: https://www.gov.cy/mof-tax/prothesmies/
8. Tax Department, T.D.63 certificate of earnings: https://www.gov.cy/mof-tax/en/documents/certificate-of-earnings-t-d-63/
9. Tax Department, employer registration: https://www.gov.cy/mof-tax/en/documents/registration-deregistration-as-an-employer/
10. Tax Department, benefits in kind: https://www.gov.cy/mof-tax/documents/paroches-se-eidos/
11. Tax Department, article 8(21) and 8(21A) table: https://www.gov.cy/media/sites/167/2026/01/implementation-of-sections-21-and-21A-of-article-8-24072023.pdf
12. Tax Department, article 8(23) and 8(23A) table: https://www.gov.cy/media/sites/167/2026/06/%CE%A0%CE%AF%CE%BD%CE%B1%CE%BA%CE%B1%CF%82-%CE%B1%CF%80%CE%B1%CE%BB%CE%BB%CE%B1%CE%B3%CF%8E%CE%BD-823-%CE%BA%CE%B1%CE%B9-823%CE%91.pdf
13. Tax Department, article 8(21B): https://www.gov.cy/media/sites/167/2026/06/Article-8-21B-of-the-Income-Tax-Law-N.118-I-2002.pdf
14. Business in Cyprus (government), social insurance registration and contributions: https://www.businessincyprus.gov.cy/social-insurance-registration-and-contributions/
15. Social Insurance Services, 2026 maximum insurable earnings notice: https://sisweb.mlsi.gov.cy/anotato2025/
16. Social Insurance Services, contributions (Single Digital Gateway): https://www.mlsi.gov.cy/mlsi/sdg/sdg.nsf/All/EA4F396F80C4BAA8C22586A10042659F?OpenDocument
17. Health Insurance Organisation, GHS financing: https://www.gesy.org.cy/sites/Sites?d=Desktop&locale=en_US&lookuphost=/en-us/&lookuppage=hiofinancing
18. Ministry of Labour, minimum wage statement of 27 December 2025: https://www.gov.cy/ergasia-kai-koinonikes-asfaliseis/dilosi-tou-ypourgou-ergasias-kai-koinonikon-asfaliseon-gia-tin-afxisi-tou-ethnikou-katotatou-misthou/

## Disclaimer

This Guide and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this Guide. All outputs must be reviewed and signed off by a qualified professional (such as a warranted accountant in Cyprus) before implementation.

The most up-to-date version of this Guide is maintained at openaccountants.com. Log in to access the latest version, request a professional review from a licensed accountant, and track updates as tax law changes.

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
