---
name: qc-employer-contributions
description: >
  Calculate and reconcile Quebec employer payroll contributions for 2026:
  QPP and second additional QPP, QPIP, the Health Services Fund (FSS),
  CNESST periodic payments, the separate labour standards contribution and
  the Workforce Skills Development and Recognition Fund. Use for Quebec
  payroll, RRQ, RQAP, CNESST, FSS, RL-1 and employer-cost questions.
  Distinguish employee payroll from a self-employed person's return and
  worldwide payroll for the FSS rate from Quebec remuneration subject to it.
  Read canada-payroll for federal income tax, EI, T4 and ROE mechanics;
  this skill supplies the Quebec overlay, not a federal CPP calculation.
version: 1.1
jurisdiction: CA
category: payroll
tax_year: 2026
last_updated: 2026-11-14
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
tier: 2
domain: payroll
type: computation
---

# Quebec employer contributions v1.1

## Scope

Quebec employer contributions for remuneration paid in calendar year 2026, in CAD. The output is a calculation and reconciliation working paper for approval. It does not submit a return, change a payroll ledger or make a payment. This skill is **Built from the law** and **Not yet approved**.

Cover QPP, second additional QPP (QPP2), QPIP, Health Services Fund (HSF/FSS), CNESST occupational health and safety periodic payments, the separate labour standards contribution and WSDRF training shortfall. Keep federal income tax, EI, T4, ROE and CRA registration/remittance work in [canada-payroll](../canada-payroll.md). Quebec income tax withholding uses the current TP-1015.3-V employee declaration and WebRAS or the current employer formulas; this skill does not compute income tax.

