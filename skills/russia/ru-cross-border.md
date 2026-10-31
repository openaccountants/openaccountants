---
name: ru-cross-border
description: >
  Russian cross-border corporate tax for tax year 2026 under Tax Code chapters 3.4 and 25. Covers Russian tax
  residence of companies by place of management, permanent establishments, withholding on Russian-source income of
  foreign companies at 25% and 10%, dividends to foreign companies at 15%, the treaty residence and beneficial owner
  conditions, foreign income of Russian companies, CFC control tests and thin capitalisation. Use for "налог у
  источника", "withholding tax Russia", "dividends to non-resident Russia", "постоянное представительство", "КИК",
  "thin cap Russia". Treaty suspension status is not confirmed and must be checked for each payment. Sanctions and
  currency control are out of scope. Individuals are in ru-income-tax and transfer pricing in ru-transfer-pricing.
jurisdiction: RU
category: cross-border
tax_year: 2026
tier: 2
last_updated: 2026-10-31
version: 0.1
trust_label: Built by Michael Cutajar and the OpenAccountants team
---

# RU Cross-Border v0.1

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

## Who this applies to

Russian organisations paying or earning across the border, and foreign organisations with Russian income. Sanctions and currency control are out of scope: refer those out.

## Rates, bands and thresholds

| Item | Amount | Tax year | Conditions | Official URL |
|---|---|---|---|---|
| Foreign company, general source income | 25% | 2026 | No Russian PE; all income except the art. 284(2)(2) to (4), (3), (4), (4.3) items, with art. 310 (art. 284(2)(1)) | https://www.consultant.ru/document/cons_doc_LAW_28165/eb9180fc785448d58fe76ef323fb67d1832b9363/ |
| Transport and container income | 10% | 2026 | Use, upkeep or rent of ships, aircraft, other transport or containers as listed (art. 284(2)(2)) | same |
| Dividends to a foreign company | 15% | 2026 | Unless art. 284(3)(1.3) applies (art. 284(3)(3)) | same |
| Thin capitalisation ratio | 3 to 1 | 2026 | 12.5 to 1 for banks and leasing organisations; controlled debt against equity (art. 269(3)) | https://www.consultant.ru/document/cons_doc_LAW_28165/0cef588141a4939f2d2f5d6c0b2e1335fce57a6f/ |
| CFC controller | over 25%, or over 10% | 2026 | Over 10% applies if all Russian residents together hold over 50%, per art. 25.13(3); read the article | https://www.consultant.ru/document/cons_doc_LAW_19671/49edc7b197ca96975d550301b271b701c8027329/ |
| Withholding payment | 28th of next month | 2026 | Month after payment to the foreign company (art. 287(2)); dividends follow art. 287(4) | https://www.consultant.ru/document/cons_doc_LAW_28165/17f089448303baae2053c544b5f1423572c91bda/ |

## The base

**Residence.** A foreign organisation is resident if managed from Russia: the executive body regularly acts from Russia, or senior officers mainly direct it from Russia (art. 246.2(2)). Shareholder decisions alone do not count (art. 246.2(3)).

**Permanent establishment.** A branch, office or other place through which the foreign organisation regularly does business in Russia, including natural resource use, listed contract work, sales from a warehouse and other work (art. 306(2)).

**Source income.** Art. 309(1) lists it. It includes sales of shares in companies with over 50% of assets in Russian real estate (art. 309(1)(5)).

**Withholding.** The Russian payer withholds at each payment (art. 310(1)). Exceptions include income tied to a notified Russian PE and 0% items (art. 310(2)).

**Treaty relief.** The foreign beneficial owner proves residence to the payer before the payment date (art. 312(1)).

**Foreign income of a Russian company** is in its base (art. 311(1)).

## Deadlines and filing

Withheld tax is paid as in the table. The payer's tax agent reporting uses the profit tax return timetable in ru-corporate-income-tax (art. 289(4)).

## Penalties and interest

