---
name: cyprus-social-contributions
description: Use this skill whenever asked about Cyprus social insurance and General Healthcare System (GHS/GESY) contributions for employees, employers, or self-employed individuals. Trigger on phrases like "how much social insurance do I pay in Cyprus", "Cyprus GESY contributions", "GHS rate", "employer on-cost Cyprus", "self-employed social insurance Cyprus", "Social Cohesion Fund", "Redundancy Fund", "HRDA contribution", "insurable earnings ceiling", "Cyprus payroll deductions", "Cyprus PAYE", or any question about Cyprus social-security or healthcare contribution obligations. Also trigger when classifying bank statement transactions that relate to Department of Social Insurance Services (Υπηρεσίες Κοινωνικών Ασφαλίσεων) debits, GHS/GESY payments, HIO (Health Insurance Organisation) payments, or government social-security remittances from Bank of Cyprus, Hellenic Bank, or other Cypriot banks. Also trigger when preparing a T.D.1 (TD1) personal income tax return where contribution deductibility or aggregate income caps are relevant. This skill covers social insurance employee/employer/self-employed rates, GHS/GESY rates across all income categories, employer-only funds (Social Cohesion, Redundancy, HRDA), insurable-earnings and GHS ceilings, payment schedule, registration, penalties, interaction with personal income tax, bank statement classification patterns, and edge cases. ALWAYS read this skill before touching any Cyprus social-contribution work.
version: 0.1
jurisdiction: CY
tax_year: 2026
last_updated: 2026-10-02
authored_by: OpenAccountants team
review_status: pending_review
trust_label: Written by the OpenAccountants team
depends_on:
  - social-contributions-workflow-base
category: international
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Cyprus social insurance and GHS (GESY) contributions

This Guide covers Cyprus social insurance and General Healthcare System (GHS, in Greek GESY) contributions for employees, employers, self-employed people and voluntary contributors. It also covers the employer-only funds (Redundancy, Human Resources Development, Social Cohesion and the Central Holiday Fund), the 2026 maximum insurable earnings, the GHS annual maximum, payment deadlines, registration and late-payment charges, and how contribution payments show on a bank statement. Figures are for tax year 2026. The Cyprus tax year is the calendar year. Every figure below comes from an official page linked in the table that holds it.

## Section 1: Quick reference

**Read this whole section before computing or classifying anything.**

**Section 1 quick reference field table**

