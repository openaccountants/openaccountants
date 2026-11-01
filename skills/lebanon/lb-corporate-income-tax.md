---
name: lb-corporate-income-tax
description: "Use this Guide for Lebanon corporate income tax, SAL and SARL profit tax, dividends and import-advance questions for 2026. It supplies the ordinary capital-company rate, distinguishes profit from distribution tax and identifies the real-profit base and customs-credit reconciliation. The two cases recompute an ordinary SAL distribution and a cash-retention comparison. It does not calculate special holding or offshore taxes, non-resident withholding, Sayrafa liability, deemed-profit coefficients or temporary revaluation relief. Current forms, extensions, suspension effects and penalty calculations are named non-operative holds. Read the conditions and obtain the missing evidence before preparing a filing or choosing a special regime."
version: 1.2
jurisdiction: LB
tax_year: 2026
last_updated: 2026-11-01
review_status: pending_review
trust_label: Built by Michael Cutajar and the OpenAccountants team
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
category: international
---

# Lebanon Corporate Income Tax

> **General reference only.** This Guide is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in Lebanon.

## Who this applies to

Lebanese SAL/SARL companies, foreign branches and other businesses with profits in Lebanon. The standard-company calculations below do not extend a special holding or offshore regime to an ordinary trading business. Income Tax Law arts. 3 and 6 tax Lebanese profits for the preceding income period; art. 14 addresses approved non-calendar accounting periods.

## Rates, bands and thresholds