Not stated here; see the "Not yet confirmed:" line. CFC notification penalties are RUB 500,000 per CFC for missing details and RUB 50,000 for each foreign organisation in the participation notice, as art. 129.6 sets out.

## Cross-border points

This whole skill. Check every treaty before relying on it.

## Two worked examples that recompute

**Decision: dividends with or without a treaty.** A Russian company pays RUB 2,000,000 to a foreign parent. With no treaty relief, withholding is RUB 300,000. If a treaty is in force and gives 5%, and art. 312 proof arrives before payment, it is RUB 100,000. The 5% is an input to test, not a stated treaty rate.

```oa-check
name: Dividend withholding, domestic rate against tested treaty rate
inputs:
  dividend: 2000000
  treaty_rate: 0.05
steps:
  - domestic: dividend * 0.15
  - treaty: dividend * treaty_rate
  - saved: domestic - treaty
expected:
  domestic: 300000
  saved: 200000
```

**Thin capitalisation.** Controlled debt RUB 90,000,000, equity share RUB 10,000,000, interest RUB 9,000,000. The ratio is 9, divided by 3 gives 3. Deductible interest is RUB 3,000,000.

```oa-check
name: Article 269 interest limit
inputs:
  debt: 90000000
  equity_share: 10000000
  interest: 9000000
steps:
  - coefficient: debt / equity_share / 3
  - allowed: interest / coefficient
expected:
  coefficient: 3
  allowed: 3000000
```

## Ask the client first

- Where is the recipient resident, and is it the beneficial owner?
- What kind of income is it?
- Is there a treaty, and is the article in force for that country today?
- Does the foreign party have a Russian PE or management in Russia?
- For loans: who is the lender, and what are the debt and equity?
- Is any Russian person a controller of a foreign company?

## Sources

| Source | URL | Read on |
|---|---|---|
| Tax Code art. 284 | https://www.consultant.ru/document/cons_doc_LAW_28165/eb9180fc785448d58fe76ef323fb67d1832b9363/ | 2026-10-31 |
| Tax Code arts. 246.2, 306, 309 | https://www.consultant.ru/document/cons_doc_LAW_28165/85972d9f375fa036456e2ddbd59699628125a49d/ ; https://www.consultant.ru/document/cons_doc_LAW_28165/fa62c975ab243732baf9cabdc96e9e9faa89bf1a/ ; https://www.consultant.ru/document/cons_doc_LAW_28165/204a8e47c47f7b4d463234dfe8e37290cc70fd40/ | 2026-10-31 |
| Tax Code arts. 310, 311, 312 | https://www.consultant.ru/document/cons_doc_LAW_28165/360d1a385ceef2ec4f0e304bcef072278fcc5d54/ ; https://www.consultant.ru/document/cons_doc_LAW_28165/f5b7f1519f350ffa85fa7d86fae6078420d593aa/ ; https://www.consultant.ru/document/cons_doc_LAW_28165/3496fa72c66e733e71c48d9faa230ca92582726c/ | 2026-10-31 |
| Tax Code arts. 25.13, 129.6, 269, 287 | https://www.consultant.ru/document/cons_doc_LAW_19671/49edc7b197ca96975d550301b271b701c8027329/ ; https://www.consultant.ru/document/cons_doc_LAW_19671/4d1bf5cd39cb02efda996f77776d629ac2737cd3/ ; https://www.consultant.ru/document/cons_doc_LAW_28165/0cef588141a4939f2d2f5d6c0b2e1335fce57a6f/ ; https://www.consultant.ru/document/cons_doc_LAW_28165/17f089448303baae2053c544b5f1423572c91bda/ | 2026-10-31 |

The consolidated Tax Code was read on the ConsultantPlus free version (edition of 4 Aug 2026), a commercial copy of the law. The official portal pravo.gov.ru did not open from curl or a real browser on 2026-10-31.

Not yet confirmed: the text and country list of any presidential decree suspending treaty articles (could not be opened, so no treaty is treated as in force or suspended here); treaty rates; exit rules for companies; CFC rate and exemptions in detail; general penalties for agents.
