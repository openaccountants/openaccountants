---
name: sm-payroll-social
description: >
  San Marino payroll and social contributions for 2026: employee and employer pension contributions to ISS (Istituto per la Sicurezza Sociale) and the FONDISS supplementary pension under ISS circular 2187/UC/2026, self-employed minimum incomes and rates, separate-management (director) rates, the employee taxable-wage base with the 7% forfait capped at EUR 2,800, IGR withholding on account and the February year-end adjustment, IGR G certification by 15 April, remittance of withheld tax, self-employed contribution balance and advance deadlines, thirteenth-month reporting, and the August 2026 rules on unpaid contributions (Regulation 24/2026 and ISS circular 4295/UC/2026). Use for San Marino payroll, ISS rates, FONDISS, self-employed contributions, employer cost and contribution arrears questions. Cross-border social-security coverage and full employer fund tables need their own facts.
jurisdiction: SM
tax_year: 2026
last_updated: 2026-10-30
review_status: pending_review
trust_label: Built by Michael Cutajar and the OpenAccountants team
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
category: international
version: 0.4
---

# San Marino payroll and social contributions v0.4

Tax year: calendar year 2026. Currency EUR. Authorities: ISS (Istituto per la Sicurezza Sociale, Ufficio Contributi) for contributions; UO Ufficio Tributario for IGR withholding.

The 2026 rates come from ISS circular 2187/UC/2026 of 22 April 2026, which cancels and replaces circular 1376/UC/2026 of 2 March 2026 and applies Law 157/2022 (pension reform) for 2026 ([ISS circular 2187/UC/2026, p. 1][iss]).

## 1. Who this applies to

- **Employers** in San Marino with employees covered by the San Marino scheme: withhold employee contributions and IGR, pay employer contributions.
- **Employees**, resident or frontier workers, insured in San Marino.
- **Self-employed** merchants, artisans, professionals, entrepreneurs, agents, autonomous workers and farmers, each with a minimum income.
- **Separate management (gestione separata):** directors, presidents, operating members and collaborators of companies.

Coverage for workers posted to or from another State follows the applicable social-security agreement; establish it before applying these rates. Income tax rates and credits are in `sm-income-tax`.

## 2. Rates, bands and thresholds

### Employees

| Item | Amount | Tax year | Source |
|---|---|---|---|
| Employee pension fund contribution | 6.90% | 2026 | [ISS circular 2187/UC/2026, p. 1][iss] |
| Employee contributions in total (including the 6.90% pension) | 7.80% | 2026 | [ISS circular 2187/UC/2026, p. 1][iss] |
| Employer pension fund contribution | 17.60% | 2026 | [ISS circular 2187/UC/2026, p. 1][iss] |
| Total pension fund contribution | 24.50% | 2026 | [ISS circular 2187/UC/2026, p. 1][iss] |
| FONDISS, employee (on the pensionable base) | 2.50% | 2026 | [ISS circular 2187/UC/2026, p. 10][iss] |
| FONDISS, employer | 2.50% | 2026 | [ISS circular 2187/UC/2026, p. 10][iss] |
| Employee forfait in the taxable wage | 7% of gross pay, capped at 2,800 | 2026 | [IGR art 24(4)][igr] |
| Default deductible contributions in the Tax Office calculator | 9.9% (pension 6.9%, FONDISS 2.5%, unemployment and solidarity 0.5%) | 2026 | [Tax Office IGR calculator][calc] |
| Employer IGR G certification to the Tax Office | By 15 April following the year | 2026 | [IGR art 85(2)][igr] |
| Remittance of IGR withheld on wages | By the end of the two-month period after the month of withholding or accrual | 2026 | [IGR art 125(1)][igr] |

### Self-employed and separate management (2026 minimum incomes and rates)