Do not apply federal CPP rates to QPP, or employer payroll rates to a self-employed person's profit. QPP self-employment is paid through the individual's Quebec return using the applicable current-year calculation, not an employer remittance. Its first-tier combined rate is 12.60% in 2026, with 8% second additional contributions. Mixed employment, CPP/QPP and self-employment require the individual-return calculation. [Revenu Quebec, self-employed QPP](https://www.revenuquebec.ca/en/citizens/income-tax-return/paying-a-balance-due-or-receiving-a-refund/paying-contributions-and-premiums/contributions-and-premiums-payable-by-a-self-employed-person-or-a-member-of-a-partnership/qpp-contribution-payable-by-a-self-employed-person-or-a-member-of-a-partnership/). The official 2026 self-employed QPIP rate is 0.764%, with an annual maximum of CAD 786.92; this is a separate personal-return contribution, not the employer rate. [Quebec government, contribution table](https://www.quebec.ca/entreprises-et-travailleurs-autonomes/administrer-gerer/embauche-gestion-personnel/assurance-parentale/taux-cotisations). Self-employed QPIP computation, benefits and personal contribution deductions belong in [qc-individual-return](qc-individual-return.md), not this employer calculation.

## Ask the client first

- Which calendar year and pay dates? Obtain employee-by-employee payroll, cash and non-cash benefits, pay frequency, year-to-date contributions and any previous-employer/successor records.
- Where does each employee report for work, and which establishment pays a remote worker? Obtain the province-of-employment determination, rather than infer it from home address. Identify foreign postings or social-security certificates.
- Are workers employees, genuine contractors, directors, partners or exempt workers? Obtain age, pension status, QPP election RR-50-V and any disability/exempt-employment documents that change contribution eligibility.
- What is the employer's own subject remuneration, worldwide payroll and payroll of associated employers at December 31? Identify sector, public-sector status and the activities qualifying for an HSF exemption.
- Obtain the current CNESST classification decision and periodic payment rate, covered workers, wages by unit, annual/weekly basis and any retrospective-rating decision. Do not guess a rate from a business description.
- Obtain Revenu Quebec employer account details and assigned remittance frequency, actual remittances, eligible training records/carryforwards and any valid training initiative quality certificate.

## The method, step by step

### 1. Establish the coverage and separate the bases

Determine province of employment before choosing QPP or CPP. Federal withholding follows province-of-employment rules rather than simply the employee's province of residence. Quebec employment requires the coordinated CRA and Revenu Quebec streams. Remote work, mixed provinces and a transfer between establishments need the specific rules, not a default to the employer's registered office. [CRA Quebec employees](https://www.canada.ca/en/revenue-agency/services/tax/businesses/topics/payroll/calculating-deductions/determining-tax-treatment/quebec-employee.html).

Make separate columns for QPP pensionable remuneration, QPIP eligible remuneration, HSF subject remuneration, labour standards subject remuneration, WSDRF payroll and CNESST insurable wages. They are not interchangeable. In particular, [HSF subject remuneration](https://www.revenuquebec.ca/en/businesses/source-deductions-and-employer-contributions/calculating-source-deductions-and-contributions/employer-contribution-to-the-health-services-fund/remuneration-subject-to-the-contribution/) has exceptions, while the [worldwide associated-employer payroll](https://www.revenuquebec.ca/en/businesses/source-deductions-and-employer-contributions/calculating-source-deductions-and-contributions/employer-contribution-to-the-health-services-fund/total-payroll/) determines only the HSF rate.

### 2. Select the 2026 rates and caps

Amounts below are annual full-year ceilings, not a formula for withholding an entire year's contributions from one ordinary pay run.

| Item | 2026 value | Official source |
|---|---|---|
| QPP maximum pensionable earnings / basic exemption | CAD 74,600 / CAD 3,500 | https://www.revenuquebec.ca/en/businesses/source-deductions-and-employer-contributions/employers-principal-changes-for-2026/ |
| QPP employee and employer first-tier rate, each | 6.30%, comprising 5.30% base and 1% first additional | https://www.revenuquebec.ca/en/businesses/source-deductions-and-employer-contributions/employers-principal-changes-for-2026/ |
| Maximum first-tier QPP, each | CAD 4,479.30 | https://www.revenuquebec.ca/en/businesses/source-deductions-and-employer-contributions/employers-principal-changes-for-2026/ |
| QPP additional maximum pensionable earnings | CAD 85,000 | https://www.revenuquebec.ca/en/businesses/source-deductions-and-employer-contributions/employers-principal-changes-for-2026/ |
| QPP2 employee and employer rate, each | 4% on the CAD 74,600 to CAD 85,000 band | https://www.revenuquebec.ca/en/businesses/source-deductions-and-employer-contributions/employers-principal-changes-for-2026/ |
| Maximum QPP2, each | CAD 416; combined QPP annual maximum CAD 4,895.30, derived | https://www.revenuquebec.ca/en/businesses/source-deductions-and-employer-contributions/employers-principal-changes-for-2026/ |
| QPIP eligible remuneration ceiling | CAD 103,000 | https://www.revenuquebec.ca/en/businesses/source-deductions-and-employer-contributions/employers-principal-changes-for-2026/ |
| QPIP employee rate / maximum | 0.430% / CAD 442.90 | https://www.revenuquebec.ca/en/businesses/source-deductions-and-employer-contributions/employers-principal-changes-for-2026/ |
| QPIP employer rate / maximum per employee | 0.602% / CAD 620.06 | https://www.revenuquebec.ca/en/businesses/source-deductions-and-employer-contributions/employers-principal-changes-for-2026/ |
| Labour standards contribution | Employer only, 0.06%; maximum subject remuneration CAD 103,000 per employee | https://www.revenuquebec.ca/en/businesses/source-deductions-and-employer-contributions/calculating-source-deductions-and-contributions/contribution-related-to-labour-standards/ |
| CNESST annual insurable maximum | CAD 103,000 per worker; actual assigned rate required | https://www.cnesst.gouv.qc.ca/sites/default/files/documents/periodic-payment-calculation-2026.pdf |
| CNESST eligible weekly basis | CAD 1,975.45 per week; only where weekly-basis conditions apply | https://www.cnesst.gouv.qc.ca/sites/default/files/documents/periodic-payment-calculation-2026.pdf |
| WSDRF threshold / training requirement | Payroll over CAD 2,000,000 / 1% of subject payroll | https://www.revenuquebec.ca/en/businesses/source-deductions-and-employer-contributions/calculating-source-deductions-and-contributions/contribution-to-the-workforce-skills-development-and-recognition-fund/ |

Historical correction: 2025 first-tier QPP was CAD 4,339.20 per employee/employer, not CAD 4,348.50. Adding the 2025 QPP2 maximum CAD 396 gives CAD 4,735.20. The previous skill's difference was an error, not a special rounding convention. Do not use either year's figures for the other year. [Revenu Quebec, historical table](https://www.revenuquebec.ca/en/businesses/source-deductions-and-employer-contributions/calculating-source-deductions-and-contributions/qpp-contributions/maximum-pensionable-earnings-and-contribution-rate/).

### 3. Calculate QPP using actual pay-period data

For an ordinary full-year employee with one employer, no exemptions and pensionable annual earnings E, the annual reasonableness check is:

`first_qpp = round(max(0, min(E, 74600) - 3500) * 0.063, 2)`

`qpp2 = round(max(0, min(E, 85000) - 74600) * 0.04, 2)`

The employer matches each component. This annual check does not replace the current-year WebRAS/formula calculation for each pay period. Enter actual pensionable pay, frequency and year-to-date amounts, apply the correct period exemption and remaining separate contribution limits, then reconcile the output. Do not annually project a single irregular payment and deduct that annual result. Special/non-continuous employment, bonuses, partial-year eligibility and transfers require the applicable current formulas.

Track the first contribution and QPP2 separately. The current RL-1 guide reports base plus first additional contributions in **B.A** and second additional contributions in **B.B**. Box G reports pensionable wages under that guide; do not put employer contributions into employee boxes or relabel B.A as QPP2. [RL-1 guide, sections 5.4 and 5.9](https://www.revenuquebec.ca/en/online-services/forms-and-publications/rl-1-g-v/guide-to-filing-the-rl-1-slip-employment-and-other-income/).

The RL-1 guide excludes pensionable remuneration paid before and during the month the employee turns 18 and after December 31 of the year they turn 72. An eligible pension recipient aged at least 65 and under 73 at year-end who has not revoked an election in the same year can deliver RR-50-V to stop QPP contributions; stopping takes effect from the first pay of the following month. Verify the election and its effective date, rather than reuse CPP's age-70 limit or CPT30. [RR-50-V rules](https://www.revenuquebec.ca/en/businesses/source-deductions-and-employer-contributions/calculating-source-deductions-and-contributions/special-cases-source-deductions-and-employer-contributions/employee-who-is-at-least-65-but-under-73-at-the-end-of-the-year-who-elects-to-stop-contributing-to-the-qpp/). Disability or excepted employment must be checked separately.

### 4. Calculate QPIP separately from QPP and federal EI

For eligible 2026 remuneration, apply the employee and employer rates separately up to the QPIP ceiling. Unlike QPP, do not subtract a CAD 3,500 exemption. QPIP applies regardless of employee age and generally regardless of residence; excluded employment/remuneration still needs checking. Use WebRAS, TP-1015.TA-V or TP-1015.F-V with actual year-to-date data. [QPIP rules](https://www.revenuquebec.ca/en/businesses/source-deductions-and-employer-contributions/calculating-source-deductions-and-contributions/qpip-premiums/qpip-premiums-what-you-need-to-know/).

Report employee QPIP in RL-1 **H** and eligible remuneration in **I**, using the current RL-1 guide's remuneration rules. Do not assume every taxable non-cash benefit has the same QPIP treatment as cash pay. [RL-1 guide, sections 5.10 and 5.11](https://www.revenuquebec.ca/en/online-services/forms-and-publications/rl-1-g-v/guide-to-filing-the-rl-1-slip-employment-and-other-income/). Federal EI remains a separate CRA obligation at the Quebec rate; load canada-payroll and fetch the current official EI figures before computing it. QPIP does not replace all federal EI.

### 5. Calculate HSF with two different payroll populations

First establish worldwide payroll T, including employers associated at December 31, for the rate. Then determine this employer's remuneration subject to HSF, after applicable exclusions, for the amount payable. Applying the low rate using only Quebec payroll can understate HSF for an employer with an associated group elsewhere. [Total payroll definition](https://www.revenuquebec.ca/en/businesses/source-deductions-and-employer-contributions/calculating-source-deductions-and-contributions/employer-contribution-to-the-health-services-fund/total-payroll/); [subject remuneration](https://www.revenuquebec.ca/en/businesses/source-deductions-and-employer-contributions/calculating-source-deductions-and-contributions/employer-contribution-to-the-health-services-fund/remuneration-subject-to-the-contribution/).

| Rate-setting payroll T | General private-sector rate (%) | Primary/manufacturing rate (%) | Public-sector rate (%) | Official source |
|---|---|---|---|---|
| CAD 1,000,000 or less | 1.65 | 1.25 | 4.26 | https://www.revenuquebec.ca/en/businesses/source-deductions-and-employer-contributions/calculating-source-deductions-and-contributions/employer-contribution-to-the-health-services-fund/total-payroll-threshold-and-health-services-fund-contribution-rate/ |
| Over CAD 1,000,000 and below CAD 7,800,000 | 1.2662 + (0.3838 x T / 1,000,000) | 0.8074 + (0.4426 x T / 1,000,000) | 4.26 | https://www.revenuquebec.ca/en/businesses/source-deductions-and-employer-contributions/calculating-source-deductions-and-contributions/employer-contribution-to-the-health-services-fund/total-payroll-threshold-and-health-services-fund-contribution-rate/ |
| CAD 7,800,000 or more | 4.26 | 4.26 | 4.26 | https://www.revenuquebec.ca/en/businesses/source-deductions-and-employer-contributions/calculating-source-deductions-and-contributions/employer-contribution-to-the-health-services-fund/total-payroll-threshold-and-health-services-fund-contribution-rate/ |

Check both principal activities and whether more than 50% of total payroll is attributable to eligible primary/manufacturing activities before using that column. Public-sector status has its own definition. For an intermediate payroll, use the official rate calculation and its prescribed precision before applying it; do not use the previous skill's 0.7575/0.9075 coefficients. [RL-1 summary, lines 50.1, 50.3, 51 and 54](https://www.revenuquebec.ca/en/online-services/forms-and-publications/rlz-1-s-g-v/guide-to-filing-the-rl-1-summary-summary-of-source-deductions-and-employer-contributions/).

The 2026-2027 agriculture, forestry and fishing temporary exemption uses **the employer's own payroll**, not associated-employer payroll, for its activity proportion. Qualifying activities are NAICS 111, 112, 113, 1141, 321111 and 32211. More than 50% gives a full exemption; 25% through 50% gives a 50% exemption. Check employer eligibility and attributable employee duties before applying either. The broadened rules are retroactive to January 1, 2026; reduced periodic payments can start with the first pay period beginning after January 28, 2026. Earlier overpayments are reconciled through the annual summary. [Official exemption rules](https://www.revenuquebec.ca/en/press-room/tax-news/details/2026-02-12/broadening-of-the-temporary-exemption-from-health-services-fund-contributions-for-the-agriculture-forestry-and-fishing-sectors/).

Reconcile the actual annual HSF rate and subject remuneration to periodic payments on RL-1 summary. Do not promise that a reasonable estimate eliminates interest. The summary guide distinguishes interest on insufficient periodic payments from the balance resulting from a changed actual HSF rate. [Guide sections 5.5 and 6.4](https://www.revenuquebec.ca/en/online-services/forms-and-publications/rlz-1-s-g-v/guide-to-filing-the-rl-1-summary-summary-of-source-deductions-and-employer-contributions/).

### 6. Keep CNESST health and safety separate from labour standards

CNESST assigns the occupational health and safety periodic payment rate. Use the employer's actual 2026 notice; a generic office-sector range or an assumed NAICS rate is not sufficient. Calculate insurable wages after exclusions and excess wages, apply the assigned dollar rate per CAD 100, and keep a worker/unit reconciliation. The annual-basis maximum and eligible weekly basis are in the table above. Multiple units, special coverage and retrospective rating need the CNESST method, not an invented universal threshold. [2026 periodic payment guide, sections 2 and 4](https://www.cnesst.gouv.qc.ca/sites/default/files/documents/periodic-payment-calculation-2026.pdf).

Periodic CNESST payments go through Revenu Quebec, but the separate CNESST Statement of Wages determines the occupational health and safety assessment. Do not put CNESST amounts into the RL-1 summary balance payable. Pay any CNESST assessment balance to CNESST as instructed on its statement. The CNESST guide requires the 2026 Statement of Wages **before March 15, 2027**, with an earlier 45-day rule when the last worker permanently leaves. Keep confirmation and reconcile the assessment to periodic payments. [Guide section 4 and its deadline footnote](https://www.cnesst.gouv.qc.ca/sites/default/files/documents/periodic-payment-calculation-2026.pdf).

The labour standards contribution was **not abolished or absorbed into the occupational health and safety premium**. Calculate its own 0.06% contribution on eligible remuneration, capped per employee. Check exemptions for the listed religious/charitable bodies, Canada Labour Code employers and international organizations. Use **LE-39.0.2-V**, then enter the subject base on RL-1 summary line 61, the contribution on line 63 and the payment on line 64. The contribution on line 63 comes from LE-39.0.2-V line 36. Pay annually with that summary. This form is not the WSDRF training calculation. [Labour standards contribution](https://www.revenuquebec.ca/en/businesses/source-deductions-and-employer-contributions/calculating-source-deductions-and-contributions/contribution-related-to-labour-standards/).

### 7. Determine the WSDRF shortfall

Determine this business's WSDRF subject payroll across its establishments; do not import the HSF worldwide associated-group figure. If subject payroll is exactly CAD 2,000,000 or less, there is no WSDRF obligation under the threshold test. Above it, calculate the 1% training requirement, deduct substantiated eligible expenditures and allowable carryforwards, and pay only a positive shortfall. A valid training initiative quality certificate exempts the contribution for its period of validity. [WSDRF rules](https://www.revenuquebec.ca/en/businesses/source-deductions-and-employer-contributions/calculating-source-deductions-and-contributions/contribution-to-the-workforce-skills-development-and-recognition-fund/).

Follow the current RL-1 summary work chart, including assistance adjustments and the special rule allowing preceding-year eligible expenditure into the first above-threshold year. Do not treat every historical training cost as a carryforward. The summary guide has separate treatment for excess eligible expenditure and multiple establishments. Report WSDRF payroll on summary line 71, the 1% requirement on line 73, eligible expenditure on line 74 and the shortfall on line 75. With a valid training initiative quality certificate, leave lines 71-75 blank. This is not the LE-39.0.2-V calculation. [Summary section 5.7](https://www.revenuquebec.ca/en/online-services/forms-and-publications/rlz-1-s-g-v/guide-to-filing-the-rl-1-summary-summary-of-source-deductions-and-employer-contributions/).

### 8. Produce the employer working paper

Show employee deductions and employer costs separately, by component. Reconcile employee-level gross pay to total payroll, component-specific subject wages to source documents, contribution limits to year-to-date payroll, and each liability to its destination. Federal income tax and EI go to CRA. Quebec income tax, QPP, QPIP and HSF go to Revenu Quebec. Labour standards and WSDRF settle annually with the RL-1 summary. CNESST has its own assessment and annual statement even when periodic payments travel through Revenu Quebec. Do not include employee deductions as employer expense or describe an illustrative contribution subtotal as full employment cost.

## Boundary and exception table

| Situation | Action before calculating | Source |
|---|---|---|
| Genuine self-employment, mixed CPP/QPP or multiple provinces | Use the personal-return and province-of-employment methods; do not double employer rates mechanically | https://www.revenuquebec.ca/en/citizens/income-tax-return/paying-a-balance-due-or-receiving-a-refund/paying-contributions-and-premiums/contributions-and-premiums-payable-by-a-self-employed-person-or-a-member-of-a-partnership/qpp-contribution-payable-by-a-self-employed-person-or-a-member-of-a-partnership/; https://www.canada.ca/en/revenue-agency/services/tax/businesses/topics/payroll/calculating-deductions/determining-tax-treatment/quebec-employee.html |
| Age, retirement pension, RR-50-V election or disability | Establish actual covered periods and exemptions; retain election/effective date | https://www.revenuquebec.ca/en/businesses/source-deductions-and-employer-contributions/calculating-source-deductions-and-contributions/special-cases-source-deductions-and-employer-contributions/employee-who-is-at-least-65-but-under-73-at-the-end-of-the-year-who-elects-to-stop-contributing-to-the-qpp/; https://www.revenuquebec.ca/en/online-services/forms-and-publications/rl-1-g-v/guide-to-filing-the-rl-1-slip-employment-and-other-income/ |
| Public sector or primary/manufacturing activities | Apply the correct HSF definition, not the ordinary small-business column | https://www.revenuquebec.ca/en/businesses/source-deductions-and-employer-contributions/calculating-source-deductions-and-contributions/employer-contribution-to-the-health-services-fund/total-payroll-threshold-and-health-services-fund-contribution-rate/; https://www.revenuquebec.ca/en/online-services/forms-and-publications/rlz-1-s-g-v/guide-to-filing-the-rl-1-summary-summary-of-source-deductions-and-employer-contributions/ |
| Agriculture, forestry, fishing, sawmill or pulp activities | Test the special 2026-2027 HSF exemption using own payroll and eligible duties | https://www.revenuquebec.ca/en/press-room/tax-news/details/2026-02-12/broadening-of-the-temporary-exemption-from-health-services-fund-contributions-for-the-agriculture-forestry-and-fishing-sectors/ |
| Indigenous/on-reserve remuneration, foreign posting or social-security agreement | Check the remuneration and coverage exceptions individually; obtain the certificate where relevant | https://www.revenuquebec.ca/en/businesses/source-deductions-and-employer-contributions/calculating-source-deductions-and-contributions/employer-contribution-to-the-health-services-fund/remuneration-subject-to-the-contribution/; https://www.revenuquebec.ca/en/online-services/forms-and-publications/rl-1-g-v/guide-to-filing-the-rl-1-slip-employment-and-other-income/ |
| Non-resident employer, remote employee or establishment change | Resolve payroll coverage, withholding and reporting separately before using this overlay | https://www.canada.ca/en/revenue-agency/services/tax/businesses/topics/payroll/calculating-deductions/determining-tax-treatment/quebec-employee.html |
| Successor, amalgamation or subsidiary wind-up | Use the summary/slip guide's continuity rules; do not automatically restart annual limits | https://www.revenuquebec.ca/en/online-services/forms-and-publications/rlz-1-s-g-v/guide-to-filing-the-rl-1-summary-summary-of-source-deductions-and-employer-contributions/; https://www.revenuquebec.ca/en/online-services/forms-and-publications/rl-1-g-v/guide-to-filing-the-rl-1-slip-employment-and-other-income/ |
| Multiple CNESST units, construction weekly basis or retrospective rating | Use CNESST classification, wage allocation and actual rating notices | https://www.cnesst.gouv.qc.ca/sites/default/files/documents/periodic-payment-calculation-2026.pdf |
| Training certificate or disputed training eligibility | Check certificate validity and supporting evidence before reducing WSDRF | https://www.revenuquebec.ca/en/businesses/source-deductions-and-employer-contributions/calculating-source-deductions-and-contributions/contribution-to-the-workforce-skills-development-and-recognition-fund/; https://www.revenuquebec.ca/en/online-services/forms-and-publications/rlz-1-s-g-v/guide-to-filing-the-rl-1-summary-summary-of-source-deductions-and-employer-contributions/ |

## Worked cases

### Case 1: one employee, CAD 55,000 in 2026

An ordinary private service employer has one full-year employee, no associated employers, no exemptions and CAD 55,000 of cash wages subject to each contribution. The employee is eligible for full-year QPP. The hypothetical CNESST notice assigns CAD 0.18 per CAD 100 of insurable wages; **this is an example input, not a published sector rate**. No WSDRF threshold is met. Use the annual check only, not a pay-period withholding instruction.

```oa-check
name: Quebec employer annual contribution check, one employee, 2026
inputs:
  wages: 55000
  cnesst_dollars_per_100: 0.18
steps:
  - qpp_first_each: round(max(0, min(wages, 74600) - 3500) * 0.063, 2)
  - qpp_second_each: round(max(0, min(wages, 85000) - 74600) * 0.04, 2)
  - qpip_employee: round(min(wages, 103000) * 0.00430, 2)
  - qpip_employer: round(min(wages, 103000) * 0.00602, 2)
  - hsf: round(wages * 0.0165, 2)
  - labour_standards: round(min(wages, 103000) * 0.0006, 2)
  - cnesst: round(min(wages, 103000) / 100 * cnesst_dollars_per_100, 2)
  - employee_quebec_contributions: qpp_first_each + qpp_second_each + qpip_employee
  - employer_quebec_contributions: qpp_first_each + qpp_second_each + qpip_employer + hsf + labour_standards + cnesst
expected:
  qpp_first_each: 3244.50
  qpp_second_each: 0
  qpip_employee: 236.50
  qpip_employer: 331.10
  hsf: 907.50
  labour_standards: 33.00
  cnesst: 99.00
  employee_quebec_contributions: 3481.00
  employer_quebec_contributions: 4615.10
```

The employer subtotal excludes federal EI, wages, income tax deductions and any benefits/other costs. It is not a take-home-pay result.

### Case 2: the nine-person employer reconciles to CAD 885,000

Six employees earn CAD 95,000, two earn CAD 130,000 and one earns CAD 55,000. All are full-year eligible employees of the same ordinary service employer, without associated employers or exemptions. All pay is subject to the listed contributions. Use the same hypothetical CNESST notice rate as case 1. Actual wages are CAD 885,000; do not replace the total by CAD 800,000 while keeping the employee list unchanged.

```oa-check
name: Quebec nine-person annual payroll reconciliation, 2026
inputs:
  standard_count: 6
  standard_wage: 95000
  senior_count: 2
  senior_wage: 130000
  manager_wage: 55000
  cnesst_dollars_per_100: 0.18
steps:
  - payroll: standard_count * standard_wage + senior_count * senior_wage + manager_wage
  - qpp_first_each_total: (standard_count + senior_count) * 4479.30 + (manager_wage - 3500) * 0.063
  - qpp_second_each_total: (standard_count + senior_count) * 416
  - capped_qpip_wages: standard_count * min(standard_wage, 103000) + senior_count * min(senior_wage, 103000) + manager_wage
  - qpip_employer: round(capped_qpip_wages * 0.00602, 2)
  - hsf: round(payroll * 0.0165, 2)
  - labour_standards: round(capped_qpip_wages * 0.0006, 2)
  - cnesst: round(capped_qpip_wages / 100 * cnesst_dollars_per_100, 2)
  - employer_quebec_contributions: qpp_first_each_total + qpp_second_each_total + qpip_employer + hsf + labour_standards + cnesst
expected:
  payroll: 885000
  qpp_first_each_total: 39078.90
  qpp_second_each_total: 3328.00
  capped_qpip_wages: 831000
  qpip_employer: 5002.62
  hsf: 14602.50
  labour_standards: 498.60
  cnesst: 1495.80
  employer_quebec_contributions: 64006.42
```

Although the capped wage totals happen to match in this cash-only example, QPIP, labour standards and CNESST bases must be tested independently in real payroll. CNESST does not cap all eight higher-paid employees at the maximum: the six CAD 95,000 employees remain below it. WSDRF is zero under the threshold.

## When to refuse or refer

Do not produce a final payroll deduction from annual earnings alone, guess a worker's legal classification, assume a tax/benefit exemption, invent a CNESST rate or use a prior-year table. Calculate only the supported component and identify which fact is missing. Near a threshold, show both outcomes; do not treat an employer as legally liable merely because a figure is within 5% of the threshold. Never convert an unknown fact into a stated higher liability.

Refer disputed employee status, foreign/non-resident payroll obligations, Indigenous exemptions, social-security coverage and complex employer succession to the relevant payroll/tax specialist. Refer CNESST multi-unit allocation, personal/volunteer coverage and retrospective assessment to the CNESST adviser. Training eligibility and certificates require evidence under CPMT rules. Pay equity and health-and-safety prevention obligations are separate from this contribution computation, not abolished by it.

## Filing and payment

Use the frequency assigned by Revenu Quebec. Do not change frequency until the Notice of Change in Filing Frequency of Returns is received. For 2026 the authority publishes these conditions and due dates; the two-year lookback is explicit, not a current-payroll shortcut. [Frequency table](https://www.revenuquebec.ca/en/businesses/source-deductions-and-employer-contributions/remitting-source-deductions-and-employer-contributions/frequency-of-remittances/).

| Frequency | Published eligibility for 2026 | Due date | Source |
|---|---|---|---|
| Annual | 2025 source deductions/employer contributions CAD 2,400 or less, or estimated for 2026 | 15th of month after last month remuneration was paid, usually January 15 | https://www.revenuquebec.ca/en/businesses/source-deductions-and-employer-contributions/remitting-source-deductions-and-employer-contributions/frequency-of-remittances/ |
| Quarterly, existing employer | Average monthly remittance in 2024 or 2025 CAD 3,000 or less; fiscal obligations met over last 12 months | April 15, July 15, October 15 and January 15 | https://www.revenuquebec.ca/en/businesses/source-deductions-and-employer-contributions/remitting-source-deductions-and-employer-contributions/frequency-of-remittances/ |
| Quarterly, new employer | Each month's source deductions and contributions below CAD 1,000; fiscal obligations met | Same quarterly dates | https://www.revenuquebec.ca/en/businesses/source-deductions-and-employer-contributions/remitting-source-deductions-and-employer-contributions/frequency-of-remittances/ |
| Monthly | 2024 average monthly remittance below CAD 25,000, or new employer, subject to assigned eligible frequency | 15th of following month | https://www.revenuquebec.ca/en/businesses/source-deductions-and-employer-contributions/remitting-source-deductions-and-employer-contributions/frequency-of-remittances/ |
| Twice monthly | 2024 average at least CAD 25,000 but below CAD 100,000 | 25th for first half; 10th of next month for second half | https://www.revenuquebec.ca/en/businesses/source-deductions-and-employer-contributions/remitting-source-deductions-and-employer-contributions/frequency-of-remittances/ |
| Weekly | 2024 average at least CAD 100,000 | Third business day after each period ending on the 7th, 14th, 21st or last day | https://www.revenuquebec.ca/en/businesses/source-deductions-and-employer-contributions/remitting-source-deductions-and-employer-contributions/frequency-of-remittances/ |

In My Account for businesses, or My Account for professional representatives with authority, prepare the source-deductions remittance using the correct account and period. Use the issued TPZ-1015.R.14.1-V, TPZ-1015.R.14.2-V, TPZ-1015.R.14.3-V or TPZ-1015.R.14.4-V form/payment reference for the assigned frequency, as applicable. Reconcile Quebec income tax, employee/employer QPP and QPIP and employer HSF; keep the CNESST periodic amount separate in the relevant remittance fields. Retain confirmation and reconcile actual bank processing, rather than treating a saved draft as payment.

Prepare the RL-1 slips and RL-1 summary (RLZ-1.S-V) for the year. The usual statutory filing deadline is the last day of February of the following year; apply the authority's due-date calendar rather than invent a calendar-day extension. Give each employee their RL-1 copy by the applicable RL-1 deadline as well; filing with the authority does not replace delivery to the employee. An RL-1 summary is required for each employer account. The guide allows My Account, approved software or the prescribed paper/PDF route; filing slips electronically alone does not file the summary. Include the labour standards calculation and WSDRF annual shortfall, reconcile remittances and retain the filed summary and payment receipt. Do not include CNESST in that summary remittance. [Summary guide, sections 3-6](https://www.revenuquebec.ca/en/online-services/forms-and-publications/rlz-1-s-g-v/guide-to-filing-the-rl-1-summary-summary-of-source-deductions-and-employer-contributions/).

If payroll permanently stops because there are no employees, the summary is due by the 20th of the month following the last-remittance month; if business activities stop, by the 30th day after cessation; if the responsible person dies, by the 90th day after death. These are separate from CNESST's last-worker rule. [Summary section 4.2](https://www.revenuquebec.ca/en/online-services/forms-and-publications/rlz-1-s-g-v/guide-to-filing-the-rl-1-summary-summary-of-source-deductions-and-employer-contributions/).

Revenu Quebec late remittance penalties on withheld/collected amounts are 7% for days 1-7, 11% for days 8-14 and 15% from day 15, with applicable interest. Do not substitute CRA penalties. Late summary filing has a separate statutory penalty; do not reuse the old unsupported per-slip formula. CNESST's 2026 guide provides a 15% insufficient-instalment penalty and a CAD 25 to CAD 2,500 late-statement penalty, with its separate interest rules. [Summary sections 6.4-6.5](https://www.revenuquebec.ca/en/online-services/forms-and-publications/rlz-1-s-g-v/guide-to-filing-the-rl-1-summary-summary-of-source-deductions-and-employer-contributions/); [CNESST guide sections 3.4 and 4](https://www.cnesst.gouv.qc.ca/sites/default/files/documents/periodic-payment-calculation-2026.pdf).

## Completion checklist

- Year, employment province, employee eligibility and elections are evidenced.
- Current rates, separate component bases and caps match the official source and actual pay-period method.
- Employee wages sum exactly to payroll; HSF rate payroll is kept separate from subject Quebec wages and WSDRF payroll.
- CNESST rate/classification comes from the employer notice, not this example.
- Employee deductions and employer costs reconcile separately to CRA, Revenu Quebec and CNESST destinations.
- Annual labour standards/WSDRF, RL-1 slips/summary and separate CNESST filing are tracked with confirmations.
- Approval stays Not yet approved unless an approved accountant stands behind this exact version.

## Sources

Official pages were read on 2026-11-13 through the web tool. Direct script downloads returned HTTP 403; that failure is not counted as source verification. The table states which portions were actually read. Statutory references for HSF, labour standards and WSDRF are reproduced in the authority's RL-1 summary guide: ARAMQ sections 33-34, ALS sections 39.0.3-39.0.6, AWSDR sections 15-19; late remittance TAA section 59.2. This skill relies on those opened authority instructions, not an assertion that every consolidated act was separately read.

| Official source and portion read | URL | Read on |
|---|---|---|
| Read for Revenu Quebec principal changes: 2026 QPP, QPIP, HSF and labour standards tables | https://www.revenuquebec.ca/en/businesses/source-deductions-and-employer-contributions/employers-principal-changes-for-2026/ | 2026-11-13 |
| Read for QPP historical table: 2025 and 2026 first-tier maximums | https://www.revenuquebec.ca/en/businesses/source-deductions-and-employer-contributions/calculating-source-deductions-and-contributions/qpp-contributions/maximum-pensionable-earnings-and-contribution-rate/ | 2026-11-13 |
| Read for HSF rate table: ordinary, primary/manufacturing and public-sector columns | https://www.revenuquebec.ca/en/businesses/source-deductions-and-employer-contributions/calculating-source-deductions-and-contributions/employer-contribution-to-the-health-services-fund/total-payroll-threshold-and-health-services-fund-contribution-rate/ | 2026-11-13 |
| Read for HSF total payroll: worldwide associated employers and activity attribution | https://www.revenuquebec.ca/en/businesses/source-deductions-and-employer-contributions/calculating-source-deductions-and-contributions/employer-contribution-to-the-health-services-fund/total-payroll/ | 2026-11-13 |
| Read for HSF subject remuneration and foreign-posting exclusions | https://www.revenuquebec.ca/en/businesses/source-deductions-and-employer-contributions/calculating-source-deductions-and-contributions/employer-contribution-to-the-health-services-fund/remuneration-subject-to-the-contribution/ | 2026-11-13 |
| Read for Labour standards: contribution, exemptions, LE-39.0.2-V and annual payment | https://www.revenuquebec.ca/en/businesses/source-deductions-and-employer-contributions/calculating-source-deductions-and-contributions/contribution-related-to-labour-standards/ | 2026-11-13 |
| Read for WSDRF: threshold, shortfall, certificate, summary and payment | https://www.revenuquebec.ca/en/businesses/source-deductions-and-employer-contributions/calculating-source-deductions-and-contributions/contribution-to-the-workforce-skills-development-and-recognition-fund/ | 2026-11-13 |
| Read for 2026 remittance frequency table and notice requirement | https://www.revenuquebec.ca/en/businesses/source-deductions-and-employer-contributions/remitting-source-deductions-and-employer-contributions/frequency-of-remittances/ | 2026-11-13 |
| Read for RL-1 summary guide: account/filing rules, HSF, labour standards, WSDRF, interest and penalties | https://www.revenuquebec.ca/en/online-services/forms-and-publications/rlz-1-s-g-v/guide-to-filing-the-rl-1-summary-summary-of-source-deductions-and-employer-contributions/ | 2026-11-13 |
| Read for RL-1 guide: QPP boxes, eligible ages, H/I, special transfers and postings | https://www.revenuquebec.ca/en/online-services/forms-and-publications/rl-1-g-v/guide-to-filing-the-rl-1-slip-employment-and-other-income/ | 2026-11-13 |
| Read for CNESST 2026 periodic payment guide: printed pages 8-10 and 16-21, wage ceilings, remittance and assessment/penalties | https://www.cnesst.gouv.qc.ca/sites/default/files/documents/periodic-payment-calculation-2026.pdf | 2026-11-13 |
| Read for QPP election: age, pension requirement, form and effective month | https://www.revenuquebec.ca/en/businesses/source-deductions-and-employer-contributions/calculating-source-deductions-and-contributions/special-cases-source-deductions-and-employer-contributions/employee-who-is-at-least-65-but-under-73-at-the-end-of-the-year-who-elects-to-stop-contributing-to-the-qpp/ | 2026-11-13 |
| Read for Self-employed QPP: 2026 rates and separate return treatment | https://www.revenuquebec.ca/en/citizens/income-tax-return/paying-a-balance-due-or-receiving-a-refund/paying-contributions-and-premiums/contributions-and-premiums-payable-by-a-self-employed-person-or-a-member-of-a-partnership/qpp-contribution-payable-by-a-self-employed-person-or-a-member-of-a-partnership/ | 2026-11-13 |
| Read for Quebec government 2026 QPIP table, including self-employed rate and maximum | https://www.quebec.ca/entreprises-et-travailleurs-autonomes/administrer-gerer/embauche-gestion-personnel/assurance-parentale/taux-cotisations | 2026-11-13 |
| Read for QPIP employer guide: eligibility, age, periodic payment and calculation tools | https://www.revenuquebec.ca/en/businesses/source-deductions-and-employer-contributions/calculating-source-deductions-and-contributions/qpip-premiums/qpip-premiums-what-you-need-to-know/ | 2026-11-13 |
| Read for CRA Quebec employee page: province-of-employment and Quebec coordination | https://www.canada.ca/en/revenue-agency/services/tax/businesses/topics/payroll/calculating-deductions/determining-tax-treatment/quebec-employee.html | 2026-11-13 |
| Read for HSF 2026-2027 exemption: eligible activities, own-payroll test, effective and periodic-payment dates | https://www.revenuquebec.ca/en/press-room/tax-news/details/2026-02-12/broadening-of-the-temporary-exemption-from-health-services-fund-contributions-for-the-agriculture-forestry-and-fishing-sectors/ | 2026-11-13 |

Not yet confirmed: this skill does not supply a full 2026 self-employed QPIP return computation, disability/exempt-worker contribution computation, CNESST retrospective qualification threshold, CPMT training-cost substantiation or pay-equity/prevention-program procedures. The prior skill's fixed sector CNESST ranges, retrospective threshold, triennial pay-equity assertion, blanket higher-liability defaults and exact late-RL-slip penalty were not substantiated and are not usable rules here. A per-pay-period engine and HSF intermediate-rate precision must follow current WebRAS/formula instructions, not the annual examples. Other Canadian skills may still contain 2025 figures; this update does not certify them.
