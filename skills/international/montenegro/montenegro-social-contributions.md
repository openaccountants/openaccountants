---
name: montenegro-social-contributions
description: "Montenegro compulsory social insurance contributions for 2026 under the Law on Compulsory Social Insurance Contributions as amended by 160/25. Covers who pays (employees, entrepreneurs, employed people with a supplementary business, board members, contract recipients, farmers, clergy, posted and foreign workers), the 2026 rates (pension and disability 10% employee and 0% employer, unemployment 0.5% plus 0.5%, entrepreneurs 1%, Labour Fund 0.2%, additional service 6% to 28%), the bases (gross pay, the 60/100/150% turnover bands on the 2025 average gross of EUR 1,206, farmers 20% and 12%), exclusions such as zimnica up to EUR 844.20, the digital-nomad relief, monthly and quarterly deadlines, the IOPPD report, fines, default interest, and the annual pension ceiling and refund (2025 ceiling EUR 75,453). Salary income tax and municipal surtax are in the payroll skill."
version: 0.4
jurisdiction: ME
tax_year: 2026
last_updated: 2026-10-30
review_status: pending_review
trust_label: Built by Michael Cutajar and the OpenAccountants team
depends_on:
  - social-contributions-workflow-base
category: international
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Montenegro social contributions (doprinosi), 2026

This skill computes Montenegrin compulsory social insurance contributions for 2026. The law is the Law on Compulsory Social Insurance Contributions (Zakon o doprinosima za obavezno socijalno osiguranje, "the Law"), consolidated by the Ministry of Finance through amendment 160/25. Amendment 160/25 applies from 1 January 2026 (160/25 art. 8). Salary income tax and the municipal surtax (prirez) are in the [payroll skill](montenegro-payroll.md); entrepreneurs' income tax is in the [income tax skill](montenegro-income-tax.md).

## Who this applies to

The Law has two contributions only: pension and disability insurance (PIO) and unemployment insurance (Law art. 2). PIO goes to the Pension and Disability Insurance Fund, unemployment to the Employment Agency (art. 3). The health insurance contribution has been removed from the Law (arts. 6, 10 and 17 deleted). The IOPPD instructions keep the health columns only for periods up to December 2021 (IOPPD rulebook, instructions to columns 10 and 13). Old tables showing about 24% employee and 10% employer contributions, or any health contribution, are out of date.

PIO is paid by (art. 5(1)):

- employees, people doing temporary and occasional work, and elected or appointed officials paid a salary (items 1 to 3);
- members of boards of directors and management boards paid a fee (item 4);
- posted workers, Montenegrin citizens working in Montenegro for foreign or international bodies, Montenegrin citizens employed abroad, and foreign nationals working in Montenegro for foreign or domestic employers, unless a treaty says otherwise (items 5 to 10);
- people receiving unemployment cash benefit (item 11);
- entrepreneurs and people carrying on a professional activity as their main occupation (item 12);
- people paid under a contract for work, author's contract or similar, if not insured on another basis (item 13);
- clergy and religious officials (item 14), farmers (item 15);
- from 2026, employed people who also carry on a supplementary business (dopunska preduzetnička djelatnost) (item 16, added by 160/25 art. 2; defined in art. 4(1)(11a)).

Unemployment contribution is paid only by the groups in art. 7(1): employees and the employee-like groups, and entrepreneurs and professionals in their main occupation (item 9). Board members, contract recipients, farmers, clergy and supplementary entrepreneurs do not appear in art. 7, so they pay PIO only.

An employer also pays an additional PIO contribution for jobs where service counts at an increased rate (art. 8(1)); an entrepreneur pays it on their own increased-rate service (art. 8(2)).