| Category | Minimum income | Pension | Social security | Family allowances |
|---|---:|---|---|---|
| Merchants | 30,164.57 | 24% | 2% on declared income up to 50,294.28 | Not liable |
| Artisans | 30,164.57 | 24% | 2% up to 50,294.28 | 3.60% |
| Artisans' family helpers | 17,500.00 | 24% | 2% up to 50,294.28 | 3.60% |
| Professionals (libero professionista) | 30,164.57 | 24% (1) | 2% up to 50,294.28 | Not liable |
| Entrepreneurs | 30,164.57 | 24% | Not liable | Not liable |
| Agents and commercial representatives | 30,164.57 | 24% (1) | 2% up to 50,294.28 | Not liable |
| Autonomous workers (DD 214/2021) | 30,164.57 | 24% (1) | 2% up to 50,294.28 | Not liable |
| Farmers | 15,000.00 | 11% | 4% on the minimum income | Not liable |
| Farmers' family helpers | 5,800.00 | 11% | 4% on the minimum income | Not liable |
| Separate management, ordinary director or president | 30,164.57 | 19% (17% if already in another pension fund and only a director) | Not liable | Not liable |
| Separate management, operating director or operating member (collaborator) | 30,164.57 | 19% (an ordinary director who becomes operating owes an extra 1% on the self-employed minimum income) | 2% | Not liable |
| Separate management, project collaborators (CO.CO.PRO.) | Per DD 162/2024 art 2 | 19% | Not liable | Not liable |
| Separate management, pensioner director, president or member | 30,164.57 | 30.50% solidarity rate, on 20% of income (sole director or president) or 60% of income (operating director or collaborating member) | Not liable | Not liable |

(1) For professionals, agents and autonomous workers only: 2% on income above 50,294.28. Directors registered in another pension fund pay on 30% of the income from the second registration (DD 162/2024, art 1). Source for the whole table: [ISS circular 2187/UC/2026, pp. 4-6][iss].

FONDISS for the self-employed, separate management and farmers is 4% of business or professional income, never on less than the minimum income for the first-pillar scheme ([ISS circular 2187/UC/2026, p. 10][iss]).

| Self-employed deadline | Date | Source |
|---|---|---|
| Contribution and FONDISS balance (self-employed, sole traders) | 31 July each year, from 2026 | [ISS circular 2187/UC/2026, p. 6][iss] |
| First contribution and FONDISS advance (self-employed, sole traders) | 31 August each year, from 2026 | [ISS circular 2187/UC/2026, p. 6][iss] |
| Separate management contributions | 31 January of the year after the reference year | [ISS circular 2187/UC/2026, p. 6][iss] |

## 3. The base

**Contributions.** Apply the employee rates to the pensionable pay of a covered worker. The 7.80% is the employee's total ISS rate and already contains the 6.90% pension; FONDISS 2.50% is on top. So a covered employee pays 7.80% + 2.50% = 10.30% in cash. The employer's pension plus FONDISS is 17.60% + 2.50% = 20.10%; other employer funds and sector charges come on top and must be taken from the employer's ISS statement before quoting total employment cost.

**Taxable wage.** Taxable wage = gross pay and benefits less compulsory employee contributions deductible under IGR article 15 less the 7% forfait capped at 2,800 ([IGR arts 15, 24(4)][igr]). The Tax Office calculator deducts 9.9%; use the payslip's actual deductible components, not the 10.30% cash figure ([Tax Office IGR calculator][calc]).

**Travel.** Unreceipted travel costs paid by traceable means are excluded up to 15 a day (San Marino and Italy) or 30 a day (abroad excluding Italy); foreign-service allowances count at 75% ([IGR art 24(3), replaced by DD 156/2026, art 8][dd156]).

**Withholding on account.** The employer annualises the expected income at the bands, deducts the family credits and the SMaC credit the employee asks for (it can be partial) and withholds on account; medical and rent credits are left to the return ([IGR art 101(4)][igr]; [IGR Annex E, art E3(3)][igr]). The year-end adjustment is collected by February of the following year ([IGR art 101(5)][igr]). Termination payments and supplementary pensions follow their own routes ([IGR art 101(3)][igr]).

**Thirteenth month.** A separate Christmas bonus payment is reported to ISS as month 13 with no hours or days worked; a December payslip that includes it uses the December flag ([ISS circular 2187/UC/2026, pp. 1-3][iss]). Entitlement and amount come from the applicable collective agreement.

**Self-employed.** Contributions are on declared income, never below the category minimum, at the rates in section 2. Contributions are fully deductible from business income for IGR ([IGR art 15][igr]).

## 4. Deadlines and filing

| Obligation | Deadline | Source |
|---|---|---|
| Remit IGR withheld from wages | Within the two-month period after the month of withholding or accrual | [IGR art 125(1)][igr] |
| Transmit IGR G (income and withholding per employee) | 15 April following the year | [IGR art 85(2)][igr] |
| Year-end withholding adjustment | By February of the following year | [IGR art 101(5)][igr] |
| Self-employed contribution balance | 31 July | [ISS circular 2187/UC/2026, p. 6][iss] |
| Self-employed first advance | 31 August | [ISS circular 2187/UC/2026, p. 6][iss] |
| Separate management contributions | 31 January of the following year | [ISS circular 2187/UC/2026, p. 6][iss] |
| Self-employed refund requests | Only through the CONTRISS portal, from 1 March 2026 | [ISS circular 2187/UC/2026, pp. 6-9][iss] |