| Item and conditions | Amount | Official source |
|---|---|---|
| Ordinary capital-company profit, SAL/SARL | 17% | [Income Tax Law art. 32 as replaced by Budget 324/2024 art. 46, pp. 45-46](https://finance.gov.lb/en-us/Finance/BI/ABDP/Documents/Budget%202024.pdf); [MoF notice 4859](https://www.finance.gov.lb/en-us/Taxation/LRT/TP/Documents/4859.pdf) |
| Ordinary company distribution, subject to character and exemption checks | 10% | [MoF notice 4676, Income Tax Law art. 72 bis](https://www.finance.gov.lb/en-us/Taxation/LRT/TP/Documents/4676.pdf) |
| Fixed-asset disposal profit, SAL/SARL; classification required | 15% | [IDAL SAL/SARL tax sections](https://www.investinlebanon.gov.lb/en/doing_business/tax_system) |
| Import advance: failure to file business-results or VAT declarations in any period of the preceding three years | 1.5% of the customs-defined import value, credited to annual tax; penalties remain | [Budget 40/2026 art. 27, p. 38](https://www.finance.gov.lb/en-us/Finance/BI/ABDP/Annual%20Budget%20Documents%20and%20Process/Budget%20Law%202026%20Approved%20by%20Parliament.pdf) |
| New industrial enterprise asset condition under Income Tax Law art. 5 bis II(c) | Minimum LBP 23 billion; not a ceiling or a complete exemption test | [Budget 40/2026 art. 28, p. 38](https://www.finance.gov.lb/en-us/Finance/BI/ABDP/Annual%20Budget%20Documents%20and%20Process/Budget%20Law%202026%20Approved%20by%20Parliament.pdf) |

## The base

Start with the relevant profit period, reconcile income and business expenses, and apply tax adjustments (arts. 6-7, 14). Real-profit filing is mandatory for the listed art. 11 classes, including companies and foreign branches. The employee-count limb says more than four permanent employees, not four or more; it has activity-specific scope. Deemed-profit businesses need their applicable official coefficient and computation before tax: hold CIT-H1.

For an art. 27 advance, retain the customs assessment, trace it to the taxpayer account, deduct the accepted advance from annual tax and reconcile the balance. An excess is refundable on request if no other taxes are owed; art. 27 gives the administration thirty days from request, then Treasury-bond-rate interest for delay. Do not promise an amount before the tax account is reconciled. Do not advise filing immediately before import as a guaranteed way to remove this advance: the test concerns failures in the preceding periods.

## Deadlines and filing

Income Tax Law art. 13 supplies the ordinary return framework, but old calendar dates are not a complete 2026 filing instruction. Current annual forms, portal boxes, payment references, extensions and Law 46/2026 suspension effects are hold CIT-H2. IDAL describes Ministry E-services registration, documentary review and emailed E-pin; it identifies holding returns as a manual exception. Obtain the current account-specific route before submission.

## Penalties and interest

Budget 2026 arts. 16-17 raise specified fixed/minimum Tax Procedures Law penalties for 2026 business years. Match the breached article and entity class; the original generic art. 18 wording is withdrawn because art. 18 concerns beneficial ownership. Current ordinary penalties and any temporary settlement are hold CIT-H3. The prior assertion that an art. 43 relief window has simply expired is not an instruction to reject relief without checking later suspension/extension law.

## Cross-border points

Hold CIT-H4 covers the old bank-interest rate, non-resident goods/services/royalty withholding, treaties and holding/offshore amounts and exemptions. The official IDAL page and older special-regime PDFs do not establish all current amounts and conditions. Preserve the topics but do not compute them as standard company tax. Sayrafa profits require the actual scope and implementation of Budget 2026 art. 52, including its USD threshold, salary exclusion and retrospective rule; hold CIT-H5. Revaluation windows under arts. 40-42 remain CIT-H6 until commencement and suspension effects are established.

## Two worked examples that recompute

An ordinary SAL has reconciled taxable profit LBP 1 billion and no reliefs, credits or special regime. Tax is LBP 170 million. If the entire LBP 830 million balance is an ordinary taxable distribution, withholding is LBP 83 million and shareholders receive LBP 747 million.

```oa-check
name: Ordinary SAL and full dividend
inputs:
  profit: 1000000000
steps:
  - cit: profit * 0.17
  - balance: profit - cit
  - wht: balance * 0.10
  - cash: balance - wht
expected:
  cit: 170000000
  wht: 83000000
  cash: 747000000
```


Distribution decision: retain all LBP 830 million or distribute half now. Half produces LBP 41.5 million withholding and LBP 373.5 million shareholder cash, leaving LBP 415 million retained. This compares cash timing only; it does not establish that retaining an amount avoids a tax or deemed-distribution rule for an unknown entity.

```oa-check
name: Retain versus half distribution
inputs:
  available: 830000000
steps:
  - distribution: available / 2
  - withholding: distribution * 0.10
  - shareholder_cash: distribution - withholding
  - retained: available - distribution
expected:
  withholding: 41500000
  shareholder_cash: 373500000
  retained: 415000000
```


## Ask the client first

- What is the registered legal form, permitted activity and profit period?
- Is this ordinary trading, a holding/offshore company or a deemed-profit activity?
- What expenses, distributions and fixed-asset disposals occurred?
- What payments go abroad, and to whom?
- Which prior declarations and customs advances appear on the tax account?
- Are there Sayrafa gains, revaluations or pending penalties?

## Sources

| Source and read scope | URL | Read on |
|---|---|---|
| Income Tax Law 144/1959, arts. 3, 6-7, 11-15; clauses and neighbours read, older consolidation | https://www.finance.gov.lb/en-us/Taxation/LRT/Documents/%D9%82%D8%A7%D9%86%D9%88%D9%86%20%D8%B6%D8%B1%D9%8A%D8%A8%D8%A9%20%D8%A7%D9%84%D8%AF%D8%AE%D9%84.pdf | 2026-11-01 |
| MoF notice 4859, 14 November 2017, whole page; CIT commencement | https://www.finance.gov.lb/en-us/Taxation/LRT/TP/Documents/4859.pdf | 2026-11-01 |
| MoF notice 4676, 7 November 2017, whole page; distribution rate | https://www.finance.gov.lb/en-us/Taxation/LRT/TP/Documents/4676.pdf | 2026-11-01 |
| Budget 324/2024 art. 46, pp. 45-46; 17% company rate read in image | https://finance.gov.lb/en-us/Finance/BI/ABDP/Documents/Budget%202024.pdf | 2026-11-01 |
| Budget 40/2026 arts. 16-18, 27-29, 40-43, 52, 57; clauses and neighbours, not annexes | https://www.finance.gov.lb/en-us/Finance/BI/ABDP/Annual%20Budget%20Documents%20and%20Process/Budget%20Law%202026%20Approved%20by%20Parliament.pdf | 2026-11-01 |
| IDAL Tax System, SAL/SARL, holding/offshore and online declaration sections; undated page read; special-regime amounts not accepted as current | https://www.investinlebanon.gov.lb/en/doing_business/tax_system | 2026-11-01 |

Not yet confirmed: CIT-H1: all deemed-profit coefficients and special base computations. CIT-H2: current filing/payment forms, boxes, dates, extensions and legal suspension. CIT-H3: exact applicable ordinary penalties and settlement availability. CIT-H4: bank-interest, non-resident and treaty withholding; holding/offshore current fixed/graduated taxes, exemptions and payroll carve-outs. CIT-H5: operative Sayrafa computation and implementation. CIT-H6: revaluation and exceptional windows after publication and later legislation. No held rule is a filing input; original values are preserved in the ledger, not current rates.

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
