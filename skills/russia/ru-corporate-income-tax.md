---
name: ru-corporate-income-tax
description: >
  Russian corporate profit tax (налог на прибыль организаций) under Tax Code chapter 25 for tax year 2026.
  Covers Russian companies and foreign companies with a permanent establishment or Russian tax residence: the 25%
  general rate and its federal and regional split, dividend rates, loss carry-forward with the 50% limit,
  advance payments, the declaration date of 25 March and the payment date of 28 March. Use for questions such as
  "налог на прибыль 2026", "Russian corporate tax rate", "ООО tax on profit", "loss carry-forward Russia" or
  "advance payments profit tax". Not for sole traders (ru-income-tax), the simplified system (ru-usn), transfer
  pricing (ru-transfer-pricing) or payments to foreign companies (ru-cross-border). Sector, regional and special
  zone reduced rates are named, not computed.
jurisdiction: RU
category: international
tax_year: 2026
tier: 2
last_updated: 2026-10-31
version: 0.1
trust_label: Built by Michael Cutajar and the OpenAccountants team
---

# RU Corporate Income Tax v0.1

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

## Who this applies to

Organisations that pay profit tax under Tax Code chapter 25. Tax residents are Russian organisations, foreign organisations resident under a treaty, and foreign organisations whose place of management is Russia (art. 246.2). Organisations on the simplified system use ru-usn. Foreign organisations with no permanent establishment are in ru-cross-border.

## Rates, bands and thresholds

| Item | Amount | Tax year | Conditions | Official URL |
|---|---|---|---|---|
| General rate | 25% | 2026 | Applies unless art. 284 sets another rate (art. 284(1)) | https://www.consultant.ru/document/cons_doc_LAW_28165/eb9180fc785448d58fe76ef323fb67d1832b9363/ |
| Federal share | 8% | 2025 to 2030 | Part of the 25% (art. 284(1)) | same |
| Regional share | 17% | 2017 to 2030 | Part of the 25%; regional laws can lower it only where art. 284 allows (art. 284(1)) | same |
| Dividends from a 50% subsidiary | 0% | 2026 | Recipient is a Russian organisation holding at least 50% continuously for at least 365 calendar days on the decision date (art. 284(3)(1)); further conditions in the article | same |
| Other dividends received by Russian organisations | 13% | 2026 | Art. 284(3)(2) | same |
| Loss limit | 50% | 1 Jan 2017 to 31 Dec 2030 | Prior losses cannot cut the current base by more than 50% (art. 283(2.1)); reduced-rate bases are excepted | https://www.consultant.ru/document/cons_doc_LAW_28165/f07c38898fd7af4a54b1c6d33e01f23cc2dae757/ |
| Quarterly advances only | RUB 15 million | 2026 | Average sales income per quarter over the previous four quarters does not exceed this (art. 286(3)) | https://www.consultant.ru/document/cons_doc_LAW_28165/a254131f0c25f73b3fe90012f964e0c3dcb39938/ |
| Multinational group members | 15% | 2026 | Art. 284(1.20) applies to group members defined in art. 105.16-1(2); read the conditions in the article | https://www.consultant.ru/document/cons_doc_LAW_28165/eb9180fc785448d58fe76ef323fb67d1832b9363/ |

## The base

Tax is the rate times the base (art. 286(1)). The tax period is the calendar year; reporting periods are the first quarter, half year and nine months, or each cumulative month for payers on actual monthly profit (art. 285). A Russian organisation includes income from sources outside Russia (art. 311(1)). Losses from 2025 onward follow art. 283 as amended by Law 259-FZ; earlier losses follow the earlier wording, as ConsultantPlus notes under the article.

## Deadlines and filing

| Step | Date | Source |
|---|---|---|
| Annual declaration | 25 March of the next year (art. 289(4)) | https://www.consultant.ru/document/cons_doc_LAW_28165/e1a5f8ba9742b3e8b843c3ee97e6f6a5bcdcd066/ |
| Annual tax | 28 March of the next year (art. 287(1)) | https://www.consultant.ru/document/cons_doc_LAW_28165/17f089448303baae2053c544b5f1423572c91bda/ |
| Advance for a reporting period | 28th of the month after the period (art. 287(1)) | same |
| Monthly advance within a period | 28th of each month of that period (art. 287(1)) | same |

