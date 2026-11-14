---
name: ok-payroll
description: "Apply Oklahoma 2026 withholding with OK-W-4 and OW-2 percentage or wage tables, whole-dollar rounding, OkTAP WTH10001 and payment schedules. Also covers employer UI: published $25,000 base, 1.5% new rate, 0.2%-5.8% range, registration and quarterly wage reporting. Trigger on OK payroll, withholding or OESC contributions."
license: "AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)"
metadata:
  source: openaccountants
  openaccountants_url: "https://www.openaccountants.com/skills/ok-payroll"
  jurisdiction: "US-OK"
  tax_year: "2026"
  last_updated: "2026-11-13"
---

# Oklahoma payroll withholding and unemployment insurance, tax year 2026

> **Source-cited draft.** Written by Codex. Not reviewed by an accountant. This skill supports a professional working paper; review the taxpayer facts and current forms before filing. Circular 230 section 10.37: this material is not a legal opinion or a substitute for reasonable factual and legal inquiry.

**Answer first.** Oklahoma employers run two state systems: employee income-tax withholding through OTC and employer unemployment contributions through OESC. The 2026 UI wage base is $25,000 per employee and the ordinary new-employer rate is 1.5%; use the employer’s actual rate notice.

## Scope and who this is for

Oklahoma wage withholding and unemployment insurance for ordinary contributing employers. Federal wages, employment taxes and Forms 941/940 belong in `us-form-941-940-payroll`; no federal rate or wage base is restated here. Interstate localization, exempt workers and reimbursing employers need separate facts. The 2026 OW-2 and 2026 OESC numbers are published; older procedural material is identified below.

## Ask the client first

1. Where does each worker physically work and reside, and what interstate work or predecessor payroll applies?
2. Are the workers employees, owners or contractors, and do domestic, farm, ministerial, tribal or nonprofit exceptions apply?
3. What marital choice, allowances, exemption claim and extra withholding are on each current OK-W-4; what pay frequency applies?
4. What are current-period and year-to-date covered wages per employee, and what is the actual 2026 OESC rate notice?
5. What OTC/OESC account numbers, deposit schedules, prior-fiscal-year monthly withholding and reporting access exist?

## The method, step by step

### Rates, bands and thresholds

