---
name: lb-tax-overview
description: "Use this Guide to route Lebanon tax questions to the correct 2026 domain and reconcile reviewed tax working papers. It identifies the separate business, employment and movable-capital schedules, links the ordinary company, VAT, payroll and formation Guides, and prevents repeating rates across the pack. Its executable cases reconcile accepted corporate credits and compare a proposed distribution with reserved tax payments. It does not establish tax liability from bank movements or supply a general exemption based on territoriality. Current directorate details, complete filing procedures, general penalties, foreign income, treaty relief and transfer pricing remain named non-operative holds or domain-specific gaps."
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

# Lebanon Tax Overview

> **General reference only.** This Guide is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in Lebanon.

## Who this applies to

People routing a Lebanon tax question to the correct domain. Income Tax Law art. 1 separates business profits, employment/pensions and movable capital; do not combine them into one general personal-tax calculation. This overview is a routing and reconciliation reference for 2026. It does not supply a second rates table that can drift from the domain Guides.

## Rates, bands and thresholds

| Question | Operative destination and boundary | Official source |
|---|---|---|
| Individual salary/business tax | [Personal income tax](lb-income-tax.md); bands, business base and explicit salary holds | [Income Tax Law arts. 1-3, 46](https://www.finance.gov.lb/en-us/Taxation/LRT/Documents/%D9%82%D8%A7%D9%86%D9%88%D9%86%20%D8%B6%D8%B1%D9%8A%D8%A8%D8%A9%20%D8%A7%D9%84%D8%AF%D8%AE%D9%84.pdf) |
| SAL/SARL and distributions | [Corporate income tax](lb-corporate-income-tax.md); ordinary rates and special-regime holds | [IDAL SAL/SARL sections](https://www.investinlebanon.gov.lb/en/doing_business/tax_system) |
| VAT and imports | [VAT](lebanon-vat.md); deduction amendments; rate/registration and filing holds | [MoF VAT section](https://www.finance.gov.lb/ar-lb/Taxation/Companies/VAT) |
| Employee contributions and benefits | [Payroll and social contributions](lb-payroll-social.md); ordinary family-branch baseline and contribution holds | [NSSF publications](https://www.cnss.gov.lb/%D8%A7%D9%84%D9%85%D8%B0%D9%83%D8%B1%D8%A7%D8%AA-%D8%A7%D9%84%D8%A5%D8%B9%D9%84%D8%A7%D9%85%D9%8A%D8%A9-2026/) |
| Entity choice | [Company formation](lb-company-formation.md); capital baselines and registry holds | [IDAL business structure](https://www.investinlebanon.gov.lb/en/doing_business/starting_a_business/choose_a_business_structure) |

## The base

First identify taxpayer, legal form, income type, source, period and currency. Keep profit, wages, distributions, VAT and NSSF in separate schedules and reconcile their combined cash effect only afterwards. Territorial profit taxation in art. 3 does not decide every salary, foreign-capital or treaty question. The old blanket territoriality row must not override the relevant income article.

LBP/LL means Lebanese pounds in this pack. Preserve original-currency records and the applicable dated conversion evidence; no fixed exchange rate is supplied. Income Tax Law arts. 13-14 distinguish the calendar-year framework from an approved different accounting period. Do not assume every company has a calendar year end.

## Deadlines and filing

IDAL describes Ministry E-services access after documentary review and an emailed E-pin; it names holding returns as a manual exception. The current operational process belongs to each domain Guide. The legacy overview calendar dates and tax-authority directorate name are OV-H1 pending direct current evidence. A year label is not proof that rates, forms and deadlines have all been confirmed. Check each domain's holds before submission.

## Penalties and interest

Route penalties to the breached law and domain. Do not apply beneficial-owner penalties as ordinary return penalties, or infer social-security settlement terms from a budget summary. OV-H2 covers any general procedural claim not established in the linked Guide.

## Cross-border points

Foreign income, non-residents, treaties, transfer pricing, withholding and special entities need the relevant source and taxpayer facts. This pack has no complete treaty/transfer-pricing computation. OV-H3 retains those open domains; they are not supplied by the word territorial.

## Two worked examples that recompute

A company has a completed and separately reviewed corporate tax working paper showing liability LBP 170 million, accepted credits LBP 30 million and prior payments LBP 100 million. The remaining cash to reserve is LBP 40 million. This reconciliation does not establish an income-tax rate or recognise a credit without evidence.

```oa-check
name: Route then reconcile corporate cash
inputs:
  reviewed_liability: 170000000
  accepted_credit: 30000000
  paid: 100000000
steps:
  - reserve: reviewed_liability - accepted_credit - paid
expected:
  reserve: 40000000
```


Cash-planning decision: separately established and undisputed tax payments total LBP 50 million. The bank balance is LBP 80 million; a proposed LBP 40 million distribution would leave a LBP 10 million shortfall. Reserve the reviewed liabilities before deciding a distribution. This does not net one tax against another or prove that a distribution is lawful.

```oa-check
name: Reserve liabilities before distribution
inputs:
  cash: 80000000
  reviewed_payments: 50000000
  proposed_distribution: 40000000
steps:
  - cash_after_reserve: cash - reviewed_payments
  - shortfall: max(proposed_distribution - cash_after_reserve, 0)
expected:
  cash_after_reserve: 30000000
  shortfall: 10000000
```


## Ask the client first

- What is the taxpayer's legal form, residence and actual activity?
- Which kind of receipt or transaction creates the question?
- Which income period, currency and conversion evidence apply?
- What registrations, returns, accepted credits and payments already exist?
- Is there a foreign party, treaty, special entity or suspended deadline?

## Sources

| Source and read scope | URL | Read on |
|---|---|---|
| Income Tax Law 144/1959 arts. 1-3 and 13-14 read with neighbours; older consolidation | https://www.finance.gov.lb/en-us/Taxation/LRT/Documents/%D9%82%D8%A7%D9%86%D9%88%D9%86%20%D8%B6%D8%B1%D9%8A%D8%A8%D8%A9%20%D8%A7%D9%84%D8%AF%D8%AE%D9%84.pdf | 2026-11-01 |
| IDAL Tax System, all substantive tax and online declaration sections read; undated | https://www.investinlebanon.gov.lb/en/doing_business/tax_system | 2026-11-01 |

Not yet confirmed: OV-H1: exact directorate name, complete current filing calendar and portal/payment instructions. OV-H2: procedural penalty and relief rules beyond confirmed domain scope. OV-H3: treaty and transfer-pricing computations, foreign-capital income and non-resident rules. Every old overview rate/deadline is mapped to its domain or a named non-operative hold in the ledger. Read the README partial entries; 2026 does not mean complete or professionally signed.

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
