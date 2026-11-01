---
name: mg-payroll-social
description: "Madagascar 2026 employer IRSA withholding and remittance workflow, permitted frequency exceptions and social-contribution verification controls; contribution rates remain partial."
jurisdiction: MG
tax_year: 2026
last_updated: 2026-11-01
version: 1.0
review_status: pending_review
trust_label: Built by Michael Cutajar and the OpenAccountants team
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
category: payroll
---

# Madagascar employer payroll: IRSA remittance and social-control checklist

> **General reference only.** This Guide is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person’s facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in Madagascar.

## Who this applies to

Use for an employer or paying body with taxable employees. The employee computation belongs to [ordinary salary IRSA](mg-income-tax.md). This Guide aggregates approved employee computations, checks remittance timing and reconciles the payroll ledger. Social-contribution calculation remains outside the verified scope. CPF I-20 requires withholding at each payment and I-23 requires a nominative statement regardless of each employee’s salary amount. [CPF](https://www.impots.mg/explorer?path=/legislation/Codes%20et%20Manuels/CPF-LFI%202026.pdf).

## Rates, bands and thresholds

| Remittance rule / condition | Period or limit | Official source |
|---|---|---|
| Ordinary IRSA withholding | First 15 days of following month | [CPF I-21](https://www.impots.mg/explorer?path=/legislation/Codes%20et%20Manuels/CPF-LFI%202026.pdf) |
| Paying body under impôt synthétique | Can cumulate by two-month period | same |
| NGOs, associations, projects, public bodies and other entities paying salary but subject to neither IR nor IS | Monthly; semester aggregation allowed only when total withholding does not exceed MGA 50,000 per month | same |
| Semester aggregation above | First 15 days following semester end | same |
| Change of remittance frequency | Taxpayer authorization request and administration decision | same |

Salary rates and dependant reductions have one home in [IRSA](mg-income-tax.md). Do not infer the social-security wage base from the income-tax base or reuse an old minimum wage.

## The base

Reconcile gross cash, benefits, deductions and employee tax computations using [IRSA](mg-income-tax.md). Sum employee withholding by actual payment month and paying location. Net wages equal gross cash less employee deductions and withholding; employer contributions belong in employer expense/payables, not an extra deduction from net pay. [CPF I-20–23](https://www.impots.mg/explorer?path=/legislation/Codes%20et%20Manuels/CPF-LFI%202026.pdf) governs withholding and the employee statement. CNaPS states that the employer registers and declares employees through [E-CNaPS](https://espace.cnaps.mg), and its current employer-registration FAQ describes monthly contribution settlement. That conflicts with the old Guide’s blanket quarterly claim. Do not calculate CNaPS, health or training contributions until the current applicable schedule, effective period and payer classification are established. [CNaPS FAQ](https://www.cnaps.mg/).

## Deadlines and filing

At payment, retain the calculated IRSA. Prepare the prescribed employer declaration and nominative employee statement, reconcile it to payslips and the payroll control account, and declare/pay at the competent fiscal centre within the applicable period. Where payments originate in multiple places, CPF I-21 points to the office for each beneficiary’s workplace. Keep the submission acknowledgement and remittance evidence; reconcile the tax payable account to zero only after payment. Obtain the current official form and actual portal workflow before submission. A foreign-employer employee self-payment has a separate process under I-22 and I-25. [CPF I-20–25](https://www.impots.mg/explorer?path=/legislation/Codes%20et%20Manuels/CPF-LFI%202026.pdf).

## Penalties and interest

CDI 20.01.54.1 distinguishes failure to withhold (40% of omitted withholding) from withholding collected but not paid over (80% of those sums), each in addition to the unpaid principal. The late-payment scale is separate; follow the applicable payer band in [business tax](mg-corporate-income-tax.md). These are tax penalties, not CNaPS penalties. [CDI](https://www.impots.mg/explorer?path=/legislation/Codes%20et%20Manuels/CDI-LFI%202026.pdf).

## Cross-border points

Identify who pays, where the employee works and resides, whether a treaty applies, and whether foreign-employer self-payment is required. Do not assume an overseas payroll removes local IRSA or social-insurance obligations. International social-security arrangements and posted-worker certificates require their own verification.

## Two worked examples that recompute

The following hypothetical employee tax amounts are inputs already computed under the IRSA Guide; these cases test payroll aggregation and remittance only.

```oa-check
name: Payroll cash and tax payable reconcile
inputs:
  gross_cash: 3000000
  employee_contributions: 60000
  employee_a_irsa: 50000
  employee_b_irsa: 70000
steps:
  - withholding: employee_a_irsa + employee_b_irsa
  - net_cash: gross_cash - employee_contributions - withholding
  - reconciled: net_cash + employee_contributions + withholding
expected:
  withholding: 120000
  net_cash: 2820000
  reconciled: 3000000
```

A qualifying non-IR/non-IS association has MGA 40,000 total withholding each month and an authorized semester frequency. Every month satisfies the statutory cap; the semester amount does not itself determine eligibility.

```oa-check
name: Authorized semester remittance
inputs:
  monthly_withholding: 40000
  months: 6
steps:
  - semester_payable: monthly_withholding * months
expected:
  semester_payable: 240000
```

## Ask the client first

Get entity tax regime and any frequency authorization, pay dates and workplaces, employees and approved tax computations, salary ledger, social registration/classification, current contribution notices and health-provider contract, training contribution assessment, expatriates/secondments, previous declarations and outstanding payables.

## Sources

| Source and provisions actually read | Read on |
|---|---|
| [DGI 2026 CPF](https://www.impots.mg/explorer?path=/legislation/Codes%20et%20Manuels/CPF-LFI%202026.pdf), I-20–25 | 2026-11-01 |
| [DGI 2026 CDI](https://www.impots.mg/explorer?path=/legislation/Codes%20et%20Manuels/CDI-LFI%202026.pdf), 01.03.11–19; 20.01.54.1 | 2026-11-01 |
| [CNaPS official site](https://www.cnaps.mg/), FAQ on affiliation, employer registration and online declaration | 2026-11-01 |
| [Signed Loi 2026-004, LFR 2026](https://www.mef.gov.mg/assets/vendor/ckeditor/plugins/kcfinder/upload/files/2026/lfr/LFR2026%20Ampliation%20SIGNEE%20DATEE.pdf), tax amendments and article 22 entry provision read | 2026-11-01 |

**Not yet confirmed:** Exact radio/posted publication date activating the July LFR under article 22; do not resolve a transaction at that transition without the publication evidence. current CNaPS employer/employee rates, category-specific caps and effective dates through all of 2026, binding monthly/quarterly contribution calendar (current FAQ and old Guide disagree), health-provider rates/base, training contribution, social penalties, treaty certificates and live tax portal fields. Old 13%/1%, 5%/1%, eight-SME and training-equals-CNaPS statements remain unverified and must not be used to calculate net pay.

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
