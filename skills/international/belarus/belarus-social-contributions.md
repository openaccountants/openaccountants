---
name: belarus-social-contributions
description: Compute Belarus mandatory FSZN pension and social contributions and occupational-accident insurance for 2026. Use for employer on-costs, the employee pension deduction, contribution ceilings and minimum bases, reduced employer classes, individual entrepreneurs and professional-income taxpayers. The skill distinguishes contribution bases from personal-income-tax bases, provides the statutory entrepreneur low-income test, pension exemptions and app allocation, and sets out ordinary payment and social-account reporting procedures. It includes two recomputing examples and sources for the 2026 reporting changes. The January and February director occupational-insurance base remains a named historical-verification gap, so the domain is partial. HTP and other presidential concession schemes require their specific legislation. Tier 2, checked against the law.
version: 0.2
jurisdiction: BY
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

# Belarus social contributions and occupational insurance, 2026 v0.2

## Who this applies to

2026 FSZN obligations of employers, working individuals, independent payers and professional-income taxpayers under Law 118-Z of 15 July 2021. Working individuals include Belarus citizens, foreign citizens and stateless persons employed or engaged under covered civil contracts; founders performing management functions are also included. Classify employment, civil services/IP, a founder-manager, an entrepreneur and professional income separately. Foreign nationality alone is not an exemption. [Law arts. 1-3](https://pravo.by/document/?guid=3871&p0=H12100118).

Occupational-accident insurance is paid separately to Belgosstrakh for the persons listed in Decree 108's approved Regulation para. 193, including employees, covered civil contractors working at places supplied by the policyholder, and specified managers. Do not apply the FSZN monthly ceiling to this separate base. [Decree 108, paras. 192-194](https://pravo.by/document/?guid=3871&p0=P32500108); [Council Resolution 1462, contribution-payment Regulation para. 2](https://pravo.by/document/?guid=3871&p0=C20601462).

## Rates, bands and thresholds

| Item | Amount | Period | Official act/article |
|---|---|---|---|
| Ordinary employer pension/social | 28% + 6% = 34% | 2026 | [Law 118-Z art. 5](https://pravo.by/document/?guid=3871&p0=H12100118) |
| Employee pension | 1% | 2026 | [Art. 5(1)](https://pravo.by/document/?guid=3871&p0=H12100118) |
| Eligible agricultural employers/farms pension | 24%, with 6% social where applicable | 2026 | [Art. 5(1)-(2)](https://pravo.by/document/?guid=3871&p0=H12100118) |
| Listed consumer/property/garden cooperatives and qualifying disability organisations pension | 5%, with 6% social where applicable | 2026 | [Art. 5(1)-(2)](https://pravo.by/document/?guid=3871&p0=H12100118) |
| Independent entrepreneur/notary/advocate | 29% pension + 6% social = 35% | 2026 | [Art. 5](https://pravo.by/document/?guid=3871&p0=H12100118) |
| Ordinary monthly FSZN maximum base | 5 times national average wage for preceding month | 2026 | [Art. 4(1)](https://pravo.by/document/?guid=3871&p0=H12100118) |
| Ordinary employee minimum base | Monthly statutory/indexed minimum wage, prorated for part-time/partial month; stated exceptions apply | 2026 | [Art. 9(1)-(2)](https://pravo.by/document/?guid=3871&p0=H12100118) |
| Monthly minimum wage | BYN 858 from 1 January 2026; use any later indexed amount the law requires for the month | 2026 | [Council Resolution 612 of 6 November 2025, paras. 1, 4](https://pravo.by/document/?guid=12551&p0=C22500612) |
| Entrepreneur low-income threshold | 12 times December minimum wage; if income does not exceed it, minimum contributions are based on actual statutory income | 2026 | [Art. 9(3)](https://pravo.by/document/?guid=3871&p0=H12100118) |
| Independent annual maximum | Contributions on 60 times national average wage for December of preceding year | 2026 | [Art. 4(1)](https://pravo.by/document/?guid=3871&p0=H12100118) |
| Professional-income social component | 60% of paid professional-income tax; pension recipient relieved of this component | 2026 | [Art. 16-1](https://pravo.by/document/?guid=3871&p0=H12100118) |
| Professional occupational pension | Statutory groups 9%, 6% or 4%; base capped at 3 times preceding month's national average wage | 2026 | [Arts. 4(2), 6](https://pravo.by/document/?guid=3871&p0=H12100118) |
| Accident insurance baseline | Budget organisations 0.1%; other policyholders 0.6%, adjusted for notified discount/surcharge/relief | 2026 | [Decree 108 Regulation para. 194 and Annex 16](https://pravo.by/document/?guid=3871&p0=P32500108) |
| Covered director accident minimum base | National average wage for corresponding month; exact proration not established here | From 1 March 2026 | [Resolution 1462 payment Regulation para. 2; amendment 660](https://pravo.by/document/?guid=12551&p0=C22500660) |

The wage amounts required by these formulae are period-specific statutory/statistical inputs. Obtain the actual indexed minimum, preceding month's official national average and December figures; do not substitute a forecast for months not yet published. [Law arts. 4, 9](https://pravo.by/document/?guid=3871&p0=H12100118).

## The base

**Employees and employer classes.** Start with covered monetary/in-kind remuneration for each person/month, excluding only items in the Council's statutory exclusion list. Determine the correct employer pension class, add social insurance, and separately withhold employee pension. Apply the FSZN maximum to the relevant monthly remuneration; compute the minimum contribution comparison using actual work time and the exceptions for covered civil contracts, specified public/religious bodies and employee-fault production shortfalls in art. 9(2). An exempt PIT benefit is not automatically FSZN-exempt. Employers are relieved of the employer pension element for group I/II disabled workers from the month following establishment of disability under art. 12(1); do not remove social insurance or the employee element without their own legal basis. [Arts. 4-5, 9, 12](https://pravo.by/document/?guid=3871&p0=H12100118).

**Independent entrepreneurs.** Determine art. 9(3) income as PIT business base after art. 205 expenses and/or the statutory minimum-wage basis for single-tax periods. If income is no more than twelve December minimum wages, calculate the minimum from that actual income. If greater, minimum contributions use the sum of statutory/indexed monthly minimum wages for the contribution months. Apply 35% to the selected lawful income, subject to the annual maximum. Keep activity-period and exemption evidence; concurrent employment alone is not listed as a voluntary category in the current art. 13. Pension receipt, entitlement to childcare benefit and full-time education are among the specified voluntary cases. Do not give every entrepreneur the same full-year fixed bill or treat low income as automatic zero contributions. [Arts. 4-5, 8-9, 11, 13](https://pravo.by/document/?guid=3871&p0=H12100118).

**Other independent payers.** Notaries/advocates generally use 35% and the art. 9 monthly minimum, with art. 13 voluntary categories for pension/childcare-benefit cases. Independent professional/craft/agro-tourism payers outside the professional-income tax use the pension coverage rules in arts. 3-5/13; their pension element is 29%, and social insurance is charged only to the categories enumerated in art. 5(2). Do not impose the entrepreneur social element on every self-employed activity. [Arts. 3-5, 9, 13](https://pravo.by/document/?guid=3871&p0=H12100118).

**Professional income.** For a nonpensioner the app tax includes social insurance; allocate 60% of paid tax to FSZN instead of charging 35% again on the same receipts. Pensioners' tax is reduced by that component, giving effective 4%/8% where ordinary app rates are 10%/20%. The July monthly minimum is likewise 45 normally and 18 for a pension recipient. Notify pension status in the app. Additional voluntary pension contributions and the annual-limit relief require arts. 4-1/9(4)/16-1 calculations, not an assumed universal top-up. [Law arts. 4-1, 9(4), 16-1](https://pravo.by/document/?guid=3871&p0=H12100118); [Tax Code arts. 381-3, 381-6](https://pravo.by/document/?guid=3871&p0=hk0900071); [MNS July minimum](https://nalog.gov.by/actual/npd_45/).

**Accident insurance.** Use the covered remuneration under the payment Regulation, without the FSZN ceiling, and the insurer's actual annual tariff notice. For the specified directors/managers from March, test the national-average-wage minimum even if remuneration is low/absent; obtain time-worked evidence and the applicable monthly official wage figure. The base and time-allocation details for January-February directors have not been independently retrieved and are not inferred from the March reform. [Resolution 1462 payment Regulation para. 2](https://pravo.by/document/?guid=3871&p0=C20601462); [Decree 108 Regulation paras. 193-194](https://pravo.by/document/?guid=3871&p0=P32500108).

**Professional occupational pension.** For covered hazardous/other statutory jobs identify the art. 6 group and full-day qualifying exposure before applying its additional 9%/6%/4% employer rate to the separate three-average-wage-limited base. Statutory pension-age/compensation-election exemptions are in art. 12(3). This additional charge is not the Belgosstrakh premium. [Arts. 4(2), 6, 12(3)](https://pravo.by/document/?guid=3871&p0=H12100118).

## Deadlines and filing

| Obligation | Deadline/rule | Official source |
|---|---|---|
| Ordinary employer FSZN payment | Actual pay day for preceding month's wages, no later than contractual pay day and in all cases by 20th following month | [Law art. 8(1)](https://pravo.by/document/?guid=3871&p0=H12100118) |
| Eligible commercial employers with preceding-year average staff no more than 100 | Quarterly payment option, no later than qualifying pay day/20th after quarter; late payment triggers monthly treatment for remainder of year | [Art. 8(1)](https://pravo.by/document/?guid=3871&p0=H12100118) |
| Independent annual payment | By 31 March following year | [Art. 8(2)](https://pravo.by/document/?guid=3871&p0=H12100118) |
| Employer 4-Fund | Electronic quarterly return by 20th after reporting period | [Ministry Resolution 143, approved Form 4-Fund](https://pravo.by/document/?guid=12551&p0=W22544374p) |
| Employer PU-3 | Quarterly within following month; covered civil-contract first report within 5 calendar days of contract, 15 for newly registered payer, then quarterly on remuneration | [Resolution 742 Rules para. 17](https://pravo.by/document/?guid=12551&p0=C22500742) |
| Independent PU-3 | Fund worker files entrepreneur and other specified cases by 15 April; the separately listed self-filers in para. 10 file by 31 March | [Resolution 742 Rules paras. 10, 17](https://pravo.by/document/?guid=12551&p0=C22500742) |
| PU-2 hiring/dismissal | Hire within 5 calendar days, newly created employer within 15 days of registration; dismissal by following day, subject to stated exceptional order dates | [Resolution 742 Rules para. 16](https://pravo.by/document/?guid=12551&p0=C22500742) |
| Accident premium | By 25th of month after quarter | [Resolution 1462 payment Regulation para. 4](https://pravo.by/document/?guid=3871&p0=C20601462) |
| Belgosstrakh annual report | Registered policyholders file calendar-year report by 25 January following year; nonworking deadline moves to next working day | [Resolution 1462 reporting Regulation paras. 2-3, 33-35](https://pravo.by/document/?guid=3871&p0=C20601462) |

FSZN payment dates falling on nonworking days are brought forward to the preceding working day, except for independent payers, under Law art. 8(5). Accident-premium dates likewise move to the preceding working day (payment Regulation para. 5). Do not apply the tax-return next-working-day convention to these payments. Reconcile employee accounts to contributions actually paid and submit corrections under the current PU rules. Employer/Fund registration and cessation follow Law art. 7 and Resolution 742's registration Regulation; confirm UNPF as well as tax UNP. [Law arts. 7-8](https://pravo.by/document/?guid=3871&p0=H12100118); [Resolution 742](https://pravo.by/document/?guid=12551&p0=C22500742); [Resolution 1462](https://pravo.by/document/?guid=3871&p0=C20601462).

From 8 January, Resolution 742 Rules 15-17 also require: PU-1 registration within two calendar days of hiring a person without a social-insurance certificate, except a person whose identity document contains an identification number; PU-1 personal-data change within five working days after the supporting document is presented (identification-number holders use population-register data); PU-2 section 2 job/occupation-only changes quarterly by the 10th after the quarter. For sickness/maternity entitlement, submit the preceding quarter's PU-3 within three working days after the certificate is presented or the Fund's portal notice is received. PU-2 is also due within three working days after the sickness certificate if the post-1-July-2019 concurrent-job code was not supplied. The pension-assignment PU-3 is due within five working days after the person's pension/recalculation application. These event-driven filings do not wait for the ordinary quarter-end batch. [Resolution 742 Rules 15-17, official PDF pp. 32-33](https://pravo.by/document/?guid=12551&p0=C22500742).

From 8 January, covered professional-occupational-pension policyholders also file PU-6 after PU-3 within the month following each quarter. Pension assignment/recalculation for the listed special-work/service/professional pensions triggers PU-6 within five working days after the relevant application; ordinary pension-age attainment or qualifying dismissal triggers it by the following month. Continued employment after a pension-event PU-6 still requires the ordinary quarterly PU-6. On Fund deregistration for liquidation/cessation, PU-2/PU-3/PU-6 are due within thirty working days after the liquidation-start documents are filed; payers outside state registration use the decision/deregistration trigger. PU-2/PU-3/PU-6 reporting deadlines falling on a nonworking day move to the next working day. [Resolution 742 Rules 19-21, official PDF pp. 34-35](https://pravo.by/document/?guid=12551&p0=C22500742).

The 2026 Belgosstrakh annual report is due 25 January 2027. Use the insurer's prescribed electronic-document/electronic software delivery and keep its receipt; the reporting deadline moves to the following working day, while quarterly premium payment moves to the preceding working day. Reorganisation/liquidation reports use the separate 15-working-day triggers in reporting Regulation para. 33 and can be filed on paper under para. 35. [Resolution 1462 reporting Regulation paras. 33-38](https://pravo.by/document/?guid=3871&p0=C20601462); [Resolution 660 commencement para. 3](https://pravo.by/document/?guid=12551&p0=C22500660).

## Penalties and interest

FSZN arrears incur daily interest including payment day, at 1/360 of the National Bank refinancing rate **on the date of payment**, under Law art. 10(2). This differs from General Tax Code art. 55's period-by-period tax-interest rule. Reconcile arrears, benefit offsets and special exceptions before charging interest. Administrative Code art. 12.15 imposes 2-20 basic units on the described responsible persons for unpaid contributions for individuals exceeding 20 basic units, with the note's pay-day exception. [Law art. 10](https://pravo.by/document/?guid=3871&p0=H12100118); [Administrative Code art. 12.15](https://pravo.by/document/?guid=3871&p0=hk2100091). The basic unit is BYN 45 from 1 January 2026 ([Council Resolution 651 of 20 November 2025](https://pravo.by/document/?guid=12551&p0=C22500651)).

Accident insurance late-registration fine is 2 basic units; late/inaccurate reporting attracts the separate 2/10-basic-unit rules, including repeated late filing within the stated five-year period. Late premium interest is 1/360 of the refinancing rate for each overdue day including payment. [Decree 108 Regulation paras. 196-197](https://pravo.by/document/?guid=3871&p0=P32500108). Concealed wages have the additional 35%/minimum-base assessment under Law art. 5-1, rather than the ordinary ceiling calculation. [Law arts. 4(1-1), 5-1](https://pravo.by/document/?guid=3871&p0=H12100118).

## Cross-border points

Law art. 2 gives applicable international agreements priority. Obtain coverage certificates and check the actual bilateral/EAEU social-security agreement before excluding foreign staff or outbound workers. Foreign branch/representation payment timing has a specific quarterly rule in art. 8(1). Income-tax treaties do not themselves remove FSZN or accident insurance. [Law arts. 1-3, 8](https://pravo.by/document/?guid=3871&p0=H12100118).

## Two worked examples that recompute

### 1. Ordinary employee, no ceiling or minimum adjustment

Covered remuneration is BYN 3,000 and the statutory limits do not change it. Employer pension is 840 and social insurance 180, total FSZN 1,020. Employee pension withheld is 30. A confirmed unadjusted 0.6% accident tariff gives 18. Employer contributions are 1,038; gross payroll cost is 4,038. PIT is separate.

```oa-check
name: BY 2026 ordinary employer contribution cost
inputs:
  covered_pay: 3000
steps:
  employer_pension: covered_pay * 0.28
  employer_social: covered_pay * 0.06
  employee_pension: covered_pay * 0.01
  accident: covered_pay * 0.006
  employer_charges: employer_pension + employer_social + accident
  total_cost: covered_pay + employer_charges
expected:
  employee_pension: 30
  employer_charges: 1038
  total_cost: 4038
```

### 2. Pension recipient using professional-income tax in July

All BYN 1,000 receipts are in the 10% app band; pension status is duly notified and no late-receipt sanction applies. Remove the 60% social component from 100 tax, leaving 40. This exceeds the pensioner's July minimum of 18, so 40 is payable and no additional mandatory FSZN amount is charged on those same receipts.

```oa-check
name: BY 2026 pensioner professional-income social relief
inputs:
  receipts: 1000
steps:
  ordinary_app_tax: receipts * 0.10
  relieved_social: ordinary_app_tax * 0.60
  reduced_tax: ordinary_app_tax - relieved_social
  payable: max(reduced_tax, 18)
expected:
  relieved_social: 60
  payable: 40
```

## Ask the client first

- What are the employer class, each worker's legal engagement and foreign coverage documents?
- What remuneration/excluded benefits and actual work days arise in each month?
- Which official monthly wages, ceilings and minimum-wage indexes apply?
- Are there disability, pension, full-time education, childcare or special-occupation facts?
- What are the entrepreneur regime, statutory income and actual contribution periods?
- What do the insurer tariff notice, UNPF account, filed reports and payment ledger show?

## Sources

| Source and read scope | Official URL | Read on |
|---|---|---|
| FSZN Law 118-Z, arts. 1-16-1, current consolidated text | https://pravo.by/document/?guid=3871&p0=H12100118 | 2026-10-24 |
| Decree 108 of 18 March 2025, approved Regulation paras. 192-197 and Annex 16 | https://pravo.by/document/?guid=3871&p0=P32500108 | 2026-10-24 |
| Council Resolution 1462, contribution-payment Regulation paras. 1-12 and reporting Regulation paras. 2-3, 33-38 | https://pravo.by/document/?guid=3871&p0=C20601462 | 2026-10-24 |
| Council Resolution 660, commencement of March 2026 insurance reform | https://pravo.by/document/?guid=12551&p0=C22500660 | 2026-10-24 |
| Ministry of Labour Resolution 143, official PDF p. 1, Form 4-Fund | https://pravo.by/document/?guid=12551&p0=W22544374p | 2026-10-24 |
| Council Resolution 742, official PDF pp. 27-35, individual-account Rules paras. 7-21 | https://pravo.by/document/?guid=12551&p0=C22500742 | 2026-10-24 |
| Administrative Code, art. 12.15 | https://pravo.by/document/?guid=3871&p0=hk2100091 | 2026-10-24 |
| Tax Code Special Part, arts. 381-3, 381-6 | https://pravo.by/document/?guid=3871&p0=hk0900071 | 2026-10-24 |
| MNS professional-income July minimum | https://nalog.gov.by/actual/npd_45/ | 2026-10-24 |
| Council Resolution 612 of 6 November 2025, paras. 1, 4, official PDF, monthly minimum wage BYN 858 from 1 January 2026 | https://pravo.by/document/?guid=12551&p0=C22500612 | 2026-10-31 |
| Council Resolution 651 of 20 November 2025, paras. 1, 3, official PDF, basic unit BYN 45 from 1 January 2026 | https://pravo.by/document/?guid=12551&p0=C22500651 | 2026-10-31 |

Pravo consolidated HTML was read in a normal browser after scripted access returned HTTP 403. Published PDFs were read in the official browser PDF viewer. Checked against the law (tier 2); no licensed Belarusian accountant has signed it off.

Not yet confirmed: January-February 2026 occupational-insurance director minimum-base rules and the exact time-proration implementation of the March director floor have not been verified from the historical/current implementing text. These are an SC partial gap. Published monthly wage inputs must be supplied for the actual contribution period; future December data are not invented.

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