| Item and conditions | Amount / treatment | Official source |
| --- | --- | --- |
| 2026 UI annual taxable wages | $25,000 per employee | [official text](https://oklahoma.gov/content/dam/ok/en/oesc/images/misc/Employer-Improtant-Numbers-2026.pdf) |
| 2026 UI ordinary new employer / experienced range | 1.5% / 0.2%-5.8%; Conditional Factor A and State Factor 30%; actual notice controls | [official text](https://oklahoma.gov/content/dam/ok/en/oesc/images/misc/Employer-Improtant-Numbers-2026.pdf) |
| 2026 withholding allowance amounts | Weekly $19.23; biweekly $38.46; semimonthly $41.67; monthly $83.33; quarterly $250; semiannual $500; annual $1,000; daily $3.85 each allowance | [2026 OW-2 pp.2-9](https://oklahoma.gov/content/dam/ok/en/tax/documents/resources/publications/businesses/withholding-tables/WHTables-2026.pdf) |
| Monthly single, net wages after allowances | Up to $842: zero; $842-$938: 2.5% excess over $842; $938-$1,129: $2.40 + 3.5% excess over $938; above $1,129: $9.10 + 4.5% excess over $1,129 | [2026 OW-2 pp.2-9](https://oklahoma.gov/content/dam/ok/en/tax/documents/resources/publications/businesses/withholding-tables/WHTables-2026.pdf) |
| Monthly married, net wages after allowances | Up to $1,683: zero; $1,683-$1,875: 2.5% excess over $1,683; $1,875-$2,258: $4.79 + 3.5% excess over $1,875; above $2,258: $18.21 + 4.5% excess over $2,258 | [2026 OW-2 pp.2-9](https://oklahoma.gov/content/dam/ok/en/tax/documents/resources/publications/businesses/withholding-tables/WHTables-2026.pdf) |
| UI ordinary coverage triggers | $1,500 quarterly wages OR an employee on at least one day in each of 20 weeks; special employer rules separate | [official text](https://oklahoma.gov/oesc/employers/tax.html) |
| Withholding delinquency | 10% penalty under OW-2 conditions; 1.25% monthly interest | [2026 OW-2 pp.2-9](https://oklahoma.gov/content/dam/ok/en/tax/documents/resources/publications/businesses/withholding-tables/WHTables-2026.pdf) |
| UI missing-report penalty after notice | Experience-rated: $200 + 10% contributions after 15-day notice window; interest 1% monthly | [official text](https://oklahoma.gov/oesc/employers/tax/wage-reporting.html) |

### Withholding

1. Determine whether compensation is for Oklahoma services and whether a statutory exclusion applies. The 2026 OW-2 identifies farm pay of $900 or less monthly, domestic service, some nonbusiness casual service, limited nonresident pay, and minister/religious-order services. Do not transplant these withholding exclusions into the separate UI coverage test. Source: [2026 OW-2 pp.2-9](https://oklahoma.gov/content/dam/ok/en/tax/documents/resources/publications/businesses/withholding-tables/WHTables-2026.pdf).
2. With FEIN, register the **payroll** withholding account in [OkTAP](https://oktap.tax.ok.gov), rather than a retirement account. Obtain the OTC account number. Use the worker’s **OK-W-4**, not an assumed federal allowance count. Source: [2026 OW-2 pp.2-9](https://oklahoma.gov/content/dam/ok/en/tax/documents/resources/publications/businesses/withholding-tables/WHTables-2026.pdf), [official text](https://oklahoma.gov/tax/helpcenter/businesses.html).
3. Choose the 2026 percentage table or wage-bracket method for the actual frequency and marital choice. A worker choosing married but higher single withholding uses the single table. Under the percentage method, subtract allowances times the published per-period allowance, apply that period’s formula and round to the nearest whole dollar, with 50 cents rounding up. The standard deduction is already embedded in the withholding table; do not deduct it again. Add any authorized extra withholding using the employee’s instruction. Above the last wage-bracket row use the percentage method for the entire payment. Source: [2026 OW-2 pp.2-9](https://oklahoma.gov/content/dam/ok/en/tax/documents/resources/publications/businesses/withholding-tables/WHTables-2026.pdf).
4. Prepare **WTH10001** quarterly with employee count, wages and total withholding. Payments alone do not file the return: from the quarter ending June 30, 2025 the agency requires a separately generated and filed quarterly return. Reconcile deposits to the quarter, submit through OkTAP and retain acknowledgment. Source: [official text](https://oklahoma.gov/tax/helpcenter/businesses.html), [2026 OW-2 pp.2-9](https://oklahoma.gov/content/dam/ok/en/tax/documents/resources/publications/businesses/withholding-tables/WHTables-2026.pdf).

### Unemployment insurance

1. Apply coverage and localization separately. Start employer registration/account enrollment using the links on [OESC’s paying-tax page](https://oklahoma.gov/oesc/employers/tax.html); identify the employer, ownership, FEIN, first payroll, locations and any predecessor. Keep the assigned SUTA number and actual rate notice. The 2026 portal launch and the agency’s transition page should be followed rather than assuming an old EZ Tax screen still exists. Sources: [official text](https://www.oklahoma.gov/oesc/about/newsroom/2026/january/oesc-launches-new-employer-portal--marking-major-technology-upgr.html), [official text](https://oklahoma.gov/oesc/employers/tax.html).
2. For each employee, current taxable wages = min(current covered wages, max(25,000 - prior 2026 covered wages, 0)). Sum taxable wages and multiply by the actual assigned rate. Report full gross wages as well as excess/taxable wages; a wage above the base does not disappear from the report. The published new rate is 1.5%; an experienced employer uses its notice. Source: [official text](https://oklahoma.gov/content/dam/ok/en/oesc/images/misc/Employer-Improtant-Numbers-2026.pdf), [official text](https://oklahoma.gov/oesc/employers/tax/wage-reporting.html).
3. File quarterly contributions and wages online through the OESC-linked portal: select the account and quarter, enter/upload employee name, SSN and gross wages, reconcile taxable excess and rate, submit, then pay and save both confirmations. Active accounts must report even with zero wages. The public pages confirm the workflow’s required data; authenticated button names are not asserted here. Sources: [official text](https://oklahoma.gov/oesc/employers/tax/wage-reporting.html), [OAC 240:10-5-91](https://oklahoma.gov/content/dam/ok/en/oesc/documents/policies/Title_240%20-%20effective%208.12.24.pdf).
4. Review benefit-wage and rate notices. Experience uses benefit-wage charges divided by timely taxable wages and the year’s rate table; do not use the current landing page’s **2027** wage base for 2026. Termination, acquisition and corrections use the appropriate OESC account/adjustment process. Sources: [official text](https://oklahoma.gov/oesc/employers/tax/contribution-rates.html), [official text](https://oklahoma.gov/oesc/employers/tax.html).


## Boundary and exception table

| Situation | Treatment |
| --- | --- |
| Married worker elects higher single withholding | Use single table with the actual OK-W-4 allowances. |
| Already at UI wage base | Report wages but no additional ordinary UI taxable wages for that employee in the year. |
| New employer versus experienced employer | Confirm the notice; 1.5% is not a universal experienced rate. |
| Active account with no payroll | OESC still requires the quarterly zero report. |
| Domestic/agricultural/public/nonprofit/tribal employer | Special UI coverage or reimbursement rules can replace ordinary contribution treatment. |
| Multistate employee or business acquisition | Establish wage localization and successor treatment before applying the base. |

Sources: [2026 OW-2 pp.2-9](https://oklahoma.gov/content/dam/ok/en/tax/documents/resources/publications/businesses/withholding-tables/WHTables-2026.pdf), [official text](https://oklahoma.gov/oesc/employers/tax.html), [official text](https://oklahoma.gov/oesc/employers/tax/wage-reporting.html), [official text](https://oklahoma.gov/content/dam/ok/en/oesc/images/misc/Employer-Improtant-Numbers-2026.pdf).

## Worked cases

**Case 1.** A single employee earns $3,000 monthly and claims one OK-W-4 allowance, with no extra withholding. Net table wages = $3,000 - $83.33 = $2,916.67. Formula tax = $9.10 + 4.5% x ($2,916.67 - $1,129) = $89.54515; whole-dollar withholding is **$90**.

```oa-check
name: OK2026 monthly single withholding
inputs:
  gross: 3000
  allowances: 1
  allowance_value: 83.33
steps:
- net: gross-allowances*allowance_value
- unrounded: 9.10+(net-1129)*0.045
- withheld: floor(unrounded+0.5)
expected:
  net: 2916.67
  unrounded: 89.54515
  withheld: 90
```

**Case 2, wage-base decision.** A new employer with a confirmed 1.5% rate pays $4,000 this quarter. If prior 2026 wages were $24,000, $1,000 remains taxable and UI is **$15**. If prior wages were $10,000, all $4,000 remains taxable and UI is **$60**. A full-year $40,000 employee reaches $25,000 taxable wages and **$375** UI at that same rate.

```oa-check
name: OK2026 UI cap both wage histories
inputs:
  current: 4000
  prior_high: 24000
  prior_low: 10000
  annual: 40000
  rate: 0.015
steps:
- high_base: min(current,max(25000-prior_high,0))
- low_base: min(current,max(25000-prior_low,0))
- high_tax: high_base*rate
- low_tax: low_base*rate
- annual_tax: min(annual,25000)*rate
expected:
  high_base: 1000
  low_base: 4000
  high_tax: 15
  low_tax: 60
  annual_tax: 375
```


## When to refuse or refer

Refer classification disputes, interstate localization, tribal immunity, farm/domestic eligibility, reimbursing employers, successor wage transfer and rate appeals. Withheld employee tax is trust money; UI contributions are a separate employer obligation.

## Filing and payment

**OTC:** OW-2 states quarterly remittance by the 20th after quarter-end when withholding does not exceed $500 per quarter, and monthly remittance by the 20th when above that ordinary quarterly threshold. It separately requires electronic payment where previous-fiscal-year withholding was at least $5,000 monthly, and federal semiweekly timing for employers averaging at least $10,000 monthly or otherwise on that schedule. Follow the account’s assigned schedule; do not wait for the quarterly return where deposits are due sooner. The packet’s wording around the $5,000 boundary mixes quarterly and monthly tests, so resolve an unclear account assignment rather than inventing a frequency. Sources: [2026 OW-2 pp.2-9](https://oklahoma.gov/content/dam/ok/en/tax/documents/resources/publications/businesses/withholding-tables/WHTables-2026.pdf), [official text](https://oklahoma.gov/tax/helpcenter/businesses.html).

**OESC:** OAC 240:10-5-91 requires quarterly wage report and payment by the last day of the following month: April 30, July 31, October 31 and January 31. Check weekend/holiday application in the account; it is not independently confirmed here. File and pay electronically unless an exception applies. Retain electronic acceptance and payment date. Source: [official text](https://oklahoma.gov/content/dam/ok/en/oesc/documents/policies/Title_240%20-%20effective%208.12.24.pdf). After a Notice of Non-Receipt, missing the 15-day cure window triggers the stated reporting penalty; this is not an extension of the original filing deadline. Source: [official text](https://oklahoma.gov/oesc/employers/tax/wage-reporting.html).

**Annual wage reporting:** OW-2 confirms electronic W-2/W-3 upload or manual entry in OkTAP, but its deadline paragraph still names tax year 2025. The 2026 wage-statement deadline and final 2027 calendar adjustment are therefore explicitly pending rather than silently copied. Source: [2026 OW-2 pp.2-9](https://oklahoma.gov/content/dam/ok/en/tax/documents/resources/publications/businesses/withholding-tables/WHTables-2026.pdf).

## Completion checklist

- Keep signed OK-W-4s, actual rate notice and coverage/localization support.
- Reconcile gross and taxable wages, rounded withholding, UI and both agency accounts.
- Submit the quarterly OTC return separately from payment.
- Save OESC report and payment references and report zero quarters where required.

## Sources

| Source | URL | Read on |
| --- | --- | --- |
| OTC 2026 OW-2. Read for pp.2-9, exclusions, registration, payment wording, withholding allowances/formulas and rounding; stale 2025 wage-statement paragraph identified. | https://oklahoma.gov/content/dam/ok/en/tax/documents/resources/publications/businesses/withholding-tables/WHTables-2026.pdf | 2026-11-13 |
| OTC business help. Read for WTH10001, OK-W-4, separate quarterly-return generation since Q2 2025 and payment schedules. | https://oklahoma.gov/tax/helpcenter/businesses.html | 2026-11-13 |
| OESC important numbers for 2026. Read for $25,000 base, 1.5% new rate, 0.2%-5.8% range and 2026 factors. | https://oklahoma.gov/content/dam/ok/en/oesc/images/misc/Employer-Improtant-Numbers-2026.pdf | 2026-11-13 |
| OESC paying unemployment tax. Read for coverage, current portal links, forms and separate UI registration/account. | https://oklahoma.gov/oesc/employers/tax.html | 2026-11-13 |
| OESC January 2026 launch. Read for new Employer Portal launch and current access context. | https://www.oklahoma.gov/oesc/about/newsroom/2026/january/oesc-launches-new-employer-portal--marking-major-technology-upgr.html | 2026-11-13 |
| OESC wage reporting. Read for employee data, mandatory online/zero reports, notice penalties and interest. | https://oklahoma.gov/oesc/employers/tax/wage-reporting.html | 2026-11-13 |
| OESC contribution rates. Read for experience-rating method, notice and new rate; main numeric table is 2027 and not used for 2026. | https://oklahoma.gov/oesc/employers/tax/contribution-rates.html | 2026-11-13 |
| OESC published rules. Read for OAC 240:10-5-91 quarterly reporting and payment; procedural baseline published 2024. | https://oklahoma.gov/content/dam/ok/en/oesc/documents/policies/Title_240%20-%20effective%208.12.24.pdf | 2026-11-13 |

Not yet confirmed: Authenticated 2026 registration/upload/amendment screens and current file layouts; special farm/domestic/nonprofit/tribal coverage and successor wage transfer; withholding account frequency at ambiguous boundaries; 2026 W-2/W-3 deadline; UI weekend/holiday due-date adjustment. No 2027 numeric rate/base is applied to 2026.

## Today's figures and who stands behind this skill

This file is an AI skill (tax rules your AI follows) from OpenAccountants, copied on 2026-11-13. Rates, thresholds and deadlines change. For the current version of this skill, its official sources and the named accountant (if any) who stands behind it, call `get_skill` with slug `ok-payroll` on the OpenAccountants connector (https://www.openaccountants.com/connect), or read https://www.openaccountants.com/skills/ok-payroll. If neither is available, confirm every figure against the official source pages cited above before relying on it.
