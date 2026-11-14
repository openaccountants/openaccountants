---
name: nm-payroll
description: "New Mexico 2026 wage withholding percentage tables, W-4 setup, TRD-41414 and new TRD-41431 quarterly wage reports; UI registration and rates are explicitly unconfirmed because official workforce sources refused access."
license: "AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)"
metadata:
  source: openaccountants
  openaccountants_url: "https://www.openaccountants.com/skills/nm-payroll"
  jurisdiction: "US-NM"
  tax_year: "2026"
  last_updated: "2026-11-13"
---

# New Mexico payroll withholding and unemployment routing, tax year 2026

> **General reference only.** Built from the official sources identified below. Written by Codex. Not reviewed by an accountant. Obtain qualified professional review before filing, paying or taking a tax position.

> **Circular 230 section 10.37:** Apply this material to the taxpayer's actual facts and the law for the relevant period, evaluate reasonable assumptions and relevant circumstances, and obtain professional review of any federal tax implications. Federal computations belong to the linked federal skills.

**Answer first.** Use New Mexico's **2026 FYI-104** wage tables and employee filing status for state withholding. From the quarter beginning 1 January 2026, employers also submit **TRD-41431**, a quarterly wage/withholding report due the twenty-fifth of the following month, in addition to **TRD-41414** used to report/pay wage withholding. UI is a separate employer obligation, but this skill cannot yet supply verified UI rates/base or filing instructions because the official workforce pages could not be opened. Sources: [FYI-104 effective January 1, 2026](https://realfile.tax.newmexico.gov/FYI-104.pdf); [TRD-41414 instructions revised July 1, 2026](https://realfile.tax.newmexico.gov/trd-41414ins.pdf).

## Scope

New Mexico employers paying wages subject to state withholding, including resident wages and nonresident NM services under the stated rules. This skill covers 2026 withholding computation and the new employee report. The pack's UI portion is **partial**, with specific source-access gaps below; do not treat this as completed UI computation. Federal taxes belong to `us-form-941-940-payroll`, final individual income tax to `nm-income-tax`.

Non-wage withholding uses **TRD-41409** rather than wage TRD-41414. Workers' compensation fees are associated with TRD-41431 but their amounts and liability conditions require separate confirmation. No federal payroll figures are repeated.

## Ask the client first

1. Legal employer, NMBTIN, first payroll date, employee/contractor classification and assigned return periods.
2. Residence, actual work locations/days, tribal/military facts and evidence of any state exemption.
3. Wage amount, pay frequency, filing status on W-4 and state-specific additional withholding request.
4. Bonuses/supplemental payments, multiple jobs and whether federal adjustments should differ for NM purposes.
5. Employee names/IDs and wages/withholding by quarter for the new 2026 report.
6. Workforce UI account, official 2026 rate notice/base, wage records, prior contributions and any acquisition or multi-state history.

## The method, step by step

### Rates, bands and thresholds

