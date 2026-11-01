---
name: td-payroll-social
description: "Prepare Chad payroll and social contribution working papers for 2026, separating CNPS from employer payroll and training taxes and referring salary IRPP to its own Guide. Covers employer and worker registration, contributable pay, genuine reimbursements, ordinary full-month floor and ceiling, employer and employee shares, headcount-based declaration periods, payment timing, daily late charges and annual ceiling reconciliation. Use for Chad CNPS, first employee, payroll tax, training levy, capped salary contributions or monthly versus quarterly remittance. Two cases recompute charges and the ceiling. The authority’s archived contribution guidance, later-law checks, special employment cases and live filing-screen limitations remain explicit; SC and PR remain partial."
jurisdiction: TD
tax_year: 2026
last_updated: 2026-11-01
review_status: pending_review
trust_label: Built by Michael Cutajar and the OpenAccountants team
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
category: payroll
version: 1.2
---

# Chad payroll and social contributions v1.2

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

## Who this applies to

Employers hiring their first employee in Chad, including occasional/probationary employees and domestic-only employers. Register the employer and workers with CNPS, retain an existing worker's permanent number and record starts/departures; notify employer cessation immediately. [CNPS employer Guide pp4–6](https://web.archive.org/web/20240717045908id_/https://cnps-tchad.com/wp-content/uploads/2021/06/GUIDE-DE-LEMPLOYEUR.pdf); [insured Guide p6](https://web.archive.org/web/20240717015622id_/https://cnps-tchad.com/wp-content/uploads/2021/06/GUIDE-DE-LASURE-SOCIAL.pdf).

This2026 preparation method separates CNPS contributions, employer payroll/training taxes and salary IRPP. The CNPS contribution source is the archived authority employer Guide, still linked from the authority's [23February2026 captured employer page](https://web.archive.org/web/20260223113650id_/https://cnps-tchad.com/download/guide-employeur/). Its cover is2019/edition2018; a later decree, new minimum wage or special social agreement has not been comprehensively excluded. Confirm those issues before a live payroll, particularly partial months/multiple employers. Salary IRPP is owned by the [income Guide](td-income-tax.md); its annual scale is not a substitute for the administration's monthly payroll table.

## Rates, bands and thresholds

Amounts are FCFA/XAF. Ordinary full-month CNPS schedule below comes from the authority's actual contribution guidance; do not extend it to unresolved special cases.

