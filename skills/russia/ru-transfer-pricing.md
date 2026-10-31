---
name: ru-transfer-pricing
description: >
  Russian transfer pricing rules under Tax Code section V.1 for tax year 2026. Covers which deals between related
  parties are controlled, the RUB 120 million and RUB 1 billion income limits, the notification due 20 May, when the
  tax office can demand documentation, and the penalties in art. 129.3 and 129.4. For Russian organisations and
  foreign organisations taxed in Russia. Use for "контролируемые сделки", "уведомление о контролируемых сделках",
  "Russia transfer pricing threshold", "related party Russia", "TP notification Russia". Country-by-country and
  global file duties are named, not computed. Corporate tax itself is in ru-corporate-income-tax, and payments
  abroad are in ru-cross-border. Pricing methods are listed with their articles and not worked through in detail.
jurisdiction: RU
category: transfer-pricing
tax_year: 2026
tier: 2
last_updated: 2026-10-31
version: 0.1
trust_label: Built by Michael Cutajar and the OpenAccountants team
---

# RU Transfer Pricing v0.1

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

## Who this applies to

Taxpayers that deal with related parties (art. 105.1). Foreign trade in listed goods and deals with listed low-tax territories can be controlled under art. 105.14(1) as well, even without related status; read the subparagraphs.

## Rates, bands and thresholds

| Item | Amount | Tax year | Conditions | Official URL |
|---|---|---|---|---|
| Limit for art. 105.14(1) deals | over RUB 120 million | 2026 | Income from such deals with one person in the calendar year (art. 105.14(3)) | https://www.consultant.ru/document/cons_doc_LAW_19671/ce0729faafa9043d99ffbae22f7bac69219a2a7d/ |
| Limit for domestic art. 105.14(2) deals | over RUB 1 billion | 2026 | Income from such deals between the parties in the calendar year, and only if a listed condition such as different profit tax rates is met (art. 105.14(2), (3)) | same |
| Notification date | 20 May | 2026 | Next year, electronically (art. 105.16(2)) | https://www.consultant.ru/document/cons_doc_LAW_19671/eb52d9c2b765f5807ea85e9eb813683b10add186/ |
| Earliest documentation demand | 1 June | 2026 | Next year (art. 105.15(3)) | https://www.consultant.ru/document/cons_doc_LAW_19671/c88a6f6ef3f79d84685097e09560a4d5fbacfd59/ |
| Penalty, art. 105.14(1) deals | 100% of unpaid tax, minimum RUB 500,000 | 2026 | Tax on income under art. 105.3(6.1); deals recognised from 1 Jan 2024 (art. 129.3(1)) | https://www.consultant.ru/document/cons_doc_LAW_19671/0dcad7fcba79ce0bdb98d2f907e49de1456a8985/ |
| Penalty, art. 105.14(2) deals | 40% of unpaid tax, minimum RUB 30,000 | 2026 | Art. 129.3(1.2) | same |
| Penalty, no notification | RUB 100,000 | 2026 | Missing notification or false data (art. 129.4) | https://www.consultant.ru/document/cons_doc_LAW_19671/48fec77c044c6c3c4b82042c7d7e7cf5dda4750c/ |

## The base

Income in related-party deals is taxed as if the terms were those of unrelated parties, and the adjustment cannot reduce the tax due (art. 105.3(1)). Methods are in arts. 105.7 to 105.13. Where a price with a non-resident related party differs from market and leads to an adjustment, art. 105.3(6.1) applies further consequences; read it with art. 129.3(1).

## Deadlines and filing

1. List deals with each related party for the calendar year and test art. 105.14.
2. File the notification electronically with the tax office by 20 May of the next year.
3. Hold art. 105.15 documentation ready for a demand from 1 June of the next year.
4. Group members also check country-by-country, global and national file duties in arts. 105.16-1 to 105.16-7.

## Penalties and interest

See the table. Art. 129.3(1.1) carves out deals recognised from 1 Jan 2022 to 31 Dec 2023 from para 1. Group-file penalties are not stated here.

## Cross-border points

Foreign deals usually fall under art. 105.14(1), with the RUB 120 million limit. Interest limits on controlled debt are in art. 269 and ru-cross-border.

## Two worked examples that recompute

**Decision: which limit bites.** A company has RUB 130,000,000 income with a related foreign party and RUB 900,000,000 with a related domestic party on a different rate. The foreign deal passes its RUB 120,000,000 limit by RUB 10,000,000 and needs a notification. The domestic deal is RUB 100,000,000 short of RUB 1,000,000,000 and does not.

```oa-check
name: Limits for foreign and domestic controlled deals
inputs:
  foreign_income: 130000000
  domestic_income: 900000000
steps:
  - foreign_over: foreign_income - 120000000
  - domestic_short: 1000000000 - domestic_income
expected:
  foreign_over: 10000000
  domestic_short: 100000000
```

**Penalty minimums.** Unpaid tax RUB 200,000. On an art. 105.14(1) deal the penalty is RUB 500,000, the minimum. On an art. 105.14(2) deal 40% gives RUB 80,000, above its RUB 30,000 minimum.

```oa-check
name: Article 129.3 penalty by deal type
inputs:
  unpaid: 200000
steps:
  - para_1: max(unpaid, 500000)
  - para_1_2: max(unpaid * 0.4, 30000)
expected:
  para_1: 500000
  para_1_2: 80000
```

## Ask the client first

- Who are the related parties, and on what link (art. 105.1)?
- Where is each party resident?
- What income came from each party in the year?
- Do domestic parties use different rates or a special status?
- Is the company in an international group?

## Sources

| Source | URL | Read on |
|---|---|---|
| Tax Code arts. 105.3, 105.14 | https://www.consultant.ru/document/cons_doc_LAW_19671/5e01f3a0a83a29f1741823fb9304593195004235/ ; https://www.consultant.ru/document/cons_doc_LAW_19671/ce0729faafa9043d99ffbae22f7bac69219a2a7d/ | 2026-10-31 |
| Tax Code arts. 105.15, 105.16 | https://www.consultant.ru/document/cons_doc_LAW_19671/c88a6f6ef3f79d84685097e09560a4d5fbacfd59/ ; https://www.consultant.ru/document/cons_doc_LAW_19671/eb52d9c2b765f5807ea85e9eb813683b10add186/ | 2026-10-31 |
| Tax Code arts. 129.3, 129.4 | https://www.consultant.ru/document/cons_doc_LAW_19671/0dcad7fcba79ce0bdb98d2f907e49de1456a8985/ ; https://www.consultant.ru/document/cons_doc_LAW_19671/48fec77c044c6c3c4b82042c7d7e7cf5dda4750c/ | 2026-10-31 |

The consolidated Tax Code was read on the ConsultantPlus free version (edition of 4 Aug 2026), a commercial copy of the law. The official portal pravo.gov.ru did not open from curl or a real browser on 2026-10-31.

Not yet confirmed: notification form and fields, group-file limits and penalties (arts. 105.16-1 to 105.16-7), advance pricing agreement detail, and how art. 105.3(6.1) computes the deemed income. The official text was not opened; all figures need a check against pravo.gov.ru.
