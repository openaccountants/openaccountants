---
name: iq-corporate-income-tax
version: 0.3
description: "Company income tax source extracts for federal Iraq, including loss timing and outward-payment conditions, with current filing and oil rules held. Use this Guide when a question mentions federal Iraq, the General Commission for Taxes, GCT Baghdad, or Iraqi dinar tax. It identifies the source version, the evidence actually read, the conditions attached to its extracts, the facts needed from the taxpayer, and the unresolved matters that stop a current filing calculation. It does not cover the Kurdistan Region. Follow the linked country Guides for the underlying job and keep every stated hold attached to any answer."
jurisdiction: IQ
tax_year: 2026
last_updated: 2026-11-01
review_status: pending_review
trust_label: Built by Michael Cutajar and the OpenAccountants team
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Iraq Corporate Income Tax 0.3

> **General reference.** Source extracts and research holds only. This Guide does not establish the law currently in force for a filing.

Tax year: 2026 is the question-routing year, not a certification that these older instruments remain unchanged. **IQ-CURRENT hold:** the complete later-amendment and commencement chain through 2026 has not been established. The extracts below describe only the named source version. Do not use their figures for a current liability until that hold is closed.

## Who this applies to

Historical company-rate source only. Law 113 art. 13(1)(c)–(e), GCT 2004 consolidation, lists limited liability companies, private joint stock companies and mixed joint stock companies. Entity classification, Iraqi-source income and any permanent establishment must be established before choosing a rate. Foreign registration, office, branch, factory, construction site, mine and oil activity are questions to investigate, not automatic liability conclusions here.

## Rates, bands and thresholds

**IQ-CURRENT applies to every source extract.**

| Source version and condition | Amount | Official URL |
|---|---|---|
| Law 113 art. 13(1)(c)–(e), 2004 consolidation, listed company types | 15% flat | https://tax.mof.gov.iq/uploads/Najwan/law/Income-Tax-Law-No.-113-of-1982-Ar.pdf |
| unverified: current oil contractor and licensing-round remuneration treatment | Held | unverified |
| Law 113 art. 19(1), 2004 consolidation, specified interest/annuities/other annual payments due abroad by an Iraqi resident, cash or account credit; statutory bank exemption applies | 15% for non-banks | https://tax.mof.gov.iq/uploads/Najwan/law/Income-Tax-Law-No.-113-of-1982-Ar.pdf |

Article 19 does not make every foreign invoice an interest payment. Contract retention, dividends and treaty reductions are held below.

## The base

Historical art. 11 permits supported losses arising in Iraq to offset other taxable-source profits in the same assessment year. Unrelieved losses carry forward for five consecutive years, limited to half the taxable income of each year and only against the originating source. Do not apply the same-source restriction to the same-year offset. The consolidation also has transitional exclusions for 2003 and the first three months of 2004; this is not a full loss-vintage opinion. IQ-CURRENT applies.

## Deadlines and filing

The historical income-report timing and notice sequence are in [individual income tax](iq-income-tax.md#deadlines-and-filing); do not infer that this completes the company-return process. Held: current company return, forms, line numbers, adjustments, accounts language, department, submission, confirmation, payment reference and record-retention period. Gather the actual form and notice before preparing a filing.

## Penalties and interest

No current penalty calculation is cleared. The income-tax procedure hold covers late reporting, payment additions, interest and bookkeeping sanctions. Read the actual assessment and the applicable version before computation.

## Cross-border points

Historical art. 5(4) limits foreign-tax credit to Iraqi tax on that foreign income; excess foreign tax can be carried for five successive years, oldest carry first. The limit is applied separately for each foreign country. Proof is a payment receipt or confirmation from the foreign tax authority. IQ-CURRENT applies. Treaty-in-force status, permanent establishments and current contract-withholding instructions remain held. See also art. 19 in the rates table.

## Two worked examples that recompute

Historical illustrations only, with the company rate and loss entitlement explicitly assumed. No oil or treaty conclusion is made.

Same-source, unexpired carried loss IQD 80m against IQD 100m income: use IQD 50m and historical tax is IQD 7.5m.

```oa-check
name: Historical carried loss cap
inputs:
  income: 100000000
  loss: 80000000
steps:
  - used: min(loss, income * 0.5)
  - tax: (income - used) * 0.15
expected:
  used: 50000000
  tax: 7500000
```

Decision: do not apply that carried-loss ceiling to a qualifying same-year loss from another taxable Iraqi source. For IQD 100m profit and IQD 80m supported same-year loss, the historical residual is IQD 20m and tax IQD 3m, IQD 4.5m below the carried-loss case.

```oa-check
name: Historical current against carried loss
inputs:
  profit: 100000000
  current_loss: 80000000
steps:
  - same_year_tax: (profit - current_loss) * 0.15
  - carried_tax: (profit - min(current_loss, profit * 0.5)) * 0.15
  - difference: carried_tax - same_year_tax
expected:
  same_year_tax: 3000000
  difference: 4500000
```

## Ask the client first

- Entity type, registration, residence and operating locations?
- Federal Iraq or Kurdistan Region, and year end?
- Oil licence or government contract, and payment classification?
- Loss year, source, support and prior utilisation?
- Foreign country, income, tax paid, evidence and treaty claimed?

## Sources

| Source and actual read scope | URL | Read on |
|---|---|---|
| Law 113: PDF pp. 6 art. 5(4), 13–14 art. 11, 16–17 art. 13 and 20–21 art. 19; cited clauses read with neighbours, decisive pages visually checked | https://tax.mof.gov.iq/uploads/Najwan/law/Income-Tax-Law-No.-113-of-1982-Ar.pdf | 2026-11-01 |

Not yet confirmed: **IQ-CURRENT** later amendments through 2026; **IQ-CORP-OIL** Law 19/2010 scope and later changes, 2018 remuneration-fee base, upstream/non-upstream distinctions; **IQ-CORP-RETURN** complete company workflow and lines 11–33, manager-pay ceiling, depreciation Regulation 9/1994, acceptance/subsequent-audit decision, Arabic accounts, dinar settlement and record retention; **IQ-CORP-XB** PE and source definitions, treaty list/status, dividend relief, resident-interest rates, contract retention ceiling and annual percentages, 2008/2014 instructions, KRI royalties; **IQ-CORP-PROCEDURE** current penalties, payment timing, advance payments, limitation and inspection requirements. The former sole-trader/LLC comparison does not establish an entity-choice recommendation; its allowance and full entity costs were not established.

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
