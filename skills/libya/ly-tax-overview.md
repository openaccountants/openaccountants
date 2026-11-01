---
name: ly-tax-overview
description: >
  Route ordinary Libyan tax questions across individual income, companies, payroll, transaction duties, connected dealings and cross-border income. Corrects the older employment-only and broad non-taxability claims, identifies the actual statutory source set and exposes the work still needed before the country pack is complete. It distinguishes the source text actually read from unresolved later amendments, records the inputs that change the result, and supplies two recomputing working papers. Use it when researching Libyan tax in 2026, preparing an adviser brief, checking an earlier answer, or identifying which return and supporting records are needed. It is a partial research reference, subject to the currentness limits in the body, and it does not represent a local accountant's sign-off or a tested electronic submission.
jurisdiction: LY
category: international
tax_year: 2026
tax_year_notes: "2026 research edition; domestic amendment chain not closed"
tier: 2
last_updated: 2026-11-01
version: 1.0
review_status: pending_review
trust_label: Built by Michael Cutajar and the OpenAccountants team
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Libya Tax Overview and Research Routing v1.0

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

**2026 research edition, incomplete currentness check.** The domestic rules below are transcribed from the Tax Authority's official 2016 compilation. Its live legislation catalogue and history still identify Income Tax Law 7/2010 and Regulation 592/2010. That establishes the source text, not a complete amendment chain through 2026. Use the calculations as statutory research working papers; obtain the applicable later instruments and current filing instructions before acting. This pack remains partial and has no accountant attestation.

## Who this applies to

Readers identifying which Libyan tax job applies before computing a liability. This overview is a router; the specialist Guides own the rates and computations. Libya's Tax Authority administers the income tax described in Law 7/2010. The live website states that it is under the Ministry of Finance. Amounts in the domestic laws and working papers are in Libyan dinars (LYD).

The pack covers ordinary individuals, businesses and employers to the extent of the read sources. It does not certify complete 2026 law. Every applicable domain remains partial; neither an AI review nor mechanical validation is accountant attestation.

## Rates, bands and thresholds

| Question | Where the operative figures live | Primary source basis | Official URL |
|---|---|---|---|
| Employment, trade, crafts, professional or deposit income | ly-income-tax | Law 7/2010 arts. 34-62 | https://tax.gov.ly/assets/m2016.pdf |
| Company/foreign-branch net profits | ly-corporate-income-tax | Law 7/2010 arts. 63-71 | https://tax.gov.ly/assets/m2016.pdf |
| Employer withholding and contribution allocation | ly-payroll-social | Reg. 592/2010 arts. 52-55; social allocation instruments | https://tax.gov.ly/assets/m2016.pdf |
| VAT status and transaction stamps | ly-vat-gst; VAT absence is unverified | Stamp Law 12/2004 and Law 8/2010 amendment | https://tax.gov.ly/assets/m2016.pdf |
| Connected dealings and UK treaty adjustments | ly-transfer-pricing | UK-Libya treaty arts. 8, 10, 12-13 | https://assets.publishing.service.gov.uk/media/5a819e9ded915d74e33ff2ef/uk-libya-dtc_-_in_force.pdf |
| Non-residents, source, residence and treaty relief | ly-cross-border-tax | Law 7/2010 arts. 1, 33, 55, 63, 84; particular treaty | https://tax.gov.ly/assets/m2016.pdf |
| LLC/JSC and tax onboarding | ly-company-formation | Commercial Activity Law 23/2010; Reg. 592 art. 2 | https://ssf.gov.ly/wp-content/uploads/2012/09/%D9%82%D8%A7%D9%86%D9%88%D9%86-%D8%B1%D9%82%D9%85-23-%D9%84%D9%84%D8%B9%D8%A7%D9%85-2010-%D8%A8%D8%B4%D8%A3%D9%86-%D8%A7%D9%84%D9%86%D8%B4%D8%A7%D8%B7-%D8%A7%D9%84%D8%AA%D8%AC%D8%A7%D8%B1%D9%8A.pdf |

## The base

Classify the taxpayer and income before choosing a rate. Law 7/2010 art. 35 has several individual categories; the old assertion that personal income tax covers employment only is not the statute. The individual exemptions, business costs, losses and employment deductions belong in the individual Guide. Companies and broadly defined foreign branches have their own chapter and cannot simply inherit every natural-person exemption.

Keep six working-paper totals separate: taxable income, income tax, employee contributions, employer contributions, solidarity contribution and transaction stamps. A bank receipt, contract certificate or payroll deduction does not prove another liability is discharged. Contract-payment tax clearance is not evidence of a general percentage withholding tax.

The original company-law capital figures and current operative minimums also differ in evidential status. Use the formation Guide's exact source-text conditions and unresolved later-decision list. The old Jihad-tax abolition, no-VAT, general withholding-zero and universal import-fee claims have not been established from the read primary sources; they are not headline conclusions in this rewrite.

## Deadlines and filing