| Field | Value |
| --- | --- |
| Country | Cyprus (Republic of Cyprus) |
| Primary legislation | The Social Insurance Law 59(I)/2010 as amended ([Social Insurance Services legislation page](https://www.mlsi.gov.cy/mlsi/sdg/sdg.nsf/All/335C7DB77BE6657AC22586A1004509A2?OpenDocument)) and the Social Insurance (Contributions) Regulations 2010 to 2025. The 2026 maximum insurable earnings are set under "Regulation 8(1) and (2)" of those Regulations "and the relevant Order issued pursuant to Article 20 of the Law" (table B source) |
| Supporting legislation | General Healthcare System Law, with the contribution rates "set by the General Healthcare System (Amending) Law of 2017" (Health Insurance Organisation); Income Tax Law No.118(I) of 2002 (TD59A 2026) |
| Social-security authority | Social Insurance Services (Υπηρεσίες Κοινωνικών Ασφαλίσεων), Ministry of Labour and Social Insurance |
| Healthcare authority | Health Insurance Organisation (HIO, Οργανισμός Ασφάλισης Υγείας), gesy.org.cy |
| Tax authority | Tax Department (Τμήμα Φορολογίας), now at gov.cy/mof-tax |
| Who pays social insurance on a salary | Employee and employer in equal shares, plus a state share that neither of them pays (table A) |
| Who pays GHS on a salary | Employee and employer at different rates (table C) |
| Employer-only funds | Redundancy, Human Resources Development, Social Cohesion, and the Central Holiday Fund unless the employer is exempt (tables A and E) |
| Ceiling for social insurance and three funds | The 2026 maximum insurable earnings (table B). It covers the Social Insurance, Annual Paid Leave, Redundancy and Human Resource Development funds only. It does NOT cover GHS or the Social Cohesion Fund |
| GHS ceiling | A separate annual maximum per person, all income added together (table D) |
| Social Cohesion Fund ceiling | None: total earnings, no maximum (table E source) |
| Employer payment deadline | By the end of the calendar month after the month the contributions are for |
| Self-employed payment | Every three months |
| Currency | EUR |

**Table A. Social insurance and employer fund rates (Business in Cyprus, government one-stop shop)**

| Item | Value | Note |
| --- | --- | --- |
| Source | all figures below | https://www.businessincyprus.gov.cy/social-insurance-registration-and-contributions/ |
| All three shares together, on an employee's insurable earnings (employer, employee and state) | 22.8% | "Employees must contribute 22.8% on their insurable earnings" |
| Employee share | 8.8% | "in the proportion of 8.8%, 8.8% and 5.2%, respectively" (employer, employee, state) |
| Employer share | 8.8% | same sentence |
| State share (paid by the state, not by the employer or the employee) | 5.2% | same sentence |
| Both shares together, on a self-employed person's insurable income (self-employed and state) | 21.8% | "The self-employed must contribute 21.8% on their insurable income" |
| Self-employed person's own share (the state pays the rest) | 16.6% | "16.6% of which is paid by the self-employed and 5.2% by the state" |
| Voluntary contributor (other than one working abroad for a Cypriot employer), both shares together | 19.7% | "Voluntary contributors owe 19.7% on their declared earnings" |
| Voluntary contributor (other than one working abroad for a Cypriot employer), own share | 15% | "15% of which is paid by the voluntary contributor and 4.7% by the state" |
| State share for a voluntary contributor | 4.7% | same sentence |
| Voluntary contributor working abroad for a Cypriot employer, own share, up to the maximum insurable earnings | 17.6% | "Voluntary contributors working abroad for Cypriot employers pay contributions of 17.6% on either their basic insurable earnings or on their normal earnings, as agreed in their contract of employment, up to the maximum insurable earnings" |
| State share for that contributor | 5.2% | "An additional contribution of 5.2% is paid by the state" |
| Redundancy Fund, employer only | 1.2% | "employers must contribute 1.2% to the Redundancy Fund" |
| Human Resources Development Fund, employer only | 0.5% | "0.5% to the Human Resources Development Fund" |
| Social Cohesion Fund, employer only | 2% | "2% to the Social Cohesion Fund for their employees" |

Never tell an employer that social insurance costs it the total in the first row. The employer pays its own share in table A, plus the employer-only funds, plus employer GHS. The Business in Cyprus page carries no publication date. Its text describes rules in force "from January 1, 2024" and its footer reads "©2026". No Social Insurance Services page dated 2026 prints these rates; the Social Insurance Services pages read for this Guide still print 2020 rates (table E).

**Table B. 2026 maximum insurable earnings (Social Insurance Services notice to employers, December 2025)**

| Item | Value | Note |
| --- | --- | --- |
| Source | all figures below | https://sisweb.mlsi.gov.cy/anotato2025/ |
| Maximum for monthly-paid employees, from 1 January 2026 | EUR 5,742 | "€5.742 από 1/1/2026" |
| Maximum for weekly-paid employees, from 5 January 2026 | EUR 1,325 | "€1.325 από 5/1/2026" |

The notice applies these limits to "the Social Insurance Fund, the Annual Paid Leave Fund, the Redundancy Fund, and the Human Resource Authority Development Levy". It names no other fund. The notice is addressed to employers about employees' earnings; it sets no ceiling for self-employed income. No allowed page prints an annual 2026 figure, so this Guide gives none.

**Table C. GHS contribution rates by category (Health Insurance Organisation)**

| Item | Value | Note |
| --- | --- | --- |
| Source | all figures below | https://www.gesy.org.cy/en-us/hiofinancing |
| Employees (public and private sector), on their salaries | 2.65% | "2,65% On their salaries" (full implementation, as of 1/3/2020) |
| Employers (including the State as an employer), on the salaries of every person they employ | 2.90% | "2,90% On the salaries of every person employed by them" |
| State, on salaries, self-employed remuneration, officials' pay and pensions | 4.70% | "4,70% On the salaries of the employees, the remuneration of the self-employed and officials and on pensions" |
| Self-employed, on their remuneration | 4.00% | "4,00% On their remuneration" |
| Pensioners, on their pension | 2.65% | "2,65% On their pension" |
| Income earners (rent, interest, dividends), on that income | 2.65% | "2,65% On their income" |
| Government officials, on their remuneration | 2.65% | "Government Officials" ... "2,65% On their remuneration" |
| Persons who pay government officials, on that remuneration | 2.90% | "2,90% On the remuneration of the Government Official" |

The same page says: "In case that the natural person is not a tax resident of Cyprus, he/she will pay contributions only for the income, earnings and pensions that derive from the Republic of Cyprus, excluding dividends and interest." The lower first-phase rates on that page applied only from 1 March 2019 to 29 February 2020. Use the full implementation column.

**Table D. GHS withholding by employers in 2026 (Tax Department form TD59A 2026, English)**

| Item | Value | Note |
| --- | --- | --- |
| Source | all figures below | https://www.gov.cy/media/sites/167/2026/02/IR59_2026_English__.pdf |
| GHS the employer withholds from income it pays as employer | 2.65% | "For income for which you are the employer, you must withhold 2.65% G.H.S." |
| Annual income above which GHS withholding stops | EUR 180,000 | "exceeds the amount of €180.000, stop withholding" |

The Health Insurance Organisation page in table C gives the same annual maximum, "For every natural person". Income from all sources is added together in a set priority order to reach it (Tax Department return guide for 2025, linked under Sources).

**Table E. Employer contributions page (Social Insurance Services, Single Digital Gateway)**

| Item | Value | Note |
| --- | --- | --- |
| Source | all figures below | https://www.mlsi.gov.cy/mlsi/sdg/sdg.nsf/All/EA4F396F80C4BAA8C22586A10042659F?OpenDocument |
| Central Holiday Fund, lowest rate (4 weeks of leave), employer only, unless exempt | 8% | "ranging from 8 % for 4 weeks leave" |
| Employer GHS rate, as printed on this page | 2.90% | "Employers 2.90%" |

This page also says: "For the Social Cohesion Fund the total earnings are taken into consideration without a maximum amount." It says the Central Holiday Fund rate "is proportional to the days of annual leave to which the employee is entitled", that "The entire contribution to the Central License Fund is paid by the employer", and that the employer need not pay it if it obtains an exemption. Its own worked example adds the Central Holiday Fund contribution to the earnings first, then charges social insurance, Redundancy, Human Resources Development, Social Cohesion and GHS on that larger total. The page was last updated in 2021 and still prints 2020 social insurance rates and a 2020 ceiling. Use it for the structure, the Central Holiday Fund rate and the employer GHS rate only. The English page prints the upper rate with a typing error. The Greek page and the Annual Leave page print it: the rate runs from 8% for 20 days of leave to 16% for 40 days on a five-day week (table G), and "The rate of contribution for leave longer than 40 days is increased accordingly".

**Table G. Central Holiday Fund rate by leave entitlement (Social Insurance Services, Annual Leave, Obligations of the Employer)**

| Item | Value | Note |
| --- | --- | --- |
| Source | all figures below | https://www.mlsi.gov.cy/mlsi/sdg/sdg.nsf/All/00DDEF169CC27CAEC22586B7003F35FE?OpenDocument |
| Lowest rate, 20 days of leave, five-day week (24 days, six-day week) | 8% | "TABLE I ... FIVE-DAY PER WEEK BASIS Days of leave Rate of contribution (%) 20 8" |
| Rate at 40 days of leave, five-day week (48 days, six-day week) | 16% | "40 16 ... The rate of contribution for leave longer than 40 days is increased accordingly" |

This page was last updated 14/04/2021. If an employer gives annual leave with pay under more favourable terms than the Annual Holiday with Pay Law, the employer "may apply for exception from obligation to pay contributions to the Central Holiday Fund", using form 1-005 of the YKA series.

**Table F. Late payment by an employer (Social Insurance Services, Single Digital Gateway)**

| Item | Value | Note |
| --- | --- | --- |
| Source | all figures below | https://www.mlsi.gov.cy/mlsi/sdg/sdg.nsf/All/D5322D5E5CD6F735C22586A10044EC34 |
| Additional charge for the first month of delay | 3% | "For the first month of delay the charge is 3%" |
| Maximum additional charge | 27% | "increases by 3 points for each month of delay after the first month up to a maximum of 27%" |

The charge is "a percentage of the contributions due" and is paid "to the Social Insurance Fund, the Social Cohesion Fund, and the Health Insurance Fund". The page does not list the Redundancy, Human Resources Development or Central Holiday funds.

**Conservative defaults**

| Ambiguity | Default |
| --- | --- |
| Unknown employment status | Ask. Do not assume. Employee, employer, self-employed, voluntary and office-holder rates differ. If forced, treat the person as an employee (table A employee share plus the table C employee GHS rate) and say so |
| Unknown self-employed rate | Use the table A self-employed share. Any lower figure from an older source is stale |
| Monthly earnings above the table B maximum | Cap social insurance, Redundancy, Human Resources Development and Central Holiday Fund contributions at the table B maximum. Do NOT cap Social Cohesion. GHS has its own annual maximum (table D) |
| Central Holiday Fund | Ask whether the employer holds an exemption. If it does not, it pays at least the table E rate, and the contribution is added to earnings before the other contributions are worked out |
| Unknown GHS scope on investment income | Apply the table C income-earner rate to rent, interest and dividends of a Cyprus tax resident, within the table D annual maximum. For a non-resident, no GHS on dividends and interest (table C note) |
| Unknown whether a Social Insurance Services debit is a contribution or a late charge | Classify as a contribution and flag it for review |
| Unknown tax year | Ask. This Guide is for 2026. The 2025 ceiling was lower |

## Section 2: Required inputs and refusal catalogue

### Required inputs

- **Minimum viable**: employment status (employee, employer, self-employed or voluntary contributor) and gross earnings with the pay period (monthly or weekly). Without status and earnings, STOP. Do not compute contributions.
- **Recommended**: monthly or weekly gross pay; whether pay exceeds the table B maximum; total yearly income from all sources (for the table D GHS maximum); whether the person is a Cyprus tax resident (for GHS on dividends and interest); whether the employer is exempt from the Central Holiday Fund; for the self-employed, the occupational category or whether they asked to pay on actual earnings.
- **Ideal**: Social Insurance Services statement, payroll register, the employee's TD59A, bank statements showing the monthly remittances, and the prior-year income tax return.

### Refusal catalogue

- **R-CY-SC-1: Self-employed insurable income unknown.** Trigger: self-employed contribution requested without the income base. Message: "Self-employed social insurance is charged on estimated earnings by occupational category (our wording; the page says the estimate is 'based on each individual's experience and field of work'). Business in Cyprus says 'The estimated earnings are calculated by the Tax Department based on each individual's experience and field of work' and 'You can file a request to be taxed based on actual earnings instead'. The category amounts are not printed on any page this Guide could read. Confirm the client's category amount or actual-earnings election with the Social Insurance Services before computing."
- **R-CY-SC-2: Contribution arrears and late charges.** Trigger: unpaid employer contributions from earlier months. Message: "Late employer contributions carry an additional charge that starts at the first-month rate in table F and rises by 3 points a month to the maximum in table F. Do not quantify arrears without a Social Insurance Services statement. Refer to a Cyprus-qualified accountant."
- **R-CY-SC-3: Special Defence Contribution and domicile.** Trigger: questions about tax on dividends, interest or rent, or non-domiciled status. Message: "Special Defence Contribution is a tax, not a social contribution, and is outside this Guide. Use `cy-non-dom` or `cyprus-income-tax`. What this Guide does cover: GHS on rent, interest and dividends at the table C income-earner rate for Cyprus tax residents, with no GHS on dividends and interest for non-residents."
- **R-CY-SC-4: Income tax penalties and interest.** Trigger: late-filing or late-payment income tax penalties. Message: "Outside this Guide. Use `cyprus-income-tax`."
- **R-CY-SC-5: Tax year other than 2026.** Trigger: tax year not stated, or a computation spanning 2025 and 2026. Message: "This Guide holds 2026 figures. The 2026 maximum insurable earnings in table B apply from 1 January 2026 (monthly) and 5 January 2026 (weekly). Confirm the year and get the earlier ceiling from the Social Insurance Services before computing an earlier period."
- **R-CY-SC-6: Cross-border cases.** Trigger: an employee insured in another EU or EEA state or Switzerland, a posted worker, or an employer with its registered office abroad. Message: "Which country's social insurance and healthcare contributions apply to a cross-border worker is a coordination question that the pages this Guide relies on do not settle. Refer."

## Section 3: Payment pattern library

This is the deterministic pre-classifier for bank statement transactions related to Cyprus social contributions. When a transaction matches a pattern below, apply the treatment directly.

**How to read this table.** Match by case-insensitive substring on the counterparty or reference as it appears on the bank statement. Social insurance and GHS payments are statutory contributions: EXCLUDE them from any VAT return and from revenue at the individual level. For an employer, its own contributions and employer-only fund payments are a payroll cost. The employee's share is withheld from gross pay (the employer "is entitled ... to deduct the amount of contributions he pays on behalf of his employee from the earnings of the employee", table E source), so it is part of gross payroll, not an extra cost. Whether an item is deductible for income tax is a question for `cyprus-income-tax`.

### 3.1 Social Insurance Services remittances

**Social Insurance Services remittance patterns**

| Pattern | Treatment | Notes |
| --- | --- | --- |
| DEPARTMENT OF SOCIAL INSURANCE, DSI, SOCIAL INSURANCE SERVICES | EXCLUDE: social insurance remittance | Monthly employer remittance, or self-employed every three months |
| SOCIAL INSURANCE, SOC INS, SISNET | EXCLUDE: social insurance | Same |
| ΥΠΗΡΕΣΙΕΣ ΚΟΙΝΩΝΙΚΩΝ ΑΣΦΑΛΙΣΕΩΝ | EXCLUDE: social insurance | Greek-language reference |
| ΚΟΙΝΩΝΙΚΕΣ ΑΣΦΑΛΙΣΕΙΣ | EXCLUDE: social insurance | Greek-language reference |
| SI CONTRIB, KOINONIKES ASFALISEIS | EXCLUDE: social insurance | Transliterated reference |

### 3.2 GHS / GESY (Health Insurance Organisation) remittances

**GHS/GESY remittance patterns**

| Pattern | Treatment | Notes |
| --- | --- | --- |
| GHS, GESY, GENERAL HEALTHCARE | EXCLUDE: GHS/GESY contribution | Healthcare system contribution |
| HIO, HEALTH INSURANCE ORGANISATION | EXCLUDE: GHS/GESY | Administering body |
| ΓΕΣΥ, ΓΕΝΙΚΟ ΣΥΣΤΗΜΑ ΥΓΕΙΑΣ | EXCLUDE: GHS/GESY | Greek-language reference |
| ΟΡΓΑΝΙΣΜΟΣ ΑΣΦΑΛΙΣΗΣ ΥΓΕΙΑΣ | EXCLUDE: GHS/GESY | HIO in Greek |

### 3.3 Employer-only fund references (may appear bundled with social insurance)

**Employer-only fund patterns**

| Pattern | Treatment | Notes |
| --- | --- | --- |
| SOCIAL COHESION, COHESION FUND | EXCLUDE: employer Social Cohesion Fund | Employer only, no ceiling |
| REDUNDANCY FUND | EXCLUDE: employer Redundancy Fund | Employer only, capped at the table B maximum |
| HRDA, HRDC, HUMAN RESOURCE, INDUSTRIAL TRAINING | EXCLUDE: employer Human Resources Development Fund | Employer only, capped at the table B maximum |
| CENTRAL HOLIDAY FUND, ANNUAL LEAVE FUND | EXCLUDE: employer Central Holiday Fund | Employer only, unless exempt |
| Bundled "SOCIAL INSURANCE + FUNDS" lump sum | EXCLUDE: combined employer remittance | Split only if a breakdown is needed |

### 3.4 Income tax payments (NOT contributions; do not confuse)

**Income tax patterns**

| Pattern | Treatment | Notes |
| --- | --- | --- |
| TAX DEPARTMENT, ΤΜΗΜΑ ΦΟΡΟΛΟΓΙΑΣ | EXCLUDE: income tax, not a contribution | PAYE or income tax payment. GHS on some non-salary income is also paid to the Tax Department (Section 5, Rule 3) |
| PAYE, T.D.1, TD1 | EXCLUDE: income tax withholding or assessment | Not social insurance |
| SDC, DEFENCE CONTRIBUTION, ΑΜΥΝΑ | EXCLUDE: Special Defence Contribution | Separate from social insurance and GHS |

### 3.5 Salary and payroll (exclude from contribution classification)

**Salary/payroll patterns**

| Pattern | Treatment | Notes |
| --- | --- | --- |
| SALARY, MISTHOS, ΜΙΣΘΟΣ (outgoing) | EXCLUDE: payroll expense | Not a contribution payment |
| SALARY, ΜΙΣΘΟΣ (incoming) | EXCLUDE: employment income received | Not a contribution payment |

### 3.6 Benefits received (not contributions paid)

**Benefits received patterns**

| Pattern | Treatment | Notes |
| --- | --- | --- |
| DSI PENSION, ΣΥΝΤΑΞΗ | EXCLUDE: pension or benefit received | Not a contribution payment |
| UNEMPLOYMENT BENEFIT, SICKNESS BENEFIT | EXCLUDE: benefit received | Not a contribution payment |

## Section 4: Worked examples

Bank statement and payroll classifications for a hypothetical Limassol software consultancy and its staff. The amounts are hypothetical. Rounding to the cent is our own.

### Example 1: Employee monthly contributions, below every ceiling (hypothetical)

The employer is exempt from the Central Holiday Fund.

| Item | Value | Note |
| --- | --- | --- |
| Source | rates in tables A and C | https://www.businessincyprus.gov.cy/social-insurance-registration-and-contributions/ |
| Hypothetical monthly gross pay | EUR 3,000 | Below the table B monthly maximum |
| Employee social insurance (table A employee share) | EUR 264.00 | Case A |
| Employer social insurance (table A employer share) | EUR 264.00 | Case A |
| Employee GHS (table C employee rate) | EUR 79.50 | Case A |
| Employer GHS (table C employer rate) | EUR 87.00 | Case A |
| Social Cohesion Fund (table A) | EUR 60.00 | Case A |
| Redundancy Fund (table A) | EUR 36.00 | Case A |
| Human Resources Development Fund (table A) | EUR 15.00 | Case A |

**Classification:** EXCLUDE: statutory contributions. The employee's social insurance and GHS are withheld from gross pay. The employer's shares and the three funds are an extra payroll cost. If the employer is NOT exempt from the Central Holiday Fund, add that contribution to the earnings first and work out every other line on the larger total (table E note).

### Example 2: High earner above the insurable-earnings maximum (hypothetical)

The employer is exempt from the Central Holiday Fund.

| Item | Value | Note |
| --- | --- | --- |
| Source | maximum in table B, rates in tables A and C | https://sisweb.mlsi.gov.cy/anotato2025/ |
| Hypothetical monthly gross pay | EUR 7,000 | Above the table B monthly maximum; yearly pay stays below the table D GHS maximum |
| Employee social insurance, on the table B maximum only | EUR 505.30 | Case B |
| Employer social insurance, on the table B maximum only | EUR 505.30 | Case B |
| Redundancy Fund, on the table B maximum only | EUR 68.90 | Case B |
| Human Resources Development Fund, on the table B maximum only | EUR 28.71 | Case B |
| Social Cohesion Fund, on the full pay (no ceiling) | EUR 140.00 | Case B |
| Employee GHS, on the full pay | EUR 185.50 | Case B |
| Employer GHS, on the full pay | EUR 203.00 | Case B |

**Classification:** EXCLUDE: statutory contributions. Social insurance, Redundancy and Human Resources Development stop at the table B maximum. GHS runs on actual pay up to the table D annual maximum. Social Cohesion runs on actual pay with no maximum.

### Example 3: Self-employed social insurance debit (Bank of Cyprus)

**Input line:**
`30.04.2026 ; DEPARTMENT OF SOCIAL INSURANCE ; DEBIT ; Q1 2026 SELF EMPLOYED ; -1,200.00 ; EUR`

**Reasoning:** Matches "DEPARTMENT OF SOCIAL INSURANCE" (pattern 3.1). The self-employed pay every three months, at the table A self-employed share, on estimated earnings for their occupational category (or actual earnings if they asked for that). Business in Cyprus adds that self-employed "Social insurance contributions now include a contribution to the National Health System". Do not back out an income figure from the payment: the category amount is not printed on any page this Guide could read.

**Classification:** EXCLUDE: self-employed social insurance. Flag the category amount for confirmation.

### Example 4: GHS / GESY remittance (Hellenic Bank)

**Input line:**
`31.05.2026 ; GESY HIO ; DEBIT ; GENERAL HEALTHCARE CONTRIB MAY ; -560.00 ; EUR`

**Reasoning:** Matches "GESY HIO" (pattern 3.2). This is a GHS contribution. For an employer it bundles the employee share (withheld) and the employer share at the table C rates. All GHS for one person is subject to the single annual maximum in table D.

**Classification:** EXCLUDE: GHS contribution. The employer share is a payroll cost; the employee share is part of gross payroll.

### Example 5: Tax Department payment (NOT a contribution)

**Input line:**
`30.06.2026 ; TAX DEPARTMENT ; DEBIT ; PAYE JUNE 2026 ; -2,100.00 ; EUR`

**Reasoning:** Matches "TAX DEPARTMENT" (pattern 3.4). This is PAYE income tax withheld and paid over, not a social insurance contribution.

**Classification:** EXCLUDE: income tax (PAYE). NOT a social or health contribution.

### Example 6: Unclear Social Insurance Services debit (late charge or arrears)

**Input line:**
`15.09.2026 ; DEPARTMENT OF SOCIAL INSURANCE ; DEBIT ; ARREARS / SURCHARGE ; -3,810.00 ; EUR`

**Reasoning:** Matches pattern 3.1, but the amount is irregular and the reference says "ARREARS / SURCHARGE". Late employer contributions carry the additional charge in table F. The contribution and the charge cannot be separated without a Social Insurance Services statement.

**Classification:** EXCLUDE from VAT. Flag for review and request a breakdown that splits the contribution from the additional charge.

## Section 5: Tier 1 rules

These rules apply when the payroll or bank data is clear and all required inputs are available. All figures are for tax year 2026.

### Rule 1: Employee and employer social insurance

- **Rates**: the employee share and the employer share in table A, each on the employee's insurable earnings. The state share in table A is paid by the state.
- **Ceiling**: insurable earnings stop at the table B maximum for the pay period: monthly from 1 January 2026, weekly from 5 January 2026.
- **Formula**: employee social insurance = the lower of (gross pay for the period, table B maximum) times the employee share. Employer social insurance = the same base times the employer share.
- **Central Holiday Fund employers**: where the employer pays into the Central Holiday Fund, add that contribution to the earnings before applying this rule (table E note).
- **Age**: "The obligation of the employer to pay contributions to the Social Insurance Fund ceases from the day when the employee reaches the pensionable age of 65." If the employee does not meet the insurance conditions for the statutory pension, the employer keeps paying until the employee is entitled to a pension, but "In no case, however, are contributions paid after the age of 68" ([Social Insurance Services, general information](https://www.mlsi.gov.cy/mlsi/sdg/sdg.nsf/All/A0E4DA6A3979A4EAC22586A100418A7A?OpenDocument)). This covers the Social Insurance Fund only. The page says nothing about GHS or the other funds.

### Rule 2: Self-employed social insurance

- **Rate**: the self-employed share in table A, on insurable income. The state pays the rest of the table A self-employed total.
- **Base**: estimated earnings by occupational category (our wording; the page says the estimate is "based on each individual's experience and field of work"), or actual earnings if the person files a request (Business in Cyprus). The category amounts are not printed on any page this Guide could read: see R-CY-SC-1.
- **Ceiling**: the table B notice is for employees. No page read here sets a ceiling for self-employed income. Refer if it matters.
- **Payment**: every three months.

### Rule 3: GHS / GESY rates and the single annual maximum

- **Rates**: by category, table C. Employees and employers pay different rates on the same salary.
- **Annual maximum**: one maximum per person in table D, with income from all sources added together. Once a person's yearly income passes it, GHS stops on the excess. The TD59A tells employers to stop withholding when the employee's income on the form passes it.
- **Non-residents**: a person who is not a Cyprus tax resident pays GHS only on Cyprus income, earnings and pensions, excluding dividends and interest (table C note).
- **Insured abroad**: a person insured in another EU or EEA country or Switzerland is a refer case (R-CY-SC-6).
- **Where GHS is paid**: on salary, with the employer's monthly Social Insurance Services remittance (Rule 9). TD59A note 16 says income on which the GHS withheld "is payable the Social Insurance Services" goes in line A1, and other income, such as deemed benefits under the Income Tax Law, goes in line A2. The Tax Department return guide for 2025 lists self-assessment codes for GHS on employee pay, officers' earnings and other income (code 315) and on interest, dividends and rents (code 316).

### Rule 4: Employer-only funds

| Fund | Rate | Base | Ceiling |
| --- | --- | --- | --- |
| Social Cohesion Fund | Table A | Total earnings | None |
| Redundancy Fund | Table A | Insurable earnings | Table B maximum |
| Human Resources Development Fund | Table A | Insurable earnings | Table B maximum |
| Central Holiday Fund (Annual Paid Leave Fund) | Table G: 8% at 20 days of leave rising to 16% at 40 days (five-day week) | Insurable earnings | Table B maximum |

- **Central Holiday Fund exemption**: "The employer may however be exempt from contributing to the Central Holiday Fund" (Business in Cyprus). Ask whether the employer holds an exemption. Do not assume either way.

### Rule 5: Totals

- Do not quote a single combined percentage for employer cost or employee deductions. No official page prints one for 2026, and the bases differ: social insurance and three funds stop at the table B maximum, GHS stops at the table D annual maximum, Social Cohesion has no maximum, and the Central Holiday Fund changes the base. Work out each line on its own base and add the euro amounts, as in Section 4.

### Rule 6: Which base is capped where

- **Capped at the table B maximum**: Social Insurance (employee and employer), Redundancy Fund, Human Resources Development Fund, Central Holiday Fund (Annual Paid Leave Fund).
- **Capped at the table D annual maximum, all income together**: GHS, every category.
- **No cap**: Social Cohesion Fund.

### Rule 7: Personal income tax scale (tax year 2026, for context only)

Income tax is outside this Guide (use `cyprus-income-tax`). The 2026 scale is here only because payroll questions often mix the two.

| Item | Value | Note |
| --- | --- | --- |
| Source | all figures below | https://www.gov.cy/media/sites/167/2026/05/FAQs-110526.pdf |
| Rate on chargeable income up to EUR 22,000 | 0% | "μέχρι €22.000" (first band) |
| Rate from EUR 22,001 to EUR 32,000 | 20% | "20% από €22.001 μέχρι €32.000" |
| Rate from EUR 32,001 to EUR 42,000 | 25% | "25% από €32.001 μέχρι €42.000" |
| Rate from EUR 42,001 to EUR 72,000 | 30% | "30% από €42.001 μέχρι €72.000" |
| Rate from EUR 72,001 upward | 35% | "35% από €72.001 και άνω" |

- **Contributions as an income tax deduction**: the TD59A 2026 says the total of the year's contributions for life insurance, approved medical funds, GHS, pension and provident funds and social insurance "must not exceed one fifth of your taxable income (i.e.1/5th of the intermediary calculation Β6)". The Tax Department return guide for 2025 says the GHS contribution total "is granted as an allowance in the TAX CALCULATION".

### Rule 8: Withholding (PAYE)

- **PAYE withholding**: employers withhold personal income tax monthly under PAYE and pay it to the Tax Department. The employer also deducts the employee's social insurance and GHS shares from pay and pays them over with its own contributions (table E source: the employer "is responsible for the payment of his and his employee's contributions").
- **Tax Department deadlines** ([Tax Department deadline calendar](https://www.gov.cy/mof-tax/prothesmies/)): the monthly PAYE return and payment is due by the end of the month after the month of withholding ("Τέλος του μήνα που ακολουθεί τον μήνα παρακράτησης"). The employer's annual PAYE return of tax and contributions withheld for 2026 is due 31 March 2027.

### Rule 9: Employer payment schedule

- **Due date**: "The employer is liable to pay contributions to the previously mentioned Funds by the end of the calendar month which follows the month for which contributions are due" ([Social Insurance Services, deadlines](https://www.mlsi.gov.cy/mlsi/sdg/sdg.nsf/All/D5322D5E5CD6F735C22586A10044EC34)). The funds named on the contributions page are the Social Insurance Fund, the Central Holiday Fund, the Redundancy Fund, the Human Resources Development Fund, the Social Cohesion Fund and the Health Insurance Fund.
- **Late payment**: the additional charge in table F.

### Rule 10: Self-employed payment schedule

- **Schedule**: "Social insurance contributions must be paid every three months" ([Business in Cyprus](https://www.businessincyprus.gov.cy/social-insurance-registration-and-contributions/)). The exact dates are not printed on the pages read: confirm them with the Social Insurance Services.

### Rule 11: Employer registration and new-hire notification

- **Employer registration**: "Every employer is obliged to register in the Register of Employers of the Social Insurance Services (SIS); before recruiting personnel." The application is form 01-001 of the YKA series, submitted to the local District Social Insurance Office. The registration number is used for paying contributions and in every communication with the Social Insurance Services ([Business in Cyprus](https://www.businessincyprus.gov.cy/social-insurance-registration-and-contributions/)).
- **New hires**: "Each employer notifies the Social Insurance Services of each employee recruitment no later than one (1) day before recruitment", only electronically through the ERGANI system. The paper "Declaration for the recruitment" was abolished from 13 September 2021 (same page).
- **Employee without a Social Insurance number**: the application for registration of an employed person is form 1-008 of the YKA series ([Social Insurance Services, registration of employees](https://www.mlsi.gov.cy/mlsi/sdg/sdg.nsf/All/DF541D1E90F75C56C22586A10042515C?OpenDocument)). The same form number is the self-employed registration form; Business in Cyprus says the self-employed number "is usually given within 1-2 weeks".

### Rule 12: Minimum wage

- Out of scope here. Use `cyprus-payroll`.

## Section 6: Tier 2 catalogue

When payroll or bank data is unclear or the client's position is uncertain, flag these situations for review.

### T2-1: State share and the Central Holiday Fund

- **Trigger**: a request for the full funding picture including the state share, or for total employer cost where the Central Holiday Fund may apply. **Issue**: the state shares (table A for social insurance, table C for GHS) are not employer costs. The Central Holiday Fund applies only where the employer has no exemption, its rate rises with the leave entitlement, and it enlarges the base for the other contributions. **Action**: confirm the exemption status and the employee's leave entitlement before giving a total cost.

### T2-2: Self-employed occupational category

- **Trigger**: a self-employed client with no confirmed category amount. **Issue**: contributions are on estimated earnings by category unless the person asked to pay on actual earnings. **Action**: get the category amount or the actual-earnings election from the Social Insurance Services before computing.

### T2-3: GHS maximum across several income sources

- **Trigger**: employment plus pension, self-employment, dividends, interest or rent. **Issue**: GHS is on all income added together up to the single table D maximum, in a set priority order. Several payers may each withhold without seeing the total. The Tax Department refunds GHS "when the total income exceeds" the table D maximum "and a refund arises" (return guide for 2025). **Action**: reconcile total GHS against the table D maximum.

### T2-4: Residence, domicile and investment income

- **Trigger**: dividends, interest or rent for a person who may be non-resident or non-domiciled. **Issue**: GHS turns on tax residence, not domicile: a non-resident pays no GHS on dividends and interest (table C note). Special Defence Contribution is a separate tax. **Action**: confirm tax residence. Send Special Defence Contribution questions to `cy-non-dom` or `cyprus-income-tax`.

### T2-5: Contribution arrears and late charges

- **Trigger**: unpaid employer contributions from earlier months. **Issue**: the table F additional charge applies to the Social Insurance, Social Cohesion and Health Insurance funds. **Action**: do not quantify arrears without a Social Insurance Services statement. Refer.

### T2-6: 2025 versus 2026

- **Trigger**: a computation that spans the 2025 and 2026 boundary, or no year given. **Issue**: the weekly maximum in table B applies from 5 January 2026, the monthly maximum from 1 January 2026. The 2026 income tax scale differs from 2025. **Action**: confirm the period and get the earlier figures from the Social Insurance Services and the Tax Department.

### T2-7: Employees past pensionable age

- **Trigger**: an employee aged 65 or over. **Issue**: the employer's Social Insurance Fund contributions stop at 65 unless the employee does not yet qualify for a pension, and never continue after 68 (Rule 1). **Action**: confirm the employee's pension entitlement before stopping contributions. The page says nothing about the other funds or GHS: refer if they matter.

## Section 7: Excel working paper template

When producing a Cyprus contributions computation, structure the working paper like this:

~~~
CYPRUS SOCIAL CONTRIBUTIONS COMPUTATION: WORKING PAPER
Client: [name]
Tax year: 2026
Prepared: [date]

INPUT DATA
  Employment status:              [Employee / Employer / Self-employed / Voluntary]
  Pay period:                     [Monthly / Weekly]
  Gross pay for the period:       [amount]
  Above the table B maximum:      [YES/NO]
  Total yearly income (GHS):      [amount]
  Above the table D maximum:      [YES/NO]
  Cyprus tax resident:            [YES/NO]
  Central Holiday Fund exemption: [YES/NO]
  Occupational category (SE):     [category and amount, or actual-earnings election]

EMPLOYEE DEDUCTIONS (per period)
  Social insurance (table A):     [amount]  (base = lower of pay and table B maximum)
  GHS (table C employee rate):    [amount]  (stop when yearly income passes table D)

EMPLOYER COSTS (per period)
  Central Holiday Fund (table E): [amount]  (only if NOT exempt; add to earnings first)
  Social insurance (table A):     [amount]  (capped at table B)
  GHS (table C employer rate):    [amount]  (within table D)
  Social Cohesion (table A):      [amount]  (NO cap: total earnings)
  Redundancy (table A):           [amount]  (capped at table B)
  Human Resources Dev. (table A): [amount]  (capped at table B)
  Total employer cost:            [sum of the amounts above]

SELF-EMPLOYED (if applicable)
  Insurable income:               [category amount or actual earnings]
  Social insurance (table A):     [amount]
  GHS (table C self-employed):    [amount]
  Payment:                        every three months

PAYMENT SCHEDULE
  Employer monthly remittance:    end of the following month
  Self-employed:                  every three months (dates from the Social Insurance Services)

REVIEWER FLAGS
  [List any Tier 2 flags here]

CONSERVATIVE DEFAULTS APPLIED
  [List any defaults applied and their effect]
~~~

## Section 8: Bank statement reading guide

### How Cyprus contribution debits appear on bank statements

**Bank of Cyprus:**
- Description: "DEPARTMENT OF SOCIAL INSURANCE", "SOCIAL INSURANCE", "GESY", "HIO"
- Timing: monthly for employers (end of the following month); every three months for the self-employed
- Amount: the monthly employer remittance may bundle social insurance, GHS and the employer-only funds

**Hellenic Bank:**
- Description: "SOC INS", "GESY HIO", "GENERAL HEALTHCARE"
- Timing: same monthly and three-monthly cycle
- Amount: may appear as separate social insurance and GHS lines or as one remittance

**Astrobank / Eurobank Cyprus / Alpha Bank Cyprus:**
- Description: "SOCIAL INSURANCE", "GESY", or Greek references (ΚΟΙΝΩΝΙΚΕΣ ΑΣΦΑΛΙΣΕΙΣ, ΓΕΣΥ)
- Timing: same cycle

These bank descriptions are observed patterns, not official text. Confirm against the client's own statements.

**Key identification tips:**
1. Contribution payments are outgoing debits. Incoming Social Insurance Services credits are benefits or pensions received.
2. Employer remittances recur monthly and track total payroll.
3. When a breakdown is needed, separate social insurance (capped at table B) from GHS (capped at table D) from Social Cohesion (no cap).
4. Do not confuse Tax Department, PAYE or Special Defence Contribution debits with social insurance contributions.
5. Arrears and late-charge payments may appear as irregular lump sums with "ARREARS" or "SURCHARGE" in the reference.

### Greek-language terminology

**Greek-language terminology table**

| Greek term | Meaning |
| --- | --- |
| Κοινωνικές Ασφαλίσεις | Social Insurance |
| Υπηρεσίες Κοινωνικών Ασφαλίσεων | Social Insurance Services |
| ΓΕΣΥ / Γενικό Σύστημα Υγείας | GHS / General Healthcare System (GESY) |
| Οργανισμός Ασφάλισης Υγείας | Health Insurance Organisation (HIO) |
| Ανώτατο όριο ασφαλιστέων αποδοχών | Maximum insurable earnings |
| Ταμείο Ετησίων Αδειών μετ' Απολαβών | Annual Paid Leave Fund (Central Holiday Fund) |
| Ταμείο Πλεονάζοντος Προσωπικού | Redundancy Fund |
| Τμήμα Φορολογίας | Tax Department |
| Μισθός | Salary |
| Σύνταξη | Pension |
| Άμυνα | Defence (Special Defence Contribution) |

## Section 9: Onboarding fallback

If the client provides only a bank statement and no other information:

1. **Scan for contribution debits**: find every outgoing payment matching Section 3 (Social Insurance Services, GESY/HIO, employer-only funds).
2. **Separate social insurance from GHS from employer funds**: where the bank shows separate lines, tag each; where bundled, note that a breakdown is needed.
3. **Infer the profile, then confirm it**:
   - Monthly recurring Social Insurance Services and GESY debits suggest an employer. Do not back out gross pay from a single ratio: the bases differ (Rule 5).
   - Debits every three months with no monthly pattern suggest a self-employed person.
4. **Flag for review**: "Contribution classification derived from bank statement amounts only. Employment status, occupational category, Central Holiday Fund status and total income have not been checked. Confirm before relying on these figures."

## Section 10: Reference material

### Key thresholds

**Key thresholds table**

| Threshold | Where |
| --- | --- |
| Maximum insurable earnings 2026, monthly and weekly | Table B |
| GHS annual maximum per person, all income together | Table D |
| Social Cohesion Fund | No ceiling (table E source) |
| Employer Social Insurance Fund contributions end | Pensionable age 65, never after 68 (Rule 1) |

### Forms and filings

**Forms table**

| Form / filing | Purpose | Deadline | Source |
| --- | --- | --- | --- |
| Monthly employer contributions | Employer and employee social insurance, GHS on salary, and the employer-only funds | End of the calendar month after the month the contributions are for | Social Insurance Services deadlines page (Rule 9) |
| Self-employed contributions | Self-employed social insurance (which "now include a contribution to the National Health System") | Every three months | Business in Cyprus (Rule 10) |
| Employer registration, form 01-001 (YKA series) | Register as an employer and get a registration number | Before recruiting staff | Business in Cyprus (Rule 11) |
| New-hire notification through ERGANI | Notify each recruitment | No later than one day before the employee starts | Business in Cyprus (Rule 11) |
| Registration of an employed or self-employed person, form 1-008 (YKA series) | Social Insurance number for a person who has none | Before contributions are reported | Social Insurance Services registration page (Rule 11) |
| Monthly PAYE return | Income tax withheld | End of the month after the month of withholding | Tax Department calendar (Rule 8) |
| Annual PAYE return for 2026 | Tax and contributions withheld in the year | 31 March 2027 | Tax Department calendar (Rule 8) |
| TD59A | Employee's declaration of deductions to the employer; GHS withholding note | Start of employment or year | TD59A 2026 (table D) |

### Penalties

**Penalties table**

| Penalty | Detail | Source |
| --- | --- | --- |
| Late payment of employer contributions | Additional charge on contributions due to the Social Insurance, Social Cohesion and Health Insurance funds: table F first-month rate, rising by 3 points a month to the table F maximum | Table F |
| Late registration or failure to register | Not printed on the pages read: refer | None |
| Late filing or late payment of income tax | Out of scope: use `cyprus-income-tax` | None |

### Test suite

- Test 1 (ordinary, hypothetical): employee on the Example 1 monthly gross pay, employer exempt from the Central Holiday Fund. Expected: the Example 1 table, line by line.
- Test 2 (boundary, hypothetical): employee on the Example 2 monthly gross pay, above the table B maximum. Expected: social insurance, Redundancy and Human Resources Development on the table B maximum only; GHS and Social Cohesion on the full pay; the Example 2 table.
- Test 3 (GHS maximum, hypothetical): a Cyprus tax resident employee whose total income for the year is EUR 200,000. Expected: GHS on the table D maximum only, at the employee rate: EUR 4,770.00 for the year (Case C). Nothing on the excess. Rate and maximum: [TD59A 2026](https://www.gov.cy/media/sites/167/2026/02/IR59_2026_English__.pdf).
- Test 4 (exclusion): a person who is not a Cyprus tax resident receives dividends and interest from a Cyprus company and bank. Expected: no GHS on the dividends and interest (table C note).
- Test 5 (exclusion): an employee aged 66 who already qualifies for the statutory pension. Expected: no employer Social Insurance Fund contributions (Rule 1). Refer for GHS and the other funds.
- Test 6 (registration): an employer hires its first employee. Expected: register with form 01-001 (YKA series) before recruiting; notify the hire through ERGANI no later than one day before the start; form 1-008 (YKA series) if the employee has no Social Insurance number.

### Prohibitions

- NEVER use a self-employed rate other than the table A self-employed share for 2026.
- NEVER use the old Social Insurance Services rates that still appear on some government pages (an employee share below table A, or GHS first-phase rates). They are stale.
- NEVER apply the table B maximum to GHS or to the Social Cohesion Fund.
- NEVER apply the Social Cohesion Fund to capped earnings only: it is on total earnings.
- NEVER include the Central Holiday Fund without confirming the employer has no exemption, and never leave it out without asking.
- NEVER quote a single combined percentage as the employer's cost.
- NEVER charge GHS on dividends or interest of a person who is not a Cyprus tax resident.
- NEVER compute self-employed contributions without the category amount or the actual-earnings election.
- NEVER compute arrears or late charges without a Social Insurance Services statement.
- NEVER present a contribution figure as final: label it estimated and direct the client to their Social Insurance Services and HIO statements.

## The method, step by step

1. Fix the period and confirm it is 2026. Use the 2026 maximum in the [Social Insurance Services notice](https://sisweb.mlsi.gov.cy/anotato2025/) (Social Insurance (Contributions) Regulations, Regulation 8(1) and (2)): monthly from 1 January 2026, weekly from 5 January 2026.
2. Classify the person: employee, self-employed, voluntary contributor, pensioner or income earner ([Business in Cyprus](https://www.businessincyprus.gov.cy/social-insurance-registration-and-contributions/); [Health Insurance Organisation](https://www.gesy.org.cy/en-us/hiofinancing)).
3. For an employee, ask whether the employer is exempt from the Central Holiday Fund. If it is not, work out that contribution and add it to the earnings ([Social Insurance Services, contributions](https://www.mlsi.gov.cy/mlsi/sdg/sdg.nsf/All/EA4F396F80C4BAA8C22586A10042659F?OpenDocument)).
4. Cap the earnings at the table B maximum and apply the employee and employer social insurance shares and the Redundancy and Human Resources Development rates in table A ([Business in Cyprus](https://www.businessincyprus.gov.cy/social-insurance-registration-and-contributions/)). Check the employee's age against Rule 1 ([Social Insurance Services, general information](https://www.mlsi.gov.cy/mlsi/sdg/sdg.nsf/All/A0E4DA6A3979A4EAC22586A100418A7A?OpenDocument)).
5. Apply the Social Cohesion Fund rate to total earnings, with no cap ([Social Insurance Services, contributions](https://www.mlsi.gov.cy/mlsi/sdg/sdg.nsf/All/EA4F396F80C4BAA8C22586A10042659F?OpenDocument)).
6. Apply GHS at the table C rates under the General Healthcare System Law, on actual pay and other income, stopping when the person's total yearly income passes the table D maximum ([TD59A 2026](https://www.gov.cy/media/sites/167/2026/02/IR59_2026_English__.pdf); [Health Insurance Organisation](https://www.gesy.org.cy/en-us/hiofinancing)). For a person who is not a Cyprus tax resident, charge GHS only on income, earnings and pensions that derive from the Republic of Cyprus, and leave out dividends and interest (table C note).
7. For the self-employed, apply the table A self-employed share to the category amount or actual earnings, and the table C self-employed GHS rate; payment is every three months ([Business in Cyprus](https://www.businessincyprus.gov.cy/social-insurance-registration-and-contributions/)).
8. Pay employer contributions by the end of the month after the month they are for; late payment carries the table F charge ([Social Insurance Services, deadlines](https://www.mlsi.gov.cy/mlsi/sdg/sdg.nsf/All/D5322D5E5CD6F735C22586A10044EC34)). PAYE income tax goes to the Tax Department on its own calendar ([Tax Department deadlines](https://www.gov.cy/mof-tax/prothesmies/)).
9. For the employee's income tax return, contributions count toward the one-fifth limit in the TD59A ([TD59A 2026](https://www.gov.cy/media/sites/167/2026/02/IR59_2026_English__.pdf)). Hand the rest of the income tax computation to `cyprus-income-tax`.

## Ask the client first

- Are you an employee, self-employed, both, or a voluntary contributor? (Rates and bases differ.)
- What is your gross pay, and are you paid monthly or weekly? (The table B maximum differs by pay period and start date.)
- What is your total income for the year from all sources, including pension, rent, interest and dividends, and are you a Cyprus tax resident? (The GHS maximum and GHS on dividends and interest turn on it.)
- For an employer: is the business exempt from the Central Holiday Fund, and how many weeks of annual leave does the employee get? (The fund applies only without an exemption, its rate rises with leave, and it enlarges the base.)
- For a self-employed person: what is your occupational category, and have you asked to pay on actual earnings? (That is the base.)
- Is the employee 65 or over, or insured in another EU or EEA country or Switzerland? (Employer Social Insurance Fund contributions may stop at 65; cross-border cases are referred.)

## When to refuse or refer

- Self-employed contributions without the category amount or actual-earnings election (R-CY-SC-1).
- Arrears or late charges without a Social Insurance Services statement (R-CY-SC-2).
- Special Defence Contribution, domicile and income tax penalties (R-CY-SC-3, R-CY-SC-4): use `cy-non-dom` or `cyprus-income-tax`.
- Any period other than 2026 (R-CY-SC-5).
- Cross-border cases: insured abroad, posted workers, employers registered in another EU or EEA state or Switzerland (R-CY-SC-6).
- Whether a ceiling applies to self-employed income, and the exact self-employed payment dates: not printed on the pages read.
- Central Holiday Fund rate for leave above 40 days (five-day week) or 48 days (six-day week): the page says only that it "is increased accordingly".
- Minimum wage questions: use `cyprus-payroll`.

## Sources

- Business in Cyprus (government one-stop shop), Social Insurance Registration and Contributions: https://www.businessincyprus.gov.cy/social-insurance-registration-and-contributions/
- Social Insurance Services, notice on the maximum insurable earnings for 2026 (December 2025): https://sisweb.mlsi.gov.cy/anotato2025/
- Health Insurance Organisation, GHS Financing and Global Budget (contribution rates and annual maximum): https://www.gesy.org.cy/en-us/hiofinancing
- Tax Department, TD59A 2026 (English), declaration for claiming tax deductions, with the GHS withholding note: https://www.gov.cy/media/sites/167/2026/02/IR59_2026_English__.pdf
- Social Insurance Services, Single Digital Gateway, Contributions: https://www.mlsi.gov.cy/mlsi/sdg/sdg.nsf/All/EA4F396F80C4BAA8C22586A10042659F?OpenDocument
- Social Insurance Services, Single Digital Gateway, Annual Leave, Obligations of the Employer: https://www.mlsi.gov.cy/mlsi/sdg/sdg.nsf/All/00DDEF169CC27CAEC22586B7003F35FE?OpenDocument
- Social Insurance Services, Single Digital Gateway, Legislation: https://www.mlsi.gov.cy/mlsi/sdg/sdg.nsf/All/335C7DB77BE6657AC22586A1004509A2?OpenDocument
- Social Insurance Services, Single Digital Gateway, Deadlines for payment of contributions: https://www.mlsi.gov.cy/mlsi/sdg/sdg.nsf/All/D5322D5E5CD6F735C22586A10044EC34
- Social Insurance Services, Single Digital Gateway, General information: https://www.mlsi.gov.cy/mlsi/sdg/sdg.nsf/All/A0E4DA6A3979A4EAC22586A100418A7A?OpenDocument
- Social Insurance Services, Single Digital Gateway, Registration of Employees: https://www.mlsi.gov.cy/mlsi/sdg/sdg.nsf/All/DF541D1E90F75C56C22586A10042515C?OpenDocument
- Tax Department, Guide for the completion of the income tax return for individuals 2025: https://www.gov.cy/media/sites/167/2026/06/Guide-for-completion-of-tax-return-2025.pdf
- Tax Department, Tax Reform 2026 FAQs (11 May 2026): https://www.gov.cy/media/sites/167/2026/05/FAQs-110526.pdf
- Tax Department, deadline calendar: https://www.gov.cy/mof-tax/prothesmies/

## Disclaimer

This Guide and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this Guide. All outputs must be reviewed and signed off by a qualified professional (such as a CPA, EA, tax attorney, or equivalent licensed practitioner in your jurisdiction) before filing or acting upon.

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