| Item/condition | Figure | Primary source |
|---|---|---|
| CNPS full-month contribution floor in authority Guide |59,995SMIG rounded to60,000 for computation | [Employer Guide pp7–9](https://web.archive.org/web/20240717045908id_/https://cnps-tchad.com/wp-content/uploads/2021/06/GUIDE-DE-LEMPLOYEUR.pdf) |
| CNPS ceiling |500,000monthly;6,000,000annual | [Employer Guide p9](https://web.archive.org/web/20240717045908id_/https://cnps-tchad.com/wp-content/uploads/2021/06/GUIDE-DE-LEMPLOYEUR.pdf) |
| CNPS employer share of capped/floored contributable pay |16.5%:7.5% family/maternity,4% occupational risk,5% pension | [Employer Guide p8](https://web.archive.org/web/20240717045908id_/https://cnps-tchad.com/wp-content/uploads/2021/06/GUIDE-DE-LEMPLOYEUR.pdf) |
| CNPS employee pension share |3.5% of same base | [Employer Guide p8](https://web.archive.org/web/20240717045908id_/https://cnps-tchad.com/wp-content/uploads/2021/06/GUIDE-DE-LEMPLOYEUR.pdf) |
| Derived monthly maximum shares |82,500employer;17,500employee | [Employer Guide pp8–9](https://web.archive.org/web/20240717045908id_/https://cnps-tchad.com/wp-content/uploads/2021/06/GUIDE-DE-LEMPLOYEUR.pdf) |
| Employer taxe forfaitaire, unless article188 exempt |7.5% of statutory gross remuneration/actual benefits | [CGI187–190](https://web.archive.org/web/20250720004455id_/https://www.finances.gouv.td/index.php/le-ministere/le-ministre/item/download/438_afa372566d4acca63cb857e846d67eef) |
| Training/apprenticeship tax, where articles172–174 apply |12per thousand,1.2%, of statutory gross remuneration | [CGI171–178](https://web.archive.org/web/20250720004455id_/https://www.finances.gouv.td/index.php/le-ministere/le-ministre/item/download/438_afa372566d4acca63cb857e846d67eef) |
| CNPS late charge |One per thousand per day on overdue contributions | [Employer Guide p11](https://web.archive.org/web/20240717045908id_/https://cnps-tchad.com/wp-content/uploads/2021/06/GUIDE-DE-LEMPLOYEUR.pdf) |

## The base

1. Reconcile each worker's paid-month remuneration: salary, gains, indemnities, bonuses, back pay and benefits, irrespective of period earned. Exclude genuine reimbursements, rather than every item called an allowance. The CNPS and IRPP exemption bases are different. [Employer Guide pp7–8](https://web.archive.org/web/20240717045908id_/https://cnps-tchad.com/wp-content/uploads/2021/06/GUIDE-DE-LEMPLOYEUR.pdf).
2. For an ordinary full month under the cited schedule, cap/floor contributable pay: `min(max(contributable_pay,60000),500000)`. Compute employer16.5% and employee3.5%; employer withholds the employee share and remits both. Keep uncapped pay for the distinct employer-tax calculations. Do not infer partial-month proration or multiple-employer allocation from this formula. [Employer Guide pp8–9](https://web.archive.org/web/20240717045908id_/https://cnps-tchad.com/wp-content/uploads/2021/06/GUIDE-DE-LEMPLOYEUR.pdf).
3. At year end reconcile paid remuneration and contributions to the6million annual ceiling and annual salary recap, subtracting amounts already declared. Resolve partial-year and multiple-employer cases before an adjustment. A monthly cap is not a licence to omit the annual reconciliation. [Employer Guide p12](https://web.archive.org/web/20240717045908id_/https://cnps-tchad.com/wp-content/uploads/2021/06/GUIDE-DE-LEMPLOYEUR.pdf).
4. First test CGI31: a qualifying natural-person IGL substitutes the listed own employer/training taxes, while third-party withholding remains. Do not charge those substituted taxes merely because a person hires workers. Outside that regime, compute taxe forfaitaire separately on CGI189's gross amounts actually paid in the civil year, including actual-value benefits. Article188 exempts the listed state/communal, diplomatic, international, specified subsidy-funded and domestic-household cases, with express exclusions for financially autonomous public bodies/state-participated companies. Its real-regime recruitment exemption covers the specified young graduates/disability/under35workers on their qualifying wage share. Establish the employer and employee facts before excluding a salary. Apply7.5% only to the remaining base. [CGI187–190](https://web.archive.org/web/20250720004455id_/https://www.finances.gouv.td/index.php/le-ministere/le-ministre/item/download/438_afa372566d4acca63cb857e846d67eef).
5. Training tax applies to articles16,17,49,130 businesses, includes gross pay/benefits/regular bonuses and directly paid temporary labour. Article174 exempts a base not exceeding100,000, qualifying exclusively educational companies and the specified real-regime recruitment wage share. Article177 disregards the stated residual fraction of pay up to1,000 and rounds tax to the nearest ten francs; resolve boundary interpretation before processing a non-round amount. Apply12per thousand to the supported base. [CGI171–178](https://web.archive.org/web/20250720004455id_/https://www.finances.gouv.td/index.php/le-ministere/le-ministre/item/download/438_afa372566d4acca63cb857e846d67eef).
6. Do not use the former training-investment exemption committee procedure: LF2026 arts22–28 delete CGI180–186. That deletion does not itself delete article174's separate exemptions. [LF22–28](https://ecofinances.gouv.td/wp-content/uploads/2026/06/Loi-n008-AN-SENAT-2025-Portant-loi-de-Finances-2026-LF-2026.pdf#page=32).
7. Build salary IRPP using the income Guide's base and the administration's actual monthly scale. Reconcile gross pay, employee CNPS, IRPP, other authorised deductions, net pay, employer charges and payment liabilities. No complete net-pay result is produced until the applicable IRPP scale and all deductions are supported. [CGI847–849](https://web.archive.org/web/20250720004455id_/https://www.finances.gouv.td/index.php/le-ministere/le-ministre/item/download/438_afa372566d4acca63cb857e846d67eef).

## Deadlines and filing

CNPS: headcount at least20 means monthly; fewer than20 means quarterly. Return the completed period declaration with payment evidence and pay by the20th of the month following the applicable period; thus an ordinary first quarter is due20April. Save the accepted declaration and receipt, then complete annual salary recap/reconciliation at year end. Missing declarations can lead to CNPS office assessment. These are the archived authority instructions, not proof of a functioning current portal screen. [Employer Guide pp10–12](https://web.archive.org/web/20240717045908id_/https://cnps-tchad.com/wp-content/uploads/2021/06/GUIDE-DE-LEMPLOYEUR.pdf).

DGI payroll withholding and employer taxe forfaitaire follow the15th of the next month under CGI846–849; training collection follows176/846. Article849 requires e-Tax-generated declaration and notified date/unique number/logo copy. Employers also provide the January named annual salary statement under986–987. Save the working paper, declaration, payment, receipt and annual reconciliation. Current CNPS portal forms, DGI monthly payroll scale, exact field identifiers and payment references remain unacquired. [CGI176,846–850,986–987](https://web.archive.org/web/20250720004455id_/https://www.finances.gouv.td/index.php/le-ministere/le-ministre/item/download/438_afa372566d4acca63cb857e846d67eef); [LF37](https://ecofinances.gouv.td/wp-content/uploads/2026/06/Loi-n008-AN-SENAT-2025-Portant-loi-de-Finances-2026-LF-2026.pdf#page=56).

## Penalties and interest

For the authority's ordinary CNPS late charge, multiply unpaid contribution by actual days late and0.001; it is simple daily charging. The Guide also describes formal recovery/office assessment, so do not assume paying that charge resolves all employer breaches. [Employer Guide pp10–12](https://web.archive.org/web/20240717045908id_/https://cnps-tchad.com/wp-content/uploads/2021/06/GUIDE-DE-LEMPLOYEUR.pdf).

IRPP withheld but not remitted by article848's deadline attracts CGI1042's1.5% per month or part capped50%, with prosecution preserved. Missing employer declarations and other tax defaults have separate CGI1061/1041/1044 rules; classify the notice and base before combining amounts. [CGI1041–1044,1061](https://web.archive.org/web/20250720004455id_/https://www.finances.gouv.td/index.php/le-ministere/le-ministre/item/download/438_afa372566d4acca63cb857e846d67eef).

## Cross-border points

Foreign employees' nationality alone does not remove CNPS coverage under the authority Guide. Expatriate/social-agreement exclusions, detachment certificates, multiple foreign employers and coordination of contributions need their actual instrument. Do not infer a foreign exemption from a tax treaty or passport. Salary source/residence and foreign-paid compensation are handled in the income Guide. [CNPS insured Guide p6](https://web.archive.org/web/20240717015622id_/https://cnps-tchad.com/wp-content/uploads/2021/06/GUIDE-DE-LASURE-SOCIAL.pdf); [CGI44,994](https://web.archive.org/web/20250720004455id_/https://www.finances.gouv.td/index.php/le-ministere/le-ministre/item/download/438_afa372566d4acca63cb857e846d67eef).

## Two worked examples that recompute

### Ordinary full-month employer cost

Full-month contributable and employer-tax gross pay is200,000, all supported; the employer is outside IGL and has no exemption, benefit, rounding issue or other employer charge. Employer CNPS33,000, employee7,000; remit40,000. Taxe forfaitaire is15,000 and training2,400. Employer cost before other charges is250,400. Employee IRPP/net pay is not guessed.

```oa-check
name: Ordinary CNPS and separate employer taxes
inputs:
  gross: 200000
steps:
  cnps_base: min(max(gross, 60000), 500000)
  employer_cnps: cnps_base * 0.165
  employee_cnps: cnps_base * 0.035
  remit_cnps: employer_cnps + employee_cnps
  forfaitaire: gross * 0.075
  training: gross * 0.012
  employer_cost: gross + employer_cnps + forfaitaire + training
expected:
  remit_cnps: 40000
  employer_cost: 250400
```

### Cap, period decision and actual delay

Full-month contributable pay800,000 produces base500,000 and employer/employee shares82,500/17,500, remittance100,000. Ten verified days late adds1,000. A9employee employer remits on the quarterly schedule; a20employee employer uses monthly. That scheduling decision depends on headcount, not salary. The uncapped160,000 comparison would overstate this month's contribution by60,000, before annual reconciliation.

```oa-check
name: Capped contribution and simple daily late charge
inputs:
  gross: 800000
  days_late: 10
steps:
  base: min(max(gross, 60000), 500000)
  employer: base * 0.165
  employee: base * 0.035
  remittance: employer + employee
  late_charge: remittance * days_late * 0.001
  due: remittance + late_charge
  uncapped_overstatement: gross * 0.20 - remittance
expected:
  employer: 82500
  employee: 17500
  late_charge: 1000
  due: 101000
  uncapped_overstatement: 60000
```

## Ask the client first

- Which employer/workers are registered, with what permanent numbers, starts and departures?
- What paid remuneration, benefits, genuine reimbursements and full/partial months apply?
- What actual headcount, other employers, annual contributions and special agreements affect period or ceiling?
- Which employer-tax and recruitment exemptions have supporting status/documents?
- What declarations, payments, receipts, notices and confirmed actual delay dates exist?

## Sources

| Primary source | Read on | Actual scope |
|---|---|---|
| [CNPS employer Guide, archive2024-07-17](https://web.archive.org/web/20240717045908id_/https://cnps-tchad.com/wp-content/uploads/2021/06/GUIDE-DE-LEMPLOYEUR.pdf) |2026-11-01| Source researcher read all23PDFpages; contribution base/rates pp7–9, periods/payment/late charge/annual recap pp10–12; p11 visually checked |
| [CNPS employer download page, archive2026-02-23](https://web.archive.org/web/20260223113650id_/https://cnps-tchad.com/download/guide-employeur/) |2026-11-01| Actual archived HTML links the same employer PDF, whose cover is2019/edition2018; not a newly promulgated2026schedule |
| [CNPS insured Guide, archive2024-07-17](https://web.archive.org/web/20240717015622id_/https://cnps-tchad.com/wp-content/uploads/2021/06/GUIDE-DE-LASURE-SOCIAL.pdf) |2026-11-01| Source researcher read24pages, contributions/coverage pp6–8 and p7 scan |
| [Official CGI2025, ministry archive2025-07-20](https://web.archive.org/web/20250720004455id_/https://www.finances.gouv.td/index.php/le-ministere/le-ministre/item/download/438_afa372566d4acca63cb857e846d67eef) |2026-11-01| Arts31/37,171–190,846–850,986–987,1041–1044,1061 and neighbouring exemption/collection clauses |
| [Enacted LF2026](https://ecofinances.gouv.td/wp-content/uploads/2026/06/Loi-n008-AN-SENAT-2025-Portant-loi-de-Finances-2026-LF-2026.pdf) |2026-11-01| Arts22–28 deleting180–186, plus37 electronic declarations; read old/new clauses pp32–34,56–57 |

Not yet confirmed: later SMIG/rate instruments beyond the2026archived CNPS link, partial-month/multiple-employer/expat rules, annual recap exact filing date, transport allowances without reimbursement character, live CNPS/DGI forms and payment screens, monthly IRPP table and article177 residual-base boundaries. These keep SC/PR partial. For independent AI source review and its limits, see the [country README](README.md). No accountant attestation.

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