Terms you will see: doprinosi (contributions); PIO, penzijsko i invalidsko osiguranje (pension and disability insurance); osiguranje od nezaposlenosti (unemployment insurance); Fond rada (Labour Fund); doprinos iz osnovice (contribution withheld from the insured person's pay); doprinos na osnovicu (contribution paid by the payer on top); zimnica (winter-supplies payment); IOPPD (monthly report of calculated and paid taxes and contributions).

## Rates, bands and thresholds

| Item | Amount | Tax year | Source |
|---|---|---|---|
| PIO, employee and employee-like groups | 10.0% employee, 0% employer | 2026 | [Law art. 15(1)](https://wapi.gov.me/download/97253561-f373-4456-a024-b15f6596a0f2?version=1.0) |
| PIO, board members, citizens employed abroad, entrepreneurs, contract recipients, farmers, supplementary entrepreneurs | 10.0%, borne by the insured person | 2026 | [Law art. 15(2)](https://wapi.gov.me/download/97253561-f373-4456-a024-b15f6596a0f2?version=1.0); [160/25 art. 4](https://wapi.gov.me/download/9c7ab8f6-6971-48cb-9ac0-4d6f87ac48bb?version=1.0) |
| PIO, unemployment benefit recipients | 10.0%, paid by the Employment Agency | 2026 | [Law art. 15(3)](https://wapi.gov.me/download/97253561-f373-4456-a024-b15f6596a0f2?version=1.0) |
| PIO, clergy | 10.0%, paid by the religious community | 2026 | [Law art. 15(4)](https://wapi.gov.me/download/97253561-f373-4456-a024-b15f6596a0f2?version=1.0) |
| Unemployment, employees and employee-like groups | 0.5% employee, 0.5% employer | 2026 | [Law art. 18(1)](https://wapi.gov.me/download/97253561-f373-4456-a024-b15f6596a0f2?version=1.0) |
| Unemployment, entrepreneurs and main-occupation professionals | 1%, borne by the insured person | 2026 | [Law art. 18(2)](https://wapi.gov.me/download/97253561-f373-4456-a024-b15f6596a0f2?version=1.0) |
| Labour Fund (Fond rada), employer | 0.2% of gross pay | 2026 | [Instruction art. 5](https://wapi.gov.me/download/f73befc2-975e-42d9-af00-4d5de0a3172d?version=1.0); [IOPPD instructions, column 15](https://wapi.gov.me/download/28aa7760-8d39-440d-8874-1ffcc5773095?version=1.0) |
| Ordinary employee total / employer total | 10.5% / 0.7% of gross pay | 2026 | Sum of the rows above |
| Additional PIO for increased-rate service (12 months counted as 14 / 15 / 16 / 18 / 24) | 6% / 9% / 12% / 18% / 28%, paid by employer or entrepreneur | 2026 | [Law art. 16](https://wapi.gov.me/download/97253561-f373-4456-a024-b15f6596a0f2?version=1.0) |
| Entrepreneur and supplementary-entrepreneur monthly base, annual turnover up to EUR 9,000 / up to EUR 15,000 / over EUR 15,000 | 60% / 100% / 150% of prior-year average monthly gross pay (higher base may be elected for PIO) | 2026 | [Law art. 9 items 7 and 11, art. 11 item 5](https://wapi.gov.me/download/97253561-f373-4456-a024-b15f6596a0f2?version=1.0); [160/25 art. 3](https://wapi.gov.me/download/9c7ab8f6-6971-48cb-9ac0-4d6f87ac48bb?version=1.0) |
| Average monthly gross pay in 2025 (the "prior-year average" for 2026) | EUR 1,206 | 2026 | [Law art. 4(1)(23)](https://wapi.gov.me/download/97253561-f373-4456-a024-b15f6596a0f2?version=1.0); [MONSTAT release, 30 Jan 2026](https://www.monstat.org/cg/novosti.php?id=4638) |
| Entrepreneur monthly base at 60% / 100% / 150% | EUR 723.60 / 1,206.00 / 1,809.00 | 2026 | Computed from the two rows above |
| Farmer base: general / own mandatory | 20% / 12% of prior-year average gross pay (EUR 241.20 / 144.72); the difference is paid from the state budget | 2026 | [Law art. 9 item 10, art. 9a](https://wapi.gov.me/download/97253561-f373-4456-a024-b15f6596a0f2?version=1.0) |
| Zimnica excluded from contributions | Up to 70% of prior-year average monthly gross pay (EUR 844.20) | 2026 | [Law art. 18a(2)](https://wapi.gov.me/download/97253561-f373-4456-a024-b15f6596a0f2?version=1.0); [160/25 art. 5](https://wapi.gov.me/download/9c7ab8f6-6971-48cb-9ac0-4d6f87ac48bb?version=1.0) |
| Lowest monthly base, employees | Gross basic salary for the qualification category under the General Collective Agreement | 2026 | [Law arts. 4(1)(21), 9 item 1, 11 item 1](https://wapi.gov.me/download/97253561-f373-4456-a024-b15f6596a0f2?version=1.0) |
| Highest annual PIO base | EUR 75,453 | 2025 | [Rulebook 134/2025 art. 1](https://www.sluzbenilist.me/propisi/387933/download); [Law art. 14(3)-(4)](https://wapi.gov.me/download/97253561-f373-4456-a024-b15f6596a0f2?version=1.0) |
| Highest annual PIO base | Set each year by Ministry of Finance rulebook; 2026 rulebook not yet published | 2026 | [Law art. 14(3)-(4)](https://wapi.gov.me/download/97253561-f373-4456-a024-b15f6596a0f2?version=1.0) |
| Payment deadline, employer and payer contributions | By the 15th of the month for the previous month | 2026 | [Law art. 21(1), (5)](https://wapi.gov.me/download/97253561-f373-4456-a024-b15f6596a0f2?version=1.0) |
| Request to keep paying during temporary deregistration | Within 5 working days of deregistration | 2026 | [Law art. 20(2)](https://wapi.gov.me/download/97253561-f373-4456-a024-b15f6596a0f2?version=1.0) |
| Refund of PIO above the annual ceiling: claim / payment | Claim by end of the year after the year paid; refund within 30 days of the decision | 2026 | [Law art. 22(3)](https://wapi.gov.me/download/97253561-f373-4456-a024-b15f6596a0f2?version=1.0); [Refund rulebook 107/23 art. 4](https://www.sluzbenilist.me/propisi/362476/download) |
| Fine, legal-person payer / its responsible person / entrepreneur payer | EUR 2,000-20,000 / 500-1,000 / 1,000-6,000 | 2026 | [Law art. 26](https://wapi.gov.me/download/97253561-f373-4456-a024-b15f6596a0f2?version=1.0) |
| Fine, individual who self-pays late | EUR 250-2,000 | 2026 | [Law art. 27](https://wapi.gov.me/download/97253561-f373-4456-a024-b15f6596a0f2?version=1.0) |
| Default interest, 1 January to 17 July 2026 | 0.03% a day | 2026 | [Tax Administration Law art. 95(1), text before 104/26](https://wapi.gov.me/download/2dd530ac-eec4-4d0c-9d8f-0c9e7ebc5b86?version=1.0) |
| Default interest, 18 July to 31 December 2026 | 5.4% a year | 2026 | [Tax Administration Law art. 95](https://wapi.gov.me/download/8e3ee8d0-f10c-453a-90ad-6439ac07aca2?version=1.0); [Poreska uprava decision, 24 Jul 2026](https://wapi.gov.me/download/6d6ec964-3dd6-4588-b81a-a5affc153f6e?version=1.0) |

The 0.7% employer total excludes the additional service contribution, the disability-employment levy and Chamber of Economy dues, which the [payroll skill](montenegro-payroll.md) covers.

## The base

### Employees and employee-like groups

The base is gross pay: pay for work and time at work, increased pay, salary compensation and other receipts under law, collective agreement or employment contract on which personal income tax is paid (art. 3a(1)). It includes payments tied directly to work and performance, such as fees for working bodies, groups and teams (art. 3a(2)). The base cannot be lower than the lowest monthly base: the gross basic salary set by the General Collective Agreement for the employee's qualification category (arts. 4(1)(21), 9 item 1, 11 item 1). The same gross base is used for the withheld and the employer contributions (Instruction arts. 4 and 5).

Other bases:

- posted workers: the pay they would earn in Montenegro for the same or similar work, not below the lowest base (art. 9 item 3);
- Montenegrin citizens working in Montenegro for foreign or international bodies: pay actually received, not below the lowest base (art. 9 item 4);
- Montenegrin citizens employed abroad: set by the ministry for pension insurance, not below the lowest base (art. 9 item 5);
- board members: the board fee (art. 9 item 2);
- contract recipients (item 13): taxable income from independent activity under the personal income tax law, not the gross cash paid (art. 9 item 8);
- unemployment benefit recipients: the benefit (art. 9 item 6);
- clergy: set by the ministry by post, education and years of service, not below the lowest base (art. 9 item 9);
- sick pay: the sick-pay compensation (art. 12); maternity and half-time work: the compensation under the social and child protection law (art. 13).

### Entrepreneurs and supplementary entrepreneurs

An entrepreneur taxed on a yearly lump sum uses taxable income set under the income tax law as the base (art. 9 item 7; art. 11 item 5). An entrepreneur taxed on actual income uses a monthly base fixed by realised or estimated annual turnover: up to EUR 9,000, 60% of prior-year average monthly gross pay; up to EUR 15,000, 100%; over EUR 15,000, 150%. For PIO the entrepreneur may elect a higher base (art. 9 item 7). The unemployment base uses the same three bands without the election (art. 11 item 5). For 2026 the bands give EUR 723.60, 1,206.00 and 1,809.00 a month (2025 average gross EUR 1,206, MONSTAT).

From 1 January 2026 an employed person running a supplementary business pays PIO at 10% on the same turnover-banded base, with the same right to elect a higher base (art. 9 item 11; 160/25 arts. 3, 4 and 8). That PIO is on top of the PIO on their salary. No unemployment contribution is due on the supplementary business, because art. 7 does not list that group.

### Farmers

A farmer is someone farming as their only or main occupation who is not liable to personal income tax on it (art. 4(1)(18)). The base is 20% of prior-year average monthly gross pay, with an option to pay on a higher base (art. 9 item 10). For a farmer entered in the Register of Farmers, the farmer's own mandatory base is 12% of that average; the state budget pays the difference between the 20% and 12% bases, based on tax-authority data (art. 9a).

### Several incomes and the annual ceiling

A person with several insured incomes pays PIO on each of them (art. 14(1)). PIO stops being due only through the annual ceiling: the highest annual PIO base, adjusted each year by the growth of average pay and fixed by a Ministry of Finance rulebook (art. 14(3)-(4)). The ceiling for 2025 is EUR 75,453 (Rulebook 134/2025, in force 28 November 2025). The 2025 rulebook was published on 21 November 2025, so the 2026 figure is expected late in 2026. The ceiling is annual: do not split it into a monthly cap and do not stop payroll withholding when it is reached. The excess is recovered by refund after the year end (see Deadlines). The ceiling applies to PIO only; unemployment and Labour Fund contributions are not refunded under it.

### Exclusions and reliefs

- Receipts up to the amounts that are free of personal income tax under the income tax law carry no contributions (art. 18a(1)).
- No contributions on severance pay, solidarity and social aid, zimnica up to 70% of prior-year average monthly gross pay (EUR 844.20 for 2026), separate-living allowance, newborn-child allowance and jubilee awards (art. 18a(2), as amended by 160/25 art. 5; before 2026 the zimnica reference was the minimum wage).
- No contributions on benefits in kind, gifts or other benefits given to an employee, unless they are given in place of unpaid salary (art. 18a(3)).
- Montenegrin diplomatic staff abroad: no contributions on the special allowances and cost reimbursements listed in art. 18a(4).
- No contributions on transfer income and other income of professional and amateur athletes (art. 18b).
- A person with digital-nomad status under the foreigners law, earning employment or self-employment income from an employer not registered in Montenegro, is exempt (art. 18d, as replaced by 160/25 art. 6). Remote work without that status does not qualify.
- Art. 18c (the new-hire PIO relief) has expired; it applied up to 31 December 2023 (art. 31a).

### Suspension

Contributions are suspended while an employee's employment is formally suspended under labour law (art. 19). An entrepreneur or main-occupation professional who temporarily deregisters the activity pays nothing for that period, unless they apply to keep paying within five working days of deregistration (art. 20). Having no revenue is not a deregistration.

### Historic pay and court awards

Contributions on pay awarded by a court decision, court settlement or labour-dispute settlement are calculated and paid when the award is paid, at the rate in force on the day the pay should have been paid (art. 29b).

## Deadlines and filing

| Who | Who calculates and pays | Deadline | Source |
|---|---|---|---|
| Employees and employee-like groups, unemployment contributions of art. 7 items 1-8, sick pay and maternity bases, additional PIO for employees | Employer or payer | By the 15th for the previous month | Law art. 21(1) |
| Board members and contract recipients | Payer of the fee | By the 15th for the previous month | Law art. 21(5) |
| Montenegrin citizens employed abroad | The insured person | By the 15th of the month after each calendar quarter | Law art. 21(2) |
| Unemployment benefit recipients | Employment Agency | When the benefit is paid | Law art. 21(3) |
| Entrepreneurs, professionals, supplementary entrepreneurs, own additional PIO | The insured person | In the same way and at the same time as their personal income tax | Law art. 21(4); 160/25 art. 7 |
| Clergy | Religious community | By the 15th of the month after each quarter | Law art. 21(6) |
| Farmers | The farmer, on a tax-authority assessment | Quarterly, by the 15th of the month after each quarter | Law art. 21(8) |
| Staff of foreign embassies and organisations with immunity, if the payer does not pay | The employee | Within 5 days of receiving the pay | Law art. 21(7) |

For employees the Ministry's instruction is stricter than the 15th: tax and contributions are paid at the same time as the salary is paid; for pay in kind, by the last working day of the month in which it is received (Instruction art. 7). An employee who receives pay directly from abroad pays the tax and contributions within five days of receipt (Instruction art. 7).

**IOPPD.** Employers and other payers report tax and contributions on the IOPPD form (IOPPD rulebook arts. 2 and 4). It is filed with the tax authority electronically by the 15th of the month for the previous period (arts. 5 and 7). An amended IOPPD must contain the complete data for every person in that period, not only the changes (art. 6). Self-employed people (except for their own employees), farmers and clergy do not file IOPPD (art. 4). The payroll skill covers the form columns and codes.

**Annual PIO refund.** A person whose PIO was paid on a base above the annual ceiling may claim the excess back (Law art. 22(1)). The claim is made after the year ends, by the end of the following calendar year, to the tax authority, which decides by formal decision (art. 22(2)-(4)). So a 2025 refund is claimed during 2026, and a 2026 refund during 2027. The procedure is in the Ministry of Finance refund rulebook (107/23, which replaced 42/12):

- The refund is based on the contributions paid, as reported to the tax authority by the payer (rulebook art. 2).
- The claim is made on Form 1 (art. 3(1)). It asks for the regional office, the year, the insured person, the insurance basis (employment, self-employment, contract fee, or other such as board membership), the account to be credited and its bank, and the applicant's name, personal number (JMB), address and date.
- The competent office is: for employees, the employer's seat; for contract recipients, the person's residence; for board members, the payer's seat; for the self-employed, their place of tax registration (art. 3(2)).
- The regional office decides by formal decision and pays within 30 days of the decision (art. 4(1)-(2)).
- With several insurance bases, the refund is made on the basis whose contributions were paid after the ceiling was reached (art. 4(3)). Build a dated schedule of every payment by basis to find it.

## Penalties and interest

Fines (Law arts. 26 and 27):

- A legal person that, as payer, fails to calculate, calculates wrongly, fails to withhold or fails to pay contributions by the 15th (art. 21(1) and (3)-(6)): EUR 2,000 to 20,000. Its responsible person, or the responsible person in a state or local body: EUR 500 to 1,000. An entrepreneur payer: EUR 1,000 to 6,000.
- An individual who does not pay on time where they pay their own contributions (art. 21(2), (7) and (8): citizens employed abroad, embassy staff, farmers): EUR 250 to 2,000.

Interest, assessment, collection, deadlines and limitation follow the tax procedure law, except that the limitation rule for PIO is not taken from it (Law art. 25). Under the Tax Administration Law, default interest runs daily from the day after the due date. The rate is the ECB main refinancing rate on the first day of the half-year plus three percentage points, set for each half-year and published by the tax authority (Tax Administration Law art. 95(1)-(5)). This half-year method applies from 18 July 2026 (104/26); until 17 July 2026 the rate was 0.03% a day (art. 95(1) before 104/26). For 18 July to 31 December 2026 it is 5.4% a year (Poreska uprava decision of 24 July 2026). No interest is charged on interest (art. 95(7)).

## Cross-border points

- **Posted workers** sent abroad by a Montenegrin employer pay PIO and unemployment, on the pay they would earn in Montenegro, unless they are compulsorily insured in the other state or a treaty provides otherwise (arts. 4(1)(5), 5(1)(5), 7(1)(5), 9 item 3).
- **Montenegrin citizens employed abroad** by a foreign employer are insured in Montenegro if they are not compulsorily insured abroad, or cannot use those rights outside that state, and were insured or resident in Montenegro just before leaving (art. 4(1)(6)). They pay PIO themselves quarterly (art. 21(2)) and file IOPPD (IOPPD rulebook art. 4(2)).
- **Foreign nationals** working in Montenegro for foreign employers, or for domestic employers under technical-cooperation agreements, pay unless a treaty provides otherwise or they are insured under another state's rules (art. 5(1)(8) and (10)). Those working for international organisations or foreign embassies pay only if a treaty provides for it (art. 5(1)(9)).
- **Montenegrin citizens working in Montenegro** for foreign embassies, international organisations or foreign employers pay unless a treaty provides otherwise (art. 5(1)(6)). If an employer with diplomatic immunity does not pay, the employee pays within five days of receiving the pay (art. 21(7)).
- **Residents receiving pay from abroad** file IOPPD themselves (IOPPD rulebook art. 4(7)) and pay within five days of receipt (Instruction art. 7).
- **Digital nomads** with status under the foreigners law, paid by an employer not registered in Montenegro, are exempt (art. 18d).
- Before applying any treaty exemption, obtain the certificate of coverage from the other state's insurer.

## Worked examples

All examples are full calendar months in 2026, in EUR, with the person's status already established, no elected higher base and no annual refund. Example 1 assumes gross pay above the lowest monthly base for the employee's category.

### 1. Ordinary employee, gross EUR 2,000

Employee PIO is 10% × 2,000 = 200 and employee unemployment 0.5% × 2,000 = 10, so EUR 210 is withheld (Law arts. 15(1), 18(1)). The employer pays unemployment 0.5% × 2,000 = 10 and Labour Fund 0.2% × 2,000 = 4, so EUR 14 on top (Law art. 18(1); Instruction art. 5). Employer PIO is 0%. Income tax and surtax are in the payroll skill.

```oa-check
name: Montenegro ordinary employee contributions
inputs:
  gross_base: 2000
steps:
  - employee_pio: gross_base * 0.10
  - employee_unemployment: gross_base * 0.005
  - employee_total: employee_pio + employee_unemployment
  - employer_unemployment: gross_base * 0.005
  - employer_labour_fund: gross_base * 0.002
  - employer_charges: employer_unemployment + employer_labour_fund
expected:
  employee_pio: 200
  employee_unemployment: 10
  employee_total: 210
  employer_unemployment: 10
  employer_labour_fund: 4
  employer_charges: 14
```

### 2. Entrepreneur on actual income, turnover EUR 8,500

Turnover is in the up-to-EUR-9,000 band, so the monthly base is 60% × 1,206 = 723.60 (Law art. 9 item 7, art. 11 item 5). PIO is 10% × 723.60 = 72.36 (art. 15(2)). Unemployment is 1% × 723.60 = 7.236, rounded to 7.24 (art. 18(2)). The monthly total is EUR 79.60, paid with the entrepreneur's income tax (art. 21(4)).

```oa-check
name: Montenegro principal entrepreneur contribution base
inputs:
  prior_average_gross: 1206
steps:
  - monthly_base: prior_average_gross * 0.60
  - pio: round(monthly_base * 0.10, 2)
  - unemployment: round(monthly_base * 0.01, 2)
  - total: pio + unemployment
expected:
  monthly_base: 723.60
  pio: 72.36
  unemployment: 7.24
  total: 79.60
```

### 3. Supplementary business alongside employment, turnover EUR 16,000

The person is employed (salary PIO EUR 200, as in example 1) and runs a supplementary business with turnover over EUR 15,000. The supplementary base is 150% × 1,206 = 1,809, and PIO on it is 10% × 1,809 = 180.90 (Law art. 9 item 11, art. 15(2); 160/25 arts. 3 and 4). No unemployment contribution is due on the business (art. 7). Total PIO for the month is EUR 380.90. Any excess over the annual ceiling is recovered by refund after the year end.

```oa-check
name: Montenegro supplementary entrepreneur pension
inputs:
  prior_average_gross: 1206
  employment_pio: 200
steps:
  - supplementary_base: prior_average_gross * 1.50
  - supplementary_pio: supplementary_base * 0.10
  - combined_pio_before_refund: employment_pio + supplementary_pio
expected:
  supplementary_base: 1809
  supplementary_pio: 180.90
  combined_pio_before_refund: 380.90
```

### 4. Registered farmer

The general base is 20% × 1,206 = 241.20 and the farmer's own base 12% × 1,206 = 144.72 (Law art. 9 item 10, art. 9a(1)). PIO on the general base is 24.12; the farmer pays 10% × 144.72 = 14.472, rounded to 14.47, and the budget pays the difference of 9.65 (art. 9a(2)-(3)). The tax authority assesses it and the farmer pays quarterly (art. 21(8)).

```oa-check
name: Montenegro registered farmer contribution allocation
inputs:
  prior_average_gross: 1206
steps:
  - general_base: prior_average_gross * 0.20
  - own_base: prior_average_gross * 0.12
  - total_pio: round(general_base * 0.10, 2)
  - own_pio: round(own_base * 0.10, 2)
  - budget_difference: total_pio - own_pio
expected:
  general_base: 241.20
  own_base: 144.72
  total_pio: 24.12
  own_pio: 14.47
  budget_difference: 9.65
```

### 5. Employee in a job where 12 months count as 15 months of service

Gross pay EUR 2,000. The employer pays additional PIO of 9% × 2,000 = 180 (Law art. 16 item 2), plus the ordinary 0.7% = 14, so EUR 194 on top of gross. The employee's withholding stays at EUR 210.

```oa-check
name: Montenegro additional credited service employer charge
inputs:
  gross_base: 2000
steps:
  - extra_pio: gross_base * 0.09
  - ordinary_employer_charges: gross_base * 0.007
  - specified_employer_charges: extra_pio + ordinary_employer_charges
expected:
  extra_pio: 180
  ordinary_employer_charges: 14
  specified_employer_charges: 194
```

### 6. Zimnica payment of EUR 800

The 2026 limit is 70% × 1,206 = 844.20 (Law art. 18a(2); 160/25 art. 5). The whole EUR 800 is free of contributions, with 44.20 of the limit unused. Income tax on it is a separate question for the payroll skill.

```oa-check
name: Montenegro 2026 zimnica contribution exclusion ceiling
inputs:
  prior_average_gross: 1206
  qualifying_payment: 800
steps:
  - exclusion_limit: prior_average_gross * 0.70
  - excluded_contribution_receipt: min(qualifying_payment, exclusion_limit)
  - headroom: exclusion_limit - excluded_contribution_receipt
expected:
  exclusion_limit: 844.20
  excluded_contribution_receipt: 800
  headroom: 44.20
```

## Ask the client first

1. What is each person's status: employee, board member, contract recipient, entrepreneur in main occupation, employee with a supplementary business, or farmer? This decides the base, the rate and whether unemployment applies.
2. For entrepreneurs: are you taxed on actual income or on a yearly lump sum, what is your realised or estimated annual turnover, and have you elected a higher base?
3. For employees: what is the qualification category under the General Collective Agreement, and does any job count service at an increased rate?
4. Does anyone have income from more than one source, or total insured income above the annual ceiling (EUR 75,453 for 2025)? If so, a refund claim may be due by the end of the following year.
5. Is anyone posted abroad, employed by a foreign or international employer, paid from abroad, or holding digital-nomad status, and is there a certificate of coverage from another state?
6. Which payments are not ordinary salary: zimnica, severance, jubilee awards, aid, or benefits in kind, and do any of them replace unpaid salary?

## Sources

| Source | URL | Read on |
|---|---|---|
| Law on Compulsory Social Insurance Contributions, Ministry of Finance consolidation through 160/25 (arts. 1-27, 29b, 31a) | https://wapi.gov.me/download/97253561-f373-4456-a024-b15f6596a0f2?version=1.0 | 2026-10-30 |
| Law amending the Contributions Law, Sl. list CG 160/25 of 30 Dec 2025 (arts. 1-8, applies from 1 Jan 2026) | https://wapi.gov.me/download/9c7ab8f6-6971-48cb-9ac0-4d6f87ac48bb?version=1.0 | 2026-10-30 |
| Instruction on calculating and paying tax and contributions on employment income, through 103/24 (arts. 4, 5, 7) | https://wapi.gov.me/download/f73befc2-975e-42d9-af00-4d5de0a3172d?version=1.0 | 2026-10-30 |
| Rulebook on the IOPPD form, consolidated through 124/24 (arts. 2, 4-7 and column instructions) | https://wapi.gov.me/download/28aa7760-8d39-440d-8874-1ffcc5773095?version=1.0 | 2026-10-30 |
| Rulebook on refund of PIO contributions, Sl. list CG 107/23, with Form 1 (arts. 1-6) | https://www.sluzbenilist.me/propisi/362476/download | 2026-10-30 |
| Rulebook adjusting the highest annual contribution base for 2025, Sl. list CG 134/2025 (art. 1) | https://www.sluzbenilist.me/propisi/387933/download | 2026-10-30 |
| MONSTAT, average earnings December and full year 2025, release of 30 Jan 2026 | https://www.monstat.org/cg/novosti.php?id=4638 | 2026-10-30 |
| Tax Administration Law, consolidated through 104/26 (arts. 95-96) | https://wapi.gov.me/download/8e3ee8d0-f10c-453a-90ad-6439ac07aca2?version=1.0 | 2026-10-30 |
| Tax Administration Law, Ministry consolidation published March 2026 (before 104/26), art. 95(1) (0.03% a day) | https://wapi.gov.me/download/2dd530ac-eec4-4d0c-9d8f-0c9e7ebc5b86?version=1.0 | 2026-10-30 |
| Poreska uprava decision on the default interest rate, 18 Jul to 31 Dec 2026 | https://wapi.gov.me/download/6d6ec964-3dd6-4588-b81a-a5affc153f6e?version=1.0 | 2026-10-30 |

Not yet confirmed: the 2026 highest annual PIO base (the Ministry rulebook under Law art. 14(4) was not published by 30 October 2026); the numerical lowest monthly base under the General Collective Agreement and the labour-law minimum wage (the old EUR 670 and EUR 800 net figures came from a secondary source); whether the 70% cap in Law art. 18a(2) limits only zimnica or also the severance and aid items listed before it; the unemployment base for board members and foreign employees, because Law art. 11 items 1 to 4 cross-refer to art. 7 items that do not match; the list of social security agreements and which coverage certificates they require; the September 2026 Government proposal to set PIO, additional PIO and unemployment rates to 0% from 1 January 2027 (proposal only, enactment not confirmed); the eUprava refund-service page (m.euprava.me, service 245), which could not be read on 30 October 2026 because of a certificate error, so the refund route above rests on the 107/23 rulebook alone.

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