An employee with one employer and no other income does not file a return if the employer transmits IGR G on time ([IGR arts 84-85][igr]).

## 5. Penalties and interest

**Unpaid contributions (Regulation 24/2026 of 7 August 2026).**

- ISS checks each employee's contribution position every two months. If three months (consecutive or not) are unpaid or partly paid, the employee is notified; ISS and FONDISS are checked separately ([Regulation 24/2026, arts 2-4][reg24]). The notification service starts on 1 October 2026, from the arrears position at 31 August 2026 (February-March 2026 bimonth) ([Regulation 24/2026, art 5][reg24]).
- Licence suspension: for employee arrears on the collection roll, each calendar month counts once whether unpaid to ISS, FONDISS or both; the threshold is thirteen months, consecutive or not. For the self-employed and farmers, three missed contribution deadlines (first advance, second advance or balance) count as thirteen months ([Regulation 24/2026, art 7][reg24]). For the listed separate-management categories the test is roll entries above 100,000 of principal ([Regulation 24/2026, art 7(4)][reg24]). Valid instalment plans, settlements and moratoria are left out of the count ([Regulation 24/2026, art 10][reg24]).
- Repayment plan with ISS: up to twelve months, with a 5% penalty and late interest under Law 179/2005 article 44(3). Missing even one instalment sends the unpaid amount to the collection roll ([ISS circular 4295/UC/2026 of 19 August 2026][iss4295]; [Regulation 24/2026, art 13][reg24]). If no plan can be agreed, ISS enters the debt on the roll within four months after the legal payment deadline; once on the roll, ISS can no longer agree a plan ([Regulation 24/2026, arts 13-14][reg24]).

**Withholding.** Late remittance of IGR withheld carries interest at the legal rate plus 2 points ([IGR art 128][igr]). If the employer neither withholds nor pays, the employee is jointly liable ([IGR art 131][igr]). Penalties for failing to withhold or remit are in IGR articles 138-139.

## 6. Cross-border points

- Frontier workers employed in San Marino pay San Marino contributions and suffer San Marino IGR withholding on San Marino-source wages ([IGR art 5][igr]); they get the SMaC credit but no family credits as non-residents ([IGR art 16(4), (8-bis)][igr]).
- Posted workers and multi-State workers: apply the relevant bilateral social-security agreement before choosing the scheme.
- Payments to non-resident self-employed individuals carry 20% IGR withholding: see `sm-cross-border`.

## 7. Two worked examples that recompute

### Example 1: monthly employee contributions and employer subtotal

A covered employee earns 3,000 a month, fully pensionable. Employee: ISS 7.80% = 234, FONDISS 2.50% = 75, total 309. Employer pension 17.60% = 528 plus FONDISS 75 = 603, before other employer funds.

```oa-check
name: San Marino 2026 monthly employee contributions and employer subtotal
inputs:
  pensionable_pay: 3000
  employee_total_iss_rate: 0.078
  employee_fondiss_rate: 0.025
  employer_pension_rate: 0.176
  employer_fondiss_rate: 0.025
steps:
  employee_iss: pensionable_pay * employee_total_iss_rate
  employee_fondiss: pensionable_pay * employee_fondiss_rate
  employee_cash_contributions: employee_iss + employee_fondiss
  employer_pension: pensionable_pay * employer_pension_rate
  employer_fondiss: pensionable_pay * employer_fondiss_rate
  employer_two_component_subtotal: employer_pension + employer_fondiss
expected:
  employee_iss: 234
  employee_fondiss: 75
  employee_cash_contributions: 309
  employer_pension: 528
  employer_fondiss: 75
  employer_two_component_subtotal: 603
```

The same rules give: gross annual wage 50,000, forfait capped at 2,800, default deductible contributions 4,950, taxable wage 42,250; annual IGR of 1,673.48 (the 30,000 wage case in `sm-income-tax`) spread over thirteen payments is 128.73 each, with a 0.01 adjustment at year end.

### Example 2: professional above the pension threshold (edge case)

A professional (footnote 1 category) declares 60,000. Pension: 24% of 50,294.28 = 12,070.63 plus 2% of the 9,705.72 excess = 194.11, total 12,264.74. Social security: 2% of income up to 50,294.28 = 1,005.89. FONDISS: 4% of 60,000 = 2,400. Total 15,670.63.