Route to the category's verified statutory form and deadline: Forms 4/5 for individual business/professional declarations; Form 7 for employment statements; Form 8 for banks' deposit-interest withholding; Form 9 for company returns; Form 1 for activity notification; Forms 16/17 for tax-clearance request/issue. These forms and deadlines are explained with their conditions in the responsible Guide, from Reg. 592/2010.

Start at the responsible Tax Authority office and the public site https://tax.gov.ly/ . The public electronic portal https://services.tax.gov.ly/ redirects to a login page. No private taxpayer data was accessed, and no claim is made about current online fields or a successful electronic filing. Keep submission and payment receipts separately.

The tax-year rule is category-specific: Law art. 22 gives the general calendar-year rule and conditional alternative accounting year; art. 71 expressly uses the company's financial year. Do not require every company to seek approval for its ordinary financial year merely because the general rule exists.

## Penalties and interest

There is no single Libyan tax penalty applying to every job. Income-tax and stamp-law charges differ; social-security law has its own recovery system and later repeal history. Route to the relevant Guide's penalty section, preserve notice dates and distinguish tax, late charge, filing penalty and deliberate-evasion penalty. Do not total unlike liabilities without checking their legal conditions.

## Cross-border points

Establish source, taxpayer type and treaty residence separately. The treaty index is a finding aid; the UK convention provides one read corridor with employment, business and investment-income conditions. Social-security agreements are separate. A foreign passport, a short stay or an offshore invoice does not alone settle the answer.

## Two worked examples that recompute

**Keep company and employee liabilities separate.** Assume the specialist computations have independently produced LYD 26,000 company income tax, LYD 2,220 employee income tax and LYD 200 confirmed total social-security contribution. A control sheet reconciles LYD 28,420 across the three items, while preserving their owners and payment routes. None is treated as a credit for another.

```oa-check
name: Reconcile independently established separate liabilities
inputs:
  company_income_tax: 26000
  employee_income_tax: 2220
  confirmed_social_contribution: 200
steps:
  - income_tax_total: company_income_tax + employee_income_tax
  - all_control_total: income_tax_total + confirmed_social_contribution
expected:
  income_tax_total: 28220
  all_control_total: 28420
```

**Capital or operating cost decision.** An incorporation funding package contains LYD 4,000 subscribed capital and LYD 1,000 third-party service costs. Cash required is LYD 5,000. Treating the whole funding package as an operating expense would misclassify LYD 4,000. Whether the service cost is deductible immediately or over time is determined in the corporate Guide, not by the bank-payment total.

```oa-check
name: Funding versus expense classification control
inputs:
  capital: 4000
  service_costs: 1000
steps:
  - cash_required: capital + service_costs
  - non_expense_capital: cash_required - service_costs
expected:
  cash_required: 5000
  non_expense_capital: 4000
```

## Ask the client first

- Is the taxpayer an individual, partnership, company, branch or employer?
- What income, transaction, period, location and currency are involved?
- What family, residence, public-budget or investment status changes the category?
- Which existing return, assessment, certificate and receipts are available?
- Which later instruments and current procedures have already been confirmed for this case?

## Sources

| Source and actual read scope | URL | Read on |
|---|---|---|
| Tax Authority, 2016 tax legislation compilation: Income Tax Law and regulation routing provisions, stamp-law structure, social allocation and solidarity texts; read sections listed in each specialist Guide; original Arabic, local OCR checked against selected page images | https://tax.gov.ly/assets/m2016.pdf | 2026-11-01 |
| Tax Authority live law and regulation catalogues; law titles and the income-law history paragraph, not a consolidated 2026 certificate | https://tax.gov.ly/Law1.aspx ; https://tax.gov.ly/Law2.aspx ; https://tax.gov.ly/TaxHistory.aspx | 2026-11-01 |
| Tax Authority home page: Ministry of Finance affiliation and published role; unrelated external links are not evidence | https://tax.gov.ly/ | 2026-11-01 |
| Commercial Activity Law arts. 101 and 271-290, and UK convention routing articles; actual read scope is in the specialist Guides | https://ssf.gov.ly/wp-content/uploads/2012/09/%D9%82%D8%A7%D9%86%D9%88%D9%86-%D8%B1%D9%82%D9%85-23-%D9%84%D9%84%D8%B9%D8%A7%D9%85-2010-%D8%A8%D8%B4%D8%A3%D9%86-%D8%A7%D9%84%D9%86%D8%B4%D8%A7%D8%B7-%D8%A7%D9%84%D8%AA%D8%AC%D8%A7%D8%B1%D9%8A.pdf ; https://assets.publishing.service.gov.uk/media/5a819e9ded915d74e33ff2ef/uk-libya-dtc_-_in_force.pdf | 2026-11-01 |
Not yet confirmed: complete domestic amendment chain and administrative practice through 2026; the full 2026 amendment chain and each domain gap listed in README; the old Jihad-tax abolition, no-VAT/no-sales-tax, universal import-service fee, blanket withholding-zero, all-foreigner social coverage and net-salary-stamp claims. No primary-law absence conclusion is inferred from an incomplete catalogue.

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