| Item | 2026 amount or requirement | Official source |
|---|---|---|
| Wage percentage tables | Actual payroll-period tables, differentiated single/married/head of household; rates run 1.5% to 5.9% on the relevant band | [FYI-104 tables, wages from January 1, 2026](https://realfile.tax.newmexico.gov/FYI-104.pdf) |
| De minimis withholding | No withholding required when total for an employee in one month is less than USD 1 | [Amount to Withhold](https://realfile.tax.newmexico.gov/FYI-104.pdf) |
| Nonresident short work exception | Withholding not required for nonresident NM work of 15 or fewer days in calendar year under publication's stated rule; final income-tax liability is separate | [Who Must Withhold, note 2](https://realfile.tax.newmexico.gov/FYI-104.pdf) |
| Wage return/payment due | Twenty-fifth day of month after assigned period, with nonbusiness-day rules | [Filing Frequency and Due Date](https://realfile.tax.newmexico.gov/trd-41414ins.pdf) |
| New 2026 quarterly employee report | TRD-41431 due twenty-fifth day of month following each calendar quarter; electronic filing required | [Required Quarterly Withholding Report](https://realfile.tax.newmexico.gov/FYI-104.pdf) |
| Annual withholding statements | Electronic state submission by last day of January following year | [Annual Withholding Statements](https://realfile.tax.newmexico.gov/FYI-104.pdf) |

The following **weekly** table is reproduced from the official 2026 source. It is not the final personal income-tax schedule. Other pay frequencies require their corresponding official FYI-104 table; do not divide a weekly result by an arbitrary factor.

| Weekly single wages (USD) | Withholding formula (USD) | Official source |
|---|---|---|
| Not over 155 | 0 | [FYI-104 Table 1](https://realfile.tax.newmexico.gov/FYI-104.pdf) |
| Over 155 through 261 | 1.5% of excess over 155 | [FYI-104 Table 1](https://realfile.tax.newmexico.gov/FYI-104.pdf) |
| Over 261 through 395 | 1.59 + 3.2% of excess over 261 | [FYI-104 Table 1](https://realfile.tax.newmexico.gov/FYI-104.pdf) |
| Over 395 through 472 | 5.89 + 3.2% of excess over 395 | [FYI-104 Table 1](https://realfile.tax.newmexico.gov/FYI-104.pdf) |
| Over 472 through 645 | 8.36 + 4.3% of excess over 472 | [FYI-104 Table 1](https://realfile.tax.newmexico.gov/FYI-104.pdf) |
| Over 645 through 799 | 15.80 + 4.3% of excess over 645 | [FYI-104 Table 1](https://realfile.tax.newmexico.gov/FYI-104.pdf) |
| Over 799 through 1,126 | 22.41 + 4.7% of excess over 799 | [FYI-104 Table 1](https://realfile.tax.newmexico.gov/FYI-104.pdf) |
| Over 1,126 through 1,434 | 37.78 + 4.7% of excess over 1,126 | [FYI-104 Table 1](https://realfile.tax.newmexico.gov/FYI-104.pdf) |
| Over 1,434 through 4,193 | 52.24 + 4.9% of excess over 1,434 | [FYI-104 Table 1](https://realfile.tax.newmexico.gov/FYI-104.pdf) |
| Over 4,193 | 187.46 + 5.9% of excess over 4,193 | [FYI-104 Table 1](https://realfile.tax.newmexico.gov/FYI-104.pdf) |

| Weekly married wages (USD) | Withholding formula (USD) | Official source |
|---|---|---|
| Not over 310 | 0 | [FYI-104 Table 1](https://realfile.tax.newmexico.gov/FYI-104.pdf) |
| Over 310 through 463 | 1.5% of excess over 310 | [FYI-104 Table 1](https://realfile.tax.newmexico.gov/FYI-104.pdf) |
| Over 463 through 617 | 2.31 + 3.2% of excess over 463 | [FYI-104 Table 1](https://realfile.tax.newmexico.gov/FYI-104.pdf) |
| Over 617 through 790 | 7.23 + 3.2% of excess over 617 | [FYI-104 Table 1](https://realfile.tax.newmexico.gov/FYI-104.pdf) |
| Over 790 through 1,098 | 12.77 + 4.3% of excess over 790 | [FYI-104 Table 1](https://realfile.tax.newmexico.gov/FYI-104.pdf) |
| Over 1,098 through 1,271 | 26.00 + 4.3% of excess over 1,098 | [FYI-104 Table 1](https://realfile.tax.newmexico.gov/FYI-104.pdf) |
| Over 1,271 through 1,963 | 33.44 + 4.7% of excess over 1,271 | [FYI-104 Table 1](https://realfile.tax.newmexico.gov/FYI-104.pdf) |
| Over 1,963 through 2,233 | 65.98 + 4.7% of excess over 1,963 | [FYI-104 Table 1](https://realfile.tax.newmexico.gov/FYI-104.pdf) |
| Over 2,233 through 6,367 | 78.63 + 4.9% of excess over 2,233 | [FYI-104 Table 1](https://realfile.tax.newmexico.gov/FYI-104.pdf) |
| Over 6,367 | 281.23 + 5.9% of excess over 6,367 | [FYI-104 Table 1](https://realfile.tax.newmexico.gov/FYI-104.pdf) |

| Weekly head of household wages (USD) | Withholding formula (USD) | Official source |
|---|---|---|
| Not over 232 | 0 | [FYI-104 Table 1](https://realfile.tax.newmexico.gov/FYI-104.pdf) |
| Over 232 through 386 | 1.5% of excess over 232 | [FYI-104 Table 1](https://realfile.tax.newmexico.gov/FYI-104.pdf) |
| Over 386 through 540 | 2.31 + 3.2% of excess over 386 | [FYI-104 Table 1](https://realfile.tax.newmexico.gov/FYI-104.pdf) |
| Over 540 through 713 | 7.23 + 3.2% of excess over 540 | [FYI-104 Table 1](https://realfile.tax.newmexico.gov/FYI-104.pdf) |
| Over 713 through 1,021 | 12.77 + 4.3% of excess over 713 | [FYI-104 Table 1](https://realfile.tax.newmexico.gov/FYI-104.pdf) |
| Over 1,021 through 1,194 | 26.00 + 4.3% of excess over 1,021 | [FYI-104 Table 1](https://realfile.tax.newmexico.gov/FYI-104.pdf) |
| Over 1,194 through 1,886 | 33.44 + 4.7% of excess over 1,194 | [FYI-104 Table 1](https://realfile.tax.newmexico.gov/FYI-104.pdf) |
| Over 1,886 through 2,155 | 65.98 + 4.7% of excess over 1,886 | [FYI-104 Table 1](https://realfile.tax.newmexico.gov/FYI-104.pdf) |
| Over 2,155 through 6,290 | 78.63 + 4.9% of excess over 2,155 | [FYI-104 Table 1](https://realfile.tax.newmexico.gov/FYI-104.pdf) |
| Over 6,290 | 281.23 + 5.9% of excess over 6,290 | [FYI-104 Table 1](https://realfile.tax.newmexico.gov/FYI-104.pdf) |

1. Register the employer withholding account through **TAP**, https://tap.state.nm.us, and retain **NMBTIN**. Business-registration updates/closure use **ACD-31015**; obligations do not automatically stop when wages cease. Source: [How to Report and Pay Withholding Taxes](https://realfile.tax.newmexico.gov/FYI-104.pdf).
2. NM has no separate mandatory state equivalent of W-4. A duplicate federal W-4 marked **For New Mexico State Withholding Only** is a permitted convenience; retain it and distinguish state extra withholding from federal adjustments. Exempt income needs actual statutory eligibility rather than a generic no-withholding request. Source: [General Information](https://realfile.tax.newmexico.gov/FYI-104.pdf).
3. Determine covered wages. The publication requires NM resident withholding on wages regardless of work location, and nonresident withholding on NM-service wages, subject to its limited exceptions. A nonresident short-work exception does not prove the wages are exempt from final state income tax. Source: [Who Must Withhold and Amount to Withhold](https://realfile.tax.newmexico.gov/FYI-104.pdf).
4. Select the actual pay-period and filing-status table in FYI-104. Locate the wage band, compute fixed amount plus marginal rate times excess wages, and add the employee's valid NM additional amount. These tables do not use old withholding allowances. Use the official supplemental/irregular-pay directions rather than assuming the ordinary periodic table always applies. Source: [How to use tables, supplemental wages and Tables 1 to 8](https://realfile.tax.newmexico.gov/FYI-104.pdf).
5. Separate wage tax withheld from other deductions. Reconcile employee wages/withholding to the TRD-41414 return, TRD-41431 quarterly details and annual wage statements. Filing a workforce/UI report does not satisfy TRD reporting. Source: [How to Report and Pay and Required Quarterly Withholding Report](https://realfile.tax.newmexico.gov/FYI-104.pdf).
6. **UI verification handoff:** obtain the employer's official 2026 UI rate notice, statutory wage base and workforce account/filing instructions before computing or submitting contributions. Retain year-to-date covered wages and predecessors/multi-state facts so the verified base can later be applied employee by employee. The blocked workforce pages listed in Sources are not treated as read; search-result numbers are not usable instructions.

## Boundary and exception table

| Situation | Treatment |
|---|---|
| Resident works out of state | Publication's resident-wage withholding rule applies, subject to specific exclusions and credit review |
| Nonresident works in NM 15 days or fewer | Test the limited withholding exception; do not infer final income-tax exemption |
| Tribal or military exempt income | Establish actual exemption and W-4 documentation; refer conflicting facts |
| Self-employed owner draw | Do not report it as employee wage withholding; individual estimates use PIT-ES |
| Supplemental wages | Follow FYI-104 supplemental-pay/Table 8 method |
| Pensions, annuities or gambling | Separate non-wage return TRD-41409, not TRD-41414 |
| No tax withheld in required period | File zero return under FYI-104 until properly closed |
| UI rates/base or reporting unsupported | Stop UI computation, obtain actual official evidence; the pack remains partial |

## Worked cases

**Case 1, additional-withholding decision.** Invented married employee receives USD 1,000 weekly wages. Official Table 1(b) uses USD 12.77 plus 4.3% over USD 790: USD 21.80. With a valid request for USD 20 additional NM withholding, deduct USD 41.80 instead. The extra USD 20 affects prepayment only, not the employee's final tax rate.

```oa-check
name: New Mexico 2026 weekly married with extra withholding
inputs:
  wages: 1000
  extra: 20
steps:
  - ordinary: 12.77 + (wages - 790) * 0.043
  - elected: ordinary + extra
  - difference: elected - ordinary
expected:
  ordinary: 21.8
  elected: 41.8
  difference: 20
```

**Case 2: correct filing-status column.** Invented single and head-of-household employees each receive USD 1,000 weekly and request no extra withholding. Single Table 1(a): USD 22.41 + 4.7% x (1,000 - 799) = USD 31.857, or USD 31.86. HOH Table 1(c): USD 12.77 + 4.3% x (1,000 - 713) = USD 25.111, or USD 25.11. Using the single column for HOH would overwithhold about USD 6.75 weekly.

```oa-check
name: New Mexico 2026 weekly single and head of household comparison
inputs:
  wages: 1000
steps:
  - single_tax: 22.41 + (wages - 799) * 0.047
  - hoh_tax: 12.77 + (wages - 713) * 0.043
  - difference: single_tax - hoh_tax
expected:
  single_tax: 31.857
  hoh_tax: 25.111
  difference: 6.746
```

## When to refuse or refer

Refer UI source/rate/base gaps before any UI filing, multi-state localization, successor accounts, classification, special-exempt wages and disputed military/tribal residency. Workers' compensation fee liability/amounts require verification rather than assuming that completing the wage-report part settles the fee. No UI numeric example is invented to conceal the missing evidence.

## Filing and payment

**Wage tax:** In TAP select withholding, assigned period and **TRD-41414**; enter wages/withholding and applicable credits, reconcile payments/balance, submit, retain acceptance and separately retain electronic payment confirmation. Use the registration certificate's monthly, quarterly or semiannual frequency. Return and payment are due by the twenty-fifth after period end, shifted under the applicable nonbusiness-day rule. This program has an electronic filing mandate; request a permitted waiver/exception if necessary. Source: [2026 TRD-41414 instructions](https://realfile.tax.newmexico.gov/trd-41414ins.pdf).

**New quarterly employee report:** From Q1 2026, file electronic **TRD-41431, Workers Compensation Fee Return and Employees Quarterly Wage and Withholding Report**, with employee gross wages and NM tax withheld. It is due 25 April, 25 July, 25 October and 25 January after the quarter, adjusted for applicable nonbusiness days. It is an additional report, not a replacement for TRD-41414 payment/return. Source: [Required Quarterly Withholding Report and HB218 change](https://realfile.tax.newmexico.gov/FYI-104.pdf).

**Annual statements:** Electronically submit state annual withholding statements by the last day of January after year end through the permitted federal/state program or TAP as applicable. FYI-104 says **RPD-41072** annual summary is optional, not mandatory. Retain annual reconciliation regardless. Source: [Annual Withholding Statements and Annual Reconciliation](https://realfile.tax.newmexico.gov/FYI-104.pdf).

**UI:** Verify the current workforce registration portal, account, contribution/wage-return form and deadlines from actual official evidence before filing. TRD returns do not replace workforce filings. The source-access gap remains explicitly open.

Late wage returns/payments follow the 2026 TRD-41414 penalty/interest instructions; determine the applicable failure and actual variable rate rather than inventing an annual interest amount. Source: [Interest and Penalties](https://realfile.tax.newmexico.gov/trd-41414ins.pdf).

## Completion checklist

- Wage coverage, filing status, pay period and state additional request documented.
- Actual 2026 percentage table used, with de minimis/special cases checked.
- TRD-41414, new TRD-41431 and annual statement obligations reconciled separately.
- UI account/rate/base/filing evidence obtained before UI calculation; no false full-coverage claim.

## Sources

| Source and scope actually read | URL | Read on |
|---|---|---|
| FYI-104 revised November 2025, effective January 1, 2026. Read general information, coverage, W-4, computation example, all three weekly table columns, other frequency/supplemental table headings, new quarterly report and annual statement/reconciliation instructions. | https://realfile.tax.newmexico.gov/FYI-104.pdf | 2026-11-13 |
| TRD-41414 instructions revised July 1, 2026. Read coverage, de minimis rule, filing frequency, due dates, electronic filing, TAP workflow and interest/penalty sections. | https://realfile.tax.newmexico.gov/trd-41414ins.pdf | 2026-11-13 |

Not yet confirmed: **UI wage base, new-employer/industry and experienced rates, registration, quarterly wage/contribution return form/deadlines and penalty/interest for 2026**. Official workforce sources https://www.dws.state.nm.us/UI-Tax-Information and https://www.dws.nm.gov/Unemployment/Unemployment-for-a-Business/Unemployment-Insurance-Tax-Information/How-UI-Tax-Rates-Are-Calculated could not be opened: legacy-host DNS failure, current-host HTTP 403/Request Rejected; ordinary browser attempt failed and archive lookup returned HTTP 429. No page is dated as read and indexed-only figures are excluded. Also unconfirmed: final TRD-41431 field/line instructions and workers-compensation fee amounts/eligibility; employer-specific military/tribal exceptions and actual variable interest rate. The withholding portion is sourced, the UI portion remains partial.

## Today's figures and who stands behind this skill

This file is an AI skill (tax rules your AI follows) from OpenAccountants, copied on 2026-11-13. Rates, thresholds and deadlines change. For the current version of this skill, its official sources and the named accountant (if any) who stands behind it, call `get_skill` with slug `nm-payroll` on the OpenAccountants connector (https://www.openaccountants.com/connect), or read https://www.openaccountants.com/skills/nm-payroll. If neither is available, confirm every figure against the official source pages cited above before relying on it.
