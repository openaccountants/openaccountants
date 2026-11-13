---
name: dc-payroll
description: "District of Columbia payroll withholding and unemployment (2026), tax year 2026: applicability, state computations, exceptions, registration, returns, payment and source-backed worked cases."
jurisdiction: US-DC
category: payroll
domain: tax
tax_year: 2026
tier: 2
last_updated: 2026-11-13
version: "1.0"
type: situation-rules
---

# District of Columbia payroll withholding and unemployment (2026)

**Circular 230 §10.37 disclosure:** This skill supplies general state-tax working papers from the sources below. It is not a professional approval. A qualified tax professional must review the facts, assumptions and outputs before filing.

**Answer first:** DC resident wage withholding goes to OTR through FR-900Q/FR-900A as assigned; employer UI goes separately to DOES. For 2026, DOES confirms a $9,000 employee wage base, 2.7% new-employer UI rate and separate 0.2% administrative assessment. The withholding computation is partial: a usable current 2026 wage-table/allowance schedule was not confirmed, so this skill must not invent one from annual income brackets. [2026 FR-900Q](https://otr.cfo.dc.gov/sites/default/files/dc/sites/otr/publication/attachments/2026_FR900Q_Instructions%20v1.0_Final.pdf); [2026 DOES announcement](https://essp.does.dc.gov/DOES%20ESSP%20Employer%20Landing%20Page.html).

## Scope

DC 2026 wage withholding registration, reports/payments and state unemployment contributions, rates, base and returns. Federal FICA/FUTA and Forms 941/940 remain in `us-form-941-940-payroll`. DC individual income/rate treatment is in `dc-income-tax`; annual tax brackets are not payroll tables. Non-payroll withholding (FR-900NP), paid family leave, workers' compensation and wage-law rates are distinct jobs, not computations claimed here.

## Ask the client first

1. Employee DC residence/domicile, any DC abode and exemption/nonresidence certificates, plus actual work locations?
2. Employer FEIN, OTR withholding account, DOES account, assigned deposit/report frequencies and 2026 rate notice?
3. Pay period, gross/taxable compensation, allowances/elections and an actually applicable current withholding table?
4. Each employee's current and year-to-date wages, other-state covered wages and localization/transfer evidence?
5. Household, nonprofit/reimbursable, successor, PEO or agent status?
6. Prior returns/payments, account balances and any corrections or notices?

## The method, step by step

### Rates, bands and thresholds

| Item | Amount or rule | Official source |
| --- | --- | --- |
| New employer UI, 2026 | 2.7% before separate assessment | [DOES 2026 portal announcement](https://essp.does.dc.gov/DOES%20ESSP%20Employer%20Landing%20Page.html) |
| Administrative assessment, 2026 | 0.2% separately from contribution | [DOES 2026 portal announcement](https://essp.does.dc.gov/DOES%20ESSP%20Employer%20Landing%20Page.html) |
| UI annual wage base | $9,000 per covered employee | [DOES 2026 portal announcement](https://essp.does.dc.gov/DOES%20ESSP%20Employer%20Landing%20Page.html) |
| Experience rates, 2026 | Table VI: 1.9% to 7.4%, before separate assessment; actual reserve ratio selects the row | [§51-103(c)(8)(A) Table VI](https://code.dccouncil.gov/us/dc/council/code/sections/51-103) |
| Annual wage withholding return eligibility | Assigned annual filer with less than $200 annual threshold; FR-900A is not annual reconciliation | [OTR withholding forms](https://otr.cfo.dc.gov/page/withholding-tax-forms) |
| FR-900Q return due | Last day of month after quarter; Q3 October 31, despite FAQ typo October 30 | [2026 FR-900Q p.2](https://otr.cfo.dc.gov/sites/default/files/dc/sites/otr/publication/attachments/2026_FR900Q_Instructions%20v1.0_Final.pdf) |
| FR-900A 2026 | Deposit January 20, 2027; return January 31, 2027, subject to business-day rule | [OTR withholding forms](https://otr.cfo.dc.gov/page/withholding-tax-forms) |
| Electronic payments | Payment exceeding $5,000 per period must be electronic | [2026 FR-900Q p.1](https://otr.cfo.dc.gov/sites/default/files/dc/sites/otr/publication/attachments/2026_FR900Q_Instructions%20v1.0_Final.pdf) |
| UI late-payment interest | 1.5% monthly until paid | [DOES current portal](https://essp.does.dc.gov/DOES%20ESSP%20Employer%20Landing%20Page.html) |
| UI late report/payment penalty | Greater of 10% of amount due or $100 | [DOES current portal](https://essp.does.dc.gov/DOES%20ESSP%20Employer%20Landing%20Page.html) |

### Register and establish withholding

Complete online FR-500 on MyTax.DC.gov, selecting wage withholding. Use FEIN and the assigned withholding account number; a return/payment does not auto-register an account. Household employers also require FEIN and FR-900Q under the published instructions. A payroll service does not relieve the employer's filing/payment responsibility. [2026 FR-900Q pp.1-2](https://otr.cfo.dc.gov/sites/default/files/dc/sites/otr/publication/attachments/2026_FR900Q_Instructions%20v1.0_Final.pdf).

DC wages of nonresidents are not subject to DC individual income tax solely because of work in DC. A genuine nonresident uses D-4A documentation; resident allowance elections use D-4. The forms page marked D-4 and D-4A under review when read. Establish domicile/abode first, not just postal address; some purported commuters can be statutory residents. [OTR forms](https://otr.cfo.dc.gov/page/withholding-tax-forms); [Home Rule limitation](https://code.dccouncil.gov/us/dc/council/code/sections/1-206.02); `dc-income-tax`.

Calculate actual withholding only with a confirmed applicable wage table/method and employee elections. This research found historical FR-230 tables, but did not establish them as a usable current 2026 method. Do not apply an obsolete allowance amount, highest historical rate or annual-return tax formula as a substitute. Maintain the verified payroll-register withholding as an input for filing/reconciliation below; obtain the current method before calculating a new payroll run. This limitation is PR partial in README.

### UI coverage, base, rates and localization

Register an employer account in the DOES Employer Self Service Portal (ESSP), separately from OTR. Keep the returned employer number and rate notice; agents need the approved POA/assignment. Covered employment and UI localization are independent of employee income-tax residence. DOES says out-of-state wage credits require proper localization and supporting wage summaries; one-state adjustment limits and exception requests apply. Do not simply subtract all wages earned outside DC. [DOES portal](https://essp.does.dc.gov/DOES%20ESSP%20Employer%20Landing%20Page.html).

Taxable quarter wages per employee are the smaller of covered quarter wages and the positive amount remaining in the annual base. Report gross and excess wages too. DOES examples show that eligible already-taxed other-state wages can consume the base, but its current localization process controls the credit. Successor/predecessor and exempt employment require the actual determination. [Tax Rate Questions](https://does.dc.gov/service/tax-rate-questions); [current portal](https://essp.does.dc.gov/DOES%20ESSP%20Employer%20Landing%20Page.html).

The generic FAQ says a new employer gets the greater of 2.7% and the previous year's average, but the explicit 2026 announcement confirms 2.7% for that year. Table VI applies to experienced employers. Its statutory rows range from 1.9% for reserve at least 8% of average annual taxable payroll to 7.4% at reserve at or below minus 10%; use the actual assigned notice rather than choosing a favorable row. Add the separately applicable assessment. [§51-103 Table VI](https://code.dccouncil.gov/us/dc/council/code/sections/51-103); [2026 portal](https://essp.does.dc.gov/DOES%20ESSP%20Employer%20Landing%20Page.html).

Qualified nonprofits/government entities can elect reimbursement rather than percentage contributions, subject to their conditions and election period. Compare actual benefit charges and stability of employment; reimbursement is not an automatic exemption. [DOES rate FAQ](https://does.dc.gov/service/tax-rate-questions).

### File OTR withholding and reconcile payment

1. In MyTax Summary open Withholding Wage, Returns, then File Now for the quarter. Answer return-information questions and final/amended status. [OTR tutorial pp.2-4](https://mytax.dc.gov/WebFiles/Documents/Tut/Bus/Wth/How_to_File_a_Withholding_Wage_Tax_Return.pdf).
2. On FR-900Q line 1 enter actual DC wage/tip/compensation withholding by the displayed monthly or quarter fields; line 2 total quarter payments; line 3 computes balance. File a required zero return unless the account has properly closed. [2026 instructions p.2](https://otr.cfo.dc.gov/sites/default/files/dc/sites/otr/publication/attachments/2026_FR900Q_Instructions%20v1.0_Final.pdf).
3. Deposits and quarterly reporting are separate. Follow the account's assigned weekly/semiweekly/monthly/quarterly deposit cadence; the general 20th-day following month/quarter statement must not be read to delay an assigned more frequent deposit. FR-900Q filing is by the last day after the quarter. The official 2026 instructions name October 31 for Q3, correcting the generic FAQ's October 30. [2026 instructions p.2](https://otr.cfo.dc.gov/sites/default/files/dc/sites/otr/publication/attachments/2026_FR900Q_Instructions%20v1.0_Final.pdf).
4. Choose payment method; No Payment is Needed only for a genuine zero balance and Pay Later does not pay a return. For ACH use correct tax type, period and bank details. Sign electronically, save return acceptance/payment confirmation, and reconcile the account/bank. Correct an old return using another FR-900Q marked amended. [2026 instructions pp.1-2](https://otr.cfo.dc.gov/sites/default/files/dc/sites/otr/publication/attachments/2026_FR900Q_Instructions%20v1.0_Final.pdf); [tutorial pp.5-8](https://mytax.dc.gov/WebFiles/Documents/Tut/Bus/Wth/How_to_File_a_Withholding_Wage_Tax_Return.pdf).
5. Annual filer FR-900A and nonpayroll FR-900NP are different return categories; do not use FR-900A as annual reconciliation of quarterly returns. W-2 transmission must follow the actual current year-end specification, not the stale date on a general forms page. [OTR forms](https://otr.cfo.dc.gov/page/withholding-tax-forms).

### File UI wage and contribution reports

In ESSP select the employer and quarter, validate account/contact details, enter each worker's identity and covered gross/taxable/excess wages, and reconcile contributions plus the separate assessment to the assigned rate. File the wage/contribution report (UC-30 route) and make payment; retain both confirmations and bank evidence. Standard quarterly filing/payment dates are April 30, July 31, October 31 and January 31; annual household schedules differ and must follow the account notice. The current portal expressly names the 2026 Q3 date. [DOES portal](https://essp.does.dc.gov/DOES%20ESSP%20Employer%20Landing%20Page.html); [UI Employer Handbook, reporting sections](https://does.dc.gov/sites/default/files/dc/sites/does/publication/attachments/UI%20Tax%20Employer%20Handbook%20-%20January%202022.pdf).

OTR late filing/payment adds 5% per month up to 25%, with statutory overlap rules; interest is 10% annually compounded daily. These OTR rates are not DOES' 1.5%-monthly UI rate. For notices, match the agency, period and payment history. [2026 FR-900Q p.3](https://otr.cfo.dc.gov/sites/default/files/dc/sites/otr/publication/attachments/2026_FR900Q_Instructions%20v1.0_Final.pdf); [§47-4213](https://code.dccouncil.gov/us/dc/council/code/sections/47-4213).

## Boundary and exception table

| Situation | Treatment |
| --- | --- |
| DC resident works elsewhere | Assess resident withholding rules and other-state payroll separately |
| Nonresident works in DC | No DC individual wage tax solely from work; UI localization still considered |
| Employee exceeds annual UI base | Keep reporting wages; do not reset base each quarter |
| 2026 new vs experienced employer | Published new rate vs assigned Table VI rate, both distinct from assessment |
| Tax withheld but no payment | Filing does not settle trust-tax debt |
| Payroll service or agent | Employer remains responsible; DOES requires authorized account access |

## Worked cases

**Case 1:** A new covered employer has one employee paid $12,000 in the first quarter and no earlier wages. Taxable wages are $9,000; UI contribution $243 plus administrative assessment $18, total $261. The next $12,000 quarter is excess wages for this employee, so no new contribution base arises.

```oa-check
name: DC 2026 UI new employer annual cap
inputs:
  first: 12000
  second: 12000
  base: 9000
steps:
- taxable_first: min(first, base)
- ui: taxable_first * 0.027
- assessment: taxable_first * 0.002
- total: ui + assessment
- taxable_second: min(second, max(base - first, 0))
expected:
  taxable_first: 9000
  ui: 243
  assessment: 18
  total: 261
  taxable_second: 0
```
**Case 2:** A payroll register already computed and verified $1,800 wage withholding; $1,200 was deposited. FR-900Q balance is $600, not a new payroll tax calculation. Separately $5,000 covered wages at a confirmed new-employer 2.7% plus 0.2% assessment produce $145; an experienced notice assigning 4.4% plus 0.2% produces $230. The notice determines the route; there is no election to use the cheaper rate.

```oa-check
name: DC withholding reconciliation and UI rate branch
inputs:
  withheld: 1800
  paid: 1200
  covered: 5000
steps:
- balance: withheld - paid
- new_total: covered * (0.027 + 0.002)
- experienced_total: covered * (0.044 + 0.002)
expected:
  balance: 600
  new_total: 145
  experienced_total: 230
```

## When to refuse or refer

Refuse new-payroll withholding computation without the applicable current method/elections. Refer disputed residence, mobile localization, household/annual UI, reimbursement election, successorship, PEOs, classification, nonpayroll pension distributions, year-end specifications and notices. Paid family leave is an additional separate employer obligation requiring its own current source review.

## Filing and payment

Withholding and UI use different agencies/accounts and due dates. Reconcile each separately and keep submission/payment evidence. Resolve the withholding-rate partial before calculating a payroll run.

## Completion checklist

- Residence/elections and applicable payroll method established.
- OTR and DOES accounts and periods distinguished.
- UI gross/excess/remaining annual base and notice rate checked.
- Separate assessment included once.
- Required returns, deposits, year-end filings and payment confirmations reconciled.

## Sources

| Source and reading scope | URL | Read on |
| --- | --- | --- |
| 2026 FR-900Q instructions. Read for all three pages: registration, filing/deposit periods, specific fields, amendments and penalties. | https://otr.cfo.dc.gov/sites/default/files/dc/sites/otr/publication/attachments/2026_FR900Q_Instructions%20v1.0_Final.pdf | 2026-11-13 |
| OTR withholding forms. Read for 2026 annual/quarterly routes, D-4/D-4A review status and dated year-end links. | https://otr.cfo.dc.gov/page/withholding-tax-forms | 2026-11-13 |
| OTR wage-withholding tutorial. Read for pp.2-8 account, return, line 1/2, payment, signature and confirmation. | https://mytax.dc.gov/WebFiles/Documents/Tut/Bus/Wth/How_to_File_a_Withholding_Wage_Tax_Return.pdf | 2026-11-13 |
| DOES 2026 employer portal announcement. Read for 2026 rates/base/assessment/Table VI, notices, localization and penalties. | https://essp.does.dc.gov/DOES%20ESSP%20Employer%20Landing%20Page.html | 2026-11-13 |
| D.C. Code §51-103. Read for Table VI reserve bands and contribution method. | https://code.dccouncil.gov/us/dc/council/code/sections/51-103 | 2026-11-13 |
| DOES Tax Rate Questions. Read for new/experienced rates, annual wage base examples, other-state wages and reimbursement. | https://does.dc.gov/service/tax-rate-questions | 2026-11-13 |
| DOES UI Tax for Employers. Read for registration, employer reports, account and authority resources. | https://does.dc.gov/page/ui-tax-employers | 2026-11-13 |
| UI Employer Handbook, January 2022. Read for registration and reporting sections only; current 2026 figures come from the explicit 2026 portal announcement. | https://does.dc.gov/sites/default/files/dc/sites/does/publication/attachments/UI%20Tax%20Employer%20Handbook%20-%20January%202022.pdf | 2026-11-13 |

Not yet confirmed: current 2026 wage withholding computation tables/allowance method, final D-4/D-4A and W-2 specifications, exact assigned frequent-deposit/annual-household calendar and specialist coverage/election rules; paid-family-leave contribution. No historical FR-230 figures are promoted as 2026 values.