The filer computes the base, deducts allowed losses, splits the tax into federal and regional parts, files the declaration with the tax office and pays by the dates above.

## Penalties and interest

Transfer pricing penalties are in ru-transfer-pricing. General late filing, under-payment and interest rules are not stated here; see the "Not yet confirmed:" line.

## Cross-border points

Payments to foreign companies, residence by place of management, CFC rules and thin capitalisation are in ru-cross-border.

## Two worked examples that recompute

**Loss limit.** Base RUB 10,000,000 before losses, losses carried forward RUB 8,000,000. The deduction stops at RUB 5,000,000, so the base is RUB 5,000,000 and tax RUB 1,250,000: federal RUB 400,000, regional RUB 850,000. RUB 3,000,000 of loss stays for later.

```oa-check
name: Loss limit at 50 percent, general rate
inputs:
  base: 10000000
  losses: 8000000
steps:
  - used: min(losses, base * 0.5)
  - taxable: base - used
  - federal: taxable * 0.08
  - regional: taxable * 0.17
  - tax: federal + regional
  - left: losses - used
expected:
  tax: 1250000
  left: 3000000
```

**Decision: hold 50% or 40% before a dividend.** A Russian company receives a RUB 1,000,000 dividend. With 50% held for 365 days and the other art. 284(3)(1) conditions met, tax is nil. With 40%, tax is RUB 130,000. The stake is what decides it.

```oa-check
name: Dividend at 50 percent stake against 40 percent stake
inputs:
  dividend: 1000000
steps:
  - tax_50_stake: dividend * 0
  - tax_40_stake: dividend * 0.13
  - difference: tax_40_stake - tax_50_stake
expected:
  difference: 130000
```

## Ask the client first

- Is the entity on the general system or on УСН?
- Which region, and does a reduced regional rate or a special status apply?
- What are the losses carried forward, and from which years?
- What was average quarterly sales income over the last four quarters?
- For dividends: what stake, held since when?

## Sources

| Source | URL | Read on |
|---|---|---|
| Tax Code arts. 284, 285 | https://www.consultant.ru/document/cons_doc_LAW_28165/eb9180fc785448d58fe76ef323fb67d1832b9363/ ; https://www.consultant.ru/document/cons_doc_LAW_28165/45b71f91f6ca44eb1272308f45bae5877228bc8f/ | 2026-10-31 |
| Tax Code arts. 283, 286 | https://www.consultant.ru/document/cons_doc_LAW_28165/f07c38898fd7af4a54b1c6d33e01f23cc2dae757/ ; https://www.consultant.ru/document/cons_doc_LAW_28165/a254131f0c25f73b3fe90012f964e0c3dcb39938/ | 2026-10-31 |
| Tax Code arts. 287, 289 | https://www.consultant.ru/document/cons_doc_LAW_28165/17f089448303baae2053c544b5f1423572c91bda/ ; https://www.consultant.ru/document/cons_doc_LAW_28165/e1a5f8ba9742b3e8b843c3ee97e6f6a5bcdcd066/ | 2026-10-31 |
| Tax Code arts. 246.2, 311 | https://www.consultant.ru/document/cons_doc_LAW_28165/85972d9f375fa036456e2ddbd59699628125a49d/ ; https://www.consultant.ru/document/cons_doc_LAW_28165/f5b7f1519f350ffa85fa7d86fae6078420d593aa/ | 2026-10-31 |

The consolidated Tax Code was read on the ConsultantPlus free version (edition of 4 Aug 2026), a commercial copy of the law. The official portal pravo.gov.ru did not open from curl or a real browser on 2026-10-31.

Not yet confirmed: declaration form and box numbers, filing portal steps, deductible expense rules (arts. 252 to 272) in computation detail, reduced sector and regional rates, the general penalties in arts. 119 and 122 and late interest in art. 75, and the full conditions of art. 284(1.20). The official text was not opened; all figures need a check against pravo.gov.ru.
