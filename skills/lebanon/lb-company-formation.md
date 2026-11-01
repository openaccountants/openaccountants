---
name: lb-company-formation
description: "Use this Guide for Lebanon company formation, SAL versus SARL, minimum capital and foreign-company presence questions in 2026. It compares ordinary capital and shareholder baselines on IDAL official guidance, explains why activity matters for holding and offshore companies, and distinguishes branches from representative offices. Two executable cases compare a single founder capital plan and a three-founder SAL plan. It does not promise an incorporation timetable or certify the current Commercial Registry process, fees, company-law amendment chain, audit triggers, permits or special-regime tax treatment. Those issues remain named non-operative holds to resolve before an incorporation application or binding entity recommendation."
version: 1.2
jurisdiction: LB
tax_year: 2026
last_updated: 2026-11-01
review_status: pending_review
trust_label: Built by Michael Cutajar and the OpenAccountants team
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
category: formation
---

# Lebanon Company Formation and Entity Choice

> **General reference only.** This Guide is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in Lebanon.

## Who this applies to

Founders comparing a Lebanese SARL, SAL, holding/offshore vehicle, sole trader, partnership or foreign-company presence. This is an entity-choice and capital-planning reference, not completed incorporation instructions. IDAL is the official investment authority; its undated page is a baseline, and current registry procedures and statutory amendments remain formation holds.

## Rates, bands and thresholds

| Entity-choice parameter | Amount/condition in official guidance | Official source |
|---|---|---|
| SARL minimum capital | LBP 5,000,000 | [IDAL, SARL section](https://www.investinlebanon.gov.lb/en/doing_business/starting_a_business/choose_a_business_structure) |
| SARL participants | One to twenty, with limited liability by contribution; the single-partner restriction requires checking | same |
| SAL minimum capital | LBP 30,000,000 | [IDAL, SAL section](https://www.investinlebanon.gov.lb/en/doing_business/starting_a_business/choose_a_business_structure) |
| SAL shareholders | At least three | same |
| SAL/SARL lawyer | Annual retainer required in IDAL guidance | same |
| SAL auditor | Principal auditor appointed by shareholders | same |
| SARL auditor | IDAL lists partner-count, capital and one-fifth partner-request triggers; current statutory trigger interpretation held under FORM-H2 | same |

## The base

Compare actual activity, owners, liability, governance, capital funding and recurring obligations. SARL limited liability is not a substitute for checking excluded activities. A holding is a special SAL with a limited object, not an ordinary trading company that elects lower tax. Offshore objects and ownership differ; IDAL expressly allows a single shareholder for an offshore vehicle. Do not transfer the ordinary SAL minimum-shareholder rule to it. Current special-regime tax and exemption computation is held in [Corporate income tax](lb-corporate-income-tax.md).

IDAL also distinguishes a foreign branch, which can trade within its parent's object, from a representative office restricted to promotion/marketing. Sole proprietorship and partnership options remain in scope for comparison, but their registration, liability and current procedures remain FORM-H1. Compare personal business tax through [Personal income tax](lb-income-tax.md), not a copied rate range.

## Deadlines and filing

The old Commercial Registry court, lawyer, capital deposit, audit and annual-compliance topics are preserved in FORM-H1/H2. Obtain the current registry application, documents, fees, beneficial-owner filing, tax registration, NSSF obligations and confirmations before a submission. The former two-to-four-week estimate has no fetched official basis and is not promised. Formation does not itself complete the tax, payroll or VAT registrations. Current deadlines and electronic/manual return routes are owned by the relevant tax Guide and remain subject to its holds.

## Penalties and interest

Registration, beneficial-owner and annual-compliance penalties are FORM-H3. No fixed penalty or incorporation fee is supplied as operative. Obtain the current legal provision and applicable filing date before advising a remedy.

## Cross-border points

Check the actual activity and sector before making a foreign-ownership statement. Branch/representative-office scope is described by IDAL, but work permits, sector licences, nationality requirements and overseas tax exposure need their own legal analysis under FORM-H4. A registered special vehicle does not prove that a particular transaction qualifies for relief.

## Two worked examples that recompute

A founder has LBP 8 million available for minimum stated capital and one owner. IDAL's SARL baseline leaves LBP 3 million above minimum; SAL leaves a LBP 22 million capital shortfall and also fails the shareholder minimum. The capital test supports considering SARL, subject to activity and registry checks; it is not a total incorporation budget.

```oa-check
name: Single founder capital comparison
inputs:
  capital_available: 8000000
  sarl_minimum: 5000000
  sal_minimum: 30000000
steps:
  - sarl_surplus: capital_available - sarl_minimum
  - sal_shortfall: max(sal_minimum - capital_available, 0)
expected:
  sarl_surplus: 3000000
  sal_shortfall: 22000000
```


Three founders plan an ordinary SAL and subscribe LBP 12 million each. Total LBP 36 million exceeds the IDAL minimum by LBP 6 million. The headcount and capital baselines are met; legal documents, auditor, lawyer and registry evidence still gate incorporation.

```oa-check
name: Three founders SAL capital plan
inputs:
  founders: 3
  subscription_each: 12000000
  sal_minimum: 30000000
steps:
  - capital: founders * subscription_each
  - excess: capital - sal_minimum
expected:
  capital: 36000000
  excess: 6000000
```


## Ask the client first

- What activity, regulated sector and customer locations are planned?
- How many owners, their residence and ownership rights?
- What capital and documented funding are available?
- Is this local trading, holding activity, offshore activity or a foreign-company presence?
- Are employees, VAT supplies or annual audited accounts expected?

## Sources

| Source and read scope | URL | Read on |
|---|---|---|
| IDAL Choose a Business Structure, SAL/SARL, holding/offshore, branch and representative-office sections read; undated official guidance, not a consolidated statute | https://www.investinlebanon.gov.lb/en/doing_business/starting_a_business/choose_a_business_structure | 2026-11-01 |
| IDAL Tax System, SAL/SARL and online-declaration sections read; special-regime amounts held | https://www.investinlebanon.gov.lb/en/doing_business/tax_system | 2026-11-01 |

Not yet confirmed: FORM-H1: current Commercial Registry authority, applications, documents, fees, capital-payment procedure, timetable and sole-trader/partnership rules. FORM-H2: current company-law amendment chain, SARL auditor trigger, lawyer and annual-compliance conditions. FORM-H3: registration/beneficial-owner/annual penalties. FORM-H4: restricted-sector ownership, permits, nationality and special-vehicle eligibility. The published capital figures are the official IDAL baseline, not certified all-in incorporation costs or proof that the complete 2026 statutory chain has been checked.

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