```oa-check
name: San Marino 2026 professional contributions above the 50,294.28 threshold
inputs:
  declared_income: 60000
  minimum_income: 30164.57
  threshold: 50294.28
steps:
  contribution_income: max(declared_income, minimum_income)
  pension: round(min(contribution_income, threshold) * 0.24 + max(contribution_income - threshold, 0) * 0.02, 2)
  social_security: round(min(contribution_income, threshold) * 0.02, 2)
  fondiss: contribution_income * 0.04
  total_contributions: pension + social_security + fondiss
expected:
  contribution_income: 60000
  pension: 12264.74
  social_security: 1005.89
  fondiss: 2400
  total_contributions: 15670.63
```

The same rules give: a professional declaring 40,000 pays pension 9,600, social security 800 and FONDISS 1,600 (12,000); an agreed ISS plan on 12,000 of arrears adds a 600 penalty, 12,600 before interest, or 1,050 a month over twelve months before interest.

## 8. Ask the client first

1. Is the worker an employee, self-employed, director or member, and in which ISS category?
2. Where the worker lives and works, and any posting or other-State coverage.
3. Gross pay, benefits, bonuses and the applicable collective agreement (thirteenth month).
4. The employee's requested family and SMaC credits for withholding.
5. For the self-employed: declared income for 2025 and 2026, and contributions already paid.
6. Any unpaid contribution months, roll entries or existing repayment plans.

## Sources

| Source | URL | Read on |
|---|---|---|
| ISS circular 2187/UC/2026 of 22 April 2026 (2026 rates, minima, deadlines), pp. 1-10 | https://www.iss.sm/on-line/home/menudestra/area-modulistica/modulistica-ufficio-contributi/documento49158490.html | 2026-10-30 |
| ISS circular 4295/UC/2026 of 19 August 2026 (repayment plans) | https://www.iss.sm/on-line/home/menudestra/area-modulistica/modulistica-ufficio-contributi/documento49160180.html | 2026-10-30 |
| Regulation 24/2026 of 7 August 2026 (unpaid contributions), arts 1-15 | https://www.bollettinoufficiale.sm/on-line/RicercaBU?operation=getDocBU&id=16951b47dbbfd35a095f3ff014ae4d7f1dd77aa7 | 2026-10-30 |
| Law 166/2013 (IGR), official coordinated text updated to 22 December 2025: arts 5, 15-16, 24, 84-85, 101, 125, 128, 131, Annex E | https://www.consigliograndeegenerale.sm/on-line/documento17086436.html | 2026-10-30 |
| Delegated Decree 156/2026 of 12 October 2026, art 8 | https://www.bollettinoufficiale.sm/on-line/RicercaBU?operation=getDocBU&id=9c3a0dfeb72a7aeab52d1c5c0440879b4cf2ad33 | 2026-10-30 |
| Tax Office public 2026 IGR calculator (Law 141/2025) | https://www.pa.sm/portalepa/servlet/portalepa.hic.servizi.HGCalcoloIGRLegge141_2025?MPasso=1&MTipo=G&profondita=1 | 2026-10-24 |

Not yet confirmed: employer contributions beyond pension and FONDISS (the earlier version's unemployment 1.9%, health 4.0% and social services fund 1.0%, and its 27.4% employer total); any contribution ceiling for employees; the monthly ISS contribution payment date for employers; the self-employed second advance date; the current sanctions under Law 179/2005 article 44 and the legal interest rate.

[iss]: https://www.iss.sm/on-line/home/menudestra/area-modulistica/modulistica-ufficio-contributi/documento49158490.html
[iss4295]: https://www.iss.sm/on-line/home/menudestra/area-modulistica/modulistica-ufficio-contributi/documento49160180.html
[reg24]: https://www.bollettinoufficiale.sm/on-line/RicercaBU?operation=getDocBU&id=16951b47dbbfd35a095f3ff014ae4d7f1dd77aa7
[igr]: https://www.consigliograndeegenerale.sm/on-line/documento17086436.html
[dd156]: https://www.bollettinoufficiale.sm/on-line/RicercaBU?operation=getDocBU&id=9c3a0dfeb72a7aeab52d1c5c0440879b4cf2ad33
[calc]: https://www.pa.sm/portalepa/servlet/portalepa.hic.servizi.HGCalcoloIGRLegge141_2025?MPasso=1&MTipo=G&profondita=1

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
